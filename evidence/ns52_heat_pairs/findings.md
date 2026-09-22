# NS-52 internal findings — 2026-09-22

Claim categories: exact identity; proved implication with explicit hypotheses; open input. No numerical illustration or numerical certificate was run.

## Main finding

Pairing survives the first algebraic test. The inverse-gap singularities of individual zero velocities cancel in the complete finite-cluster derivative. This does **not** supply uniform heat transport: an exterior-zero logarithmic derivative remains, elementary test-transform estimates grow with support, and a separate conditional obstruction rules out the proposed same-test comparison whenever the positive-time zero set contains an unmatched real zero.

`proof.tex` contains the full derivations, including smooth-core construction of the deformed zero form and all normalization factors.

## Exact normalization

Use Polymath15's H_t, where H_0(z)=xi(1/2+iz/2)/8 and ∂_t H_t=−H_t''. Set Z_t(w)=8H_t(2w), so Z_0=Xi and ∂_t Z_t=−κZ_t'' with **κ=1/4**. The time variable has not been rescaled. A heat coefficient 1 in the w coordinate would be a factor-four error.

With F_f(w)=∫f(x)e^(−iwx) dx, put Ψ_f,g(w)=F_f(w) overline(F_g(overline(w))). This is entire, sesquilinear in f,g, and reproduces the repository's zero-side Weil convention at t=0. The zero sum has no 2π factor with this nonunitary transform. It would have a 2π factor with the unitary transform. Completed Xi has no poles, so none are to be separately added to the zero form.

## Finite-cluster identity

On a contour free of zeros throughout a time interval,

S(t)=(2πi)^−1∮ Ψ Z'/Z,

S'(t)=κ(2πi)^−1∮ Ψ' Z''/Z.

Both formulas count every zero with its multiplicity and survive internal collisions. If the cluster consists of simple w_j and A=Z/∏(w−w_j), b=A'/A, then

S'=2κ Σ_{j<k} (Ψ'(w_j)−Ψ'(w_k))/(w_j−w_k)+2κ Σ_j b(w_j)Ψ'(w_j).

At a single multiplicity-m collision c,

S'=κm(m−1)Ψ''(c)+2κm b(c)Ψ'(c).

For a double collision this is 2κΨ''+4κbΨ'. The familiar 2κΨ'' term is incomplete unless the analytic exterior factor is constant or its term vanishes on the particular test. For the even real-entire family, contour clusters must include conjugate and reflected zeros without duplicating a coincident cluster. A collision at real c≠0 also requires the reflected collision at −c in a symmetry-complete contribution.

## Support dependence and the infinite sum

For supp f,g⊂[−a,a], |Ψ^(n)(w)|≤2a(2a)^n exp(2a|Im w|)||f||||g||. The resulting double-collision budget is 16κ(a³+B a²) exp(2aY)||f||||g|| when |Im c|≤Y and |b(c)|≤B.

The cubic dependence is real for the individual collision functional: conditionally on a double real collision, f_a(x)=a^−1/2 h(x/a)e^(icx), where h is odd and ∫u h(u)du=M_1≠0, has norm one and gives S'[f_a]=4κa³M_1². This does not assert that the arithmetic family has such a collision, nor preclude cancellation with other clusters.

For t≥0 the de Bruijn strip theorem puts Z_t zeros in |Im w|≤1/2. Uniform Gaussian growth majorants on compact time intervals plus Jensen give a sufficient uniform O(R²) zero count. Compact smooth test transforms decay to arbitrary order in this strip, so the zero-form sum converges absolutely and is continuous in time on the smooth core. No form-domain extension or termwise derivative of the complete sum is claimed.

A sufficient additional input for the proposed comparison would be an exhausting, multiplicity-preserving tracked cluster family with endpoint convergence and a support-independent upper bound on its integrated signed derivative. The finite identity proves none of those derivative estimates. Its sign must be an **upper** bound: q_t0−q_0≤C||f||².

## Conditional unmatched-zero obstruction

Assume the archived radical-cutoff property for a Schwartz φ and suppose positive-time q_t0 has all real zeros, one of which is c with F_φ(c)≠0. Then no finite C can make q_a[f]≥q_a,t0[f]−C||f||² hold on all compact smooth tests on a cofinal window family.

Proof mechanism: for fixed T>0 and fixed M, take h_M=M^−1/2 Σ_{j=1}^M e^(icjT)φ(·−jT). Its ordinary norm squared is bounded by the summable autocorrelation B_T, independent of M, while |F_hM(c)|²=M|F_φ(c)|². First let the window cutoff tend to infinity **for fixed M**. Its original Weil energy tends to zero; L¹ convergence preserves the real Fourier evaluation. Positivity of the deformed real-zero sum would imply m(c) M|F_φ(c)|²≤CB_T. Then let M grow, obtaining a contradiction. No uniformity of cutoff convergence in M is used; no global closability assumption is used.

The repository identifies F_φ with a nonzero constant times Xi. Thus the hypothesis means an unmatched deformed real zero. This checkpoint does not prove or certify such a zero at a specified t_0 and does not file the arithmetic heat route as closed. The comparison is conditionally obstructed; a different transported-test comparison would need a new construction and must respect the radical.

## Primary sources and exact dependencies

- D. H. J. Polymath, *Effective approximation of heat flow evolution of the Riemann xi function, and a new upper bound for the de Bruijn–Newman constant*, Research in the Mathematical Sciences **6**, 31 (2019), [journal DOI](https://doi.org/10.1007/s40687-019-0193-1), [author manuscript](https://arxiv.org/html/1904.12438). Equations (1)–(4): normalization; Proposition 3.1: zero velocities and multiple-zero splitting; Theorem 3.2: de Bruijn strip theorem. Those facts are used unconditionally.
- B. Rodgers and T. Tao, *The de Bruijn–Newman constant is non-negative*, Forum of Mathematics, Pi **8**, e6 (2020), [journal DOI](https://doi.org/10.1017/fmp.2020.6), [author manuscript](https://arxiv.org/html/1801.05914). Context: the known inequality Λ≥0; it is not a transport estimate and is not used to prove a sign here.
- Repository `audits/2026-09-22-conclusions-review.md`, Part B3, as read on `origin/audit/2026-09-22-conclusions`: asks for this finite collision test and warns against linear heat evolution of the logarithmic derivative.
- Repository `lem:v136-total-radicals`: cutoff residual tending to zero for each fixed finite translate combination; its double-exponential source decay supplies the L¹ limit and summable autocorrelation.
- Repository source-transform identity: the unitary Fourier transform of φ is a nonzero constant times Xi. The constant changes with Fourier convention; its nonzero value is all the conditional obstruction needs.

## Reporting boundary

What changed: corrected heat coordinate and time coefficient, analytic off-real pairing, retained exterior-zero term, and added a necessary radical-compatibility test for the same-test comparison.

Precise obstruction: cancellation of pair singularities leaves support-dependent derivatives and unestimated signed exterior interactions. Under the unmatched-zero hypothesis, the proposed uniform comparison itself fails. No failure of the original Weil object follows.

No new window, tail metric, midpoint computation, interval certificate, G2 claim, or RH claim. Parent owns manuscript integration, the full build, reference counts, version assignment, and repository publication. This directory is an evidence checkpoint, not a new manuscript version.

## Local validation

The complete NS-52 fragment was compiled with `latexmk -pdf`, using the existing manuscript auxiliary labels for its two explicit internal references. Result: **4 pages, 0 undefined/duplicate-reference warning lines, 0 overfull boxes**. The isolated build directory was `/private/tmp/ns52-proof-check-owsmc_23`. This is a fragment build, not the required full manuscript integration build; the parent task will report the latter separately. No unexpected control characters remain in the source.

NS-53's agent independently reviewed the mathematical fragment and reported no MAJOR findings; its two MINOR typesetting findings (a hidden form-feed and integral spacing) were corrected before this build. The separate review in this directory covers NS-53.
