# v1.44 — NS-24: weighted concentration on the level pencil

**Exact identities and proved implications with explicit hypotheses.**
No numerical experiment or new certified numerical bound is claimed.
G2 and RH remain open. The v1.43 enclosure is unchanged.

At a fixed window, define the minorant loss
`L_a[f] = integral (beta_a - m_a) |Fourier(f)|^2`, where
`m_a = -D_a + sum w_j 1_Gj <= beta_a`. For each source-admissible exact
pencil vector, the weighted concentration test is exactly

    L_a[v_k]/q_a^+[v_k] <= nu_k + eta_a ||v_k||^2/q_a^+[v_k].

At eta_a=0 the relative loss allowance is nu_k. With allowed negative
error, the eta term must be retained. Small nu_k alone does not refute
the weaker bounded-error goal or force relative accuracy nu_k.

The diagnostic uses the uncompressed 49-dimensional even head (N=48).
It does not establish source orthogonality. In exact pencil coordinates,
write R for the loss Gram, G for the ordinary Gram, and b_k=<v_k,u_a>.
The entire admissible head requires `diag(nu)-R+eta_a G >= 0` on `ker b`.
Diagonal tests alone miss cross terms. Projecting raw vectors changes their
ratios. If the first twelve exact values were below 1e-8, their span would
contain at least eleven source-admissible dimensions with ratio below 1e-8;
the reported threshold remains diagnostic, not a verified hypothesis.

These are single-window head statements. The live sufficient criterion
still requires the complete source complement on a cofinal family with
uniform errors: eta_a -> 0 in v1.31, or uniformly bounded errors in both
parities with the residual/coupling hypotheses of v1.36. No such estimate,
minorant construction or transfer from the finite head is supplied. This
is a quantifier finding, not a failure of the criterion or the object.
The task stops here as requested.

## Files

- `pencil_concentration.tex`: the exact proposition and proof integrated in the manuscript.
- `scope_review.md`: source-admissibility, cross-term and quantifier checks.
- `provenance.json`: hashes of the existing diagnostic; no diagnostic was rerun.
- `build_report.json`: actual full-manuscript build and source hash.
- `research-report-2026-09-21-v2.html`: current styled user-facing report (NS-24).
- `research-report-2026-09-21-v1.html`: preserved report before task-ID reconciliation.

The diagnostic citation is `evidence/diag_true_symbol/results.md`, section 7,
with `pencil.py` and `pencil_output.txt`. Its lambda=4 N=48 figures (twelve
nu_k below 1e-8, nu_0 about 2.9e-65) are numerical illustrations only. The
positive/negative forms in the proposition are exact complete Fourier
integrals, not their floating-quadrature approximations.

No new window, tail metric, numerical run or zero-enclosure refinement.
The two NS-1 evidence gaps remain OPEN. This translation does not recover
the missing v1.31 scripts or certify the old concentration diagnostics.

Verify and build from the repository root:

```sh
python3 tools/verify_manifest.py v144
./manuscript/build.sh
```
