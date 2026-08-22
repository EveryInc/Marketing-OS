# Compound Marketing Handoff Contract

Use this contract only when a specialist is invoked from a Compound Marketing run. One
run chooses one routed output. Related outputs use linked successor runs.

The `handoff` command creates `handoff.json` beside `run.json`. That sidecar is the
machine-readable contract. A specialist may repeat the block below in its governed
source, but a customer-facing rendering may omit it when the sidecar remains attached.

## Required block

```text
COMPOUND MARKETING HANDOFF
Run ID: [run_id]
Run record: [absolute run.json path]
Decision record: [absolute decision-record.md path]
Decision-record version: [version]
Decision-record SHA-256: [digest]
Canonical governance digest: [digest]
Workflow family: [brand_strategy / company_strategy / program / gtm]
Routed output: [marketing_gtm / program_brief / gtm_plan / one_pager]
Inherited decision IDs: [D1, D2]
Protected-language IDs: [L1]
Unresolved-question IDs: [Q1]
Artifact owner: [person]
```

## Rules

- Read `handoff.json` before reading the underlying source pile.
- Preserve every inherited decision and exact protected phrase, or record a human-ruled
  replacement in the canonical run.
- Keep unresolved questions visible. A specialist cannot silently answer one.
- Write only the routed artifact and proposed record changes. The Compound Marketing
  orchestrator is the single writer for `run.json`.
- Before acceptance, compare the artifact with the sidecar, canonical governance digest,
  and current decision-record projection digest. A stale digest requires a new handoff.
- Do not treat the block as customer-facing copy or include it in a published rendering.
