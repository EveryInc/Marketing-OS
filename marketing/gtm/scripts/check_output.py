#!/usr/bin/env python3
"""Run deterministic checks against a Marketing / GTM output."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path


SOCIAL_FORBIDDEN_HEADINGS = {
    "channel roles",
    "response rules",
    "inputs and owners",
    "what we watch",
    "required assets",
}


def words(text: str) -> int:
    return len(re.findall(r"\b[\w’'-]+\b", text))


def headings(text: str) -> set[str]:
    return {
        match.group(1).strip().lower()
        for match in re.finditer(r"^#{1,6}\s+(.+?)\s*$", text, re.MULTILINE)
    }


def heading_positions(text: str) -> list[tuple[str, int]]:
    return [
        (match.group(1).strip().lower(), match.start())
        for match in re.finditer(r"^#{1,6}\s+(.+?)\s*$", text, re.MULTILINE)
    ]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("file", type=Path)
    parser.add_argument(
        "--mode",
        choices=("gtm", "social", "scoped", "approval-deck"),
        default="gtm",
    )
    parser.add_argument("--max-words", type=int)
    parser.add_argument("--require-heading", action="append", default=[])
    parser.add_argument("--require-phrase", action="append", default=[])
    parser.add_argument("--forbid-phrase", action="append", default=[])
    parser.add_argument("--protected-prefix-file", type=Path)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    text = args.file.read_text(encoding="utf-8")
    lower = text.lower()
    found_headings = headings(text)
    failures: list[str] = []

    max_words = args.max_words
    if max_words is None and args.mode == "social":
        max_words = 650
    if max_words is not None and words(text) > max_words:
        failures.append(f"word count {words(text)} exceeds {max_words}")

    required_headings = {item.lower() for item in args.require_heading}
    for heading in sorted(required_headings - found_headings):
        failures.append(f"missing heading: {heading}")

    if args.mode == "social":
        for heading in sorted(SOCIAL_FORBIDDEN_HEADINGS & found_headings):
            failures.append(f"social brief contains operating-manual heading: {heading}")

    if args.mode == "approval-deck":
        decision_pattern = (
            r"\b(approve|authorize)\b.{0,100}\b(system|ecosystem|production mandate)\b"
            r"|\b(system|ecosystem|production mandate)\b.{0,100}\b(approve|authorize)\b"
        )
        segment_size = max(1, len(text) // 3)
        if not re.search(decision_pattern, lower[:segment_size]):
            failures.append("system approval decision missing near beginning")
        if not re.search(decision_pattern, lower[-segment_size:]):
            failures.append("system approval decision missing near close")

        positions = heading_positions(text)
        sequence_positions = [
            position
            for heading, position in positions
            if "campaign sequence" in heading or heading.startswith("phase")
        ]
        system_positions = [
            position
            for heading, position in positions
            if heading == "content system"
            or heading.startswith("content format")
            or heading.startswith("asset inventory")
        ]
        if not sequence_positions:
            failures.append("missing campaign sequence or phase heading")
        if not system_positions:
            failures.append("missing content-system or format heading")
        if sequence_positions and system_positions and min(sequence_positions) > min(system_positions):
            failures.append("content inventory appears before campaign sequence")

        calendar_positions = [
            position for heading, position in positions if "calendar" in heading
        ]
        if not calendar_positions:
            failures.append("missing publishing calendar heading")
        else:
            calendar_position = min(calendar_positions)
            later_heading_positions = [
                position for _, position in positions if position > calendar_position
            ]
            calendar_end = min(later_heading_positions, default=len(text))
            calendar_text = lower[calendar_position:calendar_end]
            literal_entries = re.findall(
                r"^(?:[-*]\s*)?(?:mon(?:day)?|tue(?:sday)?|wed(?:nesday)?|thu(?:rsday)?|fri(?:day)?|sat(?:urday)?|sun(?:day)?|week\s+\d+|\d{1,2}/\d{1,2})\s*:\s*(.+)$",
                calendar_text,
                re.MULTILINE,
            )
            substantive_entries = [
                entry
                for entry in literal_entries
                if entry.strip().lower() not in {"tbd", "open", "unknown", "n/a", "—", "-"}
            ]
            if len(substantive_entries) < 2:
                failures.append("calendar needs at least two literal, non-placeholder entries")

            workstream_positions: list[int] = []
            for workstream in ("lock", "make", "publish", "ship"):
                matches = list(
                    re.finditer(
                        rf"^(?:#{{1,6}}\s+|(?:\d+[.)]|[-*])\s+)?"
                        rf"(?:\*\*)?{workstream}:?(?:\*\*)?(?=\s|$)",
                        lower,
                        re.MULTILINE,
                    )
                )
                valid = [match.start() for match in matches if match.start() >= calendar_end]
                if not valid:
                    failures.append(f"missing close workstream after calendar: {workstream}")
                else:
                    workstream_positions.append(min(valid))
            if len(workstream_positions) == 4 and workstream_positions != sorted(workstream_positions):
                failures.append("close workstreams are not ordered lock, make, publish, ship")

        if re.search(
            r"\b(approve|review|sign[- ]off on)\s+(each|every|individual)\s+"
            r"(post|cutdown|asset|format|video|workflow|calendar item)s?\b",
            lower,
        ):
            failures.append("asks leadership to approve or review individual content items")

    forbidden = ["room", "real", *args.forbid_phrase]
    for phrase in forbidden:
        if re.search(rf"\b{re.escape(phrase.lower())}\b", lower):
            failures.append(f"forbidden phrase: {phrase}")

    for phrase in args.require_phrase:
        if phrase.lower() not in lower:
            failures.append(f"missing phrase: {phrase}")

    if args.protected_prefix_file:
        prefix = args.protected_prefix_file.read_text(encoding="utf-8")
        if not text.startswith(prefix):
            failures.append("protected prefix changed")

    result = {
        "file": str(args.file),
        "mode": args.mode,
        "word_count": words(text),
        "passed": not failures,
        "failures": failures,
    }
    if args.json:
        print(json.dumps(result, indent=2))
    else:
        print("PASS" if result["passed"] else "FAIL")
        print(f"words: {result['word_count']}")
        for failure in failures:
            print(f"- {failure}")
    return 0 if result["passed"] else 1


if __name__ == "__main__":
    sys.exit(main())
