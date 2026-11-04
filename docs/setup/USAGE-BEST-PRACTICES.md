# Using BeginNerd Well — Best Practices from Install to Maintenance

This guide is for people who use BeginNerd with a coding agent, and for whoever sets up the agent for them. It covers the whole path, from installation to running a live product. The per-phase cycles are in [PHASE-USAGE-CYCLES.md](../workflows/PHASE-USAGE-CYCLES.md).

## 1. Know what skills can and cannot do

BeginNerd skills are **guidance**. They give the agent a method, rules and words to explain things, and the agent follows them most of the time. They do not control the agent. The Owner decided to make the skills as effective as possible while accepting that behavior differs between models and harnesses ([BN-DEC-010](../decisions/BN-DEC-010-SKILLS-AS-GUIDANCE-LAYER.md)).

Why skills cannot be a guarantee:
- **A skill is text that the model chooses to load.** In the progressive-disclosure pattern used by Claude and many compatible harnesses, only a skill's name and description are always in context; exactly what loads, and when, varies by host. The full instructions load when the model decides they are relevant, so anything the agent does before that happens without them ([Anthropic, Agent Skills](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills)).
- **Loaded text is still context, not configuration.** Anthropic says the same of project instructions: they are "context, not enforced configuration", and blocking an action regardless of the model's choice needs a hook ([Claude Code memory](https://code.claude.com/docs/en/memory); [Claude Code hooks](https://code.claude.com/docs/en/hooks-guide)).
- **More rules, lower adherence.** In IFScale, the best of 20 models followed 68% of instructions when given 500 ([Jaroslawicz et al., 2025](https://arxiv.org/abs/2507.11538)). Short, early, specific rules work best.
- **Models do not reliably rank instructions by authority** ([Wallace et al., 2024](https://arxiv.org/abs/2404.13208)). Guarantees come from system design that limits what tools can do ([Debenedetti et al., 2025](https://arxiv.org/abs/2503.18813)).

BeginNerd's own runtime evaluation (docs/implementation/RUNTIME-EVAL-RUNS-4-7.md) shows both sides:
- Text that is always in context works. With the safety baseline in the project's AGENTS.md, a planted token was printed in 0 of 9 sessions; without it, in 7 of 9.
- A changed environment works completely. After the model key moved into an environment variable, it never appeared in a tool result.
- Skill text alone does not stop everything. The agent still opened harness configuration in some sessions, often before any skill had loaded.

### Three layers, three kinds of promise

| Layer | What it is | Promise | Use it for |
|---|---|---|---|
| **Harness and environment** | Permission rules, pre-tool-call hooks, sandbox, file permissions, secrets kept out of readable files, network limits | Deterministic for what it covers | Credentials, provider and network access, global configuration |
| **Project baseline** | Five lines in AGENTS.md or the harness equivalent, always loaded | Strong influence, not a guarantee | Safety rules that must hold even when no skill loads |
| **Skills** | The eight BeginNerd skills | Guidance; varies by model | Method, judgment-based rules (scope, approvals, phase ownership), explanations |

If a rule must **never** be broken, put it in the first layer. Skills cannot decide for a harness what counts as "the user approved this scope", and a hook cannot judge it, so judgment rules stay in skills.

## 2. Before the first session (whoever sets up the agent)

1. **Install once, in project scope.** Use one installation route per agent and check for older copies first ([README](../../README.md#get-started)). Note the BeginNerd commit you installed.
2. **Keep secrets out of what the agent can read.**
   - Pass model and provider keys through environment variables or the harness's secret store, not readable configuration files.
   - Keep `.env` files and tokens outside the project folder where possible.
   - An agent with a shell can still read its own environment, so give it only low-limit, revocable keys.
3. **Turn on the harness controls you have.** Examples:
   - deny rules for credential and configuration paths;
   - a pre-tool-call hook that blocks reads of those paths and unapproved network hosts;
   - a sandbox.

   Test them with a canary value on every route: read tool, shell, script, subprocess and subagent. Until that test passes, the status is **ENFORCEMENT NOT VERIFIED**. See [Harness action gates](../security/HARNESS-ACTION-GATES.md).
4. **Do not configure memory or knowledge providers in advance** unless the user chose them. A provider the harness switches on is not the user's consent, and BeginNerd will not use it until the user chooses it in setup.
5. **Pick a capable model** and expect differences. If you change model or harness, run a few behavioral scenarios (tests/behavioral) before relying on it.

## 3. The first session

1. **Start with your goal, not with setup.** For example, "I have an idea for a laundry app; help me understand the real problem first." BeginNerd helps first and asks about your experience only when it matters.
2. **Accept the safety baseline offer.** When a project folder exists, setup offers to append the five-line baseline to AGENTS.md. It is the most effective text-level protection BeginNerd has.
3. **Give one workspace grant, by folder and kinds of work.** For example, "you may create and edit documents and code in ./laundrykos, run local tests, no deletion, no network, no global settings." One grant replaces many per-file prompts.
4. **Skip optional providers unless you want them.** All six phases work without Graphify or Hindsight.

## 4. Working with the agent day to day

- **Name the skill when routing matters.** "Use beginnerd-product" or "pakai beginnerd-plan" removes the guesswork, since routing by description is not always reliable.
- **Do one phase at a time.** Follow the cycle for that phase; you do not need all six phases for a small change.
- **Approve by name.** Say which decision you approve: "first-version scope approved: order tracking and WhatsApp notification". These do not approve scope, design or tasks:
  - "lanjut", "ikut rekomendasi" or accepting a grant;
  - asking the agent to save notes.
- **Expect one question, not many.** A good BeginNerd agent groups the open decisions into a single approval request. If it asks for every file, remind it about the grant.
- **Revoke clearly and check that it stuck.** "Izin folder ./laundrykos gue cabut" should stop all writes. Only your own words granting the folder again restore them. Asking for an edit or saying "continue" does not.
- **Prefer project scope for any configuration change**, and name the exact setting when you approve a global one.

## 5. Check outcomes instead of trusting claims

- **Files:** ask the agent to read back what it saved, or open the file yourself. A claimed read-back without a read is a known failure.
- **Approvals:** check that project records mark only what you approved as approved; everything else should say pending.
- **Tests:** look for the command and its real output. Planned tests are not results, and a passing static check does not prove the app works.
- **Memory:** "memory saved" is only true when the provider acknowledged it.
- **Releases:** nothing should be live, pushed or created externally before your separate release approval naming the target.

## 6. When the agent goes wrong

1. Stop it and say plainly what was wrong. If a file write was involved, revoke the grant.
2. If a secret was shown, treat it as exposed: rotate it, and move it out of readable files.
3. After a declared failure, approve each corrective attempt separately. BeginNerd allows at most two per issue before stopping for review.
4. If the same mistake repeats, move that rule down a layer: from skill to AGENTS.md, or from AGENTS.md to a harness control.

## 7. End-to-end checklist

| Stage | Checklist |
|---|---|
| Install | One route, project scope, commit noted, no duplicate copies |
| Environment | Keys in env or secret store; harness deny rules or hooks tested with a canary, or recorded as ENFORCEMENT NOT VERIFIED |
| First use | Goal first; safety baseline in AGENTS.md; one folder grant; providers only if chosen |
| Product | Problem and evidence; first-version scope approved by name; pending items marked |
| Solution | Material technology, data and security decisions approved |
| Plan | Formal task batch approved; tests planned; first task identified |
| Foundation | Environment verified by running it; secrets reported by location only |
| Implement | Four prerequisites named before code; real test output; at most two approved recovery attempts |
| Release | Separate approval naming target, version, audience, data, cost and rollback; live verification |
| Operations | Real measurements and feedback go back to Product |
