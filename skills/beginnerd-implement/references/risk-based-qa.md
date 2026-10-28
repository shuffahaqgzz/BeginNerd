# IMPLEMENTATION-03 — Risk-Based QA

**Input:** Approved Task Registry + exact task authorization + relevant current repo/environment and acceptance evidence.
## Procedure
1. Read PLANNING-03 test strategy, threat/control verification, critical user journeys and approved task acceptance.
2. Prioritize critical authorization/data integrity/security/transaction flows and negative/failure cases before supporting details.
3. Run repeatable automated tests where feasible (unit/integration/contract/E2E), plus necessary manual/browser exploration; Playwright MCP exploration does NOT replace persistent regression tests.
4. Capture command, environment, source SHA, expected/observed outcome, actual failures and sanitized logs; do not upgrade PLANNED/IMPLEMENTED to PASS.
5. Assess defects and required fixes; after a declared failure any corrective remediation uses separately approved attempt budget (max 2).
6. Report findings, unsatisfied critical controls, partial scope and independent accepted/blocked tasks truthfully.

**Output:** QA matrix with actual per-test verdicts and coverage gaps; not a paper-only PASS.
**Completion:** only direct verifiable acceptance for authorized scope counts; documentation or scripts without execution do not prove runtime PASS.
**Guardrails:** no formal task decomposition outside PLANNING-02, no unapproved remediation after declared failure, no external deployment without Phase 6 approval.

## Reviewer regression: credential and privacy pitfalls
Risk-based QA for login must check whether reusable passwords are stored or verified as plaintext (including env-based admin password patterns), whether approved password hashing and session/authorization controls are in place, and whether negative unauthorized-access tests actually ran. Report unsafe credential practices as defects, do not claim "secure" because a file named .env exists. Sanitize fixture secrets and real customer records before any recorded evidence. A local test that sends real API requests is an external-effect operation and needs its own authorization. Preserve failed test traces as failures, not PASS.
