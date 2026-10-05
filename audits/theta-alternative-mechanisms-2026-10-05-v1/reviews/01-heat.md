# Review 01 — auxiliary heat transport exposes a subtractive source

**Decision: no estimating candidate admitted.** The auxiliary heat equation
does give an exact transfer from a known positive parameter to zero. Its
unestimated source has the adverse sign in that direction. The resulting
integral comparison, without a separate arithmetic bound, is exactly the
original first-Laguerre obligation. This is not a closure of heat methods.

**Wall check: Same open gap.** Closest: NS100/101, PR77 review 02 and PR78's
admission assessment. What changes: an actual Gaussian deformation replaces
the unsupported identification of the Jacobi clock with heat. No new signed
arithmetic estimate results. NS52 concerns a different, same-test spectral
transport comparison; its conditional obstruction does not settle this one.

Reviewed baseline: `221ceec9da825bdc787111447badad961860760a`; scope commit:
`b5147e82803cccdb641bcb611b3c90c3c76cf51e`. Read AGENTS, the commissioned
brief/review record, PR77 reviews 02/07/09, PR78 review 06 and the relevant
HEAT-TRANSPORT scope. The coordinator owns the full-register review. This is
an independent paper derivation, not historical proof or certificate replay.
Both missing-original evidence groups remain OPEN.

## 1. Exact family, parameter and positive endpoint

Keep the complete original integer-square theta coefficients, their even
kernel phi, and define

```text
H_a(r) = integral_R exp(a*u^2)*phi(u)*exp(i*r*u) du,
H_0=X=xi(1/2+i*r)/2,
Q_a=H_a'^2-H_a*H_a'',
S_a=H_a''^2-H_a'*H_a''',
J=16 Q_0.
```

Primes denote r derivatives. The double-exponential decay of phi, with all
derivatives, justifies parameter and r differentiation uniformly on compact
a intervals, with Schwartz functions on the real r line. No zero is divided
out. The target is Q_0(r)>=0 for every real r, not RH.

This a is an **auxiliary Gaussian parameter**, not the original nonlinear
Jacobi clock L=2u. The coefficients are original at every a, but the weight
exp(a*u^2) changes the function under study. A relation between these clocks
is neither assumed nor obtained.

For normalization, [Polymath, arXiv:1904.12438v2, equations (1), (3), (4)
and introduction](https://arxiv.org/html/1904.12438v2) uses a half-line kernel
Phi(v)=phi(2v). Thus `H_a(r)=4*H_lit,4a(2r)`. The recorded unconditional
real-zero result at literature parameter >=1/2 supplies `Q_A>=0` at
`A=1/8`. Reality of zeros for this real entire order-one function gives the
ordinary Laguerre inequality, including multiple zeros by continuity. We
use no strict margin or simplicity. Smaller available positive endpoints
would shorten the interval but would not remove its source estimate.

## 2. Correct evolution and complete conditional transfer

Direct differentiation, retaining the fourth derivative, gives

```text
partial_a H_a = -H_a'',
partial_a Q_a = H_a*H_a''''-2*H_a'*H_a'''+H_a''^2,
Q_a'' = H_a''^2-H_a*H_a'''',
partial_a Q_a = -Q_a''+2*S_a.                         (1)
```

More generally, `Q_(k,a)=L1[H_a^(k)]` satisfies
`partial_a Q_(k,a)=-Q_(k,a)''+2*Q_(k+1,a)`. There is no scalar
homogeneous heat closure for Q. Positivity of a higher expression is not
automatically favorable when going toward a=0.

Put tau=A-a. Then H follows forward ordinary heat in tau, whereas Q follows
`partial_tau Q=Q''-2*S`. Let

```text
G_a(r)=(4*pi*a)^(-1/2)*exp(-r^2/(4*a)), a>0,
G_0*F=F.
```

Duhamel's formula, justified in the Schwartz class, gives the exact identity

```text
Q_0(r) = (G_A*Q_A)(r) - 2*integral_0^A (G_a*S_a)(r) da.       (2)
```

Accordingly the complete sufficient comparison is

```text
2*integral_0^A (G_a*S_a)(r) da <= (G_A*Q_A)(r), every r in R.  (3)
```

Its five-item specification would be: expression (3); fixed original phi
with all coefficients and tails; all real r and every intermediate
0<=a<=A=1/8; an original-coefficient **upper estimate for the accumulated
signed source relative to the known endpoint**; and (2), followed by
J=16Q_0. There is no missing analytic boundary or zero-neighborhood transfer
in that implication. The fourth item is the absent estimating method,
however, not something supplied by writing a heat equation. By (2), (3)
itself is equivalent to the target, so naming it is not a candidate.

## 3. Why the immediate estimating attempts do not qualify

First, discarding the source would reverse its relevant sign. At r=0,
evenness gives

```text
S_a(0)=H_a''(0)^2
      =[integral_R u^2*exp(a*u^2)*phi(u)du]^2 > 0.
```

Thus `S_a<=0`, the simple favorable-source hypothesis, is false for the
original kernel. A bare forward-heat preservation claim for the Laguerre
cone is also false: `F_tau(r)=r^2-1+2*tau` solves forward heat and has
`L1[F_tau]=2*r^2+2-4*tau`, which turns negative. This polynomial is only a
control of that generic assertion, not an original-theta analogue.

Second, attempting `S_a<=b(a,r)*Q_a` with a locally bounded potential would
need a separate arithmetic inequality and would conceal a multiplicity
restriction if imposed all the way to zero. At a zero of H_a of order m>=2,
with H_a=c*x^m+O(x^(m+1)),

```text
Q_a = m*c^2*x^(2m-2)+O(x^(2m-1)),
S_a = m^2*(m-1)*c^2*x^(2m-4)+O(x^(2m-3)),
S_a/Q_a ~ m*(m-1)/x^2.
```

A locally bounded b cannot cover such a zero. No simplicity premise is
available for a=0. Singular potentials require their own transfer/domain
analysis; none is specified here.

Third, Gaussian smoothing does not turn the arithmetic source into a
positive coefficient sum. Symmetrizing the complete Fourier products gives

```text
(G_a*Q_a)(r)
 = (1/2)*int_R^2 (u-v)^2*exp(-2*a*u*v)*phi(u)*phi(v)
                    *exp(i*r*(u+v)) du dv,
(G_a*S_a)(r)
 = -(1/2)*int_R^2 u*v*(u-v)^2*exp(-2*a*u*v)*phi(u)*phi(v)
                    *exp(i*r*(u+v)) du dv.                    (4)
```

All integrals converge, including uv<0. The source changes sign between
uv>0 and uv<0, and the oscillatory factor remains. Integrating its a factor
in (2) cancels the endpoint weight exactly, leaving the original complete
quadratic integral for Q_0. Substitution of the theta series introduces the
original n,m arithmetic but estimates no cancellation. A phase-free absolute
bound obtained by deleting exp(i*r*(u+v)) produces a fixed positive budget,
while `G_A*Q_A` tends to zero as |r| tends to infinity. That particular
budget cannot prove the uniform comparison. More correlated estimates are
not excluded, but none has been supplied.

Prior art does not repair this step. [Csordas, arXiv:1309.0055v2,
equations (4.9)–(4.10), Proposition 4.9 and Open Problems 4.10–4.11](https://arxiv.org/html/1309.0055v2) explicitly studies this Gaussian flow.
The real-zero persistence is toward increasing deformation; the derivative
statements do not reverse that direction or provide (3). Its simplicity
conclusion is above the real-zero threshold, not at zero. Modern lower
bounds on the de Bruijn–Newman constant concern **all zeros**; they cannot
silently be assigned to a threshold for the first inequality alone.

## 4. Matched controls and disposition

NS101 shares smooth positive even kernels, complete decay, the exact heat
PDE, (1), (2) and (4). Its recorded negative Q_0 means its corresponding
source comparison (3) fails. We have not assumed or established positivity
at the same A=1/8 for that mixture. Original coefficients and the Jacobi IVP
differ; that mismatch is not a pass for an unproved source bound. NS100 only
excludes a per-slice positivity substitute, which is not used here.
Davenport–Heilbronn does not have the literal original kernel/completion;
a future generic source claim needs an appropriately matched control.
NS74/83 concern NB targets/rates and do not apply to this inequality.

**Stop:** no independent source-estimating technique survives. The useful
audit outcome is the exact adverse-source identity and its normalization,
not a new research estimate. Success of a genuinely supplied arithmetic
bound for (3) would prove the first-Laguerre target only; failure rejects
that bound. Budget exhausted: one paper review, zero scans, zero interval
certificates. No row, thaw, manuscript version, commit, outreach or further
agent was initiated. Only this assigned note was written.

**Final wall check: Same open gap.** RH, G2 and the cofinal signed-arithmetic
lower bound remain open.
