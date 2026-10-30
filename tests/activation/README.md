# BeginNerd — Activation / Trigger Evaluation Specification

Queries in `queries.json` test **which skill should activate**, separately from the 22 behavioral cases. Both positive and near-miss negative prompts are included for each companion skill. These are test specifications, **not executed results**.

Use isolated fresh agent sessions with current skill metadata, matching runtime version, and no hidden prior context. Record for each scenario: expected skill, observed skill activation (including no activation), wrong-skill activation, source SHA, runtime log/evidence, verdict and evaluator. Compare before/after description changes. Do not count a plausible natural-language response as proof the intended skill actually activated.

A targeted source inspection without an agent session is STATIC only. No Graphify/Hindsight writes are authorized by this test set.

References: https://agentskills.io/skill-creation/optimizing-descriptions and https://agentskills.io/skill-creation/evaluating-skills.

## Language and trigger coverage
Skill frontmatter and source instructions are authored in native English. Some test prompts intentionally use Indonesian (the user's language) to test **multilingual user requests**, not to make the source instructions bilingual. Require positive and negative activation evidence for the actual harness before claiming routing accuracy. The six new reviewer fixtures remain NOT_EXECUTED until validated.

## Loaded then routed
An agent may load beginnerd-ask to orient and then route to the owning skill. For a `should_trigger: false` ask query, record "loaded then routed to the correct owner" as a separate outcome rather than a plain FAIL, and report it next to the strict verdict. A companion skill that loads and then acts, such as setup inspecting configuration for a general technical question, is still a FAIL.
