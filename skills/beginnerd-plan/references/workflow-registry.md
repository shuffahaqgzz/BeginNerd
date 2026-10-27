<!-- GENERATED FILE — DO NOT EDIT DIRECTLY.
Canonical source: docs/workflows/WORKFLOW-REGISTRY.md
Canonical Git blob SHA-1: 2f36378d5881bc48305515f9f6dfc40f3d562712
Regenerate in source repository: build_portable_references.py --write
-->

# BeginNerd Workflow Registry — 32 Approved Responsibilities

This registry retains the original six-phase ownership and **32 workflow responsibilities**. Identifiers now use complete words for previously abbreviated phase names. A separate migration reference maps old identifiers to new identifiers without inventing extra workflows.

| ID | Responsibility | Owner |
|---|---|---|
| PRODUCT-FOUNDATION-01 | Product Discovery | beginnerd-product |
| PRODUCT-FOUNDATION-02 | Product Requirements | beginnerd-product |
| PRODUCT-FOUNDATION-03 | Minimum Viable Product Definition | beginnerd-product |
| PRODUCT-FOUNDATION-04 | Technical Requirements | beginnerd-product |
| SOLUTION-01 | User Flow & Journey | beginnerd-solution |
| SOLUTION-02 | Application Flow & Navigation | beginnerd-solution |
| SOLUTION-03 | System Architecture & Domain Modeling | beginnerd-solution |
| SOLUTION-04 | Database & Data Design | beginnerd-solution |
| SOLUTION-05 | API & Integration Design | beginnerd-solution |
| SOLUTION-06 | Technology Selection, Research & Reuse | beginnerd-solution |
| SOLUTION-07 | Security Architecture | beginnerd-solution |
| SOLUTION-08 | UI Design & Design System | beginnerd-solution |
| PLANNING-01 | Development Roadmap & Milestones | beginnerd-plan |
| PLANNING-02 | Implementation Plan, Work Structure Brainstorming & Task Decomposition | beginnerd-plan |
| PLANNING-03 | Testing Strategy & Quality Planning | beginnerd-plan |
| PLANNING-04 | Document Control & Change Tracking | beginnerd-plan |
| FOUNDATION-01 | Repository Baseline & Scaffolding | beginnerd-foundation |
| FOUNDATION-02 | Development Environment & Runtime | beginnerd-foundation |
| FOUNDATION-03 | Code Standards & Quality Tooling | beginnerd-foundation |
| FOUNDATION-04 | AI Agent & Harness Configuration | beginnerd-foundation |
| FOUNDATION-05 | Project Context & Knowledge Base | beginnerd-foundation |
| IMPLEMENTATION-01 | Approved Task Execution | beginnerd-implement |
| IMPLEMENTATION-02 | Agent Coordination & Handoff | beginnerd-implement |
| IMPLEMENTATION-03 | Risk-Based Quality Assurance | beginnerd-implement |
| IMPLEMENTATION-04 | Scoped Integration | beginnerd-implement |
| IMPLEMENTATION-05 | Execution Progress & Recovery Governance | beginnerd-implement |
| RELEASE-01 | Release Readiness & Candidate | beginnerd-release |
| RELEASE-02 | Deployment Planning & Authorization | beginnerd-release |
| RELEASE-03 | Controlled Deployment & Acceptance | beginnerd-release |
| OPERATIONS-01 | Monitoring & Operational Handoff | beginnerd-release |
| OPERATIONS-02 | Incident Response & Controlled Recovery | beginnerd-release |
| OPERATIONS-03 | Maintenance & Lifecycle Management | beginnerd-release |

## Boundaries

PLANNING-02 creates or modifies formal task structures. IMPLEMENTATION-01–05 may perform routine internal steps within already approved tasks but must return **material scope/dependency/formal-task changes** to PLANNING-02. OPERATIONS-03 can identify maintenance work, not independently invent new product scope or a formal implementation task.

The assistant should explain phase/workflow names in natural language to beginners and display stable IDs only in canonical artifacts, technical traceability or when explicitly requested.
