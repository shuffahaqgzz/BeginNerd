#!/usr/bin/env python3
"""Optional strict read-only hook example for Claude Code and Cursor.

This profile rejects every tool call except a small, explicitly recognized
set of read-only tools. It is NOT a general authorization engine. Do not install
it automatically or assume it covers browser/network tools beyond its hook.
"""
import argparse
import json
import re
import sys

READ_ONLY_TOOLS = {"Read", "Glob", "Grep", "LS"}
SECRET_PATH = re.compile(r"(^|/)(\.env(?:\.|$)|id_rsa(?:$|\.)|.*\.pem$|.*\.key$)", re.I)


def decide(record):
    if not isinstance(record, dict):
        return "deny"
    tool = record.get("tool_name")
    if not isinstance(tool, str) or tool not in READ_ONLY_TOOLS:
        return "deny"
    data = record.get("tool_input", {})
    if isinstance(data, str):
        try:
            data = json.loads(data)
        except ValueError:
            return "deny"
    if not isinstance(data, dict):
        return "deny"
    for field in ("file_path", "path", "pattern"):
        value = data.get(field)
        if isinstance(value, str) and SECRET_PATH.search(value.replace("\\", "/")):
            return "deny"
    return "allow"


def run(harness, payload):
    verdict = decide(payload)
    if harness == "claude":
        if verdict == "allow":
            return 0, "", ""
        return 2, "", "BeginNerd read-only profile: tool not allowed; use an explicitly approved harness permission profile.\n"
    if harness == "cursor":
        response = {
            "permission": verdict,
            "user_message": "This read-only profile blocks writing and external tools." if verdict == "deny" else "",
            "agent_message": "Choose a read-only operation or request separately configured authorization." if verdict == "deny" else "",
        }
        return 0, json.dumps(response) + "\n", ""
    raise ValueError("Unsupported harness")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--harness", choices=("claude", "cursor"), required=True)
    args = parser.parse_args()
    try:
        raw = sys.stdin.read(1024 * 1024)
        payload = json.loads(raw)
    except (ValueError, OSError):
        payload = {}
    code, stdout, stderr = run(args.harness, payload)
    if stdout:
        sys.stdout.write(stdout)
    if stderr:
        sys.stderr.write(stderr)
    return code


if __name__ == "__main__":
    sys.exit(main())
