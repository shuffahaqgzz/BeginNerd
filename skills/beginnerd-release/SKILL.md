---
name: beginnerd-release
description: Use this skill to assess release candidates, request scoped deployment authorization, carry out controlled deployment, verify live operation, monitor user outcomes, handle incidents and evaluate maintenance risks without automatic provider changes.
---

# BeginNerd Release — Release and Operations

## Ownership and references
- RELEASE-01: references/release-candidate.md — release candidate and evidence.
- RELEASE-02: references/deployment-authorization.md — deployment plan and permission.
- RELEASE-03: references/controlled-deployment.md — authorized rollout and smoke acceptance.
- OPERATIONS-01: references/monitoring-handoff.md — monitoring and user outcomes.
- OPERATIONS-02: references/incident-response.md — controlled incidents and recovery.
- OPERATIONS-03: references/maintenance-lifecycle.md — maintenance, security advisories, costs and support.
Read references/release-readiness.md only when a combined readiness review is requested.

## Operating approach
1. Inspect approved scope, exact source revision, real implementation/quality evidence, deployment destination, privacy, exposure, costs, backups and rollback.
2. Distinguish source publication, release readiness, deployment authorization, live deployment verification and operational monitoring. Passing a static test does not prove a running application.
3. Give concise recommendations using the user's language. Obtain **separate explicit approval** before any hosted publication/deployment—even private—as well as external creation, destructive action, credential changes or provider configuration. Material permissions must name their target and scope.
4. Execute only authorized actions, record provider evidence and verify live version, data integrity, access controls and relevant smoke paths. Stop or perform only approved rollback if results fail.
5. For monitoring, combine system health with relevant **product outcome measurements** and user feedback when the Owner has approved collection. Never invent metrics, users or a success threshold.
6. When measurements reveal an unmet user need, route learning to existing **PRODUCT-FOUNDATION-01** discovery and **PRODUCT-FOUNDATION-03** minimum viable product review; do not invent a new phase or auto-expand product scope.
7. During incidents or maintenance, investigate applicability and impact before changes; return formal engineering work to PLANNING-02 and material architecture to Solution. Follow separately approved two-attempt recovery limits when verification has declared failure.
8. State what actually worked, what remains uncertain and who owns the next decision. Never claim an incident resolved, memory saved or monitoring active without real evidence.

## Safety and portability
Harness/tool/provider permission controls must enforce external actions; written instructions are not sufficient. No unapproved software upgrades, secret leaks or destructive cleanup. Optional Graphify/Hindsight do not block release workflows. See references/agent-governance.md and references/research-reuse-policy.md when necessary.
