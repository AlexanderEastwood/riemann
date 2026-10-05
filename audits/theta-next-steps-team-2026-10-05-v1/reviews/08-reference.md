# Reviewer 8 — stop the unmatched Bessel/completion transfer

Reviewed remote: `18d324703969b5bcc9aa94043cfd90a6e8211f34` (PR76);
working HEAD: `32f599ced1abb2bf2376a715042e6e4101591639`. Read AGENTS,
the conclusion register and continuation demands, current README/checkpoints,
NEXT_STEPS freezes, MISSING, PR76's derivation, and PR74 reviews 03/04.
The coordinator's refresh is recorded in `../review-record.json`. This is
a method/dependency audit, not a historical proof replay. Both missing-original
groups remain OPEN.

**Wall check: Same open gap — ZERO-GEOMETRY, NS100/101, PR76.**
What changes: nothing in the original arithmetic hypothesis. The question is
whether two existing supporting estimates concern compatible objects and rates.
They do not supply the missing comparison. No independent estimating method
is admitted; stop this proposed combination before a scan.

## Exact obligation, including zeros

Retain the original complete even kernel, whose half-line expansion is

```text
phi(u) = sum_(n>=1) [2*pi^2*n^4*exp(9u/2)-3*pi*n^2*exp(5u/2)]
                    *exp(-pi*n^2*exp(2u)),   u>=0,
X(r) = integral_R phi(u)*exp(i*r*u)du.
```

Fix `a,kappa>0`, `H(r)=kappa*K_(ir/2)(a)` and
`e(u)=phi(u)-kappa*exp(-a*cosh(2u))`. The complete errors are

```text
E_j(r) = integral_R (i*u)^j*e(u)*exp(i*r*u)du, j=0,1,2,
Q_H(E) = 2*H'*E_1-H*E_2-H''*E_0+E_1^2-E_0*E_2,
L1[X] = m_H+Q_H(E),  m_H=L1[H].                         (1)
```

These are identities, **not an estimating method**. All integrals and
derivatives are legitimate; the complete n-squared series and the modular
cancellation at zero remain. The missing independent arithmetic input is
`Q_H(E)(r)>=-m_H(r)` for every real r, established by something other than
rewriting `L1[X]>=0`. With that input, (1) gives first-Laguerre positivity
and the positive definiteness of the complete associated kernel. PR76 then
gives its equivalent corrected inequality for `Y=4X/(r^2+1/4)`. No further
implication to RH, G2 or the cofinal Weil floor is supplied.

No quotient by X or H appears, so this includes all their zeros. A strict
fractional margin `Q_H(E)>=-(1-delta)*m_H`, delta>0, would additionally
exclude multiple real zeros of X; that stronger demand cannot be quietly
substituted for the non-strict target.

## What the reference theorem actually provides

One bounded arXiv recheck: [Gasper 0801.2996v1](https://arxiv.org/html/0801.2996v1),
Eq. (2.6), has a>0 and arbitrary real x,y. Its y-squared coefficient gives

```text
m_H(r)=kappa^2/4 * integral_0^1 [-log(t)]/[t*(1-t)]
                              *K_(ir/2)(a/sqrt(t))^2 dt > 0.
```

This holds through reference zeros. It contains no original-theta error.
Section 3 proves real zeros for the shifted-order Pólya reference, but the
extra `g_(t,c)` positivity in Eq. (3.3) is conjectural there; it cannot be
imported as the same square-margin formula. No broader literature claim
or modified-Pólya comparison is made.

An absolute sufficient replacement for the missing signed input is

```text
2*abs(H')*eps_1+abs(H)*eps_2+abs(H'')*eps_0+eps_0*eps_2 <= m_H,
abs(E_j)<=eps_j, j=0,1,2, every real r.                  (2)
```

Constant absolute moment allowances fail: their positive `eps_0*eps_2`
cannot fit the shrinking margin. At a reference zero, the surviving
`H' E_1` term still demands derivative-scale control. Real-space tail
matching and a small kernel norm supply neither oscillatory cancellation
nor this derivative comparison. Failure of these allowances does not
prove failure of the actual signed expression.

## Why the smooth completion does not finish the transfer

PR74 review 03 controls `R_M=X-X_M` and its first two derivatives, with
`abs(L1[X]-L1[X_M])<=Btilde_M`. It does **not** control `X-H`.
Writing `U_M=X_M-H` leaves the complete sufficient requirement

```text
m_H+Q_H(U_M) >= Btilde_M, every real r.                  (3)
```

The quadratic terms in U_M are indispensable. As M grows, U_M tends to
`X-H`, not to zero; making R_M arbitrarily small does not reduce that
remaining comparison. Formula (3) is the existing lower-margin input,
not a new arithmetic lemma.

There is also a concrete rate mismatch if using the available crude
Bessel lower bound. PR74 gives

```text
m_H >= kappa^2*log(2)*exp(-4V-2)/(16V),
V=max(2a,r^2/4,1).
```

Thus that **proved analytic allowance** is of order `r^(-2)*exp(-r^2)`.
The displayed completion budget for M=O(abs(r)) decreases only exponentially
in abs(r), so it does not eventually fall below this allowance. Faster
decay than `exp(-pi*abs(r)/2)` alone is insufficient when using that bound.
A quadratic M can improve the remainder budget against this crude allowance,
but still supplies nothing about (3). This is not a recommendation to
enlarge the cutoff or a claim about the sharp Bessel-margin asymptotic.

Every r derivative in the completion estimate is taken at fixed M. One
may select M(r) pointwise afterward, but cannot differentiate the resulting
integer-cutoff composite. A smoothly varying Bessel parameter or amplitude
likewise introduces chain-rule terms and loses the quoted fixed-reference
margin unless those additional terms are controlled.

## Controls and bounded decision

NS100 excludes per-slice positivity; (1) retains the full integral.
NS101 shares generic transform/perturbation algebra, and PR74/76 prove
actual first-Laguerre failure for its stated beta range. It changes the
single-lattice coefficients and original Jacobi IVP. Hence those structural
properties cannot prove (1)'s sign, while a genuinely original-coefficient
estimate remains unexcluded. Off-axis zeros alone are not used as a
first-Laguerre counterexample. PR73's fixed reflected-prefix cusp hypothesis
does not apply to these smooth references.

**Next allocation: at most two hours, conditional on a concrete proposed
oscillatory estimating mechanism.** Spend one hour deriving its complete
orders-0/1/2 error or signed mixed bound and one checking the reference
margin, compact region, every real zero, and matched controls. Success
means a separately justified estimate meeting (1) or (2), permitting a
focused proof audit of the first-Laguerre target only. If the output is
again (3), a fixed moment allowance, or an undifferentiated asymptotic,
stop; no automatic adjacent-reference or cutoff search. No present
computation budget, new row, thaw, version, commit, push or outreach.

**Final wall check: Same open gap.** Reference positivity and completion
accuracy remain separate; the original signed comparison is unestimated.
RH, G2 and the cofinal signed-arithmetic lower bound remain open.
