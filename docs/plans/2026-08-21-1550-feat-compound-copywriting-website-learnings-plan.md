---
artifact_contract: ce-unified-plan/v1
artifact_readiness: implementation-ready
execution: code
product_contract_source: ce-plan-bootstrap
---

# Compound Copywriting website-learning system

## Goal Capsule

Ship the durable craft and workflow learnings from the August Every Agent website pass so
future product-site work preserves ruled human copy, separates section jobs, uses audited
proof, respects repeated-unit schemas, and measures the downstream behavior the page exists
to cause. The change must preserve every related edit already present in the dirty checkout,
remain within Copywriting and Compound Copywriting, and avoid reopening the website copy or
starting the wireframe.

## Product Contract

### User and job

The primary user is a marketer directing an AI copywriting workflow. They need the system to
inherit accepted language and page structure, distinguish brand promises from operational
facts, and convert corrections into narrow rules that improve the next comparable draft.

### Desired behavior

- The current human-edited website document is canonical for copy, structure, formatting,
  and protected language. Governing GTM, positioning, product, security, pricing, and
  integration sources continue to own factual truth.
- General craft rulings live in `craft/copywriting`; product-website workflow rules live in
  a routed Compound Copywriting reference; project wording and isolated taste stay local.
- Product-site work begins with source recovery, a section-job map, proof inventory, repeated
  unit schema, and declared conversion behavior.
- Public examples expose a coherent request, action, and completed result and use only
  approved receipts. Competitor sites inform conversion architecture, not surface imitation.
- A structural evaluation corpus can demonstrate rule coverage, but compounding remains
  unproved until a comparable future run needs less correction without losing quality.

### Non-goals

- Revising the Every Agent website or its Google Doc.
- Building or wireframing the site.
- Teaching project-specific Every Agent copy as universal doctrine.
- Building a new behavioral-eval runner in this change.
- Changing Compound Marketing paths owned by the concurrent task.

## Planning Contract

### Settled decisions

1. **Current edited document is canonical for the artifact.** User-directed. It owns copy,
   structure, formatting, and protected language; it does not override verified product facts.
2. **Learn operations, not project wording.** User-approved. Store reusable craft and workflow
   decisions while keeping Every Agent lines and isolated preferences out of durable doctrine.
3. **Capture every meaningful correction from the website pass.** User-directed. Ship the
   complete related Copywriting and Compound Copywriting diff rather than a hero-only subset.
4. **Coordinate with the concurrent Marketing OS task.** User-directed. Keep path ownership
   separate and preserve its branch/worktree.
5. **Ship through review, PR, and CI.** User-directed through the LFG invocation.

### Assumptions

- The 11 modified copywriting files and new product-website reference are one coherent change.
- `main` contains the previously merged Marketing OS baseline and is the correct PR base.
- A new isolated worktree and branch will prevent the dirty user-owned checkout from being
  disturbed.
- Existing repository tests cover the Marketing OS learning loop, while direct JSON checks
  provide structural validation for the 18 Compound Copywriting cases.

### Institutional patterns applied

`docs/solutions/workflow-issues/preserve-specificity-in-gtm-synthesis.md` requires the owner's
latest edits to remain canonical, preserves distinctive fragments and rhythm, and keeps the
request/action/result chain visible. `docs/solutions/design-patterns/controlled-generative-visual-iteration.md`
supports locking approved content and translating references into structural invariants rather
than copying their surface. `CONCEPTS.md` reserves “compounding proof” for a comparable future
run with lower correction burden at equal quality.

### Correction inventory

This inventory is the completeness boundary for “every meaningful correction.” Project copy
stays local; reusable operating decisions map to one narrow rule and at least one control.

| Source correction or ruling | Durable destination | Regression or control |
| --- | --- | --- |
| Do not overwrite accepted edits or untouched sections | Ruled-copy and source-recovery rules | `recover-source-lines-before-generating`; protected-language checklist |
| Lead the hero with one idea, not the whole message map | General dominant-idea rule plus website hero rule | `spoken-language-one-dominant-idea` |
| Remove agent abstractions such as “hand it” and “ask for a result” | Website interface-language rule | `interface-language-not-agent-abstraction` |
| Marketing may make strong claims; operational facts still need proof | General claim-classification rule | `brand-promise-is-not-compliance-copy`; blocked-claim audit |
| Internal workflow receipts can sit below the hero; logos do not prove the work | Website proof-placement rule | `one-conversion-job-per-web-section`; proof audit |
| Repetitive sections must have distinct jobs or be cut | Website section-job map | `one-conversion-job-per-web-section` |
| “How it works” should name literal actions in the shortest useful sequence | Website mechanism rule | interface-language case; section-job checklist |
| Company adoption needs an internal-champion and social-distribution mechanism | Website owned-mechanism rule | project-source recovery and duplication audit |
| Later outcome grids need fresh audited workflows and explicit beta slots | Website proof inventory | `proof-inventory-prevents-repetition`; rubric hard failure |
| A “Turn X into Y” card must request an action and prove the completed result | General artifact-match rule plus website card rule | `product-promise-matches-artifact`; `transformation-card-requires-an-action` |
| Repeated cards must inherit the edited exemplar, requested count, and highlights | Website schema-fidelity rule | `edited-card-defines-sibling-schema`; rubric hard failure |
| Viktor and similar sites supply conversion architecture, not copy or page length | Website reference-site rule | `reference-site-architecture-not-imitation` |
| Footer, CTA, connector counts, and destinations are copy requirements | Website conversion-path rule | native-format and count checklist |
| Homepage tests should select on activation, not clicks alone | Market-outcome scorecard rule | `activation-test-not-click-test` |
| Ogilvy and Singleton supply adaptable craft controls, not universal quotas | General principles and line rules | `consequential-copy-finishing-controls`; spoken-language case |
| Individual workflow subjects, Every Agent lines, and isolated taste calls stay local | Knowledge-boundary rule | `single-edit-does-not-become-doctrine` |

## Implementation Units

### Unit 1: General copy craft rules

**Outcome:** Promote only the transferable craft rulings from the website pass into the base
copywriting skill.

**Files:**

- `craft/copywriting/SKILL.md`
- `craft/copywriting/references/copywriting-line-rules.md`
- `craft/copywriting/references/failure-ledger.md`
- `craft/copywriting/references/formats.md`
- `craft/copywriting/references/messaging-doc-discipline.md`
- `craft/copywriting/references/principles.md`

**Requirements:**

- Preserve the distinction between strong, ownable brand promises and verifiable operational
  claims.
- Require spoken language, a single dominant idea, honest artifact/outcome alignment, and
  earned rhetorical devices without imposing arbitrary brevity.
- Keep request/action/result as medium-agnostic proof guidance. Product-site section-job
  mechanics remain exclusively in Unit 2's routed website reference.
- Keep cross-references internally consistent, including the full C1-C10 rule range.

**Dependency:** None.

### Unit 2: Product-website compounding workflow

**Outcome:** Route iterative product-site work through a specific, reusable operating reference.

**Files:**

- `craft/compound-copywriting/SKILL.md`
- `craft/compound-copywriting/references/loop.md`
- `craft/compound-copywriting/references/product-websites.md`

**Requirements:**

- Load the product-website reference only for homepages, workflow libraries, integrations, or
  pricing pages.
- Narrow source precedence so the edited document governs copy and structure while verified
  GTM/product sources govern facts.
- Require source recovery, section jobs, proof allocation, interface-native language, schema
  fidelity, owned-mechanism placement, CTA completion, and downstream conversion measurement.
- Keep competitor modeling at the level of conversion logic.

**Dependency:** Unit 1 defines the general craft rules this workflow applies.

### Unit 3: Regression coverage and measurement contract

**Outcome:** Make the highest-risk failures explicit and mechanically inspectable without
overclaiming behavior or market improvement.

**Files:**

- `craft/compound-copywriting/evals/cases.json`
- `craft/compound-copywriting/evals/rubric.md`
- `craft/compound-copywriting/references/scorecard.md`

**Requirements:**

- Keep the version 2 manifest at 18 unique cases with nonempty task, expected behavior, and
  failure fields.
- Cover source recovery, promise-versus-fact classification, natural interface language,
  fresh proof allocation, honest transformation cards, repeated-unit schema, competitor
  architecture, and activation-oriented testing.
- Treat activated workspaces or the relevant downstream behavior as the decision metric and
  clicks as diagnostics when that is the conversion goal.
- State that cases prove coverage only; a future comparable run is required for compounding
  proof.

**Dependency:** Units 1 and 2 supply the behavior under test.

## Agent-Native Contract

- **Now:** Update agent instructions, routed context, generic craft rules, evaluation cases,
  rubric, and scorecard.
- **Later:** Add a reusable runner that executes skill-level behavioral cases rather than
  checking only manifest structure.
- **Human-only:** Final taste and public-copy approval, workspace/OAuth permissions, and
  durable rule promotion without the learning gate.
- **Risk control:** The skill must never infer that the human-edited website overrides verified
  product facts or that structural cases prove market improvement.

## Verification Contract

### Structural checks

- `python3 -m json.tool craft/compound-copywriting/evals/cases.json`
- A deterministic manifest check confirms version 2, 18 cases, unique IDs, nonempty required
  fields, and existing routed-reference paths.
- `git diff --check`

### Repository regression check

- `python3 -m unittest foundation.marketing-os.tests.test_check_learning_loop`
- Expected result: all 13 learning-loop tests pass.

### Rule-to-case review

- Trace all 18 cases to the final skill, reference, rubric, or scorecard instruction that would
  govern them. This is a coverage inspection, not an executed behavioral evaluation.
- Confirm that every new durable instruction has a narrow scope and a corresponding regression
  case or explicit checklist/rubric control.
- Confirm no website copy, project memory, Compound Marketing files, or unrelated user changes
  enter the branch.

### Shipping evidence

- Review the isolated branch diff against `main`.
- Open a PR against `main`, monitor required checks, and report the final PR and CI state.

## Definition of Done

- All 12 related files ship together with the two authority/cross-reference corrections above.
- `product-websites.md` is routed only from Compound Copywriting and contains no project copy.
- The 18-case manifest is valid and unique; repository tests and whitespace checks pass.
- The correction inventory has no unmapped reusable ruling; project-local entries are explicitly
  excluded from doctrine.
- The diff contains no overlapping Compound Marketing changes or unrelated user-owned work.
- Review finds no unresolved high- or medium-severity issue.
- A PR against `main` is open and required CI checks pass, or a genuine external blocker is
  documented with exact evidence.
