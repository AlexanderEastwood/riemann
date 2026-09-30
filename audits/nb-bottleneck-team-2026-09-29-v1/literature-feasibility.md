# Bounded literature feasibility assessment

Reviewed base: `a992456a6305b0b01b0d6efe2b022c73d1c0cd3b`.
Lane: original-target `NB-GAIN`; assessment by the literature sub-agent.

**Outcome: no candidate arithmetic lemma admitted.** The three checked
primary sources do not furnish an unconditional lower estimate for the
actual optimized residual. This is a bounded theorem-applicability review,
not an exhaustive literature search, independent proof audit, or assertion
that an adaptation is impossible. No computations or certificates were run.

**Wall check: Same open gap.** Closest results: NS53/61/87; preserve NS74's
target control and NS83's rate restriction. The arithmetic hypothesis is
unchanged. What changes is the source-level assessment of proposed imports.
No research row, thaw, new theorem, or RH advance follows.

## Target retained

In the fixed q=2 space from NS87, the target is
`tau(t)=1_(t>=1) log(t)`, the atoms are
`a_n(t)=A(t/n)`, `A(z)=integral_0^z {u} du/u`, and
`r_N=(I-Pi_N)tau`. Write `E_N=||r_N||^2`,
`phi_n=(I-Pi_N)a_n`, `H_N=(<phi_i,phi_j>)`, and
`h_N=(<r_N,phi_n>)` for `N<n<=2N`. Then

    E_N-E_(2N) = h_N^T H_N^(-1) h_N.

NS87 already localizes h with the complete old-space correction and
controls its omitted tail at physical cutoff `T=N^6` to relative error
`o(1/log N)`. This is a physical reciprocal-coordinate cutoff; it is not
the height T in a moving-height zeta moment. The original residual, full
Gram inverse, signs, and cofinal scales remain indispensable. A theorem
about fixed Möbius coefficients is not automatically about these
size-dependent optimized coefficients.

The prior Möbius cancellation and cotangent/Estermann applicability audits
were read. Their fixed-shift, changing-weight, comparable-index and rate
mismatches were not proposed again as new tests.

## 1. The full-line match is explicitly conditional

[Bettin–Conrey–Farmer, arXiv:1211.5191v1](https://arxiv.org/html/1211.5191v1),
Theorem 1, gives the full-line q=1 error asymptotic for

    V_N(s) = sum_(n<=N) mu(n)(1-log(n)/log(N)) n^(-s).

It assumes RH and
`sum_(|Im rho|<=T) |zeta'(rho)|^(-2) << T^(3/2-delta)` for some positive
delta; the latter also requires simple zeros. The conclusion is
`(2pi)^(-1) integral_R |1-zeta V_N|^2 dt/(1/4+t^2)
 ~ (2+gamma-log(4pi))/log N`.

Read scope: introduction, Theorem 1, unconditional Lemma 2's residue
representation, conditional Lemma 3, and the opening estimates in the
proof of Theorem 1. Lemma 2 does not provide unconditional control of the
zero-residue contribution. Lemma 3 is where RH and the derivative hypothesis
enter explicitly. No replacement for them was found here. The prescribed
V_N is an admissible competitor, not the actual finite optimum.

The q=1/q=2 mismatch alone is not a rejection: the existing bounded Mellin
integration operator has norm 2, so a complete q=1 error bound transfers
one-sidedly to a q=2 competitor error bound with factor 4. This does not
remove the source hypotheses or compare successive relative gains of the
two distinct optimizers.

## 2. Short-mollifier success concerns a different target

[Conrey–Farmer–Kwan–Lin–Turnage-Butterbaugh,
arXiv:2508.11108v1](https://arxiv.org/html/2508.11108v1), Theorem 1 and
equations (12)–(18), concern a normalized height moment of
`Q(-L^(-1)d/ds) zeta(s) M(s,P)` on `s=1/2-R/L+it`, with
`L=log(T/2pi)` and mollifier length `T^theta`. Their construction gives
positive critical-line zero proportion for sufficiently small fixed
positive theta; the theorem states a lower proportion exceeding
`2 theta/3`. It is not an all-zero assertion.

Read scope: Sections 1–2, the variational setup in Section 3, and Section 5's
proof of Theorem 1. Its supporting numerical constants were not replayed or
certified here; the result is recorded as the authors' theorem.

This does not estimate `1-zeta A_N` on the full weighted line or the
original q=2 residual numerator. The derivative combination changes the
analytic target; its functional-equation restrictions do not identify the
inverse-Gram coefficients. Varying theta, R, polynomial degree, or height
simultaneously would need uniform estimates absent from the fixed-parameter
statement. No such transfer, including control of the low-height part and
the original-target cross term, is supplied.

## 3. A coarse long-mollifier bound still carries major zero information

[Bettin–Gonek, arXiv:1604.02740v1](https://arxiv.org/html/1604.02740v1),
Theorems 1–2, provide a useful burden benchmark. Define
`I_N(U,V)=integral_U^V |M_N(1/2+it) zeta(1/2+it)|^2 dt` with the stated
logarithmic Möbius mollifier. For every epsilon>0, assume
`I_N(0,T) <<_epsilon T^(1+epsilon)` uniformly for all
`2<=N<=T^theta`. Theorem 1 implies no zeros in
`Re(s)>1/2+1/(2theta)`. For the corresponding `[T,2T]` hypothesis,
Theorem 2 gives `Re(s)>1/2+2/theta`. Arbitrarily large fixed theta implies
RH. The intervals therefore cannot be interchanged casually.

Read scope: both statements and their common Mellin-transform proof in
Section 2, particularly the integration over all mollifier lengths up to
`x=T^theta`. A bound only at one endpoint length is not the stated premise.

Replacing a long-mollifier asymptotic by this rough uniform upper bound is
not an innocuous weaker intermediate goal. This theorem does not rule out
such bounds, and it is not a direct lower-gain result for optimized NB
coefficients. No new candidate is inferred from it.

## Decision, control obligations, and specialist question

None of these imports supplies a separately defensible partial estimate
for the complete signed optimized correlations. There is no basis here
for choosing a new size scan, a new mollifier, or a claimed partial lemma.
Improved high-height tails alone would not address the localized interior
arithmetic lower bound already isolated by NS87.

A specialist-ready question is:

> For the fixed original q=2 target and the actual optimized coefficients
> above, can a known twisted-moment or arithmetic bilinear method estimate
> any explicitly identified signed sub-sum of the localized NS87
> correlations with a uniform error useful after the full H_N inverse?
> If not, what concrete arithmetic regularity of these coefficients would
> be needed beyond the repository's existing polynomial l2 bound, and can
> that regularity be formulated without assuming RH or a zero-derivative
> moment conjecture?

An affirmative answer must name the sub-sum, the coefficient class and its
verified norm bounds, the range of every size/height/shift parameter, and
the error after all summation and inverse-Gram losses. A standalone partial
theorem can be useful without proving RH, but its exact edge to the
registered input must be stated. The candidate must not merely restate
`h_N^T H_N^(-1)h_N` being sufficiently large.

This is an applicability audit; no new candidate sufficient RH implication
was proposed, proved, or certified, so there is no candidate numerical
screen to run. NS74 remains the applicable warning against promoting a
Gram-only estimate to original-target gain. Davenport–Heilbronn and
NS100/101 alterations do not preserve the exact Möbius/atom/target pair
used in these literal imports; this is a hypothesis mismatch, not a
passed control. Any subsequent candidate needs its own matched screen
under the proposal gate before proof-oriented computation.

The coordinator reviewed the full conclusion register before delegation;
this lane reread current AGENTS.md, NB-GAIN/NB-SAMPLES scopes, relevant
frozen-input entries, the two prior transfer audits, and NS87's argument.
It did not revalidate all historical proofs or numerical certificates.
RH, G2, the cofinal gain input, and both missing-original groups remain open.

## Review of coordinator brief

Reviewed `audits/nb-arithmetic-bottleneck-2026-09-29-v1.html`, particularly
the three-source table, its surrounding transfer claims, and review limits.
No additional literature search was performed.

- **MAJOR findings: none.** The draft retains BCF's RH and moment
  assumptions, distinguishes the short-mollifier target from the complete
  NB norm, and treats Bettin–Gonek as a burden benchmark rather than an
  impossibility result. The assessment is explicitly bounded to three
  sources and does not claim a comprehensive ranking or a proof audit.
- **MINOR clarification recommended:** state in the BCF table cell that
  the reciprocal-derivative condition also requires simple zeros.
- **MINOR clarification recommended:** specify sufficiently small fixed
  positive theta in the Short Mollifiers cell. Its theorem is attributed
  to the paper; no independent certification of supporting numerical
  constants was performed by this lane.

The linked assessment above retains the exact long-mollifier length
uniformity, the differing height intervals in Bettin–Gonek, and the valid
one-sided q=1-to-q=2 error transfer. These are not erased by the brief's
shorter table. Final mathematical/source disposition: acceptable, with
the two precision clarifications recommended; no new arithmetic input.

Resolution: reread the revised source-table sentences. The BCF entry now
explicitly retains simple zeros, and the Short Mollifiers entry specifies
sufficiently small fixed theta while attributing the result as the stated
theorem. Both minor findings are resolved. No unresolved major or minor
source finding remains within this bounded review scope.
