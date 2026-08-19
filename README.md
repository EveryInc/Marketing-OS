# Marketing OS

Every's AI-native marketing operating system. Its core method is **Compound Marketing**:
every project produces effective work now and improves the system that produces the
next project.

Marketing creates demand and cultural gravity. Growth converts that demand. Marketing OS
connects the two through a measurable operating loop while protecting creative ambition,
taste, and brand coherence.

## How It Works

`context -> strategy -> market -> memory -> stronger next run`

`strategy/compound-marketing` is the plain-language entry point. It creates one governed
decision record, routes the approved strategy into a recurring program or GTM plan, and
closes the run through human edits and measured results. Completed work improves the
system only when the learning transfers beyond the project that produced it.

Every specialist skill still loads `foundation/marketing-os` as its root. Research,
audiences, positioning, voice, craft, launches, and measurement remain available when
the active stage requires them.

The repository map is:

1. **foundation/** — The Marketing OS, the operating system underlying all skills
2. **brand-voice/** — Voice guides for Every's master brand and each sub-brand (Cora, Spiral, Monologue, Plus One, Proof, Sparkle)
3. **positioning/** — Positioning frameworks for Every master and each sub-brand
4. **strategy/** — Compound Marketing plus higher-order strategy skills, including role-bounded marketing pods, that compose voice, positioning, programs, GTM, and measurement
5. **craft/** — Execution-level skills for art direction, copywriting, editing, naming, and channel-specific output (launch emails, LinkedIn posts, X posts, website copy, press comms)
6. **launches/** — Orchestration skills for three launch tiers (improvement, feature, new product) that load strategy and all channel craft skills
7. **marketing-science/** — Research, archetyping, brand equity, and measurement skills that inform positioning, programs, and decisions
8. **marketing/** — Integrated planning workflows that turn strategy, sources, and campaign decisions into executable GTM artifacts

## Dependency model

Every skill loads `foundation/marketing-os` as its root dependency. Additional dependencies cascade by category — positioning skills pull in marketing-science, craft skills pull in brand-voice and positioning, launch skills orchestrate strategy and all five channel craft skills.

See [ARCHITECTURE.md](ARCHITECTURE.md) for the full dependency graph.

## Taxonomy

The repository has eight skill families:

1. **foundation/** — Every's marketing doctrine, canon, operating frameworks,
   collaboration rules, and native-document editing protocol
2. **brand-voice/** — Voice systems for Every and its products
3. **positioning/** — Durable, ruled master-brand and product positioning
4. **strategy/** — Compound Marketing, Compound Brand, messaging architecture,
   measurable program briefs, and executive one-pagers
5. **craft/** — Verbal identity, art direction, copywriting, editing, naming, PR,
   social, email, web, and long-form execution
6. **launches/** — The canonical launch process, launch calendar, brief, GTM strategy,
   claims clearance, wireframing, email flows, and three launch tiers
7. **marketing-science/** — Research, audience archetypes, brand equity, messaging
   evidence, attribution, Fame Score, cohort economics, and results compounding
8. **marketing/** — Integrated GTM planning that turns approved strategy, sources, and
   campaign decisions into executable artifacts

Optional historical cases live in `docs/cases/`. Skills never load them by default.

## What Belongs in the OS

Marketing OS stores reusable methods: how to turn context into strategy, execute a
launch, build a GTM plan or recurring program, measure the result, and compound the
learning.

It does not store active roadmaps, launch briefs, campaign concepts, current rosters,
temporary claims, prices, budgets, embargoes, or project calendars. Durable positioning
and voice may live in their product modules only after they have been ruled as canon.

Project work can change the OS when Douglas explicitly makes the learning a standard,
the pattern succeeds across multiple relevant projects, or unusually strong evidence
supports a bounded rule. Otherwise the learning stays with the project or in an optional
case.

## Current State

As of Aug. 20, 2026, Marketing OS contains 64 skills and 100 operating references.

Ready for structured use:

- Every master positioning, brand voice, audience system, and brand architecture
- Evidence-led research, competitive auditing, and positioning matrices
- Compound Brand strategy through verbal identity and art direction
- Messaging architecture, proof standards, and evidence banks
- Canonical launch planning, GTM strategy, claims clearance, and channel production
- Program briefs with owners, costs, subscriber paths, and investment gates
- PR and Instagram planning tied to authority and subscriber acquisition
- Executive one-pagers for 10- to 15-minute leadership reviews
- Marketing measurement across sourced free subscribers, cohorts, CAC, LTV:CAC, Fame
  Score, authority, and Consulting demand
- Compounding from Douglas's edits and from campaign results without importing project
  details into unrelated work
- Level 7 marketing pods that run research, strategy, operations, production, QA, and
  measurement as bounded agent roles while Douglas retains strategic and creative
  control, invoked through normal requests rather than orchestration jargon
- A Compound Marketing golden path with decision records, run records, cross-stage
  fidelity checks, and an explicit proof standard

Still in development:

- Product-specific positioning and voice where source documents have not been ruled
- Several execution-channel skills that remain explicit scaffolding
- More forward tests and comparative evaluations
- Live data integrations for repeatable quarterly reporting
- A prospective comparable second run and independent teammate rerun required for a
  publishable compounding claim

The Brand Book and Thesis GTM cases are real retrospective baselines. They pass the
structural record checks and intentionally report `proof_ready: false`; neither recorded
enough prospective evidence to prove compounding.

Files marked `## To do` are scaffolding, not authoritative product or channel guidance.

## Changelog

### Aug. 19, 2026: Compound Marketing V1

- Added the governing Compound Marketing strategy and canonical golden path
- Added one entry skill for strategy, recurring programs, GTM, and learning closeout
- Added shared decision and run records that preserve human rulings across stages
- Added deterministic validation for decision fidelity and comparable-run proof
- Added honest Brand Book and Thesis GTM baselines without upgrading them into claims
- Kept design, asset production, and agent-count claims outside V1

### July 24, 2026: Reusable Operating Layer

- Added Marketing-sourced free subscribers, attribution, cohort quality, CAC, LTV:CAC,
  Fame Score, authority, and Consulting demand measurement
- Added program briefs that preserve the creative idea while defining ownership, cost,
  instrumentation, and scale, revise, or stop gates
- Added reusable PR and Instagram planning methods
- Added executive summaries for 10- to 15-minute leadership reviews
- Added native-document editing and compounding from Douglas's edits
- Added results compounding so completed programs create dated learning without turning
  one campaign into permanent doctrine
- Added knowledge-boundary rules that separate reusable doctrine, durable brand canon,
  and optional historical cases
- Removed active project plans, launch evidence, rosters, offers, and dated campaign
  instructions from default skill paths

### July 18–21, 2026: Brand and Launch Systems

- Built the Every master brand voice
- Added the canonical marketing launch workflow and GTM plan
- Built Compound Brand strategy through art direction
- Strengthened GTM decision, conversion, and activation rules

### July 6–13, 2026: Execution Foundation

- Populated research, archetyping, positioning, and brand-equity systems
- Added launch architecture, claims clearance, PR checks, and email-flow guidance
- Added messaging-document discipline, copywriting rules, and evidence-bank standards
- Began compounding approved human edits into durable operating guidance

See the [full commit history](https://github.com/EveryInc/Marketing-OS/commits/main) for
line-level changes.
