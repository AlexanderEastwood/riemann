# v1.35: a quantified obstruction from growing physical radical blocks

## What was proved

For the actual canonical complete Weil operator, put `a=log(lambda)`.
There are explicit source-defined physical subspaces `G_a` with

\[
 \dim G_a=2\lfloor a/(2D)\rfloor+1,
 \qquad \|\mathsf W_\lambda P_{G_a}\|
 \le C a e^{-\lambda/100}.
\]

Here `D=ceil(4*pi*sqrt(M2))` is a single fixed integer, where
`M2=||(1+|x|)^2 phi||_2` and `phi` is the ordinary-unit-normalized
Gaussian co-Poisson radical already present in lemma v115-source-mass.
`C` and the eventual threshold are not numerically certified. The exponent
is deliberately conservative. It is an asymptotic analytic estimate, not
an effective finite-window certificate.

The full proof is in `new_section.tex`. Its essential quantitative steps are:

1. Translates of the same global radical remain polarized radicals by
   source dilation, preserving both source moments.
2. The weighted source norm fixes a lattice spacing with off-diagonal Gram
   row sum at most `1/6`. No growing source-to-physical transfer is assumed.
3. Cut at the physical window using a fixed smooth transition of width
   `1/2`. Centers stay in `[-a/2,a/2]`. The Gram stays above `I/2`.
4. Bound the full exterior remainder, including **all** prime powers beyond
   `lambda^2`, the two poles, and the archimedean multiplier. Ordinary
   column bounds become a growing-block operator bound only after the
   verified Gram normalization.

It follows that removal of any subspace of dimension below `dim G_a`
leaves a unit vector with absolute form value at most `C a e^{-lambda/100}`.
Thus positive polynomial or uniform lower gaps fail after removal of
`o(log lambda)` directions. This is an upper ceiling on a proposed positive
gap, not a lower bound on the form.

Antisymmetric pairs of translated columns give `floor(a/(2D))` independent
odd near-radical vectors. Every one is orthogonal to all even image columns.
Therefore the same ceiling applies to the physical G2.6 complement when
its deep and plunge images are even, however large their total rank.
If odd images are also included, the assertion requires that their number
of independent constraints be smaller than that odd block dimension.

Compact resolvent then implies at least `dim G_a` eigenvalues, including
the stated odd count, in `[-2 epsilon_a,2 epsilon_a]`. Their signs are not
determined. **No G2 sign gap was closed.**

## Full parity correction

The continuum cancellation is valid on all complex physical tests:

\[
 2|c\rangle\langle c|-2|s\rangle\langle s|-K_a^+=K_a^-.
\]

Consequently the original arithmetic `beta_a` represents the whole form,
not just its even restriction. The even and odd signed concentration
inequalities remain independent blocks. Only the even block loses the
actual even source. The resulting complete lower error is

\[
 \max\{\eta_a^{odd},\eta_a^{even}+2\epsilon_a/\sqrt3\}.
\]

The odd block is not proved positive. A pole-only countermodel already
shows why parity transfer cannot be automatic: its even form is
nonnegative with many exact null sources, but its odd eigenvalue is
`-(sinh(a)-a)`. This scoped countermodel is not the arithmetic Weil form.

## Novelty and dependency audit

**Register ID:** G2.6-RAD-02, a quantitative growing-block obstruction.
**Classification:** continuation and strengthened no-go, not a new live
positivity mechanism; worldwide novelty unresolved and not claimed.

The nearest project antecedent is the v1.14 research-log entry under
“Adversarial work, rejected shortcuts, and research findings.” It uses
even derivatives of exactly the same Gaussian radical and smooth cuts to
exclude a fixed gap after any fixed-rank removal. That entry explicitly
does not establish a growing-rank rate.

The additional ingredient here is a **uniform physical Riesz Gram bound
for a growing lattice of translates**, together with a complete operator
residual uniform over that lattice. It gives rank proportional to
`log(lambda)`, an explicit exponential scale, and an odd-block statement
that survives arbitrarily many even image columns. It is not a renamed
Schur complement, coordinate change, cutoff tuning, or tighter scalar
prime-norm estimate. The prime absolute bound is used on an exponentially
small exterior radical remainder, not on arbitrary vectors to infer sign.

It does not duplicate the structured inverse, finite-rank metric,
dyadic pair-norm, shared-channel/common-Gram, Picone, negative-only Schatten,
or primitive transport sign proposals. None of those mechanisms supplies
the sign here. CAP-01b remains the live conditional sign target.

**Primary literature:** Connes--Consani, *Spectral triples and zeta-cycles*,
Section 3, supplies the classical radical and explains near-radical
prolate sources:
[published article](https://ems.press/journals/lem/articles/11033001),
[original preprint](https://arxiv.org/abs/2106.01715).
Connes--Consani--Moscovici's
[Zeta Spectral Triples](https://arxiv.org/abs/2511.22755)
is the operator framework already used by the manuscript.
Zhu's [compact-window study, v2](https://arxiv.org/abs/2608.24827v2)
separately treats the two pole signs and fixed-window parity certificates.
The present extension reuses these classical structures; no priority claim
is made for radical localization or small Weil eigenvalues.

## Domain, projection and normalization

Everything acts in ordinary `L^2(-a,a)` after zero extension, with the
manuscript's first-slot-linear pairing. The cutoff columns are in
`C_c^infinity(-a,a)`, so operator-domain membership is direct. The
orthogonal projector is `G(G*G)^(-1)G*`. No Fourier cutoff is imposed.
The original finite sampler and its explicit graph defect are unchanged.
No new endpoint comparison is asserted; the new columns vanish near
the actual endpoints. The old repaired source and its boundary normalization
are not replaced by these columns.

## Remaining lemma

The gap-free estimate remains conditional on the signed arithmetic bound

\[
 q_a[f]\ge-\eta_a\|f\|^2,
 \quad f\perp G_a,\quad \eta_a\to0.
\]

Alternatively keep the actual rank-one source and establish both parity
blocks of CAP-01b with errors tending to zero. Small residuals do not prove
either inequality. The new growing projection may be useful but is not
registered as a new coercivity mechanism without an independent sign
estimate for its remaining complement.

## Checks and limitations

An independent adversarial agent reviewed the analytic proof, its source
dilation, all-prime tail estimate, Gram factors, explicit spacing, and
spectral-count deduction. See `adversarial_review.md`.
`check_growing_radical.py` checks Gaussian moments, Poisson symmetry and
complex mixed-parity pole cancellation. Its values are ordinary floating
point diagnostics, not interval certificates. Its approximate spacing
`D=15` is not used as an exact constant by the proof.

The previous primitive-transport diagnostic remains only a finite-window
failure to demonstrate decay; it is not a proved arithmetic cofinal no-go.
The rigorous new obstruction is the growing-block estimate above.

No lambda=8 computation was attempted. G2 and RH remain open.
