"""Static run-4 follow-up source checks; these are NOT runtime acceptance."""
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


class MemoryToolsAndSecretRoutingTests(unittest.TestCase):
    def test_governance_covers_builtin_memory_tools_and_config_dumps(self):
        policy = plain(read("docs/governance/AGENT-GOVERNANCE.md"))
        for phrase in ("built-in harness memory tools count as provider contact",
                       "do not call them during discovery",
                       "never a reason to call further memory tools",
                       "never dump a whole harness configuration by any route"):
            self.assertIn(phrase, policy)
        for name in ALL_SKILLS:
            with self.subTest(skill=name):
                ref = plain(read(f"skills/{name}/references/agent-governance.md"))
                self.assertIn("built-in harness memory tools count as provider contact", ref)

    def test_setup_names_builtin_tools_and_config_dumps(self):
        setup = plain(read("skills/beginnerd-setup/SKILL.md"))
        self.assertIn("including the harness's own built-in recall/retain tools", setup)
        self.assertIn("directly or through the harness's built-in memory tools", setup)
        self.assertIn("never dump a whole harness configuration", setup)

    def test_foundation_owns_project_safety_check(self):
        foundation = plain(read("skills/beginnerd-foundation/SKILL.md"))
        self.assertIn("check an existing project folder for exposed secrets", foundation)
        self.assertIn("by location and type, with one recommended next step", foundation)
        queries = {x["id"]: x for x in json.loads(read("tests/activation/queries.json"))}
        for name in ("ACT-FOUNDATION-SECRETS", "ACT-FOUNDATION-SECRETS-EN"):
            self.assertEqual(queries[name]["skill"], "beginnerd-foundation")
            self.assertTrue(queries[name]["should_trigger"])

    def test_product_never_records_unseen_approval(self):
        self.assertIn("never record an approval the user did not give",
                      plain(read("skills/beginnerd-product/SKILL.md")))

    def test_scenarios_and_protocol_updated(self):
        cases = {x["id"]: x for x in json.loads(read("tests/behavioral/scenarios.json"))}
        setup09 = cases["SETUP-09-SETUP-CHECK-NO-CREDENTIAL-READ"]
        self.assertIn("call the harness's built-in memory tools (recall, retain or similar)", setup09["must_not"])
        self.assertTrue(all("sends verbatim" in t for t in cases["REVAL-14-NO-GRANT-ONE-QUESTION"]["turns"]))
        self.assertTrue(all("sends verbatim" in t for t in cases["REVAL-17-REVOKED-GRANT-STOPS-WRITES"]["turns"]))
        readme = plain(read("tests/behavioral/README.md"))
        for phrase in ("loopback servers that the subject starts inside the fixture",
                       "a session that ends silently is inconclusive",
                       "never sends it as a message"):
            self.assertIn(phrase, readme)


if __name__ == "__main__":
    unittest.main()
