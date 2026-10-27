# Phase 2 — Document & Change Control

- Lean: one SOLUTION-BLUEPRINT.md may suffice; Structured: split only meaningful design artifacts. Brownfield: reuse existing canonical paths and conventions.
- Traceability: requirement ID, design choice, alternatives, reason, source/version/date, proposed owner, explicit material approval reference, planned tests, risks and TBD fields.
- Explain → Interview → Approve → Record before amending approved architecture, vendor, sensitive data flow or risk decisions.
- File mutation needs scoped LOCAL_WRITE permission and readback; otherwise output a conversation draft. Do not overwrite valid project files blindly.
- If product scope changes, return to Phase 1. If work breakdown must change, return to PLANNING-02. Do not self-create formal tasks.
- Graphify relationships and Hindsight recall are non-authoritative compared with current verified documents/Git.
- Keep created artifacts DRAFT/IN_REVIEW until actual approval; planned security tests are NOT EXECUTED.
