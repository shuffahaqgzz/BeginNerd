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
