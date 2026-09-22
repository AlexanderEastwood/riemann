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

Suzuki's fixed-window construction uses a shift strictly below the spectral
bottom. The existence of that shifted positive space does not decide the
unshifted bottom's sign. In particular, `W_lambda >= -8 I` safely permits a
shift `8+epsilon`; the nonnegative endpoint shift may have a nullspace and
needs separate quotient/domain analysis. This is a limitation of the stated
shift construction, not a theorem excluding all de Branges methods.

Positive local screw data admit positive extensions under the cited extension
theorems. The required arithmetic conclusion is that the prescribed global
Weil screw function is positive. Uniqueness of arbitrary extensions is not
established and is not substituted for that identification. NS-51 below
instead uses the published nondegeneracy/continuity formulation and states
its missing arithmetic injectivity input explicitly.

### Li's criterion and Nyman–Beurling (scoped assessments)

The prior Li assessment concerns the direct identification of rational Li
transforms with finite-window entire Paley–Wiener tests. It does not prove
that every indirect transfer is impossible. The historical diagnostics are
retained in `evidence/diag_routes/li/`.

Nyman–Beurling is reopened by NS-53. The established criterion is `d_N -> 0`;
any proved upper rate tending to zero suffices. Burnol's lower bound of order
`1/log N` for the squared distance does not require a matching upper bound.
The archived finite distances in `evidence/diag_routes/nb/` establish no
asymptotic decay theorem. NS-53 gives the exact residualized block gain
`h^T S^(-1) h`, with the full Schur complement, and the unconditional lower
bound `||h||^2 / (kappa log(M/N))`, `kappa=log(2pi)-gamma`. A divergent
cumulative relative gain would prove convergence; the needed arithmetic
residual block-correlation bound is explicitly OPEN, not a consequence of
the finite identities. See `evidence/ns53_nb_blocks/`.

### In Toeplitz–Hankel terms (`evidence/diag_circle_split/`)

The certified matrix splits exactly as symbol + Toeplitz-structured
commutator + Hankel reflection term. The reflection term alone makes the
form negative by O(1); the Toeplitz commutator cancels it to 10^-75. The
parity sectors are the pencils `T(φ) ± H(φ)` (Basor–Ehrhardt). A prime-free
control of the assembled form is negative by O(1) at every window, so the sign
is arithmetic (exact). On the manuscript's
own symbol `β_a` (validated against the assembled matrix to 2e-7,
`evidence/diag_true_symbol/`), the λ=3 ground state puts 49.9% of its Fourier
mass on `{β_a < 0}`, with negative- and positive-level energies `∓0.0898`
cancelling to `10^-38`, all below `ξ ≈ 10`; it never touches the deep
negativity of `β_a` at high frequency. That is the scale the weighted
concentration criterion has to control. (An earlier KMS claim here used the
wrong object and is withdrawn.)

### de Bruijn–Newman (NS-52: exact paired transport, open arithmetic route)

RH is equivalent to Lambda=0 after Rodgers–Tao's unconditional lower bound.
The historical Polymath15 barrier reproduction does not exclude all bridges
from Weil forms. NS-52 fixes the normalization `Z_t(w)=8 H_t(2w)`, so the
heat coefficient in the ordinary zeta coordinate is 1/4. Finite zero-cluster
transport has an exact contour formula; inverse-gap singularities cancel
inside the paired contribution, but the exterior-cluster logarithmic
derivative remains. The smooth-core complete zero sum exists; differentiating
it and controlling it uniformly in support are separate demands.

A particular same-test comparison `q_0 >= q_t0 - C ||f||^2` is impossible
if the real-zero deformed function has even one zero at which the original
radical transform is nonzero. The result is conditional: this checkpoint
does not verify an unmatched zero at a specified time. It closes neither
the heat approach nor a comparison with a different justified test transport.
See `evidence/ns52_heat_pairs/`. No physical negative Weil direction follows.

### Complete kernel exclusion (NS-51)

For `f` in the complete logarithmic form domain, `A_a f=0` exactly when
its screw potential `(g * E_a f)|(-a,a)` is affine. This local continuous
integral equation avoids an unproved `H_0^1` assumption. Even parity allows
a constant potential; odd parity allows `b x`, and its derivative constant
must be retained. Ordinary `L2` screw-operator injectivity cannot be silently
substituted for injectivity on the derivative completion.

A bounded self-adjoint rank-one perturbation of the same logarithmic
principal operator has a zero eigenfunction with logarithmic boundary decay
outside `H_0^1`. Thus the proposed generic bootstrap fails; an arithmetic
bootstrap is neither proved nor refuted. Affine-potential injectivity (API)
on the complete form domain remains OPEN. With continuity of the lowest
eigenvalue and a positive small-window starting point it would prevent a
first sign crossing, without a uniform positive gap. This is the established
nondegeneracy route in an explicit integral formulation, not a proved new
positivity mechanism. See `evidence/ns51_kernel/`.

### What the comparisons establish

The assessed finite-window data do not supply the missing cofinal assertions.
They do not prove that every alternative mechanism fails, or that logically
equivalent criteria have equally difficult proofs. Literal Toeplitz–Hankel
structure and applicable asymptotics remain separate obligations; a truncated
moment analogy is not a proved arithmetic determinacy equivalence. NS-51–53
record concrete first lemmas and their remaining inputs without promoting
an unexcluded route to a proved estimate.

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


## Complete-ground local transfer (v1.42)

The complete lambda=4 ground transform now has a certified unique simple
zero in `(gamma_1-0.1, gamma_1+0.1)`; see [v1.42](evidence/v142/).
The even-sector separator 1e-67 and the exact trial's complete energy
bound its orthogonal ground-projection error. Endpoint signs and a
positive derivative pass at 1024/1280 bits, with all old infinite-tail
bounds retained. This is a coarse local enclosure. It does not determine
the sign of the discrepancy or transfer the minute finite-compression
values, and it does not order earlier zeros. Cofinal convergence, G2
and RH remain open.


## NS-19 resolution accounting (v1.43)

The complete first positive lambda=4 ground-transform zero is now certified
simple and within `8.752082e-33` of gamma_1. At 1024/1280 bits the evaluator
dual comparison gives `sqrt(C_ell*rho)/0.0016 = 8.7520815739...e-33`.
Its limit is the upper energy budget times the evaluator constant, not
the original `sqrt(rho/b)` ordinary projection error.

A hypothetical certified lower ground-energy bound l would improve the
separate trial-transfer estimate through `b*(rho-l)/(b-l)`. Resolution
`1e-71` would need a gap about `3.2032e-153`, relative `1.3055e-78`.
No such estimate is archived, and the frozen trial's transform value
`1.0641...e-40` at gamma_1 would still prevent that transfer alone from
giving the desired gamma-centered enclosure. The direct energy bound
instead requires an upper-energy improvement; a lower bound is not a
substitute for that improvement in the direct formula. It can improve
the separate transfer enclosure toward its frozen-trial floor
`abs(fhat(gamma_1))/d = 1.064123340460...e-40/0.0016`, about `6.65e-38`.
This is a floor of that enclosure formula, not of the actual discrepancy;
attainment is not asserted.

The finite N=120 discrepancy `(2.9250,2.9251)e-71` is separately certified.
Its scale lies below the resolution of the displayed archived estimates;
the actual complete discrepancy is not certified to have that scale.
No universal impossibility claim about every use of v125/v126 data is made.
This is a bound failure, not an object failure. CCM's source-to-ground
approximation and cofinal convergence, G2 and RH remain open.


## Weighted concentration on the level pencil (NS-24, v1.44)

For an exact source-admissible pencil direction, the weighted criterion
requires `L_a[v_k]/q_a^+[v_k] <= nu_k + eta_a ||v_k||^2/q_a^+[v_k]`, where
L_a is the loss between the exact symbol and its proposed lower minorant.
At zero allowed error, the relative loss budget is nu_k. For the weaker
bounded-error goal the eta term remains; tiny nu_k alone is not a no-go.

The section-7 diagnostic uses the uncompressed even head. Its twelve
lambda=4 N=48 values below 1e-8 are diagnostic only, and do not establish
source orthogonality. The exact class is restricted by the source constraint;
mixtures require a full matrix inequality, not only directional checks.
A fixed head supplies no complete-complement or cofinal estimate. The live
criterion still requires uniform errors on a cofinal family, with the
bounded-error weakening and both-parity/source hypotheses retained. The
task stops at this distinction; no new concentration bound, G2 or RH claim.


## Exact lattice identity and the minorant gap (NS-26/27, v1.46)

The symbol is the sharply truncated explicit formula with the shifted
Perron denominator. Its archimedean block cancels by the functional equation,
without RH; the strict prime-power endpoint, trivial zeros and finite-prefix
remainder remain. This is classical explicit-formula content, not a new
lens or sign theorem. The lattice envelopes vary. The archived x=9,16,36,64
are integers; treating them as nonintegers loses a substantial endpoint term.
Forty low sample locations and fourteen deep-trough/centroid locations were
reproduced numerically with an explicit Gaussian/desmoothing convention,
sufficient zero counts and residuals, all below 1e-6. This is not a cofinal
trough-density or zero-spacing theorem.

The minorant task proves eta >= [(b+B)c-B]+ and eta >= [c*delta-Q]+,
retaining positive spill and original packet energy. A conditional distinct-
level bound eta >= [c D_a/(2K)-Q]+ gives the requested linear complexity
consequence only with a uniform arithmetic level-distribution lower bound
seen by a source-admissible bounded-energy packet. v1.37's unconditional
D_a->infinity does not establish these hypotheses. The J-trough lobe-floor
family has the exact bound eta>=d_(J+1), but the required cofinal trough
multiplicity is also not established. A two-value countermodel demonstrates
why depth and concentration alone are insufficient; it is not a counterexample
to the arithmetic criterion. Source projection and odd-sector scope are
explicit. The route remains blocked, not closed. G2 and RH remain open.


## Level distribution as a zero statement (NS-29, v1.47)

The exact corrected zero field equals beta_a. Uniform lower measures of
all its level bands form the named open input ZLD; a lower bound on each
cumulative sublevel set is insufficient. The reduction separately requires
a source-admissible packet whose Fourier density covers those same bands
and whose original energy is bounded. On [-theta D,0] these hypotheses give
eta >= [b alpha kappa theta^2 D/K - Q]+.

The cited zero-counting, zero-density, Landau-Gonek and pair-correlation
results do not provide this signed value-distribution statement. No
implication or equivalence with RH, pair correlation, the density hypothesis
or Lindelof is established; logical independence is not claimed either.
v1.37 gives global depth divergence, not uniform band measure. The explicit
local slope estimate has a window-dependent cost. Broad Fourier pulses
have energy log X + O(1), so broad spread alone does not give uniform Q.
Both arithmetic distribution and bounded-energy coverage remain open.
This is a gap in the proposed minorant obstruction, not an object failure;
the route remains blocked and the weighted criterion valid. G2 and RH
remain open. See evidence/v147/ and its primary-source bibliography.


## Weighted zero input after review (NS-32/33, v1.49)

The proposed peak-density scalar is not a bound justified by the finite
histogram. A negative critical value makes the continuous coarea density
essentially unbounded; v1.47's absolute continuity never asserted a bounded
peak. The exact weighted quantization implication survives without that
assumption, with the uniform case giving c=c'*phi exactly. PR #14's v1.48
revised candidate f3611ef recognizes the peak problem but remains held for
incorrect K rearrangements, a bin maximum identified with the full
concentration function, and an infeasible lambda=4 diagnostic vector
(minimum bin ratio 0.636 at c'=1). The concentration-function bound is
proved here with its correct rearrangement.

QC_1=phi*D-mean(beta^-) is an exact corrected-zero functional, but its
growth alone is insufficient: even full-support absolutely continuous
measures can have QC_1~D/2 and QC_2->0. The named cofinal input QG is growth
of QC_K for every fixed K, plus separate admissible bounded-energy weighted
packets. A QC_1/K law requires an additional quantization-shape hypothesis.
Neither input is established; depth divergence gives no fraction limit.
The failure is of the crude bound and diagnostic interpretation, not of
the valid concentration criterion or physical form. G2 and RH remain open.


## Explicit capacity weight and its relative-error obstruction (NS-34, v1.50)

The positive Gaussian arithmetic radical h=E(H)(exp x) is an explicit
comparison weight with pole mass 1/sqrt(3), independent of an unknown
lowest eigenvector. Its full Picone identity gives q[hg]=J_h[g] minus
(2/3)Var_nu(g) and the negative odd sinh square. The exact finite-window
exterior contribution is retained; this is not a new tail metric.

For this weight, generic strict absorption fails even at the weaker
bounded-error target. Discarding delta>0 of transformed energy forces
eta >= [delta*kappa exp(gamma lambda^2)-O(lambda log lambda)]+. Deleting
only prime-2 energy also fails. The proof uses compact far-translated
bumps in two parity spaces; one even linear constraint removes the actual
source without uncontrolled cross terms. It establishes no negative
physical Weil direction and does not exclude a different weight.

The surviving Critical Arithmetic Energy comparison (CAE), with full
coefficient one and the odd pole retained, is the existing uniform
complement-floor requirement written in these coordinates. It is open;
so is the stronger local capacity test that discards the positive potential.
The calculation identifies the accuracy the weight demands but supplies
no independent arithmetic sign bound. Both parities, source residual and
cofinal uniformity are still needed. G2 and RH remain open.


## NS-55 / v1.55: local uniqueness is not whole-window injectivity

The logarithmic-Laplacian theorem requires u = L_Delta u = 0 on the same open
set. Its hypothesis does not transfer to the arithmetic bounded nonlocal
remainder. The exact prime-2 construction in `evidence/v155/proof.tex` proves
local UCP false for the actual operator when 2a > log 2, in both parities for
a > log 2 and after finitely many source constraints. It never asserts
A_a f = 0 on the whole window. This is a failure of a proposed local property,
not a negative Weil direction or a failure of API.

The full real-space semigroup is not order preserving when 2a > log r,
r^3-r-1=0, by an exact positive off-diagonal pairing of disjoint nonnegative
tests. Bounded positive multiplication cannot repair this cone property;
quadratic-form positivity remains a different question. A prime-free
exterior-of-support observation cell yields a valid restricted uniqueness
lemma. First-zero support saturation prevents obtaining such a cell inside
the window from zero endpoint traces alone.

The complete-domain inward-dilation identity leaves precisely the signed
prime autocorrelation changes together with both pole changes to estimate.
No such arithmetic exclusion is supplied. The supporting primitive equation,
prime-entry norm obstruction and fixed-window Fredholm reduction are archived
in `evidence/ns55_kernel/`; the physical exceptional coupling remains unresolved.
Full build: 285 pages, zero undefined/duplicate references. API, G2 and RH remain open.
