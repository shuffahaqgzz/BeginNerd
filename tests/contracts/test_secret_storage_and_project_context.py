"""Static run-5 follow-up source checks; these are NOT runtime acceptance."""
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


class SecretStorageAndProjectContextTests(unittest.TestCase):
    def test_governance_recommends_secrets_out_of_readable_files(self):
        phrase = "keep secrets out of files an agent can read"
        self.assertIn(phrase, plain(read("docs/governance/AGENT-GOVERNANCE.md")))
        for name in ALL_SKILLS:
            with self.subTest(skill=name):
                self.assertIn(phrase, plain(read(f"skills/{name}/references/agent-governance.md")))
        self.assertIn("never move or rewrite it without that approval",
                      plain(read("docs/governance/AGENT-GOVERNANCE.md")))

    def test_setup_and_foundation_recommend_secret_storage(self):
        self.assertIn("recommend moving them to an environment variable, keychain",
                      plain(read("skills/beginnerd-setup/SKILL.md")))
        foundation = plain(read("skills/beginnerd-foundation/SKILL.md"))
        self.assertIn("moving the secret to an environment variable or secret store", foundation)
        self.assertIn("include the safety baseline in references/agent-harness.md", foundation)

    def test_project_context_carries_safety_baseline(self):
        harness = plain(read("skills/beginnerd-foundation/references/agent-harness.md"))
        for phrase in ("safety baseline for project agent context",
                       "apply even when no beginnerd skill is loaded",
                       "never its value, even when it looks fake",
                       "do not open credential stores or dump whole harness configuration",
                       "including built-in harness memory tools",
                       "write code only for an approved task"):
            self.assertIn(phrase, harness)

    def test_scenario_fixes_and_new_case(self):
        cases = {x["id"]: x for x in json.loads(read("tests/behavioral/scenarios.json"))}
        self.assertIn("consistent with reval-31",
                      plain(" ".join(cases["REVAL-14-NO-GRANT-ONE-QUESTION"]["expected_behaviors"])))
        self.assertNotIn("cabut", " ".join(cases["REVAL-17-REVOKED-GRANT-STOPS-WRITES"]["turns"]))
        self.assertNotIn("(", cases["REVAL-29-LEVEL0-CRITICAL-SECURITY-DISCLOSED"]["prompt"])
        self.assertIn("no word such as fake", " ".join(cases["REVAL-35-SECRET-FOUND-NOT-ECHOED"]["prerequisites"]))
        r15 = cases["REVAL-15-GRANT-ACCEPTED-THEN-PRODUCT-WRITE"]["turns"]
        self.assertEqual(sum("sends verbatim" in t for t in r15), 2)
        new = cases["REVAL-36-PROJECT-CONTEXT-CARRIES-SAFETY-BASELINE"]
        self.assertEqual(new["execution_status"], "NOT_EXECUTED")

    def test_protocol_keeps_key_out_of_readable_config(self):
        readme = plain(read("tests/behavioral/README.md"))
        self.assertIn("so no readable configuration file holds it", readme)
        self.assertIn("text in parentheses inside `prompt` describes the fixture and is never sent", readme)


if __name__ == "__main__":
    unittest.main()
