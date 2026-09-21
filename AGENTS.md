# Instructions for agents working in this repository

This file is for AI agents (Astra, Claude, or any other) contributing to this
project. Humans should read `REPO_LAYOUT.md` and `RESEARCH_MAP.md` instead.

Read this file before your first commit. It encodes failure modes that have
already cost this project real work.

---

## 1. What this project is

A research record for an attempt on the Riemann Hypothesis via Weil
positivity on semilocal Weil forms, following Burnol's Sonine spaces.

**RH is not proved. G2 is not proved. Nothing here claims otherwise.**

The complete semilocal Weil form at window lambda=4 is nonnegative in both
parity sectors. Version 1.40 additionally certifies its simple even ground
and, by Connes–van Suijlekom Theorem 6.1, real zeros of the ground's entire
Fourier transform. These are fixed-window results; convergence to Riemann's
Xi remains unproved. Roughly ten scoped no-go results also close proposed
routes. Treat a proved closure as a contribution, not a setback.

---

## 2. Claim discipline — the non-negotiable part

Every statement must be filed as exactly one of:

| Category | Standard |
|---|---|
| exact identity | algebraic, checkable |
| proved implication | hypotheses stated explicitly, in full |
| numerical illustration | not proof evidence; label it so |
| certified computation | interval/ball arithmetic, replayed at two precisions |
| open input | named, with what is missing |

Specific rules:

- **Never** claim RH, G2, positivity transfer, or publication readiness.
- A failed sufficient criterion is **not** a negative Weil direction. Say
  which one you mean.
- A floating-point residual is not a certificate. Replaying an analytic or
  interval inequality is.
- An LDL pivot is a **coordinate** quantity, not an ordinary spectral gap.
- If you write "therefore", check that the cross terms are controlled.
  Positivity on a subspace plus positivity on a complement does **not** give
  positivity on the span unless the complement is orthogonal in the right
  metric and the cross term is handled. See `prop:v126-direction-complement`
  for the correct pattern.

---

## 3. Four facts that stop wasted work

**3.1 Finite windows do not accumulate.** `prop:v121-cofinal-rh`: RH follows
from a *cofinal* family with error tending to zero. No finite list of
certified windows — however long — contributes anything. Computing lambda=5,
then 6, then 8 is not progress toward G2 unless it tests a stated prediction.

**3.2 The target is now weaker than "decay".** `prop:v136-bounded-floor`: a
*uniform finite floor* `q_a >= -C_* ||f||^2` with `C_*` independent of `a`
already suffices. You do not need to prove the error vanishes. Check whether
your estimate meets this weaker bar before abandoning it.

**3.3 Windows cost exponentially.** `prop:v125-cutoff-cost` proves the remote
cutoff satisfies `N+1 > L exp(M_phi/(1-c))` with `M_phi/lambda -> 1`:

```
  lambda      4      5       6        8         12        16
  cutoff N    283    1502    7488     124442    ~2.6e7    ~5e9
```

Do not attempt lambda >= 8 without a specific reason. The method's ceiling is
near lambda = 10-12.

**3.4 "Margin" names two different quantities.** They are not comparable.

```
  certificate margin   1 - lambda_max(U, K)              does the gate pass
  resolution margin    m(M1,M2) = min (x*S_M2 x)/(x*S_M1 x)   energy lost between cuts
```

Resolution margins at different lambda **cannot be ordered** — they belong to
different operators. Always state which you mean.

---

## 4. Numerical standards

- **Interval/ball arithmetic only** for anything entering a proof. Arb via
  python-flint. Replay every gate at **two precisions**.
- **Never use an uncertified midpoint solve** in a proof path.
  `Z = T.solve(B).mid()` discards error bounds; against `cond(T) ~ 1e170` the
  result is noise. This has produced numbers wrong by 67 orders of magnitude
  at 768 bits that looked entirely plausible and threw no error.
- **768 bits is not safe** at lambda >= 6. Verify precision-stability by
  recomputing at a higher precision and confirming the value is unchanged.
  Two precisions agreeing is necessary, not sufficient — check cutoff
  stability separately.
- **Changing the cutoff changes the finite problem.** Variation across cutoffs
  is expected and is not by itself an error signal. Variation at *fixed*
  problem size across precisions **is**.
- A proposal step needs no rigor; only verification does. Say which is which.

---

## 5. Where things go

See `REPO_LAYOUT.md` for the full scheme. The short version:

```
manuscript/   one live .tex; build with ./manuscript/build.sh
evidence/vNNN ONLY what that version adds -- never cumulative
manifest/     sha256 per version
audits/       adversarial passes
log/          research log, revision notes
tools/        make_manifest.py, verify_manifest.py, make_map.py
```

**Do not build cumulative bundles.** Re-bundling every prior artifact into
each release produced a 207 MB ZIP that failed to upload (HTTP 502) and left
the project's only positive result unreproducible. Git stores history; use it.
No file over 100 MB — GitHub rejects it.

**If you cite an artifact, commit it.** If you cannot, add a row to
`evidence/MISSING.md`. Never let the manuscript imply an artifact is archived
when it is not. This is currently an open audit finding (MAJOR M1).

**Before starting any task, claim it in `NEXT_STEPS.md`** — write your name
in the `owner` column in its own small commit, then work. Two agents push
here concurrently; an unclaimed task gets done twice. Add a row for anything
not listed; never delete rows; record the version that finished a task.

**Diagnostics that are not certificates** go in `evidence/diag_<topic>/` with
a `results.md` whose first line says so. They may use midpoint eigenvalues,
float scans or uncertified solves — but only under that label, never under
`evidence/vNNN/`, and never cited as a bound.

After adding evidence:

```sh
python3 tools/make_manifest.py vNNN
python3 tools/verify_manifest.py vNNN
```

After changing the research map, regenerate it:

```sh
python3 tools/make_map.py          # updates RESEARCH_MAP.md
```

---

## 6. Branches

```
main                     live manuscript and committed evidence
lane/<topic>             a long-running research direction
result/<label>           one numbered result plus its evidence
closed/<route>           a route proved closed -- keep it, never delete
audit/<date>-v<version>  an audit pass
```

Nest as `main <- lane/<topic> <- result/<label>`. Name `result/` branches
after the manuscript label (`result/v137-scalar-no-go`) so the branch and the
proposition are searchable together. Tag one `v1.NN` per manuscript version.

Several agents push here concurrently. Use a worktree per lane rather than
switching branches in place — a mid-run branch switch corrupts long interval
computations:

```sh
git worktree add ../riemann-worktrees/<name> lane/<topic>
```

---

## 7. Pushing to GitHub

The repository is **public**: `github.com/AlexanderEastwood/riemann`.
Anything you push is visible immediately and permanently.

### Authentication

Push access belongs to the **AlexanderEastwood** account. Other accounts on
this machine have read access only and will fail with `403`:

```sh
gh auth status                                              # which accounts exist
gh auth switch --hostname github.com --user AlexanderEastwood
git push origin <branch>
gh auth switch --hostname github.com --user <previous>      # switch back
```

Set the commit identity **per repository**, never globally — a work email on
a public personal repo is a leak:

```sh
git config user.name  "Alex Eastwood"
git config user.email "30302255+AlexanderEastwood@users.noreply.github.com"
```

**Never put a token in a remote URL.** Use `gh` or a credential helper.

### The push sequence

```sh
./manuscript/build.sh                       # must build before you push
python3 tools/verify_manifest.py vNNN       # artifacts must verify
git fetch origin && git rebase origin/main  # others push here concurrently
git push origin main
git tag v1.NN && git push origin v1.NN      # one tag per manuscript version
```

### Hard rules

- **Never force-push `main`.** It is public and other agents branch from it.
  If you need to discard something, revert it.
- **Never rewrite published history.** Force-pushed commits stay reachable by
  SHA on GitHub anyway, so a rewrite destroys local recoverability without
  actually removing anything from the remote.
- **Never delete a `closed/` branch or a version tag.**
- **Nothing over 100 MB**, ever. GitHub rejects it outright and the push
  fails after transferring everything. 50 MB triggers a warning.
- Rebase before pushing. Several agents push to this repository, sometimes
  minutes apart.
- If you are mid-restructure or doing anything wide-reaching, **work on a
  branch** and let a human merge it. Do not reorganize `main` underneath
  someone else's in-flight work.

---

## 8. Common failures

Observed in this project. Check here before debugging from scratch.

| Symptom | Cause | Fix |
|---|---|---|
| `Permission to ...denied` / `403` on push | wrong `gh` account active | `gh auth switch` to AlexanderEastwood |
| Push rejected, file too large | a cumulative bundle was committed | commit artifacts **unpacked and incremental**; gitignore the archive |
| `HTTP 502` uploading a release bundle | bundle grew past what the endpoint accepts | stop bundling; use `evidence/vNNN/` |
| `fatal: 'origin' does not appear to be a repository` | fresh `git init` dropped the remote | `git remote add origin <url>` |
| Manuscript claim has no artifact behind it | evidence generated but never committed | commit it, or add a row to `evidence/MISSING.md` |
| Value changes by tens of orders of magnitude between 768 and 2048 bits | uncertified midpoint solve at high condition number | certified interval solve; replay at two precisions |
| `singular matrix in solve()` | precision too low for `cond(T)`, **or** head too small so the deep block sits in the tail | raise precision; scale the head as `N ~ lambda^2` |
| Finite-section result moves across cutoffs | expected — a different cutoff is a different finite problem | not an error; do not report it as one |
| Two "margins" disagree across versions | certificate margin vs resolution margin | state which; they are not comparable |
| Manifest verification reports `RELOCATED` | manifest predates a reorganization | expected; regenerate with `make_manifest.py` |
| Manifest reports `MISMATCH` on a file you edited | the manifest is stale | regenerate for that version |
| Gate passes but the conclusion does not follow | positivity combined across subspaces without the cross term | use the `prop:v126-direction-complement` pattern |
| A new version records only a failure | normal and correct here | publish it; do not pad it |

---

## 9. Reporting

When you are given an experiment, run **that** experiment. If you substitute a
cheaper diagnostic, say so explicitly and in the first sentence. Reporting a
different quantity as though it answered the question has happened more than
once and cost a full cycle each time.

When something fails, report:

1. **what had to change** — if a construction transfers only with
   modification, the modification is the finding, not a footnote;
2. the obstruction, precisely, rather than a substitute result;
3. whether the failure is of the *bound* or of the *object* — a true
   inequality that a certificate cannot see is not the same as a false one.

"Source validation passed" is not a build. Run `./manuscript/build.sh` and
report the page count and the undefined-reference count.

Do not produce a new version number to show motion. A version that only
records a failure is fine and normal here. A version that overstates is not.
