---
name: beginnerd-product
description: Use this skill to discover and validate a product problem, interview prospective users, define product requirements and acceptance criteria, prioritize a minimum viable product, capture technical constraints, and assess Product Baseline Readiness without implementing an application.
---

# BeginNerd Product — Product Foundation

## Ownership
This lifecycle skill owns **PRODUCT-FOUNDATION-01** Product Discovery, **PRODUCT-FOUNDATION-02** Product Requirements, **PRODUCT-FOUNDATION-03** Minimum Viable Product Definition, **PRODUCT-FOUNDATION-04** Technical Requirements, and Product Baseline Readiness (internal G1).

Only run the workflow relevant to the user's request. The four responsibilities are internal to one skill, not four installable skills.

## How to work
1. **Start with the real problem.** Review the user's goals, existing project/market evidence, existing product decisions and unknown assumptions. Do not pretend that the Owner's belief is evidence of real user behavior.
2. **Choose the smallest validation step that reduces uncertainty.** When relevant, load references/product-discovery.md for non-leading problem interviews, Jobs-to-be-Done, existing alternatives, hypotheses and lightweight experiments. No mandatory research ritual for obvious, low-risk internal work.
3. **Use plain language and relevant questions.** Explain what is being decided before asking. Recommend the best-fit option; group closely related material decisions. Never expose test-case numbers, internal readiness labels or authorization codes in ordinary user conversation.
4. **Choose the documentation depth.** Use one PRODUCT.md for simple work; use separate Product Brief, Requirements, Minimum Viable Product and Technical Requirements files only when useful. Inspect and reuse existing brownfield artifacts. See references/documentation-and-change-control.md.
5. **Write traceable requirements.** Link source/evidence, user outcome, stable requirement IDs, acceptance, critical risks, assumptions and Owner approval. Read references/product-requirements.md.
6. **Define and test the minimum product hypothesis.** Prioritize meaningful learning and observable user value, distinguish included/deferred/out-of-scope features, and plan how real feedback will change the next iteration. Read references/mvp-definition.md.
7. **Capture actionable technical constraints.** Translate vague guarantees such as "100% secure" or "free forever" into **proposed observable conditions**, requirement links, assumptions, an owner, and tests **planned, not executed**. Compare Product Baseline, Solution Design feasibility, and release/runtime evidence separately. Do not select the final framework or cloud provider here; read references/technical-requirements.md.
8. **Review readiness only when requested.** Read references/g1-readiness.md. A document being filled out does not mean the product is validated or ready. Mark only the scope supported by evidence as ready and explain unresolved decisions.
9. **Observe the write boundary.** Draft in conversation freely; edit project files only with scoped local-write permission and actual read-back of the saved content. Do not infer that untracked/ignored files stayed unchanged from Git status alone.

## Save a useful Product draft under an existing grant
When the confirmed project-root Scoped Workspace Grant includes Product documentation, write/read-back the Lean or Structured draft without requesting another per-file permission. Product discovery/requirement work does not need a formal implementation task just to maintain its own authorized documents. If the grant is missing, propose one named project-folder write scope and continue useful in-chat discovery pending approval. A document grant never authorizes product-scope approval, coding, provider calls or deployment. A generic "lanjut" or "ikut rekomendasi" at this point approves saving the draft, not the scope or coding; after saving, ask the single combined approval described in references/agent-governance.md ("Continuation phrases stay within the current phase").
## Demonstrable validation without premature application code
When a user needs evidence for an idea, propose the smallest validation aid: paper/mock screen, sample order flow, manual concierge test or disposable prototype. Product may produce an in-chat walkthrough or interview script; actual application code, files and deployment remain owned by Planning/Foundation/Implementation/Release and require the corresponding scoped permission. A proposed prototype is not an observed customer test; never invent validation results. Deliver a meaningful Product outcome even when coding is not yet authorized.
## Approval and learning
Routine analysis and authorized edits do not need approval for every sentence. Informed approval is needed for material product scope, data access, risk/cost changes, or changes to an approved baseline. An approved product draft is **not** authorization to code, deploy, install providers or create formal development tasks.

When a released product generates relevant measurements, customer feedback or evidence, return to **PRODUCT-FOUNDATION-01** and **PRODUCT-FOUNDATION-03** to revise the hypothesis and scope through normal change control. This is a learning loop inside existing workflows, **not a new workflow**.

## Boundaries and references
- Technology research and final selection belong to SOLUTION-06. Formal tasks and work structure belong to PLANNING-02.
- No overclaim, no unauthorized deployment, no invented interviews/test results/metrics/approval.
- Load references/research-reuse-policy.md only when reuse constraints matter and references/agent-governance.md for material authorization.
- Optional memory/knowledge setup belongs to beginnerd-setup; do not require providers to use this skill.

## Output
Use beginner-friendly descriptions of the product problem, evidence versus assumptions, proposed next experiment or requirement, unresolved material decisions and what can be done next. Keep stable IDs and internal verdict codes in artifacts or technical evidence, not default messages.

## Adapt to the user's familiarity
Apply references/familiarity-check.md in place when this skill is the first BeginNerd skill used in a project: use evident familiarity as a provisional level or the supportive Level 0, ask a familiarity question only when it materially helps, and do not send the user into a separate setup interview or build a questionnaire here. Adapt explanation depth, user-facing steps and choices presented; complete already authorized internal work without extra prompts. A level never changes permissions, safety checks, ownership or verification, and critical risks are always disclosed in plain language.
