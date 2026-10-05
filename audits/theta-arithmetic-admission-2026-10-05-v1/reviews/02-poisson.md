# Proposer 02 — divisor-variance regrouping does not supply a signed block estimate

Reviewed baseline: `670864385024041d24612cf620054c1975473928` (PR77), refreshed by the coordinator; worktree HEAD at review: `b914ac47e8006951a22d030e920d592243e7e0fe`. Read AGENTS, the new brief, the coordinator's recorded full-register review, relevant conclusion/continuation entries, current checkpoint and frozen-group summaries, MISSING, PR76's derivation and PR77 reviews 03, 04 and 08. This is a bounded paper method audit, not a replay of historical proofs. Both missing-original recovery groups remain OPEN.

**Wall check: Same open gap — ZERO-GEOMETRY, NS100/101, PR76–77.** What changes: one specific regrouping exposes prime-factor-dependent divisor variances. It supplies an arithmetic identity, but no independently estimating inequality. No candidate is admitted. No scan, certificate, row, thaw, version or outreach was undertaken.

## 1. The concrete mechanism tried

Try to collapse the two Mellin factors by their product index, then use a completed Poisson/Voronoi summation to estimate the resulting signed divisor blocks. This differs from applying an ordinary theta addition identity at mismatched moduli: it keeps both complete factors and exposes an exact prime-power coefficient. It is still only a method proposal until a signed block bound is supplied.

Write, with s-derivatives denoted by dots,

```text
s = 1/2+i*r,                 p = r^2+1/4,
g(s) = pi^(-s/2)*Gamma(s/2), Lambda(s)=g(s)*zeta(s),
A(s) = s*(s-1)*g(s)/2,      xi(s)=A(s)*zeta(s),
C(s) = (log A)''(s)
     = -1/s^2-1/(s-1)^2+psi1(s/2)/4.

D(s) = zeta(s)*zeta''(s)-zeta'(s)^2.
```

On Re(s)>1, absolute convergence permits multiplication and rearrangement:

```text
D(s) = sum_(n>=1) c(n)*n^(-s),
c(n) = (1/2)*sum_(d|n) [log d-log(n/d)]^2,
zeta(s)^2 = sum_(n>=1) d(n)*n^(-s).
```

Here d(n) is the divisor count; it is not a freely chosen coefficient. If `n=prod p^a`, finite independent divisor-exponent averaging gives exactly

```text
c(n) = d(n)/6 * sum_(p^a || n) a*(a+2)*(log p)^2.
```

For a prime, c(p)=(log p)^2; c(1)=0. The formula follows because the mean of `2j-a`, for j=0,...,a, is zero and its mean square is a(a+2)/3. Mixed prime contributions cancel in this finite variance computation. This is the step that uses the original Euler coefficients and unique factorization, beyond reflection symmetry.

The complete identity to which an estimate would have to transfer is

```text
J(r) = 4*(xi*xi''-xi'^2)(s)
     = p^2*g(s)^2 * [D(s)+C(s)*zeta(s)^2].          (1)
```

At s=1/2+ir this value is real. Formula (1) follows from `X(r)=xi(s)/2` and the product rule. It retains the gamma contribution and the two polynomial-completion terms, and is precisely PR76's complete J. No division by zeta occurs, so zeros and multiplicities are retained. J>=0 would give first-Laguerre positivity only.

## 2. Completion is mandatory, not a removable error

The Dirichlet identities just written have their ordinary absolute-convergence domain Re(s)>1. They cannot be evaluated termwise at Re(s)=1/2. Even `sum d(n)/sqrt(n)` diverges. A positive-coefficient observation in the right half-plane is therefore not an estimate on the required line.

One legitimate starting point for completion is the complete two-shift product

```text
P(s,z)=Lambda(s+z)*Lambda(s-z),
(1/2)*partial_z^2 P(s,0)
    = Lambda(s)*Lambda''(s)-Lambda'(s)^2.
```

Its exact functional equation is `P(s,z)=P(1-s,z)`. Multiplying by the corresponding two polynomial factors gives the xi product and includes the rest of (1). Thus any smoothed Mellin contour construction must first retain the complete two-variable product, including poles/residues and parameter derivatives of gamma and smoothing weights. An unsmoothed finite Dirichlet block is not that completed object.

This starting point avoids the illegitimate full-line theta-summand interchange catalogued in PR77 review 03. It does not repair that interchange retroactively. Nor can the two theta moduli be set equal, or the parity/coupling conditions of PR75 be discarded. A correctly derived completed divisor formula would just be another representation of the full pair.

I did not import a prior-art Voronoi theorem for c(n). Parameter differentiation of a generalized divisor identity would require its full statement, domain, differentiation control and residue terms. An arXiv discovery search supplies no substitute for that applicability check. No such theorem is being claimed to prove a sign here.

## 3. Why the obvious estimating step fails admission

The proposed estimating technique was to exploit c(n)>=0, separate the explicit summatory main terms, and control completed remainder blocks by absolute exponential-sum/discrepancy estimates. There is no independently positive main quantity in this scheme on the critical line.

Already an individual uncompleted coefficient contribution in (1), for fixed n>=2, is

```text
T_n(r) = p^2*Re{g(1/2+i*r)^2
                 *[c(n)+C(1/2+i*r)*d(n)]*n^(-1/2-i*r)}.
```

Its dominant phase as r tends to positive infinity is

```text
r*log(r/(2*pi*n))-r-pi/4+O(1/r).
```

Stirling's expansion gives C(1/2+ir)=O(1/r), while c(n)>0 is fixed. The phase grows without bound and is eventually strictly increasing. Consequently the leading cosine takes both signs along arbitrarily large sequences; the lower-order completion coefficient does not turn this uncompleted block into a nonnegative block. This is an elementary check of the suggested termwise inference, **not** a counterexample to a fully completed block or to J.

A finite fixed square prefix is an even less suitable substitute: PR73 already proves its eventual first-Laguerre failure, including the nonzero reflection jet. The proposed product-index regrouping does not erase that fact. A valid completion must retain infinite complementary terms and their mixed contribution.

One can instead leave all oscillatory blocks intact and hypothesize a lower bound for their sum. But without a separate cancellation mechanism this is merely (1)'s sign again. Likewise, a summatory-error bound could justify continuation or control the magnitude of a remainder, yet its absolute value cannot supply the absent lower main term. This is a failure to provide a method, not a theorem that no refined signed divisor estimate can work.

## 4. The exact unfilled candidate specification

1. **Expression:** the completed coupled divisor quantity in (1), or a fully specified original/dual block decomposition equal to it. No such decomposition with an independent signed estimating lemma has been supplied.
2. **Coefficients:** exact d(n) and c(n) above, original conductor-one gamma and polynomial completion; no free reweighting or truncated replacement.
3. **Range:** every real r, or an explicit eventual range plus an independently proved compact-range transfer. Zeros must be included by the undivided formula. No uniform onset is available.
4. **Method:** multiplicative divisor variance followed by completed Poisson/Voronoi summation was examined. Positivity of coefficients and absolute remainder estimates do not give its required signed lower bound. A specific further prime-dependent cancellation mechanism is missing.
5. **Transfer:** a complete lower bound in (1) gives J>=0 directly, with all gamma/polynomial terms. A partial block estimate additionally needs a compatible signed complementary-block bound, uniform remainder control and any compact-range proof. These are unproved inputs; they cannot be hidden in a phrase such as “the tail is small.”

Because item 4 has no estimating step and the partial version leaves item 5 unfilled, this is a **stop specification**, not an admissible conjectural candidate. Requiring an estimate to be proved before admission would be too strict; requiring that an actual technique be named is appropriate.

## 5. Controls and bounded decision

- NS101 changes the integer-square lattice and these Euler coefficients. It is not a matched counterexample to a hypothetical original-coefficient bound. It does match an argument that keeps only generic completion, smoothness and primitive positivity; that inference already fails. The arithmetic mismatch is not a passed screen.
- NS100 excludes positive slices, which this completed regrouping does not assume. It does not settle the full sum.
- PR73 excludes fixed reflected prefixes, not an exact infinite completed divisor identity. It does settle the attempted use of such prefixes as nonnegative comparison blocks.
- Davenport–Heilbronn has different coefficients, conductor and gamma factor; it does not share the literal arithmetic premise. Generic contour/symmetry manipulations alone would still be insufficient. No numerical control run is warranted without an estimating statement.
- NS74/83 concern NB target sensitivity and dyadic rates, not this theta expression.

**Budget/decision:** this bounded paper attempt ends here; allocate zero computation budget to the coefficient-positivity/Voronoi-completion idea as presently stated. Success of a future independently formulated signed block lemma would change the first-Laguerre proof obligation through (1), not establish RH. The present failure only rejects this missing-method proposal and its termwise shortcut. It leaves original arithmetic Poisson methods open.

**Final wall check: Same open gap.** Closest: PR77 reviews 03/04 and PR76. Prime-factor structure was exposed, but the coupled signed estimate remains absent. Stop this proposer lane; no row, thaw or version.
