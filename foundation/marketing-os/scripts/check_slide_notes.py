#!/usr/bin/env python3
"""Fail a default no-notes Slides edit on note mutations or changed note objects.

Usage: check_slide_notes.py preflight BEFORE.json REQUESTS.json
       check_slide_notes.py compare BEFORE.json AFTER.json
       check_slide_notes.py self-test
Accept native presentation JSON or its structuredContent wrapper. Requests may be a
list or a batchUpdate object. This guard does not inspect prose on slide faces or Docs.
"""
import copy
import json
import sys
import unittest
from pathlib import Path


def presentation(value):
    value = value.get("structuredContent", value)
    if not isinstance(value.get("slides"), list):
        raise ValueError("Expected native presentation JSON with slides")
    return value


def note_pages(value):
    result = {}
    for slide in presentation(value)["slides"]:
        if "notesPage" not in slide.get("slideProperties", {}):
            raise ValueError("Missing notesPage: retrieve complete native slide data")
        result[slide["objectId"]] = slide["slideProperties"]["notesPage"]
    return result


def strings(value):
    if isinstance(value, str):
        yield value
    elif isinstance(value, dict):
        for key, item in value.items():
            yield key
            yield from strings(item)
    elif isinstance(value, list):
        for item in value:
            yield from strings(item)


def note_ids(pages):
    result = set()
    for page in pages.values():
        result.add(page.get("objectId"))
        result.add(page.get("notesProperties", {}).get("speakerNotesObjectId"))
        result.update(e.get("objectId") for e in page.get("pageElements", []))
    return result - {None, ""}


def has_text(value):
    if isinstance(value, dict):
        if str(value.get("textRun", {}).get("content", "")).strip():
            return True
        return any(has_text(item) for item in value.values())
    if isinstance(value, list):
        return any(has_text(item) for item in value)
    return False


def preflight(before, batch):
    pages = note_pages(before)
    protected = note_ids(pages)
    requests = batch if isinstance(batch, list) else batch["requests"]
    errors = []
    for index, request in enumerate(requests):
        if protected.intersection(strings(request)):
            errors.append(f"Request {index}: targets a protected notes object")
        duplicate = request.get("duplicateObject", {}).get("objectId")
        if duplicate in pages and has_text(pages[duplicate]):
            errors.append(f"Request {index}: duplicates a slide containing notes")
    return errors


def compare(before, after):
    old, new = note_pages(before), note_pages(after)
    errors = []
    for slide_id, page in new.items():
        if slide_id in old:
            if page != old[slide_id]:
                errors.append(f"{slide_id}: notes page changed; inspect before proceeding")
        elif has_text(page):
            errors.append(f"{slide_id}: new slide contains notes")
    # Slide deletions are governed by the separate content-target scope check.
    return errors


def fixture(text="Existing user note"):
    return {"slides": [{"objectId": "slide1", "slideProperties": {"notesPage": {
        "objectId": "notes1", "notesProperties": {"speakerNotesObjectId": "note1"},
        "pageElements": [{"objectId": "note1", "shape": {"text": {
            "textElements": [{"textRun": {"content": text}}]}}}]
    }}}]}


class GuardTests(unittest.TestCase):
    def test_cell_edit_allowed(self):
        self.assertEqual(preflight(fixture(), [{"insertText": {"objectId": "cell1", "text": "New example"}}]), [])

    def test_source_note_blocked(self):
        self.assertTrue(preflight(fixture(), [{"insertText": {"objectId": "note1", "text": "Source and production details"}}]))

    def test_note_deletion_blocked(self):
        self.assertTrue(preflight(fixture(), [{"deleteText": {"objectId": "note1", "textRange": {"type": "ALL"}}}]))

    def test_note_page_mutation_blocked(self):
        self.assertTrue(preflight(fixture(), [{"deleteObject": {"objectId": "notes1"}}]))

    def test_annotated_duplicate_blocked(self):
        self.assertTrue(preflight(fixture(), [{"duplicateObject": {"objectId": "slide1"}}]))

    def test_clean_duplicate_allowed(self):
        self.assertEqual(preflight(fixture("\n"), [{"duplicateObject": {"objectId": "slide1"}}]), [])

    def test_existing_notes_preserved(self):
        self.assertEqual(compare(fixture(), copy.deepcopy(fixture())), [])

    def test_added_note_detected(self):
        self.assertTrue(compare(fixture(), fixture("Unrequested source")))

    def test_new_slide_inherited_notes_detected(self):
        after = fixture()
        after["slides"].append(copy.deepcopy(after["slides"][0]))
        after["slides"][1]["objectId"] = "new_slide"
        self.assertTrue(compare(fixture(), after))

    def test_missing_notes_data_fails_closed(self):
        with self.assertRaises(ValueError):
            preflight({"slides": [{"objectId": "slide1"}]}, [])


if __name__ == "__main__":
    if sys.argv[1:] == ["self-test"]:
        unittest.main(argv=[sys.argv[0]])
    elif len(sys.argv) == 4 and sys.argv[1] in ("preflight", "compare"):
        try:
            values = [json.loads(Path(p).read_text()) for p in sys.argv[2:]]
            errors = globals()[sys.argv[1]](*values)
        except (ValueError, KeyError, OSError, TypeError) as error:
            errors = [str(error)]
        print("\n".join(errors) if errors else "PASS: no note changes detected")
        sys.exit(bool(errors))
    else:
        sys.exit(__doc__)
