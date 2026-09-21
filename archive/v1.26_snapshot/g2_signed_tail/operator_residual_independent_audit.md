# Independent audit: ordinary operator residual

Reviewed September 21, 2026 against the v1.14 complete source, `operator_residual_derivation.md`, and `residual_insert.tex`.

**Verdict:** no mathematical gap found, conditional on the already established v1.14 Sobolev G1 and polynomial coefficient-tail results. The proof supports the stated absolute ordinary-norm residual. It does not support a residual normalized by the physical endpoint or a ground-state identification.

## Points checked

1. **Uniform Sobolev premise.** The manuscript's Proposition `prop:g1-sobolev`, equation `eq:G1-sobolev`, explicitly states that its constant is independent of both lambda and the periodic H1 test. Thus the exponentially large auxiliary output cutoff is legitimate. A merely fixed-band estimate with constant C_T would not justify the proof. The zero mode and endpoint traces are included in the displayed premise.
2. **Hermite normalization and scalar.** With the manuscript's unit-normalized Hermite functions, the coefficient combination is exactly

       −H4(0)H0(u)+H0(0)H4(u)
       = (4 pi/sqrt3) u²(2 pi u²−3) exp(−pi u²).

   The cross term in the squared norm uses the fixed Hermite L1 norm, preserving an O(lambda^-2) uniform source approximation after exact unit normalization. The fixed bump amplitude is exponentially smaller.
3. **Nonzero ordinary mass.** The limiting source is Fourier-invariant and has both zero scalar moments. Its co-Poisson image is inversion-even and in Haar L2. For u≥1 every summand is positive, and the factor sqrt(u) cancels the Haar denominator when bounding its squared norm below by the displayed positive integral. The compact-source approximation contributes squared error at most C lambda^-2 integral_(1/lambda)^lambda u^-2 du=O(lambda^-1). Omitted Gaussian summands and the external-window tail are exponentially smaller.
4. **Uniform graph tail.** The coefficient bound |p_hat(n)|≤C|B|lambda sqrt(L)/|n| for |n|>N is present in v1.14, including the exact repair. Multiplying by the actual logarithmic diagonal and summing squares gives the claimed graph bound; the bounded commutator costs O(lambda). At N≈lambda⁸(1+L), the combined result is O(|B|lambda^-2). The logarithm of arbitrarily large n is retained through the weighted integral comparison, rather than replaced pointwise by log N.
5. **Output split.** M is used only to decompose the infinite operator output. The source remains P_N p with its original polynomial cutoff. For M>2N, the actual complete off-diagonal entries give sum_(|m|≤N,|n|>M) |W_nm|²≤C lambda²N/M. The diagonal has no such cross block. The remaining source Fourier tail is controlled in graph norm, so no omitted component is silently discarded.
6. **Optimization.** With M=ceil(exp(2c/3)), the low-output bound is a polynomial times exp(−c/3), as is lambda sqrt(N/M). The source endpoint bound is |B|≤C lambda^(11/2) exp(−c), and sqrt(1+L) is absorbed by one extra power of lambda. The stated common C lambda⁶ exp(−c/3) estimate follows.
7. **Normalization and interpretation.** The limiting ordinary mass is positive, so unit normalization is valid. It produces small Rayleigh value and centered residual; neither implies bottom ordering. The diagonal(-1,epsilon) counterexample correctly excludes that inference. Dividing by the physical endpoint remains uncontrolled because the displayed upper bound would grow like exp(2c/3) times a polynomial.

## Presentation correction

The inspected LaTeX insert had `otag\\` on line 111; it should be `\notag\\`. This is a typesetting error, not a proof issue.

No additional computation is needed for this implication: all new steps are deterministic inequalities applied to the specified source and canonical operator. The separate signed Schur estimate or quantitative lowest-space overlap remains open.
