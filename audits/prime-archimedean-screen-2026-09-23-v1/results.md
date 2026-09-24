Rejected pre-claim screen and overlap audit; floating-point diagnostics, not a new certificate or arithmetic theorem.

# Exponential damping does not supply the missing uniform floor

The bounded attempt stopped at the proposal gate. A fixed damping parameter
makes the prime sum absolutely convergent and combines it exactly with the
original archimedean and pole terms. The desired bounded cost of removing
that damping is already excluded by NS47. Sending the damping to zero
avoids this particular fixed-comparison argument but loses the justified
Euler-series/Fourier representation before reaching zero. No independent
arithmetic estimate has been found for that transition.

No research row was claimed. No frozen input group is thawed, no theorem
node or manuscript version is added, and no general Euler-product or
regularization route is claimed closed. The draft proposal in PROPOSAL.md
was written before the numerical screen; the final rejection below records
its disposition. This is an application of existing results, not a new
closure to count as research progress.

## The precise attempted inequality

Use the complete support-consistent form and correlation of NS50:

    c_f(t) = integral f(x+t) conjugate(f(x)) dx,
    rho(t) = exp(t/2)/(2 sinh t),
    c_ar = psi(1/4) - log pi,       w_n = Lambda(n)/sqrt(n).

For compact smooth f define the damped form by

    q_e[f] = c_ar ||f||^2
      + 2 integral_0^infinity rho(t) (||f||^2 - exp(-e*t) Re c_f(t)) dt
      - 2 sum_(n>=2) Lambda(n) n^(-1/2-e) Re c_f(log n)
      + 4 integral_0^infinity cosh(t/2) exp(-e*t) Re c_f(t) dt.

Every term, including the odd pole contribution, is retained. At fixed
compact support the prime sum is finite. This changes all off-diagonal
correlations consistently; damping the prime term alone gives another form.
The new estimate sought was, for one fixed e>1/2,

    q_e[f] - q[f] <= C ||f||^2     for EVERY compact smooth f,   (A)

with one finite C independent of support. It would also suffice to have the
compatible complete parity/source inequalities cofinally. The odd core is
already source admissible, so it cannot be omitted.

## Control and coefficient screen, performed before the overlap audit

`screen.py` uses `controls/davenport_heilbronn.py::screen` with the actual
logarithmic-derivative expression, not the unchanged example. At 30 and 50
decimal digits it evaluates

    2 Re(F'/F)(e+i*t), e=2,
    t=0, gamma_1, 20, Im(the DH zero near85.7), 176.702461.

The original xi and all four controls pass these five positivity samples:
Davenport-Heilbronn, NS100's order-two Gaussian model, NS101's reciprocal
positive-dilation model, and the shifted product
G(z)=xi(1+2z)xi(2z)/4. The last has nonnegative multiplicative Euler
coefficients for zeta(2s)zeta(2s-1), s=1/2+z, but different gamma/pole data.
None of these sampled passes proves a global condition.

At separately chosen points just to the left of an off-axis zero, the
continued expression is negative for each control:

| Control | Re z | Im z | 2 Re(F'/F)(z), approximately |
|---|---:|---:|---:|
| Davenport-Heilbronn | 0.28851718 | 85.69934849 | -96.16306417 |
| NS100 order two | 0.94242365 | pi | -94.88388941 |
| NS101 dilation | 0.46121183 | pi/2 | -97.25404857 |
| shifted zeta product | 0.23 | gamma_1/2 | -95.58618384 |

The original xi expression is positive at those four points. These are
function-expression diagnostics; no physical-form multiplier identity is
asserted outside each separately justified convergence domain. In
particular the order-two model has no original Euler/gamma representation.

**Full-hypothesis assessment:** transferring Riemann's exact prime, gamma
and pole data to these controls is not-applicable. The existential all-test
bound (A) is inconclusive on the controls, because no finite samples decide
it and no matching complete form comparison was supplied. The samples
establish neither its validity nor its failure. They screen the proposed
intermediate condition and stop any inference from positive damped samples
alone. The rejection for the original form instead uses NS47 below.

For the original function, actual prime-power prefixes at N=1000 and4000,
s=5/2+i*t, agree with the complete logarithmic derivative within the
recorded elementary tail allowance

    2 N^(1-sigma) [log N/(sigma-1) + 1/(sigma-1)^2], sigma=5/2.

This comes from Lambda(n)<=log n and the decreasing all-integer integral.
All ten comparisons at each precision pass. Numerical values are mpmath
illustrations of normalization and convergence, not interval certificates.

## Exact match to the existing NS47 obstruction

For e>1/2, using the unitary Fourier transform, the original damped form is

    q_e[f] = integral m_e(t) |fhat(t)|^2 dt,
    m_e(t) = 2 Re[xi'/xi(1/2+e+i*t)].                        (B)

Here the prime part is -2 Re sum Lambda(n)n^(-s). The archimedean part is
Re psi(s/2)-log pi, and the pole part is 2 Re(1/s+1/(s-1)). The digamma
integral and the two elementary damped pole integrals give these terms
with precisely the displayed constants. They equal (B) by differentiating
the standard xi definition. Absolute convergence requires Re s>1; this is
not an identity obtained by replacing divergent sums by midpoint values.
See [DLMF 27.4.12](https://dlmf.nist.gov/27.4.E12) and
[DLMF 25.4.4](https://dlmf.nist.gov/25.4.E4).

In that zero-free right half-plane m_e is nonnegative. This is classical
logarithmic-derivative/monotonicity information outside the critical strip,
not a new consequence of our samples; see
[Sondow and Dumitrescu, Theorem1 and its proof](https://arxiv.org/abs/1005.1104).
For fixed e>1/2 the absolutely convergent prime series is bounded uniformly
in t, while the digamma term gives

    m_e(t) = log(2+|t|) + O_e(1).

Thus T_e f=sqrt(m_e) fhat is a densely defined, closed, unbounded ordinary
L2 operator. It commutes with reflection and is unbounded in both parity
sectors. The proposed (A) is exactly

    q[f] >= ||T_e f||^2 - C||f||^2.

Proposition `prop:ns47-no-closed-square`, inequality
`eq:ns47-lower-comparison`, says that any ordinary-closable
T satisfying this estimate must extend to a bounded operator. Its dense
cutoff-radical and complete-domain hypotheses are the original ones here.
This directly contradicts the unbounded T_e. The odd-sector statement
alone defeats the required two-sector comparison; there is no substitution
of a full-even statement for the varying even source complement.

The comparison (A), with any finite C and any fixed e>1/2, is therefore
already excluded by the recorded theorem. It fails even under RH. We are
not adding a new theorem or claiming that q itself has a negative direction.
Replacing q_e by a fixed capped multiplier is the NS50 cap reformulation:
it removes this obstruction but supplies no independent floor estimate.

## Does shrinking damping escape?

If e=e_a tends to zero with the logarithmic half-width a, a fixed T_e is no
longer the comparison. We do NOT extend the fixed-operator no-go to all such
families. But eventually e_a<=1/2: the prime and pole terms no longer have
the absolute convergence used to establish the global representation (B).
The compact-support physical form q_(e_a) is still defined. Its positivity
or uniform lower floor is not supplied by the Euler product.

Meromorphic continuation of xi'/xi is not permission to transport the
Fourier identity across zeros: extra residue terms or a different
representation may be required. Assuming that the continued expression is
nonnegative throughout Re(s)>1/2 invokes the classical RH-equivalent
criterion already noted in NS100; it does not estimate the original prime
cancellation. Keeping both a uniform comparison cost and a useful lower
bound for q_(e_a) remains an unproved arithmetic task. No schedule,
cutoff or analytic continuation proving those inputs was obtained here.

## Review, final disposition and replay

Reviewed main `5ddff5e215fce7c0236e7a27860ec8fdd697176a`. Its complete
104-node register and 14 continuation groups agree with the just-reviewed
NS104 head. Current README, board, evidence ledger and affected NS47/50,
v136/v137 and NS100/101 arguments were checked. This is a conclusions and
dependency review, not a replay of all historical proofs or certificates.
Both missing-original groups remain OPEN. Local author review only.

**Wall check: Known wall for fixed damping**, closest NS47/50; the
matching hypothesis is an unbounded ordinary-closable positive comparison
with a support-independent error. **Same open gap for damping tending to
zero**, WEIL-FLOOR; the required arithmetic lower bound and comparison have
not been obtained. Final disposition: REJECT before research claim.
No admissible thaw or new arithmetic estimate arose from this attempt.

Replay from the repository root, using a fresh output path:

```
.venv/bin/python audits/prime-archimedean-screen-2026-09-23-v1/screen.py --output /tmp/prime-arch-fresh.json
pyright audits/prime-archimedean-screen-2026-09-23-v1/screen.py
```

The JSON includes precision, sample domains, component values, control
outcomes, scope limits and source hashes. Build and consistency validation
are recorded separately. No larger-window positivity computation was run.
