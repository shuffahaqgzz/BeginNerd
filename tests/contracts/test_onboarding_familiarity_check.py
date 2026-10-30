"""Static familiarity-guidance source checks (BN-DEC-003 revised); these are NOT runtime acceptance."""
import json
import re
import shutil
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

from scripts.validate_skill_packages import validate_skill

CONTRACT = "docs/governance/FAMILIARITY-GUIDANCE-CONTRACT.md"
ALL_SKILLS = ("beginnerd-ask", "beginnerd-setup", "beginnerd-product", "beginnerd-solution",
              "beginnerd-plan", "beginnerd-foundation", "beginnerd-implement", "beginnerd-release")
LIFECYCLE = ALL_SKILLS[2:]


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def plain(text: str) -> str:
    return re.sub(r"\s+", " ", text.replace("**", "")).lower()


class FamiliarityGuidanceContractTests(unittest.TestCase):
    def test_first_use_helps_before_optional_questions(self):
        contract = plain(read(CONTRACT))
        for phrase in ("provide the smallest useful, safe result",
                       "default to the supportive level 0",
                       "ask a familiarity question only if its answer would materially improve the next step",
                       "continue the requested workflow without requiring an answer",
                       "zero questions when the available information is enough",
                       "at most three", "don't know",
                       "never required to choose a guidance mode",
                       "does not limit clarification that safety, permission or a high-impact action requires"):
            self.assertIn(phrase, contract)

    def test_familiarity_never_grants_permission(self):
        contract = plain(read(CONTRACT))
        for phrase in ("never changes authorization, security, workflow ownership or verification",
                       "not how many authorized internal operations the agent performs",
                       "does not make the agent stop after one internal command",
                       "still needs separate release authorization",
                       "critical security or data risk is always disclosed",
                       "a guidance preference never permits a file write"):
            self.assertIn(phrase, contract)

    def test_adaptation_is_provisional_topic_specific_and_overridable(self):
        contract = plain(read(CONTRACT))
        for phrase in ("provisional level", "topic-specific adaptation", "explicit user override",
                       "takes precedence over inference",
                       "a topic signal, not a reason to change the overall level",
                       "do not use numerical confidence scoring"):
            self.assertIn(phrase, contract)

    def test_storage_is_minimal_and_separate_from_workspace_grant(self):
        contract = plain(read(CONTRACT))
        for phrase in ("without writing any file", "logically separate",
                       "minimal, project-scoped guidance preference",
                       "do not store raw questionnaire answers",
                       "view, change or delete",
                       "unless the user separately opted in"):
            self.assertIn(phrase, contract)

    def test_every_skill_packages_and_uses_the_contract_standalone(self):
        for name in ALL_SKILLS:
            with self.subTest(skill=name), tempfile.TemporaryDirectory() as folder:
                portable = Path(folder) / name
                shutil.copytree(ROOT / "skills" / name, portable)
                self.assertTrue((portable / "references" / "familiarity-check.md").is_file())
                self.assertIn("references/familiarity-check.md", (portable / "SKILL.md").read_text(encoding="utf-8"))
                self.assertEqual(validate_skill(portable), [])

    def test_lifecycle_skills_apply_in_place_without_permission_effect(self):
        for name in LIFECYCLE:
            with self.subTest(skill=name):
                text = plain(read(f"skills/{name}/SKILL.md"))
                self.assertIn("adapt to the user's familiarity", text)
                self.assertIn("do not send the user into a separate setup interview", text)
                self.assertIn("never changes permissions", text)
                self.assertIn("complete already authorized internal work", text)

    def test_no_instruction_still_requires_choosing_a_guidance_style(self):
        forbidden = ("ask for the user's guidance preference once",
                     "explain two guidance styles",
                     "ask the required one-time guidance preference",
                     "beginnerd-setup must still ask the guidance preference",
                     "can help choose a guidance style")
        files = [p for p in (ROOT / "skills").rglob("*.md")] + [ROOT / "README.md", ROOT / "docs/setup/QUICKSTART.md"]
        for path in files:
            text = plain(path.read_text(encoding="utf-8"))
            for phrase in forbidden:
                with self.subTest(file=str(path.relative_to(ROOT)), phrase=phrase):
                    self.assertNotIn(phrase, text)

    def test_providers_not_promoted_in_beginner_first_reply_but_honored_on_request(self):
        for path in (CONTRACT, "docs/governance/MEMORY-KNOWLEDGE-CONTRACT.md",
                     "skills/beginnerd-setup/references/onboarding.md"):
            with self.subTest(file=path):
                text = plain(read(path))
                self.assertIn("first reply", text)
        self.assertIn("immediately when the user asks", plain(read(CONTRACT)))

    def test_decision_register_supersedes_without_erasing_bn_dec_003(self):
        register = read("docs/decisions/DECISION-REGISTER.md")
        self.assertIn("BN-DEC-003 (historical) | Ask guidance preference at first use", register)
        self.assertIn("SUPERSEDED FOR FIRST-USE BEHAVIOR", register)
        self.assertIn("BN-DEC-003 revised", register)
        self.assertIn("SOURCE ACCEPTED — PR #15 MERGED", register)
        self.assertIn("RUNTIME NOT VERIFIED", register)

    def test_familiarity_scenarios_are_definitions_not_executed(self):
        cases = {x["id"]: x for x in json.loads(read("tests/behavioral/scenarios.json"))}
        names = ["SETUP-01", "REVAL-13-FIRST-VALUE-AND-PREFERENCE"] + [
            x for x in cases if re.match(r"REVAL-(2[1-9]|30)-", x)]
        self.assertEqual(len(names), 12)
        for name in names:
            with self.subTest(case=name):
                self.assertEqual(cases[name]["execution_status"], "NOT_EXECUTED")
        setup = " ".join(cases["SETUP-01"]["expected_behaviors"]).lower()
        self.assertNotIn("ask preference", setup)


if __name__ == "__main__":
    unittest.main()
