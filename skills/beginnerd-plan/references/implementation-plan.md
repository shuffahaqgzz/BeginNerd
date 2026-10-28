# PLANNING-02 — Implementation Plan & Task Decomposition

**Input:** Approved G1/G2 artifacts applicable to the scope, existing project state and authorized decisions.
## Procedure
1. Begin with references/work-structure-brainstorming.md and decide how much hierarchy is genuinely useful: Lean, Structured or Extended.
2. Inventory existing approved tasks/issues and reusable components so duplicates are not created. Never change an approved hierarchy silently.
3. Break approved solution into small, vertical end-to-end feature slices by default (UI→logic→data→tests) with measurable completion. Infrastructure/refactors can use justified alternate slicing.
4. For each task ID record objective, parent/milestone, REQUIREMENTS IDs, dependencies, approved scope, exclusions, acceptance, verification plan, owner, status and authorization reference.
5. Detect dependency cycles, missing requirements/approval, oversized work and unrealistic concurrency; recommend return-to-user decision.
6. Obtain Work Structure Agreement and material approval before locking formal task registry. Executor cannot re-decompose, even via agent delegation.
7. During execution, internal technical steps or additional debugging within an approved task are allowed without creating formal subtasks. A material change to product scope, acceptance, architecture or the formal dependency graph requires a scoped HOLD → impact analysis → PLANNING-02 controlled replanning and Owner approval. Preserve task identity and allow unrelated authorized work to continue.

## Ready-first-task handoff
For the earliest approved and unblocked task, provide a readable "ready to start" summary of goal, acceptance, dependencies, executor, scoped project/path/action authorization and necessary foundation checks. An approved plan alone does **not** grant local-write rights. If a separate valid execution batch exists, route directly to Implementation without another permission question; otherwise request one precise execution authorization while continuing unblocked read-only work. Preserve formal task ownership under PLANNING-02.
**Canonical output:** IMPLEMENTATION-PLAN.md or Lean DEVELOPMENT-PLAN.md section plus approved task registry.
**Completion criteria:** Each approved task has Ready definition, explicit dependencies and measurable Done criteria; no authorization to execute implied.
**Boundaries:** Do not claim task accepted or tests executed from drafting. Files/issues publishing require target-specific authorization and readback. If prerequisites fail, report PARTIAL/BLOCKED and restrict affected work.
