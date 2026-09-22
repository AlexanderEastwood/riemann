# v1.42 — NS-17 integration and PR preparation, September 21, 2026

## 2026-09-21 — v1.49 / NS-32 and NS-33: audit and exact weighted zero input

PR #14 was re-reviewed at revised head f3611ef and remains held, not merged
or tagged. Its revision resolves the false biconditional and acknowledges
unbounded critical-level density, but three MAJOR findings remain: the new
K rearrangements are invalid; the lambda=4 c'=1 returned state still fails
bin feasibility (ratio 0.636); aligned-bin maxima are identified with the
full concentration function in the wrong bound direction. The exact
weighted-cost implication and uniform constant c=c'*phi pass. Revised PR
head builds to 239 pages, 0 undefined/duplicate; audit v3 preserves v1/v2.

What had to change: the crude peak-density scalar is vacuous for any range
containing a negative critical value. The exact density has an integrable
unbounded singularity there; a histogram peak is not an upper bound. For a
finite R, phi^2/R can grow only if R=o(phi^2); bounded above does not exclude
R->0. The bounded fraction phi alone is not an impossibility argument.

The concentration-function proof is repaired, with edge correction -h*phi/2
and its correctly rearranged denominator. The surviving quantity is QC_K. QC_1=phi*D-mean(beta^-) is an exact
zero functional, but its growth alone does not control fixed K: a continuous-
measure full-support countermodel has QC_1~D/2 and QC_2->0. Named input QG
requires QC_K->infinity for every fixed K, together with independent
source-admissible bounded-energy WLH packets. A QC_1/K lower law needs a
separate shape hypothesis; linear growth in D needs QC_1>=d0*D as well.

No limit of phi or growth of negative-set measure follows from v1.37's
pointwise depth divergence. No claim of equivalence/independence with RH
is made. The source overlap/energy/projection check is named, not run;
NS-28 raw files are preserved and its report receives a correction notice.
This is failure of the proposed bound and diagnostic interpretation, not
of the physical form. Both cofinal inputs remain open; the route stays
blocked. No new window, tail metric, optimizer or zero enclosure. G2/RH
and NS-1's two evidence groups remain open. Final build: 242 pages,
0 undefined references, 0 duplicate references, 0 overfull boxes.

## 2026-09-21 — v1.47 / NS-29: level distribution as a zero statement

Actual build: 237 pages, 0 undefined references, 0 duplicate references,
0 overfull boxes. Analytic work only; no numerical experiment substituted.

What had to change: lower cumulative sublevel measures are insufficient;
one needs increments across every interval of levels. Packet density must
be bounded below on a set covering each of those level bands, with original
energy uniformly bounded. Positive fraction alone and upper density are
insufficient. The conditional bound on [-theta D,0] is
eta >= [b alpha kappa theta^2 D/K - Q]+.

The corrected complete zero sum equals beta, so its band distribution is
precisely the named open input ZLD. Primary zero-counting, zero-density,
Landau-Gonek and pair-correlation results were assessed; no theorem or
standard-conjecture reduction supplies this signed value distribution.
Its logical strength relative to RH and pair correlation remains
unclassified; no equivalence or independence is asserted.

The v1.37 depth proof gives no uniform band measure. An explicit derivative
bound gives local width with a window-dependent cost; the RH probe gives
a cumulative bound that can be zero at t=theta D. A smooth pulse spread
across [0,X] has energy log X + O(1), illustrating the separate energy
obstacle; source projection retains its cross and pointwise costs.

Outcome: named zero-distribution input plus independent packet coverage,
both open. This is a gap in the proposed obstruction, not failure of the
true concentration inequality or physical form. The route remains blocked,
not closed. No new window, head run, tail metric or zero enclosure. NS-28
is untouched; NS-1's two groups, G2 and RH remain open.

## 2026-09-21 — v1.46 / NS-26 and NS-27: explicit formula and scoped obstruction

Actual build: 232 pages, 0 undefined references, 0 duplicate references,
0 overfull boxes. New diagnostic scripts: pyright 0 errors, 0 warnings.

NS-26 is an exact unconditional shifted Perron identity. The functional
equation cancels the archimedean block; the strict integer endpoint,
trivial zeros and finite-prefix remainder remain. The lattice has varying
cosine/sine envelopes, not exact equal crests or quarter-point zeros.
The naive sum is an amplitude contribution, not a crest-minus-trough.
Forty low and fourteen deep/centroid locations were reproduced at two
precisions. With Gaussian epsilon=.025 and exact desmoothing, sufficient
positive-zero counts are 83/83/80/80 for lambda=3/4/6/8 low samples, and
530/609 for the selected lambda=4/8 deep samples. All corresponding
residuals are below 1.5e-7. These are numerical illustrations and empirical
sufficient counts, not interval certificates; the reference prefix has
1200 positive zeros and a 1000-to-1200 stability check. The sharp sum's
symmetric-height convention and finite Perron remainder are explicit.
A centroid is not a trough location; two have positive beta. This is the
explicit formula restated, with no new cofinal density or sign content.

NS-27 proves eta >= [(b+B)c-B]+ and eta >= [c*delta-Q]+, retaining
positive spill and the original packet energy. It proves explicit full-
and half-cell packet concentration and handles source projection and odd
parity. The 0.6-0.8 diagnostic concerns the entire negative set, not a
single half-cell (whose even concentration norm is <0.509 at the stated
carrier scale). A conditional level-count theorem gives
eta >= [c D_a/(2K)-Q]+, but uniform arithmetic level mass and bounded
packet energy remain unproved. For J-trough floors eta>=d_(J+1); v1.37
proves only d_1=D_a grows, not the requisite cofinal multiplicity.
A two-level countermodel shows that depth/concentration alone are not
sufficient premises. The actual arithmetic route remains blocked, not
closed; the concentration proposition remains a valid sufficient criterion.
This is a gap in the proposed bound/obstruction, not failure of the object.

No new window, head, Weil-tail metric, or v1.43 zero-enclosure refinement.
G2, RH and the two NS-1 evidence groups remain open.

## 2026-09-21 — v1.44 / NS-24: pencil demands and cofinal quantifiers

Actual build: 225 pages, 0 undefined references, 0 duplicate references,
0 overfull boxes. No numerical experiment was run.

The exact directional demand is L_a[v_k]/q_a^+[v_k] <= nu_k +
eta_a ||v_k||^2/q_a^+[v_k]. The diagnostic raw even head is not
source-compressed, so admissibility is explicit; all mixtures require
the restricted matrix inequality with its loss and norm cross terms.
The single-window test does not supply the cofinal complete-complement
estimate. Uniformly bounded errors already suffice under the existing
v1.36 both-parity and source hypotheses. Small diagnostic nu_k values
alone do not refute that weaker target. NS-24 is done and the analysis
stops at this finding: no new run, window, tail metric or enclosure
refinement. This is an exact translation, not a new concentration bound
or a failure of the object. G2, RH and the two NS-1 evidence groups remain open.


## 2026-09-21 — v1.43 / NS-19: complete enclosure and scoped resolution

The revised Task B closes with |z_1(4)-gamma_1|<8.752082e-33<9e-33,
including first-positive-zero exclusion, at 1024/1280 bits. The construction
uses the complete evaluator dual bound instead of the old ordinary
projection error; all archived tail cross terms remain. The direct limit
is C_ell*rho. A hypothetical lower-energy transfer would require
rho-l about 3.2032e-153 (relative 1.3055e-78); this is missing and the
frozen trial is not centered for a gamma-based 1e-71 enclosure. A lower
bound alone does not improve the direct upper-energy formula, but can
improve the separate transfer enclosure toward the frozen-trial floor
abs(fhat(gamma_1))/d = 1.064123340460...e-40/0.0016, about 6.65e-38.
This is a floor of that formula, not of the actual discrepancy; attainment
is not asserted.

The separately certified finite N=120 discrepancy ~+2.92504e-71 remains
finite. Resolution failure is scoped to the displayed bounds, not the
object or all possible arguments using the archive. User ended the signed
target; NS-19 is done. Actual build: 222 pages, 0 undefined references,
0 duplicate references, 0 overfull boxes. Tagged v1.42 evidence unchanged.
No new window or tail metric. NS-1, cofinal convergence, G2 and RH remain open.


Rebased the local result onto origin/main at 0f8cb16, preserving concurrent diagnostics. All five requested insert groups are integrated at their header anchors, with previous positioning prose consolidated. Groskin is updated to v3; KreinLanger2014 and BasorEhrhardt2002 are present; all Zhu citations use one Zhu2026 bibitem. NS-6/NS-17 complete in this version. The continuation paragraph explicitly avoids inferring global arithmetic identification from local extension uniqueness, and the matrix comparison does not falsely identify divided-difference commutators with standard one-symbol T±H. Original draft files are unchanged; integrated variants and source hashes are archived. Added the user's symbol context as a finite-compression midpoint diagnostic, with numerical zeros beyond the plotting scale not interpreted as exact absence of mass.

Build: 218 pages, 0 undefined/duplicate references, 0 overfull boxes. The 1024/1280-bit coarse NS-18 certificate is unchanged; sign/factor-10 discrepancy sharpening is now in progress. G2 and RH remain open; both NS-1 evidence groups remain OPEN.

---

# Version 1.42 — September 21, 2026

- NS-18: certified a unique simple local zero of the complete lambda=4 ground transform in (gamma_1-0.1, gamma_1+0.1). No earlier-zero enumeration or discrepancy sign is asserted.
- Reused the complete even Schur data with separator 1e-67, verified at 1024/1280 bits. The old global separator 1e-73 gives a transform-error bound too large for the same endpoint test. The new threshold is even-sector separation, not a global spectral gap.
- Proved the spectral-energy projection estimate and applied it to the same exact support-4096 trial. Compared the trial with its nonzero orthogonal ground projection; no unaccounted normalization change. The inherited infinite-tail bounds remain complete and the small prior gates are replayed; full old residual assemblies are not rerun.
- Verified endpoint signs and derivative positivity on eight intervals at both precisions. A second implementation checks principal-determinant inertia, direct centered cosine integrals and derivative signs on 32 intervals. Saved intervals retain all sign gates after parsing. This is a same-agent implementation check, not an external audit.
- No new windows, eigensolves, trial cutoffs or residual cutoffs. Tiny-discrepancy CCM transfer, cofinal convergence, G2 and RH remain open. NS-1 retains both OPEN historical evidence groups.

Build: 217 pages, 0 undefined/duplicate references, 0 overfull boxes.
Pyright: 0 errors and 0 warnings. Local branch; no publication is recorded.

---

# Version 1.41 — September 21, 2026

- NS-2: reproduced CCM section 6 Figure 1 at the existing lambda=3, N=120 benchmark; eight local root discrepancies match the published rounded values. The first is approximately 1.582329697193127e-34.
- Retained the unchanged original coefficient assembler with K=128. Isolated finite eigenpairs and verified root brackets at 768 and 1024 bits; midpoint roots are proposals only. Same problem across precision; no new window and no complete-ground zero transfer.
- Proved the exact (-1)^n centering dictionary. The old NS-14 reconstruction omitted it and evaluated a different function; its sinc-lattice inference is withdrawn. Original diagnostic files are preserved with a separately versioned correction.
- NS-3: added the half-width translation table, Zhu/Groskin comparisons and CCM mu_lambda paragraph. Corrected the stale comparison summary and retained the distinction between ground values, ordinary gaps and coordinate pivots.
- NS-4b: checked the already archived ten-route coverage table and concentration exclusion; linked its exact location from the manuscript.
- NS-1: original later evidence groups remain OPEN. Available archives, refs and saved records did not yield the missing original scripts or witnesses; no regenerated substitute is passed off as recovery.

Build: 215 pages, 0 undefined/duplicate references, 0 overfull boxes.
No new independent audit is claimed. G2 and RH remain open.

Resumed verification (2026-09-21): all eight local root gates passed again at 768 and 1024 bits, with identical centers and overlapping discrepancy intervals. Added the exact limitation that A -> c A + s I, c > 0, preserves the tested zeros; renamed the CCM infimum locally to avoid collision with the inverse-approximation parameter. Rebuilt: 215 pages, zero undefined/duplicate references and zero overfull boxes. Preserved the original reports and wrote research-report-2026-09-21-v2.html and build_report_v2.json. Later main-branch diagnostics/retractions still require coordinated integration; no push or merge occurred.

Integration (2026-09-21, NS-16): reconciled the saved candidate with main at 289961d. Retained all broader CCM diagnostic files, detailed NS-4b analysis, NS-3/NS-6 draft inserts, circle retraction files and original NS-14 outputs byte-for-byte. The obsolete KMS summary was not restored. Both interval replays and their verifier are unchanged; the manuscript links the detailed coverage analysis. Build: 215 pages, 0 undefined/duplicate references, 0 overfull boxes. Pyright: 0 errors/warnings. Added a separately versioned integration report and build record. Legacy v1.34-v1.37 manifest warnings match the pre-merge baseline; no historical recovery or cleanup is claimed. NS-1, complete-ground transfer, G2 and RH remain open.

---

# Version 1.40 — September 21, 2026

- Completed NS-5 for the complete lambda=4 operator: a simple even ground with 0<mu0<2.454e-75 and mu1>1e-73, hence ordinary gap>9.7546e-74.
- Extended the v1.17 shifted-inertia mechanism using a proved resolvent-change upper bound; lambda3 tail constants were not reused. The old lambda4 exact trial matrices and complete Schur inequalities remain fixed.
- Reconstructed ordinary head and tail Grams from exact frozen dyadic coefficients, retained every inverse-shift term, and certified one even negative pivot versus none odd at1024/1280bits. The complete Rayleigh witness supplies the actual shifted negative direction.
- Replayed the small prior even margin, odd complement, matching-head and repaired-direction gates. The full old infinite-tail assemblies are inherited inputs, not freshly recomputed at the new precisions.
- Checked the precise real-distribution and essential-selfadjoint-core hypotheses of Connes–van Suijlekom Theorem6.1. The entire Fourier transform of the complete ground has only real zeros; no simple-zero or Riemann-Xi convergence claim is made.
- Corrected the experimental interpretation: the eight-order figure describes a finite even-sector diagnostic; the chosen complete threshold must also respect the odd sector. The initially tried1e-70 is too large, as an exact odd trial lies below it;1e-73 passes.
- Added incremental evidence/v140/, updated the shared task board and research map, and retained LaTeX-only delivery. No older missing evidence was replaced by regenerated substitutes.

Build: 213 pages, zero undefined/duplicate references.

NS-5 is closed at lambda=4. No cofinal G2 gap was closed, and RH is not proved.

---

# Version 1.39 — September 21, 2026

- Replaced the informal proposed meta-obstruction with two exact hypotheses: a density relaxation admitting the v1.37 cutoff probe, and a compression bound invariant under domain-preserving spectral rotations fixing finite graph data.
- Proved that every sound budget in the former class diverges for the actual arithmetic symbol. This includes the optimal full-histogram mass-cap bound, and the mass/height/total-variation relaxation. Both parities and the complete-source-complement premise are explicit.
- Proved that arbitrary finite head and complete operator-action data can be kept exactly while a spectral rotation realizes compression Rayleigh values arbitrarily close to the multiplier's essential infimum. The form domain and source residual are preserved; the conjugates generally leave the multiplier class.
- Gave a positive location-independent counterexample and audited all ten historical closures. These theorems do not logically subsume all ten. In particular, concentration Schatten norms and block/cross-channel quantities may retain geometric information.
- Independent adversarial analysis corrected parity quantifiers and rejected a claim that the cutoff probe satisfies every physical derivative constraint. Conditional linear rates remain conditional; unconditional budget divergence is proved by the existing bounded-floor implication.
- Added exact rational model verification and primary-literature comparison with the classical bathtub principle and Fan–Pall spectral compression. The arithmetic specialization is a project continuation, not a claimed globally new theorem or publication-ready result.
- Retained one live LaTeX manuscript in manuscript/, incremental evidence/v139/, manifests, and log/. An actual local build is required; its ignored PDF is not delivered.

No G2 sign gap was closed, and RH is not proved.

---

# Version 1.38 — September 21, 2026

- Executed the requested cheaper finite-floor experiment at lambda = 5, 6, 8. Both complete parities satisfy W>=-8I, with every remote Fourier row enclosed.
- Held delta = 8, N = 256, J = 4096, moment order 16, tau = 1/10 and zero solve fixed across all six cases. Freshly evaluated every window-dependent constant; no false positive weighted-tail metric was reused.
- Replayed exactly the same dyadic congruence and trial vectors at 256 bits after160-bit initial certificates. All gates passed. Each trial quotient is positive and below 1e-16.
- Recorded certified lower bounds for the generalized shifted-certificate margin, separately from near-one whitening row margins. Margin bounds decline across the tested windows but do not diagnose negative eigenvalues.
- Proved the shifted scalar cutoff cost N+1>L exp(M_phi-delta): a fixed finite shift is a large practical constant-factor saving, but cannot turn this comparison into a polynomial-cutoff cofinal argument.
- By support consistency, the lambda = 8 floor also covers all 1 < lambda ≤ 8. This bounded interval is not the cofinal premise of v1.36.
- Classified the experiment as continuation of the existing shifted Schur/moment route, not a new arithmetic mechanism. Preserved all physical subspace, scale, endpoint and graph-defect qualifications.
- Updated the complete source, abstract, status, evidence inventory, cumulative log and notes. LaTeX only; no new PDF.

No G2 sign gap was closed, and RH is not proved.

---

# Version 1.37 — September 21, 2026

- Retested the v1.34 scalar primitive bound against v1.36's relaxed uniform finite lower-floor objective.
- Proved for the actual arithmetic symbol that a*Delta(beta_a) tends to infinity and inf beta_a tends to minus infinity. Neither scalar route can provide even a bounded cofinal error.
- Constructed a fixed nonnegative frequency probe with vanishing transform at the two physical cutoff endpoints. Its negative truncated mass isolates one critical zero under RH; all other zeros and the full exterior archimedean tail are controlled.
- Separated the RH-conditional linear bounds from the unconditional divergence conclusion. The latter follows by contradiction using the already proved finite-floor implication.
- Checked the strict prime endpoint, Fourier factors, explicit-formula regularity, physical domain and both parities with an independent adversarial reviewer. Added analytic constants and separate quadrature diagnostics.
- This is a proved no-go for a prior scalar route, not a new live positivity mechanism. The joint signed concentration estimate with one uniform finite ordinary lower constant remains open.
- Updated the complete source, abstract, status, research goals, historical route status, evidence inventory and references. No graph defect, endpoint or scale convention was changed.
- LaTeX-only delivery. Source validation uses draft mode without generating a PDF.

No G2 sign gap was closed, and RH is not proved.

---

## Delivery policy — September 21, 2026

At the author’s explicit request, manuscript delivery is LaTeX only from this update forward. The previously generated v1.36 PDF is not published or included in the update package. The existing GitHub v1.35 PDF and evidence are archived; the root contains one live LaTeX manuscript. Future runs must not generate or deliver PDFs unless requested again. This changes delivery only, not the mathematical conclusions.

# Version 1.36 — September 21, 2026

The complete manuscript now proves a sharper sufficient G2 reduction:
one finite lower bound uniform along a cofinal family on the complete
small-residual complement suffices. Its error need not tend to zero.
The uniform arithmetic estimate itself remains unproved.

- Proved totality of all fixed real translates of the actual Gaussian radical in ordinary L2, with complete localized operator residuals tending to zero.
- Proved unconditional strong-resolvent convergence to zero for the zero-extended complete Weil operators, also after deleting a block whose full residual tends to zero.
- Proved negative amplification: any negative compact smooth Weil test forces lower spectral edges to diverge to minus infinity. This gives the finite-floor reduction and its source-complement version.
- Proved that uniformly bounded positive comparisons with vanishing error must disappear strongly on the actual source complement; accounted separately for the odd subspace of physical C_a^low.
- Added exact support-consistent positive/negative countermodels, an independent adversarial review, domain and parity checks, and a formula-level novelty audit. The result is a continuation of the radical route, not a newly claimed arithmetic sign mechanism.
- Integrated the results into the abstract, current status, proofs, research goals and reproducibility appendix. Preserved the sampler's explicit graph defect, endpoints, Fourier scales, logarithmic diagonal and all earlier gap statements.

No G2 sign gap was closed, and RH is not proved.

The repository retains one live manuscript at its canonical root paths.
Superseded supporting evidence and provenance are archived rather than
presented as additional live versions.

---

# Complete manuscript v1.35 revision notes

## v1.35 — full parity symbol and growing physical radical blocks

- Extended the exact continuum-symbol representation to both complex parity
  sectors, retaining the negative odd pole. The combined gap-free error is
  `max(eta_odd, eta_even + 2 epsilon_source/sqrt(3))`.
- Proved a uniformly conditioned physical translate block of dimension
  `2 floor(log(lambda)/(2D)) + 1`, with full ordinary operator residual
  `C log(lambda) exp(-lambda/100)`; `D` is fixed by the source.
- Included every exterior prime row, both pole terms and the archimedean
  action in the proof. No Fourier cut or source-to-physical transfer is used.
- Proved the corresponding near-zero spectral count and the obstruction to
  positive uniform/polynomial gaps after `o(log lambda)` constraints.
- The odd subblock remains in the physical G2.6 complement of any even deep
  and plunge images, independently of their rank. Additional odd constraints
  must be counted separately.
- Novelty audit found the prior v1.14 fixed-rank derivative obstruction.
  This is its quantitative growing-rank continuation, not a new positive
  mechanism. The new ingredient is the uniform physical Riesz Gram estimate.
- Proof underwent an independent adversarial review. Numerical checks are
  explicitly diagnostic and are not used to certify any sign.
- No G2 sign gap closed. The near-zero eigenvalue signs, both parity blocks
  of the cofinal signed concentration estimate, and RH remain open.

The full manuscript is included. The update package contains new evidence
only; it does not replace the unavailable cumulative historical archive.

---

# Complete manuscript v1.34 revision notes

## v1.34 — disjoint-channel persistence and optimal primitive transport

- Proved that two disjoint reciprocal-scale Paley--Wiener channels retain
  actual-source-compressed cross norm at least `73/(375*pi) > 0.0619`
  cofinally.  Fixed-ratio separation does not make adjacent Cotlar terms
  vanish.
- Proved that channel atomization and regrouping leave `Z_a^* Z_a`
  unchanged.  A direct Cotlar row sum is not a new mechanism unless its full
  constant meets the original signed coverage budget.
- Proved the signed-primitive/Bernstein lower bound
  `q_a[f] >= -a Delta_a ||f||^2`, where `Delta_a` is the maximum negative
  signed interval area of the exact symbol.
- Proved this is the optimal scalar primitive budget: the least centered
  bounded-primitive norm is exactly `Delta_a/2`.
- Proved a structural obstruction in the nonnegative Dirichlet model with an
  exact null source: `a Delta_a = pi^3/6`, so positivity and perfect source
  alignment do not imply primitive decay.
- Non-rigorous arithmetic diagnostics at lambda `3,4,5,6` show no decay;
  they are not proof evidence.  The primitive candidate is therefore
  registered as rejected, not live.
- The existing signed weighted concentration inequality remains the live
  conditional even-sector mechanism.  Its cofinal arithmetic estimate and
  the odd sector remain open.  No G2 sign gap was closed and RH is not
  proved.

See `g2_primitive_transport/` and the persistent research log.

---

# Complete manuscript v1.33 revision notes

## v1.33 — concentration-product algebra and reciprocal-band no-go

- Derived the exact Toeplitz--leakage product and commutator identities for physical even concentration operators.
- Retained both rank-one terms created by compression off the actual repaired source, using the fixed first-slot-linear convention.
- Proved a cofinal obstruction for the manuscript's actual source: the source-compressed concentration operators for the nested reciprocal bands `[-1/(10a),1/(10a)]` and `[-1/(5a),1/(5a)]` have commutator norm with liminf greater than `9e-6`.
- The nonzero bound is analytic and rational. A separate degree-four verifier certifies the stronger lower bound `1.198e-5`.
- This rules out generic approximate simultaneous diagonalization from nesting, reciprocal scaling and source removal. It does not identify the test bands with the arithmetic superlevels and therefore does not refute the signed weighted mechanism.
- Recast the surviving target as one complete joint-channel norm bound. This is algebraically the v1.31 signed concentration inequality, not a new candidate; the manuscript explicitly avoids relabeling the v1.28 common-Gram idea.
- Primary-literature screening identifies the product algebra as classical Brown--Halmos/Widom theory. The actual-source cofinal obstruction is new within this project; worldwide novelty is not claimed.
- No G2 sign gap was closed and RH is not proved. The odd sector remains separate.

See `g2_nested_commutator/adversarial_nested_commutator_review.md`, `certify_scaled_commutator.py`, and the persistent research log.

---

# Complete manuscript v1.32 revision notes

## v1.32 — source-compressed Schatten refinement and no-go tests

- Proved the exact Hilbert--Schmidt identity for every source-compressed concentration operator and derived a sharper negative-level layer-cake bound.
- Proved by a scale-invariant Dirichlet model that the integrated negative-only operator, trace and Hilbert--Schmidt budgets need not vanish even when the complete form is nonnegative and the removed source is an exact null vector.
- Proved the interlacing obstruction showing that rank-one source removal cannot erase a second concentration channel.
- Upgraded the failure of global pointwise positivity at lambda 4 from a numerical observation to an exact rational enclosure: beta_(log 4)(1)<-3/5. This implies infinite negative index for the full-line multiplier but does not contradict positivity on the compact physical window.
- Proved that no nontrivial positive convolution kernel can be both a flat-top exact form-preserver and a genuine smoother. Any nontrivial form-exact flat-top kernel must change sign.
- Kept the signed source-compressed weighted concentration inequality as the live project-new even-sector mechanism. Its cofinal arithmetic estimate and the odd sector remain open.
- No G2 sign gap was closed and RH is not proved.

See `g2_schatten_no_go/g2_schatten_no_go_report.md`, the adversarial review, exact rational certificate and diagnostic scripts in the cumulative bundle.

---

# Complete manuscript v1.31 revision notes

## v1.31 — source-compressed weighted concentration

- Added a rigorous source-compressed time–frequency concentration operator for the exact even arithmetic symbol.
- Proved the negative-level layer-cake bound and the exact trace formula after even projection and source removal.
- Added a sharper finite/convergent weighted-superlevel criterion that retains favorable symbol mass and would imply the even v118 gap-free estimate with ordinary error tending to zero.
- Derived the exact two-level signed budget, showing why thickness of the merely nonnegative set and generic Logvinenko–Sereda constants do not suffice.
- Recorded numerical falsification diagnostics at lambda 3, 4 and 5 only. Packets centred at the deepest located negative wells retain positive complete energy, with independent Fourier and physical-space calculations agreeing to about 3e-10.
- Classified the mechanism as a project-new development of G2.6-CAP-01, not a new Schur, tail-metric or common-Gram construction. Classical concentration theory is credited; no worldwide novelty is claimed.
- The cofinal weighted concentration inequality and the odd sector remain open. No G2 gap is closed and RH is not proved.

---

## v1.30 — continuum cancellation and perturbative no-go

September 21, 2026 — complete working manuscript.

- Developed G2.6-CAP-01 through the exact PNT continuum kernel (e^{|x-y|/2}).
- Proved that the existing even cosh pole cancels the continuum kernel's harmful channel exactly; the positive remainder is the compact kernel (e^{-|x-y|/2}), so no spectral gap is imported.
- Derived the exact even Fourier symbol (\beta_a(\xi)=\Re\psi(5/4+i\xi/2)-\log\pi-\mathfrak r_a(\xi)), with the discrete-minus-continuum prime discrepancy explicit.
- Proved a six-bump prime-2 obstruction: the discrepancy is bounded below by (\log2/\sqrt2) on vectors orthogonal to any finite-dimensional removed block. It is not an (o(1)) ordinary perturbation.
- The surviving lemma is a support- and source-constrained lower bound for the full signed symbol. It must use physical uncertainty/concentration; the stronger pointwise symbol bound is numerically false at known positive windows.
- The odd sector and cofinal signed estimate remain open. No G2 gap was closed and RH is not proved.

---

# Complete manuscript v1.29 revision notes

September 21, 2026 — complete working manuscript.

- Added project-new candidate G2.6-CAP-01: an exact source-weighted nonlocal Picone transform for the inversion-even physical Weil form.
- Proved the killed archimedean-plus-prime jump decomposition with the correct logarithmic diagonal and exterior killing, and reduced the rank-one complement estimate to an explicit source-constrained capacity inequality.
- Screened the candidate by formula against all named prior mechanisms and primary literature. The transform is known mathematics; only the arithmetic target is new within this project. No worldwide novelty claim is made.
- Adversarial review corrected a false pointwise-supersolution shortcut and confined the result to the even sector. A finite lambda3 diagnostic falsifies the stronger shortcut but does not evaluate the complete physical endpoint action.
- The uniform capacity estimate, physical low-concentration block accounting, and odd sector remain open. No G2 gap was closed and RH is not proved.

See `g2_capacity_candidate/g2_capacity_candidate_report.md` and the persistent research log for the exact formula, novelty register, falsification attempt and remaining lemma.

---

# Complete manuscript v1.28 revision notes

September 21, 2026 — complete176-page working manuscript. New proofs:pages114–115; reproduction:page166.

- Tested the actual lambda = 5 signed dyadic blocks at the preregistered N=lambda^2=25.
- Certified positivity of all four diagonal blocks in each parity, but proved the norm-row comparison fails in both sectors. Exact comparison-eigenvalue lower bounds:1.539632 even and1.6014215 odd.
- Proved the obstruction persists under every smaller admissible positive block metric and every positive scalar row reweighting; uncomputed blocks cannot decrease the comparison.
- Replayed frozen witnesses at320/448 bits; all twelve coupling gates independently checked in signed Fourier coordinates.
- No complete lambda = 5 positivity margin or negative Weil direction is asserted. Other partitions, cutoffs and signed joint estimates remain open. Weak G1 and complete lambda = 4 positivity are unchanged; no G2/RH closure.

See g2_block_metric/block_metric_test_report.md and the persistent research log for the exact protocol, scope, reproduction and next target.

---

# Complete manuscript v1.27 revision notes

September 21,2026 —173pages — all72historical dispositions preserved.

- Rigid lambda = 5 transfer fails at the actual fixed tail metric in both parities. Finite-support interval counterwitnesses prove this on the complete tail; both unshifted Weil energies remain positive.
- Head or metric must change. No successful tuning rule, positive lambda = 5 tail/factors, or complete certificate margin is asserted. The full run stops at that prerequisite; no lambda = 8 calculation.
- New nonclosability proof rules out bounded sourceL2 transport through the fixed point-value repair. Physical G2.6 spaces are explicitly defined through finite image Grams; dimension and residual hypotheses are retained.
- New finite-rank obstruction shows polynomial-rank repairs cannot make the old unsigned diagonal comparison positive at polynomial cutoffs. A signed infinite-block metric criterion is proved as a conditional alternative; its Weil-specific uniform hypotheses remain open.
- Complete lambda = 4 positivity and weakG1 are retained. No G2 sign gap is closed; RH is not proved.

New proofs and definitions: pages112–117. New reproduction details: page164. Frozen parameters, witnesses, reports, analytic reviews and scripts are in g2_lambda = 5_transfer/ in the cumulative bundle. Every prior manuscript label is preserved, and the release uses explicit v1_27 filenames to avoid confusion with earlier bundles.

---

# Revision notes - full manuscript v1.26

September 21, 2026. Complete170-page working manuscript.

- Closed the remaining complete odd-sector sign at lambda = 4. The full form is now positive and its exact fixed-window negative error is zero.
- Proved a sharp subspace/complement inequality. Certified the entire fifteen-dimensional odd complement, then a same-head8192-support directional trial, giving the complete relative head bound107/250.
- Replayed the exact frozen directional witness at1024 and1280bits; independently verified the physical head with exact rational arithmetic and checked the argument adversarially.
- Derived a localized ordinary-error criterion for future windows, retaining the physical normalization cost on the unresolved block. Its cofinal decay is unproved.
- Preserved the unsuccessful trials and intermediate1e-43 lower error in the research log, with no negative Weil vector or growing-window conclusion inferred from them.
- Updated the complete paper throughout, retaining weak G1, all historical claims, the physical endpoint and explicit sampler graph defect.

This closes a fixed-window obligation. G2 uniformity and RH remain open.

---

# Revision notes - full manuscript v1.25

September 21, 2026. Complete166-page working manuscript.

- Certified strict positivity of the entire even-parity Weil form at lambda = 4, including every infinite residual row, using a simultaneous17-column frozen trial. The odd sector remains open.
- Certified complete generalized margin >0.62629 for the same witness at768/896bits. Coordinate LDL pivots are not identified with ordinary spectral gaps.
- Proved a joint-remote-Gram estimate retaining correlated residual terms; stated its required positive lower-Gram hypothesis explicitly after adverse review.
- Proved exponential cutoff cost for the current scalar far majorant and freshly certified its thresholds at lambda3,4,5,6,8.
- Recorded a separate finite-only growth study, condition numbers and declining margins. It does not supply missing complete tail certificates or a cofinal error estimate.
- Integrated abstract, status, proofs, next targets and reproduction appendix; preserved all496prior labels and72historical claim dispositions. Compiled and visually checked the full PDF.

One local complete even-sector sign obligation is closed. Full lambda = 4 positivity, growing-window G2 and RH remain unproved. Weak G1, physical endpoint, Fourier cut, logarithmic diagonal, scale factors and explicit sampler graph defect are preserved.

---

# Revision notes - full manuscript v1.24

September 21, 2026. Complete162-page working manuscript.

- Certified a positive value of the COMPLETE lambda = 4 Schur form on the unchanged archived even head vector:3.0930e-20<S_infinity(v,v)<3.2356e-20.
- Used a better frozen finite trial and a complete residual certificate, including all omitted rows. This does not equate finite iterative powers with full operator powers.
- Kept the previous first-degree failure results intact; their scope is the old majorants/trial, not the Schur form itself.
- Replayed the main16step and supplementary4step exact dyadic trials at768/896bits. Added dense-row and energy-identity checks, and completed adversarial proof/code review.
- Integrated the abstract, current status, proofs, future goals and reproducibility appendix; retained all490prior labels and72historical claims.

The saved one-direction test is closed. The full simultaneous even/odd head comparison and growing-window uniformity remain open; G2 and RH are not proved.

---

# Revision notes - full manuscript v1.23

September 21, 2026. Complete160-page manuscript. No G2 sign gap closed.

- Proved complete mixed-pairing enclosures including both omitted input and omitted first-polynomial output.
- Certified that the saved first-degree inverse majorant fails on the actual frozen lambda = 4 trial, even with its exact positive head update: lower6.6588e-20 exceeds trial6.4693e-20.
- Proved a monotone complete inverse refinement that retains the induced head matrix and a rigorous finite-probe enclosure of its improvement.
- Kept higher-degree finite-prefix successes in the research log, without asserting complete-tail positivity.
- Integrated the abstract, status, Section20, Section32 and reproduction appendix; retained all prior labels and72 historical dispositions.
- Replayed the exact witnesses at768/896bits and completed independent adversarial review. The fullPDF was compiled and visually checked.

Next target: degree4/8 complete corrections with certified remote excursions, then simultaneous whole-head sign and growing-window uniformity. No RH proof.

---

# Revision notes - full manuscript v1.22

September 21, 2026. Complete156-page working manuscript; no G2 sign gap closed.

- Proved sharper full far-inverse constants20even/90odd atlambda = 4, replacing67/335 for the same operator and weights.
- Proved finite-prefix scalar and matrix estimates with every omitted residual row enclosed.
- Certified a complete far-energy comparison on one previously obstructing even head direction: upper5.758e-20 is below trial energy6.469e-20. This does not include the structured mixed term or certify the entire head matrix.
- Proved that an improved inverse must replace both inverse occurrences in the structured bound, retaining the original finite certificate and closed form domains.
- Added the user's whole-head LDL acceptance test, requiring a form-order upper enclosure of the complete correction; no eigenvalue estimate is necessary.
- Integrated the abstract, current status, Section20, Section32 and reproduction appendix; preserved all72 historical claims and all prior labels.
- Checked constants at320/384bits and the exact same directional witnesses at768/896bits. Internal adverse review checked signs, parity/scale factors, complete remote terms and form domains.

Still open: refined mixed correction, simultaneous low-head Schur sign, and uniform estimates on growing windows. No RH proof or new global positivity claim.

---

# Complete manuscript v1.21 - September 21, 2026

The complete manuscript is 152 pages, with 32 main sections, two appendices, 466 unique labels and all 72 historical claim dispositions. All 454 prior labels are preserved. The abstract, status, main proofs, research goals and reproducibility appendix are updated together.

**Established locally:** Proposition 20.55 certifies K_X positive in both parity sectors at lambda=4, split16, for X=0 and the exact frozen dyadic trials supported on modes17..256. This establishes alpha4=0 for these complete-operator trial forms. Every pivot is interval-positive at768 and896bits with identical witnesses. These pivot bounds are not spectral lower bounds.

**Exact distinction:** Proposition 20.53 proves the finite-support compression identity, K_X-S_infinity=(X-T^-1 B)*T(X-T^-1 B), and S_infinity=S_M-r_M*T^-1*r_M for exact Galerkin solves. Finite Schur complements decrease to the full complement under nested form-core exhaustion. The semidefinite version states the required Ran(B) subset Ran(T^(1/2)) condition. The actual certified lambda = 4 tail is coercive.

**Certified correction to a proposed shortcut:** Proposition 20.42 constructs a unit even Fourier polynomial in E64 exactly orthogonal to the literal repaired source p3, with 0<QW3(v,v)<3e-31, non-prime energy>0.4 and signed prime energy<-0.4. Thus substantial cancellation persists on the exact source complement. This is a positive direction; it disproves neither complement positivity nor RH. The pure archimedean and pole contributions are separately identified.

**Dependency accounting:** Proposition 32.1 explicitly proves that complete cofinal Weil lower bounds -epsilon_j with epsilon_j->0 imply RH through fixed-support embedding and Weil positivity. This route bypasses the conditional Riesz realization; that realization remains open for the operator route. For the sufficient Schur criterion the needed rates are e_lambda->0 and t_lambda/sqrt(mu_lambda)->0, along with a justified head bound. Inverse approximation convergence alone does not force residual-energy convergence.

The final PDF compiles without warnings, undefined references or overflow. All152 pages were rendered and inspected, with detailed checks of the new proofs and tables. The mathematical integration passed internal adverse review. Both requested wording fixes about orthogonal compression and retained finite subspaces were applied. The literal Fourier cut, physical endpoint, logarithmic diagonal, first-slot-linear convention, sampler graph defect and previously proved weak G1 are preserved.

**Still open:** the complete low-mode Schur sign at lambda = 4 and uniform residual/sign estimates on growing windows. No G2 sign gap was closed, and no RH proof is claimed. No publication or outside contact occurred.

The cumulative evidence bundle adds g2_schur_cancellation with the verified witnesses, scripts, both precision replays, mathematical audit and integration review. Earlier evidence and revision history are retained.

---

# v1.20 Schur revision — September 21, 2026

The complete manuscript keeps the requested version1.20 label. This revision adds proved structured tail-inverse and finite-row estimates, a sufficient ordinary-error criterion with growing-dimension and congruence factors retained, and monotone arithmetic inverse polynomials.

At lambda = 4 the actual infinite far operators satisfy I<=D_g^(-1/2)U D_g^(-1/2)<=67I (even,n>512) and<=335I (odd,n>1536). The two-sided archimedean diagonal bound and correct pole scale justify these constants; strict gates replay at320/384bits.

The attempted low Schur sign did not close. Three candidate majorants have rigorously certified negative ceiling directions; those are failures of the bounds, not negative Weil directions. The research log and cumulative bundle retain all attempts and reproducible witnesses. The next target is the signed inverse-polynomial correction.

No growing-window G2 sign gap was closed; RH is not claimed. Weak G1, the physical endpoint, exact diagonal, sampler graph defect, all442 prior labels and72 historical audit dispositions are retained. New results are integrated in the abstract/status, main argument, research goals and reproducibility appendix.

---

# Complete manuscript v1.20 — September 21, 2026

The complete manuscript has143 pages,442 unique labels,32 main sections,two appendices and all72 historical claim dispositions. All431 prior labels and the physical endpoint, literal Fourier cut, logarithmic diagonal and sampler graph defect are retained.

**New signed estimate:** Proposition20.47 proves QW4(f,f)>=10^-8 sum(-A_n)|f_n|^2 for every complex closed-form vector with literal Fourier support|n|>16. The exact archimedean diagonal is positive there, with a proved lower bound>1.7940. The entire infinite tail in both parity sectors is included. This closes a larger fixed-window tail-sign obligation; it does not establish full lambda = 4 positivity or growing-window G2.

The certificate retains the actual prime,pole and archimedean entries. A positive physical weight gives a prime upper bound<4.624042316766478. Signed verified solves use heads17..512 and17..1536, with every residual through4096 and explicit infinite moment remainders. Frozen exact dyadic solve and congruence witnesses pass320-bit interval verification of every Gershgorin row. The same witnesses were generated at 256 bits; even256 was also replayed under the final gates. This is internal computer-assisted validation, not an outside referee check.

Proposition20.48 certifies a positive dyadic trial with energy/archimedean-energy ratio>2.05254. Thus the two-sided weighted remainder norm contraction fails even though the one-sided sign bound succeeds. It is not a negative Weil direction.

Proposition20.44 proves the sharp weighted-error conversion -eta*C/(1+eta), preventing a dimensionless error from being mistaken for the ordinary error required by G2. Proposition20.45 proves the weighted prime operator and the exact weighted remainder are compact but in no finite Schatten class; a whole-tail Frobenius budget is therefore invalid, while finite-column residual Grams remain valid. Proposition20.46 proves the sharp logarithmic weighted-tail asymptotic at fixed window, explicitly without a uniform joint-limit inference.

The abstract,status,Section20,research goals,reproduction appendix and bibliography are integrated. The PDF is compiled without warnings and visually reviewed throughout, including detailed new-proof checks. The cumulative bundle contains proof scripts, exact witnesses, interval reports, exploratory diagnostics, adverse review and the persistent log. The log records an early discarded pole-denominator coding error and the subsequent exact comparison and all-row gate corrections; no invalid intermediate is presented as a result.

**Remaining:** full lambda = 4 positivity requires the signed effective head F-B*T^-1*B on17 even+16 odd coordinates. Raw finite-matrix positivity is insufficient. Uniform signed control along growing windows remains RH-strength and is still open. No growing-window G2 sign gap was closed; no RH proof is claimed. No publication or outside contact occurred.

## Previous release: complete manuscript v1.19 — September 21, 2026

The complete paper has 139 pages, 32 main sections, two appendices, 431 unique labels and all 72 historical claim dispositions.

**New analytic obstruction:** Proposition 20.42 proves that the unsigned prime-shift norm is exactly unchanged by every finite-rank orthogonal source or Fourier-head removal. Its essential norm equals its ordinary norm; subtracting a compact operator, including the rank-two pole operator, cannot make the complementary norm smaller. The proof uses simultaneous phase recurrence and weakly null Fourier modulations, with no rational independence or operator-domain assumption.

**Sharp growth:** Proposition 20.43 proves ||T_pr||=(1+o(1))lambda, with the actual weights Lambda(m)/sqrt(m) and L=2log(lambda). A positive exponential-cosh weight gives an exact ratio; the unconditional prime number theorem and Chebyshev estimate sandwich its norm. The result remains true after any family of finite-rank orthogonal removals, however fast their ranks grow.

The consequence is limited to the paper's scalar place-by-place tail bound: subtracting the exact unsigned prime norm from the minimum logarithmic archimedean diagonal still requires an exponential cutoff in lambda. This is not a necessary cutoff for actual signed positivity. Frequency-weighted estimates and directional inverse-action bounds remain viable because the recurrence vectors may occur far above the cutoff, where their logarithmic energy is much larger. The paper's earlier broad wording about every scalable complement method was narrowed accordingly.

The abstract, status, Section 20, Section 32 research goals, reproduction appendix and bibliography are updated. The independent adverse review checks the compact-correction extension and scope. A non-certified numerical script checks the exact positive-trial autocorrelation and illustrates recurrence away from the first 64 Fourier modes. No numerical observation is used as a proof of a sign or asymptotic statement.

The full PDF was compiled without warnings and visually reviewed throughout, including detailed checks of new proof pages 89–90. All prior labels, ledger rows, physical endpoint and Fourier conventions, separate logarithmic diagonal and the corrected sampler graph defect are preserved. The cumulative evidence archive includes the new proofs, review, diagnostic, result, reproduction guide and persistent log.

**No G2 sign gap was closed.** The small unweighted complementary-norm shortcut is now ruled out. The next target is a frequency-weighted prime comparison retaining the increasing diagonal, or an independent signed arithmetic estimate along growing windows. Weak G1, fixed-window positivity and ground ordering, and the zero continuum endpoint remain unchanged. G2 and RH remain open. No publication or outside contact occurred.

## Previous release: complete manuscript v1.18 — September 21, 2026

The complete paper is 137 pages, with 32 main sections, two appendices, 423 unique labels and all 72 historical claim dispositions retained.

**Continuum endpoint resolved, with a correction to the proposed target:** Proposition 20.29 identifies the complete canonical Weil operator as one half of the restricted logarithmic Laplacian plus an explicitly bounded operator. Theorem 20.30 proves that every eigenfunction has a bounded representative with continuous zero physical boundary trace and inverse-square-root logarithmic boundary decay. This applies to every fixed window and every spectral level, without assuming RH or positivity.

The proof retains the exact scalar -log(2pi), both prime-shift orientations and both pole signs. A common-core argument establishes the closed realization before a simultaneous L2/L-infinity resolvent argument proves eigenfunction boundedness. Only then is the bounded-solution boundary theorem applied. Two independent internal reviews checked these gates.

Corollary 20.31 gives fixed-window Fejer endpoint decay and exact relative endpoint mismatch one between a complete eigenfunction and the repaired source's nonzero endpoint. Thus the proposed nonzero continuum ground-to-source endpoint comparison is false. It must not be pursued as a missing estimate. This is consistent with the retained ordinary overlap results and finite-compression endpoint calculations. It does not establish sharp Fourier endpoint convergence or joint finite-cut/window control.

Proposition 20.32 gives an explicit real even polynomial shell with physical endpoint one and Weil graph norm tending to zero. The physical trace is therefore not closable on that polynomial core in the operator graph norm. Eigenfunction boundary regularity is a separate property, not a consequence of graph convergence.

Proposition 20.41 proves the sharp complement estimate |q(f)-q((I-P)f)| <= (2/sqrt(3))||AP|| ||f||^2. A complementary lower bound -eta therefore gives a complete lower bound -eta-(2/sqrt(3))||AP||, without a positive complementary gap. The already proved rank-one source residual tends to zero; the arithmetic nonnegativity estimate on its entire complement remains unproved. A fixed negative compact test persists after source removal, so the desired cofinal sign remains RH-strength.

The abstract, status, Section 20, Section 32 goals, reproduction appendix and bibliography are integrated. The complete PDF was rendered and visually reviewed, with detailed checks of new proof pages 75–78 and 87–88. The final build has no warnings, unresolved references or overflow. All old labels and ledger rows are preserved. The evidence bundle adds the analytic derivations, primary-source audit, independent adverse reviews and a 90-decimal normalization diagnostic, which is explicitly not a proof certificate.

**Remaining:** growing-window G2 still needs an independent signed lower bound tending to zero, or a sufficient independent quantitative ground-space argument. Finite-compression endpoint control, uniform source-block residuals, the corrected sampler graph defect and full-strip obligations remain separate. No G2 sign gap was closed and no RH proof is claimed. No publication or outside contact occurred.

## Previous release: complete manuscript v1.17 — September 21, 2026

The complete paper is 132 pages, with 32 main sections, two appendices, 410 unique labels and all 72 historical claim dispositions retained.

**Closed an additional fixed-window obligation:** Proposition 20.27 proves that the complete canonical Weil operator at lambda=3 has a simple even ground state, with 0<mu0<3.644e-38 and mu1>1e-36. Every other even eigenvalue exceeds1e-34. Corollary 20.28 proves ordinary ground-angle sine less than .01931 for the exact normalized P64 p3. The earlier finite-matrix and new complete-operator angle bounds are carefully distinguished.

The proof applies signed interval LDL to lower Schur forms for W-aI, shifting every actual diagonal and every inverse weight. The same exact dyadic inverse-action witnesses pass at 768 and 896 bits: one negative and256 positive even pivots at a=1e-34, and512 positive odd pivots at a=1e-36. A separately certified finite-supported trial has full-form Rayleigh quotient below3.644e-38. That matching direction is essential: a negative pivot of a lower matrix alone does not prove a negative direction of the exact operator. Closed-form square completion, compact resolvent, min--max and prior complete positivity supply the spectral conclusion.

The source-overlap estimate uses the stronger even threshold and an exact finite correction of the rational trial. The v1.13 exact P64-source error transfers the angle by normalization geometry, with an additional error below4e-36. It does not transfer a tiny energy by an ordinary-norm perturbation estimate. No actual-ground endpoint control follows, and the earlier N64 relative endpoint error remains unchanged.

The abstract, status, Section20 proof, Section32 goals, reproduction appendix and bibliography are integrated. The full PDF was rendered and visually inspected, including new proof pages73–75. The final build has no warnings, overflow, or unresolved references. All old labels and all72 ledger dispositions are retained.

The cumulative reproducibility bundle includes the exact inputs, analytic dependencies, signed pivot enclosures, both precision replays, scalar and trial certifiers, internal adverse review and persistent log. A truncated prior ZIP was repaired from the valid older archive and intact v1.16 evidence verified against recorded hashes. The new archive is atomically completed and checked before saving.

**Remaining:** independently justified bounds along unbounded windows, with an error tending to zero or adequate quantitative ground-space overlap, are still required for G2. A larger physical-window block certificate is the next concrete test. Endpoint stability, uniform source-block control, the corrected sampler graph defect and full-strip obligations remain separate. No growing-window G2 gap was closed; no RH proof is claimed. No publication or outside contact occurred.

## Previous release: complete manuscript v1.16 — September 21, 2026

The complete paper is 129 pages, with 32 main sections, two appendices, 407 unique labels and all 72 historical claim dispositions retained.

**Closed fixed-window obligation:** Proposition 20.26 gives a computer-assisted proof of strict coercivity of the complete canonical closed Weil form at lambda=3. Both complex parity sectors and the entire infinite Fourier complement are included. This strengthens the earlier finite-matrix certificates; it does not close growing-window G2 or prove RH.

The proof combines four supported improvements. Proposition 20.22 uses the positive physical weight cosh(x-log3) to reduce the prime-shift norm bound to 2.6890557719..., with all endpoint comparisons certified. Proposition 20.23 retains the increasing tail diagonal and proves inverse order. Proposition 20.24 bounds every remote residual row using exact Fourier moments and a controlled geometric remainder. Proposition 20.25 combines these with the complete signed Schur identity.

For the even sector the head has 257 dimensions, N = 256/M512/J = 4096/r80. For the odd sector it has 512 dimensions, N512/M1024/J = 4096/r100. All finite rows and the infinite remote moment Grams are included. Every pivot of each final interval LDL decomposition is strictly positive. The witnesses are exact frozen dyadic matrices, and their middle residuals are explicitly retained. Independent replays at 896 bits using the identical witnesses reproduce both 768-bit certificates. The reported pivots are not spectral lower bounds; the paper asserts existence, without a numerical value, of a positive complete-form coercivity constant.

The abstract, status, Section 20, Section 32 research goals and appendix are integrated. New material is on pages 67–73, with the reproduction summary on 124. All 129 PDF pages were rendered and visually reviewed, including detailed inspection of the new proof pages. The complete LaTeX build has no warnings or unresolved references. The historical 72-row ledger is unchanged apart from its release heading.

The cumulative bundle retains prior audit/reproducibility material and adds the new proofs, scripts, interval outputs, both exact witnesses, precision replays, internal adverse review and research log. Exploratory failures of weaker sufficient bounds are recorded as failures of those bounds, never as negative Weil-form results. No publication or outside contact occurred.

**Remaining:** a lower error tending to zero along an unbounded window sequence, or sufficiently strong independent ground-space overlap, is still required for G2. At the fixed window the next concrete certificate can use W-aI to establish ground-state ordering and parity, with both diagonal and tail weights shifted consistently. Source-to-ground endpoint stability, the corrected sampler graph defect and full-strip obligations remain separate. Earlier weak G1 and ordinary source-residual results are unchanged. No RH proof is claimed.

## Previous release: complete manuscript v1.15 — September 21, 2026

The full manuscript is 123 pages, with 32 main sections, two appendices, 392 unique labels and all 72 historical dispositions retained.

**Closed prerequisites:** Lemma 20.27 proves a nonzero ordinary L2 limit of the exact repaired source and its polynomial Fourier projection. Proposition 20.28 proves their actual full semilocal Weil operator residual is O(lambda^6 exp(-2*pi*lambda^2/3)). Their ordinarily normalized Rayleigh values and centered residuals therefore tend to zero. This uses the existing uniformly quantified Sobolev G1 and Fourier coefficient-tail results, with a new output split. The exponentially large auxiliary output cutoff does not change the actual polynomial source cutoff. No effective threshold at lambda=3 is asserted.

**Sharper infinite complement:** Proposition 20.21 retains the weighted degree of physical prime shifts, the decaying negative pole Fourier tail, and the limiting archimedean commutator. At lambda=3 the complete omitted Fourier complement beyond N=256 is bounded below by 0.0148 times the norm squared; the even complement has bound 1.5867. The exact scalar evaluations were enclosed with 256-bit Arb arithmetic and independently rerun. This is not a certificate for the remaining finite head or its Schur correction.

**Remaining G2 target:** Equation 181 keeps the exact signed Schur complement and improves its verified-solve bound by retaining the residual Gram matrix R*R/Gamma before taking a scalar norm. The sign of this corrected finite head remains open. The revised overlap calibration now uses proved source residual/Rayleigh inputs, but still requires an independent quantitative lowest-eigenspace overlap. Tiny residual alone does not exclude a negative level orthogonal to the source. No G2 sign gap or RH proof is claimed.

The source, first-slot-linear convention, physical endpoint, Fourier cut, logarithmic diagonal and corrected sampler graph defect are preserved. The new ordinary residual does not become a small endpoint-normalized residual and does not control a growing prolate block. Source-to-ground endpoint stability, graph/full-strip comparison and the alternative arithmetic shell sign remain separate obligations.

The abstract, status, Section 20, Section 32 and appendix are updated throughout. The main additions are on pages 65–68 and 73–76; the scalar certificate summary is on page 118. All pages were rendered and reviewed, with close inspection of the new proof pages. The final LaTeX build has no warnings, unresolved references or overfull/underfull boxes. The bibliography was compacted to avoid a one-entry final page. The historical ledger is unchanged apart from version headings.

Two internal reviewers checked the new operator residual; the tail constants and parity were separately audited. This is not external referee verification. The bundle preserves all earlier evidence and adds the derivations, proof inserts, review reports, interval checker and output, and the v1.15 reproduction guide.

Next: a directional inverse-action certificate for the lambda=3,N=256 head and its infinite complement, retaining the full error Gram matrix. A proof of G2 additionally needs growing-window lower control.

## Previous release: complete manuscript v1.14 — September 21, 2026

The full manuscript is 119 pages, with 32 main sections, two appendices, 376 unique labels, and all 72 historical dispositions retained.

**New analytic results:** Propositions 20.19–20.20 identify the canonical semilocal Weil operator and Fourier core through an exact diagonal-plus-bounded-commutator representation, and give an explicit positive high-frequency complement. Lemmas 21.5–21.6 and Proposition 21.7 prove physical-endpoint recovery with relative error O(1/lambda) at the original ordinary cutoff N=ceil(lambda^8(1+2log lambda)). Corollary 21.8 establishes weak G1 on the same finite vector, using a separately proved coefficient-tail bound. The asymptotic cutoff threshold is not numerically certified at lambda=3.

The operator theorem concerns the semilocal Weil operator, not the conditional arithmetic generator of Section 18. Its fixed-window BV graph convergence does not erase the corrected sampler's graph defect. The tail theorem uses an expensive unsigned arithmetic estimate; a scalar Arb check proves Gamma_(3,50000000)>1.0797, without assembling that matrix or certifying the low modes.

The remaining signed effective low block is stated exactly as F-B* T^(-1)B, with an inverse-action residual certificate. Its growing-window lower bound is open. The source endpoint theorem does not imply endpoint stability of a ground-state approximation. The new proofs close prerequisites, not G2 or RH.

Two internal reviews independently audited endpoint recovery; the operator/core proof and weak-G1 consequence received separate checks. The adverse report rejects fixed positive complement gaps after removing finitely many radical sources, unsigned fixed arithmetic perturbation bounds, and generic Perron reasoning as substitutes for the required signed arithmetic estimate. The supplied research reports preserve these distinctions.

The abstract, status, Sections 20–21, Section 32 goals, appendix scope and assistance disclosure are updated consistently. New proofs appear on pages 63–65 and 81–84, and the scalar check on page 113. The PDF was compiled and all pages visually reviewed, with close inspection of new material. No LaTeX warnings, unresolved references, overflow/underflow messages or duplicate labels remain. The historical ledger is unchanged apart from version headings.

The cumulative reproducibility bundle preserves the prior material and adds the analytic derivation, source audit, adversarial and independent reviews, proof excerpts, scalar checker and intervals, and a reproduction guide under g2_deep_next/.

**Still open:** the independent arithmetic G2 sign, uniform growing-window spectral control, source-to-ground endpoint/strip normalization, growing-source-block operator estimates, and the corrected graph pairing. No G2 sign gap is claimed closed.

## Previous release: complete manuscript v1.13 — September 20, 2026

The complete manuscript is now 111 pages, with 32 main sections, two appendices, 354 unique labels and all 72 historical claim dispositions preserved.

**New in v1.13:** Lemma 20.26 proves a rigorous angular eigenfunction error bound using an infinite-tail inertia comparison, the full residual and a graph-norm pointwise estimate. Proposition 20.27 identifies the exact repaired prolate source at lambda=3,N=64 with the previously certified finite candidate to coefficient error below 2.60e-36. Its normalized angle sine to the actual finite Weil ground state is below 0.000216. This closes the fixed-window exact-source identification prerequisite.

**A separate certified limitation:** the exact projection's relative physical-endpoint error is strictly between 1.374 and 1.375. The endpoint mismatch is therefore established for the exact source, beyond the earlier numerical pilot. It does not contradict the ordinary-norm angle bound. Endpoint recovery still needs a suitable cutoff or shell with all graph terms included.

The verifier includes the omitted angular Legendre link, exact modal normalization, source integral coefficients, the complete moment repair and strict interior endpoint. A proved bound ||psi||_infinity<=129 replaces any numerical assumption about the bump integral ratio. Exact polynomial Mellin moments are enclosed with Arb. The input candidate and prior finite Weil result are linked by hashes and parameter checks. The new certificate depends explicitly on that earlier finite matrix proof.

The source and proof are in Section 20, pages 71–73; full verification details are on pages 105–106. The abstract, current status, research goals and assistance disclosure are updated throughout. All 111 PDF pages were rendered and inspected; title/new-result pages received a separate close review. No LaTeX warnings, undefined references or overflow/underflow messages remain. The historical ledger is unchanged apart from its version headings.

**Still open:** a uniform arithmetic G2 estimate, growing-window residual/complement control, the omitted Weil Fourier complement, relative endpoint recovery, and the required graph/full-strip transfer. The angular tail controlled by this certificate is not the omitted Weil complement. Weak G1 is unchanged. No RH proof is claimed.

The cumulative bundle retains every prior audit and script and adds `g2_source_certificate/`, containing the input vectors, optional generator, rigorous verifier, interval outputs and `G2_Exact_Source_Certificate.md` reproduction guide. The adversarial reviewer found no blocking error after checking the argument, code and outputs, but did not rerun the certificate; no external referee verification is claimed.

## Previous release: complete manuscript v1.12 — September 20, 2026

The complete manuscript is 108 pages, with 32 main sections, two appendices and all 72 historical claim dispositions. The full source and PDF have been regenerated and visually checked.

**New in v1.12:** Proposition 20.25 proves the inverse-weighted finite spectral certificate, including a matrix/solve error budget. Proposition A.1 certifies the actual 129-dimensional arithmetic Weil matrix at lambda=3,N=64 using two interval calculation paths. Its lowest eigenvalue lies strictly between 3.64e-38 and 5.32e-38, its ground state is simple and even, and the sine of its angle to the explicitly frozen rational candidate is below 0.000216. The complement above that candidate's Rayleigh quotient exceeds 1e-34.

One implementation uses certified integration and a parity/Householder complement; the second uses an exact archimedean digamma/trigamma expansion with explicit tails and a rational full-space complement with its Gram matrix. Both use rigorous Arb arithmetic, not approximate eigensolver output. The exact candidate file, certifier scripts, interval outputs and reproduction instructions are in `g2_certificate/` in the cumulative bundle. These are independent calculation paths using the same arithmetic library, not independent software or external referee verification.

**Limits:** The candidate is defined by exact rational coefficients derived from an earlier numerical approximation. The result does not certify its proximity to the exact prolate source, omitted Fourier directions, growing windows, relative physical-endpoint recovery, graph transfer, G2 or RH. Weak G1 is unchanged. The original sampler's graph defect remains explicit. The next local task is certified true-source coefficient/projector error with a separate endpoint budget; the central uniform arithmetic inequality remains open.

New proof pages: Proposition 20.25 on page 71, Proposition A.1 and its two verification paths on pages 101–102, endpoint and scope limitations on page 103. The abstract, current status and Section 32 research goals are updated consistently. All 108 pages were rendered and visually reviewed; 343 labels are unique, references resolve, and the final build has no LaTeX warnings or overflow/underflow messages. Earlier proofs, numerical illustrations, audit materials and research attempts are retained.

## Previous release: complete manuscript v1.11 — September 20, 2026

The deliverable is a complete 105-page working manuscript by Alexander Eastwood, with a standalone LaTeX source, 32 main sections, two appendices, and an integrated ledger accounting for all 72 numbered results in the previous r11 manuscript. It is not a claim of an RH proof or a publication-ready certification.

**New in v1.11:** Lemma 9.1 proves L2 convergence of an integral-corrected co-Poisson cutoff with error `V(h)sqrt(b/M)` and shows that the uncorrected integer sum instead has a positive sqrt(M) divergence for every nonzero zero-integral compact source. Proposition 9.2 constructs its arithmetic adjoint in local H^-1 and proves the exact local characterization `y in Q_R iff A y=A_y+B_y/t` for `y in H_R`. It includes exact dilation covariance and a normalized growing-interval error budget. Corollary 9.3 supplies controlled finite source-Gram approximation, without claiming inverse convergence. New proofs are on pages 14–16. A Mellin-power check recovers the zeta zero condition but yields no independent sign. The infinite-source pairing prerequisite is closed; G2 and RH remain open.

`check_copoisson_adjoint.py` and `copoisson_adjoint_checks.json` provide 45-digit finite identity checks, including a complex first-slot-linear pairing, for a piecewise-polynomial two-moment source. These are not certified arithmetic evaluators, inverse bounds or RH evidence. The complete paper, status, research goals and numerical appendix are updated; all earlier results and historical audit files are retained.

**New in v1.10:** Lemma 8.1 retains the signed Fredholm cross term and resums the constant-kernel contributions into three scalar moments, with explicit error `4 pi^2 a^5 H_a/[5(1-2a)^2]`. Proposition 8.2 proves that both this error and the full moment correction vanish relative to the evaluator norm for each fixed off-line zero, without Assumption 2.1. Its elementary upper bound follows from the compact physical support and Mellin reflection; its lower bound is just nonzero nested evaluation. This closes a normalization prerequisite, not the signed G2 estimate. The remaining target is the leading shell-energy sign at the single prime 2. The new arguments are on pages 11–12, and the abstract, assumption discussion, goals and numerical appendix are updated together. The full critical-line, sharp lower-growth and projection-error assumptions are not discharged.

`check_fredholm_shell.py` and `fredholm_shell_checks.json` add 48-/80-node cosine-kernel Nyström convention checks. Their interval profiles are not asserted to arise from Sonine evaluators. Exact algebra discrepancies are below `7.50e-16`; no numerical or RH certification is claimed. The research log records the failed attempt to extract a new moment sign merely from the already vanishing three-range/sieved source pairings, and specifies the next independent arithmetic target.

**New in v1.9:** Lemma 19.11 proves a local L2 synthesis bound for decaying zero coefficients using the unconditional unit-interval zero count. Proposition 19.12 upgrades the full-strip transfer to norm-level control of the actual finite Weil action, with the stronger fixed tail condition p>1. Corollary 19.13 computes the positive squared-Weil metric S W^2 S: mass grows on top roots, while lower jets at a multiple zero lose unscaled coercivity. The exact signed budget remains, and the independent G2 estimate is not closed.

**New in v1.8:** Proposition 19.9 constructs a projection in the full expanding Fourier space that annihilates the source and both endpoint-shell graph directions exactly, retains a positive lower bound on each fixed root space, and preserves Weil transfer. A new full-strip error bound, including endpoint jumps, provides the summable zero-product majorant. This closes a transfer sub-obligation for the revised projection; it does not repair the sharp fixed-band projection. Corollary 19.10 shows that a fixed scalar shift of the resulting projected Weil form still has a nonvanishing relative Lyapunov defect under the hypothetical off-line-root setup. The independent signed G2 estimate remains open.

**Current result:** Theorem 20.1 replaces the remaining G1 source/domain assumption with a proof. Weak G1 is now established for the explicit repaired source: fixed physical bands, periodic Sobolev pairings and the stated deterministic finite transfer. Growing-block operator-norm estimates, the economical-cutoff improvement, G2 and RH remain open. The explicit sampler graph defect is unchanged.

**Section 19 update:** Theorem 19.2 gives a finite-core metric criterion without the global closed-operator or evaluator assumptions. Proposition 19.3 constructs a positive metric that is coercive on each fixed root space and exactly annihilates the zeta source and endpoint-shell graph defect. Proposition 19.4 computes the remaining rank-two commutator and its positive variance limit; Proposition 19.5 proves that removing increasingly many source derivatives by bounded fixed-band projections destroys coercivity. This bypasses a foundational dependency and rejects a tempting metric repair, but does not close the G2 compatibility estimate.

**New in v1.6:** Lemma 19.6 and Proposition 19.7 prove that the sharp physical band cut used by that projection creates exponentially growing off-line transforms, despite bounded ordinary norms and exact source orthogonality. Thus the earlier bounded holomorphic-strip transfer cannot be applied to the projected vectors without a new argument. This does not prove divergence or negativity of the complete Weil form: its signed prime, pole and archimedean terms may cancel. No G2 gap was closed.

**New in v1.7:** Proposition 19.8 computes the contribution of one functional-equation-reflected zero pair to the sharp-band zero-side formula. Unless an explicit product of the two frequency-edge coefficients vanishes, reflection produces an exponentially large oscillatory real term; it does not cancel the cut growth. The proposition is deliberately pairwise. It does not control the entire zero sum or prove a sign/divergence statement for the complete Weil form. No G2 gap was closed.

The starting source was `fixed_space_prime_action(20260920-060548).tex` (SHA-256 `84dd52131cd2c64e9df6420f51de2bc58bc89f5340b78d15ad9160659717ad14`). The supplied audits and earlier versions were used as material to check. Original uploads were not overwritten.

| Previous coverage | Location in v1 | Revision |
| --- | --- | --- |
| Sections 1–11: fixed compression, source covariance, Fredholm shells, projections, prime sieve | Sections 1–11 | Retained and corrected; diagonal positivity distinguished from full-span positivity, synthesis range replaced by its closure, cutoff renamed R. |
| Sections 12–16: leakage, generator, boundary theory | Sections 12–16 and new lemmas in Section 2 | Compact Mellin division and finite-jet density supplied; off-line hypotheses and the skew-extension sign corrected; quantitative evaluator inputs made explicit. |
| Sections 17–19: calibration, resolvent, metric comparison | Sections 17–19 | Missing evaluator and closed-operator inputs stated as assumptions; unsupported certified-nonorthogonality claim removed. |
| Section 20: prolate source and G1 | Sections 20–21 | Source normalization and uniform correlation obligations exposed; correct diagonal and older weighted-sampler/jump estimates restored; Rayleigh, domain, Schur-sign, and cutoff-quantifier issues corrected. |
| Section 21: original sampling transfer | Sections 22–27 | Replaced by centered transfer with boundary terms, an explicit raw-cut defect, and an exact endpoint repair on the same finite matrix. |
| Section 21: downstream G2 and arithmetic routes | Sections 28–31 | Graph defect retained in all rebuilt identities; corrected reflected top-root lower bound; exact arithmetic beta formula retained; unsupported pole-aware and beta-limit claims withdrawn; phase/filter/exact-matcher claims scoped. |
| Sections 22–23: criterion and conclusions | Section 32 | Rewritten research goals and remaining obligations. |
| Numerical checks and claim tracking | Appendices A–B | Finite illustrations, limitations, and all 72 historical claim dispositions. |

The central result is that a centered sampler plus a high-frequency endpoint correction preserves the physical endpoint, ordinary norm limit, and Weil-form limit on one explicitly defined finite matrix. The correction adds a graph defect with unavoidable derivative growth. The weaker arithmetic pairing of that defect remains open; it is included in the downstream formulas rather than discarded.

Remaining obligations include the quantitative evaluator estimates, a complete closed arithmetic operator realization for the Riesz-window formulation, growing-block residual control, and the corrected graph and meromorphic-test pairings needed for positivity transfer. The formerly proposed bounded endpoint ratio is now disproved for the corrected sampler under the hypothetical off-line-root setup; a replacement test construction is needed.

Version 1.1 added four results, retained in Section 28: the corrected resolvent endpoint asymptotic (Lemma 28.5), uniform resolvent Gram bounds (Lemma 28.6), divergence of the old endpoint ratio (Corollary 28.7), and loss of the reflected signal for bounded endpoint-zero resolvent tests from any fixed admissible finite input space (Theorem 28.8). The new theorem uses holomorphic form transfer only and does not depend on the withdrawn pole-aware Weil transfer. It limits one G2 strategy; changing test spaces or different endpoint corrections remain possible but need new estimates. The abstract, continuum-ratio discussion, goals, numerical appendix, and claim ledger have been updated accordingly.

The `RH_G1_G2_research_log.md` records successive checkpoints and concrete next targets. `check_resolvent_endpoints.py` and `resolvent_endpoint_checks.json` supply a rational-transform check of the endpoint mechanism, with no inserted zeta zeros and no Weil-form computation. G1 and the full G2 argument were still open at the v1.1 checkpoint.

Version 1.2 added Lemma 20.4, Proposition 20.5 and Corollary 20.6: a two-sided endpoint/exterior-energy comparison, an explicit two-mode normalization proving endpoint noncancellation and a superpolynomially small value-at-zero ratio, and the lower-tail size of the exact value-and-integral repair. These use classical fixed-order PSWF results, not any RH hypothesis. `check_prolate_source.py` and `prolate_source_checks.json` provide high-precision Legendre-Galerkin illustrations with a larger-dimension comparison; no interval or infinite-dimensional error certification is claimed.

Version 1.3 adds Corollary 20.9 and Lemma 20.10 (pages 37–39). The actual repaired source now has a proved inversion-even endpoint comparison, including one-sided traces when `lambda^2` is an integer. A distribution-level zero-extension calculation proves the uniform two-sided correlation derivative and both translated endpoint terms. A sharp `H^1` translation estimate shows that the archimedean numerator is generally only Hölder `1/2` at the origin because of endpoint strips, but this still integrates against the `O(1/x)` kernel and supplies the required uniform local bound. These results remove the correlation, endpoint-comparison and local archimedean items from Assumption 20.1. The remaining assumption is the global radical/closed-form-domain passage. The standard Schwartz radical theorem cannot be applied verbatim because the compact source has a nonzero one-sided endpoint; a naive taper would erase the normalizing boundary channel. G1, G2 and RH remain open.

Version 1.4 adds Theorem 20.1 (pages 31–33), replacing Assumption 20.1. Euler summation isolates a mean-zero endpoint sawtooth; its logarithmic primitive gains one power of decay. Correlation against a compact BV test then makes the prime series and pole terms separately absolutely convergent. Moment-preserving multiplicative smoothing passes the classical Schwartz radical identity to the actual compact source. Uniform BV and logarithmic Fourier weights justify the semilocal form domain. The approximation is at fixed cutoff before normalization; it need not preserve the endpoint of each approximant. This corrects v1.3's overly restrictive approximation requirement. Lemma 20.10 also now calls its interior-test derivative `bulk`, because its translated endpoint terms belong to the full absolutely continuous derivative as well.

The resulting continuum estimate (114), Sobolev Proposition 20.13 and fixed-band finite closure Theorem 20.23 are now proved for the repaired source, with no remaining source assumption. The whole manuscript, weighted-sampler consequences, goals and historical claim ledger have been updated. `check_bv_radical_passage.py` and `bv_radical_passage_checks.json` add a 70-digit toy-source convention check, not proof evidence or an RH experiment.

Version 1.5 integrates these four Section 19 results into the whole manuscript (new arguments on pages 30–33). The criterion uses the relative defect `||GB+B*G||/c_n`, so a collapsing metric cannot pass by rescaling alone. The corrected sampler itself and its exact physical endpoint are retained; only the metric is changed in the new benchmark. It uses analytic samples of `kappa zeta`, not a zero list, and is not asserted to be a finite-prime Weil metric. The abstract, status, Section 28 interface, research goals and ledger distinguish this reduction from a proved small Lyapunov defect. The global Riesz realization remains unproved for statements that specifically use it.

`check_section19_metric.py` and `section19_metric_checks.json` test nine complex/Jordan finite identities and the polynomial-resolvent remainder with a rational source. All nine discrepancies are below `2.1e-15`; the model eigenvector-relative defect stays at `2 Re(mu)=0.46`. No zeta zeros or Weil matrix enter the experiment, and no certified numerical or RH conclusion is inferred.

Version 1.6 adds the exact sharp-band transform and its alternating-sum edge expansion (Lemma 19.6), followed by the source-projection obstruction (Proposition 19.7), on pages 34–35. At any fixed pair `s=1/2 +/- b`, at least one endpoint coefficient is nonzero for a hypothetical off-line first root vector, provided the two frequency edges avoid zeros of `kappa zeta`. The corresponding transform grows like `exp(b L/2)/L`; b may be chosen strictly below 1/2. The full-strip limitation is kept separate from the still-open signed Weil product estimates. The abstract, status, Section 28 interface, goals, numerical appendix and ledger version heading are updated. The original sampler, physical endpoint, Fourier cut, logarithmic diagonal and graph defect are unchanged.

`check_band_cut.py` and `band_cut_checks.json` add rational-source checks of the exact second-difference formula and independent physical quadrature. Their discrepancies are below `2e-15` and `1e-14`, respectively. No Weil matrix or zeta zero is used. The next target is a combined finite prime/pole/archimedean estimate for the compressed correction, not an inference from the separate pole growth.

Version 1.7 extends the sharp-band analysis on page 36 by retaining both first-slot-linear reflected summands. If `v=d+i gamma`, the leading pair term is `-m exp(dL)/(2L^2) Re(exp(i gamma L) C_a(v) conj(C_a(-conj(v))))`. Its proof tracks the minus sign from `sinh(-conj(v)L/2)` and the squared centered edge phase. The exceptional case of a zero endpoint product is retained. The rational-model check now runs through N=256 and finds about 1.47 percent relative error between the exact pair product and sampled-edge leading expression there; this is not a zeta or Weil-form experiment.

Version 1.8 adds Proposition 19.9 and Corollary 19.10 on pages 37-38. With Q0 the orthogonal complement of span{c,Dc}, u=Q0 z and S=Q0-u u*/||u||^2, the entire corrected graph source is annihilated exactly. For R>=3 and K>=ceil(exp(2L)L^4), the centered projected transform differs from H_F-alpha_L(F)H_zeta by at most C[exp(-(p-1/2)L/2)+L exp(L/4)(1+K/L)^(2-R)]/(1+|Im s|) throughout the closed critical strip. The source subtraction leaves all zero values unchanged, so the complete Weil limit transfers. A fixed positive scalar Weil shift is coercive on each one-sided root space but fails the small signed metric criterion. All commutator terms and the original graph defect remain explicit.

`check_full_projection.py` and `full_projection_checks.json` test eight finite identities and a strip grid using holomorphic rational model outputs, with no zeta zeros or Weil matrix. Algebra discrepancies are below 4.2e-14; the strip-grid error decreases from about 0.02043 to 4.121e-6 over the sampled lengths, while the eigenvector-relative defect remains 0.46. The tractable numerical cutoff is smaller than the theorem cutoff. The model bound scale uses a strict admissible tail rate p=1. These checks neither certify the full strip nor constitute evidence for RH.

The v1.8 integration also corrects wording that treated equivalent arithmetic and zero-side representations as additional canceling contributions. The abstract no longer suggests an unproved generic nonvanishing statement for the actual endpoint product. Shortening the title material removes the nearly empty page caused by the prior reading-conventions overflow.

Version 1.9 adds the norm-level results on pages 39-41. The synthesis estimate is C epsilon sqrt(A+1) exp(A/2), including multiplicities without a zero-separation hypothesis. Applied at A=L/2, it gives action error C sqrt(L+1) exp(L/4) epsilon_(L,K), which vanishes for p>1 and the existing exponential cutoff. The root signal is the finite sum of H_F(rho) exp((rho-1/2)y). Top-root mass in S W^2 S is asymptotic to |C_rho|^2 sinh(|Re(mu)| L)/|Re(mu)| off the line and |C_rho|^2 L on it; lower-jet mass tends to zero. The original graph defect and every term of the squared-metric commutator remain explicit. The full-space projection statement now explicitly includes genuine critical-line root chains, whose transform poles cancel.

`check_weil_action.py` and `weil_action_checks.json` use the actual finite arithmetic Weil matrix and the first known critical-line zero. At K=256, relative action errors for L=4,6,8,10 are approximately 0.057219, 0.014045, 0.0021459 and 0.00068992. The script also tests K=128, direct physical quadrature of the target Fourier coefficient, and 400 additional quadrature nodes for the final matrix action. These cutoffs do not attain the theorem scale. This is a floating-point convention check, not a root/multiplicity certificate or RH evidence. The zero-count input is cited to Trudgian, arXiv:1208.5846v2, Corollary 1.

To build the manuscript:

```sh
latexmk -pdf -interaction=nonstopmode -halt-on-error fixed_space_prime_action_v1.tex
```

The source is self-contained and requires no external figure files or bibliography database. Standard LaTeX packages used include amsmath, amsthm, mathtools, mathrsfs, microtype, booktabs, longtable, hyperref, and lmodern.

To reproduce the finite checks, install NumPy, SciPy, and mpmath and run:

```sh
python check_sampler.py
python verify_finite_identities.py
python check_resolvent_endpoints.py
python check_prolate_source.py
python check_bv_radical_passage.py
python check_section19_metric.py
python check_band_cut.py
python check_full_projection.py
python check_weil_action.py
```

`sampler_checks.json` contains the previously executed finite sampler illustrations and quadrature comparison. `finite_identity_checks.json` contains nine previously executed complex-vector algebra checks for the corrected finite identities. These are floating-point checks, not certified interval estimates or substitutes for proofs.

Validation: the PDF compiles with all references resolved, no duplicate labels, and no LaTeX overflow/underflow warnings. Rendered inspection covers the full 100-page manuscript and higher-resolution views of the new Section 19 argument. `v1_validation.json` records the final source/PDF hashes and validation scope.

The bundle includes the final PDF, standalone source, this revision record, the research log, reproducibility scripts and results, the final validation record, and the three historical audit documents in an `audits/` folder. Historical audits describe their own review stage; the integrated v1 ledger gives the current disposition of each claim.
