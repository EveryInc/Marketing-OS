# Every Skills

A skills repository for Every's marketing OS. Each skill is a structured prompt module designed to be loaded into Plus One (or any Claude-based workflow) for a specific marketing task.

The repo combines active operating skills with scaffolding that is populated as Every's
brand documents, measurement systems, and channel strategies are finalized.

## Taxonomy

The repository is organized into seven top-level folders:

1. **foundation/** — The Marketing OS, the operating system underlying all skills
2. **brand-voice/** — Voice guides for Every's master brand and each sub-brand (Cora, Spiral, Monologue, Plus One, Proof, Sparkle)
3. **positioning/** — Positioning frameworks for Every master and each sub-brand
4. **strategy/** — Higher-order strategy skills (messaging architecture, program briefs, one-pagers) that compose voice, positioning, and measurement
5. **craft/** — Execution-level skills for specific deliverables: copywriting, editing, naming, and channel-specific output (launch emails, LinkedIn posts, X posts, website copy, press comms)
6. **launches/** — Orchestration skills for three launch tiers (improvement, feature, new product) that load strategy and all channel craft skills
7. **marketing-science/** — Research, archetyping, brand equity, and measurement skills that inform positioning, programs, and decisions

## Dependency model

Every skill loads `foundation/marketing-os` as its root dependency. Additional dependencies cascade by category — positioning skills pull in marketing-science, craft skills pull in brand-voice and positioning, launch skills orchestrate strategy and all five channel craft skills.

See [ARCHITECTURE.md](ARCHITECTURE.md) for the full dependency graph.

## Status

The foundation doctrine, Every-master positioning, audience model, measurement system,
program briefs, and core editing workflows are active. Some product-level voice,
positioning, and channel skills remain scaffolding.
