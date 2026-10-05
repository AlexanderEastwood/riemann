# Decaying primitive: legitimate transforms, unchanged signed obligation

Reviewed commit: d93aaf6b8dbe1fcbebf6fff4f6d1f71d993f4208 (PR75).
**Wall check: Same open gap — ZERO-GEOMETRY, NS100/101, PR74/75.**

This is a bounded paper audit of PR75's transform-domain issue. No numerical
or symbolic scan, new sign candidate, research row, node, thaw, certificate
or manuscript version. The initial paper draft received twelve focused agent reviews, archived
in reviews/ and summarized in README.md. This is not a historical
proof/certificate replay. Both original-recovery groups
remain OPEN. The question is whether a decaying regularization makes PR75's
complete kernel manipulable without silently discarding a sign term.

## 1. An integrable primitive of the complete original kernel

Keep PR75's normalization, with a=1/2 fixed throughout:

```text
Theta(x) = sum_(n in Z) exp(-pi*n^2*x), x>0,
h(u) = exp(u/2)*Theta(exp(2u)),
phi(u) = (h''(u)-a^2*h(u))/4,
X(r) = integral_R phi(u)*exp(i*r*u) du = xi(1/2+i*r)/2.
```

Theta reciprocity makes h even. The complete original phi is smooth,
positive, even and double-exponentially decaying with all derivatives.
These are inherited original-kernel premises, not a new curvature result.

Define the smooth homogeneous subtraction

```text
f(u) = 2*cosh(u/2)-h(u).
```

For u>=0 its exact series is

```text
f(u) = exp(-u/2)
       -2*exp(u/2)*sum_(n>=1) exp(-pi*n^2*exp(2u)).       (1)
```

Evenness supplies u<0. Thus f and every derivative decay exponentially,
and f(u)/exp(-abs(u)/2)->1 at both ends. In particular f is smooth at zero:
(1) is an expression on the half-line, not a new reflected truncation.
Every polynomially weighted derivative of f is integrable. Directly,

```text
(a^2-partial_u^2)*f = 4*phi.                            (2)
```

The Green kernel of a^2-partial_u^2 on the line with decay at both ends is
G_a(u)=exp(-a*abs(u))/(2*a). At a=1/2 this gives

```text
f(u) = 4*integral_R exp(-abs(u-v)/2)*phi(v) dv > 0.     (3)
```

To verify the boundary prescription, the convolution is a decaying solution
of (2): the derivative jump of G_a gives (a^2-d^2)G_a=delta. The difference
from f solves the homogeneous equation and decays at both ends, so its two
exponential coefficients vanish. No inverse or midpoint solve is involved.
Combining (1) and (3) proves the exact useful envelope

```text
0 < f(u) < exp(-abs(u)/2),   every real u.              (4)
```

The Fourier integral is consequently legitimate with two derivatives (and
indeed all polynomial moments). Put

```text
Y(r) = integral_R f(u)*exp(i*r*u) du,
p(r) = r^2+1/4.
```

Integrating (2) by parts has no endpoint terms, and yields

```text
Y(r) = 4*X(r)/p(r),    X(r)=p(r)*Y(r)/4, r real.       (5)
```

In the usual completed-zeta notation Lambda(s)=pi^(-s/2)*Gamma(s/2)*zeta(s),
this is exactly Y(r)=-Lambda(1/2+i*r), because s*(s-1)=-p(r) and
xi(s)=s*(s-1)*Lambda(s)/2. This identifies the object; no new arithmetic
information is introduced by removing the quadratic prefactor.

This is an exact supporting identity, not a sign estimate. Positivity of f
makes Y positive definite as a function of frequency; it does not make Y
pointwise nonnegative or establish a Laguerre inequality for Y.

## 2. All terms in the repaired pair formula now transform separately

Unlike PR75's growing M_j, define

```text
A_j(t) = integral_R s^j*f(s+t)*f(s-t) ds, j=0,2.
```

Both are smooth and nonnegative. From (4), with T=abs(t),

```text
0 <= A_0(t) <= 2*(T+1)*exp(-T),
0 <= A_2(t) <= 2*(T^3/3+T^2+2*T+2)*exp(-T).           (6)
```

Indeed abs(s+t)+abs(s-t)=2*max(abs(s),T); integrate separately on
abs(s)<=T and abs(s)>T. Derivatives have bounds of the same integrable
polynomial-exponential type because each derivative of f is bounded by a
constant times exp(-abs(u)/2). This justifies all differentiations, Fubini
steps, and integrations by parts below, including the t endpoints.

Each phi factor is -(partial_u^2-1/4)f/4, so the two minus signs cancel.
PR75's pair differential operator therefore applies to f(s+t)f(s-t):

```text
C(t) = integral_R s^2*phi(s+t)*phi(s-t) ds
     = [(partial_t^2-1)^2*A_2(t)
        -4*(partial_t^2+1)*A_0(t)]/256.                (7)
```

The factor 256 comes from the product of
((partial_s+partial_t)^2-1)/16 and
((partial_s-partial_t)^2-1)/16. Integration in s uses
integral s^2*F_ss=2*integral F and integral s^2*F_ssss=0,
where F=f(s+t)f(s-t). Every boundary term vanishes. This expression equals
the original complete C; no lattice term, artificial cusp, cross term or
far tail has been removed.

For an explicit comparison to PR75, put c(u)=2*cosh(u/2) and
F(s,t)=f(s+t)*f(s-t). Its old smooth subtraction R satisfies

```text
R-F = 2*cosh(t)-c(s+t)*f(s-t)-c(s-t)*f(s+t).
```

This complete smooth difference is annihilated by the pair operator P:
one factor in each c*f term is homogeneous, as is the remaining cosh term.
Its s tails decay, but its displayed summands are not separately integrable
in s. Keep this difference intact. The old M_j and new A_j brackets thus
give the same 256*C without a discarded homogeneous contribution or delta.

For real r, the change of variables u=s+t, v=s-t has Jacobian 1/2, giving

```text
integral_R A_0(t)*cos(2*r*t)dt = Y(r)^2/2,
integral_R A_2(t)*cos(2*r*t)dt = L1[Y](r)/4,
L1[Y] = Y'^2-Y*Y''.                                   (8)
```

For the second identity, s^2=(u+v)^2/4 and the two cross moments give
+2*Y'^2, while the square moments give -2*Y*Y''. Equation (8) distinguishes
pointwise A_2>=0 from positive definiteness of A_2; the former does not
supply the sign of its cosine transform.

Using (7), (8) and L1[X]=4*integral C(t)cos(2rt)dt gives

```text
16*L1[X](r)
 = p(r)^2*L1[Y](r) + 2*(r^2-1/4)*Y(r)^2.             (9)
```

Independent check: for any real C^2 p,Y, expansion gives
L1[pY]=p^2*L1[Y]+Y^2*L1[p]. Here L1[p]=2*(r^2-1/4),
and X=pY/4. Both derivations agree, including at zeros of X or Y.
No logarithmic derivative or division by Y is needed.

Thus PR75's ordinary-transform difficulty can be removed, but the exact
remaining requirement is

```text
L1[Y](r) >= 2*(1/4-r^2)/(r^2+1/4)^2 * Y(r)^2,
for EVERY real r.                                    (10)
```

For abs(r)>=1/2, L1[Y]>=0 would be sufficient, but it is not supplied here.
For abs(r)<1/2 the positive right-hand side cannot simply be omitted.
At abs(r)=1/2 it vanishes; at a zero of Y the formula remains regular.
This is precisely the original first-Laguerre sign in new coordinates,
not an independent estimating inequality or an implication to RH by itself.

As a check at zero, define the complete moments m0=integral phi and
m2=integral u^2*phi. Equation (5) gives Y(0)=16*m0 and
Y''(0)=-128*m0-16*m2. Consequently
L1[Y](0)-8*Y(0)^2=256*m0*m2>0, exactly as (9) requires.
This endpoint check supplies no estimate at arbitrary real heights.

## 3. The regularized function is not an admissible entire-transform model

The exponential tail in (1) matters. The Fourier integral for Y is
holomorphic on abs(Im r)<1/2. Equation (5) continues it meromorphically,
with actual simple poles at r=+/-i/2: X(+/-i/2)=xi(0)/2=xi(1)/2=1/4.
Its unit exponential tails prevent convergence of the ordinary improper
Fourier integral on either boundary line Im r=+/-1/2. The meromorphic
continuation is nevertheless regular at every other point of those lines;
only r=+/-i/2 are poles. Decay on the real frequency axis does not remove
these complex poles.

[Csordas, arXiv:1309.0055v2](https://arxiv.org/html/1309.0055v2), Definition
1.2, requires faster-than-Gaussian decay for its admissible kernels and
thereby an entire transform. Our f does not satisfy that decay hypothesis.
Consequently that admissible-kernel class cannot be imported for f without
checking a different theorem. Its generic real-variable Laguerre algebra
remains valid. The source also explicitly separates first-Laguerre
positivity from the all-order real-zero criterion (Section 2).
This is a scoped source check, not an exhaustive literature search.

## 4. Matched control: the positive primitive and its tail are retained

Use the exact NS101 family already assessed analytically in PR74:

```text
B_beta=3+2*cosh(beta/2), beta>0,
q_beta(r)=3+2*cos(beta*r),
phi_beta(u)=[3*phi(u)+phi(u-beta)+phi(u+beta)]/B_beta,
X_beta(r)=q_beta(r)*X(r)/B_beta.
```

The positive Green operator commutes with translations, so its primitive is

```text
f_beta(u)=[3*f(u)+f(u-beta)+f(u+beta)]/B_beta,
Y_beta(r)=q_beta(r)*Y(r)/B_beta = 4*X_beta(r)/p(r).      (11)
```

For each fixed beta>0 it shares smoothness, evenness, positivity,
exponential decay of every derivative, (2), (5), the complete pair identities
(7)-(9), and the same unit leading exponential tail. Derivative and remainder
constants may depend on beta; no uniform-in-beta estimate is claimed. Even the envelope (4) survives. For u>=0,

```text
exp(u/2)*exp(-abs(u-beta)/2) <= exp(beta/2),
exp(u/2)*exp(-abs(u+beta)/2) = exp(-beta/2).
```

Together with (4), these prove f_beta(u)<exp(-u/2); evenness covers u<0.
For u>beta the leading coefficients sum to B_beta, so the tail ratio is one.
Thus these repaired boundary and positivity properties do not distinguish
the original object from the existing control.

Let m0=integral phi>0, m2=integral u^2*phi>0, k=m2/m0. PR74's complete-moment
argument gives, for beta>=max(2,pi*sqrt(k)), r_beta=pi/beta,

```text
L1[X_beta](r_beta)
 <= -(beta^2-3*k)*m0^2/(2*B_beta^2) < 0.               (12)
```

Its proof uses X(r)>=m0-r^2*m2/2, abs(X')<=abs(r)*m2,
abs(X'')<=m2 and the exact product identity at q_beta=1, q_beta'=0,
q_beta''=2*beta^2. No off-axis-zero inference, fixed numerical threshold,
new scan or certification is substituted for that argument.
Applying (9) to the control shows that its exact left side of (10) minus
its right side is strictly negative at r_beta. This directly stops the
inference from the shared primitive properties to (10).

The concrete mismatch remains crucial: phi_beta changes the original
single-lattice coefficients and loses the original nonlinear Jacobi IVP.
Therefore this is not a counterexample to the original target or a no-go
for an estimate genuinely using that IVP. A mismatch is not a control pass.

Other controls and scopes:

- NS100's negative original slice still excludes per-slice positivity, not
  the integrated target. Neither (7) nor (10) assumes a positive slice.
- Davenport-Heilbronn shares generic transform algebra, but its coefficients,
  conductor, completion and original-IVP hypotheses differ. Its kernel need
  not satisfy the positive-phi premise of (3); no positive-resolvent matched
  control is claimed from it. NS101 already supplies the exact match needed
  for the structural inference here.
- PR73's fixed reflected prefix is not used; f is complete and smooth.
- PR74's Bessel reference margin and smooth-approximation error belong to
  different comparisons. Neither supplies (10).
- NS74/83's NB family, target and dyadic-rate hypotheses do not apply.

## 5. Stop decision and next admission requirement

Boundary repair succeeds: all terms in (7) admit ordinary transforms.
The proposed shortcut from positive primitive/envelope/tail to the required
sign does not survive the existing NS101 control. This is application of
an existing obstruction, not a new closure of the nonlinear theta route.
No new original-arithmetic sign estimate or estimating method was found.

To resume sign research, specify an estimate for the COMPLETE corrected
expression in (10), or the original pair, using the original arithmetic
or distinguished IVP at a step absent from (11). Keep all real heights,
zeros and mixed terms. Relabelling (10) as a target is existing bookkeeping;
its equivalence is not progress on the estimate. A finite height table,
new dimensional rendering or another Green-kernel parameter does not meet
this admission requirement. Stop this regularization-as-positivity attempt.

Budget used: one bounded paper boundary/control audit and one findings PR.
No computation budget follows. No outreach. RH, G2 and the cofinal
signed-arithmetic lower bound remain open.
