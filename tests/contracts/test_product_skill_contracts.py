"""Static contract validation for the Phase 1 Product Foundation skill candidate.

These tests inspect source packages/templates only; they do not run Codex, workflows,
G1 on a real product, or a knowledge/memory provider.
"""
import json
import shutil
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
from scripts.validate_skill_packages import validate_skill

PACKAGE = ROOT / "skills" / "beginnerd-product"
REFERENCES = (
    "product-discovery.md", "product-requirements.md", "mvp-definition.md",
    "technical-requirements.md", "g1-readiness.md", "documentation-and-change-control.md",
    "agent-governance.md", "memory-knowledge-contract.md", "research-reuse-policy.md",
    "artifact-readiness-contract.md",
)
ASSETS = (
    "product-lean-template.md", "product-brief-template.md",
    "product-requirements-template.md", "mvp-scope-template.md",
    "technical-requirements-template.md",
)
STRUCTURED = (
    "PRODUCT-BRIEF.md", "PRODUCT-REQUIREMENTS-DOC.md",
    "MINIMUM-VIABLE-PRODUCT-SCOPE.md", "TECHNICAL-REQUIREMENTS-DOC.md",
)


class ProductSkillStaticTests(unittest.TestCase):
    def test_product_skill_can_be_isolated(self):
        with tempfile.TemporaryDirectory() as td:
            target = Path(td) / "beginnerd-product"
            shutil.copytree(PACKAGE, target)
            self.assertEqual(validate_skill(target), [])

    def test_all_four_pf_and_g1_references_exist(self):
        for name in REFERENCES:
            with self.subTest(reference=name):
                self.assertTrue((PACKAGE / "references" / name).is_file())

    def test_templates_exist_and_remain_draft(self):
        for name in ASSETS:
            with self.subTest(asset=name):
                content = (PACKAGE / "assets" / name).read_text(encoding="utf-8")
                self.assertIn("DRAFT", content)
                self.assertIn("PENDING", content)
                self.assertNotIn("**Status:** APPROVED", content)

    def test_final_phase_one_filenames(self):
        reference = (PACKAGE / "references" / "documentation-and-change-control.md").read_text(encoding="utf-8")
        self.assertIn("PRODUCT.md", reference)
        for name in STRUCTURED:
            self.assertIn(name, reference)
        self.assertIn("proposal historis", reference)
        self.assertIn("API-GUIDE.md", reference)

    def test_traceability_and_approval(self):
        prd = (PACKAGE / "references" / "product-requirements.md").read_text(encoding="utf-8")
        technical = (PACKAGE / "references" / "technical-requirements.md").read_text(encoding="utf-8")
        g1 = (PACKAGE / "references" / "g1-readiness.md").read_text(encoding="utf-8")
        self.assertIn("REQUIREMENTS-001", prd)
        self.assertIn("ACCEPTANCE-CRITERIA-001", prd)
        self.assertIn("TECHNICAL-REQUIREMENTS-001", technical)
        self.assertIn("PASS", g1)
        self.assertIn("PARTIAL", g1)
        self.assertIn("BLOCKED", g1)
        self.assertIn("approval", g1.lower())

    def test_cross_phase_ownership(self):
        text = (PACKAGE / "SKILL.md").read_text(encoding="utf-8")
        self.assertIn("SOLUTION-06", text)
        self.assertIn("PLANNING-02", text)
        self.assertIn("No overclaim", text)

    def test_behavioral_scenarios_for_product_unexecuted(self):
        data = json.loads((ROOT / "tests" / "behavioral" / "scenarios.json").read_text(encoding="utf-8"))
        product = [item for item in data if item["id"].startswith("PRODUCT-")]
        self.assertGreaterEqual(len(product), 12)
        self.assertTrue(all(item["execution_status"] == "NOT_EXECUTED" for item in product))

    def test_positive_and_negative_activation_cases_unexecuted(self):
        data = json.loads((ROOT / "tests" / "activation" / "queries.json").read_text(encoding="utf-8"))
        product = [item for item in data if item["skill"] == "beginnerd-product"]
        self.assertGreaterEqual(len(product), 8)
        self.assertTrue(any(item["should_trigger"] for item in product))
        self.assertTrue(any(not item["should_trigger"] for item in product))
        self.assertTrue(all(item["execution_status"] == "NOT_EXECUTED" for item in product))

    def test_documentation_does_not_claim_runtime_product_pass(self):
        status = (ROOT / "docs" / "implementation" / "STATUS.md").read_text(encoding="utf-8")
        self.assertIn("IMPLEMENTATION CANDIDATE", status)
        self.assertIn("NOT VERIFIED", status)
        contract = (ROOT / "docs" / "implementation" / "PHASE-1-PRODUCT-IMPLEMENTATION-CONTRACT.md").read_text(encoding="utf-8")
        self.assertIn("BN-DEC-009.1", contract)
        self.assertIn("NOT EXECUTED", contract)


if __name__ == "__main__":
    unittest.main()
