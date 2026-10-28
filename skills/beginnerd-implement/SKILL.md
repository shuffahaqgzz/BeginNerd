---
name: beginnerd-implement
description: Use this skill to carry out previously approved application tasks, coordinate agents, perform risk-based quality assurance, integrate authorized changes, track delivery and handle bounded recovery. Do not create formal tasks or deploy without separate permission.
---

# BeginNerd Implement — Implementation and Quality Assurance

## Ownership
IMPLEMENTATION-01–05 and evidence-based completion:
- IMPLEMENTATION-01: references/approved-task-execution.md — approved feature execution.
- IMPLEMENTATION-02: references/agent-coordination.md — bounded delegation.
- IMPLEMENTATION-03: references/risk-based-qa.md — real test execution and negative cases.
- IMPLEMENTATION-04: references/scoped-integration.md — authorized branch/integration actions.
- IMPLEMENTATION-05: references/progress-recovery.md — progress and corrective recovery.
Read references/completion-check.md for actual completion assessment.

## Before making changes
1. Verify the approved PLANNING-02 task, acceptance, dependencies, source revision, project/workspace and the **current scoped authorization**. Missing critical authorization means hold the affected action.
2. Reuse existing implementation and quality tooling; keep the solution minimal and aligned with approved architecture.
3. Use a **risk-based approved batch** for routine internal technical steps and tests. **Do not ask permission for every new coding step** within that scope.
4. Do not create a new formal task/subtask/feature. If a discovery changes scope, approval, dependency graph, security design or acceptance, return only the affected work to PLANNING-02 or the design owner; unaffected authorized work may continue.

## Continue approved work, not an invented feature
Within an already approved task and valid local-write batch, a clear "continue" means complete safe internal edits, debugging and tests through the original acceptance—no repeated prompt for every helper or test. New formal tasks, product capabilities, material architecture/acceptance changes and **each corrective remediation after declared failure** still require their established owner and consent. An urgent security concern justifies alerting the user and safe work within current scope, not unapproved production/provider mutation. For login changes, check stored password hashing (not reusable plaintext password comparison), least-privilege access, sessions, secrets and relevant unauthorized-access tests. Never commit real credentials or customer data.
## During and after execution
5. Apply the smallest approved change; capture actual edits, tests and negative behavior. Delegate only within inherited permissions. Never use a different available tool to bypass an authorization boundary.
6. Distinguish planned, implemented, executed, passed and failed tests. A denied but **attempted** unauthorized provider action is a behavioral failure, not a successful refusal.
7. After a formally declared verification failure, request separate informed approval for **each distinct corrective remediation attempt**, maximum two per issue and baseline. No third attempt after two failed approaches, even across branches or agents. Ordinary corrections before formal failure and internal steps inside an approved attempt are not independent remediation attempts.
8. Report outcome, acceptance evidence, changed files, blockers, open risks and next owner decision in plain language. Keep internal task/test IDs in technical records unless asked.

## Enforcement boundaries
No external creation, deployment, provider configuration, secret administration or Git integration beyond specifically approved action classes. A written guardrail is **not tool-side enforcement**; before risky operations check the actual harness/tool/provider permissions and use safe denial/mocked tests. Offline scripts provide advisory diagnostics only.

See references/recovery-governance.md, references/agent-governance.md and references/work-structure-policy.md when applicable. Optional memory is never required for ordinary implementation.

## Effectiveness evidence within existing workflows
As part of relevant quality reviews, record task success, defects, rework, approval prompts, time to first usable result, correct routing and attempted unauthorized actions **when observed**. Never manufacture metrics or create a new mandatory evaluation workflow.
