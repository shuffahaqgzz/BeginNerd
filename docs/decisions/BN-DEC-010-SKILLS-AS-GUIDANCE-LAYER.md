# BN-DEC-010 — Skills as the Guidance Layer: Optimize Fully, Accept Model Variance

**Date:** 3 November 2026. **Status:** OWNER DECISION — APPROVED. Source changes in the PR that adds this record. Runtime behavior NOT VERIFIED.

## Context
Runs 4 to 8 of the issue #2 runtime evaluation (OMP 18.14.0 with DeepSeek V4.1 Flash; see docs/implementation/RUNTIME-EVAL-RUNS-4-7.md) showed a consistent pattern across five source remediations.

**What changed behavior:**
- Rules always present in context (the Project safety baseline in AGENTS.md) changed behavior strongly. The token was printed in 0 of 9 sessions with the baseline and 7 of 9 without it.
- Changes to the environment worked completely. The model key never appeared in a tool result once it moved to an environment variable.

**What skill text did not stop:**
- Run 7: harness configuration was read in 9 of 21 setup-related sessions.
- Run 8: the configuration canary appeared in 5 sessions, all before the setup skill's text reached the model.
- Run 8: one session called built-in memory recall after reading a memory-contract line that conflicted with the consent rule.

The Owner asked three questions:
1. Do skills determine an agent model's habits?
2. Is governance in skills pointless?
3. How do skills compare with plugins for rules a model must follow accurately?

## Findings presented to the Owner
- **Skills influence behavior but do not determine it.** A skill is text that the model chooses to load. In the progressive-disclosure pattern used by Claude and many compatible harnesses, only its name and description are always in context (loading varies by host), and loaded instructions are context, not enforced configuration. Adherence also falls as the number of instructions grows. Sources:
  - [Anthropic, Agent Skills](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills)
  - [Claude Code memory](https://code.claude.com/docs/en/memory)
  - [IFScale, arXiv:2507.11538](https://arxiv.org/abs/2507.11538)
- **Governance in skills is not pointless.** Rules that need judgment can live only in skills: what counts as scope approval, phase ownership, when to ask. Security invariants need enforcement outside the model. Sources:
  - [The Instruction Hierarchy, arXiv:2404.13208](https://arxiv.org/abs/2404.13208)
  - [CaMeL, arXiv:2503.18813](https://arxiv.org/abs/2503.18813)
- **A plugin is packaging.** A skill inside a plugin is still a skill. Deterministic control comes from hooks, permission rules or a sandbox, and only for what they can match mechanically ([Claude Code plugins](https://code.claude.com/docs/en/plugins); [Claude Code hooks](https://code.claude.com/docs/en/hooks-guide)).

## Decision
In the Owner's words: *"Dari main idea yang dibentuk untuk skills BeginNerd, lakukan optimalisasi penuh terhadap penggunaan skills walaupun perilaku model agent akan berbeda-beda. Selanjutnya, buat best-practice penggunaan dari skills BeginNerd ini dari awal sampai akhir. Buatkan siklus penggunaan untuk masing-masing use case Fase."*

Restated:
1. **Keep BeginNerd's main idea:** eight skills, six phases, Guided Building. Optimize how the skills are used and loaded as far as source text allows, and accept that behavior will differ between models and harnesses.
2. **Publish an end-to-end best-practice guide** for using BeginNerd.
3. **Publish a usage cycle for each phase.**

## What the optimization covers
- **Front-loaded safety.** Every SKILL.md now opens with the five-line Project safety baseline. Instructions placed early are followed more often, and the baseline is the text with the strongest runtime evidence.
- **Always-present text.**
  - The setup skill's description, which is in context before the skill loads, now states that discovery is name-only and never opens harness configuration or credential files.
  - The baseline lines name the exact run 8 failure routes:
    - configuration files opened through any tool;
    - a provider switched on in configuration being treated as consent;
    - revocation that does not stick.
- **No internal contradiction.** The memory contract no longer says to recall at session start whenever Hindsight "is enabled". "Enabled" now means the user chose the provider for this project in setup. A backend switched on in harness configuration is not consent.
- **Usage guidance in the package.** The per-phase cycles are packaged into beginnerd-ask and beginnerd-setup, so orientation can explain them in any installation.
- **Layered guidance for operators.** The best-practice guide tells users and operators which rules belong in skills, which in AGENTS.md and which in harness controls.

## Consequences and limits
- **Two kinds of status.** Criteria that need a guarantee are reported in two parts: the instruction status (source text and observed runtime behavior), and the **enforcement** status, which comes only from tested harness controls and is otherwise ENFORCEMENT NOT VERIFIED. These criteria are no forbidden configuration read and no provider contact without consent.
- **Skill text is not a closing fix for those two criteria.** A runtime pass of skill text alone will not be reported as proof that they cannot happen.
- **Runtime acceptance stays OPEN.** Harness enforcement for OMP is not implemented by this decision. Investigating OMP's tool-call controls remains a separate follow-up.
- **No new skill, phase or workflow is added.** The 32 workflow responsibilities are unchanged.
