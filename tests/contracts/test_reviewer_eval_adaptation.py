"""Static reviewer-adaptation source checks; these are NOT runtime acceptance."""
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


class ReviewerEvaluationAdaptationTests(unittest.TestCase):
    def test_bounded_lights_do_not_grant_blanket_writes(self):
        policy = read("docs/governance/AGENT-GOVERNANCE.md")
        for phrase in ("GREEN", "YELLOW", "RED", "scoped LOCAL_WRITE", "already authorized",
                       "local destructive", "maximum two attempts", "approved plan"):
            self.assertIn(phrase.lower(), policy.lower(), phrase)
        self.assertIn("a local action is not automatically safe", policy.lower())
        self.assertIn("previously described", policy.lower())
        self.assertIn("separate", policy.lower())

    def test_no_extra_lifecycle_ownership_or_plan_autorun(self):
        plan = read("skills/beginnerd-plan/SKILL.md")
        implement = read("skills/beginnerd-implement/SKILL.md")
        product = read("skills/beginnerd-product/SKILL.md")
        for phrase in ("Planning does not code", "approved plan", "execution authorization"):
            self.assertIn(phrase.lower(), plan.lower())
        for phrase in ("continue approved", "maximum two", "stored password hashing", "formal tasks"):
            self.assertIn(phrase.lower(), implement.lower())
        for phrase in ("prototype", "actual application code", "Planning"):
            self.assertIn(phrase.lower(), product.lower())

    def test_first_use_and_prelaunch_keep_separate_permissions(self):
        ask = read("skills/beginnerd-ask/SKILL.md")
        setup = read("skills/beginnerd-setup/SKILL.md")
        release = read("skills/beginnerd-release/SKILL.md")
        self.assertIn("first useful result", ask.lower())
        self.assertIn("guidance preference", setup.lower())
        self.assertIn("one evidence-supported", release.lower())
        self.assertIn("separate", release.lower())
        self.assertIn("no live", release.lower())

    def test_user_facing_primary_templates_and_technical_appendices(self):
        primary = (
            "skills/beginnerd-product/assets/product-lean-template.md",
            "skills/beginnerd-product/assets/product-brief-template.md",
            "skills/beginnerd-product/assets/product-requirements-template.md",
            "skills/beginnerd-product/assets/mvp-scope-template.md",
            "skills/beginnerd-product/assets/technical-requirements-template.md",
            "skills/beginnerd-solution/assets/solution-blueprint-template.md",
            "skills/beginnerd-plan/assets/development-plan-template.md",
            "skills/beginnerd-release/assets/release-plan-template.md",
        )
        for name in primary:
            with self.subTest(name=name):
                body = read(name)
                self.assertIn("## Plain-language summary", body)
                self.assertIn("## Technical appendix", body)
                self.assertLess(body.index("## Plain-language summary"),
                                body.index("## Technical appendix"))
                self.assertNotIn("Status:** APPROVED", body)

    def test_credentials_and_provider_opt_in_provenance(self):
        security = read("skills/beginnerd-solution/references/security-architecture.md")
        self.assertIn("password hashing", security.lower())
        self.assertIn("plaintext", security.lower())
        decisions = read("docs/decisions/DECISION-REGISTER.md")
        self.assertIn("SUPERSEDED FOR DEFAULT ONBOARDING", decisions)
        self.assertIn("optional, opt-in", decisions)
        self.assertIn("not", read("docs/implementation/STATUS.md").lower())

    def test_review_scenarios_are_new_definitions_not_executed(self):
        cases = json.loads(read("tests/behavioral/scenarios.json"))
        review = [x for x in cases if x["id"].startswith("REVAL-")]
        self.assertGreaterEqual(len(review), 13)
        self.assertTrue(all(x["execution_status"] == "NOT_EXECUTED" for x in review))
        self.assertEqual(len({x["id"] for x in cases}), len(cases))
        self.assertTrue(all(x["execution_status"] == "NOT_EXECUTED" for x in cases))


if __name__ == "__main__":
    unittest.main()
