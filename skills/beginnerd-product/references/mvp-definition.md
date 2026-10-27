# PRODUCT-FOUNDATION-03 — Minimum Viable Product Definition

**Trigger:** Determine the first useful product scope, what to defer, or which risk/hypothesis the smallest release should test.

## Procedure
1. Read current Product Brief, user evidence (where available), approved requirements and acceptance. Unknown market assumptions may remain explicitly open.
2. Describe the **core user value and risky assumption** this minimum viable product should test. A minimum viable product is a learning instrument, not just the smallest feature count.
3. Divide capability into **essential**, **deferred** and **out of scope**, linking each material item to existing requirement and acceptance IDs. Avoid inventing approved IDs.
4. Compare tradeoffs: expected user learning, user value, time/resource constraints, risk, existing reusable components, privacy and potential operating costs.
5. Recommend a **minimal validation path** (for example a usability walkthrough or user-observed prototype before expensive production work) when evidence is weak. Record chosen metrics or qualitative success signals, who can observe them and a next decision point. Unapproved thresholds remain TBD. A proposed experiment remains PLANNED until actual user observations are collected.
6. Obtain informed Owner approval for material inclusion/exclusion and consequences. Group related decisions; routine elaborations need not restart a formal approval ceremony.
7. Preserve the scope in PRODUCT.md or MINIMUM-VIABLE-PRODUCT-SCOPE.md with source evidence and open questions.
8. After actual release/operations measurements, compare results with hypotheses and route learning back to PRODUCT-FOUNDATION-01 and this workflow for a deliberate next iteration. No new workflow is introduced.

## Boundary
Release planning, formal implementation tasks and engineering milestones belong to PLANNING-01/02. Do not claim market validation or user testing merely because a minimum viable product was specified.
