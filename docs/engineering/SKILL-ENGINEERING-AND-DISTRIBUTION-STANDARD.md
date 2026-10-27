# BeginNerd — Agent Skills Engineering and Distribution Standard

**Status:** Approved source-engineering baseline, updated after Owner-reviewed T1–T7 improvements. The framework still needs independent runtime acceptance.

## What to follow
1. [Agent Skills specification](https://agentskills.io/specification): portable SKILL.md metadata, progressive disclosure and references.
2. [Agent Skills authoring and evaluation](https://agentskills.io/skill-creation/best-practices): clear triggers, compact entry points and with/without-skill tests.
3. [Matt Pocock's skill collection](https://github.com/mattpocock/skills): inspiration for practical, composable workflows—not BeginNerd governance authority.
4. BeginNerd's [approved architecture](../architecture/FRAMEWORK-ARCHITECTURE.md), [workflow registry](../workflows/WORKFLOW-REGISTRY.md) and [Owner decisions](../decisions/REVIEW-T1-T7-OWNER-DECISIONS.md).

## Authoring standards
- Every installable skill lives under skills/<name>/SKILL.md. The file starts with valid YAML frontmatter containing exact `name` and meaningful native-English `description`.
- Use short entry points; load supporting references only when relevant. Aim below 500 lines and 5,000 tokens per entry point (guidance, not a formal limit).
- Source instructions and canonical documents use **native English**. User-visible replies follow the user's preferred language, with internal tracking IDs and issue codes omitted unless technically necessary or requested.
- Stable workflow IDs use the **full words** of their phase names, such as PRODUCT-FOUNDATION-01 and IMPLEMENTATION-01. Historical aliases remain documented at docs/workflows/WORKFLOW-ID-MIGRATION.md.
- Preserve internal acceptance, source, security and permission details in references/technical records, not conversational jargon.
- Eight skills are the approved inventory: two companions and six lifecycle entry points. Do not add a new skill/workflow for research, effectiveness or governance.
- Guidance must remain adaptive: a small bug fix should not trigger the entire product lifecycle. Material approvals should be risk-tiered, and routine authorized technical steps should not restart Planning.

## Portable packages and duplicate references
Skills CLI often copies a **single skill folder** without the root canonical docs. Every package therefore contains the self-contained references it needs. The six canonical sources synchronized by scripts/build_portable_references.py produce **38 generated snapshots**, with Git blob provenance.

The canonical sources remain authoritative: docs/governance/AGENT-GOVERNANCE.md, docs/governance/MEMORY-KNOWLEDGE-CONTRACT.md, docs/governance/WORK-STRUCTURE-POLICY.md, docs/governance/RESEARCH-REUSE-POLICY.md, docs/architecture/ARTIFACT-AND-READINESS-CONTRACT.md and docs/workflows/WORKFLOW-REGISTRY.md.

After changing a canonical source, run `python3 scripts/build_portable_references.py --write`, inspect the generated diff, then run `--check`. Never hand-edit generated snapshots or make standalone skills depend on ../../docs at runtime.

## Optional provider integrations
Graphify (knowledge) and Hindsight (persistent memory) are opt-in choices during beginnerd-setup. Do not require them for ordinary use of any lifecycle skill. If enabled, verify real project-scoped operations, consent, isolation and acknowledgement; if disabled, rely on canonical project files without reporting a failure. A skill file must not silently install or configure an external provider.

## Validation layers — keep claims separate
| Layer | Evidence | What it cannot prove |
|---|---|---|
| Source/static | scripts/validate_repository.py, scripts/validate_skill_packages.py and CI | Agent routing or user experience |
| Portable parity | build_portable_references.py --check, isolated package checks | Live installation or correct provider permissions |
| Upstream format | Verified official Agent Skills validator where available | Security certification |
| Discovery | Actual Skills CLI or native harness enumeration | Correct activation |
| Activation | Positive, negative and bilingual prompts with per-case evidence | Correct execution/permission enforcement |
| Behavior | Safe tool traces, user-facing clarity, no unauthorized attempted action | Every possible runtime or provider integration |
| Effectiveness | Observed tasks, user outcomes, friction and error/rework measures | A universal product success guarantee |
| Provider | Consented Graphify/Hindsight isolated operations | Safety of unrelated tools |
| Release | Real authorization, deploy smoke, rollback and operations evidence | Permission to label untested areas PASS |

Source cases in tests/activation/queries.json and tests/behavioral/scenarios.json are **NOT_EXECUTED** until real case-specific runs are reconciled. Static tests do not establish runtime pass. Read-only contract diagnostics do not enforce external provider permissions.

## Multi-harness compatibility and permission enforcement
- Supported source format targets Claude Code, Codex, Cursor, OpenCode, Hermes Agent and other Agent Skills-compatible harnesses. Consult [multi-harness adoption](../setup/MULTI-HARNESS-ADOPTION.md).
- Harness security requires actual native permissions, hooks, sandbox policies or provider allowlists. See docs/security/HARNESS-ACTION-GATES.md. Never automatically write global configuration or install hook samples.
- Test external-mutation refusals through isolated denied/mocked tools, not live creation of a private Site. A denied attempted forbidden action is still a **behavioral failure**.
- Keep exact skill source revision, authorization and before/after evidence. When outcome metrics are absent, say so.

## Distribution
No dedicated BeginNerd npm installer is required. First inspect existing installed skills; use Skills CLI or native harness installation once, prefer isolated project scope, verify updates and rollback, and prevent duplicate copies of the same skill.

Do not add auto-update installers, new provider dependencies, mandatory marketplaces or release tags just for appearances. Release/version claims remain linked to real acceptance and Owner authorization.
