# Agent 3 — smooth modular completion and the missing sign margin

Reviewed mathematical baseline: `5434d96f0034f842b0229f1d69dbbf3fb7fea270`
(merged PR73). Working-tree HEAD when read:
`971c8bd02c834cf31ab98ea2a50060289fbece40` (the coordinator's audit-scope
record). The coordinator refreshed the remote and reviewed the complete
104-node register, checkpoints, freezes and missing-evidence ledger. This
lane read the current agent instructions, proposal gate, ZERO-GEOMETRY
scope, NS100/101 arguments, PR72's source/transfer notes, PR73's current
report, and the September 29 Jacobi-product admission report. This is a
paper applicability/error-budget audit, not a replay of historical proofs
or certificates. No numerical or symbolic scan was run.

**Wall check: Same open gap.** Closest results: NS101, PR72/73 and the
September 29 product audit. What changes: a particular smooth reciprocal
completion permits an explicit, uniform-in-height error comparison; it
has no reflected-prefix cusp. What does not change: no independently
proved lower bound for the complete first Laguerre expression is supplied.
The completion below is a supporting comparison, not an admitted sign
method or a thaw of ZERO-GEOMETRY.

## Exact question and dependency

Can a smooth completion of the original theta coefficients both evade
PR73 and transfer a lower first-Laguerre bound to the original function?
Write

```text
Theta(x) = sum_(n in Z) exp(-pi*n^2*x),
h(u) = exp(u/2)*Theta(exp(2u)),
D = (d^2/du^2 - 1/4)/4,
phi = D h,
X(r) = integral_R phi(u)*exp(i*r*u) du,
L1[X] = X'^2-X*X''.
```

The exact dependency will be

```text
L1[X_M](r) >= B_M(r) for every real r, with the specified complete
error B_M (or a pointwise choice M=M(r))
  => L1[X](r)>=0 for every real r
  => positive definiteness of the complete associated kernel C.
```

This is only the first-Laguerre target, not the all-order criterion or RH.
The lower-reference inequality on the first line is absent. The work
below makes the error and the missing lower margin explicit; it does not
rename that margin an estimate.

## 1. A specified completion, including the weight derivatives

Fix `a=pi/4` (a completion parameter, unrelated to the Jacobi state a),
and define for integers `M>=1`

```text
H_M(u) = exp(u/2)*(1+2*sum_(1<=n<=M) exp(-pi*n^2*exp(2u))),
w(u) = 1/(1+exp(-2*a*sinh(2u))),
h_M(u) = w(u)*H_M(u)+w(-u)*H_M(-u),
phi_M(u) = D h_M(u),
X_M(r) = integral_R phi_M(u)*exp(i*r*u) du.
```

All derivatives of w are included in `D h_M`. This is not reflection of
a half-line differential kernel and not the finite Jacobi-product object
from September 29. Because `w(u)+w(-u)=1`, h_M is even and smooth. It is
holomorphic in a neighborhood of the closed strip `|Im u|<=pi/8`, as
verified below. Thus every odd boundary derivative vanishes. There is no
distributional atom at zero and no algebraic cusp tail of PR73's kind.

In the limited sense of reciprocity, it is a modularly compatible
completion: `Theta_M(x)=x^(-1/4)*h_M((log x)/2)` satisfies
`Theta_M(x)=x^(-1/2)*Theta_M(1/x)`. It is **not** claimed to satisfy every
theta modular law, to be a one-lattice Gaussian series globally, or to
solve the original normalized nonlinear Jacobi initial-value problem.

The complete original remainder is retained exactly:

```text
T_M(u) = h(u)-H_M(u)
       = 2*exp(u/2)*sum_(n>M) exp(-pi*n^2*exp(2u)),
Delta_M(u) = h(u)-h_M(u)
           = w(u)*T_M(u)+w(-u)*T_M(-u),
phi-phi_M = D Delta_M.                                      (1)
```

Here the second equality uses the original theta reciprocity `h(-u)=h(u)`.
Both modular tails in (1) matter. In particular, the negative-u evaluation
of a finite original sum cannot be silently replaced by the even original
kernel. The original coefficients and n-squared frequencies enter the
estimates of T_M below; the completion operation alone is generic and
contains no arithmetic sign information.

At both real infinities h_M has leading homogeneous mode `exp(|u|/2)`;
its corrections and their differentiated versions have double-exponential
decay. Therefore phi_M is a smooth, real, even, rapidly decreasing
function. The endpoint normalization is retained, rather than assumed:

```text
integral_R exp(u/2)*phi_M(u) du
 = (1/4)*[exp(u/2)*(h_M'(u)-h_M(u)/2)]_(-infinity)^(infinity)
 = (1/4)*(0-(-1)) = 1/4.                                   (2)
```

The negative endpoint in (2) is essential. Evenness supplies the same
normalization at Laplace parameter -1/2. These facts do not assign a sign
to phi_M or to L1[X_M].

## 2. A necessary warning: this completion has a negative far tail

For each fixed M and real `u->+infinity`, set `y=exp(2u)`. Direct expansion
of the finite sum and of w gives

```text
H_M(u) = exp(u/2)*(1+O_M(exp(-pi*y))),
H_M(-u) = (2*M+1)*exp(-u/2)*(1+O_M(1/y)),
w(-u) = exp(-a*y)*(1+O(1/y)),
h_M(u)-exp(u/2)
 = -exp(u/2)*exp(-a*y)*(1+O_M(y^(-1/2))).                  (3)
```

The remainders come from differentiable exponential/power expansions, so
applying D preserves the leading term and yields

```text
phi_M(u) ~ -a^2*exp(9*u/2)*exp(-a*exp(2u)) < 0.             (4)
```

The original phi is positive on the real line. Its exact remainder in
(1) cancels this slower, negative artificial tail (`a<pi`). This explains
why an argument importing positivity or real logarithmic curvature of the
original Jacobi orbit into phi_M would be invalid. In particular the
source's P=logarithmic-slope variables cannot be carried globally through
a sign-changing phi_M as if it were the original positive orbit.

Equation (4) is **not** a proof that L1[X_M] is negative anywhere; kernel
sign and transform first-Laguerre sign are different questions. We do not
replace one unproved sign by the other. The negative tail also does not
invalidate the absolute approximation bound below.

## 3. Explicit strip and complete-tail estimate

The following elementary estimate supplies an actual error rate. Define

```text
v = pi/8,
B = pi/sqrt(2),
d = pi/(4*sqrt(2)),
beta = pi/(2*sqrt(2)),
J(u) = exp(u/2)*exp(-(B/2)*exp(2u))
     + exp(a)*exp(-u/2)*exp(-(d/2)*exp(2u)),     u>=0,
C_j = [8/(1-exp(-beta))] * integral_0^infinity (u+v)^j*J(u) du,
                                                        j=0,1,2.
```

These are explicit finite positive constants, independent of r and M.
They are defined by convergent elementary integrals, not fitted or
numerically evaluated constants.

Here is the denominator check for the weight. For `z=u+i*eta`, `u>=0`,
`|eta|<=v`, put `q=exp(-2*a*sinh(2*z))` and

```text
u_* = (1/2)*asinh(log(2)/(2*a*cos(2*v))).
```

For `u>=u_*`, `|q|<=1/2`, so `|1+q|>=1/2`. For `0<=u<=u_*`,

```text
|arg q| <= sqrt(pi^2/8 + log(2)^2) < pi/2
```

using the continuously specified exponent argument, hence `Re q>=0`
and `|1+q|>=1`. Consequently, throughout that half-strip,

```text
|w(z)|<=2,
|w(-z)|<=2*exp(-2*a*sinh(2*u)*cos(2*eta)).                 (5)
```

This proves the required absence of poles and provides an explicit bound,
rather than treating smoothness on the real axis as a complex-strip bound.

Let `y=exp(2u)>=1`, `b=pi*cos(2*eta)>=B` and
`d_eta=a*cos(2*eta)>=d`. From (1) and (5),

```text
|Delta_M(u+i*eta)|
 <= 4*y^(1/4)*sum_(n>M) exp(-b*n^2*y)
  + 4*exp(a)*y^(-1/4)*sum_(n>M) exp(-d_eta*y-b*n^2/y).
                                                               (6)
```

For the first sum, `n^2*y>=(n^2+y)/2` and `n^2>=n` give a factor
`exp(-beta*n)*exp(-(B/2)*y)`. For the second, split its exponent in
halves and use

```text
(d_eta*y+b*n^2/y)/2 >= sqrt(d_eta*b)*n >= beta*n.
```

In the remaining half discard only the additional nonnegative
`b*n^2/(2*y)`. Summing the geometric majorant gives

```text
|Delta_M(u+i*eta)|
 <= [4/(1-exp(-beta))]*exp(-beta*(M+1))*J(u).               (7)
```

Evenness supplies the same bound with `|u|` on the other half-strip. Thus
there are no omitted real tails or internal endpoint pieces.

Let `Dhat_M(r)=integral_R Delta_M(u)*exp(i*r*u) du`. Contour shifting to
`Im u=sign(r)*v`, justified by (7) on the vertical boundaries, yields

```text
|Dhat_M^(j)(r)|
 <= C_j*exp(-v*|r|-beta*(M+1)),       j=0,1,2, r real.       (8)
```

The factor `(u+v)^j` above bounds `|u+i*v|^j`. At r=0 the same inequality
follows by shifting either way or by continuity. This is a uniform
all-height estimate for a specified approximation error. It is not an
all-height lower bound.

## 4. Transfer to X, X', X'' and L1

Because Delta_M and its derivatives decay at both ends, integrating D in
(1) produces no boundary term:

```text
E_M(r) := X(r)-X_M(r) = -(r^2+1/4)*Dhat_M(r)/4.             (9)
```

Put `p=r^2+1/4`, `q_M(r)=exp(-v*|r|-beta*(M+1))`, and

```text
S_0(r) = p*C_0/4,
S_1(r) = (2*|r|*C_0+p*C_1)/4,
S_2(r) = (2*C_0+4*|r|*C_1+p*C_2)/4,
epsilon_j(r,M) = S_j(r)*q_M(r).
```

Differentiating (9), rather than an upper envelope, proves

```text
|X^(j)(r)-X_M^(j)(r)| <= epsilon_j(r,M),   j=0,1,2,          (10)
```

for **every real r and every integer M>=1**. Every r derivative is at
fixed M. A later selection M(r) is pointwise selection among these
inequalities; one must not differentiate the discontinuous composite
`X_(ceil(r))(r)` and call those derivatives `X_M'` or `X_M''`.

Expansion of the complete quadratic expression gives the explicit
conditional transfer

```text
|L1[X](r)-L1[X_M](r)| <= B_M(r),

B_M = 2*|X_M'|*epsilon_1 + epsilon_1^2
    + |X_M|*epsilon_2 + |X_M''|*epsilon_0
    + epsilon_0*epsilon_2.                                (11)

L1[X_M](r) >= B_M(r)  =>  L1[X](r)>=0.                    (12)
```

The cross terms in (11) are indispensable. Small transform error alone
is not a sign-transfer argument.

One can remove unknown transform values even from the upper error bound.
For `j=0,1,2` define the explicit original-theta majorants

```text
A_j = 2*integral_0^infinity (u+v)^j *
      sum_(n>=1) [2*pi^2*n^4*exp(9*u/2)
                  +3*pi*n^2*exp(5*u/2)]
                 *exp(-B*n^2*exp(2*u)) du.
```

These constants converge, and shifting the original smooth theta kernel
in the same strip proves `|X^(j)(r)|<=A_j*exp(-v*|r|)`.
Expanding the difference in terms of X and E_M instead of X_M gives the
alternative fully specified upper error

```text
Btilde_M(r)
 = [2*A_1*S_1 + A_0*S_2 + A_2*S_0]
     *exp(-2*v*|r|-beta*(M+1))
   + [S_1^2+S_0*S_2]
     *exp(-2*v*|r|-2*beta*(M+1)),                          (13)

|L1[X]-L1[X_M]| <= Btilde_M.
```

There is no lower-sign estimate hidden in the definition of A_j.
In particular, choosing `M(r)>=ceil(|r|)+M_0`, `M_0>=1`, gives

```text
Btilde_(M(r))(r)
 = O((1+r^2)*exp(-(pi/4+beta)*|r|-beta*(M_0+1)))
 + O((1+r^2)^2*exp(-(pi/4+2*beta)*|r|-2*beta*(M_0+1))),    (14)
```

with constants already specified in (13). Both rates are faster than
`exp(-pi*|r|/2)`, since `beta>pi/4`. This illustrates how a growing,
smooth completion could have adequate *absolute error rate*. It proves
neither a useful lower scale nor nonnegativity of the reference expression.

For example, if an independent argument supplied

```text
[L1[X_M]](r) evaluated at M=M(r)
 >= m*(1+|r|)^(-k)*exp(-pi*|r|/2),   every |r|>=R,
```

for explicit `m>0`, finite k and R, (13) would give an explicit eventual
transfer threshold; the remaining compact interval would still require
its own complete proof. No such premise is proved here. A strict margin
also requires care around possible vanishing of L1: an arbitrary positive
absolute allowance cannot transfer a zero margin. Even an all-height
nonnegative-reference theorem by itself would not establish (12).

## 5. Why the original nonlinear trajectory does not finish (12)

For the actual theta kernel the clock is `L=2u`, and the distinguished
Jacobi state satisfies

```text
a'=(U+a^2-1)/2, U'=2*U*(a+chi), chi'=a*chi-U,
a(0)=chi(0)=0, U(0)=Gamma(1/4)^8/(64*pi^4).
```

The retained original remainder makes the complete phi exactly this
kernel. It therefore retains the original odd-derivative cancellation,
the nonlinear trajectory, and both factors of C. The finite h_M has only
the declared reciprocal symmetry and endpoint normalization; (4) already
shows that the source's positive-kernel real-orbit hypotheses do not
transfer to it. Replacing (12) by real monotonicity of the original state
would again drop the signed oscillatory comparison.

The source [Planat–Sole, arXiv:2608.19160v1](https://arxiv.org/html/2608.19160v1),
Sections 5 and 7, distinguishes the original Jacobi orbit and gives
real-coordinate curvature/Turán conclusions. Its quoted theorem is not
an all-frequency lower bound for the Fourier first-Laguerre expression.
No external finite certificates were replayed here. The classical
associated-kernel/Laguerre setting is also explicit in
[Csordas, arXiv:1309.0055](https://arxiv.org/abs/1309.0055); a new completion
does not create a new criterion.

The analysis above uses original arithmetic to control a complete
approximation error. It does **not** use the nonlinear arithmetic to
estimate the missing lower-reference sign. This distinction is precisely
why the output remains a supporting comparison rather than a candidate
for admission.

The coordinator's separately reviewed Bessel reference is a different
object. Nothing above estimates `X-B_a` or its first two derivatives
relative to a Bessel Laguerre margin. A positive first-Laguerre formula
for that reference cannot be substituted for the missing lower bound for
X_M in (12). This lane supplies no all-height original-theta-to-Bessel
comparison.

## 6. Matched controls and overlap

- **PR73:** its hypothesis is an even-reflected fixed finite half-line
  theta sum with a nonzero odd boundary derivative. This h_M is smooth
  even before D is applied, so that cusp theorem does not apply. This is
  an explicit hypothesis change, not a larger M in the rejected family.
- **September 29 finite Jacobi product:** that completion has a retained
  atom at zero and a different differential density. Its negative
  radial-sign diagnostic does not decide the smooth family above, and a
  radial sign away from the imaginary axis is not the same as first
  Laguerre at x=0. Its normalization warning is addressed by (2), not by
  dropping an endpoint.
- **NS101 reciprocal mixture:** it shares smooth reciprocal completion
  and general transform calculus but changes the exact Gaussian lattice
  and fails the original normalized Jacobi ODE (PR72). The general
  error-transfer lemma would apply whenever analogous error hypotheses
  were proved. Such a lemma is permitted to be generic; the missing sign
  premise is separate. The mixture's off-axis zeros do **not** by
  themselves prove failure of its first-Laguerre sign, and none is claimed.
- **NS100:** its original complete negative slice excludes per-slice
  positivity, which is never assumed in (11). Its log-concave control
  lacks the original theta data and cannot be imported as a
  first-Laguerre counterexample merely from its radial-sign failure.
- **Davenport–Heilbronn:** its conductor, coefficients and gamma/theta
  law differ from the original integer-square theta input used in (1),
  (6) and the Jacobi IVP. It is not a matched counterexample to those
  original-data premises. The generic perturbation inequality is valid
  for it too if its error hypotheses hold; it never supplies its sign.

This is an analytic admission/scope assessment. No control scan, sampled
pass or new numerical sign claim is recorded.

## Disposition and bounded next budget

**No admitted sign method emerges.** We have an explicit cusp-free
reciprocal approximation with all-height error bounds (10) and (13),
complete endpoint normalization, and a warning that its real differential
kernel has a negative artificial tail. Constructing and accurately
approximating the complete original object is therefore separable from
estimating its sign. The missing lower bound in (12) is still the
NS100/101 full first-Laguerre comparison.

Success of a future independent lower-reference estimate meeting (12),
with all heights and any zero margins addressed, would prove the stated
first-Laguerre target only. Failure for this smooth reference family would
stop that comparison; it would not close smooth completions or the exact
original nonlinear evolution generally. There is currently no reason to
fund a height/M scan. A bounded next step, only if this comparison is
needed by another specified estimating method, is a one-hour independent
paper check of (5)–(13) and of the proposed method's actual lower-margin
hypothesis. No automatic search of adjacent weight parameters is proposed.

**Final wall check: Same open gap.** The supporting approximation rate is
explicit; the complete arithmetic sign remains unestimated. No research
row, manuscript change, computation, commit, push or outreach. RH, G2 and
the cofinal signed-arithmetic lower bound remain open.
