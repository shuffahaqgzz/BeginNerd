# BeginNerd — Agent Operating Contract

Scope: all repository contributors and AI agents. This file is a repository guideline; approved user decisions, safety constraints, and scoped authorization remain controlling.

## Before work
1. Read README, docs/implementation/STATUS.md, the current approved decision register, and relevant contracts.
2. Inspect existing files and installed tooling. Reuse working configurations; do not silently duplicate or replace them.
3. State objective, work boundaries, source version, dependencies, acceptance criteria, and explicit write permission.
4. Distinguish approved framework DESIGN from verified implementation and executed tests.

## Decision ownership
- Product requirements and material scope: Phase 1.
- Solution, technology, security: Phase 2.
- Formal work packages, tasks, subtasks, and dependencies: PLANNING-02 (Phase 3).
- Environment baseline: Phase 4.
- Execute approved tasks and QA: Phase 5.
- Authorized release, deployment, incident and maintenance: Phase 6.
- beginnerd-ask: explain, recall, orient, and route; never usurp ownership.
- beginnerd-setup: onboarding, existing-state inspection, consented provider configuration, functional verification; not application scaffolding.

## Non-negotiable behavior
- Explain Before Execute; Contextual Learning.
- Research Before Build and Reuse Before Reinvent.
- Explain → Interview → Approve → Record for material decisions.
- No Overclaim; no claims of tests passed without execution evidence.
- No Overengineering and No Overrules.
- Do not create or decompose formal work units outside PLANNING-02.
- Respect least authority. No unapproved code, remote, provider, credential, or production mutations.
- Record gaps as PARTIAL, BLOCKED, UNVERIFIED, or MEMORY_SYNC_PENDING where appropriate.

## Failure & recovery
A corrective remediation attempt after a declared verification failure requires separately recorded user approval. Maximum two approved attempts per issue per execution baseline. If both fail: HOLD / REVIEW_REQUIRED, preserve evidence; no third automatic attempt, re-labeling, agent rotation, or bypass.

## Evidence & handoff
Preserve current status, source refs, authorization, requirement/task/test IDs, changed files, test command and actual result, open risks, and next action. Recall Hindsight at session start if authorized and reachable; verify against canonical sources. Retain meaningful changes and before handoff; never report memory saved unless provider confirms it.

## Git contribution
Use focused branches and PRs. Do not push directly to main after bootstrap, merge PRs, change repository settings, publish releases, or alter CI permissions without appropriate authorization. Never commit credentials or private knowledge/memory.

## Current reviewer-approved guidance
- All runtime instructions and canonical source documents use native English, while user-facing explanations follow the user's chosen language and avoid internal identifiers unless requested.
- Formal workflow IDs use full words; see docs/workflows/WORKFLOW-ID-MIGRATION.md for compatibility with previous IDs.
- Routine technical steps within authorized tasks do not require fresh approval or PLANNING-02 replanning. Only material scope/formal-task changes do.
- Graphify and Hindsight are opt-in choices made during beginnerd-setup; absence when declined is not a framework blocker.
- Source guardrails and offline validators are not a substitute for harness-side permission controls. Never claim permission-enforcement PASS from a passing static unit test.
