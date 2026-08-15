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


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("file", type=Path)
    parser.add_argument("--mode", choices=("gtm", "social", "scoped"), default="gtm")
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

    forbidden = ["room", *args.forbid_phrase]
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
