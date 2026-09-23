# Repository layout and branch conventions

This repository is a **research record**, not a software project. Its unit
of work is a numbered result plus the evidence that supports it. The layout
and branch names exist so that every claim in the manuscript resolves to a
checkout, and so that negative results are first-class rather than buried.

## Directory layout

```
manuscript/
  fixed_space_prime_action_v1.tex   the single live manuscript
  build.sh                          latexmk wrapper
  snapshots/                        frozen PDFs of past versions
evidence/
  v124/ v135/ v136/ v137/ ...       artifacts, ONE DIRECTORY PER VERSION
  MISSING.md                        ledger of cited-but-absent artifacts
  diag_<topic>/                     diagnostics that are NOT certificates, labeled as such
NEXT_STEPS.md                       shared task board: claim before you start
PROPOSAL_TEMPLATE.md                proposal gate: fill in before claiming a research row
controls/
  davenport_heilbronn.py            known-false analogue (diagnostic, not a certificate)
manifest/
  v1.NN_manifest.json               sha256 of every artifact in that version
audits/
  YYYY-MM-DD-vNNN-<kind>.html       adversarial audit passes
log/
  RH_G1_G2_research_log.md          cumulative research log
  v1_revision_notes.md              per-version notes
tools/
  make_manifest.py                  regenerate a version manifest
  verify_manifest.py                check artifacts against a manifest
```

### The one rule that matters

**Evidence is incremental, never cumulative.** `evidence/vNNN/` contains
only what that version added. Git already stores history; re-bundling every
prior artifact into each release is what produced a 207 MB ZIP that failed
to upload with an HTTP 502 and left the complete lambda=4 positivity result
unreproducible (see `evidence/MISSING.md`).

No single file may exceed 100 MB — GitHub rejects it outright. The largest
current artifact is ~39 MB, so Git LFS is not yet needed. If a witness ever
approaches the limit, split it or add LFS before committing.

## Tags

One immutable tag per released manuscript version:

```
v1.24  v1.25  ...  v1.37
```

A tag is the answer to "which checkout supports the claim on page N of
version M". Tag at the commit that carries both the manuscript and its
evidence.

## Branches

```
main                     the live manuscript and its committed evidence
lane/<topic>             a long-running research direction
result/<label>           one numbered result and its evidence
audit/<date>-v<version>  an audit pass
restructure/<topic>      repository maintenance
```

### `lane/` — research directions

A lane is a line of attack that outlives any single result. Lanes branch
from `main` and are long-lived. Current and recent lanes:

```
lane/concentration     the live signed weighted concentration mechanism
lane/bounded-floor     the v1.36 uniform-floor reduction and its physical test
lane/odd-sector        odd-parity obligations
lane/window-scaling    behaviour of certificates as lambda grows
```

### `result/` — one proposition at a time

A result branch carries a single numbered proposition together with the
evidence that establishes it, named after the manuscript label so the two
are searchable together:

```
result/v137-scalar-no-go        -> cor:v137-scalar-no-go
result/v136-bounded-floor       -> prop:v136-bounded-floor
result/v126-direction-complement-> prop:v126-direction-complement
```

Branch a `result/` from its `lane/` when it belongs to a direction, or from
`main` when it stands alone. Merge it into the lane, then the lane into
`main` when the manuscript version is cut. That is the "subbranch" structure:
`main <- lane/<topic> <- result/<label>`.

### `closed/` — retired routes are results too

Roughly ten routes to a uniform estimate have been proved closed. These are
the project's main publishable output and must stay findable. When a route
is closed, keep its `result/` branch and tag it:

```
closed/scalar-primitive     cor:v137-scalar-no-go
closed/block-metric         v1.28
closed/scalar-far-majorant  prop:v125-cutoff-cost
closed/schatten             prop:v132-schatten
closed/reciprocal-band      v1.33
closed/cotlar-atomization   v1.34
```

Do not delete a branch whose route was closed. A closed route with its
certificate is a contribution; an orphaned commit is not.

## Parallel work with worktrees

Multiple lanes can be checked out at once without stashing:

```sh
git worktree add ../riemann-worktrees/concentration lane/concentration
git worktree add ../riemann-worktrees/audit         audit/2026-09-21-v134
git worktree list
git worktree remove ../riemann-worktrees/audit
```

Each worktree is a real working directory on its own branch sharing one
object store. This matters here because several agents and people push to
this repository concurrently; a worktree per lane prevents the mid-run
branch switches that corrupt long interval-arithmetic computations.

## Committing a new version

1. Put new artifacts in `evidence/vNNN/` — only what is new.
2. `python3 tools/make_manifest.py vNNN`
3. `python3 tools/verify_manifest.py vNNN`
4. Update `log/` and, if a gap closed, `evidence/MISSING.md`.
5. Commit, then `git tag v1.NN`.
6. `git push origin main --tags`

## Claim discipline

The manuscript distinguishes exact identities, proved implications with
explicit hypotheses, failed approaches, numerical illustrations, and open
inputs. The repository must not blur that: a numerical diagnostic goes in
`evidence/`, never in `manifest/` as though it were a certificate, and an
artifact that is cited but absent goes in `evidence/MISSING.md` rather than
being quietly omitted.
