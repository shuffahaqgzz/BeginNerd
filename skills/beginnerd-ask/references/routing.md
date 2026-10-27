# Routing Requests to the Right BeginNerd Skill

Choose a workflow by the **user's actual goal**, not a rigid phase lock. Consult references/workflow-registry.md when formal ownership or ID traceability is needed. User-facing answers should name the action in plain language, not recite workflow codes.

| User intent | Owning skill | Canonical workflow or function |
|---|---|---|
| Choose guidance style or optionally activate knowledge/memory | beginnerd-setup | First-use onboarding |
| Explain current project state, decisions or the next step | beginnerd-ask | Orientation and routing |
| Investigate a user problem, validate hypotheses or define the user segment | beginnerd-product | PRODUCT-FOUNDATION-01 |
| Define acceptance-backed product requirements | beginnerd-product | PRODUCT-FOUNDATION-02 |
| Set the minimum viable product and learning goal | beginnerd-product | PRODUCT-FOUNDATION-03 |
| Define testable technical constraints | beginnerd-product | PRODUCT-FOUNDATION-04 |
| Design user journeys, navigation and architecture | beginnerd-solution | SOLUTION-01–05 |
| Research technology or security and user interface design | beginnerd-solution | SOLUTION-06–08 |
| Set roadmaps, **formal tasks**, tests and document control | beginnerd-plan | PLANNING-01–04 |
| Prepare repository, tools, runtime and agent context | beginnerd-foundation | FOUNDATION-01–05 |
| Execute an **approved** task, quality checks or safe integration | beginnerd-implement | IMPLEMENTATION-01–05 |
| Release, monitor, handle incidents and maintain services | beginnerd-release | RELEASE-01–03 and OPERATIONS-01–03 |

## Broad requests and missing owners
"Build my app", "do whatever is necessary" and "deploy this privately" are not universal approval. First explain the smallest safe next step and the difference between local code, provider setup, external creation and deployment.

If a needed skill is not installed or available, do not substitute an unrelated Sites/cloud/shell tool to exceed authorization. A read-only outline can be offered, but provider writes and deployment require explicit separate permissions. Report only actual tool calls and test results, not imaginary handoffs.

A bug fix does not require rebuilding every lifecycle phase. An approved internal technical step is not a new formal task. A critical product/architecture/security conflict holds only the affected scope and returns to the appropriate owner; Planning alone owns changes to formal task records.

Optional Graphify/Hindsight context may be used only when enabled through beginnerd-setup and functionally verified. Canonical project records always take precedence.

## Example user-facing answer
"Your project has a clear initial product scope, but the login security approach still needs a decision. I recommend reviewing access requirements before coding this feature. The rest of the approved work can continue."

Internal workflow IDs and readiness codes may appear in technical records but should not appear in this kind of default explanation.
