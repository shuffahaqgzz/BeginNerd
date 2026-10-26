"""H-01 STATIC guardrail checks; do not confuse with agent runtime enforcement."""
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def content(path):
    return (ROOT / path).read_text(encoding="utf-8")


class H01GovernanceStaticTests(unittest.TestCase):
    def test_canonical_authorization_matrix_and_secrets(self):
        policy = content("docs/governance/AGENT-GOVERNANCE.md")
        for phrase in ("LOCAL_WRITE", "EXTERNAL_CREATE", "DEPLOY_RELEASE",
                       "SECRET_ADMIN", "private", "delegation is not unlimited authorization"):
            self.assertIn(phrase.lower(), policy.lower())
        self.assertIn("never repeat its value", policy)

    def test_routing_rejects_tool_substitution(self):
        routing = content("skills/beginnerd-ask/references/routing.md")
        for phrase in ("beginnerd-implement", "beginnerd-release",
                       "Sites", "not installed", "deployment"):
            self.assertIn(phrase, routing)
        self.assertIn("do not substitute", routing)

    def test_portable_skills_cover_general_delegation_and_provider_boundary(self):
        for skill in ("beginnerd-ask", "beginnerd-product", "beginnerd-setup"):
            with self.subTest(skill=skill):
                text = content(f"skills/{skill}/SKILL.md")
                self.assertIn("Sites", text)
                self.assertIn("approval", text.lower())
        self.assertIn("remote plugin permissions", content("skills/beginnerd-setup/SKILL.md"))

    def test_canonical_reference_provenance_is_generated(self):
        policy = content("docs/governance/AGENT-GOVERNANCE.md")
        self.assertIn("Runtime enforcement and fast-track", policy)
        from scripts.build_portable_references import synchronize
        self.assertEqual(synchronize(check=True), [])

    def test_six_adversarial_scenarios_are_planned_not_claimed_executed(self):
        cases = json.loads(content("tests/behavioral/scenarios.json"))
        h = {x["id"]: x for x in cases if x["id"].startswith("H01-")}
        self.assertEqual(set(h), {f"H01-{n:02d}" for n in range(1, 7)})
        self.assertTrue(all(x["execution_status"] == "NOT_EXECUTED" for x in h.values()))
        self.assertTrue(all(x["must_not"] and x["expected_behaviors"] for x in h.values()))

    def test_beginner_activation_cases_have_positive_and_negative(self):
        q = json.loads(content("tests/activation/queries.json"))
        ids = {x["id"] for x in q}
        self.assertTrue({"ACT-ASK-09", "ACT-ASK-10", "ACT-PRODUCT-11", "ACT-PRODUCT-12"} <= ids)
        self.assertTrue(all(x["execution_status"] == "NOT_EXECUTED" for x in q))

    def test_runtime_plan_does_not_claim_success_or_live_deploy(self):
        p = content("docs/implementation/H01-RUNTIME-HARDENING.md")
        self.assertIn("NOT EXECUTED", p)
        self.assertIn("mock", p.lower())
        self.assertIn("provider", p.lower())
        self.assertIn("unauthorized mutation", p)


if __name__ == "__main__":
    unittest.main()
