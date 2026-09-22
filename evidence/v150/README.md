# v1.50 — NS-34: the positive arithmetic weight and critical capacity budget

**Exact identities and proved scoped implications, plus named open input
CAE. No numerical experiment or certificate. G2 and RH remain open.**

The task follows the recommendation to try an explicit positive comparison
weight in the existing physical prime-shift/Picone identity, allowing the
uniform finite error of v1.36. The selected weight is the archived Gaussian
arithmetic radical, h(x)=E(H)(exp x). It is explicit, even, strictly positive,
and independent of the unknown ground state. It is not identified with the
actual repaired finite-window source.

## What was established

- Positivity and explicit upper/lower double-exponential bounds for h.
  Its pole mass is exactly integral cosh(x/2) h(x) dx = 1/sqrt(3), by the
  Mellin transform. The associated completed-zeta kernel is classical.
- The exact global identity q[hg] = J_h[g] - (2/3) Var_nu(g)
  - 2 |integral sinh(x/2) h(x) g(x) dx|^2. Both J_h and the subtracted
  expression are nonnegative; the last square is essential in the odd
  sector. All expressions are finite on compact tests, and extend to
  each fixed-window form domain. No positive global realization is assumed.
- The exact finite-window exterior term T_a is retained. The local potential
  is r_a = (T_a - 2 I_h cosh(x/2))/h. This is an identity, not a tail metric.
- For this weight, the sufficient capacity form is
  B_(a,delta) = q_a - integral (r_a)+ |f|^2 - delta J_(a,h)[f/h].
  Every valid capacity error on either parity must obey

      eta_a >= [delta_a*kappa*exp(gamma*lambda^2) - B_a]+,
      B_a = A + (8a+1)*exp(a) + 2a,
      kappa = (2*pi-3)*log(2)/(128*pi),
      gamma = (3*pi/4)*exp(-4*log(2)-2*b), b=log(2)/16.

  The finite A depends only on two fixed compact smooth bumps, never on
  the window. A fixed positive energy fraction cannot be discarded with
  uniformly bounded eta. Necessarily delta is at most
  O(lambda*log(lambda)*exp(-gamma*lambda^2)). Deleting prime-2 transformed
  energy alone gives the same obstruction with delta=1.
- Source admissibility is exact: a two-dimensional even translated-bump
  space contains a unit vector orthogonal to the actual source for every
  window. The odd space is already source-orthogonal. The bounds apply to
  all mixtures in these spaces, so no uncontrolled cross term is omitted.

## What had to change; what remains missing

A generic strictly contractive absorption estimate cannot work for this
weight, even with the weakened bounded-error target. Its transformed edge
ratios amplify a fixed energy loss like exp(gamma*lambda^2). This closes
only the stated fixed-slack/prime-2-deletion comparisons.

The full coefficient-one signed comparison remains the named open input
**Critical Arithmetic Energy comparison (CAE)**. In these coordinates it
is equivalent to the original uniform complement-floor target; writing it
has not supplied an independent arithmetic proof. The local capacity test
with delta=0 is stronger because it also drops the positive potential.
Neither its uniform error nor CAE is proved. A different weight is not
excluded. This is a failure of the proposed lower comparisons, not of the
physical Weil form or the full capacity route.

## Record and provenance

- `capacity_weight.tex`: complete integrated proof and open-input statement.
- `scope_review.md`: internal claim, domain, parity and algebra checks.
- `provenance.json`: source hashes and reviewed mathematical ancestry.
- `build_report.json`: actual manuscript build and reference counts.
- `research-report-2026-09-21-v1.html`: user-facing report.
- NS-37: `audits/ns37-capacity-weight-2026-09-21-v2.html` records no unresolved MAJOR/MINOR; the reviewed fragment hash matches exactly.
- Actual manuscript build: 246 pages, 0 undefined/duplicate references, 48 bibliography items, no duplicate keys or overfull boxes.
- The audited goals sentence about the symbol amplitude now agrees with the weighted strict-cutoff formula already proved in v1.46; historical diagnostic artifacts are untouched.

No new window, tail metric, numerical optimizer, source projection run,
or zero enclosure. NS-1's two evidence groups remain OPEN. Existing
missing v1.29/v1.30 candidate artifacts are not claimed recovered; this
work relies on the complete manuscript identities and its archived
v1.15/v1.35 analytic radical inputs.
