# Six-agent arithmetic admission audit

[Rendered report](theta-arithmetic-admission-2026-10-05-v1.html) · [Reviewed baseline](review-record.json) · [Proposal record](PROPOSAL.md)

**Wall check: Same open gap — ZERO-GEOMETRY, NS100/101, PR76–77.**
One well-posed new sufficient construction was assessed and rejected on the
original theta tail. Two arithmetic regroupings supply no independent signed
lower estimate. No candidate survives for computation. This does not close
the original nonlinear theta route or require a candidate lemma to be proved
before it can be considered.

Alex explicitly requested continuation and six assistants after PR77. Three
agents formulated mechanisms; three independently checked algebra, controls
and admission. The initial scope is in [BRIEF.md](BRIEF.md). The baseline was
`670864385024041d24612cf620054c1975473928`. The full-register review is a
conclusions/dependency review, not a replay of all historical proofs.

## What changed

The nonlocal attempt defines, for the complete original theta kernel,

```text
M(t) = integral phi(s+t)*phi(s-t) ds,
C(t) = integral s^2*phi(s+t)*phi(s-t) ds,
k(t) = C(t)/M(t).
```

An explicit centered Volterra correction has residual `k((u-v)/2)` and
vanishing complete flux boundaries. Positive definiteness of k would be
sufficient for the complete first-Laguerre target because M is an
autocorrelation and C=M*k. The construction alone does not prove k positive
definite. The proposed separate estimating hypothesis was a finite positive
mixture `k(t)=integral sech(2*t)^a dnu(a)`, `a>=0`, for all real t.

That is a concrete sufficient candidate with a complete conditional transfer,
different from PR77's Gaussian mixtures for C. It fails its original-data
necessary condition. For `Q(z)=k(0.5*arcosh(exp(z)))`, the complete theta tail gives

```text
Q(z) = exp(-z)/(16*pi) - exp(-2*z)/(128*pi^2) + O(exp(-3*z)).
```

A positive Laplace mixture with this leading decay must have support in
`[1,infinity)` and mass `1/(16*pi)` at 1. It would approach that leading
coefficient from above; the original quotient approaches from below.
The full lattice and outer integration tails are included. No numerical
onset is claimed. Stop this positive-mixture class; general positive
definiteness of k, other nonlocal corrections, and the original sign remain open.

The divisor regrouping exposes the exact arithmetic coefficients
`c(n)=d(n)/6 * sum_(p^a||n) a*(a+2)*(log p)^2` of
`zeta*zeta''-zeta'^2` in its right-half-plane convergence domain. Complete
continuation retains gamma, polynomial and oscillatory terms; coefficient
positivity supplies no lower sign on the critical line.

The Riemann–Siegel attempt retains both ratio and product phases, phase
acceleration, gamma curvature and the exact differentiated remainder. At its
balanced length, the stationary dual block has comparable length. The
phase-free budget is of order N, while its positive ratio diagonal is only
of order `(log N)^3`. These are bounds-strategy scales, not actual signs.
Neither observation excludes a future signed Poisson estimate.

## Six reviews

1. [Nonlocal construction and mixture rejection](reviews/01-nonlocal.md).
2. [Divisor-variance completion and missing sign](reviews/02-poisson.md).
3. [Complete Hardy/Riemann–Siegel quadratic](reviews/03-riemann-siegel.md).
4. [Independent algebra and full-tail check](reviews/04-algebra.md).
5. [Matched controls and coefficient check](reviews/05-controls.md).
6. [Adversarial admission decision](reviews/06-admission.md).

## Disposition and limits

All three attempts retain the target
`J=(r^2+1/4)^2*(Y'^2-Y*Y'')+2*(r^2-1/4)*Y^2>=0`
at every real height, including zeros. Success would prove the first
Laguerre inequality only; that alone does not imply RH. No transfer to
the cofinal NB gain or Weil floor is claimed.

NS100's slice failure does not decide the integrated target. NS101 shares
generic centering/transform identities. Its established negative-Laguerre
range forces its own quotient k_beta to fail positive definiteness, so
conditional variance alone cannot supply that property. It changes the
original lattice and IVP; that mismatch is not a control pass. Davenport–Heilbronn has different
coefficients and completion. NS74/83 are NB target/rate controls, not literal
controls for this theta assertion. No numerical control command was run:
the actual sufficient candidate fails on paper on the original input;
the other two never supply a signed estimating statement.

Budget: six bounded paper reviews and one publication PR; **zero scans or
certification runs**. Stop this round. No automatic adjacent variation or
route pivot follows. No research row, new theorem node, thaw or manuscript
version. Both original-evidence recovery groups remain OPEN. RH, G2 and
the cofinal arithmetic bounds remain open.
