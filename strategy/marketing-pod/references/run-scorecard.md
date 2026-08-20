# Marketing Pod Run Scorecard

Use this scorecard before the first dispatch and after each completed run. Level 7 is an
operating behavior, not an agent-count claim.

## Contents

1. Preflight baseline
2. Run measures
3. Level 7 proof standard
4. Decision rule

## Preflight baseline

Record the closest prior workflow or first-run estimate:

- Human production time
- Human review and integration time
- Number of revision rounds
- First-pass acceptance rate
- Claim, source, version, and duplicate defects
- Number of people who can run the workflow
- Existing artifact or skill reused

If no comparable baseline exists, call cycle 1 BASELINE. Judge it on the absolute
reliability, adoption, and guardrail thresholds below, then use it as the comparison for
cycle 2. Do not invent an improvement claim for cycle 1.

## Run measures

### Primary decision metric

Use **human review and integration burden**: minutes Douglas spends reconciling,
correcting, and approving pod outputs.

The pod succeeds only if it creates more room for judgment and stronger ideas. Agent
throughput alone is not success.

### Reliability

- Handoff completeness: percent of required return fields present
- First-pass acceptance: percent of artifacts needing no substantial strategic rewrite
- Source defects: unsupported, stale, or misattributed facts
- Cross-surface conflicts: inconsistent name, claim, price, date, offer, or primary action
- Duplicate or superseded outputs reaching review
- Blockers surfaced before downstream work began

### Review efficiency

- Total human review and integration minutes
- Review minutes per accepted artifact
- Revision rounds per artifact
- Percent of baseline human production time retained for review and integration

### Adoption and compounding

- Roles successfully run by someone other than Douglas
- Existing Marketing OS skills reused without local reinvention
- Second-run correction and review-time change
- New project evidence recorded
- Program guidance or durable doctrine proposed and correctly classified

### Guardrails

- External actions taken without authorization
- Private or permissioned evidence exposed
- Human-owned decision made by an agent
- Creative premise diluted during compression or channel adaptation
- Marketing judged only by Growth's last-click metrics

Any guardrail breach fails the run regardless of speed.

## Level 7 proof standard

Call the workflow Level 7 only after two relevant project cycles satisfy all of these:

- Douglas managed at least three role-bounded agents working concurrently in each cycle.
- The pod used at least two safe waves or one parallel wave plus independent QA.
- No worker delegated or managed other workers.
- At least 90% of required handoff fields were complete.
- At least 80% of artifacts passed first review without substantial strategic rewriting.
- No unsupported external claim, stale source conflict, or superseded artifact reached
  the ship gate.
- When a comparable prior workflow exists, human review and integration consumed no
  more than 25% of its human production time in each cycle.
- When no comparable prior workflow exists, cycle 1 established the baseline and cycle
  2 reduced correction count or review time by at least 20% while preserving the other
  thresholds.
- When a comparable prior workflow exists, the second cycle still reduced correction
  count or review time by at least 20% relative to cycle 1.
- At least one teammate could reuse the packet, role charter, or workflow without
  Douglas rebuilding it from scratch.

If the project is too small for three concurrent roles, do not claim Level 7 from it.

## Decision rule

End each run with one decision:

- **Scale:** Thresholds passed; reuse the same pod on a comparable project.
- **Revise:** Strategic value is sound, but one role, handoff, gate, or source contract
  caused avoidable review work.
- **Serialize:** Parallelism created more collisions than value; keep the underlying
  specialist skills and run the workflow sequentially.
- **Stop:** Guardrails failed, outputs were not adopted, or integration exceeded the
  baseline without producing a meaningful quality gain.

Update the narrowest charter or contract after a revise decision. Do not rewrite the
whole pod from one failure.
