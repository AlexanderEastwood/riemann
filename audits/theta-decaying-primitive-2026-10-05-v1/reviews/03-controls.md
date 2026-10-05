# Review 03 — matched controls and scope

**Result: PASS for the control argument; OPEN for the original sign target.**

Reviewed scientific baseline: `d93aaf6b8dbe1fcbebf6fff4f6d1f71d993f4208`
(PR75). I read the review brief and current derivation, AGENTS section 0 and
the proposal gate, the relevant research-map scopes and freeze, the original
missing-evidence ledger, PR74 review 05 and PR72's published Jacobi mismatch
argument. The coordinator performed the global register/dependency review.
This review independently checks the paper control calculation below; it
does not replay historical certificates, evaluate moments, or run a scan.
Both original-evidence recovery groups remain OPEN.

**Wall check: Same open gap.** Closest results: NS101 and PR74/75.
The repaired primitive has legitimate transforms, but the exact original
arithmetic sign in derivation (10) is still missing. NS101 excludes only an
inference from the retained generic primitive properties to that sign.

## 1. Exact match for the primitive, including its normalization

Take `beta>0` and `B=3+2*cosh(beta/2)`. Let
`T_beta g(u)=[3g(u)+g(u-beta)+g(u+beta)]/B`. Then

```text
T_beta[2*cosh(u/2)] = 2*cosh(u/2),
T_beta[phi] = phi_beta,
T_beta[f] = f_beta = 2*cosh(u/2)-T_beta[h].
```

Thus derivation (11) is the same normalized homogeneous subtraction for the
actual NS101 family, not an independently chosen positive comparison
function. Translation commutes with `1/4-partial_u^2` and its decaying Green
inverse. Hence `(1/4-partial_u^2)f_beta=4phi_beta`, and its transform is
`Y_beta=q_beta*Y/B=4X_beta/p` with exactly the same `p=r^2+1/4`.

Smoothness, evenness, positivity and the derivative decay needed for (7)-(9)
are inherited by finite translation and positive summation. For `u>=0`,

```text
e^(u/2)e^(-|u-beta|/2) <= e^(beta/2),
e^(u/2)e^(-|u+beta|/2) = e^(-beta/2).
```

Together with the strict original envelope these give
`0<f_beta(u)<e^(-u/2)`. Evenness supplies all negative `u`. For fixed beta and
`u>beta`, the three positive tail coefficients are
`3`, `e^(beta/2)`, `e^(-beta/2)`; their sum is exactly B. Therefore
`f_beta(u)/e^(-|u|/2)->1` at both ends. The envelope and unit leading tail
are truly shared. Constants in derivative bounds may depend on beta; this
does not affect the finite-beta control or require a uniform-beta bound.

## 2. Strict failure of the corrected inequality

The product identity is

```text
B^2 L1[X_beta](r)=q_beta(r)^2 L1[X](r)
                 +2beta^2(2+3cos(beta*r))X(r)^2.
```

At `r_beta=pi/beta`, this becomes
`B^2 L1[X_beta]=L1[X]-2beta^2 X^2`. Define the complete unevaluated positive
moments `m0=int phi`, `m2=int u^2 phi` and `k=m2/m0>0`. If
`beta>=pi*sqrt(k)`, then `r_beta^2 k<=1` and elementary moment inequalities
give

```text
X(r_beta)>=m0/2,
|X'(r_beta)|<=r_beta*m2, |X''(r_beta)|<=m2,
L1[X](r_beta)/X(r_beta)^2 <= 4r_beta^2 k^2+2k <=6k.
```

Consequently

```text
L1[X_beta](r_beta)
 <= -(beta^2-3k)m0^2/(2B^2)<0.
```

This confirms derivation (12), including its negative-margin direction.
The stronger stated range `beta>=max(2,pi*sqrt(k))` also retains the NS101
critical-strip hypothesis. The estimate makes no separate assertion about
the historical beta=2 member, since k has not been evaluated here.

For clarity, define the corrected residual in (10) as

```text
R_beta(r)=L1[Y_beta](r)
          -2(1/4-r^2)/(r^2+1/4)^2 * Y_beta(r)^2.
```

Equation (9) says exactly
`R_beta(r)=16L1[X_beta](r)/(r^2+1/4)^2`. The denominator is strictly
positive for every real r. At the displayed parameter and height this gives
the explicit bound

```text
R_beta(r_beta)
 <= -8(beta^2-3k)m0^2/[B^2(r_beta^2+1/4)^2] <0.
```

No division by X or Y at their zeros is involved in the identity. The
moment proof divides by X only at a point where `X>=m0/2>0` was established.
The failure is of the complete corrected expression, including the
low-height term, rather than an inferred consequence of off-axis zeros.

## 3. What the control loses

The normalized reciprocal theta mixture has its slowest exponential at
`kappa=pi*exp(-2beta)`, with positive coefficient
`c=2exp(-beta/2)/B`. For `Theta_beta(v)=1+c exp(-kappa v)+o(exp(-kappa v))`,
with its differentiated expansion through order three, the original
normalized Jacobi expression has leading term

```text
Q[Theta_beta](v)
 =c^2 kappa^4(kappa^2-pi^2)exp(-2kappa v)
  +o(exp(-2kappa v)).
```

This is strictly negative eventually for every beta>0. One can check the
coefficient directly: the leading `T^2` contributes `c^2 kappa^6`, the
`-pi^2 Theta_beta^10 S^2` term contributes `-pi^2 c^2 kappa^4`, and `32S^3`
is smaller. Thus the mixture cannot satisfy the original normalized
Jacobi equation, and a fortiori does not match its distinguished IVP.
It also changes the original single-lattice coefficients. Neither a
general positivity conclusion nor failure of the original target follows
from this mismatch. An estimate actually using that original IVP remains
outside the control's scope.

## 4. Other recorded controls

- **NS100: correctly scoped.** The actual negative original slice excludes
  positivity of each separate slice. It does not determine the sign after
  the full weighted integration used by C, and the draft does not assert
  such slice positivity.
- **Davenport-Heilbronn: correctly not claimed as a full match.** Generic
  transform/product calculus transfers when the analytic hypotheses hold;
  the original theta coefficients, conductor/completion and distinguished
  IVP do not. A positive phi and the resulting positive Green primitive
  have not been established for that analogue here. It is therefore not
  presented as a positive-primitive counterexample. No unchanged screen
  script has been treated as a screen of this different target.
- **NS74: not applicable to this formula.** Its inner-factor control
  preserves Gram geometry of a particular NB approximation family while
  altering target approximation. No such Gram/target inference occurs in
  the primitive calculation. Its general warning does not make its
  theorem a direct theta-transform obstruction.
- **NS83: not applicable to this formula.** Its fixed-smoothing NB error
  and dyadic relative-gain restrictions differ from the real frequency
  variable and first-Laguerre target here. This audit neither proposes a
  per-doubling rate nor bypasses that restriction.

## Disposition

No correction to derivation (11)-(12) or the control classifications is
required. Explicitly declaring `beta>0` at the family definition would make
the domain easier to read; the sufficient range already imposes it.
The result is an application of PR74's established control to additional
shared primitive/envelope/tail properties, not a new original sign bound.
No candidate, research row, thaw, manuscript version or further scan is
licensed. **Final wall check: Same open gap.**
