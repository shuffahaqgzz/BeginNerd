# Phase 5 BN-DEC-009.5M — Extended Bounded Recovery

**Definition:** A corrective remediation attempt is one distinct scoped approach after a verification checkpoint declares a failure; routine coding corrections *before* declared failure are not automatically remediation attempts.

1. Record stable issue ID, execution baseline SHA, task ID, failure evidence, impact and already attempted approaches.
2. Propose one bounded diagnosis/fix/verification plan with risk, files, environment and rollback; seek explicit Owner approval **for attempt 1**.
3. Execute exactly the approved scope; verify outcome and record evidence. If failed, preserve history, status PARTIAL/BLOCKED.
4. Explain why attempt 1 failed; propose distinct bounded approach and seek **fresh approval for attempt 2**.
5. If attempt 2 fails: **HARD STOP**, REVIEW_REQUIRED and NOT_ACCEPTED. No attempt 3, no renaming, branch switching, agent rotation or hidden alternative strategies to avoid limit.
6. If new tasks or architecture are needed, return to PLANNING-02 or Phase 2 with Owner approval. Independent already-approved tasks may proceed only if safe.

**Always preserve:** issue/baseline, attempt number, authorization ref, expected/observed, tests, timestamps, changes and blockers. No silent retry. Pure read-only example checker in scripts/verify_execution_contract.py can detect malformed approval, but runtime enforcement still requires actual tool permission controls.
