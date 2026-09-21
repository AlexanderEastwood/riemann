# External audit - fixed_space_prime_action, r11

Date: 2026-09-19
Auditor: external review pass (independent re-derivation, not expert referee report)
Subject: `fixed_space_prime_action.tex` / `.pdf` (r11, 89pp), with `_copy` (87pp) and `_latest` (65pp) as comparison sources, plus `AUDIT_G1_G2_2026-09-19.md`

## Status

This audit **does not find an error that invalidates the manuscript's stated claims**. It confirms four load-bearing algebraic results by independent derivation, confirms the manuscript is mechanically clean, and finds one prose/support mismatch that should be repaired before the document is shown to anyone, plus one structural risk that should be closed by an explicit lemma.

The manuscript's self-assessment - that this is **not a proof of RH** - is accurate and is stated with unusual discipline. Nothing in this audit contradicts it, and nothing in this audit brings the document closer to an RH proof.

## Scope: what was and was not checked

**Checked in full, by independent re-derivation:**

- the Run-8 exact CCM coefficient identity (`prop:beta-arithmetic-channel`);
- the Run-10 endpoint/PNT threshold disjointness;
- the Run-11 continuum normal form `prop:boundary-test-normal-form` (`alpha_infinity`, bracket vanishing at `s=sigma`, reflected-pole residue);
- the Run-11 bounded-filter no-go inequality `prop:bounded-filter-no-go`;
- the boundary-quotient invariance algebra (both the even/same-endpoint form and the Run-9 projective form).

**Checked mechanically, across all three sources:**

- label/reference integrity, duplicate labels, dangling references, rendered `??` in output PDFs;
- placeholder and overstatement scan;
- version lineage and content diff.

**Not checked.** The bulk of the 89 pages was not verified. In particular this audit makes no statement about the correctness of: the PSWF/prolate cross-tail estimate chain (`thm:lattice-tail`, `cor:pswf-cross-tail`), the Sobolev continuum estimate `prop:g1-sobolev`, the periodization strip error estimates, the `W^2` coercivity proposition `prop:simple-reflected-w2`, the Jordan-block transport in `prop:multiple-reflected-block`, or the use of the Connes-Consani trigonometric union as a form core. Those require a subject-matter referee. What follows is a bound on confidence, not a clearance.

## 1. Version control (fix first)

| file | pages | timestamp | md5 (short) |
|---|---|---|---|
| `fixed_space_prime_action.pdf` | 89 | 05:56 | `d6341a4b` |
| `fixed_space_prime_action_g1g2_2026-09-19_r11.pdf` | 89 | 05:56 | `d6341a4b` |
| `fixed_space_prime_action_copy.pdf` | 87 | 05:00 | `48c6adfd` |
| `fixed_space_prime_action_latest.pdf` | 65 | 02:31 | `9b178cb8` |

Findings:

- `.pdf` and `_g1g2_..._r11.pdf` are **byte-identical**. One is redundant.
- `_latest` is the **oldest** file in the set, by three and a half hours and 24 pages. The name is inverted.
- Lineage by label-set inclusion is `_latest` -> `_copy` -> `.tex` (r11).

Action: adopt `fixed_space_prime_action_rNN_YYYY-MM-DD.{tex,pdf}` as the only naming scheme, delete `_latest` and `_copy` or move them to an `archive/` directory, and never ship a file called `latest`.

## 2. Results confirmed by independent derivation

### 2.1 Run-8 CCM coefficient identity - CORRECT

The claim is that the direct point+prime+archimedean formula for `b_lambda(n)` equals the centered-discrepancy formula.

Reconciling the two forms requires exactly

`PointTerm = -(1/pi) int_0^L (e^(y/2) + e^(-y/2)) sin(t_n y) dy`.

Evaluating (Appendix A) gives

`32 L n sinh^2(L/4) / (L^2 + 16 pi^2 n^2)`,

which is the manuscript's displayed point term, exactly. The integration-by-parts boundary term vanishes identically.

Numerical confirmation: agreement to `~1e-15` across `L in {2.9, 3.7, 4.3, 5.1, 6.4}` and `n in {1, -2, 3, 2, -5, 7, -11}` (Appendix B). Naive quadrature gives residuals of order `1e-4` and looks like a failure; it is not, it is the prime step function defeating adaptive quadrature. Anyone re-checking this needs the piecewise method or they will report a false error.

**Required hypothesis, currently implicit.** The boundary term vanishes only because `t_n L = 2 pi n` with **n an integer**. The identity is false for non-integer index. The manuscript should state `n in Z` at the point of use. The existing audit note says "positive/negative Fourier indices," which is consistent but not explicit.

### 2.2 Run-10 threshold disjointness - CORRECT

With `q = sigma - 1/2`:

`1/(2 sigma) - d/(d+q) = q(1-2d) / ((d+q)(2q+1))`,

which is positive iff `d < 1/2`. The moving-phase route is genuinely closed for every nontrivial off-line zero. No gap.

### 2.3 Run-11 continuum normal form - CORRECT

Endpoint annihilation `delta(v-) - alpha_infinity delta(v+) = 0` forces

`alpha_infinity = ((sigma-rho)/(sigma-rho#))^m`

exactly as displayed. Substituting back, the bracket

`alpha_infinity/(s-rho)^m - 1/(s-rho#)^m`

vanishes at `s = sigma`, cancelling the simple Cauchy pole of `kappa`. At `s = rho` the order-`m` zero of `zeta` cancels the apparent pole. At `s = rho#` exactly one power survives, giving

`Res = -kappa(rho#) zeta^(m)(rho#)/m!`.

All correct.

One step is used without comment and is worth a sentence in the text: the argument needs `rho#` to have multiplicity **exactly** `m`. That follows from the functional equation plus `zeta(conj s) = conj zeta(s)`, so it is free, but a referee will look for it.

### 2.4 Run-11 bounded-filter no-go - CORRECT, with a scope note

`|conj(Phi(rho)) Phi(rho#)| >= c0` and `|Phi(rho)| <= M_L` give `|Phi(rho#)| >= c0/M_L`. Elementary and right.

The manuscript states the necessary hypothesis: `Phi_L` must admit holomorphic continuation to neighborhoods of `rho` and `rho#`. This matters, because `rho# = 1/2 - d + i gamma` lies **outside** `Re s > 1/2`, so `M_L` does not bound `Phi_L(rho#)`. That asymmetry is the engine of the argument.

**Discrepancy:** `AUDIT_G1_G2_2026-09-19.md` states this no-go without that hypothesis, and concludes it "closes a broad class of bounded-filter rescue attempts." The proved statement covers bounded filters **analytic across the critical line**. A filter with a natural boundary on `Re s = 1/2`, or defined only on the half-plane, is not covered. Align the audit note with the manuscript's hypothesis.

### 2.5 Mechanical integrity - CLEAN

- 335 labels in r11, **zero duplicates**, **zero undefined references**.
- Zero rendered `??` in any of the four PDFs.
- No `TODO`, `FIXME`, placeholder, or "citation needed" text.
- 16 explicit non-proof / RH-strength disclaimers.
- r11 PDF matches r11 source (the new `prop:bounded-filter-no-go` is present in the output).

## 3. Defect: deleted G1 sub-chain, surviving cofinality claim

`_latest.tex` contains a G1 sub-chain that r11 does not. Approximately twenty labels, including:

- `prop:g1-weighted-sampler` (Cofinal finite G1 bound on a weighted sampler class)
- `lem:g1-jump-train` (Exact arithmetic jump train)
- `prop:g1-jump-split` (Jump/continuous split for the weighted G1 transfer)
- `cor:g1-complete-matrix` (Complete Fourier-matrix bound)
- `cor:g1-jump-natural-scale` (arithmetic jumps resolvable at near-Slepian scale)

These are deleted in `_copy` and absent from r11, with no replacement proposition.

The strength difference is material:

- **deleted** `prop:g1-weighted-sampler`: uniform. "Let `R>3`, let `K >= 2N` ... If `N >= 2L`, then ..." with an explicit bound. Quantified over **all** ambient cutoffs `K >= 2N`.
- **surviving** `prop:g1-full-hardy-pairing`: existential. "There are core cutoffs `N_c(lambda) -> infinity` and ambient sampler cutoffs `K(lambda) >= 2N_c(lambda)`, which may be enlarged ..."

But the r11 prose was not updated to match. The Claim Discipline section still asserts decay of the literal `D_log W k` pairing "against the full smoothed Hardy sampler **on a common cofinal finite diagonal**," and line 5590 still says "after a **cofinal** finite transfer."

Cofinality for the **full smoothed Hardy sampler** is no longer proved anywhere in r11. `prop:finite-g1-transfer` supplies cofinality only for the unmodified Fourier projection, which the manuscript itself concedes at line 2406 ("the set of acceptable cutoffs is eventually cofinal" - stated there specifically about the unmodified Fourier projection).

This is the single most exposed item in the document. Resolve it one of two ways:

1. **The deletion was deliberate** (superseded by the VP-filtered transfer plus exact-boundary shell route). Then downgrade the two prose claims from "cofinal" to "a diagonal," and state plainly that cofinality for the full Hardy sampler is not claimed in r11.
2. **The deletion was accidental.** Then restore the sub-chain from `_latest.tex` and re-check that its proof still matches r11's current definitions of `k^VP` and the Hardy sampler.

Either is fine. Shipping with the current mismatch is not: a referee who finds an unsupported "cofinal" will discount the rest of the document, including the parts this audit confirmed.

## 4. Structural risk: diagonal quantifier bookkeeping

The architecture is a hoped-for contradiction between a G1 upper bound and a G2 lower bound **on one common finite object**. That makes diagonal selection load-bearing, and r11 now carries at least four independently chosen diagonals:

1. `thm:off-line-form-transfer`: `N(lambda)` chosen **after** `lambda`, large enough that the finite-section form error is at most `1/lambda`. The proof states explicitly "No uniform Galerkin rate in `lambda` is required."
2. `prop:g1-full-hardy-pairing`: `(N_c(lambda), K(lambda))` with `K >= 2N_c`, "which may be enlarged to satisfy the G2 form transfer simultaneously."
3. `cor:beta-critical-scale`: the `sqrt(L) <beta_log, vtilde_m>` limit.
4. `prop:multiple-reflected-block`: the block mismatch limit.

Each is phrased as an existence statement with a licence to enlarge. Enlargement is not free. An estimate that needs `K` large and an estimate that needs `K` controlled relative to `L` conflict without either statement looking wrong in isolation, and the conflict would be invisible in the current presentation because no single object carries all four conditions.

Recommendation: add one **diagonal selection lemma** that fixes a single sequence `(lambda_j, N_c(lambda_j), K(lambda_j))` and re-states all four results on that sequence, with the compatibility conditions shown to be simultaneously satisfiable. If they are simultaneously satisfiable this is a page of bookkeeping and it removes the largest remaining place an error could hide. If they are not, that is a finding worth more than the rest of r11.

## 5. Minor

- The status box is a single ~300-word prose block. For a referee, break it into the three established components and the one open target as an enumerated list. Content is fine; the format buries it.
- 54 source lines exceed 400 characters. Cosmetic, but it makes diffs between runs nearly unreadable, which is plausibly how the G1 sub-chain in section 3 went missing without being noticed.
- 82 labels in r11 are defined and never referenced. Harmless, but some are probably orphans left by the same deletion.

## 6. Recommended order of work

1. Resolve the cofinality mismatch (section 3). Blocking.
2. Fix file naming and delete the duplicate PDF (section 1). Five minutes.
3. Add `n in Z` to the CCM coefficient identity (section 2.1). One line.
4. Align the audit note's filter no-go with the manuscript's analyticity hypothesis (section 2.4). One sentence.
5. Add the multiplicity-of-`rho#` remark (section 2.3). One sentence.
6. Write the diagonal selection lemma (section 4). The real work.

## Bottom line

The verified components hold up. The four results re-derived here are correct as stated, the document is mechanically clean, and the claim discipline is the strongest feature of the package and should not be softened.

The manuscript's own assessment of where it stands is accurate. r11's contributions are negative results - genuinely narrowing, correctly reasoned, and not closer to a proof in the sense that matters. By the manuscript's own `prop:pnt-beta-barrier` the unsigned PNT route is dead, which leaves signed prime correlation against a specific Hardy kernel as the active target. That is not a step down in difficulty from the original problem, and the document is right to say so rather than dress it as a remaining technicality.

The two items that would cost credibility fastest with an expert reader are the version chaos and the unsupported "cofinal." Both are cheap to fix. Fix them before anyone else reads this.

---

## Appendix A: point-term derivation

With `V(y) = 2(e^(y/2)-1) - P(y)`, `P(y) = sum_{k<=e^y} Lambda(k)/sqrt(k)`, and `t_n = 2 pi n / L`:

Since `sin(t_n L) = sin(2 pi n) = 0` and `sin(0) = 0`, integration by parts has no boundary term:

`int_0^L sin(t_n y) dV(y) = -t_n int_0^L V(y) cos(t_n y) dy`.

Hence the direct formula's prime sum satisfies

`(1/pi) int sin dP = (1/pi) int_0^L sin(t_n y) e^(y/2) dy + (t_n/pi) int_0^L V cos(t_n y) dy`.

Matching against the centered formula, whose archimedean term differs by `(1/pi) int_0^L e^(-y/2) sin(t_n y) dy`, the two forms agree iff

`PointTerm = -(1/pi) int_0^L (e^(y/2) + e^(-y/2)) sin(t_n y) dy`.

Using `int_0^L e^(ay) sin(by) dy = [e^(ay)(a sin by - b cos by)/(a^2+b^2)]_0^L` with `b = t_n`, `cos(t_n L) = 1`:

- `a = 1/2`: `-t_n (e^(L/2)-1)/(1/4 + t_n^2)`
- `a = -1/2`: `t_n (1 - e^(-L/2))/(1/4 + t_n^2)`

Sum: `-t_n (e^(L/2) + e^(-L/2) - 2)/(1/4 + t_n^2) = -4 t_n sinh^2(L/4)/(1/4 + t_n^2)`.

Therefore `PointTerm = 4 t_n sinh^2(L/4) / (pi (1/4 + t_n^2))`, and substituting `t_n = 2 pi n/L`:

`PointTerm = 32 L n sinh^2(L/4) / (L^2 + 16 pi^2 n^2)`.

Matches the manuscript exactly.

## Appendix B: numerical protocol

Adaptive quadrature on `int_0^L V(y) cos(t_n y) dy` fails because `V` is a step function with jumps at `y = log k` over every prime power `k <= e^L`. Residuals of order `1e-4` to `1e-6` are quadrature artifacts, not disagreement.

Correct method: split `V` into its smooth part `2(e^(y/2)-1)`, integrated in closed form, and the step part `P(y)`, integrated exactly as a finite sum over the intervals between consecutive prime-power jump points. Only the archimedean integral needs numerical quadrature.

With that method, direct and centered formulas agree to `4e-17` to `6e-15` across the tested `(L, n)` grid, residual consistent with double-precision accumulation over the prime sum. This supports the manuscript's reported `1e-17`-`1e-19` agreement.
