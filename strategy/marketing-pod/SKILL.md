# Marketing Pod

Run a role-bounded team of marketing agents in parallel while Douglas remains the
conductor, strategic decision-maker, and final taste authority. Use Marketing OS as the
shared constitution, then give each worker only the sources, skills, authority, and
output contract required for its job.

This is the Level 7 operating layer. It coordinates specialist agents; it does not
replace the specialist skills or introduce a manager agent. If an agent decomposes,
assigns, reviews, and redirects the pod without Douglas, the workflow has crossed into
Level 8 and requires a separate authorization and control design.

## When to invoke

- When Douglas asks to run a marketing pod, parallelize Marketing OS work, or work at
  Level 7
- When Douglas says “help me run marketing for this,” “take point on this launch,”
  “figure out how we should market this,” or otherwise asks for substantial marketing
  work with several moving parts
- When a launch, brand system, campaign, event, or recurring program has three or more
  separable workstreams
- When research, strategy, operations, channel production, and QA need distinct owners
- When one long agent thread is producing context loss, duplicated work, weak source
  authority, or expensive review
- When testing whether a Marketing OS workflow can compound across repeated runs

Do not invoke for a single copy edit, one channel asset, a narrow research question, or
work whose strategic foundation is still too ambiguous to divide responsibly.

## How Douglas invokes this

Douglas never has to say “wave,” “project packet,” “work order,” or name the agents he
needs. Those are internal operating terms, not a command language.

A normal request is enough:

- “Help me run the Every Agent launch.”
- “Take point on the marketing for this event.”
- “Can we figure out how to launch this?”
- “There are too many moving pieces here. Organize this for me.”

Translate the request into the operating system silently. Respond in plain English:

1. Interview Douglas before doing any work.
2. Summarize what you heard and what remains genuinely unclear.
3. Propose the first few agents by the work they will do, not by formal role names.
4. Explain what Douglas will receive, then ask a natural approval question such as: “I
   think the first move is to have three agents check the product truth, customer
   evidence, and competitive landscape. Want me to start?”
5. After approval, handle IDs, versions, source maps, assignments, and status tracking
   without making Douglas operate the machinery.

Use these translations in user-facing updates:

| Internal term | Say to Douglas |
|---|---|
| Project packet | Shared brief, or “what everyone is working from” |
| Wave | Batch, round, or “the agents working now” |
| Work order | Assignment, or “what this agent owns” |
| Discovery gate | “Here is what we learned and what you need to decide” |
| Strategy gate | “Here is the recommended direction; approve or redirect it” |

Use the formal terms only inside logs and reusable contracts where precision matters.

## Mandatory opening interview

Always interview Douglas before taking action. This applies even when the request seems
clear, relevant context already exists, or a similar project has run before.

Before the interview is complete, do not:

- Search Slack, Notion, Drive, the web, analytics, or other project sources
- Dispatch agents or prepare assignments
- Draft strategy, copy, briefs, plans, or deliverables
- Modify files, post messages, contact people, or change any system

Ask one to three plain-language questions at a time. The first round should establish
the highest-leverage human context, usually:

- What outcome would make this feel successful?
- What is the idea, tension, or instinct Douglas does not want flattened?
- What is already decided, politically sensitive, constrained, or off-limits?

Do not turn the interview into intake paperwork. Do not ask for information Douglas has
already supplied. Even when his opening request answers most of the brief, ask at least
one question that sharpens the stakes, judgment, or quality bar.

Wait for Douglas's response. Then summarize the brief in his language. Ask another
round only if the answer could materially change the strategy, team, approval chain, or
definition of success. Otherwise propose the first batch and ask permission to start.

## Operating contract

Keep Douglas in the manager role:

- Douglas chooses the problem, rules strategic conflicts, approves the launch
  constitution, protects the creative premise, and owns final quality.
- Worker agents execute bounded jobs. They do not delegate, expand scope, publish,
  contact people, or alter a canonical source unless explicitly authorized.
- One role owns each decision surface. Parallel workers never edit the same canonical
  artifact.
- Every factual claim traces to a current source. Every inference is labeled.
- Project state stays in the project packet. Only transferable, sufficiently supported
  learning enters Marketing OS.

Load `references/role-charters.md` before selecting workers. Load
`references/handoff-contracts.md` before dispatch. Load `references/run-scorecard.md`
before the first wave so the run has a baseline and decision rule.

## Choose the pod

Use the smallest pod that covers the work. Prefer three to five concurrent workers.

### Launch pod

Use for product, event, editorial-franchise, or major feature launches:

1. Truth and evidence
2. Customer proof
3. Category and competition
4. Launch operations
5. Strategy after the discovery gate
6. Channel production after strategy lock
7. Independent QA and measurement

### Brand pod

Use with `strategy/compound-brand`:

1. Customer and category research
2. Competitive verbal audit
3. Competitive visual and semiotic audit
4. Brand-equity evidence
5. Verbal and visual production only after the relevant human gate

### Program pod

Use for a recurring campaign, channel, partnership, event, affiliate, PR, or research
program:

1. Audience and demand evidence
2. Mechanism and operational feasibility
3. Economics and measurement preflight
4. Creative system and channel expression after the Program Brief locks

## Run the workflow

### 1. Establish authority

Complete the mandatory opening interview first.

Identify the sources and people that own product truth, strategic decisions, canonical
copy, structure, formatting, evidence, approval, and publication. After the interview,
search the supplied Slack, Notion, Drive, product, and analytics sources before asking
Douglas for anything discoverable.

After the opening interview, ask follow-up questions only when an unresolved answer
would change the pod structure, strategic direction, approval chain, external action,
or definition of success. Ask one to three questions at a time.

### 2. Build the shared brief

Build one versioned shared brief using `references/handoff-contracts.md`. Internally this
is the project packet. Include the objective, primary audience action, authority map,
locked decisions, protected creative premise, open questions, exclusions, required
artifacts, approval owners, source links, baseline, and success gate.

Do not turn the packet into durable doctrine. It is current project state.

### 3. Choose the next batch

Run only independent jobs in the same wave. Work is parallel-safe when workers have:

- No dependency on another worker's unfinished decision
- Disjoint output artifacts and authority
- The same approved source packet
- No shared live document or destination to edit
- A reconciliation cost smaller than the expected production savings

Serialize uncertain or overlapping work. Cap a wave at five workers.

Before every dispatch, tell Douglas what the shared brief says, which agents you propose
to start, what each will return, and what remains blocked. Dispatch only after he
approves that exact batch or explicitly approves a brief version that names and
pre-authorizes a later batch and its assignments. Record that authorization in the
decision log. A broad request to “run the pod” is not standing approval for later
batches.

### 4. Give each agent a clear assignment

Give each worker a fresh context containing only:

- The project packet
- Its role charter
- Its assigned Marketing OS skills
- Its task and output contract
- Its allowed sources and tools
- Explicit exclusions and stop conditions
- Its verification and handoff recipient

Use actual parallel agent tools when the environment permits them. If parallel agents
are unavailable, produce complete work orders for separate tasks and state that the pod
was prepared but a Level 7 run did not occur. Do not simulate independence with multiple
personas in one context.

### 5. Review what the first batch learned

Reconcile the first wave into one discovery packet. Surface contradictions rather than
averaging them. Douglas approves the evidence base, resolves authority conflicts, and
rules what the Strategy worker must decide.

Do not begin strategy or channel production before this gate passes.

### 6. Choose the strategy

Dispatch one Strategy worker from the approved discovery packet. It returns the
governing audience, offer, value hierarchy, position, proof system, campaign hierarchy,
conversion path, creative premise, primary action, and strategic refusal.

Douglas approves or redirects that exact decision brief. Record the ruling and increment
the project-packet version. Do not begin channel production before the strategy gate
passes.

### 7. Run production in parallel

Dispatch channel or craft workers from the same approved decision packet. Give web,
email, social, press, video, and art-direction workers separate artifacts. Require them
to preserve the same proposition, claims, naming, dates, prices, and primary action.

Channel workers adapt the strategy to their medium. They do not reopen it.

### 8. Run independent QA

Give the QA worker the approved packet and produced artifacts, not the production
workers' reasoning. Require:

- Claims clearance and permission checks
- Cross-surface fact and offer consistency
- Positioning, audience, and voice alignment
- Missing-state, dependency, and approval checks
- Measurement and instrumentation readiness
- A plain block list for anything that cannot ship

QA reports findings. It does not silently rewrite the canonical work.

### 9. Review, decide, and compound

Present Douglas with the governing decisions, finished artifacts, contradictions,
blockers, QA findings, and the scorecard. Record his rulings in the decision log.

After the measurement window, use `marketing-science/measurement` and
`marketing-science/measurement/references/compound-from-results.md`. Promote a learning
only when it passes the Marketing OS knowledge-boundary test.

## Failure rules

- Stop a worker that invents facts, changes its role, or writes beyond its authority.
- Supersede stale outputs after a source or decision changes; never merge both versions.
- Re-run only the affected downstream work after a ruling changes.
- Collapse to a serial workflow when parallel outputs repeatedly collide.
- Never count agent volume as progress. Count accepted artifacts, lower review burden,
  reliability, and improved second-run performance.

## Dependencies

- `foundation/marketing-os`
- `foundation/marketing-os/references/collaboration.md`
- `foundation/marketing-os/references/knowledge-boundaries.md`
- `strategy/program-brief` for recurring programs
- `strategy/compound-brand` for brand systems
- `launches/launch-brief` and `launches/gtm-plan` for L/XL launches
- `marketing/gtm` for non-flagship launches and drumbeats
- `marketing-science/research`
- `marketing-science/measurement`
- `launches/claims-clearance`
- The relevant `positioning/`, `brand-voice/`, and `craft/` skills

## Quick checklist

- [ ] Douglas was interviewed before research, delegation, drafting, or system action
- [ ] Douglas remains the manager and final decision-maker
- [ ] The project has three or more genuinely separable workstreams
- [ ] Authority and canonical sources are explicit
- [ ] The project packet contains the baseline and success gate
- [ ] Every worker has one role, one artifact, and explicit exclusions
- [ ] Parallel workers do not share a live document or unresolved dependency
- [ ] Strategy is approved before channel production
- [ ] QA is independent from production
- [ ] No external write or contact occurs without authorization
- [ ] The scorecard records reliability, review burden, adoption, and second-run change
- [ ] Project learning passes the knowledge-boundary test before entering Marketing OS
