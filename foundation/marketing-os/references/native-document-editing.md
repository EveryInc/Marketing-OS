# Native Document Editing

Use this protocol before changing an existing Google Doc, Word document, presentation,
spreadsheet, or other formatted collaborative artifact.

## Formatting is part of the source

Treat tab topology, section order, spacing, typography, lists, tables, links, comments,
inline objects, and local formatting as authored content. Visible text alone is not the
document.

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
