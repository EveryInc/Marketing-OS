# Marketing Pod Shared Brief and Assignment Contracts

Use these contracts to prevent context loss, authority drift, duplicate work, and stale
outputs across a multi-agent run.

In conversation, call these the **shared brief** and **agent assignments**. “Project
packet” and “work order” are precise internal labels for logs and templates; Douglas
does not need to use or remember them.

## Contents

1. Shared brief
2. Agent assignment
3. Worker return
4. Decision and change control
5. State model

## Shared brief

Create one versioned shared brief before dispatch. The run ledger may label it the
project packet. Include:

### Identity

- Project and version
- Project type and current stage
- Objective and intended audience behavior
- Primary action
- Deadline or measurement window

### Authority map

| Authority | Owner | Canonical source | Confirmed or open | Freshness requirement |
|---|---|---|---|---|
| Product truth | | | | |
| Strategic decisions | | | | |
| Canonical copy | | | | |
| Structural model | | | | |
| Formatting | | | | |
| Evidence | | | | |
| Approval | | | | |
| Publication | | | | |

Authority belongs to a role or person, not automatically to the newest file. When two
sources conflict, record both and route the decision to the named owner.

### Strategic state

- Locked decisions
- Protected creative premise and exact language
- Primary audience and explicit non-target
- Offer, first value, and proof requirement
- Known facts
- Hypotheses
- Open questions and owners
- Explicit exclusions

### Delivery state

- Required artifacts and owners
- Dependencies and approval gates
- Output locations
- External actions allowed
- Baseline, primary decision metric, target or threshold, data source, decision date

Track each active job in a ledger:

| Run ID | Work order ID | Worker label | Platform handle | Artifact ID/version | Input version | Job status | Artifact state |
|---|---|---|---|---|---|---|---|

The manager records the platform handle immediately after dispatch so a specific job
can be stopped, superseded, or re-run without relying on a role name alone.

## Agent assignment

Give every worker this bounded assignment. The run ledger may label it a work order:

```text
RUN ID
[Stable pod-run identifier]

WORK ORDER ID
[Stable job identifier]

ARTIFACT ID / VERSION
[One owned output and its starting version]

ROLE
[One charter from role-charters.md]

TASK
[One concrete outcome]

INPUT VERSION
[Project packet version]

WORKER LABEL
[Stable label assigned before dispatch]

ALLOWED SOURCES
[Exact links, files, databases, or search scope]

MARKETING OS ROUTES
[Only the required skills and references]

OUTPUT CONTRACT
[Artifact, structure, location, and recipient]

OUT OF SCOPE
[Decisions, artifacts, tools, and destinations this worker cannot touch]

STOP CONDITIONS
[Missing authority, source conflict, unavailable tool, permission gap, unsafe action]

VERIFICATION
[Evidence, checks, and completion threshold]
```

Do not assign “help with the launch.” Name one job, one artifact, and one recipient.

## Worker return

Require every worker to return:

```text
RUN ID / WORK ORDER ID / WORKER LABEL
[Echo the exact dispatch identity]

ARTIFACT ID / VERSION / INPUT VERSION
[Echo the owned output and source packet version]

JOB STATUS
COMPLETE | BLOCKED | SUPERSEDED

ARTIFACT STATE
IN REVIEW | BLOCKED | SUPERSEDED

RESULT
[The completed artifact or exact artifact link]

DECISIONS APPLIED
[Locked decisions followed]

EVIDENCE
[Source-linked facts and dated checks]

INFERENCES
[Clearly labeled interpretation]

CONFLICTS AND OPEN QUESTIONS
[Owner required and downstream impact]

VERIFICATION
[Checks run, failures, and unresolved risk]

HANDOFF
[Named next role and what it can safely begin]
```

Reject a return that omits sources, hides conflicts, changes scope, or reports completion
without its required verification.

Job status and artifact state are separate. COMPLETE means the assigned work ended; it
maps the artifact to IN REVIEW, never APPROVED. Only the named approval owner can move
that exact artifact version to APPROVED.

Valid worker-return pairs are COMPLETE / IN REVIEW, BLOCKED / BLOCKED, and SUPERSEDED /
SUPERSEDED. Later approval changes artifact state without rewriting the completed job
status.

## Decision and change control

Maintain a decision log:

| ID | Decision | Owner | Date | Source | Affected artifacts | Re-run required |
|---|---|---|---|---|---|---|

When a source or ruling changes:

1. Increment the project packet version.
2. Mark affected outputs SUPERSEDED.
3. Trace downstream artifacts from the decision log.
4. Re-run only the affected jobs.
5. Require QA against the new packet before approval.

Do not patch conflicting outputs together. Preserve the ruling and rebuild the narrowest
affected layer.

## State model

Use one state per artifact:

- **READY:** Inputs and authority are sufficient for work to begin.
- **IN PROGRESS:** One role owns the current version.
- **BLOCKED:** A named missing input, conflict, permission, or ruling prevents completion.
- **IN REVIEW:** The artifact is complete enough for its approval gate.
- **APPROVED:** The named approver accepted this exact version.
- **SUPERSEDED:** A newer source or ruling invalidated this version.
- **SHIPPED:** The approved artifact reached its authorized destination.

An emoji, “looks good,” ordinary praise, or silence is not APPROVED unless the project
packet explicitly defines it as an approval signal.
