---
name: marketing-os
description: Coordinate brand and marketing work through Compound Strategy, Compound GTM, Compound Copywriting, or Compound Art Direction, using shared theory, source standards, brand context, and evidence-based learning.
---

# Marketing OS

## Choose the workflow

For a direct Marketing OS request, choose the smallest workflow that produces the requested
outcome. When a specialist loads this file as a dependency, supply the foundation only;
do not route back to the specialist or restart the task.

| User needs | Public entry |
|---|---|
| Decide what to do, for whom, and why | `workflows/compound-strategy/SKILL.md` |
| Bring an approved strategy to market | `workflows/compound-gtm/SKILL.md` |
| Write or revise the words | `workflows/compound-copywriting/SKILL.md` |
| Direct or produce the visual system and assets | `workflows/compound-art-direction/SKILL.md` |

These paths resolve from the repository root. A mixed assignment uses one brief and only
the relevant workflows. Read `references/compound-workflows.md` for boundaries, handoffs,
and the shared learning protocol. A narrow edit skips upstream stages already settled.
Research, measurement, voice, positioning, reviewers, and production tools remain
specialists underneath the four workflows; direct specialist requests still work.

For substantial cross-discipline projects, use `strategy/compound-marketing` as the
existing run coordinator and `references/golden-path.md` as the record protocol. The old
name remains compatible; it is not a fifth public workflow. Do not start a second run
when the task already has a governing record.

## Shared foundation

For substantive work, a changed brief, or a reset, use `references/task-context.md`.
Assemble context from current sources and load only the selected workflow's applicable
references. A narrow edit inherits approved strategy; it does not require the entire
method, canon, or specialist library. New strategic or creative choices still need their
grounding. Keep mandatory approval and verification checks intact.

Every's in-house marketing operating system, authored by Douglas Brundage as Head of
Marketing. This is the theoretical and methodological foundation that every downstream
skill in the repo — brand-voice, positioning, craft, strategy, launches — pulls from
at invocation time.

The goal: an AI collaborator that is first a master marketer grounded in the discipline's
best thinking, then Every-specific as brand docs and frameworks come online. Marketing OS
ensures that no skill operates in a vacuum. Every piece of generated, edited, or evaluated
work inherits a shared point of view, a shared canon, and a shared set of operational
frameworks.

## System

The foundational references below remain authoritative. The workflow map above organizes
access to them without replacing their theory or operating standards.

### references/canon.md
The reference encyclopedia. Thinkers, practitioners, and researchers organized by domain
(effectiveness, creative, brand theory, behavioral, strategy, deep history). Load this
when a task needs historical grounding, a specific thinker's lens, or evidence-based
reasoning from the marketing canon.

### references/method.md
The opinionated layer. Every's argumentative positions on effectiveness, creative, brand
theory, behavioral science, taste, AI-native marketing, and what makes Every different.
Load this when a task needs the point of view — when the work reflects what we believe
rather than only what the field knows.

### references/frameworks.md
The operational reference. Battle-tested frameworks (Binet/Field, Sharp, Keller, Aaker,
Romaniuk, Rumelt, Thaler/Sunstein, Christensen, Trout/Ries) with deployment guidance.
Load this when a task needs to operationalize a framework — when we need to apply a
model in context.

### references/collaboration.md
How AI collaborators work with Douglas: interview before ambiguous long-form work,
preserve creative specificity, use active language, and learn from his edits. Load this
when developing or revising substantial strategy, positioning, campaign, or brand work.

### references/native-document-editing.md
How to edit existing native documents without destroying their structure or design.
Load this before creating or changing a formatted or collaborative document, even for
a narrow edit. Douglas's standing rule: no added notes, including speaker notes, unless
explicitly requested. Follow that reference's annotation preflight and readback checks.

### references/knowledge-boundaries.md
How project work becomes reusable operating doctrine without contaminating future work
with dated briefs, campaign facts, or one-off preferences. Load this when adding,
revising, or compounding a skill.

### references/learning-loop.md
How normal work compounds: detect meaningful feedback or results, capture the smallest
useful learning, classify it, and promote only evidence that clears the knowledge
boundary. Load this after a meaningful correction, explicit ruling, measured result, or
repeated pattern changes a future decision.

### references/golden-path.md
The canonical Compound Marketing workflow. Load this for substantial strategy,
recurring marketing, or GTM work that should carry governed decisions from context
through delivery and learning.

## When to invoke

This file supplies the root dependency to downstream skills; its reference library is
loaded by task, not in full. Specific situations where it is invoked directly:

- When generating any brand or marketing work (copy, positioning, strategy, launches)
- When editing or evaluating existing work against Every's standards
- When building or auditing a new skill for alignment with the OS
- When onboarding a new brand or product into the Every system
- When resolving a conflict between brand-voice and positioning guidance

## Reference routing

When this skill is loaded, route to the appropriate reference file based on the task:

| Task type | Load |
|---|---|
| Need a reference, thinker, or historical grounding | `references/canon.md` |
| Need the point of view or argumentative position | `references/method.md` |
| Need to operationalize a framework (Binet/Field, Sharp, Aaker, etc.) | `references/frameworks.md` |
| Need to develop or revise substantial work with Douglas | `references/collaboration.md` |
| Need to edit an existing formatted document | `references/native-document-editing.md` |
| Build, restructure, or review a substantive brand or marketing strategy pitch deck | `references/strategy-decks.md` |
| Need to add or compound repository guidance | `references/knowledge-boundaries.md` |
| Meaningful feedback or a result should improve future work | `references/learning-loop.md` |
| Substantial strategy, recurring marketing, or GTM work | `references/golden-path.md` |
| 10- to 15-minute GTM approval deck for a launch content ecosystem | `../../marketing/gtm/SKILL.md` and `../../marketing/gtm/references/content-system-approval-deck.md` |

Multiple references can be loaded simultaneously. A positioning task, for example, might
load canon.md for Trout/Ries context, method.md for Every's positioning stance, and
frameworks.md for the operational positioning template.

## Close the learning loop

Do not add a questionnaire or ceremonial retrospective. When normal feedback, an explicit
ruling, a measured result, or a repeated pattern supplies evidence that should change a
future decision, load `references/learning-loop.md` and capture the candidate as part of
the task closeout. If the evidence teaches nothing transferable, finish the task without
creating a learning record.

Never promote a candidate merely because it is memorable or recent. Apply the knowledge
boundary, protect sensitive project detail, and update the narrowest source only when the
promotion standard is met.

After changing root doctrine, routing, collaboration, knowledge boundaries, or this
learning loop, run the five cases in `evals/smoke-cases.json` against
`evals/smoke-rubric.md`. Use `scripts/check_learning_loop.py` to validate the case
manifest and any learning candidate before it enters the repository.

## Dependencies

None — this is the root dependency. All other skills load this skill.

## Interaction with downstream skills

- **brand-voice/** skills inherit the method's creative and taste stances
- **positioning/** skills inherit the method's brand theory weighting and the frameworks
- **craft/** skills inherit the canon's creative lineage and the method's creative stack
- **strategy/** skills inherit the full OS — canon, method, and frameworks
- **launches/** skills orchestrate all of the above through the OS
- **marketing-science/** skills contribute back to the OS — research and archetyping
  inform the canon and frameworks over time
- **measurement/** connects Marketing-created demand with subscriber quality, brand
  movement, authority, and business outcomes
- **compound-from-results** turns completed programs into decisions, program guidance,
  and narrowly supported updates to durable doctrine
- **strategy/compound-marketing** carries governed decisions through strategy, market
  execution, and a measured learning closeout
- **marketing/gtm** is the single GTM entry point across flagship, standard, revision,
  drumbeat, and social modes
- **craft/compound-copywriting** turns accepted edits into bounded project guidance and
  tests transfer on fresh copy before any durable promotion
- **workflows/** exposes four public entries over the existing specialists; it does not
  copy their implementation or weaken their approval and evidence requirements
- **strategy/** preserves the full idea while producing concise, decision-ready briefs
- **strategy/marketing-pod** coordinates specialist skills across parallel agent roles
  while Douglas retains strategic decisions, approval, and final taste authority

## Knowledge boundary

Project work supplies evidence. It does not become operating doctrine automatically.
Reusable skills contain transferable methods; brand and product modules contain durable
ruled canon; optional historical cases live under `docs/cases/` and are never loaded by
default. Apply `references/knowledge-boundaries.md` before any repository update.

## Status

The doctrine, collaboration rules, unified GTM route, and Compound Marketing run records
are active. Compound Copywriting and marketing pods remain beta until prospective use
clears their stated transfer and review-burden thresholds. Files marked `## To do` are
scaffolding and never route as authoritative guidance.
