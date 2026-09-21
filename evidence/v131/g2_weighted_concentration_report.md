# G2.6-CAP-01b: source-compressed weighted concentration

## Classification

This is a substantive project-new development of the v1.29–v1.30 capacity/continuum-symbol candidate, not a separately renamed mechanism. Time-frequency concentration operators and Logvinenko–Sereda inequalities are classical; no claim of worldwide novelty is made. The arithmetic specialization below was not present in the project's Schur, structured-inverse, scalar prime-norm, finite-rank repair, source-residual, dyadic tail-metric, or common-Gram proposals.

## Physical space and exact operator

Work on the even physical space

\[
\mathcal H_a^{\rm ev}=L^2_{\rm ev}(-a,a)
\]

with the complete physical form domain used by the manuscript. Zero extension followed by the unitary Fourier transform is denoted by (\mathcal F_a). Let (u_a) be the normalized repaired source and

\[
P_a=I-|u_a\rangle\langle u_a|.
\]

For a symmetric measurable frequency set (E), define

\[
\mathcal C_{a,u}(E)=P_a\mathcal F_a^*1_E\mathcal F_aP_a.
\]

This is a positive contraction on the actual rank-one source complement. It does not identify that complement with (C_a^{low}); instead it controls the larger complement required by `prop:v118-gap-free`.

## Proved negative-level bound

For the exact v1.30 symbol (\beta_a), set

\[
D_a=\|(\beta_a)_-\|_\infty,
\qquad E_a(t)=\{\xi:\beta_a(\xi)<-t\}.
\]

At every fixed (a), (\beta_a) is continuous, bounded below and tends to positive infinity. Hence (D_a) is finite and the negative level sets are bounded. Layer cake and Plancherel prove

\[
q_W[f]\ge-
\left(\int_0^{D_a}\|\mathcal C_{a,u}(E_a(t))\|dt\right)\|f\|^2
\quad(f=P_af).
\]

The exact trace refinement is

\[
\operatorname{tr}\mathcal C_{a,u}(E)
=\int_E\left[
\frac{a+\sin(2a\xi)/(2\xi)}{2\pi}
-|\widehat{\widetilde u_a}(\xi)|^2
\right]d\xi.
\]

Here (E) is the full symmetric set. When integrating only its positive half, the integrand contribution must be doubled.

## Sharper live criterion

The negative-only estimate discards all favorable symbol mass. Choose symmetric superlevel sets (G_{a,j}) and positive weights (w_{a,j}) such that

\[
-D_a+\sum_j w_{a,j}1_{G_{a,j}}\le\beta_a.
\]

The sufficient operator inequality is

\[
-D_aP_a+\sum_jw_{a,j}\mathcal C_{a,u}(G_{a,j})
\succeq-\eta_aP_a,
\qquad\eta_a\to0
\]

along a cofinal family. This implies the even `prop:v118-gap-free` conclusion without a positive spectral gap.

For one good set (G_a(\theta)=\{\beta_a\ge\theta D_a\}), a lower concentration bound (\mathcal C(G_a(\theta))\succeq p_aP_a) gives

\[
q_W[f]\ge D_a((1+\theta)p_a-1)\|f\|^2.
\]

Thus ordinary thickness of (\{\beta_a\ge0\}) is not enough. Generic Logvinenko–Sereda constants do not automatically approach the near-unit concentration budget required by this formula.

## Adversarial test

The scalar layer-cake bound was tested at lambda 3, 4 and 5 only. On the truncated frequency range (|\xi|\le5000), it had already accumulated approximately 2.1363, 3.2440 and 4.5622. These are non-rigorous partial diagnostics, not full-frequency enclosures.

Even compactly supported packets proportional to

\[
\cos(\pi x/(2a))\cos(\omega x)
\]

were centred at the deepest located negative wells. Although the symbol values there were approximately -2.37816, -3.41944 and -5.01788, the complete signed packet quotients were +0.951081, +2.757308 and +3.683514. Fourier integration and an independent physical archimedean/prime/pole computation agreed to about (3\times10^{-10}). This does not prove positivity, but it prevents those wells from serving as an immediate counterexample and demonstrates the loss in negative-only estimates.

## Literature and novelty screen

Closest general tools:

- H. J. Landau and H. O. Pollak, *Prolate spheroidal wave functions, Fourier analysis and uncertainty—II*, Bell System Technical Journal 40 (1961), 65–84.
- F. L. Nazarov, *Local estimates for exponential polynomials and their applications to inequalities of the uncertainty principle type*, Algebra i Analiz 5:4 (1993), 3–66; St. Petersburg Math. J. 5:4 (1994), 663–717.
- O. Kovrijkine, *Some results related to the Logvinenko–Sereda theorem*, arXiv:math/0012186v1 (2000).

These sources supply concentration and uncertainty machinery, not the signed arithmetic operator inequality or its cofinal constants. Project novelty is limited to the exact arithmetic symbol, actual source compression, and weighted superlevel hierarchy. Worldwide novelty is unresolved and not claimed.

## Exact remaining lemma

Construct an explicit finite or convergent superlevel hierarchy for the exact (\beta_a) and prove the corresponding source-compressed weighted concentration operator is bounded below by (-\eta_aP_a), with (\eta_a\to0) along a cofinal family. Every constant must retain its dependence on (a), the source, and the arithmetic levels. The odd sector remains separate.

No G2 gap is closed and RH is not proved.
