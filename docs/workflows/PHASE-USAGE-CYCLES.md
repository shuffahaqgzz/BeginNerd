# BeginNerd Usage Cycles — One Cycle per Phase

This is the practical companion to the workflow registry. It shows how a user and an agent move through each BeginNerd skill: when to use it, what the agent does, what only the user can approve, what is left behind and when to move on. The cycles describe intended behavior. Actual agent behavior varies by model and harness, so check the outputs named in each cycle instead of assuming them.

## The whole lifecycle at a glance

```
Setup (first use, optional) ──► Ask (any time: "where am I, what next?")
                                  │
Product ──► Solution ──► Plan ──► Foundation ──► Implement ──► Release & Operations
   ▲                                                                   │
   └──────────── real use, feedback and measurements ◄─────────────────┘
```

- **It is not a waterfall.** Use only the phase that fits the current problem. A small bug fix in an approved task goes straight to Implement.
- **Each phase owns its decisions.** Product owns scope, Solution owns design and technology, Plan owns formal tasks, Foundation owns the environment, Implement owns coding and QA, Release owns anything live.
- **One cycle, five beats.** Every phase repeats the same rhythm: **orient → explain → propose → approve → record and verify**. The agent does routine work inside an approval without asking again; it asks only for material decisions and new permissions.
- **Two permissions never come from a phase.** A workspace grant lets the agent write files in one folder for named kinds of work. It never approves product scope, a design, a task, a deployment, a provider or a global configuration change.

## Setup — first use and optional integrations (beginnerd-setup)

**Use it when:** starting BeginNerd in a project, changing how much the agent explains, or deliberately choosing Graphify (project knowledge) or Hindsight (persistent memory).

**Openers:** "Aku mau mulai pakai BeginNerd di proyek ini." · "Set up BeginNerd for this project; I don't want memory tools yet."

**Cycle:**
1. The agent gives something useful first, then sets a provisional familiarity level from your own words; it asks at most one to three short questions, and only when they change the next step.
2. Discovery is name-only: it checks installed skills and named, non-secret settings. It never opens harness configuration or credential files and never contacts a memory or knowledge provider during discovery.
3. If a project folder exists, it offers **one** consent request: a workspace grant for that folder (kinds of work, exclusions) and the five-line Project safety baseline appended to the project's agent instructions (AGENTS.md or the harness equivalent).
4. Optional providers are offered only when relevant, each separately, with privacy, cost and what works without them. Nothing is installed or connected without your choice.
5. If you choose a provider, the agent runs a disposable, project-scoped check (retain → acknowledgement → recall, or knowledge retrieval and isolation) and reports what actually works.

**You approve:** the workspace grant, the baseline write, each provider and each named global setting. "Activate memory" alone does not approve a global change.

**Leaves behind:** recorded familiarity level, grant and consent in existing project state, the baseline in AGENTS.md (read back), provider status (enabled, NOT_ENABLED or failing).

**Done when:** you can start real work. Providers that you did not choose are NOT_ENABLED, which is not a failure.

**Next:** Ask, or Product for a new idea.

## Ask — orientation and routing (beginnerd-ask)

**Use it when:** you are not sure where the project stands, what a decision means or which phase should handle a request. It works at any point.

**Openers:** "Proyek ini udah sampai mana, langkah berikutnya apa?" · "Review this existing project and recommend the next useful step."

**Cycle:**
1. Read current project files (and enabled memory, if you chose one) and resolve conflicts in favor of current files.
2. Explain where the project stands in plain language, without internal IDs.
3. Recommend **one** next step, the phase that owns it and any approval it needs.
4. Hand off to that phase. Ask never writes product decisions, designs, tasks, code or releases itself.

**You approve:** nothing new in Ask itself; it only prepares the approval the owning phase will request.

**Leaves behind:** a recommendation, and a handoff note only when a handoff actually happens.

## Product — what to build and why (beginnerd-product)

**Use it when:** shaping an idea, checking that a problem is real, defining requirements, choosing what goes in the first version or revisiting scope after real feedback.

**Openers:** "Aku punya ide aplikasi laundry kos, bantu pahami masalah utamanya dulu." · "Help me decide what belongs in the first version."

**Cycle:**
1. Discover: the problem, who has it, existing alternatives and what is evidence versus assumption.
2. Choose the smallest validation step (interview script, paper mock, manual test) instead of building early.
3. Draft requirements and acceptance criteria with stable IDs, and a first-version scope split into included, deferred and out of scope.
4. Save the draft (one `PRODUCT.md` for simple work) inside the granted folder and read it back. Saving needs the grant only, not another prompt per file.
5. Ask **once** for the material decisions still open, grouped: first-version scope, key requirements, risky constraints.
6. Record approvals and assumptions in the same turn; anything not approved stays **pending**.

**You approve:** first-version scope, material requirements and constraints, and any change to an approved baseline. Accepting a grant, saying "lanjut" or asking to save notes does not approve scope; a feature you explicitly name and ask to include is your choice for that feature only.

**Leaves behind:** `PRODUCT.md` (or separate files when useful) with approved and pending items clearly marked.

**Done when:** Product Baseline Readiness holds for the approved part of the scope. Unapproved parts stay pending without blocking the rest.

**Next:** Solution for the approved scope. Product never writes application code, even on "langsung bikin".

## Solution — experience and architecture (beginnerd-solution)

**Use it when:** designing user flows, screens, data, interfaces, security, or choosing technology for approved scope.

**Openers:** "Rancang alur pesanan dan datanya untuk scope yang sudah disetujui." · "Which stack fits this, and why?"

**Cycle:**
1. Reconcile approved Product scope and existing assets; design only the unblocked part.
2. Research and reuse first: credible existing components, licenses, costs, security.
3. Recommend one default per decision with a short alternative; low-risk, reversible choices proceed without repeated questions.
4. Ask once for material decisions: technology, data sensitivity, trust boundaries, cost, architecture.
5. Choose the security depth by product risk, not by your coding skill. A critical unmitigated gap blocks readiness for that scope.
6. Save the design inside the granted folder and read it back.

**You approve:** material technology, architecture, data and security decisions. An unspecified "continue" does not approve unknown technology or costs.

**Leaves behind:** proportionate design documents with recorded decisions.

**Done when:** Solution Design Readiness holds for the approved scope.

**Next:** Plan. Solution installs nothing and deploys nothing.

## Plan — work structure and tests (beginnerd-plan)

**Use it when:** turning an approved design into a roadmap, formal tasks and a test strategy, or changing that structure.

**Openers:** "Pecah jadi tugas-tugas kecil yang bisa dikerjakan bertahap." · "What should we build first, and how will we know it's done?"

**Cycle:**
1. Read approved scope and design, existing tasks and capacity.
2. Recommend the smallest useful structure, often end-to-end slices; explain lean versus structured breakdowns only when it helps.
3. Give each task an outcome, requirement link, acceptance evidence, dependencies and planned tests. Planned tests are not results.
4. Ask once for the task batch (Work Structure Agreement). Plan is the **only** phase that creates or changes formal tasks.
5. Save the plan inside the granted folder and read it back.
6. Identify the first unblocked task and check separately whether execution authorization and Foundation prerequisites exist.

**You approve:** the formal task batch and later material changes to it. Plan approval is not execution authorization.

**Leaves behind:** a development plan, tasks with acceptance and tests, and a first-task handoff.

**Done when:** Planning Readiness holds: approved, consistent tasks with satisfied or named dependencies.

**Next:** Foundation if the environment is not ready; otherwise Implement, without an extra "go" ritual when authorization already exists.

## Foundation — repository, environment and agent context (beginnerd-foundation)

**Use it when:** preparing the repository, runtime, quality tools and project agent context, or checking whether an existing folder is safe to continue (exposed secrets, risky files).

**Openers:** "Siapkan repo dan environment buat tugas pertama." · "Is this project folder safe to keep working in?"

**Cycle:**
1. Discover before changing: branch, modified files, runtime versions, installed tools, existing instructions.
2. Explain the smallest safe changes and reuse existing tools.
3. Within the grant and approved tasks, scaffold and configure without per-file prompts; snapshot and keep rollback.
4. Write or update project agent context with the safety baseline (append, never overwrite) when that is approved work.
5. Verify for real: startup, build, lint, tests and skill discovery. A config file existing is not proof it works.
6. Report secrets by location and type only, with one recommended fix (environment variable or secret store).

**You approve:** new installs, global or harness configuration (by named setting), credential operations and anything outside the folder grant.

**Leaves behind:** a working baseline with recorded versions, changed paths and gaps.

**Done when:** Foundation Readiness holds. It is not feature QA and not deployment permission.

**Next:** Implement.

## Implement — build and test approved tasks (beginnerd-implement)

**Use it when:** carrying out approved tasks, testing them, integrating changes or recovering from a declared failure.

**Openers:** "Kerjakan tugas pertama yang sudah disetujui." · "Continue the approved task and run its tests."

**Cycle:**
1. Before the first code write, name four things: the approved task, the design decisions it relies on, its satisfied dependencies and the execution authorization. If one is missing, write no code, say what is missing in one sentence and ask once.
2. Make the smallest change that meets the task's acceptance; routine internal steps and tests need no new approval.
3. Run real tests, including negative and security cases; separate planned, executed, passed and failed.
4. If a discovery changes scope, design, security or acceptance, hold only the affected part and return it to its owner.
5. After a **declared** verification failure, each corrective attempt needs your separate approval, at most two per issue; then stop for review.
6. Report outcome, evidence, changed files, risks and the next decision in plain language.

**You approve:** the execution authorization (usually the grant plus an approved task), each corrective attempt after a declared failure, and any Git integration beyond what was approved. A revoked grant stays revoked until you grant the folder again; asking to edit a named file or to "continue" is not a new grant.

**Leaves behind:** code and tests in the granted folder, actual test output and an evidence-based completion check.

**Done when:** the task's acceptance is met with execution evidence.

**Next:** the next approved task, Plan for structural changes, or Release when a candidate is ready.

## Release & Operations — go live and keep it healthy (beginnerd-release)

**Use it when:** assessing a release candidate, preparing and authorizing deployment, deploying, monitoring, handling incidents or maintenance.

**Openers:** "Siapin rencana deploy, tapi jangan deploy dulu." · "We're ready to release version 1; what do you need from me?"

**Cycle:**
1. Check the exact source revision, real implementation and QA evidence, privacy, cost, backups and rollback.
2. Recommend one simple hosting option with costs and a short alternative; prepare an inactive deployment guide, placeholders without secrets, a smoke checklist and rollback steps.
3. Ask for a **separate, specific release approval** that names target, version, audience, data exposure, cost and rollback. Nothing external is created, pushed or called before it.
4. Deploy only what was approved, verify the live version, access controls and smoke paths; stop or roll back only as approved.
5. Monitor system health and agreed product measurements; never invent metrics.
6. For incidents and maintenance, investigate impact first and return engineering work to Plan and architecture to Solution.

**You approve:** every hosted publication or deployment (even private), external resources, credential changes and provider configuration.

**Leaves behind:** release evidence, live verification, monitoring handoff and incident records.

**Next:** real usage evidence returns to **Product** (discovery and first-version review) to decide the next iteration; this loop is part of the existing phases, not a new workflow.

## Shortcuts that stay inside the rules
- **Small fix in an approved task:** go straight to Implement; no new Product or Plan cycle.
- **Existing project (brownfield):** start with Ask; it reads what exists and routes to the phase that fits.
- **Unsure whether something is material:** the agent should say so and ask once, not guess.
