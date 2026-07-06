# Notion Launch Scaffold

Builds the standard Notion launch structure for an Every launch: the calendar entry, the
sectioned burn-down with owned/dated/annotated tasks, and the per-section views — exactly
to the scaffold standard in `launches/canonical-process.md`. This skill exists because the
scaffold was built by hand twice in one day (the Every Agent and Cora 2.0, July 2026) and
every future launch needs the same structure without re-deriving it.

## When to invoke

- "Build the Notion doc / launch doc / burn-down for [launch]"
- "Set up the launch calendar entry for [product]"
- "Reorganize this launch page into sections"
- Standing up Week 1 of any L/XL launch (canon Rule 4: calendar and burn-down exist from Week 1)
- Cleaning up a template-generated launch page into the standard

## Inputs to collect before writing anything

1. The launch calendar entry (URL) or permission to create one; the launch date and tier.
2. The roster — collected, never inherited. Project owner is Brandon with the product GM
   as co-ruler (canon ruling); everything else is asked.
3. The section subset. Default six per the canon; launches subset by ruling (Cora 2.0
   dropped Influencer + Affiliate + PR).
4. Actual state of each track for mid-flight (L) entries — completed phases get marked
   with evidence, never regenerated as Not Started.
5. Work-back dates from `launch-calendar` — this skill places dates, it does not compute them.

## Procedure

1. **Audit before writing.** Query the shared tasks database for the launch's existing
   tasks. Diff against the canon's phase checklists. Update stubs in place; never create
   a duplicate of a task that exists under another name.
2. **Tasks.** Create/update every burn-down item with: Owner (real person, or "TBD with
   [name]" in the note — never a silent blank), Deadline from the work-back, Section, and
   a note in the standard format: `[Function] What it is. What it derives from / feeds.
   Open questions plainly marked.` Assumed owners and proposed dates are labeled as such
   in the note itself.
3. **Page.** Remove duplicate untitled views (verify a block is a linked view before
   deleting it — fetch it; if it is the source database, stop). Insert one heading + one
   section-filtered table view per section, in canon order, each view sorted by Deadline
   showing Deliverable / Owner / Status / Deadline / Notes.
4. **Verify.** Re-query and diff the final task list against the intended list. Report
   exactly what was created, updated, and skipped — never imply completeness.
5. **Hand back the manual steps** as a checklist (see limitations).

## Known API limitations (verified July 2026 — hand these to the human)

- View relation filters cannot be set via the API. Every section view needs
  "Launch → contains → [this page]" added in the UI and saved for everyone, or views
  cross-contaminate between launches that share Section values.
- Rows ARE the tasks. Deleting a row deletes the task from every view on every page.
  Views are removed to change display; rows are deleted only to kill a task.
- Page moves out of a database require an interactive approval; if it fails, hand the
  drag-and-drop step to the human.
- Tasks cannot be trashed via the API — flag deletions for the human instead.

## Dependencies

- `foundation/marketing-os`
- `launches/canonical-process.md` (loaded always — the scaffold standard and phase checklists)
- `launches/launch-calendar` (dates in)
- `launches/launch-brief` (Week 1 content in, when it exists)

## Quick checklist

- [ ] Existing tasks queried and diffed before any write
- [ ] Every task: Owner, Deadline, Section, standard-format note
- [ ] Assumptions and proposed dates labeled in the notes themselves
- [ ] Mid-flight completed work marked with evidence, not regenerated
- [ ] Duplicate views verified as linked views before removal
- [ ] Section headings + views in canon order
- [ ] Final diff reported: created / updated / skipped
- [ ] Manual checklist delivered: Launch filters per view, any flagged deletions
