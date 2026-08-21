# Marketing OS Learning Loop

Make completed work improve the next run without turning every correction into doctrine.
Use normal task feedback as the input. Do not ask Douglas to complete a retrospective.

## Trigger

Run the loop only when one of these signals changes a future decision:

- Douglas makes a meaningful edit or rejects an approach.
- Douglas or company leadership explicitly rules a standard.
- A measured result supports a program decision.
- The same useful pattern appears in two independent pieces of work.
- Current evidence corrects a factual error in the system.

Do nothing when the change is formatting cleanup, a temporary project fact, an unresolved
preference, or a correction already covered by a durable rule.

## Capture

Use the evidence already produced during the task:

1. Name the task type and the source roles that governed it.
2. Preserve artifact references, not raw private source material.
3. State the meaningful delta or result in one sentence.
4. Explain which future decision it changes.
5. State the boundary: where the lesson applies and where it does not.

Do not interrupt delivery to collect fields that can be derived from the work. Never copy
private drafts, customer data, credentials, embargoed facts, or personal information into
a repository candidate.

## Classify

Choose exactly one:

- **Durable rule:** A transferable instruction that changes future decisions.
- **Good example:** A compact illustration of an existing rule.
- **Regression test:** A failure mode the system should catch in future runs.
- **Temporary fact:** A dated product, people, price, launch, or portfolio fact.
- **One-off taste decision:** A local choice that should remain with the project.

Temporary facts and one-off taste decisions stay project-only. Good examples and
regression tests remain candidates until they are sanitized and placed in the narrowest
relevant evaluation. Durable rules must pass the promotion gate.

## Promote

Promote a durable rule only when at least one condition holds:

1. Douglas or company leadership explicitly establishes it.
2. Two independent tasks support the same bounded pattern.
3. A credible experiment or unusually strong result supports it.
4. It corrects a factual error in current doctrine.

Then:

1. Apply `knowledge-boundaries.md`.
2. Search for an existing broader rule before adding text.
3. Update the narrowest authoritative file.
4. Add or strengthen one regression case when the lesson prevents a repeatable failure.
5. Run the Marketing OS smoke tests and the affected skill evaluation.
6. If the work has a Compound Marketing run record, name the promoted destination and
   decision it will change on the next comparable run.

Do not promote the full project, its creative premise, or its working language. Abstract
only the decision rule. Keep the human-edited artifact canonical for the project.

## Candidate record

Use `../scripts/check_learning_loop.py candidate <file>` to validate a repository
candidate before promotion. A candidate records:

- Task ID, date, and task type.
- Signal and evidence references.
- Classification and bounded lesson.
- Proposed destination and limits.
- Promotion state and independent evidence count.
- Whether credible causal evidence supports a single measured result.
- Confirmation that sensitive detail was removed.

The record is an intake format, not permanent doctrine. Delete it after the lesson is
promoted, rejected, or captured by a narrower evaluation.

## Closeout rule

Keep the user-facing closeout focused on the work. Mention the learning only when it
caused a material system change or requires a decision. The absence of a learning record
is a valid result.
