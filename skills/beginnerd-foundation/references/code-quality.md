# FOUNDATION-03 — Code Standards & Quality Tooling

**Input:** Approved architecture/technology, Planning task registry, authorization boundary, current project/host evidence.
## Procedure
1. Read existing formatter/linter/type checker/test runner/CI conventions before adding tools; do not create parallel config for same purpose.
2. Choose risk-proportional code standards, dependency locking, secrets hygiene, formatting, lint, security checks and test tools.
3. Document minimal acceptance commands from actual project scripts; keep CI reproducible and avoid forbidden network/install steps.
4. Implement only approved configuration changes and run real checks; status must reflect executed versions and failures.
5. Differentiate 'build works', 'tests implemented', 'tests passed', accessibility/security reviewed and complete QA separately.

**Canonical output:** Repository quality configuration, commands and evidence.
**Foundation completion condition:** Quality tooling runs with expected outputs; status truthful and not called full product QA.
**Guardrails:** Before mutations require permission for exact target, preserve current settings and rollback; no duplicate tooling or unapproved formal decomposition. An artifact/checklist does not establish actual host runtime PASS.
