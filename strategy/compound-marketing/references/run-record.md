# Compound Marketing Run Record

Use one Markdown record for human review and one JSON companion for deterministic
validation. Keep both in `<project-root>/.compound-marketing/<run-id>/` beside the
decision record. Search this directory for an unfinished matching run before creating a
new one.

## Open

- Run ID:
- Project:
- Workflow: brand-strategy / company-strategy / program / GTM
- Evidence status: prospective / retrospective / incomplete
- Objective:
- Intended audience behavior:
- Requested artifact:
- Decision-record path and version:
- Primary decision metric:
- Measurement window and decision date:
- Explicit exclusions:

## Baseline

- Comparable run ID, if any:
- Why the workflows are comparable:
- Human review and integration minutes:
- First-pass accepted: yes / no
- Critical defects reaching review:
- Revision rounds:
- Missing evidence:

Label a first or incomplete run `BASELINE`. Never reconstruct missing time or quality
measures from memory.

## Stage record

| Stage | Status | Artifact | Input decision IDs | Preserved or output IDs | Human ruling |
|---|---|---|---|---|---|
| Context to strategy | | | | | |
| Strategy to market | | | | | |
| Market to memory | | | | | |

Use `not applicable` only when the project genuinely stops before that stage. A partial
run can be useful evidence, but cannot support an end-to-end claim.

## Review evidence

- Human review and integration minutes:
- First-pass accepted:
- Critical defects:
- Substantial corrections:
- Decisions inherited from previous work:
- Inherited decisions accepted without reconstruction:
- Accepted inherited decision IDs:
- Independent operator:
- Artifact fidelity verified by:
- Artifact fidelity verified at:

## Closeout

- Result:
- Decision: scale / revise / stop / continue measuring
- Human edits classified:
- Market results classified:
- Durable updates proposed:
- Regression cases added:
- Project-only learning retained:
- Next comparable run:

## JSON companion

Use the field structure in `../evals/fixtures/brand-book-baseline.json`. Locked decisions
that govern downstream work must appear in both the strategy output and the market
artifact's `preserved_decision_ids`. A follow-up proof also lists the exact baseline
decision IDs it inherited in `proof.accepted_inherited_decision_ids`; the validator
cross-checks those IDs against both runs.

Resolve `<MARKETING_OS_ROOT>` from the loaded Compound Marketing skill. Validate with
absolute paths so the command works from the project directory:

```bash
python3 <MARKETING_OS_ROOT>/strategy/compound-marketing/scripts/check_run.py validate <absolute-record.json>
```
