# BeginNerd Framework Architecture — Approved Design v1.0

## Scope and interpretation
BeginNerd is a Guided Building framework for beginners and mixed-experience teams. BN-DEC-009 approved a six-phase Hybrid Modular Architecture with 32 lifecycle workflows. Companion skills provide navigation and setup across phases, but do not own phase workflows. These are DESIGN decisions, not a claim that runtime integration is working.

| Phase | Lifecycle skill | Workflows | Assessment |
|---|---|---:|---|
| 1 — Product Foundation | beginnerd-product | 4 | G1 Product Baseline Readiness |
| 2 — UX & Solution Architecture | beginnerd-solution | 8 | G2 Solution Design Readiness |
| 3 — Planning & Control | beginnerd-plan | 4 | Planning Readiness Check |
| 4 — Development Foundation | beginnerd-foundation | 5 | Foundation Readiness Check |
| 5 — Implementation & QA | beginnerd-implement | 5 | Evidence-Based Completion Check |
| 6 — Release & Operations | beginnerd-release | 6 | Release / Deployment / Operational Readiness |
| **Total** | **6 lifecycle skills** | **32** | |

Cross-phase companion skills:
- beginnerd-ask: understand intent, explain position and terminology, recall context, route to the proper owner.
- beginnerd-setup: first-use onboarding, guidance-mode selection, contextual configuration and consented Graphify/Hindsight setup.

## Design principles
Hybrid Modular: one main entry point per phase with internal workflow references and adaptive Lean / Structured artifacts. Workflows can operate independently where dependencies permit. The six lifecycle skills plus two companion skills form the target inventory of eight skills.

Research-first and reuse-first across all phases. Phase 2 SOLUTION-06 owns principal evaluation and selection of reusable software. Phase 3 PLANNING-02 owns formal task decomposition; Phase 5 cannot silently re-decompose tasks. Security architecture is risk-based, not dependent on user coding experience.

## Source-of-truth order
Approved requirements and material decisions → approved work structure/implementation plan → current scoped execution authorization → agent proposals and execution. Actual environment evidence, security constraints, and permissions must be checked; contradictions cause a scoped HOLD, not a silent override.

## Handoffs
- G1 supports Phase 2 solution work.
- G2 supports Phase 3 planning; PARTIAL restricts planning to unblocked scope.
- Planning Readiness supports Phase 4 foundation.
- Foundation Readiness supports bounded Phase 5 execution.
- Evidence-based Phase 5 completion supports Phase 6 release review.
- Operational incidents, new product scope, or material solution changes are returned to their designated owner; no direct bypass of Planning.

See docs/workflows/WORKFLOW-REGISTRY.md for canonical phase responsibility IDs.
