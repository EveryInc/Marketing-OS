# Compound Marketing Artifact Receipt

The `receipt` command scaffolds an unsigned JSON receipt in the run directory. A named
human fills `verified_by` and `verified_at` only after checking the exact artifact against
the rendered decision record.

A valid schema V2 receipt binds:

- The run and the `strategy_to_market` stage.
- The canonical governance digest covering source ownership and freshness, conflicts,
  locked decision meaning and provenance, protected language, and open questions.
- The current decision-record SHA-256 digest as a projection-staleness check.
- Every locked decision ID.
- A local artifact path and SHA-256 digest, or a remote immutable revision ID or hashed
  local export.
- The verifier and verification time.

The producing agent may create the file but may not sign it. A remote URL or human version
label without an immutable revision or hashed export is structural evidence only and
cannot make a run operationally ready.

Remote artifacts must use HTTPS. Local artifacts must be regular files inside the run
directory; receipts cannot point elsewhere on the machine.

Artifact acceptance and fidelity approvals must carry the digest of the receipt's exact
artifact binding. A valid receipt paired with an approval for another path, revision, or
hash fails closed.

The checker proves that the recorded files and fields agree. It does not authenticate the
human or establish that an attestation is truthful.
