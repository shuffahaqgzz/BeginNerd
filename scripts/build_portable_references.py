#!/usr/bin/env python3
"""Generate independently installable skill reference snapshots from canonical docs.

No network, no runtime/provider changes. Run --check in CI and --write only when
canonical docs change; generated files MUST NOT be edited by hand.
"""
import argparse
import hashlib
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCES = {
    "docs/governance/AGENT-GOVERNANCE.md": (
        "skills/beginnerd-ask/references/agent-governance.md",
        "skills/beginnerd-setup/references/agent-governance.md",
    ),
    "docs/governance/MEMORY-KNOWLEDGE-CONTRACT.md": (
        "skills/beginnerd-ask/references/memory-knowledge-contract.md",
        "skills/beginnerd-setup/references/memory-knowledge-contract.md",
    ),
    "docs/workflows/WORKFLOW-REGISTRY.md": (
        "skills/beginnerd-ask/references/workflow-registry.md",
    ),
}


def git_blob_sha(content: bytes) -> str:
    header = ("blob " + str(len(content)) + "\0").encode("ascii")
    return hashlib.sha1(header + content).hexdigest()


def render(source: str, content: bytes) -> str:
    text = content.decode("utf-8")
    if "\r" in text:
        raise ValueError(f"Canonical source must use LF line endings: {source}")
    banner = (
        "<!-- GENERATED FILE — DO NOT EDIT DIRECTLY.\n"
        f"Canonical source: {source}\n"
        f"Canonical Git blob SHA-1: {git_blob_sha(content)}\n"
        "Regenerate: python3 scripts/build_portable_references.py --write\n"
        "-->\n\n"
    )
    return banner + text.rstrip("\n") + "\n"


def synchronize(*, check: bool = True, root: Path = ROOT) -> list[str]:
    issues = []
    for source, destinations in SOURCES.items():
        path = root / source
        if not path.is_file():
            issues.append(f"missing canonical source: {source}")
            continue
        try:
            expected = render(source, path.read_bytes())
        except (ValueError, UnicodeDecodeError) as exc:
            issues.append(str(exc))
            continue
        for destination in destinations:
            target = root / destination
            if check:
                if not target.is_file():
                    issues.append(f"missing portable reference: {destination}")
                elif target.read_text(encoding="utf-8") != expected:
                    issues.append(f"stale portable reference: {destination}")
            else:
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_text(expected, encoding="utf-8", newline="\n")
    return issues


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--check", action="store_true", help="Verify committed copies (default).")
    mode.add_argument("--write", action="store_true", help="Regenerate copies from canonical docs.")
    args = parser.parse_args()
    issues = synchronize(check=not args.write)
    if issues:
        print("PORTABLE REFERENCES: FAIL")
        for issue in issues:
            print(" - " + issue)
        return 1
    if args.write:
        print("PORTABLE REFERENCES: GENERATED (review diff before committing)")
    else:
        print("PORTABLE REFERENCES: PASS (all generated snapshots match canonical sources)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
