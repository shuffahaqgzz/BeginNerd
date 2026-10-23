# Research-First & Reuse-First — Approved Addendum

Sequence: requirements & constraints → inventory existing assets → research relevant reusable solutions → evaluate alternatives (including custom implementation) → recommend → explain & obtain material approval → record technology decision → plan → verify compatibility → implement in approved scope.

- Phase 1 PF workflows collect reuse constraints (license, budget, hosting, customization), not premature final tech choices.
- Phase 2 SOLUTION-06 owns research of existing software, frameworks, packages, APIs and SDKs. Architecture, integration and security workflows assist the validation.
- Phase 3 PLANNING-02 maps approved building blocks into formal work packages and tasks; PLANNING-03 plans integration/dependency tests.
- Phase 4 foundation verifies installed/runtime compatibility and avoids duplicate scaffolding, dependencies and toolchain setup.
- Phase 5 execution uses approved building blocks; material technology changes return to the decision owner.
- Phase 6 OPS-03 assesses vulnerability advisories, vendor EOL, API changes, license obligations, data lifecycle and cost using relevance and evidence, without automatic upgrades.

Research depth is risk-adjusted. Do not require a library search for every trivial standard-library operation. Material evidence records candidate/source/date, licensing, security, compatibility, costs, rationale and approval. Missing evidence must be marked UNVERIFIED. No extra mandatory skill or workflow is introduced.
