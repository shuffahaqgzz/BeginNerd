# Full-Length Workflow Identifier Migration — 27 October 2026

**Approved by the BeginNerd Owner in response to reviewer T1.** This is a naming migration, **not a new workflow, phase, artifact gate, or retroactive deletion of evidence**.

## Stable identifier aliases

| Legacy prefix | Canonical prefix | Workflows |
|---|---|---|
| PF- | PRODUCT-FOUNDATION- | 01–04 |
| IMPLEMENT- | IMPLEMENTATION- | 01–05 |
| OPS- | OPERATIONS- | 01–03 |

SOLUTION-, PLANNING-, FOUNDATION- and RELEASE- are already complete words and remain unchanged. The total stays **32**. Existing references in historical evidence, approved external product documents or already-issued task/test records remain readable as aliases; do not silently rename signed evidence or rewrite historical approvals.

## Migration and interoperability
1. New canonical documents, skill reference instructions, routing and the workflow registry use full-length IDs.
2. Read legacy IDs and map them to the canonical equivalent during discovery/traceability. Preserve the raw ID and the mapping when external artifacts depend on it; never count both as different requirements or tasks.
3. New generated artifacts write only canonical workflow IDs. Existing task IDs, requirement IDs, acceptance IDs and historical issue IDs do **not** change under this migration.
4. A legacy H-01/H02-03 scenario identifier or BN-DEC decision ID belongs to historical test/decision provenance, not a workflow ID. It may remain in an evidence register but should not appear in beginner-facing explanations.
5. When a user asks what a code means, explain the **full workflow name and purpose**, not just a longer code.

A script or test that parses workflow prefixes must recognize the complete canonical prefix, and use these aliases only for reading pre-migration evidence.
