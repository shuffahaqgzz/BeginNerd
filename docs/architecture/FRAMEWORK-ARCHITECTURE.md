# BeginNerd Framework Architecture — Approved Six-Phase Design

BeginNerd supports beginners and mixed-experience teams through **Guided Building**. The approved design contains six modular lifecycle skills, two optional-entry companion skills and **32 workflow responsibilities**. Approval of the design does not mean implementation or runtime evaluation has passed.

| Phase | Lifecycle skill | Workflow IDs | Readiness review |
|---|---|---|---|
| Product Foundation | beginnerd-product | PRODUCT-FOUNDATION-01–04 | Product Baseline Readiness (internal G1) |
| User Experience & Solution Architecture | beginnerd-solution | SOLUTION-01–08 | Solution Design Readiness (internal G2) |
| Planning & Control | beginnerd-plan | PLANNING-01–04 | Planning Readiness |
| Development Foundation | beginnerd-foundation | FOUNDATION-01–05 | Foundation Readiness |
| Implementation & Quality Assurance | beginnerd-implement | IMPLEMENTATION-01–05 | Evidence-Based Completion |
| Release & Operations | beginnerd-release | RELEASE-01–03 and OPERATIONS-01–03 | Release, deployment and operational readiness |

**Companions:** beginnerd-ask orients a user and routes to the correct owner; beginnerd-setup handles onboarding, guidance style, and optional Graphify/Hindsight provider choices.

## Guided Building design principles

- **One skill per phase, references per workflow.** Load only the references needed for the question; a small repair does not need to restart six phases.
- **Research First and Reuse First.** SOLUTION-06 primarily owns research and selection of relevant existing software. PRODUCT-FOUNDATION-01 explores the real user problem before committing to implementation.
- **Proportional approval and iteration.** Material decisions receive informed approval; routine steps inside an authorized task or batch proceed with evidence. PLANNING-02 alone maintains formal tasks; IMPLEMENTATION-01–05 may create internal technical steps without turning them into new formal work units.
- **Contextual learning.** Runtime instructions are authored in native English; user-facing explanations match the user's selected language and avoid internal codes unless requested.
- **Optional memory and knowledge.** Graphify and Hindsight are opt-in features of beginnerd-setup. They are not hard prerequisites for the six lifecycle skills.
- **Evidence, not claims.** A planned test is not an executed test. A written guardrail is not tool-side enforcement. A source-package PASS is not a cross-harness behavioral PASS.

## Evidence priority

Approved product decisions and requirements → approved architecture/work structure → scoped action authorization → actual environment evidence and test results → agent proposals. Memory and knowledge caches assist navigation but never override canonical project artifacts.

## Handoffs and learning loops

Product Baseline Readiness supports Solution Design; Solution Design Readiness supports planning the unblocked scope. Planning and Foundation Readiness support bounded implementation; real implementation acceptance supports release assessment.

This is **iterative, not a forced waterfall**: unblocked work can continue; new discoveries can return to Product or Solution as needed. After a permitted release, OPERATIONS-01 measurement and user feedback can return to PRODUCT-FOUNDATION-01 and PRODUCT-FOUNDATION-03 to validate hypotheses and refine the next iteration. Each material scope change is reviewed with the appropriate Owner.

See docs/workflows/WORKFLOW-REGISTRY.md and docs/workflows/WORKFLOW-ID-MIGRATION.md for precise responsibilities and migration.
