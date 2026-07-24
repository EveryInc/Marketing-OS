# Marketing OS

A skills repository for Every's marketing OS. Each skill is a structured prompt module designed to be loaded into Plus One or another agent workflow for a specific marketing task.

The repository combines mature operating skills with active modules that are still being developed and tested.

## Taxonomy

The repository is organized into seven top-level folders:

1. **foundation/** — The Marketing OS, the operating system underlying all skills
2. **brand-voice/** — Voice guides for Every's master brand and each sub-brand
3. **positioning/** — Positioning frameworks for Every master and each sub-brand
4. **strategy/** — Higher-order strategy skills, including the gated Compound Brand workflow, messaging architecture, measurable program briefs, and one-pagers
5. **craft/** — Identity and execution skills, including verbal identity, art direction, copywriting, editing, naming, and channel-specific output
6. **launches/** — Orchestration skills for three launch tiers plus the flagship GTM, calendar, brief, claims, wireframe, and email systems
7. **marketing-science/** — Research, archetyping, brand-equity theory, and measurement that inform strategy, identity, and investment decisions

## Dependency model

Every skill loads `foundation/marketing-os` as its root dependency. Additional dependencies cascade by category. The Compound Brand orchestrator runs a gated sequence from research and strategic foundation through brand character, optional equity modeling, verbal identity, and art direction. Launch skills orchestrate strategy and channel craft skills.

See [ARCHITECTURE.md](ARCHITECTURE.md) for the full dependency graph.

## Current operating coverage

Ready for structured use:

- Every master positioning and brand voice
- Evidence-led research, competitive auditing, and positioning matrices
- Compound Brand strategy through art direction
- Aaker-led brand-equity modeling
- Messaging architecture and flagship launch systems
- Marketing measurement, quarterly scorecards, and results compounding
- Program briefs that protect the creative premise while defining ownership, cost, and decision gates
- The Thesis 2027 brand brief as a worked art-direction case

Still being developed:

- Product-specific positioning and voice modules that remain stubs
- Several channel and deliverable craft skills
- Additional worked cases and evaluations
