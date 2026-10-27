# Native Document Editing

Use this protocol before changing an existing Google Doc, Word document, presentation,
spreadsheet, or other formatted collaborative artifact.

## Formatting is part of the source

Treat tab topology, section order, spacing, typography, lists, tables, links, comments,
inline objects, and local formatting as authored content. Visible text alone is not the
document.

## Douglas's annotation policy: explicit permission only

Do not add notes to Douglas's documents or decks unless he explicitly requests them.
This includes speaker notes, comments, footnotes, source appendices, production caveats,
editorial instructions, and visible or hidden process annotations. Moving a note to a
different surface does not satisfy a no-notes instruction. Research and citation habits,
templates, and generic presentation guidance cannot override this policy.

Keep research provenance and production records in local working files. Put material
qualifications inside the substantive claim, or omit the unsupported claim. Do not add a
source section as a workaround. A later explicit request for comments or citations
authorizes only that requested surface and scope; it does not lift this standing policy.
Preserve existing user-authored notes unless their removal is requested.

Before every write, including a one-cell edit:

1. List the permitted content targets. Exclude annotation surfaces by default.
2. Inspect the proposed mutation for extra notes, citations, comments, and footers.
3. For Google Slides, capture the notes-page IDs and speakerNotesObjectId values from
   the native presentation. Run `../scripts/check_slide_notes.py preflight BEFORE.json
   REQUESTS.json` before submitting the batch. Stop on failure. This blocks mutations
   targeting existing note objects; it does not inspect the meaning of slide-face copy.
4. Read back after saving. Run `../scripts/check_slide_notes.py compare BEFORE.json
   AFTER.json` to detect changed notes and notes inherited by new slides. For Docs and
   other formats, compare the accessible comment/footnote/annotation surfaces directly.
   If an annotation surface cannot be checked, report that verification limit.

Do not duplicate slides containing notes into new pages by default. Use a clean layout
or recreate the requested content. Preflight and readback are both required; rendering
the slide faces alone cannot verify this policy. Explicitly requested note edits use a
separately scoped batch and an authorized target list, not a blanket guard bypass.

## Use the bounded-edit fast path

When the user asks for a narrow append, insertion, or replacement in a named destination,
do only the work needed to make that edit safely:

1. Read the supplied source material.
2. Open the target tab or section and inspect the insertion point plus the nearest
   comparable formatting.
3. Draft and write the requested content in one bounded update when the tool allows it.
4. Re-read the edited target once to confirm the content and local formatting.

This fast path supersedes the broader document audit below when the operation does not
rename, reorder, merge, delete, or restructure tabs; alter tables, comments, or inline
objects; or depend on conflicting sources elsewhere in the file. Do not inventory
unrelated tabs, search the wider workspace, or reconstruct the document's authority map
for a straightforward local edit. Expand the inspection only when the target is unclear,
a material fact is missing, the write fails, or the requested change affects document
structure.

## Before editing

1. Identify the exact file and current revision.
2. Record every tab or sheet, its title, order, and nesting.
3. Inspect headings, paragraph styles, lists, tables, links, comments, and inline
   objects near the intended edit.
4. Establish a recoverable version-history checkpoint.
5. Separate the requested operation into copyedit, targeted rewrite, restructuring, or
   full replacement. Do not infer a broader operation.

## During editing

- Edit inside the existing native structure.
- Make the smallest change that satisfies the request.
- Preserve local formatting by copying the nearest comparable element.
- Re-read after index-shifting or structural changes.
- Do not reconstruct a formatted, multi-tab document from extracted plain text.
- Do not rename, reorder, merge, or delete tabs unless the user explicitly requests it.

## After editing

Verify:

- Tab count, titles, order, and nesting.
- Heading and paragraph hierarchy.
- Lists, tables, links, and inline objects.
- The requested content and nothing outside its scope.
- The saved revision and the ability to restore the prior version.

If native structure cannot be preserved reliably, stop before writing and explain the
limitation.

## Remove presentation annotations precisely

When asked to remove notes from slide faces, identify the annotation objects and remove
only those objects. Preserve the argument, artwork, branding, navigation, page numbers,
and native structure. Do not recreate the same commentary as smaller footer text.

Do not relocate removed annotations into speaker notes, comments, or another section.
Apply the annotation policy above. Retain any qualifier needed for a truthful visible
claim. A request to remove notes does not authorize changing the strategy or deleting
substantive production-plan content. Read back the saved deck and verify that unaffected
objects and slide order remain intact. For broader deck work, use `strategy-decks.md`.

## Reconcile multi-tab strategy documents

When a workbook or document contains several generations of strategy, do not treat every
tab as equally authoritative or rewrite the file into a new summary.

1. Inventory every tab before editing.
2. Identify the governing strategy and the source with authority for its current wording.
3. Classify each tab as canonical strategy, supporting execution, dated research, or
   archive. Mark dated material; do not let it quietly compete with the current strategy.
4. Reconcile one messaging hierarchy across the document: brand promise, positioning,
   value proposition, mechanism, reason to believe, proof, and category-parity support.
5. Preserve approved phrases exactly. Do not replace sharp language with generic synthesis.
6. Edit the minimum set of tabs in place and verify both content and formatting after each
   write. Confirm untouched tabs remain unchanged.
7. Keep execution detail separately linked when it operates at a different altitude from
   the executive strategy. The governing tab should state the strategy exactly rather than
   becoming another channel plan.

Conflicting tabs are a document-governance problem before they are a writing problem. Name
the winning source and the status of the others so a later reader does not reconstruct the
conflict.

## Cross-platform publishing

When the same strategy must appear in more than one tool:

1. Declare the canonical copy and formatting source separately.
2. Update every requested destination from the same approved copy.
3. Preserve the formatting source's heading hierarchy, paragraph roles, bullets,
   indentation, emphasis, links, tables, and spacing as closely as each tool allows.
4. Re-read every destination after writing.
5. Compare section order and paragraph text.
6. Verify protected phrases, links, citations, headings, bullets, and nested content.
7. Report unavoidable platform differences and state which destination remains
   canonical.

Two documents are synchronized only when the approved copy, section order, and intended
formatting match. Similar meaning is insufficient.
