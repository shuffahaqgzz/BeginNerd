# Setup Onboarding & Rerun

## First use — minimum conversational interview
1. Establish project identifier, user goal, whether the project is new or existing, and permission to review existing non-sensitive configuration.
2. Explain two guidance styles in plain language: **proactive guided building** (agent suggests next steps and teaches relevant concepts), or **recommendation-first** (agent waits for user goal and recommends only relevant options). Do not silently lock a preference when the user has not chosen.
3. Explain project-scope memory: what decisions/checkpoints are recorded, where they are stored, and whether it is currently configured. Ask for explicit consent to activate or change persistent memory; no consent means no activation.
4. Detect existing Graphify/Hindsight installs and project boundaries before considering new ones.
5. Recommend Lean/Structured documentation mode based on project complexity; the application and work-structure decisions belong to owning lifecycle phases, not setup.
6. Present a concise action summary and request approval for each material configuration change. Carry out only the authorized scope.

## Rerun rules
- Read current guidance choice, scope, provider configuration and evidence.
- Keep all valid existing settings unchanged unless user explicitly requests modifications.
- Compare desired vs current; avoid duplicate install or duplicate provider registration.
- Validate actual provider read/write functionality before claiming PASS.
- For differences or incompatible settings, give an impact analysis and ask before replacing.
- Record the state, not a false zero-gap result.

## Status semantics
- PASS: first-use/rerun behavior and all applicable critical integrations verified with evidence.
- PARTIAL: local guidance/config ready but one required integration or confirmation not verified.
- BLOCKED: cannot safely complete setup due to a critical condition.
- MEMORY_SYNC_PENDING: attempted required retain/checkpoint not acknowledged.
- NOT_ENABLED: user has chosen not to activate optional persistence at present; do not bypass consent.

## Handoff
The output should include chosen guidance preference, active project ID, current integration states (installed/verified/blocked), last checkpoint reference if confirmed, approved changes performed, pending approvals, and the next routed skill.
