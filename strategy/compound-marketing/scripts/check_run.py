#!/usr/bin/env python3
"""Validate Compound Marketing run records and compare repeated workflows."""

from __future__ import annotations

import argparse
import json
import math
import sys
from pathlib import Path
from typing import Any


REQUIRED_STAGES = (
    "context_to_strategy",
    "strategy_to_market",
    "market_to_memory",
)
VALID_STAGE_STATUSES = {
    "not_started",
    "in_progress",
    "approved",
    "complete",
    "not_applicable",
}
VALID_DECISION_STATUSES = {"locked", "open", "rejected"}
VALID_EVIDENCE_STATUSES = {"prospective", "retrospective", "incomplete"}
REQUIRED_METRICS = (
    "human_review_minutes",
    "first_pass_accepted",
    "critical_defects",
    "inherited_decisions",
    "accepted_inherited_decisions",
    "independent_operator",
    "artifact_fidelity_verified",
    "artifact_fidelity_verifier",
)


def _is_number(value: Any) -> bool:
    if isinstance(value, bool):
        return False
    if isinstance(value, int):
        return True
    return isinstance(value, float) and math.isfinite(value)


def _required_string(record: dict[str, Any], field: str, errors: list[str]) -> None:
    if not isinstance(record.get(field), str) or not record[field].strip():
        errors.append(f"{field} must be a non-empty string")


def _string_set(value: Any) -> set[str]:
    if not isinstance(value, list):
        return set()
    return {item for item in value if isinstance(item, str)}


def validate_record(
    record: dict[str, Any], *, comparison_context: bool = False
) -> dict[str, Any]:
    errors: list[str] = []
    warnings: list[str] = []

    if record.get("schema_version") != 1:
        errors.append("schema_version must equal 1")
    for field in ("run_id", "project", "workflow"):
        _required_string(record, field, errors)

    evidence_status = record.get("evidence_status")
    if evidence_status not in VALID_EVIDENCE_STATUSES:
        errors.append("evidence_status is invalid")

    decisions = record.get("decisions")
    decision_ids: set[str] = set()
    locked_decisions: list[dict[str, Any]] = []
    if not isinstance(decisions, list):
        errors.append("decisions must be a list")
        decisions = []
    for index, decision in enumerate(decisions):
        if not isinstance(decision, dict):
            errors.append(f"decision {index + 1} must be an object")
            continue
        decision_id = decision.get("id")
        if not isinstance(decision_id, str) or not decision_id.strip():
            errors.append(f"decision {index + 1} has no id")
            continue
        if decision_id in decision_ids:
            errors.append(f"duplicate decision id {decision_id}")
        decision_ids.add(decision_id)
        for field in ("decision", "owner", "source", "status"):
            if not isinstance(decision.get(field), str) or not decision[field].strip():
                errors.append(f"decision {decision_id} has no {field}")
        if decision.get("status") not in VALID_DECISION_STATUSES:
            errors.append(f"decision {decision_id} has invalid status")
        applies_to = decision.get("applies_to", [])
        if not isinstance(applies_to, list) or not all(
            isinstance(item, str) for item in applies_to
        ):
            errors.append(f"decision {decision_id} applies_to must be a string list")
        elif any(item not in REQUIRED_STAGES for item in applies_to):
            errors.append(f"decision {decision_id} applies_to has an invalid stage")
        if decision.get("status") == "locked":
            locked_decisions.append(decision)

    stages = record.get("stages")
    if not isinstance(stages, dict):
        errors.append("stages must be an object")
        stages = {}
    for stage_name in REQUIRED_STAGES:
        stage = stages.get(stage_name)
        if not isinstance(stage, dict):
            errors.append(f"missing stage {stage_name}")
            continue
        if stage.get("status") not in VALID_STAGE_STATUSES:
            errors.append(f"stage {stage_name} has invalid status")
        if not isinstance(stage.get("artifact"), str) or not stage["artifact"].strip():
            errors.append(f"stage {stage_name} has no artifact")

    strategy_stage = stages.get("context_to_strategy", {})
    market_stage = stages.get("strategy_to_market", {})
    if not isinstance(strategy_stage, dict):
        strategy_stage = {}
    if not isinstance(market_stage, dict):
        market_stage = {}
    output_ids = strategy_stage.get("output_decision_ids", [])
    preserved_ids = market_stage.get("preserved_decision_ids", [])
    if not isinstance(output_ids, list):
        errors.append("context_to_strategy output_decision_ids must be a list")
        output_ids = []
    if not isinstance(preserved_ids, list):
        errors.append("strategy_to_market preserved_decision_ids must be a list")
        preserved_ids = []
    output_id_set = _string_set(output_ids)
    preserved_id_set = _string_set(preserved_ids)

    for decision in locked_decisions:
        decision_id = decision.get("id")
        applies_to = decision.get("applies_to", [])
        if decision_id not in output_id_set:
            errors.append(f"locked decision {decision_id} is missing from strategy output")
        if "strategy_to_market" in applies_to and decision_id not in preserved_id_set:
            errors.append(f"locked decision {decision_id} was not preserved")

    metrics = record.get("metrics")
    if not isinstance(metrics, dict):
        errors.append("metrics must be an object")
        metrics = {}
    for metric in REQUIRED_METRICS:
        if metric not in metrics:
            errors.append(f"missing metric {metric}")

    review_minutes = metrics.get("human_review_minutes")
    if review_minutes is None:
        warnings.append("human_review_minutes is missing")
    elif not _is_number(review_minutes) or review_minutes < 0:
        errors.append("human_review_minutes must be a non-negative number or null")

    first_pass = metrics.get("first_pass_accepted")
    if first_pass is None:
        warnings.append("first_pass_accepted is missing")
    elif not isinstance(first_pass, bool):
        errors.append("first_pass_accepted must be a boolean or null")

    defects = metrics.get("critical_defects")
    if defects is None:
        warnings.append("critical_defects is missing")
    elif not isinstance(defects, int) or isinstance(defects, bool) or defects < 0:
        errors.append("critical_defects must be a non-negative integer or null")

    inherited = metrics.get("inherited_decisions")
    accepted = metrics.get("accepted_inherited_decisions")
    for name, value in (
        ("inherited_decisions", inherited),
        ("accepted_inherited_decisions", accepted),
    ):
        if not isinstance(value, int) or isinstance(value, bool) or value < 0:
            errors.append(f"{name} must be a non-negative integer")
    if isinstance(inherited, int) and isinstance(accepted, int) and accepted > inherited:
        errors.append("accepted_inherited_decisions cannot exceed inherited_decisions")
    if not isinstance(metrics.get("independent_operator"), bool):
        errors.append("independent_operator must be a boolean")
    artifact_fidelity_verified = metrics.get("artifact_fidelity_verified")
    artifact_fidelity_verifier = metrics.get("artifact_fidelity_verifier")
    if not isinstance(artifact_fidelity_verified, bool):
        errors.append("artifact_fidelity_verified must be a boolean")
    if artifact_fidelity_verifier is not None and not isinstance(
        artifact_fidelity_verifier, str
    ):
        errors.append("artifact_fidelity_verifier must be a string or null")
    if artifact_fidelity_verified is True and (
        not isinstance(artifact_fidelity_verifier, str)
        or not artifact_fidelity_verifier.strip()
    ):
        errors.append("artifact_fidelity_verifier is required when fidelity is verified")

    proof = record.get("proof")
    if not isinstance(proof, dict):
        errors.append("proof must be an object")
        proof = {}
    comparable_to = proof.get("comparable_to")
    if comparable_to is not None and not isinstance(comparable_to, str):
        errors.append("comparable_to must be a string or null")
    if not isinstance(proof.get("publishable_claim"), bool):
        errors.append("publishable_claim must be a boolean")
    accepted_ids = proof.get("accepted_inherited_decision_ids", [])
    if not isinstance(accepted_ids, list) or not all(
        isinstance(item, str) and item for item in accepted_ids
    ):
        errors.append("accepted_inherited_decision_ids must be a non-empty string list or []")
        accepted_ids = []
    if len(set(accepted_ids)) != len(accepted_ids):
        errors.append("accepted_inherited_decision_ids must not contain duplicates")
    if isinstance(accepted, int) and not isinstance(accepted, bool):
        if accepted != len(accepted_ids):
            errors.append(
                "accepted_inherited_decisions must match accepted_inherited_decision_ids"
            )

    proof_requirements = {
        "prospective_evidence": evidence_status == "prospective",
        "comparison_named": isinstance(comparable_to, str) and bool(comparable_to),
        "review_minutes_recorded": _is_number(review_minutes),
        "first_pass_recorded": isinstance(first_pass, bool),
        "critical_defects_recorded": isinstance(defects, int)
        and not isinstance(defects, bool),
        "inherited_decision_accepted": isinstance(accepted, int)
        and not isinstance(accepted, bool)
        and accepted > 0
        and len(accepted_ids) == accepted,
        "independent_operator": metrics.get("independent_operator") is True,
        "artifact_fidelity_verified": artifact_fidelity_verified is True
        and isinstance(artifact_fidelity_verifier, str)
        and bool(artifact_fidelity_verifier.strip()),
    }
    comparison_ready = all(proof_requirements.values())
    if proof.get("publishable_claim") is True:
        if not comparison_context:
            errors.append("publishable claim must be evaluated with the compare command")
        elif not comparison_ready:
            missing = [name for name, met in proof_requirements.items() if not met]
            errors.append(
                "publishable claim lacks required evidence: " + ", ".join(missing)
            )

    return {
        "valid": not errors,
        "comparison_ready": comparison_ready and not errors,
        "proof_ready": False,
        "errors": errors,
        "warnings": warnings,
        "proof_requirements": proof_requirements,
    }


def compare_records(
    baseline: dict[str, Any], followup: dict[str, Any]
) -> dict[str, Any]:
    baseline_validation = validate_record(baseline, comparison_context=True)
    followup_validation = validate_record(followup, comparison_context=True)
    failures: list[str] = []

    if not baseline_validation["valid"]:
        failures.append("baseline record is invalid")
    if not followup_validation["valid"]:
        failures.append("followup record is invalid")
    if baseline.get("workflow") != followup.get("workflow"):
        failures.append("workflow types do not match")
    if baseline.get("run_id") == followup.get("run_id"):
        failures.append("baseline and followup run IDs must differ")
    baseline_proof = baseline.get("proof")
    followup_proof = followup.get("proof")
    baseline_proof = baseline_proof if isinstance(baseline_proof, dict) else {}
    followup_proof = followup_proof if isinstance(followup_proof, dict) else {}
    if followup_proof.get("comparable_to") != baseline.get("run_id"):
        failures.append("followup does not name the baseline run")
    if baseline.get("evidence_status") != "prospective":
        failures.append("baseline evidence was not prospective")
    if followup.get("evidence_status") != "prospective":
        failures.append("followup evidence was not prospective")

    stage_requirements = (
        ("context_to_strategy", {"approved", "complete"}),
        ("strategy_to_market", {"approved", "complete"}),
        ("market_to_memory", {"complete"}),
    )
    stage_maps: dict[str, dict[str, Any]] = {}
    for label, record in (("baseline", baseline), ("followup", followup)):
        stages = record.get("stages")
        stages = stages if isinstance(stages, dict) else {}
        stage_maps[label] = stages
        for stage_name, allowed in stage_requirements:
            stage = stages.get(stage_name, {})
            status = stage.get("status") if isinstance(stage, dict) else None
            if status not in allowed:
                failures.append(f"{label} stage {stage_name} is unfinished")
    followup_stages = stage_maps["followup"]

    baseline_metrics = baseline.get("metrics")
    followup_metrics = followup.get("metrics")
    baseline_metrics = baseline_metrics if isinstance(baseline_metrics, dict) else {}
    followup_metrics = followup_metrics if isinstance(followup_metrics, dict) else {}
    baseline_minutes = baseline_metrics.get("human_review_minutes")
    followup_minutes = followup_metrics.get("human_review_minutes")
    reduction_percent: float | None = None
    if (
        _is_number(baseline_minutes)
        and baseline_minutes > 0
        and _is_number(followup_minutes)
    ):
        raw_reduction_percent = (
            (baseline_minutes - followup_minutes) / baseline_minutes
        ) * 100
        reduction_percent = round(raw_reduction_percent, 2)
        if raw_reduction_percent < 20:
            failures.append("review burden fell by less than 20%")
    else:
        failures.append("review burden cannot be compared")

    baseline_first_pass = baseline_metrics.get("first_pass_accepted")
    followup_first_pass = followup_metrics.get("first_pass_accepted")
    if not isinstance(baseline_first_pass, bool) or not isinstance(
        followup_first_pass, bool
    ):
        failures.append("first-pass acceptance cannot be compared")
    elif baseline_first_pass and not followup_first_pass:
        failures.append("first-pass acceptance regressed")

    baseline_defects = baseline_metrics.get("critical_defects")
    followup_defects = followup_metrics.get("critical_defects")
    if not isinstance(baseline_defects, int) or not isinstance(followup_defects, int):
        failures.append("critical defects cannot be compared")
    elif followup_defects > baseline_defects:
        failures.append("critical defects increased")

    inherited = followup_metrics.get("inherited_decisions")
    accepted = followup_metrics.get("accepted_inherited_decisions")
    if not isinstance(inherited, int) or not isinstance(accepted, int) or accepted < 1:
        failures.append("no inherited decision was accepted")
    elif accepted > inherited:
        failures.append("accepted inherited decisions exceed inherited decisions")

    accepted_ids = _string_set(
        followup_proof.get("accepted_inherited_decision_ids", [])
    )
    baseline_decision_items = baseline.get("decisions")
    followup_decision_items = followup.get("decisions")
    baseline_decision_items = (
        baseline_decision_items if isinstance(baseline_decision_items, list) else []
    )
    followup_decision_items = (
        followup_decision_items if isinstance(followup_decision_items, list) else []
    )
    baseline_locked_decisions = {
        decision.get("id"): decision
        for decision in baseline_decision_items
        if isinstance(decision, dict)
        and decision.get("status") == "locked"
        and isinstance(decision.get("id"), str)
    }
    followup_decisions = {
        decision.get("id"): decision
        for decision in followup_decision_items
        if isinstance(decision, dict) and isinstance(decision.get("id"), str)
    }
    followup_market = followup_stages.get("strategy_to_market")
    followup_market = followup_market if isinstance(followup_market, dict) else {}
    preserved_ids = _string_set(followup_market.get("preserved_decision_ids", []))
    if not accepted_ids:
        failures.append("accepted inherited decision IDs are missing")
    elif not accepted_ids <= baseline_locked_decisions.keys():
        failures.append("accepted inherited decision IDs are absent from the baseline")
    elif not accepted_ids <= followup_decisions.keys():
        failures.append("accepted inherited decision IDs are absent from the followup")
    elif not accepted_ids <= preserved_ids:
        failures.append("accepted inherited decision IDs were not preserved")
    else:
        for decision_id in accepted_ids:
            baseline_decision = baseline_locked_decisions[decision_id]
            followup_decision = followup_decisions[decision_id]
            if followup_decision.get("status") != "locked":
                failures.append(
                    f"accepted inherited decision {decision_id} is not locked in followup"
                )
            elif any(
                followup_decision.get(field) != baseline_decision.get(field)
                for field in ("decision", "source")
            ):
                failures.append(
                    f"accepted inherited decision {decision_id} changed meaning or source"
                )

    if followup_metrics.get("independent_operator") is not True:
        failures.append("independent teammate rerun is missing")
    for label, metrics in (
        ("baseline", baseline_metrics),
        ("followup", followup_metrics),
    ):
        verifier = metrics.get("artifact_fidelity_verifier")
        if (
            metrics.get("artifact_fidelity_verified") is not True
            or not isinstance(verifier, str)
            or not verifier.strip()
        ):
            failures.append(f"{label} artifact fidelity was not human-verified")

    return {
        "qualifies": not failures,
        "proof_ready": not failures,
        "baseline_run": baseline.get("run_id"),
        "followup_run": followup.get("run_id"),
        "review_reduction_percent": reduction_percent,
        "failures": failures,
        "baseline_validation": baseline_validation,
        "followup_validation": followup_validation,
    }


def load_json(path: Path) -> dict[str, Any]:
    with path.open(encoding="utf-8") as handle:
        data = json.load(handle)
    if not isinstance(data, dict):
        raise ValueError("run record must be a JSON object")
    return data


def main() -> int:
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest="command", required=True)

    validate_parser = subparsers.add_parser("validate")
    validate_parser.add_argument("record", type=Path)

    compare_parser = subparsers.add_parser("compare")
    compare_parser.add_argument("baseline", type=Path)
    compare_parser.add_argument("followup", type=Path)

    args = parser.parse_args()
    try:
        if args.command == "validate":
            result = validate_record(load_json(args.record))
            print(json.dumps(result, indent=2, allow_nan=False))
            return 0 if result["valid"] else 1
        result = compare_records(load_json(args.baseline), load_json(args.followup))
        print(json.dumps(result, indent=2, allow_nan=False))
        return 0 if result["qualifies"] else 1
    except (OSError, ValueError) as exc:
        print(json.dumps({"error": str(exc)}, indent=2, allow_nan=False))
        return 2


if __name__ == "__main__":
    sys.exit(main())
