# Changelog

All notable source changes are recorded with Git history and Pull Requests. This file avoids suggesting an unshipped runtime release.

## Unreleased — phase-bounded continuation (source merged via PR #16, 30 October 2026)
- Clarifies Agent Governance: a generic "lanjut" or "ikut rekomendasi" approves only the described next step of the current phase and never passes an unseen lifecycle approval point; an early grant proposal does not bundle immediate code; one combined stop after the Product draft only for still-unapproved material decisions; one explicit approval may cover several described decisions, but coding requires an approved Planning task, design decisions, satisfied dependencies and execution authorization.
- REVAL-31 to REVAL-34 added (REVAL-34 negative: coding request before prerequisites) as definitions only (NOT EXECUTED). Source and offline contract validation only; runtime behavior unverified.

## Unreleased — adaptive first-use guidance, BN-DEC-003 revised (source merged via PR #15, 30 October 2026)
- Owner decision: ACCEPT DESIGN DIRECTION — CHANGES REQUIRED (FC-01–FC-09). BN-DEC-003's first-use guidance-mode choice is superseded, with the original approval kept in the register.
- New canonical contract docs/governance/FAMILIARITY-GUIDANCE-CONTRACT.md, generated into references/familiarity-check.md of all eight skills (7 canonical sources, 46 portable copies), so each standalone skill adapts without another package.
- Help first; provisional level from context or supportive Level 0; familiarity questions zero by default, one when needed, at most three; guidance style derived from the level; explicit override and topic-specific adaptation.
- Familiarity never changes authorization, security, ownership or verification; the guidance preference is minimal, project-scoped and separate from the workspace grant; Graphify/Hindsight are not promoted in a beginner's first reply unless requested.
- SETUP-01 and REVAL-13 synchronized; REVAL-21–30 added as definitions only (NOT EXECUTED). Source and offline contract validation only; runtime behavior unverified.

## Unreleased — post-merge security and workspace grant hardening (28 October 2026)
- Narrow optional read-only hook to explicit project-root regular-file Read and direct-file Grep; reject recursive searches, glob bypass, symlinks, sensitive paths and unsupported tools by default.
- Introduce one-time Scoped Workspace Grant to reuse approved safe local actions across lifecycle skills without repeated file prompts or new privileges.
- Add negative and multi-turn novice acceptance fixtures, clarify conditional provider tests, correct status history and remove machine-specific absolute reviewer evidence paths.
- This is source and offline contract hardening only; new behavioral cases, live harness enforcement and full framework E2E remain NOT EXECUTED.

## Unreleased — beginner evaluation adaptation (28 October 2026)
- Owner-authorized one-PR source hardening after the 27 October blinded beginner review: scoped GREEN/YELLOW/RED permissions, named batch delegation, first useful result and authorized task continuity.
- Updated eight skill entry points, relevant workflow references, plain-language templates and historical Graphify/Hindsight decision provenance without adding workflows.
- Added credential/login security guidance, inactive host recommendation/deployment preparation and regression scenario definitions.
- Reviewer statistics and new behavioral cases remain **reported/unexecuted** respectively until independent fresh-harness validation; no v1.0 runtime or deployment claim.


## Unreleased — source candidates (27 October 2026)
- Approved design baseline: six lifecycle phases, 32 workflow responsibilities, two companion skills.
- Phase 1 Product source and governance hardening via PR #4/#5/#6. Runtime acceptance remains PARTIAL.
- Scoped H02-03 source remediation and evidence-status corrections merged through PR #7 (source only; runtime retest pending).
- Phase 2–6 portable source candidates, references, templates, static/offline contract tests and release/operations governance merged through PR #9 (not runtime-accepted).
- MIT LICENSE, contribution guide and publication checklist integrated through PR #8; copyright-holder and third-party obligations still require review before validated v1.0 release.
- No v1.0 tag, runtime E2E PASS, deployment or release is claimed here.

## Release notes policy
Only add a versioned entry after Owner authorizes a release and verified artifact SHA, documented changes, expected environment, QA/behavioral/e2e evidence, known limitations and license compliance exist. Source commits/PR merges alone do not constitute a product release.
