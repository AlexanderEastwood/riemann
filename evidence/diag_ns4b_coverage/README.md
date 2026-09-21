Analysis (coverage table); not a certificate.

# `evidence/diag_ns4b_coverage/`

NS-4b (2026-09-21). Maps each of the ten closed routes under "Uniform mechanism for G2"
in `RESEARCH_MAP.md` to the two v1.39 meta-obstructions `thm:v139-probe-relaxation` (A)
and `thm:v139-protected-orbit` (B), by checking each theorem's hypotheses against the
closure's actual proposition, and checks that the live mechanism
`prop:v131-concentration` is outside both classes.

Result: (A) covers 1 of 10 (scalar signed primitive); (B) covers 0 of 10 cleanly
(it covers the pointwise-minimum estimator, which is not one of the ten); 9 are
neither; the concentration route violates (A2) probe inclusion and (B3) orientation
universality. Consistent with the manuscript's own scoping sentence (v1.40 lines
10616–10623) and with `evidence/v139/adversarial_review.md` §6–7, with hypothesis-level
justification and line references added.

No new computation. No G2 or RH claim. `manuscript/*.tex` is not modified.

## Files

- `coverage.md` — the table, hypothesis-by-hypothesis justifications, the concentration
  check, and the reading of `prop:v139-location-counterexample`.
- `coverage_insert.tex` — LaTeX draft (table + paragraph) with the suggested insertion
  anchor marked in the header comment. Test-compiled against a scratch copy of the v1.40
  manuscript; not inserted.
