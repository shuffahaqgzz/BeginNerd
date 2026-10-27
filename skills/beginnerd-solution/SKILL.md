---
name: beginnerd-solution
description: Use this skill to design application journeys, navigation, architecture, data models, application programming interfaces, integrations, researched technology choices, security and user interfaces, and to review Solution Design Readiness for an approved product scope.
---

# BeginNerd Solution — User Experience and Solution Architecture

## Ownership
One modular skill covers SOLUTION-01–08 and Solution Design Readiness (internal G2). Choose only the needed workflow:
- SOLUTION-01: references/user-flow.md — user journeys.
- SOLUTION-02: references/application-navigation.md — screens and navigation.
- SOLUTION-03: references/system-architecture.md — domain and system architecture.
- SOLUTION-04: references/database-data-design.md — data model, integrity and lifecycle.
- SOLUTION-05: references/api-integration.md — interfaces and integration.
- SOLUTION-06: references/technology-selection.md — Research First and Reuse First.
- SOLUTION-07: references/security-architecture.md — adaptive, risk-based security.
- SOLUTION-08: references/ui-design.md — adaptive visual review.
- Read references/g2-readiness.md only for a final review/handoff.

## Working approach
1. Reconcile the current Product Baseline, approved requirements and actual existing assets. Design only the unblocked part when earlier readiness is partial.
2. Explain a concise proposal in the user's language, recommend a best-fit option, then seek informed approval only for material decisions such as technology, data sensitivity, cost, trust boundary or architecture.
3. Use proportionate Lean or Structured artifacts. Reuse the existing design conventions in brownfield projects; file edits require scoped authorization and read-back.
4. SOLUTION-06 evaluates credible existing components, including source/date, licenses, security applicability, compatibility and operating costs. Do not install unapproved dependencies.
5. Choose Basic, Application or Enhanced security design by **product risk**, not user coding skill. A critical unmitigated security gap prevents Solution Design Readiness for affected scope.
6. Cross-check flows, data, API, user interface, technology, threat controls and planned tests against actual requirements. Explain missing evidence plainly.
7. Handoff only the approved unblocked scope to Planning. A design document does not prove code, security certification or deployment readiness.

## Boundaries
No formal task decomposition (PLANNING-02 owns it), provider installation, code execution or deployment. Source instructions are native English, but user-facing terms must be easy to understand and internal codes hidden unless requested. Optional Graphify/Hindsight integrations are configured only by beginnerd-setup and are never prerequisites for design.

See references/document-control.md, references/agent-governance.md and references/research-reuse-policy.md only when relevant.
