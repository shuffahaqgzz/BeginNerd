# Provider-Native Verification Checklist

This document is intentionally **runtime-agnostic**. No provider endpoint, schema, executable name, or side-effectful test command is assumed. Discover and inspect the actual installed adapters/tools first.

## Preflight — read-only
- Inspect provider registration and available tool methods.
- Record actual versions, hosts/runtime identifiers, namespace/project scope, known permissions, health metadata and credential source **without exposing secrets**.
- Compare configuration with approved project scope; do not use global namespace by default.
- Inspect whether setup is already complete to avoid reinstall.

## Graphify knowledge provider
- Validate connection using a provider-native read-only capability.
- Inspect an approved project-scoped knowledge relationship and its source/freshness metadata.
- Confirm that unapproved project scopes are not traversed.
- If a test write is unavoidable, require consent and use a disposable, clearly labeled test dataset; clean up only if authorized.

## Hindsight memory provider
- Require explicit prior approval to activate or write persistent project memory.
- Use a disposable test project namespace or agreed test identifier.
- Retain one non-sensitive checkpoint with an unambiguous marker; preserve returned acknowledgement.
- Recall that marker in a separate query, check scope, timestamp and factual content; document differences.
- Verify behavior when write fails, provider is unreachable or the acknowledgement is ambiguous; report MEMORY_SYNC_PENDING when applicable.
- Do not infer memory success from an HTTP connection, configuration file or a model response alone.

## Continuity test
- Start a new agent session with the same authorized project scope.
- Observe actual recall, compare it against current canonical files, and verify outdated/contradictory facts are not treated as authority.
- Retain meaningful changes before handoff, verify acknowledgement, and record a sanitized evidence ref.

## Decision table
- **PASS:** appropriate provider functions and permissions actually verified.
- **PARTIAL:** one functional provider check or second-session proof remains outstanding.
- **BLOCKED:** critical provider/prerequisite fails and scope cannot safely continue.
- **UNVERIFIED:** no direct evidence.
- **MEMORY_SYNC_PENDING:** an expected retain has no confirmed acknowledgement.

Do not paste credentials, raw private memory, tokens, or sensitive project logs into issues, PRs, or public test artifacts.
