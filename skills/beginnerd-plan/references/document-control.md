# PLANNING-04 — Document Control & Change Tracking

**Input:** Approved G1/G2 artifacts applicable to the scope, existing project state and authorized decisions.
## Procedure
1. Inventory existing canonical docs, ADRs, trackers and decision register; reuse instead of duplicating.
2. Use valid naming convention and status DRAFT/IN_REVIEW/APPROVED/SUPERSEDED; version with Git where appropriate.
3. Maintain requirement→design→task→test traceability, bounded PROJECT-STATE, approval refs and change impact.
4. For material changes: identify affected scope, explain impact, interview Owner, preserve old baseline until approval, then update canonical plan and references.
5. Graphify can assist relationship discovery, Hindsight session checkpoint only after provider verification; neither overrides Git/docs.
6. Prevent administrative overengineering: Lean combines docs; Structured split only by complexity. No new mandatory quality gate.

**Canonical output:** DOC-CONTROL.md, and DECISION-LOG.md/PROJECT-STATE.md only when justified.
**Completion criteria:** A single current canonical source per decision with traceable revisions, not paperwork for its own sake.
**Boundaries:** Do not claim task accepted or tests executed from drafting. Files/issues publishing require target-specific authorization and readback. If prerequisites fail, report PARTIAL/BLOCKED and restrict affected work.
