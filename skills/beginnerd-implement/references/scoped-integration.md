# IMPLEMENTATION-04 — Scoped Integration

**Input:** Approved Task Registry + exact task authorization + relevant current repo/environment and acceptance evidence.
## Procedure
1. Determine whether integration is authorized: target branch/repo/environment, commits/PR, allowed action classes, reviewers, required checks and rollback.
2. Inspect diff, conflicts, test evidence, dependency version drift, secret exposure and approval scope before any integration.
3. Use least-privilege PR process and existing branch protection; do not bypass required checks or force-push/merge without separate authorization.
4. After authorized integration verify actual HEAD, expected files, required checks and smoke results. If CI skipped or not run, state that.
5. Unapproved provider updates, staged deployments or credentials are separate actions, not implicit side effects of a code PR.

**Output:** PR/merge or bounded integration record with before/after refs and tests, or NOT_AUTHORIZED if missing.
**Completion:** only direct verifiable acceptance for authorized scope counts; documentation or scripts without execution do not prove runtime PASS.
**Guardrails:** no formal task decomposition outside PLANNING-02, no unapproved remediation after declared failure, no external deployment without Phase 6 approval.
