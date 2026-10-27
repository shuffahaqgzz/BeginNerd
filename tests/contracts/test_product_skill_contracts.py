"""Offline Product Foundation source contracts. No customer research or runtime is executed."""
import json
import shutil
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
from scripts.validate_skill_packages import validate_skill

PACKAGE = ROOT / "skills/beginnerd-product"
REFERENCES = (
    "product-discovery.md", "product-requirements.md", "mvp-definition.md",
    "technical-requirements.md", "g1-readiness.md", "documentation-and-change-control.md",
    "agent-governance.md", "memory-knowledge-contract.md", "research-reuse-policy.md",
    "artifact-readiness-contract.md",
)
ASSETS = (
    "product-lean-template.md", "product-brief-template.md", "product-requirements-template.md",
    "mvp-scope-template.md", "technical-requirements-template.md",
)


class ProductSkillStaticTests(unittest.TestCase):
    def test_standalone_package_validates(self):
        with tempfile.TemporaryDirectory() as tmp:
            target = Path(tmp) / "beginnerd-product"
            shutil.copytree(PACKAGE, target)
            self.assertEqual(validate_skill(target), [])

    def test_product_discovery_validation_and_linked_ownership(self):
        skill = (PACKAGE / "SKILL.md").read_text()
        discovery = (PACKAGE / "references/product-discovery.md").read_text()
        mvp = (PACKAGE / "references/mvp-definition.md").read_text()
        for num in range(1, 5):
            self.assertIn(f"PRODUCT-FOUNDATION-{num:02d}", skill)
        for name in REFERENCES:
            self.assertTrue((PACKAGE / "references" / name).is_file())
        for phrase in ("Jobs-to-be-Done", "non-leading", "hypothesis", "experiment", "competitor"):
            self.assertIn(phrase.lower(), discovery.lower())
        for phrase in ("learning", "PLANNED", "PRODUCT-FOUNDATION-01"):
            self.assertIn(phrase, mvp)
        self.assertNotIn("H-02/H-03 hardening", skill)
        self.assertNotIn("H02-03", skill)

    def test_templates_are_draft_not_artificially_approved(self):
        for name in ASSETS:
            with self.subTest(name=name):
                content = (PACKAGE / "assets" / name).read_text()
                self.assertIn("DRAFT", content)
                self.assertIn("PENDING", content)
                self.assertNotIn("**Status:** APPROVED", content)

    def test_traceability_and_approval_are_not_code_authorization(self):
        requirements = (PACKAGE / "references/product-requirements.md").read_text()
        technical = (PACKAGE / "references/technical-requirements.md").read_text()
        readiness = (PACKAGE / "references/g1-readiness.md").read_text()
        docs = (PACKAGE / "references/documentation-and-change-control.md").read_text()
        for term in ("REQUIREMENTS-001", "ACCEPTANCE-CRITERIA-001"):
            self.assertIn(term, requirements)
        for term in ("TECHNICAL-REQUIREMENTS-001", "REQUIREMENT_ID_PENDING",
                     "SECURITY_UNVERIFIED", "COST_UNVERIFIED", "Planned verification (NOT EXECUTED)"):
            self.assertIn(term, technical)
        for term in ("PASS", "PARTIAL", "BLOCKED", "approval"):
            self.assertIn(term.lower(), readiness.lower())
        for filename in ("PRODUCT.md", "PRODUCT-BRIEF.md", "PRODUCT-REQUIREMENTS-DOC.md",
                         "MINIMUM-VIABLE-PRODUCT-SCOPE.md", "TECHNICAL-REQUIREMENTS-DOC.md"):
            self.assertIn(filename, docs)
        self.assertIn("API-GUIDE.md", docs)

    def test_product_behavioral_scenarios_still_unexecuted(self):
        data = json.loads((ROOT / "tests/behavioral/scenarios.json").read_text())
        cases = [x for x in data if x["id"].startswith("PRODUCT-")]
        self.assertGreaterEqual(len(cases), 12)
        self.assertTrue(all(x["execution_status"] == "NOT_EXECUTED" for x in cases))

    def test_queued_activation_cases_still_unexecuted(self):
        data = json.loads((ROOT / "tests/activation/queries.json").read_text())
        subset = [x for x in data if x["skill"] == "beginnerd-product"]
        self.assertGreaterEqual(len(subset), 8)
        self.assertTrue(any(x["should_trigger"] for x in subset))
        self.assertTrue(any(not x["should_trigger"] for x in subset))
        self.assertTrue(all(x["execution_status"] == "NOT_EXECUTED" for x in subset))

    def test_reconciled_status_does_not_claim_runtime_pass(self):
        status = (ROOT / "docs/implementation/STATUS.md").read_text()
        self.assertIn("PARTIAL", status)
        self.assertIn("NOT EXECUTED", status)


if __name__ == "__main__":
    unittest.main()
