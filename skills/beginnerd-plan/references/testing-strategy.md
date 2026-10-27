# PLANNING-03 — Testing Strategy & Quality Planning

**Input:** Approved G1/G2 artifacts applicable to the scope, existing project state and authorized decisions.
## Procedure
1. Read approved requirements/acceptance, solution, security threats and dependency risks BEFORE coding.
2. Choose proportionate unit, integration, contract, E2E, security, accessibility, performance, recovery tests by risk and impact.
3. Map REQUIREMENTS ID → acceptance → planned test IDs → expected evidence, including negative/invalid/auth failure cases for critical flows.
4. Plan isolation, disposable fixture data, safe mocked external writes, regression scope, quality criteria and evidence capture.
5. Identify untestable claims, missing thresholds or critical security control without test; escalate material exceptions for approval.
6. Separate PLANNED, IMPLEMENTED, EXECUTED, PASSED and FAILED. Playwright MCP exploration is not a persisted repeatable test suite.

**Canonical output:** TESTING-STRATEGY.md or Lean DEVELOPMENT-PLAN.md section.
**Completion criteria:** Critical requirements and controls have planned verification owners; no unexecuted tests marked PASS.
**Boundaries:** Do not claim task accepted or tests executed from drafting. Files/issues publishing require target-specific authorization and readback. If prerequisites fail, report PARTIAL/BLOCKED and restrict affected work.
