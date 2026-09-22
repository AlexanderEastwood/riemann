# NS-55: scoped unique-continuation findings

Classification: exact identity; proved implications and counterexample; named open input. No numerical experiment or certified computation is asserted.

## Main result

The full arithmetic operator does **not** inherit the logarithmic Laplacian's local simultaneous-vanishing property. For every `a > (log 2)/2`, the proof constructs a nonzero real `f ∈ D(A_a)` and an open interior interval `U` such that `f = A_a f = 0` on `U`. For `a > log 2`, there is an infinite-dimensional space of witnesses in each parity; imposing finitely many linear conditions, including the actual source constraint, leaves nonzero witnesses.

These are local-patch witnesses, not full arithmetic nullvectors. They do not disprove positivity, API, G2, or RH. What fails is the proposed local unique-continuation theorem for the actual operator, rather than merely an estimate for it.

## Mechanism and complete-domain check

Away from the support, the actual operator is its smooth integral kernel

`R(t) = 2 cosh(t/2) - exp(-t/2)/(1-exp(-2t))`

minus the finite prime-power shifts with their exact weights. On two short intervals separated by `log 2`, that shift gives the invertible diagonal `w_2 I`, with `w_2 = log 2 / sqrt(2)`. All remaining integral interactions have norm `O(|U|)`. A third disjoint support interval supplies arbitrary forcing. The Neumann inverse cancels the complete operator on the observation interval. The construction retains both the pole kernel and all prime terms; support geometry, rather than deleting terms, removes the unwanted shifts there.

The witnesses are compactly supported piecewise smooth functions, hence lie in `H^s(R)` for `0 < s < 1/2`. Their logarithmic Fourier multiplier is in `L²`: high frequencies are controlled by the positive Sobolev weight, and the bounded Fourier transform handles the integrable logarithmic singularity at zero. The form representation and the bounded remainder put them in the complete operator domain. This does not require an unproved `H¹` bootstrap.

## Exact restricted uniqueness that does hold

Let `S` be the closed essential support of the zero extension and `b = sup S < a`. If a nonempty interval `J ⊂⊂ (b,a)` avoids all translated supports `S + log n` for the finite prime powers active at the window, and the weak arithmetic equation holds on `J`, then `f = 0`. Reflection gives the left-hand version.

All shifts vanish on `J`, leaving an analytic integral potential. Continuing only that separated integral potential to `x > b` produces its exponential moment series. One pole term cancels the first term of the kernel expansion exactly. The surviving positive integer moments of the measure obtained by pushing `exp(y/2)f(y)dy` through `t = exp(2y)` all vanish. Its support is compact and bounded away from zero, so these moments determine it. This proves the stated uniqueness theorem without RH.

The support-separation hypothesis is substantial. The first-crossing lane independently proves that a proposed first-zero nullvector reaches both window endpoints. That support saturation rules out the empty interior exterior-of-support strip required above. Boundary trace zero alone cannot replace it.

## Primary sources and transfer audit

1. Huyuan Chen, Daniel Hauer and Tobias Weth, *An extension problem for the logarithmic Laplacian*, arXiv:2312.15689v1 (25 December 2023), [primary full text](https://arxiv.org/html/2312.15689v1), Theorem 1.7. Their hypothesis is simultaneous vanishing of `u` and `L_Δ u` on the same nonempty open set, for `u ∈ L¹((1+|x|)^(-1)dx)` in dimension one. Compactly supported `L²` functions meet the integrability requirement. The complete arithmetic equation supplies `L_Δ E_a f = -2 K_a f`, not vanishing of the logarithmic part on a patch where `f` vanishes. Here `K_a` is nonlocal.
2. Bastian Harrach, Yi-Hsuan Lin and Tobias Weth, *The Calderón problem for the logarithmic Schrödinger equation*, **Journal of Differential Equations 444 (2025), 113665**, [DOI](https://doi.org/10.1016/j.jde.2025.113665), [primary preprint](https://arxiv.org/html/2412.17775v1), Proposition 4.1. The forward inverse problem assumes the appropriate absence of a zero Dirichlet eigenvalue; it cannot be used circularly to prove that absence here. Its local multiplication potential differs from the arithmetic nonlocal remainder.

Manuscript citation keys: `ChenHauerWeth2023`, `HarrachLinWeth2025`. Version-specific theorem numbering is pinned above.

## Existing geometric representation and missing data

The Chen–Hauer–Weth representation in dimension one can be written as the three-dimensional line-source Newton potential

`W_u(x,y) = (1/2) ∫ u(s)/sqrt((x-s)²+|y|²) ds`, where `y ∈ R²`.

It satisfies `-Δ W_u = 2π u dx ⊗ δ_0` and is harmonic off the line. Its renormalized trace `T_u = lim_{r→0}(W_u(·,r)+u log r)` obeys `L_Δ u = 2(log 2 - γ)u - 2T_u`, distributionally. Thus the actual null equation gives

`T_(E_a f) = (log 2 - γ) f + K_a f` on the interval.

This is known external geometric representation, not a new positivity estimate. The arithmetic nonlocal boundary operator survives. Exterior `E_a f = 0` does not prescribe the renormalized trace there, and does not supply the second datum required for the unique-continuation theorem. These formulas are included as context, not as a new proof claim.

## Review and validation

- Parent independently checked the constructions, constants, complete-domain membership and moment argument without identifying a mathematical defect.
- Prime-shift agent independently checked the same points, parity/source constraints and both primary unique-continuation statements; no MAJOR/MINOR findings. Its review is archived in its own subdirectory.
- I independently read the first-crossing lane's complete `proof.tex`. No MAJOR/MINOR findings in support saturation, finite dilation identity, archimedean constant 5, or restricted-logarithmic crossing countermodel. This was a mathematical review, not an independent manuscript build.
- Parent owns full manuscript integration/build, page count, reference counts and version selection. This subtask does not claim a full build.

## Remaining input

Complete arithmetic affine-potential injectivity remains open. Neither the local counterexamples nor the restricted support theorem settles whether a nonzero vector can satisfy `A_a f = 0` throughout the window. A valid first-crossing exclusion needs arithmetic information beyond direct transplantation of the logarithmic open-set theorem. No new window, tail metric, G2 claim, or RH claim was introduced.
