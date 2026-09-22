# NS-55: first-crossing subtask findings

Category: exact identities, proved implications with explicit hypotheses, abstract countermodel, and an open arithmetic input. Not a numerical illustration or certificate.

## What changed

The tempting shape-derivative argument was replaced by finite dilation differences on zero extensions. This retains the full logarithmic form domain and does not assume H¹ regularity, pointwise boundary derivatives, differentiable eigenvalues, or differentiable prime correlations.

## Results proved in proof.tex

1. At a first-zero window a*, every nonzero kernel vector has essential support diameter 2a*, hence reaches both interval endpoints. Otherwise translate it into a smaller positive window. This does not assert nonzero boundary trace and is compatible with logarithmic boundary decay.
2. Inward dilation U_r f belongs to the smaller complete domain and has the same ordinary norm. For a nullvector, q_(ra*)[U_r f]=q_(a*)[U_r f−f]>0. Both cross terms vanish by the full form-domain null equation.
3. The exact dilation defect separates the digamma multiplier, **both signed pole terms**, and the finite weighted prime autocorrelation changes R_f(log n/r)−R_f(log n). A fixed prime cutoff e^(2a) is valid because every added correlation is exactly zero. Thus endpoint crossings do not introduce omitted terms.
4. The archimedean defect satisfies 0<A_r≤5 log(1/r)||f||². The constant is proved by the positive digamma series and a sum–integral bound for a unimodal summand; it is not numerically estimated.
5. Two translated nullvectors have zero diagonal values on a larger window but retain their full cross pairing B_h. The exact energies of their phased sum/difference are ±2 Re(e^(−iθ) B_h). If B_h≠0 this produces negativity **after** the proposed first crossing, consistent with the scenario rather than excluding it.
6. The complete restricted logarithmic form ell_a,c has ground energy ν(1)−log a−c. It meets the generic support-consistency, translation, compact-resolvent and small-window-positivity assumptions yet crosses zero at a finite window. This is an actual infinite-dimensional form countermodel, not an arithmetic negative direction.

## Precise remaining gap

At a proposed first-zero nullvector the variational inequality forces the signed prime-overlap defect to be strictly below the sum of archimedean and pole defects for every inward dilation. A separate arithmetic result forcing the reverse inequality for one dilation would exclude that vector. No such result follows from the finite-difference algebra, and simply proposing it is not a new arithmetic theorem. Differentiating the prime correlations would require more than the known logarithmic Fourier moment.

Only nullvectors at windows with A_a≥0 need exclusion for sign continuation. That narrows the hypotheses under which an arithmetic argument might work, but no uniqueness mechanism is established by inclusion, translation or the logarithmic principal part. API, G2 and RH remain open.

The support-saturation lemma also prevents using an exterior support gap *inside the interval* at the first crossing. It does not rule out separate arithmetic arguments that force such a gap or otherwise improve uniqueness.

## Sources and novelty boundaries

- [Suzuki, v2](https://arxiv.org/html/2606.09096v2): Theorem 1.3 proves continuity of the lowest eigenvalue; Section 4 transfers Rayleigh quotients by scaling and passes through the closed form domain. This subtask does not claim that scaling or continuity is new.
- [Hernández-Santamaría–López Ríos–Saldaña](https://arxiv.org/html/2401.18033v2), introduction and Appendix A.1: restricted logarithmic Laplacian symbol 2 log|ξ| and scaling. The first-crossing countermodel is an elementary consequence of that symbol, proved directly here.
- Existing repository inputs: `prop:v118-log-dirichlet`, `eq:v129-jump-decomposition`, `prop:v135-both-parities`, and the NS-51 complete affine-potential criterion. The retained prime/pole decomposition is exactly the existing arithmetic form, not a new surrogate.
- The digamma series used to bound ξ alpha′ is obtained from the classical psi partial-fraction expansion (also used in the repository's archimedean identities); see [NIST DLMF Chapter 5](https://dlmf.nist.gov/5.9).

No new window, tail metric, operator-domain bootstrap, midpoint solve, or RH assumption. Parent owns manuscript integration, complete build, reference counts and publication.

## Local validation and independent review

The complete first-crossing fragment was compiled with `latexmk -pdf`, importing the existing integrated manuscript labels and citation keys. Final result: **3 pages, 0 undefined/duplicate-reference warning lines, 0 overfull boxes**. Build directory: `/private/tmp/ns55-first-crossing-check-x3uj79fg`. An initial wrapper redundantly included an already imported bibliography key; that wrapper-only duplicate was removed before the final successful check. The proof source has no unexpected control characters. This is a fragment build, not the full manuscript build.

The parent independently checked the main first-crossing claims and requested only that the real translation parameter be explicit; this wording was corrected. A separate independent review of the prime-shift lane is delivered as `prime-shift-review-2026-09-22-v1.html`: **0 MAJOR, 0 MINOR mathematical findings**. It checks the actual semigroup obstruction, compressed-shift norm, ramp Hilbert–Schmidt norm, actual bounded-remainder norm jump, and fixed-window Fredholm reduction.
