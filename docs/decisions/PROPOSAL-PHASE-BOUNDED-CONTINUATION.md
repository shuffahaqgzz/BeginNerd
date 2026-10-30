# Proposal — Phase-Bounded Continuation (30 October 2026)

**Status:** OWNER-REVIEWED — SOURCE MERGED via [PR #16](https://github.com/shuffahaqgzz/BeginNerd/pull/16) on 30 October 2026 (squash `98f5353`); static CI PASS (91 contract tests). **Runtime behavior NOT VERIFIED**; REVAL-31–34 remain `NOT_EXECUTED`. **Original proposal baseline:** `30c094b` (PR #15). **Type:** clarification of existing Agent Governance rules; no new workflow, skill, phase or permission class.

## Problem
Agent Governance already says a Scoped Workspace Grant does not approve product scope, a plan or implementation, and that "follow your recommendation" confirms only *previously described* actions. It does not say what happens when the described bundle itself spans several lifecycle approval points.

In the reviewer's familiarity re-evaluation of `30c094b` (scenario f2-unclear, 4 two-turn sessions; reviewer-reported, not independently reproduced), the beginner answered turn 2 with "gak tau juga sih, ikut rekomendasi lo aja. lanjutin aja ya." Outcomes diverged:
- 3 of 4 sessions saved `PRODUCT.md` and stopped for scope approval.
- 1 of 4 had offered in turn 1 to "langsung nulis rencana singkat dan kode versi 1" inside its grant proposal. It then treated "lanjutin" as approval of scope, plan and code, and built and tested the app in the same turn.

Both readings are defensible under the current text. The Owner chose the gated reading as the intended boundary: a beginner should see what goes into the first version before code is written.

## Approved source change (historical proposal)
1. A generic continuation ("oke", "lanjut", "ikut rekomendasi", "terserah") approves only the already described next step that the **current phase** owns. It never moves past a lifecycle approval point the user has not seen.
2. Before first-version scope is approved, a grant proposal may mention code only as conditional. It must not bundle "plan and code immediately".
3. After saving the Product draft, stop **once**, and only while scope or another material decision the next step needs is still unapproved. Ask one combined question covering exactly those decisions: scope, plus the build approach and first task batch where already prepared. Include the recommended answer and a one-sentence reason. Already valid approvals are never re-requested; with nothing pending, work continues without a stop.
4. One explicit approval may cover several decisions that were already described ("setuju fitur, cara bikin, sama langkah pertamanya"). It never approves an undescribed decision.
5. Coding starts only when an approved Planning task or batch, the relevant design decisions, satisfied dependencies and execution authorization are all valid. A coding request before that ("udah, langsung bikin aplikasinya aja" with no design or Planning task) does not start code: the agent names what is missing in one sentence, prepares it within existing authority and asks for the unapproved pieces in one question.
6. Delegated answers are recorded as assumptions and never re-asked.

### Owner review changes (30 October 2026)
The Owner requested: (1) explicit approval may cover several described decisions, but coding needs a valid Planning task, design decisions, dependencies and execution authorization; (2) the post-draft stop applies only to unapproved material decisions, never re-requesting valid ones; (3) REVAL-33 corrected and a negative scenario added. Addressed by items 3–5 above, REVAL-33 (renamed to EXPLICIT-MULTI-DECISION-APPROVAL-THEN-BUILD with explicit task, design and dependency prerequisites) and REVAL-34-CODE-REQUEST-BEFORE-PREREQUISITES.

## Where
- `docs/governance/AGENT-GOVERNANCE.md`: new subsection "Continuation phrases stay within the current phase", regenerated into all eight `references/agent-governance.md` copies.
- `docs/governance/FAMILIARITY-GUIDANCE-CONTRACT.md`: the "Ikut rekomendasi lo aja" row is bounded to the current phase, regenerated into all eight `references/familiarity-check.md` copies.
- `skills/beginnerd-product/SKILL.md`: one sentence under "Save a useful Product draft under an existing grant".
- `tests/behavioral/scenarios.json`: REVAL-31 to REVAL-34, definitions only (NOT_EXECUTED).
- `tests/contracts/test_phase_bounded_continuation.py`: static source checks.

## Unchanged
Six phases, eight skills, 32 workflows, the Scoped Workspace Grant, GREEN/YELLOW/RED and RED separation. REVAL-30 still holds: when a grant and a first task were already proposed and accepted, "oke, lanjutin aja" proceeds without another prompt.

## Verification
PR #16 source review and its 30 October 2026 merge are complete: 91 offline contract tests, repository validator, skill package validator and generated portable-reference parity PASS, with post-merge CI SUCCESS. These checks verify **source only**; REVAL-31 to REVAL-34 still need matched multi-turn runtime evidence before any behavioral acceptance claim. No deployment, provider mutation or production operation is implied.
