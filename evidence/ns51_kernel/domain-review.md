# NS-51 independent domain review

Internal research/review note. Categories: proved implications with explicit hypotheses; an abstract countermodel; and an open arithmetic input. This is not numerical or certified-computation evidence. No arithmetic window, tail metric, G2 result, or RH result is added.

## Finding

The implication `A_a f=0 => f in H_0^1(-a,a)` is not supplied by the manuscript's endpoint theorem. It is false for the general class consisting of the same restricted logarithmic principal operator plus a bounded self-adjoint perturbation. A derivative-in-the-distribution-sense formulation avoids needing this implication, but its injectivity on the complete physical form domain remains the arithmetic problem.

## What is already justified

At a fixed interval `I=(-a,a)`, the manuscript's `prop:v118-log-dirichlet` identifies the complete physical operator with

`A_a = (1/2) L_Delta^Dir + K_a`,

where `L_Delta^Dir` is the restricted, exterior-Dirichlet logarithmic Laplacian (full-line symbol `2 log|xi|`), not the spectral logarithm of a Dirichlet Laplacian. The remainder is bounded and self-adjoint on `L²(I)` and bounded on every `L^p(I)` for `1 <= p <= infinity`.

The subsequent `thm:v118-eigen-endpoint-zero` proves that every eigenfunction has a bounded representative, continuous after zero extension, with upper boundary estimate `|f(x)| <= C / sqrt(|log d(x)|)` for small boundary distance `d(x)`. This holds at eigenvalue zero too. Its proof uses the equation `L_Delta f = 2(mu f-K_a f)` with bounded right side. Setting `mu=0` removes a bounded multiplication term; it supplies no positive-order Sobolev gain.

The logarithmic form topology controls a Fourier weight comparable to `1+log^+|xi|`, not a positive power of `|xi|`. Mere membership in this topology is not an `H^s`, let alone an `H^1`, estimate. The endpoint upper bound likewise does not establish any square-integrability of the derivative. These are limitations of these arguments, not a proof that a hypothetical arithmetic nullvector fails to belong to `H_0^1`.

## Explicit countermodel to a general zero-energy bootstrap

**Proposition (generic log-plus-bounded class, not the arithmetic Weil operator).** There exist an interval `I`, a bounded self-adjoint rank-one operator `K` on `L²(I)`, bounded also on every `L^p(I)`, and a nonzero even real vector

`tau in Dom((1/2)L_Delta^Dir+K) \ H_0^1(I)`

such that `((1/2)L_Delta^Dir+K)tau=0`. The zero extension of `tau` is bounded and continuous and has the same logarithmic boundary scale as the upper estimate in v1.18.

**Proof.** Take `I=(-r,r)` with `0<r<exp(-gamma_E)`. This is the one-dimensional small-ball condition in Theorem 1.2 of Hernández-Santamaría–López Ríos–Saldaña: their condition is

`|B_r| < 2^N exp[(N/2)(psi(N/2)-gamma_E)] |B_1|`.

For `N=1`, using `psi(1/2)=-gamma_E-2 log 2` and `|B_1|=2`, its right side is `2 exp(-gamma_E)`, while `|B_r|=2r`. The theorem gives a positive torsion solution `tau` of

`L_Delta tau=1 in I`, with `tau=0 outside I`,

and positive finite constants `c,C` with

`c/sqrt(|log d(x)|) <= tau(x) <= C/sqrt(|log d(x)|)`

near either endpoint. It belongs to the logarithmic Dirichlet form space. Since the right side `1` lies in `L²(I)`, the definition of the associated operator puts `tau` in its operator domain. Uniqueness and reflection invariance make `tau` even.

Set `M=integral_I tau>0` and

`K f = -(integral_I f)/(2M) * 1_I`.

This is a real self-adjoint rank-one operator. Hölder's inequality gives `||K||_(p->p) <= |I|/(2M)` for all the indicated `p`, including the endpoints. Also `K tau=-1/2`, so `(L_Delta^Dir/2+K)tau=0`.

If `tau` belonged to `H_0^1(I)`, the one-dimensional fundamental theorem and Cauchy–Schwarz would imply `|tau(-r+d)| <= sqrt(d) ||tau'||_2`. The lower bound above contradicts this because `1/sqrt(d |log d|)` tends to infinity as `d` tends to zero. Its zero trace and continuous representative also show it cannot be an `H^1(I)` function with a different trace. This proves the proposition.

This countermodel does not use the arithmetic remainder `K_a`, and is not a negative direction or a nullvector for the Weil form. It rules out only the claim that the bounded-perturbation structure and the special eigenvalue zero themselves imply the proposed `H_0^1` bootstrap.

Primary source: [Hernández-Santamaría, López Ríos and Saldaña, Theorem 1.2, arXiv:2401.18033v2](https://arxiv.org/html/2401.18033v2), published in *Discrete and Continuous Dynamical Systems* 45 (2025), 1–36, [DOI 10.3934/dcds.2024084](https://www.aimsciences.org/article/doi/10.3934/dcds.2024084). The operator's symbol and normalization are stated in their introduction, equations (1.1)–(1.2).

## Weak screw-potential reduction: review of the proposed proof

Let `V_a` be the closed physical Weil form domain, let `E_a f` denote zero extension, and let `g` be Suzuki's explicit even screw function. Define

`C_a f(x) = integral_I g(x-y) f(y) dy`, `x in I`.

The local expansion `g(t)=(1/2)|t|log|t|+O(|t|)` and the finite derivative jumps at prime-power logarithms give `g' in L²_loc(R)`. For `f in L²(I)`, both the potential and its first derivative are continuous on the closed interval: local `L²` translation continuity of the kernels, paired with `f in L²`, proves this without differentiating `f`. The weak derivative is `C_a'f=g'*E_a f`.

For every `f in V_a`, the following statements are equivalent:

1. `f in Dom(A_a)` and `A_a f=0`.
2. `C_a f` is affine on `I`.
3. `P_0(g'*E_a f)=0` on `I`, where `P_0 h=h-(1/(2a)) integral_I h`.

To prove this, first test the core identity `A_a=-g''*E_a` against compactly supported smooth functions. Approximate a form-domain `f` by the common smooth form core. Form convergence implies `L²` convergence; convolution with `g` on the compact interval is continuous under that convergence. Hence the identity holds weakly for `f in V_a`. A zero second distributional derivative is exactly an affine function. Conversely, if it is affine, `q_a(f,phi)=0` for every smooth compactly supported `phi`; form-core density and continuity of the closed sesquilinear form extend this to every `phi in V_a`. The representation theorem then gives `f in Dom(A_a)` and `A_a f=0`.

For even `f`, the potential is even, hence constant in this equation, and its first derivative is zero. For odd `f`, the potential is odd, hence `b x`, and its first derivative is the possibly nonzero constant `b`. Deleting this constant in the odd sector would change the kernel problem.

The continuous-kernel operator `(I-Pi_aff) C_a` is compact on `L²(I)` because `C_a` is Hilbert–Schmidt and `Pi_aff` has finite rank. Its kernel characterizes the complete physical nullspace **only after intersection with `V_a`** in the proof above. No converse for every arbitrary `L²` vector is established here. Compactness by itself does not give injectivity.

All equations are on the interval. An affine convolution potential on `I` need not remain affine on the real line; there is no full-line annihilation conclusion. There is also no source-complement restriction: this is the complete even/odd physical operator.

The differentiated explicit formula for `t>0`, away from the finite jump locations, is

`g'(t) = -4 sinh(t/2) + sum_(n<exp(t)) Lambda(n)/sqrt(n) - (psi(1/4)-log pi)/2 - (1/2) exp(-t/2) Phi(exp(-2t),1,1/4)`.

All constants and signs in the proposed parent formula check. The strict endpoint convention is legitimate away from jumps; the derivative at jump points need not be selected for the convolution. The Lerch derivative coefficient is `-1/2` because `2n+1/2=2(n+1/4)`. Extend by oddness for negative arguments.

## Derivative completion and prior art

Using the global distributional derivative `i partial_x(E_a f)` places derivatives of `L²` supported vectors in `H^-1(R)` and retains endpoint distributions; in particular, differentiating the zero extension of a nonzero constant on the interval does not give zero. This is the right convention if the first-derivative factorization is used.

One must not assert an unqualified bounded extension of the quadratic pairing `G_a` to all of `H^-1 x H^-1`: the paired form has an additional logarithmic weight. On the derivative image of `V_a`, the form may instead be transported by `f -> i partial_x(E_a f)`, with its shifted physical form norm. That construction avoids an `L²` derivative requirement. This restriction concerns the quadratic pairing, not a claim that no operator mapping between distribution spaces can be defined.

This completion mechanism is already present in [Suzuki, sections 8.3–8.5](https://arxiv.org/html/2606.09096v1#S8.SS3): choose `sigma<inf spec A_a`, use `T_a=A_a-sigma I` and `S_a=G_a-sigma K_a` with `K_a` the inverse Neumann Laplacian, and complete the mean-zero derivative test space in the `S_a` norm. The derivative extends isometrically between the two form completions; the derivative-side completion is explicitly not contained in `L²`. Section 8.5 formulates the corresponding generalized eigenvalue problem. Thus proving ordinary `L²` injectivity of `G_a` would not, without a further domain argument, establish injectivity of this extension.

## Exact remaining input

The arithmetic open input can be stated without any `H^1` assumption:

For each relevant finite `a`, the only `f in V_a` for which `C_a f` is affine on `(-a,a)` is zero (with the respective constant/linear parity forms stated above).

The weak reduction removes an unnecessary regularity demand. It does not supply the arithmetic uniqueness estimate or theorem. RH and G2 remain open.
