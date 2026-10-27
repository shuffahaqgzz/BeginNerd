"""All six phase skill packages: source evidence only, not live acceptance."""
import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
REGISTRY = ROOT / "docs/workflows/WORKFLOW-REGISTRY.md"
OWNERS = {
    "PRODUCT-FOUNDATION": "beginnerd-product",
    "SOLUTION": "beginnerd-solution",
    "PLANNING": "beginnerd-plan",
    "FOUNDATION": "beginnerd-foundation",
    "IMPLEMENTATION": "beginnerd-implement",
    "RELEASE": "beginnerd-release",
    "OPERATIONS": "beginnerd-release",
}


class AllLifecycleSourceTests(unittest.TestCase):
    def test_all_32_workflow_ids_are_owned_by_skill_sources(self):
        rows = re.findall(
            r"^\|\s*((?:PRODUCT-FOUNDATION|SOLUTION|PLANNING|FOUNDATION|IMPLEMENTATION|RELEASE|OPERATIONS)-\d{2})\s*\|.*?\|\s*(beginnerd-[a-z-]+)\s*\|",
            REGISTRY.read_text(), re.M
        )
        self.assertEqual(len(rows), 32)
        for workflow, owner in rows:
            with self.subTest(workflow=workflow):
                prefix = workflow.rsplit("-", 1)[0]
                self.assertEqual(OWNERS[prefix], owner)
                self.assertIn(workflow, (ROOT / "skills" / owner / "SKILL.md").read_text())

    def test_governance_survives_without_providers(self):
        references = {
            "beginnerd-product": ("PRODUCT-FOUNDATION-01", "Product Baseline"),
            "beginnerd-solution": ("SOLUTION-06", "Solution Design"),
            "beginnerd-plan": ("PLANNING-02", "technical steps"),
            "beginnerd-foundation": ("beginnerd-setup", "provider"),
            "beginnerd-implement": ("IMPLEMENTATION-01", "maximum two"),
            "beginnerd-release": ("OPERATIONS-01", "separate explicit approval"),
        }
        for name, terms in references.items():
            with self.subTest(skill=name):
                text = (ROOT / "skills" / name / "SKILL.md").read_text().lower()
                for term in terms:
                    self.assertIn(term.lower(), text)
        setup = (ROOT / "skills/beginnerd-setup/SKILL.md").read_text().lower()
        self.assertIn("optional", setup)
        self.assertIn("opt-in", setup)

    def test_activation_and_behavior_are_not_premarked_pass(self):
        activation = json.loads((ROOT / "tests/activation/queries.json").read_text())
        behavior = json.loads((ROOT / "tests/behavioral/scenarios.json").read_text())
        assert_names = {"beginnerd-ask", "beginnerd-setup", "beginnerd-product",
                        "beginnerd-solution", "beginnerd-plan", "beginnerd-foundation",
                        "beginnerd-implement", "beginnerd-release"}
        self.assertEqual({x["skill"] for x in activation}, assert_names)
        for items in (activation, behavior):
            self.assertEqual(len({x["id"] for x in items}), len(items))
            self.assertTrue(all(x["execution_status"] == "NOT_EXECUTED" for x in items))
        for name in assert_names:
            subset = [x for x in activation if x["skill"] == name]
            self.assertTrue(any(c["should_trigger"] for c in subset))
            self.assertTrue(any(not c["should_trigger"] for c in subset))

    def test_status_discloses_unverified_real_use(self):
        content = (ROOT / "docs/implementation/STATUS.md").read_text()
        for term in ("PARTIAL", "NOT EXECUTED", "srv-test01", "A2"):
            self.assertIn(term, content)


if __name__ == "__main__":
    unittest.main()
