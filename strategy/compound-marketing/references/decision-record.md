# Compound Marketing Decision Record

Keep one canonical decision ledger inside schema V2 `run.json`. Generate this Markdown
projection with the `render` command for human review. Do not edit the projection as a
second source of truth. Store the run beside the project, not inside Marketing OS.

## Identity

- Project:
- Run ID:
- Decision-record version:
- Current stage:
- Strategy owner:
- Approval owner:
- Last ruled date:

## Authority map

| Authority | Owner | Canonical source | Freshness | Status |
|---|---|---|---|---|
| Product or company facts | | | | confirmed / open |
| Strategic decisions | | | | confirmed / open |
| Customer evidence | | | | confirmed / open |
| Canonical language | | | | confirmed / open |
| Dates, price, and offer | | | | confirmed / open |
| Approval | | | | confirmed / open |

Authority belongs to a named person or ruled source. The newest document does not win by
default.

## Governing strategy

- Diagnosis:
- Primary audience:
- Desired audience behavior:
- Guiding choice:
- Offer or value:
- Proof requirement:
- Primary action:
- Strategic refusal:

## Decision ledger

| ID | Decision | Owner | Source | Status | Applies to | Supersedes |
|---|---|---|---|---|---|---|
| D1 | | | | locked / open / rejected | | |

Use a new row when a decision changes. Do not overwrite the previous ruling.

## Protected language

| ID | Exact language | Job it performs | Owner | Change rule |
|---|---|---|---|---|
| L1 | | | | preserve / propose alternative |

## Evidence state

### Confirmed facts

- Fact, source, date.

### Observations

- Observed behavior or language, source, date.

### Inferences

- Interpretation, evidence used, confidence.

### Open questions

| Question | Owner | Decision affected | Due or gate |
|---|---|---|---|
| | | | |

### Rejected or deferred directions

- Direction, owner, reason, revisit condition.

## Handoff

- Artifact requested:
- Decision-record version inherited:
- Decision IDs that must appear or govern:
- Protected language IDs:
- Open questions that must remain open:
- Output owner:
- Approval gate:

The machine-readable handoff lives in `handoff.json` and follows
`handoff-contract.md`. Every accepted artifact is bound to the current projection digest.
