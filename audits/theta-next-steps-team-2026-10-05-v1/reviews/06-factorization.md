# Review 06 — complete-kernel positive factorization

Reviewed remote mathematical baseline: `18d324703969b5bcc9aa94043cfd90a6e8211f34` (PR76), using the coordinator's refreshed isolated worktree. Read repository instructions, current checkpoints and ZERO-GEOMETRY scope/freeze, NS100/101, PR76's derivation and PR74's nonlinear certificate review. This is a paper applicability assessment, not a historical proof or certificate replay. Both original-evidence recovery groups remain OPEN.

**Wall check: Same open gap.** Closest: NS100/101, PR74/76. No new arithmetic estimate is supplied. The concrete question is whether complete-kernel convolution, half-line convexity, or positive Gaussian mixtures yield an independently estimable sufficient condition. The two specified positive-mixture constructions fail necessary hypotheses; general positive factorization remains open.

## Exact target and transfer

Keep the original complete square-lattice coefficients:

```text
phi(u)=sum_(n>=1) (2*pi^2*n^4*exp(9u/2)-3*pi*n^2*exp(5u/2))
                  *exp(-pi*n^2*exp(2u)),  u>=0,
phi(-u)=phi(u),
X(r)=integral_R phi(u)*exp(i*r*u)du,
C(t)=integral_R s^2*phi(s+t)*phi(s-t)ds.
```

The extension is the complete smooth Jacobi kernel, never a reflected finite prefix. All polynomial moments and derivatives needed below are integrable. The requirement is positive definiteness of `C` on the whole real line: every finite matrix `C(x_i-x_j)`, arbitrary real nodes and arbitrary complex coefficients, must be positive semidefinite. There are no parity/source restrictions. Its exact consequence is

```text
L1[X](r)=X'(r)^2-X(r)*X''(r)=4*integral_R C(t)*cos(2*r*t)dt>=0
for EVERY real r,
J(r)=16*L1[X](r)>=0.
```

The identity includes zeros and `r=0`; no division by a transform occurs. First-Laguerre positivity alone is not RH. PR76's polynomial correction is already included by working directly with `C`.

An independently derived equality `C(t)=sum_j (g_j*tilde(g_j))(2t)`, with `g_j` in `L2(R)`, `tilde(g)(u)=conj(g(-u))`, and `sum_j ||g_j||_2^2<infinity`, would suffice: arbitrary finite quadratic forms become sums of squared `L2` norms. Fourier positivity follows almost everywhere, then everywhere from the continuous complete transform. But constructing `g_j` from the square root of the unknown Fourier transform assumes the target. No such original-coefficient factor is obtained here.

## The natural exact convolution still has a minus sign

Put `f_j(u)=u^j*phi(u)` for `j=0,1,2`, and `h_+=f_2+f_0`, `h_-=f_2-f_0`. Writing `y=s+t` and expanding `(y-t)^2` gives

```text
C(t) = (1/2)*(f_2*f_0-f_1*f_1)(2t)
     = (1/8)*(h_+*tilde(h_+)-h_-*tilde(h_-)
               +4*f_1*tilde(f_1))(2t).                 (1)
```

The oddness of `f_1` is essential: `tilde(f_1)=-f_1`. Each autocorrelation in (1) is positive definite, but its negative coefficient cannot be discarded. Its Fourier domination is exactly

```text
|X+X''|^2 <= |X-X''|^2+4*|X'|^2,  every real r,
```

which expands to `L1[X]>=0`. Thus (1) gives no independently estimating lemma. It uses complete integrable functions, so no forbidden full-line termwise theta unfolding occurs. NS101 already exposes the same signed-comparison issue for the tilted autocorrelation derivative; the polynomial feature decomposition does not escape it.

## Pólya/Fejér half-line convexity is unavailable

The precise Pólya criterion is continuity, evenness, normalization at zero, convexity on `t>0`, and decay to zero; it implies positive definiteness. The cited source itself warns that its smooth admissible kernels fail the convexity hypothesis. This is not an all-purpose curvature theorem. [Csordas, arXiv:1309.0055v2, Theorem 3.4 and following paragraph](https://arxiv.org/html/1309.0055v2).

For our actual `C`, smooth evenness gives `C'(0)=0`, positivity gives `C(0)>0`, and the complete tails give `C(t)->0`. If `C` were convex on the positive half-line, its derivative would be nondecreasing from zero; hence `C(t)>=C(0)` there, a contradiction. This also excludes a nonzero positive triangular-mixture representation

```text
C(t)=integral_(0,infinity) (1-|t|/a)_+ dnu(a),  nu>=0,
```

whose members are convex on the positive half-line. The usual Fejér/Pólya cosine-positivity criterion based on decreasing convex input therefore cannot apply directly. Eventual convexity alone does not supply its missing near-origin hypothesis. A different Fejér-type theorem would need separately stated hypotheses and transfer; none is asserted here.

## Positive Gaussian scale mixtures also fail

The complete original theta tail yields constants `K,c>0` with
`phi(u)<=K*exp(-c*exp(2*|u|))` on all of `R`. Since

```text
exp(2*|s+t|)+exp(2*|s-t|)
 >= (exp(2*|s|)+exp(2*|t|))/2,
```

integration gives `0<C(t)<=B*exp(-(c/2)*exp(2*|t|))`, with finite positive
`B=K^2*integral_R s^2*exp(-(c/2)*exp(2*|s|))ds`.

Suppose instead `C(t)=integral_[0,infinity) exp(-a*t^2)dmu(a)`, `mu>=0`. Its finite nonzero mass equals `C(0)`. Some finite `A` has `m=mu([0,A])>0`, implying `C(t)>=m*exp(-A*t^2)`, contradicting the bound above. This excludes exactly positive Gaussian scale mixtures, not general autocorrelations or positive-definite kernels with faster-than-Gaussian decay.

## Controls, decision and bounded budget

NS100 excludes per-slice positivity; none is assumed. NS101's reciprocal control shares smoothness and double-exponential decay, so the two rejections above also apply to it: they do not distinguish original arithmetic. PR74 additionally supplies an analytic first-Laguerre failure range for that family, with its original coefficients/Jacobi initial data changed. Those changes leave an original-coefficient factorization unexcluded. PR74's failed local drift certificate is preserved; no modified drift, divided-difference, or transport ansatz is proposed here.

**Decision:** admit no new estimating lemma. Stop the two stated mixture constructions. The remaining missing input is an explicit factor/comparison derived from the original square-lattice coefficients, with complete tails and all coefficient combinations retained. Merely demanding such a factor is the existing gap.

**Budget:** at most 1–4 hours for paper admission of one externally supplied explicit factor formula; zero scan/certification budget without that formula. Success would establish the complete first-Laguerre target, with no further transfer estimate, but not RH/G2. Failure would reject only that formula. No automatic adjacent variation, new row, thaw, manuscript version, computation, commit or outreach.

**Final wall check: Same open gap — ZERO-GEOMETRY, NS100/101, PR74/76.** Scoped known walls exclude direct convex-half-line and positive-Gaussian-mixture certificates. The original complete sign and cofinal signed-arithmetic lower bound remain open.
