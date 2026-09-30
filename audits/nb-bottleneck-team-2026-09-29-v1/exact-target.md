# Exact target reconstruction: full optimized q=2 Nyman–Beurling gain

Internal specialist working note, 2026-09-29. Reviewed base:
`a992456a6305b0b01b0d6efe2b022c73d1c0cd3b` (`origin/main`, supplied by the
coordinator after refresh). I read the current `AGENTS.md`, all 104 registered
conclusion notes and their wall scopes, and the relevant source arguments
below. This is a dependency/normalization reconstruction, not an independent
revalidation of every historical proof or numerical certificate. No new
computation, candidate, research row, or claimed partial arithmetic theorem.

**Wall check: Same open gap — NB-GAIN.** Closest results: NS53/61/86/87;
required controls: NS74 and NS83. No arithmetic hypothesis has changed.
The task is to expose the actual missing input precisely enough for specialist
assessment. It does not thaw the research family.

## 1. Fix the Hilbert space, smoothing, target, and coefficients

Use the real space \(L^2((0,\infty),dx)\),
\(\chi=\mathbf1_{(0,1)}\), \(\rho_n(x)=\{1/(nx)\}\), and
\[
 (Jf)(x)=\int_0^1 f(x/u)\,du/u,\qquad
 \tau=J\chi=(-\log x)\mathbf1_{(0,1)},\qquad \sigma_n=J\rho_n.
\]
The smoothing order is **fixed at q=2**, independently of N. With
\(W_N=\operatorname{span}(\sigma_1,\ldots,\sigma_N)\), define
\[
 R_N=(I-\Pi_N)\tau,\qquad E_N=\|R_N\|_2^2>0,
 \qquad c_N=G_N^{-1}b_N,
\]
where \(G_{mn}=\langle\sigma_m,\sigma_n\rangle\) and
\(b_n=\langle\tau,\sigma_n\rangle\). Thus E is a squared norm, and
\(\|\tau\|_2^2=2\). All subsequent E's denote this q=2 quantity, not
NS53's unsmoothed error.

The normalization is fixed by
\[
 \widehat\sigma_n(s)=-\frac{\zeta(s)n^{-s}}{s^2},\qquad
 \widehat\tau(s)=\frac1{s^2}\qquad (0<\Re s<1).
\]
NS61 retains the entire exterior tail \(\sigma_n(x)=1/(nx)\) for x>1.
It proves, using the established strong integer Nyman–Beurling criterion
and a bounded off-line-zero evaluation functional in this tail space,
\[
 E_N\longrightarrow0\quad\Longleftrightarrow\quad\mathrm{RH}.
\]
Boundedness of J alone gives only the forward approximation implication;
its inverse is not asserted bounded. No Weil parity or source-complement
condition belongs to this separate NB criterion. Conversely, no exterior
normalization \(\sum c_n/n=0\) is imposed on the actual optimum.

Source: `evidence/v159/ns61/proof.tex`, propositions
`prop:ns61-rh-equivalence`, `prop:ns61-loads`; unsmoothed antecedent:
`evidence/ns53_nb_blocks/proof.tex`. The repository attributes the strong
criterion to Báez-Duarte, Theorem 1.1, arXiv:math/0202141, and the weighted
q=2 problem to Ehm (2024). Those literature proofs were not re-audited here.

## 2. The exact gain, and the weakest aggregate obligation

For integers M>N, partition the complete Gram into old block G, cross block
C, and new block D. Write
\[
 h=b_{\rm new}-C^TG^{-1}b_{\rm old},\qquad
 H=D-C^TG^{-1}C>0.
\]
Then
\[
 \Delta_{N,M}=E_N-E_M=h^TH^{-1}h
 =\sup_{w\ne0}\frac{|w^Th|^2}{w^THw}.
\]
H is the Gram of the projected new atoms
\((I-\Pi_N)\sigma_n\). Replacing it by the raw D in the equality,
or replacing h by uncorrected target loads, changes the statement.

For N_j=2^j, set
\(\gamma_j=(E_{N_j}-E_{N_{j+1}})/E_{N_j}\in[0,1)\). The exact product
\[
 E_{N_J}=E_{N_{j_0}}\prod_{j=j_0}^{J-1}(1-\gamma_j)
\]
shows that \(\sum_j\gamma_j=\infty\) is **equivalent** to convergence,
and hence RH. This is algebraic target specification, not an independently
proved arithmetic estimate. It does not require a pointwise a/j bound,
a prescribed rate, or a positive gain on every individual doubling.

A useful sufficient estimate could instead supply explicit nonnegative
lower bounds \(\beta_j\le\gamma_j\) whose cumulative sum diverges, or a
direct lower bound
\(\sum_{j=j_0}^{J-1}\gamma_j\ge\omega(J)\to\infty\).
Merely writing either condition does not make it a partial lemma.

Source: NS53 exact block identities and any-rate proposition; NS61's
smoothed version; NS83's rate discussion.

## 3. The first genuinely unestimated signed quantity

NS61 gives the exact target loads
\[
 b_n=\frac{P(\log n)}n,\qquad
 P(v)=\tfrac12v^2+(2-\gamma)v+3-2\gamma-\gamma_1,
\]
with convention \(\zeta(1+z)=z^{-1}+\gamma-\gamma_1z+O(z^2)\).
For adjacent differences
\(\epsilon_n=\sigma_n-\frac{n-1}{n}\sigma_{n-1}\), the actual residual
correlation is
\[
 g_n=\frac{P(\log n)-P(\log(n-1))}{n}
       -\sum_{m\le N}(c_N)_m\langle\sigma_m,\epsilon_n\rangle,
 \qquad N<n\le2N.
\]
**The second term's signed cancellation against the first is unestimated
at the required scale.** The unprojected load has a simple asymptotic;
that asymptotic does not lower-bound g. The coefficients c_N already depend
on the full original arithmetic Gram and target.

NS61's complete raw trace budget is
\[
 \operatorname{tr}\mathcal D_N\le\frac{3\kappa}{8N^2},\qquad
 \kappa=\log(2\pi)-\gamma,
\]
so it suffices to prove
\[
 N^2\|g\|_2^2\ge\frac{3\kappa}{8}\alpha_jE_N,
 \quad N=2^j,\quad 0\le\alpha_j<1,\quad\sum_j\alpha_j=\infty.
\]
This trace-based sufficient input is **not asserted necessary or equivalent
to RH**: it can lose small Gram eigenvalues that amplify the exact gain.
The full h–H quotient is the less restrictive target.

Source: `evidence/v159/ns61/proof.tex`, equations
`eq:ns61-gain`, `eq:ns61-open-correlation`, `eq:ns61-retained-cross`.

## 4. What NS86/87's complete tail control actually buys

In reciprocal coordinates t=1/x, use
\(\mathcal H=L^2((0,\infty),dt/t^2)\),
\(a_n(t)=A(t/n)\), \(A(z)=\int_0^z\{u\}\,du/u\),
\(\tau(t)=\mathbf1_{t\ge1}\log t\), and
\(r_N(t)=\tau(t)-\sum_{n\le N}(c_N)_na_n(t)\).
In particular, below t=1 the residual is
\(-t\sum(c_N)_n/n\); this exterior contribution remains in every integral.

For T≥1, define the truncated potential
\[
 P_T(t)=\int_t^T\log(u/t)r_N(u)\,du/u^2\quad(0<t\le T).
\]
The finite arithmetic observation is exactly
\[
 q_n(T)=\langle\mathbf1_{t\le T}r_N,a_n\rangle
       =\frac1n\int_0^T P_T(t)dt-\sum_{1\le k\le T/n}P_T(kn).
\]
For the block N<n≤M the projected observation vector is
\[
 \widehat h_T=q_{\rm new}(T)-C^TG^{-1}q_{\rm old}(T).
\]
The old vector cannot be dropped: the **full** residual is old-orthogonal,
but its truncation generally is not. Thus the finite observation energy
\(A_T=\widehat h_T^TH^{-1}\widehat h_T\) still contains the complete
arithmetic Gram and its inverse. “Finite observations” does not mean a
cheap matrix calculation or independently known optimized coefficients.

NS87 gives a complete residual-tail bound F_N(T) and
\[
 L_N(T):=(\sqrt{A_T}-\sqrt{F_N(T)})_+^2\le\Delta_{N,M},
 \qquad
 0\le\frac{\Delta_{N,M}-L_N(T)}{E_N}
       \le4\sqrt{F_N(T)/E_N}.
\]
For every fixed ε>0 and T=ceil(N^(5+ε)),
\[
 F_N(T)/E_N=O_\varepsilon(N^{-\varepsilon}\log^4N).
\]
The proof uses NS81's polynomial coefficient bound and NS83's unconditional
critical-zero lower bound; it supplies no effective asymptotic onset.
T=N^6 suffices. The loss is o(1/log N), so
\(\liminf_{j\to\infty}jA_{(2^j)^6}/E_{2^j}>0\) would suffice for RH.
No necessity is asserted for that positive-liminf condition.

For the requested weakest aggregate formulation, set
\(A_j=A_{(2^j)^6}\) and \(L_j=L_{2^j}((2^j)^6)\), always with the
N=2^j to M=2^(j+1) block. NS87's explicit bounds are
\[
 |A_j/E_{2^j}-\gamma_j|\le2\epsilon_j+\epsilon_j^2,
 \qquad0\le\gamma_j-L_j/E_{2^j}\le4\epsilon_j,
 \qquad\epsilon_j=\sqrt{F_{2^j}((2^j)^6)/E_{2^j}}.
\]
Its relative-tail estimate gives
\[
 \epsilon_j=O(2^{-j/2}j^2),
\]
whose sum is finite (as is the sum of its square). Consequently either
\(\sum_jA_j/E_{2^j}=\infty\) or
\(\sum_jL_j/E_{2^j}=\infty\) is equivalent to the exact aggregate target
above. A_j itself need not be a lower bound on individual gain; its use
here relies on the summable two-sided error. This is an immediate
bookkeeping consequence of NS87, **not a new
arithmetic lower bound or partial RH advance**. It explicitly permits
irregular gains and arbitrarily slow divergence. The tail is no longer a
hidden obstacle at this cutoff; the signed interior observation energy is.

Sources: `evidence/ns86_optimized_arithmetic/argument.tex` (86.1–86.5),
`evidence/ns87_joint_tail/argument.tex`, and
`evidence/v164/ns81/proof.tex`. NS86's full potential satisfies
\(P_N(1)=E_N\) only for the actual optimal residual; arbitrary residuals
must not inherit that equality.

## 5. Controls, rates, and the narrower Möbius branch

- **NS74, target-aware control.** A unitary inner-factor alteration of all
  atoms preserves every complete Gram entry and permits arbitrarily close
  finite loads/efficiencies, yet leaves a strictly positive error floor for
  the fixed target. Therefore Gram geometry, projection identities, and
  finite gain fractions alone cannot supply the missing implication.
  The original floor/divisor formula changes under this alteration. A
  proposed arithmetic estimate must identify the step that uses that
  original structure; writing an original-looking matrix is insufficient.
- **NS83, rate constraint.** For each fixed smoothing order,
  \(\liminf(\log N)E_N^{(q)}\ge C_q>0\). Thus eventual fixed-fraction
  contraction per doubling is excluded; so is eventual
  \(\gamma_j\ge a/j\) with a>1. It does not exclude 0<a≤1, irregular
  nonsummable gain, or a slower proved convergence rate. There is no
  pointwise upper bound on each individual gain asserted here.
- **NS90–98, prescribed direction only.** The logarithmic Möbius taper
  yields a particular numerator ℓ_N and projected cost K_N, with gain
  ℓ_N²/K_N. Its two prime main terms cancel exactly (NS90). NS91–98 leave
  the signed margin and cost open, while excluding specified absolute-value
  estimates. Those missing inputs and exclusions are not identical to the
  full vector target above. Returning to the full optimizer escapes the
  restriction to that direction, but supplies no new arithmetic leverage.

Sources: `evidence/v161/ns74/proof.tex`, `evidence/v166/proof.tex`,
`evidence/ns90_mobius_gain/argument.tex`,
`evidence/ns98_projected_cost/argument.tex`; current continuation board.

## 6. Admission assessment and a focused specialist question

| Gate | Assessment | Evidence / limitation |
|---|---|---|
| Dependency edge to RH | **Present** | Exact gain, fixed q=2 criterion, and complete tail transfer retain their quantifiers and target. |
| New arithmetic leverage | **Absent** | No independent estimate for the corrected observations or their aggregate has been identified here. Original arithmetic data are present, but the inequality using them is missing. |
| Decision value of this audit | **Present** | The brief specifies what a specialist must improve and prevents substituting fixed-direction cost, finite efficiency, or another tail improvement for the actual input. |
| Admission of another candidate computation | **Absent** | No mechanism or weaker partial lemma has been supplied. A screen would have no established new dependency edge to assess. |

**No weaker partial arithmetic lemma is proposed in this note.** Better
conditioning or a smaller sufficient cutoff could be useful numerically,
but the existing localization already makes their loss negligible at the
target scale; such an improvement is not a substitute for signed gain.
The aggregate divergence above is RH-equivalent target specification and
must not be offered as a supposedly easier theorem.

Suggested specialist question (not sent):

> For the original fixed q=2 integer-dilation system, can a known
> arithmetic method give a nontrivial estimate for
> q_new(T) − CᵀG⁻¹q_old(T), evaluated on the actual residual
> c_N=G_N⁻¹b_N, that survives its complete inverse-Gram cost and can
> contribute to a divergent aggregate of relative block gains? The tail
> at T=N⁶ is already summably negligible on dyadic scales. Which exact
> signed correlation can current techniques estimate, with what uniform
> range and loss, and which step uses the original divisor structure in
> a way the NS74 altered family cannot share? If no such intermediate
> estimate is presently supported, that is the useful answer.

This question does not ask a generic supporting lemma to distinguish all
false analogues on its own. Its complete proposed transfer would need a
matched target-aware control before admission. RH, G2, and the actual
cofinal signed-arithmetic lower bound remain open.

## Coordinator HTML scope review — 2026-09-29

Reviewed `audits/nb-arithmetic-bottleneck-2026-09-29-v1.html` against this
reconstruction and the NS61/74/83/86/87 arguments. **No MAJOR findings.**
The fixed q=2 normalization, exact block gain, old-space correction,
dyadically summable observation error, and a>1 rate exclusion are correctly
stated. This review does not independently verify the literature table,
which belongs to the source-assessment agent, or historical certificates.

Two MINOR clarifications were sent to the coordinator:

1. The localized aggregate divergence is in fact equivalent to convergence
   under the summable two-sided error, not only sufficient. Stating that
   explicitly prevents it being mistaken for a weaker-than-RH partial lemma.
2. The displayed asymptotic tail rate inherits NS83's lack of an effective
   onset. State that limitation beside the rate.

An optional notation clarification is to write “eventual a/j contraction”
as \(\Delta_{2^j}/E_{2^j}\ge a/j\). None of these points invalidates the
draft's mathematical claims. No new research or numerical replay was run.

Resolution, 2026-09-29: the coordinator's HTML now explicitly states the
aggregate equivalence, the lack of an effective onset, and the indexed
relative-gain inequality. Both MINOR clarifications are resolved.
Every repository path cited in this note was checked to exist. The NS83
source reference is normalized to `evidence/v166/proof.tex`; its previously
cited copy at `evidence/v166/ns83/proof.tex` also exists in the reviewed
worktree and is byte-for-byte identical. No mathematical source was changed.
