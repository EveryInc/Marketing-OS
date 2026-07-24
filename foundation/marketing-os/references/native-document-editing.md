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
