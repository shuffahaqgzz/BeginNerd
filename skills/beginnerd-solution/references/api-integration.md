# SOLUTION-05 — API & Integration Design

**Input/trigger:** Domain boundaries, use cases, external provider constraints. Run when this specific solution domain is requested; respect current G1 scope and approval.

## Procedure
1. Map consumers, provider/endpoints/events, requests, response schemas and input validation.
2. Define auth/authz, errors, timeout, retry/idempotency, versioning and outages proportionately.
3. Research existing APIs/SDKs via SOLUTION-06 and note unverified fees, scopes and compatibility.
4. Describe planned contract/security tests, privacy boundaries and approval for material integration.
5. Link each material decision to source REQUIREMENTS / ACCEPTANCE IDs, evidence and timestamp where available; mark missing facts TBD and assign a decision owner.

**Canonical output:** API-AND-INTEGRATION-DESIGN.md or Lean section. Lean/Structured is adaptive; do not require every design document.
**Acceptance for this design workflow:** API contracts clear and verifiable; API not yet implemented.
**Governance:** Explain → Interview → Approve → Record; write only within an authorized path. A planned verification is NOT EXECUTED. No formal task decomposition and no change of application runtime.
