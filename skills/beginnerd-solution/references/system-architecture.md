# SOLUTION-03 — System Architecture & Domain Modeling

**Input/trigger:** Requirements, integrations, data flow, existing modules and real scale needs. Run when this specific solution domain is requested; respect current G1 scope and approval.

## Procedure
1. Partition by business domain, explicit module ownership and trust boundaries.
2. Design minimal viable components, communication contracts and failure isolation; microservices only if justified.
3. Compare cost/security/maintenance implications; consult SOLUTION-06 for software building blocks.
4. Capture diagrams/decision refs, requirement mapping, assumptions, alternatives and owner approval.
5. Link each material decision to source REQUIREMENTS / ACCEPTANCE IDs, evidence and timestamp where available; mark missing facts TBD and assign a decision owner.

**Canonical output:** SYSTEM-ARCHITECTURE.md or Lean section. Lean/Structured is adaptive; do not require every design document.
**Acceptance for this design workflow:** Responsibilities and boundaries understandable; no infrastructure mutated.
**Governance:** Explain → Interview → Approve → Record; write only within an authorized path. A planned verification is NOT EXECUTED. No formal task decomposition and no change of application runtime.
