# BeginNerd Effectiveness Evidence — Existing Workflows Only

**No new mandatory workflow or quality gate.** This is an observation guide for the already approved Product Foundation, Planning, Implementation/Quality Assurance and Operations responsibilities.

## Why measure
A readable README and 60 static tests demonstrate source structure, not whether beginners build better products with BeginNerd. We need actual observations, meaningful denominators and comparison context before making effectiveness claims.

| Indicator | How to observe | Existing owner | Important limitation |
|---|---|---|---|
| Skill routing accuracy | Correctly selected skill across positive, negative and multilingual prompts / all assessed cases | beginnerd-ask / existing activation evaluation | Do not treat a static scenario file as an executed test |
| Task success | Owner-accepted task outcomes / tasks genuinely attempted | IMPLEMENTATION-03 quality review | Separate completed code from accepted behavior |
| Time to first useful result | Elapsed active session time to first accepted useful output | IMPLEMENTATION-05 progress review | Record interruptions and task complexity |
| Approval friction | Redundant prompts / decisions actually eligible for batch authorization; also total material prompts | Existing governance review during Implementation | Zero approvals is not automatically safer or better |
| Rework | Verified rework incidents and effort per accepted task | IMPLEMENTATION-05 | Do not count planned work as rework |
| Safety | Attempted unauthorized writes/deploys / assessed risky opportunities | IMPLEMENTATION-03 and RELEASE-03 | A denied but attempted action is still a behavioral failure |
| Product learning | Observed user outcomes vs hypothesis/success signal, with context | PRODUCT-FOUNDATION-01/03 and OPERATIONS-01 | Owner opinion is not customer evidence |
| User clarity | Whether a novice correctly understood the next action without internal codes | Product discovery / quality review | Requires actual user feedback, not a model self-score |

## Evidence rules
1. Predefine a relevant outcome and recording method before interpreting a score. If no data exist, write NOT MEASURED / UNVERIFIED; **never invent a success percentage**.
2. Use a consented, anonymous/disposable assessment cohort. Do not publish private interview audio or sensitive runtime traces.
3. Compare with-skill vs without-skill when useful and feasible, while noting case difficulty, evaluator bias, model/harness version and environment differences.
4. Record sample size, numerator/denominator, observation method, raw source reference, date, expected/actual and uncertainty.
5. Run the quality analysis within existing workflows; **do not create an additional skill, workflow, mandatory gate or fake closed-loop automation**.
6. Any material changes based on results return to their existing Product/Planning/Solution owners.

## Current baseline
Repository sources specify behavioral and activation cases, but their execution_status remains NOT_EXECUTED. Previous Owner reports include bounded behavioral PASS/FAIL/BLOCKED; those are not a statistically meaningful effectiveness score. Cross-harness runtime behavior, Graphify/Hindsight opt-in operation and real A2 end-to-end evaluation remain unverified.
