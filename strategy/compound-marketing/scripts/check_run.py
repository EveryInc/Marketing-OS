#!/usr/bin/env python3
"""Validate Compound Marketing run records and compare repeated workflows."""

from __future__ import annotations

import argparse
import fcntl
import hashlib
import json
import math
import os
import re
import sys
from contextlib import contextmanager
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


REQUIRED_STAGES = (
    "context_to_strategy",
    "strategy_to_market",
    "market_to_memory",
)
V2_RECEIPT_STAGE = "strategy_to_market"
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


def _as_dict(value: Any) -> dict[str, Any]:
    return value if isinstance(value, dict) else {}


def _as_list(value: Any) -> list[Any]:
    return value if isinstance(value, list) else []


def _nonempty_string(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def _parse_iso(value: Any) -> datetime | None:
    if not _nonempty_string(value):
        return None
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        return None
    if parsed.tzinfo is None:
        return None
    return parsed


def _stable_digest(value: Any) -> str:
    payload = json.dumps(
        value, sort_keys=True, separators=(",", ":"), ensure_ascii=False, allow_nan=False
    ).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


def _resolve_shared_file(reference: str, record_path: Path) -> Path:
    run_root = record_path.resolve().parent
    path = Path(reference)
    if not path.is_absolute():
        path = run_root / path
    resolved_path = path.resolve()
    try:
        resolved_path.relative_to(run_root)
    except ValueError as exc:
        raise ValueError("shared files must stay inside the run directory") from exc
    return resolved_path


def _load_shared_json(reference: str, record_path: Path) -> dict[str, Any]:
    path = _resolve_shared_file(reference, record_path)
    with path.open(encoding="utf-8") as handle:
        data = json.load(handle)
    if not isinstance(data, dict):
        raise ValueError(f"{reference} must contain a JSON object")
    return data


def _artifact_receipt_failures(
    record: dict[str, Any], *, label: str, record_path: Path | None
) -> list[str]:
    """Verify shared artifact receipts required for a compounding claim."""

    failures: list[str] = []
    if record_path is None:
        return [f"{label} artifact receipts cannot be verified without a record path"]

    decision_record = record.get("decision_record")
    if not isinstance(decision_record, dict):
        return [f"{label} decision record reference is missing"]
    decision_path = decision_record.get("path")
    decision_version = decision_record.get("version")
    if not isinstance(decision_path, str) or not decision_path.strip():
        failures.append(f"{label} decision record path is missing")
    else:
        try:
            with _resolve_shared_file(decision_path, record_path).open(encoding="utf-8"):
                pass
        except (OSError, ValueError):
            failures.append(f"{label} decision record is unreadable")
    if not isinstance(decision_version, str) or not decision_version.strip():
        failures.append(f"{label} decision record version is missing")

    stages = record.get("stages")
    stages = stages if isinstance(stages, dict) else {}
    for stage_name in REQUIRED_STAGES:
        stage = stages.get(stage_name)
        if not isinstance(stage, dict) or stage.get("status") == "not_applicable":
            continue
        receipt_reference = stage.get("artifact_receipt")
        if not isinstance(receipt_reference, str) or not receipt_reference.strip():
            failures.append(f"{label} stage {stage_name} has no artifact receipt")
            continue
        try:
            receipt = _load_shared_json(receipt_reference, record_path)
        except (OSError, ValueError):
            failures.append(f"{label} stage {stage_name} artifact receipt is unreadable")
            continue

        if receipt.get("schema_version") != 1:
            failures.append(
                f"{label} stage {stage_name} artifact receipt schema is invalid"
            )
        if receipt.get("run_id") != record.get("run_id"):
            failures.append(
                f"{label} stage {stage_name} artifact receipt names the wrong run"
            )
        if receipt.get("stage") != stage_name:
            failures.append(
                f"{label} stage {stage_name} artifact receipt names the wrong stage"
            )
        if receipt.get("artifact") != stage.get("artifact"):
            failures.append(
                f"{label} stage {stage_name} artifact receipt names the wrong artifact"
            )

        receipt_decision_record = receipt.get("decision_record")
        if not isinstance(receipt_decision_record, dict) or (
            receipt_decision_record.get("path") != decision_path
            or receipt_decision_record.get("version") != decision_version
        ):
            failures.append(
                f"{label} stage {stage_name} artifact receipt has the wrong decision record"
            )

        expected_ids: set[str] = set()
        if stage_name == "context_to_strategy":
            expected_ids = _string_set(stage.get("output_decision_ids", []))
        elif stage_name == "strategy_to_market":
            expected_ids = _string_set(stage.get("preserved_decision_ids", []))
        receipt_ids = receipt.get("decision_ids")
        if not isinstance(receipt_ids, list) or not all(
            isinstance(item, str) and item for item in receipt_ids
        ):
            failures.append(
                f"{label} stage {stage_name} artifact receipt decision IDs are invalid"
            )
        elif _string_set(receipt_ids) != expected_ids:
            failures.append(
                f"{label} stage {stage_name} artifact receipt decision IDs do not match"
            )

        for field in ("verified_by", "verified_at"):
            if not isinstance(receipt.get(field), str) or not receipt[field].strip():
                failures.append(
                    f"{label} stage {stage_name} artifact receipt has no {field}"
                )

    return failures


def _validate_v1(
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


def _compare_v1(
    baseline: dict[str, Any],
    followup: dict[str, Any],
    *,
    baseline_path: Path | None = None,
    followup_path: Path | None = None,
) -> dict[str, Any]:
    baseline_validation = _validate_v1(baseline, comparison_context=True)
    followup_validation = _validate_v1(followup, comparison_context=True)
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

    failures.extend(
        _artifact_receipt_failures(
            baseline, label="baseline", record_path=baseline_path
        )
    )
    failures.extend(
        _artifact_receipt_failures(
            followup, label="followup", record_path=followup_path
        )
    )

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


WORKFLOW_FAMILIES = {"brand_strategy", "company_strategy", "program", "gtm"}
ROUTED_OUTPUTS = {"marketing_gtm", "program_brief", "gtm_plan", "one_pager"}
ACTIVE_LIFECYCLE = {
    "open",
    "strategy_pending",
    "strategy_approved",
    "artifact_pending",
    "artifact_approved",
    "measuring",
    "blocked",
}
TERMINAL_LIFECYCLE = {"closed", "abandoned"}
LEGAL_TRANSITIONS = {
    "open": {"strategy_pending", "blocked", "abandoned"},
    "strategy_pending": {"strategy_approved", "blocked", "abandoned"},
    "strategy_approved": {"artifact_pending", "blocked", "abandoned"},
    "artifact_pending": {"artifact_approved", "blocked", "abandoned"},
    "artifact_approved": {"measuring", "blocked", "abandoned"},
    "measuring": {"closed", "blocked", "abandoned"},
    "blocked": {"abandoned"},
}

LIFECYCLE_METADATA = {
    "open": ("context_to_strategy", "Confirm source authority and governing decisions."),
    "strategy_pending": ("context_to_strategy", "Resolve blockers and approve the strategy."),
    "strategy_approved": ("strategy_to_market", "Create the routed market artifact."),
    "artifact_pending": ("strategy_to_market", "Verify the artifact against locked decisions."),
    "artifact_approved": ("market_to_memory", "Declare the measure before the next run starts."),
    "measuring": ("market_to_memory", "Record outcomes and close the run."),
    "closed": ("complete", "Start a linked successor run when the workflow repeats."),
    "abandoned": ("complete", "Start a new run if the work resumes."),
}


class IneligibleError(ValueError):
    """Expected domain failure that should return CLI exit code 1."""


def _governance_projection(record: dict[str, Any]) -> dict[str, Any]:
    """Return the canonical, approval-governed strategy state."""

    return {
        "schema_version": record.get("schema_version"),
        "run_id": record.get("run_id"),
        "project": record.get("project"),
        "project_key": record.get("project_key"),
        "workflow_family": record.get("workflow_family"),
        "routed_output": record.get("routed_output"),
        "sources": _as_list(record.get("sources")),
        "source_conflicts": _as_list(record.get("source_conflicts")),
        "decisions": _as_list(record.get("decisions")),
        "protected_language": _as_list(record.get("protected_language")),
        "questions": _as_list(record.get("questions")),
    }


def governance_digest(record: dict[str, Any]) -> str:
    return _stable_digest(_governance_projection(record))


def approval_digest(record: dict[str, Any], approval: str) -> str:
    if approval != "comparability":
        return governance_digest(record)
    primary = _as_dict(_as_dict(record.get("metrics")).get("primary"))
    comparison_projection = {
        "governance_digest": governance_digest(record),
        "proof": _as_dict(record.get("proof")),
        "primary_metric_declaration": {
            key: primary.get(key)
            for key in (
                "name",
                "unit",
                "method",
                "declared_by",
                "declared_at",
                "work_started_at",
                "measurement_window",
            )
        },
    }
    return _stable_digest(comparison_projection)


def _locked_decision_ids(record: dict[str, Any]) -> list[str]:
    return sorted(
        item["id"]
        for item in _as_list(record.get("decisions"))
        if isinstance(item, dict)
        and item.get("status") == "locked"
        and _nonempty_string(item.get("id"))
    )


def _artifact_binding_digest(binding: Any) -> str | None:
    return _stable_digest(binding) if isinstance(binding, dict) else None


def _set_lifecycle_metadata(lifecycle: dict[str, Any]) -> None:
    status = lifecycle.get("status")
    if status == "blocked":
        prior = lifecycle.get("prior_status")
        stage, _ = LIFECYCLE_METADATA.get(
            prior, ("context_to_strategy", "Resume the prior stage.")
        )
        lifecycle["current_stage"] = stage
        lifecycle["next_action"] = "Resolve the recorded blocker, then resume."
        return
    stage, action = LIFECYCLE_METADATA.get(
        status, ("context_to_strategy", "Repair the lifecycle record.")
    )
    lifecycle["current_stage"] = stage
    lifecycle["next_action"] = action


def _now() -> str:
    return datetime.now(timezone.utc).isoformat()


def _slug(value: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")
    return slug or "project"


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _atomic_json(path: Path, data: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(f".{path.name}.{os.getpid()}.tmp")
    temporary.write_text(
        json.dumps(data, indent=2, sort_keys=True, allow_nan=False) + "\n",
        encoding="utf-8",
    )
    os.replace(temporary, path)


def _run_root(project_root: Path) -> Path:
    root = (project_root / ".compound-marketing").resolve()
    project = project_root.resolve()
    try:
        root.relative_to(project)
    except ValueError as exc:
        raise ValueError("run root must stay inside the project directory") from exc
    return root


def _unfinished_matches(
    project_root: Path, *, project_key: str, workflow_family: str
) -> list[Path]:
    root = _run_root(project_root)
    if not root.exists():
        return []
    matches: list[Path] = []
    for path in sorted(root.glob("*/run.json")):
        resolved = path.resolve()
        try:
            resolved.relative_to(root)
        except ValueError:
            continue
        try:
            record = load_json(resolved)
        except (OSError, ValueError, json.JSONDecodeError):
            continue
        lifecycle = record.get("lifecycle")
        status = lifecycle.get("status") if isinstance(lifecycle, dict) else None
        if (
            record.get("schema_version") == 2
            and record.get("project_key") == project_key
            and record.get("workflow_family") == workflow_family
            and status not in TERMINAL_LIFECYCLE
        ):
            matches.append(resolved)
    return matches


@contextmanager
def _initialization_lock(
    project_root: Path, *, project_key: str, workflow_family: str
):
    """Serialize discovery and creation for one project/workflow pair."""

    lock_root = _run_root(project_root) / ".locks"
    lock_root.mkdir(parents=True, exist_ok=True)
    lock_path = lock_root / f"{project_key}-{workflow_family}.lock"
    with lock_path.open("a+", encoding="utf-8") as handle:
        fcntl.flock(handle.fileno(), fcntl.LOCK_EX)
        try:
            yield
        finally:
            fcntl.flock(handle.fileno(), fcntl.LOCK_UN)


def discover_run(
    project_root: Path, *, project: str, workflow_family: str
) -> Path | None:
    if not _nonempty_string(project):
        raise ValueError("project must be a non-empty string")
    if workflow_family not in WORKFLOW_FAMILIES:
        raise ValueError("workflow family is invalid")
    matches = _unfinished_matches(
        project_root,
        project_key=_slug(project),
        workflow_family=workflow_family,
    )
    if len(matches) > 1:
        raise IneligibleError(
            "multiple unfinished runs match: " + ", ".join(str(path) for path in matches)
        )
    return matches[0] if matches else None


def _unsigned_approval(*, applicable: bool = True) -> dict[str, Any]:
    return {
        "applicable": applicable,
        "approved_by": None,
        "approved_at": None,
        "record_digest": None,
        "artifact_binding": None,
        "reason": None,
    }


def _new_v2_record(
    *,
    run_id: str,
    project: str,
    workflow_family: str,
    routed_output: str,
    operator: str,
) -> dict[str, Any]:
    timestamp = _now()
    return {
        "schema_version": 2,
        "run_id": run_id,
        "project": project,
        "project_key": _slug(project),
        "workflow_family": workflow_family,
        "routed_output": routed_output,
        "operator": operator,
        "created_at": timestamp,
        "updated_at": timestamp,
        "lifecycle": {
            "status": "open",
            "prior_status": None,
            "current_stage": "context_to_strategy",
            "next_action": "Confirm source authority and governing decisions.",
            "blocked_on": None,
            "closed_at": None,
            "abandoned_at": None,
        },
        "predecessor_run": None,
        "sources": [],
        "source_conflicts": [],
        "decisions": [],
        "protected_language": [],
        "questions": [],
        "artifact": {
            "class": routed_output,
            "scope": None,
            "primary_audience": None,
            "owner": None,
            "path": None,
            "remote_revision": None,
            "snapshot_sha256": None,
            "receipt": None,
        },
        "metrics": {
            "primary": {
                "name": None,
                "unit": None,
                "method": None,
                "declared_by": None,
                "declared_at": None,
                "work_started_at": None,
                "observed_at": None,
                "value": None,
                "measurement_window": None,
                "decision_date": None,
            },
            "human_review_minutes": None,
            "first_pass_accepted": None,
            "critical_defects": None,
        },
        "approvals": {
            "strategy": _unsigned_approval(),
            "artifact": _unsigned_approval(),
            "fidelity": _unsigned_approval(),
            "comparability": _unsigned_approval(),
            "publication": _unsigned_approval(applicable=False),
        },
        "evidence": {"timing": "prospective", "origin": "operational"},
        "proof": {
            "comparable_to": None,
            "accepted_inherited_decision_ids": [],
            "dimensions": {
                "artifact_class": routed_output,
                "scope": None,
                "primary_audience": None,
                "measurement_method": None,
            },
            "comparability_rationale": None,
        },
        "projections": {
            "run": {"path": "run.md", "sha256": None},
            "decision_record": {"path": "decision-record.md", "sha256": None},
        },
    }


def initialize_run(
    project_root: Path,
    *,
    project: str,
    workflow_family: str,
    routed_output: str,
    operator: str,
    force_new: bool = False,
    predecessor: Path | None = None,
) -> Path:
    if workflow_family not in WORKFLOW_FAMILIES:
        raise ValueError("workflow family is invalid")
    if routed_output not in ROUTED_OUTPUTS:
        raise ValueError("routed output is invalid")
    for name, value in (("project", project), ("operator", operator)):
        if not isinstance(value, str) or not value.strip():
            raise ValueError(f"{name} must be a non-empty string")
    project_key = _slug(project)
    with _initialization_lock(
        project_root, project_key=project_key, workflow_family=workflow_family
    ):
        predecessor_binding: dict[str, Any] | None = None
        if predecessor is not None:
            predecessor = predecessor.resolve()
            try:
                predecessor.relative_to(_run_root(project_root))
            except ValueError as exc:
                raise ValueError(
                    "predecessor must stay inside the project run root"
                ) from exc
            previous = load_json(predecessor)
            previous_lifecycle = _as_dict(previous.get("lifecycle"))
            if previous.get("schema_version") != 2:
                raise ValueError("predecessor must be a schema V2 record")
            if previous_lifecycle.get("status") not in TERMINAL_LIFECYCLE:
                raise IneligibleError("predecessor run must be terminal")
            if previous.get("project_key") != project_key:
                raise IneligibleError("predecessor project does not match")
            if previous.get("workflow_family") != workflow_family:
                raise IneligibleError("predecessor workflow does not match")
            predecessor_binding = {
                "run_id": previous.get("run_id"),
                "path": str(predecessor),
                "governance_digest": governance_digest(previous),
            }
            force_new = True
        else:
            existing = discover_run(
                project_root, project=project, workflow_family=workflow_family
            )
            if existing is not None and not force_new:
                return existing

        root = _run_root(project_root)
        root.mkdir(parents=True, exist_ok=True)
        prefix = f"{project_key}-{workflow_family}"
        suffix = datetime.now(timezone.utc).strftime("%Y%m%d%H%M%S%f")
        run_id = f"{prefix}-{suffix}"
        run_dir = root / run_id
        run_dir.mkdir()
        record_path = run_dir / "run.json"
        record = _new_v2_record(
            run_id=run_id,
            project=project,
            workflow_family=workflow_family,
            routed_output=routed_output,
            operator=operator,
        )
        record["predecessor_run"] = predecessor_binding
        _commit_rendered_record(record_path, record)
        return record_path.resolve()


def _decision_markdown(record: dict[str, Any]) -> str:
    lines = [
        "# Compound Marketing Decision Record",
        "",
        f"Run: {record.get('run_id')}",
        f"Project: {record.get('project')}",
        f"Workflow: {record.get('workflow_family')}",
        "",
        "## Sources",
        "",
    ]
    for source in record.get("sources", []):
        if isinstance(source, dict):
            lines.append(
                f"- {source.get('id')}: {source.get('authority')} — "
                f"{source.get('location')} ({source.get('status')})"
            )
    lines.extend(["", "## Decisions", ""])
    for decision in record.get("decisions", []):
        if isinstance(decision, dict):
            lines.append(
                f"- {decision.get('id')} [{decision.get('status')}]: {decision.get('decision')}"
            )
    lines.extend(["", "## Protected language", ""])
    for phrase in record.get("protected_language", []):
        if isinstance(phrase, dict):
            lines.append(f"- {phrase.get('id')}: {phrase.get('text')}")
    lines.extend(["", "## Open questions", ""])
    for question in record.get("questions", []):
        if isinstance(question, dict) and question.get("status") != "resolved":
            lines.append(f"- {question.get('id')}: {question.get('question')}")
    return "\n".join(lines).rstrip() + "\n"


def _run_markdown(record: dict[str, Any]) -> str:
    lifecycle = record.get("lifecycle", {})
    artifact = record.get("artifact", {})
    return (
        "# Compound Marketing Run\n\n"
        f"- Run: {record.get('run_id')}\n"
        f"- Project: {record.get('project')}\n"
        f"- Workflow: {record.get('workflow_family')}\n"
        f"- Route: {record.get('routed_output')}\n"
        f"- Operator: {record.get('operator')}\n"
        f"- Status: {lifecycle.get('status')}\n"
        f"- Next action: {lifecycle.get('next_action')}\n"
        f"- Artifact: {artifact.get('path')}\n"
    )


def _assert_renderable(record: dict[str, Any]) -> None:
    if record.get("schema_version") != 2:
        raise ValueError("render requires a schema V2 record")
    for field in ("lifecycle", "artifact", "projections"):
        if not isinstance(record.get(field), dict):
            raise ValueError(f"render requires {field} to be an object")
    for field in (
        "sources",
        "source_conflicts",
        "decisions",
        "protected_language",
        "questions",
    ):
        if not isinstance(record.get(field), list):
            raise ValueError(f"render requires {field} to be a list")


def _require_active_run(record: dict[str, Any]) -> None:
    status = _as_dict(record.get("lifecycle")).get("status")
    if status in TERMINAL_LIFECYCLE:
        raise IneligibleError("terminal run cannot be mutated")
    if status not in ACTIVE_LIFECYCLE:
        raise ValueError("lifecycle status is invalid")


def _commit_rendered_record(
    record_path: Path, record: dict[str, Any]
) -> dict[str, Path]:
    """Render projections first, then atomically commit the canonical record."""

    record_path = record_path.resolve()
    _assert_renderable(record)
    run_path = _resolve_shared_file("run.md", record_path)
    decision_path = _resolve_shared_file("decision-record.md", record_path)
    run_temporary = run_path.with_name(f".{run_path.name}.{os.getpid()}.tmp")
    decision_temporary = decision_path.with_name(
        f".{decision_path.name}.{os.getpid()}.tmp"
    )
    previous_projection_bytes = {
        run_path: run_path.read_bytes() if run_path.is_file() else None,
        decision_path: decision_path.read_bytes() if decision_path.is_file() else None,
    }
    try:
        run_temporary.write_text(_run_markdown(record), encoding="utf-8")
        decision_temporary.write_text(_decision_markdown(record), encoding="utf-8")
        projections = {
            "run": {"path": "run.md", "sha256": _sha256(run_temporary)},
            "decision_record": {
                "path": "decision-record.md",
                "sha256": _sha256(decision_temporary),
            },
        }
        os.replace(run_temporary, run_path)
        os.replace(decision_temporary, decision_path)
        record["governance_digest"] = governance_digest(record)
        record["projections"] = projections
        record["updated_at"] = _now()
        _atomic_json(record_path, record)
    except Exception:
        for path, previous in previous_projection_bytes.items():
            if previous is None:
                try:
                    path.unlink()
                except FileNotFoundError:
                    pass
                continue
            restore = path.with_name(f".{path.name}.{os.getpid()}.restore")
            restore.write_bytes(previous)
            os.replace(restore, path)
        raise
    finally:
        for temporary in (run_temporary, decision_temporary):
            try:
                temporary.unlink()
            except FileNotFoundError:
                pass
    return {"run": run_path, "decision_record": decision_path}


def render_run(record_path: Path) -> dict[str, Path]:
    record_path = record_path.resolve()
    record = load_json(record_path)
    _assert_renderable(record)
    _require_active_run(record)
    return _commit_rendered_record(record_path, record)


def _require_current_governance(record: dict[str, Any], record_path: Path) -> None:
    projection_errors, _ = _projection_failures(record, record_path)
    if projection_errors or record.get("governance_digest") != governance_digest(record):
        raise IneligibleError("render the current governance record before handoff or receipt")


def scaffold_handoff(record_path: Path, *, owner: str) -> Path:
    record_path = record_path.resolve()
    record = load_json(record_path)
    if record.get("schema_version") != 2:
        raise ValueError("handoff requires a schema V2 record")
    _require_active_run(record)
    _require_current_governance(record, record_path)
    if not _nonempty_string(owner):
        raise ValueError("owner must be a non-empty string")
    decision_ids = _locked_decision_ids(record)
    protected_ids = [
        item.get("id")
        for item in record.get("protected_language", [])
        if isinstance(item, dict)
    ]
    question_ids = [
        item.get("id")
        for item in record.get("questions", [])
        if isinstance(item, dict) and item.get("status") != "resolved"
    ]
    decision_projection = record.get("projections", {}).get("decision_record", {})
    handoff = {
        "schema_version": 2,
        "run_id": record.get("run_id"),
        "run_record": str(record_path),
        "decision_record": str(record_path.parent / "decision-record.md"),
        "decision_record_version": record.get("updated_at"),
        "decision_record_sha256": decision_projection.get("sha256"),
        "governance_digest": governance_digest(record),
        "workflow_family": record.get("workflow_family"),
        "routed_output": record.get("routed_output"),
        "inherited_decision_ids": decision_ids,
        "protected_language_ids": protected_ids,
        "unresolved_question_ids": question_ids,
        "artifact_owner": owner,
        "approved_by": None,
        "approved_at": None,
    }
    path = _resolve_shared_file("handoff.json", record_path)
    _atomic_json(path, handoff)
    return path


def scaffold_receipt(record_path: Path, *, stage: str, artifact: str) -> Path:
    record_path = record_path.resolve()
    record = load_json(record_path)
    if record.get("schema_version") != 2:
        raise ValueError("receipt requires a schema V2 record")
    _require_active_run(record)
    _require_current_governance(record, record_path)
    if stage != V2_RECEIPT_STAGE:
        raise ValueError(f"receipt stage must be {V2_RECEIPT_STAGE}")
    artifact_path = Path(artifact)
    binding: dict[str, Any]
    if artifact_path.is_absolute() or "://" not in artifact:
        local = (
            artifact_path
            if artifact_path.is_absolute()
            else record_path.parent / artifact_path
        )
        local = local.resolve()
        try:
            local.relative_to(record_path.parent)
        except ValueError as exc:
            raise ValueError("artifact must stay inside the run directory") from exc
        if not local.is_file():
            raise ValueError("local artifact must be an existing regular file")
        binding = {"kind": "local", "path": str(local), "sha256": _sha256(local)}
    elif artifact.startswith("https://"):
        binding = {"kind": "remote", "url": artifact, "revision": None, "snapshot_sha256": None}
    else:
        raise ValueError("remote artifact must use https://")
    receipt = {
        "schema_version": 2,
        "run_id": record.get("run_id"),
        "stage": stage,
        "artifact": binding,
        "decision_record_sha256": record.get("projections", {})
        .get("decision_record", {})
        .get("sha256"),
        "governance_digest": governance_digest(record),
        "decision_ids": _locked_decision_ids(record),
        "verified_by": None,
        "verified_at": None,
    }
    path = _resolve_shared_file(f"{stage}-receipt.json", record_path)
    _atomic_json(path, receipt)
    record["artifact"]["path"] = artifact
    record["artifact"]["receipt"] = path.name
    _commit_rendered_record(record_path, record)
    return path


def _approval_signed(
    value: Any,
    *,
    artifact_required: bool = False,
    record_digest: str | None = None,
) -> bool:
    if not isinstance(value, dict) or value.get("applicable") is not True:
        return False
    if not all(
        isinstance(value.get(field), str) and value[field].strip()
        for field in ("approved_by", "approved_at", "record_digest")
    ):
        return False
    if _parse_iso(value.get("approved_at")) is None:
        return False
    if artifact_required and not (
        isinstance(value.get("artifact_binding"), str)
        and value["artifact_binding"].strip()
    ):
        return False
    if record_digest is not None and value.get("record_digest") != record_digest:
        return False
    return True


def _governance_structure_failures(record: dict[str, Any]) -> list[str]:
    failures: list[str] = []
    specifications = {
        "sources": ("id", "owner", "location", "authority", "freshness", "status"),
        "source_conflicts": ("id", "conflict", "owner", "status"),
        "decisions": ("id", "decision", "owner", "source_id", "status"),
        "protected_language": ("id", "text", "owner"),
        "questions": ("id", "question", "owner", "status"),
    }
    for collection, required_fields in specifications.items():
        entries = record.get(collection)
        if not isinstance(entries, list):
            failures.append(f"{collection} must be a list")
            continue
        invalid = any(
            not isinstance(item, dict)
            or not all(_nonempty_string(item.get(field)) for field in required_fields)
            or (
                collection in {"source_conflicts", "questions"}
                and not isinstance(item.get("blocking"), bool)
            )
            or (
                collection == "decisions"
                and item.get("status") not in VALID_DECISION_STATUSES
            )
            for item in entries
        )
        if invalid:
            failures.append(f"{collection} entries are invalid")
        identifiers = [
            item.get("id")
            for item in entries
            if isinstance(item, dict) and _nonempty_string(item.get("id"))
        ]
        if len(identifiers) != len(set(identifiers)):
            failures.append(f"{collection} IDs must be unique")

    source_ids = {
        item.get("id")
        for item in _as_list(record.get("sources"))
        if isinstance(item, dict) and _nonempty_string(item.get("id"))
    }
    if any(
        isinstance(item, dict)
        and _nonempty_string(item.get("source_id"))
        and item.get("source_id") not in source_ids
        for item in _as_list(record.get("decisions"))
    ):
        failures.append("decision source_id must reference a source")
    return failures


def _strategy_structure_failure(record: dict[str, Any]) -> str | None:
    sources = _as_list(record.get("sources"))
    if not sources:
        return "at least one authoritative source is required"
    structure_failures = _governance_structure_failures(record)
    if structure_failures:
        return structure_failures[0]
    if not _locked_decision_ids(record):
        return "at least one locked decision is required"
    for collection in ("source_conflicts", "questions"):
        if any(
            isinstance(item, dict)
            and item.get("blocking") is True
            and item.get("status") != "resolved"
            for item in _as_list(record.get(collection))
        ):
            return "blocking governance item is unresolved"
    return None


def _validate_v2_receipt(
    record: dict[str, Any], record_path: Path | None
) -> tuple[bool, str | None]:
    artifact = _as_dict(record.get("artifact"))
    reference = artifact.get("receipt")
    if record_path is None or not _nonempty_string(reference):
        return False, None
    try:
        receipt = _load_shared_json(reference, record_path)
    except (OSError, ValueError, json.JSONDecodeError):
        return False, None
    if (
        receipt.get("schema_version") != 2
        or receipt.get("run_id") != record.get("run_id")
        or receipt.get("stage") != "strategy_to_market"
        or receipt.get("governance_digest") != governance_digest(record)
        or receipt.get("decision_record_sha256")
        != _as_dict(_as_dict(record.get("projections")).get("decision_record")).get(
            "sha256"
        )
        or receipt.get("decision_ids") != _locked_decision_ids(record)
        or not _nonempty_string(receipt.get("verified_by"))
        or _parse_iso(receipt.get("verified_at")) is None
    ):
        return False, None
    binding = _as_dict(receipt.get("artifact"))
    if binding.get("kind") == "local":
        try:
            path = _resolve_shared_file(binding.get("path"), record_path)
            valid = (
                path.is_file()
                and _nonempty_string(binding.get("sha256"))
                and _sha256(path) == binding.get("sha256")
                and _resolve_shared_file(artifact.get("path"), record_path) == path
            )
        except (OSError, TypeError, ValueError):
            valid = False
    elif binding.get("kind") == "remote":
        valid = (
            _nonempty_string(binding.get("url"))
            and binding.get("url").startswith("https://")
            and artifact.get("path") == binding.get("url")
            and (
                _nonempty_string(binding.get("revision"))
                or _nonempty_string(binding.get("snapshot_sha256"))
            )
        )
    else:
        valid = False
    return (valid, _artifact_binding_digest(binding) if valid else None)


def _metrics_failure(record: dict[str, Any]) -> str | None:
    metrics = _as_dict(record.get("metrics"))
    minutes = metrics.get("human_review_minutes")
    defects = metrics.get("critical_defects")
    if not _is_number(minutes) or minutes < 0:
        return "human review minutes must be a nonnegative number"
    if not isinstance(metrics.get("first_pass_accepted"), bool):
        return "first-pass acceptance must be recorded"
    if isinstance(defects, bool) or not isinstance(defects, int) or defects < 0:
        return "critical defects must be a nonnegative integer"
    primary = _as_dict(metrics.get("primary"))
    if not all(
        _nonempty_string(primary.get(field))
        for field in ("name", "unit", "method", "declared_by", "measurement_window")
    ):
        return "primary metric declaration is incomplete"
    declared = _parse_iso(primary.get("declared_at"))
    started = _parse_iso(primary.get("work_started_at"))
    observed = _parse_iso(primary.get("observed_at"))
    if (
        declared is None
        or started is None
        or observed is None
        or not declared <= started <= observed
    ):
        return "primary metric timing is invalid"
    return None


def _transition_prerequisite(
    record: dict[str, Any], target: str, *, record_path: Path
) -> str | None:
    approvals = _as_dict(record.get("approvals"))
    digest = governance_digest(record)
    if target == "strategy_approved":
        structural_failure = _strategy_structure_failure(record)
        if structural_failure:
            return structural_failure
        if not _approval_signed(approvals.get("strategy"), record_digest=digest):
            return "strategy approval is unsigned or stale"
    if target == "artifact_approved":
        receipt_ok, binding_digest = _validate_v2_receipt(record, record_path)
        if not receipt_ok:
            return "artifact receipt is unsigned, stale, or unbound"
        if not (
            _approval_signed(
                approvals.get("artifact"), artifact_required=True, record_digest=digest
            )
            and _approval_signed(
                approvals.get("fidelity"), artifact_required=True, record_digest=digest
            )
            and approvals["artifact"].get("artifact_binding") == binding_digest
            and approvals["fidelity"].get("artifact_binding") == binding_digest
        ):
            return "artifact acceptance or fidelity attestation is unsigned or stale"
    if target == "closed":
        return _metrics_failure(record)
    return None


def transition_run(record_path: Path, target: str, *, reason: str | None = None) -> None:
    record_path = record_path.resolve()
    record = load_json(record_path)
    if record.get("schema_version") != 2:
        raise ValueError("transition requires a schema V2 record")
    lifecycle = record.get("lifecycle")
    if not isinstance(lifecycle, dict):
        raise ValueError("lifecycle is invalid")
    current = lifecycle.get("status")
    if current in TERMINAL_LIFECYCLE:
        raise IneligibleError("terminal run cannot be mutated")
    if target == "resume":
        if current != "blocked" or lifecycle.get("prior_status") not in ACTIVE_LIFECYCLE:
            raise ValueError("blocked run has no resumable prior state")
        target = lifecycle["prior_status"]
        lifecycle["prior_status"] = None
        lifecycle["blocked_on"] = None
    elif target == "blocked":
        if current not in ACTIVE_LIFECYCLE - {"blocked"} or not reason:
            raise ValueError("blocking requires an active state and a reason")
        lifecycle["prior_status"] = current
        lifecycle["blocked_on"] = reason
    elif target not in LEGAL_TRANSITIONS.get(current, set()):
        raise ValueError(f"illegal lifecycle transition {current} -> {target}")
    prerequisite = _transition_prerequisite(record, target, record_path=record_path)
    if prerequisite:
        raise ValueError(prerequisite)
    lifecycle["status"] = target
    if target == "closed":
        lifecycle["closed_at"] = _now()
    if target == "abandoned":
        lifecycle["abandoned_at"] = _now()
        if reason:
            lifecycle["blocked_on"] = reason
    _set_lifecycle_metadata(lifecycle)
    record["updated_at"] = _now()
    _commit_rendered_record(record_path, record)


def _projection_failures(
    record: dict[str, Any], record_path: Path | None
) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    codes: list[str] = []
    if record_path is None:
        return ["record path is required to verify projections"], ["RECORD_PATH_REQUIRED"]
    projections = record.get("projections") if isinstance(record.get("projections"), dict) else {}
    for key, code in (
        ("run", "RUN_PROJECTION_STALE"),
        ("decision_record", "DECISION_PROJECTION_STALE"),
    ):
        item = projections.get(key) if isinstance(projections.get(key), dict) else {}
        reference = item.get("path")
        expected = item.get("sha256")
        try:
            path = (
                _resolve_shared_file(reference, record_path)
                if isinstance(reference, str)
                else None
            )
            matches = (
                path is not None
                and path.is_file()
                and isinstance(expected, str)
                and _sha256(path) == expected
            )
        except (OSError, TypeError, ValueError):
            path = None
            matches = False
        if not matches:
            errors.append(f"{key} projection is missing or stale")
            codes.append(code)
    return errors, codes


def _validate_v2(record: dict[str, Any], *, record_path: Path | None = None) -> dict[str, Any]:
    errors: list[str] = []
    warnings: list[str] = []
    codes: list[str] = []
    for field in ("run_id", "project", "project_key", "operator", "created_at", "updated_at"):
        if not _nonempty_string(record.get(field)):
            errors.append(f"{field} must be a non-empty string")
            codes.append("FIELD_REQUIRED")
    if record.get("workflow_family") not in WORKFLOW_FAMILIES:
        errors.append("workflow_family is invalid")
        codes.append("WORKFLOW_INVALID")
    if record.get("routed_output") not in ROUTED_OUTPUTS:
        errors.append("routed_output is invalid")
        codes.append("ROUTE_INVALID")
    for field in (
        "lifecycle",
        "artifact",
        "metrics",
        "approvals",
        "evidence",
        "proof",
        "projections",
    ):
        if not isinstance(record.get(field), dict):
            errors.append(f"{field} must be an object")
            codes.append("SHAPE_INVALID")
    for field in ("sources", "source_conflicts", "decisions", "protected_language", "questions"):
        if not isinstance(record.get(field), list):
            errors.append(f"{field} must be a list")
            codes.append("SHAPE_INVALID")
    approvals_shape = _as_dict(record.get("approvals"))
    if any(
        not isinstance(approvals_shape.get(name), dict)
        for name in ("strategy", "artifact", "fidelity", "comparability", "publication")
    ):
        errors.append("approval entries must be objects")
        codes.append("SHAPE_INVALID")
    if not isinstance(_as_dict(record.get("metrics")).get("primary"), dict):
        errors.append("metrics.primary must be an object")
        codes.append("SHAPE_INVALID")
    proof_shape = _as_dict(record.get("proof"))
    if not isinstance(proof_shape.get("dimensions"), dict) or not isinstance(
        proof_shape.get("accepted_inherited_decision_ids"), list
    ):
        errors.append("proof dimensions and inherited decision IDs are invalid")
        codes.append("SHAPE_INVALID")
    projections_shape = _as_dict(record.get("projections"))
    if any(
        not isinstance(projections_shape.get(name), dict)
        for name in ("run", "decision_record")
    ):
        errors.append("projection entries must be objects")
        codes.append("SHAPE_INVALID")

    lifecycle = _as_dict(record.get("lifecycle"))
    status = lifecycle.get("status")
    if status not in ACTIVE_LIFECYCLE | TERMINAL_LIFECYCLE:
        errors.append("lifecycle status is invalid")
        codes.append("LIFECYCLE_INVALID")
    if status == "blocked" and (
        lifecycle.get("prior_status") not in ACTIVE_LIFECYCLE
        or not _nonempty_string(lifecycle.get("blocked_on"))
    ):
        errors.append("blocked lifecycle is missing prior state or reason")
        codes.append("BLOCKED_STATE_INVALID")
    closed_at = lifecycle.get("closed_at")
    abandoned_at = lifecycle.get("abandoned_at")
    timestamps_valid = (
        status == "closed"
        and _parse_iso(closed_at) is not None
        and abandoned_at is None
    ) or (
        status == "abandoned"
        and _parse_iso(abandoned_at) is not None
        and closed_at is None
    ) or (
        status in ACTIVE_LIFECYCLE and closed_at is None and abandoned_at is None
    )
    if not timestamps_valid:
        errors.append("terminal timestamps contradict lifecycle status")
        codes.append("LIFECYCLE_TIMESTAMP_INVALID")
    expected_lifecycle = dict(lifecycle)
    _set_lifecycle_metadata(expected_lifecycle)
    if (
        lifecycle.get("current_stage") != expected_lifecycle.get("current_stage")
        or lifecycle.get("next_action") != expected_lifecycle.get("next_action")
    ):
        errors.append("lifecycle stage or next action contradicts status")
        codes.append("LIFECYCLE_METADATA_STALE")

    sources = _as_list(record.get("sources"))
    if not sources:
        warnings.append("at least one authoritative source is required")
        codes.append("SOURCE_REQUIRED")
    governance_failures = _governance_structure_failures(record)
    if governance_failures:
        errors.extend(governance_failures)
        codes.extend("GOVERNANCE_INVALID" for _ in governance_failures)
    conflicts = _as_list(record.get("source_conflicts"))
    if any(
        isinstance(item, dict)
        and item.get("blocking") is True
        and item.get("status") != "resolved"
        for item in conflicts
    ):
        errors.append("blocking source conflict is unresolved")
        codes.append("SOURCE_CONFLICT_OPEN")
    questions = _as_list(record.get("questions"))
    if any(
        isinstance(item, dict)
        and item.get("blocking") is True
        and item.get("status") != "resolved"
        for item in questions
    ):
        errors.append("blocking question is unresolved")
        codes.append("QUESTION_BLOCKING")
    decisions = _as_list(record.get("decisions"))
    locked_ids = set(_locked_decision_ids(record))
    if not locked_ids:
        warnings.append("at least one locked decision is required")
        codes.append("DECISION_REQUIRED")

    predecessor = record.get("predecessor_run")
    if predecessor is not None:
        predecessor_failure: str | None = None
        if record_path is None or not isinstance(predecessor, dict):
            predecessor_failure = "predecessor binding is invalid"
        elif not all(
            _nonempty_string(predecessor.get(field))
            for field in ("run_id", "path", "governance_digest")
        ):
            predecessor_failure = "predecessor binding is incomplete"
        else:
            try:
                previous_path = Path(predecessor["path"]).resolve()
                previous_path.relative_to(record_path.resolve().parent.parent)
                if previous_path.name != "run.json":
                    raise ValueError("predecessor must reference a run.json file")
                previous = load_json(previous_path)
                if (
                    previous.get("schema_version") != 2
                    or _as_dict(previous.get("lifecycle")).get("status")
                    not in TERMINAL_LIFECYCLE
                    or previous.get("run_id") != predecessor.get("run_id")
                    or previous.get("run_id") == record.get("run_id")
                    or previous.get("project_key") != record.get("project_key")
                    or previous.get("workflow_family") != record.get("workflow_family")
                    or governance_digest(previous)
                    != predecessor.get("governance_digest")
                ):
                    predecessor_failure = "predecessor binding does not match a terminal run"
            except (OSError, ValueError, json.JSONDecodeError):
                predecessor_failure = "predecessor run is unreadable"
        if predecessor_failure:
            errors.append(predecessor_failure)
            codes.append("PREDECESSOR_INVALID")

    projection_errors, projection_codes = _projection_failures(record, record_path)
    errors.extend(projection_errors)
    codes.extend(projection_codes)
    current_digest = governance_digest(record)
    if record.get("governance_digest") != current_digest:
        errors.append("canonical governance digest is missing or stale")
        codes.append("GOVERNANCE_DIGEST_STALE")

    structural_ready = not errors and bool(sources) and bool(locked_ids)
    approvals = _as_dict(record.get("approvals"))
    artifact = _as_dict(record.get("artifact"))
    metrics = _as_dict(record.get("metrics"))
    receipt_ok, binding_digest = _validate_v2_receipt(record, record_path)
    artifact_approvals_ok = (
        _approval_signed(
            approvals.get("artifact"), artifact_required=True, record_digest=current_digest
        )
        and _approval_signed(
            approvals.get("fidelity"), artifact_required=True, record_digest=current_digest
        )
        and binding_digest is not None
        and _as_dict(approvals.get("artifact")).get("artifact_binding") == binding_digest
        and _as_dict(approvals.get("fidelity")).get("artifact_binding") == binding_digest
    )
    operational_ready = (
        structural_ready
        and status == "closed"
        and _approval_signed(approvals.get("strategy"), record_digest=current_digest)
        and artifact_approvals_ok
        and receipt_ok
        and _metrics_failure(record) is None
        and record.get("evidence") == {"timing": "prospective", "origin": "operational"}
    )
    proof = _as_dict(record.get("proof"))
    primary = _as_dict(metrics.get("primary"))
    dimensions = _as_dict(proof.get("dimensions"))
    expected_dimensions = {
        "artifact_class": artifact.get("class"),
        "scope": artifact.get("scope"),
        "primary_audience": artifact.get("primary_audience"),
        "measurement_method": primary.get("method"),
    }
    dimensions_ok = (
        dimensions == expected_dimensions
        and all(_nonempty_string(value) for value in dimensions.values())
    )
    comparison_ready = (
        operational_ready
        and _nonempty_string(proof.get("comparable_to"))
        and bool(_string_set(proof.get("accepted_inherited_decision_ids")))
        and _nonempty_string(proof.get("comparability_rationale"))
        and dimensions_ok
        and _approval_signed(
            approvals.get("comparability"),
            record_digest=approval_digest(record, "comparability"),
        )
    )
    if not receipt_ok and artifact.get("receipt"):
        warnings.append("artifact receipt is unsigned, stale, or unbound")
        codes.append("RECEIPT_INVALID")
    return {
        "valid": not errors,
        "legacy": False,
        "structural_ready": structural_ready,
        "operational_ready": operational_ready,
        "comparison_ready": comparison_ready,
        "proof_ready": False,
        "failure_codes": list(dict.fromkeys(codes)),
        "errors": errors,
        "warnings": warnings,
    }


def validate_record(
    record: dict[str, Any],
    *,
    comparison_context: bool = False,
    record_path: Path | None = None,
) -> dict[str, Any]:
    if record.get("schema_version") == 2:
        return _validate_v2(record, record_path=record_path)
    result = _validate_v1(record, comparison_context=comparison_context)
    result.update(
        {
            "legacy": True,
            "structural_ready": result["valid"],
            "operational_ready": False,
            "proof_ready": False,
            "failure_codes": [] if result["valid"] else ["LEGACY_INVALID"],
        }
    )
    return result


def _compare_v2(
    baseline: dict[str, Any],
    followup: dict[str, Any],
    *,
    baseline_path: Path | None,
    followup_path: Path | None,
) -> dict[str, Any]:
    baseline_validation = _validate_v2(baseline, record_path=baseline_path)
    followup_validation = _validate_v2(followup, record_path=followup_path)
    failures: list[str] = []
    if not baseline_validation["valid"] or not followup_validation["valid"]:
        if not baseline_validation["valid"]:
            failures.append("baseline record is invalid")
        if not followup_validation["valid"]:
            failures.append("followup record is invalid")
        return {
            "qualifies": False,
            "proof_eligible": False,
            "proof_ready": False,
            "publication_authorized": False,
            "baseline_run": baseline.get("run_id"),
            "followup_run": followup.get("run_id"),
            "review_reduction_percent": None,
            "failures": failures,
            "baseline_validation": baseline_validation,
            "followup_validation": followup_validation,
        }
    if not baseline_validation["operational_ready"]:
        failures.append("baseline is not operationally ready")
    if not followup_validation["comparison_ready"]:
        failures.append("followup is not comparison ready")
    if baseline.get("workflow_family") != followup.get("workflow_family"):
        failures.append("workflow families do not match")
    if baseline.get("run_id") == followup.get("run_id"):
        failures.append("baseline and followup run IDs must differ")
    baseline_operator = str(baseline.get("operator", "")).strip().casefold()
    followup_operator = str(followup.get("operator", "")).strip().casefold()
    if baseline_operator == followup_operator:
        failures.append("followup operator is not independent")
    proof = _as_dict(followup.get("proof"))
    if proof.get("comparable_to") != baseline.get("run_id"):
        failures.append("followup does not name the baseline run")
    baseline_metrics = _as_dict(baseline.get("metrics"))
    followup_metrics = _as_dict(followup.get("metrics"))
    baseline_primary = _as_dict(baseline_metrics.get("primary"))
    followup_primary = _as_dict(followup_metrics.get("primary"))
    baseline_artifact = _as_dict(baseline.get("artifact"))
    followup_artifact = _as_dict(followup.get("artifact"))
    baseline_dimensions = {
        "artifact_class": baseline_artifact.get("class"),
        "scope": baseline_artifact.get("scope"),
        "primary_audience": baseline_artifact.get("primary_audience"),
        "measurement_method": baseline_primary.get("method"),
    }
    followup_dimensions = {
        "artifact_class": followup_artifact.get("class"),
        "scope": followup_artifact.get("scope"),
        "primary_audience": followup_artifact.get("primary_audience"),
        "measurement_method": followup_primary.get("method"),
    }
    if (
        not all(_nonempty_string(value) for value in baseline_dimensions.values())
        or baseline_dimensions != followup_dimensions
        or _as_dict(_as_dict(baseline.get("proof")).get("dimensions"))
        != baseline_dimensions
        or _as_dict(proof.get("dimensions")) != followup_dimensions
    ):
        failures.append("comparison dimensions do not match")
    if not _nonempty_string(proof.get("comparability_rationale")):
        failures.append("comparability rationale is missing")
    accepted_ids = _string_set(proof.get("accepted_inherited_decision_ids"))
    baseline_locked = {
        item.get("id"): item
        for item in _as_list(baseline.get("decisions"))
        if isinstance(item, dict) and item.get("status") == "locked"
    }
    followup_locked = {
        item.get("id"): item
        for item in _as_list(followup.get("decisions"))
        if isinstance(item, dict) and item.get("status") == "locked"
    }
    if (
        not accepted_ids
        or not accepted_ids <= baseline_locked.keys()
        or not accepted_ids <= followup_locked.keys()
    ):
        failures.append("accepted inherited decision IDs are not preserved")
    else:
        baseline_sources = {
            item.get("id"): item
            for item in _as_list(baseline.get("sources"))
            if isinstance(item, dict) and _nonempty_string(item.get("id"))
        }
        followup_sources = {
            item.get("id"): item
            for item in _as_list(followup.get("sources"))
            if isinstance(item, dict) and _nonempty_string(item.get("id"))
        }
        for decision_id in sorted(accepted_ids):
            baseline_decision = baseline_locked[decision_id]
            followup_decision = followup_locked[decision_id]
            source_id = baseline_decision.get("source_id")
            baseline_source = _as_dict(baseline_sources.get(source_id))
            followup_source = _as_dict(
                followup_sources.get(followup_decision.get("source_id"))
            )
            source_identity_changed = any(
                baseline_source.get(field) != followup_source.get(field)
                for field in ("id", "owner", "location", "authority")
            )
            if source_identity_changed or any(
                baseline_decision.get(field) != followup_decision.get(field)
                for field in ("status", "decision", "source_id")
            ):
                failures.append(
                    f"accepted inherited decision {decision_id} changed meaning or source"
                )
                break
    baseline_minutes = baseline_metrics.get("human_review_minutes")
    followup_minutes = followup_metrics.get("human_review_minutes")
    reduction: float | None = None
    if _is_number(baseline_minutes) and baseline_minutes > 0 and _is_number(followup_minutes):
        raw_reduction = ((baseline_minutes - followup_minutes) / baseline_minutes) * 100
        reduction = round(raw_reduction, 2)
        if raw_reduction < 20:
            failures.append("review burden fell by less than 20%")
    else:
        failures.append("review burden cannot be compared")
    if (
        baseline_metrics.get("first_pass_accepted") is True
        and followup_metrics.get("first_pass_accepted") is not True
    ):
        failures.append("first-pass acceptance regressed")
    if (
        isinstance(baseline_metrics.get("critical_defects"), int)
        and isinstance(followup_metrics.get("critical_defects"), int)
        and followup_metrics["critical_defects"]
        > baseline_metrics["critical_defects"]
    ):
        failures.append("critical defects increased")
    return {
        "qualifies": not failures,
        "proof_eligible": not failures,
        "proof_ready": not failures,
        "publication_authorized": False,
        "baseline_run": baseline.get("run_id"),
        "followup_run": followup.get("run_id"),
        "review_reduction_percent": reduction,
        "failures": failures,
        "baseline_validation": baseline_validation,
        "followup_validation": followup_validation,
    }


def compare_records(
    baseline: dict[str, Any],
    followup: dict[str, Any],
    *,
    baseline_path: Path | None = None,
    followup_path: Path | None = None,
) -> dict[str, Any]:
    if baseline.get("schema_version") != 2 or followup.get("schema_version") != 2:
        return {
            "qualifies": False,
            "proof_eligible": False,
            "proof_ready": False,
            "publication_authorized": False,
            "failures": ["only schema V2 records are eligible for public proof"],
        }
    return _compare_v2(
        baseline,
        followup,
        baseline_path=baseline_path,
        followup_path=followup_path,
    )


def load_json(path: Path) -> dict[str, Any]:
    with path.open(encoding="utf-8") as handle:
        data = json.load(handle)
    if not isinstance(data, dict):
        raise ValueError("run record must be a JSON object")
    return data


def main() -> int:
    parser = argparse.ArgumentParser(description="Operate and verify Compound Marketing runs.")
    subparsers = parser.add_subparsers(dest="command", required=True)

    init_parser = subparsers.add_parser("init")
    init_parser.add_argument("project_root", type=Path)
    init_parser.add_argument("--project", required=True)
    init_parser.add_argument("--workflow", required=True, choices=sorted(WORKFLOW_FAMILIES))
    init_parser.add_argument("--route", required=True, choices=sorted(ROUTED_OUTPUTS))
    init_parser.add_argument("--operator", required=True)
    init_parser.add_argument("--force-new", action="store_true")
    init_parser.add_argument("--predecessor", type=Path)

    discover_parser = subparsers.add_parser("discover")
    discover_parser.add_argument("project_root", type=Path)
    discover_parser.add_argument("--project", required=True)
    discover_parser.add_argument("--workflow", required=True, choices=sorted(WORKFLOW_FAMILIES))

    for command in ("render", "handoff", "receipt", "transition"):
        command_parser = subparsers.add_parser(command)
        command_parser.add_argument("record", type=Path)
        if command == "handoff":
            command_parser.add_argument("--owner", required=True)
        elif command == "receipt":
            command_parser.add_argument(
                "--stage", required=True, choices=(V2_RECEIPT_STAGE,)
            )
            command_parser.add_argument("--artifact", required=True)
        elif command == "transition":
            command_parser.add_argument("status")
            command_parser.add_argument("--reason")

    validate_parser = subparsers.add_parser("validate")
    validate_parser.add_argument("record", type=Path)

    compare_parser = subparsers.add_parser("compare")
    compare_parser.add_argument("baseline", type=Path)
    compare_parser.add_argument("followup", type=Path)

    args = parser.parse_args()
    try:
        if args.command == "init":
            record_path = initialize_run(
                args.project_root,
                project=args.project,
                workflow_family=args.workflow,
                routed_output=args.route,
                operator=args.operator,
                force_new=args.force_new,
                predecessor=args.predecessor,
            )
            print(json.dumps({"record_path": str(record_path)}, indent=2))
            return 0
        if args.command == "discover":
            record_path = discover_run(
                args.project_root,
                project=args.project,
                workflow_family=args.workflow,
            )
            print(
                json.dumps(
                    {"record_path": str(record_path) if record_path else None},
                    indent=2,
                )
            )
            return 0
        if args.command == "render":
            paths = render_run(args.record)
            print(json.dumps({key: str(value) for key, value in paths.items()}, indent=2))
            return 0
        if args.command == "handoff":
            path = scaffold_handoff(args.record, owner=args.owner)
            print(json.dumps({"handoff_path": str(path)}, indent=2))
            return 0
        if args.command == "receipt":
            path = scaffold_receipt(
                args.record, stage=args.stage, artifact=args.artifact
            )
            print(json.dumps({"receipt_path": str(path)}, indent=2))
            return 0
        if args.command == "transition":
            transition_run(args.record, args.status, reason=args.reason)
            print(
                json.dumps(
                    {
                        "record_path": str(args.record.resolve()),
                        "status": args.status,
                    },
                    indent=2,
                )
            )
            return 0
        if args.command == "validate":
            result = validate_record(load_json(args.record), record_path=args.record)
            print(json.dumps(result, indent=2, allow_nan=False))
            ready = result["structural_ready"] if not result.get("legacy") else result["valid"]
            return 0 if ready else 1
        result = compare_records(
            load_json(args.baseline),
            load_json(args.followup),
            baseline_path=args.baseline,
            followup_path=args.followup,
        )
        print(json.dumps(result, indent=2, allow_nan=False))
        return 0 if result["qualifies"] else 1
    except IneligibleError as exc:
        print(json.dumps({"error": str(exc)}, indent=2, allow_nan=False))
        return 1
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print(json.dumps({"error": str(exc)}, indent=2, allow_nan=False))
        return 2


if __name__ == "__main__":
    sys.exit(main())
