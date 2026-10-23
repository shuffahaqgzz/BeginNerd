"""Checks for portable companion packages. These are STATIC tests, not runtime evals."""
import json
import shutil
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

from scripts.build_portable_references import synchronize, SOURCES
from scripts.validate_skill_packages import validate, validate_skill, check_references


class SkillPortabilityTests(unittest.TestCase):
    def test_generated_references_are_current(self):
        self.assertEqual(synchronize(check=True), [])

    def test_exactly_three_distributable_skills(self):
        self.assertEqual(validate(), [])

    def test_canonical_sources_have_portable_copies(self):
        self.assertEqual(len(SOURCES), 5)
        self.assertEqual(sum(len(paths) for paths in SOURCES.values()), 9)

    def test_standalone_copy_needs_no_repository_docs(self):
        for name in ("beginnerd-ask", "beginnerd-setup", "beginnerd-product"):
            with self.subTest(skill=name), tempfile.TemporaryDirectory() as folder:
                portable = Path(folder) / name
                shutil.copytree(ROOT / "skills" / name, portable)
                self.assertEqual(validate_skill(portable), [])

    def test_missing_packaged_governance_detected(self):
        with tempfile.TemporaryDirectory() as folder:
            portable = Path(folder) / "beginnerd-ask"
            shutil.copytree(ROOT / "skills" / "beginnerd-ask", portable)
            (portable / "references" / "agent-governance.md").unlink()
            self.assertTrue(any("missing packaged resource" in x for x in check_references(portable)))

    def test_bad_name_detected(self):
        with tempfile.TemporaryDirectory() as folder:
            portable = Path(folder) / "beginnerd-setup"
            shutil.copytree(ROOT / "skills" / "beginnerd-setup", portable)
            md = portable / "SKILL.md"
            md.write_text(md.read_text(encoding="utf-8").replace("name: beginnerd-setup", "name: BeginNerd--Setup", 1), encoding="utf-8")
            self.assertTrue(any("invalid/mismatched name" in x for x in validate_skill(portable)))

    def test_activation_cases_not_executed(self):
        data = json.loads((ROOT / "tests" / "activation" / "queries.json").read_text(encoding="utf-8"))
        self.assertGreaterEqual(len(data), 12)
        self.assertTrue(all(x["execution_status"] == "NOT_EXECUTED" for x in data))
        self.assertEqual({x["skill"] for x in data}, {"beginnerd-ask", "beginnerd-setup", "beginnerd-product"})


if __name__ == "__main__":
    unittest.main()
