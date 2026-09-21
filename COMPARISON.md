# Where the certified window sits relative to published work

This file exists because the manuscript's window parameter `lambda` is not
the parameter used in the published literature, and a referee cannot tell
from either side whether the `W_4 >= 0` certificate is beyond or inside
the published state of the art. The translation below settles it.

Only published (arXiv) prior art is compared here. Self-published and
repository-only work is deliberately excluded.

## The translation

The semilocal window `lambda > 1` corresponds to test functions supported
multiplicatively in `[lambda^{-1}, lambda]`, i.e. in the logarithmic
coordinate to support half-width

    a = log lambda

The published literature parameterizes directly by that half-width (Zhu
writes it `L`; the classical Yoshida / Connes–Consani bound is stated as
`supp f ⊂ [-(log 2)/2, (log 2)/2]`). So every result can be placed on one
axis:

| result | half-width `a` | `lambda = e^a` |
|---|---:|---:|
| classical Yoshida / Connes–Consani | 0.3466 | 1.414 |
| Zhu, arXiv:2608.24827, certified `L = 0.8` | 0.8000 | 2.226 |
| this manuscript, `lambda = 3` (`prop:v116-window-positive`) | 1.0986 | 3.000 |
| this manuscript, `lambda = 4` (`W_4 >= 0`, `prop:v126-full-window`) | **1.3863** | **4.000** |

**The `lambda = 4` certificate is at 1.73× the half-width of the
published Zhu window and 4× the classical range.** It is not subsumed on
reach.

The comparison is legitimate because the semilocal form `QW_lambda` and
the global Weil form agree on every test supported inside the window
(`prop:v121-cofinal-rh` relies on exactly this), so the two sides certify
the same object on the same functions.

## What each side establishes — they are not the same strength

| | Zhu (`a = 0.8`) | this manuscript (`a = 1.386`) |
|---|---|---|
| statement | two-sided **quantitative** enclosure `8.9e-18 <= lambda_min <= 2.27e-17` | **nonnegativity of the complete form** `W_4 >= 0`; v1.40 also certifies a simple ground and ordinary gap > `9.7546e-74` |
| parity | both sectors; ground state simple and even | both sectors; complete ground simple and even at lambda=4 (`prop:v140-ground4`), with `0<mu0<2.454e-75`, `mu1>1e-73` |
| method | one-stroke reduction to a single finite PSD matrix | structured inverse, simultaneous 17-column certificate, direction–complement gluing |
| arithmetic | interval | Arb ball arithmetic, 768–1280 bits, two-precision replay |

Zhu supplies an explicit positive lower bound for the ground value on a smaller window.
This manuscript is stronger *in reach*. Neither subsumes the other, and the
manuscript should say so rather than leave it to the reader.

The `LDL*` pivots and the invariant margin `1 - lambda_max(U, K)` recorded in
`evidence/v126/g2_simultaneous/` are **not** an ordinary-norm eigenvalue
bound and must not be quoted as one; see the scope string inside each
certificate JSON.

## Empirical decay comparison: limited scope

The former roughly-20-times comparison used unconverged finite compressions.
It is not a semantic lock and does not determine the complete ground value.
For lambda=4, the quoted empirical prediction 2.07e-73 is more than 84 times
the certified complete-ground upper bound 2.454e-75. For lambda=6 and 8 the
available unconverged compressions cannot test the law. The numerical
comparison does not determine an asymptotic constant.

A separate external numerical benchmark is now available: at the existing lambda=3,
N=120 benchmark, the first eight local transform-zero discrepancies agree
with CCM section 6 Figure 1 at its displayed precision. The first is
approximately 1.582329697193127e-34, matching 1.6e-34. The interval gates replay
at 768 and 1024 bits; see [v1.41](evidence/v141/). This is a finite-compression
reproduction, not a complete-ground or cofinal convergence theorem.

## The one no-go with published prior art

`prop:v125-cutoff-cost` proves the scalar diagonal far majorant needs a
remote cutoff `N+1 > L exp(M_phi/(1-c))` with `M_phi / lambda -> 1`, i.e.
`N ~ exp(e^a)` — doubly exponential in the half-width.

Zhu's abstract states that any one-stroke certificate must resolve
frequencies up to `2 pi e^{A_L}` with `A_L ~ 4 e^L` — the same doubly
exponential shape, drawn as the same conclusion ("why the positivity route
cannot reach RH unassisted"). Groskin, arXiv:2607.02828, gives the
corresponding brute-cutoff cost (`T ~ 10^{63}` at `c = 100`) for
Connes–van Suijlekom truncations, using cutoff-free interval `LDL^T` —
the same factorization technique used here.

The objects differ: Zhu bounds frequency resolution for a one-stroke
certificate; this manuscript bounds the remote cutoff for one specific
scalar majorant, and says explicitly that this is a cost of that majorant
rather than of every possible argument. But the result belongs to a
published family and should be cited as such, not presented as new.

No published prior art was found for: norm contraction
(`prop:v120-norm-counterexample`), Schatten / Hilbert–Schmidt summation
(`prop:v132-schatten`), reciprocal-band approximate commutation (v1.33),
or the unconditional divergence of the scalar signed-primitive budget
(`cor:v137-scalar-no-go`).

## Recommended structural differentiation

The certified-Weil-positivity literature now shares a house style
(certificate-first, "not a proof of RH", scoped no-gos, checksummed
witnesses), so tone does not distinguish this project. Two things would:

1. **The semantic lock is recorded in v1.41.** The unchanged assembler
   reproduces eight CCM §6 Figure 1 discrepancies at lambda=3, N=120,
   with the centering dictionary stated explicitly and interval gates
   replayed at two precisions. This validates this external benchmark;
   it does not audit every archived computation. The zero comparison is
   invariant under A -> c A + s I (c > 0), so it cannot by itself test a
   common positive scalar or an identity shift; full normalization requires
   the separate coefficient identities. The broader 170-value numerical
   reproduction in `evidence/diag_ns2_semantic_lock/` is retained as a
   diagnostic; the eight interval root gates in `evidence/v141/` are the
   certified finite-compression statement.
2. **A named external reviewer** on `evidence/MISSING.md` and the
   certificate ledger. Self-review cannot reach a `REVIEWED` state.

## References

- Zhu, X., *Weil positivity in compact windows: a finite reduction,
  certified two-sided bounds, and a Landau–Widom decay law*,
  arXiv:2608.24827 (2026).
- Groskin, A., *A finite Guinand–Weil dictionary and archimedean tail
  order for the truncated Weil quadratic form*, arXiv:2607.02828 (2026).
- Connes, A., Consani, C., Moscovici, H., arXiv:2511.22755 (2025).
- Yoshida; Connes–Consani — the classical `(log 2)/2` positivity range.

---

## Addendum, 2026-09-21: three more lenses on the same scalar

Three independent route assessments (Connes–Consani–Moscovici's operator
framework, de Branges / Hermite–Biehler theory, and a Toeplitz–Hankel
decomposition of the certified matrix) all land on the same conclusion:
the certified window statements are values of **one scalar**, and every
classical theory names the remaining gap as the same thing.

### In CCM's own notation (arXiv:2511.22755, Cor. 3.7–3.8)

CCM define `μ_λ = inf spec A_λ` for exactly the form `QW_λ` this manuscript
certifies, prove `μ_λ` is decreasing in λ, write *"we cannot assert that
μ_λ ≥ 0"*, and prove `lim μ_λ = 0 ⇒ RH`. Hence, by monotonicity:

    W_4 >= 0   ⟺   μ_λ >= 0  for every  λ <= 4,

replacing "cannot assert" across a range 1.73× Zhu's certified window and
beyond CCM's own λ = 3 numerics. The floors `W_λ >= −8·I` are lower bounds
on `μ_5, μ_6, μ_8`. This is the cleanest positioning statement available and
it is a target statement, not a shortcut: cofinal `μ_λ >= 0` is RH.

NS-5 is now completed in v1.40. The complete ground of `W_4` is
simple, isolated and even, with `0<mu0<2.454e-75`, `mu1>1e-73` and
ordinary gap greater than `9.7546e-74` (`prop:v140-ground4`). The
1024/1280-bit shifted-inertia certificates retain the full tail inverse
change and reuse the archived complete lambda4 Schur bounds. These
figures replace no finite eigenvalue diagnostic: they are bounds for
the complete operator. The earlier eight-order figure concerns the
finite even-sector separation, not the complete global gap.

The precise real-distribution and trigonometric-core hypotheses of
Connes–van Suijlekom Theorem6.1 (arXiv:2511.23257) are verified in
`cor:v140-real-zeros`. Thus `xi-hat_4`, the entire Fourier transform
of the complete ground eigenfunction, has only real zeros. This does
not assert simplicity of those zeros or convergence to Riemann Xi.
See [the proof and certificate](evidence/v140/research_report.md).

### In de Branges / Krein–Langer terms (Suzuki, arXiv:2606.09096)

Suzuki proves unconditionally that at every window, after shifting by any
`μ < λ_a := inf σ(A_a)`, the windowed Weil space is a de Branges space with
real-zero structure functions. The Hermite–Biehler structure therefore
exists whether or not the form is positive; the sign is carried entirely by
`λ_a`, which de Branges data cannot produce. Exact dictionary:

    W_λ >= 0      ⟺  λ_a >= 0  ⟺  g|(−2a, 2a) is a screw function on the interval
    W_λ >= −8·I   ⟺  shift 8 makes the windowed space a de Branges space

with `g` the Weil screw function and `a = log λ`. Conrey–Li (IMRN 2000)
refuted de Branges' own positivity conditions on ζ-built spaces numerically
(34th zero; `ξ(1+282i)/ξ(2+282i) < 0`); nothing unconditional survives there.
Lagarias / Suzuki give the RH-conditional identification `H_W ≅ K(Θ_ξ)` with
no converse. **No de Branges tool supplies a positivity mechanism.**

What the theory does supply is a name for the wall. By Krein–Langer
continuation, `W_4 >= 0` says the Weil screw function on
`(−2 log 4, 2 log 4) = (−2.77, 2.77)` has **at least one** positive-definite
extension to ℝ; RH says that extension is **unique and equals g**.
Determinacy at any certified window would already be RH.

### Li's criterion and Nyman–Beurling (assessed; closed)

Li: the Bombieri–Lagarias test functions have Mellin transforms with a pole
at 0, so the Li class meets the Paley–Wiener class of every finite window only
in {0}; no window certificate constrains any `λ_n`. `W_4 >= 0` does give the
windowed coefficients `λ_n^{[log 16]} >= 0` for all n. Nyman–Beurling: no
finite statement is equivalent to `W_λ >= 0`; `d_N` was certified to N = 600
and `d_N² log N` oscillates around `C = 2+γ−log 4π` with Burnol's bound making
that rate sharp — no analogue of the v1.36 floor weakening exists there.
Burnol's Thm 3.1 (co-Poisson complement = span of zero evaluators) is the one
structural bridge, and it is a semantic lock, not a result.
(`evidence/diag_routes/li/`, `evidence/diag_routes/nb/`)

### In Toeplitz–Hankel terms (`evidence/diag_circle_split/`)

The certified matrix splits exactly as symbol + Toeplitz-structured
commutator + Hankel reflection term. The reflection term alone makes the
form negative by O(1); the Toeplitz commutator cancels it to 10^-75. The
parity sectors are the pencils `T(φ) ± H(φ)` (Basor–Ehrhardt). A prime-free
control of the assembled form is negative by O(1) at every window, so the sign
is arithmetic (exact). An earlier version of this paragraph claimed a
Kac–Murdock–Szegő prediction of 4 → 11 negative eigenvalues from a "line
symbol"; that function was the analytic continuation of the diagonal, not the
multiplier symbol, and the claim is withdrawn (`evidence/diag_circle_split/`,
retraction section).

### de Bruijn–Newman (assessed; closed)

RH ⇔ Λ = 0 (Rodgers–Tao, arXiv:1801.05914; Polymath15, arXiv:1904.12438,
Λ ≤ 0.22). No bridge exists in either direction between a finite-window Weil
certificate and any bound Λ ≤ c: H_t has no Euler product and no explicit
formula, and every known zero-location → Λ statement needs RH to a height.
The project toolchain reproduces Polymath15's certified barrier from scratch
(`evidence/diag_routes/dbn/`), which confirms capability and nothing else.

### The unification

A certified window is **positivity of a truncated moment problem** whose
sections are `T(φ) ± H(φ)`; RH is the **determinacy** of that moment
problem. Positivity of finitely many sections never decides determinacy.
That is why no finite list of windows can close G2, stated in language
(Krein–Langer on one side, Szegő–Widom / Basor–Ehrhardt on the other) that
predates this project. It does not move RH; it stops "one more window"
arguments and it tells the next attempt what kind of statement it must be.

## Correction to NS-14 (v1.41)

The sinc-lattice conclusion in the original `diag_ns14_zeros` report is
withdrawn. Its reconstruction omitted the `(-1)^n` change from unshifted
to centered cosine coefficients. The corrected exact formula has removable
poles, and its value at a retained lattice point is `sqrt(L/2)(-1)^k v_k`,
not zero merely because `v_k` is small. The new lambda=3, N=120 certificate
reproduces CCM's local zero discrepancies. It does not rerun NS-14's N=256
experiment or transfer zero locations to the complete ground. Thus no
negative conclusion about CCM step (b) follows from the old diagnostic.
See [the preserved report's correction](evidence/diag_ns14_zeros/results-v2.md).
G2 and RH remain open.
