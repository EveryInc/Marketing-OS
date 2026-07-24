# Marketing OS

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

Marketing OS is composed of five reference files, each serving a distinct role:

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
Load this before changing a formatted, multi-tab, table-heavy, or collaborative document.

## When to invoke

This skill is loaded automatically by every other skill in the repo. It is the root
dependency. Specific situations where it is invoked directly:

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

Multiple references can be loaded simultaneously. A positioning task, for example, might
load canon.md for Trout/Ries context, method.md for Every's positioning stance, and
frameworks.md for the operational positioning template.

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
- **strategy/** preserves the full idea while producing concise, decision-ready briefs

## Status

The core doctrine and collaboration rules are active. Canon and framework applications
continue to develop as the corresponding thinking is finalized.
