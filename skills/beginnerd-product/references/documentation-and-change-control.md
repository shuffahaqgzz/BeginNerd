# Product Foundation — Adaptive Documentation and Change Control

## Documentation depth
**Lean:** A single PRODUCT.md is appropriate for a small product, containing Product Brief/Discovery, Requirements, Minimum Viable Product, Technical Constraints, decisions and readiness. Do not generate multiple mostly empty documents.

**Structured:** Use PRODUCT-BRIEF.md, PRODUCT-REQUIREMENTS-DOC.md, MINIMUM-VIABLE-PRODUCT-SCOPE.md and TECHNICAL-REQUIREMENTS-DOC.md where risk, complexity or team size justify them.

Historical PRD.md, MVP-SCOPE.md and TRD.md are not mandatory canonical names. PRODUCT-BRIEF.md remains valid. API-GUIDE.md is not a mandatory Product Foundation artifact.

## Existing projects
Inspect current docs/approved names and reuse valid sources. If a stable requirement ID or existing decision exists, link it rather than duplicating or silently replacing it.

## Material change handling
1. Locate canonical requirements, acceptance, technical constraints, experiment evidence, approved product scope and source version.
2. Preserve stable IDs such as REQUIREMENTS-001, ACCEPTANCE-CRITERIA-001 and TECHNICAL-REQUIREMENTS-001. Canonical workflow IDs now use PRODUCT-FOUNDATION-01–04; read old aliases through the migration reference.
3. Explain the impact of proposed requirement/scope changes and group related **material** approvals. Ordinary corrections inside an already authorized documentation batch do not require per-line approval.
4. Record real Owner evidence, decisions, open assumptions, hypotheses and next verification; do not invent participants, interview findings, approval or experiment success.
5. For authorized file writes, read back the actual saved content, validate traceability, status, and pending decision references. File-write permission does not imply product-scope approval.

## One-time grant and document readback
For a novice starting a project, check the existing Scoped Workspace Grant before prompting for file-write permission. An approved grant for in-scope Product documentation covers multiple draft updates and readback across sessions while valid; do not ask "may I save PRODUCT.md?" after every revision. If missing, propose once with the project root, allowed new/edited documents and excluded unrelated/hidden/destructive files. A clear answer to the specific proposal is effective permission, not an unrelated product decision. Preserve actual before/after evidence and do not infer access beyond the named root.
## Workspace integrity
- Before writing, inspect target files and in-scope preexisting edits, including untracked/ignored files when permission permits.
- After writing, record path, content hash, timestamp and a scoped **before-and-after** inventory of relevant paths. An unchanged Git status for untracked directories does **not** prove their contents are unchanged.
- If no comparable baseline exists, report unrelated-file preservation as UNVERIFIED instead of claiming it.
- Do not copy private memory, secrets or credentials into documents or evidence.
- A static document checker cannot prove a user interview occurred, a runtime test passed, a change was approved or a deployment happened.

## Templates
Load only the needed artifact:
- assets/product-lean-template.md
- assets/product-brief-template.md
- assets/product-requirements-template.md
- assets/mvp-scope-template.md
- assets/technical-requirements-template.md

Each begins DRAFT/PENDING. Artifact structure is not evidence of readiness.
