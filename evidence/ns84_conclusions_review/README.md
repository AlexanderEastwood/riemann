# NS-84: per-turn review of the full conclusion register

All 91 registered conclusions were read for scope, hypotheses, evidence
status and implications before the continuation. This is a conclusions and
dependency review, not a fresh proof audit or numerical replay of every
historical result. `review.json` records the reviewed main commit, complete
register, current findings and corrections.

All current proposition labels and declared evidence paths resolve. Four
map nodes explicitly say MISSING, as the existing ledger requires. Two
historical original-evidence groups remain open. Publication artifacts
stored at historical tags do not recover their underlying missing science.

The official all-manifest checker returns failure in the current tree for
four legacy manifests: v1.34–v1.37. Its raw output is preserved. Every one
of the 18 affected publication artifacts matches its expected SHA-256 at
the corresponding original version tag; paths and immutable tag commits
are recorded separately. All newer manifests pass. No historical manifest
is rewritten to make this check appear clean.

The user’s requirement to review the repo and all recorded conclusions at
every turn is now in AGENTS.md section 0. The current review corrects stale
summary claims and arrows, without changing a scientific theorem or
creating another manuscript version. G2 and RH remain open.
