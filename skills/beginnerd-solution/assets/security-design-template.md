# SECURITY-ARCHITECTURE — [Project]

**Your current status:** Safety design proposal; not yet security-tested.
**Technical record:** DRAFT · **Approval:** PENDING

## Plain-language summary
- **What information matters most:** TBD
- **Who should be allowed to do what:** TBD
- **What can go wrong:** TBD
- **How the system should defend against that:** TBD
- **How we will check the defenses:** TBD (planned, not executed)
- **What needs your decision:** TBD

For login systems, use appropriate password hashing for stored passwords, protected secrets, access control, session safety and negative tests. A plaintext reusable admin password in an environment file is not secure credential storage; a config file is not proof of safety. No live secret management without permission.

## Technical appendix — threat and control trace
**Risk profile:** Basic / Application / Enhanced based on actual risk.
| Product ID | Threat | Security requirement | Proposed control | Planned security test | Risk and owner |
|---|---|---|---|---|---|
| REQUIREMENTS-TBD | THREAT-001 | SECURITY-REQUIREMENTS-001 | SECURITY-CONTROL-001 | SECURITY-TEST-001 | UNVERIFIED/TBD |
An unmitigated critical risk blocks G2 PASS. Designed does not mean implemented/tested.
