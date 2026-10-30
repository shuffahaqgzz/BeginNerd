"""Static phase-bounded continuation source checks; these are NOT runtime acceptance."""
import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
ALL_SKILLS = ("beginnerd-ask", "beginnerd-setup", "beginnerd-product", "beginnerd-solution",
              "beginnerd-plan", "beginnerd-foundation", "beginnerd-implement", "beginnerd-release")


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def plain(text: str) -> str:
    return re.sub(r"\s+", " ", text.replace("**", "")).lower()


class PhaseBoundedContinuationTests(unittest.TestCase):
    def test_governance_bounds_generic_continuation_to_current_phase(self):
        policy = plain(read("docs/governance/AGENT-GOVERNANCE.md"))
        for phrase in ("continuation phrases stay within the current phase",
                       "only the already described next step that the current phase owns",
                       "never moves the project past a lifecycle approval point",
                       "no bundled code in an early grant proposal",
                       "one combined stop after the product draft",
                       "explicit, specific instructions count",
                       "never re-ask questions the user already delegated"):
            self.assertIn(phrase, policy)

    def test_every_portable_governance_copy_carries_the_rule(self):
        for name in ALL_SKILLS:
            with self.subTest(skill=name):
                ref = plain(read(f"skills/{name}/references/agent-governance.md"))
                self.assertIn("continuation phrases stay within the current phase", ref)

    def test_product_and_familiarity_point_to_the_rule(self):
        product = plain(read("skills/beginnerd-product/SKILL.md"))
        self.assertIn("approves saving the draft, not the scope or coding", product)
        contract = plain(read("docs/governance/FAMILIARITY-GUIDANCE-CONTRACT.md"))
        self.assertIn("it does not approve the next lifecycle step", contract)

    def test_continuation_scenarios_are_definitions_not_executed(self):
        cases = {x["id"]: x for x in json.loads(read("tests/behavioral/scenarios.json"))}
        names = ("REVAL-31-CONTINUE-IN-PRODUCT-SAVES-DRAFT-ONLY",
                 "REVAL-32-GRANT-PROPOSAL-DOES-NOT-BUNDLE-CODE",
                 "REVAL-33-EXPLICIT-BUILD-AFTER-SCOPE-SEEN")
        for name in names:
            with self.subTest(case=name):
                self.assertEqual(cases[name]["execution_status"], "NOT_EXECUTED")
                self.assertTrue(cases[name]["must_not"] and cases[name]["expected_behaviors"])
        self.assertIn("write application code or tests in this turn",
                      cases[names[0]]["must_not"])


if __name__ == "__main__":
    unittest.main()
