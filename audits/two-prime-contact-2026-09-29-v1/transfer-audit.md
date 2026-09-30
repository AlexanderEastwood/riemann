# Transfer audit: connected cotangent model versus an arithmetic spectrum

Bounded exact construction audit, 2026-09-29. Reviewed working base `eb4e180`; the parent refreshed the full conclusions and current gaps. This lane reread the connected-construction specification, current OPERATOR-BRIDGES and WEIL-FLOOR, and the prior signed-trace/source-domain cautions. No numerical scan, model request, external theorem admission, or historical replay was performed.

**Wall check: Same open gap.** The connected two-orbit geometry supplies a construction prerequisite. It does not supply OPERATOR-BRIDGES' complete trace/positivity transfer or WEIL-FLOOR. Within this bounded audit, the naive scalar ordinary-L² spectral realization is explicitly identified and fails to yield discrete zero-like levels. That conclusion concerns one realization, not all weighted, resonant, or geometric constructions.

## Model and scope

Take `S¹=R/Z`, `a=1/log 2`, `c=1/log 3`, and

```
b(x) = x(1−x)/(x²−x+1),
v(x) = (a+c)/2 + (a−c) cos(πx)/2,
λ = τ dt + y dx,       H = v(x)τ+b(x)y.
```

Because `v≥min(a,c)>0`, the energy surface `Y={H=1}` is globally parametrized by `(t,x,y)`, with `τ=(1−by)/v`. The convention `ι_(X_H)dλ=−dH` gives

```
X_H = v∂t+b∂x−(v′τ+b′y)∂y,       τ̇=0.
```

Its restriction is the Reeb field of `α=λ|Y`, since `λ(X_H)=H` and the restricted contraction with `dλ` vanishes. Directly,

```
α = ((1−by)/v)dt+y dx,
α∧dα = (1/v)dt∧dy∧dx.
```

No compact-Anosov or global trace theorem is invoked to obtain these identities. The hypersurface is connected, noncompact, and three-dimensional; its cotangent ambient space is four-dimensional.

## Connected does not mean the trapped components interact

The only zeros of `b` are `0,1`, with `b′(0)=1`, `b′(1)=−1`; also `v′(0)=v′(1)=0`. Away from these planes, `x` is strictly monotone. On a plane, `ẏ=−b′(j)y`, so only `y=0` can be periodic. The two periodic circles are therefore precisely

```
γ₂: x=y=0, τ=1/a=log 2;
γ₃: x=1,y=0, τ=1/c=log 3.
```

The momentum `τ` is a global first integral. Consequently **no full lifted trajectory joins these two circles heteroclinically**: their momentum values differ. The base flow in `0<x<1` does approach `x=0` backward and `x=1` forward, but a lifted trajectory obeys

`y(x)=(1−τv(x))/b(x)`.

It can have bounded `y` near `x=0` only when `τ=log 2`, and near `x=1` only when `τ=log 3`. Every corridor trajectory escapes in `|y|` at at least one end. Thus eliminating mixed primitive periods here is achieved by monotone escape and conserved momentum, not by cancellation among recurrent interactions. The construction meets connectedness, but connectedness alone supplies no coupling mechanism for the two trapped components.

## Exact scalar spectral realization: three translation channels

For any of the three intervals `I=(-∞,0),(0,1),(1,∞)`, define

```
u(x)=log|x/(1−x)|−x,
F_I(x)=∫_(x_I)^x v(r)/b(r) dr,       θ=t−F_I(x) mod 1,
τ=(1−b(x)y)/v(x).
```

The anchor `x_I` is any fixed interior point. Since

`u′(x)=1/x+1/(1−x)−1=1/b(x)`,

`u` is a smooth diffeomorphism from each interval onto `R`. It increases from `−∞` to `+∞` on `(0,1)`; it decreases from `+∞` to `−∞` on each exterior interval. The other coordinates are also invertible: once `x` is recovered, `t=θ+F_I(x)` and `y=(1−τv)/b`.

These coordinates put the **entire contact form on each strip** into the standard form

`α=τ(dθ+(v/b)dx)+((1−τv)/b)dx=τdθ+du`.

Thus `R=∂u`, not merely to first order near an orbit. Its contact-volume measure satisfies the exact absolute-Jacobian identity

`dμ=|α∧dα|=dt dx dy/v=dθ dτ du`.

One can check the latter directly from `|∂y/∂τ|=v/|b|` and `|dx|=|b|du`. There is no omitted density or finite-volume approximation. These coordinates show completeness on the three strips; the explicit exponential flow on the two remaining planes is also complete.

The invariant planes `x=0,1` have zero contact-volume measure. Consequently, for **the full scalar Hilbert space**, not merely a selected subspace,

`L²(Y,dμ) ≅ ⊕_(I=1)^3 L²(S¹_θ×R_τ×R_u,dθ dτ du)`.

Under this unitary identification, the scalar Koopman group `U_s f=f∘φ_(−s)` acts by `f(θ,τ,u−s)`. With `U_s=exp(−isD)`, its self-adjoint generator is

`D=⊕_(I=1)^3 (−i∂u)`.

Its domain is the direct sum of vector-valued Sobolev spaces `H¹(R_u;L²(S¹_θ×R_τ))`: equivalently, `f` and its weak `u` derivative are square-integrable, or `∫ ξ²|f̂(θ,τ,ξ)|² dθ dτ dξ<∞`. Fourier transformation in `u` identifies `D` with multiplication by the real variable `ξ`. Hence its spectrum is all of `R`, purely absolutely continuous, with infinite multiplicity and **no L² eigenvalues**. The periodic circles are measure-null and do not become scalar Hilbert-space eigenvectors.

This is the first exact obstruction to the naive scalar spectral bridge. Self-adjointness does hold here, but it produces a translation spectrum, not a discrete sequence attached to zeta zeros. The flow operators are unitaries on an infinite-dimensional space and therefore not trace class. A nonzero time-smearing remains a Fourier multiplier with an infinite transverse multiplicity; it is not an ordinary trace-class repair. Infinite measure does not prohibit a spectral measure: the explicit absolutely continuous spectral measure above is exactly what this realization supplies.

## The weighted flat-trace proposal is a different object

The transverse linearizations at the two circles have eigenvalues `+1,−1` per unit Reeb time, so the return multipliers remain `exp(±T)` for `T=log 2,log 3`. Local hyperbolic germs can therefore retain the proposed half-density weights and graded repetition coefficients. That does not identify their local distributional flat trace with the scalar trace, which does not exist in the ordinary trace-class sense.

There is also a concrete global-bundle issue. The vertical contact line `span(∂y)` is globally invariant under the derivative flow, but it is stable at `γ₂` and unstable at `γ₃`. It cannot be designated the common unstable line. The desired unstable covector half-density is defined by the hyperbolic germs on the two trapped circles; a global invariant extension, its transport law and its closed functional realization have not been supplied. This is an omitted construction, not a proof that every such extension is impossible.

A different, **ad hoc global smooth transport already exists**: on compactly supported horizontal exterior forms tensored with a trivial line, set `V_s=e^(−s/2)φ_(−s)*`. Completeness of the flow makes this well defined and preserves horizontality; its infinitesimal expression is `−Lie_R−1/2`. Its compact-spatial-cutoff flat supertrace, with time support away from zero and cutoffs equal to one near both circles, has the two desired local prime-block coefficients. This construction is a scalar weight, not the as-yet-unconstructed natural global unstable half-density. It should not be reported as absent, nor as a positive ordinary trace.

For this finite two-orbit distribution its Laplace series also has an elementary meromorphic continuation:

`−Σ_(j=0,1) T_j Σ_(m≥1) exp(−(z+1/2)mT_j) = −Σ_(j=0,1) T_j/[exp((z+1/2)T_j)−1]`,

initially for `Re z>−1/2`. Meromorphic continuation of this explicit scalar function is not a Fredholm/operator identity and supplies neither the infinite-prime limit nor the original archimedean completion.

The remaining weighted/anisotropic obligation is a closed **analytic** realization: its functional spaces, generator domain, allowable growth at every end, and a justified spectral/trace/Fredholm identification. The exterior-degree grading used in a supertrace is not the even/odd parity of the original Weil test functions. Neither scalar self-adjointness nor the constructed signed local trace supplies that missing identification.

## Arithmetic independence and the exact conditional edge

Replace `log 2,log 3` by any distinct positive real periods `T₀,T₁`, setting `a=1/T₀,c=1/T₁`. All the constructions, noninteraction argument, contact straightening and scalar spectral conclusions survive. Local weights become `exp(−mT_j/2)`; primality has not been used. This is an exact period-label control of these geometric identities, not a false-RH analogue. The two selected Euler factors are input, and the full set of primes and the archimedean completion remain absent.

The proposed eventual implication must be:

1. Construct the required closed analytic realization of the available smooth transport, or specify another geometric realization, and prove its full explicit-formula identity, including both time directions, all prime powers, original gamma factor, poles, trivial-zero/zero-time regularization, exterior terms and multiplicities.
2. For every `A` in a cofinal family, construct maps on the **actual** domains `D(q_A)^even∩u_A^⊥` and `D(q_A)^odd` giving `q_A[f]=||B_A J_A f||²+E_A[f]`, with `E_A[f]≥−C||f||²` for one finite `C` independent of `A` and parity. All cross terms and complete-domain extensions must be justified.
3. Supply the established source transfer to the full form with its hypotheses intact; then invoke v1.36's registered common-floor implication to RH.

Every substantive transfer/estimate in this chain remains missing. The local construction has supplied neither `J_A` nor `B_A`, no arithmetic error bound, and no source/parity map. NS47 still bars identifying a proposed global ordinary-L² closable square with the full Weil form plus a bounded remainder under its stated hypotheses. No positive spectral gap is required by the actual floor target, and absence of such a gap is not its refutation.

**Decision:** the connected geometric prerequisite and an ad hoc smooth weighted transport are concrete; stop the naive scalar-L²/discrete-spectrum inference. Any continuation must supply the required closed analytic/form/scattering realization and its completed transfer, rather than infer them from connectedness, an elementary meromorphic function or local orbit coefficients. **Final wall check: Same open gap**, OPERATOR-BRIDGES and WEIL-FLOOR; a scoped scalar-realization failure has been identified, not a general geometric closure.

## Bounded cross-check

The symplectic-lane agent independently confirmed `u′=1/b`, the three onto coordinate maps, the conserved-momentum noninteraction, and the exact strengthening `α=du+τdθ`. It agreed with the resulting scalar translation decomposition and its stated scope. This is a check of the displayed construction, not an audit of historical proofs or a global weighted trace theorem.

That review also distinguished the available ad hoc scalar-weighted smooth transport from the missing natural unstable-line construction; the distinction and the elementary finite-two-prime Laplace continuation are explicitly incorporated above. The parent's separate exact-algebra check reports 25 passed identities; this note does not recast those checks as a global analytic theorem.
