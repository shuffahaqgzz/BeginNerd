"""Static runtime re-evaluation remediation source checks; these are NOT runtime acceptance."""
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


class RuntimeReevalRemediationTests(unittest.TestCase):
    def test_governance_closes_runtime_gaps(self):
        policy = plain(read("docs/governance/AGENT-GOVERNANCE.md"))
        for phrase in ("check before the first code write",
                       "if any one is missing, write no code",
                       "record approvals in the same turn",
                       "revocation is sticky",
                       "only a new explicit grant from the user restores local writes",
                       "never records an approval, grant or consent on the user's behalf",
                       "credential locations and provider data are off-limits for discovery",
                       "secrets found in files are reported, never printed",
                       "read-only discovery does not open credential stores",
                       "memory and knowledge providers are contacted only when chosen",
                       "never list, read, recall from or repeat another project's banks"):
            self.assertIn(phrase, policy)

    def test_every_portable_copy_carries_the_rules(self):
        for name in ALL_SKILLS:
            with self.subTest(skill=name):
                gov = plain(read(f"skills/{name}/references/agent-governance.md"))
                self.assertIn("revocation is sticky", gov)
                self.assertIn("read-only discovery does not open credential stores", gov)
                fam = plain(read(f"skills/{name}/references/familiarity-check.md"))
                self.assertIn("at level 0 the disclosure uses no unexplained technical words", fam)

    def test_familiarity_override_and_disclosure(self):
        contract = plain(read("docs/governance/FAMILIARITY-GUIDANCE-CONTRACT.md"))
        self.assertIn("even when a level is already recorded", contract)
        self.assertIn("over a recorded level; it changes explanation depth only, never safety disclosures",
                      contract)
        self.assertIn("route the fix as a separately approved task", contract)

    def test_skill_bodies_surface_the_coding_check(self):
        implement = plain(read("skills/beginnerd-implement/SKILL.md"))
        self.assertIn("before the first code write", implement)
        self.assertIn("a request to edit a named file is not one", implement)
        self.assertIn("product never writes application code or tests",
                      plain(read("skills/beginnerd-product/SKILL.md")))
        self.assertIn("implementation checks them again before the first code write",
                      plain(read("skills/beginnerd-plan/SKILL.md")))

    def test_setup_discovery_is_name_only_and_scoped(self):
        setup = plain(read("skills/beginnerd-setup/SKILL.md"))
        for phrase in ("not for general technical questions about apis, databases, caches",
                       "mention application code only as conditional",
                       "never open credential-bearing files",
                       "never contact a memory or knowledge provider during discovery",
                       "report only its location and type, never its value",
                       "never list, read or repeat other projects' banks"):
            self.assertIn(phrase, setup)
        self.assertIn("never print or quote the value", plain(read("skills/beginnerd-foundation/SKILL.md")))

    def test_new_scenarios_are_definitions_not_executed(self):
        cases = {x["id"]: x for x in json.loads(read("tests/behavioral/scenarios.json"))}
        for name in ("SETUP-09-SETUP-CHECK-NO-CREDENTIAL-READ", "REVAL-35-SECRET-FOUND-NOT-ECHOED"):
            with self.subTest(case=name):
                self.assertEqual(cases[name]["execution_status"], "NOT_EXECUTED")
        self.assertIn("contact the memory endpoint", cases["SETUP-09-SETUP-CHECK-NO-CREDENTIAL-READ"]["must_not"])
        self.assertIn("only as conditional",
                      " ".join(cases["REVAL-14-NO-GRANT-ONE-QUESTION"]["expected_behaviors"]))
        self.assertEqual(len(cases["REVAL-17-REVOKED-GRANT-STOPS-WRITES"]["turns"]), 3)
        queries = {x["id"]: x for x in json.loads(read("tests/activation/queries.json"))}
        for name in ("ACT-SETUP-09", "ACT-SETUP-10", "ACT-SETUP-11"):
            self.assertFalse(queries[name]["should_trigger"])

    def test_runtime_evaluation_isolation_is_documented(self):
        readme = plain(read("tests/behavioral/README.md"))
        for phrase in ("runtime evaluation isolation",
                       "never copy the operator's harness configuration",
                       "limit network access to the model endpoint",
                       "at least three sessions per case"):
            self.assertIn(phrase, readme)


if __name__ == "__main__":
    unittest.main()
