---
name: beginnerd-implement
description: Jalankan Phase 5 BeginNerd hanya pada approved execution tasks: koordinasi agent, risk-based QA, scoped integration, progress tracking dan bounded recovery. Gunakan untuk mengimplementasikan/mengetes fitur atau menangani failure setelah authorization, tanpa membuat task baru atau auto-deploy.
---

# BeginNerd Implement — Phase 5 Implementation & QA

**Ownership:** IMPLEMENT-01–05 dan Evidence-Based Completion Check, bukan perencanaan/pemecahan task, perubahan requirement/architecture, konfigurasi provider tanpa izin atau production release.

## Controlled operating procedure
1. **Read/verify** approved requirements and architecture, implementation plan and **task registry from PLANNING-02**, dependencies, repository baseline and currently granted batch authorization. Missing required information → HOLD affected scope.
2. Select only relevant workflow references: IMPLEMENT-01 references/approved-task-execution.md, IMPLEMENT-02 references/agent-coordination.md, IMPLEMENT-03 references/risk-based-qa.md, IMPLEMENT-04 references/scoped-integration.md, IMPLEMENT-05 references/progress-recovery.md. For final check use references/completion-check.md.
3. **Pre-execution check:** task ID and acceptance exist, prerequisites satisfied, authorization specifies task IDs/target repo/path/environment/action class/expiry if relevant, no critical security blocker, planned verification available. If no permission or outside scope, propose/ask; do not mutate. Reference scripts/verify_execution_contract.py for read-only machine-checkable examples (never replace runtime/tool-side access checks).
4. **During execution:** implement the minimum sufficient approved vertical slice; do not formal-decompose tasks/subtasks/packages, change tech choices or delegate with broader authority. Track commands/diffs/tests, attempted external writes and evidence. A subagent inherits restrictions; availability of a tool does not grant rights.
5. **Risk-based verification:** execute relevant unit, integration, security, contract, accessibility and E2E tests according to PLANNING-03. Distinguish PLANNED, IMPLEMENTED, EXECUTED, PASSED and FAILED. Never convert a blocked/denied provider action into a behavioral PASS if agent attempted unauthorized operation.
6. **Recovery:** after a declared verification failure, propose one scoped corrective approach, obtain explicit per-attempt Owner approval; max **2** approaches per same issue + baseline, retain history across agents/branches/sessions. Attempt #2 requires new approval. Two failures → HARD STOP / HOLD / REVIEW_REQUIRED, no automatic third retry. References/recovery-governance.md.
7. **Post-execution:** compare diff and acceptance to authorized tasks, verify committed/tested changes and integration authorization, record findings, owners, evidence, remaining risk and disposition. If no direct evidence, report PARTIAL/BLOCKED/UNVERIFIED; CI static PASS != user acceptance.
8. Hindsight: on consented reachable provider, recall checked against canonical docs, retain meaningful checkpoint and handoff with acknowledgement; otherwise report MEMORY_SYNC_PENDING where retain needed. Never persist secrets. Adhere to references/agent-governance.md.

## Boundaries & handoff
- PLANNING-02 exclusively owns formal work structure and decomposition. Issue discovered during execution requiring new task or architecture change → scoped HOLD and controlled return to Planning/Solution; not silent scope expansion.
- No unauthorized local write, provider config, API/Sites mutation, Git integration/merge or release deployment. IMPLEMENT-04 requires separate scoped integration permissions.
- No Overclaim / No Overengineering / No Overrules / Strict Recommendation Relevance and Least Authority.
- Report task IDs, authorization, baseline SHA, commands and actual test results, scoped diff/evidence, integration reference, blocker/finding, recovery attempt ledger, completion verdict and handoff. No Phase 6 deployment without release authorization.
