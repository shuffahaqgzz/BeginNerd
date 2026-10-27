"""Offline repository source checks. These do not demonstrate actual skill runtime behavior."""
import json
import re
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
from scripts.validate_repository import validate, ROW, COUNTS

SKILLS = ("beginnerd-ask", "beginnerd-setup", "beginnerd-product",
          "beginnerd-solution", "beginnerd-plan", "beginnerd-foundation",
          "beginnerd-implement", "beginnerd-release")


class RepositoryContractsTests(unittest.TestCase):
    def test_repository_static_checks_pass(self):
        self.assertEqual(validate(), [])

    def test_32_unique_canonical_workflows(self):
        source = (ROOT / "docs/workflows/WORKFLOW-REGISTRY.md").read_text()
        ids = ROW.findall(source)
        self.assertEqual(len(ids), 32)
        self.assertEqual(len(set(ids)), 32)
        counts = {prefix: sum(1 for item in ids if item[0] == prefix) for prefix in COUNTS}
        self.assertEqual(counts, COUNTS)
        self.assertIn("PRODUCT-FOUNDATION-01", source)
        self.assertNotIn("| PF-01 |", source)
        migration = (ROOT / "docs/workflows/WORKFLOW-ID-MIGRATION.md").read_text()
        for term in ("PF-", "PRODUCT-FOUNDATION-", "IMPLEMENT-", "IMPLEMENTATION-",
                     "OPS-", "OPERATIONS-"):
            self.assertIn(term, migration)

    def test_all_eight_sources_are_not_claimed_runtime_pass(self):
        for name in SKILLS:
            with self.subTest(skill=name):
                source = (ROOT / "skills" / name / "SKILL.md").read_text()
                self.assertTrue(source.startswith("---\n"))
                self.assertIn("name: " + name, source)
                self.assertIn("description:", source)
        for name in SKILLS[3:]:
            self.assertIn("RUNTIME UNVERIFIED", (ROOT / "skills" / name / "README.md").read_text().upper())
        status = (ROOT / "docs/implementation/STATUS.md").read_text()
        self.assertIn("PARTIAL", status)

    def test_opt_in_provider_contract_and_bounded_recovery(self):
        policy = (ROOT / "docs/governance/AGENT-GOVERNANCE.md").read_text()
        memory = (ROOT / "docs/governance/MEMORY-KNOWLEDGE-CONTRACT.md").read_text()
        self.assertIn("maximum two attempts", policy.lower())
        for key in ("READ", "LOCAL_WRITE", "PROVIDER_CONFIG", "EXTERNAL_CREATE", "DEPLOY_RELEASE", "SECRET_ADMIN"):
            self.assertIn(key, policy)
        for word in ("Graphify", "Hindsight", "opt-in", "NOT_ENABLED", "MEMORY_SYNC_PENDING"):
            self.assertIn(word, memory)

    def test_phase_decision_matrix_provenance_retained(self):
        content = (ROOT / "docs/decisions/BN-DEC-009-APPROVED-DETAILS.md").read_text()
        self.assertEqual(len(re.findall(r"^\| 5[A-N] \|", content, re.M)), 14)
        self.assertEqual(len(re.findall(r"^\| 6[A-F] \|", content, re.M)), 6)

    def test_behavioral_registry_is_only_a_specification(self):
        items = json.loads((ROOT / "tests/behavioral/scenarios.json").read_text())
        self.assertGreaterEqual(len(items), 67)
        self.assertTrue(all(item["execution_status"] == "NOT_EXECUTED" for item in items))


if __name__ == "__main__":
    unittest.main()
