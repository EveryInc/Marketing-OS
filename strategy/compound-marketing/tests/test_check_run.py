from __future__ import annotations

import importlib.util
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch


SCRIPT = Path(__file__).parents[1] / "scripts" / "check_run.py"


def load_module():
    spec = importlib.util.spec_from_file_location("check_run", SCRIPT)
    if spec is None or spec.loader is None:
        raise RuntimeError("could not load check_run.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


CHECK_RUN = load_module()


class LegacyComparisonAdapter:
    """Exercise the legacy algorithm without exposing V1 as public proof."""

    def __getattr__(self, name):
        return getattr(CHECK_RUN, name)

    def compare_records(self, baseline, followup, **kwargs):
        return CHECK_RUN._compare_v1(baseline, followup, **kwargs)


LEGACY_CHECK_RUN = LegacyComparisonAdapter()


def run_record(
    run_id: str,
    *,
    workflow: str = "gtm",
    review_minutes: int | None = 100,
    first_pass: bool | None = False,
    defects: int | None = 2,
    inherited: int = 0,
    accepted_inherited: int = 0,
    comparable_to: str | None = None,
    publishable_claim: bool = False,
    evidence_status: str = "prospective",
    independent_operator: bool = False,
    artifact_fidelity_verified: bool = True,
):
    return {
        "schema_version": 1,
        "run_id": run_id,
        "project": f"Project {run_id}",
        "workflow": workflow,
        "evidence_status": evidence_status,
        "decisions": [
            {
                "id": "D1",
                "decision": "Lead with the customer problem.",
                "owner": "Douglas",
                "source": "approved strategy",
                "status": "locked",
                "applies_to": ["strategy_to_market"],
            }
        ],
        "stages": {
            "context_to_strategy": {
                "status": "approved",
                "artifact": "strategy.md",
                "output_decision_ids": ["D1"],
            },
            "strategy_to_market": {
                "status": "approved",
                "artifact": "gtm.md",
                "preserved_decision_ids": ["D1"],
            },
            "market_to_memory": {
                "status": "complete",
                "artifact": "result.md",
                "learning_classification": "result_record",
            },
        },
        "metrics": {
            "human_review_minutes": review_minutes,
            "first_pass_accepted": first_pass,
            "critical_defects": defects,
            "inherited_decisions": inherited,
            "accepted_inherited_decisions": accepted_inherited,
            "independent_operator": independent_operator,
            "artifact_fidelity_verified": artifact_fidelity_verified,
            "artifact_fidelity_verifier": (
                "Douglas" if artifact_fidelity_verified else None
            ),
        },
        "proof": {
            "comparable_to": comparable_to,
            "accepted_inherited_decision_ids": ["D1"] if accepted_inherited else [],
            "publishable_claim": publishable_claim,
        },
    }


def write_artifact_receipts(root: Path, record: dict) -> Path:
    """Write the shared files required to verify artifact fidelity."""

    run_root = root / record["run_id"]
    run_root.mkdir(parents=True)
    decision_path = run_root / "decision-record.md"
    decision_path.write_text("# Decision record\n\nVersion: v1\n", encoding="utf-8")
    record["decision_record"] = {"path": "decision-record.md", "version": "v1"}

    for stage_name, stage in record["stages"].items():
        if stage["status"] == "not_applicable":
            continue
        if stage_name == "context_to_strategy":
            decision_ids = stage["output_decision_ids"]
        elif stage_name == "strategy_to_market":
            decision_ids = stage["preserved_decision_ids"]
        else:
            decision_ids = []
        receipt_name = f"{stage_name}-receipt.json"
        stage["artifact_receipt"] = receipt_name
        (run_root / receipt_name).write_text(
            json.dumps(
                {
                    "schema_version": 1,
                    "run_id": record["run_id"],
                    "stage": stage_name,
                    "artifact": stage["artifact"],
                    "decision_record": {
                        "path": "decision-record.md",
                        "version": "v1",
                    },
                    "decision_ids": decision_ids,
                    "verified_by": "Douglas",
                    "verified_at": "2026-08-21T12:00:00-04:00",
                }
            ),
            encoding="utf-8",
        )

    record_path = run_root / "run.json"
    record_path.write_text(json.dumps(record), encoding="utf-8")
    return record_path


class ValidateRunTests(unittest.TestCase):
    module = CHECK_RUN

    def test_retrospective_baseline_can_be_valid_but_incomplete(self):
        record = run_record(
            "baseline",
            review_minutes=None,
            first_pass=None,
            defects=None,
            evidence_status="retrospective",
        )
        result = self.module.validate_record(record)
        self.assertTrue(result["valid"])
        self.assertFalse(result["proof_ready"])
        self.assertIn("human_review_minutes is missing", result["warnings"])

    def test_missing_locked_decision_in_downstream_artifact_fails(self):
        record = run_record("broken")
        record["stages"]["strategy_to_market"]["preserved_decision_ids"] = []
        result = self.module.validate_record(record)
        self.assertFalse(result["valid"])
        self.assertIn("locked decision D1 was not preserved", result["errors"])

    def test_missing_locked_decision_in_strategy_output_fails(self):
        record = run_record("broken")
        record["stages"]["context_to_strategy"]["output_decision_ids"] = []
        result = self.module.validate_record(record)
        self.assertFalse(result["valid"])
        self.assertIn(
            "locked decision D1 is missing from strategy output", result["errors"]
        )

    def test_unknown_decision_status_and_stage_fail(self):
        record = run_record("broken")
        record["decisions"][0]["status"] = "lockd"
        record["decisions"][0]["applies_to"] = ["market"]
        result = self.module.validate_record(record)
        self.assertFalse(result["valid"])
        self.assertIn("decision D1 has invalid status", result["errors"])
        self.assertIn("decision D1 applies_to has an invalid stage", result["errors"])

    def test_publishable_claim_requires_complete_prospective_proof(self):
        record = run_record(
            "overclaim",
            review_minutes=None,
            comparable_to="baseline",
            publishable_claim=True,
            evidence_status="retrospective",
        )
        result = self.module.validate_record(record)
        self.assertFalse(result["valid"])
        self.assertIn(
            "publishable claim must be evaluated with the compare command",
            result["errors"],
        )

    def test_complete_followup_is_comparison_ready_but_not_proof_ready_alone(self):
        record = run_record(
            "followup",
            first_pass=True,
            defects=0,
            inherited=1,
            accepted_inherited=1,
            comparable_to="baseline",
            independent_operator=True,
        )
        result = self.module.validate_record(record)
        self.assertTrue(result["valid"])
        self.assertTrue(result["comparison_ready"])
        self.assertFalse(result["proof_ready"])

    def test_non_finite_review_minutes_are_invalid(self):
        for value in (float("nan"), float("inf"), float("-inf")):
            with self.subTest(value=value):
                result = self.module.validate_record(
                    run_record("invalid", review_minutes=value)
                )
                self.assertFalse(result["valid"])
                self.assertIn(
                    "human_review_minutes must be a non-negative number or null",
                    result["errors"],
                )

    def test_malformed_nested_values_fail_without_crashing(self):
        cases = {
            "stage": lambda record: record["stages"].update(
                {"context_to_strategy": []}
            ),
            "applies_to": lambda record: record["decisions"][0].update(
                {"applies_to": "strategy_to_market"}
            ),
            "proof": lambda record: record.update({"proof": []}),
            "metrics": lambda record: record.update({"metrics": []}),
        }
        for name, mutate in cases.items():
            with self.subTest(name=name):
                record = run_record("invalid")
                mutate(record)
                result = self.module.validate_record(record)
                self.assertFalse(result["valid"])

    def test_duplicate_decision_ids_fail_validation(self):
        record = run_record("invalid")
        record["decisions"].append(dict(record["decisions"][0]))
        result = self.module.validate_record(record)
        self.assertFalse(result["valid"])
        self.assertIn("duplicate decision id D1", result["errors"])


class CompareRunTests(unittest.TestCase):
    module = LEGACY_CHECK_RUN

    def test_twenty_percent_reduction_with_no_regression_qualifies(self):
        baseline = run_record("baseline", review_minutes=100, defects=2)
        followup = run_record(
            "followup",
            review_minutes=80,
            first_pass=True,
            defects=1,
            inherited=1,
            accepted_inherited=1,
            comparable_to="baseline",
            publishable_claim=True,
            independent_operator=True,
        )
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            baseline_path = write_artifact_receipts(root, baseline)
            followup_path = write_artifact_receipts(root, followup)
            result = self.module.compare_records(
                baseline,
                followup,
                baseline_path=baseline_path,
                followup_path=followup_path,
            )
        self.assertTrue(result["qualifies"])
        self.assertTrue(result["proof_ready"])
        self.assertEqual(20.0, result["review_reduction_percent"])

    def test_compounding_proof_requires_resolvable_artifact_receipts(self):
        baseline = run_record("baseline", defects=2)
        followup = run_record(
            "followup",
            review_minutes=70,
            first_pass=True,
            defects=1,
            inherited=1,
            accepted_inherited=1,
            comparable_to="baseline",
            independent_operator=True,
        )
        result = self.module.compare_records(baseline, followup)
        self.assertFalse(result["qualifies"])
        self.assertIn(
            "baseline artifact receipts cannot be verified without a record path",
            result["failures"],
        )

    def test_artifact_receipt_decision_mismatch_fails_closed(self):
        baseline = run_record("baseline", defects=2)
        followup = run_record(
            "followup",
            review_minutes=70,
            first_pass=True,
            defects=1,
            inherited=1,
            accepted_inherited=1,
            comparable_to="baseline",
            independent_operator=True,
        )
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            baseline_path = write_artifact_receipts(root, baseline)
            followup_path = write_artifact_receipts(root, followup)
            receipt_path = (
                followup_path.parent / "strategy_to_market-receipt.json"
            )
            receipt = json.loads(receipt_path.read_text(encoding="utf-8"))
            receipt["decision_ids"] = []
            receipt_path.write_text(json.dumps(receipt), encoding="utf-8")
            result = self.module.compare_records(
                baseline,
                followup,
                baseline_path=baseline_path,
                followup_path=followup_path,
            )
        self.assertFalse(result["qualifies"])
        self.assertIn(
            "followup stage strategy_to_market artifact receipt decision IDs do not match",
            result["failures"],
        )

    def test_artifact_receipt_cannot_escape_the_run_directory(self):
        baseline = run_record("baseline", defects=2)
        followup = run_record(
            "followup",
            review_minutes=70,
            first_pass=True,
            defects=1,
            inherited=1,
            accepted_inherited=1,
            comparable_to="baseline",
            independent_operator=True,
        )
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            baseline_path = write_artifact_receipts(root, baseline)
            followup_path = write_artifact_receipts(root, followup)
            followup["stages"]["strategy_to_market"]["artifact_receipt"] = (
                "../baseline/strategy_to_market-receipt.json"
            )
            result = self.module.compare_records(
                baseline,
                followup,
                baseline_path=baseline_path,
                followup_path=followup_path,
            )
        self.assertFalse(result["qualifies"])
        self.assertIn(
            "followup stage strategy_to_market artifact receipt is unreadable",
            result["failures"],
        )

    def test_less_than_twenty_percent_reduction_does_not_qualify(self):
        baseline = run_record("baseline", review_minutes=100)
        followup = run_record(
            "followup",
            review_minutes=85,
            inherited=1,
            accepted_inherited=1,
            comparable_to="baseline",
            independent_operator=True,
        )
        result = self.module.compare_records(baseline, followup)
        self.assertFalse(result["qualifies"])
        self.assertIn("review burden fell by less than 20%", result["failures"])

    def test_rounding_does_not_turn_sub_threshold_reduction_into_proof(self):
        baseline = run_record("baseline", review_minutes=100)
        followup = run_record(
            "followup",
            review_minutes=80.004,
            inherited=1,
            accepted_inherited=1,
            comparable_to="baseline",
            independent_operator=True,
        )
        result = self.module.compare_records(baseline, followup)
        self.assertFalse(result["qualifies"])
        self.assertEqual(20.0, result["review_reduction_percent"])
        self.assertIn("review burden fell by less than 20%", result["failures"])

    def test_different_workflows_are_not_comparable(self):
        baseline = run_record("baseline", workflow="brand-strategy")
        followup = run_record(
            "followup",
            workflow="gtm",
            inherited=1,
            accepted_inherited=1,
            comparable_to="baseline",
        )
        result = self.module.compare_records(baseline, followup)
        self.assertFalse(result["qualifies"])
        self.assertIn("workflow types do not match", result["failures"])

    def test_retrospective_followup_cannot_support_compounding_claim(self):
        baseline = run_record("baseline")
        followup = run_record(
            "followup",
            review_minutes=70,
            first_pass=True,
            defects=1,
            inherited=1,
            accepted_inherited=1,
            comparable_to="baseline",
            evidence_status="retrospective",
            independent_operator=True,
        )
        result = self.module.compare_records(baseline, followup)
        self.assertFalse(result["qualifies"])
        self.assertIn("followup evidence was not prospective", result["failures"])

    def test_unfinished_followup_stage_cannot_qualify(self):
        baseline = run_record("baseline")
        followup = run_record(
            "followup",
            review_minutes=70,
            inherited=1,
            accepted_inherited=1,
            comparable_to="baseline",
            independent_operator=True,
        )
        followup["stages"]["market_to_memory"]["status"] = "in_progress"
        result = self.module.compare_records(baseline, followup)
        self.assertFalse(result["qualifies"])
        self.assertIn(
            "followup stage market_to_memory is unfinished", result["failures"]
        )

    def test_malformed_nested_records_fail_without_crashing(self):
        baseline = run_record("baseline")
        followup = run_record("followup")
        followup["proof"] = []
        followup["metrics"] = "invalid"
        result = self.module.compare_records(baseline, followup)
        self.assertFalse(result["qualifies"])
        self.assertIn("followup record is invalid", result["failures"])

    def test_non_list_decisions_fail_comparison_without_crashing(self):
        for side in ("baseline", "followup"):
            with self.subTest(side=side):
                baseline = run_record("baseline")
                followup = run_record("followup")
                if side == "baseline":
                    baseline["decisions"] = None
                else:
                    followup["decisions"] = None
                result = self.module.compare_records(baseline, followup)
                self.assertFalse(result["qualifies"])
                self.assertIn(f"{side} record is invalid", result["failures"])

    def test_inherited_ids_must_exist_in_both_runs_and_market_artifact(self):
        baseline = run_record("baseline")
        baseline["decisions"][0]["id"] = "BASE-D1"
        baseline["stages"]["context_to_strategy"]["output_decision_ids"] = ["BASE-D1"]
        baseline["stages"]["strategy_to_market"]["preserved_decision_ids"] = [
            "BASE-D1"
        ]
        followup = run_record(
            "followup",
            review_minutes=70,
            inherited=1,
            accepted_inherited=1,
            comparable_to="baseline",
            independent_operator=True,
        )
        result = self.module.compare_records(baseline, followup)
        self.assertFalse(result["qualifies"])
        self.assertIn(
            "accepted inherited decision IDs are absent from the baseline",
            result["failures"],
        )

    def test_inherited_decision_must_keep_locked_meaning_and_source(self):
        for field, value, expected in (
            (
                "decision",
                "Lead with a different problem.",
                "accepted inherited decision D1 changed meaning or source",
            ),
            (
                "source",
                "new strategy",
                "accepted inherited decision D1 changed meaning or source",
            ),
            (
                "status",
                "rejected",
                "accepted inherited decision D1 is not locked in followup",
            ),
        ):
            with self.subTest(field=field):
                baseline = run_record("baseline")
                followup = run_record(
                    "followup",
                    review_minutes=70,
                    inherited=1,
                    accepted_inherited=1,
                    comparable_to="baseline",
                    independent_operator=True,
                )
                followup["decisions"][0][field] = value
                result = self.module.compare_records(baseline, followup)
                self.assertFalse(result["qualifies"])
                self.assertIn(expected, result["failures"])


class GovernedRunV2Tests(unittest.TestCase):
    module = CHECK_RUN

    def make_ready_v2(
        self,
        root: Path,
        *,
        project: str,
        operator: str,
        minutes: int,
        force_new: bool = False,
        comparable_to: str | None = None,
        decision: str = "Lead with learning.",
        artifact_reference: str = "artifact.md",
    ) -> Path:
        record_path = self.module.initialize_run(
            root,
            project=project,
            workflow_family="gtm",
            routed_output="gtm_plan",
            operator=operator,
            force_new=force_new,
        )
        if artifact_reference == "artifact.md":
            artifact_path = record_path.parent / artifact_reference
            artifact_path.write_text("# Accepted artifact\n", encoding="utf-8")
        record = self.module.load_json(record_path)
        record["sources"] = [
            {
                "id": "S1",
                "owner": "dan",
                "location": "notion://strategy",
                "authority": "company_strategy",
                "freshness": "2026-08-21",
                "status": "confirmed",
            }
        ]
        record["decisions"] = [
            {
                "id": "D1",
                "decision": decision,
                "owner": "douglas",
                "source_id": "S1",
                "status": "locked",
            }
        ]
        record["artifact"].update(
            {
                "scope": "launch",
                "primary_audience": "operators",
                "owner": "douglas",
            }
        )
        record["metrics"].update(
            {
                "human_review_minutes": minutes,
                "first_pass_accepted": True,
                "critical_defects": 0,
            }
        )
        record["metrics"]["primary"].update(
            {
                "name": "human_review_minutes",
                "unit": "minutes",
                "method": "timer",
                "declared_by": "douglas",
                "declared_at": "2026-08-21T10:00:00+00:00",
                "work_started_at": "2026-08-21T11:00:00+00:00",
                "observed_at": "2026-08-21T12:00:00+00:00",
                "value": minutes,
                "measurement_window": "one run",
                "decision_date": "2026-08-21",
            }
        )
        record["proof"]["dimensions"].update(
            {
                "scope": "launch",
                "primary_audience": "operators",
                "measurement_method": "timer",
            }
        )
        if comparable_to:
            record["proof"].update(
                {
                    "comparable_to": comparable_to,
                    "accepted_inherited_decision_ids": ["D1"],
                    "comparability_rationale": (
                        "Same artifact, audience, scope, and measure."
                    ),
                }
            )
        record_path.write_text(json.dumps(record), encoding="utf-8")
        self.module.render_run(record_path)
        self.module.transition_run(record_path, "strategy_pending")
        record = self.module.load_json(record_path)
        record["approvals"]["strategy"].update(
            {
                "approved_by": "human-reviewer",
                "approved_at": "2026-08-21T12:30:00+00:00",
                "record_digest": self.module.governance_digest(record),
            }
        )
        record_path.write_text(json.dumps(record), encoding="utf-8")
        self.module.transition_run(record_path, "strategy_approved")
        self.module.transition_run(record_path, "artifact_pending")
        receipt_path = self.module.scaffold_receipt(
            record_path, stage="strategy_to_market", artifact=artifact_reference
        )
        receipt = json.loads(receipt_path.read_text(encoding="utf-8"))
        receipt.update(
            {
                "verified_by": "human-reviewer",
                "verified_at": "2026-08-21T12:30:00+00:00",
            }
        )
        if receipt["artifact"].get("kind") == "remote":
            receipt["artifact"]["revision"] = "rev-1"
        receipt_path.write_text(json.dumps(receipt), encoding="utf-8")
        record = self.module.load_json(record_path)
        digest = self.module.governance_digest(record)
        binding_digest = self.module._artifact_binding_digest(receipt["artifact"])
        for name in ("artifact", "fidelity"):
            record["approvals"][name].update(
                {
                    "approved_by": "human-reviewer",
                    "approved_at": "2026-08-21T12:30:00+00:00",
                    "record_digest": digest,
                    "artifact_binding": binding_digest,
                }
            )
        if comparable_to:
            record["approvals"]["comparability"].update(
                {
                    "approved_by": "human-reviewer",
                    "approved_at": "2026-08-21T12:30:00+00:00",
                    "record_digest": self.module.approval_digest(
                        record, "comparability"
                    ),
                }
            )
        record_path.write_text(json.dumps(record), encoding="utf-8")
        self.module.transition_run(record_path, "artifact_approved")
        self.module.transition_run(record_path, "measuring")
        self.module.transition_run(record_path, "closed")
        return record_path

    def test_init_is_idempotent_and_discoverable(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            first = self.module.initialize_run(
                root,
                project="Every Brand Book",
                workflow_family="brand_strategy",
                routed_output="one_pager",
                operator="douglas",
            )
            second = self.module.initialize_run(
                root,
                project="Every Brand Book",
                workflow_family="brand_strategy",
                routed_output="one_pager",
                operator="douglas",
            )
            self.assertEqual(first, second)
            self.assertTrue((first.parent / "run.md").is_file())
            self.assertTrue((first.parent / "decision-record.md").is_file())
            found = self.module.discover_run(
                root, project="Every Brand Book", workflow_family="brand_strategy"
            )
            self.assertEqual(first, found)

    def test_concurrent_init_creates_one_active_run(self):
        with tempfile.TemporaryDirectory() as directory:
            command = [
                sys.executable,
                str(SCRIPT),
                "init",
                directory,
                "--project",
                "Launch",
                "--workflow",
                "gtm",
                "--route",
                "gtm_plan",
                "--operator",
                "douglas",
            ]
            first = subprocess.Popen(command, stdout=subprocess.PIPE, text=True)
            second = subprocess.Popen(command, stdout=subprocess.PIPE, text=True)
            first_stdout, _ = first.communicate(timeout=10)
            second_stdout, _ = second.communicate(timeout=10)
            self.assertEqual(0, first.returncode)
            self.assertEqual(0, second.returncode)
            self.assertEqual(
                json.loads(first_stdout)["record_path"],
                json.loads(second_stdout)["record_path"],
            )
            records = list(Path(directory).glob(".compound-marketing/*/run.json"))
            self.assertEqual(1, len(records))

    def test_discovery_ignores_symlinked_records_outside_the_run_root(self):
        with tempfile.TemporaryDirectory() as directory, tempfile.TemporaryDirectory() as outside:
            root = Path(directory)
            run_root = root / ".compound-marketing"
            run_root.mkdir()
            outside_run = Path(outside) / "escaped"
            outside_run.mkdir()
            record = self.module._new_v2_record(
                run_id="escaped",
                project="Launch",
                workflow_family="gtm",
                routed_output="gtm_plan",
                operator="attacker",
            )
            (outside_run / "run.json").write_text(json.dumps(record), encoding="utf-8")
            (run_root / "escaped").symlink_to(outside_run, target_is_directory=True)
            self.assertIsNone(
                self.module.discover_run(
                    root, project="Launch", workflow_family="gtm"
                )
            )

    def test_multiple_matching_runs_fail_closed(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            first = self.module.initialize_run(
                root,
                project="Every Brand Book",
                workflow_family="brand_strategy",
                routed_output="one_pager",
                operator="douglas",
            )
            record = json.loads(first.read_text(encoding="utf-8"))
            duplicate = first.parents[1] / "duplicate"
            duplicate.mkdir()
            (duplicate / "run.json").write_text(json.dumps(record), encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "multiple unfinished runs"):
                self.module.discover_run(
                    root,
                    project="Every Brand Book",
                    workflow_family="brand_strategy",
                )

    def test_ambiguous_discovery_is_an_ineligible_cli_result(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            for force_new in (False, True):
                self.module.initialize_run(
                    root,
                    project="Launch",
                    workflow_family="gtm",
                    routed_output="gtm_plan",
                    operator="douglas",
                    force_new=force_new,
                )
            result = subprocess.run(
                [
                    sys.executable,
                    str(SCRIPT),
                    "discover",
                    str(root),
                    "--project",
                    "Launch",
                    "--workflow",
                    "gtm",
                ],
                capture_output=True,
                text=True,
                check=False,
            )
            self.assertEqual(1, result.returncode)

    def test_unsigned_starter_is_honest_and_not_operational(self):
        with tempfile.TemporaryDirectory() as directory:
            record_path = self.module.initialize_run(
                Path(directory),
                project="Launch",
                workflow_family="gtm",
                routed_output="gtm_plan",
                operator="douglas",
            )
            result = self.module.validate_record(
                self.module.load_json(record_path), record_path=record_path
            )
            self.assertTrue(result["valid"])
            self.assertFalse(result["structural_ready"])
            self.assertFalse(result["operational_ready"])
            self.assertIn("SOURCE_REQUIRED", result["failure_codes"])

    def test_blocked_run_restores_prior_state_and_terminal_is_immutable(self):
        with tempfile.TemporaryDirectory() as directory:
            record_path = self.module.initialize_run(
                Path(directory),
                project="Launch",
                workflow_family="gtm",
                routed_output="gtm_plan",
                operator="douglas",
            )
            self.module.transition_run(record_path, "strategy_pending")
            self.module.transition_run(record_path, "blocked", reason="source conflict")
            blocked = self.module.load_json(record_path)
            self.assertEqual("strategy_pending", blocked["lifecycle"]["prior_status"])
            self.module.transition_run(record_path, "resume")
            resumed = self.module.load_json(record_path)
            self.assertEqual("strategy_pending", resumed["lifecycle"]["status"])
            resumed["lifecycle"]["status"] = "closed"
            record_path.write_text(json.dumps(resumed), encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "terminal run"):
                self.module.transition_run(record_path, "open")

    def test_projection_tampering_fails_validation(self):
        with tempfile.TemporaryDirectory() as directory:
            record_path = self.module.initialize_run(
                Path(directory),
                project="Launch",
                workflow_family="gtm",
                routed_output="gtm_plan",
                operator="douglas",
            )
            decision_path = record_path.parent / "decision-record.md"
            decision_path.write_text("tampered", encoding="utf-8")
            result = self.module.validate_record(
                self.module.load_json(record_path), record_path=record_path
            )
            self.assertFalse(result["valid"])
            self.assertIn("DECISION_PROJECTION_STALE", result["failure_codes"])

    def test_handoff_and_receipt_scaffolds_remain_unsigned(self):
        with tempfile.TemporaryDirectory() as directory:
            record_path = self.module.initialize_run(
                Path(directory),
                project="Launch",
                workflow_family="gtm",
                routed_output="gtm_plan",
                operator="douglas",
            )
            record = self.module.load_json(record_path)
            record["decisions"] = [
                {
                    "id": "D1",
                    "decision": "Lead with learning.",
                    "owner": "douglas",
                    "source_id": "S1",
                    "status": "locked",
                }
            ]
            record["sources"] = [
                {
                    "id": "S1",
                    "owner": "dan",
                    "location": "notion://strategy",
                    "authority": "company_strategy",
                    "freshness": "2026-08-21",
                    "status": "confirmed",
                }
            ]
            record_path.write_text(json.dumps(record), encoding="utf-8")
            self.module.render_run(record_path)
            handoff = self.module.scaffold_handoff(record_path, owner="douglas")
            (record_path.parent / "artifact.md").write_text(
                "# Draft artifact\n", encoding="utf-8"
            )
            receipt = self.module.scaffold_receipt(
                record_path, artifact="artifact.md", stage="strategy_to_market"
            )
            self.assertIsNone(json.loads(handoff.read_text())["approved_by"])
            self.assertIsNone(json.loads(receipt.read_text())["verified_by"])

    def test_cli_returns_documented_exit_codes(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            created = subprocess.run(
                [
                    sys.executable,
                    str(SCRIPT),
                    "init",
                    str(root),
                    "--project",
                    "Launch",
                    "--workflow",
                    "gtm",
                    "--route",
                    "gtm_plan",
                    "--operator",
                    "douglas",
                ],
                capture_output=True,
                text=True,
                check=False,
            )
            self.assertEqual(0, created.returncode, created.stderr)
            record_path = Path(json.loads(created.stdout)["record_path"])
            invalid = subprocess.run(
                [sys.executable, str(SCRIPT), "validate", str(record_path)],
                capture_output=True,
                text=True,
                check=False,
            )
            self.assertEqual(1, invalid.returncode)
            malformed = root / "bad.json"
            malformed.write_text("{", encoding="utf-8")
            unreadable = subprocess.run(
                [sys.executable, str(SCRIPT), "validate", str(malformed)],
                capture_output=True,
                text=True,
                check=False,
            )
            self.assertEqual(2, unreadable.returncode)

    def test_content_bound_closed_run_is_operationally_ready(self):
        with tempfile.TemporaryDirectory() as directory:
            record_path = self.make_ready_v2(
                Path(directory), project="Launch", operator="douglas", minutes=100
            )
            result = self.module.validate_record(
                self.module.load_json(record_path), record_path=record_path
            )
            self.assertTrue(result["structural_ready"])
            self.assertTrue(result["operational_ready"])
            self.assertFalse(result["comparison_ready"])
            self.assertFalse(result["proof_ready"])

    def test_stale_human_approval_digest_blocks_operational_readiness(self):
        with tempfile.TemporaryDirectory() as directory:
            record_path = self.make_ready_v2(
                Path(directory), project="Launch", operator="douglas", minutes=100
            )
            record = self.module.load_json(record_path)
            record["approvals"]["fidelity"]["record_digest"] = "stale"
            record_path.write_text(json.dumps(record), encoding="utf-8")
            result = self.module.validate_record(record, record_path=record_path)
            self.assertFalse(result["operational_ready"])

    def test_receipt_cannot_bind_an_external_local_file(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            record_path = self.make_ready_v2(
                root, project="Launch", operator="douglas", minutes=100
            )
            external = root / "outside-run.md"
            external.write_text("# Different artifact\n", encoding="utf-8")
            record = self.module.load_json(record_path)
            receipt_path = record_path.parent / record["artifact"]["receipt"]
            receipt = json.loads(receipt_path.read_text(encoding="utf-8"))
            receipt["artifact"] = {
                "kind": "local",
                "path": str(external),
                "sha256": self.module._sha256(external),
            }
            receipt_path.write_text(json.dumps(receipt), encoding="utf-8")
            result = self.module.validate_record(record, record_path=record_path)
            self.assertFalse(result["operational_ready"])

    def test_governance_change_invalidates_signed_approval_even_when_markdown_is_unchanged(self):
        with tempfile.TemporaryDirectory() as directory:
            record_path = self.make_ready_v2(
                Path(directory), project="Launch", operator="douglas", minutes=100
            )
            record = self.module.load_json(record_path)
            record["sources"][0]["freshness"] = "2026-08-22"
            record_path.write_text(json.dumps(record), encoding="utf-8")
            result = self.module.validate_record(record, record_path=record_path)
            self.assertFalse(result["structural_ready"])
            self.assertFalse(result["operational_ready"])
            self.assertIn("GOVERNANCE_DIGEST_STALE", result["failure_codes"])

    def test_receipt_contract_fields_fail_closed(self):
        mutations = {
            "schema": lambda receipt: receipt.update({"schema_version": 1}),
            "stage": lambda receipt: receipt.update({"stage": "market_to_memory"}),
            "decision ids": lambda receipt: receipt.update({"decision_ids": []}),
            "governance": lambda receipt: receipt.update({"governance_digest": "stale"}),
        }
        for name, mutate in mutations.items():
            with self.subTest(name=name), tempfile.TemporaryDirectory() as directory:
                record_path = self.make_ready_v2(
                    Path(directory), project="Launch", operator="douglas", minutes=100
                )
                record = self.module.load_json(record_path)
                receipt_path = record_path.parent / record["artifact"]["receipt"]
                receipt = json.loads(receipt_path.read_text(encoding="utf-8"))
                mutate(receipt)
                receipt_path.write_text(json.dumps(receipt), encoding="utf-8")
                result = self.module.validate_record(record, record_path=record_path)
                self.assertFalse(result["operational_ready"])
                self.assertIn("RECEIPT_INVALID", result["failure_codes"])

    def test_artifact_approvals_must_name_the_exact_receipt_binding(self):
        with tempfile.TemporaryDirectory() as directory:
            record_path = self.make_ready_v2(
                Path(directory), project="Launch", operator="douglas", minutes=100
            )
            record = self.module.load_json(record_path)
            record["approvals"]["artifact"]["artifact_binding"] = "different"
            record_path.write_text(json.dumps(record), encoding="utf-8")
            result = self.module.validate_record(record, record_path=record_path)
            self.assertFalse(result["operational_ready"])

    def test_strategy_transition_enforces_governance_and_updates_stage_metadata(self):
        with tempfile.TemporaryDirectory() as directory:
            record_path = self.module.initialize_run(
                Path(directory),
                project="Launch",
                workflow_family="gtm",
                routed_output="gtm_plan",
                operator="douglas",
            )
            self.module.transition_run(record_path, "strategy_pending")
            with self.assertRaisesRegex(ValueError, "authoritative source"):
                self.module.transition_run(record_path, "strategy_approved")
            pending = self.module.load_json(record_path)
            self.assertEqual("context_to_strategy", pending["lifecycle"]["current_stage"])
            pending["sources"] = [
                {
                    "id": "S1",
                    "owner": "dan",
                    "location": "notion://strategy",
                    "authority": "company_strategy",
                    "freshness": "2026-08-21",
                    "status": "confirmed",
                }
            ]
            pending["decisions"] = [
                {
                    "id": "D1",
                    "decision": "Lead with learning.",
                    "owner": "douglas",
                    "source_id": "S1",
                    "status": "locked",
                }
            ]
            pending["questions"] = [
                {
                    "id": "Q1",
                    "question": "Who owns it?",
                    "owner": "douglas",
                    "blocking": True,
                    "status": "open",
                }
            ]
            record_path.write_text(json.dumps(pending), encoding="utf-8")
            self.module.render_run(record_path)
            pending = self.module.load_json(record_path)
            pending["approvals"]["strategy"].update(
                {
                    "approved_by": "human-reviewer",
                    "approved_at": "2026-08-21T12:30:00+00:00",
                    "record_digest": self.module.governance_digest(pending),
                }
            )
            record_path.write_text(json.dumps(pending), encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "blocking governance"):
                self.module.transition_run(record_path, "strategy_approved")

    def test_missing_local_artifact_does_not_create_receipt_or_mutate_record(self):
        with tempfile.TemporaryDirectory() as directory:
            record_path = self.module.initialize_run(
                Path(directory),
                project="Launch",
                workflow_family="gtm",
                routed_output="gtm_plan",
                operator="douglas",
            )
            before = record_path.read_text(encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "existing regular file"):
                self.module.scaffold_receipt(
                    record_path, stage="strategy_to_market", artifact="missing.md"
                )
            self.assertEqual(before, record_path.read_text(encoding="utf-8"))
            self.assertFalse((record_path.parent / "strategy_to_market-receipt.json").exists())

    def test_malformed_nested_v2_records_fail_closed_without_crashing(self):
        fields = (
            "lifecycle",
            "artifact",
            "metrics",
            "approvals",
            "evidence",
            "proof",
            "projections",
            "sources",
            "source_conflicts",
            "decisions",
            "protected_language",
            "questions",
        )
        with tempfile.TemporaryDirectory() as directory:
            record_path = self.module.initialize_run(
                Path(directory),
                project="Launch",
                workflow_family="gtm",
                routed_output="gtm_plan",
                operator="douglas",
            )
            original = self.module.load_json(record_path)
            for field in fields:
                with self.subTest(field=field):
                    malformed = json.loads(json.dumps(original))
                    malformed[field] = [] if isinstance(malformed[field], dict) else {}
                    result = self.module.validate_record(malformed, record_path=record_path)
                    self.assertFalse(result["valid"])
                    self.assertIn("SHAPE_INVALID", result["failure_codes"])

    def test_successor_run_records_a_terminal_predecessor(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            predecessor = self.make_ready_v2(
                root, project="Launch", operator="douglas", minutes=100
            )
            successor = self.module.initialize_run(
                root,
                project="Launch",
                workflow_family="gtm",
                routed_output="gtm_plan",
                operator="austin",
                predecessor=predecessor,
            )
            record = self.module.load_json(successor)
            self.assertEqual(
                self.module.load_json(predecessor)["run_id"],
                record["predecessor_run"]["run_id"],
            )
            self.assertTrue(
                self.module.validate_record(record, record_path=successor)["valid"]
            )
            record["predecessor_run"]["governance_digest"] = "tampered"
            self.assertFalse(
                self.module.validate_record(record, record_path=successor)["valid"]
            )

    def test_terminal_timestamp_must_match_terminal_status(self):
        with tempfile.TemporaryDirectory() as directory:
            record_path = self.make_ready_v2(
                Path(directory), project="Launch", operator="douglas", minutes=100
            )
            record = self.module.load_json(record_path)
            record["lifecycle"]["closed_at"] = None
            result = self.module.validate_record(record, record_path=record_path)
            self.assertFalse(result["valid"])
            self.assertIn("LIFECYCLE_TIMESTAMP_INVALID", result["failure_codes"])

    def test_metric_values_and_timing_must_be_valid(self):
        mutations = {
            "negative minutes": lambda record: record["metrics"].update(
                {"human_review_minutes": -1}
            ),
            "boolean minutes": lambda record: record["metrics"].update(
                {"human_review_minutes": True}
            ),
            "negative defects": lambda record: record["metrics"].update(
                {"critical_defects": -1}
            ),
            "boolean defects": lambda record: record["metrics"].update(
                {"critical_defects": True}
            ),
            "late declaration": lambda record: record["metrics"]["primary"].update(
                {"declared_at": "2026-08-21T12:00:00+00:00"}
            ),
        }
        for name, mutate in mutations.items():
            with self.subTest(name=name), tempfile.TemporaryDirectory() as directory:
                record_path = self.make_ready_v2(
                    Path(directory), project="Launch", operator="douglas", minutes=100
                )
                record = self.module.load_json(record_path)
                mutate(record)
                record_path.write_text(json.dumps(record), encoding="utf-8")
                result = self.module.validate_record(record, record_path=record_path)
                self.assertFalse(result["operational_ready"])

    def test_synthetic_run_cannot_become_operational_proof(self):
        with tempfile.TemporaryDirectory() as directory:
            record_path = self.make_ready_v2(
                Path(directory), project="Launch", operator="douglas", minutes=100
            )
            record = self.module.load_json(record_path)
            record["evidence"]["origin"] = "synthetic"
            record_path.write_text(json.dumps(record), encoding="utf-8")
            result = self.module.validate_record(record, record_path=record_path)
            self.assertFalse(result["operational_ready"])

    def test_comparable_independent_v2_followup_is_proof_eligible(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            baseline_path = self.make_ready_v2(
                root, project="Launch", operator="douglas", minutes=100
            )
            followup_path = self.make_ready_v2(
                root,
                project="Launch",
                operator="austin",
                minutes=80,
                force_new=True,
                comparable_to=self.module.load_json(baseline_path)["run_id"],
            )
            baseline = self.module.load_json(baseline_path)
            followup = self.module.load_json(followup_path)
            result = self.module.compare_records(
                baseline,
                followup,
                baseline_path=baseline_path,
                followup_path=followup_path,
            )
            self.assertTrue(result["proof_eligible"])
            self.assertFalse(result["publication_authorized"])

    def test_v2_comparison_gates_fail_closed(self):
        cases = {
            "blank rationale": (
                lambda baseline, followup: followup["proof"].update(
                    {"comparability_rationale": ""}
                ),
                "comparability rationale is missing",
            ),
            "blank dimension": (
                lambda baseline, followup: followup["proof"]["dimensions"].update(
                    {"scope": None}
                ),
                "comparison dimensions do not match",
            ),
            "late baseline metric": (
                lambda baseline, followup: baseline["metrics"]["primary"].update(
                    {"declared_at": "2026-08-21T12:00:00+00:00"}
                ),
                "baseline is not operationally ready",
            ),
            "same normalized operator": (
                lambda baseline, followup: followup.update({"operator": " Douglas "}),
                "followup operator is not independent",
            ),
        }
        for name, (mutate, expected) in cases.items():
            with self.subTest(name=name), tempfile.TemporaryDirectory() as directory:
                root = Path(directory)
                baseline_path = self.make_ready_v2(
                    root, project="Launch", operator="douglas", minutes=100
                )
                followup_path = self.make_ready_v2(
                    root,
                    project="Launch",
                    operator="austin",
                    minutes=80,
                    force_new=True,
                    comparable_to=self.module.load_json(baseline_path)["run_id"],
                )
                baseline = self.module.load_json(baseline_path)
                followup = self.module.load_json(followup_path)
                mutate(baseline, followup)
                result = self.module.compare_records(
                    baseline,
                    followup,
                    baseline_path=baseline_path,
                    followup_path=followup_path,
                )
                self.assertFalse(result["proof_eligible"])
                self.assertIn(expected, result["failures"])

    def test_v2_inherited_decision_must_preserve_meaning_and_source(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            baseline_path = self.make_ready_v2(
                root, project="Launch", operator="douglas", minutes=100
            )
            followup_path = self.make_ready_v2(
                root,
                project="Launch",
                operator="austin",
                minutes=80,
                force_new=True,
                comparable_to=self.module.load_json(baseline_path)["run_id"],
                decision="Lead with software.",
            )
            baseline = self.module.load_json(baseline_path)
            followup = self.module.load_json(followup_path)
            result = self.module.compare_records(
                baseline,
                followup,
                baseline_path=baseline_path,
                followup_path=followup_path,
            )
            self.assertFalse(result["proof_eligible"])
            self.assertIn(
                "accepted inherited decision D1 changed meaning or source",
                result["failures"],
            )

    def test_terminal_runs_reject_every_public_mutator(self):
        with tempfile.TemporaryDirectory() as directory:
            record_path = self.make_ready_v2(
                Path(directory), project="Launch", operator="douglas", minutes=100
            )
            for operation in (
                lambda: self.module.render_run(record_path),
                lambda: self.module.scaffold_handoff(record_path, owner="douglas"),
                lambda: self.module.scaffold_receipt(
                    record_path,
                    stage="strategy_to_market",
                    artifact="artifact.md",
                ),
                lambda: self.module.transition_run(record_path, "abandoned"),
            ):
                with self.subTest(operation=operation), self.assertRaisesRegex(
                    self.module.IneligibleError, "terminal run"
                ):
                    operation()

    def test_approval_timestamps_must_be_parseable_and_timezone_aware(self):
        for bad_timestamp in ("yesterday", "2026-08-21T12:30:00"):
            with self.subTest(timestamp=bad_timestamp), tempfile.TemporaryDirectory() as directory:
                record_path = self.make_ready_v2(
                    Path(directory), project="Launch", operator="douglas", minutes=100
                )
                record = self.module.load_json(record_path)
                record["approvals"]["strategy"]["approved_at"] = bad_timestamp
                record_path.write_text(json.dumps(record), encoding="utf-8")
                result = self.module.validate_record(record, record_path=record_path)
                self.assertFalse(result["operational_ready"])

    def test_governed_collections_require_unique_ids_and_source_links(self):
        cases = {
            "duplicate source": lambda record: record["sources"].append(
                dict(record["sources"][0])
            ),
            "duplicate decision": lambda record: record["decisions"].append(
                dict(record["decisions"][0])
            ),
            "missing protected id": lambda record: record["protected_language"].append(
                {"id": None, "text": "One subscription", "owner": "douglas"}
            ),
            "unknown source": lambda record: record["decisions"][0].update(
                {"source_id": "S404"}
            ),
        }
        for name, mutate in cases.items():
            with self.subTest(name=name), tempfile.TemporaryDirectory() as directory:
                record_path = self.module.initialize_run(
                    Path(directory),
                    project="Launch",
                    workflow_family="gtm",
                    routed_output="gtm_plan",
                    operator="douglas",
                )
                record = self.module.load_json(record_path)
                record["sources"] = [
                    {
                        "id": "S1",
                        "owner": "dan",
                        "location": "notion://strategy",
                        "authority": "company_strategy",
                        "freshness": "2026-08-21",
                        "status": "confirmed",
                    }
                ]
                record["decisions"] = [
                    {
                        "id": "D1",
                        "decision": "Lead with learning.",
                        "owner": "douglas",
                        "source_id": "S1",
                        "status": "locked",
                    }
                ]
                mutate(record)
                record_path.write_text(json.dumps(record), encoding="utf-8")
                self.module.render_run(record_path)
                result = self.module.validate_record(
                    self.module.load_json(record_path), record_path=record_path
                )
                self.assertFalse(result["valid"])
                self.assertIn("GOVERNANCE_INVALID", result["failure_codes"])

    def test_failed_projection_generation_does_not_advance_lifecycle(self):
        with tempfile.TemporaryDirectory() as directory:
            record_path = self.module.initialize_run(
                Path(directory),
                project="Launch",
                workflow_family="gtm",
                routed_output="gtm_plan",
                operator="douglas",
            )
            with patch.object(
                self.module, "_run_markdown", side_effect=OSError("projection failed")
            ), self.assertRaisesRegex(OSError, "projection failed"):
                self.module.transition_run(record_path, "strategy_pending")
            self.assertEqual(
                "open", self.module.load_json(record_path)["lifecycle"]["status"]
            )
            self.module.transition_run(record_path, "strategy_pending")
            self.assertEqual(
                "strategy_pending",
                self.module.load_json(record_path)["lifecycle"]["status"],
            )

    def test_receipt_commit_failure_rolls_back_projections_and_can_retry(self):
        with tempfile.TemporaryDirectory() as directory:
            record_path = self.module.initialize_run(
                Path(directory),
                project="Launch",
                workflow_family="gtm",
                routed_output="gtm_plan",
                operator="douglas",
            )
            artifact_path = record_path.parent / "artifact.md"
            artifact_path.write_text("# Artifact\n", encoding="utf-8")
            before_record = record_path.read_bytes()
            before_run = (record_path.parent / "run.md").read_bytes()
            before_decisions = (record_path.parent / "decision-record.md").read_bytes()
            original_atomic_json = self.module._atomic_json

            def fail_record_commit(path, data):
                if path.resolve() == record_path.resolve():
                    raise OSError("record commit failed")
                return original_atomic_json(path, data)

            with patch.object(
                self.module, "_atomic_json", side_effect=fail_record_commit
            ), self.assertRaisesRegex(OSError, "record commit failed"):
                self.module.scaffold_receipt(
                    record_path,
                    stage="strategy_to_market",
                    artifact="artifact.md",
                )
            self.assertEqual(before_record, record_path.read_bytes())
            self.assertEqual(before_run, (record_path.parent / "run.md").read_bytes())
            self.assertEqual(
                before_decisions,
                (record_path.parent / "decision-record.md").read_bytes(),
            )
            receipt = self.module.scaffold_receipt(
                record_path,
                stage="strategy_to_market",
                artifact="artifact.md",
            )
            self.assertTrue(receipt.is_file())

    def test_blocked_run_can_be_abandoned_and_linked_to_a_successor(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            predecessor = self.module.initialize_run(
                root,
                project="Launch",
                workflow_family="gtm",
                routed_output="gtm_plan",
                operator="douglas",
            )
            self.module.transition_run(predecessor, "blocked", reason="Dan must rule")
            self.module.transition_run(predecessor, "abandoned")
            abandoned = self.module.load_json(predecessor)
            self.assertEqual("Dan must rule", abandoned["lifecycle"]["blocked_on"])
            self.assertIsNotNone(
                self.module._parse_iso(abandoned["lifecycle"]["abandoned_at"])
            )
            successor = self.module.initialize_run(
                root,
                project="Launch",
                workflow_family="gtm",
                routed_output="gtm_plan",
                operator="austin",
                predecessor=predecessor,
            )
            binding = self.module.load_json(successor)["predecessor_run"]
            self.assertEqual(abandoned["run_id"], binding["run_id"])
            self.assertTrue(
                self.module.validate_record(
                    self.module.load_json(successor), record_path=successor
                )["valid"]
            )

    def test_receipts_accept_only_the_market_stage_and_safe_artifact_refs(self):
        with tempfile.TemporaryDirectory() as directory:
            record_path = self.module.initialize_run(
                Path(directory),
                project="Launch",
                workflow_family="gtm",
                routed_output="gtm_plan",
                operator="douglas",
            )
            with self.assertRaisesRegex(ValueError, "strategy_to_market"):
                self.module.scaffold_receipt(
                    record_path, stage="context_to_strategy", artifact="artifact.md"
                )
            with self.assertRaisesRegex(ValueError, "https"):
                self.module.scaffold_receipt(
                    record_path,
                    stage="strategy_to_market",
                    artifact="file:///tmp/artifact.md",
                )

    def test_remote_receipt_binding_is_operational_and_tamper_evident(self):
        with tempfile.TemporaryDirectory() as directory:
            record_path = self.make_ready_v2(
                Path(directory),
                project="Launch",
                operator="douglas",
                minutes=100,
                artifact_reference="https://example.com/artifact",
            )
            record = self.module.load_json(record_path)
            self.assertTrue(
                self.module.validate_record(record, record_path=record_path)[
                    "operational_ready"
                ]
            )
            receipt_path = record_path.parent / record["artifact"]["receipt"]
            receipt = json.loads(receipt_path.read_text(encoding="utf-8"))
            receipt["artifact"]["revision"] = "rev-2"
            receipt_path.write_text(json.dumps(receipt), encoding="utf-8")
            result = self.module.validate_record(record, record_path=record_path)
            self.assertFalse(result["operational_ready"])

    def test_v2_reduction_gate_uses_unrounded_value(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            baseline_path = self.make_ready_v2(
                root, project="Launch", operator="douglas", minutes=100
            )
            baseline = self.module.load_json(baseline_path)
            followup_path = self.make_ready_v2(
                root,
                project="Launch",
                operator="austin",
                minutes=80.004,
                force_new=True,
                comparable_to=baseline["run_id"],
            )
            result = self.module.compare_records(
                baseline,
                self.module.load_json(followup_path),
                baseline_path=baseline_path,
                followup_path=followup_path,
            )
            self.assertFalse(result["proof_eligible"])
            self.assertEqual(20.0, result["review_reduction_percent"])
            self.assertIn("review burden fell by less than 20%", result["failures"])

    def test_all_specialist_routes_use_the_shared_handoff_contract(self):
        root = SCRIPT.parents[3]
        contract = (
            root
            / "strategy"
            / "compound-marketing"
            / "references"
            / "handoff-contract.md"
        ).read_text(encoding="utf-8")
        for field in (
            "Run ID",
            "Decision-record SHA-256",
            "Canonical governance digest",
            "Inherited decision IDs",
            "Protected-language IDs",
            "Unresolved-question IDs",
            "Artifact owner",
        ):
            self.assertIn(field, contract)
        for relative in (
            "marketing/gtm/SKILL.md",
            "strategy/program-brief/SKILL.md",
            "launches/gtm-plan/SKILL.md",
            "strategy/one-pager/SKILL.md",
        ):
            with self.subTest(relative=relative):
                text = (root / relative).read_text(encoding="utf-8")
                self.assertIn("handoff-contract.md", text)
                self.assertIn("handoff.json", text)

class CompareRunLegacyAdditionalTests(unittest.TestCase):
    module = LEGACY_CHECK_RUN

    def test_run_cannot_compare_against_itself(self):
        baseline = run_record("same")
        followup = run_record(
            "same",
            review_minutes=70,
            inherited=1,
            accepted_inherited=1,
            comparable_to="same",
            independent_operator=True,
        )
        result = self.module.compare_records(baseline, followup)
        self.assertFalse(result["qualifies"])
        self.assertIn("baseline and followup run IDs must differ", result["failures"])

    def test_each_compounding_gate_fails_closed(self):
        cases = {
            "wrong comparison": (
                lambda baseline, followup: followup["proof"].update(
                    {"comparable_to": "other"}
                ),
                "followup does not name the baseline run",
            ),
            "retrospective baseline": (
                lambda baseline, followup: baseline.update(
                    {"evidence_status": "retrospective"}
                ),
                "baseline evidence was not prospective",
            ),
            "unfinished baseline": (
                lambda baseline, followup: baseline["stages"][
                    "market_to_memory"
                ].update({"status": "in_progress"}),
                "baseline stage market_to_memory is unfinished",
            ),
            "first pass regression": (
                lambda baseline, followup: (
                    baseline["metrics"].update({"first_pass_accepted": True}),
                    followup["metrics"].update({"first_pass_accepted": False}),
                ),
                "first-pass acceptance regressed",
            ),
            "defect regression": (
                lambda baseline, followup: followup["metrics"].update(
                    {"critical_defects": 3}
                ),
                "critical defects increased",
            ),
            "no independent operator": (
                lambda baseline, followup: followup["metrics"].update(
                    {"independent_operator": False}
                ),
                "independent teammate rerun is missing",
            ),
            "no accepted inherited decision": (
                lambda baseline, followup: (
                    followup["metrics"].update(
                        {
                            "inherited_decisions": 0,
                            "accepted_inherited_decisions": 0,
                        }
                    ),
                    followup["proof"].update(
                        {"accepted_inherited_decision_ids": []}
                    ),
                ),
                "no inherited decision was accepted",
            ),
            "no artifact verification": (
                lambda baseline, followup: followup["metrics"].update(
                    {
                        "artifact_fidelity_verified": False,
                        "artifact_fidelity_verifier": None,
                    }
                ),
                "followup artifact fidelity was not human-verified",
            ),
            "unverified baseline": (
                lambda baseline, followup: baseline["metrics"].update(
                    {
                        "artifact_fidelity_verified": False,
                        "artifact_fidelity_verifier": None,
                    }
                ),
                "baseline artifact fidelity was not human-verified",
            ),
        }
        for name, (mutate, expected) in cases.items():
            with self.subTest(name=name):
                baseline = run_record("baseline", defects=2)
                followup = run_record(
                    "followup",
                    review_minutes=70,
                    first_pass=True,
                    defects=1,
                    inherited=1,
                    accepted_inherited=1,
                    comparable_to="baseline",
                    independent_operator=True,
                )
                mutate(baseline, followup)
                result = self.module.compare_records(baseline, followup)
                self.assertFalse(result["qualifies"])
                self.assertFalse(result["proof_ready"])
                self.assertIn(expected, result["failures"])


class RealWorldFixtureTests(unittest.TestCase):
    module = CHECK_RUN

    def test_observed_baselines_validate_without_overclaiming(self):
        fixture_dir = Path(__file__).parents[1] / "evals" / "fixtures"
        fixture_paths = (
            fixture_dir / "brand-book-baseline.json",
            fixture_dir / "thesis-gtm-baseline.json",
        )
        for path in fixture_paths:
            with self.subTest(path=path.name):
                record = self.module.load_json(path)
                result = self.module.validate_record(record)
                self.assertTrue(result["valid"])
                self.assertFalse(result["proof_ready"])
                self.assertFalse(record["proof"]["publishable_claim"])


class CliTests(unittest.TestCase):
    def test_cli_exit_codes_and_json_output(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            valid_path = root / "valid.json"
            invalid_path = root / "invalid.json"
            malformed_path = root / "malformed.json"
            valid_path.write_text(json.dumps(run_record("valid")), encoding="utf-8")
            invalid_path.write_text(json.dumps({}), encoding="utf-8")
            malformed_path.write_text("{", encoding="utf-8")

            for path, expected_code in (
                (valid_path, 0),
                (invalid_path, 1),
                (malformed_path, 2),
            ):
                with self.subTest(path=path.name):
                    result = subprocess.run(
                        [sys.executable, str(SCRIPT), "validate", str(path)],
                        check=False,
                        capture_output=True,
                        text=True,
                    )
                    self.assertEqual(expected_code, result.returncode)
                    self.assertIsInstance(json.loads(result.stdout), dict)

    def test_render_cli_reports_malformed_nested_shape_as_json(self):
        with tempfile.TemporaryDirectory() as directory:
            record_path = Path(directory) / "run.json"
            record_path.write_text(
                json.dumps(
                    {
                        "schema_version": 2,
                        "lifecycle": {},
                        "artifact": {},
                        "projections": {},
                        "sources": None,
                        "source_conflicts": [],
                        "decisions": [],
                        "protected_language": [],
                        "questions": [],
                    }
                ),
                encoding="utf-8",
            )
            result = subprocess.run(
                [sys.executable, str(SCRIPT), "render", str(record_path)],
                check=False,
                capture_output=True,
                text=True,
            )
            self.assertEqual(2, result.returncode)
            self.assertIn("sources", json.loads(result.stdout)["error"])

    def test_public_compare_rejects_legacy_records(self):
        result = CHECK_RUN.compare_records(
            run_record("baseline"), run_record("followup")
        )
        self.assertFalse(result["qualifies"])
        self.assertFalse(result["proof_ready"])
        self.assertIn("only schema V2 records", result["failures"][0])

    def test_compare_cli_rejects_legacy_records_as_public_proof(self):
        baseline = run_record("baseline", defects=2)
        followup = run_record(
            "followup",
            review_minutes=70,
            first_pass=True,
            defects=1,
            inherited=1,
            accepted_inherited=1,
            comparable_to="baseline",
            independent_operator=True,
        )
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            baseline_path = write_artifact_receipts(root, baseline)
            followup_path = write_artifact_receipts(root, followup)
            result = subprocess.run(
                [
                    sys.executable,
                    str(SCRIPT),
                    "compare",
                    str(baseline_path),
                    str(followup_path),
                ],
                check=False,
                capture_output=True,
                text=True,
                cwd=root,
            )
        self.assertEqual(1, result.returncode)
        payload = json.loads(result.stdout)
        self.assertFalse(payload["proof_ready"])
        self.assertIn("only schema V2 records", payload["failures"][0])


if __name__ == "__main__":
    unittest.main()
