# Assistant 4 — independent audit of the Jacobi source chain

Reviewed baseline: `33bda7f04a34e49f578c666b7f8953a8ca09c3c4`. I read the shared brief, current agent rules, applicable ZERO-GEOMETRY register and frozen-input scopes, yesterday's arXiv-method review, today's Assistant 1 transfer note, and the source's Sections 1–5, 7–8 and Appendix A. The coordinator performed the full current-register review. This note is a bounded algebra/source-scope audit, not a historical proof replay or a validation of external certificates.

**Wall check: Same open gap.** Closest: NS100/101. What changes: check the actual theta normalization and differential chain before importing it into the two-shift integral. The checked identities are usable; the source does not supply the required all-frequency estimate for J. No candidate, computation, row, thaw or version follows.

## Exact question and source status

Does the real Jacobi flow in [Planat–Sole, arXiv:2608.19160v1](https://arxiv.org/html/2608.19160v1) justify the proposed transport to our signed transform target? Its stated result is second-level concavity of `s(t)=Phi(sqrt(t))`, through the first Laguerre expression `s'^2-s*s''`, for real `t>0`. The paper uses inherited first-level concavity and elliptic-ratio facts, exact differential reductions, a local modular certificate, compact cone/anchor certificates and a large-coordinate continuation. I have not independently replayed its directed Decimal intervals, rational positivity scripts or inherited theorem hypotheses. Thus I do not endorse its complete theorem as independently validated. No defect was found in the normalization and algebra checked below. This is narrower than “the paper is correct.”

## Independent normalization and nonsingular flow checks

Let `Y(x)=sum_(n in Z) exp(-pi*n^2*x)`, `x=exp(L)`, and set `h(L)=log Y(exp(L))`, `A=pi*exp(L)*Y(exp(L))^4`, `a=A'/A`, where primes mean L derivatives. Termwise differentiation on compact positive x intervals gives

```text
Phi(L/4)=x^(5/4)*(x*Y_xx+(3/2)*Y_x),
h'=(a-1)/4,
x*Y_xx+(3/2)*Y_x = (Y/x)*(a'/4+(a^2-1)/16).
```

Consequently, with `U=2*a'+1-a^2`, the factorization is

```text
Phi(L/4)=(A/pi)^(1/4)*(U+(3/2)*(a^2-1))/8.
```

There is no missing factor two here. Direct comparison with the repository's defining theta series gives `phi(u)=Phi(u/2)`: the source clock for our variable is **L=2u**, as Assistant 1 uses. The factorization is at finite real clock; parity extends the original kernel across negative L.

One qualification matters at the modular point. Put `V=a''+a^3-3*a*a'-a` and `chi=V/U`. From the definitions, `U'=2*U*(a+chi)`. Differentiating `A^2=4*(U+chi^2)` then gives only

```text
chi*(chi' - a*chi + U)=0.
```

Dividing by chi at L=0 would be invalid. The actual theta trajectory resolves this: with `m=theta_2^4/theta_3^4`, its elliptic identities imply

```text
U=A^2*m*(1-m), m'=-A*m*(1-m),
chi=A*(m-1/2), hence chi'=a*chi-U.
```

This is regular when `m=1/2` and chi=0. Equivalently, one may use the actual analytic orbit and continuation from nonzero chi. The squared Jacobi equation alone should not be silently substituted for that distinguished theta branch. The flow's use of the original theta data is concrete; mere reflection symmetry does not specify it.

## Curvature reduction and cone scope

I independently differentiated the clock change. To avoid collision with our entire function f, call the source Laguerre expression `ell=s_t^2-s*s_tt`. With `u=1/L`, `G=log Phi(L/4)`, `P=G'`, `P_j=G^(j+1)`, and `H=u*P-P_1`,

```text
ell = 64*u^2*exp(2*G)*H,
(log ell)_tt = 64*u^2 *
 [6*u^2-2*H-P_3/H-(P_2/H)^2].
```

These formulas require L>0 and H>0. In particular the normalized cone does not include L=0 by simply substituting infinity for u. The separate modular argument has a genuine domain role.

Substituting `H=-P_1*delta` and `u=(1-delta)*P_1/P` reproduces the quartic after multiplication by a positive factor. Its triangular shear is an algebraic coordinate change for fixed C; when C varies, differentiating the barrier must retain C'. The source does retain that derivative. I also checked `delta'=omega*(1-delta)*(alpha-delta)` from its definitions. I did not independently expand the full displayed contact polynomial or replay its interval cover. The cone is a real kernel-curvature barrier, not a sphere or cone containing complex zeros, and its real clock is not the transform frequency.

## Assistant 1's transfer passes the checked algebra

The two factors require clocks `2*(p+t)` and `2*(p-t)`, including negative clocks when t>p. Writing `K=phi(p+t)*phi(p-t)` and `P_plus/P_minus` for their logarithmic slopes, independent differentiation gives

```text
K_pp-K_tt=16*P_plus*P_minus*K.
```

The second-derivative P_1 terms cancel. Integrating against `cos(2*r*t)` gives `A_pp+4*r^2*A=16*B`; smooth evenness kills the t=0 derivative boundary. The independent change of variables in the full double integral gives `|f|^2=8*int cosh(2*x*p)*A_p dp`, so a second integration by parts yields

```text
(x^2+r^2)*J = 32*int p*sinh(2*x*p)*B_p dp - x*|f|^2.
```

The coefficients 16, 8 and 32, the minus sign, and the zero lower boundaries are consistent. Theta decay justifies the complete integrals at each fixed finite x,r. These identities do not create a lower bound: the product P_plus*P_minus changes sign across t=p, and the cosine is signed too.

## Disposition and one possible validation task

No five-item estimating candidate emerged. The missing dependency is a bound for the complete B moment, with the original theta trajectory, every `0<x<1/2` and every `r>=0`, strong enough to dominate `x*|f|^2`. Real-coordinate curvature does not supply it. NS100 blocks individual-slice positivity; NS101 does not exclude a future trajectory-specific estimate because its mixture does not preserve the specified theta ODE and data. NB controls have different hypotheses.

If the second-level concavity theorem is to become an actual premise of a specified downstream lemma, an admissible **source-validation** task is an independent Arb implementation of its finite local/cone/anchor statements, with exact symbolic checks and complete analytic tails. Budget one initial two-hour implementation-and-scope session, reporting incomplete work honestly; it cannot be described as an RH experiment. Without a downstream lemma that uses this curvature premise, I do not recommend funding that replay now. Assistant 1's present transport uses only exact theta calculus, so it does not need the unvalidated concavity theorem at all.
