# Review 04 — prime-sum estimating feasibility after PR76

**Recommendation: do not allocate another prime-prefix, damping, or contour-identity task. No original-arithmetic estimating lemma is admitted by this review.** One unconditional smoothing mechanism was assessed below. It controls remote residues, but leaves precisely the local signed quantity that needs new arithmetic information.

**Wall check: Same open gap — ZERO-GEOMETRY.** Closest result: PR76, review 08; NS100/101 for structural controls. What changes: an explicit unconditional smoothed-prime formula is tested against its local and remote residue budgets. No new hypothesis estimates the local signed part. NS47 concerns a different all-test comparison and is not a no-go theorem for this pointwise question.

Reviewed public baseline: `18d324703969b5bcc9aa94043cfd90a6e8211f34` (PR76), in the refreshed isolated worktree. Worktree HEAD when inspected was `32f599ced1abb2bf2376a715042e6e4101591639`, whose additional commits claim the explanation and this assessment. Read AGENTS, the full registered-node status/note/wall-input projection, the shared-input scopes, current README/checkpoints, NEXT_STEPS frozen groups, MISSING, PR76 derivation and review 08. This is a dependency and feasibility review, not a replay of historical proofs or certificates. Both original-evidence recovery groups remain OPEN.

## 1. One concrete mechanism: smooth the explicit formula, keep every residue

The relevant prior art is [Gonek–Hughes–Keating, arXiv:math/0511182v1, Section 2, Lemma 1](https://arxiv.org/html/math/0511182#S2). Its exact smoothed logarithmic-derivative formula is unconditional and allows any nonnegative smooth mass-one cutoff supported in `[1,e]`. It excludes evaluation at zeros and poles. Its proof retains nontrivial zeros, the pole at 1, and trivial zeros; smoothing supplies absolute convergence. The paper's subsequent moment models and temporary RH interpretation are not imported. In particular, I do not differentiate the error term in its approximate product theorem.

Fix, independently of the cutoff parameter, a nonnegative function

```text
u in C_c^infinity((sqrt(e),e)),  integral u(y)dy = 1.
x >= e, L = log x,
v(y) = integral_y^infinity u(z)dz,
A_x(z) = integral u(y) exp(-L*z*log y)dy,
R_x(z) = A_x(z)/z,
S_x(s) = sum_(2<=n<=x) Lambda(n) log(n) n^(-s) v(n^(1/L)).
```

The arithmetic coefficients are exactly the original von Mangoldt coefficients, with their prime-power support. The cutoff equals one through `sqrt(x)` and zero from `x` onward. Locally differentiating the exact formula, rather than an asymptotic remainder, gives

```text
F(s) := (zeta'/zeta)'(s)
      = S_x(s) + sum_rho R_x'(s-rho)
        - R_x'(s-1) + sum_(m>=1) R_x'(s+2m).       (1)
```

Zeros are counted with multiplicity; all nontrivial zeros are retained. The formula is used at `s=1/2+i*r`, `r real`, `zeta(s) != 0`. Smooth-cutoff decay justifies locally uniform differentiation away from zeros/poles. The pole term has the displayed minus sign: near `s=1`, it contributes `+1/(s-1)^2`. Each zero term instead contributes `-1/(s-rho)^2`. No zero-free strip is assumed.

This is a legitimate representation to which an estimate could be applied. Its existence is already prior art, and is not the proposed advance.

## 2. What this mechanism actually estimates

There is a useful unconditional **remote-zero** bound. Put `U>=1`, and remove from the zero sum all terms with `abs(Im rho-r)<=U`. For any fixed integer `K>=1`, the remaining sum satisfies

```text
sum_(abs(Im rho-r)>U) abs(R_x'(s-rho))
 <= C_(u,K) * sqrt(x) * L^(1-K)
             * log(2+abs(r)+U) / U^K.              (2)
```

This is an analytic bound with a cutoff-dependent constant determined by fixed derivative norms of `u`, not a numerical certificate or an optimized constant. To see the scale, change variables `q=log y` and write `g(q)=e^q u(e^q)`, supported inside `(1/2,1)`. Integrating `g` and `q*g` by parts `K` times yields, for `z=s-rho`,

```text
abs(A_x(z)) + abs(integral q*g(q)*exp(-L*z*q)dq)
 <= C_(u,K) * sqrt(x)/(L*abs(z))^K,
R_x'(z) = -A_x(z)/z^2
          - (L/z)*integral q*g(q)*exp(-L*z*q)dq.
```

Only `0<Re rho<1` is used for `sqrt(x)`. Summing over unit ordinate intervals using the unconditional `O(log(2+abs(t)))` local zero-count bound gives (2). The trivial-zero terms converge rapidly because the support of `u` stays above 1. The pole term and gamma completion remain explicit.

Thus remote residues can be made smaller than a *previously established* positive margin by enlarging `U`. This is real tail control, but it is not control of the local residues. Increasing `x` also incurs the horizontal `sqrt(x)` allowance; it does not remove all residues for free.

## 3. Why the estimating step does not close

There are two precise limitations, neither an impossibility theorem for the original arithmetic problem.

**A. An all-height distance-free absolute residue error is already unavailable near known critical-line zeros.** If `rho=1/2+i*gamma`, then as `r->gamma`, its term in (1) is

```text
R_x'(i*(r-gamma)) = 1/(r-gamma)^2 + O_u(L^2).
```

Consequently the complete zero contribution cannot be put into a uniformly bounded logarithmic-quotient error across all nonzero points of such a neighborhood. It must retain the pole, or work with the undivided expression and its exact vanishing factors. The positive sign of this particular principal part is helpful, but an absolute-value estimate loses that help.

**B. Keeping nearby residues exactly exposes an unestimated signed local term.** Set `mu_j=integral u(y)(log y)^j dy`. Direct Taylor expansion gives

```text
R_x'(z) = -1/z^2 + L^2*mu_2/2 - L^3*mu_3*z/3
          + L^4*mu_4*z^2/8 + ... .
```

For a hypothetical symmetric pair `rho_+=1/2+a+i*gamma`, `rho_-=1/2-a+i*gamma`, at `s=1/2+i*gamma`, their contribution is therefore

```text
R_x'(-a)+R_x'(a) = -2/a^2 + L^2*mu_2 + O_u(L^4*a^2),
for 0<a*L<=1/2.                                   (3)
```

It is negative and of inverse-square size when `a*L` is small. Ordinate counting, multiplicity bounds and smoothness provide no lower horizontal separation `a` and no compensating positive local arithmetic term. Zero-density estimates that allow even one such exceptional pair do not repair that pointwise defect by counting it sparsely. Taking `L` comparable to or larger than `1/a` is not a supplied schedule: the location is unknown, the signed terms change, and the remote/error budgets also change.

Equation (3) is an algebraic stress test of a residue estimate using only zero geometry/counting. It is **not** an assertion that zeta has this pair, a matched counterexample to the original Euler product, or a claim that the other terms cannot compensate it. Precisely that compensation is missing. No new prime-specific cancellation argument was found that bounds the coupled local zero sum and `S_x` from below.

## 4. Exact transfer and remaining unknowns

Retain the completion

```text
C(s) = -1/s^2 - 1/(s-1)^2 + psi1(s/2)/4,
E(r) = Re(C(1/2+i*r)+F(1/2+i*r)).
```

PR76 gives, away from zeros,

```text
J(r) = p(r)^2 * Y(r)^2 * E(r),  p(r)=r^2+1/4.
```

If `E_local` denotes (1) with the remote nontrivial-zero terms removed, then (2) controls `abs(E-E_local)`. A sign proof would require a **signed lower bound for this actual local expression exceeding that error at every real nonzero point**, using the exact prime coefficients. Neither the original Euler product nor (2) supplies it. There is no established positive margin to choose `U` against. A bare `o(1)` remainder would not suffice in the absence of such a margin; even an `O((1+abs(r))^-2)` remainder needs a compatible signed lower estimate.

At zeros use PR76's undivided `J=p^2*Y'^2>=0`, without assuming simplicity. Multiplying a quotient estimate by `p^2*Y^2` cancels its poles but does not manufacture the missing sign between zeros. No additional implication from the first-Laguerre target alone to RH is claimed.

## 5. Controls and decision

- **NS101:** its reciprocal mixture has changed Euler coefficients and therefore is not a matched control for literal (1). It still rejects an inference that discards arithmetic and keeps only primitive positivity, envelope and symmetry. The mismatch is not a pass for a new estimate.
- **Davenport–Heilbronn:** different coefficients, conductor/completion and absence of the original Euler product prevent a literal match. Generic contour algebra alone still cannot distinguish it. No new numerical screen is warranted.
- **NS100:** no per-slice positivity is used, so its slice failure does not settle this exact prime representation.
- **NS47 / earlier Abel audit:** their fixed-damping, support-independent all-test comparison is not this pointwise second-derivative problem. Only the earlier warning against silently crossing poles applies.

**Budget and falsifiable outcome:** a 1–2 hour paper-only feasibility slot is sufficient for this proposed smoothing mechanism; it should stop at the local-residue decision above. Success would require an independent, original-coefficient lower estimate controlling the signed local prime-plus-residue combination with a compatible error. Failure means do not commission larger prime tables, a damping scan, or another identity audit in this lane. It does not close all Euler-product methods, and this note does not propose an adjacent regularization as the next task.

**Final classification: Same open gap.** The available mechanism estimates the distant error but leaves the local signed arithmetic input untouched. No research row, thaw, theorem node, certificate, manuscript version, or RH/G2 advance follows.
