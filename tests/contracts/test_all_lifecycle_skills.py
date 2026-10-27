"""Checks all six lifecycle source contracts, no runtime claim."""
import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
REGISTRY = ROOT / "docs/workflows/WORKFLOW-REGISTRY.md"
OWNERS = {
    "PF": "beginnerd-product", "SOLUTION": "beginnerd-solution",
    "PLANNING": "beginnerd-plan", "FOUNDATION": "beginnerd-foundation",
    "IMPLEMENT": "beginnerd-implement", "RELEASE": "beginnerd-release",
    "OPS": "beginnerd-release",
}


class AllLifecycleSourceTests(unittest.TestCase):
    def test_all_32_workflow_ids_are_owned_by_installable_sources(self):
        rows = re.findall(r"^\|\s*((?:PF|SOLUTION|PLANNING|FOUNDATION|IMPLEMENT|RELEASE|OPS)-(?:\d{2}))\s*\|.*?\|\s*(beginnerd-[a-z-]+)\s*\|", REGISTRY.read_text(), re.M)
        self.assertEqual(len(rows), 32)
        for workflow, owner in rows:
            with self.subTest(workflow=workflow):
                prefix = workflow.split("-")[0]
                self.assertEqual(owner, OWNERS[prefix])
                source = ROOT / "skills" / owner / "SKILL.md"
                self.assertTrue(source.is_file())
                self.assertIn(workflow, source.read_text(encoding="utf-8"))

    def test_required_execution_boundaries_exist(self):
        data = {
            "beginnerd-solution": ["SOLUTION-06", "SOLUTION-07", "G2", "PLANNING-02", "UNVERIFIED"],
            "beginnerd-plan": ["PLANNING-02", "work-structure-brainstorming.md", "PARTIAL", "authorization"],
            "beginnerd-foundation": ["beginnerd-setup", "Hindsight", "Foundation Readiness"],
            "beginnerd-implement": ["PLANNING-02", "2", "REVIEW_REQUIRED", "authorization"],
            "beginnerd-release": ["OPS-03", "DEPLOY_RELEASE", "authorization", "rollback"],
        }
        for skill, phrases in data.items():
            with self.subTest(skill=skill):
                source = (ROOT / "skills" / skill / "SKILL.md").read_text()
                for phrase in phrases:
                    self.assertIn(phrase.lower(), source.lower())

    def test_activation_and_behavior_cases_have_no_fabricated_execution(self):
        activations = json.loads((ROOT / "tests/activation/queries.json").read_text())
        behavior = json.loads((ROOT / "tests/behavioral/scenarios.json").read_text())
        expected = {"beginnerd-ask", "beginnerd-setup", "beginnerd-product",
                    "beginnerd-solution", "beginnerd-plan", "beginnerd-foundation",
                    "beginnerd-implement", "beginnerd-release"}
        self.assertEqual({x["skill"] for x in activations}, expected)
        self.assertEqual(len({x["id"] for x in activations}), len(activations))
        self.assertEqual(len({x["id"] for x in behavior}), len(behavior))
        self.assertTrue(all(x["execution_status"] == "NOT_EXECUTED" for x in activations + behavior))
        for skill in expected:
            subset = [x for x in activations if x["skill"] == skill]
            self.assertTrue(any(x["should_trigger"] for x in subset))
            self.assertTrue(any(not x["should_trigger"] for x in subset))

    def test_no_e2e_success_claimed_from_source(self):
        state = (ROOT / "docs/implementation/STATUS.md").read_text()
        self.assertIn("PARTIAL", state)
        self.assertIn("NOT EXECUTED", state)
        self.assertIn("srv-test01", state)
        self.assertIn("A2", state)


if __name__ == "__main__":
    unittest.main()
