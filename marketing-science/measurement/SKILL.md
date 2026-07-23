# Measurement

Build a measurement contract that turns a marketing objective into an observable result
and a decision. Use this skill before a campaign, launch, experiment, or sustained
marketing program begins. The contract tells the team what it is trying to learn, how
the evidence will be interpreted, and what happens next. Dashboard specifications come
later.

Measurement supports judgment. It does not replace it. What is easy to count is not
automatically what matters. Hard-to-attribute effects still need evidence.

## When to invoke

- When a strategy, campaign, launch, experiment, or ongoing program needs success criteria
- When a brief contains goals such as awareness, demand, cultural impact, or engagement
  without defined evidence
- When a dashboard has many metrics but no primary decision metric
- When Marketing and Growth need a shared scorecard without collapsing their mandates
- When a result must be interpreted, compared with a baseline, or turned into a decision
- Before launch, when instrumentation, ownership, and measurement windows can still be fixed

## Start with the decision

Write the decision this evidence must inform before choosing a metric. Examples:

- Continue, change, or stop the campaign
- Increase or reduce investment
- Keep or revise the message, offer, audience, channel, or first-value path
- Promote an experiment into a repeatable program
- Decide whether the launch created demand, converted it, or merely generated activity

If the result would not change a decision, the metric is context rather than a key
performance indicator. Keep it only when it helps explain the primary result.

## The measurement contract

Every contract contains these fields. Mark an unknown `OPEN`; do not fill it with an
invented benchmark.

| Field | Required decision |
|---|---|
| Objective | The business, customer, brand, or learning outcome this work should create |
| Hypothesis | The causal claim: if we do X for Y, we expect Z because of Q |
| Unit of analysis | Person, account, subscriber, customer, session, cohort, market, or other defined unit |
| Baseline | Current value, source, and comparison period; write `NO BASELINE` when none exists |
| Primary decision metric | The single measure that best determines whether the objective was met |
| Formula | Numerator, denominator, exclusions, and segmentation rules |
| Target or threshold | The value and date that separate success, mixed evidence, and failure |
| Diagnostic metrics | A small set that explains why the primary metric moved or did not |
| Guardrails | Measures that catch damage, poor-fit growth, degraded quality, or unintended effects |
| Qualitative and cultural signals | Named evidence that captures meaning the quantitative measures miss |
| Data source and instrumentation | System of record, events or fields required, access, and known gaps |
| Owner | The person accountable for collection, analysis, and reporting |
| Window and cadence | Start, stop, maturation period, reporting rhythm, and comparison period |
| Attribution limits | What the method can and cannot claim caused the result |
| Decision rule | The action for success, mixed evidence, failure, and an inconclusive result |

Write decision rules before results arrive. A useful rule is explicit:

> If the primary metric reaches [target] by [date] without breaching [guardrail], take
> [action]. If it lands in [mixed range], inspect [diagnostics] and take [bounded action].
> If it falls below [failure threshold], take [action]. If data quality is insufficient,
> fix [instrumentation] before drawing a conclusion.

## Metric hierarchy

Use four layers. Do not give every available number equal status.

1. **Primary decision metric:** one measure tied directly to the objective
2. **Diagnostics:** usually two to five measures that explain the primary result
3. **Guardrails:** usually one to three measures that prevent a local win from becoming
   an overall loss
4. **Context:** trends and observations worth monitoring but not used to declare success

Use a rate when opportunity or exposure varies. Pair volume with quality or composition.
Report absolute numbers beside percentages when a small denominator could mislead.

For launches, retain the GTM plan's four outcome classes:

- **Business:** qualified demand, paid conversion, revenue, capacity, retention, referrals
- **Conversion:** decision time, first value, completion, activation, repeat behavior,
  attendance, or participation
- **Proof:** publishable receipts, advocates, outcomes, and case-study candidates
- **Brand:** awareness, branded search, direct and organic traffic, earned coverage,
  distinctive associations, and reuse of campaign language

These classes organize the scorecard. They do not eliminate the need to choose one
primary decision metric for each objective.

## Marketing and Growth

Marketing creates demand and cultural gravity. Growth converts demand through the offer,
funnel, onboarding, lifecycle, and retention. Measurement should show both jobs without
pretending they are the same.

- Marketing owns the hypothesis and evidence for awareness, memory, associations,
  cultural position, earned attention, audience quality, and demand creation.
- Growth owns instrumentation and evidence for conversion, activation, revenue,
  retention, and funnel efficiency.
- Shared work requires a shared contract with named owners. Attribution software does not
  settle the mandate split.
- Last-click and platform-reported attribution are diagnostic views, not complete accounts
  of marketing effectiveness.

When brand effects will mature outside the campaign window, name the expected time
horizon and use leading signals without presenting them as final proof.

## Data quality and interpretation

Before interpreting a result, check:

- Numerator, denominator, exclusions, and duplicate handling
- Sample size and whether the sample represents the intended audience
- Missing data, instrumentation changes, and inconsistent event definitions
- Cohort, channel, customer quality, and audience-composition differences
- Seasonality, launch novelty, promotions, pricing changes, and other confounders
- Correlation versus plausible causation
- Selection, survivorship, response, and confirmation bias
- Whether the comparison period or benchmark is genuinely comparable
- Whether a statistically visible change is large enough to matter operationally

Do not manufacture precision. Small samples, noisy brand signals, and directional
qualitative evidence should be labeled honestly. Triangulate when no single measure can
carry the claim.

## Baselines and instrumentation

Capture the baseline before work begins whenever possible. Use the same definition,
segment, and time basis for the comparison.

If no baseline exists:

1. Write `NO BASELINE`.
2. Choose the earliest defensible observation window.
3. Separate the act of establishing a baseline from the claim of improvement.
4. Add the missing event, field, survey, or manual collection step before launch.
5. State which conclusions remain impossible until enough data accrues.

The minimum viable instrumentation is the smallest reliable setup that can execute the
decision rule. Do not delay useful work to build an ornamental dashboard.

## Required output

Return:

1. The completed measurement-contract table
2. A scorecard showing the primary metric, diagnostics, guardrails, owner, source,
   baseline, target, window, and current status
3. The pre-launch instrumentation checklist
4. The result interpretation, when data exists
5. The resulting decision and next measurement date

Lead with the decision, not the metric dump. Explain quantitative findings in plain
language and show calculations when the result depends on them.

## Dependencies

- `foundation/marketing-os`
- `marketing-science/research`

## Quick checklist

- [ ] The decision this evidence must inform is explicit
- [ ] Objective and causal hypothesis are written separately
- [ ] The unit of analysis and metric formulas are defined
- [ ] A real baseline is cited, or `NO BASELINE` is visible
- [ ] Each objective has one primary decision metric
- [ ] Diagnostics, guardrails, and context are visibly distinct
- [ ] Targets, thresholds, windows, and decision rules were set before results arrived
- [ ] Data source, instrumentation gaps, and owner are named
- [ ] Quality or audience composition is tracked beside volume
- [ ] Attribution limits and confounders are stated
- [ ] Marketing and Growth outcomes remain distinct but connected
- [ ] Qualitative and cultural signals cover important effects the numbers miss
- [ ] The result ends in a decision, not a dashboard recap
