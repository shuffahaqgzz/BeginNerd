# BeginNerd Behavioral Acceptance Scenarios

The cases in scenarios.json define **expected behavior only**. They are all NOT_EXECUTED until a real supported runtime, an evaluator, and evidence are recorded. Static CI validates scenario structure; it does not run the prompts.

Execution protocol:
1. Identify agent runtime version, installed skill SHA, actual provider status and project scope.
2. Select a safe test project and obtain permission before any provider/repository write.
3. Run each scenario in an isolated session where appropriate; record sanitized prompts, observed outputs and actual provider invocations.
4. Judge must_not assertions and expected behaviors using real evidence, not the skill definition text.
5. Record PASS, FAIL, BLOCKED, or UNVERIFIED per case in a separate execution evidence report; do not overwrite the source scenario fixture with unverified verdicts.
6. Include negative/abuse cases: duplicate setup, stale memory, no consent, scope expansion, unauthorized decomposition, attempt limit.

See docs/implementation/VALIDATION-PLAN.md and docs/templates/TEST-EVIDENCE-TEMPLATE.md. Do not upload private project memory or credentials.

## H-01 dedicated negative suite
H01-01 repeats the exact beginner-impatience input that previously resulted in an unapproved private Sites deployment. H01-02–H01-06 exercise private-release coercion, general delegation, false readiness, workspace restrictions and synthetic tool-output secrets. These are **NOT_EXECUTED fixtures**, not evidence of corrected agent behavior. Run in isolated sessions with external creation/deployment unavailable or mocked; evaluate prohibited attempts even when the external tool blocks them. Provider tokens must never appear in test fixtures or reports. Positive controls are mandatory so safe beginner workflows still work.

## Reviewer evidence improvements (existing cases, no new lifecycle workflow)
New reviewer scenarios cover beginner language, batch-approval friction, iterative internal steps, real product validation, external-write refusal, effectiveness evidence and optional provider setup. These **scenario definitions remain NOT_EXECUTED** until a real harness run captures the attempted actions, outcome, sample size and source SHA.

Metrics such as correct routing, approval prompts per completed task, time to useful output, observed user results, rework and unauthorized tool attempts belong to existing Product, Quality Assurance and Operations responsibilities. See docs/implementation/EFFECTIVENESS-EVIDENCE.md. No universal effectiveness claim is supported by the fixture registry.
