# Review 09 — high-height asymptotics and a compact remainder

**Disposition: NO CANDIDATE ADMITTED; a valid conditional proof architecture, without its essential arithmetic estimate.**

Reviewed baseline: `18d324703969b5bcc9aa94043cfd90a6e8211f34` (PR76). Read AGENTS/proposal gates, current README/NEXT_STEPS and ZERO-GEOMETRY map scope, missing-evidence ledger, NS100/101 arguments, PR73's independently checked prefix obstruction, PR74's smooth-completion/error and matched-control reviews, and PR76's moment/admission reviews. The coordinator owns the refreshed full-register review; this is a bounded method audit, not historical proof replication. Both missing-original groups remain OPEN.

**Wall check: Same open gap.** Closest: NS100/101, PR73/74/76. What changes: partitioning the real axis into a compact interval and an eventual regime changes no arithmetic input. The original complete theta coefficients are retained, but no new estimate uses them to establish the eventual signed comparison. PR73 is a **known wall only for fixed reflected prefixes**, not growing smooth approximations.

## Exact obligation and error budget

Write `L[F]=F'^2-F F''`. With the complete original objects,

```text
p=r²+1/4, X=pY/4=xi(1/2+ir)/2,
J=p²L[Y]+2(r²-1/4)Y²=16L[X].
```

An eventual theorem `L[X](r)>=0` for **every** `|r|>=R`, with explicit finite R, plus a rigorous proof on `[-R,R]`, would prove the first-Laguerre target. This is a sound dependency, not RH, G2, or an established cofinal Weil bound. An asymptotic holding outside unspecified exceptional neighborhoods or for almost all heights does not meet it.

For a specified real approximation P with fixed-object derivatives and complete bounds `|X^(j)-P^(j)|<=epsilon_j`, `j=0,1,2`, the exact quadratic expansion gives

```text
B=2|P'|epsilon_1+epsilon_1²+|P|epsilon_2
  +|P''|epsilon_0+epsilon_0 epsilon_2,
L[P]>=B  ==>  L[X]>=0.
```

The missing input is a uniform lower comparison of this kind, or a sharper **signed correlated remainder** estimate. It is not another upper error bound. PR74 already gives a smooth reciprocal completion with all three errors and, for `M(r)>=ceil(|r|)+M_0`, a complete quadratic error decaying faster than `exp(-pi|r|/2)`. It supplies no lower margin. All derivatives remain derivatives with M fixed, evaluated afterward at M(r); differentiating a changing integer cutoff is invalid. Smooth cutoffs instead require every cutoff derivative in the error analysis.

## Exceptional points are part of the theorem

At a simple real zero gamma, `L[X](gamma)=X'(gamma)²>0`; no uniform lower derivative bound follows merely from simplicity. At a zero of arbitrary multiplicity m, write exactly `X=(r-gamma)^m g`, with `g(gamma)!=0`. Then

```text
L[X]=(r-gamma)^(2m-2)*[m g²+(r-gamma)² L[g]].
```

This gives local positivity near each real zero without assuming simplicity, but requires quantitative control of g and its neighborhood for a uniform transfer. For `m>1` the margin is exactly zero at gamma. Thus a strictly positive eventual bound such as `c r^(-k) exp(-pi r/2)` would also prove eventual simplicity; it cannot be assumed as harmless normalization. Nonnegative target proofs need not have such a strict margin.

Near coalescence, the local polynomial `P(x)=x²-d²` has `L[P]=2(x²+d²)`, whose minimum tends to zero with d. Changing to `x²+d²` changes the function by only `2d²` but makes L negative at zero. This is a local stability warning, not an original-theta counterexample. At stationary points with `X!=0`, the obligation is `-XX''>=0`; absolute derivative estimates do not establish it. Degenerate stationary points can again have zero margin. A uniform method must cover all these cases through local factors or correlated estimates, without dividing by X or Y.

## What the asymptotic mechanisms actually provide

**Riemann–Siegel/saddle point.** The exact Hardy normalization is `X=-A Z`, where `A=p pi^(-1/4)|Gamma(1/4+ir/2)|/4>0`. Hence

```text
L[X]=A²*(L[Z]-(log A)'' Z²).
```

The elementary gamma factor can be estimated; the signed quadratic expression in the full oscillatory arithmetic sum remains. Approximating that sum and two derivatives accurately does not bound its lower sign or its cross terms. A dominant single-cosine saddle model would need a uniform differentiated remainder relative to its Laguerre margin, including every cancellation height; none is supplied here.

Bounded arXiv check: [Arias de Reyna, 2406.04714v1, Theorem 5](https://arxiv.org/html/2406.04714v1) gives the auxiliary-function expansion for fixed integer K>=1 in `-pi+theta<=arg s<=pi-theta`, `|s|>=2pi`. Positive critical-line heights lie in an allowed sector, but the theorem estimates a remainder, not this quadratic sign. [2201.00342](https://arxiv.org/pdf/2201.00342) concerns prescribed-error evaluation; its polynomial-derivative routines are not an eventual first-Laguerre theorem. No differentiated asymptotic is inferred by differentiating an uncontrolled O-term.

[Csordas, 1309.0055v2, Proposition 2.2](https://arxiv.org/pdf/1309.0055) assumes `f in S(1)` (its canonical-product strip class), `f(0)!=0`, `B-A>2`, and no nonreal zero with real part in `[A,B]`; it concludes `L[f]>=0` on `[A+1,B-1]`. X belongs to the corresponding rescaled strip class. Applied eventually, that exclusion would require eventual critical-line zero information, not an available unconditional asymptotic input. Open Problem 4.7 names the first inequality; Remark 4.8 identifies the simplicity consequence of strict positivity. This checks those statements' scope, not every subsequent literature development.

## Controls, decision and budget

NS100's negative original slice forbids replacing the integrated comparison by slice positivity. NS101/PR74/76 retain reciprocal symmetry, smoothness, positive primitive, unit primitive tail and rapid transform decay, yet fail J at the stated `pi/beta` witness. This defeats the corresponding **all-height structural shortcut**. That low-height witness is not proof of arbitrarily high failures for one fixed mixture; no such stronger control is claimed. The mixture changes the original lattice/IVP, so it does not refute a future arithmetic-specific eventual estimate. Davenport–Heilbronn likewise lacks the original coefficients/completion.

**Stop:** no independent arithmetic estimating mechanism was found in this bounded check. Allocate at most **one hour** to auditing a subsequently specified uniform lower inequality and its zero-neighborhood transfer; no scan or compact certification follows now. Success would admit the eventual-plus-compact first-Laguerre architecture. Failure would reject that estimate under its stated hypotheses, not all asymptotic methods. No research row, thaw, new theorem node, computation or manuscript version.

**Final wall check: Same open gap — ZERO-GEOMETRY, NS100/101, PR73/74/76.** RH, G2 and the cofinal signed-arithmetic lower bound remain open.
