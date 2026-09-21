# Section-by-section audit of Fixed-Space Prime Compatibility

Review date: September 20, 2026; updated after reviewing Claude's audit and the additional 32-page manuscript identified by the author as v10. Review baseline: the supplied 89-page r11 manuscript and its timestamped LaTeX source. This is a review report for discussion, not a revised manuscript. The supplied manuscripts have not been edited.

Agreed purpose: this is a working research manuscript, with publication considered if the mathematics develops sufficiently. Sections 11–12 record the new audit reconciliation and the section-by-section v10 review.

Research follow-up: the author selected sampler/endpoint/Weil-form compatibility as the next target. Section 13 records the resulting construction and its unresolved graph defect. The earlier verdicts remain assessments of the supplied r11 text, not of the modified sampler developed in the new research note.

## 1. Assessment for our discussion

The manuscript contains useful exact operator identities, a substantial proposed co-Poisson tail argument, and several well-scoped obstruction calculations. It does not establish RH, as it correctly states. More significantly, the stronger status claim that the supporting G1/G2 chain is established except for one final arithmetic upper bound is not justified by the supplied proofs.

The principal issue is the passage from a global Hardy function to the same finite Weil matrix used by the endpoint calculations. The proof mixes a centered periodization with a sampler normalized at the cut endpoint. It also claims arbitrary vertical decay after sharp restriction to a fundamental interval, without the necessary boundary terms. These are upstream issues: they affect the asserted semilocal form transfer, reflected-pair lower limit, and critical boundary-trace asymptotic. They do not invalidate the independent finite-dimensional commutator identities.

There is also a definite version regression. The older file named `fixed_space_prime_action_latest.tex` contains the correct diagonal matrix estimate; r11 deletes it and substitutes a false diagonal formula. Fortunately, the weaker correct logarithmic bound appears sufficient to repair several affected continuity and shell estimates. That repair must be written, not assumed.

Recommended present description:

> A research manuscript on exact reductions and compatibility obstructions in Sonine/co-Poisson and finite-Weil models, with a proposed G1 estimate and an unresolved Hardy-to-semilocal transfer. It contains no proof of RH and does not yet establish the advertised single remaining G2 gate.

The author has chosen continued proof development as the immediate purpose. The earlier suggestion to prioritize a reduction-and-obstruction publication is therefore superseded. Preserve the broader RH program and useful failed routes, while keeping an explicit distinction between established local identities, incomplete proofs, and conditional consequences.

Recommended next research milestone: determine whether one precisely defined finite sampler can support the required endpoint, graph, and Weil-form limits simultaneously. First repair the known matrix and convention errors; then prove a corrected transfer theorem or establish a precisely scoped obstruction. The claimed final arithmetic little-o estimate becomes the next target only if that common finite realization survives.

## 2. Files and version reconciliation

| Supplied item | Finding | Review role |
|---|---|---|
| `AUDIT_G1_G2_2026-09-19.md` | Contains the base audit and Runs 8–11. Treats several disputed transfer claims as proved. | Reviewed as a set of claims, not as proof certification. |
| `fixed_space_prime_action_latest.tex` and `.pdf` | 3,963 source lines; 65-page PDF. Older than the other manuscript pairs despite the name. | Reviewed fully where shared, and separately for deleted/changed arguments. |
| `fixed_space_prime_action copy.tex` and `.pdf` | 5,604 source lines; 87-page PDF. Intermediate version. | Main body agrees with r11 until the added Run-11 material, apart from front matter and conclusion. |
| `fixed_space_prime_action(20260920-060548).tex` | 5,831 source lines. | Baseline source. |
| `fixed_space_prime_action(20260920-060549).pdf` | 89 pages. | Baseline PDF. |
| `fixed_space_prime_action_g1g2_2026-09-19_r11.pdf` | Byte-for-byte identical to the preceding PDF. | Duplicate, not another mathematical version. |
| `claude_audit.md` | Additional external audit of selected r11 results; expressly excludes most analytic transfer proofs. | Reconciled critically in Section 11. |
| `fixed_space_prime_action(20260920-062232).pdf` | 32 pages, supplied as v10; 22 sections. PDF metadata dates creation to September 19, 2026, before the other versions. | Earlier research snapshot, reviewed throughout; Section 12 records every section's disposition. No matching v10 LaTeX was supplied. |

Baseline source SHA-256: `84dd52131cd2c64e9df6420f51de2bc58bc89f5340b78d15ad9160659717ad14`.

Both r11 PDFs SHA-256: `1fb27a63338428fe0417b33a32886c98e122b5b45e55361e2edabbdc1e52af5c`.

The review covered all 23 baseline sections, all 72 theorem/lemma/proposition/corollary statements, the intervening discussion, the existing audit, and the older source's substantial deleted material. The follow-up covered Claude's complete audit and all 22 sections of v10, including a text comparison of Sections 1–19 against r11. The numbered claim register below records a verdict for every one of the 72 r11 statements. These verdicts are mathematical review judgments, not claims of formal verification or priority.

Status terms:

- **Pass:** the displayed local argument checks under the framework or prerequisites identified here.
- **Repair:** a specific formula, hypothesis, definition, or proof step needs correction; the intended result may survive.
- **Open:** the supplied argument does not establish the conclusion. This does not assert that the conclusion is false.
- **Conditional:** the deduction is valid only after an explicitly identified unresolved input is assumed.

## 3. Findings that determine the paper's status

### F1. The centered periodization and endpoint sampler are different finite vectors

Location: Section 21, source lines 2581–2603 and 2653–2707; labels `eq:high-order-graph`, `eq:periodization-strip-error`, and `thm:off-line-form-transfer`.

The manuscript defines samples with coefficients

\[
 L^{-1/2}\kappa(1/2+it_n)F(1/2+it_n),\qquad t_n=2\pi n/L,
\]

in the CCM basis, whose boundary values are equal. Consequently its physical endpoint is the unphased Riemann sum

\[
 \delta(JF)=\frac1L\sum_n\kappa(1/2+it_n)F(1/2+it_n)
 \longrightarrow \sigma F(\sigma).
\]

But the transfer proof uses the centered periodization

\[
 h_L(y)=\sum_{k\in\mathbb Z}g(y+kL),\qquad |y|\le L/2.
\]

For the exponentially localized functions used there, its values at the cut endpoints satisfy \(h_L(\pm L/2)\to0\). These are incompatible endpoint limits for the same vector when \(\sigma F(\sigma)\ne0\).

In coordinates \(x=y+L/2\), the missing translation character is \((-1)^n\). Depending on the Fourier sign convention there may also be an index reflection, which does not remove this translation character. The phrase “basis-origin phase already accounted for” does not insert it into the displayed sampler, matrix, boundary covector, or graph-source formulas. CCM explicitly defines its basis through \(x=\log(\lambda u)\in[0,L]\); its matrix and boundary functional are tied to this cut. See [CCM, Proposition 3.2 and equation (3.21)](https://arxiv.org/html/2511.22755v1#S3).

This is not resolved by saying that the global Weil form is translation-invariant. A translation on the whole line and a rotation followed by cutting a circle at a fixed endpoint are different operations. If the basis is changed by the diagonal unitary \(P=\operatorname{diag}((-1)^n)\), the matrix and covectors must also be conjugated/transformed. Preserving the old equal-coefficient endpoint functional while using the centered global limit needs a new proof.

Independent check, using the smooth Gaussian \(g(y)=e^{-y^2}\) with \(L=4\):

| Quantity | Value |
|---|---:|
| Center of centered periodization \(h_L(0)\) | 1.0000002250703495 |
| Endpoint of centered periodization \(h_L(L/2)\) | 0.03663127777746882 |
| Unphased Fourier sample sum | 1.0000002250703497 |
| Sample sum with \((-1)^n\) | 0.03663127777746877 |

This numerical illustration checks an exact Fourier translation identity; it uses no zeta zeros. As \(L\) grows, the first limit is 1 and the second is 0.

**Required action:** choose and explicitly write one physical realization of the sampler, its Fourier transform, its finite matrix, and its endpoint functional. Reprove the transfer on that exact object. Until then, the later reflected G2 lower limit and its \(L^{-1/2}\) normalization are not established by this manuscript.

### F2. The strip-error estimate drops sharp-cut boundary terms

Location: Section 21, source lines 2653–2671, `eq:periodization-strip-error`.

The claimed estimate has the form

\[
 |\widehat h_L(z)-\widehat g(z)|
 \le C_R e^{-\delta L}(1+|\Im z|)^{-R}
\]

for arbitrary sufficiently large fixed \(R\), uniformly across a strip. The proof invokes repeated integration by parts in a smooth periodic coordinate. However, \(\widehat h_L\) here is the transform of the zero-extended fundamental representative, not just its lattice Fourier coefficients.

For a smooth periodic \(h\), with \(A=L/2\), direct integration gives

\[
 \int_{-A}^{A}h(y)e^{-ity}\,dy
 =\frac{h(A)e^{-itA}-h(-A)e^{itA}}{-it}
 +\frac1{it}\int_{-A}^{A}h'(y)e^{-ity}\,dy.
\]

Even when \(h(A)=h(-A)\), the boundary term generally does not vanish at arbitrary \(t\). It vanishes on the Fourier lattice, not at arbitrary zero ordinates. A tiny nonzero coefficient multiplying \(1/t\) is still not bounded by a constant times \(t^{-R}\) for all \(t\) when \(R>1\). At off-line strip points, the unequal real exponential weights give additional boundary terms.

For the same Gaussian example, at \(t=(2k+1)\pi/4\), the computed \(t\)-scaled transform error tends to \(2h_L(2)=0.07326255555\), rather than to zero. This is the boundary term predicted by the displayed integration-by-parts identity.

**Required action:** replace the estimate with one retaining boundary terms, or change the truncation and then account for its effect on the sampler and graph identities. A bound with only \(1/(1+|t|)\) decay can still be enough for some quadratic zero sums, since products decay faster; that is a possible repair, not a proof of the present same-object statement. The exponent in \(L\) must also be derived from the half-window tail distances, not merely asserted from pole locations.

### F3. r11 replaces the correct diagonal Weil kernel with an incorrect one

Location: Lemma 21.5, source lines 2785–2798, and Lemma 21.48, source lines 5415–5423.

r11 obtains the diagonal by taking a formal limit of the off-diagonal divided difference and writes

\[
 q(U_n,U_n)(y)=-2yL^{-1}\cos(2\pi ny/L).
\]

Direct autocorrelation instead gives

\[
 q(U_n,U_n)(y)=2(1-y/L)\cos(2\pi ny/L),\qquad 0\le y\le L.
\]

In particular its value at zero is 2, not 0. The separate diagonal formula is also stated in [CCM, Lemma 2.3](https://arxiv.org/html/2511.22755v1#S2.SS2).

Thus the asserted uniform-in-\(n\) bound \(|\tau_{n,n}|\le C\lambda\) is false for fixed \(\lambda\): the archimedean term has logarithmic high-frequency growth. The older 65-page source already contains the correct replacement at lines 2008–2057:

\[
 |\tau_{n,n}|\le C\{\lambda+1+\log(2+|n|/L)\}.
\]

It explicitly warns that the diagonal is not the off-diagonal limit. This correction was deleted in the later versions.

**Required action:** restore the separate diagonal estimate and redo Lemmas 21.5 and 21.48. Their intended conclusions are plausibly repairable: logarithmic growth times rapidly decaying sampler coefficients is summable, and a finite operator bound of order \(\lambda\log K\) can absorb the corrected diagonal. The older weighted-sampler argument is a better starting point than the r11 proof.

### F4. First-slot-linear and first-slot-antilinear formulas are mixed

Locations: Propositions 21.14 and 21.18; Corollary 21.31; existing audit's claimed conjugation correction.

The manuscript commits to \(\langle cx,y\rangle=c\langle x,y\rangle\). A cross form identified with \(\langle Wx,y\rangle\) therefore satisfies

\[
 Q(x,cy)=\overline c\,Q(x,y).
\]

Corollary 21.31 instead writes \(Q(g,A^*(cv^-+w))=c\mathcal C\) and says the form is linear in the second slot. Under the declared convention the factor must be \(\overline c\). Proposition 21.14's displayed cross constant conjugates the first test factor, while its proof even drops the conjugation entirely. These cannot all represent the same declared sesquilinear form.

**Required action:** choose one convention throughout, state the polarized zero-side formula explicitly, and correct constants, filter factors, and second-slot scalar factors. Magnitude bounds and nonvanishing often survive conjugation; exact complex limits do not survive unchanged. Calling this only a global Fourier phase issue is insufficient.

### F5. The pole-aware transfer needs estimates at all zeros, not only the pole

Location: Lemma 21.16, source lines 3659–3697.

The nonzero residue at \(\rho^\sharp\) is correctly identified. The proof then says the fundamental-window transform grows only linearly at that exceptional point and treats every other zero by ordinary strip-error control. A function with a one-sided tail of rate \(d=\Re\rho-1/2\) does not have the same full-strip transform bounds as the earlier holomorphic, faster-decaying Hardy outputs. Beyond its strip of absolute convergence, finite-window transforms can grow exponentially with the window length, even at points distinct from the pole.

A sufficiently small truncation error in the radical factor might compensate for that growth, but the required product estimate, including high ordinates and the chosen physical cut, is not supplied. F1 and F2 also apply here.

**Required action:** state a separate quantitative product estimate for the radical and meromorphic test transforms, uniformly over all relevant zeros, and prove summability. Do not mark Lemma 21.16 or its beta-channel corollaries as established until that is done.

### F6. The shifted periodic-kernel upper bound omits an image it later proves significant

Location: Proposition 21.27, particularly `eq:shifted-kernel-terminal-weight`, and Proposition 21.28.

The proof of 21.27 treats the opposite periodic image as exponentially smaller merely because \(\tau<L/2\). But the two sides have different decay rates. Proposition 21.28 itself identifies a reflected-pole image of size

\[
 e^{-d(L-\tau)}.
\]

That term can be larger than the claimed weighted-kernel scale \(e^{-\tau/2}\). For instance, with \(\sigma=2\), \(d=0.1\), and \(\theta=\tau/L=0.26\), the image has exponential scale \(e^{-0.074L}\), whereas \(e^{-\tau/2}=e^{-0.13L}\). These parameters obey the advertised range \(1/(2\sigma)<\theta<1/2\).

The nonzero simple-pole residue generates such a term in the derivative of the odd trace near the endpoint unless an additional cancellation is proved. The current proof gives no such cancellation. Therefore the periodic-kernel estimate cannot be accepted on the stated argument. If the intended object was an unperiodized continuum kernel, its definition and the assertion must be changed.

The elementary comparison

\[
 \frac d{d+q}<\frac1{2q+1}\quad(0<d<1/2)
\]

is correct. Its use as a no-go theorem must specify which transfer and which upper estimate it excludes. Also, the alias expansion's remainder must be proved smaller than the displayed alias; writing merely \(O(e^{-cL})\) with unspecified \(c>0\) does not imply that asymptotic dominance.

### F7. Several foundations are imported from unspecified earlier audits

Locations: Sections 3, 12, 17–19 and 23.

Examples include the “checked” evaluator norm law, the exact source-moment repair, the closed arithmetic operator \(A\), the zero/jet graph-core property, the “certified two-zero calculation,” and final claims about source quasimodes and partner-blind functional calculus. Some may be valid results from prior work, but their proofs or precise references are not supplied here.

Completeness/minimality of a family is not by itself a graph-core theorem for an unbounded operator. A numerical observation is not a certified nonorthogonality proof without an error enclosure. Statements about earlier work need either a reproduced lemma, an exact cited theorem, or a clearly labeled assumption.

**Required action:** add a foundation appendix defining the Hilbert space, the domain of \(A\), the graph functional, and the required core/resolvent assertions. Identify project deductions as such rather than attributing all of them to Burnol.

### F8. The bottom-eigenvalue calibration uses more than the displayed G1 estimate

Location: Section 20, source lines 2445–2461, preceding (G2.2).

Monotonicity of the semilocal bottom eigenvalue under extension of support is a sound min–max observation. The claimed implication from the preceding G1 estimates to \(\lambda_a\le o(1)\), however, is not demonstrated. Fixed-band residual smallness does not by itself control the Rayleigh quotient of the changing BV prolate proxy. The proxy need not be an admissible uniformly bounded \(H^1\) test in the Sobolev estimate, and no uniform self-pairing estimate is written.

The later spectral-overlap inequality is correct when its vector is in the operator domain, but form-domain membership alone does not define \((A_a-\alpha_a)p_a\).

**Required action:** supply a direct normalized Rayleigh-quotient estimate, cite an applicable theorem with its hypotheses, or state (G2.2) conditionally on that estimate. Keep the norm-residual/overlap criterion separate from weak G1 pairing control.

## 4. Section-by-section review

Page numbers are printed r11 PDF pages; source line ranges refer only to the timestamped r11 `.tex`.

| Section | Pages; source lines | Audit finding and action |
|---|---|---|
| 1. Objective and correction | 1; 36–52 | **Pass with exposition repair.** The conversion from bilinear Burnol evaluators to a first-slot-linear Riesz convention is consistent. Define the completed transform and conjugation symmetry before using it. State that asymptotic compatibility is the practical target; “positive action” alone is too vague. |
| 2. Burnol framework | 2; 53–103 | **Pass subject to explicit conventions.** Support spaces, source range, quotient, nesting, and dilation are consistent with the cited framework. Define \(M_0\), \(M\), \(c_0(s)=\pi^{-s/2}\Gamma(s/2)\), and cosine normalization. Smooth sources supported in a closed interval must mean smooth ambient functions with that support. |
| 3. Corrected fixed compression | 2–3; 104–130 | **Pass for exact identity; incomplete proof of rate.** Contractivity and the corrected boundary identity check. The \(\log L\) evaluator norm law is invoked rather than proved. Supply its normalization and error estimate; the relative residual conclusion then follows. |
| 4. Source covariance | 3–4; 131–188 | **Pass.** The differential/source dilation covariance and three overlapping source intervals yield the closure-of-sum decomposition. The strict \(L^2>p\) condition provides overlap for a smooth partition. The projection-drop identities follow from orthogonality. |
| 5. Quotient-native pencil | 4; 189–213 | **Pass.** Adjoints, contractions, and the generalized eigenrelation check. Keep the distinction between an exact pencil and a contractive single operator. |
| 6. Defect kernel | 4–5; 214–253 | **Pass with scope repair.** Difference-of-Gram and diagonal sign identities check; diagonal nonnegativity plus functional-equation symmetry excludes off-line zeros. Full-span positivity adds cross-term restrictions. Say it is not implied by the displayed RH argument, rather than claiming a strict logical separation without a demonstrated counterexample. |
| 7. Pure Sonine comparison | 5; 254–278 | **Pass as a reduction; target wording conflicts with Section 6.** The arithmetic projection drops exactly. The paragraph again proposes a norm inequality on the full zero span, although the preceding section identifies diagonal evaluator inequalities as the appropriately weak target. Revise the target consistently. |
| 8. Fredholm shell imbalance | 5–7; 279–379 | **Pass.** The two-channel lost-energy formula, dilated one-channel collapse, and Hilbert–Schmidt remainder bounds check. Specify \(L>2\) for the displayed small-\(a\) estimates. The error is an absolute bound, not a sign or relative-dominance theorem. |
| 9. Projection-angle form | 7–8; 380–437 | **Pass for projection identities; repair the range claim.** The synthesis operator has closure of its range equal to \(W_{pL}\). Theorem 4.1 does not show its actual range is closed. Replace “closed range” accordingly. The block Gram matrix is positive automatically and supplies no sign theorem. |
| 10. Local-prime sieve | 8–9; 438–482 | **Pass.** Deletion of multiples of \(p\), Mellin Euler factor, reflected factor, and norm identity check. Require \(p\) to be prime here; earlier dilation statements work for general real scales. |
| 11. Finite Euler-product failure | 9–10; 483–533 | **Pass with citation/detail repair.** The prime-shell reduction and first surviving logarithmic moment produce the stated divergent \(L^2\) contribution for a fixed nonzero source. State the weighted PNT remainder used uniformly over the compact \(u\)-interval. Scope correctly excludes only the raw finite sieve and fixed finite moment repair. |
| 12. Reflection leakage and multiplicity | 10–14; 534–743 | **Repair.** Source-jet transport and determinant reasoning are coherent once the factorization is established. The proof must show that zero source jets force the transformed vector back into \(W_L\), not infer this merely from vanishing output jets. Use compact source division. Restate the inherited off-line assumption in Theorem 12.1: at \(w=w^\sharp\), the multiplier is 1 and leakage has rank 0, not \(m\). Explicitly justify the ambient jet Gram bound. |
| 13. Bridge to prime compression | 14–16; 744–836 | **Pass conditional on the preceding leakage realization.** The positive defect, return decomposition, alias bound, and finite-dimensional counterexamples check. Rename \(J_{L,p}\): it is the opposite-direction map from Section 5's \(J\). |
| 14. Infinitesimal source defect | 16–17; 837–914 | **Repair/proof completion.** The Mellin generator identity and compact-source moment criterion are credible and directly derivable. Give the Volterra division proof and the finite-jet correction argument for closure. Distinguish powers of the core restriction from powers of its closure. |
| 15. Boundary-triplet and incidence | 17–19; 915–1002 | **Pass conditional on source-division/domain lemmas.** Basic deficiency dimension one and the off-line pole-removability criterion are sound. For a skew-symmetric operator, an extension of \(S\) is obtained by restricting \(-S^*\), not \(S^*\); state the action. Reserve a different symbol from the Sonine projection \(S_L\). |
| 16. Nested defect ladder | 19–20; 1003–1069 | **Pass with proof completion.** Rank at most one follows from division; explicitly prove the arithmetic defect is nonzero both at and away from a zero. Then the orthogonal decomposition and Pythagorean identity follow. Keep the off-line restriction and avoid identifying it with a characteristic function without proof. |
| 17. Exact returns versus asymptotics | 20–22; 1070–1152 | **Pass for the contraction theorem; repair asymptotic support.** Dense unimodular eigenvectors force unitarity and orthogonality. The claimed \(O(L^{-1})\) projection correction and bounded critical cross terms need a proved evaluator estimate. Finite-mode Gram calibration then follows; it gives no uniform growing-window theorem. |
| 18. Off-line resolvent and determinant | 22–25; 1153–1249 | **Conditional.** The divided-difference bound and determinant argument are useful, but the fixed closed operator, its domain, and its graph core are not established here. Riesz calculus is zero-list-independent, not independent of zeta: it explicitly uses \(\zeta\) and contours in the resolvent. The self-commutator anti-symmetry checks. |
| 19. Finite-prime comparison and metric | 25–26; 1250–1302 | **Pass for the metric implication; repair the comparison.** The finite-window Lyapunov criterion follows by testing an eigenvector. The norm-resolvent no-go relies on an absent “certified” nonorthogonality calculation and needs precise identification assumptions. Preserve the finite-prime theorem's simplicity/evenness hypotheses; do not present them as unconditional at every cutoff. |
| 20. Focused finite-Weil residual | 26–47; 1303–2551 | **Substantial argument, with remaining proof obligations.** Exact commutator algebra, high–low estimates, BV/VP transfer, and shell calculations are sound in their stated weak regimes. The fixed-order radial estimates align with the primary asymptotic source. Fully specify the two-mode source normalization and prove the endpoint comparison/moment-repair scale. G2 bottom-level inference needs F8. Add \(\alpha_a\ge0\) (or the appropriate weaker sign condition) to the Schur proposition. See the claim register. |
| 21. Hardy sampling and G2 | 47–86; 2552–5696 | **Main transfer open; numerous independent identities pass.** F1–F6 prevent endorsement of the heading's claimed closure. Preserve exact graph, commutator, projective-invariance, and periodic-resolvent identities. Reopen semilocal transfer and every downstream nonzero finite limit depending on it. Correct the diagonal and sesquilinearity regressions. See the detailed claim register. |
| 22. Original boundary criterion | 86–87; 5697–5713 | **Pass as a criterion, repair the research direction.** The contractive-compression residual criterion is valid; its critical-line rate depends on Section 3. The final item points to a barrier later shown partly tautological. Replace it with the actual unresolved normalization/transfer task. |
| 23. Claim discipline and next step | 87–88; 5714–5747 | **Rewrite after agreement.** “Not a proof of RH” is correct, but “the lower-side gates are closed” overstates the supplied evidence. Restore upstream gaps. Quasimode, partner-blindness, and equivalence claims need precise lemmas. Distinguish diagonal evaluator signs from positivity on their full span. |

## 5. Additional technical repairs and scope limits

1. **Definitions and domains.** \(M\), \(M_0\), \(c_0\), \(\widehat L_1\), \(A\), and \(\eta\) need one authoritative definition. Separate the original \(L\) cutoff from the later logarithmic length \(L=2\log\lambda\). The same symbols \(S_L,J_{L,p},C_{L,p},P_a,a,\alpha,\kappa\) are repeatedly repurposed.
2. **Weak versus strong control.** A small fixed-band projection, a small smooth-test pairing, a small form value, and a small operator norm are different conclusions. The manuscript sometimes distinguishes them carefully and sometimes moves between them without a theorem. State the exact topology at every limit.
3. **Core versus closure.** For Section 12, if the source jet vanishes, repeated compact Volterra division should yield an admissible source. This supplies the missing kernel inclusion. Passing to the closed source space then requires continuity and a finite-dimensional moment correction. For Section 14, the same argument proves density in the intersection of kernels; it should be written once and cited internally.
4. **Schur sign hypothesis.** Proposition 20.18's last comparison requires \(\alpha_a+\beta_a^2/c_a\ge0\), normally ensured by \(\alpha_a\ge0\). Without this, take \(q=\operatorname{diag}(10,1)\), \(\alpha=-10\), \(\beta=0\), \(c=1\): the stated bound would falsely assert \(1\ge10\).
5. **Repeated poles.** The pole at \(-a\) of order \(M\) generally produces a polynomial factor multiplying the exponential tail. The exact rate in `eq:gF-logtails` omits it. Use a slightly weaker exponential rate or include the polynomial.
6. **Filter admissibility.** Proposition 21.32's elementary inequality \(|\Phi(\rho^\sharp)|\ge c_0/\|\Phi\|_\infty\) is sound for \(\Re\rho>1/2\). But holomorphy in the right half-plane plus continuation only near two points does not by itself give an admissible global Weil test. Also require a nonzero endpoint factor \(\Phi(\sigma)\) when using its boundary-annihilation ratio. Separate the elementary inequality from the global transfer claim.
7. **Upper bounds do not prove impossibility.** The PNT-envelope and growing-filter-norm calculations show a limitation of the estimates used. They do not prove that all signed arithmetic cancellation or all transfers with large sup norms are impossible. A large available norm bound is not a lower bound on the actual pairing error.
8. **Exact matcher scope.** Proposition 21.38 eliminates a vector mismatch algebraically; it does not make endpoint recovery the only remaining analytic problem. Sampler injectivity, norm control, form transfer, and weak G1 compatibility remain. The shell-collapse example correctly demonstrates this.
9. **Boundary-jet subtraction.** The fixed-\(\lambda\), large-\(|t|\) expansion is valid with one-sided smoothness and vanishing lower-end traces. The terms \(1/(it)^j\) cannot be subtracted globally across \(t=0\) without a cutoff or a low-frequency prescription. It is an asymptotic expansion, not immediately a globally bounded regularizer.
10. **No-go quantifiers.** Projective candidate invariance is an exact paired identity for a fixed test with zero boundary. Its nonzero asymptotic interpretation additionally needs the disputed G2 transfer. Do not generalize it to changed tests, changed matrices, or arbitrary new transports.

## 6. Earlier-version material worth retaining

The intermediate `copy.tex` adds no major independent body argument beyond what r11 contains, while its oversized status box is much less readable. The 65-page `latest.tex`, however, has material that should not be discarded merely because it is older:

| Older result | Source location in `latest.tex` | Verdict |
|---|---|---|
| Complete Fourier-matrix bound | 2008–2057; `cor:g1-complete-matrix` | **Restore.** Correctly separates diagonal autocorrelation and retains logarithmic growth. Directly repairs an r11 regression. |
| Weighted-sampler G1 transfer | 2265–2385; `prop:g1-weighted-sampler` | **Retain, conditional on continuum G1.** The three-region convolution argument and separate diagonal estimate give a useful explicit bound uniform in the ambient cutoff. Check constants in the final rewrite. |
| Exact arithmetic jump train | 2387–2498; `lem:g1-jump-train` | **Pass for fixed cutoff.** Jumps occur when summands leave the source support; inversion gives the signed pair of atoms. The Fourier sine-sum formula follows by Stieltjes integration. Define endpoint representatives and exclude boundary thresholds from the interior list. |
| Jump/continuous transfer split | 2505–2578; `prop:g1-jump-split` | **Pass conditional on the preceding G1 and matrix estimates.** Subtracting the jump train improves the continuous remainder to an \(n^{-2}\) Fourier bound. This does not establish a uniform endpoint-normalized derivative bound. |
| Near-Slepian jump scale | 2580–2638; `cor:g1-jump-natural-scale` | **Pass for the jump component only.** The \(\lambda^{2+o(1)}\) cutoff follows from the subexponential tolerance. The continuous-remainder condition is explicitly unproved and must stay so. |

The exact line extents above identify the relevant neighborhoods; theorem labels are the stable identifiers for merging.

## 7. Review of the supplied G1/G2 audit file

| Audit portion | What survives | What must change |
|---|---|---|
| Base status and G1/G2 summary | Correctly disclaims an RH proof and distinguishes \(WDk\) from \(DWk\). | Its certification of all lower-side transfer steps is unsupported by F1–F5. |
| Claimed sesquilinear correction | Correctly recognizes that a conjugation is necessary. | The chosen placement is inconsistent with the stated first-slot-linear convention; Corollary 21.31 confirms the inconsistency. |
| Boundary traces and critical scale | Exact rank-two boundary identity is useful. | The nonzero limiting constant and critical scale remain conditional on repaired transfer. |
| Candidate invariance and shell universality | The projective paired identity is sound. | The common *nonzero* limit requires the currently unproved lower transfer. |
| Run 8, arithmetic beta realization | Exact prime/pole/archimedean coefficient and trace algebra is a strong retainable result. | It identifies an arithmetic observable; it does not independently establish its claimed zero-forced limit. The stated high-precision numerical audit has no accompanying script in the supplied files. |
| Run 9, moving Hardy phase | The global phase product, graph covariance, and Cauchy damping identity check. | The periodic-kernel upper estimate neglects the image discussed in F6. |
| Run 10, pole-aware repair | Correctly notices that the reflected resolvent test has a pole. The threshold comparison is algebraically correct. | Counting only the exceptional pole is not a uniform full-zero-sum transfer proof. The alias remainder needs an explicit relative estimate. |
| Run 11, normal form and bounded filters | The rational normal form, pole residue, and elementary bounded-filter tradeoff are useful. | Correct conjugations, add test admissibility/endpoint assumptions, and describe the norm-cost conclusion as a limitation of the proved estimates. It does not repair F1–F5. |

## 8. Source and presentation checks

Key primary-source checks were made against:

- [Burnol, 2001](https://arxiv.org/pdf/math/0105120), especially the definitions of \(H_\Lambda\), continuous completed-Mellin evaluation, and the co-Poisson range. These support the baseline framework, not every later project-specific operator claim.
- [Burnol, Sonine spaces, 2002](https://arxiv.org/pdf/math/0208121), Lemma 2 and Theorem 4. The Fredholm projection structure agrees with Section 8 after translating conventions.
- [Dunster, final arXiv version](https://arxiv.org/pdf/1601.00699), equations (1.24), (3.5), (3.7), and (3.10). The radial Bessel formula is uniform on the exterior interval, and at order zero the endpoint normalization used in the draft is consistent. The earlier v2 has different equation numbering; use v3 in the bibliography and checks.
- [Connes–Consani–Moscovici](https://arxiv.org/html/2511.22755v1), for the basis, separate diagonal kernel, and finite-form setup. Its opening finite-operator theorem assumes the relevant ground-state simplicity and parity. The draft should preserve those hypotheses.
- [Suzuki, v2](https://arxiv.org/html/2606.09096v2), for the distinction between general semilocal structure and sufficiently-small-support ground-state conclusions. Section 20 appropriately warns against extrapolating the small-support argument to large support.

This was not a novelty search, and every cited reference was not independently re-proved. The externally sourced facts above were checked where they affect the manuscript's main logical dependencies. Project-specific claims lacking a proof are identified in this report rather than being accepted from the previous audit's wording.

PDF checks in the first pass: extracted text from the four supplied PDFs, scanned their pages for gross content outside a generous safe area, and visually inspected the opening layouts of the three distinct PDF versions. No unresolved `??` references were found in their extracted text. The baseline source has no duplicate labels or missing `ref`/`eqref` targets. In the follow-up, extracted and read the additional 32-page v10 throughout and visually inspected its opening page; a full visual layout audit of v10 was not performed. These checks do not substitute for a full visual pass after the eventual revision.

Presentation priorities: add an abstract and contents; split the approximately 40-page Section 21 into short named sections; reduce the status box to a brief current-status paragraph; move chronological “latest audit” narratives to a changelog; define G1 and G2 before using them; and use one notation table. The bibliography's AI-assistance entry should be treated as an acknowledgment of assistance, not evidence that a mathematical claim was independently certified.

## 9. Agreed purpose and remaining Q&A

**Settled:** continue a working RH research manuscript; publication is a later possibility. Preserve promising constructions and the reasons earlier routes failed. Do not reorganize the project around a publication-sized negative result unless the author later chooses that direction.

**Recommended immediate goal:** rebuild the common finite realization connecting G1 and G2. A successful next stage would specify the exact matrix, sampler, physical cut, endpoint functional, and graph action; correct the diagonal bound and conjugations; and establish which form limits actually hold for those objects. A rigorous obstruction to a particular realization would also be useful progress, provided its scope is stated precisely.

**Subsequently settled:** the author selected the sampler/endpoint/Weil-form compatibility question. The follow-up result is recorded in Section 13; no change of route to the original prime-compression approach was requested.

Proposed organization once that target is agreed: keep an authoritative main manuscript with explicit proof-status notes, place lengthy failed-route calculations in an appendix, and retain a separate change log. Restore the correct diagonal/weighted-sampler material without importing incompatible conventions. The source/domain lemmas remain required groundwork. Update the status box and conclusion to reflect the actual dependencies, then compile and visually verify the revised LaTeX/PDF.

## 10. Numbered claim register

The register below covers every theorem, lemma, proposition, and corollary in r11. Numbering includes intervening remarks because the LaTeX shares their counter. “Pass” concerns the local deduction with the stated prerequisites; it does not silently certify the upstream framework or a disputed transfer.

| Claim | Source line | Status | Finding |
|---|---:|---|---|
| 4.1. Three-piece arithmetic source decomposition | 153 | **Pass** | Support partition and covariance give equality after closure; no closed-range assertion. |
| 4.2. Arithmetic projection disappears in two adjoint channels | 175 | **Pass** | Orthogonality to the three transported source spaces proves the identities. |
| 6.1. Finite-cutoff span positivity would imply RH | 232 | **Pass** | Sufficient hypothesis; do not treat full-span positivity as an established or necessary RH criterion. |
| 12.1. Exact multiplicity-$m$ leakage factorization | 613 | **Repair** | Restate off-line hypothesis; prove the zero-jet kernel inclusion by compact division before asserting exact factorization. |
| 13.1. No generic domination between cross-scale and fixed-space defects | 807 | **Pass** | The two explicit three-dimensional examples reverse the defect ordering. |
| 14.1. Exact generator range defect | 883 | **Repair** | Write compact division and finite-jet density correction; distinguish core powers from closure powers. |
| 15.1. Exact zero-incidence criterion | 972 | **Pass** | Off-line pole removability gives equivalence, subject to the stated ambient division theorem. |
| 17.1. Exact diagonal contractions force orthogonality | 1073 | **Pass** | Dense unimodular eigenvectors force a surjective isometry and phase orthogonality. |
| 17.2. Finite-mode asymptotic calibration | 1131 | **Conditional** | Finite-dimensional Gram argument is valid; supply the preceding evaluator asymptotics. |
| 18.1. Exact off-line spectrum of the fixed arithmetic operator | 1186 | **Conditional** | Needs the missing closed-operator/domain/graph-core construction; the displayed bounded resolvent alone is not that construction. |
| 19.1. Uniform metric defect excludes an off-line window | 1270 | **Pass** | Valid finite-window implication given the Riesz realization and the two explicit metric hypotheses. |
| 20.1. Endpoint-normalized radial bound | 1344 | **Pass** | Exterior bound follows from the cited uniform Bessel formula at fixed order. |
| 20.2. Away-boundary and exterior-energy bounds | 1382 | **Pass** | Away-endpoint decay and the change of radial variable give the displayed energy estimate. |
| 20.3. Uniform far field with controlled $c$-dependence | 1413 | **Pass** | The radial ODE, integrable perturbation, and fixed radial phase support the stated far-field estimate. |
| 20.4. Endpoint-normalized radial lattice bound | 1458 | **Pass** | Absolute summation before the far field and the uniform harmonic-sine tail control resonance. |
| 20.5. Fixed-order co-Poisson cross-tail | 1517 | **Repair** | Give the explicit two-mode normalization, endpoint noncancellation and moment-repair asymptotics; define the cross-correlation fully. |
| 20.6. Quantitative endpoint-jump bound | 1587 | **Conditional** | Rate calculation is coherent once the exact tail normalization and centered discrepancy bounds are in place. |
| 20.7. Inversion symmetrization preserves the G1 envelope | 1710 | **Pass** | Simultaneous inversion transfers the bound on the same test class. |
| 20.8. Sobolev form of the continuum G1 estimate | 1739 | **Conditional** | Derivative/trace argument is plausible; fully justify the correlation and local archimedean estimates from the corrected cross-tail lemma. |
| 20.9. Arithmetic BV structure and absence of a periodic boundary jump | 1781 | **Pass** | Finite arithmetic sum is piecewise smooth; inversion makes the one-sided periodic endpoint limits agree. |
| 20.10. Fixed-cutoff boundary-preserving Galerkin approximation | 1813 | **Pass** | Fixed-cutoff BV Fourier decay and the logarithmic form weight give form convergence; endpoint convergence uses Dirichlet–Jordan. |
| 20.11. Quantitative and cofinal finite-section transfer of G1 | 1865 | **Pass** | Correct finite-band transfer of an assumed continuum bound; its cofinal threshold need not be economical. |
| 20.12. Zero-independent high--low decay of the Weil matrix | 1957 | **Pass** | Off-diagonal convolution, Chebyshev prime bound and sine-integral estimate give the high–low bound. |
| 20.13. Explicit BV rate for the fixed-band Galerkin defect | 2018 | **Pass** | BV coefficient decay times the high–low matrix bound gives the stated summable tail. |
| 20.14. Quantitative endpoint recovery by de la Vall\'ee--Poussin filtering | 2092 | **Pass** | Near/far convolution split gives the endpoint modulus estimate. |
| 20.15. Filtered BV transfer with explicit boundary control | 2138 | **Pass** | Conditional on the stated continuum estimate and endpoint constants; specify the degenerate zero-Lipschitz-constant case. |
| 20.16. High-frequency boundary repair has unavoidable square-root derivative cost | 2230 | **Pass** | Weighted Cauchy–Schwarz proves the sharp derivative cost. |
| 20.17. Constructive zero-independent finite G1 closure | 2301 | **Pass** | Constructive finite weak transfer follows from its inputs; it is not a global operator-norm G1 theorem. |
| 20.18. Form-Schur lower bound | 2481 | **Repair** | Add a nonnegative error parameter or the sign condition needed in the final norm comparison. |
| 21.1. One-sided off-line Weil isotropy | 2636 | **Pass** | Global zero-side isotropy for the holomorphic smoothed one-sided root functions; fix the surrounding transform conventions. |
| 21.2. Off-line semilocal form transfer | 2673 | **Open** | F1–F2: the centered periodization does not match the unphased endpoint sampler, and the strip estimate drops boundary terms. |
| 21.3. G2b under the off-line contradiction hypothesis | 2709 | **Conditional** | Coercivity follows from repaired form transfer, a negative compact test, and ordinary sampling coercivity. |
| 21.4. Restricted scalar-shift coercivity is automatic after form transfer | 2730 | **Conditional** | Elementary consequence of form transfer; it is not an independent arithmetic positivity theorem. |
| 21.5. Smooth-test continuity of the semilocal Weil pairing | 2769 | **Repair** | F3: use the correct logarithmic diagonal estimate. Rapid test decay can still give the claimed continuity conclusion. |
| 21.6. The proved G1 estimate applies to the full Hardy sampler | 2820 | **Repair** | Use corrected diagonal/weighted-sampler estimates. Its weak G1 part can be separated from the unproved joint G2 transfer. |
| 21.7. Finite G1 jet hierarchy on the full Hardy sampler | 2925 | **Repair** | Same as the preceding result for each fixed finite derivative order; no growing-order uniformity follows. |
| 21.8. Fixed residual-jet Gramians cannot supply G2 coercivity | 2980 | **Conditional** | Sum-of-squares argument is exact once the stated weak jet estimates are established. |
| 21.9. Off-line coercivity forces a boundary-weighted sampler residual | 3019 | **Pass** | Finite Lyapunov/commutator identity and lower bound check under the stated coercivity and norm hypotheses. |
| 21.10. Exact sampler--prolate compatibility decomposition | 3115 | **Pass** | Exact algebra for an even candidate with nonzero endpoint; the pairing inequality is a consequence, not closure. |
| 21.11. Commuting-correction cancellation and the scalar-shift no-go | 3195 | **Pass/Conditional** | Exact source and scalar cancellations pass. The final asymptotic statement additionally assumes disputed form transfer. |
| 21.12. Exact noncommuting G2 excess | 3286 | **Pass** | Exact graph identity; positivity must be paired with an independent upper estimate. |
| 21.13. $W^2$ benchmark: positivity moves the gap to norm transfer | 3357 | **Pass** | Positive square and rank-at-most-four commutator calculation check; form smallness does not imply norm smallness. |
| 21.14. Reflected-partner $W^2$ coercivity at arbitrary multiplicity | 3385 | **Conditional** | Global reflected nonvanishing is valid after convention repair; finite cross transfer and norm lower bound depend on F1–F2. |
| 21.15. A boundary-annihilating G2 test isolates the exact sampler--prolate mismatch | 3491 | **Conditional** | Finite annihilation and residual algebra check; its nonzero limit requires the repaired reflected transfer. |
| 21.16. Pole-aware radical transfer for the fixed Hardy sampler | 3659 | **Open** | F5: needs full-strip product estimates over all zeros, together with a consistent finite cut. |
| 21.17. The surviving simple-zero obstruction is a boundary commutator channel | 3699 | **Conditional** | Exact decomposition, but the nonzero beta limit requires the unproved pole-aware and reflected transfers. |
| 21.18. Multiplicity-robust reflected-partner block obstruction | 3729 | **Conditional** | Top-Jordan selection and graph relation check. Finite lower limits and radical transfer remain unproved; fix cross-form conjugation. |
| 21.20. Rank--two boundary traces exhaust the reflected G2 signal | 3892 | **Pass/Conditional** | Exact rank-two identity passes; exhaustion of an asymptotic signal assumes vanishing radical pairing on that test family. |
| 21.21. Critical $L^{-1/2}$ scale of the surviving boundary trace | 3951 | **Conditional** | Division of two nonzero limits is valid, but the necessary same-object lower limit is not yet established. |
| 21.22. Exact arithmetic realization of the surviving CCM boundary channel | 3991 | **Pass** | Finite sine-transform, Stieltjes integration, and folding identities check for the declared matrix and first-slot convention. |
| 21.23. G2 is an explicit finite prime/pole/archimedean forcing statement | 4135 | **Conditional** | Arithmetic identity passes; the nonzero asymptotic forcing depends on the disputed critical-scale result. |
| 21.24. The present absolute PNT remainder is quantitatively insufficient for the G2 boundary channel | 4169 | **Pass** | The absolute PNT envelope gives only the stated large upper bound; scope is this estimation method. |
| 21.26. Hardy phase shifts preserve the global G2 signal while damping the Hardy endpoint | 4220 | **Pass** | Global graph covariance, Cauchy damping, and reflected product invariance check; correct the general sesquilinear convention. |
| 21.27. A translated Hardy kernel recovers an absolute PNT gain at the continuum-kernel level | 4287 | **Open** | F6: periodic reflected images are not controlled by the claimed weighted-kernel estimate. |
| 21.28. Reflected-pole alias obstruction to the moving Hardy phase | 4381 | **Repair** | Threshold algebra checks; prove alias-relative remainder bounds and carefully scope the no-go after correcting the preceding upper estimate. |
| 21.30. Exact continuum normal form of the boundary-annihilated G2 test | 4488 | **Pass** | Cauchy-ratio algebra, cancellation at sigma, and the unique reflected strip pole check for the fixed sampler. |
| 21.31. The reflected pole is forced by any cross-retaining holomorphic correction | 4563 | **Repair** | The residue statement passes; second-slot scaling is conjugate-linear under the declared convention. |
| 21.32. Bounded Hardy filtering cannot suppress the reflected pole while retaining G2 | 4596 | **Repair** | Elementary modulus inequality passes. Add global admissibility and nonzero endpoint conditions before claiming sampler/form consequences. |
| 21.33. Absolute-PNT rescue by pole damping lies outside the audited G1 regime | 4645 | **Repair** | Present as a limitation of an envelope/norm-based proof strategy, not as a necessary lower bound on actual error. |
| 21.35. Projective boundary-quotient invariance of the G1/G2 mismatch | 4713 | **Pass** | Exact paired commutator identity needs neither parity nor equal endpoint magnitude; asymptotic equivalence assumes the two G1 pairings. |
| 21.36. The prolate core may be replaced by a pure boundary shell in the lower obstruction | 4774 | **Conditional** | Candidate invariance and shell weak bounds are useful; a shared nonzero limit still needs repaired G2 transfer. |
| 21.37. Moving Hardy evaluation aligns the graph functional | 4822 | **Pass/Conditional** | Finite-root-space scalar asymptotic passes. Joint preservation of the G2 transfer remains conditional. |
| 21.38. Candidate-adapted graph sampler: exact vector matching | 4892 | **Pass** | Exact coefficientwise graph matching and scalar mismatch factorization; this does not establish sampler coercivity or form transfer. |
| 21.39. Exact-radical factorization removes the zeta quotient but exposes an endpoint phase | 4955 | **Pass** | Müntz factorization plus one-sided integration by parts yields the nondecaying phase and bulk Plancherel identity. |
| 21.40. Finite boundary-jet expansion of the exact matcher | 5040 | **Pass** | Valid fixed-cutoff high-frequency expansion with the stated smoothness; low-frequency regularization is a separate task. |
| 21.42. Exact periodic-resolvent formula for the adapted endpoint | 5109 | **Pass** | Periodic first-order ODE and parameter derivatives give the Laplace-jet identity. |
| 21.43. Boundary-perfect high-frequency matching has vanishing bulk mass | 5165 | **Pass** | Explicit Laplace sum and Fourier coefficient count give endpoint matching with vanishing Hilbert mass. |
| 21.45. Parity projection gives a bounded noncommuting G2 benchmark | 5254 | **Pass** | Rational principal-part comparison gives injectivity on a fixed one-sided root space; finite norm sampling suffices here. |
| 21.48. The exact-boundary shell is compatibility-efficient in the coercive pairing | 5346 | **Repair** | Correct the diagonal estimate. The weaker logarithmic bound fits the stated finite norm and shell estimates after redoing the proof. |
| 21.49. One shell cutoff neutralizes both the G1 repair and its G2 pairing cost | 5472 | **Conditional** | Cutoff arithmetic checks given the corrected shell estimates; applies to the repair part, not all core terms. |
| 21.50. A joint exact-boundary G1/pairing diagonal | 5530 | **Conditional** | Valid assembly of the stated weak core/shell inputs; do not read as closure of the full G2 mismatch. |
| 21.51. Scalar-shift positivity cannot remove the final defect | 5622 | **Pass** | Triangle/reverse-triangle argument is exact under the explicitly assumed full residual and derivative-norm hypotheses. |

The next manuscript should cite stable theorem labels while merging; numbering will change after restructuring. No revised LaTeX or PDF has been generated in this review stage.

## 11. Reconciliation with Claude's audit

Claude's audit independently confirms several useful local calculations. Its stated exclusions are essential: it expressly does not check the periodization strip estimates, reflected finite coercivity, multiple-root transfer, or most of the PSWF/Sobolev chain. Its opening statement that it found no invalidating error is therefore a report about that limited review, not evidence against F1–F8. The two audits agree more closely on the formulas actually checked than their headline assessments suggest.

| Claude finding | Combined assessment | Consequence for the working manuscript |
|---|---|---|
| Exact beta coefficient/discrepancy identity | **Agree.** The finite Stieltjes calculation and point-term integral check. The identity uses integer Fourier indices. | Keep as an established finite identity; explicitly state \(n\in\mathbb Z\). Do not infer the downstream nonzero beta limit from this identity alone. |
| Endpoint/PNT threshold disjointness | **Agree on the algebra; qualify the no-go.** For \(q=\sigma-1/2>0\), the threshold difference is \(q(1-2d)/[(d+q)(2q+1)]>0\) when \(0<d<1/2\). | The assertion that the whole moving-phase route has “no gap” additionally needs the periodic-image and relative-remainder estimates disputed in F6. An algebraic comparison does not verify those estimates. |
| Boundary-annihilated normal form and reflected residue | **Agree.** The rational bracket cancels the Cauchy pole and leaves the displayed simple reflected pole. | Add that reflected multiplicity is exactly \(m\), by the functional equation and conjugation symmetry. Keep finite transfer separate from the continuum residue calculation. |
| Bounded-filter tradeoff | **Agree with the elementary inequality.** Continuation to the reflected point is necessary. | Correct the older audit's broader wording. Also require admissibility of the resulting global test and nonvanishing of the endpoint denominator before using sampler/form consequences. Local continuation alone does not provide those properties. |
| Boundary/projective invariance | **Agree.** The finite paired commutator identity is useful independently of the prolate core. | State explicitly that equality of two asymptotic values does not prove their common value is nonzero; that requires the disputed G2 transfer. |
| Deleted uniform weighted-sampler chain | **Agree that useful material was deleted; qualify the claimed cofinality failure.** See below. | Restore the correct diagonal estimate. Retain or reconstruct the uniform weighted theorem where useful. State the actual cutoff quantifiers instead of relying on the word “cofinal.” |
| One common diagonal | **Agree as proof organization.** Finite cutoff choices should be collected in one lemma. | Such a lemma combines compatible, proved estimates; it cannot repair a false transform bound or identify different finite vectors. |
| Mechanical integrity and version naming | **Agree on duplicate PDFs and misleading `latest` naming.** Strict label-set inclusion is not the lineage relation, because labels were deleted. | Use explicit version names for new work and preserve the historical files. Citation/reference integrity does not certify the mathematics. |
| Claim discipline and overall status | **Partly agree.** The RH disclaimer and many local scope limits are appropriate. | r11's stronger statement that the lower-side gates are established is not supported by the supplied proofs. Rewrite it for a working manuscript with unresolved upstream transfer. |

### 11.1 What the surviving full-Hardy proof actually gives

The old weighted-sampler proposition supplies an explicit estimate for every \(K\ge2N\). r11 no longer contains that theorem. Claude is right that this uniform statement should not be claimed as though it survived unchanged.

However, the categorical claim that r11 contains no full-Hardy cofinal argument is too strong. Source lines 2895–2916 use convergence of the full sequence of VP means, then uniform absolute convergence of a Fourier series after the core is fixed. If the invoked analytic estimates are corrected and established, these give **eventual thresholds**, not just isolated successful cutoffs:

\[
 \forall\lambda\ \forall\varepsilon>0\quad
 \exists N_0(\lambda,\varepsilon)\quad
 \forall N_c\ge N_0\quad
 \exists K_0(\lambda,N_c,\varepsilon)\quad
 \forall K\ge\max\{2N_c,K_0\}.
\]

The first threshold controls replacement of the continuum proxy and its endpoint recovery; the second controls truncation against the fixed finite-support core. The old theorem's stronger assertion is that the stated rate already holds throughout \(K\ge2N_c\), without this extra core-dependent ambient threshold. These are different assertions. Moreover, “cofinal sequence,” meaning cutoffs eventually exceeding any fixed bound, should not be confused with “every sufficiently large cutoff is admissible.” The rewrite should avoid that ambiguity.

The incorrect diagonal formula in Lemma 21.5 is a real defect, but it need not destroy this weak-continuity mechanism. With the correct diagonal bound from Section 6, its diagonal contribution is

\[
 O_{\lambda,R}\!\left(C_u(1+|n|)^{-R}\log(2+|n|)\right).
\]

The off-diagonal split still gives \(O_{\lambda,R}(C_u/(1+|n|))\): for \(|m|\le|n|/2\), use the summability of the test coefficients; near \(m=n\), use their \(|n|^{-R}\) decay and the harmonic logarithm; in the remaining region, use distance from the diagonal. Thus the matrix-series estimate needed for square-summable action survives for \(R>2\). This supplies a concrete repair to the local estimate, subject to the stated closed-form realization. It does not resolve the G1 source-normalization obligations or the G2 cut mismatch.

### 11.2 A valid diagonal-selection statement, and its limit

The appropriate elementary selection lemma is the following conditional statement.

Fix a finite collection of test families and their parameters. Each error below must already include the normalization required by the intended conclusion; unscaled convergence does not imply convergence after multiplication by a growing factor. Suppose:

1. the required continuum errors tend to zero as \(\lambda\to\infty\);
2. for each fixed \(\lambda\), every required core-approximation error tends to zero as \(N_c\to\infty\);
3. for each fixed \((\lambda,N_c)\), every required ambient-truncation or shell-pairing error tends to zero as \(K\to\infty\), uniformly over the specified test families;
4. no additional condition imposes an incompatible upper bound on the selected cutoffs.

Then one can select \((\lambda_j,N_{c,j},K_j)\), with all cutoffs growing and \(K_j\ge2N_{c,j}\), on which all these finitely many errors tend to zero. Choose \(\lambda_j\) to control the continuum errors, then \(N_{c,j}\) beyond the maximum of the finitely many core thresholds, then \(K_j\) beyond the maximum of the ambient thresholds and the previous cutoff. At each stage one may prescribe a smaller positive tolerance, including the factors needed for an endpoint or critical-scale normalization. This is an eventual-tail argument; arbitrary unbounded sets of good cutoffs would not suffice, since their intersections can be empty.

For a moving smoothing parameter such as \(\sigma_j\), fix it first at each stage and apply only statements valid at that fixed value. No uniform rate in \(\sigma\) is then implied.

This lemma is a useful replacement for repeated informal enlargement claims. Its hypotheses are **not presently all verified for the proposed r11 G1/G2 combination**. In particular, F1–F2 and F5 concern the underlying continuum-to-finite limits themselves. Adding the selection lemma cannot make those limits true.

### 11.3 Numerical evidence

Claude correctly warns that direct adaptive quadrature across prime-power jumps can create false residuals. For independent numerical checks, integrate the prime step contribution as a finite sum and treat the smooth terms separately. The algebraic derivation already confirms the beta identity.

Claude reports double-precision residuals around \(10^{-17}\)–\(10^{-15}\). Those are consistent with the identity at that precision; they do not substantiate the earlier audit's claimed \(10^{-19}\) accuracy. Neither supplied audit includes a reproducible high-precision script. No conclusion in this reconciliation relies on those numerical precision claims.

## 12. Review of the additional 32-page v10

The file is the earlier manuscript identified by the author as v10; its title page itself carries no v10 identifier. SHA-256: `b24a2c0da6fc8e59fd3a181765739c7780ec56ff62379810ace375c8b5fbb118`.

Its main value is architectural. Sections 1–19 largely carry the same early framework as r11. Section 20 is a six-page predecessor of the later expanded G1 treatment; it does not contain r11's large Hardy/G2 section. The final two sections correspond to r11 Sections 22–23. It offers an earlier account of the research state, not an independent proof of the later transfer claims.

The following register covers all 22 v10 sections. Shared results inherit the detailed qualifications in Sections 3–5 and the r11 claim register above; repeated statements are not counted as independent evidence.

| v10 section | Pages | Audit and disposition |
|---|---:|---|
| 1. Objective and correction | 1 | **Retain.** Same first-slot Riesz correction and prime multiplier as r11. Useful statement of the program's original objective. |
| 2. Burnol framework | 1–2 | **Retain with definitions clarified.** Same spaces and nested-evaluation identity; write closures and all transform conventions explicitly. |
| 3. Corrected fixed compression | 2 | **Exact identity passes; rate conditional.** The evaluator norm law remains described as previously checked, without its proof. v10 does not fill that gap. |
| 4. Source covariance | 3 | **Pass after closure.** Same partition-of-unity decomposition and projection corollary. This still does not prove the synthesis range is closed. |
| 5. Operator pencil | 4 | **Pass.** Preserve the exact generalized eigenrelation and its limited implication for a single fixed-space action. |
| 6. Defect kernel | 4–5 | **Pass as a sufficient criterion.** The warning that full-span positivity is stronger than evaluator-wise sign control remains important. |
| 7. Pure Sonine comparison | 5 | **Reduction passes; target wording needs repair.** It again proposes positivity on the whole zero span after the preceding section warns that this is overstrong. |
| 8. Fredholm shell reduction | 5–7 | **Pass with stated scale restrictions.** Retain the exact lost-energy formula and remainder; no shell-sign theorem is supplied. |
| 9. Projection-angle form | 7–8 | **Projection identity passes; repair range wording.** The claim that the source synthesis has closed range is not established. |
| 10. Local-prime sieve | 8–9 | **Pass.** Keep the exact Euler-factor deletion with \(p\) prime; it does not determine the shell sign. |
| 11. Finite Euler-product failure | 9–10 | **Pass with PNT detail/citation.** Same scoped obstruction to the raw sharp sieve and fixed finite moment repairs. |
| 12. Reflection leakage and multiplicity | 10–14 | **Repair.** Same missing compact-division kernel argument. v10 also asserts a stronger ambient jet-Gram asymptotic than r11; do not restore that unsupported strengthening. |
| 13. Bridge to prime compression | 14–16 | **Conditional on leakage realization.** Exact defect/alias identities and the two counterexamples agree with r11. |
| 14. Infinitesimal range defect | 16–17 | **Proof completion needed.** References earlier compact-source Volterra division; does not actually provide the missing division and closure proof. |
| 15. Boundary-triplet/incidence criterion | 17–19 | **Conditional on domain lemmas.** Same useful incidence criterion and deficiency discussion; specify the skew-adjoint extension action as a restriction of \(-S^*\). |
| 16. Nested defect ladder | 19–20 | **Pass after division/nonvanishing details.** Orthogonal decomposition is useful, but no new characteristic-function identification appears. |
| 17. Exact returns and asymptotics | 20–22 | **Contraction theorem passes; asymptotic estimates need proof.** v10 repeats the raw-evaluator projection estimate rather than establishing it. |
| 18. Off-line resolvent/determinant | 22–24 | **Conditional.** The closed arithmetic operator and graph-core property are still invoked from a prior construction. r11 adds a useful nonextendibility argument for the displayed Jordan chain. |
| 19. Finite-prime metric comparison | 24–26 | **Metric implication passes; bridge conditional.** Same absent certified nonorthogonality calculation; preserve the external finite-model hypotheses. |
| 20. Focused finite-Weil residual | 26–31 | **Useful predecessor, not a replacement proof.** Exact rank-two residual identity and fixed-order radial bound survive. The lattice/cross-tail proof is less complete than r11, and boundary-preserving finite transfer is explicitly left open. See below. |
| 21. Original boundary criterion | 31 | **Valid conditional criterion.** Corresponds to r11 Section 22. Distinguish evaluator-wise relative residual control from the stronger whole-span sign target. |
| 22. Claim discipline and next step | 31–32 | **Useful research framing; unsupported summaries remain.** Corresponds to r11 Section 23. Quasimode and partner-blindness assertions still refer to missing audits; the asserted equivalence with a general arithmetic return needs precise hypotheses. |

### 12.1 Material to recover, retain, or decline

**Recover the three-gate roadmap on page 31.** It separates (i) continuum co-Poisson tail control, (ii) finite approximation preserving the relevant boundary/form scale, and (iii) coercivity or positive-metric transport. This is a better working structure than saying that only a final signed cancellation remains. Update its status labels: the present review has not certified all source-normalization details in the first gate, and it identifies substantive unresolved compatibility issues in the second. Calling the second gate merely “technical” is not a proof of its solvability.

**Retain r11's weaker jet-Gram requirement.** v10 equation (40) claims
\(\det V_{w,L}=C_{w,m}L^{2md}(1+o(1))\), using an unproved relative projection estimate. r11 replaces this by the one-sided bound \(\det V_{w,L}\ll L^{2md}\), which is all the subsequent determinant argument needs. That is a genuine improvement in proof burden. The raw-representative construction and its normalization should still be written explicitly.

**Retain the expanded r11 radial analysis.** v10 Proposition 20.1 is the same endpoint-normalized bound retained in r11. In v10 Proposition 20.2, the far representation is justified for \(x\ge Kc\), but its amplitude is then said to be matched on \(2\le x\le3\); that is not an overlap of the stated regimes for large \(c\). An additional continuation/ODE estimate is needed. r11's separate away-boundary, exterior-energy, and controlled far-field lemmas provide a more explicit route. Use that later argument, with the source-repair qualifications already recorded, rather than reinstating the shorter proof.

**Do not restore v10's unqualified cross-correlation derivative estimate.** Sharp zero extension introduces endpoint terms. r11 explicitly separates the absolutely continuous derivative and the endpoint-jump contribution; that is an improvement. v10 does not supply a missing proof that bypasses the later endpoint problem.

**The useful deleted matrix/weighted-sampler material is in the 65-page `latest.tex`, not this 32-page v10.** Keep the two historical recovery sources distinct. The 65-page version supplies the correct separate diagonal estimate and the quantitative weighted-sampler chain. The 32-page version supplies a clearer early roadmap and a record of which finite-transfer questions were still open.

Neither historical version resolves the same-object transfer issue in F1–F2. The next research decision should therefore be made on the basis of that unresolved mathematical question, rather than on version age or agreement between audit headlines.

## 13. Research follow-up: a coherent finite construction and the remaining graph defect

The author asked us to determine whether the sampler, endpoint functional, and Weil-form transfer can work together on one consistently defined finite object. The resulting nine-page note is `sampler_compatibility_2026-09-20.tex` / `.pdf`, accompanied by `check_sampler.py` and `sampler_checks.json`.

**Answer:** yes, after changing the sampler by an explicit phase and rank-one endpoint correction. The original unphased sampler does not have the claimed full-scale transfer. The corrected construction changes the exact graph identity used downstream, so it does not close the G1/G2 or RH argument.

The note fixes the Fourier transform as \(H_F(s)=\int g_F(y)e^{-(s-1/2)y}\,dy\), keeps the original CCM basis on \([0,L]\), and uses its actual equal-coefficient endpoint. It establishes the following results under stated smoothness/decay hypotheses available with sufficient fixed Hardy smoothing:

1. **Correct centered transfer.** The centered samples have coefficients \((-1)^nL^{-1/2}H_F(s_n)\). Retaining the sharp-cut boundary terms gives a strip error of size \(Ce^{-cL}/(1+|\Im s|)\). That decay suffices for products in the zero sum. Correct logarithmic diagonal bounds give a quantitative Fourier-truncation estimate. This repairs F2 for the centered realization, whose physical endpoint tends to zero.
2. **Explicit uncentered obstruction.** In this Fourier convention the Hardy output has negative tail \(g_F(y)=E e^{qy}\), where \(E=\sigma F(\sigma)\), \(q=\sigma-1/2\). The unphased sampler cuts at zero and moves that half by \(L\). Its transform is asymptotic, in the paired form sense, to
   \[
   H_F(s)+E\frac{e^{-(s-1/2)L}-1}{\sigma-s}.
   \]
   The resulting explicit zero sum has a nonzero Laplace-transform residue at every critical-line zero when \(E\ne0\) and \(H_F\) vanishes there. It cannot have a finite full-real-scale limit. This applies conditionally to any nonempty hypothetical one-sided root window, and unconditionally to the larger output class through \(H=\kappa\zeta\). It does not exclude specially selected subsequences or other transports.
3. **A constructive repair of the three properties.** In the ambient space \(|n|\le2K\), take
   \[
   c_{L,K}=\frac{\sqrt L}{2K}\sum_{K<|n|\le2K}V_n,
   \qquad
   \widetilde JF=J^{\mathrm c}F+c_{L,K}\{\sigma F(\sigma)-\delta(J^{\mathrm c}F)\}.
   \]
   Then \(\delta(c)=1\), so endpoint recovery is exact. The explicit choice \(K=\lceil\lambda^4L^4\rceil\), \(\lambda=e^{L/2}\), makes the correction vanish in ordinary norm and in the finite Weil pairings. Both self- and reflected cross-form transfer hold for this modified sampler. This cutoff is sufficient, not asserted optimal.
4. **The graph defect is explicit and cannot be omitted.** Writing \(d(F)=\sigma F(\sigma)-\delta(J^{\mathrm c}F)\), the new graph residual is
   \[
   \mathcal RF=iD_Lc\,d(F)-c\,d(BF).
   \]
   Its ordinary norm grows for a fixed \(F\) with nonzero recovered value. More generally, a correction vanishing in ordinary norm while restoring a nonzero endpoint must have growing derivative norm, by the periodic trace inequality. The Sylvester equation also makes the sampler unique when its exact source vector and graph functional are prescribed.
5. **A precise next pairing.** The exact commutator exposes
   \[
   \langle W\mathcal RF,v\rangle
   =i d(F)\langle DWc,v\rangle
   -i\sqrt L\,d(F)\langle\beta,v\rangle
   -d(BF)\langle Wc,v\rangle.
   \]
   Thus form-smallness of the endpoint correction does not remove the boundary channel from the graph calculation. For an even G1 candidate, adding this even shell to the test sampler leaves the literal \(DWk\) pairing unchanged by parity; that fact does not cancel the displayed graph defect.

The accompanying finite checks use \(H=\kappa\zeta\), without inserting any hypothetical zero. At \(L=10,N=512\), the uncentered form is approximately 1.337515 and the centered form is approximately \(4.078\times10^{-7}\); the recovered endpoint is approximately 3.289868. These are illustrative floating-point checks, not proofs. A quadrature refinement changed a representative matrix by less than \(2\times10^{-12}\). All analytic conclusions above have separate arguments in the note.

The original r11 manuscript has not been silently rewritten to use this new sampler. Integrating the construction requires carrying its graph residual through the later reflected-test and boundary-channel arguments. The source-normalization and operator/domain obligations elsewhere in this audit also remain.
