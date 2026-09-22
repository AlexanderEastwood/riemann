# v1.48 — NS-30: level-measure-weighted form of the level-count bound

**One proved implication with explicit hypotheses, and a re-shaping of two
named open inputs. No new numerical certificate. G2 and RH remain open.**

`prop:v148-weighted-levels`: if a unit source-admissible packet g has level
mass mu_g(B) >= c' m~(B) for every Borel set B of symbol levels in [-D, 0],
where m~ is the symbol's own normalized level distribution on the head range
[0, X], and q_a[g] <= Q, then every step minorant with at most K distinct
values loses at least

    eta(m) >= [ c' QC_K(m~) - Q ]_+,

QC_K(m~) being the one-sided K-level quantization cost of m~ (eq:v148-qc),
with QC_K(m~) >= h phi_-^2 / (2 K M(h)) - (3/2) h phi_- for every h, M(h) the
concentration function (largest mass of an interval of levels of length h).
Under a bounded density this gives phi_-^2/(2K sup rho), and under uniform
density exactly eq:v146-level-lower with c = c' phi_-. The arithmetic level
measure does NOT have a bounded density (it diverges like an inverse square
root at every trough level; Astra's review of the first draft caught this),
so the concentration function, not a sup-density, is the finite substitute.

What changes: the zero-distribution input ZLD (ass:v147-zld, a lower bound
on every level band) is replaced by growth of the quantization cost of the
level distribution, sharpest as QC_1(m~) = phi_- D - mean(beta_a^-) -> infinity
with K QC_K >= kappa_0 QC_1, or more crudely through the concentration function; the packet-coverage input (coverage of every band with
bounded energy) is replaced by the existence of one admissible state whose
level mass is at least a fixed multiple of the symbol's own level
distribution. Both remain open inputs. The gain is in shape, not in proof.

Why the shape matters (diagnostic, `evidence/diag_level_distribution/`,
sections 4-6, even head N=256, float): the uniform hypothesis with c = 0.3
costs a minimum energy 5e-4 / 1e-3 / 0.29 / 0.13 at lambda 3/4/6/8, so
eq:v146-level-lower reaches only K <= 2 (lambda 6) or 7 (lambda 8) levels;
the weighted hypothesis with c' = 1 costs 2e-9 / <1e-15 / 1.8e-3 / 5e-5 and
c' QC_K(m~) - Q stays positive for hundreds to thousands of levels. The
measured QC_1(m~) is 0.084, 0.22, 0.65, 0.94 and K QC_K / QC_1 ~ 0.55 for K <= 32. These numbers
are illustrations; the source constraint is not imposed on the LP states.

Files: `weighted_levels.tex` (the integrated text), `build_report.json`,
`provenance.json`. The route stays blocked, not closed.
