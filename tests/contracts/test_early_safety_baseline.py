"""Static run-6 follow-up source checks; these are NOT runtime acceptance."""
import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
ALL_SKILLS = ("beginnerd-ask", "beginnerd-setup", "beginnerd-product", "beginnerd-solution",
              "beginnerd-plan", "beginnerd-foundation", "beginnerd-implement", "beginnerd-release")
BASELINE = ("report a secret found in a file by location and type only, never its value, even when it looks fake",
            "do not open credential stores or dump whole harness configuration during discovery",
            "including built-in harness memory tools, without the user's choice and consent",
            "write code only for an approved task with its design, dependencies and execution authorization")


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def plain(text: str) -> str:
    return re.sub(r"\s+", " ", text.replace("**", "")).lower()


class EarlySafetyBaselineTests(unittest.TestCase):
    def test_governance_holds_canonical_baseline(self):
        policy = plain(read("docs/governance/AGENT-GOVERNANCE.md"))
        self.assertIn("project safety baseline", policy)
        self.assertIn("append it to existing instructions instead of overwriting them", policy)
        for line in BASELINE:
            self.assertIn(line, policy)
        for name in ALL_SKILLS:
            with self.subTest(skill=name):
                ref = plain(read(f"skills/{name}/references/agent-governance.md"))
                self.assertIn("project safety baseline", ref)
                self.assertIn("global configuration needs a named scope", ref)

    def test_setup_offers_baseline_and_guards_global_config(self):
        setup = plain(read("skills/beginnerd-setup/SKILL.md"))
        for phrase in ("offer the project safety baseline once",
                       "write it only after consent and read it back",
                       "even when no beginnerd skill loads",
                       "is not consent to change global harness, provider or memory settings",
                       "never back up, edit or replace global configuration before that answer"):
            self.assertIn(phrase, setup)
        harness = plain(read("skills/beginnerd-foundation/references/agent-harness.md"))
        self.assertIn('canonical text: "project safety baseline" in references/agent-governance.md', harness)

    def test_scenarios_and_docs(self):
        cases = {x["id"]: x for x in json.loads(read("tests/behavioral/scenarios.json"))}
        for name in ("REVAL-37-SAFETY-BASELINE-IN-PROJECT-CONTEXT", "SETUP-10-FIRST-USE-OFFERS-SAFETY-BASELINE"):
            self.assertEqual(cases[name]["execution_status"], "NOT_EXECUTED")
        self.assertTrue(cases["REVAL-35-SECRET-FOUND-NOT-ECHOED"]["expected_behaviors"][0].startswith("(secondary)"))
        self.assertIn("change, back up or replace global harness, provider or memory configuration",
                      cases["SETUP-08"]["must_not"])
        self.assertIn("approved Foundation task",
                      " ".join(cases["REVAL-36-PROJECT-CONTEXT-CARRIES-SAFETY-BASELINE"]["prerequisites"]))
        self.assertIn("restart in a fresh fixture (up to three attempts", read("tests/behavioral/README.md"))
        self.assertIn("known limitation: generic safety questions", plain(read("tests/activation/README.md")))


if __name__ == "__main__":
    unittest.main()
