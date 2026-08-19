# Compound Marketing

Turn scattered company context into governed strategy and market action, then make the
accepted work improve the next comparable run. Use one decision record across the work
so human judgment survives every handoff.

## When to invoke

- When Douglas asks to run Compound Marketing or use Marketing OS end to end
- When a strategy, recurring marketing program, or GTM project has scattered sources
  and several decisions that must stay aligned
- When substantial human edits or measured results should improve the next project
- When the team needs evidence that a repeated workflow became faster or better

Do not invoke for a single line edit, one narrow research question, visual production,
or a task with no meaningful decision to preserve.

## Load the system

Read:

1. `../../foundation/marketing-os/SKILL.md`
2. `../../foundation/marketing-os/references/golden-path.md`
3. `../../foundation/marketing-os/references/collaboration.md`
4. `../../foundation/marketing-os/references/knowledge-boundaries.md`

Load `../../foundation/marketing-os/references/learning-loop.md` when an edit, ruling,
result, or repeated pattern may change future work.

## Open the run

Use `<project-root>/.compound-marketing/<run-id>/` as the shared run directory. Before
creating one, search `.compound-marketing/*/run.json` for an unfinished record with the
same project and workflow. Resume it when found; do not create a duplicate run.

Create `run.md`, `run.json`, and `decision-record.md` there from the references in this
skill. Do not store active project details in the Marketing OS repository. Pass the
three absolute paths and current decision-record version in every specialist handoff.

Establish:

- The objective and intended audience behavior.
- The project type: strategy, recurring program, or GTM.
- The source owners for facts, decisions, protected language, structure, and approval.
- The closest comparable workflow and available baseline.
- The primary decision metric, review-burden measure, guardrails, and decision date.
- The requested artifact and explicit exclusions.

If the user has already supplied these answers, continue. Search supplied company
sources before asking for anything discoverable. Ask one to three questions only when a
missing human judgment could change the direction, approval chain, or definition of
success.

## Carry one decision record

Build `references/decision-record.md` before writing the deliverable. Give each locked
decision a stable ID. Separate facts, decisions, protected language, evidence,
inferences, open questions, and rejected directions.

The decision record is the contract between stages. Every downstream artifact names the
version it inherited and the decision IDs it preserved. A source conflict remains open
until the named owner decides it.

## Run the path

Follow `../../foundation/marketing-os/references/golden-path.md`. It owns the stage
requirements and specialist routing. At every handoff, update `run.json` with the
artifact location, status, inherited decision IDs, protected-language IDs, open
questions, and human ruling. The specialist produces the work; this skill keeps the
governing record intact.

## Prove the system

Read `references/proof-standard.md` before making an improvement claim. Resolve
`<MARKETING_OS_ROOT>` from this loaded skill's repository, then run:

```bash
python3 <MARKETING_OS_ROOT>/strategy/compound-marketing/scripts/check_run.py validate <absolute-run-record.json>
python3 <MARKETING_OS_ROOT>/strategy/compound-marketing/scripts/check_run.py compare <absolute-baseline.json> <absolute-followup.json>
```

Structural checks prove only that the run record is internally consistent. A named human
must verify artifact fidelity before an operational or compounding claim.

## Use optional pods sparingly

Read `references/optional-pods.md` only when three or more independent jobs can run from
the same approved decision record. Keep the user in plain English. Agent count is never
a success metric.

## Dependencies

- `foundation/marketing-os`
- `strategy/program-brief` (routed)
- `strategy/one-pager` (routed)
- `marketing/gtm` (routed)
- `launches/gtm-plan` (routed)
- `craft/editing`
- `marketing-science/measurement`

## Quick checklist

- [ ] The run has an objective, baseline status, metric, and decision date
- [ ] Facts, decisions, protected language, and open questions are separate
- [ ] The human approved the governing decisions
- [ ] Downstream work names and preserves inherited decision IDs
- [ ] Human edits and results were compared with the original inputs
- [ ] Learning was classified before any durable file changed
- [ ] Improvement claims use comparable real runs and pass the proof standard
- [ ] Design, asset production, and channel automation remained outside V1
