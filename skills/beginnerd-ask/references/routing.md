# Ask Routing Reference

Read current project state; open packaged references/workflow-registry.md when exact workflow IDs/owners matter. Routing is based on **what the user needs**, not a simplistic global phase lock.

| User intent | Responsible skill | Workflow |
|---|---|---|
| What is BeginNerd, how to start, set guidance preference | beginnerd-setup | First-use onboarding |
| Which phase are we in / explain next step / recall decision | beginnerd-ask | Cross-phase orientation only |
| Identify product problem or users | beginnerd-product | PF-01 |
| Define requirements / MVP / technical requirements | beginnerd-product | PF-02 / PF-03 / PF-04 |
| Map user flow or navigation | beginnerd-solution | SOLUTION-01 / SOLUTION-02 |
| Design architecture, database, APIs | beginnerd-solution | SOLUTION-03 / SOLUTION-04 / SOLUTION-05 |
| Compare frameworks/reusable components | beginnerd-solution | SOLUTION-06 |
| Security controls / UI design | beginnerd-solution | SOLUTION-07 / SOLUTION-08 |
| Roadmap, formal task breakdown | beginnerd-plan | PLANNING-01 / PLANNING-02 |
| Testing strategy, doc control | beginnerd-plan | PLANNING-03 / PLANNING-04 |
| Repository scaffolding, environment, coding standards | beginnerd-foundation | FOUNDATION-01 / FOUNDATION-02 / FOUNDATION-03 |
| Configure coding agents, project context | beginnerd-foundation | FOUNDATION-04 / FOUNDATION-05 |
| Execute approved feature/task | beginnerd-implement | IMPLEMENT-01 |
| Agent coordination, QA, integration, progress/recovery | beginnerd-implement | IMPLEMENT-02 / IMPLEMENT-03 / IMPLEMENT-04 / IMPLEMENT-05 |
| Release acceptance, deployment planning or execution | beginnerd-release | RELEASE-01 / RELEASE-02 / RELEASE-03 |
| Monitoring, incident, maintenance | beginnerd-release | OPS-01 / OPS-02 / OPS-03 |

## Broad beginner requests and missing owners (H-01)
Requests like "langsung bikin aplikasi", "aku ikut aja", "deploy saja" or "you decide everything" must be classified by **requested action and impact**, not treated as a blanket approval. Separate idea/product discovery (beginnerd-product), design (beginnerd-solution), implementation (beginnerd-implement) and deployment (beginnerd-release). Verify which skill is actually installed, then route only to a verified available owner with required inputs and authorization.

When the requested owning skill is not installed, **do not substitute an unrelated tool** (Sites, shell, external app) or let a companion execute its lifecycle work. Offer a concise safe next step, explain the missing owner without forcing the beginner to know phase IDs, and use an in-chat outline or non-deploying concept preview only within its actual authorization. Private Sites deployment remains an EXTERNAL_CREATE/DEPLOY_RELEASE action, never a harmless preview. Neither user impatience nor general delegation overrides consumer AGENTS.md or workspace boundaries.

Before any external creation or publication, check the packaged references/agent-governance.md authorization classes, readiness and explicit release consent. Distinguish routing recommendations from executed handoffs; never claim Phase 2–6 acceptance from Phase 1 artifacts.

## Exceptions / blocked state
- A single bug fix does not require recreating all prior SDLC documents.
- A current critical architecture/security conflict requires scoped HOLD and return to the owning phase.
- Partial G2 supports planning only for unblocked work; missing data must not be quietly made up.
- Routing to a lifecycle owner is a **design recommendation** unless that skill is actually installed, discoverable, and verified. Do not claim automatic handoff based solely on this registry.
- Graphify/Hindsight may assist context only after permission and functional verification; never replace approved documents.

Example response:
"Proyek saat ini berada pada [verified state]. Permintaan ini milik [skill / workflow] karena [reason]. Bukti yang tersedia adalah [reference]. Berikut langkah yang direkomendasikan, dengan [necessary approval/blocker] sebelum mengubah apa pun."
