#!/usr/bin/env python3
"""Optional fail-closed, explicit-file read hook example for Claude Code and Cursor.

This is NOT a general confidentiality boundary or an installed runtime policy.
Only explicitly rooted, non-sensitive regular-file Read and single-file Grep
are permitted. Recursive search, directory listing and all mutations are denied.
Use filesystem sandbox/ACL and provider-side permissions as the real boundary.
"""
import argparse
import json
import sys
from pathlib import Path

READ_ONLY_TOOLS = frozenset({"Read", "Grep"})
SENSITIVE_PARTS = frozenset({
    ".git", ".ssh", ".aws", ".kube", ".npmrc", ".pypirc", ".netrc",
    ".env", ".envrc", "id_rsa", "id_ed25519", "credentials", "secrets",
})
SENSITIVE_SUFFIXES = (".pem", ".key", ".p12", ".pfx")
GLOB_META = frozenset("*?[]{}")


def _safe_root(raw):
    if not isinstance(raw, (str, Path)) or not str(raw).strip():
        return None
    candidate = Path(raw)
    if not candidate.is_absolute():
        return None
    try:
        root = candidate.resolve(strict=True)
    except (OSError, RuntimeError):
        return None
    return root if root.is_dir() else None


def _sensitive_part(part):
    name = part.lower()
    return (
        name in SENSITIVE_PARTS
        or name.startswith(".env.")
        or name.startswith("id_rsa.")
        or name.startswith("id_ed25519.")
        or name.endswith(SENSITIVE_SUFFIXES)
    )


def _allowed_regular_file(raw, root):
    # Unknown path encodings, wildcards and parent traversal are denied.
    if not isinstance(raw, str) or not raw or len(raw) > 4096:
        return False
    if any(char in raw for char in "\x00\r\n\\") or any(char in raw for char in GLOB_META):
        return False
    request = Path(raw)
    if ".." in request.parts or any(_sensitive_part(part) for part in request.parts):
        return False
    candidate = request if request.is_absolute() else root / request
    try:
        lexical = candidate.relative_to(root)
        if not lexical.parts or any(_sensitive_part(part) for part in lexical.parts):
            return False
        segment = root
        for part in lexical.parts:
            segment = segment / part
            if segment.is_symlink():
                return False
        resolved = candidate.resolve(strict=True)
        return resolved.is_relative_to(root) and resolved.is_file()
    except (OSError, ValueError, RuntimeError):
        return False


def decide(record, allowed_root=None):
    """Evaluate only well-understood explicit-file reads; otherwise deny."""
    root = _safe_root(allowed_root)
    if root is None or not isinstance(record, dict):
        return "deny"
    tool = record.get("tool_name")
    if tool not in READ_ONLY_TOOLS:
        return "deny"
    data = record.get("tool_input", {})
    if isinstance(data, str):
        try:
            data = json.loads(data)
        except (ValueError, TypeError):
            return "deny"
    if not isinstance(data, dict):
        return "deny"

    if tool == "Read":
        if set(data) - {"file_path", "offset", "limit"}:
            return "deny"
        for field in ("offset", "limit"):
            if field in data and (
                type(data[field]) is not int or data[field] < (1 if field == "limit" else 0)
            ):
                return "deny"
        return "allow" if _allowed_regular_file(data.get("file_path"), root) else "deny"

    # Grep is allowed against ONE explicit existing regular file only. In particular,
    # 'glob', directory path '.', implicit search root, broad includes and other
    # tool-specific parameters are intentionally denied, not merely name-filtered.
    if set(data) - {"path", "pattern"}:
        return "deny"
    pattern = data.get("pattern")
    if not isinstance(pattern, str) or not pattern or len(pattern) > 4096:
        return "deny"
    return "allow" if _allowed_regular_file(data.get("path"), root) else "deny"


def run(harness, payload, allowed_root=None):
    verdict = decide(payload, allowed_root)
    if harness == "claude":
        if verdict == "allow":
            return 0, "", ""
        return 2, "", "BeginNerd strict-read profile denied the tool or path.\n"
    if harness == "cursor":
        response = {
            "permission": verdict,
            "user_message": "This strict-read profile denied the tool or path." if verdict == "deny" else "",
            "agent_message": "Use an approved explicit-file read, or request a different permission profile." if verdict == "deny" else "",
        }
        return 0, json.dumps(response) + "\n", ""
    raise ValueError("Unsupported harness")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--harness", choices=("claude", "cursor"), required=True)
    parser.add_argument("--root", required=True, help="Absolute approved project directory")
    args = parser.parse_args()
    try:
        payload = json.loads(sys.stdin.read(1024 * 1024))
    except (ValueError, OSError):
        payload = {}
    code, stdout, stderr = run(args.harness, payload, args.root)
    if stdout:
        sys.stdout.write(stdout)
    if stderr:
        sys.stderr.write(stderr)
    return code


if __name__ == "__main__":
    sys.exit(main())
