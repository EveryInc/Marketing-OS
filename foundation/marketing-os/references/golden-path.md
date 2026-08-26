# Compound Marketing Golden Path

Use this path for substantial strategy, recurring marketing, and GTM work. It connects
the existing specialist skills without making the user operate the repository.

## The loop

`context -> strategy -> market -> memory -> stronger next run`

Every run must produce useful work and leave behind a bounded improvement for the next
run. A project that ships without a learning may still be successful; a project that
creates a learning without shipping useful work is not.

## 0. Open the run

Before drafting, search `<project-root>/.compound-marketing/*/run.json` for an unfinished
matching run. Resume it when found. Otherwise create one run directory and record using
`../../../strategy/compound-marketing/references/run-record.md`.

Record:

- The objective and intended audience behavior.
- The project type: strategy, recurring program, or GTM.
- The sources that own facts, strategic decisions, canonical language, and approval.
- The closest comparable workflow and available baseline.
- The primary decision metric, guardrails, and decision date.
- What is explicitly outside this run.

If no baseline exists, label this run `BASELINE`. Do not invent improvement.

## 1. Context to strategy

Build a decision record using
`../../../strategy/compound-marketing/references/decision-record.md`.

Separate:

- Confirmed facts.
- Human-ruled decisions.
- Protected language.
- Evidence and observations.
- Inferences.
- Open questions with owners.
- Rejected or deferred directions.

Then write the smallest strategy that can govern the work. It must name the diagnosis,
audience, desired behavior, guiding choice, offer or value, proof requirement, primary
action, and strategic refusal.

Do not draft execution while a missing decision could change the strategy. Search
supplied Notion, Slack, Drive, research, and company sources before asking for anything
discoverable. Ask the human only for judgment, authority, or a decision the sources
cannot supply.

**Human gate:** The named strategy owner approves or redirects the decision record. A
positive reaction to prose is not approval of every embedded decision.

## 2. Strategy to market

Route from the approved decision record:

| Work | Route |
|---|---|
| Recurring campaign, channel, event, partnership, PR, or research program | `strategy/program-brief` |
| Any launch strategy, GTM plan, launch backbone, drumbeat, or social brief | `marketing/gtm` |
| 10- to 15-minute GTM approval deck for a launch content ecosystem | `marketing/gtm`, using its content-system approval-deck reference and the approved decision record |
| Related copy sequence that should learn from human edits | `craft/compound-copywriting` |
| Executive decision document | `strategy/one-pager` |

Every downstream artifact must cite the decision-record version it inherited. Preserve
the approved audience, idea, offer, proof, primary action, exact protected language, and
open questions. Adapt the expression to the artifact; do not reopen the strategy.

Before delivery, compare the artifact with the decision record. Any missing or changed
decision must be restored, approved as a new decision, or left visibly unresolved.

**Human gate:** The named approver accepts the exact artifact version. Record substantial
edits instead of absorbing them silently.

## 3. Market to memory

Close the run from two evidence streams:

1. **Human edits:** Compare the draft and accepted artifact using
   `../../../craft/editing/references/compound-from-edits.md`.
2. **Market results:** After the measurement window, use
   `../../../marketing-science/measurement/references/compound-from-results.md`.

Classify each candidate as a result record, program guidance, durable doctrine,
regression test, temporary fact, or one-off taste decision. Apply `knowledge-boundaries.md`
before changing the repository.

Update only the narrowest governed source. Preserve the dated run record even when no
learning is promoted.

## 4. Prove compounding

Structural checks prove only that the run record is internally consistent. A named human
must verify artifact fidelity before an operational or compounding claim.

A publishable compounding claim requires:

- Two comparable prospective workflows.
- Metrics declared before the second run.
- At least 20% less human correction or review time on the second run.
- No regression in first-pass acceptance or critical defects.
- Clear evidence of which prior decisions or rules the second run inherited.
- One independent teammate rerun before claiming team-level reuse.

Use `../../../strategy/compound-marketing/scripts/check_run.py` for record and comparison
checks, resolving the script from the loaded Marketing OS repository and passing absolute
project-local record paths. Keep incomplete baselines honest: missing evidence is a
result, not a field to backfill from memory.

## Stop conditions

Stop and surface the issue when:

- Sources disagree about a fact or decision that changes the work.
- No person or source owns the strategic choice.
- The requested artifact would require inventing proof, pricing, dates, approval, or
  customer evidence.
- A downstream request contradicts the approved decision record.
- A proposed learning fails the knowledge-boundary test.
- The comparison is not genuinely comparable enough to support an improvement claim.
