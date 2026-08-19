# Compound Marketing Proof Standard

Use the smallest honest claim supported by the evidence.

## Three proof levels

### 1. Structural proof

Shows that the run record carries source authority, locked decisions, protected
language, open questions, and approval state without internal drift.

Evidence: a valid run record and zero cross-stage decision failures.

Allowed claim: "The run record is internally consistent."

The validator cannot inspect every Google Doc, slide deck, or published surface. A named
human must verify that the accepted artifacts match their recorded decision IDs before
an operational or compounding claim can pass.

### 2. Operational proof

Shows that a real project produced an accepted strategy, program, or GTM artifact with
measured human review burden and defects.

Evidence: a prospective run record, accepted artifact, human ruling, and complete run
metrics.

Allowed claim: "The workflow produced useful work under measured conditions."

### 3. Compounding proof

Shows that a comparable second real run inherited prior decisions and improved without
quality loss.

Require:

- Matching workflow type and a named baseline run.
- Measures declared before the follow-up run.
- At least 20% less human review or correction time.
- No regression in first-pass acceptance.
- No increase in critical defects.
- At least one inherited decision accepted without reconstruction.
- The accepted decision IDs exist in the baseline, the follow-up decision record, and
  the follow-up market artifact.
- One independent teammate rerun before claiming team-level reuse.
- A named human verified that the accepted artifacts match the recorded decisions and
  protected language.

Allowed claim: "The second run required less human correction because it inherited
decisions and learning from the first."

## Non-proof

Do not use these as evidence that marketing improved:

- Number of skills, prompts, agents, or generated artifacts.
- A synthetic rubric score without reproducible inputs and checks.
- Structural validation alone.
- Faster generation without accepted output.
- A retrospective estimate presented as a measured baseline.
- Two different workflow types compared as if they were repetitions.

## Comparison command

```bash
python3 <MARKETING_OS_ROOT>/strategy/compound-marketing/scripts/check_run.py compare <absolute-baseline.json> <absolute-followup.json>
```

The comparison must fail closed. Missing evidence, unmatched workflows, or a quality
regression prevents the compounding claim.

The `validate` command can mark a follow-up `comparison_ready`. It cannot mark a single
record `proof_ready`; only a successful `compare` result can do that.
