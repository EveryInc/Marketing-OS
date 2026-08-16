#!/usr/bin/env python3
"""Validate Marketing OS smoke cases and learning candidates."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any


EXPECTED_WORKFLOWS = {
    "gtm",
    "executive-summary",
    "copy-adaptation",
    "art-direction-figma",
    "measurement",
}
CLASSIFICATIONS = {
    "durable-rule",
    "good-example",
    "regression-test",
    "temporary-fact",
    "one-off-taste",
}
SIGNALS = {
    "human-edit",
    "explicit-ruling",
    "measured-result",
    "repeated-pattern",
    "factual-correction",
}
PROMOTIONS = {"project-only", "candidate", "promote"}


def read_object(path: Path) -> tuple[dict[str, Any] | None, list[str]]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        return None, [f"cannot read valid JSON from {path}: {error}"]
    if not isinstance(value, dict):
        return None, [f"{path} must contain a JSON object"]
    return value, []


def require_text(value: Any, field: str, errors: list[str]) -> None:
    if not isinstance(value, str) or not value.strip():
        errors.append(f"{field} must be non-empty text")


def validate_smoke_manifest(path: Path, repo_root: Path) -> list[str]:
    data, errors = read_object(path)
    if data is None:
        return errors

    if data.get("skill") != "marketing-os":
        errors.append("smoke manifest skill must be marketing-os")
    if data.get("version") != 1:
        errors.append("smoke manifest version must be 1")

    cases = data.get("cases")
    if not isinstance(cases, list):
        return [*errors, "smoke manifest cases must be a list"]
    expected_case_count = len(EXPECTED_WORKFLOWS)
    if len(cases) != expected_case_count:
        errors.append(f"smoke manifest must contain exactly {expected_case_count} cases")

    ids: set[str] = set()
    workflows: set[str] = set()
    for index, case in enumerate(cases):
        label = f"case {index + 1}"
        if not isinstance(case, dict):
            errors.append(f"{label} must be an object")
            continue
        case_id = case.get("id")
        require_text(case_id, f"{label}.id", errors)
        if isinstance(case_id, str):
            if case_id in ids:
                errors.append(f"duplicate case id: {case_id}")
            ids.add(case_id)
        workflow = case.get("workflow")
        require_text(workflow, f"{label}.workflow", errors)
        if isinstance(workflow, str):
            workflows.add(workflow)
        require_text(case.get("task"), f"{label}.task", errors)

        for field in ("expected_behavior", "hard_failures"):
            values = case.get(field)
            if not isinstance(values, list) or not values:
                errors.append(f"{label}.{field} must be a non-empty list")
            elif not all(isinstance(item, str) and item.strip() for item in values):
                errors.append(f"{label}.{field} must contain non-empty text")

        skill_paths = case.get("skill_paths")
        if not isinstance(skill_paths, list) or not skill_paths:
            errors.append(f"{label}.skill_paths must be a non-empty list")
        else:
            for skill_path in skill_paths:
                if not isinstance(skill_path, str) or not skill_path.strip():
                    errors.append(f"{label}.skill_paths must contain non-empty paths")
                    continue

                relative_path = Path(skill_path)
                if relative_path.is_absolute():
                    errors.append(f"{label} skill path must be relative to the repository: {skill_path}")
                    continue
                if relative_path.name != "SKILL.md":
                    errors.append(f"{label} skill path must name a SKILL.md file: {skill_path}")
                    continue

                resolved_root = repo_root.resolve()
                resolved_path = (resolved_root / relative_path).resolve()
                try:
                    resolved_path.relative_to(resolved_root)
                except ValueError:
                    errors.append(f"{label} skill path escapes the repository: {skill_path}")
                    continue
                if not resolved_path.is_file():
                    errors.append(f"{label} references missing skill path: {skill_path}")

    if workflows != EXPECTED_WORKFLOWS:
        missing = sorted(EXPECTED_WORKFLOWS - workflows)
        extra = sorted(workflows - EXPECTED_WORKFLOWS)
        errors.append(f"smoke workflow coverage mismatch; missing={missing}, extra={extra}")
    return errors


def validate_learning_candidate(path: Path) -> list[str]:
    data, errors = read_object(path)
    if data is None:
        return errors

    for field in (
        "task_id",
        "observed_at",
        "task_type",
        "lesson",
        "destination",
        "limits",
    ):
        require_text(data.get(field), field, errors)

    signal = data.get("signal")
    if signal not in SIGNALS:
        errors.append(f"signal must be one of {sorted(SIGNALS)}")
    classification = data.get("classification")
    if classification not in CLASSIFICATIONS:
        errors.append(f"classification must be one of {sorted(CLASSIFICATIONS)}")
    promotion = data.get("promotion")
    if promotion not in PROMOTIONS:
        errors.append(f"promotion must be one of {sorted(PROMOTIONS)}")

    evidence = data.get("evidence")
    derived_evidence_count: int | None = None
    if not isinstance(evidence, list) or not evidence:
        errors.append("evidence must be a non-empty list")
    else:
        evidence_is_valid = all(
            isinstance(item, dict)
            and all(
                isinstance(item.get(field), str) and item[field].strip()
                for field in ("kind", "reference", "reason")
            )
            for item in evidence
        )
        if not evidence_is_valid:
            errors.append("each evidence item needs non-empty kind, reference, and reason")
        else:
            derived_evidence_count = len({item["reference"].strip() for item in evidence})

    evidence_count = data.get("independent_evidence_count")
    if not isinstance(evidence_count, int) or isinstance(evidence_count, bool) or evidence_count < 1:
        errors.append("independent_evidence_count must be a positive integer")
    elif derived_evidence_count is not None and evidence_count != derived_evidence_count:
        errors.append(
            "independent_evidence_count must match the number of distinct evidence references "
            f"({derived_evidence_count})"
        )

    causal_evidence = data.get("credible_causal_evidence")
    if not isinstance(causal_evidence, bool):
        errors.append("credible_causal_evidence must be true or false")
    elif causal_evidence and signal != "measured-result":
        errors.append("credible_causal_evidence may be true only when signal is measured-result")

    if data.get("contains_sensitive_detail") is not False:
        errors.append("repository candidates must not contain sensitive detail")

    if classification in {"temporary-fact", "one-off-taste"} and promotion != "project-only":
        errors.append(f"{classification} learning must remain project-only")

    promotion_evidence = signal in {"explicit-ruling", "factual-correction"} or (
        derived_evidence_count is not None and derived_evidence_count >= 2
    ) or (signal == "measured-result" and causal_evidence is True)
    if classification == "durable-rule" and promotion == "promote" and not promotion_evidence:
        errors.append(
            "durable-rule promotion needs an explicit ruling, factual correction, credible causal evidence, or two independent examples"
        )
    if classification in {"good-example", "regression-test"} and promotion == "promote":
        errors.append(f"{classification} must remain a candidate until placed in a relevant evaluation")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest="command", required=True)

    smoke = subparsers.add_parser("smoke")
    smoke.add_argument("manifest", type=Path)
    smoke.add_argument("--repo-root", type=Path, required=True)

    candidate = subparsers.add_parser("candidate")
    candidate.add_argument("file", type=Path)

    args = parser.parse_args()
    if args.command == "smoke":
        errors = validate_smoke_manifest(args.manifest, args.repo_root)
    else:
        errors = validate_learning_candidate(args.file)

    if errors:
        print("FAIL")
        for error in errors:
            print(f"- {error}")
        return 1
    print("PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
