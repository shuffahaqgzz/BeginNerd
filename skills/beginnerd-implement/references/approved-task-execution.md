# IMPLEMENTATION-01 — Approved Task Execution

**Input:** Approved Task Registry + exact task authorization + relevant current repo/environment and acceptance evidence.
## Procedure
1. Check approved implementation plan, exact task ID/parent, requirements, dependencies, acceptance, current baseline SHA and permitted paths/actions.
2. Compare task objective with requested change; do not reinterpret ambiguity by making new packages/subtasks. If unsuitable → HOLD and return-to-PLANNING-02.
3. Use approved dependencies/building blocks from SOLUTION-06; research existing code and adapt with minimal changes, not custom subsystem rewrite.
4. Perform smallest authorized technical steps; monitor scope and keep reproducible commit/diff/test evidence.
5. After changes, validate actual behavior against acceptance and error paths; do not declare DONE from successful code generation alone.

## Scope-aware no-repeat permission check
Resolve existing task approval and a valid project-root Scoped Workspace Grant before edits. A grant allows safe offline creates/edits/tests only as explicitly enumerated; reuse it across in-scope code changes rather than prompting again on each tool call. Record actual changed files, before/after behavior and tests. A changed root, unapproved dependency/feature, destructive local operation, real external API or high-risk secret action needs fresh authorization. This is not a replacement for Plan ownership or separately approved corrective remediation attempts.
## Internal steps do not consume new approval
Inside an already authorized task, perform safe helper edits, tests and debugging until accepted or genuinely blocked. Do not generate formal tasks or add new feature scope. An explicit declared verification failure activates the separate approved-remediation budget (maximum two) and cannot be reframed as a routine retry. For login-related work verify stored-password hashing, auth/session/access boundaries and negative security tests. Avoid exposing customer data or credentials in fixtures or logs.
**Output:** Implementation/diff and test evidence attached to existing approved task, not a newly created formal task.
**Completion:** only direct verifiable acceptance for authorized scope counts; documentation or scripts without execution do not prove runtime PASS.
**Guardrails:** no formal task decomposition outside PLANNING-02, no unapproved remediation after declared failure, no external deployment without Phase 6 approval.
