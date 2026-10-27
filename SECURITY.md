# Security Policy — BeginNerd

BeginNerd is an open-source AI coding-agent workflow framework. Security boundaries are described in its governance contracts, but the six-phase runtime is **not yet fully verified**. Source instruction text cannot substitute provider-side approval gates, restricted tool permissions or safe test environments.

## Reporting a suspected vulnerability
Prefer GitHub **private vulnerability reporting** under the repository Security tab **if the maintainer has enabled it**. Verify the private reporting route is available before sharing sensitive details. If it is not available, do not publish credentials, exploit payloads or private reproduction logs in public issues/PRs; request a safe private channel from the maintainer through an appropriate existing contact method.

Never include actual bearer tokens, passwords, Hindsight memory, user project data, or private host configs in vulnerability reports. The project does not currently claim a published incident response SLA or guaranteed patch timelines.

## What to include
Affected source commit/tag, relevant skill/workflow, observable behavior, impact, safest minimal reproduction, expected vs actual authorization, sanitized tool traces and mitigation suggestions. Do not test an external provider by creating/deploying a resource without approval.

## Scope and boundaries
- Security test suites and static CI are not proof that Codex, Sites, Graphify or Hindsight provider permissions are secure.
- The H-01 historical unauthorized private deployment finding demonstrates that runtime testing must inspect **attempted** prohibited tool use, not only tool-denied outcomes.
- Each corrective remediation after a declared verification failure requires separate Owner approval (maximum two attempts), with critical findings disclosed and evidence retained.

Security advisories for published versions and disclosure contact settings are **pending maintainer configuration** before v1.0 can claim security policy operational readiness.
