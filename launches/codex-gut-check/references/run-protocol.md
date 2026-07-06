# Codex Gut-Check — Run Protocol

The exact protocol for executing the Week 5 gut-check. The SKILL.md defines when and
what; this file defines how. Run all five passes; each produces findings in the output
template at the bottom. The pass names matter — they set the adversarial stance that
makes the check worth running.

## Assembling the context (before any pass)

Feed, in this order: (1) the launch's positioning/strategy doc, (2) Every master brand
positioning + archetypes, (3) the competitive audit with its citations, (4) the current
web copy draft with its round number. If any is missing, stop and report the gap —
a gut-check on partial context produces confident nonsense.

## The five passes

### 1 · Cold read
Read the copy as a first-time visitor with no context. After the hero only: what is
this product, who is it for, what should I do next? Write the answers before reading
further. Wherever the cold-read answer diverges from the strategy doc's intent, that
divergence is a finding — the visitor doesn't get a second screen.

### 2 · The competitor's CMO
Read as the sharpest marketer at each named competitor. For every claim in the copy,
ask: could I say this too? Claims any competitor could copy-paste are category noise,
not positioning. Findings name the competitor and cite what they actually run (from the
audit — re-verify anything older than ~4 weeks before leaning on it).

### 3 · The archetype read
Read once per target archetype from the Week 1 customer profile. Section by section:
does this speak to that reader's actual motivation, or has it drifted to a different
reader (commonly: written for the builder, drifted to the executive)? Findings quote
the drifting section and name which archetype it lost.

### 4 · Voice and banned-term sweep
Run the brand's voice rules mechanically: banned terms, tone descriptors, the "get
specific" rule against every abstract claim. This pass also catches copy-doc artifacts —
duplicate blocks, truncated bodies, numbering drift — which are findings for the copy
owner, not silent fixes.

### 5 · Claims inventory
Extract every stat, quote, logo, price, and availability claim with its location. Tag
each sourced/unsourced/conflicted. This inventory is the handoff to claims-clearance —
it opens their sweep, it doesn't replace it.

## CTA and prompt-copy brainstorm (after the passes)

With the passes done, generate CTA and prompt-copy candidates against what named
competitors actually run (cited from the audit). Candidates in threes per surface;
each with one line on why it beats the competitor's version. Candidates are inputs to
the human copy round, never direct replacements.

## Output template

```
CODEX GUT-CHECK — [product] · copy R[n] · [date]
Verdict: CONFIRM / CHALLENGE — [one line]
Pass 1 · Cold read: [findings with locations]
Pass 2 · Competitor's CMO: [claim → competitor → citation]
Pass 3 · Archetype read: [section → archetype lost]
Pass 4 · Voice sweep: [violations + copy artifacts]
Pass 5 · Claims inventory: [table → to claims-clearance]
CTA/prompt candidates: [threes, with reasons]
Not checked: [anything skipped, named plainly]
```

The verdict is advisory. Douglas rules. A CHALLENGE that gets overruled still did its
job — it forced the strategy to defend itself before the website inherited it.
