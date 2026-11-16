---
title: Live-editable plan page lost line breaks, could not delete blocks, and broke on save
date: 2026-11-16
category: ui-bugs
module: marketing/gtm
problem_type: ui_bug
component: development_workflow
symptoms:
  - "Line breaks typed in an editable text block ran together after save and reload"
  - "The owner typed DELETE into a card because text editing could not remove it"
  - "A saved copy of the page came back without its editor, or with a script error"
  - "Removing a block made a saved text override land on a different element"
root_cause: missing_validation
resolution_type: workflow_improvement
severity: medium
tags:
  - editable-page
  - plan-document
  - saved-edits
  - self-publishing-page
---

# Live-editable plan page lost edits

## Context

A plan was delivered as a single HTML page that the owner could edit in place. Text edits
were stored as overrides keyed by the original text and its occurrence number, and the page
republished itself with the overrides embedded. Four faults reached the owner.

## What went wrong

- **Line breaks.** Overrides were applied with `textContent` under normal white-space, so
  typed line breaks collapsed after reload.
- **No way to delete.** Text editing cannot remove an element. The owner marked a card
  "DELETE" and cleared two fields, leaving a visible stub and an empty slot.
- **Capture order.** The page captured its own source for republishing from a script that
  ran before a later script had been parsed, so saved copies lost the later script.
- **Self-matching pattern.** The save step used a pattern containing the literal opening
  tag of the overrides block. The pattern text itself sat earlier in the document and
  matched first, corrupting the saved copy.
- **Key drift.** After a block was removed from the template, an override keyed to "the
  first element with this text" matched a different element.

## Solution

- Set `white-space: pre-line` on editable text.
- Treat "DELETE" or an emptied field as a request to remove the block, and remove it in
  the source. Give the editor a remove control if owners will restructure.
- Capture the source in the last script, before any script changes the page, and start
  every other script from there.
- Locate the overrides block with string search on a marker assembled at run time, never
  with a pattern that contains the marker literally.
- When removing or changing a block in the template, drop the overrides keyed to it and
  check the rest still land on the intended elements.
- Before every republish, read the live page's saved overrides and merge them. Tell the
  owner that a republish reloads open views and drops unsaved edits.
- Check who the page is shared with before promising a republish. A change in sharing can
  change what the session is allowed to publish.

## Verify

Run the full loop in a browser: edit, save, reload the saved copy, edit again, save again.
Confirm the second-generation copy still has the editor, the line breaks, and no script
errors.
