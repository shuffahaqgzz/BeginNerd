"""Static run-7 follow-up source checks; these are NOT runtime acceptance."""
import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
ALL_SKILLS = ("beginnerd-ask", "beginnerd-setup", "beginnerd-product", "beginnerd-solution",
              "beginnerd-plan", "beginnerd-foundation", "beginnerd-implement", "beginnerd-release")
FIFTH_LINE = "change global or harness configuration only after the user approves that named setting and scope"


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def plain(text: str) -> str:
    return re.sub(r"\s+", " ", text.replace("**", "")).lower()


class ConfigAllowlistAndGrantBoundaryTests(unittest.TestCase):
    def test_governance_rules_reach_every_skill(self):
        phrases = ("configuration discovery uses an allowlist",
                   "masking or filtering a value yourself is not a safe substitute",
                   "every route counts as contact",
                   "a grant is not a product approval",
                   "never changes a revoked or withdrawn grant back to approved",
                   "credential-read enforcement must cover every route",
                   "enforcement not verified",
                   FIFTH_LINE)
        sources = {"governance": plain(read("docs/governance/AGENT-GOVERNANCE.md"))}
        for name in ALL_SKILLS:
            sources[name] = plain(read(f"skills/{name}/references/agent-governance.md"))
        for label, text in sources.items():
            for phrase in phrases:
                with self.subTest(source=label, phrase=phrase):
                    self.assertIn(phrase, text)

    def test_baseline_has_five_lines(self):
        policy = read("docs/governance/AGENT-GOVERNANCE.md")
        block = policy.split("### Project safety baseline", 1)[1].split("```")[1]
        lines = [x for x in block.splitlines() if x.startswith("- ")]
        self.assertEqual(len(lines), 5)
        self.assertIn(FIFTH_LINE, plain(lines[4]))
        harness = plain(read("skills/beginnerd-foundation/references/agent-harness.md"))
        self.assertIn("include these five lines", harness)
        self.assertIn("(5) " + FIFTH_LINE, harness)
        self.assertIn("five-line project safety baseline", plain(read("skills/beginnerd-setup/SKILL.md")))

    def test_skill_text(self):
        setup = plain(read("skills/beginnerd-setup/SKILL.md"))
        for phrase in ("discovery uses an allowlist", "memory resource uris",
                       "memory uris, a script, an http call", "enforcement not verified"):
            self.assertIn(phrase, setup)
        self.assertIn("accepting a grant proposal never marks scope", plain(read("skills/beginnerd-product/SKILL.md")))
        for name in ("beginnerd-product", "beginnerd-implement"):
            self.assertRegex(plain(read(f"skills/{name}/SKILL.md")), r"never (set|change) (it|a revoked grant) back to approved")

    def test_scenarios_protocol_and_record(self):
        cases = {x["id"]: x for x in json.loads(read("tests/behavioral/scenarios.json"))}
        new = cases["REVAL-38-GRANT-NOT-PRODUCT-APPROVAL-THEN-REVOKE"]
        self.assertEqual(new["execution_status"], "NOT_EXECUTED")
        self.assertEqual(len(new["turns"]), 3)
        self.assertTrue(all("sends verbatim" in t for t in new["turns"]))
        self.assertIn("even with self-masking", " ".join(cases["SETUP-09-SETUP-CHECK-NO-CREDENTIAL-READ"]["must_not"]))
        self.assertIn("record a product direction, scope or feature as approved from acceptance of the grant proposal",
                      cases["REVAL-14-NO-GRANT-ONE-QUESTION"]["must_not"])
        readme = read("tests/behavioral/README.md")
        for phrase in ("Log every attempted tool call", "separate placeholders", "canary line",
                       "only from reads of a skill's SKILL.md"):
            self.assertIn(phrase, readme)
        gates = read("docs/security/HARNESS-ACTION-GATES.md")
        self.assertIn("ENFORCEMENT NOT VERIFIED", gates)
        self.assertIn("every read route", gates)
        record = read("docs/implementation/RUNTIME-EVAL-RUNS-4-7.md")
        self.assertIn("REVIEWER-REPORTED / NOT INDEPENDENTLY REPRODUCED", record)
        for sha in ("63232556f83e", "c946e0332982", "811c24932650", "3c7601f47d01"):
            self.assertIn(sha, record)
        self.assertEqual(len(re.findall(r"`[0-9a-f]{64}`", record)), 5)


if __name__ == "__main__":
    unittest.main()
