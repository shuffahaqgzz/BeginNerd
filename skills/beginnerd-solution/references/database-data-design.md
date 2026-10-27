# SOLUTION-04 — Database & Data Design

**Input/trigger:** Business data requirements, roles, lifecycle and existing stores. Run when this specific solution domain is requested; respect current G1 scope and approval.

## Procedure
1. Define conceptual entities, relationships, stable keys, uniqueness and referential integrity.
2. Describe create/change/delete semantics, concurrency, transactions, deduplication and consistency.
3. Include retention, PII classification, authorization, backup, export and recovery requirements.
4. Assess brownfield migration impacts without running migrations; select DB only through SOLUTION-06.
5. Link each material decision to source REQUIREMENTS / ACCEPTANCE IDs, evidence and timestamp where available; mark missing facts TBD and assign a decision owner.

**Canonical output:** DATABASE-DESIGN.md or Lean section. Lean/Structured is adaptive; do not require every design document.
**Acceptance for this design workflow:** Data constraints are testable and traceable; not applied migrations.
**Governance:** Explain → Interview → Approve → Record; write only within an authorized path. A planned verification is NOT EXECUTED. No formal task decomposition and no change of application runtime.
