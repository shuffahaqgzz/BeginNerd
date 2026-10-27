"""Offline read-only hook fixture tests; these are not effective harness installs."""
import importlib.util
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
file = ROOT / "scripts/guardrails/read_only_hook.py"
spec = importlib.util.spec_from_file_location("beginnerd_read_only_gate", file)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


class ReadOnlyHookTests(unittest.TestCase):
    def test_explicit_read_only_tools(self):
        self.assertEqual(module.decide({"tool_name": "Read", "tool_input": {"file_path": "docs/README.md"}}), "allow")
        self.assertEqual(module.decide({"tool_name": "Grep", "tool_input": {"pattern": "architecture"}}), "allow")

    def test_unknown_and_mutation_tools_are_denied(self):
        for name in ("Bash", "Write", "Edit", "Task", "Shell", "mcp__sites__create", "mcp__sites__deploy", ""):
            with self.subTest(tool=name):
                self.assertEqual(module.decide({"tool_name": name, "tool_input": {}}), "deny")
        self.assertEqual(module.decide({"tool_input": {}}), "deny")
        self.assertEqual(module.decide(None), "deny")

    def test_sensitive_paths_and_malformed_inputs_denied(self):
        for filename in (".env", ".env.production", "secrets/id_rsa", "keys/private.pem", "secrets/private.key"):
            self.assertEqual(module.decide({"tool_name": "Read", "tool_input": {"file_path": filename}}), "deny")
        self.assertEqual(module.decide({"tool_name": "Read", "tool_input": "{broken"}), "deny")

    def test_claude_exit_two_blocks(self):
        self.assertEqual(module.run("claude", {"tool_name": "Write", "tool_input": {}})[0], 2)
        self.assertEqual(module.run("claude", {"tool_name": "Read", "tool_input": {}})[0], 0)

    def test_cursor_returns_permission_json(self):
        code, output, error = module.run("cursor", {"tool_name": "mcp__deploy", "tool_input": {}})
        self.assertEqual(code, 0)
        self.assertEqual(json.loads(output)["permission"], "deny")
        self.assertEqual(error, "")
        code, output, _ = module.run("cursor", {"tool_name": "Read", "tool_input": {}})
        self.assertEqual(json.loads(output)["permission"], "allow")

    def test_docs_mark_source_vs_runtime(self):
        docs = (ROOT / "docs/security/HARNESS-ACTION-GATES.md").read_text()
        for term in ("fail-closed", "not a harmless tool-denial", "UNVERIFIED", "not technical enforcement"):
            self.assertIn(term.lower(), docs.lower())


if __name__ == "__main__":
    unittest.main()
