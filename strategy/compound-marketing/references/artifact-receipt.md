# Compound Marketing Artifact Receipt

Create one JSON receipt for every applicable stage before making a compounding claim.
Keep it in the run directory and link it from the stage's `artifact_receipt` field in
`run.json`.

The receipt connects the accepted artifact to the decision record it inherited. It also
records the named human who checked the artifact. The checker reads this file; a claim
fails when the file is missing, unreadable, or inconsistent with the run record.

```json
{
  "schema_version": 1,
  "run_id": "spiral-launch-2026-08",
  "stage": "strategy_to_market",
  "artifact": "https://docs.google.com/document/d/example/edit",
  "decision_record": {
    "path": "decision-record.md",
    "version": "v3"
  },
  "decision_ids": ["D1", "D2"],
  "verified_by": "Douglas Brundage",
  "verified_at": "2026-08-21T12:00:00-04:00"
}
```

Use the stage's `output_decision_ids` for `context_to_strategy` and
`preserved_decision_ids` for `strategy_to_market`. Use an empty list for
`market_to_memory` when no decisions govern the result record.

The receipt does not prove that a Google Doc, slide deck, or published page contains the
right language on its own. The named verifier must inspect the accepted artifact before
signing it. The receipt makes that ruling explicit, shared, and checkable.
