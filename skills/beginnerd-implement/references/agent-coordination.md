# IMPLEMENTATION-02 — Agent Coordination & Handoff

**Input:** Approved Task Registry + exact task authorization + relevant current repo/environment and acceptance evidence.
## Procedure
1. Inventory available agents/tools and approved responsibilities; decide single-agent vs delegation based on actual complexity, not a mandatory multiagent model.
2. Specify delegated task IDs, immutable approved scope, authorization limits, workspace, evidence format, and relevant security/privacy boundaries.
3. Never delegate broader permissions than parent authorization or task creation to subagent. Ensure simultaneous changes avoid conflicts via isolated branches/worktrees where authorized.
4. At handoff reconcile changed files and statuses against original task IDs, actual tests, overlapping diffs and pending decisions.
5. On conflict or missing evidence stop affected integration and raise to Owner/Planning rather than inventing progress.

**Output:** Delegation/handoff log, stable task references and sanitized evidence; no independent task hierarchy.
**Completion:** only direct verifiable acceptance for authorized scope counts; documentation or scripts without execution do not prove runtime PASS.
**Guardrails:** no formal task decomposition outside PLANNING-02, no unapproved remediation after declared failure, no external deployment without Phase 6 approval.
