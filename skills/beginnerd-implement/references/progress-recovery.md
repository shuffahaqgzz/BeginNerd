# IMPLEMENT-05 — Progress & Recovery Governance

**Input:** Approved Task Registry + exact task authorization + relevant current repo/environment and acceptance evidence.
## Procedure
1. Track approved task IDs with NOT_STARTED/IN_PROGRESS/PARTIAL/PASS/BLOCKED and evidence (not just agent declaration).
2. Detect scope expansion, prerequisites, ownership conflicts, stalled work, too-large tasks or runtime drift; isolate affected area.
3. Return material decomposition changes to PLANNING-02 with impact analysis, keeping historical identity and approvals.
4. For verification failure register stable issue identity + baseline; request authorization before attempt #1 and separately before #2, with diagnosis/risk/expected verification.
5. After two failed attempts, HARD STOP REVIEW_REQUIRED; no reset via branch, renamed issue, subagent or side task. Independent approved work may continue safely.
6. Update canonical project state and consented Hindsight checkpoint only if provider acknowledges.

**Output:** Execution status, attempt ledger and controlled disposition, without invented task completion.
**Completion:** only direct verifiable acceptance for authorized scope counts; documentation or scripts without execution do not prove runtime PASS.
**Guardrails:** no formal task decomposition outside PLANNING-02, no unapproved remediation after declared failure, no external deployment without Phase 6 approval.
