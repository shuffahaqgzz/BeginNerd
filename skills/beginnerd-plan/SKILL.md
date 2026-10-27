---
name: beginnerd-plan
description: Gunakan untuk menyusun Phase 3 BeginNerd—development roadmap dan milestones, implementation plan dan approved task decomposition, testing strategy, document control, serta Planning Readiness. Termasuk Adaptive Work Structure Brainstorming dan vertical slicing berbasis outcome.
---

# BeginNerd Plan — Phase 3 Planning & Control (PLANNING-01–04)

**Owner utama formal decomposition:** PLANNING-02. Ini SATU-SATUNYA workflow yang boleh membuat/mengubah work packages, tasks, subtasks, submilestones dan dependency graph formal. Executor Phase 5 tidak boleh membuat unit baru sendiri.

## Protocol
1. Explain Before Execute, inspect G1/G2 verdict, approved MVP scope, Solution Blueprint, requirements/design traceability, available staff/capacity, existing issues and user decisions.
2. Jangan memaksa full Phase 3 untuk permintaan sempit/bug fix; load references only as needed:
   - PLANNING-01 → references/development-roadmap.md
   - PLANNING-02 → references/implementation-plan.md and references/work-structure-brainstorming.md
   - PLANNING-03 → references/testing-strategy.md
   - PLANNING-04 → references/document-control.md
   - Planning readiness request → references/planning-readiness.md
3. Apply Hybrid Modular with Lean/Structured docs. Use outcome-driven milestones, vertical slices for feature delivery, risk-based test strategy before coding, lightweight DoR/DoD, dependency/owner tracking. Adapt structure to real project complexity.
4. **Work Structure Brainstorming:** explain terms and Lean/Structured/Extended examples; compare, recommend best-fit and ask explicit approval of material hierarchy/granularity. Do not instantiate every possible hierarchy level. Record Work Structure Agreement and stable task IDs in an approved plan.
5. G2 PARTIAL → only plan unblocked scope as ready; G2 BLOCKED → focus on resolving blockers, not implementing affected work. Don't create tasks for unapproved product scope or select new technology.
6. Material milestone dates, release priorities, work structure, delivery risk and testing exceptions require Explain → Interview → Approve → Record. No micro-approval for minor technical steps within scope; no authorization to execute merely because a plan is ready.
7. Reuse existing project issue tracker and docs. Publishing GitHub issues is a provider write requiring user-scoped approval; absent permission keep proposed plan local/in chat. File writes require scoped path permission, readback and diff; no inferred approval.
8. For session context use approved Hindsight recall/retain if verified; canonical docs/Git supersede memory. If retain not acknowledged, report MEMORY_SYNC_PENDING.
9. Verify Planning Readiness and hand off approved task registry/dependencies/acceptance/testing strategy to Phase 4. Include owner, evidence, blocker and next decision.

## Governance
Research-First/Reuse-First, No Overclaim, No Overengineering, No Overrules, least authority and max two **separately authorized** remediation attempts on declared failures. No formal executor-side decomposition or bypass via subagent. See references/agent-governance.md, references/work-structure-policy.md and references/research-reuse-policy.md.
