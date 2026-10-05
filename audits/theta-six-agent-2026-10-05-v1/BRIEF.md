# Six-agent theta continuation brief

Baseline: 5434d96f0034f842b0229f1d69dbbf3fb7fea270 (merged PR73).
Remote refreshed; no open PRs. Coordinator freshly reviewed all 104 node
scope/status/evidence/dependency notes, 14 continuation demands, current
README, NEXT_STEPS freezes and evidence/MISSING.md (unchanged original
recovery groups OPEN), plus the current PR72/73 findings. Node records are
byte-for-byte semantically unchanged from the preceding full review. This
is not a historical proof/certificate replay.

Read current AGENTS.md, PROPOSAL_TEMPLATE.md, relevant ZERO-GEOMETRY map
scope, and the current reports below before your assigned work.

- audits/theta-orbit-followup-2026-10-05-v1/README.md and report
- audits/theta-orbit-followup-2026-10-05-v1/support/01-jacobi-transfer.md
- audits/theta-orbit-followup-2026-10-05-v1/support/04-jacobi-source.md
- audits/theta-pair-laguerre-2026-10-05-v1/theta-pair-laguerre-2026-10-05-v2.html
- evidence/ns100_reassessment/argument.tex
- evidence/ns101_theta_factorization/argument.tex

## Objective and gate

User explicitly requests continuation with six agents. Seek a concrete
estimating method for the COMPLETE original theta two-factor expression,
or a useful independent partial estimate with a fully stated transfer.
Default wall check: Same open gap (ZERO-GEOMETRY, NS100/101, PR72/73).
Do not count identities, alternate notation, finite tables, or unexcluded
possibilities as arithmetic progress. Prior art only from arXiv, with actual
hypotheses/normalizations checked. State original arithmetic beyond symmetry.
No numerical or symbolic scan, certificate, new research row, manuscript
version, outreach, push or commits by agents. Admission/proof applicability
and paper derivations only. No new computation until a concrete dependency
and matched controls are specified and assessed. A screen can be on paper.

NS100 excludes positivity of every unintegrated slice for the original
kernel. NS101 reciprocal mixture fails the original normalized Jacobi
ODE (PR72); its off-axis zeros alone do NOT settle its first Laguerre sign.
PR73 excludes all-height nonnegative certificates based on a fixed finite
sum reflected at zero: its nonzero odd boundary derivative forces
L1[X_M]=-8*delta_M^2*r^-6+O_M(r^-8). It does not exclude smooth completions,
growing M(r), or the exact original nonlinear evolution. Do not reopen
that fixed-prefix strategy or a finite constant-matrix moment closure.

## Exact target

phi(u) is the smooth even COMPLETE original theta kernel; for u>=0,
phi(u)=sum_(n>=1) (2*pi^2*n^4*exp(9u/2)-3*pi*n^2*exp(5u/2))
                        *exp(-pi*n^2*exp(2u)).
X(r)=integral_R phi(u)*exp(i*r*u)du=xi(1/2+i*r)/2.
C(t)=integral_R s^2*phi(s+t)*phi(s-t)ds.
L1(r)=X'(r)^2-X(r)*X''(r)=4*integral_R C(t)*cos(2rt)dt.
Want L1>=0 for ALL real r; equivalent to C positive definite. This is only
first Laguerre, not the full all-order criterion.

Original state has L=2u, a'=(U+a^2-1)/2, U'=2U(a+chi), chi'=a*chi-U,
a(0)=chi(0)=0, U(0)=Gamma(1/4)^8/(64*pi^4). Define d=U+1.5(a^2-1),
P=a/4+[2U(a+chi)+1.5a(U+a^2-1)]/d, P1=V(P).
K_tt=4[(Pplus-Pminus)^2+P1plus+P1minus]K, clocks 2(s+-t).

The mixed form for arbitrary finite real x_i, complex c_i is
Q=sum c_i conj(c_j) C((x_i-x_j)/2)
 =||E||^2+0.5 Re<D2,D0>-0.5||D1||^2,
f_i(y)=phi(y-x_i), Dk=sum c_i*x_i^k*f_i,
E=sum c_i*(y-x_i)*f_i. No lower bound follows from this identity alone.

## Deliverable

Write only your assigned internal review note. Start with reviewed commit,
wall classification, exact question and dependency. Separate what you
actually derived/checked from guesses or conditional statements. Give a
precise estimate with domains and method if one survives; otherwise say
which missing comparison remains and why. Name matched controls and
hypothesis mismatches, success/failure consequence and bounded next budget.
Do not recommend further scans without an independently estimating method.
You are not alone in the worktree; preserve all other agents' edits.
