# Editing

A rigorous editing skill for marketing copy, adapted from a publishing-editor methodology
and retuned for brand and campaign work. Where copywriting generates, editing refines —
running existing drafts through structured filters to ensure they meet Every's standards
for clarity, voice, effectiveness, and craft.

This skill is opinionated: it doesn't just fix grammar. It evaluates whether the copy
works commercially, whether it sounds like the brand, and whether it reads like a human
wrote it with intention.

## System

Editing is composed of four reference files, each representing a filter or methodology:

### references/filters.md
The four editorial filters: blind spot (what's missing?), thesis (does this have a
point?), prose quality (does it read well?), and brand fit (does it sound like us?).
Every piece of copy runs through all four.

### references/ai-tells.md
How to detect and strip AI-generated patterns — the rhythms, hedges, structures, and
vocabulary choices that mark copy as machine-written. The goal is not to hide AI use
but to ensure the output meets human editorial standards.

### references/surgery.md
When to cut vs. rewrite vs. reorder. The decision framework for structural editing —
knowing whether a paragraph needs a scalpel, a rewrite, or a different position in
the piece.

### references/effectiveness-check.md
Does this copy actually work commercially? The final filter — evaluating whether the
copy does what it was written to do (convert, persuade, inform, engage) rather than
just sounding good.

### references/compound-from-edits.md
How to learn from Douglas's edits: compare versions, classify the delta, preserve his
version as canonical, and update the relevant durable rule without overwriting the work.

## When to invoke

- When reviewing and refining a draft for voice alignment
- When tightening copy that's already been written
- When a piece needs a final pass before publication
- When evaluating whether existing copy meets brand and effectiveness standards
- When stripping AI tells from generated or co-written copy
- When Douglas returns an edited draft and asks to compound or remember the changes

## Reference routing

| Task type | Load |
|---|---|
| Full editorial pass on a draft | `references/filters.md` |
| Detecting or removing AI-generated patterns | `references/ai-tells.md` |
| Structural editing decisions (cut, rewrite, reorder) | `references/surgery.md` |
| Evaluating commercial effectiveness of copy | `references/effectiveness-check.md` |
| Learning durable rules from a human-edited draft | `references/compound-from-edits.md` |

## Dependencies

- `foundation/marketing-os`
- `brand-voice/{relevant brand}` (loaded dynamically)

## Quick checklist

- Did the edit preserve the argument and creative premise?
- Did it remove repetition rather than unique information?
- Is the language active, specific, and recognizably Every?
- Does the piece still do its intended job?
- If Douglas edited it, did the system learn from the delta?
