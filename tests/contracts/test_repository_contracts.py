"""Unit tests for bootstrap static contracts; not proof of runtime behavior."""
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
from scripts.validate_repository import validate, ROW, COUNTS

class RepositoryContractsTests(unittest.TestCase):
    def test_bootstrap_contracts_have_no_static_errors(self):
        self.assertEqual(validate(), [])

    def test_workflow_registry_count_and_unique_ids(self):
        text = (ROOT / "docs/workflows/WORKFLOW-REGISTRY.md").read_text(encoding="utf-8")
        ids = ROW.findall(text)
        self.assertEqual(len(ids), 32)
        self.assertEqual(len(set(ids)), 32)

    def test_phase_counts_are_locked(self):
        text = (ROOT / "docs/workflows/WORKFLOW-REGISTRY.md").read_text(encoding="utf-8")
        ids = ROW.findall(text)
        actual = {name: sum(1 for item in ids if item[0] == name) for name in COUNTS}
        self.assertEqual(actual, COUNTS)

    def test_both_companions_have_skill_metadata(self):
        for name in ("beginnerd-ask", "beginnerd-setup"):
            with self.subTest(skill=name):
                skill = (ROOT / "skills" / name / "SKILL.md").read_text(encoding="utf-8")
                self.assertTrue(skill.startswith("---\n"))
                self.assertIn("name: " + name, skill)
                self.assertIn("description:", skill)

    def test_all_lifecycle_sources_exist_but_not_runtime_verified(self):
        for name in ("beginnerd-solution", "beginnerd-plan",
                     "beginnerd-foundation", "beginnerd-implement", "beginnerd-release"):
            with self.subTest(skill=name):
                self.assertTrue((ROOT / "skills" / name / "SKILL.md").is_file())
                content = (ROOT / "skills" / name / "README.md").read_text(encoding="utf-8").upper()
                self.assertIn("SOURCE", content)
                self.assertIn("RUNTIME UNVERIFIED", content)

    def test_product_skill_exists_but_runtime_unverified(self):
        skill = (ROOT / "skills" / "beginnerd-product" / "SKILL.md").read_text(encoding="utf-8")
        self.assertIn("name: beginnerd-product", skill)
        for workflow in ("PF-01", "PF-02", "PF-03", "PF-04", "G1"):
            self.assertIn(workflow, skill)
        state = (ROOT / "docs" / "implementation" / "STATUS.md").read_text(encoding="utf-8")
        self.assertIn("beginnerd-product", state)
        self.assertIn("Entire beginnerd-product operational acceptance", state)
        self.assertIn("PARTIAL", state)

    def test_memory_and_recovery_limits_documented(self):
        memory = (ROOT / "docs/governance/MEMORY-KNOWLEDGE-CONTRACT.md").read_text(encoding="utf-8")
        policy = (ROOT / "docs/governance/AGENT-GOVERNANCE.md").read_text(encoding="utf-8")
        self.assertIn("Graphify", memory)
        self.assertIn("Hindsight", memory)
        self.assertIn("MEMORY_SYNC_PENDING", memory)
        self.assertIn("maximum two attempts", policy.lower())

    def test_phase_decision_matrix_coverage(self):
        import re
        content = (ROOT / "docs/decisions/BN-DEC-009-APPROVED-DETAILS.md").read_text(encoding="utf-8")
        self.assertEqual(len(re.findall(r"^\| 5[A-N] \|", content, re.M)), 14)
        self.assertEqual(len(re.findall(r"^\| 6[A-F] \|", content, re.M)), 6)

    def test_behavioral_cases_remain_not_executed(self):
        import json
        cases = json.loads((ROOT / "tests/behavioral/scenarios.json").read_text(encoding="utf-8"))
        self.assertGreaterEqual(len(cases), 16)
        self.assertTrue(all(case["execution_status"] == "NOT_EXECUTED" for case in cases))

if __name__ == "__main__":
    unittest.main()
