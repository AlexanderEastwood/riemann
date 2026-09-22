# NS-54 Selberg-to-QG review: internal source notes

Analytic assessment and proved conditional implications; no numerical experiment or arithmetic CLT certificate.

Owner: Astra-2. Base `f0178e0`; joint board claim `ccd722bf2b0e6fd6f0133f5b9220fed130b2c325`. Only this `selberg/` directory is owned here. No manuscript, board, map, commit or push action is included.

## Repository definitions

- `prop:v146-beta-explicit`, `eq:v146-perron-remainder`: complete corrected zero field, all complex zeros, strict prime endpoint, trivial zeros and limiting prescription.
- `ass:v147-zld`: every level band down to a fixed positive fraction of the **global** depth, uniformly on one prescribed cofinal head rule.
- `eq:v149-measures`, `eq:v149-qc`, `ass:v149-qg`: negative subprobability pushforward of uniform `[0,X_a]`; at most K downward levels including `-D_a`; growth and weighted bounded-energy packet clauses separate. The v1.48 quantization label in the assignment is superseded by this live v1.49 definition.
- `evidence/ns40_qg/qg_zero_field.tex`: separated-band lower bound, exact head dilution and prefix transfer. NS54 refines the scale and unbounded-left-law consequence; it does not claim a new arithmetic input.

## Primary sources read, 2026-09-22 UTC

1. Radziwiłł–Soundararajan, [arXiv:1509.06827](https://arxiv.org/pdf/1509.06827), Theorem 1, printed p.1. Uniform height `[T,2T]`, fixed normalized threshold, real logarithm normalized by `sqrt((1/2) log log T)`. Unconditional. This is not a derivative theorem. Its proof moves off the line and controls that particular logarithm; that does not automatically control the present complete field.

2. Bourgade, [arXiv:0902.1757v1](https://arxiv.org/pdf/0902.1757v1), Theorem 1.1, printed p.2; §1.2, pp.4–5. Uses uniform height `omega*t`, `omega in (0,1)`, a **fixed** finite number of shifts, and limits for logarithmic separation ratios. The normalization changes with distance from the critical line. At the line the complex logarithm divided by `sqrt(log log t)` has real and imaginary component variances `1/2`; thus `S(t) = Im log zeta / pi` has scalar scale `sqrt(log log t/(2*pi^2))`. Joint finite-dimensional convergence supplies neither differentiation nor control of a growing kernel.

3. Maples–Rodgers, [arXiv:1404.3080v2](https://arxiv.org/pdf/1404.3080v2), Theorem 1.2, printed pp.1–2. Uniform `[T,2T]`; fixed real compactly supported bounded-variation test `eta`; `n(T) -> infinity`, `n(T)=o(log T)`; sum over **ordinates of all zeros with multiplicity**. Variance is asymptotic to the integral of `|u| |eta-hat(u)|^2` over `[-n(T),n(T)]`, required to diverge. This result is unconditional and must not be described as assuming RH. Its stated test hypotheses exclude the unmodified sinc, and it does not itself identify the weighted complex-zero field with an ordinate count.

4. Bourgade–Kuan, [arXiv:1203.5328](https://arxiv.org/pdf/1203.5328), Theorem 1 and (3)–(5), printed p.3. RH assumed. Fixed test functions, mesoscopic scaling `1 << lambda_t << log t` in the paper's little-o convention. The theorem includes finite Fourier-variance smooth tests under sufficient decay/regularity; (3) requires the function and its first two derivatives to decay as `O(|x|^(-2-delta))`. The bare sinc fails that condition. Smoothing it introduces a transfer error that must be estimated for our moving field.

These source descriptions delimit the displayed theorems. They are not a comprehensive no-go against every extension or variant of Selberg's method. No source theorem is used to assert an arithmetic Gaussian law here.

## New proofs and review checks

- Exact differentiated finite sine-polynomial identity retains archimedean and continuum terms, with sign fixed by direct differentiation.
- Fixed-a height variance follows by elementary integration of distinct cosine frequencies. The `O_a(1/T)` constants are not uniform in growing a.
- Gaussian/surrogate transfer uses CDF error plus exceptional-set error and explicit centering; fixed K needs only finitely many negative bands. No first-moment convergence is assumed.
- Stronger one-sided theorem uses compactness of K normalized grid levels in `[-infinity,0]`. Any smallest finite limiting level leaves positive limiting mass below it; all lower levels tend to minus infinity. This handles lack of an attained optimizer and grids with fewer than K levels by near-optimization and repeated entries.
- A full law with unbounded negative support forces `D_a/b_a -> infinity`. Tightness then contradicts any fixed-fraction global-depth ZLD. A dyadic-subinterval law alone cannot give that conclusion for the whole head.
- Centered CLT countermodel is a measure-theoretic inference counterexample only; no arithmetic independence, ZLD failure, or physical negativity is asserted.

Build/verification results will be recorded separately after a temporary integration build. All external source content above is paraphrased; no long quotation is reproduced.
