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

    def test_scoped_workspace_grant_reuse_and_separate_owners(self):
        policy = read("docs/governance/AGENT-GOVERNANCE.md").lower().replace("**", "")
        for phrase in ("one-time scoped workspace grant", "project-root",
                       "existing project state", "reused across product",
                       "never permits destructive", "approved task"):
            self.assertIn(phrase, policy)
        setup = read("skills/beginnerd-setup/SKILL.md").lower()
        product = read("skills/beginnerd-product/SKILL.md").lower()
        plan = read("skills/beginnerd-plan/SKILL.md").lower()
        implement = read("skills/beginnerd-implement/SKILL.md").lower()
        self.assertIn("one bounded workspace grant", setup)
        self.assertIn("document grant", product)
        self.assertIn("planning does not code", plan)
        self.assertIn("both permit", implement)
        for name in ("beginnerd-ask", "beginnerd-setup", "beginnerd-product",
                     "beginnerd-solution", "beginnerd-plan", "beginnerd-foundation",
                     "beginnerd-implement", "beginnerd-release"):
            ref = read(f"skills/{name}/references/agent-governance.md").lower()
            self.assertIn("one-time scoped workspace grant", ref)

    def test_merged_source_status_and_public_docs_are_reconciled(self):
        status = read("docs/implementation/STATUS.md")
        self.assertIn("PR #12 MERGED", status)
        self.assertIn("PR #13 MERGED", status)
        self.assertIn("8e9272d", status)
        self.assertNotIn("proposed PR branch", status.lower())
        validation = read("docs/implementation/VALIDATION-PLAN.md")
        self.assertNotIn("/home/infra/beginnerd-review", validation)
        e2e = read("docs/implementation/REAL-WORLD-E2E-VALIDATION.md")
        self.assertIn("opt-in only", e2e.lower())
        checklist = read("docs/implementation/FRAMEWORK-RELEASE-CHECKLIST.md")
        self.assertIn("otherwise N/A", checklist)
        self.assertIn("NOT EXECUTED", status)

    def test_novice_grant_transition_cases_require_real_execution(self):
        cases = json.loads(read("tests/behavioral/scenarios.json"))
        selected = [x for x in cases if x["id"].startswith("REVAL-") and
                    int(x["id"].split("-")[1]) >= 14]
        self.assertEqual(len(selected), 7)
        self.assertTrue(all(x["execution_status"] == "NOT_EXECUTED" for x in selected))
        for name in ("REVAL-14-NO-GRANT-ONE-QUESTION",
                     "REVAL-15-GRANT-ACCEPTED-THEN-PRODUCT-WRITE",
                     "REVAL-16-PRODUCT-PLAN-IMPLEMENT-GRANT-CONTINUITY"):
            case = next(x for x in selected if x["id"] == name)
            self.assertGreaterEqual(len(case["turns"]), 2)
            self.assertTrue(case["must_not"] and case["expected_behaviors"])

    def test_review_scenarios_are_new_definitions_not_executed(self):
        cases = json.loads(read("tests/behavioral/scenarios.json"))
        review = [x for x in cases if x["id"].startswith("REVAL-")]
        self.assertGreaterEqual(len(review), 13)
        self.assertTrue(all(x["execution_status"] == "NOT_EXECUTED" for x in review))
        self.assertEqual(len({x["id"] for x in cases}), len(cases))
        self.assertTrue(all(x["execution_status"] == "NOT_EXECUTED" for x in cases))


if __name__ == "__main__":
    unittest.main()
