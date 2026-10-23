# BeginNerd Phase 1 — beginnerd-product Implementation Contract

**Status:** IMPLEMENTATION CANDIDATE / PR REVIEW; framework **BN-DEC-009.1 is already APPROVED at design level**. This file describes the translation of that design to a portable Agent Skill, not a new user approval or proof of runtime acceptance.

## Known approved decisions and unresolved provenance
- One Hybrid Modular `beginnerd-product` owns PF-01 Product Discovery, PF-02 Product Requirements, PF-03 MVP Definition and PF-04 Technical Requirements.
- Explain Before Execute → Context Discovery → Recommend → Interview & Approve → Produce → Validate.
- Adaptive Lean / Structured documents, independent/full-phase invocation, stable requirement-to-acceptance-to-technical traceability, lightweight change control and G1 readiness.
- Final naming from prior Phase 1 decision discussion: **Lean `PRODUCT.md`**; Structured `PRODUCT-BRIEF.md`, `PRODUCT-REQUIREMENTS-DOC.md`, `MINIMUM-VIABLE-PRODUCT-SCOPE.md`, `TECHNICAL-REQUIREMENTS-DOC.md`. Earlier drafts `PRD.md`, `MVP-SCOPE.md`, `TRD.md` are superseded as defaults. Product Brief remains unchanged; `API-GUIDE.md` remains a separate optional artifact rather than a mandatory Phase 1 document.
- Approval rule for G1: critical requirements have acceptance and traceability, material decisions understood and approved, no unresolved critical blockers, evidence to support PASS. G1 does not certify implementation or security production readiness.
- Research/Reuse-First Phase 1 records reuse needs/constraints but does **not** choose technical components as final (SOLUTION-06 is owner).
- Historical discussion decisions are represented by approved design summaries; full original Phase 1 transcript/provenance still needs reconciliation before claiming the repository stores exhaustive approval evidence.

## Implementation boundaries
- Single installable `skills/beginnerd-product/SKILL.md`, six workflow/readiness/control references, five assets.
- Four generated cross-cutting references from canonical source docs (agent governance, memory/knowledge, research/reuse, artifact/readiness) with Git blob hashes; no hard reference to source-repo root after isolated install.
- No new SDLC phase, workflow, quality gate, MCP provider, technology choice or required project document.
- Five pending lifecycle directories must remain README-only.
- No explicit authorization to mutate consumer repositories, store persistent memory or approve requirements on behalf of users.

## Acceptance plan
1. Static/spec subset: frontmatter valid, exact installable inventory **three** (ask, setup, product), references self-contained, generated snapshots fresh.
2. Structural coverage: four PF workflow procedures, correct final file names and G1, templates cannot claim approval, no SOLUTION-06/PLANNING-02 ownership violations.
3. Activation eval: positive/negative product prompts where true target is PF/G1, and false when technology selection, planning, execution or provider setup is requested.
4. Behavioral eval: standalone PF, full PF flow, Lean vs Structured, brownfield reuse, traceability, explicit approval, conflicts, G1 partial/blocked, no technology/implementation overreach.
5. Distribution: `npx skills@latest add shuffahaqgzz/BeginNerd --list` **after merge** should detect **three** skills; install/invocation/routing must be tested on approved runtime before operational claims.
6. Cross-phase integration and provider tests: remain separate tasks, with Issue #2 still OPEN for Graphify/Hindsight.

## Status model
PR + CI PASS validates only static source and package structure. Runtime skill activation, behavioral quality, provider recall/retain and real project G1 are **NOT EXECUTED** unless backed by separate evidence.
