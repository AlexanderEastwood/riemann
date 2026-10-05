# Proposer 3 — pointwise Riemann–Siegel quadratic estimate

**Disposition: no candidate admitted.** I examined one specific estimating mechanism: expose the complete main-sum quadratic, group its ratio and product phases, and try Poisson/stationary-phase cancellation at the Riemann–Siegel length. The algebra gives a precise arithmetic sum, but the proposed cancellation step has no sign-producing estimate. An accurate Riemann–Siegel expansion alone does not repair that omission.

**Wall check: Same open gap.** Closest: PR77 reviews 09, 04 and 08, with PR76's complete target. What changes: the proposed pointwise arithmetic estimating step is made explicit below. No new arithmetic hypothesis or bound has been admitted. This is narrower than repeating the general high-height review, and it ends without a scan.

Baseline: public commit `670864385024041d24612cf620054c1975473928`; parent review record in `../review-record.json`. Read current AGENTS, the six-agent brief and the three assigned closest reviews. The coordinator records the refreshed conclusion/dependency review; this note is not a replay of historical proofs or certificates. Both missing-original recovery groups stay OPEN. No external theorem is newly imported here: the proposed Poisson mechanism is assessed through its explicit phase and scale, not a cited remainder theorem.

## 1. Exact arithmetic expression

Use the usual continuous real gamma phase and the exact Hardy function:

```text
theta(r) = Im log Gamma(1/4+i*r/2) - (r/2)*log pi,
Z(r) = exp(i*theta(r))*zeta(1/2+i*r),
p(r) = r^2+1/4,
A(r) = p(r)*pi^(-1/4)*abs(Gamma(1/4+i*r/2))/4,
X(r) = -A(r)*Z(r),
d(r) = (log A(r))''.
```

Thus, without dividing by Z or X,

```text
J(r) = 16*A(r)^2*Q_d[Z](r),
Q_d[F] = F'^2-F*F''-d*F^2.
```

For every fixed positive integer N define

```text
a_n = n^(-1/2),
v_n(r) = theta(r)-r*log n,
w_n(r) = theta'(r)-log n,
P_N(r) = 2*sum_(n<=N) a_n*cos(v_n(r)),
R_N(r) = Z(r)-P_N(r).
```

R_N is the **complete exact remainder**, not an omitted O-term. All derivatives below are taken with N fixed. Only after taking derivatives may one evaluate at `N=floor(sqrt(r/(2*pi)))`. At an integer-cutoff transition, either neighboring fixed-N identity remains valid with its own complete remainder; there is no derivative of the floor function.

Put `delta_nm=r*log(m/n)` and `sigma_nm=2*theta(r)-r*log(n*m)`. Elementary differentiation gives

```text
Q_d[P_N] = sum_(n,m<=N) (n*m)^(-1/2) * {
  [(w_n+w_m)^2-2*d]*cos(delta_nm)
 +[(w_n-w_m)^2-2*d]*cos(sigma_nm)
 +2*theta''*sin(sigma_nm)
}.
```

In particular, both phases, the common phase acceleration, and the gamma-curvature term survive. The exact remainder correction is

```text
T_N = 2*P_N'*R_N' - P_N*R_N'' - P_N''*R_N
      + R_N'^2 - R_N*R_N''
      - d*(2*P_N*R_N + R_N^2),
Q_d[Z] = Q_d[P_N]+T_N.
```

The original coefficient condition is exactly `a_n=n^(-1/2)`, with frequencies `log n`, the original gamma phase, and the original zeta remainder. Replacing these by arbitrary positive weights, independently phased terms or a generic reciprocal kernel changes the claim.

## 2. The attempted estimating method and where it stops

The ratio phase carries multiplicative ratios; the product phase can be grouped by `k=n*m`. Its squared-frequency coefficient becomes the explicit restricted divisor sum

```text
b_N(k) = k^(-1/2) *
         sum_(n*m=k; n,m<=N) (log(m/n))^2.
```

This is a concrete arithmetic coefficient, but its nonnegativity does not imply the sign of its cosine transform. The theta'' and d terms involve the corresponding restricted divisor count and cannot be discarded. Keeping only the product phase would change the complete quadratic.

The candidate method was two-variable Poisson summation, or a one-variable stationary-phase transformation inside each dyadic block, followed by retaining the paired ratio/product contributions. At a block `m` comparable to N and `N` comparable to `sqrt(r/(2*pi))`, the phase derivative in cycles has size

```text
abs(partial_m(delta_nm)/(2*pi)) = r/(2*pi*m),
abs(partial_m(sigma_nm)/(2*pi)) = r/(2*pi*m).
```

The associated stationary dual integers therefore also have size N and occupy a block of comparable length. This is the balanced, self-dual scale, not a regime in which the transformed off-diagonal sum is automatically a lower-order error. The original coefficient amplitudes and both common-phase terms must still be compared with their dual contributions. Neither a positive transformed kernel nor a signed domination identity has been supplied.

A simple scale check shows why termwise bounds are inadequate. If `theta'=log N` at leading order and `w_n=log(N/n)`, the positive ratio-phase diagonal is

```text
D_N = 4*sum_(n<=N) w_n^2/n ~ (4/3)*(log N)^3.
```

Writing `S_j=sum_(n<=N) n^(-1/2)*log(N/n)^j` gives
`S_j ~ 2^(j+1)*j!*sqrt(N)` for j=0,1,2. Consequently the phase-free coefficient budget for the ratio and product squared-frequency terms together is

```text
sum_(n,m<=N) (n*m)^(-1/2) *
  [(w_n+w_m)^2+(w_n-w_m)^2]
= 4*S_0*S_2 ~ 128*N.
```

These elementary leading scales describe a proposed upper-bound strategy, not actual magnitudes or signs of the oscillatory sum. They show that taking absolute values cannot establish diagonal domination from this budget. They do not prove that the true signed sum is negative or that every stationary-phase strategy fails. The needed arithmetic improvement is exactly a **pointwise, jointly phased lower comparison**, uniform even at cancellation heights. I found no independently justified mechanism producing it.

## 3. Uniform transfer, including zeros

A prospective arithmetic lemma would have to imply

```text
Q_d[P_N](r)+T_N(r) >= 0
for every real r>=R_0, N=floor(sqrt(r/(2*pi))),
```

for a specified finite R_0, together with a separate complete proof on `[0,R_0]`. Evenness supplies negative heights. All orders 0,1,2 of the exact remainder must be retained. This transfer proves only the first-Laguerre target, not RH.

One could instead use derivative error bounds and a lower bound for the main quadratic exceeding their full induced budget. That is PR77 review 09's existing architecture. Merely conjecturing the displayed complete inequality, or naming Poisson summation without a sign estimate after transformation, does not add an estimating lemma. A lower comparison for the restricted divisor/ratio sums plus a compatible signed remainder comparison would be additional **unproved inputs**, not consequences of their explicit coefficients.

No strictly positive uniform slack is assumed. At a multiple zero of Z, `Q_d[Z]=0`; a strictly positive eventual bound would prove eventual simplicity as an additional result. At simple zeros it equals `Z'^2`, with no supplied quantitative lower derivative bound. Our undivided identity covers all zeros, stationary points and cutoff transitions. Removing small neighborhoods or asserting an almost-everywhere estimate would leave an unspecified bridge and is not proposed.

## 4. Controls, decision and budget

- **NS100:** its negative original slice blocks slice positivity, whereas the displayed expression retains the full transform. It does not decide this pointwise quadratic.
- **NS101:** the mixture changes the exact single-lattice coefficients, original Hardy arithmetic sum and original remainder; the generic rescaling by the same gamma factor is still available. It is not a literal matched counterexample to an original-coefficient estimate. It still rejects replacing that estimate by generic smoothness, reciprocity or positive-kernel data. The mismatch is not a passed screen.
- **Davenport–Heilbronn:** conductor, completion and coefficients differ; a literal Riemann–Siegel coefficient match is absent. A generic oscillatory-algebra argument would require a matched analogue before any inference, but no such argument is admitted here.
- **PR73:** a growing Hardy sum with its complete remainder is not the fixed reflected theta prefix covered by its cusp obstruction. That mismatch supplies no lower bound.

**Stop:** no numerical control screen or computation budget is authorized by this proposal, because the estimating mechanism remains unspecified at the decisive signed step. A future explicit paired-sum transformation with a sign-controlling remainder deserves at most one hour of paper audit before any scan. Success would admit a particular arithmetic estimating lemma and its full transfer; failure would reject that lemma, not the whole original-theta or high-height route. No row, thaw, version or RH/G2 claim follows.

**Final wall check: Same open gap — PR77 review 09 and PR76.** The pointwise signed arithmetic lower comparison and compatible complete remainder estimate remain unproved; changing to Riemann–Siegel coordinates has not supplied them.
