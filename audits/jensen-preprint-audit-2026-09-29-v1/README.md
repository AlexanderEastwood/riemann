# Holland Jensen preprint: focused proof and dependency audit

Date: 2026-09-29. Reviewed repository: `aa2d52b4bb37acce571cfd9db787ad8627b469af`.
Source: Jonathan Holland, [arXiv:2608.08682v1](https://arxiv.org/abs/2608.08682v1).

**Wall check: Same open gap — ZERO-GEOMETRY / NS100's second proposal.**
This is validation of an existing external argument, not a new candidate,
research row, theorem node, control pass or thaw. The coordinator reviewed
all 104 conclusion records and 14 continuation demands; historical proofs
and certificates were not replayed. Both missing-original groups stay OPEN.

## Outcome and limits

No fatal defect was found in the checked hyperbolicity chain, when its
parameters retain the relations supplied by the matching construction.
Lemma 7.3 should retain that qualification explicitly if reused: its four
displayed range inequalities alone do not imply its uniform localization
conclusion. The degree-two family below demonstrates this scope issue.
It does not contradict the application to the actual matched parameters.

This is a focused audit, not full independent verification of the preprint.
The complex saddle theorem and finite-free preservation theorems are
inherited inputs checked against primary statements. The entire uniform
matching expansion has not been independently reconstructed term by term.
The joint semicircle theorem was not independently audited. No effective
numerical threshold K, interval certificate, zero scan, or RH implication
is claimed. No separate agent or external expert reviewed this turn.

## Independent checks

The source uses gamma(n)=n! M_n/(2n)! for the even theta moments M_n.
Duplication therefore gives R_j=E_n[U^(2j)]/[4^j(n+1/2)_j]. The factorial
ratio is essential. The theta integral can also be reconstructed directly:
with x=exp(2u), its measure is
`[4*x^(5/4)*theta_+''(x)+6*x^(1/4)*theta_+'(x)] dx`.
Two integrations by parts give the moment formula; the checked integrand
is `x^(-3/4)*(4*k*(k-1)*log(x)^(k-2)-log(x)^k/4)`.
Boundary terms vanish for Re(k)>1 and by theta decay at infinity. Maxima
checks the algebra, not these analytic boundary limits. The factor-eight
normalization difference with GORTTW is harmless for ratios; replacing
gamma by raw moments would not be harmless.

The stability step can be verified without any zeta assumption. Newton
interpolation expresses a coefficient multiplier through finite differences.
If its first five sampled values are 1, the error starts at k=5. Cauchy's
estimate in a tube of radius 2r bounds each normalized finite difference by
epsilon/(2r)^k. A critical-point derivative bound r^k then gives total error
at most epsilon/16. For epsilon<16 the signs at all critical points, zero,
and positive infinity give the full number of distinct positive roots.
There is no inference from numerical root proximity here.

The limiting matching system has solution (a,b,c)=(6/5,1/3,1/24).
The archived script verifies its exact equations, Jacobian inverse and
contraction constants. The resulting parameter sizes are A of order n log n,
B,C,D of order n and C-D of order n/log n. The Jacobi factors have positive
simple roots in this range. The cited finite-free positivity and logarithmic
mesh results preserve that property. The reciprocal normalization is
compatible with the standard convolution. The MSS maximum-root bound is
explicit in arXiv v2 Theorem 1.6; the published Theorem 1.13 is a stronger
transform inequality with that bound as a limit. Numbering differs between
versions, so it is not a missing inequality.

For the analytic remainder, five derivatives of the log coefficient ratio
leave the theta log-moment fifth derivative and paired polygamma terms.
The inherited sectorial estimate and parameter closeness bound these by
O(1/(n^4 log n)). Five exact matching zeros and complex divided differences
give a factor of order r^5, where r is of order sqrt(nd). Thus the governing
small quantity is d^(5/2)/(n^(3/2) log n). The needed complex neighborhood
has d+2r=o(n), so it stays inside the asymptotic domain in the stated range.

The derivative-ratio step is an a priori estimate, not circular. At a
critical point set T_k=y^k p^(k)(y)/p(y), and M=max |T_k|/r^k. Simplicity
ensures p(y) is nonzero. The exact perturbed Jacobi equation, backward
recurrence for its defect, and differentiated Jacobi recurrence give
coefficients bounded by 1/4 after choosing constants and then n large.
Since T_0=1 and T_1=0, any M>1 would occur at k>=2 and imply M<=3M/4.
The factorization and both coefficient recurrences are checked symbolically
for a general monomial, rather than sampled degrees. Analytic smallness
still depends on the matched parameter sizes and root localization.

## Lemma 7.3 scope: the construction cannot be discarded

The proof invokes D comparable to B. The matched construction supplies it,
but the displayed assumptions A>=8B, B,D>=K_r*d and
4d<=C-D<=D/4 alone do not.

To see the distinction exactly, fix d=2 and any D>=max(2K_r,32), put C=5D/4,
A=8B, and let B tend to infinity. All four inequalities eventually hold.
After y=Bx the model is

`p_F(Bx) = 1 - 2x + kappa_B*x^2`,

where

`kappa_B = (1+1/(8B))*(5D+4)/(5(D+1)*(1+1/B))`.

Its limit is 1-t^2, with t=1/sqrt(5(D+1))>0. The limiting normalized roots
are 1/(1+t) and 1/(1-t), both separated from 1 by a positive constant.
Consequently |y-B| is of order B, not bounded by a universal constant
times sqrt(Bd). Positivity and simplicity are not the issue; localization
is. The script checks the coefficient, deficit and root identities exactly.

Use Lemma 7.3 only with the earlier matching construction, or add a suitable
uniform lower bound D>=cB. This is a scope clarification for an external
lemma, not a counterexample to the main theorem or to a repo result.

## Research decision

The claimed region n^3 log^2(n+2)>=K d^5 still forces d/n to zero as
n grows. For fixed n it permits only bounded d; it never reaches the
unshifted all-degree requirement. Enlarging this asymptotic region alone
does not provide the missing backward-in-shift arithmetic mechanism.
NS100 already names that exact obligation. The present audit lowers the
priority of a suggestion to use this preprint as our next RH proof lane.
Keep the method as a source; do not start larger root scans or higher-order
matching without a complete, independently testable transfer to that input.

Farmer's 2022 discussion explains why differentiation universality deserves
caution. It is not used as a theorem closing this program. We have not
proved that Davenport–Heilbronn or another false analogue satisfies
Holland's entire quantitative region with matched hypotheses. The generic
algebra checks are not an RH candidate and require no unrelated control
run. Any proposed RH-sufficient extension must pass its own matched screen.

## Replay and provenance

From repository root:

```sh
maxima --no-init --quit-on-error --very-quiet --batch-string='batchload("audits/jensen-preprint-audit-2026-09-29-v1/check_identities.mac")$'
```

Require `ALL_EXACT_CHECKS_PASSED 26` and no FAIL/error marker. The final
clean run disables personal initialization. Two additional rational
contraction inequalities are checked with explicit failure guards.
`maxima-output-initial.txt` retains a harness error: default Maxima left
an infinite geometric sum unevaluated. Writing its elementary closed form
resolved it. This was not evidence against the paper. The 23-check replay
and later 26-check run with initialization are also retained; the clean
26-check replay is authoritative for reproducibility.

Source PDF and TeX hashes, exact versions and inherited dependencies are in
`sources.json`. Printed pages 7 and 18–21 were visually inspected; this is
not a whole-document visual review. The final build and map checks are in
`validation.json`. No scientific archive or manuscript source was modified.
