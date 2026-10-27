<!-- GENERATED FILE — DO NOT EDIT DIRECTLY.
Canonical source: docs/workflows/WORKFLOW-REGISTRY.md
Canonical Git blob SHA-1: a462b6cbc2b08bd3c0684980424c900e3e13acf6
Regenerate in source repository: build_portable_references.py --write
-->

# BeginNerd Workflow Registry — Approved 32 Contracts

Owner is always the corresponding lifecycle skill, even when beginnerd-ask directs a request to it. Descriptions below are responsibility summaries rather than full detailed executable references.

| ID | Responsibility | Owner |
|---|---|---|
| PF-01 | Product Discovery | beginnerd-product |
| PF-02 | Product Requirements | beginnerd-product |
| PF-03 | MVP Definition | beginnerd-product |
| PF-04 | Technical Requirements | beginnerd-product |
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
| IMPLEMENT-01 | Approved Task Execution | beginnerd-implement |
| IMPLEMENT-02 | Agent Coordination & Handoff | beginnerd-implement |
| IMPLEMENT-03 | Risk-Based QA | beginnerd-implement |
| IMPLEMENT-04 | Scoped Integration | beginnerd-implement |
| IMPLEMENT-05 | Execution Progress & Recovery Governance | beginnerd-implement |
| RELEASE-01 | Release Readiness & Candidate | beginnerd-release |
| RELEASE-02 | Deployment Planning & Authorization | beginnerd-release |
| RELEASE-03 | Controlled Deployment & Acceptance | beginnerd-release |
| OPS-01 | Monitoring & Operational Handoff | beginnerd-release |
| OPS-02 | Incident Response & Controlled Recovery | beginnerd-release |
| OPS-03 | Maintenance & Lifecycle Management | beginnerd-release |

## Contract boundaries
PLANNING-02 alone owns formal work structure creation and changes. IMPLEMENT-01–05 consume approved tasks, with scoped HOLD and return to planning on material decomposition conflicts. OPS-03 identifies maintenance needs but does not independently invent product scope, architecture, or formal tasks. No additional mandatory workflow is created for research, guardrails, or companion skills.
