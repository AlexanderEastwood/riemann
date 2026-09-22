# v1.49 — PR #14 audit and the exact weighted zero input

**Exact identities, proved implications and countermodels, plus named open
inputs. No new numerical experiment or certificate. G2 and RH remain open.**

Task A is NS-32 after a concurrent task-ID reconciliation. PR #14 at 9b2b900
is left unmerged for three MAJOR findings: the false “exactly when” claim;
identification of a finite histogram peak with the continuous density cap;
and the claimed cheap lambda=4 c'=1 state, whose saved bin ratio is only
0.636. Its main weighted-cost implication, monotonicity argument, measure
domination step and uniform-density constant pass. The exact PR head builds
to 238 pages with 0 undefined/duplicate references; all four artifacts verify.
The versioned audit is `audits/2026-09-21-v1.48-pr14-v2.html`.

Task B is NS-33. The v1.49 manuscript is based on v1.47 main and is
self-contained: it does not merge the rejected v1.48 wording. Its findings:

- The exact normalized level density is X^-1 times the sum of inverse
  slopes of the complete corrected zero field at every level preimage.
  A negative critical value produces an integrable but unbounded density;
  the continuous peak is infinite whenever the stated geometric condition
  holds. The finite histogram's maximum near zero is not that peak.
- If the peak R is finite, phi^2/R diverges exactly when R=o(phi^2).
  Since phi<=1, R must tend to zero. Bounded above alone does not prevent
  divergence; uniform density phi/D is an example. The critical-level
  singularity, not bounded phi by itself, makes the crude bound vacuous.
- ZLD's lower band bound and a peak-density upper bound do not imply each
  other for general level measures. No arithmetic independence is claimed.
- The exact weighted bound eta >= [c' QC_K - Q]+ requires no bounded
  density. The density packing estimate is retained conditionally, and
  uniform density recovers c=c'*phi exactly.
- QC_1 = phi*D - mean(beta^-) is the averaged gap above the deepest negative
  value. Its growth alone is insufficient: an absolutely continuous,
  full-support countermodel has QC_1~D/2 but QC_2->0.
- The named input **Exact Level Quantization Growth (QG)** requires QC_K
  to diverge for every fixed K on a prescribed cofinal head-size family.
  It also requires separate admissible bounded-energy packets satisfying
  all-Borel weighted domination. A QC_1/K bound is a further shape
  hypothesis, not a consequence of one-level growth.

Neither a positive limit nor decay of phi follows from the cited depth
corollary. No cofinal input is proved. The route remains blocked; the
physical form and the valid weighted concentration criterion are not refuted.

No source-projection calculation was run. The audit names the missing
lambda=3 overlap, complete-energy/cross-term and projected-constraint
checks; a small source residual alone gives no constant-factor guarantee.
NS-28 raw scripts and outputs are unchanged; its report gets a correction
notice, preserving the original text below it.

## Incremental record

- `weighted_zero_input.tex`: self-contained manuscript insert.
- `scope_review.md`: internal mathematical and claim audit.
- `provenance.json`: reviewed PR head, archived source/input hashes.
- `build_report.json`: actual final v1.49 build and reference counts.
- `pr14_build_report.json`: actual independent PR #14 build.
- `research-report-2026-09-21-v1.html`: user-facing report for both tasks.

The two NS-1 evidence groups remain OPEN. No new window, head run,
tail metric, optimization or zero enclosure. No v1.48 merge/tag.
