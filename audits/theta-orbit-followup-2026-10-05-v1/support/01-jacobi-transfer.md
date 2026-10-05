# Assistant 1 — transporting Jacobi dynamics to the complete signed target

Reviewed baseline: `33bda7f04a34e49f578c666b7f8953a8ca09c3c4`, refreshed by the coordinator. Read the current agent rules, shared brief, applicable NS100/101 register scopes and yesterday's arXiv-method note. This is a paper transfer audit, not a source-certificate replay or a new theorem claim. No computation was run.

**Wall check: Same open gap.** Closest: NS100/101, ZERO-GEOMETRY. What changes: explicitly transport the distinguished Jacobi ODE through both shifted factors and integrate its first differential identity. This exposes a definite signed moment needing control; it supplies no bound for that moment. The original ODE and its initial value are more specific than reflection symmetry, but have not yet been used in an estimating inequality.

## The source and its actual scope

[Planat–Sole, arXiv:2608.19160v1](https://arxiv.org/html/2608.19160v1), Section 5, gives the distinguished theta trajectory, with derivatives in the clock L:

```text
a'=(U+a^2-1)/2,  U'=2U(a+chi),  chi'=a*chi-U,
a(0)=chi(0)=0, U(0)=Gamma(1/4)^8/(64*pi^4).
A=pi*exp(L)*theta_3(exp(L))^4, A'/A=a,
Phi(L/4)=A^(1/4)*(U+3*(a^2-1)/2)/(8*pi^(1/4)).
```

Its main theorem is a second-level real kernel-concavity result, not transform positivity. I read the orbit definition, factorization, real-domain signs and theorem scope, but did not independently validate its supplied interval certificates. The paper's clock and our kernel obey `phi(u)=Phi(u/2)`, hence `L=2u`; using `L=4u` here would be incorrect.

## Carrying the two factors, without dropping the oscillation

Write `G(L)=log Phi(L/4)`, `P=G'`, and `P_1=P'`. Let V be the displayed three-variable autonomous vector field. To avoid confusing the paper's U with a kernel, define

```text
d=U+3*(a^2-1)/2,
P=a/4 + [2*U*(a+chi)+(3*a/2)*(U+a^2-1)]/d.
```

Thus `P_1=V(P)` along the actual orbit. The positive kernel makes this division legitimate at every finite real clock. Evenness extends G evenly and P oddly to negative L; this matters when `t>p`.

For `p,t>=0`, let

```text
K(p,t)=phi(p+t)*phi(p-t),
P_plus=P(2*(p+t)), P_minus=P(2*(p-t)),
A_p(r)=int_0^infinity K(p,t)*cos(2*r*t) dt.
```

The chain rule, including both clock factors of two, gives

```text
K_p=2*(P_plus+P_minus)*K,
K_t=2*(P_plus-P_minus)*K,
K_pp-K_tt=16*P_plus*P_minus*K.                 (1)
```

Here subscripts on K mean derivatives; the subscript on A labels the shift. Both second derivatives individually contain
`4*(P_1_plus+P_1_minus)*K`, which cancels in their difference. Nothing has been approximated by a first summand.

Define the newly weighted signed moment

```text
B_p(r)=int_0^infinity P_plus*P_minus*K(p,t)*cos(2*r*t) dt.
```

Two integrations by parts in t give the exact audit identity

```text
d^2 A_p(r)/dp^2 + 4*r^2*A_p(r) = 16*B_p(r).  (2)
```

The boundary from the first integration is `K_t*cos(2rt)`; that from the second is `2*r*K*sin(2rt)`. Both vanish at infinity by the complete theta decay. At zero, `K_t(p,0)=0` and `sin(0)=0`. There is no cut at `t=p`: the even theta kernel and its derivatives are smooth there. Formula (2) includes `r=0` and `p=0` by continuity.

For the requested complete expression, put `w(p)=p*sinh(2xp)`. Integrating (2) over p retains

```text
w''=4*x*cosh(2xp)+4*x^2*w,
w(0)=w'(0)=0,
|f(x+ir)|^2=8*int_0^infinity cosh(2xp)*A_p(r) dp.
```

All upper boundaries vanish at each fixed finite x,r by theta decay. Consequently,

```text
(x^2+r^2)*J(x,r)
 = 32*int_0^infinity p*sinh(2xp)*B_p(r) dp
   - x*|f(x+ir)|^2.                           (3)
```

These identities hold, in particular, throughout `0<x<1/2`, every `r>=0`, with complete integrals. They are supporting calculus identities, not an arithmetic lower bound.

## Exactly where the attempted evolution stops

The pointwise pair of Jacobi states is a closed six-dimensional system before integration. But differentiating the integrated moment introduces a further moment:

```text
dB_p/dp = 2*int K * [
 (P_plus+P_minus)*P_plus*P_minus
 + P_1_plus*P_minus + P_plus*P_1_minus
] * cos(2rt) dt.                              (4)
```

The original ODE makes every factor in (4) explicit. It does not express this integral as a known combination of A and B or bound it with a useful sign. More generally, for a state function R, p differentiation sends the moment of R to twice the moment of
`(V_plus+V_minus)R+(P_plus+P_minus)R`. No finite invariant space of these integrated observables, with a sign-preserving evolution, has been identified in the supplied argument. This is a limitation of this attempted closure, not a proof that all closures are impossible.

Moreover, the real-coordinate sign `P(L)<0` for L>0 makes `P_plus*P_minus` positive for `0<=t<p` and negative for `t>p`. The cosine changes sign as well. Pointwise orbit bounds therefore cannot simply be integrated as lower bounds against this weight. An absolute error estimate must be compared against the complete signed target, including its potentially tiny values.

## Missing estimate, controls, and disposition

The precise missing estimate from this attempted transport is

```text
32*int_0^infinity p*sinh(2xp)*B_p(r) dp
 >= x*|f(x+ir)|^2,
for every 0<x<1/2 and every r>=0.              (5)
```

By (3), (5) is equivalent to the original J sign in this range. Stating (5) alone is not a candidate: no independent estimating method for it emerged. The chain-rule identities hold for generic smooth positive even kernels; actual arithmetic enters only through restricting P to the distinguished Jacobi orbit. The necessary step is a signed, two-shift oscillatory estimate using that restriction.

NS100 rules out replacing this by positivity of every A slice. NS101's reciprocal-mixture control does not preserve the specified original theta trajectory or initial data, so it does not exclude an eventual Jacobi-specific estimate. Its already recorded missing derivative comparison is the closest dependency. Davenport–Heilbronn likewise has different theta data; NS74/83 are NB controls with different hypotheses, not direct restrictions here. No numerical control pass is claimed.

**No five-item candidate survives.** The useful output is (2)–(4), which identify the unestimated moment and its next derivative. Do not fund a larger orbit scan from these identities. Reopen only upon an independently justified bound for (5), or a weaker explicit companion estimate that demonstrably implies the original target. No row, thaw, version, outreach or push.
