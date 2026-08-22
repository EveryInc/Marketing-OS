# Compound Marketing Run Record

`run.json` is the canonical record. `run.md` and `decision-record.md` are generated
projections for human review. Never edit a projection as governing state.

Keep all files in `<project-root>/.compound-marketing/<run-id>/`. Resolve
`scripts/check_run.py` from the loaded Compound Marketing skill and use its absolute path.

## Start or resume

```bash
python3 <ABSOLUTE_CHECKER> discover <PROJECT_ROOT> --project "Project name" --workflow gtm
python3 <ABSOLUTE_CHECKER> init <PROJECT_ROOT> --project "Project name" --workflow gtm --route gtm_plan --operator douglas
```

`init` returns the single unfinished match instead of creating a duplicate. Multiple
matches fail with their paths. Use `--force-new` only for an intentionally concurrent
run. It creates a new run and never overwrites the existing one.

After a terminal run, create a linked successor instead of reopening history:

```bash
python3 <ABSOLUTE_CHECKER> init <PROJECT_ROOT> --project "Project name" --workflow gtm --route gtm_plan --operator austin --predecessor <ABSOLUTE_PRIOR_RUN_JSON>
```

The predecessor must be terminal and match the project and workflow. The successor
records its run ID, path, and canonical governance digest.

New runs use schema V2. Workflow families are `brand_strategy`, `company_strategy`,
`program`, and `gtm`. Routes are `marketing_gtm`, `program_brief`, `gtm_plan`, and
`one_pager`. One run governs one routed artifact.

## Lifecycle

`open -> strategy_pending -> strategy_approved -> artifact_pending -> artifact_approved -> measuring -> closed`

- `blocked` records the prior state and a reason. `transition ... resume` restores it.
- A blocked run may be abandoned without erasing the blocker that stopped it.
- `abandoned` and `closed` are immutable. `render`, `handoff`, `receipt`, and further
  transitions fail; later work creates a linked successor.
- Strategy approval must be human-signed before `strategy_approved`.
- Artifact acceptance and fidelity attestation must be human-signed before
  `artifact_approved`, and both must name the exact verified artifact binding.
- Nonnegative measurements and valid prospective timestamps must be present before
  `closed`.

```bash
python3 <ABSOLUTE_CHECKER> transition <ABSOLUTE_RUN_JSON> strategy_pending
python3 <ABSOLUTE_CHECKER> transition <ABSOLUTE_RUN_JSON> blocked --reason "Dan must rule the offer"
python3 <ABSOLUTE_CHECKER> transition <ABSOLUTE_RUN_JSON> resume
```

## Handoff and receipt

```bash
python3 <ABSOLUTE_CHECKER> render <ABSOLUTE_RUN_JSON>
python3 <ABSOLUTE_CHECKER> handoff <ABSOLUTE_RUN_JSON> --owner douglas
python3 <ABSOLUTE_CHECKER> receipt <ABSOLUTE_RUN_JSON> --stage strategy_to_market --artifact artifact.md
```

These commands scaffold machine-readable files. Approval and verification fields remain
unsigned. A producing agent cannot fill the human gate. Schema V2 receipts bind only the
`strategy_to_market` artifact; the other stages are governed by the canonical decision
record and the measured successor run.

## Readiness

```bash
python3 <ABSOLUTE_CHECKER> validate <ABSOLUTE_RUN_JSON>
```

- `structural_ready`: authority, decisions, blockers, projections, lifecycle metadata,
  and the canonical governance digest agree.
- `operational_ready`: the terminal run also has content-bound receipts, human rulings,
  prospective operational evidence, and complete measures.
- `comparison_ready`: an operational run additionally names a baseline, accepted
  inherited decisions, predeclared measures, and human-approved comparability.
- `proof_ready` remains false for one record. Only `compare` can return proof eligibility.

Schema V1 fixtures remain legacy structural evidence. Public `compare` accepts only two
schema V2 records. V1 records cannot become operational or compounding proof and must not
be backfilled with invented history.
