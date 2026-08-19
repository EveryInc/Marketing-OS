from __future__ import annotations

import importlib.util
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


SCRIPT = Path(__file__).parents[1] / "scripts" / "check_run.py"


def load_module():
    spec = importlib.util.spec_from_file_location("check_run", SCRIPT)
    if spec is None or spec.loader is None:
        raise RuntimeError("could not load check_run.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


CHECK_RUN = load_module()


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


class CompareRunTests(unittest.TestCase):
    module = CHECK_RUN

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
        result = self.module.compare_records(baseline, followup)
        self.assertTrue(result["qualifies"])
        self.assertTrue(result["proof_ready"])
        self.assertEqual(20.0, result["review_reduction_percent"])

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


if __name__ == "__main__":
    unittest.main()
