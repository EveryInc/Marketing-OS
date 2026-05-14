# Marketing OS

A skills repository for Every's marketing OS. Each skill is a structured prompt module designed to be loaded into Plus One (or any Claude-based workflow) for a specific marketing task.

This repo is **scaffolding only** — stubs will be populated as the corresponding brand docs and frameworks are completed.

## Taxonomy

The repository is organized into seven top-level folders:

1. **foundation/** — The Marketing OS, the operating system underlying all skills
2. **brand-voice/** — Voice guides for Every's master brand and each sub-brand (Cora, Spiral, Monologue, Plus One, Proof, Sparkle)
3. **positioning/** — Positioning frameworks for Every master and each sub-brand
4. **strategy/** — Higher-order strategy skills (messaging architecture, one-pagers) that compose voice and positioning
5. **craft/** — Execution-level skills for specific deliverables: copywriting, editing, naming, and channel-specific output (launch emails, LinkedIn posts, X posts, website copy, press comms)
6. **launches/** — Orchestration skills for three launch tiers (improvement, feature, new product) that load strategy and all channel craft skills
7. **marketing-science/** — Research, archetyping, and brand-equity theory skills that inform positioning and naming

## Dependency model

Every skill loads `foundation/marketing-os` as its root dependency. Additional dependencies cascade by category — positioning skills pull in marketing-science, craft skills pull in brand-voice and positioning, launch skills orchestrate strategy and all five channel craft skills.

See [ARCHITECTURE.md](ARCHITECTURE.md) for the full dependency graph.

## Status

All 31 skill stubs are in place. Each will be populated as its corresponding brand doc or framework is finalized.
