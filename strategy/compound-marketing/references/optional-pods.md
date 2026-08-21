# Optional Compound Marketing Pods

Use parallel agents only when independent work can reduce cycle time without increasing
human reconciliation.

## When a pod helps

Require all of these:

- Three or more separable jobs.
- One approved decision record.
- Different owned artifacts or evidence surfaces.
- No unresolved decision shared by parallel workers.
- Independent review costs less than serial production.

Otherwise work serially.

When the gate clears, load `../../marketing-pod/SKILL.md` for the authoritative role
charters, handoff contracts, authorization rules, and run scorecard. This reference
decides whether a pod is useful; `strategy/marketing-pod` governs the pod itself.

## Useful jobs

- **Truth:** Verify sources, facts, freshness, and conflicts.
- **Customer evidence:** Extract language, desired progress, barriers, and proof.
- **Category evidence:** Map competitor claims, conventions, and collisions.
- **Strategy:** Synthesize approved evidence into one governing decision record.
- **Operations:** Build owners, dependencies, dates, and approval gates.
- **QA:** Check claims, decision fidelity, permissions, and open questions.
- **Measurement:** Establish the baseline and close the result against the original bet.

Use only the jobs the project needs. Keep strategy serial after evidence gathering, and
keep QA independent from the artifact it reviews.

## Worker contract

Give each worker:

- The run ID and decision-record version.
- The absolute run-record and decision-record paths.
- One job and one owned output.
- Exact allowed sources.
- The decisions and language it must preserve.
- Explicit exclusions and stop conditions.
- The verification required for handoff.

Require the return to separate evidence, inference, conflicts, and verification. A
finished worker output enters review; it does not become approved automatically.

## Success

Judge a pod by accepted work, review burden, defects, and inherited decisions. Never use
agent count, parallelism, or an autonomy label as the claim.
