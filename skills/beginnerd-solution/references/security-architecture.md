# SOLUTION-07 — Security Architecture / Adaptive Security

**Input/trigger:** Data sensitivity, roles, exposure, trust boundaries and requirement links. Run when this specific solution domain is requested; respect current G1 scope and approval.

## Procedure
1. Select Basic/Application/Enhanced by context and consequences, not beginner skill; profiles are not certifications.
2. Threat model relevant assets, data flows, attack paths and failure modes.
3. Trace REQUIREMENTS ID → THREAT ID → SECURITY-REQUIREMENTS ID → SECURITY-CONTROL ID → SECURITY-TEST ID (PLANNED).
4. Recommend controls for authorization, secrets, data protection, logging and recovery as relevant; explain critical risks.
5. Link each material decision to source REQUIREMENTS / ACCEPTANCE IDs, evidence and timestamp where available; mark missing facts TBD and assign a decision owner.

**Canonical output:** SECURITY-ARCHITECTURE.md or Lean section. Lean/Structured is adaptive; do not require every design document.
**Acceptance for this design workflow:** Critical threats mitigated by proposed controls, test plans and approval; no G2 PASS with critical gap.
**Governance:** Explain → Interview → Approve → Record; write only within an authorized path. A planned verification is NOT EXECUTED. No formal task decomposition and no change of application runtime.
