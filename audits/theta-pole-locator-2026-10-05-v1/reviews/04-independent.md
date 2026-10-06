# Independent evaluator review 04 — four fixed endpoints

**Outcome: the four selected endpoints reproduce independently, and none is
an approximate denominator zero under the registered threshold.** The bounded
locator remains inconclusive. There is no candidate warranting an Arb
argument-count/C-exclusion certificate. No further points, corners, root
iterations, or scan were run by this reviewer.

Reviewed remote baseline `bc3ff0c962c485ac8104ce8cd832c119c260c871` (PR79),
the current AGENTS instructions, this audit's BRIEF/PROPOSAL, PR79's contour
and independent-contour reviews, and the current evaluator/locator code.
The parent owns the complete 104-node register review; this is a genuine
independent numerical replay of four new endpoints, not a historical proof
or certificate replay. Both missing-original recovery groups remain OPEN.
No prior-art result is imported, research row claimed, group thawed, or
manuscript version requested.

**Wall check: Distinct test.** Closest: PR78/79 and NS100/101. The tested
input was one uncancelled zero of the complete original M in the fixed
rectangle, sufficient to reject general quotient-PD. No such input was
found by this diagnostic. The original signed Laguerre estimate remains
the same open gap.

## Independent implementation and exact scope

`evidence/diag_theta_pole_locator/independent_replay.py` imports neither the
primary evaluator nor the locator. It evaluates the original phi through
direct individual complex exponentials, with 36 original lattice terms,
at 256-bit precision. This replaces the primary power recurrence. It
integrates by adaptive tanh-sinh, replacing composite Gauss-Legendre;
the real-s endpoint is 5, replacing the replay endpoint 9/2. The intervals
also split at the reflection transition `s=Re(z)`. Exact full-kernel
evenness is shared by both correct representations; its finite-truncation
error is included in the lattice majorant.

The moments use the same analytic nonzero normalization
`B(z)=exp(2*pi*exp(2*z)-9*z)/(4*pi^4)`, so the stored values are
`m=B*M`, `c=B*C`, and `dm=(B*M)'`. The analytic derivative is differentiated
directly from each theta summand; the derivative of B is retained. The
derivative replay therefore checks the Newton input, not just M and C.

The parent explicitly authorized replay after `original.json` existed.
The script evaluated exactly its four `second_refinements` endpoints.
The optional fixed-corner mode was not used. The source archive SHA256 is
recorded in `independent.json`; no original grid was rerun and no endpoint
was moved.

Command:

```text
.venv/bin/python evidence/diag_theta_pole_locator/independent_replay.py --approved
pyright evidence/diag_theta_pole_locator/independent_replay.py
```

Elapsed numerical replay: 65.94 seconds. Pyright: zero errors/warnings.

## Observed agreement

All numbers below are diagnostics, not interval enclosures. Relative
differences divide by the independently computed magnitude; the last
column is the primary 256-bit residual divided by its registered corner
scale. The required residual threshold was `2^-40`, approximately
`9.09e-13`.

| Original cell | Re z, Im z (rounded) | abs(m) | relative m difference | relative c difference | relative dm difference | registered residual ratio |
|---|---|---:|---:|---:|---:|---:|
| (0,7) | 0.2081163498, 0.6249999896 | 0.02380934 | 4.71e-30 | 6.31e-30 | 1.01e-29 | 0.03914164 |
| (1,7) | 0.4851714218, 0.6249979643 | 0.25133079 | 8.37e-29 | 1.40e-26 | 1.05e-26 | 0.54809427 |
| (0,6) | 0.2362889793, 0.5624995143 | 0.23890523 | 2.66e-44 | 9.89e-43 | 2.05e-42 | 0.49442807 |
| (0,5) | 0.3117720379, 0.4375055522 | 0.26895750 | 5.15e-66 | 6.80e-64 | 1.52e-63 | 0.64851256 |

Every selected path stopped because the next Newton step could not stay
inside its original cell after the permitted halvings. Their agreement
across precision does not turn these boundary-stalled endpoints into
roots. Each residual remains many orders above the registered threshold.
Numerator samples are nonzero, but without a denominator-zero witness
they say nothing about a pole.

## Complete truncation accounting and remaining numerical limitation

An independently coded uniform majorant uses the full registered height
`abs(Im z)<=5/8`, `b=pi*cos(5/4)>0`, and `d=b/2`. Direct positive sums
through n=40 plus a geometric Gaussian tail bound the constants K0,K1
in `abs(phi^(j)(u))<=Kj*exp(-d*exp(2*abs(Re u)))`. Polynomial-exponential
maxima absorb the coefficient factors. For the n>36 remainder, uniform
monotonicity holds since `b*37^2>13/4`. The derivative tail includes the
n^6 term. Product, weighted-product, and derivative-product lattice
errors are retained, along with both real-s tails and the B' contribution.

The normalized M,C,dm analytic truncation majorants, evaluated as ordinary
numbers, have maxima below `1.52e-575` for lattice truncation and
`6.33e-4737` for real-s truncation across the four points. These large
margins do **not** certify the values: floating evaluation is not outward
rounded, and neither roundoff nor quadrature error has been enclosed.
Tanh-sinh's reported errors are heuristic (roughly 1e-78 or smaller here).
The weaker observed GL/tanh-sinh agreement is the appropriate diagnostic
comparison; the heuristic estimates are not a proof of 78 digits.

## Certification disposition

No Arb certificate was started. The current data supply no approximate
denominator zero, and a certificate cannot be justified merely because
the values reproduce. Were a future separately admitted witness obtained,
the required proof would still include complete M/M'/C interval
enclosures, a zero-free boundary, a positive rigorous argument count, and
C nonvanishing throughout the box (or rigorously separated zeros), at two
precisions. A sampled winding, approximate root, or numerator sample
cannot replace those requirements.

The null bounded test neither proves M zero-free in this rectangle nor
establishes PD of C/M. It does not decide the all-height Laguerre target,
G2, or RH. Stop this bounded test without automatic enlargement.

**Final wall check: Distinct test, inconclusive outcome.** The tested
pole-based rejection edge remains uninstantiated. The original signed
arithmetic/Laguerre lower estimate remains open.
