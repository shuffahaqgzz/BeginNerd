---
name: beginnerd-plan
description: Use this skill to develop a product delivery roadmap, brainstorm and approve proportionate formal work packages and tasks, create a risk-based testing strategy, manage documentation changes, and assess Planning Readiness.
---

# BeginNerd Plan — Planning and Control

## Ownership
PLANNING-01–04 and Planning Readiness. **PLANNING-02 exclusively owns formal tasks, work packages, subtasks and changes to their approved structure.** It does not own ordinary implementation steps.

## Choose only the relevant reference
- PLANNING-01: references/development-roadmap.md — outcome-driven roadmap and milestones.
- PLANNING-02: references/implementation-plan.md and references/work-structure-brainstorming.md — formal work structure.
- PLANNING-03: references/testing-strategy.md — risk-based test plan.
- PLANNING-04: references/document-control.md — decision and document tracking.
- references/planning-readiness.md — final readiness check when requested.

## Procedure
1. Read only relevant approved product/solution scope, existing tasks, dependencies and available team capacity. Avoid duplicating trackers and meaningless documentation.
2. Explain Lean, Structured and Extended task hierarchies when they are useful. Recommend the smallest practical breakdown, often end-to-end vertical slices. Seek material Work Structure Agreement before creating or replacing formal task IDs.
3. Give each approved task a user-visible outcome, requirement link, acceptance evidence, dependencies, owner and suitable test plan.
4. Define testing expectations **before execution**; prioritize critical data, security and failure scenarios. Planned tests are not test results.
5. Use risk-based **batch approval** for already scoped tasks. Avoid demanding approval for every implementation step. Execution authorization is still separate from plan approval.
6. During coding, an executor may discover and perform additional internal technical steps while preserving the approved task outcome and architecture. Only **material changes** to formal work structure, dependencies, scope, security or acceptance return to PLANNING-02.
7. If such a change arises, hold only the affected scope, review its impact and obtain the necessary material approval. Other authorized work can proceed.
8. Assess Planning Readiness based on actual plan consistency, approval and dependencies; hand the valid scope to Development Foundation.

## First-task handoff, not an extra go ritual
When the approved plan identifies the first unblocked slice, produce its outcome, acceptance, dependencies, allowed paths/actions and target executor. **Check separately** whether scoped execution authorization and foundation prerequisites already exist. If yes, hand off promptly to the authorized beginnerd-implement/executor without asking for another "gas T0". If not, request one precise local-write batch permission. Planning does not code, and approved planning is never implicit execution authorization.
## Boundaries
Do not select new software without Solution ownership, execute code, reconfigure providers or deploy. Avoid internal IDs and jargon in beginner-facing conversation unless requested. File/provider mutations require their own scoped authorization. Optional Graphify/Hindsight do not block planning. See references/agent-governance.md and references/work-structure-policy.md when needed.
