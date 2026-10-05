# Agent 4 — arXiv mechanisms and the reference-margin gap

Reviewed mathematical baseline: `5434d96f0034f842b0229f1d69dbbf3fb7fea270`
(merged PR73). Current audit scaffold: `971c8bd02c834cf31ab98ea2a50060289fbece40`;
its three changed files add the assignment/record, not a mathematical premise.
Read AGENTS, the shared brief/proposal gate, relevant ZERO-GEOMETRY scopes,
NS100/101 arguments and PR72/73 reports/support notes. The coordinator's
104-node review is recorded in BRIEF; I did not replay historical proofs or
external certificates. This is a bounded primary-source applicability audit
with paper derivations, not a numerical or symbolic scan.

**Wall check: Same open gap.** Closest: NS100/101, PR72/73. What changes:
check a smooth, real-zero Bessel/Pólya reference and its actual Laguerre
margin, then state the complete original-theta comparison that would be
needed. Smooth reference kernels escape PR73's reflected-prefix hypothesis;
that alone supplies no arithmetic estimate or thaw.

## Question, dependency and outcome

Can a reviewed arXiv theorem estimate
`L1[X](r)=X'(r)^2-X(r)X''(r)` for every real `r`, where
`X=xi(1/2+ir)/2` is the complete original theta transform?

**A useful reference theorem exists; a transfer estimate for the original
theta does not emerge from these sources.** The concrete dependency is

```text
positive reference margin m_H(r)
 + original-theta error estimates satisfying (T), for every real r
 => L1[X](r)>=0 for every real r
 => the complete associated kernel C is positive definite.
```

This does not imply RH from the first inequality alone. No original-theta
candidate is admitted on the basis of the reference result.

## 1. A genuine positive reference margin

[Gasper, arXiv:0801.2996v1](https://arxiv.org/html/0801.2996v1), Eq. (2.6),
is a square-integral identity for `K_{iz}(a)`, with **a>0**, `z=x+iy`,
**x,y arbitrary real**. Taking its `y^2` coefficient and using
`2F1(1,1;2;1-t)=-log(t)/(1-t)` yields

```text
B_a(r)=K_{i*r/2}(a)=integral_R exp(-a*cosh(2u))*exp(i*r*u) du,

m_a(r):=L1[B_a](r)
 = (1/4)*integral_0^1 [-log(t)]/[t*(1-t)]
                   *K_{i*r/2}(a/sqrt(t))^2 dt > 0.       (R)
```

The factor `1/4` is the frequency chain rule. At `t=1` the weight is
removable; at `t=0` Bessel decay controls the integral and differentiation.
Strictness follows because the real Bessel function, as its positive
argument varies, is not identically zero. This includes reference zeros.

The same source proves real zeros for
`F_{a,c}(z)=K_{i*z+c}(a)+K_{i*z-c}(a)`, **a>0, c real**.
The standard Pólya model in our normalization is

```text
p(u)=4*pi^2*cosh(9u/2)*exp(-2*pi*cosh(2u)),
H_P(r)=integral_R p(u)*exp(i*r*u)du
      =2*pi^2*F_{2*pi,9/4}(r/2)=Xi_star(r)/2.
```

Do not copy the manifest positivity of (R) to that shifted sum: the extra
`g_{t,c}` term in Gasper's Eq. (3.3) has positivity **conjectured**, not
proved there. The separate real-zero proof remains valid.

### An explicit, crude reference lower bound (derived here)

To make clear that reference positivity need not remain an unspecified
margin, put `nu=r/2`, `V=max(2a,nu^2,1)`. Changing variables
`v=a/sqrt(t)` in (R) gives

```text
m_a(r)=integral_a^infinity
 log(v/a)/[v*(1-a^2/v^2)] *K_{i*nu}(v)^2 dv.
```

From `cos(nu*u)>=1-nu^2*u^2/2` and integration by parts,

```text
integral_0^infinity u^2*exp(-v*cosh u)du <= K_0(v)/v,
K_{i*nu}(v) >= (1-nu^2/(2v))*K_0(v).
```

Indeed, the first inequality follows from
`v*integral u*sinh(u)*exp(-v*cosh u)du=K_0(v)` and
`u*sinh(u)>=u^2`. For `v>=1`, integration over
`0<=u<=1/sqrt(v)`, where `cosh(u)<=1+u^2`, gives
`K_0(v)>=exp(-v-1)/sqrt(v)`. Restricting the positive integral to
`V<=v<=2V` therefore proves, for **every a>0 and r real**,

```text
m_a(r) >= [log(2)/(16*V)]*exp(-4*V-2) > 0.              (R0)
```

This elementary supporting estimate has no original theta content. It
decays very rapidly and is not proposed as a competitive comparison bound.
Neither (R) nor (R0) is a positive constant floor in frequency:
`B_a`, its derivatives and its Laguerre expression tend to zero.

## 2. The missing arithmetic comparison, with all cross terms

Fix a smooth real reference `H`, and let `E=X-H` on the real axis. Then

```text
L1[X]=L1[H]+2*H'*E'-H*E''-H''*E+(E')^2-E*E''.
```

If `|E^(j)(r)|<=epsilon_j(r)`, `j=0,1,2`, a sufficient bound is

```text
2*|H'(r)|*epsilon_1(r)
 + |H(r)|*epsilon_2(r) + |H''(r)|*epsilon_0(r)
 + epsilon_0(r)*epsilon_2(r)
 <= m_H(r) <= L1[H](r),     for EVERY real r.            (T)
```

This retains all potentially negative terms and discards only `(E')^2`.
For `H=kappa*B_a`, fixed `kappa>0`, use `m_H=kappa^2*m_a` (or the lower
bound (R0)). Its errors are the complete oscillatory integrals

```text
E^(j)(r)=integral_R (i*u)^j
 [phi(u)-kappa*exp(-a*cosh(2u))]*exp(i*r*u)du.
```

For the Pólya reference replace the second kernel by `p(u)` and establish
a usable reference lower bound separately. No division by `H` or `X`
is allowed at their zeros. A signed direct lower bound for the displayed
cross-term expression could replace the absolute sufficient bound (T).

The original arithmetic would enter **here**: control of these complete
errors using the exact integer-square theta coefficients and modular
cancellation, uniformly in frequency. It is absent from (R), (R0) and
the generic perturbation algebra. Pointwise closeness of real kernels,
matching their value at zero, or matching real tails does not imply (T).

For example the absolute moment allowances
`epsilon_j=integral |u|^j*|phi-h|du` are constants. For a nonidentical
Bessel reference, the positive constants `epsilon_0*epsilon_2` already
prevent (T) at sufficiently large height, since `m_a(r)->0`. Even without
that product, at a reference zero (T) demands an error on the shrinking
derivative scale. This rejects the fixed absolute allowance, not the
actual oscillatory error or all smooth-reference strategies.

## 3. Bounded source checks beyond the square identity

| arXiv primary source | Checked scope and relevance |
|---|---|
| [Paris 2108.01447v1](https://arxiv.org/html/2108.01447v1), Sections 2–3 | Large-order asymptotics and large-index zeros of `K_{i*nu}(a)` with **fixed a>0**, `nu->+infinity`; the real saddle parametrization uses `nu>a`. This is reference information, not an all-height original-theta error bound. The displayed asymptotic expansion alone is not a certified differentiated remainder through order two for (T), and does not cover the turning/compact region. |
| [Shi 1502.06844v1](https://arxiv.org/html/1502.06844v1), Sections 1 and 4 | The advertised matching is at `t=0` and as **t->infinity**, plus real zeros of modified transforms; it is not convergence to the original as the model index grows. In the source clock `Phi(t)=phi(t/2)` and its transform is `Xi(2z)`, so a model becomes `H(r)=Xi_model(r)/2` after `t=2u`. The reported real-space integral differences and plots are not (T), regardless of whether every model theorem is accepted. No modified-model theorem from this paper is a premise of this note. |
| [Wagner 2108.01827](https://arxiv.org/html/2108.01827), Theorem 1.2 | For a function in the **shifted Laguerre–Pólya class**, each fixed `d` has `N_3(d)` such that `L_k[f^(n)](x)>=0` for all `0<=k<=d`, **n>=N_3(d)** and real `x`. The Xi application is to the indicated coefficient-generating transform (`Xi(i*sqrt(x))` in the text), not directly our `X(r)`. Neither the derivative threshold nor this change of variable yields `n=0`, original-frequency (T); no backward derivative transfer is supplied. |

The search stopped with these four sources. This is not an exhaustive
literature search, a novelty assessment, or a claim about the current
global open status of every related inequality. Csordas 1309.0055 and
Planat–Sole 2608.19160 remain the already-reviewed context; their criterion
and real-curvature conclusions do not furnish the missing comparison.

## Controls, consequence and stop

- **NS100:** its failure of individual-slice positivity does not refute (T),
  which retains the complete transform. No per-slice sign is assumed.
- **NS101:** it shares generic transform/error calculus, but does not share
  the original theta IVP. No error bound (T) for it is established, and its
  off-axis zeros alone do not establish failure of its first Laguerre sign.
- **Davenport–Heilbronn:** different coefficients/completion; no claim that
  it satisfies the proposed original-theta comparison. Generic perturbation
  algebra is valid for it too, but is not asserted to imply real zeros.
- **PR73:** the smooth reference has no reflected-prefix cusp, so the
  fixed-prefix obstruction does not apply. Smoothness does not estimate
  the remaining arithmetic error. No finite-prefix strategy is reopened.
- **NS74/83:** Nyman–Beurling and dyadic-rate hypotheses do not match.

Success would mean proving (T), or a stated signed replacement, for the
complete original kernel and every real height; that would establish this
first-Laguerre target only. The present outcome changes route selection:
reference positivity is available, but this literature search supplies no
admissible arithmetic transfer. Stop before scans or model fitting.

Budget used: one bounded arXiv-source pass and the paper checks above.
Next budget: none for computation. Reopen only upon a concrete proposed
all-height original-theta error estimate (with its proof mechanism), then
allow one bounded applicability audit before any numerical work.
No NS row, manuscript change, certificate, commit/push or outreach.

**Final wall check: Same open gap — ZERO-GEOMETRY, NS100/101, PR72/73.**
The Bessel reference has an explicit positive margin; the complete original
theta comparison remains unestimated. RH, G2 and the cofinal signed
arithmetic lower bound remain open.
