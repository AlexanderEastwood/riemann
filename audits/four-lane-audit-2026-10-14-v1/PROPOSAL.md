# Proposal & Admission Gate Record — October 14, 2026 Four-Lane Audit

This audit executes bounded algebraic/dependency reductions and control screens across the three active analytical lanes (`NB-GAIN`/`COEFF`, `KERNEL-API`, `ZERO-GEOMETRY`) plus local archive reconciliation. No new row in `NEXT_STEPS.md`, no group thaw, and no manuscript version bump are claimed.

## 1. Lane 1 (`NB-GAIN` / `COEFF` — Untruncated Schur–Rayleigh Dual & Exact Constants)

```
Proposal: Exact rational evaluation of (C_b, Var_R(b'''), A_b, I_diag) for
  b(s)=(s-1)^3(2-s)^3(2s-3)1_[1,2](s), and untruncated Schur-Rayleigh
  identity M_N(u,y) = (lambda_new - C^T G^{-1} lambda_old)^T y on V_{2N} cap V_N^perp
  with squared cost tilde_lambda_N^T S^{-1} tilde_lambda_N <= C_b N - lambda_old^T G^{-1} lambda_old <= C_b N.

Shared-input group: NB-GAIN (supporting COEFF tool audit; closest NS61, NS78, NS80, NS87).
Status: Frozen. Supporting algebra/cost audit only; no thaw or unapproved COEFF scan.

Arithmetic input beyond the functional equation:
  Exact integer divisor jump identity (t a_n')' = 1/n - sum_{k>=1} delta_{kn} (NS87);
  the companion lower signal |tilde_lambda_N^T S^{-1} h|^2 >= a C_b N E_N / j
  requires original target loads h = b_new - C^T G^{-1} b_old and remains OPEN.

Dependency edge and arithmetic use:
  Proves C_b = 6904/45045, Var_R(b''') = 543/14, A_b = 181/3360, I_diag = 1219/38798760,
  eliminates the K = floor(sqrt(N)) low-old alias truncation penalty on V_{2N} cap V_N^perp,
  and proves that testing with psi_N is algebraically isomorphic to the Rayleigh quotient
  along w_{psi_N} = S^{-1} tilde_lambda_N (so S^{-1} remains in the numerator).

Control screen:
  NS74 unitary-altered family: preserves G, C, D, S and the dual cost bound
    tilde_lambda_N^T S^{-1} tilde_lambda_N <= C_b N identically, while changing h
    and violating eventual SIGNAL due to its positive floor F_beta > 0.
  Davenport-Heilbronn / NS100 / NS101: not-applicable (different kernel/atom family).
  Command/artifact: `.venv/bin/python audits/four-lane-audit-2026-10-14-v1/verify_four_lanes.py`
    (exact Fraction arithmetic + 50-digit mpmath; N=16 untruncated cost 2.4523 < D_16 = 10.9058).
  Full-scope obstruction: NONE ESTABLISHED for actual-target SIGNAL; Known wall for
    bypassing S^{-1} purely via coordinate reparametrization (u,y) = (-G^{-1}Cy, y).

Wall check: Same open gap.
  Closest result: NS78/80/87, Oct 1 COEFF review (04-proposal-dual / 10-review-dual).
  What changes: exact rational constants and removal of low-old truncation penalty;
    the actual-target lower signal tilde_lambda_N^T S^{-1} h remains open.

What success changes: Sharpens the verified compact dual extractor to C_b N = (6904/45045)N
  with zero low-old truncation error and direct NS87 T=N^6 transfer.
What failure changes: N/A (exact algebraic/rational verification passed).
Budget: Completed within this single audit turn; zero scans.
Disposition before claim: Retain as supporting tool refinement; do not claim a new NS row.
Version bump expected: no.
```

## 2. Lane 2 (`KERNEL-API` — Interior Adjoint Embedding & Multi-Prime Support Barrier)

```
Proposal: Interior adjoint embedding L_p : V_{a-ell} -> V_a (ell = log p < a, r = p^{-1/2})
  with exact pole annihilation K_pole L_p = 0, and proof of the Multi-Prime Interior
  Support Barrier for commuting products L_P = prod_{p in P} L_p.

Shared-input group: KERNEL-API (closest node: kernelapi; NS51, NS55, NS57, NS58).
Status: Frozen. Structural dependency audit; no thaw.

Arithmetic input beyond the functional equation:
  Exact multiplicative prime-power recurrence w_{p^k} = (log p) p^{-k/2} giving
  L_p C_p = (1 - p^{-1}) I and L_p(exp(+/- x/2)) = 0; Chebyshev/Bertrand prime distribution.

Dependency edge and arithmetic use:
  Maps g in V_{a-ell} directly into V_a without smooth cutoff chi or exterior truncation,
  yielding P_{a-ell} L_p W_0 F = 0 on (-a+ell, a-ell) for any first-zero nullvector F.
  Proves that for every a > 0 and every prime set P with ell_P = sum_{p in P} log p < a,
  at least one prime q not in P satisfies log q < 2a - ell_P < 2a, so pure algebraic
  elimination cannot clear all active window primes before exhausting the window width.

Control screen:
  NS57 prime-2 perturbation (delta_2 = -log(2)/100): L_2 C_2_tilde acquires the exact
    non-vanishing defect -eps[(1+r^2)(T_ell+T_{-ell}) - r(T_{2ell}+2I+T_{-2ell})],
    verified to 7.19e-51 across 32 frequencies.
  Davenport-Heilbronn / NS100 / NS101: not-applicable to the literal prime-shift/pole operator.
  Command/artifact: `.venv/bin/python audits/four-lane-audit-2026-10-14-v1/verify_four_lanes.py`.
  Full-scope obstruction: Known wall for pure interior finite-prime-product elimination
    of all active window primes (`ell_P < a` forces an uncancelled prime `log q < 2a - ell_P`).

Wall check: Same open gap (with narrower Known wall for pure interior multi-prime elimination).
  Closest result: NS55/57/58, Oct 5 Reviewer 05 (`05-euler-api.md`).
  What changes: eliminates cutoff/pole commutator on V_{a-ell} and proves the Chebyshev/Bertrand
    support barrier against complete multi-prime elimination.

What success changes: Focuses future KERNEL-API work on quantitative archimedean dominance
  of L_p alpha(D) over the surviving prime chains sum_{q != p} (log q) L_p(C_q - I).
What failure changes: Stop attempts to eliminate all active primes on (-a,a) via commuting L_p products.
Budget: Completed within this single audit turn; zero scans.
Disposition before claim: Archive as structural dependency theorem; no new NS row.
Version bump expected: no.
```

## 3. Lane 3 (`ZERO-GEOMETRY` — Tautological Collapse of the Two-Shift Moment $B_p(r)$)

```
Proposal: Exact algebraic and control audit of the two-shift moment B_p(r) and strip identity
  (x^2+r^2)J(x,r) = 32 int_0^inf p sinh(2xp) B_p(r) dp - x|f(x+ir)|^2 from 01-jacobi-transfer.md.

Shared-input group: ZERO-GEOMETRY (closest results: NS100, NS101, PR72, PR76, PR78).
Status: Frozen. Falsification/collapse audit of an active lead; no thaw.

Arithmetic input beyond the functional equation:
  NONE in B_p(r): although P(L) was written via the Planat-Sole Jacobi variables (a,U,chi),
  multiplying P(2(p+t))P(2(p-t)) by K(p,t) = phi(p+t)phi(p-t) cancels the denominator
  identically to (1/4) phi'(p+t)phi'(p-t).

Dependency edge and arithmetic use:
  Proves B_p(r) = (1/4) int_0^inf phi'(p+t)phi'(p-t)cos(2rt)dt and its p-derivatives lie
  entirely in the universal linear derivative-autocorrelation algebra, and that its x -> 0+
  limit is 64 int_0^inf p^2 B_p(r) dp - X(r)^2 = r^2 L_1[X](r).

Control screen:
  Davenport-Heilbronn: strip identity (6) holds to 1.76e-97 at z = 0.3085 + 85.699i.
  NS100 log-concave order-2: shares all universal derivative-autocorrelation identities.
  NS101 reciprocal dilation: sampled-failure of the target inequality at beta = 4, r = pi/4,
    where 64 int_0^inf p^2 B_{beta,p}(pi/4) dp - X_beta(pi/4)^2 = (pi/4)^2 L_1[X_beta](pi/4)
    = -0.01068524686157 < 0 (identity verified to 1.79e-43).
  Command/artifact: `.venv/bin/python audits/four-lane-audit-2026-10-14-v1/verify_four_lanes.py`.
  Full-scope obstruction: Known wall for B_p(r) and multilinear products
    P(2u_1)...P(2u_k)phi(u_1)...phi(u_k) as Jacobi-specific invariants.

Wall check: Known wall for the linearized two-shift B_p(r) moment lead; Same open gap for ZERO-GEOMETRY.
  Closest result: NS101, PR72 (`theta-orbit-followup-2026-10-05-v1`), PR76, Oct 5 `01-jacobi-transfer.md`.
  What changes: closes the B_p(r) lead from Oct 5 by proving it cancels the Jacobi ODE denominator
    and fails on NS101; establishes that any genuine Jacobi transfer must be nonlinear at a single clock argument.

What success changes: Prevents wasted orbit/moment scans on B_p(r) and formulates the exact
  single-clock nonlinearity criterion for future ZERO-GEOMETRY proposals.
What failure changes: Stop the B_p(r) two-shift slope hierarchy.
Budget: Completed within this single audit turn; zero scans.
Disposition before claim: Archive audit and close the linearized B_p(r) lead; no new NS row.
Version bump expected: no.
```
