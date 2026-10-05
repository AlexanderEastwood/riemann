# Agent 5 — direct first-Laguerre screen for the NS101 mixture

Reviewed scientific baseline: `5434d96f0034f842b0229f1d69dbbf3fb7fea270`
(merged PR73). Working HEAD: `971c8bd02c834cf31ab98ea2a50060289fbece40`,
the coordinator's scope/ownership-only commit. The coordinator refreshed
the remote and reviewed all 104 registered conclusion/dependency records;
I read the shared brief, current AGENTS/proposal gate, relevant
ZERO-GEOMETRY freeze, PR72/73 reports and transfer notes, NS100/101
arguments, and the unchanged missing-original ledger. This is a paper
control audit, not a historical certificate replay or new arithmetic method.

**Wall check: Same open gap.** Closest results: NS101 and PR72/73.
What changes: directly determine the first-Laguerre sign of the existing
reciprocal-mixture family in an explicit parameter range. Its off-axis
zeros alone do not answer that question. The original theta comparison,
ZERO-GEOMETRY, RH and G2 remain open.

**Question and dependency.** Does the actual NS101 family contradict the
implication from its retained general theta properties to
`L1[X](r) >= 0` for every real `r`? A direct negative value closes this
specific control-screen question and rejects that general implication.
It supplies no bound for the original arithmetic function and is not a
candidate for thawing the original estimating task.

## Exact product formula

Use the complete positive even original kernel `phi`, with

```text
X(r) = integral_R phi(u)*cos(r*u) du,
L1[f] = f'^2 - f*f'',
B_beta = 3 + 2*cosh(beta/2),
q_beta(r) = 3 + 2*cos(beta*r),
X_beta(r) = q_beta(r)*X(r)/B_beta,       beta > 0.
```

Here `beta` denotes NS101's translation/dilation parameter `a`, not its
separately named inverse-hyperbolic-cosine constant. Expanding the two
derivatives cancels both mixed terms and gives, for real `C^2` functions,

```text
L1[q*X] = q^2*L1[X] + X^2*L1[q].
L1[q_beta] = 4*beta^2*sin(beta*r)^2
              + 2*beta^2*(3+2*cos(beta*r))*cos(beta*r)
           = 2*beta^2*(2+3*cos(beta*r)).

B_beta^2*L1[X_beta](r)
 = q_beta(r)^2*L1[X](r)
   + 2*beta^2*(2+3*cos(beta*r))*X(r)^2.                 (1)
```

At `r_beta = pi/beta`, the multiplier has `q=1`, `q'=0`,
`q''=2*beta^2`. Therefore

```text
B_beta^2*L1[X_beta](r_beta)
 = L1[X](r_beta) - 2*beta^2*X(r_beta)^2.              (2)
```

No zero information or assumption about the sign of the original `L1`
has entered these identities.

## Complete-moment sufficient range: direct strict negativity

Define the unevaluated **complete** moments

```text
m0 = integral_R phi(u) du > 0,
m2 = integral_R u^2*phi(u) du > 0,
k = m2/m0.
```

They are finite by the complete theta tails. Differentiation through
order two is justified by these moments. Positivity of `phi` and the
elementary inequalities `cos t >= 1-t^2/2`, `|sin t| <= |t|` give

```text
X(r) >= m0 - r^2*m2/2,
|X'(r)| <= |r|*m2,
|X''(r)| <= m2.                                     (3)
```

If `beta^2 >= pi^2*k`, then at `r=r_beta` we have `r^2*k <= 1`
and `X(r) >= m0/2 > 0`. Consequently

```text
L1[X](r)/X(r)^2
 <= (r*m2/X(r))^2 + m2/X(r)
 <= 4*r^2*k^2 + 2*k
 <= 6*k < 2*pi^2*k <= 2*beta^2.                     (4)
```

The strict inequality uses only `pi^2>3`. Combining (2)–(4) proves

```text
For every beta >= pi*sqrt(m2/m0),

L1[X_beta](pi/beta)
 <= -(beta^2-3*k)*m0^2/(2*B_beta^2) < 0.             (5)
```

This is an analytic parameter condition in full moments, with an explicit
strict margin. No numerical threshold, cutoff, scan or Taylor remainder
is asserted. Smoothness and `X(0)>0` alone already give the qualitative
large-beta conclusion from (2); (3) makes the sufficient range explicit.
The fixed historical choice `a=2` is not separately certified here.

## Matched hypotheses and limits

The control is exactly the NS101 family, with complete kernel

```text
phi_beta(u) = [3*phi(u)+phi(u-beta)+phi(u+beta)]/B_beta.
```

- **Retained:** positive Gaussian mixture and normalized constant term of
  its reciprocal theta sum; reciprocal symmetry; positive even real
  analytic differential kernel; full double-exponential tails (changed
  constants); the exact completion/differential identity; order-one entire
  transform and its reality/evenness; the generic pair/associated-kernel
  and mixed-quadratic-form identities. PR72's boundary subtraction still
  gives the same regular disk energy identity. These properties therefore
  do not imply all-height first-Laguerre positivity.
- **Critical-strip matching:** put `eta=arcosh(3/2)`. The added zeros are
  `z=+/-eta/beta + i*(2j+1)*pi/beta` in the `F(z)=X(-i*z)` convention.
  Since `eta<1`, every `beta>=2` puts them strictly inside `|Re z|<1/2`;
  the original zeros are retained. Thus (5) and the same strip property
  hold simultaneously for every `beta>=max{2,pi*sqrt(m2/m0)}`. This zero
  statement matches hypotheses only; it is not used in the sign proof.
- **Original ODE lost:** PR72 directly proves failure of the normalized
  nonlinear Jacobi equation for every `beta>0`: the slowest exponential
  in its theta sum has rate `pi*exp(-2*beta)`, whereas that equation with
  the stated constant-term/tail normalization forces rate `pi`. Hence this
  is not a control against a bound using the distinguished original
  Jacobi trajectory and complete arithmetic data. The precise original
  single-lattice frequencies/coefficients are changed; monotonicity,
  log-concavity and all original modular transformations are not asserted.
- **Boundary smoothness retained:** all odd derivatives of `phi_beta`
  vanish at zero, including `phi_beta'(0)=0`. Its transform and derivatives
  have rapid decay. It therefore avoids PR73's finite-reflection cusp and
  boundary asymptotic, yet still has the negative value (5). This shows
  that smooth even completion and the retained general properties alone
  do not suffice. It does not exclude a quantitatively faithful smooth
  approximation to the original kernel: no such approximation property,
  full-height error estimate or original-ODE match is supplied here.

The sharper screen corrects the prior *absence of a first-Laguerre screen*
forward; PR73 correctly refused to infer its sign from off-axis zeros.
It does not turn first-Laguerre positivity into the all-order RH criterion.

**Disposition and bounded next budget.** The matched-control question is
resolved by (1)–(5); stop, with no scan or additional numerical budget.
Agent 6 independently checked the product-sign argument and the constants
in the sufficient moment range; that bounded paper review is complete.
No original-theta estimating method is obtained, no research row or
manuscript version is claimed, and no existing report is overwritten.
**Final wall check: Same open gap.**
