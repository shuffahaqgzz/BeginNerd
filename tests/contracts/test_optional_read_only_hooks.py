"""Offline strict-read hook tests. They do NOT prove live harness enforcement."""
import importlib.util
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SCRIPT = ROOT / "scripts/guardrails/read_only_hook.py"
spec = importlib.util.spec_from_file_location("beginnerd_read_only_gate", SCRIPT)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


class ReadOnlyHookTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(prefix="beginnerd-hook-")
        self.addCleanup(self.tmp.cleanup)
        base = Path(self.tmp.name)
        self.root = base / "allowed-project"
        (self.root / "docs").mkdir(parents=True)
        (self.root / "docs" / "README.md").write_text("architecture and .env documentation\n")
        (self.root / ".env").write_text("synthetic_fixture_not_a_real_token\n")
        (self.root / "keys").mkdir()
        (self.root / "keys" / "private.pem").write_text("synthetic fixture\n")
        self.outside = base / "outside.md"
        self.outside.write_text("synthetic outside content\n")

    def decide(self, tool, data, *, root=None):
        return module.decide(
            {"tool_name": tool, "tool_input": data},
            self.root if root is None else root,
        )

    def test_only_explicit_regular_files_are_readable(self):
        self.assertEqual(self.decide("Read", {"file_path": "docs/README.md"}), "allow")
        self.assertEqual(self.decide("Read", {"file_path": str(self.root / "docs/README.md")}), "allow")
        self.assertEqual(self.decide("Read", {"file_path": "docs/README.md", "offset": 0, "limit": 1}), "allow")
        self.assertEqual(self.decide("Grep", {"path": "docs/README.md", "pattern": "architecture"}), "allow")
        # A text search for the literal word '.env' inside a safe explicit file is not a path traversal.
        self.assertEqual(self.decide("Grep", {"path": "docs/README.md", "pattern": ".env"}), "allow")

    def test_recurse_and_glob_are_denied(self):
        for tool, data in [
            ("Grep", {"pattern": "anything"}),
            ("Grep", {"path": ".", "pattern": "anything"}),
            ("Grep", {"path": str(self.root), "pattern": "anything"}),
            ("Grep", {"path": "docs/README.md", "pattern": "anything", "glob": "**/.env*"}),
            ("Grep", {"path": "docs/README.md", "pattern": "anything", "include": "*.md"}),
            ("Grep", {"path": "docs/*.md", "pattern": "anything"}),
            ("Glob", {"path": ".", "pattern": "**/*"}),
            ("Glob", {"glob": "**/.env*"}),
            ("LS", {"path": "."}),
        ]:
            with self.subTest(tool=tool, data=data):
                self.assertEqual(self.decide(tool, data), "deny")

    def test_sensitive_and_scope_escape_are_denied(self):
        for filename in [
            ".env", ".env.production", "keys/private.pem", ".git/config",
            ".ssh/id_rsa", "../outside.md", str(self.outside),
            ".", "docs", "docs/missing.md", "docs\\README.md",
            "docs/../../outside.md", "docs/README.md*", "\u0000.env",
        ]:
            with self.subTest(path=filename):
                self.assertEqual(self.decide("Read", {"file_path": filename}), "deny")
        self.assertEqual(self.decide("Grep", {"path": ".env", "pattern": "synthetic"}), "deny")

    def test_symlink_to_outside_or_sensitive_file_is_denied(self):
        try:
            (self.root / "docs" / "outside-link.md").symlink_to(self.outside)
            (self.root / "docs" / "env-link.md").symlink_to(self.root / ".env")
            (self.root / "linked-docs").symlink_to(self.root / "docs", target_is_directory=True)
        except (OSError, NotImplementedError):
            self.skipTest("symlinks unsupported")
        for filename in ("docs/outside-link.md", "docs/env-link.md", "linked-docs/README.md"):
            self.assertEqual(self.decide("Read", {"file_path": filename}), "deny")

    def test_missing_or_bad_root_fail_closed(self):
        payload = {"tool_name": "Read", "tool_input": {"file_path": "docs/README.md"}}
        for root in (None, "", ".", "relative/path", self.outside, self.root / "absent"):
            with self.subTest(root=root):
                self.assertEqual(module.decide(payload, root), "deny")
        self.assertEqual(module.decide(None, self.root), "deny")
        self.assertEqual(module.decide({"tool_name": "Read", "tool_input": "{broken"}, self.root), "deny")
        self.assertEqual(module.decide({"tool_name": "Read", "tool_input": []}, self.root), "deny")

    def test_unknown_tools_and_parameters_fail_closed(self):
        for tool in ("Bash", "Write", "Edit", "Task", "Shell", "mcp__sites__deploy", ""):
            self.assertEqual(self.decide(tool, {"file_path": "docs/README.md"}), "deny")
        for data in (
            {"file_path": "docs/README.md", "unknown": True},
            {"file_path": "docs/README.md", "limit": -1},
            {"file_path": "docs/README.md", "offset": True},
        ):
            self.assertEqual(self.decide("Read", data), "deny")

    def test_claude_and_cursor_deny_and_allow_with_root(self):
        for tool, data, verdict in (
            ("Read", {"file_path": "docs/README.md"}, "allow"),
            ("Grep", {"path": ".", "pattern": "test"}, "deny"),
        ):
            payload = {"tool_name": tool, "tool_input": data}
            self.assertEqual(module.run("claude", payload, self.root)[0], 0 if verdict == "allow" else 2)
            code, output, error = module.run("cursor", payload, self.root)
            self.assertEqual(code, 0)
            self.assertEqual(json.loads(output)["permission"], verdict)
            self.assertEqual(error, "")
        self.assertEqual(module.run("claude", {"tool_name": "Read", "tool_input": {"file_path": "docs/README.md"}})[0], 2)

    def test_cli_requires_explicit_root_and_denies_unscoped_request(self):
        payload = json.dumps({"tool_name": "Grep", "tool_input": {"path": ".", "pattern": "anything"}})
        result = subprocess.run(
            [sys.executable, str(SCRIPT), "--harness", "claude", "--root", str(self.root)],
            input=payload, text=True, capture_output=True, check=False,
        )
        self.assertEqual(result.returncode, 2)
        safe = subprocess.run(
            [sys.executable, str(SCRIPT), "--harness", "claude", "--root", str(self.root)],
            input=json.dumps({"tool_name": "Read", "tool_input": {"file_path": "docs/README.md"}}),
            text=True, capture_output=True, check=False,
        )
        self.assertEqual(safe.returncode, 0)
        missing = subprocess.run(
            [sys.executable, str(SCRIPT), "--harness", "claude"],
            input=payload, text=True, capture_output=True, check=False,
        )
        self.assertNotEqual(missing.returncode, 0)

    def test_docs_disclose_true_boundaries(self):
        docs = (ROOT / "docs/security/HARNESS-ACTION-GATES.md").read_text()
        for term in ("fail-closed", "not a harmless tool-denial", "UNVERIFIED",
                     "not technical enforcement", "--root", "Grep", "Glob", "symlink"):
            self.assertIn(term.lower(), docs.lower())


if __name__ == "__main__":
    unittest.main()
