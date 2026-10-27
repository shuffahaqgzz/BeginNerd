#!/usr/bin/env python3
"""Read-only release/operations scoped-authorization record diagnostics.

Never connects to or mutates a provider. A STATIC_CONTRACT_OK result is not
permission to deploy and is not proof that a service is live.
"""
import argparse
import json
import sys
from pathlib import Path


def evaluate(record):
    problems = []
    candidate = record.get("candidate", {})
    release = record.get("release_authorization", {})
    action = record.get("action", {})
    if (not candidate.get("source_sha") or candidate.get("qa_verdict") != "PASS"
            or not candidate.get("qa_evidence_ref")):
        problems.append("RELEASE_CANDIDATE_QA_NOT_VERIFIED")
    if candidate.get("critical_findings_open"):
        problems.append("CRITICAL_FINDINGS_UNRESOLVED")
    if not release.get("approved") or not release.get("approval_ref"):
        problems.append("SEPARATE_RELEASE_APPROVAL_REQUIRED")
    for field in ("provider", "environment", "audience", "source_sha"):
        if not action.get(field) or action.get(field) != release.get(field):
            problems.append("RELEASE_SCOPE_MISMATCH_" + field.upper())
    if action.get("source_sha") != candidate.get("source_sha"):
        problems.append("CANDIDATE_SHA_MISMATCH")
    if not release.get("rollback_plan_approved"):
        problems.append("ROLLBACK_PLAN_NOT_APPROVED")
    if release.get("cost_impact_acknowledged") is not True:
        problems.append("COST_IMPACT_NOT_ACKNOWLEDGED")
    if action.get("destructive") and not release.get("destructive_actions_approved"):
        problems.append("DESTRUCTIVE_SCOPE_NOT_AUTHORIZED")
    if (action.get("external_mutation") or action.get("type") in ("DEPLOY_RELEASE", "EXTERNAL_CREATE")) and not release.get("external_mutation_approved"):
        problems.append("EXTERNAL_MUTATION_NOT_AUTHORIZED")
    if action.get("credential_admin") and not release.get("secret_admin_approved"):
        problems.append("SECRET_ADMIN_NOT_AUTHORIZED")
    if action.get("creates_formal_tasks"):
        problems.append("FORMAL_TASK_CHANGE_OWNED_BY_PLANNING_02")
    return sorted(set(problems))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("record", type=Path)
    args = parser.parse_args()
    try:
        content = json.loads(args.record.read_text(encoding="utf-8"))
        if not isinstance(content, dict):
            raise ValueError("JSON object required")
        problems = evaluate(content)
    except (OSError, ValueError, TypeError, AttributeError) as exc:
        print("BLOCKED: INVALID_RECORD: " + str(exc))
        return 2
    print(json.dumps({"advisory_verdict": "BLOCKED" if problems else "STATIC_CONTRACT_OK_NOT_DEPLOYMENT", "findings": problems}, indent=2))
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
