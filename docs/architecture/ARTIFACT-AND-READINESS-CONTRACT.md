# Artifacts, Traceability & Readiness — Design Baseline

## Adaptive artifact strategy
Use Lean documentation when project size and risk justify concise artifacts; Structured when complex needs, multiple dependencies, or compliance require distinct files. Reuse valid brownfield project documents and naming conventions. Artifacts communicate decisions, not artificial completion claims.

## By phase

| Phase | Representative canonical outputs from approved contracts | Readiness proof |
|---|---|---|
| 1 — Product | Product Brief, Product Requirements, MVP definition, Technical Requirements, decision references | G1 — Product Baseline Readiness; criteria and scope are approved |
| 2 — Solution | User Flow, Application Flow, System Architecture, Database Design, API & Integration Design, Technology Selection evidence, SECURITY-ARCHITECTURE.md, UI/Design System | G2 — Solution Design Readiness with risk-aware security coverage and approval |
| 3 — Planning | DEVELOPMENT-ROADMAP.md, IMPLEMENTATION-PLAN.md, TESTING-STRATEGY.md, DOC-CONTROL.md; Lean may use DEVELOPMENT-PLAN.md | Planning Readiness: tasks, dependencies, acceptance, tests and scope consistent |
| 4 — Foundation | Repository baseline/configuration, workspace manifest, agent registry, AGENTS.md, environment/quality/context evidence as applicable | Foundation Readiness from actual repository and runtime verification |
| 5 — Implementation | Authorized execution evidence, integration references, QA/test results, blockers and completion disposition | Evidence-Based Completion Check; planned tests do not imply executed tests |
| 6 — Release | Release candidate/readiness, deployment authorization, deployment verification, operational handoff, incidents and maintenance records | Distinct release, deployment, operation and maintenance evidence |

File names beyond those explicitly settled in prior discussions remain subject to project-specific naming rules; do not generate a mandatory file for every potential output.

## Verification semantics
- G1: product requirements/approved MVP baseline.
- G2: solution coverage, design consistency, technical decisions, security risk and approval evidence.
- Planning Readiness: valid decomposition and verification plan; no new large bureaucratic gate.
- Foundation Readiness: actual environment and tools work.
- Phase 5 Completion: approved scope demonstrably meets acceptance; FAIL or PARTIAL is not PASS.
- Phase 6: release authorization, deployed runtime verification, monitoring/operations handoff and maintenance completion are distinct from each other.

## Traceability examples
Requirement → UX/solution design → approved milestone/work package/task → planned test → implemented test → test execution result → acceptance record → release/deployment evidence when applicable.

Stable IDs such as REQUIREMENTS-001 and TEST-CASE-001 help cross-references. A security risk may link requirement → threat → control → security test. A **test case planned** is not evidence that the test was **executed** or **passed**.

## Status precedence
Canonical approved documents and confirmed current-state evidence take precedence over agent assumptions, Hindsight recall or Graphify cached relationships. Graphify/Hindsight improve discovery and continuity, not source-of-truth authority.

## Scope exception
A user-requested small change may invoke the relevant narrow workflow directly; the framework must not force regeneration of all phases if existing approved context suffices.
