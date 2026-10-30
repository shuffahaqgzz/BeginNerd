# Proposal — Phase-Bounded Continuation (30 October 2026)

**Status:** Proposed; pending Owner decision, repository validation, CI and merge. Runtime behavior NOT VERIFIED. **Baseline:** `30c094b` (PR #15). **Type:** clarification of existing Agent Governance rules; no new workflow, skill, phase or permission class.

## Problem
Agent Governance already says a Scoped Workspace Grant does not approve product scope, a plan or implementation, and that "follow your recommendation" confirms only *previously described* actions. It does not say what happens when the described bundle itself spans several lifecycle approval points.

In the reviewer's familiarity re-evaluation of `30c094b` (scenario f2-unclear, 4 two-turn sessions; reviewer-reported, not independently reproduced), the beginner answered turn 2 with "gak tau juga sih, ikut rekomendasi lo aja. lanjutin aja ya." Outcomes diverged:
- 3 of 4 sessions saved `PRODUCT.md` and stopped for scope approval.
- 1 of 4 had offered in turn 1 to "langsung nulis rencana singkat dan kode versi 1" inside its grant proposal. It then treated "lanjutin" as approval of scope, plan and code, and built and tested the app in the same turn.

Both readings are defensible under the current text. The Owner chose the gated reading as the intended boundary: a beginner should see what goes into the first version before code is written.

## Proposed change
1. A generic continuation ("oke", "lanjut", "ikut rekomendasi", "terserah") approves only the already described next step that the **current phase** owns. It never moves past a lifecycle approval point the user has not seen.
2. Before first-version scope is approved, a grant proposal may mention code only as conditional. It must not bundle "plan and code immediately".
3. After saving the Product draft, stop **once** with one combined question: scope, plus the build approach and first task batch where already prepared. Include the recommended answer and a one-sentence reason. This keeps the gate to a single stop instead of serial approvals.
4. An explicit, specific instruction after the scope has been shown ("setuju fiturnya, langsung bikin aplikasinya") approves that bundle with no further stop.
5. Delegated answers are recorded as assumptions and never re-asked.

## Where
- `docs/governance/AGENT-GOVERNANCE.md`: new subsection "Continuation phrases stay within the current phase", regenerated into all eight `references/agent-governance.md` copies.
- `docs/governance/FAMILIARITY-GUIDANCE-CONTRACT.md`: the "Ikut rekomendasi lo aja" row is bounded to the current phase, regenerated into all eight `references/familiarity-check.md` copies.
- `skills/beginnerd-product/SKILL.md`: one sentence under "Save a useful Product draft under an existing grant".
- `tests/behavioral/scenarios.json`: REVAL-31 to REVAL-33, definitions only (NOT_EXECUTED).
- `tests/contracts/test_phase_bounded_continuation.py`: static source checks.

## Unchanged
Six phases, eight skills, 32 workflows, the Scoped Workspace Grant, GREEN/YELLOW/RED and RED separation. REVAL-30 still holds: when a grant and a first task were already proposed and accepted, "oke, lanjutin aja" proceeds without another prompt.

## Verification
Static contracts and portability tests only. REVAL-31 to REVAL-33 need a matched multi-turn runtime run before any behavioral claim.
