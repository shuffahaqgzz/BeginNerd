"""H-02/H-03 offline checks only; runtime behaviors still require actual agent sessions."""
import json
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
from scripts.validate_phase1_artifact import validate
from scripts.audit_workspace_manifest import snapshot, compare

SAMPLE = """# Synthetic PRODUCT — testing only
**Status:** DRAFT
| ID | Need | Acceptance |
|---|---|---|
| REQUIREMENTS-001 | Store link | ACCEPTANCE-CRITERIA-001 |
| REQUIREMENTS-002 | Private data | ACCEPTANCE-CRITERIA-002 |
| ID | Verification |
|---|---|
| ACCEPTANCE-CRITERIA-001 | Save is observed |
| ACCEPTANCE-CRITERIA-002 | Unauthorized read denied |
| ID | Product link | Technical constraint | Planned verification |
|---|---|---|---|
| TECHNICAL-REQUIREMENTS-001 | REQUIREMENTS-002 | Access denied | Try unauthenticated read (PLANNED) |
## Proposal — belum disetujui
PROPOSAL-001 — Additional feature, PROPOSED
## Product Readiness
G1: PARTIAL
"""


class Phase1HardeningContractTests(unittest.TestCase):
    def test_synthetic_valid_traceability_is_static_pass(self):
        issues, counts = validate(SAMPLE)
        self.assertEqual(issues, [])
        self.assertEqual(counts, {"requirements": 2, "acceptance": 2,
                                  "technical": 1, "g1": "PARTIAL"})

    def test_duplicate_and_orphaned_ids_are_rejected(self):
        corrupt = SAMPLE.replace("| REQUIREMENTS-002 | Private data | ACCEPTANCE-CRITERIA-002 |",
                                 "| REQUIREMENTS-001 | Private data | TBD |")
        issues, _ = validate(corrupt)
        self.assertTrue(any("duplicate req" in x for x in issues))
        self.assertTrue(any("not linked" in x for x in issues))

    def test_unknown_cross_references_are_rejected(self):
        issues, _ = validate(SAMPLE.replace("TECHNICAL-REQUIREMENTS-001 | REQUIREMENTS-002",
                                            "TECHNICAL-REQUIREMENTS-001 | REQUIREMENTS-999"))
        self.assertTrue(any("unknown product requirement" in x for x in issues))

    def test_approval_provenance_is_not_conjured(self):
        issues, _ = validate(SAMPLE.replace("**Status:** DRAFT", "**Status:** APPROVED"))
        self.assertTrue(any("approval provenance" in x for x in issues))

    def test_missing_g1_status_cannot_appear_passed(self):
        issues, _ = validate(SAMPLE.replace("G1: PARTIAL", "product ready"))
        self.assertTrue(any("G1" in x for x in issues))

    def test_workspace_manifest_catches_ignored_or_untracked_mutation(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            (root / ".beginnerd").mkdir()
            target = root / ".beginnerd" / "hidden.txt"
            target.write_text("first")
            before = snapshot(root)
            target.write_text("changed")
            after = snapshot(root)
            self.assertEqual(compare(before, after)["changed"], [".beginnerd/hidden.txt"])

    def test_workspace_manifest_tracks_additions_and_removals(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            p = root / "source.txt"
            p.write_text("x")
            before = snapshot(root)
            p.unlink()
            (root / "new.txt").write_text("z")
            changes = compare(before, snapshot(root))
            self.assertEqual(changes["removed"], ["source.txt"])
            self.assertEqual(changes["added"], ["new.txt"])

    def test_h02_h03_references_have_gaps_and_no_overclaim(self):
        technical = (ROOT / "skills/beginnerd-product/references/technical-requirements.md").read_text()
        control = (ROOT / "skills/beginnerd-product/references/documentation-and-change-control.md").read_text()
        for term in ("failure", "TBD", "Phase 2", "verification"):
            self.assertIn(term.lower(), technical.lower())
        for term in ("read back", "untracked", "before-and-after", "UNVERIFIED"):
            self.assertIn(term.lower(), control.lower())

    def test_hardening_behavioral_definitions_not_falsely_executed(self):
        data = json.loads((ROOT / "tests/behavioral/scenarios.json").read_text())
        expected = {f"H02-{i:02d}" for i in range(1, 4)} | {f"H03-{i:02d}" for i in range(1, 4)}
        cases = {x["id"]: x for x in data if x["id"] in expected}
        self.assertEqual(cases.keys(), expected)
        self.assertTrue(all(x["execution_status"] == "NOT_EXECUTED" for x in cases.values()))


if __name__ == "__main__":
    unittest.main()
