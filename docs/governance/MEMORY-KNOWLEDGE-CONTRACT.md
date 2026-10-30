# Optional Knowledge and Persistent Memory — BeginNerd Contract

BeginNerd can use **Graphify** for project relationship discovery and **Hindsight** for continuity between sessions. Both are **opt-in integrations configured through beginnerd-setup**. Their original selection remains the recommended provider pairing when a user chooses these capabilities.

## Default: no provider dependency

- All eight skills remain useful without Graphify and Hindsight; do not require them for ordinary product, design, planning, implementation or release guidance.
- When relevant or when the user asks, beginnerd-setup asks whether the user wants project knowledge, persistent memory, both, or neither. Do not promote either provider in a new beginner's first reply when the user only wants to build something. Explicit consent, privacy/cost context and scope are required before any provider configuration or persistent write.
- Inspect existing setup and reuse it where appropriate; never automatically install duplicate providers, override settings or silently substitute another provider.
- When not opted in, record the optional provider as NOT_ENABLED and use current project documents, decision records and Git as the source of continuity. **Do not** report MEMORY_SYNC_PENDING because an optional integration was intentionally disabled.

## When a provider has been explicitly enabled and verified
1. Resolve project identity, privacy and permitted knowledge/memory scope.
2. If Hindsight is enabled, recall the last project checkpoint at the start of a session; verify it against current canonical documents and versioned evidence.
3. If Graphify is enabled, query relationships and check project isolation and freshness before relying on them.
4. Retain material decisions or checkpoints only when authorized for the configured project; verify provider acknowledgement and read-back for controlled acceptance tests.
5. Before a handoff/closure, retain an appropriate checkpoint if the memory preference requires it. If a required retain is attempted but not acknowledged, record MEMORY_SYNC_PENDING in the technical log and explain the limitation plainly to the user.
6. Provider data does not override user-approved decisions or current Git/repository evidence.

## Provider validation

- Existing-state inventory and effective permissions must be verified, not inferred from configuration text.
- Graphify: confirm project-scoped retrieval and deliberate cross-project isolation using harmless fixtures.
- Hindsight: verify approved disposable retain → acknowledgement → recall/readback.
- Idempotent setup, failure handling, cost/privacy scope and ability to disable must be tested if providers are selected.
- Missing permission or unavailable provider means the **optional integration** is PARTIAL/BLOCKED/UNVERIFIED, not that the whole application/product workflow is unusable.
- Never store secrets, credentials, unnecessary sensitive data, or live private user history in public test artifacts.

## Fallback and reporting

If providers are disabled or absent, continue from authoritative project files and the current conversation. If enabled but temporarily unreachable, explain that cross-session knowledge/memory could not be refreshed, avoid claiming successful recall/retain, and record the provider-specific failure. Do not ask the user to reconnect the tools on every unrelated skill invocation.

**Hindsight and Graphify are not canonical sources of truth and do not replace tool-side permission enforcement.**
