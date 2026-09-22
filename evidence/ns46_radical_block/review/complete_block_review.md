# NS-46 complete radical-block bounds — independent bounded review

Review type: analytic and read-only. No numerical replay, author-file edit, manuscript/map edit, commit or push was performed. This note reviews the complete residual/rank argument together with its finite-arc Gram input. It does not prove the remaining signed complementary floor.

## Pinned inputs

| File | SHA256 |
|---|---|
| `evidence/ns46_radical_block/astra2/complete_block_bounds.tex` | `44307ff1ab01dd6d93b1d287367359cb209bf6166789c30de894f281591bd3d2` |
| `evidence/ns46_radical_block/coordinator/finite_arc_gram.tex` | `ed8d0093fb1a21e8f81857b4c3f053762a9d22a2a50d38313aec2237df1e701b` |
| `evidence/v135/new_section.tex` | `95b12e631f5f55c987ca8ddfdb1c8712b2a40bbaa01967ec29157742769b77fa` |

The live manuscript's existing v1.35 cutoff/radical proof and v1.14 operator-domain/compact-resolvent statements were inspected as dependencies. References below are to the pinned complete-block file unless another file is specified.

## Ranked findings

**MAJOR: none.**

**MINOR: none.**

**NOTE — lines 89–96: the full Gram-loss envelope is necessary and is present.** The proof bounds the actual positive loss `K−Γ`, whose diagonal integrand is `(1−χ_a²)|φ(x−t_j)|²`. It uses the complete uncut tail mass outside `|x|≥a−1`. A norm bound on `(1−χ_a)φ` alone would not suffice because `(1−χ_a)²≤1−χ_a²`; that incorrect replacement is explicitly excluded. No change is requested.

**NOTE — lines 122–124 and 150–187: physical rank, source removal and spectral counts are distinct and correctly stated.** The full cutoff block has dimension `2J+1`, with exact even/odd dimensions `J+1` and `J`. The actual even source removes at most one even dimension; the admissible even dimension is exactly `J` when the source projection is nonzero and `J+1` otherwise. The full-operator spectral count is a separate conclusion for the unprojected parity blocks. The later source-admissible constraint count does not incorrectly subtract another rank from the spectral count. No change is requested.

**NOTE — lines 189–205: the conclusion is a necessary rank obstruction for positive coercivity, not a complementary lower bound.** The draft retains the missing cofinal signed estimate on the entire ordinary orthogonal complement and states that enlarging the block does not control negative eigenvalues outside it. The energy signs are not inferred from small residuals. No change is requested.

There is no outstanding actionable finding within this review's scope.

## Tail exponent and norm accounting

At lines 46–54, for fixed `|t|≤T` and `|x|≥a−1`, let `X=exp(2|x−t|)`. Then

```
X >= exp(2a−2(T+1)),
exp(2|x|) <= exp(2T) X.
```

The archived derivative bounds are `|φ^(r)(u)|≤C_r exp(−π exp(2|u|)/2)`. The cutoff derivative bounds are uniform in `a`; the apparent absolute-value cusp in `χ_a(x)=vartheta(|x|−a)` lies where the cutoff is constant for sufficiently large `a`. Thus both `r` and `r'` have the asserted smooth weighted-tail bound after absorbing `X` into half the Gaussian exponent.

For the H1 norm and the uncut tail mass, square the original Gaussian envelope and substitute `X=exp(2|x−t|)` separately on the two tails. The Jacobian contributes `1/(2X)`. The resulting integral is bounded by a constant times `exp(−π X_min)` (indeed with an additional inverse-power factor). It is therefore bounded by the weaker stated squared scale `exp(−(π/2)X_min)`. Taking the norm gives the same `c_T=(π/4)exp(−2(T+1))` as the pointwise bound. Enlarging the fixed constant covers the sum of the H1 norm and the weighted supremum. The full uncut tail-mass estimate in lines 36–38 follows with this same weaker exponent.

The centers remain in the fixed interval `[-1,1]`, so the decay parameter is `exp(2a)=λ²`, not the `λ` scale in the older separated-center construction whose centers moved as far as `a/2`. The constants here do not grow with the number of columns.

## Complete operator action and domain

Lines 56–69 correctly reuse polarized radicality as a distributional identity on `I_a`. Its three geometric parts have L2 representatives with the claimed bounds:

- The complete archimedean multiplier `Re ψ(1/4+iξ/2)−log π` is bounded by `C(1+|ξ|)`, so the full-line H1 tail controls its L2 action and hence its restriction to `I_a`.
- The weighted pointwise tail gives `|r(x±log n)|≤τ_a exp(2|x|) n^(−2)`. Multiplication by `Λ(n)/sqrt(n)` yields the absolutely convergent sum `sum Λ(n)/n^(5/2)`. The sum is over every `n≥2`, including rows beyond `exp(2a)`. No finite-prime residual has been substituted.
- Each pole integral is bounded using `|r(y)|≤τ_a exp(−2|y|)`: the integrals against `exp(±y/2)` converge absolutely, giving an output bounded by `Cτ_a exp(|x|/2)`. Both signed pole terms are retained.

On `I_a`, the displayed common upper bound `C sqrt(a) exp(2a) τ_a` dominates all three L2 contributions. This is the complete operator residual, not merely `q[g]` or a compressed residual. Every column is in `C_c^infinity(I_a)` because the fixed cutoff vanishes already at `|x|≥a−1/2`. Thus the complete operator-domain use is legitimate.

## Finite Gram and amplification

The companion finite-arc proof was checked for compatibility with the block use. Its frequency change of variables produces the factor `c0/d`; interval length `ell=rd/m` yields the final prefactor `c0 r/m`. The separated interpolation nodes give chord distance at least `2 ell |j−k|/π`; the Lagrange denominator product is bounded by `(2ell/π)^(m−1) k!(m−1−k)!`. The factorial estimate produces the stated `(rd/(4πe))^(2(m−1))`. Complex coefficients and a common translate are covered. It makes no uniform infinite-lattice assertion.

The loss `K−Γ` is positive semidefinite because `0≤χ_a≤1`. Its operator norm is at most its trace, bounded by `m τ_a²`. Consequently `m τ_a²≤γ/2` implies `Γ≥γI/2` and rank exactly `m`.

Writing `V=G Γ^(−1/2)` gives an isometry. Since `P_G=VV*`, the equality `||W P_G||=||W V||` is valid: `V*` maps the physical space onto the coefficient space. The column-residual Hilbert–Schmidt bound gives the full factor `sqrt(2m/γ)`. This pays for nonorthogonality and all cross terms; it does not silently assume a uniformly conditioned basis.

## Constants and cofinal balance

For `T=1`, `c_T=π/(4e^4)>1/1000` is an elementary strict inequality. The column prefactor `sqrt(a) exp(2a)` is absorbed into the excess exponent, so the weaker bound `C exp(−λ²/1000)` is valid eventually. The same weakened bound applies to the full tail norm.

For the prescribed `J=floor(λ²/(40000a))`, one has eventually `m=2J+1≤λ²/(10000a)` and `log(4πe/(rd))≤3a`. Therefore

```
γ^(-1/2) <= C sqrt(m) exp(3ma)
          <= C sqrt(m) exp(3λ²/10000).
```

The Gram-loss condition follows even with the weakened tail estimate:

```
m τ_a² / γ <= C m² exp(−14λ²/10000) -> 0.
```

The complete residual is then at most `C m exp(−7λ²/10000)`. The factor `m` can be absorbed into the remaining exponent gap to give `C exp(−λ²/2000)`. No finite numerical onset is asserted; all constants depend only on the fixed source/cutoff/Fourier arc, not on `a`.

## Parity, actual source, and spectral conclusions

Reflection interchanges columns `j` and `−j` because both the source radical and the cutoff are even. The coefficient-space symmetric and antisymmetric embeddings have dimensions `J+1` and `J`. Injectivity of the full synthesis makes their physical images have exactly those dimensions. The full image is reflection-invariant, so these are exactly its parity parts and their orthogonal projections lie below `P_G`; they inherit the residual bound.

The source constraint is one linear functional on the even block and zero on the odd block. No overlap estimate, source approximation, or identification of a cutoff column with the actual repaired source is required.

For any `F_a` of dimension below `m`, elementary dimension counting gives a unit vector in `Ran(G)∩F_a^perp`, and its complete residual bounds the absolute value of its quadratic energy by `eta_a`. Thus no positive coercivity lower constant above `eta_a` can hold there. Since `m` is asymptotic to a positive constant times `λ²/log λ`, the stated little-o removal obstruction follows.

For the spectral count, if the projection onto `[-2eta_a,2eta_a]` had smaller rank than the corresponding block, a unit block vector orthogonal to that spectral range would have operator norm at least `2eta_a`, contradicting its upper bound `eta_a`. One may take the constant in `eta_a` strictly positive. The existing complete self-adjoint compact-resolvent realization justifies counting eigenvalues with multiplicity. Applying the argument separately gives at least `J+1` even and `J` odd eigenvalues in that symmetric interval; no sign is specified.

## Verdict

The pinned argument supports the claimed complete near-zero block and the stronger necessary rank obstruction for a positive-gap strategy, conditional only on its cited established radical/domain facts and the finite-arc lemma checked above. It supplies no signed complementary lower floor and no positivity, G2 or RH conclusion. No numerical or manuscript build was part of this bounded analytic review.
