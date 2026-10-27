"""Read-only contract diagnostic tests, not actual provider permission enforcement."""
import copy
import importlib.util
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def load(path, module_name):
    spec = importlib.util.spec_from_file_location(module_name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.evaluate


task_eval = load(ROOT / "skills/beginnerd-implement/scripts/verify_execution_contract.py", "task_contract")
release_eval = load(ROOT / "skills/beginnerd-release/scripts/verify_release_contract.py", "release_contract")


def good_task():
    return {
        "approved_task_registry": {
            "TASK-001": {"status": "APPROVED", "dependencies": ["TASK-000"]}
        },
        "completed_task_ids": ["TASK-000"],
        "execution_request": {
            "task_id": "TASK-001", "repository": "demo/project",
            "environment": "isolated-dev", "baseline_sha": "abc123",
            "paths": ["app/src/main.py"], "action_class": "LOCAL_WRITE",
        },
        "authorization": {
            "approved": True, "approval_ref": "OWNER-EXE-01",
            "task_ids": ["TASK-001"], "repository": "demo/project",
            "environment": "isolated-dev", "baseline_sha": "abc123",
            "allowed_paths": ["app"], "action_classes": ["LOCAL_WRITE"],
        },
    }


def good_release():
    return {
        "candidate": {"source_sha": "abc123", "qa_verdict": "PASS",
                      "qa_evidence_ref": "TEST-RUN-001", "critical_findings_open": False},
        "action": {"provider": "demo-provider", "environment": "staging",
                   "audience": "testers", "source_sha": "abc123",
                   "type": "DEPLOY_RELEASE", "external_mutation": True},
        "release_authorization": {
            "approved": True, "approval_ref": "OWNER-REL-01",
            "provider": "demo-provider", "environment": "staging",
            "audience": "testers", "source_sha": "abc123",
            "rollback_plan_approved": True, "external_mutation_approved": True,
            "cost_impact_acknowledged": True,
        },
    }


class OfflinePolicyChecks(unittest.TestCase):
    def test_valid_task_record_is_advisory_only(self):
        self.assertEqual(task_eval(good_task()), [])

    def test_task_with_no_approval_rejected(self):
        p = good_task()
        p["authorization"]["approved"] = False
        self.assertIn("EXPLICIT_EXECUTION_AUTHORIZATION_REQUIRED", task_eval(p))

    def test_unapproved_formal_decomposition_rejected(self):
        p = good_task()
        p["execution_request"]["creates_formal_subtask"] = True
        self.assertIn("DECOMPOSITION_OWNER_PLANNING_02_ONLY", task_eval(p))

    def test_scope_escape_and_wrong_action_rejected(self):
        for path in ("app/../secrets.txt", "app//secrets", "/root/secrets", "app\\secrets", "other/file"):
            with self.subTest(path=path):
                p = good_task()
                p["execution_request"]["paths"] = [path]
                self.assertIn("PATH_SCOPE_MISMATCH", task_eval(p))
        p = good_task()
        p["execution_request"]["action_class"] = "PROVIDER_CONFIG"
        self.assertIn("ACTION_CLASS_NOT_AUTHORIZED", task_eval(p))

    def test_task_dependencies_and_registry_are_binding(self):
        p = good_task()
        p["completed_task_ids"] = []
        self.assertIn("TASK_DEPENDENCY_UNSATISFIED", task_eval(p))
        p = good_task()
        p["approved_task_registry"]["TASK-001"]["status"] = "DRAFT"
        self.assertIn("TASK_NOT_APPROVED_BY_PLANNING_02", task_eval(p))

    def test_recovery_attempt_requires_new_approval(self):
        p = good_task()
        p["recovery"] = {"stable_issue_id": "DEF-001", "baseline_sha": "abc123",
                         "attempts": [{"approval_ref": "APP-ONE", "result": "FAILED"}],
                         "new_attempt": True, "per_attempt_approval_ref": "APP-ONE"}
        self.assertIn("RECOVERY_APPROVAL_MUST_BE_NEW_PER_ATTEMPT", task_eval(p))
        p["recovery"]["per_attempt_approval_ref"] = ""
        self.assertIn("RECOVERY_ATTEMPT_APPROVAL_REQUIRED", task_eval(p))

    def test_third_recovery_attempt_hard_stop(self):
        p = good_task()
        p["recovery"] = {"stable_issue_id": "DEF-001", "baseline_sha": "abc123",
                         "attempts": [{"approval_ref": "A1", "result": "FAILED"},
                                      {"approval_ref": "A2", "result": "FAILED"}],
                         "new_attempt": True, "per_attempt_approval_ref": "A3"}
        errors = task_eval(p)
        self.assertIn("RECOVERY_MAX_TWO_ATTEMPTS", errors)
        self.assertIn("RECOVERY_HARD_STOP_REVIEW_REQUIRED", errors)

    def test_valid_release_is_diagnostic_only(self):
        self.assertEqual(release_eval(good_release()), [])

    def test_private_release_also_requires_separate_permission(self):
        p = good_release()
        p["release_authorization"]["approved"] = False
        p["action"]["audience"] = "private"
        p["release_authorization"]["audience"] = "private"
        self.assertIn("SEPARATE_RELEASE_APPROVAL_REQUIRED", release_eval(p))

    def test_unapproved_external_or_critical_release_blocked(self):
        p = good_release()
        p["release_authorization"]["external_mutation_approved"] = False
        p["candidate"]["critical_findings_open"] = True
        issues = release_eval(p)
        self.assertIn("EXTERNAL_MUTATION_NOT_AUTHORIZED", issues)
        self.assertIn("CRITICAL_FINDINGS_UNRESOLVED", issues)

    def test_wrong_host_and_secret_admin_not_implicit(self):
        p = good_release()
        p["action"]["provider"] = "other-provider"
        p["action"]["credential_admin"] = True
        findings = release_eval(p)
        self.assertIn("RELEASE_SCOPE_MISMATCH_PROVIDER", findings)
        self.assertIn("SECRET_ADMIN_NOT_AUTHORIZED", findings)


if __name__ == "__main__":
    unittest.main()
