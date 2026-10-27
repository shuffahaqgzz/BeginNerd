"""Documentation-level cross-harness checks, NOT a live install or runtime compatibility test."""
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
README = ROOT / "README.md"
GUIDE = ROOT / "docs/setup/MULTI-HARNESS-ADOPTION.md"
SKILLS = (
    "beginnerd-ask", "beginnerd-setup", "beginnerd-product",
    "beginnerd-solution", "beginnerd-plan", "beginnerd-foundation",
    "beginnerd-implement", "beginnerd-release",
)
AGENTS = ("claude-code", "codex", "cursor", "opencode", "hermes-agent")


class MultiHarnessDocumentationTests(unittest.TestCase):
    def test_readme_leads_with_portable_approach_and_original_tagline(self):
        text = README.read_text(encoding="utf-8")
        self.assertIn("Start with a vibe. Build with a plan. Learn along the way.", text)
        self.assertIn("Agent Skills", text)
        self.assertIn("MULTI-HARNESS-ADOPTION.md", text)
        self.assertNotIn("Pakai **Codex**?", text)
        for name in SKILLS:
            with self.subTest(name=name):
                self.assertIn("skills/" + name + "/SKILL.md", text)
                self.assertTrue((ROOT / "skills" / name / "SKILL.md").is_file())

    def test_supported_cli_ids_and_hermes_native_are_documented(self):
        guide = GUIDE.read_text(encoding="utf-8")
        readme = README.read_text(encoding="utf-8")
        for name in AGENTS:
            with self.subTest(agent=name):
                self.assertIn("-a " + name, guide)
                self.assertIn("-a " + name, readme)
        self.assertIn("hermes skills tap add shuffahaqgzz/BeginNerd", guide)
        self.assertIn("hermes skills trust", guide)
        self.assertIn("hermes skills install shuffahaqgzz/BeginNerd/beginnerd-ask", guide)

    def test_no_false_cross_harness_runtime_claim(self):
        guide = GUIDE.read_text(encoding="utf-8")
        quickstart = (ROOT / "docs/setup/QUICKSTART.md").read_text(encoding="utf-8")
        self.assertIn("not a platform restriction", guide)
        self.assertIn("not Codex-only", quickstart)
        self.assertIn("not proof of actual BeginNerd workflow execution", guide)
        self.assertIn("runtime acceptance", guide)
        self.assertIn("project-scoped", guide)
        self.assertIn("Graphify", guide)
        self.assertIn("Hindsight", guide)


if __name__ == "__main__":
    unittest.main()
