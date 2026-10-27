#!/usr/bin/env python3
"""Read-only BeginNerd execution authorization sanity checker.

Input JSON is a diagnostic fixture, NOT a security enforcement point. This tool
never runs tasks, mutates resources, or grants rights. Runtime policies and
provider-side permissions MUST still be independently verified.
"""
import argparse
import json
import sys
from pathlib import Path


def evaluate(payload):
    errors = []
    registry = payload.get("approved_task_registry", {})
    request = payload.get("execution_request", {})
    authorization = payload.get("authorization", {})
    task_id = request.get("task_id")
    task = registry.get(task_id, {}) if isinstance(registry, dict) else {}
    if not task_id or not task:
        errors.append("TASK_NOT_IN_APPROVED_REGISTRY")
    if not authorization.get("approved") or not authorization.get("approval_ref"):
        errors.append("EXPLICIT_EXECUTION_AUTHORIZATION_REQUIRED")
    if task_id not in authorization.get("task_ids", []):
        errors.append("TASK_NOT_AUTHORIZED_FOR_BATCH")
    if request.get("repository") != authorization.get("repository"):
        errors.append("REPOSITORY_SCOPE_MISMATCH")
    if request.get("environment") != authorization.get("environment"):
        errors.append("ENVIRONMENT_SCOPE_MISMATCH")
    if not request.get("baseline_sha") or request.get("baseline_sha") != authorization.get("baseline_sha"):
        errors.append("BASELINE_SCOPE_MISMATCH")
    allowed_paths = authorization.get("allowed_paths", [])
    proposed_paths = request.get("paths", [])
    if not proposed_paths or not allowed_paths:
        errors.append("PATH_SCOPE_UNSPECIFIED")
    elif any(not isinstance(p, str) or not any(p == ap or p.startswith(ap.rstrip("/") + "/") for ap in allowed_paths if isinstance(ap, str) and ap and ".." not in ap) for p in proposed_paths):
        errors.append("PATH_SCOPE_MISMATCH")
    if request.get("creates_formal_task") or request.get("creates_formal_subtask"):
        errors.append("DECOMPOSITION_OWNER_PLANNING_02_ONLY")
    if request.get("deploys_externally"):
        errors.append("RELEASE_AUTHORIZATION_SEPARATE")
    if task and any(dep not in payload.get("completed_task_ids", []) for dep in task.get("dependencies", [])):
        errors.append("TASK_DEPENDENCY_UNSATISFIED")
    rec = payload.get("recovery")
    if rec:
        attempts = rec.get("attempts", [])
        if not isinstance(attempts, list):
            errors.append("INVALID_RECOVERY_HISTORY")
        elif len(attempts) >= 2 and any(a.get("result") == "FAILED" for a in attempts[-1:]):
            errors.append("RECOVERY_HARD_STOP_REVIEW_REQUIRED")
        if rec.get("new_attempt"):
            if len(attempts) >= 2:
                errors.append("RECOVERY_MAX_TWO_ATTEMPTS")
            if not rec.get("per_attempt_approval_ref"):
                errors.append("RECOVERY_ATTEMPT_APPROVAL_REQUIRED")
            if not rec.get("stable_issue_id") or not rec.get("baseline_sha"):
                errors.append("RECOVERY_IDENTITY_AND_BASELINE_REQUIRED")
    return sorted(set(errors))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("input", type=Path, help="JSON of approved registry + proposed action")
    args = parser.parse_args()
    try:
        record = json.loads(args.input.read_text(encoding="utf-8"))
        errors = evaluate(record)
    except (OSError, ValueError, TypeError, AttributeError) as exc:
        print("BLOCKED: INVALID_RECORD: " + str(exc))
        return 2
    print(json.dumps({"advisory_verdict": "BLOCKED" if errors else "STATIC_CONTRACT_OK_NOT_AUTHORIZED_BY_TOOL", "findings": errors}, indent=2))
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
