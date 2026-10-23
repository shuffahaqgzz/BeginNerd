# BeginNerd — Activation / Trigger Evaluation Specification

Queries in `queries.json` test **which skill should activate**, separately from the 22 behavioral cases. Both positive and near-miss negative prompts are included for each companion skill. These are test specifications, **not executed results**.

Use isolated fresh agent sessions with current skill metadata, matching runtime version, and no hidden prior context. Record for each scenario: expected skill, observed skill activation (including no activation), wrong-skill activation, source SHA, runtime log/evidence, verdict and evaluator. Compare before/after description changes. Do not count a plausible natural-language response as proof the intended skill actually activated.

A targeted source inspection without an agent session is STATIC only. No Graphify/Hindsight writes are authorized by this test set.

References: https://agentskills.io/skill-creation/optimizing-descriptions and https://agentskills.io/skill-creation/evaluating-skills.
