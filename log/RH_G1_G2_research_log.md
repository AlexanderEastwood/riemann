# v1.42 — NS-17 integration and PR preparation, September 21, 2026

## v1.62: divisor feedback and the continuous relaxation (NS-75–77)

Cancelling the actual residual's next derivative jumps is exact locally,
but its held-old unit step increases the full error on all five checked
blocks. At N=256 its optimized three-direction span captures **56.02%** of
full gain, versus **97.63%** for curvature. This is a finite control, not
an asymptotic exclusion of all arithmetic feedback.

The continuous-dilation relaxation has an exact distance formula in terms
of the classical unknown inner factor. Its closure is strictly larger than
the integer closure; a certified explicit witness separates the two.
A complete positive zero-tail budget, combined with published finite-height
zero verification, gives continuous squared distance **below 2.08e-32**.
This is not an upper bound for integer error, a new zero verification, or a
proof of zero distance. The original cofinal arithmetic input remains open.

[Readable update](../evidence/v162/research-update-2026-09-23-v1.html) ·
[Proofs and complete finite replays](../evidence/v162/).
No new Weil window, uniform floor, G2 or RH proof.

Validation: `evidence/v162/validation.json`; local self-review only.


## v1.61: local geometry and an arithmetic control (NS-72–74)

The repaired model has an explicit positive differential energy. Its
numerator is uniformly comparable to a discrete curvature energy, yielding
an O(N) coefficient rule once the actual residual correlations are known.
At N=256 the diagonal curvature rule captures **97.63% of the full block
gain**, an **8.13% reduction of squared error**, versus the optimum's 8.33%.
The best combination of three prescribed Mobius/log-taper templates captures
83.66%; these finite comparisons do not exclude other arithmetic formulas.

An explicit unitary altered family has identical complete Gram matrices
and arbitrarily close finite efficiency statistics, but an unconditional
positive approximation floor. This is a control on the inference from
finite geometry, not an off-line zeta zero or a floor for the original
family. The original cofinal arithmetic numerator/cost estimate remains open.

[Readable update](../evidence/v161/research-update-2026-09-23-v1.html) ·
[Proofs and complete finite replays](../evidence/v161/).
No new Weil window, uniform floor, G2 or RH proof.

Validation and the complete scope are recorded in `evidence/v161/validation.json`. Local self-review only; no independent review is claimed.


## v1.60 local draft — complete cancellation and selected directions (September 23, 2026)

Version 1.60 local draft (NS-67–71) gives complete canonical cells and
an O(log N) tail beyond N^2, retaining the exact growth criterion.
Centered complete Abel terms have conditioning at most 1+2*||sigma_1||<4.617;
whole-term cancellation cannot change the power exponent. Positive renewal
transfers the same forcing power; its critical weighted total energy is
unconditionally infinite, not the canonical norm itself. The actual optimized
endpoint remainder exceeds its model at N=64,128. Repairing the elementary
Gram cusp subtracts d/max(u,v), exactly diagonal in adjacent differences;
no uniform all-coefficient comparison survives zeta zeros and large values.
The repaired kernel still selects efficient finite directions: at N=256,
97.06% of full gain, versus 38.41% for the unmodified correlation direction.
The selected numerator and true-energy ratios have no cofinal estimate.
Complete Arb 256/384 and cutoff replays, exact Maxima checks, local self-review
only. No new Weil window, floor, G2 or RH proof.

Validation details and exact source hashes are in `evidence/v160/validation.json`.
The user authorized PR publication, then explicitly allowed merges and version tags.

## v1.59 local draft — fixed smoothing and arithmetic correlation (NS-60–66)

Classification: exact identities, proved implications and scoped obstructions,
certified finite computations, and an open optimized-correlation input.
One Mellin integration preserves the RH approximation criterion in its stated
tail space. Its adjacent differences are positive averages, up to a unitary
map, and their complete raw trace is at most 3*kappa/(8*N^2), with that
constant as its scaled trace limit. The complete Schur complement remains.
Explicit endpoint moments give a correlation formula with a full remainder;
the coefficient-mass bound does not yield a lower correlation estimate.

The explicit Euler-grid correction family still cannot satisfy a fixed-log
N^(-2) all-coefficient norm bound when Q_N <= N^alpha for fixed alpha < 1.
Optimal projections and selected residual directions are outside this result.
A localized Laguerre witness shows the canonical sharp Mobius interpolant
fails along the full integer sequence after any number of Mellin integrations.
No selected-subsequence exclusion is asserted. Positive smoothed atoms still
need signed coefficients: local matching forces the sixth coefficient -1/5.
NS-64 constructs the explicit local dual separator, with a certified
full-space cone-distance lower bound greater than 0.00228323. The local
cone distance is attained; equality for the full-space distance is not asserted.
With increasing smoothing order, even one fixed atom has vanishing relative
squared error while its absolute squared error diverges; this changing norm
cannot replace fixed-order NB convergence.

NS-65 excludes a fixed number of ordinary arithmetic Cesaro averages
as a repair of canonical full-sequence convergence. NS-66 changes the
canonical target to growth: at any fixed Mellin order r>=1 its complete
norm-growth exponent equals beta_star-1/2. This follows from exact local
zero evaluation and a Bochner-Abel estimate under a stated Mertens bound.
No unconditional subpolynomial bound or bounded cofinal subsequence is
proved; the criterion is a reformulation, not an independent RH estimate.

Validation: 419 exact Maxima checks. Complete q=2 Grams through index 64 at
256/384 bits, a doubled series-tail cutoff replay, and seven independent
positive-cell integrals at each precision. The finite trace lower bound is
below 1/50 of the exact gain at N=16 and N=32. The endpoint error budget is
more than 2000 times the leading norm on those blocks. A separate one-atom
control has certified relative squared error about 0.01387563 at order 64,
but absolute squared error above 1e35. These finite facts are not convergence.
Full build: 317 pages, zero undefined/duplicate references or overfull boxes.
Local self-review only; no independent review is claimed. No new Weil window,
tail metric, uniform floor, G2 or RH proof. Local publication remains pending.

## September 22, 2026 — NS-59 / v1.58 NB difference budget

Classification: exact identities, proved implications, certified finite
computations, and a named open lower-correlation input. The adjacent
functions delta_n=rho_n-(n-1)rho_(n-1)/n have norm squared between
H_(n-1)/n^2-(n-1)/n^3 and H_(n-1)/n^2. The complete coordinate change
uses g=T* h and K=T* S T; a smaller denominator cannot keep the old h.

The raw difference Gram has an exact zeta-weighted Mellin identity.
A piecewise-exponential fractional Sobolev inverse estimate, including
jumps, converts any critical-line zeta exponent theta<1/2 into norm
O(N^(-2+2 theta)). Classical Weyl gives O_epsilon(N^(-5/3+epsilon)).
Conversely, localized Mellin packets and the classical short-interval
point bound show near-N^(-2) power control equivalent to Lindelof, even
on dyadic blocks. Known zeta large values exclude every fixed logarithmic
N^(-2) raw norm bound. Scope: raw all-coefficient norm, not the projected
Gram, not the actual residual direction, and not the NB route as a whole.

Finite Arb checks replayed at 256/384 bits show raw-trace gain below 1/400
of the true gain at N=128 and N=256. The adjacent trace bound becomes
worse at N=256 after its numerator is transformed. The full directional
quotient does better there but supplies no asymptotic input. The floating
scan is separate, not proof evidence. Full evidence and local self-review
are in evidence/v158/. No independent review is claimed. No new Weil
window, tail metric, convergence, uniform floor, G2 or RH claim.

## September 22, 2026 — NS-58 / v1.57 translated-radical boundary test

Classification: exact identities and proved implications; API and the signed
arithmetic estimate remain open. The bounded attempt reached its explicit
stop condition: vanishing of the complete boundary pairing against all
translated radicals is equivalent to the original nullvector equation.

What had to change: the sharp radical restriction is handled in the complete
operator domain, allowing boundary jumps; no H1 derivative of a hypothetical
nullvector is assumed. The exterior formula retains the singular continuous
kernel, both poles and all prime shifts beyond the window cutoff. A compact
support distribution argument proves the exact equivalence without inferring
form density from ordinary L2 density.

The altered-weight controls obey an inhomogeneous equation with forcing
P_a B_delta phi_t. That profile is nonzero for any nonzero test because the
finite cosine multiplier is injective on ordinary L2. The forcing map is
Hilbert--Schmidt, so injectivity yields no uniform lower bound on the whole
fixed-window unit sphere; a particular finite kernel is outside that exclusion.

A single inherited RBC display was changed to the starred equation environment
to remove four duplicate PDF destinations, preserving its formula and tag.

No independent sign or uniqueness estimate was obtained. This is a limitation
of the proposed inference, not a negative original Weil direction or an API
closure. Evidence/v157 records the analytic proofs, finite exact algebra,
local self-review and actual manuscript build. No new numerical window,
tail metric, uniform floor, G2 or RH claim.

## September 22, 2026 — NS-57 / v1.56 finite prime-weight controls

Classification: exact identities, proved implications, and open input. The
September 22 standalone checkpoint is integrated on top of v1.55; its prior
versioned report remains unchanged in the working archive. No private email
or personal correspondence is included in the public repository.

What changed: generic geometric discrimination is replaced by actual complete
operator families whose finite prime-shift weights are perturbed. Their
negative tests occur in both parities and their first-zero vectors satisfy
the same support geometry and a modified affine-potential equation. The
original arithmetic near-radical identity does not survive the perturbation.
A fixed-pattern sensitivity upper bound follows from the complete v1.53
residual. These controls do not refute the original arithmetic operator.

A separate exact result preserves the bounded-floor objective under every
fixed bounded self-adjoint perturbation and identifies scalar compensation
and the RH-conditional perturbed lower-edge limit. This is a consequence of
the v1.36 reduction, not an additional signed estimate. NS-58 records a bounded
next attempt using the exact arithmetic radical and exterior pairing; a mere
restatement of the null equation does not count as progress on that input.

Validation, the local (not independent) review, twelve Maxima checks, and
incremental evidence are in evidence/v156/. API, uniform floor, G2 and RH
remain open.

## v1.55 — NS-55 arithmetic kernel mechanism tests (2026-09-22)

What changed: a local logarithmic unique-continuation argument must retain the
prime shifts. Exact Neumann constructions show that the actual arithmetic
operator permits f = A_a f = 0 on a nonempty open patch with f nonzero elsewhere.
The witnesses lie in the complete operator domain, work in both parities for
a > log 2, and survive finitely many source constraints. They are not global
nullvectors and give no negative diagonal Weil direction. This local property
is actually false, rather than merely uncertified.

A separate exact sign calculation rules out preservation of the ordinary
nonnegative cone by the full semigroup. Positive bounded multiplication
conjugation does not repair it. This does not refute nonnegative Weil energy
or a specific ground state's positivity. A prime-free exterior observation
cell yields a scoped uniqueness theorem; a first-zero nullvector's support
saturates both window endpoints, so the needed cell is not supplied.

The finite inward-dilation identity replaces an unjustified differentiated
virial calculation. It keeps the complete domain, both pole terms and all prime
correlation differences. The signed arithmetic estimate remains absent.
Primitive/Fredholm/window-entry statements are archived as supporting evidence;
a discrete exceptional set does not exclude the physical coupling.

Independent cross-reviews found no unresolved MAJOR/MINOR issues. Actual full
build: 285 pages, 0 undefined references, 0 duplicate references, 0 overfull boxes.
No new window, tail metric or uniform floor. API, G2 and RH remain open.


## v1.54 — NS-51/52/53 first analytic results (2026-09-22)

What changed: nullvectors are tested through a continuous affine screw potential
on the complete logarithmic form domain; no ordinary H0¹ derivative is assumed.
A positive torsion function plus a bounded self-adjoint rank-one perturbation
of the same logarithmic principal operator disproves the generic bootstrap.
This is not a counterexample for the arithmetic operator. API is the named,
unproved affine-potential injectivity input; both parities are retained.

Paired heat-zero transport has coefficient 1/4 in Xi coordinates. Finite cluster
contours give exact derivatives through collisions and preserve the exterior
zero interaction. Same-test comparison with a real-zero positive-time form is
impossible if it has one zero unmatched by Xi; that hypothesis is not established
at a specified time here. The general heat route and suitable test transport
remain open. The original Weil form has not been shown negative.

Nyman–Beurling approximation is reopened: any rigorous d_N→0 rate suffices.
Exact residualized block gain retains all old/new Gram couplings and has an
unconditional lower bound ||h||²/(kappa log(M/N)). No asymptotic bound on its
arithmetic numerator is proved. RBC is a named sufficient open input; failure
of the raw Möbius prefix is prior art and is not a failure of optimal approximation.

Independent domain and cross-route reviews have no outstanding mathematical
MAJOR/MINOR findings; two heat typesetting corrections were fixed. The release
proof is integrated verbatim and all new reports have an artifact hash inventory.
Actual manuscript build: 278 pages, 0 undefined references, 0 duplicate references,
0 overfull boxes. No new numerical window, tail metric, uniform floor, G2 or RH
claim. Publication status is recorded by the PR and tag, not inferred from a draft.


## v1.53 local draft — NS-46 with Astra-2 (2026-09-22)

What changed: the source translates stay in [-1,1] with shrinking spacing;
we explicitly bound the finite Gram instead of requiring uniform conditioning.
The complete boundary residual then decays exponentially in -lambda² and pays
for a block of rank ~lambda²/(20000 log lambda). The full prime remainder,
both poles, exact parity dimensions, source codimension and all block mixtures
are retained. Independent finite-arc and complete-residual reviews pass.

The obstruction is to a uniform or polynomial positive gap after
o(lambda²/log lambda) constraints. A smaller positive gap is not excluded.
It is an actual upper ceiling on that coercivity constant, not a negative Weil
direction. No signed lower bound on the remaining complement was obtained.
The existing gap-free floor transfer was identified as prior art and is not
repackaged as a new result. No new numerical window or tail metric; G2/RH open.
Evidence, actual build and versioned report are in evidence/v153/. Draft based
on PR21; no publication or tag is asserted for v1.53.


## v1.52 local draft — NS-43/44/45 (2026-09-22)

Fresh exact dyadic witnesses at the existing lambda=5 window close two precise
comparison criteria: the stipulated 1e-8D tail lower bound, and the tested N25
dyadic norm comparison. Arb320/448 replay, independent signed-index assemblies,
and reviews pass. The tail witnesses have positive Weil energies. These are
new certificates, not recovered historical artifacts; both NS-1 original
recovery groups stay OPEN.

NS-43 proves fixed/moving prime-channel loss obstructions, unrestricted exact
adaptive concentration equivalence, a scalar-set countermodel, and scoped CCM
nonselection/coarse-profile results. Complete relative-selection and entire
transform criteria identify the missing input. A bounded discrepancy for one
explicit smooth bump would already exclude off-line zeros; it is unproved and
is not promoted as a weaker route. Direct uniform complete lower-floor work
remains the priority; QG+packet investigates bounded-complexity failure only.

The substantive draft is based on PR20/a89a581 and is not merged or tagged.
See evidence/v152/ for proofs, validation, provenance and versioned assessment.
No new window, tail metric, G2 or RH claim.


## 2026-09-22 — v1.51 / NS-39, NS-38 disclosures and delegated measurements

Classification: exact identities, proved implications and named open arithmetic
inputs. NS-39 is one analytic proposition, not a substituted measurement.
The potential is r_a=(F^{-1}(Z_a F h_a)-2 I_(h,a)c)/h on I_a, with the complete
corrected field, finite window pole mass and exterior edges retained. ZLD gives
QC_K >= kappa theta² D/(2K) on the same rule; the bounded-energy packet clause
remains separate. CAE is exactly the existing uniform complement floor. Abstract
measure countermodels do not prove independence of actual arithmetic assertions.
The universal-head QG demand is false by excessive cutoff dilution regardless
of CAE truth. No new signed estimate has been proved.

NS-38 selected disclosure for BOTH original NS-1 groups, not recovery: all local
archival assertions and historical numerical accounts are qualified. Original
recovery remains open. Five v1.35 scientific files match the old hashes; v129/v130
companion artifacts remain absent. The unavailable v128 numerical closure is
marked blocked; printed analytic proofs remain unchanged. No separate version
bump was made for the disclosure. NS40 is Astra-2's separate PR19.

NS41/42 were delegated and reviewed independently. The odd finite-bin records
print every constraint slack and distinguish dual minima from feasible primal
states. The 12 transformed-energy records separate direct J, variance, signed
potential, pole and exterior terms. Quadrature does not resolve tiny matrix q.
These remain diagnostic records under evidence/diag_*, never proof bounds.
No new window, tail metric, G2 or RH claim.


## 2026-09-21 — v1.50 / NS-34: explicit capacity weight and a scoped loss obstruction

Classification: exact identities, proved scoped implications, and named
open input CAE. This is the proposed analytic capacity attempt, not a
substituted numerical diagnostic. No new window or tail metric.

The selected h(x)=E(H)(exp x) is the positive, even Gaussian arithmetic
radical already archived in v1.15/v1.35. Its pole mass is exactly
integral cosh(x/2) h(x) dx = 1/sqrt(3). The full identity is
q[hg]=J_h[g]-(2/3)Var_nu(g)-2|integral sinh(x/2)h(x)g(x)dx|^2.
The odd square and all finite-window exterior edges are retained; h is
not substituted for the actual repaired source in the constraint.

What had to change: generic strict absorption of the negative potential
cannot spend a fixed fraction delta>0 of this transformed positive energy.
The inward prime-2 edge on far-translated compact tests costs at least
kappa exp(gamma lambda^2), while their original form is at most
A+(8a+1)exp(a)+2a. A two-dimensional even test space imposes the actual
source constraint exactly; the odd tests are already admissible. Thus
eta >= [delta*kappa exp(gamma lambda^2)-B_a]+, and bounded eta forces
delta=O(lambda log(lambda) exp(-gamma lambda^2)). Omitting prime-2 alone
has the same obstruction. All mixtures and cross terms are controlled.

Failure is of these lower comparisons, not of the physical form. The
unweakened coefficient-one capacity condition remains unproved; retaining
all terms gives the named Critical Arithmetic Energy comparison (CAE),
which is an exact re-expression of the missing uniform complement floor,
not an independently established positivity mechanism. Other weights are
not excluded. The map closes only fixed-slack/prime-2-deletion for this
weight and leaves the full capacity route blocked. G2 and RH remain open;
NS-1's two original evidence groups remain OPEN.

Actual build: 246 pages, 0 undefined references, 0 duplicate references,
48 bibliography items, 0 duplicate bibliography keys and 0 overfull boxes.
New proof pages 160-164 rendered and inspected. Independent NS-37 review
has no unresolved MAJOR/MINOR; both clarifications are integrated and the
reviewed fragment hash matches. See evidence/v150/build_report.json and
audits/ns37-capacity-weight-2026-09-21-v2.html. The remaining NS-31 goals
sentence was corrected to the weighted strict-cutoff amplitude already
proved in eq:v146-amplitude; historical diagnostics are unchanged.
The general Picone method and completed-zeta kernel are classical; no
worldwide novelty or publication readiness is claimed.


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

# v1.42 — NS-18 complete-ground local zero, September 21, 2026

**Requested experiment:** transfer a local zero near gamma_1 to the complete ground at the existing lambda=4 window, starting with the spectral/residual feasibility budget. Claimed at 2e5364b before research under the provisional ID NS-17; renamed NS-18 after concurrent main used NS-17 for documentation. The resulting certificate addresses that complete object; no finite-compression diagnostic is substituted.

**What had to change:** applying the global separator 1e-73 directly gives nonunitary transform error about 0.260823, so the endpoint sign test fails. The same archived complete shifted-Schur comparison certifies an even-sector separator b=1e-67. Exactly even trial error has no odd component, so this separator suffices and reduces the transform budget by 1000. It is not the global spectral gap. This is a failure of the original bound, not the zero or the operator.

**Proof:** with unit trial f and h=P_ground f, nonnegativity and even spectral separation give ||f-h||<=sqrt(q[f]/b). The projection is nonzero since q[f]<b, and is a scalar multiple of the complete ground. Comparing to this projection avoids an extra unit-normalization error. Transform/derivative error norms are sqrt(L) and sqrt(L^3/12), L=2log4. The exact frozen trial has q[f] about 2.45361754930714e-75, yielding errors below 0.000260824 and 0.000208757. Opposite endpoint signs at gamma_1±0.1 and derivative lower bound 0.0016 prove a unique simple local zero.

**Complete inputs:** shifted lower inertia has one negative and 16 positive directions at b, and the exact trial supplies the required complete negative direction. T-b stays positive. Archived 768/896-bit even residual enclosures include all rows beyond J=65536; small complete gates are replayed. Full old residual assemblies are not rerun. No new window, finite eigensolve, support or remote cutoff was introduced. All 4097 trial coefficients retain their exact centering phase.

**Verification:** new gates at1024/1280bits; second implementation with principal determinants and direct sinc integrals, including derivative positivity on32intervals; saved-interval and dependency-hash checks. This is same-agent cross-checking, not an external audit. New proof and evidence under evidence/v142/, with a separately versioned styled HTML report. Build217pages, zero undefined/duplicate references and overfull boxes; Pyright clean.

**Scope:** one local real zero, not necessarily the first positive transform zero. No sign or tiny value of its discrepancy is determined. Complete zero enumeration, high-accuracy CCM transfer, cofinal Xi convergence, G2 and RH remain open. The two NS-1 missing evidence groups remain OPEN and are not dependencies of this result. This branch is local; concurrent main through 0f8cb16 is merged here, with its diagnostic artifacts preserved. No remote publication is recorded.

**Next useful refinement:** retain the even separator while bounding the transform error directly in an energy/residual dual norm. That would test how much the global Cauchy-Schwarz projection bound loses, without computing another window. It is an open task, not a new claimed estimate.

---

# NS-1 — partial v1.31 original evidence recovery, September 21, 2026

Recovered and committed the original 4,925-byte `g2_weighted_concentration_report.md` under `evidence/v131/`, with complete saved-text line coverage, provenance and a per-version manifest. The text was not regenerated from the manuscript. The original scripts, saved outputs and complete adversarial evidence remain unavailable: the saved 207,224,098-byte v1.34 cumulative archive returns HTTP 502, including through the native download helper. No substitute computations were made and no missing-evidence flag is cleared. NS-1 and both historical ledger groups remain OPEN. The manuscript revision remains v1.40; no mathematical claim or version bump is made. No G2 gap closed.

---

# v1.40 — NS-5 complete ground ordering, September 21, 2026

**Requested task:** certify simple even ground of the complete W4 using the v1.17 machinery, then check Connes–van Suijlekom Theorem6.1. This task was claimed in NEXT_STEPS.md at dc8b396a09f22bdd16ff52e1ac8f5711837768e6. No cheaper finite-compression diagnostic was substituted.

**What had to change:** v1.17 hard-codes lambda3 tail constants and directly reassembles shifted residuals. At lambda4 we retained the exact4096-support normalized trials and complete unshifted Schur bounds from v1.25/v1.26, and proved a resolvent-change comparison for W4−sigma I. With delta=1.7940e-8, K=G*WG, Hh=V*V and Ht=Z*Z,

    S_sigma^V >= kappa K - sigma[Hh + 2/(1-sigma/delta)(Ht+K/delta)].

Here kappa=.62629 even and .428 odd. C=r*T^-1r satisfies0<=C<=K; Y=T^-1BV=−Z+T^-1r gives Y*Y<=2Ht+2K/delta. The full inverse change is retained; simply shifting an unshifted lower matrix would have been invalid.

**Initial attempt and correction:** sigma=1e-70 gives one negative lower pivot in each parity, at1024/1280bits. This alone would not prove an odd negative shifted direction. However the old exact odd trial has complete Rayleigh quotient in (3.59269956625,3.59269956626)e-71, which DOES prove that1e-70 is too large for odd positivity. This falsifies that threshold, not simple even ground. The user's eight-order separation describes the even finite-compression gap; it is not the complete global spectral gap, and the N64 values move substantially by N256. We changed only the exact test threshold to1e-73. No extra window, inverse solve, CG depth or remote cutoff was introduced.

**Certified result:** at1024 and1280bits the even17x17 shifted lower form has1negative and16positive pivots; the odd16x16 form has16positive pivots. All exclude zero. The exact frozen even trial, column16, has complete Rayleigh quotient in (2.45361754930,2.45361754931)e-75. Square completion and compact resolvent therefore give 0<mu0<2.454e-75, mu1>1e-73, and gap>9.7546e-74 for the complete operator. The ground is simple and even. This is an ordinary spectral threshold, not an LDL pivot magnitude or a congruence-relative margin.

**Inherited evidence versus fresh work:** all exact trial coefficients and ordinary Grams are reconstructed at both new precisions. The verifier replays the prior small even margin gate, odd K-orthogonal complement gate, exact Fraction shared-head check, and odd directional scalar gate. Full residual assemblies remain the archived complete inputs: even768/896bits, odd complement768bits, repaired odd direction1024/1280bits. Each includes all rows after J65536 via the original order64 majorant. These old full assemblies were not rerun. Input paths and byte hashes are recorded in the reports, and no previous file is modified.

**External implication:** the exact one-sided real distribution on[0,2log4], with its origin subtraction and logarithmic diagonal, is exhibited in the proof. prop:v114-weil-core gives essential selfadjointness on trigonometric polynomials. CvS Theorem6.1 (https://arxiv.org/html/2511.23257v1#S6.Thmtheorem1) then gives only real zeros for the entire Fourier transform of the complete normalized ground. Translation/unitary-normalization factors are zero-free. No endpoint-nonzero condition, simplicity of transform zeros, or convergence to Riemann Xi is asserted.

**Classification and novelty:** certified fixed-window extension of v1.17 and application of the published CvS theorem. The new ingredient within this project is a rigorous shift bound reusing existing complete Schur certificates and retaining the ordinary Gram. This is not registered as a new uniform G2 mechanism; worldwide novelty/publication readiness is unresolved.

**Adversarial review:** independent reviewer checked the resolvent comparison, all domains and inertia steps, theorem hypotheses and the same-trial normalization. Detailed code/proof review is in evidence/v140/adversarial_review.md. Both complete parities are included. The actual physical endpoint, first-slot-linear convention, Fourier cut, logarithmic diagonal and explicit sampler graph defect are unchanged.

**Build:** ./manuscript/build.sh completed: 213 pages, zero undefined/duplicate references. LaTeX-only delivery; the temporary ignored PDF is not published. The independent principal-determinant and exact-Fraction norm checks passed at1024/1280bits and are archived with their checker.

**Next obligation:** cofinal ordinary lower control, or an independently justified convergence linking these complete ground transforms to Riemann Xi. NS-5 closes a local spectral-ordering obligation only. No G2 gap was closed; RH remains unproved. Two historical evidence groups remain OPEN, unchanged.

---

# v1.39 — Scoped meta-obstructions, September 21, 2026

**Requested task:** prove a general obstruction to estimates insensitive to the arithmetic location of negative beta_a mass, extending cor:v137-scalar-no-go. No fixed-window computation was substituted.

**What had to change:** the informal universal hypothesis is false. We replaced it by two explicitly different information-loss properties, and retained a coverage table rather than claiming to explain all ten closures.

**Proved result 1:** every sound density-relaxation budget B_a diverges if the relaxation contains all normalized physical Fourier densities (full space or the complete actual source complement) and the explicit symmetrized v1.37 cutoff probe. Both parities must be included for the unconditional finite-floor implication. Under RH only, B_a >= a/(6 pi^2) eventually. Unconditionally, a bounded cofinal B_a would imply RH and then contradict that probe pairing.

The concrete mass/height/variation class is p>=0, integral p=1, sup p<=a/pi, TV(p)<=2a. The exact probe has variation <=2a/pi and passes it. The optimal full-histogram mass-cap floor is

    ell_cap(a,beta_a) = (a/pi) integral_0^(pi/a) beta_a^up(s) ds -> -infinity.

It retains the distribution of all favorable and unfavorable values; any lower rule sound on every capped probability density is no better. This is a stronger class obstruction than using only the scalar minimum. Arbitrary sharper local-derivative or source-dependent evaluation constraints are not declared probe-insensitive.

**Proved result 2:** let M_a multiply by beta_a. Protect any finite physical head E with F_a E in D(M_a) by fixing S=F_a E + M_a F_a E. Among domain-preserving finite-rank unitary changes U fixing S, the infimum physical compression Rayleigh value is exactly ess inf beta_a. All protected complete operator actions, including the actual finite-source residual, remain unchanged. The conclusion is valid separately in either parity and even when head rank grows with a, provided it is finite at each a. Since ess inf beta_a -> -infinity, a universally orientation-blind bound cannot supply a cofinal floor. Such U* M_a U generally ceases to be a multiplier: no rearranged-prime or negative-Weil assertion follows.

**Falsification of overbroad wording:** b=1-(D+1)1_E with |E|=pi/[2a(D+1)] has physical form >=(1/2)||f||^2 for every placement and shape of E, even as D->infinity. Thus location independence and divergent negative depth alone do not imply failure. The actual arithmetic signed-probe pairing is essential.

**Candidate register:** G2.6-META-01; status PROVED SCOPED OBSTRUCTION, not a live positive mechanism. Nearest prior: v1.37 primitive/pointwise no-go. New within the inspected project: optimal histogram benchmark and arbitrary probe-containing relaxations, plus protected finite graph data in the orientation adversary. Classical ancestors: Lieb–Loss bathtub principle and Fan–Pall spectral compression. Worldwide novelty/publication readiness remain unresolved. Signed Schur/inverse, dyadic metrics, source-compressed Schatten, common-Gram, Picone and cross-channel routes are not relabeled as members without checking the stated property. The report/review contain the ten-route coverage table; most closures are not logical consequences of this theorem.

**Adversarial outcome:** independent review passed the actual proof file (SHA256 pinned in evidence/v139/adversarial_review.md). It corrected parity quantifiers, rejected a claim about all physical derivative constraints, and required explicit non-multiplier scope. Exact Fraction checks passed six protected-column finite-dimensional models, three location-blind positive models, and the v1.37 rational probe constant. They are abstract tests, not numerical proof substitutes or arithmetic window certificates.

**Physical scope:** a=log(lambda), interval(-a,a), original unitary Fourier normalization and log-weighted form domain; no new Fourier cutoff. The full source complement is used only with its established residual. C_a^low is not identified with it; remaining blocks and couplings remain obligations. First-slot linearity, endpoints, prime cut, log diagonal and sampler graph defect are unchanged.

**Build:** ./manuscript/build.sh completed: 210 pages, zero undefined/duplicate references. Temporary PDF ignored and not delivered. Incremental evidence is in evidence/v139/; no cumulative archive created. Existing missing originals for v1.28 and v1.31–v1.34 remain missing; none were regenerated as substitutes.

**Next precise target:** a signed joint concentration lower estimate with a single finite cofinal ordinary constant, both parities and all physical couplings, using realizability/geometry sufficient to exclude the forbidden probes/orientations. The new no-go does not provide it. No G2 sign gap closed; RH remains unproved.

---

# RH manuscript research log

# Complete manuscript v1.38 — September 21, 2026

# Complete finite-floor test — v1.38

September 21, 2026. Starting snapshot: complete v1.37, GitHub commit `c623b21aca132a3b87a95dc19e24da9393f56a00`. The saved canonical ChatGPT copies remain behind at v1.34 after transfer failures; the verified GitHub source is used. Delivery remains LaTeX only.

## Outcome

The requested weaker experiment succeeds: both parity sectors at lambda=5,6,8 have **complete ordinary lower floor -8**, using the same fixed parameters. Every omitted Fourier row is enclosed. The frozen trial quotients are positive and below 1e-16, so each sector's spectral edge is bracketed between -8 and 1e-16. No certified negative physical trial was found.

The lambda=8 floor also bounds all smaller physical windows by support consistency and zero extension. Thus a finite list of floors is not additional evidence of a cofinal theorem; the intermediate windows test the same construction's cost and enclosure headroom.

No G2 sign gap was closed. RH is not proved.

## What changed, and what was held fixed

The practical improvement is to use the finite-floor theorem literally: choose a **moderate fixed additive shift delta=8**, rather than trying to certify positivity or a tiny error of 0.001. This allows a much smaller remote split. It does not revive the disproved lambda=5 inequality W>=1e-8 D on Q16.

Compared with the old positivity pipeline, this experiment changes the target to W+8I, uses a head ending at 256, and uses Z=0 instead of any CG or structured inner solve. The same procedure and the following parameters were then used for every lambda/parity case:

| Parameter | Frozen value |
|---|---|
| Ordinary additive shift delta | 8 |
| Fourier head cutoff N | 256 |
| Explicit residual cutoff J | 4096 |
| Moment order r | 16 |
| Remote Young parameter tau | 1/10 |
| Trial solve Z | 0 |
| Even head | 0 through 256, dimension257 |
| Odd head | 1 through 256, dimension256 |
| Archimedean series terms | 64, plus analytic remainder |
| Initial arithmetic | Arb160 bits |
| Replay arithmetic | Arb256 bits, identical dyadic witnesses |

The window length L=2log(lambda), prime list, coefficients, separate logarithmic diagonal, prime norm, tail weights, moment matrices and congruence proposals were freshly evaluated per window. Those evaluations are part of the fixed procedure. No lambda=4 constant was reused. The construction transferred without window-specific retuning **within this three-window test**. Delta=8 and N=256 were selected for this finite range; they are not asserted as an unbounded-window rule.

## Exact inequality and physical scope

Use the canonical closed Weil form on H_a=L2(-a,a), a=log(lambda), with unitary Fourier transform of the zero extension and logarithmic form domain. The physical Fourier head is the existing orthonormal even/odd basis; no prolate-source or source-L2 norm transfer is used. In the first-slot-linear convention, the block adjoints and real quadratic orders are unchanged.

For W=[[F,B*],[B,T]], suppose T>=D_g and g_(N+1)+delta>0. A general finite solve obeys

    K_delta=K_Z+delta(I+Z*Z),
    R_delta=R-delta Z.

The remote rows beyond the support of Z are unchanged. Therefore

    L_delta=K_delta - sum_(N<n<=J) R_delta,n*R_delta,n/(g_n+delta)
            - U_J/(g_(J+1)+delta) >= 0

implies W>=-delta I on the complete form domain. In this test Z=0, so K_delta=F+delta I and R_delta=B. The moment theorem is used with M=N<J and G the orthonormal head embedding; G*G=I. Its proof does not need a nonempty intermediate solve block. The lower enclosure includes both the leading remote moment Gram and the geometric remainder.

Both parities are certified. Hence the bound applies to every physical subspace, including C_a^low where it is defined, without identifying it with the larger rank-one complement. No centered sampler is used, and its explicit graph defect is neither removed nor bypassed in any transfer claim.

## Certificate margins and spectral brackets

Let U_delta=K_delta-L_delta. The generalized margin is

    h=1-lambda_max(U_delta,K_delta).

The exact dyadic congruence C verifies C L_delta C* >=mI and C K_delta C*<=MI, with m=999/1000. Thus h>=m/M. The table displays downward-rounded lower bounds; it does not display resolution margins or exact generalized eigenvalues.

| lambda | even h lower | odd h lower | complete ordinary floor | each parity's trial upper |
|---|---:|---:|---:|---:|
|5|0.8430|0.9190|-8|<1e-16|
|6|0.7166|0.7620|-8|<1e-16|
|8|0.2474|0.1022|-8|<1e-16|

Exact rational M bounds, even then odd, are: lambda5=(1185,1087)/1000, lambda6=(1394,1311)/1000, lambda8=(4037,9772)/1000. The corresponding bounds on h are exactly999 divided by these integer numerators.

All six 160-bit passes were replayed at256 bits using the same C and trial vectors. The saved NPZ contains exact IEEE754 dyadics; converting each value to Arb gives an exact scalar. Each C is checked triangular with nonzero diagonal, and every outward row gate passes. The rounded finite-matrix eigenvalue proposals were negative near machine precision; the exact frozen trial quotients were **positive**. The float signs are not spectral evidence.

All computations took seconds per sector in this environment. Timings are recorded for reproducibility, not promised as hardware-independent complexity.

## Shifted cutoff cost: proved obstruction for this comparison

With c=0, the existing scalar far weights are g_n=log(n/L)-E_L(2pi n/L)-kappa_(lambda,N), where kappa>=M_phi,lambda. Thus their shifted positivity gate requires

    N+1 > L exp(M_phi,lambda-delta).

A fixed shift saves a large constant factor, approximately exp(-delta), but retains the existing asymptotic exponential-in-lambda cost. Since M_phi,lambda>=||T_prime,lambda||~lambda, bounded delta forces liminf log((N+1)/L)/lambda>=1. A polynomial N would instead require delta at least M_phi,lambda-O(log(lambda)). This rules out a polynomial-cost, bounded-floor conclusion from **this scalar comparison**, not from all signed matrix metrics.

Fresh outward thresholds (the smallest admitted N>=1) are:

| lambda | delta=.001 even | delta=.001 odd | delta=8 even | delta=8 odd |
|---|---:|---:|---:|---:|
|5|1501|7217|1|4|
|6|7481|35985|3|14|
|8|124317|598024|43|204|

The chosen N256 covers all delta8 cases. A -.001 target would hardly reduce the old cost, even though it also avoids the false positive weighted metric. Every nonboundary threshold has an outward-positive gate and an outward-negative predecessor. The formulas are monotone in N.

## Failed or exploratory attempts

Before freezing the common-floor protocol, smaller N128 pilots passed complete floors -3 (lambda5 even), -4.5 (lambda5 odd and lambda6 even), and -8 (lambda8 even). A lambda8 even shift7.5 proposal failed the lower-enclosure Cholesky gate, and a lambda5 odd shift4 failed the scalar tail gate. Neither failure is a negative Weil direction. These pilots were not used to infer cross-window stability.

The first replay's optional margin reporting attempted to pick nearly equal interval extrema through binary64 keys. A protective assertion rejected that choice. It was replaced by explicit rational thresholds and strict outward comparisons; every final proof gate and generalized margin passed. The underlying six positivity checks had already passed. This illustrates why the floating ordering is only a proposal, never a proof assumption.

## Candidate register and novelty screening

**G2.6-FF-01 — fixed moderate additive floor. Status: validated finite diagnostic / continuation, not a new independent live arithmetic mechanism.**

- Precise target: W_(lambda_j)>=-C*I with C* finite independent of j along a cofinal family; current certificate proves C*=8 only for1<lambda<=8.
- Assumptions used for current certificates: the proved canonical form/core, coefficient and moment enclosures, shifted scalar tail estimate, and outward arithmetic. No G2, RH, hidden complement positivity, or unjustified source transfer.
- Essential practical change: using a non-small additive shift permitted by v1.36. This relaxes the spectral target; it is not a new factorization or arithmetic cancellation.
- Nearest prior proposals: v1.16 signed Schur/moment certificate, v1.17 shifted inertia, v1.25 cutoff-cost theorem, and v1.36 finite-floor implication. The formulas are direct specializations with Z=0.
- Explicit exclusions: not a new structured inverse, prime norm estimate, finite-rank repair, source-only residual argument, dyadic pair metric, common-Gram factorization, Picone mechanism, or weighted-concentration mechanism. It reuses the existing scalar prime bound and signed Schur correction openly.
- Literature: finite-window lower bounds and verified trial upper bounds are familiar in the nearby primary preprint [Zhu2026v2](https://arxiv.org/html/2608.24827v2), sections1.2,1.3 and5. No external numerical constants or sign claims are imported. The shift and block completion are elementary spectral tools. Neither worldwide novelty nor a project-new positive mechanism is claimed.

## Exact remaining lemma and next step

Prove the existence of one fixed C* and a cofinal family of physical windows for which the complete lower-floor inequality holds, either on both full parities or on a source complement satisfying the already stated residual and coupling hypotheses. A finite list, even a whole bounded interval of windows, supplies no such proof.

For this pipeline the concrete unresolved estimate is L_(C*,lambda)>=0 with a controlled complete correction on an unbounded family. The current scalar remote comparison imposes its exponential cost even after shifting. A useful next analytic target is a signed tail estimate with bounded additive loss that does not replace the prime operator by its growing absolute norm. A declining lower certificate alone cannot diagnose spectral divergence; a negative certified Rayleigh quotient would be needed for actual negative evidence.

The completed experiment answers the cost question positively for5,6,8, but leaves the asymptotic arithmetic problem open.


---

# RH manuscript research log

# Complete manuscript v1.37 — September 21, 2026

# v1.37 — an arithmetic no-go for bounded scalar primitive budgets

**Status:** proved obstruction to a previously proposed route. No G2 sign gap was closed. RH is not proved. Delivery is LaTeX only.

## Question tested

The v1.36 reduction made a uniform finite ordinary-norm lower floor sufficient. That relaxed the earlier o(1) target and required retesting the v1.34 primitive mechanism rather than simply retaining its old rejection.

For the complete physical symbol beta_a, define

    Delta_a = sup_{x<y} (−integral_x^y beta_a(xi) dxi)_+.

The previous proved estimate is q_a[f] >= −a Delta_a ||f||². Could a Delta_a stay bounded along a cofinal family?

**Answer: no. The new proof establishes a Delta_a -> infinity unconditionally for the actual arithmetic symbol.** It also establishes inf_xi beta_a(xi) -> −infinity. A linear rate is only proved conditionally on RH.

## Exact setting and scope

- a=log(lambda), T=2a, I_a=(-a,a), ordinary norm in L2(I_a,dx), first-slot-linear convention.
- Complete canonical closed physical Weil form, domain integral log(2+|xi|) |F(xi)|² dxi < infinity, where F is the unitary Fourier transform of zero extension.
- No finite Fourier cutoff is introduced. All prime powers with log n<T appear with weight Lambda(n)/sqrt(n), with the strict endpoint convention.
- beta_a is exactly Re psi(5/4+i xi/2) − log pi − r_a(xi), including the continuum term of v1.30 and the full both-parity identity of v1.35. It is not the raw prime-comb symbol.
- The result concerns scalar sufficient bounds on the full physical space. It neither identifies C_a^low with the source complement nor supplies a bound on either complement. Both parity blocks and all required couplings remain obligations.

## Proof mechanism

Choose delta=1/100 and a fixed even positive smooth mollifier kappa supported in (−delta,delta), with integral1. Set

    w = 1_[pi,3pi] * kappa,
    H(t) = integral w(s) exp(−its) ds,
    K(u) = integral_[−1,1] H(t) exp(iut) dt.

Then w>=0, integral w=2pi, ||w'||_1=2, H(±1)=0, K(u)=O((1+u²)^−1), and K(0)<−1/(3pi). The sign follows analytically from

    integral_pi^(3pi) sin(s)/s ds
      = −pi integral_0^pi sin(u)/[(pi+u)(2pi+u)] du <= −1/(3pi),

plus the 1/2 Lipschitz bound for sinc and the mollification error pi/100. All constants are fixed before the window grows.

Assume RH temporarily and fix a zero ordinate gamma0 of multiplicity m0. The explicit formula gives the exact identity

    J_a = integral beta_a(xi) w(T(xi−gamma0)) dxi
        = sum_gamma m_gamma K(T(gamma−gamma0)) + E_T,

    |E_T| <= 8pi exp(−5T/2) / [5T(1−exp(−2T))].

There is no omitted 2pi or T factor. The inverse-transform kernel outside |t|<=T is precisely −exp(−5|t|/2)/(1−exp(−2|t|)), from the 5/4 reference multiplier. The transform of the probe is T^−1 exp(−i gamma0 t) H(t/T). Inside the cutoff, the complete geometric distribution and both pole signs are retained.

The endpoint zeros make the truncated test continuous and piecewise smooth, with its second derivative a finite measure. Mollification extends the smooth explicit formula to this test with a uniform O((1+|gamma|)^−2) zero-sum majorant at fixed T. If exp(T) is a prime power, its endpoint atom pairs with zero. Isolation of gamma0 and N(Y)=O(Y log Y) give

    J_a = m0 K(0) + O_gamma0,w(T^−2) + E_T <= −1/(6pi)

eventually. The last inequality is RH-conditional.

The optimal scalar primitive decomposition beta_a=b_a+U_a', b_a>=0, ||U_a||∞=Delta_a/2 gives J_a>=−Delta_a, because the probe has variation2. Its mass is pi/a. Thus, under RH,

    Delta_a >= 1/(6pi),
    inf beta_a <= −a/(6pi²)

eventually. The threshold is not claimed effective here.

Now suppose a Delta_a were bounded on any cofinal sequence. The old primitive inequality would give a complete ordinary uniform lower floor; v1.36 would imply RH. The preceding RH-conditional estimate would then contradict that same bounded sequence. This proves a Delta_a -> infinity unconditionally. The identical contradiction, using the full symbol identity, excludes any cofinal pointwise lower bound beta_a>=−C and proves inf beta_a -> −infinity.

This is not circular: RH is first a consequence of the hypothesized scalar certificate, and is then used to disprove that certificate. We do not assume RH to obtain an unconditional sign for the physical form.

## Adversarial checks and limits

An independent reviewer checked the explicit-formula extension, all Fourier factors, the reference multiplier's exterior tail, the strict prime cutoff at resonance, multiplicity and the cofinal contradiction. See adversarial_review.md.

The nonnegative frequency probe is **not** asserted to equal |F|² for a physical Paley–Wiener transform supported in I_a. Under RH its negative pairing therefore does not contradict Weil positivity. This is precisely why a scalar frequency comparison can fail while a support-constrained operator comparison survives.

The script check_probe.py checks the rational gate 6*(22/7)²<100 and gives independent binary64 quadrature diagnostics of the probe and a single spectral atom at T=2,7,19,100. These T values are abstract scaling tests, not new arithmetic windows. The approximate K(0) is −0.35434715073059375. Numerical quadrature is not an interval certificate and is not used as the proof of the theorem. No lambda=8 calculation was attempted. An initial attempt to use mpmath found that package unavailable; the diagnostic was rewritten using the standard library. The analytic proof is independent of that implementation choice.

No unconditional linear rate for Delta_a or inf beta_a is asserted. The unconditional conclusions are the two divergent limits. The theorem does not rule out all matrix-valued metrics, signed concentration estimates, or symbol modifications with a separately proved physical error bound.

## Candidate register and novelty audit

**ID:** G2.6-PT-01b, retest of PT-01 under the v1.36 finite-floor reduction.

**Precise proposed sufficient estimate:** sup_j a_j Delta(beta_a_j)<infinity, a_j->infinity. **Status: rigorously ruled out.** The related scalar pointwise estimate inf_j,xi beta_a_j(xi)>−infinity is also ruled out.

**Nearest prior proposal:** v1.34 optimal signed-primitive/Bernstein estimate, previously rejected as an o(1) mechanism using a Dirichlet model and finite diagnostics. Those tests did not settle the relaxed O(1) objective. The new ingredient is an endpoint-vanishing positive probe and the absolutely convergent actual zero-sum identity; it proves divergence for the arithmetic symbol rather than fitting a few windows or changing a constant.

**Other prior routes:** this is not a renamed Schur or structured inverse, scalar prime norm, finite-rank metric repair, source-only small-residual argument, dyadic pair norm, common-Gram off-block factorization, Picone transform, or a new concentration criterion. It closes a scalar simplification of the surviving signed concentration route. It does not revive the negative-only Schatten, commuting-channel, Cotlar, point-value repair, or raw-transfer shortcuts.

**Primary-literature screen (September 21, 2026):**

- [Burnol, Sur les Formules Explicites I: analyse invariante (2000), Theorem2.1](https://arxiv.org/abs/math/0101068): classical explicit-formula foundation and normalization; our limited-regularity extension is supplied by the mollification argument.
- [Suzuki, Weil's quadratic form via the screw function, v2](https://arxiv.org/html/2606.09096v2): nearby finite-window operator setting, not a source of this scalar divergence claim.
- [Zhu, Weil positivity in compact windows, v2, September2,2026](https://arxiv.org/html/2608.24827v2), Sections3 and14: a nearby envelope/cutoff barrier bounds the raw prime comb by its total mass. Our calculation uses the continuum-cancelled beta_a and a negative truncated spectral-atom mass to exclude bounded optimal primitive errors. We do not use its numerical certificates or assert a new priority over general cutoff oscillation theory.

The obstruction is new within the inspected project log. The ingredients are classical; worldwide novelty remains unresolved. It is registered as a proved no-go, not as a new live positive mechanism.

## Remaining target

Retain the signed source-compressed concentration estimate

    −D_a P_a + sum_j w_a,j C_a,u(G_a,j) >= −C_* P_a,

with one finite C_* along a cofinal family, plus the full odd block and any physical blocks/couplings not subordinate to this projection. Here P_a=I−|u_a><u_a| is the actual ordinary source-complement projection and C_a,u is the physical concentration operator. The new theorem says that the primitive budget and the minimum of the scalar symbol cannot supply C_*; favorable and unfavorable frequency levels must be controlled jointly on the physical transform image.

The next concrete lemma is a uniform signed estimate for that joint operator, retaining off-diagonal concentration interactions rather than replacing it by a scalar drawdown or pointwise envelope. No arithmetic proof of this lemma is supplied here. **No G2 gap was closed; RH remains open.**


---

## Delivery policy — September 21, 2026

At the author’s explicit request, manuscript delivery is LaTeX only from this update forward. The previously generated v1.36 PDF is not published or included in the update package. The existing GitHub v1.35 PDF and evidence are archived; the root contains one live LaTeX manuscript. Future runs must not generate or deliver PDFs unless requested again. This changes delivery only, not the mathematical conclusions.

# RH manuscript research log

# Complete manuscript v1.36 — September 21, 2026

# G2.6-RAD-03: dense radicals and the uniform finite-floor reduction

Status: proved reductions and no-go results; no independent signed arithmetic lower bound. G2 and RH remain open.

## Main improvement

For a cofinal family of complete physical windows, it now suffices to prove

\[
q_a[f]\ge-C_*\|f\|_2^2,\qquad f\perp\operatorname{Ran}P_a,
\qquad C_*<\infty\text{ independent of }a,
\]

where P_a is the actual rank-one repaired source or the v1.35 growing radical block, and its already established full operator residual tends to zero. Both parities must be controlled. The finite constant need not tend to zero. This is a sharper sufficient reduction, not a proof of its hypothesis and not a new independent positivity mechanism.

The key proved dichotomy is: either all compact smooth Weil tests are nonnegative, or the complete lower spectral edge tends to minus infinity. If q[f]=-d<0, approximate f in ordinary norm by a finite combination h of translated Gaussian radicals. For w_a=f-chi_a h, the complete residual calculation gives q_a[w_a] -> -d while ||w_a|| -> ||f-h||. Arbitrarily close ordinary approximation amplifies the negative normalized form without bound. The coefficients and required window need not be uniform in approximation accuracy; no effective amplification rate is claimed.

## Domain and exact ingredients

- H=L2(R,dx), I_a=(-a,a), a=log(lambda), first-slot-linear pairing; J_a is zero extension.
- The local operator is the canonical self-adjoint complete Weil operator, with its logarithmic form domain and both pole signs. Smooth compactly supported functions form a core by prop:v118-log-dirichlet.
- The Gaussian radical phi from v1.35 is ordinary-unit normalized, even and double-exponentially decaying. All its real translates are polarized radicals.
- Its Fourier transform is a nonzero entire function, hence nonzero almost everywhere on the real line. Fourier uniqueness proves the span of all real translates is dense in ordinary L2. Reflected translates give dense even and odd spans.
- For every fixed finite translate combination h, the v1.35 exterior-remainder proof gives ||W_a(chi_a h)|| -> 0 and chi_a h -> h. All global prime rows, including those beyond lambda^2, enter that proof. No finite Fourier cutoff occurs.
- These are not claims of density in a global form topology or of uniform approximation coefficients. No global positive closed Weil realization is assumed.

## Further proved obstructions

1. The operators A_a=W_a direct-sum zero on L2(I_a^c) converge strong-resolvent to zero, unconditionally. The same is true after assigning zero to a removed block with ||A_a P_a|| -> 0. The bounded perturbation has norm at most 3||A_a P_a||.
2. Ordinary strong-resolvent convergence therefore cannot be the missing sign input. It does not imply convergence of fixed compact-test form values or control the lower spectral edge.
3. Uniformly bounded positive comparisons B_a, compressed off the actual source, satisfying q_a[f]>=<B_a f,f>-eta_a||f||² with eta_a->0 must tend strongly to zero after zero extension. This rules out any nonzero persistent bounded comparison on the limiting source complement, not all moving matrix metrics.
4. If the actual physical C_a^low removes only even image columns, every odd reflected radical cutoff lies in it exactly. The same strong disappearance is required on every fixed odd vector, regardless of the rank of the even image block. There is no identification of C_a^low with the whole source complement.
5. A fixed closed nonnegative comparison form, with all projected cutoff tests in its domain, must vanish on phi-perp. It can remain nonzero on the source direction. An unspecified domain intersection is insufficient.

## Falsification and sharpness

The exact support-consistent countermodels q_±(x)=±|sum x_k|² on finite sequences share a dense radical and the same zero strong-resolvent limit. Their n-coordinate matrices are ±11*, with nonzero eigenvalue ±n. Thus the negative model has arbitrarily negative lower edges while the positive model is nonnegative. A common finite lower bound distinguishes them; density and resolvent convergence alone do not.

For f=e1, h=e1-(1/m)sum_{k=2}^{m+1}e_k is an exact radical, ||f-h||²=1/m, and q_-(f-h)/||f-h||²=-m. `check_topology_countermodels.py` checks these identities with exact fractions for m=2,4,16,64,256. These are abstract countermodels, not arithmetic numerics or a new finite-window certificate.

Other sharpness checks: escaping rank-one projections have norm one but strong limit zero; unbounded comparisons n²|e_n><e_n| show why uniform operator boundedness cannot be omitted. A source-direction comparison shows why the fixed closed-form conclusion is only vanishing on phi-perp.

An independent adversarial agent checked the dense-translate proof, the arbitrary-center extension of the v1.35 residual, resolvent identities, domains of deleted blocks, both proofs of the finite-floor criterion, parity restrictions, and the distinction between ordinary and form topology. Its report is `adversarial_review.md`.

## Candidate register and novelty screen

**ID:** G2.6-RAD-03.

**Classification:** continuation of RAD-02 and a stronger conditional reduction/no-go; not registered as a new live positivity mechanism. The stable positive-comparison shortcut is rejected. CAP-01b remains a conditional route, now with a bounded-error sufficient target.

**Nearest project proposal:** v1.35's uniformly separated growing lattice of radicals, which gave O(log lambda) near-zero modes and excluded positive polynomial gaps. The new ingredient is totality of all fixed real translates in ordinary L2, together with support consistency of the complete form. A single fixed lattice was not asserted total. This produces an actual strong-resolvent limit and negative amplification, not another eigenvalue count or constant improvement.

**Other formula/dependency comparisons:** signed Schur/residual and structured-inverse routes seek upper bounds on omitted corrections; none is used to infer sign here. Scalar prime-norm, finite-rank repair, dyadic pair norms and common-Gram routes seek positive comparisons or norm bounds; the current results instead constrain their possible limits. Source-only residual arguments are explicitly falsified by q_±. Picone/capacity, continuum cancellation and signed concentration retain arithmetic sign information; the new argument does not replace that information. Negative-only Schatten bounds, commuting-channel assumptions, Cotlar regrouping and primitive transport remain subject to their previous obstructions.

**Primary-literature screening (September 21, 2026):**

- [Wiener, Tauberian Theorems (1932), original article](https://archive.org/download/wiener-1938/wiener1932.pdf): classical translation-density ancestry. The L2 uniqueness proof needed here is supplied in full; no priority claim is made.
- [Connes--Consani, Spectral triples and zeta-cycles, Section 3](https://arxiv.org/abs/2106.01715): the radical structure is classical and already used by the project.
- [Suzuki, Weil's quadratic form via the screw function, v2](https://arxiv.org/html/2606.09096v2), Section 7: discusses derivative operators in Weil-metric quotient completions and a strong-resolvent expectation there. Those are different operators and Hilbert spaces from the ordinary-L2 Weil operators treated here. This distinction prevents a false contradiction or claimed resolution of that conjecture.
- [Connes--van Suijlekom (2025)](https://doi.org/10.1007/s00220-025-05493-1): finite-window quadratic forms and real-zero constructions are nearby context, not an input establishing the cofinal signed floor.
- Searches for a bounded-below Weil criterion also located [Kim et al., v2](https://arxiv.org/abs/2607.24830v2), Section 3.7 of its PDF studies an RMS residual built from a zero sum with factors exp(2a(rho-s))/(rho-s), excluding neighborhoods of ordinates and using finite zero lists in its numerical checks. That is different from a lower bound for the complete Rayleigh form over every physical ordinary-unit test. The present proof uses radical totality and no inserted zero list; that paper is not used to certify the arithmetic floor or worldwide novelty.

The precise specialization is new within the inspected project register. Worldwide novelty is unresolved; an unsuccessful search does not establish it. The manuscript supplies self-contained proofs and makes no priority claim.

## Exact remaining lemma and next step

Construct an explicit arithmetic signed concentration hierarchy with

\[
-D_a P_a+\sum_j w_{a,j}\mathcal C_{a,u}(G_{a,j})\succeq-C_*P_a
\]

on the even source complement, and the corresponding bound with one finite constant on the full odd sector, along a cofinal family. Equivalently pursue the complete complement inequality at the start of this report. The form domain, both parities and the ordinary normalization must be retained. A finite list of windows, a constant depending on a, or a bound only on each fixed vector does not suffice.

The next arithmetic attempt should therefore ask for a uniform O(1) signed lower error before trying to optimize it to o(1). Existing absolute prime-norm estimates grow with lambda and do not prove this. No candidate arithmetic proof has survived yet; the reduction has narrowed what must be estimated without supplying that estimate.

The source sampler, endpoint shell and explicit graph defect are untouched. No lambda=8 calculation was attempted. **No G2 sign gap was closed, and RH is not proved.**


---

# RH manuscript research log

# Complete manuscript v1.35 — September 21, 2026

## G2.6-RAD-02: quantified growing-block obstruction

## Delivery checkpoint

The canonical manuscript/notes replacements (expected version 35) and log
replacement (expected version 39) failed with `transfer_failed`. The v1.35
update ZIP create failed likewise. Keep the existing Library identities;
those canonical saved copies remain v1.34. The complete validated v1.35
snapshot, including this log and its new evidence, is being synced to the
authorized GitHub destination. Subsequent work must compare the remote
manifest/version before restarting from the older Library text. The original
207,224,098-byte cumulative v1.34 archive is still unavailable and is not
replaced by the smaller v1.35 update package.

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


---

# RH manuscript research log

# Complete manuscript v1.34 — September 21, 2026

## G2.6 candidate audit: Cotlar deduplication and optimal primitive transport

This run tested two possible mechanisms for the signed source-compressed
concentration target.  Direct Cotlar--Stein channel splitting is not new:
it leaves the complete operator unchanged.  A genuinely distinct scalar
signed-primitive/Bernstein estimate was proved and optimized exactly, but it
failed the required falsification threshold and is therefore registered as
rejected rather than live.  The existing signed weighted concentration
criterion G2.6-CAP-01b remains the live conditional even-sector mechanism.

### Exact disjoint-channel obstruction

On the even Paley--Wiener range put

\[
 \Pi_{a,u}=\mathcal F_a\mathcal F_a^*
 -|\widehat{\widetilde u_a}\rangle
  \langle\widehat{\widetilde u_a}|.
\]

For

\[
 E_a=[-1/(10a),1/(10a)],\qquad
 F_a=[-3/(10a),-1/(5a)]\cup[1/(5a),3/(10a)],
\]

the exact sinc-kernel test with normalized even indicators proves

\[
 \liminf_{a\to\infty}\|1_{E_a}\Pi_{a,u}1_{F_a}\|
 \ge {73\over375\pi}>0.0619.
\]

The source correction tends to zero by the proved strong source limit and
absolute continuity on the shrinking bands.  Thus even disjoint
fixed-ratio reciprocal channels retain a cofinal cross interaction.  This
does not rule out a Cotlar estimate with summable scale difference; it proves
that adjacent interactions cannot be declared small.

More decisively, for

\[
 Z_af=(\sqrt{w_{a,j}}1_{B_{a,j}}\mathcal F_af)_j,
\]

one has the exact identity

\[
 Z_a^*Z_a=P_a\mathcal F_a^*
   \left(\sum_jw_{a,j}1_{B_{a,j}}\right)\mathcal F_aP_a.
\]

Splitting, merging or regrouping the channels does not change the target.
Repeated-channel examples show that diagonal channel norms can tend to zero
while the complete Gram is fixed.  Any Cotlar argument must retain the cross
terms and prove the original signed margin; otherwise it is the v1.28 block
norm comparison in different coordinates.

### Candidate register entry G2.6-PT-01

**Name:** signed primitive transport with the Paley--Wiener Bernstein bound.

**Precise inequality:** for the exact even symbol let

\[
 \Delta_a=\sup_{x<y}\left(-\int_x^y\beta_a(\xi)d\xi\right)_+.
\]

Then every physical test supported in `[-a,a]` satisfies

\[
 \int\beta_a|\widehat f|^2\ge-a\Delta_a\|f\|^2.
\]

Therefore `a Delta_a -> 0` would prove the even v118 gap-free estimate on
the whole physical space, hence on the actual source complement.

**Exact optimization:** among all scalar decompositions
`beta_a=b_a+W_a'`, `b_a>=0`, the least centered `L-infinity` norm of
`W_a` is exactly `Delta_a/2`.  It is achieved by subtracting the running
maximum of a primitive of `beta_a`.  Integration by parts and
`||F'||_2=||xf||_2<=a||f||_2` then give the displayed bound.  The use of a
primitive based at a finite point is essential; the prime cosine terms do
not have an improper primitive from minus infinity.

**Physical space and domain:** the inequality holds for all of
`L^2(-a,a)` after zero extension, with no Fourier cut and the unitary Fourier
normalization used in the manuscript.  It therefore applies to the actual
normalized source complement.  Finite-rank source removal cannot improve the
generic factor `a`: even endpoint strips contain an infinite-dimensional
space after any finite number of constraints.

**Essential new ingredient:** one-dimensional signed primitive transport
and the physical derivative bound.  This retains positive shoulders around
negative wells before taking an ordinary norm.

**Nearest prior proposals and formula-level distinction:** unlike the signed
Schur and structured-inverse routes it has no head/tail solve; unlike scalar
prime norms it estimates the complete signed symbol; unlike finite-rank
metrics, dyadic pair metrics and v1.28 common-Gram factorization it has no
matrix metric or off-block factorization; unlike source-only residual bounds
it is valid on the whole physical space; unlike CAP-01b it uses cumulative
signed interval area rather than concentration operators.  It is a distinct
sufficient estimate inside the continuum-symbol route, not a coordinate
change.  The mathematical ingredients are classical; the exact arithmetic
drawdown optimization is new within this project.  Worldwide novelty is not
claimed.  The Bernstein--Nikolsky literature is the closest primary source.

**Adversarial failure:** for the exact positive Dirichlet model already used
in v1.32,

\[
 \beta_a^{\rm mod}(\xi)=a^2\xi^2-\pi^2/4,
 \qquad \Delta_a^{\rm mod}=\pi^3/(6a).
\]

The form is nonnegative and its normalized cosine source is an exact null
vector, yet the optimal primitive error is the fixed constant `pi^3/6`.
Thus positivity plus a perfect source does not imply the proposed decay.

A non-rigorous scan of the actual arithmetic symbol gave `a Delta_a`
approximately `2.5448, 3.4002, 4.9148, 5.5052` at lambda `3,4,5,6`.
These values are diagnostic, not interval certificates or a cofinal no-go.
They show no evidence of the required decay.

**Status:** rejected as a live candidate.  It did not survive the meaningful
Dirichlet-model and arithmetic falsification tests.  It remains a valid exact
sufficient criterion.

### Surviving candidate and exact remaining lemma

**Retained live candidate:** G2.6-CAP-01b, the signed source-compressed
weighted concentration inequality

\[
 -D_aP_a+\sum_jw_{a,j}\mathcal C_{a,u}(G_{a,j})
 \succeq-\eta_aP_a,\qquad\eta_a\to0.
\]

No formulaically distinct candidate survived this run.  Its exact remaining
lemma is unchanged: prove the displayed inequality for an explicit arithmetic
hierarchy along a cofinal family, retaining every cross-channel and the actual
source.  The odd sector remains a separate obligation.  No G2 sign gap was
closed and RH is not proved.

### Reproducibility

- `g2_primitive_transport/adversarial_cotlar_review.md`: independent exact
  disjoint-channel proof and deduplication audit.
- `g2_primitive_transport/adversarial_signed_primitive_review.md`: exact
  primitive optimization, source-complement audit and Dirichlet obstruction.
- `g2_primitive_transport/test_primitive_transport.py`: non-rigorous arithmetic
  drawdown diagnostic; no lambda 8 run.

# Complete manuscript v1.33 — September 21, 2026

## Development of G2.6-CAP-01b: exact leakage algebra and a cofinal no-go

This run tested a proposed simplification of the signed source-compressed concentration hierarchy: nested reciprocal-scale bands might become asymptotically commuting after removal of the repaired source. The proposal is false in that generality. No new candidate is registered; CAP-01b remains the live conditional even-sector mechanism.

### Exact Toeplitz--leakage identities

On the even physical space let (J=\mathcal F_a), (Pi=JJ^*),

\[
C_E=J^*1_EJ,\qquad H_E=(I-\Pi)1_EJ.
\]

Then

\[
C_EC_F=C_{E\cap F}-H_E^*H_F,
\qquad [C_E,C_F]=H_F^*H_E-H_E^*H_F.
\]

For the actual normalized source (u_a), put (P_a=I-|u_a\rangle\langle u_a|), (A_E=P_aC_EP_a) on (u_a^\perp), and (v_E=P_aC_Eu_a). In the fixed first-slot-linear convention,

\[
[A_E,A_F]=P_a(H_F^*H_E-H_E^*H_F)P_a
+|v_F\rangle\langle v_E|-|v_E\rangle\langle v_F|.
\]

No source term has been dropped. With (L_Ef=(H_Ef,\langle f,v_E\rangle)),

\[
A_EA_F=A_{E\cap F}-L_E^*L_F,
\quad [A_E,A_F]=L_F^*L_E-L_E^*L_F,
\quad A_E-A_E^2=L_E^*L_E.
\]

This is the classical Toeplitz--Hankel product-defect algebra, derived directly in the present even-interval normalization.

### Certified reciprocal-band obstruction for the actual source

Scale (L^2_{\rm ev}(-a,a)) to (L^2_{\rm ev}(-1,1)) and take

\[
E_a=[-1/(10a),1/(10a)],\qquad
F_a=[-1/(5a),1/(5a)].
\]

The uncompressed operators become fixed interval concentration operators (C_{1/10},C_{1/5}). Exact Taylor bounds, evaluated between the normalized Legendre modes (e_0=1/\sqrt2) and (e_2=\sqrt{5/8}(3x^2-1)), prove

\[
\|[C_{1/10},C_{1/5}]\|>9\times10^{-6}.
\]

This is an analytic rational certificate, not a numerical eigenvalue test. The separate degree-four verifier gives the stronger bound (>1.198\times10^{-5}).

Lemma `lem:v115-source-mass` proves that the normalized repaired source converges strongly on the unscaled logarithmic line to a fixed nonzero vector. After interval dilation it converges weakly to zero. Fixed concentration operators are compact, so their action on the dilated source tends to zero and source compression changes them by (o(1)) in operator norm. Therefore

\[
\liminf_{a\to\infty}\|[A_{E_a},A_{F_a}]\|>9\times10^{-6}.
\]

This is a cofinal result for the actual source. It does not identify the chosen bands with the arithmetic superlevels of (eta_a), so it does not falsify CAP-01b. It proves that nesting, reciprocal scale and the known source limit do not imply approximate simultaneous diagonalization.

### Candidate register and novelty screening

**Retained candidate:** G2.6-CAP-01b, signed source-compressed weighted concentration.

**Status:** live conditional even-sector mechanism; no G2 gap closed.

**Proposed simplification tested:** asymptotic commutation of nested concentration operators.

**Result:** rejected as a generic mechanism by the actual-source reciprocal-band theorem above. Even exact commutation would be insufficient without a separate weighted coverage lower bound.

**Nearest literature:** Brown--Halmos Toeplitz product algebra and the Widom/Virtanen Toeplitz--Hankel product formula; Landau--Pollak concentration theory supplies the physical operators. These are known mechanisms. The explicit source-compressed identities are new bookkeeping within this project; the actual-source reciprocal-band obstruction is a new project result. Worldwide novelty is not claimed.

**Deduplication:** the joint maps (L_E) form a common Gram only for concentration product defects. They do not factor the signed Weil off-blocks and therefore do not close or replace the v1.28 common-Gram proposal. Registering them as a new positive mechanism would be a relabeling. The result also differs from signed Schur/structured-inverse estimates, scalar prime norms, finite-rank repairs, source-only residual arguments and dyadic pair metrics because it is an exact physical Paley--Wiener product identity followed by a cofinal counterexample.

### Exact surviving lemma

For cofinite good sets (G_{a,j}), let (B_{a,j}=\mathbb R\setminus G_{a,j}) and

\[
Z_af=(\sqrt{w_{a,j}},1_{B_{a,j}}\mathcal F_af)_j,
\qquad f\perp u_a.
\]

The complete joint-channel target is

\[
\|Z_a\|^2\le\sum_jw_{a,j}-D_a+\eta_a,
\qquad \eta_a\to0.
\]

Its block Gram retains all channel overlaps and the actual source before taking a norm. It is algebraically equivalent to the existing signed weighted concentration inequality, not a new theorem. The exact remaining task is to prove it for an explicit arithmetic hierarchy or produce a different genuinely signed physical factorization. The odd sector remains separate. No G2 sign gap was closed and RH is not proved.

### Files and reproducibility

- `certify_scaled_commutator.py`: exact-rational derivation and certificate.
- `scaled_commutator_certificate.json`: machine-readable bound.
- `adversarial_nested_commutator_review.md`: independent derivation, scope audit and formula-level novelty comparison.

# Complete manuscript v1.32 — September 21, 2026

## Development of G2.6-CAP-01b: Schatten refinement and exact no-go tests

This run retained the v1.31 signed weighted concentration mechanism and tested two possible simplifications. Neither is registered as a new candidate: the Hilbert--Schmidt estimate is a scalar continuation of CAP-01b, and positive flat-top smoothing is impossible except for the identity kernel.

### Exact source-compressed second moment

For (C_E=\mathcal F_a^*1_E\mathcal F_a), normalized source (u_a), and (P_a=I-|u_a\rangle\langle u_a|), cyclicity gives

\[
\operatorname{tr}(P_aC_EP_a)^2
=\operatorname{tr}(C_E^2)-2\|C_Eu_a\|^2
+\langle C_Eu_a,u_a\rangle^2.
\]

Therefore the exact negative-level coefficient may use

\[
\|P_aC_EP_a\|\le
\min\{1,\operatorname{tr}(P_aC_EP_a),
\|P_aC_EP_a\|_{HS}\}.
\]

This is a valid strengthening of the v1.31 trace bound and includes the actual source before taking a scalar majorant.

### Structural no-go for negative-only budgets

The strengthening is not a uniform mechanism by itself. For the nonnegative Dirichlet model

\[
q_a[f]=a^2\|f'\|^2-\frac{\pi^2}{4}\|f\|^2,
\qquad u_a(x)=a^{-1/2}\cos\frac{\pi x}{2a},
\]

(u_a) is an exact null source. Its negative multiplier levels scale by (a^{-1}), so dilation makes every source-compressed concentration operator independent of (a). The integrated Hilbert--Schmidt budget is consequently a fixed positive number. Complete positivity and a perfect source therefore do not imply vanishing of any negative-only layer-cake/Schatten coefficient.

Min--max additionally proves

\[
\|P_aC_EP_a\|\ge\lambda_2(C_E),\qquad
\|P_aC_EP_a\|_{HS}^2\ge\sum_{j\ge2}\lambda_j(C_E)^2.
\]

One source direction cannot remove a second concentration channel.

### Exact global-index obstruction

The exact-rational verifier `certify_beta4_negative.py` proves

\[
-0.64784909<\beta_{\log4}(1)<-0.6321938<-3/5.
\]

Continuity supplies an open negative interval. Arbitrarily many even Schwartz functions with disjoint Fourier supports in that interval give infinite negative index for the full-line multiplier, surviving every fixed finite number of constraints. This rules out a global finite-negative-index/conditional-positive-definite strengthening. It does not contradict the certified positive physical lambda-4 form, because the full-line tests are not supported in the physical window.

### Exact flat-top obstruction

If a positive probability measure has characteristic function equal to one near zero, positivity of (1-\cos(t\xi)) forces the measure to be a point mass at zero. Hence no nontrivial positive frequency smoothing can be exact on every physical difference (|x-y|\le2a). A signed flat-top kernel can be form-exact, but making its extension nonnegative is a separate sign problem.

### Adversarial computations

Binary64 finite cosine compressions were run only at lambda 3, 4 and 5. In the largest tested frequency windows/dimensions, the integrated second concentration eigenvalue was approximately 0.72, 1.12 and 1.25. These are non-certified lower diagnostics, not physical sign results. Canonical signed trapezoid flat-top kernels also left the located negative wells negative. The exact analytic no-go results do not depend on these computations.

### Candidate register and novelty

**Candidate:** G2.6-CAP-01b, signed source-compressed weighted concentration.

**Status:** live conditional even-sector mechanism; no G2 gap closed.

**Formula:** choose a pointwise step minorant

\[
-D_a+\sum_jw_{a,j}1_{G_{a,j}}\le\beta_a
\]

and prove

\[
-D_aP_a+\sum_jw_{a,j}\mathcal C_{a,u}(G_{a,j})
\succeq-\eta_aP_a,\qquad \eta_a\to0.
\]

**Essential project-new ingredient:** favorable and unfavorable levels of the exact arithmetic symbol remain coupled in one Loewner-order operator sum after removing the actual source. The current run proves that replacing this by negative-only Schatten moments or positive form-exact smoothing loses the mechanism.

**Nearest literature and classification:** Landau--Pollak concentration theory, Nazarov uncertainty estimates and Kovrijkine's Logvinenko--Sereda theorem remain the closest classical foundations. The general machinery is known; the arithmetic signed hierarchy is new within this project. Worldwide novelty is not claimed.

**Deduplication:** formula comparison again distinguishes CAP-01b from the signed Schur/residual and structured-inverse routes, scalar prime norms, finite-rank metric repairs, source-only residual arguments, dyadic pair-norm metrics and the v1.28 common-Gram factorization. The Hilbert--Schmidt formula is explicitly classified as a continuation, not a new candidate.

**Exact remaining lemma:** construct an explicit finite or convergent arithmetic hierarchy satisfying the signed weighted concentration inequality with ordinary error tending to zero along a cofinal family. The odd sector remains separate. No G2 sign gap was closed and RH is not proved.

# Complete manuscript v1.31 — September 21, 2026

## Development of G2.6-CAP-01: source-compressed weighted concentration

This run developed the v1.30 continuum-symbol candidate rather than registering a renamed route. The essential new ingredient is a hierarchy of source-compressed Paley–Wiener concentration operators that retains favorable as well as unfavorable levels of the exact arithmetic symbol.

### Exact operator criterion

On the even physical space (H_a^ev=L²_ev(-a,a)), let (F_a) be zero extension followed by the unitary Fourier transform, let (u_a) be the normalized repaired source, and put (P_a=I-|u_a><u_a|). For symmetric measurable (E), define

\[
C_{a,u}(E)=P_aF_a^*1_EF_aP_a.
\]

This is a positive contraction on the actual source complement, with no Fourier cutoff. If (D_a=||(beta_a)_-||_infty) and (E_a(t)={beta_a<-t}), then the exact layer-cake argument proves

\[
q_W[f]\ge-\eta_a^{op}\|f\|²,
\qquad
\eta_a^{op}=\int_0^{D_a}\|C_{a,u}(E_a(t))\|dt.
\]

For finite-measure (E), the trace is exact:

\[
tr C_{a,u}(E)=\int_E\left[
\frac{a+\sin(2a\xi)/(2\xi)}{2\pi}-|\widehat{\widetilde u_a}(\xi)|²
\right]d\xi.
\]

The full symmetric-set convention contains both frequency signs; if only the positive half is integrated, the integrand must be doubled. Evenness and source removal are therefore included rather than appended heuristically.

The sharper surviving criterion chooses symmetric sets (G_{a,j}) and positive weights (w_{a,j}) satisfying the pointwise step minorant

\[
-D_a+\sum_jw_{a,j}1_{G_{a,j}}\le\beta_a
\]

and proves

\[
-D_aP_a+\sum_jw_{a,j}C_{a,u}(G_{a,j})\succeq-\eta_aP_a,
\qquad \eta_a\to0.
\]

This implies the even v118 gap-free estimate without a positive complement gap. It controls the complete even rank-one complement required there; it does not identify that space with the physical block (C_a^low).

### Scalar route tested and rejected as presently inadequate

The trace specialization is rigorous but discards all favorable symbol mass. On grids truncated at |xi|<=5000, its already accumulated values are approximately 2.1363, 3.2440 and 4.5622 for lambda 3, 4 and 5. These are diagnostic lower accumulations for the complete scalar upper bound, not certified enclosures.

For the two-level good set (G_a(theta)={beta_a>=theta D_a}), a concentration lower bound (C(G)>=pP) gives exactly

\[
q_W[f]\ge D_a((1+\theta)p-1)\|f\|².
\]

Thus reciprocal-scale thickness alone is insufficient: the concentration constant must be near (1+theta)^(-1), while generic Logvinenko–Sereda constants are far smaller. This rules out claiming that a standard thick-set theorem closes the arithmetic estimate. It does not rule out the full weighted hierarchy.

### Adversarial compact-support test

Even packets proportional to cos(pi x/(2a))cos(omega x) were centred at the deepest located wells for lambda 3, 4 and 5 only. The symbol point values were approximately -2.37816, -3.41944 and -5.01788, but the complete packet Rayleigh quotients were +0.951081, +2.757308 and +3.683514. Independent physical archimedean/prime/pole quadrature agreed with Fourier integration to about 3e-10. This is numerical evidence only. It fails to falsify the weighted mechanism and illustrates why beta-plus cannot be discarded.

### Novelty and prior-route comparison

Classification: substantive project-new development of G2.6-CAP-01; no claim of worldwide novelty. Time-frequency concentration and Logvinenko–Sereda theory are classical. The formula is distinct from prior signed Schur/residual and structured-inverse estimates, scalar prime norms, finite-rank repairs, source-only residuals, dyadic tail metrics and the v1.28 common-Gram factorization: it uses the complete exact arithmetic Fourier symbol and compresses physical Paley–Wiener concentration off the actual source before taking any scalar comparison. It is also distinct from v1.30's scalar uncertainty suggestion because the essential surviving object is the signed weighted sum of concentration operators, not thickness or the trace of the negative set.

Nearest literature: Landau–Pollak concentration theory, Nazarov's finite-measure uncertainty theorem, and Kovrijkine's quantitative Logvinenko–Sereda theorem. None proves the required signed arithmetic operator inequality with cofinal constants.

### Exact remaining lemma

Construct an explicit finite or convergent superlevel hierarchy satisfying the step minorant and prove its source-compressed weighted concentration operator is at least (-eta_a P_a) with eta_a->0 along a cofinal family. The constants must retain the full dependence on a, the source and all arithmetic levels. The odd sector remains separate.

No G2 sign gap was closed and RH is not proved.

# Complete manuscript v1.30 — September 21, 2026

## Development of G2.6-CAP-01: continuum cancellation and a perturbative no-go

This run developed the existing source-weighted capacity candidate rather than registering a renamed mechanism. The new essential ingredient is the exact PNT-continuum prime kernel

\[
K_a^+(x,y)=e^{|x-y|/2}.
\]

On the even sector the existing pole cancels its only harmful channel exactly:

\[
2|\cosh(\cdot/2)\rangle\langle\cosh(\cdot/2)|-K_a^+
=K_a^-+2|\sinh(\cdot/2)\rangle\langle\sinh(\cdot/2)|,
\quad K_a^-(x,y)=e^{-|x-y|/2}.
\]

The sinh term vanishes on even functions and (K_a^-\succ0), with Fourier multiplier ((\xi^2+1/4)^{-1}). It is compact on the physical interval and therefore supplies no positive uniform gap.

### Exact arithmetic symbol

For the exact prime correlation (C_a), put (R_a=C_a-K_a^+). Its full-line multiplier after zero extension is

\[
\mathfrak r_a(\xi)=2\sum_{1<m<e^{2a}}\frac{\Lambda(m)}{\sqrt m}\cos(\xi\log m)
-2\int_0^{2a}e^{t/2}\cos(\xi t)dt.
\]

Combining the archimedean multiplier with (K_a^-) gives the exact even symbol

\[
\beta_a(\xi)=\Re\psi(5/4+i\xi/2)-\log\pi-\mathfrak r_a(\xi),
\qquad
q_W[f]=\int\beta_a(\xi)|\widehat{\widetilde f}(\xi)|^2d\xi.
\]

Thus the live lemma is the support- and source-constrained estimate

\[
\int\beta_a|\widehat{\widetilde f}|^2\ge-\eta_a\|f\|^2
\quad(f\perp u_a,\ f\text{ even},\ \operatorname{supp}f\subset[-a,a]),
\qquad \eta_a\to0.
\]

Together with the proved source residual this is sufficient for the even v118 gap-free conclusion. It controls the whole even rank-one complement, not merely (C_a^{low}); no unproved identification of those spaces is made.

### Rigorous falsification of the vanishing-remainder shortcut

The remainder (R_a) is not (o(1)) on the actual source complement. Let (\ell=\log2), (d=0.1), (0<\varepsilon<0.01), and choose an even bump (\phi\) supported in ((-\varepsilon,\varepsilon)). With (c_{\pm1}=1), (c_0=-2\cosh(d/2)), form six bumps centered at (\pm\ell/2+jd). Their total diameter is below (\log3), so only the prime-2 shift correlates. Both exponential moments vanish exactly. Hence

\[
\langle R_ag_\phi,g_\phi\rangle>
\frac{\log2}{\sqrt2}\|g_\phi\|^2.
\]

The full bump family is infinite-dimensional, so the ordinary (o(1)) bound fails after removal of any finite-dimensional block at each window. A fixed two-complex-dimensional subfamily always contains a nonzero vector perpendicular to the rank-one source, while its fixed archimedean reference energies remain uniformly bounded. Therefore neither (R_a\preceq\eta_aI) with (\eta_a\to0), nor (R_a\preceq\alpha_aA_{ref}+\eta_aI) with both coefficients tending to zero, can hold on the source complement. This does not rule out absorption by the full archimedean energy with a fixed sharp coefficient.

### Novelty and prior-route comparison

This is a substantive development of CAP-01, not a separate candidate. The exact kernel cancellation and scalar discrepancy symbol were not present in the prior Schur/inverse, scalar prime-norm, finite-rank metric, source-only residual, dyadic pair-norm or common-Gram proposals. It differs from the withdrawn moving-Hardy continuum estimate: no translated test, endpoint ratio, absolute PNT gain or reflected-pole damping is used. The general Fourier/uncertainty framework is classical; no worldwide novelty is claimed.

### Result and next lemma

Established: exact continuum cancellation, exact even discrepancy symbol, and an exact no-go for treating the discrepancy as a vanishing perturbation. Numerically, the stronger pointwise condition (\beta_a\ge-o(1)) fails at already positive fixed windows; those values are diagnostics only. The remaining proof must exploit physical support uncertainty or concentration in the full signed symbol, not a norm estimate on the remainder. The odd sector remains separate.

No G2 sign gap was closed and RH is not proved.

# Complete manuscript v1.29 — September 21, 2026

## Candidate register: G2.6-CAP-01

**Name:** source-weighted nonlocal jump-capacity absorption.  
**Classification:** new within this project; ground-state/Picone machinery is known in the literature; worldwide novelty is not claimed.  
**Status:** live conditional even-sector mechanism. No G2 gap closed.

### Exact fingerprint

On the centered physical interval, retain the zero-extension killing terms and write the even Weil form as a nonnegative archimedean-plus-prime jump form, the exact scalar potential (c_{ar}-2P_\lambda), and the positive cosh pole. For any positive zero-free even (h), the exact Picone identity is

\[
q_W[hg]=E_{\lambda,h}[g]+\int (H_\lambda h/h)|g|^2h^2dx
       +2|\int gh\cosh(x/2)dx|^2,
\]

where (H_\lambda=W_\lambda-2|c\rangle\langle c|). For the actual removed near-radical (u_\lambda), impose the exact constraint (\int gh\overline u_\lambda=0). The candidate lemma absorbs the negative part of (Hh/h) into the weighted jump energy and positive pole, up to ordinary error (\eta_\lambda\). Together with (\|Wu_\lambda\|\le\epsilon_\lambda), v118-gap-free gives lower error (\eta_\lambda+2\epsilon_\lambda/\sqrt3), with no complement spectral gap.

### Essential new ingredient and deduplication

The essential ingredient is a physical-space nonlocal ground-state transform followed by a source-constrained capacity inequality. It preserves joint prime/archimedean edge signs before any Fourier split. Formula comparison shows it is not the prior signed Schur/structured-inverse route, scalar prime-norm bound, finite-rank metric repair, source-only residual argument, dyadic pair-norm metric, or v1.28 shared-channel/common-Gram off-block factorization. The old generic Perron suggestion did not contain this exact killed-jump identity, favorable-pole term, source constraint or a capacity estimate. This is nevertheless an established mathematical technique, not a new general theorem.

Primary literature screen: Frank–Seiringer, *Non-linear ground state representations and sharp Hardy inequalities*, JFA 255 (2008), arXiv:0803.0503v2; Chen–Wang, *Functional inequalities for nonlocal Dirichlet forms with finite range jumps or large jumps*, arXiv:1212.6100v2. These support the method class but do not provide the arithmetic inequality or cofinal constants.

### Adversarial checks and falsification attempt

- The exact diagonal constant is (\psi(1/4)-\log\pi=-\gamma-\log(8\pi)-\pi/2). Exterior killing must remain with the constant (-2P_\lambda).
- Pointwise (Wh\ge0) is not sufficient: incorporating the positive pole into (Wh/h) creates a negative weighted variance term.
- The saved lambda3, N64 compressed projected source ratio has numerical minimum about -0.413827 and is negative on 44.9503% of a dense grid, representing about 32.3325% of its source-weighted mass. This falsifies the stronger finite pointwise-supersolution shortcut.
- The compressed ratio is not the complete physical ratio. A positive nonzero endpoint weight has positive logarithmic boundary growth under the killed continuous jump operator.
- The finite transformed absorption ratio is one at binary64 resolution. It supplies no certified margin and warns that the mechanism can be tautological without an independent capacity argument.

### Scope and exact next lemma

The proposition controls the whole even rank-one complement, not automatically (C_a^{low}). A subspace inclusion must be proved or all remaining blocks and couplings accounted for. The odd sector is untouched because its sinh pole is negative.

The exact next lemma is: choose an explicit zero-free (h_\lambda) and prove the full-domain source-constrained absorption inequality with (\eta_{\lambda_j}\to0) on a cofinal family. A generic Poincaré constant, ordinary residual estimate, another fixed-window certificate or an unjustified source-to-physical transfer is insufficient. Full G2 additionally requires the odd sector. Detailed formulas and classification are in `g2_capacity_candidate/g2_capacity_candidate_report.md`.

The complete manuscript integrates the exact identity and conditional implication. No G2 sign gap was closed and RH is not proved.

# Complete manuscript v1.28 — September 21, 2026

## Tested target and result

User requested a test of the new signed block-metric criterion. We froze lambda=5, N=lambda^2=25, literal dyadic blocks26..50,51..100,101..200,201..400, and maximal admissible metrics M_j=T_jj. This is a new construction, not unchanged transfer of the already false Q16 metric. No lambda8 calculation or alternate cutoff was run.

**The proposed norm-row criterion fails on this partition in both parities, even for every smaller admissible positive block metric and every positive scalar row reweighting.** Each of the four signed diagonal blocks is certified positive, but the exact nonnegative coupling-lower matrices have largest eigenvalue at least1.539632 even and1.6014215 odd. Every infinite extension inherits this obstruction. No negative Weil vector or complete lambda5 sign was proved; its complete generalized certificate margin remains unavailable.

## Computational evidence upgraded to proof

The floating-point pilot proposed Cholesky congruences and pair singular vectors; it is not proof evidence. Exact dyadic witnesses are evaluated at320 and448 bits using96-term analytic coefficient enclosures. All eight congruence matrices pass C_j T_jj C_j* >0.99I, certifying actual diagonal-block positivity without assuming proposal accuracy. All twelve pair quotients have positive denominators and strictly exceed the rational entries of H with denominator1e6.

Even entries01,02,03,12,13,23:999998,570610,337575,483821,196957,490303. Odd:999998,486261,324229,614752,289700,487903. The exact uniform-vector Rayleigh gates are6158528/4000000 and6405686/4000000. Already the leading three blocks give4108858/3000000>1 and4202022/3000000>1.

Both precision replays retain identical pair/congruence hashes and rational matrices. The adversarial agent independently expanded all twelve pairings to signed Fourier indices at448 bits, bypassing the parity block assembler and all proposal solvers. It confirmed normalization, signs, positive energies, rational lower bounds and interval overlaps. This shares the audited analytic coefficient formulas and Arb, and is not external verification or an independent analytic kernel derivation.

## Analytic extension of the failed gate

For any M_j<=T_jj, the normalized coupling norm equals the supremum of |x*T_jk y| divided by sqrt((x*M_j x)(y*M_k y)). Thus the maximal metrics minimize every individual coupling norm. Any successful weighted row test would imply H w<=b w with positive w and b<1. Similarity by diag(w) would force the spectral radius of H below1, contradicting its certified Rayleigh bound. Omitted norm terms are nonnegative, so no remote upper enclosure is needed to prove this failure.

A simple positive model T=I/4+3*11*/4 has pair-norm comparison radius3/2 despite positive eigenvalues1/4,1/4,5/2. This illustrates information lost by independent pair norms; it is not an identified model of the arithmetic operator. No claim about all polynomial cutoffs, all partitions or asymptotic impossibility is made.

## Next concrete step

Do not spend another run shrinking these metrics, rotating their coordinates or optimizing scalar row weights: the proved obstruction covers those modifications on this partition. Seek a genuinely signed joint estimate or a consistent shared-direction factorization of the normalized off-blocks, with a complete signed remainder. The review records the exact identity for a hypothetical common Gram channel E_jk=Z_jZ_k*+R_jk, but no such actual Weil factorization or uniform remainder estimate is asserted. Changing the cutoff or partition is a distinct experiment and must be identified as such.

The complete176-page v1.28 manuscript compiles without warnings and has been visually checked throughout, with new proofs inspected individually. All523previous labels and72historical dispositions are preserved. It integrates the new obstruction, keeps the abstract criterion correct, and distinguishes comparison eigenvalues from generalized certificate and resolution margins. It retains weak G1, complete lambda4 positivity, the physical endpoint, diagonal, scale factors, first-slot-linear convention and explicit sampler graph defect. No growing-window G2 sign gap was closed and RH is not proved.

# Complete manuscript v1.27 — September 21, 2026

## Outcome, in requested order

**The lambda5 construction does not transfer unchanged.** The frozen Q16 metric W5 >= 1e-8 D_arch is rigorously false in both parities. The necessary modification is to the outer head or the metric itself; no successful tuning rule was found. The full pipeline stopped before outer trials or inverse correction. Its complete generalized certificate margin is unavailable. No resolution margin or finite-prefix result substitutes for it, and no positive lambda5 metric or structured inverse factors were produced.

Separate obstruction reports, exact dyadic witnesses, protocol, original replays and an independent signed-index verification are saved in g2_lambda5_transfer/. No lambda8 calculation was performed during this checkpoint.

## Frozen protocol and attempted transfer

The complete archived lambda4 scripts use literal support sizes, without a general window-dependent support rule. We froze those sizes rather than importing the different finite-resolution probe's lambda-squared head rule. The record includes scaling, preconditioner, CG depths, support, tau and moment orders before testing. Its SHA256 is 6de75f0e5121fb4a452de7f0518418820c2acb113b9c02915c450f42875dff1e.

Fresh physical constants at lambda5 cause negative first far weights at the frozen N512 even and N1536 odd cuts: approximately -1.0764504091 and -1.5489108675. For the same scalar formula the first positive cuts are1502 and7224. We did not confuse this with falsity of the actual metric: we next tested that precise required inequality by negative shifted quadratic witnesses, as permitted in the stopped protocol.

Exact frozen vectors on modes17..128 give W/D in (2.0806767455e-18,2.0806767456e-18) even and (6.7808574118e-17,6.7808574120e-17) odd. Both W values are positive and both W-1e-8D values negative. Outward320/448-bit replays and a separate448-bit signed-index assembly confirm them. The second assembly bypasses the parity block routine but shares the analytic coefficient enclosures and Arb. Finite support makes the complete quadratic exactly finite, so this is a counterexample to the complete shifted tail metric with no missing remote enclosure.

Increasing remote cutoff, moment order or CG depth cannot fix this false inequality. Keeping Q16 and a common scalar cD forces c below2.0806767456e-18; this is necessary, not a sufficient certified replacement. No weaker metric or larger physical head was silently adopted. No negative Weil vector or RH counterexample was found.

## New analytic route obstruction and surviving G2.6 definition

For an arbitrary fixed even repair bump psi, with psi(0)=1, integral zero and actual support radius b<1, the windowed repaired map B_lambda(h-h(0)psi) is not closable in sourceL2 whenever lambda>1/b. The sequence psi(t/epsilon) tends to zero in sourceL2 and has identically zero uncorrected windowed image for epsilon b<1/lambda, while its repaired image is the same nonzero -B_lambda psi. This closes bounded global L2 transport through that repair. It does not invalidate fixed smooth sources, weakG1, finite repaired spans, or Connes–Consani's actual finite-image projection construction.

G2.6 now uses exact source thresholds c=2pi lambda^2, explicit moment repairs, physical image matrices and their Grams. Source concentration counts alone prove neither physical rank nor stability. The growing removed-block residual is exactly ||Gamma^-1/2(AG)*(AG)Gamma^-1/2||. The signed ordinary-error complement target in reference D coordinates is Pi(K+eta D^-1)Pi>=0, where Pi projects off D^-1/2G, not off G. This is an exact reformulation, not a proved sign. The existing rank-one source residual remains usable with the gap-free proposition; a growing deep block requires its own normalized bound.

## Non-scalar metrics: a proved limitation and a live candidate

User asked whether matrix tail metrics could allow polynomial cutoffs. We proved that no invertible congruence or polynomial-rank correction can repair the old unsigned diagonal comparison at polynomial N: every n with N<n<L exp(kappa/(1-c)) is negative, and a rank-r correction leaves a negative direction whenever r is smaller than that subspace dimension. Since kappa>=||T_prime||~lambda, the negative dimension is exponential. This conclusion concerns the weakened comparison only, not the actual Weil form.

Infinite signed-block metrics are not excluded. A sufficient theorem keeps T_jj>=M_j>0 within each block and controls sup_j sum_{k!=j} ||M_j^-1/2 T_jk M_k^-1/2|| by rho<1. It yields T>=(1-rho) directsum M_j on the actual common form core/closed extension. A finite block list is insufficient. Uniformly verifying this above N=C lambda^p is still an open arithmetic problem; no polynomial-cutoff theorem for Weil was claimed. Both analytic arguments and domain qualifications passed adversarial review.

## Next concrete step and scope

The unchanged lambda5 route is closed. Before launching a modified complete certificate, derive an independently positive signed block metric and control its complete inter-block couplings with explicit window dependence. In parallel, use the corrected physical Gram projection in any G2.6 estimate. Do not reuse source concentration counts as a physical sign or ignore the eta D^-1 factor. A finite far-block success would still leave the full head Schur correction and cofinal ordinary-error decay.

The complete v1.27 manuscript is173pages with523unique labels, preserving all514prior labels and all72historical dispositions. It compiles without LaTeX warnings and is visually checked throughout. The previous complete lambda4 positivity, weakG1, first-slot-linear convention, physical endpoint, exact diagonal, scale factors and explicit sampler graph defect are retained. No G2 sign gap or RH proof is claimed.

# Complete manuscript v1.26 — September 21, 2026

## Established result and scope

**The complete lambda = 4 sign problem is closed.** The odd sector is now strictly positive on the full closed form domain; combined with the previously proved even sector, the canonical full Weil form is positive and epsilon_4 = 0 exactly. This is an internal computer-assisted fixed-window proof, not independent external verification. No growing-window G2 gap was closed and no RH proof is claimed.

The new proof preserves the exact original operator, first-slot-linear convention, physical head and endpoint, Fourier cut, logarithmic diagonal, all scale factors, and the sampler's explicit graph defect. It uses no zero locations or RH assumption. Weak G1 is unchanged.

## Proof mechanism

Let G_0 be the old frozen odd sixteen-column trial of support4096, V its invertible physical head, K = G_0* W G_0 > 0, r_0 = Q W G_0, and C = r_0* T^-1 r_0 >= 0 for the complete coercive odd tail. Thus S = K - C is the exact complete Schur matrix in the old head coordinates.

An exact frozen dyadic direction v is suggested by the largest generalized eigenvector of a numerical upper bound; no eigenvector accuracy is assumed. The exact projection P = I - v(v* K)/(v* K v) is enclosed using interval arithmetic, without midpoint freezing. Removing its column12 spans the exact K-orthogonal complement. Outward LDL proves C <= 0.001 K on that entire fifteen-dimensional complement; its smallest coordinate pivot exceeds0.0004086079. This includes every omitted residual row.

The successful new scalar trial f is supported through8192, preserves its physical head exactly as Vv, and was proposed by24 finite preconditioned steps. Its frozen physical head contains dyadic mantissas up to912bits, checked independently with Python Fraction. The verifier reconstructs the same fixed witness at1024 and1280bits. At J = 65536, with the existing odd inner factors and order64 remote moment, it proves:

- old denominator a = v* K v is between1 and1.000000000000002;
- QW(f,f) is between0.9016760830 and0.9016760831;
- the complete correction upper is between0.4725352935 and0.4725352936;
- (QW(f,f) - complete upper)/a is between0.4291407894 and0.4291407895.

Choose the exact rational s = 429/1000 and sigma = 1/1000. PSD Cauchy--Schwarz for the SAME OLD correction C gives S >= (s - sigma) K = (107/250) K on the entire head. This is a simultaneous matrix inequality, not separately tested positive directions. The complete positive tail square, invertible physical head and old even-sector certificate give the full closed-form sign. The relative0.428 is not an ordinary spectral-gap constant, and exact positivity requires no congruence loss in epsilon_4 = 0.

The combined verifier binds all witnesses and reports by SHA256, rechecks exact Fraction head equality, checks physical-head invertibility, and independently recomputes both outward directional inequalities. The complement896-bit replay reuses the old certified768-bit ingredients; it is not claimed as an independent reconstruction of them. New scalar residual rows are reconstructed at both stated precisions, with the same valid archived remote inner enclosure.

## New analytic estimates

The sharp direction/complement lemma is valid for any finite positive K and positive semidefinite complete correction C. For a subspace E and F = E^{perp_K}, hypotheses S|E >= s K|E and C|F <= sigma K|F, with s <= 1 and sigma >= 0, imply S >= (s - sigma) K. It extends to a whole unresolved block without multiplying by its dimension. The rank-one positive correction generated by (sqrt(1-s),sqrt(sigma)) shows sharpness.

For 0 <= sigma < 1 there is a stronger localized negative-error form:

    S >= -eta P_E* K P_E,
    eta = max(sigma - s, 0)/(1 - sigma).

It follows by completing the scalar cross-term square. With physical head V the full ordinary error is at most

    eta ||K^(1/2) P_E V^-1||^2.

This keeps the physical norm conversion only on the unresolved subspace. Cofinal convergence to zero, together with the manuscript's fixed-support identification and complete-tail prerequisites, would imply RH. No such convergence is asserted or inferred from this fixed window.

## Attempts that did not close the sign

1. Sixteen extra finite steps on a single direction at the old support4096 lowered recursive residuals but decreased trial energy by only about6.38e-5. Full recomputation of the sixteen-column matrix, including remote rows, remained inconclusive: the directional Young lower was about-0.42 in the old K normalization. The rounded update need not be exactly rank one; its energy change would be rank at most two before rounding. All verification uses reconstructed coefficients instead of proposal identities.
2. Retaining one common remote Gram and its cross block at support4096 did not fix the problem. Its directional complete lower was about-0.44599516, with a negative lower-bound pivot. A negative lower-bound pivot is not a negative Weil vector.
3. The old sixteen-step trial separately certified the ordinary full-form lower error1e-43 via K - U + 1e-43 V*V > 0. This was useful intermediate progress but is superseded by exact lambda4 positivity.
4. A proposed scalar trial could not be reconstructed exactly at768bits because its physical-head mantissas reached912bits. Exact rational construction and1024/1280-bit reconstruction fix this. A strict equality test between differently rounded interval representations of mu was also corrected to enclosure containment; the unchanged inner certificate independently proves the chosen rational mu. These were verifier diagnostics, not failed mathematical inequalities.
5. A low-precision suggested direction is sufficient for an exact positive gluing test but can be poor for converting a residual negative error to the physical norm. One direct projected-dual calculation gave an ordinary dual norm squared about0.0048118. The final negative-error route retains this factor explicitly rather than assuming a tiny factor from the direction's small trial energy.

## Adversarial audit

The adverse agent checked the exact physical-head identity using independent Fraction arithmetic, old versus new K normalization, unshifted residual versus shifted inner inverse factors, complete remote coverage, reuse of a remote upper on a smaller row subset, rank and exactness of the K-orthogonal projection, complex Hermitian extension under the first-slot-linear convention, and the closed-form square completion. The sharp gluing lemma and localized negative-error refinement passed. Detailed reasoning and both failures and success are retained in review_rank_one_trial.md.

## Next concrete target

Do not spend the next run improving the already positive lambda4 margin. Use the new subspace criterion to seek a **complete growing-window estimate**: identify an unresolved block E_lambda, independently bound the full correction on its K_lambda-orthogonal complement with sigma_lambda < 1, and prove either s_lambda >= sigma_lambda or decay of the localized ordinary error above. All inner factors, remote moments, dimension and physical normalization costs must be controlled at each window. The scalar far bound still imposes an exponential cutoff cost; a signed estimate that avoids that loss is a primary analytic target. The finite lambda8 scalar-head collapse from the previous checkpoint remains a warning that changing coordinates or reducing the head alone is insufficient. No finite list of windows settles this obligation.

## Files and preservation

The complete170-page v1.26 LaTeX/PDF compiles with no warnings and was visually checked throughout, with the new proof pages inspected individually. It integrates the new results in the abstract, status, Section20, future targets and reproduction appendix. All prior labels and72historical dispositions are retained. The cumulative bundle adds g2_odd_complement; its README identifies exact proof inputs and replay commands. The downloadable filenames explicitly identify v1.26 to avoid the earlier version ambiguity. Prior v1.25 snapshots and the full historical bundle content are preserved.

---

# Post-v1.25 window-resolution checkpoint — September 21, 2026

The released full manuscript remains v1.25 (166 pages). This checkpoint continues its finite-window investigation; it does not add a complete lambda8 sign certificate or prove G2/RH.

## Concrete question and result

Does the very small lambda8 margin disappear upon modestly enlarging the cutoff or reducing the head? **No, in the tested finite configurations.** The loss persists both at the next cutoff and with only the physical constant Fourier mode retained. It cannot be attributed solely to conditioning of multi-dimensional head coordinates.

All quantities below belong to the same unshifted physical lambda8 Weil form, the fixed normalized even Fourier basis and first-slot-linear convention. No operator, window or boundary functional is changed. Each eliminated finite tail and finite Schur head passes its own interval positivity gate. The arithmetic assembly was independently rederived in the adverse audit; the new computation increases the archimedean series from192 to256 terms and uses4096bits.

| Retained/test cutoff | Head | Certified generalized margin range (conservatively rounded) |
|---|---|---|
|256/384|0..64|5.697e-101 < m < 5.755e-101|
|384/512|0..64|1.349e-44 < m < 1.363e-44|
|256/384|0..36|1.155e-93 < m < 1.168e-93|
|256/384|physical constant mode0 only|9.5263e-42 < m < 9.5264e-42|
|384/512|physical constant mode0 only|1.4535e-14 < m < 1.4536e-14|

The first line reproduces the previous192-term coefficient calculation. The matrix brackets use a high-precision eigenvector only as a proposal. A verified invertible triangular congruence followed by interval LDL proves S_test−delta S_ret>0; an outward frozen-vector Rayleigh quotient proves the upper bound. Matrix witnesses and reports are saved. All modes above512 are absent from these experiments.

The constant-head energies are 3.2907912176941e-278 atcut256, 3.1349152424855e-319 atcut384 and4.5566952718104e-333 atcut512. They are certified finite minima with the constant coefficient fixed to1, not ordinary unit-vector eigenvalues. The first two values independently agree when obtained by shorting either the37-dimensional or65-dimensional finite head. A scalar normalizing congruence has condition1; although its absolute scale is large, its generalized margin is unaffected by that rescaling. The remaining eliminated operator can still be badly conditioned.

## Exact finite accounting

Let W_M>0 be nested compressions of one fixed Hermitian form, H a fixed finite head, and S_M^H its Schur complement. The variational identity is

    x* S_M^H x = min_y [x;y]* W_M [x;y].

Thus S_M decreases with M. For a retained tail T and newly added rows, write the larger block as

    [ F  B* C* ]
    [ B  T  D* ]
    [ C  D  U  ].

After eliminating the retained tail,

    R = C − D T^(-1)B,       A = U − D T^(-1)D* > 0,
    S_new = S_old − R* A^(-1)R.

The effective A is essential: replacing it by raw U discards the coupling. The generalized margin m(M1,M2)=min_{x!=0}(x*S_M2 x)/(x*S_M1 x) measures relative improvement/loss of positive finite trial energy. It is neither an absolute negative Weil error nor the complete residual correction.

For nested heads Hsmall subset Hbig, Schur-complement associativity, homogeneity and order preservation imply m_small >= m_big. A recovered small-head margin alone can move the fragile direction into the eliminated tail: A=I2 and B=diag(1,epsilon) have full-head margin epsilon, whereas eliminating the second coordinate gives margin1 and leaves a tail scale epsilon.

For fixed head and cuts M1<M2<M3, multiplying the inequalities gives

    m12*m23 <= m13 <= min(m12,m23).

These comparisons require a common window and common form. They cannot be used to order the lambda3,4,5,6,8 data across changing operators. A finite list of positive margins supplies no estimate for all subsequent cuts or a cofinal window family.

The constant-head shortcut follows from Schur inversion:

    S_M^{mode0} = 1 / [(S_M^{larger head})^(-1)]_{00}.

The script checks the larger Schur sign and evaluates this inverse column outward. It avoids solving another large tail problem and makes the head comparison exact.

## Source and adversarial checks

Primary sources consulted: Connes–Consani, Spectral triples and zeta-cycles (2023), https://alainconnes.org/wp-content/uploads/Spectral-triples-and-zeta-cycles_2021.pdf, Section2.5–3; and Weil positivity and trace formula, the archimedean place (2020), https://arxiv.org/pdf/2006.13771. Their discussion of tiny semilocal eigenvalues and prolate near-radical constructions is relevant context. Neither paper supplies the omitted complete growing-window certificate used here. No numerical conclusion is imported from those papers, and their window parameter conventions are not silently identified with this manuscript's L=2log(lambda).

The adverse review confirms the finite shorting identities, warns that head reduction can relocate inverse difficulty, and notes that probes expressed in different normalizing congruences cannot be compared directly. Future direction tracking must save their actual physical head vectors Vz. The main complete even lambda4 certificate from v1.25 is unchanged.

## Next concrete step

The newly tested cuts have not reached a stable relative finite energy. Before building a huge complete inner witness atlambda8, either extend the nested cutoff study with physical-direction tracking or construct source-adapted finite trials and compare their complete residuals. Any positive finite limit or apparent stabilization still needs a beyond-cutoff enclosure. The current scalar far method also retains its exponential cutoff cost. No G2 sign gap was closed by this checkpoint.


---

## Current research checkpoint: September 21, 2026 - full manuscript v1.25

**Local obligation closed:** the COMPLETE even-parity Weil form at lambda=4 is strictly positive/coercive on its form domain. This covers the whole 17-dimensional outer head and every infinite tail mode. It extends v1.24's one-direction result; it does not establish the odd sector, full W4 positivity, G2, or RH.

**Exact identity and certificate:** for the actual frozen trial matrix G, V=P16 G, E=Q16 W4 G and K=G* W4 G, V* S_infinity V=K-E* T^(-1)E. The actual V is interval-certified invertible. All trial columns are finite Fourier vectors in the operator domain; completing the coercive tail square is valid on the closed form domain. The complete tail floor and archimedean shift are the previously certified ones, with the shift used only to upper-bound the inverse; K and E remain unshifted.

**Witness:** normalize the old even trial by its head energy BEFORE generating 16 finite preconditioned-CG corrections, support4096, candidate512bits. Freeze both the rounded base and corrections as exact dyadics. Rounding the base defines a nearby exact trial, not an assumed exact old congruence; the actual head is checked. Reconstruct the same frozen coefficients at768/896bits, retain all residual cross-Grams throughJ65536, and enclose every omitted row by the order64 moment theorem. With mu=.9999999999, rho<.165102333 and tau=.1, all17 pivots of K-U_tau are positive, the smallest >.7645944101. This is a coordinate pivot, not an ordinary spectral gap. Independently certify the exact rational gate U_tau < (1-62629/100000)K at both precisions. This gives complete generalized margin >.62629. Nine dense physical-row checks and provenance checks are retained.

**Joint remote estimate proved:** one joint Gram Gamma >= [Y,y]*[Y,y], together with 0<=L_Y<=Y*Y and A0=mu I+L_Y-Gamma_YY>0, yields complete inverse upper V_J+Gamma_kk+(H-Gamma_Yk)* A0^(-1)(H-Gamma_Yk). Its proof applies the joint Gram to(-z,x) in a variational supremum. A shared cross block is essential. Adversarial review corrected the printed hypothesis to L_Y>=0, needed for the scalar inverse corollary. Implementations already used L_Y=0. An optional768bit joint-Gram check has smallest pivot >.7892519172 using the scalar denominator and >.7892519657 with the full denominator; these are additional checks, not prerequisites for the main two-precision even result.

**Failed or inconclusive attempts:** independently corrected unscaled even columns did not give a positive whole-head gate; the energy-scaled-before-CG construction resolved that problem. Odd4step and16step trials atsupport4096 remain inconclusive (best gates fail around head indices4/5 and10/11 respectively). These are failures of majorants, not negative Weil vectors. The canonical even and odd4step trials give only ordinary negative-error bounds of1e-17 and1e-12, respectively. They do not prove exact signs. No whole-space epsilon4=0 is claimed. The odd witness has its own certified inner factors and remote rho about.041200151; even constants were not transplanted to it.

**Growing-window work:** priority shifted per the user's request to lambda=3,4,5,6,8. Fresh scalar far thresholds give evenN44,283,1502,7488,124442 and oddN209,1360,7224,36021,598623. Both positive-at-N and negative-at-N-1 gates replay at320/384bits; monotonicity proves minimality for this formula. Analytically proved that the present scalar far bound forces exponential cutoff growth, using the previously established prime norm/lambda ->1. This restriction belongs to this majorant, not every possible G2 method.

| Window | Head dimension | Finite relative margin | log10 cond(V) | Reference-column headroom | First admissible even N | First admissible odd N |
|---:|---:|---:|---:|---:|---:|---:|
| 3 | 10 | 0.781598 | 18.96343 | 521.339 | 44 | 209 |
| 4 | 17 | 0.545521 | 37.51866 | 93.717 | 283 | 1360 |
| 5 | 26 | 0.341968 | 61.60390 | 710.489 | 1502 | 7224 |
| 6 | 37 | 0.191097 | 91.13502 | 1204.37 | 7488 | 36021 |
| 8 | 65 | 5.75469e-101 | 139.45064 | 1.59185 | 124442 | 598623 |

**Finite diagnostic scope:** the displayed Schur study uses heads throughlambda² and fixed cuts256/384, not the full4096/65536 pipeline. Every finite eliminated tail and resulting finite head is interval-positive. All omitted modes beyond384 remain absent from this probe; these finite correction matrices are not complete upper bounds. Complete growing-window witnesses, mu/rho/moment constants and ordinary error rates are still missing. Conditions and raw-energy logs are diagnostics, not lower eigenvalue certificates. The reference-column headroom in this table is not the old v1.24 direction. Healthy one-direction headroom alone does not distinguish conditioning from other bad directions. The simple diagonal counterexample in the manuscript makes these quantities independent.

**Numerical reliability:** early2048bit scaling attempts and interval-LU lambda8 solves had broad interval metrics and were rejected. A verified preconditioned solve resolves finite lambda8 positivity; the double-precision subtraction1-theta cannot resolve its very small relative margin. A100-digit inverse-metric proposal, followed by a frozen-vector Rayleigh upper and an independent interval LDL lower, rigorously brackets the FINITE generalized margin between5.697e-101 and5.755e-101. The metric/probe witness is saved and replayed. Thus a substantial loss is present for these fixed cuts, but neither an infinite correction nor an asymptotic decline has been certified. An adverse review caught an unsafe floating maximum in the auxiliary trace bound; it was replaced by the analytic upper1+65e-20 from the certified normalized metric, and the saved trace bound was regenerated. Decimal serialization of the normalized metric widened intervals enough to defeat naive LDL; replay uses a certified triangular congruence before LDL and a separate frozen-vector Rayleigh upper, so the bracket survives reloading its witness. This did not affect the main lower gate or Rayleigh upper. The local python-flint generic power of a tiny zero-centred ball could return NaN; using x*x in the new LDL avoids false inconclusive gates. Prior positive gates could not have accepted NaN, so this was not a discovered false-positive certificate. Candidate floats select congruences only; every accepted proof gate is outward interval arithmetic.

**Review and integration:** independent adverse review checked full operator/form-domain implication, dyadic actual-head rank, scale/parity/zero-mode factors, complete residual majorants and rational margin. The L_Y hypothesis correction was applied before final integration. Full v1.25 retains all496prior labels,72historical ledger dispositions and the explicit sampler graph defect. The complete166page PDF was compiled and all pages rendered, with new proofs/tables inspected at full size. No publication or external contact.

**Next concrete target:** produce complete window-specific inner inverse certificates and a controlled residual-family estimate, or improve the signed far comparison to avoid the current exponential head cost. Do not extrapolate the five finite windows or reuse lambda4 mu/rho without proof. Finishing oddlambda4 remains a separate local milestone. The local even sign gap is closed; no global G2 sign gap or RH proof is closed.

---

## Current research checkpoint: September 21, 2026 - full manuscript v1.24

**Obligation selected and closed in its precise scope:** the saved single even head direction at lambda4 now has a complete positive Schur certificate, including the infinite residual tail. This is the same head vector v that defeated the previous first-order majorants. It is not positivity of the whole head or a G2/RH proof.

**Route:** use a finite iterative solve only to propose an exact dyadic correction z, then verify the new unshifted trial g=f-(0,z) directly. The exact identity is S_infinity(v,v)=QW(g,g)-<T^(-1)e,e>, e=P_tail Wg. Only the new residual inverse is bounded with the saved shifted tail certificate. This is a reuse of the verified-solve identity with a better trial, not a new claim equating finite polynomial powers to complete powers. It includes the full head reconstruction and avoids all unproved intermediate-power excursions.

**Main certificate:** proposal supportM4096, verification cutoffJ65536, momentorder64,16finite preconditionedCG steps at256bits. The resulting4080dyadic tail coefficients are frozen. The original17head coefficients and the old support256source are unchanged. Verification from the frozen coefficients at768/896bits gives Knew=3.235584348132818e-20, retained far correction3.742924323122588e-22, retained mixed square1.617782099611548e-23, complete remote residual norm-squared upper8.080848755848843e-22, and complete inverse-correction upper1.424888810223207e-21. Consequently

`3.0930e-20 < S_infinity(v,v) < 3.2356e-20`.

The old residual inverse correction is between3.2337e-20 and3.3762e-20, and S_infinity(v,v)>0.4781times the original K_X(v,v). Thus this direction was difficult for the old majorant, but is not identified as the most difficult direction of the actual Schur matrix.

**Additional supported trial:** a separately frozen4step preconditionedCG correction at the same support/cutoff also passes768/896bits, with complete lower2.902807375091886e-20. Four CG steps are not the previous degree4 inverse polynomial. No spectrum-uniform polynomial degree claim follows from this result. The16step trial gives a tighter interval and is used for the main proposition.

**Adversarial and mechanical checks:** the inner witness hash is checked against the archived complete shifted-tail report, and the cached remote Gram uses the same factors, J and precision. The standalone verifier checks J>M>=1024, exact dyadic reconstruction, witness dimensions/M/steps, and cache provenance. Nine rows including0,1,16,17,256,512,513,1024,4096 are checked by dense coefficient assembly. An independently expanded old-energy/new-correction identity overlaps the direct new energy. Candidate CG residuals and floating candidate choices never enter the proof gate. Review found no blocking domain, shift, adjoint, zero-mode, normalization or omitted-row issue. Its minor printed-rho rounding request was applied: rho<.165102333 makes the printed table independently sufficient.

**New screenshot F-86/F-87:** the supplied image was readable. It reports independent reproduction of earlier even/odd trial LDL and lambda3tail constants, but states that the mixed/directional witnesses were unavailable. These reports remain user-provided; their external source was not replayed here. The complete cumulative bundle will be linked with this delivery so those witnesses are available. F-87reports finite theta=.999999987419 and spectrum-uniform degree/budget diagnostics. Their precise approximation definitions and code were not supplied, so those counts are not transferred to this construction. The screenshot itself distinguishes directional methods from uniform bounds. Our new result is directional and uses a different, explicitly frozen verified solve; it neither contradicts nor certifies those external degree diagnostics.

**Integration:** full v1.24 is162pages. Abstract, status, Section20, Section32 and reproduction appendix now distinguish the still-valid first-degree failures from the new complete positive direction. All490previous labels and72historical ledger rows are retained. WeakG1, physical endpoint, Fourier cut, first-slot-linear convention, correct logarithmic diagonal, scale factors and explicit sampler graph defect remain unchanged. Full compilation and visual validation are recorded separately.

**Next concrete step:** construct a simultaneous matrix of improved frozen trials on the entire17dimensional even and16dimensional odd heads, retaining all residual cross-Grams and the remote matrix majorant. Use verified congruences to focus on remaining directions of small Schur energy; do not infer matrix positivity from individually positive directions. The present direction is now certified and should not be repeatedly optimized as a substitute for that task. Complete lambda4 matrix positivity and cofinal growing-window uniformity remain open. The single-direction obligation is closed; no overall G2 sign gap or RH proof is closed. No publication or outside contact occurred.

---

## Current research checkpoint: September 21, 2026 - full manuscript v1.23

Selected obligation: compute the complete refined mixed correction for the frozen lambda4, support256 even trial. Fresh Library metadata and the authoritative log were read first; current local identities matched their versions. The screenshot received during this work was read successfully despite the client error message.

**Proved complete obstruction, not a negative Weil vector.** The first inverse polynomial Q1=Dg^(-1/2)(I-H/20)Dg^(-1/2), with the saved scalar inner certificate mu=0.9999999999, cannot certify the archived head direction. The complete scalar-head majorant exceeds6.760969872499e-20, while the complete trial energy is6.469284394159e-20. A further metric-Cauchy test proves that even the EXACT positive first head update M1=mu I+Y*H Y/20 still gives a complete majorant above6.658861522405e-20. Its excess is greater than1.89577e-21. Both tests retain every omitted input/output correlation and replay at768/896bits with the same frozen dyadic witnesses. They reject this degree and initial certificate; they do not reject a stronger initial M0, higher degree, the true residual inverse, or Weil positivity.

**New analytic tools.** Put Y=Dg^(-1/2)R C*, y=Dg^(-1/2)k, p=P_J y, q=Q_J y, H=A-I>=0, Q_J H Q_J<=nu Q_J. For a head probe z, eta_z=<H P_J Yz,P_J Yz>, ||Q_J Yz||²<=rho_z, ||q||²<=E, a=<Hp,p>. The complete mixed-pairing error is bounded by [sqrt(nu eta_z E)+sqrt(nu a rho_z)]/m+sqrt(rho_z E). This includes the Q1 output outside the prefix as well as the omitted input. Completing a scalar square gives the complete far LOWER bound ||p||²-a/(m-nu). For any positive initial head certificate M0<=C K_Z C*-Y*Y, retaining M_j=M0+Y*(I-P_j(A))Y yields monotone decreasing complete upper corrections. The common block lower form has fixed head M0+Y*Y and increasing far block Q_j^(-1). Norm convergence of the inverse polynomials does not eliminate any initial head-certificate slack. A finite-probe Gram/Young lower enclosure keeps its remote pairing explicitly, without an invalid matrix positive-part operation.

**Directional data at J65536.** Retained first far energy4.916335942202e-20; retained mixed square3.006520553833e-20; retained scalar total7.922856496335e-20. The exact probe has496 integer numerators over2^160. eta_z=.4276838592143925, rho_z<.067205778409068, mixed pairing error<2.961708366055e-11. Complete far lower>4.693812399865e-20. The complete scalar mixed lower>2.067157472633e-20. For the positive head update, z*M1*z<1.051962237848 and the mixed lower>1.965049122540e-20. The complete directional upper enclosure was also evaluated and remains inconclusive (about1.246e-19); the method-failure result uses the LOWER certificate, not that failed upper gate.

**Exploratory attempts, not manuscript results.** At the same prefix, higher-degree scalar-head totals were approximately: degree2=6.89656e-20, degree4=5.89261e-20, degree8=5.31815e-20, degree16=5.16866e-20. The latter three lie below K at the retained level. These are powers of the finite compression, not compressions of the full powers: a full power can leave the prefix and return. Their intermediate excursions, mixed correlations, and positive head-update Grams have not been enclosed. They are candidate-selection diagnostics only. The initial crude complete-mixed lower just missed the failure test; the stronger far lower bound from optimizing the unknown omitted norm resolved that obstruction.

**User screenshot F-82/F-83/F-84.** It reports odd and even positive finite LDL at nmax96/192, finite theta<1 after correcting an unsafe float(mid()) extraction, and a53-order loss in another scalar recipe. It also reports a fitted remaining normalized budget near1e-8 through cutoff320. No replayable source code or complete beyond-cutoff enclosure was attached. These are recorded as user-reported finite findings, not imported certificates. The dimension/precision bugs described in the screenshot concern that external implementation, not a discovered defect in the present code. Its global-norm/scalar-head recipe is not identified with our inner C-congruent mu certificate; the reported53-order factor cannot be transferred to our bound. The convergence fit is not an infinite-tail estimate. Our complete first-degree lower gate now also tests the exact induced head update, so changing coordinates alone cannot reverse that proved comparison.

**Validation.** Independent adverse review checked the complete mixed identity, lower bound, first-slot-linear adjoints, shifted-inner/unshifted-outer separation, actual probe normalization, corrected head metric and shared form domains. It checked the new metric-Cauchy quotient separately after it was added. All478 prior labels and72 historical ledger rows are retained. Complete v1.23 is160pages, compiled with no warnings or unresolved references; all pages were visually inspected in contacts and new proofs/tables at full size. Weak G1, physical endpoint, Fourier cut, logarithmic diagonal and explicit sampler graph defect are unchanged. No publication or outside contact.

**Next concrete step.** Evaluate a degree4 or degree8 complete inverse correction with a certified enclosure of intermediate remote excursions, retaining the monotone head update and the actual initial matrix certificate where possible. Begin on this exact saved direction, then seek simultaneous17-dimensional even and16-dimensional odd head comparison. Merely increasing precision or rerunning the proved-failing first degree cannot close this target. The complete lambda4 low Schur sign and cofinal growing-window estimates remain open. No G2 sign gap was closed; no RH proof is claimed.

---

## Follow-up: F-80 withdrawal and the reported 10^65 coercivity loss

The user explicitly clarified that Claude had already withdrawn the complete-tail positivity claim in F-80. Every matrix was assembled from `G.assemble(Momit, ...)`: T uses indices through Momit, R uses only Mret+1 through Momit, and `Cx=R^T Sch^(-1)R` uses the corresponding finite Schur matrix. There is no beyond-Momit enclosure. Consequently the reported positive LDL tables concern the finite S_M for Momit96,128,160,192; they do not certify S_infinity. The matching F-68 pivot is explained by finite Schur-complement associativity. This clarification supersedes the earlier pending-scope entry below. The reported finite certificates have not been independently replayed here.

The user reports a scalar coercivity majorant3.27e7, minimum LDL pivot1.32e-58, and ratio approximately2.5e65, with the actual established tail floor epsilon=1.7940e-8. Their arithmetic ratio is3.27e7/(1.32e-58)=2.4772727...e65. The underlying residual norm was not supplied for independent verification; if it was measured only on finite rows it is not itself an upper bound for the complete residual. A large finite-row contribution can nevertheless expose the crudeness of that scalar bound.

**Correction to the interpretation:** this ratio does not prove that every successful method must recover65orders of accuracy or that the structured inverse is the only possible route. A global norm discards which head directions carry the residual, while an LDL pivot is not an ordinary smallest-eigenvalue bound and depends on the elimination coordinates. The existing failures establish failure of particular estimates, not a general no-go theorem.

An exact two-dimensional model reproduces the quoted ratio while the true relative correction is one half. Set delta=1.32e-58, A=6.54e7, K=diag(delta,A), T=epsilon I, and r=sqrt(epsilon/2)diag(sqrt(delta),sqrt(A)). Then C=r*T^(-1)r=K/2 and S=K-C=K/2 is strictly positive, while epsilon^(-1)||r||^2=3.27e7. Hence the coarse norm divided by the smallest pivot is2.47727...e65 even though K^(-1/2)CK^(-1/2)=I/2 exactly. In this model the full matrix coercivity estimate epsilon^(-1)r*r is already exact; only replacement by a scalar norm creates the enormous loss. This is an algebraic illustration, not a model for the actual Weil coefficients and not a repair of the already failed actual matrix majorants.

The coordinate-correct target remains the simultaneous relative matrix inequality. If the positive trial K=L D L* has D>0, let V=L^(-*)D^(-1/2), so V*KV=I. Then S=K-r*T^(-1)r>=0 iff ||T^(-1/2)rV||<=1. Equivalently, construct a complete form-order upper enclosure Cbar>=r*T^(-1)r and certify V*(K-Cbar)V>=0. An implementation may use a frozen exact dyadic V, certify V*KV>=kappa I, and compare the complete transformed correction against that same kappa; approximate normalization must not be silently treated as exact.

**Next step and unchanged scope:** retain the actual signed structured inverse and all mixed/remote terms while applying them to rV, with a simultaneous whole-head Gram certificate. The prior v1.22 far-energy comparison succeeds on one direction only. The full mixed term, full lambda4 Schur sign, and growing-window uniformity remain open. No G2 sign gap was closed by the finite tables or this illustrative model. The complete v1.22 manuscript already has the correct finite/infinite distinction and needs no revision to withdraw a claim it never adopted.

---

## Current research checkpoint: September 21, 2026 - full manuscript v1.22

**Selected obligation:** Step 1 of the user's plan: bound the complete lambda=4 low-mode Schur correction, starting from the signed inverse refinement. Freshly recovered the authoritative v1.21 manuscript, research log and cumulative evidence bundle. Replayed the exact dyadic negative witnesses for the old optimistic ceilings K_X-V_J at outer support256,512,1024. Their signs reproduce; they are failures of those majorants, not negative Weil directions.

**Established analytically and with interval constants:** Retaining parity signs sharpens the complete shifted far sandwiches from m=67 to20 on even n>512 and from335 to90 on odd n>1536. The ratios are below19.215607 and89.840960, respectively, verified at320and384bits. The positive even pole tail contributes at most hL^3/(12pi^4 N^3); the odd limiting Hilbert matrix and odd pole term are nonpositive in an upper bound. The shift cD acts only on the exact archimedean diagonal. The new inverse-polynomial error factors are(19/20)^k and(89/90)^k. These constants apply at one fixed window; they assert no growing-window uniformity.

**Established finite-prefix estimate:** For H=D_g^(-1/2)UD_g^(-1/2)-I>=0, prefix p, omitted q, a=<Hp,p>, v=||p||^2, ||q||^2<=E, and Q_JHQ_J<=nu_J Q_J, positivity gives <H(p+q),p+q> >= [sqrt(a)-sqrt(nu_J E)]_+^2. Thus the complete first inverse-polynomial contribution is bounded above by v+E minus one twentieth of this square in the even sector. A matrix Young version and a relative matrix-tail version are proved; scalar positive parts must not be replaced by an unjustified matrix positive part. The remote nu_J retains the original kappa_N in D_g and improves only the far remainder at J.

**Concrete certified progress:** On the archived even head direction formerly obstructing the diagonal majorant, using the frozen support256 solve, the complete shifted far energy now satisfies

`<U^(-1)k,k> < 5.758e-20 < 6.469e-20 < K_X(v,v)`.

This gate includes every residual row beyond J65536 using the order64 infinite moment bound. The enclosed values are K=6.4692843941586476e-20, prefix V=6.9332416283028267e-20, prefix <Hp,p>=4.0338113722023497e-19, remote norm-squared upper3.4797080872158321e-21, remote H norm upper1.987323729731466, complete first-polynomial upper5.7578877881088833e-20. The strict remaining budget exceeds7.11396606049e-21. Identical exact dyadic inputs replay at768and896bits. This removes the old far-energy obstruction on ONE direction only. The refined mixed square has NOT been included, and no simultaneous head-matrix sign is certified.

### Attempts and failures retained as research history

- J4096: prefix V6.81404407434e-20, AP3.97732748593e-19, remote norm bound1.12794423584e-19 and nu4.04915505817. The reverse-triangle lower improvement is zero; the resulting far upper1.80934864327e-19 exceeds K. This is an inconclusive enclosure, not failure of the true inverse or even of the first polynomial.
- J16384: AP4.02588642283e-19 and the complete AP lower1.69260219267e-19 are positive, but the far upper7.93789328887e-20 still exceeds K. Extending the certified prefix, rather than increasing precision, resolves this particular enclosure obstruction atJ65536.
- A scalar refinement cannot be subtracted from the old structured energy while freezing its mixed term. For any U^(-1)<=Q_*<=D_g^(-1), the valid whole bound is k*Q_*k+mu^(-1)||C(h-Z*k-R*Q_*k)||^2. Both appearances must change. The original finite certificate survives because K_Z-R*Q_*R>=K_Z-R*D_g^(-1)R>=L_lower. Its closed-form/domain justification is supplied in the manuscript.
- The adverse review also derived a sharper scalar bound using prefix-tail orthogonality and a first-polynomial failure test. These auxiliary directions are recorded in adversarial_first_inverse_review.md. They are not asserted as completed G2 work.

### Verification and scope

The new matrix actions use four outward Arb polynomial products for the exact Toeplitz divided-difference and Hankel parts; a dense25row calculation independently checks indexing and the opposite-sign parity diagonal. The original assembly's archimedean-series remainder, logarithmic diagonal, Fourier normalization and shift are retained. No floating sign decision, zero list or RH assumption enters the directional gate. The adverse agent checked the pole factors, original kappa_N, scalar/matrix distinction, convolution indexing and general Q_* form-domain argument. Its request to state nu>=0 explicitly was incorporated.

The complete manuscript is v1.22,156pages. The title/status, abstract, Section20 proofs, Section32 targets and reproduction appendix were integrated together. All466 prior labels and72 historical claim dispositions are retained. Weak G1, the physical endpoint, first-slot-linear convention and explicit sampler graph defect remain unchanged. The revised complete PDF compiles with resolved references and no box warnings; final visual inspection is recorded in the validation file.

**No G2 sign gap was closed.** The entire low-mode Schur matrix at lambda4 is still open, as are the cofinal growing-window estimates. No RH proof is claimed.

### User-supplied whole-head LDL proposal

During this work the user relayed Claude's suggestion to replace a theta_X eigenvalue estimate by interval LDL. The equivalence is correct when K_X is positive definite and C_X is the COMPLETE r*T^(-1)*r: theta_X<=1 iff K_X-C_X>=0. The manuscript now states the concrete sufficient gate: construct a form-order upper enclosure Cbar_X>=C_X and certify K_X-Cbar_X>=0. Strict positive LDL pivots suffice and prove a stronger strict inequality. An entrywise upper bound is not a form-order upper enclosure; an interval containing a zero pivot is not a semidefinite certificate. For a tail compression, r_M*T_M^(-1)*r_M<=C_X, so its uncorrected finite LDL sign does not close the infinite-tail gap. The reported crude upper bound about1.75 and numerical theta about0.9998 were not supplied as replayable complete-tail matrices and are not imported as certificates.

The user then reported positive interval LDL for ret:omit64:96,64:128,64:160,64:192, claiming the complete S_infinity and noting that the64:160 minimum pivot1.3832e-58 matches F-68's finite nmax160 low_block. The source code and an enclosure of modes beyond omit were not supplied or recovered by the targeted file search. Agreement with a finite low_block is consistent with finite Schur-complement associativity and does not by itself establish inclusion of the infinite remainder. The claim is recorded as user-reported, pending inspection of the actual correction upper enclosure. If that enclosure really covers the complete tail and the correct whole-head form, the LDL result would close the fixed-lambda4 sign; it would still not establish growing-window uniformity or RH. No categorical claim is made that the user's computation omitted the tail; its scope is not evidenced by the supplied table.

### Next concrete step

Evaluate C(h-Z*k-R*Q_1*k) for the same frozen head direction, where Q_1=D_g^(-1/2)(I-H/20)D_g^(-1/2). Enclose remote correlations jointly rather than discarding them or treating small ordinary residual norm as sufficient. The mixed square divided by mu must fit within the certified remaining7.11396606049e-21 budget (or a sharper inverse polynomial must be used). Then extend to the whole17-dimensional even head and16-dimensional odd head through a simultaneous Gram/congruence certificate. Only after complete fixed-window sign gates should a growing-window estimate be claimed; the actual head dimension, C norm, mu and arithmetic rescaling must remain in that estimate. A cofinal complete-Weil lower error tending to zero would imply RH directly; the conditional Riesz/evaluator route retains its separate assumptions.

---

## Current research checkpoint: September 21, 2026 - full manuscript v1.21

**Completed:** integrated the preceding Schur/cancellation audit into the full 152-page manuscript, including the abstract, status, Section20, Section32 and reproduction appendix. All454 prior labels and72 historical ledger rows are retained; there are466 labels after this integration.

**Results and scope:** local alpha4=0 is certified for X=0 and the frozen support256 trials in both parity sectors. Finite-support K_X is exactly the complete trial form; the full Schur complement additionally subtracts r*T^-1*r. The new exact-source-orthogonal test has positive Weil energy below3e-31 while the signed non-prime/prime terms exceed0.4 in magnitude. This rejects the strong single-source cancellation explanation, not complement positivity. These use the previous audit's verified witnesses and its existing exact-source certificate, not the unprovided F-68/F-69 files.

**Review:** the integrated analytic and computer-assisted arguments passed an independent internal adverse review. Its two wording requests (orthogonal P_M and general retained finite subspace) were applied. Existing768/896-bit interval validations were retained; no exploratory output was promoted to a result.

**Dependency correction:** a full cofinal complete-Weil lower error tending to zero would already imply RH by fixed-support embedding and Weil positivity, without requiring the conditional Riesz realization. The operator route retains that assumption. The residual target is e_lambda->0 and t_lambda/sqrt(mu_lambda)->0; geometric inverse convergence controls the approximation error, not the residual itself.

**Next concrete obligation:** evaluate and bound the complete inverse-weighted residual correction at lambda4 using the certified signed tail factors, then obtain estimates with the actual growing-window head dimension, congruence scale and mu_lambda retained. No complete lambda4 low-head sign or cofinal G2 sign is newly proved. No G2 sign gap was closed; no RH proof is claimed.

**Deliverables:** complete LaTeX/PDF v1.21, revision notes, validation record and cumulative evidence bundle. The prior audit and all historical attempts follow below unchanged.

## Current checkpoint: September21,2026 — source-complement cancellation audit and local alpha=0

Reviewed six supplied screenshots and the follow-up finite Schur argument. Reproduced their frozen-source total5.312381700586359e−38 on the actual lambda3,N64 form; the screenshots’ “arch” number equals archimedean plus pole, not pure archimedean.

**New certified correction:** a unit even Fourier polynomial in E64 orthogonal to the exact literal repaired source p3 has0<qW(v)<3e−31 while q_nonprime(v)>.4 and q_prime(v)<−.4. The candidate values are+.4173237590174977,−.4173237590174977 and2.58441341799e−31. Exact-source transfer uses the already certified projector distance<4e−36 and verified finite row-sum operator bounds. Two exact dyadic trial columns and interval quadratic forms replay at768/896bits. Thus strong near-cancellation is not confined to the source. This is not an exact null vector or a negative Weil test. The result was independently checked by the adversarial agent.

**Valid part of the user’s Schur argument:** for any finite-supportX, K_X is exactlyG*W_MG withG=[I;−X]. A rigorously positive finite compression covering that support proves the complete K_X>0 without knowing the infinite Schur sign. We independently certified this at lambda4, split16, forX=0 and frozen finite solves through256 in both parity sectors; all interval LDL pivots are positive at768/896bits with identical solve hashes. Thus alpha=0 is now established for those actual choices. The user-reported F-68 certificates at additional cutoffs/windows were not available for independent replay and are not imported as results.

The complete tail here is already coercive: T>1.7940e−8I. Therefore K_X−S=(X−T^(-1)B)*T(X−T^(-1)B) and S=K_X−r*T^(-1)r hold without a generalized-inverse ambiguity. For an exact finite solve, S_infinity=S_M−r_M*T^(-1)r_M. FiniteS_M are upper enclosures, whereas the structured inverse produces lower enclosures of the same original operator. Positive finite data alone do not prove the complete sign. For merely semidefiniteT the form identity requires RanB contained inRanT^(1/2), not just orthogonality tokerT.

**No G2 sign gap closed.** The cofinal uniform inverse-residual estimate remains open. Preserve the current inverse-polynomial target, now with localalpha=0 at the certifiedlambda4 solves. Do not assume a crude separate estimate suffices on the source complement. Test the whole near-null subspace and its signed correlations.

Supplementary proof and reproduction files: RH_Cancellation_Claim_Audit.md and RH_Cancellation_Audit_Bundle.zip. The complete manuscript remains148-pagev1.20; this new audit is recorded here for integration in its next revision.

---

**Dependency accounting clarified:** local finite-support K_X positivity needs no infinite-tail transfer; the residual subtraction does. Full cofinal complete-Weil lower bounds -o(1) would imply RH directly by fixed-support embedding and Weil positivity, bypassing the conditional Riesz realization. Geometric inverse convergence alone does not prove residual-energy convergence.

## Current research checkpoint: September 21, 2026 — v1.20 low-mode Schur revision

**Established in this revision:** a structured inverse bound that reuses the certified signed tail factors; a finite-row version with every infinite residual row enclosed; an ordinary-error criterion with the growing-head and congruence scales explicit; and convergent upper approximations to the actual infinite far-tail inverse at lambda=4. The latter have rigorously certified contraction factors66/67 (even, n>512) and334/335 (odd, n>1536).

**Not established:** the effective low-head sign at lambda=4 or a lower bound−o(1) on unbounded windows. **No G2 sign gap was closed.** Weak G1 and all existing certificates remain in their previous scope. The explicit sampler graph defect remains. No RH proof is claimed. The complete manuscript retains the requested version label1.20.

### Recovery and selected obligation

Fresh authoritative reads/materialization recovered the complete current manuscript, log, notes, validation and cumulative historical bundle. Starting versions were20 for the manuscript/notes/validation and21 for the log/bundle. The recovered181-member bundle has SHA256 `2b7f003e1e7d10f47780708e87892cc739de4f5eea6a621746e1be716fd8f597`. It is preserved cumulatively. The selected target was the actual33-dimensional low Schur matrix at lambda4:17 even and16 odd coordinates, with the complete positive complement Q16 already certified. No raw finite-matrix positivity was substituted for this inverse-corrected target.

### Attempt1: the scalar tail inverse loses too much

Using the exact lower tail bound T>=10^(-8)D_arch, construct a768-bit finite solve on17..256 for the17-dimensional even head. Every residual row through2048 and the infinite directional moment Gram (order64) was included. The resulting lower matrix failed at its first LDL pivot, approximately−27684.1. This is failure of an enclosure, not a negative Weil direction.

A noncertifying high-precision diagnostic of the signed K_X matrix shows eigenvalues down to about2.83e−75. This explains the need to preserve directional cancellations. Merely dividing an ordinary residual by the coarse tail floor is insufficient.

### Proved structured inverse estimate

Split a certified tail as T=[[F,B*],[B,U]], U>=D_g>=gamma I. For the saved finite-support Z, set R=B−UZ and K_Z=F−B*Z−Z*B+Z*UZ. If L_lower<=K_Z−R*D_g^(-1)R and C L_lower C*>=mu I>0, then for r=(h,k),

`<T^(-1)r,r> <= ||D_g^(-1/2)k||² + mu^(-1)||C(h−Z*k−R*D_g^(-1)k)||²`.

Both signs inside the last norm are minus. The proof uses a closed lower form on the possibly larger D(D_g^(1/2)) domain, followed by inverse order; it does not assume the second triangular change preserves D(U^(1/2)). If the saved certificate belongs to T−cD, its factors give an upper bound on T^(-1) by inverse order. The shifted residual is never relabeled as an unshifted one.

The finite-row implementation encloses the omitted mixed Gram by an operator Cauchy–Schwarz bound and matrix Young inequality. All Fourier signs are represented through the normalized parity basis. Finite-column remote Grams are valid despite the whole weighted operator not being Hilbert–Schmidt. The prior320-bit tail witness hashes and congruence margins are checked before reuse.

### Attempts2–4 and adversarial falsification of the current majorants

The structured even calculation uses inner head17..512, saved solve support513..1024, J4096, moment order64,768-bit arithmetic, and mu=0.9999999999. The outer actual-W solve support was enlarged successively to256,512,1024. The last expansion crosses the inner head boundary; this is valid because J exceeds both support cutoffs. Outer residuals belong to W, while inner factors belong to W−10^(-8)D.

A preliminary Young parameter10^(-8) made the remote mixed bound much worse (first pivot about−144198); it was replaced by1 after inspecting the explicit rho U_k term, not by increasing precision. With parameter1, the first pivots were positive but the second pivots still failed:

| outer solve cutoff M | first pivot | second pivot |
|---|---:|---:|
|256|0.0001185083|−2.79577e−5|
|512|0.0011263500|−1.56760e−6|
|1024|0.0017430178|−4.71642e−7|

These values are interval enclosure outputs; none is a Weil Rayleigh value.

An adversarial agent then tested the optimistic ceiling K_X−V_J, which omits all the further positive inverse penalties. Exact160-bit dyadic test vectors prove a strictly negative value for that ceiling in every case:

| M | certified ceiling quadratic value, approximately |
|---|---:|
|256|−3.4475968e−21|
|512|−1.1146930e−19|
|1024|−7.20037e−59|

The standalone `check_structured_ceiling.py` verifies input hashes and recomputes these quadratic forms in Arb; the witnesses replay at896bits. Holding each solve fixed, changing Young's parameter or moment order cannot rescue that certificate. Increasing J only increases V_J, so it cannot rescue the same candidate either. This is a rigorous obstruction to these particular inverse majorants, **not evidence of a negative Weil test and not a disproof of positivity**. Exploratory eigensolver diagnostics remain labeled numerical.

### Proved replacement for the diagonal far inverse

The failed ceiling test directs the next step at the actual far inverse rather than another unsigned remote bound. If D_g<=U<=mD_g, let A=D_g^(-1/2)U D_g^(-1/2), S=I−A/m, and

`P_k(A)=m^(-1) sum_(j=0)^(k−1) S^j + S^k`.

The spectral theorem proves A^(-1)<=P_(k+1)<=P_k<=I and

`0<=P_k−A^(-1)=S^k(I−A^(-1))<=(1−1/m)^k I`.

Thus the conjugated polynomials give decreasing complete inverse upper bounds. The first is

`U^(-1)<=D_g^(-1)−m^(-1)D_g^(-1)(U−D_g)D_g^(-1)`.

This retains a signed arithmetic correction to the diagonal inverse. The polynomial is an operator on the full far tail; its evaluation has not been replaced by an unjustified finite power.

The needed actual upper sandwich is now proved at lambda4. The existing lower archimedean bound was strengthened to the two-sided estimate

`|a_n−log(|n|/L)|<=E_L(|t_n|)`.

The new upper half follows from Binet at w=5/4+it/2: Re log w−log(t/2)<=25/(8t²), the recurrence real terms are negative, and25/8<7/2. The prior absolute trigamma and exponential-tail bounds finish it.

The complete bounded remainder obeys

`||R_0||<=C_R=2*pi*B_*+32*h_L/L+2*P_4 <34.450462`.

Adversarial normalization review corrected a preliminary pole bound32h/L² to the correct32h/L before integration. The obsolete preliminary constants60/301 are not results and their draft JSON is excluded from the evidence archive.

For g_n=(1−c)(log(n/L)−E_L(t_n))−kappa, c=10^(-8),

`U<=D_g+[kappa+2(1−c)E_L(t_*)+C_R]I`.

The ratio1+[...]/g_(N+1) is rigorously below66.76640 for the evenN512 tail and334.71708 for the oddN1536 tail. Therefore m=67 and335 are valid for the complete infinite tails. `certify_far_inverse.py` proves the strict gates independently at320 and384bits. This closes the upper-sandwich prerequisite for a convergent arithmetic inverse refinement at this one window. It closes no low-head or G2 sign gap.

### Uniform scales and next concrete work

The structured estimate yields the sufficient ordinary lower error

`alpha_lambda+e_lambda²+t_lambda²/mu_lambda`.

Here alpha controls the signed outer K_X, and e and t are **operator norms on the entire outer head**. If only columnwise residual bounds delta are available, their operator norm squared can be d_lambda delta²; equal columns show that factor is sharp. A negative congruence bound CLC*>=−eta I converts to ordinary error eta||C^(-1)||², not eta. All these factors remain separate from the previously proved eta C_lambda/(1+eta) weighted-to-ordinary conversion.

The inverse-polynomial error on a residual matrix Y is bounded by(1−1/m)^k Y*D_g^(-1)Y. A growing-window application therefore needs the actual m_lambda and residual operator norm, for example ||D_g^(-1/2)Y||² exp(−k_lambda/m_lambda)->0. The integers67/335 are not asserted uniformly in lambda.

**Next concrete step:** certify the signed quadratic correction from the first inverse polynomial, including its entire remote contribution, on the fragile low-head directions. If insufficient, add further monotone inverse-polynomial terms with a certified full-operator remainder. Reuse the saved exact ceiling witnesses to measure which loss is actually reduced. Prove the full low-head sign before attempting ground ordering; then identify independent arithmetic estimates for a cofinal window family. Do not repeat precision-only or Young-parameter-only experiments on the already falsified candidates. The odd low-head sign also remains unproved; no even-only result is extrapolated to the complete form.

---

## Current research checkpoint: September 21, 2026 — v1.20 signed energy control on the complete lambda=4 Fourier tail

**Established:** at lambda=4, for every complex vector in the closed Weil form domain supported on literal Fourier indices |n|>16,

`QW_4(f,f) >= 10^(-8) sum_(|n|>16) (-A_n)|f_n|^2`.

The exact archimedean diagonal is retained and is positive on this tail; its proved lower bound is greater than 1.7940. Both complex parity sectors and every omitted Fourier mode are covered by interval certificates and analytic remote moment bounds. This closes a **larger fixed-window tail-sign obligation**. It does not prove full positivity at lambda=4, and **no growing-window G2 sign gap was closed**. G2 and RH remain open.

### Current input and selected target

Fresh saved-file reads confirmed v1.19, its current log and revision notes. Remote materialization returned transient HTTP502 errors; the exact just-saved local working copies remained available with matching authoritative file identities, versions and byte sizes. Those current copies were retained, not reconstructed from an earlier scratch state. The cumulative archive is preserved and validated. The prior checkpoint's next target was a frequency-weighted comparison retaining the increasing logarithmic diagonal and the signed arithmetic matrix.

We set `D=diag(a_n)`, `a_n=-A_n` exactly, on a tail where it is positive. Write the actual compressed operator as `W=D+R`, retaining prime, signed pole and off-diagonal archimedean terms in R. The exact positivity target is `D^(-1/2) R D^(-1/2) >= -I`. A two-sided norm contraction is stronger and need not hold.

### First attempt: a two-sided energy norm bound fails

A floating exploration assembled the actual Fourier matrices at lambda=3,4,5,8,10,16,24 with literal cutoffs and separate diagonals. At lambda=4, N=16, M=256, the even normalized matrix had a positive top eigenvalue about 2.05254. At several larger windows the computed lower eigenvalues reached double-precision noise. Those tiny negative values are unresolved roundoff, not negative Weil directions.

An exact dyadic vector suggested by the positive eigenvector was then certified in Arb. It is supported on 17<=|n|<=256 and satisfies

`2.05254409540345 < QW_4(v,v)/<Dv,v> < 2.05254409540346`.

Its energy minus twice its exact diagonal energy exceeds0.0525 in the saved normalization. This disproves `||D^(-1/2)(W-D)D^(-1/2)||<=1` at that tail, because of a positive direction. It does not disprove the desired one-sided sign. This correction motivated the successful signed calculation.

### Successful one-sided certificate

Apply the existing directional verified-solve machinery to `W_4-cD` with exact c=1/100000000 on Q16. All finite rows use the full actual arithmetic matrix. The exponential archimedean-series tails are bounded explicitly. The exact pole diagonal has denominator `(L^2+16*pi^2*n^2)^2`; it is never a divided-difference limit.

A physical weight `phi(x)=exp(-x/2)+exp(-(L-x)/2)` yields a prime norm upper bound below4.624042316766478. The ratio is a linear-fractional function of u=exp(x) between rational breakpoints1,16,m,16/m. Every one-sided breakpoint is evaluated and the selected upper endpoint is rigorously checked against every candidate. The active prime powers are2,3,4,5,7,8,9,11,13; m16 is a zero full-length translation.

Use R_L=64/255, C_L=1 and h_L=9/16. The remote inverse weights are

`g_n=(1-c)(log(n/L)-E_L(2*pi*n/L))-kappa`,

with `kappa=M_phi+2/t_*` for even parity and the additional `pi/2+4h_LL/(pi^2N)` for odd parity. Only the archimedean diagonal is scaled by1-c. The off-diagonal losses remain unscaled.

Parameters:

| sector | finite head indices | solve support | remote starts after | moment order |
|---|---|---|---|---|
| even |17..512 |513..1024 |4096 |48 |
| odd |17..1536 |1537..2048 |4096 |64 |

The respective remote lower constants exceed0.59418 and0.12179. The finite heads have496 and1520 coordinates. These are internal certification blocks; the literal tail being proved starts at17 throughout. The large remote cutoff is not claimed to have disappeared.

The exact frozen dyadic solve Z gives G=I-Z, signed K_Z and residual R. All rows through4096 are computed. The existing full-index moment formula supplies an upper Gram for both infinite tails, with squared geometric remainder constants about1.025e-60 (even) and4.716e-41 (odd). The lower matrix is

`L_cert=K_Z-sum(R_n*R_n/g_n)-U_J/g_(J+1)`.

An inverse-Cholesky matrix proposed in double precision is frozen to exact dyadics C. It is only a witness. Outward interval evaluation verifies every row of `C L_cert C*` is strictly diagonally dominant with positive diagonal. This proves positivity of L_cert independently of how C or Z were computed. Square completion proves the complete infinite-tail bound. Reflection decomposes the complex Hilbert space into orthogonal even and odd reducing sectors, so the two certificates prove the assertion for arbitrary complex vectors.

The even witness was replayed at256 and320 bits with every positivity gate checked. The odd witness was formed at256 bits and replayed at320 bits with the tightened gates. The same dyadic witness hashes must match. The current reports, rather than the preliminary floating pilot, are the proof artifacts.

### Adversarial corrections and discarded intermediates

An independent assembly comparison found an early coding error: the new pole diagonal used the square of an already squared denominator. The error was corrected before any result was integrated. All old `sequences_l...` caches and their preliminary outputs are excluded from the evidence archive; only `sequences_v2...` can be read by the final verifier. The corrected Arb and independently assembled double sequences agree to below1.8e-13 through index256. This comparison is a diagnostic, not the proof of those entries.

The adversarial reviewer also tightened two gates: choose the prime bound by comparing exact upper endpoints, not floating midpoint ordering; verify every Gershgorin row is positive, not merely the row chosen by a floating minimum. The certificate directly checks that the analytic archimedean lower estimate at n17 is positive. The final runs use these gates. Full residual rows, all scale factors and the correct first-slot-linear interpretation are retained.

### Analytic results that delimit the weighted route

1. **Ordinary-error conversion.** If D>=d0I>0, R>=-CI and D^(-1/2)RD^(-1/2)>=-(1+eta)I, then `W>=-eta*C/(1+eta) I`. The proof combines W>=-eta D and W>=D-CI. The scalar model D=C/(1+eta), R=-C proves sharpness. Thus eta_lambda->0 alone is insufficient when C_lambda grows; the sufficient ordinary-error scale is eta_lambda*C_lambda->0. No signed arithmetic estimate is assumed to follow from this reduction.

2. **Compact but not Schatten.** For every fixed window with an active prime shift and every positive diagonal a_n~log|n|, the weighted prime operator is compact but in no finite Schatten class. Its diagonal is a nonzero finite cosine sum divided by a_n. The numerator has a strictly positive Cesaro mean square, without any rational-independence assumption, and is bounded away from zero on a positive-density set. Its pth-power diagonal sum therefore diverges. For the exact archimedean diagonal the complete signed remainder has the same obstruction: the pole correction is O(n^-2) and the archimedean remainder has zero diagonal. A global weighted Frobenius tail budget is impossible. This does not affect separated finite-column residual Grams, which retain off-diagonal decay.

3. **Sharp fixed-window weighted-tail scale.** At each fixed lambda, `(log J)||Q_J D^(-1/2) T_pr D^(-1/2) Q_J|| -> ||T_pr||`. Compact subtraction before weighting leaves the leading constant unchanged. The lower bound uses a fixed norm-testing Fourier polynomial and relatively dense returns of the finite vector of shift phases; the upper bound follows from the minimum diagonal. The recurrence gap depends on the window and tolerance. This theorem cannot be combined with ||T_pr||~lambda to claim a uniform lambda/log(J_lambda) lower bound in a joint limit. No such quantitative recurrence rate is proved.

### Primary-source research and scope

The actual Fourier matrix was checked against Connes, Consani and Moscovici, *Zeta Spectral Triples*, arXiv2511.22755v1, Sections3–4: https://arxiv.org/html/2511.22755v1. Their opposite sesquilinear convention is translated as already fixed in the manuscript; the real Hermitian entries and quadratic signs are unchanged.

A relevant new comparison is Xuefeng Zhu, *Weil positivity in compact windows: a finite reduction, certified two-sided bounds, and a Landau–Widom decay law*, arXiv2608.24827v2, revised September2,2026: https://arxiv.org/abs/2608.24827v2. It studies finite-window certification and a pointwise prime-comb envelope barrier. This is contextual related work; no external computational certificate or conjectured asymptotic is imported into our proof. Its finite-window conclusions do not supply uniform G2.

### Next concrete obligation

At lambda4 the positive tail reduces full positivity to the signed effective matrix `F-B*T^(-1)B` on E16, with17 even and16 odd coordinates. This is a33-dimensional effective problem with an infinite inverse correction, not the raw33-by33 Weil matrix. Next compute and certify an inverse-action enclosure for these remaining columns using the newly proved tail lower weights. A failure of a lower enclosure must not be called a negative Weil direction.

For G2 itself, the remaining task is an ordinary lower bound tending to zero along an unbounded family of windows, with the arithmetic scale in the weighted-to-ordinary conversion retained. The known weak G1, the zero continuum endpoint, the literal physical evaluation and Fourier cut, the separate logarithmic diagonal, and the sampler's explicit graph defect are unchanged. No publication or outside contact occurred.

**Completed validation:** v1.20 has143 pages,442 unique labels,32 main sections,two appendices and the unchanged72-claim historical ledger. All431 prior labels remain. Both320-bit frozen-witness parity replays pass every sign gate, with lower Gershgorin margins above0.9999999999. Every PDF page was rendered and visually reviewed; new proof pages90–93,title,research-goal page127 and reproduction page137 received detailed review. The final LaTeX build has no warnings, unresolved references or overflow. The cumulative archive is checked for CRC and exact hashes of all current deliverables and new evidence.

## Previous research checkpoint: September 21, 2026 — v1.19 finite-source removal cannot shrink the unsigned prime norm

**Established:** every finite-codimension compression of the actual prime-shift operator has exactly its full ordinary operator norm. Its essential norm is the same, and subtracting a compact operator, including the rank-two pole operator, cannot reduce the complementary norm below that value. The sharp leading growth is `||T_pr||=(1+o(1))lambda`. **No G2 sign gap was closed.** These results rule out a small unweighted complementary arithmetic norm, not full signed Weil positivity or RH.

### Starting point and concrete attempt

Fresh reads and materialization recovered the complete v1.18 manuscript, current research log, revision notes, validation record and cumulative evidence bundle. The saved PDF was confirmed as v1.18, 137 pages. The prior checkpoint established zero continuum eigenfunction endpoints and the sharp gap-free complement reduction. Its next obligation was a signed bound for the entire source-orthogonal complement along growing windows.

This run tests a simpler possible prerequisite: could removal of a sufficiently large finite source block, or of a finite Fourier head, make the prime term small enough for the archimedean diagonal to dominate using an ordinary operator-norm estimate? This was not assumed. It is now falsified exactly. The prime norm's previously discussed large arithmetic scale is proved for the actual operator, not just for the sum of its coefficients.

### Exact recurrence and finite-rank obstruction

At fixed lambda let L=2log(lambda) and let T_pr be the bounded self-adjoint sum of both truncated translations by log(m), weighted by Lambda(m)/sqrt(m), with 1<m<lambda^2. A full-length translation is zero. For periodic integer modulations M_k f=exp(2pi i kx/L)f, conjugation only inserts the finitely many shift phases.

Pigeonhole simultaneous recurrence provides k_j->infinity for which all active phases tend to one. The proof covers exact rational recurrences as well as approximate irrational returns, and does not require rational independence of prime logarithms. Thus

`||M_kj* T_pr M_kj - T_pr|| <= 2 sum_m w_m |exp(2pi i k_j log(m)/L)-1| -> 0`.

For each fixed L2 vector f, M_kj f tends weakly to zero by the Riemann–Lebesgue lemma. Any finite-rank projection P and any compact C consequently satisfy P M_kj f->0 and C M_kj f->0 in norm. Writing Q=I-P gives

`Q(T_pr-C)Q M_kj f - M_kj T_pr f -> 0`.

Taking norms and a supremum over unit f proves `||Q(T_pr-C)Q|| >= ||T_pr||`. With C=0, compression contractivity proves equality. With P=0, taking the infimum over compact C identifies the essential norm. No domain assumption is needed for the finite-rank source block; all operators involved here are bounded at fixed window.

The statement is pointwise in lambda and therefore applies to any family of finite-rank removals, however quickly the finite ranks grow with lambda. It does not provide a recurrence frequency bound uniform in lambda. The optional parity strengthening suggested in review is not needed and is not claimed in this release.

### Sharp actual operator scale

Use the positive physical weight `phi(x)=a(x)+b(x)`, with `a=exp(-x/2)` and `b=exp(-(L-x)/2)`. Define strict sums `Psi(X)=sum_(1<m<X) Lambda(m)` and `S(X)=sum_(1<m<X) Lambda(m)/m`. Direct substitution gives

`T_pr phi / phi = [a(S(exp(L-x))+Psi(exp(x))) + b(Psi(exp(L-x))+S(exp(x)))]/(a+b)`.

The leading constant follows from the exact identity `a exp(x)+b exp(L-x)=lambda(a+b)`. For any delta>0, the unconditional prime number theorem supplies a finite C_delta such that `|Psi(X)-X|<=delta X+C_delta` for every X>=1, including the small-X range. Chebyshev and partial summation give `0<=S(X)<=C(1+log X)`.

Uniformly in physical position,

`(1-delta)lambda-C_delta <= T_pr phi/phi <= (1+delta)lambda+C_delta+C(1+L)`.

The weighted Schur inequality proves the upper norm bound; the Rayleigh quotient of phi proves the lower. Divide by lambda, let lambda grow, and then let delta decrease to zero. This proves the exact leading asymptotic `||T_pr||/lambda->1` without RH. The finite-rank norm equality transfers it unchanged to every finite-codimension complement.

Primary reference for the classical prime number theorem: NIST DLMF Section 27.12, https://dlmf.nist.gov/27.12. The equivalence with the von Mangoldt form follows by partial summation and the smaller prime-power contribution. The operator argument and normalization are written out in the manuscript, not imported from the source.

### Consequence and explicit limits

For the paper's specific whole-space scalar tail budget, which subtracts an unsigned prime norm and other nonnegative errors from log((N+1)/L), positivity requires

`log((N+1)/L) > ||T_pr|| = (1+o(1))lambda`.

Even using the exact compressed norm cannot remove this exponential-in-lambda cutoff requirement. Enlarging a finite source block does not help that scalar-norm method. The pole operator is rank two, hence its inclusion cannot make the ordinary norm of the combined prime/pole operator small on the finite-codimension complement.

This is not a necessary cutoff for actual Weil positivity. The modulation sequence can recover the prime norm only at frequencies much higher than the first omitted mode, where the archimedean logarithmic energy is correspondingly larger. Consequently frequency-weighted unsigned estimates and directional inverse-action bounds are not excluded. The prior broadly worded sentence about every scalable complement theorem requiring signed cancellation was narrowed to avoid claiming otherwise. No negative direction of the complete Weil form is obtained.

### Independent review and computational checks

A separate adversarial agent checked recurrence, weak convergence, finite-rank removal, exact shift weights, the positive weight identity, the uniform-in-position PNT estimate and the scope of the scalar-budget conclusion. The saved review explicitly distinguishes the failed ordinary-norm shortcut from viable frequency-weighted estimates. This is internal review only.

The numerical script checks the exact autocorrelation formula for phi and independently integrates the physical quadratic form at lambda=2 and3. At 60 decimal digits the discrepancy is below 1e-50. It also evaluates trial Rayleigh values at lambda=2,3,5,10,30,100,300; the ratio to lambda is approximately 1.026889 at lambda=300. This is neither an interval norm certificate nor the asymptotic proof.

At lambda=2, a concrete integer modulation k=381074 leaves normalized P64 head norm about 9.52e-13, while the prime Rayleigh quotient differs from the unmodulated trial value by about 4.7e-14. These non-certified computations illustrate recurrence and escape from a finite head. They are not evidence of a negative complete-Weil direction or evidence for RH.

### Result of the attempted route and next step

The attempt to obtain a small unweighted prime/pole norm by finite source removal fails by theorem. The two new analytic results sharpen the obstruction and prevent repeated work on that false prerequisite. They do not establish the complementary arithmetic sign or close G2.

The next concrete test is a frequency-weighted prime comparison on the actual Fourier tail: retain the increasing positive logarithmic diagonal inside the two-sided inverse-square-root weighting instead of replacing it by its minimum. Quantify the directional weighted norm or residual Gram as lambda grows, with the exact signed pole and archimedean terms retained. A finite-window diagnostic can test this bound, but a proof requires uniform control on an unbounded family. Keep source removal, literal Fourier cut and sampler graph defect explicit. No publication or outside contact occurred.

**Completed validation:** complete v1.19 is 139 pages, with 431 unique labels, all 32 main sections, two appendices and the 72 historical ledger rows retained. Every PDF page was rendered and visually reviewed, with the new proof on pages 89–90, title, goals and reproduction summary checked at higher resolution. The final build has no warnings, unresolved references or overflow. An incomplete intermediate build was discarded and rebuilt in a fresh directory; only the complete, closed, parseable PDF was installed. Truncated intermediate image renders were regenerated. The cumulative archive retains all prior evidence and is independently checked for CRC and current artifact hashes.

## Previous research checkpoint: September 21, 2026 — v1.18 continuum endpoint proof and complementary sign reduction

**Established:** every eigenfunction of the complete canonical fixed-window Weil operator has a bounded representative with continuous zero physical boundary trace. Its boundary decay is at most a constant times the inverse square root of the logarithm of inverse boundary distance. This settles the continuum endpoint question and **falsifies the proposed nonzero endpoint comparison with the repaired source**. A sharp complementary-form estimate removes an unnecessary positive-gap hypothesis from one growing-window route. **The growing-window arithmetic sign, G2 and RH remain open.**

### Starting point and selected obligations

Fresh saved-file reads confirmed the complete v1.17 manuscript and persistent log. That release had already certified positivity, simple even ground ordering and an ordinary source-to-ground overlap at lambda=3 for the complete operator. Its open targets were control as the physical window grows and the physical endpoint of the actual ground state. This checkpoint addresses both analytically. The valid cumulative v1.17 archive was read and checked locally; no missing historical result was reconstructed by assumption.

The endpoint goal needed correction. Small ordinary residual and ordinary overlap do not themselves transfer an endpoint. Instead of extrapolating a finite endpoint numerically, we identified the singular part of the actual operator and proved its boundary regularity. The analysis uses the actual first-slot-linear convention, physical logarithmic interval (0,L), L=2log(lambda), normalized basis L^(-1/2) exp(2pi i n x/L), exact prime/pole signs and logarithmic diagonal. It does not modify the literal Fourier cut or remove the corrected sampler's graph defect.

### Exact operator identity and domain gate

Write A=(1/2)L_Delta^Dir for the restricted, exterior-Dirichlet logarithmic Laplacian, with full-line symbol log|t|. This is not the spectral logarithm of the Dirichlet Laplacian. The complete operator equals A+K_lambda, with equality of operator domains. K_lambda consists of:

- the scalar -log(2pi);
- the symmetric kernel minus k(|x-y|), k(y)=exp(y/2)/(2sinh(y))-1/(2y), with k(0)=1/4;
- the actual negative truncated prime shifts, including both orientations;
- the signed pole contribution 2cosh((x-y)/2), retaining its negative sinh rank-one part.

The scalar follows exactly from the integral of csch(y)-1_(y<1)/y, which is log(2). A common bound on all L^p norms of K_lambda is log(2pi)+2 integral_0^L |k(y)|dy+2P_lambda+4sinh(L/2). Compactly supported smooth functions form a common closed-form core: smooth endpoint tapers of a finite periodic Fourier sum converge in H^s for every fixed 0<s<1/2, hence in the logarithmic form norm. This identifies the realizations without imposing the endpoint conclusion as a premise.

### Bounded eigenfunctions, then the boundary theorem

An arbitrary L2 eigenfunction is not assumed bounded. For small epsilon, split

`A = A_epsilon + (log(1/epsilon)-gamma)I - J_epsilon`,

where A_epsilon is the nonnegative killed small-jump generator and J_epsilon integrates f(y)/(2|x-y|) over |x-y|>=epsilon. The first resolvent is a contraction on both L2 and L-infinity, while J_epsilon maps L2 to L-infinity with norm at most (2epsilon)^(-1/2). Choose a=log(1/epsilon)-gamma-mu>||K_lambda||. The same convergent Neumann series in L2 and L-infinity solves (A_epsilon+a+K_lambda)u=J_epsilon u. Uniqueness identifies its bounded solution with the original eigenfunction.

Consequently L_Delta u=2(mu u-K_lambda u) has bounded right-hand side. The interval satisfies the exterior uniform sphere hypothesis of Hernandez-Santamaria, Lopez Rios and Saldana, Theorem 1.1. Their theorem now applies and gives continuous zero extension and

`|u(x)| <= C sqrt(ell(d(x)))`, `ell(r)=1/|log(min(r,.1))|`, `d(x)=min(x,L-x)`.

The argument applies to every eigenfunction, without positivity or spectral-order assumptions. For complex functions it applies to real and imaginary parts. The constant is fixed-window and may depend on lambda, the eigenvalue and the eigenfunction. No useful uniform growing-window constant was established.

### Endpoint consequences and the failure of graph-norm transfer

Since the repaired source has nonzero physical endpoint B_lambda, the complete eigenfunction has exact relative endpoint mismatch `|p_lambda(0)-c u(0)|/|B_lambda|=1` for every scalar c. This falsifies nonzero continuum endpoint matching. It does not negate the prior ordinary overlap certificate or the finite source endpoint calculations.

A positive Fejer kernel gives the quantitative filtered endpoint estimate

`|sigma_(N-1) u(0)| <= C sqrt(ell(L/sqrt(N))) + ||u||_infinity/(2sqrt(N))`.

The normalization is the actual physical L^(-1/2) Fourier factor. The proof splits at distance L/sqrt(N), with far-kernel mass bounded by 1/(2sqrt(N)). This is an O((log N)^(-1/2)) fixed-window filtered estimate. It does not assert convergence of sharp Fourier endpoint sums or supply a joint cutoff/window estimate for finite-compression eigenvectors.

There is an exact counterexample to physical trace continuity in the Weil graph norm. The real even shell `h_N=sqrt(L)/(2N) sum_(N<|n|<=2N) U_n` has endpoint one and norm sqrt(L/(2N)), whereas its complete Weil operator norm is O_lambda(log N/sqrt(N)). Thus the endpoint map on the polynomial core is not even closable in that graph norm. This does not preclude the independently obtained zero continuous trace on actual eigenfunctions; it explains why graph convergence alone cannot prove it. The distinct logarithmic-derivative graph defect in the sampler is retained.

### Sharp complement bound, and what it does not prove

For a lower-bounded self-adjoint A, a finite-rank orthogonal P with range in D(A), Q=I-P and ||AP||<=epsilon, the exact form expansion yields

`|q(f,f)-q(Qf,Qf)| <= (2/sqrt(3)) epsilon ||f||^2`.

Indeed, with h=Pf and g=Qf, the difference equals Re<Ah,h+2g>. The maximum of t sqrt(4-3t^2) is 2/sqrt(3). The constant is sharp, witnessed by `A=-(epsilon/sqrt(3))*[[1,sqrt(2)],[sqrt(2),0]]`. Therefore a complementary lower bound q|Q>=-eta I implies `inf spectrum(A)>=-eta-2epsilon/sqrt(3)`, without a positive complementary gap.

The prior full operator residual supplies epsilon_lambda->0 for the rank-one projection onto either normalized repaired source considered in Proposition 20.39. The remaining input can therefore be phrased as asymptotic nonnegativity of the whole source-orthogonal complement. A growing source block would need an additional uniform ||W_lambda P_lambda||->0 estimate.

This reduction does not establish the complementary sign. A fixed negative compact test of energy -delta remains negative after projection off any block whose operator residual tends to zero: its projected energy is <=-delta+2epsilon/sqrt(3). Thus source removal cannot hide an RH-violating compact direction. The desired cofinal complementary sign remains RH-strength by the paper's existing nested-support criterion. The nested-window and RH-strength observations were already in the paper and are not counted as new results.

### Adversarial review, sources and diagnostics

Two independent agent reviews checked the exact kernel normalization, form-domain identification, boundedness bootstrap and the boundary theorem hypotheses. The complementary inequality and the graph-trace counterexample were separately checked. These are internal reviews, not external referee validation.

Primary sources consulted:

- Chen and Weth, *The Dirichlet Problem for the Logarithmic Laplacian*, Theorems 1.1 and 3.1: https://arxiv.org/pdf/1710.03416.
- Hernandez-Santamaria, Lopez Rios and Saldana, *Optimal boundary regularity and a Hopf-type lemma for Dirichlet problems involving the logarithmic Laplacian*, Theorem 1.1, version 2 (July 3, 2024): https://arxiv.org/pdf/2401.18033.

The archived 90-decimal diagnostic compares the original and decomposed constant-mode archimedean diagonal at lambda=1.2,2,3,10. The largest discrepancy is below 5e-91. This detects normalization mistakes but is not a proof; the exact integral establishes the identity. No numerical endpoint extrapolation is used in the boundary theorem.

### Failed approaches, scope and next concrete step

1. Nonzero endpoint transfer from the source to the complete ground is false, not merely unproved.
2. Ordinary operator residual or graph-norm control cannot by itself control the physical trace; the shell above disproves that implication.
3. Continuity of a periodic representative does not alone justify sharp Fourier endpoint convergence. Only the specified positive filter is estimated here.
4. The new block inequality removes a gap denominator but leaves the arithmetic complementary sign unresolved. It is not a positivity proof.

Next, seek a signed lower estimate for the entire source-orthogonal complement as lambda grows, using the existing physical prime/pole/archimedean decomposition and retaining the directional Schur residual. A larger-window certificate can test the proposed bound but cannot replace the unbounded-window argument. Finite-compression endpoint control, when needed for a sampler construction, must be estimated on that actual finite object rather than through a nonzero continuum ground endpoint. G2 and RH remain open; no G2 sign gap was closed. No publication or outside contact occurred.

**Completed validation:** 137 pages, 423 unique labels, all 32 main sections, two appendices and all 72 historical dispositions retained. The complete PDF was rendered and visually reviewed; new proof pages 75–78 and 87–88, the title, research goals and reproduction summary were also reviewed at larger scale. A short front-matter spill page was removed by condensing duplicated status prose. The final build has no warnings, unresolved references or overflow. One truncated intermediate page render was regenerated; the PDF was intact.

## Previous research checkpoint: September 21, 2026 — v1.17 complete ground ordering at one window

**Closed an additional fixed-window obligation:** the complete canonical Weil operator at lambda=3 has a simple even ground state, with `0<mu0<3.644e-38`, every other even eigenvalue greater than `1e-34`, and every odd eigenvalue greater than `1e-36`. Consequently the full next eigenvalue is greater than `1e-36`. The exact normalized P64 p3 has ordinary ground-angle sine less than `0.01931`. **No growing-window G2 gap was closed; RH remains open.**

### Starting point and selected obligation

Fresh reads of the saved v1.16 complete manuscript, persistent log and evidence bundle confirmed the prior checkpoint. v1.16 already proved complete fixed-window positivity, including all omitted modes. The selected next obligation was its recorded shifted-operator test: establish parity, simplicity and separation of the actual lowest state, then connect the exact projected source by a quantitative ordinary overlap bound. We retained the first-slot-linear convention, physical basis, literal Fourier cut, separate logarithmic diagonal and all parity factors. The corrected sampler and its graph defect were not altered.

### Exact shifted identity and certified inertia

For each exact threshold a, the implementation shifts every actual diagonal `d_n` and every tail inverse weight `g_n` by a. It uses the unchanged frozen exact dyadic witness Z from v1.16. With `G=(I_head,-Z)^T`, the identities are

`K_Z(a)=K_Z(0)-a(I+Z*Z)`, `R(a)=R(0)+aZ`.

Every finite residual row through J=4096 is recomputed, including the middle rows affected by the shift. Remote rows have no diagonal entry, so their moment Gram majorant is unchanged; its inverse weight is still shifted. The full bound is

`S_a >= L_a = K_Z(a)-sum R_n(a)*R_n(a)/(g_n-a)-U_remote/(g_(J+1)-a)`.

All inverse weights are positive. Interval LDL continues through negative pivots and requires every pivot to exclude zero. The exact successful tests are:

| Sector | Threshold | N / M / J / moment order | Pivot signs | Precision replays |
|---|---:|---|---|---|
| Even | 1e-34 | 256 / 512 / 4096 / 80 | 1 negative, 256 positive | 768 and 896 bits |
| Odd | 1e-36 | 512 / 1024 / 4096 / 100 | all 512 positive | 768 and 896 bits |

The one negative even pivot is at zero-based index 24. Its size, and every other pivot size, is NOT an eigenvalue estimate. Witness hashes are unchanged from v1.16: even `993c5b325c1cc7dce64c1dbdab9384dd54dea6a480cce8739cf623e9e8bce43c`; odd `4054507110d6a806c3dfa926c716c1692de4c9b7dc7801263d50b92cbd8dfdea` (SHA256 of uncompressed exact witness JSON). Each 896-bit replay reuses precisely the same witness as its 768-bit run.

### Matching trial direction and actual spectral conclusion

The signed inertia is for a LOWER Schur form. Its negative pivot alone supplies no negative direction of the exact shifted operator. The required matching direction comes from the existing exact rational, finitely supported even candidate u at N=64. Its full-form Rayleigh quotient is exactly its finite-compression quotient, alpha=5.312381700586359...e-38.

A separately verified finite correction uses `z=(C-alpha I)^(-1)r`, with z orthogonal to u, and `v=(u-z)/sqrt(1+||z||^2)`. Direct expansion proves the exact identity

`beta=QW3(v,v)=alpha-<z,r>/(1+||z||^2)`.

The prior finite inverse certificate and a new direct 768-bit enclosure both imply beta<3.644e-38 (new enclosure 3.643399656992330629578...e-38). Thus the complete even shifted operator has at least one negative direction. Its lower Schur form has positive second eigenvalue, so min--max allows at most one nonpositive even level. Square completion on the established form domain transfers negative index, and kernels correspond. Hence exactly one even eigenvalue lies below 1e-34, and none equals that threshold. The odd certificate puts all odd levels strictly above 1e-36. Compact resolvent, the old full positivity certificate, and beta<1e-36 identify the global ground as simple and even.

The proof does not confuse a finite-compression gap with a complete-operator gap. The author-hosted source consulted for min--max and its form-domain version was G. Teschl, Mathematical Methods in Quantum Mechanics (2009), Section 4.3, https://www.mat.univie.ac.at/~gerald/ftp/book-schroe/schroe.pdf. The square-completion and index argument is written explicitly in the manuscript.

### Exact projected-source overlap

All non-ground even spectrum lies above 1e-34. Positivity and the corrected trial energy imply `sin angle(v,xi0)<sqrt(3.644e-38/1e-34)`. The finite correction contributes less than .000216 in rank-one projector norm. Their sum is below .019305264 and hence .01931.

The exact source certificate gives `||P64 p3-c||<2.60e-36`; direct rational normalization gives `||c||>0.65172555`. Elementary ball geometry bounds the normalized-vector distance by less than 4e-36. This fits inside the displayed angular margin and transfers the claim to the exact normalized projected source. It does not transfer a tiny energy by an ordinary perturbation bound, nor does it identify the unprojected source with the ground. The earlier certified 137.4%–137.5% relative endpoint error at N64 is unchanged.

### Failed or insufficient attempts, retained as failures

1. The odd lower Schur matrix at the stronger shift 1e-34 had one negative pivot (index 85). This failed to certify the desired odd lower threshold. It does NOT prove that an actual odd level lies below 1e-34. The weaker sufficient threshold 1e-36 passed and suffices to order the ground.
2. The exact candidate's complete centered residual was enclosed between 3.3368484596e-19 and 3.8871364266e-19, including all rows through 4096 and a remote moment bound. Dividing this by the available tiny separation gives an ineffective ordinary residual/gap estimate, of order 1e15 even with the larger even threshold. The successful overlap argument instead uses independently proved positivity and the trial energy.
3. Neither the ordinary angle nor simple ground ordering controls the physical endpoint trace. No endpoint claim, uniform spectral theorem, or RH implication was inferred from the fixed-window computation.

### Adversarial review and evidence integrity

Two internal agents independently checked the trial normalization, signed-inertia direction, zero-threshold exclusion, parity ordering, form-domain square completion and overlap geometry. The same exact witnesses passed higher-precision replays. This is a computer-assisted proof with analytic infinite-tail bounds and outward intervals, not proof-assistant verification or external peer review.

An integrity check found the prior saved v1.16 ZIP truncated (33,355,678 bytes, missing its central directory). The manuscript, PDF, log and individual evidence files were intact. All 37 v1.16 reproducibility files were checked against their previously recorded SHA256 values, with no mismatches; both dyadic witnesses decompressed correctly. The cumulative archive was rebuilt from the valid v1.15 bundle plus those checked files and the v1.16 root documents. The recovered v1.16 archive is 42,113,921 bytes with 118 intact members. The present v1.17 archive is built from that recovered base using a temporary file, flush/fsync and atomic rename, followed by an independent ZIP CRC check. No mathematical evidence was reconstructed from unverified numerical output.

### Manuscript integration and next concrete step

The complete manuscript is v1.17. The abstract, status, Section 20 proof, Section 32 goals, reproduction appendix and bibliography are updated; all 72 historical claim dispositions and prior labels are retained. Failed sufficient tests stay in this log rather than appearing as negative Weil-form results.

The next substantive target is a larger physical window: generalize the coefficient assembly and weighted prime-tail constants, build a complete low-mode block certificate, and measure how the signed inverse correction and remote moments scale. The eventual obligation is an independently justified error bound along an unbounded window sequence, not a list of successful fixed examples. Endpoint stability for actual ground vectors, uniform source-block control, the sampler graph defect and full-strip transfer remain separate. G2 and RH remain open; no publication or outside contact occurred.

**Completed validation:** 132 pages, 410 unique labels, 32 main sections, two appendices and all 72 historical dispositions. The whole PDF was rendered and visually inspected, with new proof pages 73–75 and changed front/reproduction pages checked at larger scale. The final LaTeX build has no warnings, unresolved references or overflow. A truncated contact-sheet PNG was regenerated; the PDF itself was intact.

## Previous research checkpoint: September 21, 2026 — v1.16 complete fixed-window positivity

**Closed: the signed head/complement positivity obligation for the complete canonical Weil form at lambda=3, including both parity sectors and every omitted Fourier mode. G2 along unbounded windows and RH remain open.** The full manuscript is v1.16, 129 pages, with 32 main sections, two appendices, 407 unique labels and all 72 historical claim dispositions retained.

### Starting point and selected obligation

Fresh reads of the saved v1.15 manuscript, research log, notes and bundle confirmed the current versions before work began. v1.15 supplied the canonical logarithmic-domain operator, a positive entire Fourier tail, ordinary source mass and a small full source residual. It did not certify the signed head/complement correction. This continuation targeted that concrete missing fixed-window estimate, following the previous log's proposed inverse-action/moment route. Three internal agents supplied an independent numerical pilot, the remote-moment proof and an adversarial audit. No positivity, zero-location or RH assumption was introduced.

### Proved: a stronger independent arithmetic tail bound

Proposition 20.22 applies the positive-weight Schur test to the actual truncated prime translations on [0,L], L=2 log 3. With phi(x)=cosh(x-log 3), the exact prime norm bound is

`m3=(85/116)w2+(65/87)w3+(193/232)w4+(137/145)w5+(35/29)w7`, where `wm=Lambda(m)/sqrt(m)`.

It is between 2.6890557719319011796 and 2.6890557719319011797. On each physical shift interval the weighted ratio is monotone; its one-sided endpoint values are rational combinations of the six actual prime-power weights. All comparisons and resulting tail constants were enclosed by 256-bit Arb arithmetic. The m=8 term is included wherever active; the full-length m=9 shift is exactly zero as an L2 operator. This improves the entire-tail bounds at N=256 to more than .4970 for all vectors and 2.0690 for even vectors, and at N=512 to more than 1.1907 for all vectors.

Proposition 20.23 preserves the frequency-dependent archimedean diagonal rather than replacing it by its minimum. With the base cut N retained in all norm losses, `T >= Dg`, where

`g_n=log(|n|/L)-E_L(2*pi*|n|/L)-kappa`.

The constant kappa is m3 plus the common archimedean error; the odd/full case also retains pi/2 and the negative-pole tail cost. The positive weights increase with |n|. The variational inverse formula gives `T^(-1) <= Dg^(-1)` on the entire infinite complement. This is stronger than substituting a scalar gap into every residual row. It does not infer inverse order from positivity of a remote subblock alone.

### Proved: a directional bound for every remote residual row

Proposition 20.24 starts from the exact off-diagonal identity `W_nm=(b_n-b_m)/(n-m)`, keeping the separate diagonal for finite rows. For a finite lift G supported in |m|<=M, it retains the moments

`S_j=sum (m/M)^j G_m`, `T_j=sum (m/M)^j b_m G_m`.

The exact finite geometric expansion through order r has a leading Gram built from

`H_jk=M^(j+k)[1+(-1)^(j+k)] zeta(j+k+2,J+1)`.

The PSD upper bound is `(1+tau)[2B_*^2 S*HS+2T*HT]+(1+tau^(-1))delta^2 G*G`, where

`delta^2=8B_*^2 c_(M,r) M^(2r) zeta(2r+2,J+1)/(1-M/(J+1))^2`,

and `c_(M,r)=sum_(|m|<=M)(|m|/M)^(2r)`. The factor eight, both signed tails, the zero Fourier mode and every normalized parity sqrt(2) factor were independently checked. This is a quadratic-form bound for all input directions, not independent entrywise errors or a scalar norm times the identity.

Proposition 20.25 combines this with the exact signed identity. For `G=I_head-Z`, `R=Q_N W G`, and `K_Z=F-B*Z-Z*B+Z*TZ`, it proves

`K >= K_Z-sum_(N<|n|<=J) R_n*R_n/g_n-U_remote/g_(J+1)`.

All finite residual rows are present, including the nonzero middle residual from freezing an interval solve to a dyadic matrix. Z has finite support and therefore belongs to the proved operator domain. Square completion extends a finite lower certificate to the whole closed form.

### Computer-assisted result: complete coercivity at lambda=3

Proposition 20.26 certifies the actual complete Weil form, not just a Fourier compression. It uses the following exact parameters:

| Sector | Head dimension | N | M | J | r | Positive LDL pivots |
|---|---:|---:|---:|---:|---:|---:|
| Even | 257 | 256 | 512 | 4096 | 80 | 257 |
| Odd | 512 | 512 | 1024 | 4096 | 100 | 512 |

The two certificates use tau=1/1000000 and the earlier conservative global sequence bound B_*≈2.118745185946. The geometric remainder factors are below 1.656e-148 and 3.288e-124 respectively. These factors bound only the geometric remainders; the much larger leading moment Grams are included in full.

Every matrix entry is enclosed with Arb. The archimedean coefficient evaluation retains the exact digamma/trigamma part and 128 exponentially weighted terms, followed by explicit uniform radii. Every actual shorter prime-power shift and the separate logarithmic diagonal are retained. The new sequence assembly was compared with the previous independent integration certificate through N=64: all 8,321 even/odd entries overlap their reference enclosures. That consistency check supplements the analytic assembly proof.

The exact dyadic midpoint of the intermediate inverse solve is frozen as the witness. Every LDL pivot of the final lower matrix is strictly positive. The minimum pivot is approximately 9.17498693948e-9 (even) and 9.68026341053e-8 (odd). These are **not eigenvalue lower bounds**. Positive finite Schur matrices, the positive entire tails and the boundedly invertible square-completion map establish the existence of an epsilon_3>0 for the full closed form. No numerical value of epsilon_3 is asserted.

An independent agent replayed the identical witnesses at 896 bits, after the original 768-bit checks; all 769 pivots again pass. Their uncompressed exact-witness SHA256 values are:

- Even: `993c5b325c1cc7dce64c1dbdab9384dd54dea6a480cce8739cf623e9e8bce43c`.
- Odd: `4054507110d6a806c3dfa926c716c1692de4c9b7dc7801263d50b92cbd8dfdea`.

The witnesses, every pivot enclosure, assembly code, analytic derivations and replay reports are preserved in the cumulative bundle. This is internal mathematical and computational verification, not external referee review or proof-assistant formalization.

### Attempts that failed, and what those failures mean

1. Finite-output pilots were positive in the even N256/M512/J1024 case, but those calculations omitted every row beyond J. They were not treated as continuum certificates.
2. The first full even scalar-gap budget, with J1024/r128, had a rigorously negative LDL pivot at index 7. Increasing J to 4096/r80 moved the failure to index 28. The later diagonal inverse weighting passed with the same larger J. The earlier failures reject their conservative sufficient bounds, not the Weil operator.
3. The odd finite-output budget at N256 with a scalar gamma=.4970 failed. A larger N512/M1024/J2048 finite-output pilot passed, but its full remote scalar majorant failed at index 23. Even diagonal weighting at N256/M512/J4096 failed at index 41. The successful odd architecture uses N512/M1024/J4096/r100 and the growing diagonal weights.
4. Double-precision eigensolvers can report spurious negative values near 1e-15 where the energy scale is about 1e-38. Float vectors contaminate this energy at about the square of their ordinary error. Only certified ball arithmetic and the analytic tail bounds are used for the new sign result.
5. A sharper remote bound from the asymptotic trigonometric b sequence and exact Lerch sums was considered but not needed. It was not presented as a proved new certificate. Large-order special-function balls would need their own precision budget. Positive Hilbert finite-rank inverse refinements and annular weights are also optional future improvements, not inputs to this result.

### Primary-source research and adverse checks

The recent primary preprint [Weil positivity in compact windows](https://arxiv.org/html/2608.24827v2) was reviewed as an alternative certified-tail strategy. Its revision explicitly retracts an earlier larger-window claim and distinguishes finite-matrix evidence from continuum bounds. No certificate or asymptotic assertion from that paper is used here. The present proof instead controls the actual Fourier operator via physical prime shifts, diagonal inverse order and explicit remote moment Grams.

Adversarial review checked the weighted prime ratios, every finite comparison, archimedean and pole constants, common base-cut losses, inverse order, exact dyadic freezing, all intermediate residuals, source-independent moment inequalities, complex parity normalization, complete diagonal, series tails and the form-domain square completion. No blocking issue was found. An independent run verified both final certificates at higher precision using unchanged witnesses. The original first-slot-linear convention, physical endpoint, Fourier cut and corrected sampler graph defect remain in force.

### Integration and remaining target

The abstract, status, Section 20, Section 32 goals and reproducibility appendix now distinguish completed fixed-window positivity from the unresolved growing-window problem. The new proofs are on pages 67–73; the reproduction summary is on page 124. The full 129-page PDF was rendered and visually inspected, with close review of all new proof pages. One incomplete PNG was rerendered; the PDF itself compiled without warnings. All 407 references/labels are consistent, and all 72 historical ledger dispositions are retained apart from the release heading.

**Next concrete step:** use the same entire-complement machinery for W-aI at a rigorously chosen positive threshold. Subtract a from both the actual diagonal and every tail lower weight. A positive odd certificate plus an even negative-index bound and a certified even trial quotient could establish parity and simplicity of the actual fixed-window bottom. Do not infer its ordering from a source residual or from LDL pivot magnitudes. After that, test a larger window with a complete error budget and seek a uniform estimate rather than extrapolating isolated successes. G2 ultimately needs lower error tending to zero along an unbounded window sequence, or a quantitatively adequate independent ground-space overlap. Source-to-ground endpoint stability, growing-block estimates and alternative metric/shell sign routes remain open. No RH proof is claimed.


## Previous research checkpoint: September 21, 2026 — v1.15 ordinary operator residual and sharp positive Fourier tail

**Closed: the ordinary source-mass, Rayleigh-value and full operator-residual prerequisites for the actual repaired fixed-order source and its literal polynomial Fourier projection. Improved: a positive entire omitted Fourier complement at lambda=3 already beyond N=256. The signed low-block/G2 gap is not closed; RH remains open.** The complete manuscript is now v1.15, 123 pages, with all 32 main sections, two appendices and 72 historical claim dispositions retained.

### Starting point and work selected

The current saved v1.14 manuscript and persistent log were checked before this continuation. The earlier fixed-window matrix certificate at lambda=3,N=64 does not control the infinite Fourier complement. v1.14's conservative complement bound only became useful at tens of millions of modes. This pass targeted two actual dependencies: a practical positive tail for a signed Schur solve, and the previously separate ordinary Rayleigh/residual assumptions. Three research/review agents participated at the user's explicit request; no positivity or RH assumption was introduced.

### Proved: nonzero ordinary source mass

Lemma 20.27 derives the exact Hermite limit of the unit-angular-normalized, repaired source:

`h_infinity(u)=(4*pi/sqrt(3))*u^2*(2*pi*u^2-3)*exp(-pi*u^2)`.

Its co-Poisson image f_infinity is inversion-even and square integrable in du/u. The actual p_lambda, zero-extended outside the physical window, converges to f_infinity in ordinary L2 at O(lambda^(-1/2)). The uniform fixed-mode approximation is the primary-source input from Connes–Consani–Moscovici, Lemma 7.2. The proof explicitly transfers their suitable normalization to the manuscript's exact unit norm using the squared-norm expansion; a naive L2 triangle estimate would lose the needed rate. The actual source coefficients and the exponentially small zero-value repair are included.

At u>=1 all limiting summands are positive, so the limiting norm is bounded below by the positive square root of integral_1^2 h_infinity(u)^2 du. A quarter of this value is an eventual common lower bound for p_lambda and k_lambda=P_N p_lambda. Here and throughout `N=ceil(lambda^8(1+L))`, `L=2 log lambda`. No effective threshold at lambda=3 is claimed.

### Proved: an absolute full operator residual on the same source

Proposition 20.28 gives, for c=2*pi*lambda^2 and all sufficiently large lambda,

`||W_lambda p_lambda|| + ||W_lambda k_lambda|| + ||W_(lambda,N) k_lambda|| <= C lambda^6 exp(-c/3)`.

This is the actual closed semilocal Weil operator, with the original physical scale, Fourier projection, separate logarithmic diagonal and first-slot-linear convention. It is an unweighted norm of the whole output, not merely fixed-band weak G1 or a numerical residual.

The proof uses v1.14's already-proved endpoint-normalized coefficient tail for every |n|>N. With W=D_d+[M_b,H], the weighted Chebyshev bound gives a commutator norm O(lambda), while the complete diagonal is bounded by C[lambda+1+log(2+|n|/L)]. Consequently the specific source's omitted input e=(I-P_N)p obeys the uniform graph bound

`||W_lambda e|| <= C |B_lambda| lambda^(-2)`.

The output, not the candidate, is then split at an auxiliary `M=ceil(exp(2c/3))`. Existing Proposition g1-sobolev is uniform over all periodic H1 test functions. Taking the dual supremum over unit vectors in E_M yields

`||P_M Wp|| <= C |B| r(lambda)[1+M/L+sqrt(M/L)]`.

There is no extra sqrt(M) from summing individual mode bounds. The complete off-diagonal matrix gives the Hilbert–Schmidt high-low estimate

`||Q_M W P_N|| <= C lambda sqrt(N/M)`.

Since the actual source norm is bounded, this is at most C lambda^5 sqrt(1+L) exp(-c/3). The physical endpoint size |B|<=C lambda^(11/2)exp(-c) and bounded r(lambda) finish the proof. The auxiliary exponentially large M is used only analytically and is not a new finite matrix or source cutoff.

Ordinary unit normalization is now justified by Lemma 20.27. Both the Rayleigh value alpha and the centered residual (W-alpha)u tend to zero at the stated rate. This closes the separate hypotheses in the G2 overlap calibration; it does not establish ground-state overlap. Dividing this upper bound by the exponentially smaller endpoint leaves a growing bound. No endpoint-normalized graph claim, growing-prolate-block operator estimate, or derivative norm estimate for the unbounded output is inferred.

### Proved: the whole omitted Fourier tail is positive at lambda=3,N=256

Proposition 20.21 keeps three previously discarded structures. First, truncated prime shifts have lower bound minus their maximum physical weighted degree, rather than minus twice their total mass. At lambda=3 the full-length m=9 shift is zero and the exact degree is

`M3=sum_(m=2,3,4,5,7,8) Lambda(m)/sqrt(m)=3.171298718...`.

Second, the negative pole is the rank-one sinh(x/2) term. Its Fourier-tail norm costs at most `4 sinh^2(L/4)L/(pi^2 N)` and vanishes in the even sector. Third, the archimedean sine sequence has an explicit uniform approximation to (pi/4)sgn(n), derived from its positive exponential series. The limiting even-sector commutator is the positive Hilbert matrix 1/[2(n+m)], while the whole-space norm loss is pi/2. The phase change between centered and unshifted Fourier bases was checked by both reviewers.

With `R_L=exp(-L/2)/(1-exp(-2L))`, `C_L=max(1,1/4+R_L)` and `t_*=2pi(N+1)/L`, the complete diagonal satisfies

`-A_n >= log(|n|/L)-E_L(|t_n|)`,

`E_L(t)=1/(15t)+7/(2t^2)+pi/(2Lt)+(2+2R_L)/(Lt^2)`.

This uses Binet's exact digamma formula, its recurrence and the convergent trigamma series; no differentiated asymptotic remainder is used. Every finite-L and logarithmic constant remains in the exact diagonal identity. Combining the three pieces yields

`Gamma_even=log((N+1)/L)-M_lambda-2C_L/t_*-E_L(t_*)`,

`Gamma_all=Gamma_even-pi/2-4sinh^2(L/4)L/(pi^2N)`.

The proof extends from finite Fourier sums to the entire omitted form domain using the established core. Independent 256-bit Arb evaluation certifies

`Gamma_all(3,256)>0.0148329`, `Gamma_even(3,256)>1.5867887`, `Gamma_all(3,512)>0.7085077`.

The scalar script and output are retained. No new head matrix was assembled and no full-window positivity was claimed. The older N=64 matrix certificate cannot be combined with this tail while ignoring the intervening modes or coupling.

### Exact signed certificate and what remains

For W=[[F,B*],[B,T]] with T>=Gamma I>0, let Z map the finite head into D(T), R=B-TZ, and K_Z=F-B*Z-Z*B+Z*TZ. The exact identity is retained with a sharper matrix-valued error:

`K=F-B*T^(-1)B=K_Z-R*T^(-1)R >= K_Z-Gamma^(-1)R*R >= K_Z-||R||^2/Gamma I`.

Keeping R*R preserves the directions in which the source residual is tiny; replacing it by its largest eigenvalue can destroy this information. This is an exact finite lower-bound criterion, not a proved sign for the actual K.

The revised overlap calibration now has a quantified remaining assumption. With epsilon_lambda=C lambda^6 exp(-c/3), an independent ground-space overlap kappa satisfying epsilon_lambda/kappa ->0 along unbounded windows would suffice. For example kappa>=exp(-theta*c), theta<1/3, would suffice. No such lower bound is known here. If the actual bottom level is <=-delta, then delta*kappa<=||Wu||; it can therefore coexist with the new near-zero source through exponentially small overlap. The diagonal countermodel diag(-1,epsilon), source (0,1), rejects the false inference from tiny residual to ground-state positivity.

### Adversarial review and discarded work

The adverse agent and an independent second reviewer checked the norm limit, exact Hermite scalar, all lambda and L factors, zero Fourier mode, the crucial dual low-output estimate, graph-tail bound and high-low Hilbert–Schmidt sum. No blocking error was found using the existing v1.14 inputs. The sharp-tail proof was separately checked for Binet constants, physical prime degree, full-length shift, pole scale, first-slot convention and even-sector phase. The scalar interval calculation was rerun independently with the same result.

An alternative first-order Hermite-quasimode route was explored but not completed, because the stronger direct proof made it unnecessary. It is recorded only as an abandoned backup in the adverse report, not as an additional result. A LaTeX escape typo was corrected during review. These are internal checks, not external peer review or a formal proof-assistant verification.

### Integration, validation and next concrete step

The full abstract, status, Section 20 proofs and G2 calibration, Section 32 goals and appendix are consistent. New material is on pages 65–68 and 73–76; the scalar certificate summary is on 118. All 123 pages were rendered and visually reviewed, with close inspection of new proof pages and the final bibliography. The final build has 392 unique labels and no warnings, unresolved references, overfull or underfull boxes. The 72 historical ledger rows are unchanged apart from version headings. The cumulative bundle preserves all prior certificates and adds the current derivations, proof inserts, adverse/independent reviews, scalar script and output, and reproduction guide.

**Next task:** construct a verified inverse-action approximation Z for the lambda=3,|n|<=256 head (even 257 and odd 256 dimensions) and its infinite complement, retaining the full residual Gram R*R. Derive a directional omitted-mode Gram bound from the exact divided-difference entries, using Fourier moment cancellations near the source directions rather than a scalar norm penalty. A finite certificate at one window would still need extension to lower errors tending to zero along unbounded windows for G2. Do not assume a fixed spectral gap, extrapolate finite eigenvalue signs, or omit the corrected sampler graph defect. The alternative arithmetic shell sign at p=2 and the metric/Lyapunov route remain open.


## Previous research checkpoint: September 21, 2026 — v1.14 polynomial endpoint recovery and canonical Weil operator

**Closed: asymptotic physical-endpoint recovery for the exact fixed two-mode source, weak G1 on that same polynomial-cutoff vector, the semilocal Weil operator-core prerequisite, and a sufficiently remote Fourier-tail lower bound. No G2 sign gap is closed; RH remains open.** The full manuscript is v1.14, 119 pages. Its 32 main sections, two appendices and all 72 historical claim dispositions remain. The corrected sampler, first-slot-linear convention, physical endpoint, correct logarithmic diagonal and explicit graph defect are unchanged.

### Starting point and selected obligation

The latest saved v1.13 source and persistent log were checked before choosing this step. That version already certified the exact source at lambda=3,N=64 and proved its relative endpoint mismatch lies between 1.374 and 1.375. Repeating isolated finite certificates would not address the missing uniform endpoint/complement estimates. This pass instead developed analytic estimates, researched primary sources, and explicitly commissioned adversarial and independent endpoint reviews.

### Proved endpoint and weak-G1 results

Let L=2 log lambda and N_lambda=ceil(lambda^8(1+L)). Proposition 21.7 proves

`|delta_N(P_N p_lambda)-B_lambda|/|B_lambda| <= C/lambda`

for all sufficiently large lambda and the exact repaired source of fixed orders 0 and 4. This is the original ordinary Fourier projection, not a newly chosen shell or filter. The constant and threshold are asymptotic, not numerically certified for lambda=3.

The key step uses g(x)=sqrt(lambda) h_circle(lambda x), represented by a finite Fourier measure of bandwidth c=2 pi lambda^2 and total variation O(lambda). The finite arithmetic extension G(v)=sum_(m<=ceil(2lambda^2)) g(mv/lambda^2) has bandwidth O(c) and measure variation O(lambda^3). On v in [1/2,1], its relation to the already controlled exterior co-Poisson tail and the endpoint-normalized radial bound gives ||G||_2 <= C|Bplus|lambda^2. Degree O(c) polynomial approximation, with derivative order up to ceil(c), and Markov/Nikolskii bounds give endpoint jets <=C|Bplus|lambda^3(C lambda^4)^j. Product and logarithmic derivatives have constants uniform in the growing order; no asymptotic remainder is differentiated.

Repeated piecewise integration by parts retains every arithmetic function and derivative jump. The largest integer below lambda^2 is separated before harmonic-sine estimation, giving an O(1/lambda) allowance even arbitrarily close to an integer threshold. The other function jumps cost O(lambda L(1+log lambda)/N); the higher derivative jumps cost O(lambda^7 L/N). With r=ceil(c), the analytic remainder has logarithm bounded above by -6c log(lambda)+O(c+log lambda+log L). The exact smooth compact repair is excluded from high-order differentiation and restored using the Fourier Lebesgue constant and its exponentially small coefficient. Dirichlet–Jordan identifies the actual endpoint with the full Fourier sum.

The same expansion proves the all-tail coefficient bound

`|p_hat_lambda(n)| <= C|B_lambda| lambda sqrt(L)/|n|` for every `|n|>N_lambda`.

The compact repair's direct variation is O(|h_circle(0)|sqrt(lambda)); this is enough for its coefficient contribution. A separate adversarial audit checked insertion of the coefficient bound into the established weighted convolution proof, including the correct logarithmic diagonal. Corollary 21.8 therefore puts weak G1 on the same finite vector uniformly for ambient K>=N in the weighted test norm, with extra error lambda^2[L/N+(L/N)^(R-1)(1+log(2N))], R>3. This is not operator-norm control over a growing family of sources.

### Proved operator and omitted-tail results

Proposition 20.19 writes the actual all-index matrix as W_lambda=D_d+[M_b,H], where H_nm=1/(n-m), H_nn=0, ||H||=pi and H*=-H. The exact b sequence is bounded by (4sinh^2(L/4)+P_lambda+1+pi/4)/pi, with P_lambda=sum_(m<=lambda^2) Lambda(m)/sqrt(m). The sine integral is evaluated by its exponential series; discarding the factor 1-exp(-a_k L) before decreasing integral comparison gives the bound 1+pi/4. The diagonal retains its separate correct formula and satisfies d_n=log|n|+O_lambda(1).

Thus the canonical Weil operator is self-adjoint on the Fourier sequence domain sum log^2(2+|n|)|x_n|^2<infinity, with form domain sum log(2+|n|)|x_n|^2<infinity, compact resolvent and finite-Fourier operator core. Equality with the physical closed Weil form follows from the actual trigonometric form-core result of CCM, Propositions 3.2–3.4, independently checked in the primary source. Every periodic BV source lies in this operator domain, with graph convergence of its Fourier projections at fixed lambda. This does not solve the separate closed arithmetic-generator realization in Section 18 and does not remove the sampler graph defect.

Proposition 20.20 proves, on |n|>N, QW(f,f)>=Gamma_(lambda,N)||f||^2, where

`Gamma=log(2 pi(N+1)a/L)-Ctail`, `a=min(1,L)`,

`Ctail=|A0|+4+pi/2+a+2a/L+2P_lambda+2sinh(L/2)-L`.

A0 is the complete archimedean zero diagonal. The proof uses w(y)>=1/y-1/2-1/L, the explicit archimedean off-diagonal norm, truncated prime shifts of norm at most one, and the exact negative pole eigenvalue -(2sinh(L/2)-L). These signs and scale factors were independently audited. A rigorous 256-bit Arb scalar calculation gives Ctail_3 in (17.69849,17.69851) and Gamma_(3,50000000)>1.0797. No matrix at that dimension was assembled. This illustrates the expensive absolute arithmetic estimate; it does not control the intervening low-frequency modes.

The exact remaining Schur matrix is K=F-B* T^(-1)B, with T>=Gamma I>0. For any inverse-action approximation Z into D(T), R=B-TZ gives the identity

`K=F-B*Z-Z*B+Z*TZ-R*T^(-1)R`.

Replacing the last term by ||R||^2/Gamma gives a rigorous sufficient finite lower bound. Its sign has not been proved for the growing-window arithmetic matrix. Positive F alone is not enough.

### Adversarial work, rejected shortcuts, and research findings

The adverse agent constructed h(x)=x^2(2 pi x^2-3)exp(-pi x^2), Fourier(h)=h, and the strictly positive even co-Poisson function g(y)=exp(y/2)sum h(n exp y). Its Mellin-Fourier transform is xi(s)/(2 pi). Even derivatives form an infinite independent global radical family. Smooth compact cutoffs give arbitrarily large fixed-dimensional blocks with absolute form norm tending to zero. This rules out a fixed positive complement gap after removal of any fixed-rank source family. It does not disprove a unique lowest eigenvector with a shrinking gap, or give a growing-rank rate.

Increasing one prime-power coefficient by any fixed epsilon>0 gives a negative quadratic form on sufficiently large cutoffs of this positive radical function. This is a perturbation countermodel, not a claim about the true prime data. It rejects uniform positivity arguments insensitive to fixed signed arithmetic errors. The one-vector Schur certificate also has an exact high-energy contamination requirement alpha<lambda_1; an arbitrarily small norm error can break it when the low gap collapses. These explorations are kept in adversarial_spectral.md rather than described as progress proving the missing sign.

Endpoint recovery of the source is different from endpoint stability of its ground-state approximation. The latter requires the directional resolvent pairing delta_N(A+tI)^(-1)r relative to delta_Nu. The norm certificate alone loses sqrt((2N+1)/L) and can be inadequate at an exponentially small endpoint. A generic positivity-improving/Perron assumption also does not imply real Fourier zeros; the report gives a positive even Gaussian-mixture countermodel. No conjectural shortcut was imported as a proof.

The primary-source report checks CCM, Connes–van Suijlekom, Suzuki, and recent compact-window computational work. It also proves a conditional fixed-window form-core/Ritz convergence statement and identifies the exact finite real-zero consequence of the existing simple-even ground certificate. None supplies the missing uniform large-window source-to-ground estimate. Those auxiliary conditional results remain in the research report; the stronger explicit operator core and tail argument are integrated into the paper.

### Review, reproduction and complete-manuscript integration

Two independent internal analytic reviews found no blocking error in the endpoint proof after checking growing derivative constants, the exact finite extension, arithmetic threshold resonance, physical normalization, raw/repaired distinction and endpoint convergence. The coefficient/weak-G1 consequence was reviewed separately. The operator/core/tail proof received its own adversarial and source audit. The only mathematical wording correction was to compare a decreasing majorant after dropping the exponential factor. This is internal review, not external referee verification.

The complete abstract, status, Sections 20–21, research goals, certificate scope and appendix now agree. New proofs are on pages 63–65 and 81–84; the scalar scale check is on page 113. The final PDF has 119 pages and 376 unique labels, with no LaTeX warnings, unresolved references, or overflow/underflow messages. All pages were inspected in eight contact sheets; title/new proof/scale-check pages were separately inspected at higher resolution. A title-page spill was corrected by shortening the abstract. Transient incomplete render files were regenerated. The 72-row historical ledger is byte-identical apart from version headings.

The cumulative bundle preserves the previous audit and all scripts/certificates, adding g2_deep_next/ with proof excerpts, derivation, primary-source report, two adversarial/independent audits, the scalar interval checker and its output, and G2_v114_Research_and_Reproduction.md. The earlier finite matrix and source certificates were not unnecessarily rerun. The new endpoint and operator results are analytic; the numerical scalar evaluation is explicitly separate.

### Next concrete step and unresolved obligations

Use the explicit canonical domain and positive far tail to formulate a signed effective low block with a growing near-null source family, then estimate its inverse-action residual without discarding the prime/pole/archimedean cancellation. A practical first test is a certified small multi-source block at an endpoint-adequate cutoff, while keeping a rigorous budget for the omitted modes; positive finite sections alone cannot certify that budget. The target for G2 is a lower error tending to zero along unbounded windows, or an independent normalized source-to-ground theorem with its actual endpoint and strip losses accounted for.

The newly proved source endpoint estimate does not close source-to-ground endpoint stability, the independent shell-sign inequality at p=2, the signed metric/Lyapunov estimate, growing-source-block operator bounds, or the required graph/full-strip transfer. Do not reinstate the withdrawn raw-transfer, critical beta-limit, or unproved meromorphic-transfer claims. **No G2 sign gap was closed.**


## Previous research checkpoint: September 20, 2026 — v1.13 exact-source certificate and proved endpoint mismatch

**Closed: the exact repaired source identification prerequisite at lambda=3,N=64. No uniform G2 sign gap is closed; RH remains open.** The complete manuscript is v1.13, 111 pages, with all 32 main sections, two appendices and 72 historical claim dispositions retained. The corrected sampler, physical endpoint, Fourier cut, correct logarithmic diagonal and explicit graph defect are unchanged.

### Mathematical work and result

Lemma 20.26 supplies an analytic validation method for the actual normalized angular modes, including their infinite Legendre tails and pointwise endpoint values. The canonical self-adjoint operator is J=D+c^2 X^2 on D(D), with D diagonal ell(ell+1) in the normalized Legendre basis; c=18 pi. Bounded self-adjoint perturbation gives compact resolvent. The omitted even block starts at ell=140, hence is bounded below by 19740. Its single boundary link produces a rank-one Schur correction bounded between zero and b_link^2/(19740-x). Equal signed interval LDL inertia counts for both bounding finite matrices certify the exact infinite spectral count.

The two exact rational input vectors have 70 even coordinates. Their approximate eigenvalues xi_0≈55.7952761850 and xi_4≈497.9447748455 are likewise defined by exact decimal strings. At xi±1 the bounding counts are (0,1) for mode zero and (2,3) for mode four. Thus there is exactly one target eigenvalue and every other even eigenvalue is at distance at least one from xi. The residual includes the first omitted component. Bounds are epsilon_0<5.913e-56 and epsilon_4<4.796e-52. The L2 error is at most sqrt(2) epsilon; the graph-norm estimate gives uniform angular errors <2.723e-52 and <2.509e-48. A telescoping Legendre evaluation estimate, with constant at most one, justifies the pointwise and endpoint conclusions. True positive central signs are also certified.

The physical integral coefficients retain every factor of sqrt(lambda). Propagating modal errors through their zero-integral combination gives a raw-source uniform error eta<1.725e-48. For the exact fixed bump, a direct integral inequality gives ||psi||_infinity<=129; it avoids any unproved bump-quadrature accuracy. Because |hat h_circle(0)|<2.611e-39, the exact repaired source differs from the raw finite polynomial uniformly by less than 3.368e-37. Co-Poisson summand counting, inversion contractivity and Bessel's inequality then give a Fourier-projection norm error budget. Exact polynomial Mellin moments are evaluated with interval enclosures, retaining the translation phase and physical factors.

Proposition 20.27 certifies, at lambda=3,N=64, ||v_exact-c_frozen||_2<2.60e-36, with normalized rank-one projector distance below 4e-36. Combining this with the already proved finite Weil certificate by the projector triangle inequality gives sin(angle(exact projected source, Weil ground state))<0.000216. It does not perturb or assume stability of the tiny complement gap; no division by that gap is used in source replacement.

The separate physical-endpoint computation proves 5.58669e-19<B_3<5.58670e-19 and

`1.374 < |delta_64(P_64 p_3)-B_3|/B_3 < 1.375`.

Thus the previously numerical endpoint mismatch is now a computer-assisted result for the exact repaired source. The lower interior trace excludes m=9 and retains m=1,...,8. In the Fourier moment integral m=9 instead contributes a zero-length interval, whose terms cancel exactly. The repair vanishes at the upper physical endpoint. Ordinary ground-state agreement does not establish relative endpoint recovery.

### Certification and adversarial review

`certify_pswf_source.py` uses Python-FLINT 0.9.0 / FLINT 3.6.0 at 768 bits. Strict interval comparisons pass. The input SHA-256 is `ac9dfa8c03f54a326e3ba7af59917ac435e63d41e978310301e6df6e53e83076`. The previous candidate hash remains `6d326cafbe715752f89b90cd92eb1d5a68ab0b78befb6afe074e797372b1a18e`. The script verifies that the imported prior Weil result has this candidate hash, lambda=3,N=64, dimension129 and passing checks; the output records that prior result's hash. The composed angle proof explicitly depends on the prior certified matrix. Both verifiers use Arb and are not independent software verification.

The authorized adversarial reviewer examined the analytic argument, code and saved results and found no blocking error. It specifically required that the separation be measured from xi to the other exact spectrum (satisfied by the xi±1 counts), that the first omitted residual link be included, that the canonical self-adjoint angular domain be stated, and that the previous Weil-certificate dependency be bound to the correct candidate. All requirements are included. The reviewer did not rerun the scripts; this is internal review, not external referee approval.

No failed mathematical attempt is presented as a result. Rather than spend effort certifying the bump integral ratio numerically, a proved coarse bound was used; its error is already much smaller than the needed thresholds. Earlier failed routes and insufficient interval runs remain below. A transient empty PNG during rendering was regenerated successfully and does not affect the PDF or mathematics.

### Remaining obligations and next concrete target

The infinite angular tail certified here is distinct from the omitted Weil Fourier complement. No lower bound for the latter, uniform growing-window complement/residual inequality, endpoint-shell graph pairing or full-strip normalization follows. The next substantive spectral target is a uniform arithmetic estimate for the inverse-weighted residual along a justified growing-window/cutoff sequence, paired with an independent complement bound and relative physical-endpoint budget. Additional isolated positive matrices alone would not establish that target. The source error method is reusable, but no uniform constants or asymptotic conclusion are claimed here.

The alternative independent signed evaluator-shell inequality at p=2 remains open. Weak G1 is unchanged. Do not reinstate the withdrawn raw-transfer, critical beta-limit or meromorphic-transfer claims. Any endpoint shell still brings its full derivative and graph defect.

### Complete-manuscript integration and saved evidence

The abstract, current status, Section 20, Section 32 research goals, certificate appendix and assistance disclosure are updated consistently. Lemma 20.26 and Proposition 20.27 are on pages 71–73; reproduction details are on pages 105–106. The full 111-page PDF compiled without warnings, undefined references or overflow/underflow messages. All pages were inspected in seven contact sheets; title and new proof pages were inspected separately at higher resolution. All 354 labels are unique. The 72-row historical ledger is byte-identical apart from its version headings.

The cumulative bundle preserves all prior files and adds `g2_source_certificate/` with the frozen angular input, optional numerical generator, rigorous verifier, result intervals, polynomial coefficient enclosures and a reproduction guide. Original historical numerical illustrations remain non-certified; the new exact-source and endpoint assertions are explicitly marked computer-assisted.


## Previous research checkpoint: September 20, 2026 — v1.12 finite interval certificate

**One finite certification obligation is closed. G2 and RH remain open.** The complete manuscript is now v1.12, 108 pages. Weak fixed-band/Sobolev G1, the corrected sampler, physical endpoint, Fourier-cut convention, separate logarithmic diagonal and explicit graph defect remain unchanged. All 32 main sections, two appendices and 72 historical claim dispositions are retained.

### Established results and exact scope

Proposition 20.25 incorporates the inverse-weighted finite spectral estimate from the preceding pilot, including its proof and error budget. Proposition A.1 applies it by rigorous interval arithmetic to the actual arithmetic Weil matrix at lambda=3, N=64 (129 dimensions) and a frozen exact rational candidate. Both parity sectors are included. The coefficient strings are interpreted as exact decimal rationals before normalization; their SHA-256 is `6d326cafbe715752f89b90cd92eb1d5a68ab0b78befb6afe074e797372b1a18e`. They define the candidate without an unproved true-PSWF accuracy claim.

Both certificates give A=C-alpha I > 10^(-34) I and q=||A^(-1)r||<0.000216. The Schur energy bound gives 3.64 x 10^(-38)<lambda_0<5.32 x 10^(-38). Thus this finite matrix is positive definite, with a simple even ground state whose angle sine to the specified candidate is below 0.000216. This uses no zeta-zero list and no RH assumption.

### Two verification paths

1. `certify_g2_finite.py`: Python-FLINT 0.9.0 / FLINT 3.6.0, 512 bits. Certified Acb integration after analytic removal of the apparent zero singularity; exact parity sectors; exact-candidate Householder complement enclosed entrywise; 64 positive LDL pivots in each complement sector; enclosed LU solve. Orthogonality refers to the underlying exact matrix, not arbitrary independent elements chosen from its balls. All final inequalities pass as strict interval comparisons.
2. `certify_g2_series.py`: 768 bits, 128 terms. Derived an exact digamma/trigamma formula for the complete archimedean diagonal and sine integral, with explicit geometric tails. At lambda=3 exponential weights are rational 3^(-4k-1). Tail bounds are approximately 3.405e-248 and 2.417e-250. A rational full-space complement Q uses G=Q^T Q, H=Q^T(W-alpha I)Q and b=Q^T Wc. All 128 pivots of H-10^(-34)G are positive; Hz=b gives q^2=z^T Gz/(c^T c) and E=b^T z/(c^T c). All 8,321 parity-block entry enclosures overlap the first path. The two paths share Arb; they are not independent software verification or external refereeing.

The series-path enclosures give q approximately 0.0002158920941115253, E approximately 1.668982121384274e-38, alpha approximately 5.312381700586359e-38, and alpha-E approximately 3.643399579202085e-38. These approximate displays summarize rigorous interval comparisons; the complete balls are saved in JSON.

### Failed attempt and adversarial checks

The first series/complement run at 512 bits and K=80 passed complement positivity and the angle check, but its energy enclosure had width about 2.89e-30, exceeding the 1e-38 target. The strict energy assertion rejected it. Precision was increased to 768 bits and K=128; no threshold was weakened. The insufficient enclosure was not evidence of a negative energy or eigenvalue.

The authorized adversarial review checked the min-max/Schur proof, the analytic archimedean series, both implementations, saved results and final manuscript scope. No blocking issue was found. The final reviewer read the code and outputs but did not rerun the certificates. It required exact Householder geometry, the full parity complement, rigorous rather than approximate solves, a correct Gram matrix in nonorthonormal coordinates, and strict separation between the frozen candidate and the exact source. The manuscript retains the three-dimensional counterexample showing that a failed sufficient complement test need not disprove convergence. The convergent digamma difference is never separated into divergent sums; diagonal tails are enclosed on both sides.

### Remaining obligations and next concrete step

No uniform G2 inequality has been proved. A finite positive matrix is not a positivity theorem for its omitted Fourier complement or all growing windows. The next local task is to certify the exact repaired PSWF source's coefficient/projector error relative to the frozen candidate at lambda=3,N=64, with a separate physical-endpoint error budget. The prior non-certified endpoint errors (about 1.375 at N=64 and 0.1046 at N=4096) remain warnings about Fourier recovery, not certified asymptotics; no N=4096 Weil matrix was assembled. Endpoint-shell insertion still carries all derivative and graph terms. After source certification, a uniform signed-arithmetic bound on the inverse-weighted residual and complement, or an independent evaluator shell sign at p=2, is still required. No raw-transfer, critical beta-limit or pole-aware claim is reinstated.

### Manuscript and reproducibility integration

The abstract, current status, Section 20, research goals, numerical/certification appendix and assistance disclosure are updated together. The full LaTeX/PDF pair compiled with no LaTeX warnings or undefined references; all 108 pages were rendered and inspected in contact sheets, with title/new result pages inspected at higher resolution. There are 343 unique labels. The complete cumulative bundle preserves every earlier file, adds `g2_certificate/` with both runnable certifiers, frozen input, interval outputs and a reproduction guide, and replaces the canonical manuscript, notes, validation and log. The previous pilot remains explicitly non-certified.


## Previous research checkpoint: September 20, 2026 — actual finite Weil spectral pilot; manuscript remains v1.11

Continued the preceding deep-research recommendation using the actual finite Weil matrix and the manuscript's repaired n=0,4 prolate source. The complete v1.11 source and current research log were retrieved before work began. **No G2 arithmetic sign gap was closed. No RH proof or interval-certified finite positivity result is claimed.** The full 105-page manuscript and its PDF remain unchanged; this is an experimental checkpoint in the cumulative reproducibility bundle.

### Exact conditional improvement

For a unit candidate u, write alpha=<Wu,u>, r=P_(u perp)Wu, C=P_(u perp)WP_(u perp)|_(u perp), and A=C-alpha I. If A>=gamma I>0, elementary min–max and the scalar Schur equation prove a unique ground state and

`tan(theta)<=q:=||A^(-1)r||`, `sin(theta)<=q/sqrt(1+q²)`, and `alpha-<A^(-1)r,r> <= lambda_0 <= alpha`.

The proof uses `(C-lambda_0)^(-1)=(A+t)^(-1)` with t=alpha-lambda_0>=0; spectral calculus for the same positive A gives both bounds. An approximate solve z obeys `q<=||z||+||r-Az||/gamma`. For errors delta_A,delta_r and certified gamma_tilde>delta_A, use `||z||+(delta_r+delta_A||z||+||r_tilde-A_tilde z||)/(gamma_tilde-delta_A)`. For fixed exact u and matrix norm error eta, delta_r=eta and delta_A=2eta are valid. Source error remains separate; certify the fixed numerical candidate first, then add the true source's projector-distance error. These are conditional linear-algebra estimates, not independently established arithmetic assumptions or claims of originality.

### Actual computation and what it says

Used L=2 log(lambda), c=2 pi lambda², normalized even Legendre PSWF modes 0 and 4, and source coefficients from the same finite approximation's integrals. The fixed allowed smooth repair has support radius b=3/4: phi=exp(1-1/(1-(v/b)²)), psi=phi(1-Cv²), C=integral(phi)/integral(v²phi). All spectral computations include this repair. The translated Fourier coefficients retain (-1)^n, Haar measure, and the sole sqrt(u) factor in E(h). The physical endpoint uses n<lambda² at integer lambda². The matrix includes prime powers, poles, archimedean subtraction and its separate logarithmic diagonal. Both parity sectors enter the complement minimum.

At N=32, refined calculations give:

| lambda | ordinary residual/gap | inverse-weighted q | computed ground-angle sine |
|---:|---:|---:|---:|
| 2 | 553.598 | 0.00121100321 | 0.00121099977 |
| 2.5 | 4.55575e7 | 0.000514694790 | 0.000514694569 |
| 3 | 1.41142e14 | 0.000217848696 | 0.000217848671 |

At lambda=3,N=64, q≈0.000215892094 and angle sine≈0.000215892075, while the ordinary residual/gap is approximately 4.67624e14. Thus the crude bound loses useful spectral information. The positive computed complement minimum is approximately 1.313e-34; it is not certified. Small cutoffs can give gamma<0 without disproving convergence, as the explicit three-dimensional adversarial counterexample in the report shows.

Double precision was inadequate for the tiny lower spectrum: observed matrix changes under quadrature refinement were about 4.2e-12. Those apparent tiny negative/positive eigenvalues were discarded as sign evidence. N=32 runs at 80 digits/55 even modes/160 quadrature points and 105 digits/70 modes/224 points preserve the reported figures; matrix entries agree at the stored 70-digit precision. Source coefficient differences were approximately 9.17e-65, 1.91e-48 and 1.02e-36; at lambda=3 the endpoint differed relatively by 1.68e-17. Agreement is not an error enclosure. N=64 used 105 digits/70 modes/320 points. Five direct adaptive correlation integrals independently check matrix entries to the exported precision, with discrepancies below 5e-72.

### Independent endpoint experiment

Derived an exact finite-polynomial Mellin formula for the translated source coefficients and checked its phase and factors independently. This avoids oscillatory quadrature for the endpoint-only extension to N=4096. It is exact for a finite Legendre polynomial; the Galerkin approximation and numerical evaluation remain non-certified. The smooth repair was omitted only in this secondary endpoint calculation, with explicit absolute bound `|h_circle(0)|(2N+1)||E psi||_1/L` and `||E psi||_1<=2 sqrt(b) floor(b lambda)(1+C b²)`. At lambda=3 its relative bound is below 4.5e-16 even at N=4096.

For lambda=3, B≈5.58669542e-19. Relative endpoint errors are approximately 1.37454 at N64, 1.63677 at N128, 0.798989 at N512, 0.412764 at N1024, 0.208431 at N2048 and 0.104617 at N4096. No N4096 Weil matrix was assembled. This is a Fourier-cutoff effect, not merely the discarded double-precision noise. Do not infer a proved 1/N asymptotic; interior jumps can contribute oscillatory terms. Small ordinary-norm ground-state error does not imply relative physical-endpoint accuracy.

### Adversarial findings and next concrete step

The authorized adversarial agent checked basis phase, source normalization, strict endpoint trace, the full parity complement, the weighted Schur proof, the polynomial moment formula and the repair bound. It emphasized that gamma<=0 invalidates this sufficient certificate only, not source-to-ground convergence. It also rejected reading a tiny residual or an unconstrained numerical inverse as proof.

Next certify the fixed finite candidate at lambda=3,N=64: obtain interval/operator-norm bounds for matrix assembly, a genuine complement lower bound and an error-controlled solve. Add true-source error separately. Then seek a uniform signed-arithmetic estimate for the inverse-weighted residual on a valid growing window/cutoff sequence. For endpoint efficiency, the existing jump/continuous-derivative decomposition is the appropriate next target; the present observations do not justify deleting its terms. Full Fourier-complement control, continuum domain, endpoint normalization and full-strip convergence remain open. A source approximation theorem without spectral ordering is insufficient.

The centered sampler and its graph defect were not modified or used to claim metric transfer. Endpoint-shell insertion would still require its full derivative and graph terms. The independent p=2 evaluator-shell sign alternative remains open and must pass the preceding nonzero-forcing test. Weak G1 is unchanged.

### Saved deliverables

`G2_Spectral_Pilot_Report.md` gives the full conditional proof, settings, tables, limitations and reproduction instructions. The cumulative bundle contains `g2_spectral_pilot/` with five runnable scripts, JSON outputs and this checkpoint, plus the preceding deep-research artifacts. The canonical research log is updated while preserving all earlier attempts. The LaTeX/PDF pair is not regenerated because these numerical findings do not change a manuscript theorem or close a proof obligation.


## Previous research checkpoint: September 20, 2026 — deep literature and adversarial review; manuscript remains v1.11

User requested deep research before selecting the next G2 proof attempt, explicitly including an adversarial agent trying unconventional assumptions. Read the current full manuscript source and the saved log; examined relevant primary-source theorem statements/proofs and commissioned an independent adversarial derivation. The outcome changes the recommended next test. **No G2 sign gap was closed, and no RH proof is claimed.** Weak G1, finite sampler conventions and the complete v1.11 paper are unchanged.

### Exact obstruction to the previously proposed geometric step

For every off-line parameter w in the open critical strip, not only a zero, the ambient evaluator v_w^R=k_(conjugate w)^R obeys

`S_R v_w^(pR)=v_w^R`, and `S_R D_p v_w^(pR)=p^(1/2-w) v_w^R`.

The latter follows by testing against f in H_R, moving D_p to D_(1/p) in the first slot, and using `M(D_(1/p)f)(conjugate w)=p^(1/2-conjugate w) M f(conjugate w)`. All conjugates agree with first-slot linearity. The same ambient norm and Fredholm estimates used in v1.10 give normalized shell limit `1-p^(1-2 Re w)` without zeta(w)=0. At the ordinary point w=1/4,p=2 this is `1-sqrt(2)<0`. These are genuine ambient evaluators with both support conditions and their Riesz extremal property. Therefore those geometric ingredients alone cannot prove the sign. This is not a counterexample to G2 because zeta(1/4) is nonzero and the vector is not in Q_R.

The arithmetic distinction can be made exact. Source testing plus formal self-adjointness of `D=(t² partial_t)'` gives, distributionally on `(1/R,R)`,

`A v_w^R = c0(w) zeta(w) t^(w-1) + a_(w,R) + b_(w,R)/t`.

Thus in the open strip `v_w^R in Q_R iff zeta(w)=0`. The homogeneous source equation combined with evaluation therefore re-encodes zero incidence. A new inequality is still needed; merely solving the equation is not a sign argument. The counterterm in the definition of A is retained.

### Other adversarial tests and scope

1. Reflected defect diagonals sum to `-(p^d-p^(-d))² ||v_w^R||²`, where `d=Re w-1/2`. Nonnegative finite multi-prime weighting retains the negative sign. This is a statement about sums of diagonals, not superposition cross terms.
2. The two-mode model `B=diag(d+i gamma,-d+i gamma)` preserves the indefinite swap metric J and has commuting prime actions, yet every positive G has relative Lyapunov defect at least `2|d|`. Scalar repair `cI+J` and squaring J do not remove it.
3. A zero-diagonal Hermitian 2x2 matrix with off-diagonal z is at operator-norm distance at least |z| from the positive cone. Positive completion is not arbitrarily cheap.
4. In the finite de Branges model `E(z)=(z+i)^3`, the orthogonal complement of `span{z²+1}` fails norm-preserving Blaschke division. The explicit pair `1-z²+(5i/2)z` and `-z²-(3i/2)z-1` has equal norm squared `41pi/32`, but source pairings zero and -pi. This disproves automatic inheritance of the de Branges structure by an orthogonal quotient, not arithmetic compatibility for the actual co-Poisson source.

### Literature findings

The accompanying `G2_Deep_Research_and_Adversarial_Assessment.md` contains ten pinned primary-source references with scope restrictions: Burnol's evaluator/cosine models; Conrey–Li's published counterexamples to specific shift positivity; Suzuki's canonical-system range; Connes–Consani archimedean positivity; CCM's explicit missing spectral steps; Connes–van Suijlekom's precise core/ground-state theorem; and recent Suzuki, Groskin and Zhu preprints on continuous kernels and certified finite forms. Recent finite certificates were not rerun and are not incorporated as established manuscript inputs. In particular, small-window positivity and conditional/empirical asymptotics are not growing-window G2. The whole-plane limit of an entire function to a meromorphic ratio requires a domain/normalizer audit before using Hurwitz.

### Revised next concrete step

For the actual finite Weil matrix W and a normalized explicit source u, set `alpha=<Wu,u>`, `epsilon=||(W-alpha)u||`, and `gamma=lambda_min(P_(u perp) W P_(u perp)|_(u perp))-alpha`. If gamma>0, min–max and the scalar Schur equation give a unique ground state with eigenvalue in `[alpha-epsilon²/gamma,alpha]` and angle sine at most epsilon/gamma. If W and u have the required exact parity, the ground state is even. This is elementary conditional spectral algebra; gamma positivity and a useful ratio are not proved for the manuscript's source. Weak G1 does not supply this full residual or ordering estimate.

The recommended pilot is to compute and certify this gap-relative ratio from the arithmetic form, retaining the pole and archimedean terms and the correct logarithmic diagonal. Separate archimedean integration, omitted Fourier modes, source error, rounding and inverse conditioning. For exact unit u and `||W-W_tilde||<=eta`, use numerator `epsilon_tilde+eta` and denominator `gamma_tilde-2eta>0`. If the eventual goal is normalized ground-transform convergence on `|Im z|<=T`, the sufficient error is additionally multiplied by `|c_a| sqrt(4a) exp(aT)`. Plain L2 convergence and real-axis spectral agreement are insufficient; endpoint normalization needs its own relative bound.

If this identification route fails, return to the shell target only with a new arithmetic estimate passing the mandatory w=1/4 nonzero-forcing test. Retain the exact centered-sampler graph defect in any finite-core metric alternative.

### Verification and deliverables

`check_g2_adversarial.py` checks the rational polynomial identities and small spectral models; `g2_adversarial_checks.json` records the outputs. It also reproduces Conrey–Li's real xi-ratio at height 282 at 40 and 80 digits as `-0.00013195729337208344071313530228861814`; this is high-precision numerical reproduction, not an interval certificate or new theorem. The gap-collapse model retains angle sine about 0.5257311121 while the absolute residual decreases from 1 to 1e-12. No actual finite Weil matrix was assembled in this research pass. The analytic identities and model obstructions, not the numerical illustrations, justify the strategy correction. No speculative claim was added to the complete manuscript, so no new manuscript/PDF version is issued.

## Previous checkpoint: September 20, 2026 — convergent arithmetic adjoint, manuscript v1.11

Continued the p=2 leading-shell route from the saved v1.10 manuscript and log. The concrete obligation was to justify expanding co-Poisson source orthogonality and its quadratic Gram expressions against arbitrary L2 evaluators. **That convergence prerequisite is now proved with an explicit counterterm. No independent shell sign, G2 closure, or RH proof was obtained.** Weak G1 and the finite sampler are unchanged.

### Established results

**Lemma 9.1: corrected integer cutoff.** For a smooth source supported in `(alpha,b)`, define

`E_M h(x)=sum_(n<=M) h(nx) - x^(-1) integral_0^(Mx) h(t)dt`.

The tail quadrature error is bounded pointwise by `V(h)=integral |h'|` and vanishes for `x>=b/M`. Thus

`||E_M h-E h||_2 <= V(h) sqrt(b/M)`.

This proof does not exchange an infinite sum with an arbitrary L2 pairing. It uses the difference between a right-endpoint Riemann sum and its integral, cell by cell. It also proves E h is square-integrable for a compact smooth source. For a nonzero source with zero integral, the uncorrected cutoff is demonstrably unsafe:

`||sum_(n<=M) h(nx)-E h||_2 = sqrt(M) ||H(t)/t||_2 + O_h(M^(-1/2))`,

where `H(t)=integral_0^t h` is compactly supported and its displayed norm is positive. The direct cutoff therefore diverges in Hilbert norm even for the admissible source class. The integral correction is essential for the particular convergence argument used here; this is not a no-go for other regularizations.

**Proposition 9.2: regularized arithmetic adjoint.** For any L2 vector y,

`A_M y(t)=sum_(n<=M) y(t/n)/n - integral_(t/M)^infinity y(x)/x dx`

converges in local H^-1 to a distribution A y, with

`<E h,y>=<h,A y>`, and `|<h,(A_M-A)y>| <= V(h) sqrt(b/M)||y||_2`.

The finite identity follows by ordinary changes of variables and Fubini; the latter is justified by `integral_(alpha/M)^infinity |y(x)|/x dx <= sqrt(M/alpha)||y||_2`. The variation bound implies H^-1 convergence since `V(h)<=sqrt(b-alpha)||h'||_2`. No pointwise or local L2 convergence for arbitrary y is claimed.

The operator `D phi=x(x phi)''=(x^2 phi')'` is formally self-adjoint. Consequently, for `y in H_R`,

`y in Q_R iff (t^2 (A y)')'=0 on (1/R,R) iff A y=A_y+B_y/t there`,

where the equations are distributional. Both directions are proved, including passage to the closed arithmetic source range. The two constants are not asserted to be zero. The cutoff and limiting adjoints commute exactly with all unitary dilations. Thus the three-range condition is the one equation on the expanded interval `(1/(pR),pR)`, not three newly independent scalar cancellations.

The estimate also has a growing-interval interpretation. Using the derivative norm on H0^1 of the expanded interval, its dual error is at most `sqrt(pR(pR-1/(pR))/M)||y||_2`. For a fixed off-line evaluator normalized by `||v_rho^R||`, v1.10's elementary upper bound makes this `O(R^(1+d)/sqrt(M))`. Choosing the independent co-Poisson cutoff `M=ceil(R^4)` makes the error tend to zero. This is a source-testing norm statement, not a shell-energy bound and not a modification of the manuscript's Fourier cutoff.

**Corollary 9.3: source Gram approximation.** For any fixed finite family h_i, its three channels `D_c E_M h_i`, `c in {1,p,1/p}`, have Gram entries converging to those of the actual source vectors. With `epsilon_i=V(h_i)sqrt(b/M)`, the entry error is bounded by

`epsilon_i ||E h_j|| + epsilon_j ||E h_i|| + epsilon_i epsilon_j`.

This gives a legitimate finite arithmetic quadratic representation. It gives no inverse convergence, closed-range result, or uniform lower singular value. In particular it cannot justify an uncontrolled Schur-complement inversion.

### Sign attempt and its failure

Tested the new local equation against a truncated Mellin power. For `1/2<Re w<1` and `y=x^(w-1)1_(0,B)`, which is genuinely in L2, direct substitution gives on `(0,B)`

`A y(t)=zeta(w)t^(w-1)+B^(w-1)/(1-w)`.

The Euler-summation limit is proved by comparison with integrals, with locally uniform error `O_w(M^(-Re w))`; analytic continuation identifies the limit as zeta. At a hypothetical zero the power term vanishes, leaving an allowed constant. This checks the normalization but merely recovers the zero condition. It is not an independent sign estimate. The raw truncated power is not claimed to satisfy the second Sonine support condition.

Likewise, source-Gram positivity is automatic and does not orient the signed shell difference. The regularized equation adds a rigorously usable constraint, not a positivity theorem. No generic sign on all of Q_R or its entire zero span was assumed; such a target would be stronger than the needed individual-evaluator criterion. No new zero, absence of zeros, or RH result is inferred from the finite computations.

### Verification and primary context

- Rechecked the sign and lower limit of the integral counterterm. It is `minus integral_(t/M)^infinity y/x`, not a cutoff at t or a plus sign.
- The physical cutoff counterterm is `x^(-1) integral_0^(Mx) h`; it is generally nonzero even for a source with zero total integral. Dropping it is exactly what produces the sqrt(M) divergence.
- The adjoint is defined on all L2 vectors only distributionally. Formal pointwise summation is not silently substituted for local H^-1 convergence.
- The source ODE is `(t^2 u')'=0`, with solution span `{1,1/t}`. It is not `u''=0`; both exact source moments are reflected in its kernel.
- Dilation covariance holds already at finite M. The independent integer cutoff M does not replace the physical Fourier cut K, smoothing order, endpoint shell or graph defect later in the paper.
- Consulted [Burnol, Entrelacement de co-Poisson](https://arxiv.org/pdf/math/0407443) and [Burnol, Two complete and minimal systems](https://arxiv.org/pdf/math/0203120v7) for the distributional/co-Poisson conventions. The norm estimate and adjoint passage are proved explicitly here, rather than attributed to an unverified source theorem. No new literature claim of originality is made.

### Reproducibility and integration

`check_copoisson_adjoint.py` uses the toy source `D phi` for `phi=(t-1)^3(2-t)^3` on `[1,2]`. Both source moments vanish by exact rational arithmetic. The source is piecewise smooth, not C-infinity; the variation proof applies, and no arithmetic-core/evaluator status is claimed. Independent physical and adjoint integrals at M=4,8,16,32 agree to below `7e-49` at 45-digit working precision. A genuinely complex `y=exp(-(1+0.4i)x)` checks the first-slot conjugation (discrepancy about `1.21e-48`). The weak pairing error against the explicit exponential-test limit drops from about `3.50e-4` to `9.64e-6`. The nonzero-parameter power check at `w=0.7+1.1i` drops from about 0.0644 to 0.00353 as M goes from 16 to 1024. These are non-certified identity/convergence illustrations, not proof of a uniform bound or RH evidence. The analytic estimates are separate.

The complete v1.11 manuscript has 105 pages; the new arguments are on pages 14–16. The abstract/status, Section 9, Section 32 and the numerical appendix are updated together. All 32 main sections, two appendices and all 72 historical claim dispositions are retained. Complete PDF rendering and visual review are recorded in the validation file. The source, PDF, notes, log, validation and cumulative reproducibility bundle retain their existing identities.

### Next concrete step

Use the explicit local adjoint equation together with both Sonine support conditions and the individual evaluator's Riesz extremal property to derive a *localized quadratic identity* for the two shells. A proposed estimate should be tested on the actual evaluator, not upgraded to positivity on the whole quotient. If finite source Gram systems are used, first establish a quantitative inverse/Schur bound or retain a regularization parameter; entrywise convergence alone does not justify inversion. Keep the counterterm and its normalized growing-interval error in every expansion. The remaining goal is still an independent nonnegative lower bound at p=2, not another recovery of the known prime eigenvalue. **No G2 sign gap was closed; the infinite-source pairing/convergence prerequisite was closed.**

## Previous checkpoint: September 20, 2026 — signed Fredholm shells, manuscript v1.10

Started from the saved v1.9 cumulative bundle and separately saved research log. Followed the proposed Section 8 route: preserve the signed Fredholm cross term, then test its size relative to the nonzero evaluator norm. **The normalized-remainder prerequisite is now proved without Assumption 2.1. The independent arithmetic shell sign is not proved: G2 and RH remain open.** Weak G1 is unchanged.

### New results and assumptions actually used

**Lemma 8.1: signed formula and rank-one resummation.** With `A=(I-F_a^2)^-1`, the exact energy difference is

`<u',Au'>-<u,Au>-<v,Av>+2 Re<u,F_a A v>`.

Here all products are first-slot linear, and `u=P_a q`, `v=P_a F_+q`, `u'=P_a D_(1/p)q`. The positive sign of the cross term belongs to the difference of the two lost energies; the lost energy itself has the negative cross term. Replacing `F_a` by the constant-kernel operator `T_a f=2 integral_0^a f` gives the explicit correction

`C_a=[4 Re(m conjugate(n))+4a(|m'|^2-|m|^2-|n|^2)]/(1-4a^2)`

to the physical outer-shell minus Fourier inner-shell energy. The moments are the integrals of `u,v,u'`; in particular `m'=p^(-1/2) integral_(a/p)^(pa) q`. This is a resummation, not an assertion that the actual cosine kernel is exactly rank one. Its error is at most

`4 pi^2 a^5 H_a / [5(1-2a)^2]`, where `H_a=||u'||^2+||u||^2+||v||^2`.

Proof: `|2 cos(2 pi xt)-2|<=4 pi^2 x^2t^2` gives the Hilbert-Schmidt bound `||F_a-T_a||<=4 pi^2 a^5/5`. A resolvent identity on the two-channel block matrix `[[I,F_a],[F_a,I]]` gives the displayed error. The constant kernel has one nonzero eigenvalue `2a`, so its inverse is explicit. No arithmetic sign assumption is used.

**Proposition 8.2: normalization does not need the unproved sharp evaluator asymptotics.** For each fixed hypothetical off-line root `rho`, set `d=|Re rho-1/2|<1/2`, `q_R=I v_rho^(pR)`, `a=1/R`, and `N_R=||v_rho^R||^2`. Elementary Cauchy-Schwarz on the physical support gives

`||v_rho^R||^2 <= C_rho R^(2d)`.

For `Re rho>1/2` this is the L2 norm of the raw Mellin kernel on `(0,R)`. For the other half-strip, the unitary involution satisfies `M(Gf)(s)=M(f)(1-s)`, supplying the reflected bound with the correct gamma factor. Nested evaluation gives `N_R>=N_R0>0` at a fixed initial cutoff. Therefore `H_a/N_R=O(R^(2d))`, which proves

`|R_a|/N_R=O(R^(2d-5))`, and `|C_a|/N_R=O(R^(2d-1))=o(1)`.

Consequently the normalized *uncorrected* shell difference is

`B_(1/R,p)(q_R)/N_R = 1-p^(1-2 Re rho)+O(R^(2d-1))`.

This conclusion uses the exact arithmetic diagonal identity already in the manuscript; it is not an independent sign estimate. The original unsigned O(a) Fredholm bound also becomes relatively negligible once the same elementary evaluator bound is supplied. The rank-one refinement is useful finite-scale information but is not needed for that qualitative conclusion.

The result removes the evaluator-asymptotic prerequisite only from this shell reduction. It proves neither the matching off-line lower asymptotic nor the critical-line estimates, jet asymptotics, or raw projection-error claims still in Assumption 2.1. Constants depend on the fixed root and initial cutoff; there is no uniformity as the root approaches the critical line or strip edges.

### Attempt at the missing arithmetic sign and outcome

The proposed route initially suggested that the leading signed Fredholm cross term might be decisive. The normalization calculation shows instead that it is asymptotically negligible on every fixed hypothetical off-line evaluator. Controlling that term cannot reverse the leading negative shell imbalance attached to a left-hand zero. This changes the next research target: the shell energies themselves must be constrained by genuinely arithmetic information.

Checked the three source orthogonalities and the one-prime sieve combination from Sections 5 and 10. Testing `y` against the sieved source gives only a linear combination of already vanishing pairings with `W_R` and `D_(1/p)W_R`; it supplies no additional scalar moment cancellation. Generic positivity of their source Gram matrix likewise does not compare the two shell norms. No new signed inequality was obtained from these facts. This is a failed inference, not a counterexample to a possible arithmetic theorem. No finite-dimensional profile was mislabeled as an actual Sonine evaluator.

The precise remaining sufficient target, equation `eq:v110-sign-target`, fixes just `p=2` and asks for an independently proved nonnegative lower limit of

`[integral_(1/R)^(2/R)|I v_rho^(2R)|^2 - integral_(1/(2R))^(1/R)|F_+ I v_rho^(2R)|^2] / ||v_rho^R||^2`

for every hypothetical left-hand zero. The exact diagonal limit would then contradict it, and reflection excludes right-hand zeros. A value evaluator suffices at a multiple zero, so no simple-zero hypothesis or jet coercivity is required for this route. This is a sharply stated remaining RH-strength obligation, not a claim that it is routine.

### Adversarial checks and primary-source verification

- Checked the first-slot-linear conjugation: the signed term is `+4 Re(m conjugate(n))` in the difference, not its negative. The moment `m'` carries `p^(-1/2)`, not `p^(1/2)`.
- Retained every diagonal constant-kernel contribution as well as its exact denominator `1-4a^2`. The residual is measured against `H_a`, not against an unproved uniformly bounded evaluator norm.
- Used the exact cosine kernel `2 cos(2 pi xt)`. The fifth power comes from integrating its squared `x^2 t^2` bound in the Hilbert-Schmidt norm.
- Verified [Burnol, math/0208121, Lemma 2](https://arxiv.org/pdf/math/0208121), the two-channel Fredholm inverse, and [Burnol, math/0203120v7, Section 1, equation (7)](https://arxiv.org/pdf/math/0203120v7), the Mellin cosine multiplier. The latter uses right Mellin transforms; converting to the manuscript's left Mellin convention gives `M(Gf)(s)=M(f)(1-s)`. Neither primary source is cited as supplying the new arithmetic sign.
- The evaluator upper bound uses support and Cauchy-Schwarz only, together with the established Sonine continuation. No evaluator asymptotic was differentiated or assumed. The lower bound uses a single nonzero nested evaluator.
- Preserved all original finite sampler conventions, shell graph terms, Fourier scale and logarithmic Weil diagonal. This separate Sonine calculation does not reinstate raw transfer, critical beta limits, or meromorphic-test transfer.

### Computational and document checks

`check_fredholm_shell.py` uses the actual cosine kernel in Gauss-Legendre Nyström matrices at `a=0.2,0.1,0.05,0.025`, with 48 and 80 nodes and arbitrary normalized complex interval profiles. The exact signed identity differs from the block inverse by at most `4.45e-16`; the constant-kernel closed formula by at most `7.50e-16`. The two quadrature orders' energy differences agree within `2.23e-15`. Every sampled remainder satisfies the stated bound (largest ratio about 0.2491). Reversing one profile reverses the mixed term as expected. These are non-certified convention checks, not Sonine/evaluator data, a proof of the uniform estimate, or RH evidence. The analytic proof is separate.

The new results are integrated into Section 8, the abstract/status, the evaluator-assumption discussion, Section 32 and the numerical appendix. All 32 main sections, two appendices and the 72 historical dispositions remain. The full manuscript is rebuilt and visually reviewed under the scope recorded in `v1_validation.json`; the preceding v1.9 results are retained.

### Next concrete step

Work at `p=2` on the arithmetic constraints for the *leading shell energies*, not on a smaller Fredholm remainder. Derive a convergent quadratic representation of this signed shell functional from the three co-Poisson source ranges (or their cross-scale correlation operators), explicitly retaining the old/enlarged quotient distinction. A proposed representation must yield an independent sign on individual evaluators, not require full-span positivity. First audit any exchange of an infinite co-Poisson sum with a shell pairing; arbitrary L2 membership does not justify termwise absolute summation. If only the existing prime eigenvalue reappears, record that as a tautology rather than progress toward the sign. No G2 sign gap was closed in this run; a technical normalization gap was closed.

## Previous checkpoint: September 20, 2026 — norm-level Weil action and square metric, manuscript v1.9

Started from the saved v1.8 cumulative bundle and independently saved research log. The selected G2 candidate was the genuinely positive arithmetic metric `M_square=S W^2 S`, using the existing full-space source-and-shell projection S and the actual finite Weil matrix W. **A stronger norm-level transfer result is proved, but the independent signed G2 estimate is still missing. No G2 closure or RH proof was obtained.** The candidate exposes a multiplicity-sensitive loss of unscaled coercivity and a nonvanishing relative defect at a hypothetical simple off-line root.

### Proved norm-level results

**Lemma 19.11: local synthesis.** The unconditional unit-interval zero count, including multiplicity, is O(log(2+|j|)). Hence coefficients bounded by epsilon/(1+|Im rho|) synthesize `sum a_rho exp((rho-1/2)y)` in L2(-A,A), with norm at most C epsilon sqrt(A+1) exp(A/2). The proof inserts a smooth nonnegative cutoff equal to one on the interval, integrates its Gram kernel twice by parts, groups ordinates into unit intervals, and applies an l1*l2 convolution bound to block masses b_j. Those masses are O(epsilon log(2+|j|)/(1+|j|)), a square-summable sequence. No zero separation, simple-zero hypothesis or RH is used. The proof gives Cauchy convergence for arbitrary finite exhaustions; it does not claim absolute pointwise convergence.

**Proposition 19.12: actual finite Weil action.** Strengthen the fixed Hardy tail rate to p>1, retaining R>=3 and K>=ceil(exp(2L)L^4). This is available, for example, with sigma=2, a=4 and sufficient M. If T_L translates the original physical vector to [-L/2,L/2] and Pi is the centered Fourier projection, then

`||T_L W S J F - Pi q_F||_2 <= C Delta_(L,K)||F||`,

where `q_F(y)=sum_rho H_F(rho) exp((rho-1/2)y)` is a finite sum for a fixed root family, multiplicities included, and `Delta_(L,K)=sqrt(L+1) exp(L/4) epsilon_(L,K) -> 0`. Its physical-tail part is `sqrt(L+1) exp(-(p-1)L/2)`. The earlier p>1/2 margin alone is insufficient for this bound. At R=3 the Fourier-cut part is O(exp(-3L/2)L^(-3/2)).

The proof applies the synthesis lemma to the full-strip transform error at every zero, then uses the exact finite zero-form pairing to identify W's action after orthogonal projection. The sign is positive in `exp((rho-1/2)y)` because `conj(rho#)-1/2=-(rho-1/2)`. The original physical W, centered phase and endpoint-repaired J are retained. This is a new norm proof, not an inference of operator convergence from form convergence. It concerns these smoothed fixed-family vectors, not the norm of W on the whole expanding space.

The full-space projection result is also explicitly extended to genuine critical-line root chains. Their apparent poles cancel in the holomorphic outputs, and the proper-rational independence proof applies away from isolated zero locations. This is not an extension to meromorphic resolvent tests.

### Audit of the squared-Weil candidate

**Corollary 19.13.** The matrix S W^2 S is globally positive semidefinite and annihilates the exact total graph source. At a zero rho=1/2+mu of multiplicity m, the top-root output has `q_F=C_rho exp(mu y)`, with `C_rho=m kappa(rho) zeta^(m)(rho)/m!`. Its squared-metric mass is asymptotic to `|C_rho|^2 sinh(|Re mu| L)/|Re mu|` off the line, or `|C_rho|^2 L` on it. The omitted Fourier tail of this exponential is O(exp(|Re mu|L/2) sqrt(L/K)), which tends to zero at the actual cutoff.

Every lower jet j<m has zero values at every nontrivial zero, so its squared-metric mass is O(Delta^2)->0. Thus this normalization has no uniform positive lower bound on a full multiple-zero chain. This absolute collapse alone is not a no-go for all rescalings; any rescaling must be judged by the relative criterion.

For a hypothetical simple off-line eigenvector, the squared metric's signed Lyapunov pairing divided by its metric mass is exactly 2 Re(mu), not a vanishing quantity. Its full commutator is retained as `[D,S]W^2S + S([D,W]W+W[D,W])S + SW^2[D,S]`. Positivity and source annihilation do not establish the independent small signed estimate. This candidate does not close G2.

### Primary input and computational check

Verified the unconditional zero-count input in [Trudgian, arXiv:1208.5846v2, Corollary 1 and equation (2.5)](https://arxiv.org/html/1208.5846v2): N(T) equals its Riemann-von Mangoldt main term plus O(log T). Taking endpoint differences gives the unit-interval count needed here. No numerical constants from that paper are needed. An initially retrieved paper on linear relations between zero ordinates was not used as support for this step.

`check_weil_action.py` computes the actual finite arithmetic Weil matrix, including its logarithmic diagonal, and uses the first known critical-line zero at about 14.1347251417. It compares the projected root's matrix action with the finite Fourier projection of `kappa(rho) zeta'(rho) exp((rho-1/2)y)`. Root data use 40-digit arithmetic, followed by double-precision matrices. At K=256 and L=4,6,8,10, relative errors are about 0.057219, 0.014045, 0.0021459 and 0.00068992. It also checks K=128, an individual target coefficient by direct physical quadrature, and the final action with 400 additional quadrature nodes. Numerical values are in `weil_action_checks.json`. The moderate cutoff does not attain the theorem's exponential cutoff. No off-line zero is inserted; no new root/multiplicity certificate, uniform bound or RH evidence is claimed.

### Adversarial checks and failed shortcuts

- An unsigned positive square was a new candidate, not a repeated scalar shift. Its explicit root-action asymptotics expose why positivity alone is insufficient.
- Do not infer the new norm estimate from Proposition 19.9's form limit. The local zero-synthesis lemma and the stronger p>1 margin are necessary parts of the present proof.
- The synthesis series need not be pointwise absolutely convergent. Its local L2 convergence and the absolutely convergent finite-test product series justify the identification.
- Multiplicity is counted both in the local density bound and in C_rho. Top roots and lower jets have different zero-value data, so they cannot share a claimed positive mass asymptotic.
- The centered exponential's Fourier coefficient has a factor (-1)^n; translating back to the original [0,L] basis cancels that factor. The numerical target uses the latter coefficients and checks them independently by quadrature.
- The finite W is self-adjoint and its square is positive, but S does not commute with D or W. All commutator terms stay explicit; the original shell graph defect is killed inside this metric, not declared small.
- No positive lower bound uniform over increasing root families, economical cutoffs, meromorphic-test transfer, or closed Riesz realization follows from these fixed-family results.

### Integration and next concrete target

The complete v1.9 manuscript has 100 pages, 32 main sections, two appendices and the full 72-claim historical ledger. Lemma 19.11, Proposition 19.12 and Corollary 19.13 are on pages 39-41. The abstract, status, Section 28 interface, Section 32 goals and numerical appendix are updated. The validation file records the compiled PDF, visual review scope and hashes.

The norm-action result makes the ordinary action of W on these vectors explicit, but gives no independent small signed G2 budget. A next useful test is a bounded spectral regularization of W, with a precise multiplicity analysis: a function vanishing quadratically at zero cannot restore the lower jets whose W-action tends to zero. A nonzero constant term returns the scalar-metric budget on those jets. Before further metric construction, determine what additional arithmetic operator could distinguish these lower jets while controlling the full commutator independently of assumed roots. Alternatively work directly on the separate Fredholm arithmetic shell-sign criterion. Do not repeat the squared-metric or scalar-shift calculations as new progress.

## Previous checkpoint: September 20, 2026 — full-space metric transfer, manuscript v1.8

Started from the saved v1.7 cumulative bundle and the independently saved research log. The requested task was further work on G2. **A transfer sub-obligation is closed for a new full-space source-and-shell projection. The independent small signed Lyapunov estimate remains open; G2 and RH are not proved.** Weak G1 retains exactly its previous fixed-band/Sobolev scope.

### Established result: one positive projection with both exact annihilation and Weil transfer

**Proposition 19.9.** Retain the actual finite space E_(2K), D, W, corrected sampler J, centered source z=Jc(zeta), physical endpoint and shell c. Let P_sh be the ordinary orthogonal projection onto span{c,Dc}, Q0=I-P_sh, u=Q0 z, and S=Q0-u u*/||u||^2. Symmetric shell support makes c and Dc orthogonal, and u has a nonzero limiting norm. The construction uses source samples and the shell, not a zero list.

Exactly, S z=S c=S Dc=0, hence S annihilates the entire graph defect R=i Dc d-c(d composed with B). Moreover S J F=Q0 Jc(F-alpha_L(F) zeta), where alpha_L(F)=<Q0 Jc F,u>/||u||^2 in the first-slot-linear convention. This retains the two shell terms rather than declaring their diverging graph norm small.

For smoothing exponent R>=3 and tail rate p>1/2, with K>=ceil(exp(2L)L^4), the centered zero-extended transform satisfies

`|H_(SJF)(s)-H_F(s)+alpha_L(F)H_zeta(s)| <= C epsilon_(L,K)||F||/(1+|Im s|)`

uniformly on the full closed critical strip, where

`epsilon_(L,K)=exp(-(p-1/2)L/2)+L exp(L/4)(1+K/L)^(2-R) -> 0`.

The proof bounds the omitted Fourier tail and shell projection in weighted coefficient l1. Their physical value and first derivative bounds give an L1-plus-total-variation estimate, including both physical endpoint atoms. The second contribution is at most C exp(-7L/4)L^-2 when R=3 at the stated cutoffs. This is a proved uniform bound, not a fixed-frequency numerical extrapolation.

The ordinary Gram pullback tends to the positive Schur complement of the whole-line Hardy Gram against zeta; positivity follows from proper-rational independence. The Weil pullback tends to the original global Weil form, because H_zeta vanishes at every nontrivial zero. The product error is bounded by C(epsilon+epsilon^2)/(1+|Im rho|)^2 and sums over all zeros without RH. Thus the expanding-space projection avoids the earlier sharp fixed-band strip obstruction and preserves the nonzero reflected global cross-form when present.

### Remaining failure: a fixed scalar Weil shift still does not provide G2

**Corollary 19.10.** For M=S(W+a0 I)S with fixed a0>0 on a hypothetical nonempty one-sided root space, write A_L=J*SWSJ and G_L=J*SJ. Then A_L->0, G_L->G_infinity>0, and J*M J=A_L+a0 G_L->a0 G_infinity. The Weil piece's finite-core Lyapunov budget A_L B+B*A_L also tends to zero. The remaining limit is a0(G_infinity B+B*G_infinity), whose pairing on Bf=mu f is 2 a0 Re(mu)<G_infinity f,f>, nonzero for an off-line eigenvalue. The relative defect therefore does not vanish.

Restricted coercivity is proved, not global positivity of M. The exact commutator remains `[D,M]=[D,S](W+a0 I)S+S[D,W]S+S(W+a0 I)[D,S]`. In particular Q0 does not commute with D. These are combined pulled-back statements, not separate estimates discarding large shell or arithmetic terms. No small signed G2 estimate was obtained.

### Attempts and adversarial checks

- Considered canceling only the two fixed frequency-edge contributions. The exact second-difference identity controls the resulting remainder only algebraically in L, which does not establish a bounded full-strip estimate in the presence of exp(|Re v|L/2). No general no-go theorem for all edge corrections is asserted. The new construction instead removes the artificial fixed physical band and estimates the tail at the existing expanding cutoff.
- The projection changes the metric, not the original sampler. Its projected output does not claim the original physical endpoint; J still has that endpoint exactly.
- Tail exponent R>=3 is explicit. The weighted first derivative tail needs R>2; the older R>=2 ordinary/form argument alone would not prove this strip estimate.
- The shell derivative norm remains large before projection. Both c and Dc are killed algebraically; c alone would not suffice. The commutator of the shell projection with D is retained.
- The coefficient alpha_L depends on L and K but stays bounded. The product argument uses the fixed enlarged family V+C zeta uniformly; it does not apply a fixed-vector limit to an uncontrolled varying family.
- Source radicality in this new argument follows directly from the holomorphic output H_zeta's zero values and its admissible strip bounds. No new PSWF-domain or meromorphic resolvent assertion is smuggled in.
- The exact first-slot-linear signs, physical 2 pi/L, L^-1/2 basis scale, centered phase and L/2 half-length were retained. The weighted variation cost is exp(L/4), since |Re(s)-1/2|<=1/2 on the interval of half-length L/2.
- Corrected v1.7 wording: other zero summands can cancel a displayed pair; the arithmetic side is an equivalent representation of the whole form, not another term added to the zero sum. Also removed the title-page unproved genericity language about the actual endpoint product.
- The prior PDF's reading conventions spilled onto a nearly empty second page. The shortened abstract/status restores a single title page in the current version; the old clean-layout assertion was too strong.

### Computational checks and integration

`check_full_projection.py` uses Z(v)=(v-mu)^2(v-nu)/((v+2)^8(2-v)), mu=0.23+0.7i, nu=0.37+1.4i, with a length-two model Jordan chain. All root outputs are holomorphic in the full critical strip. Eight exact finite identities have maximum discrepancy below 4.2e-14 at L=8,12,16,24,32. The first-eigenvector relative defect stays 0.46. On a 25-point strip grid the weighted transform error decreases from 0.02043 to 4.121e-6. The model uses tractable K=4L^2 rather than the theorem cutoff; it contains neither zeta zeros nor a Weil matrix and is not a uniform-strip certificate or RH evidence. The order-eight pole requires a strict exponential tail rate; the recorded bound scale uses p=1, not the invalid endpoint rate p=2.

The full v1.8 manuscript contains 98 pages, 32 main sections, two appendices and all 72 historical claim dispositions. Proposition 19.9 and Corollary 19.10 are on pages 37-38; the abstract/status, Section 28 interface, Section 32 goals, numerical appendix and relevant ledger entry are updated. The complete PDF is rebuilt; final rendering and inspection scope are recorded in `v1_validation.json`.

### Next concrete target

Do not repeat the fixed-band edge argument, source-derivative annihilation or scalar-shift repair. The full-space metric now makes the relevant holomorphic Weil products admissible. Seek an arithmetic correction whose **combined** finite-core signed budget cancels the surviving ordinary-metric commutator while retaining a positive lower bound, with every source/shell term included. A useful falsification gate is to compute its limiting pulled-back matrix and B-anticommutator before attempting norm estimates: any correction with vanishing pullback on the one-sided root space cannot cancel the fixed scalar budget. Alternatively continue the independent Fredholm arithmetic shell-sign formulation. Neither a new suitable correction nor the independent signed estimate is established here. Separate growing-block, economical-cutoff, meromorphic-test and Riesz/evaluator obligations retain their previous status.

## Previous checkpoint: September 20, 2026 — reflected-pair edge audit, manuscript v1.7

Started from the saved v1.6 manuscript, cumulative bundle and independent research log. The selected obligation was to determine whether the functional-equation partner cancels the exponential sharp-band edge term before attempting a full prime/pole/archimedean estimate. **It does not cancel it in general. No G2 gap was closed and no RH proof was obtained.**

### New proved result and exact scope

**Proposition 19.8 (reflected-pair edge contribution).** Let `H_L(v)` be the transform of the sharp-band centered polynomial from Lemma 19.6, let `v=d+i gamma` with `d>0`, and set `v#=-conj(v)`. If `a_L=a+O(1/L)` in C2 and the reflected zeros have multiplicity m, their two value-level zero-form summands satisfy

`P_(v,L) = -m exp(dL)/(2L^2) Re(exp(i gamma L) C_a(v) conj(C_a(v#))) + O(exp(dL)/L^3)`.

The proof retains the first-slot-linear conjugation. The two `(-1)^N` edge phases square to one, while `sinh(v# L/2)=-conj(sinh(vL/2))`; the resulting product has a minus sign and the phase `exp(i gamma L)`. If the explicit endpoint product is nonzero, the pair contribution has subsequences of both signs and magnitude comparable to `exp(dL)/L^2`. Thus functional-equation reflection makes the leading edge contribution real and oscillatory; it does not annihilate it.

For the actual source-projected root samples, the coefficient is explicit with `a(t)=Z(t)((it-mu)^-1-alpha_T)`. This run does **not** prove that this product is nonzero for every admissible band; a vanishing factor is an explicitly retained exceptional case. It also does not promote the one-pair asymptotic to the whole zero sum.

### Adversarial checks and rejected inferences

- The proposition concerns exactly one reflected pair of summands. Other zeros can have equal or larger exponential type, so a whole-sum asymptotic needs uniform summability and control of cancellations across all zeros.
- The prime, pole and archimedean representations of the same finite form are not independent quantities to be added to the zero sum. The new pair formula is a diagnostic on the zero-side representation, not a proof that the complete form diverges.
- If either endpoint coefficient vanishes, the displayed leading product vanishes and the O(exp(dL)/L^3) remainder is not assigned a sign or lower bound. No genericity assumption is hidden.
- The result does not contradict finite-matrix well-definedness, ordinary Gram convergence, or weak G1. It shows only that neither bounded ordinary norm nor functional-equation pairing supplies the missing full-strip cancellation.
- The physical frequency scale, centered half-period phase, sharp cut, actual source projection and original corrected sampler are unchanged. The endpoint shell remains outside the band but remains explicit in all formulas where it is not annihilated.

### Reproducibility and integration

Extended `check_band_cut.py` to test the reflected transform product in the same rational model, now through N=256. At N=256 the exact product and its sampled-edge leading expression differ by about 1.47 percent; the real reflected-pair sum is about `1.414e43`. This contains no zeta zero and no Weil matrix. It is a floating-point sign/phase/asymptotic convention check, not evidence for RH or for divergence of the full form.

The complete 96-page v1.7 manuscript adds Proposition 19.8 and its proof on page 36, updates the abstract/status, the Section 28 interface, Section 32 goals, numerical appendix and ledger headings, while preserving 32 main sections, two appendices and all 72 historical claim dispositions. The full PDF is rebuilt and visually checked; final hashes and review scope are recorded in the validation file.

### Next concrete step

The remaining sharp-band obligation is now genuinely global: either prove a uniform entire-zero-sum estimate after subtracting the explicit edge model, or work on the equivalent finite prime/pole/archimedean expression and exhibit its cancellations before seeking positivity. A useful next calculation is to subtract the two frequency-edge modes from the projected vector and determine whether the residual has a summable full-strip product majorant without destroying the fixed-core Schur-complement lower bound. The correction must retain the graph commutator and cannot depend on an inserted zero list. No independent positive-metric compatibility estimate sufficient for RH is currently available.

## Previous checkpoint: September 20, 2026 — sharp-band audit, manuscript v1.6

Started from the saved v1.5 source, notes and reproducibility bundle, and the independently saved research log. The selected obligation was the previous entry's proposed low-frequency compression of the signed Weil form after source projection. **No G2 gap was closed and no RH proof was obtained.** This run proves a new transfer obstruction before that candidate can legitimately use the existing holomorphic sampler theorem. Weak G1 and the original corrected sampler remain unchanged.

### Exact calculation and proved consequence

1. **Lemma 19.6, sharp-band transform.** For `N=floor(T L/(2 pi))`, `t_n=2 pi n/L`, and the centered representative `f_L(y)=L^-1 sum_(|n|<=N) a_L(t_n) exp(i t_n y)` on `[-L/2,L/2]`, the transform at `s=1/2+v` is exactly `-2 sinh(v L/2)/L sum (-1)^n a_L(t_n)/(i t_n-v)`. A telescoping alternating-sum identity retains the two physical-frequency edge values and bounds the remainder by `N (2 pi/L)^2 ||(a_L/(it-v))''||_infinity`. Hence the transform is `-(-1)^N sinh(v L/2)/L [C_a(v)+O(1/L)]` if `a_L=a+O(1/L)` in C2, where `C_a(v)=a(T)/(iT-v)+a(-T)/(-iT-v)`. For a nonzero edge coefficient its magnitude is asymptotic to `|C_a(v)| exp(|Re v| L/2)/(2L)`. Ordinary norm remains bounded. The estimate is uniform on compact sets separated from the imaginary v-axis; it makes no uniform claim as Re(v) tends to zero.
2. **Proposition 19.7, the source projection does not remove this growth.** For a hypothetical off-line first root vector, set `Z(t)=H_zeta(1/2+it)`, `R(t)=1/(it-mu)`. The actual source-projected samples have `a_L(t)=Z(t)(R(t)-alpha_L)`, with alpha_L the sampled |Z|2-weighted mean of R. Its limit alpha_T has O(1/L) Riemann-sum error. Choose a band whose two Z endpoint values are nonzero; the excluded values are discrete. At any fixed b>0, vanishing of both C_a(b) and C_a(-b) would force both a(T) and a(-T) to vanish, hence R(T)=R(-T), impossible for T>0. Thus at least one transform at `s=1/2 +/- b` grows exponentially. Taking b<1/2 places the obstruction strictly inside the critical strip; taking b=1/2 includes the explicit-formula pole points.
3. **Exact compressed-metric budget retained.** For `M=S(W+a0 I)S`, the source and shell still vanish, but `[D,M]=[D,S](W+a0 I)S+S[D,W]S+S(W+a0 I)[D,S]`. None of these three terms is discarded. Positivity or a small signed Lyapunov defect for this new candidate has not been proved.

### Adversarial scope checks and rejected inference

- The ordinary band projection is harmless for the previously proved Gram convergence, not for exponential strip control. The growth is computed on the actual finite centered polynomial, with its zero extension; it is not inferred merely from the infinite band-limited inverse Fourier transform.
- The half-period phase, physical `2 pi/L`, coefficient `L^-1/2` of the actual sampler, and centered physical amplitude `L^-1` are all retained. The endpoint shell is killed only because its support is outside the band. The original corrected sampler and its physical endpoint are not redefined.
- Source orthogonality subtracts one weighted moment; it does not impose the two independent frequency-edge conditions. The two-by-two determinant is `-4 i b T/(T^2+b^2)^2`, nonzero for positive b and T.
- This is **not** a proof that the entire finite Weil form diverges or is negative: prime, pole and archimedean terms may cancel. It also does not by itself disprove a product majorant restricted to the zero set. It blocks importing the existing bounded holomorphic-strip transfer without a new argument.
- No contradiction with weak G1 is inferred. Its fixed-band tests control the residual pairing without requiring the tests to inherit the source output's full-strip bounds.
- A fixed smooth compactly supported frequency taper was not certified as a repair in this run. Improved algebraic edge decay alone would not justify the exponential estimates needed. Moving-band or analytic filters need separate error, positivity and graph analysis.

### Reproducibility and manuscript integration

Executed `check_band_cut.py` on the rational model `Z(t)=(2+it)^-3`, `mu=0.23+0.7i`, with T=3 and N=8,16,32,64,128. This model contains no zeta zeros or Weil matrix. The exact second-difference identity has maximum discrepancy below 2e-15; independent physical quadrature at N=8 differs by less than 1e-14. At N=128, the ordinary squared norm is about 0.0156032, while the transforms at s=1 and s=0 have magnitudes about 1.088e24 and 6.525e23. Results in `band_cut_checks.json` are floating-point convention checks, not certificates or RH evidence.

The complete 94-page v1.6 manuscript adds Lemma 19.6 and Proposition 19.7 with proofs on pages 34–35, updates the abstract/status, Section 28 interface, research goals and numerical appendix, and preserves the 72 historical claim dispositions, 32 main sections and two appendices. The full PDF is regenerated and visually inspected; hashes and review scope are in the validation record. A title-page overflow was removed before final delivery. No obsolete raw-transfer or beta-limit claim is reinstated.

### Next concrete step

Work directly with the complete finite expression for `S(W+a0 I)S`, retaining the edge-induced pole contributions, the signed prime sum and the archimedean term together. The immediate question is whether their combined projected pairing has a finite asymptotic and whether its correction can remain positive relative to the existing Schur-complement metric. Do not use separate pole growth to claim a Weil-form no-go; do not import the old full-strip transfer onto hard-band projections. An alternative is a changing analytic filter with explicit full-strip product errors and the same graph budget. No independent positive-metric compatibility estimate sufficient for RH is currently available.

## Previous checkpoint: September 20, 2026 — complete manuscript v1.5

The complete manuscript is now **92 pages**, preserving 32 main sections, two appendices and all 72 historical claim dispositions. This session continues Section 19, as requested. Weak G1 remains established in the scope of v1.4. **No G2 compatibility estimate or RH proof was obtained.** A foundational dependency was bypassed for a finite-core route, and a concrete positive metric was constructed and its obstruction proved.

### Section 19 results and exact scope

1. **Theorem 19.2: finite-core metric criterion and full transport budget.** Define `B` algebraically on finitely many genuine zero/jet chains and equip that finite space with any fixed positive norm. No closed global operator, graph-core theorem, Riesz projection or quantitative evaluator asymptotic is needed. For a finite sampler `J`, physical self-adjoint `D`, and self-adjoint `S`, set `Y=iDJ-JB`, `G=J*SJ`, and `L=GB+B*G`. The exact first-slot-linear identity is `L=-i J*[D,S]J-J*SY-Y*SJ`. If `G>=c_n I` and `||L||/c_n -> 0`, every eigenvalue has zero real part. Every multiplicity has a genuine first eigenvector, so multiple zeros are covered by the criterion. This is a conditional exclusion theorem, not a construction of the missing small defect. The original Riesz realization is bypassed here, not proved elsewhere.
2. **Proposition 19.3: a source-annihilating positive projection with fixed-core coercivity.** On a fixed physical frequency band `[-T,T]`, let `P` be the band projection, `z_T=P z_centered`, `w=z_T/||z_T||`, and `S=P-w w*`. This is a zero-list-independent orthogonal projection made from samples of `kappa zeta`, not a new finite-prime Weil metric. If the endpoint shell lies above the band, `Sz=0` and `S R=0` exactly: it annihilates both the original zeta source and the whole shell graph defect. Its pullback on every fixed finite root space converges to the Schur complement of the ordinary band Gram form against `zeta`. That form is positive definite because a proper rational root combination cannot equal a nonzero constant on an interval. Thus `J*SJ>=c_(T,V) I` for all sufficiently large cutoffs. Constants may depend on the fixed band and root family.
3. **Proposition 19.4: the surviving rank-two commutator and a new graph source.** Put `m=<Dw,w>` and `h=(D-m)w`. Then `[D,S]=-h w*+w h*` and its norm is `||h||`. The squared norm tends to the strictly positive variance of frequency under the density `|kappa zeta(1/2+it)|^2` on the band. The source-free Lyapunov budget is exactly `-i J*[D,S]J`, which is not made small by positivity or source annihilation. Compressing the generator to the range of S only moves this term: `i(SDS)(SJ)-(SJ)B=-i h <J(.),w>`. The original graph defect is not discarded or confused with the new one.
4. **Proposition 19.5: growing polynomial-source projections lose coercivity.** Suppose a contraction supported in the fixed band kills `D^j z_T` for `0<=j<=2m+1`. For a hypothetical off-line eigenvector with `mu=d+i gamma`, an explicit polynomial geometric-series approximation to `1/(it-mu)` gives `||Q_(m,L) J F_(rho,1)|| <= |d|^-1 r^(m+1) ||z_T||`, where `r=1-d^2/(d^2+(T+|gamma|)^2)<1`. Thus removing increasingly many source derivatives by bounded projections also removes the zero vector one needs to control. This is a proved obstruction to that particular repair, not a no-go for all metrics or changing bands.

### Attempts, failure modes and adversarial checks

- **Successful reduction:** replace the closed-operator/Riesz route by a finite algebraic root-space criterion with its exact common-matrix transport budget. This removes a foundational prerequisite from one possible RH route; it supplies no independent arithmetic estimate.
- **Partly successful metric attempt:** remove the low-frequency zeta source by orthogonal projection and keep the high shell outside the metric's support. Positivity, fixed-core coercivity and exact annihilation of both original source terms are proved. The attempt does not solve G2 because the metric fails to commute with D.
- **Rejected shortcut:** claim that positivity plus `SY=0` implies a small Lyapunov defect. The rank-two commutator survives and has a positive ordinary operator-norm limit. On a hypothetical eigenvector its signed pairing is exactly `2 Re(mu) <Gf,f>`, so that identity alone cannot be used as an independent upper estimate.
- **Rejected follow-on repair:** project away the source and all its first several D-derivatives to reduce the commutator. The explicit polynomial resolvent remainder proves that the coercive lower bound collapses when the number of annihilated derivatives grows at fixed band.
- **Normalization check:** shrinking or rescaling a metric is evaluated through `||L||/c_n`, not the absolute defect. Coercivity and defect scale together. A vanishing unnormalized defect does not create a contradiction.
- **Convention and finite-object checks:** retained the `(-1)^n` centered phase, physical `2 pi/L` scale, coefficient `L^-1/2`, first-slot-linear conjugations, and both shell terms. Every new identity uses the same actual ambient cutoff. The projection does not alter the previously defined sampler or its physical endpoint; it changes only the metric used to test it.
- **No hidden positivity claim:** S is positive on the full finite space and positive definite only after pullback to the fixed root space. It is not a proof of Weil positivity or of a positive transported Weil metric.
- **No global no-go:** the commutator's nonzero ordinary norm does not alone preclude small restricted signed pairings. The obstruction to this source-derivative strategy is separately quantified; other arithmetic metrics remain open.

### Computational checks and integration

Executed `check_section19_metric.py` at `L=8,16,32`, with `T=3`, a rational source, a length-two Jordan chain and an additional model eigenvector. No zeta zeros or Weil matrix are inserted. Nine complex finite identities have discrepancies below `2.1e-15`. The pullback Gram matrices are positive in this model, while the eigenvector-relative Lyapunov defect is exactly 0.46 to floating-point precision, matching `2 Re(mu)`. The polynomial remainder identity is checked separately on a frequency grid. These are convention checks, not interval certificates or proof evidence for RH; results are in `section19_metric_checks.json`.

The full paper incorporates Theorem 19.2 and Propositions 19.3–19.5 on pages 30–33, and updates the abstract, status, Section 28 interface, Section 32 goals, numerical appendix and historical ledger. The stale historical 21.6 reference to an unproved source assumption is corrected to the v1.4 result. The complete LaTeX/PDF pair is rebuilt and visually checked; final hashes and review scope are recorded in `v1_validation.json`.

### Next concrete target

Do not repeat the discarded source-derivative projection strategy. The metric route now requires a genuinely different signed arithmetic estimate for the combined expression `-i J*[D,S]J-J*SY-Y*SJ`, small relative to a retained positive lower bound. A concrete next investigation is a low-frequency compression of the signed prime/archimedean Weil form, with its source-projection cross terms retained, to determine whether it can correct the rank-two commutator without destroying the Schur-complement lower bound. An unsigned norm bound or a positive scalar shift is not enough. The alternative reflected-test endpoint-correction target from v1.4 also remains open. No positive-defect comparison sufficient for RH is currently available.

## Previous checkpoint: September 20, 2026 — complete manuscript v1.4

The complete manuscript is now **88 pages**, with 32 main sections, two appendices and all 72 historical claim dispositions. **The remaining source/domain assumption for weak G1 is discharged.** This closes the fixed-physical-band continuum estimate, its periodic Sobolev-pairing form, and the stated deterministic finite transfer for the explicit repaired source. It does not close growing-block operator-norm G1, the economical near-Slepian cutoff subgate, G2, the fixed-operator/evaluator foundations, or RH. The sampler's explicit graph defect is unchanged.

### Concrete obligation addressed and result

The v1.3 checkpoint left only the global radical/closed-semilocal-domain passage in Assumption 20.1. That assumption has been replaced by **Theorem 20.1, radicality with a nonzero compact-source endpoint**. The proof applies to an even smooth function on `[-b,b]`, zero extended, with `h(0)=0` and `integral_0^b h=0`; its interior endpoint is allowed to be nonzero. It establishes `QW(Eh,v)=0` for every compact zero-extended `H^1` test and the exact truncation identity in the closed semilocal form.

1. **Euler-summation cancellation.** With `beta(t)=1/2-{t}`, the compact Riemann sum obeys `E(h)(u)=h(b-) sqrt(u) beta(b/u)+O_h(u^(3/2))` almost everywhere as `u -> 0`. If `k(x)=E(h)(exp x)` and `K(x)=integral_-infinity^x k(t)dt`, the bounded primitive of the mean-zero sawtooth gives `K(x)=O_h(exp(3x/2))`. The exact central-value repair is essential: a nonzero `h(0)` generally leaves a `sqrt(u)` term whose primitive has no extra decay.
2. **Absolute geometric-side convergence.** For a compact BV test (in particular a zero-extended `H^1` function), integration by parts puts the derivative on the test measure, including both endpoint atoms. Its correlation with `k` decays like `exp(-3|y|/2)` in the unbounded support direction. The growing pole term and prime series are therefore absolutely convergent at each fixed source; the prime majorant is a constant times `sum log(n)/n^2`. The local archimedean numerator is controlled by the already proved square-root translation estimate.
3. **Exact moment-preserving approximation.** Define `h_epsilon(u)=integral phi_epsilon(t) exp(t/2) h(exp(t)u)dt`, with a nonnegative smooth kernel supported in `(epsilon,2 epsilon)` of integral one. This is even compactly supported smooth, retains both exact moments, and intertwines with `k_epsilon(x)=integral phi_epsilon(t) k(x+t)dt`. Translation continuity gives global `L^2` convergence. Its primitive is the same average of `K`, hence has the required tail bound uniformly in epsilon. No uniform estimate on the blowing-up endpoint derivatives of `h_epsilon` is used.
4. **Radical and domain passage.** Start from the classical Schwartz radical identity, first extend the compact test class by ordinary convolution, and then send epsilon to zero. Uniform BV, primitive-tail and local translation bounds justify dominated convergence separately for primes, poles and the archimedean subtraction. Compact BV truncations have Fourier decay `O(1/|xi|)`, which is sufficient for the logarithmic semilocal form norm. The finite prime translations and pole terms are bounded on each fixed support. This proves the exact truncation identity without assuming a globally positive closed form or a meromorphic-test transfer theorem.

The existing uniform source, endpoint, tail, PNT and local estimates now give the proved envelope

`r(lambda)=(1+L)^(3/2) exp(-c1 sqrt(L))+(1+L) exp(-L/2)`, `L=2 log(lambda)`.

The approximation is performed at **fixed lambda before endpoint normalization**. Its constants may depend on that fixed source. No uniformity in lambda is needed to prove an exact identity at each lambda; the separate quantitative tail estimates supply the subsequent uniform rate. Likewise, no uniformity on a growing prolate block follows from this proof.

### Adversarial checks and corrected earlier reasoning

- The v1.3 suggestion that a Schwartz approximation must itself preserve the physical endpoint was unnecessarily restrictive. The approximants here do not preserve it. Endpoint noncancellation and the one-sided endpoint value are proved directly for the original source; they are never inferred by continuity of the endpoint functional in a form norm.
- The proof does not differentiate a concentration asymptotic, discard a boundary strip, assume RH, or exchange a conditionally convergent prime series with a limit. The extra primitive decay is what makes the last exchange legitimate.
- At source arithmetic cuts, endpoint conventions affect point values but not logarithmic integrals or the continuous correlations used in the explicit formula. The original physical endpoint is still interpreted through its interior trace.
- The v1.3 correlation lemma called the interior-test derivative the “absolutely continuous part.” That name was inaccurate: both translated-tail endpoint contributions are themselves locally integrable densities in the derivative of the correlation. The notation is now `bulk`, and the full derivative explicitly includes both contributions. The preceding numerical rates are unchanged.
- The growing-block discussion no longer suggests that a uniform polynomial truncation cost has been proved. It remains a separate obligation with both graph/form and endpoint-normalization requirements.
- No independent external referee review is claimed; this is a fully written working-manuscript proof with internal adversarial checks.

### Primary input and reproducible check

[Connes–Consani, *Spectral triples and zeta-cycles*, arXiv:2106.01715](https://arxiv.org/pdf/2106.01715), Section 3, supplies the Schwartz radical identity. Lemmas 6.1–6.2 supply the BV Riemann-sum and scaling/multiplicative-smoothing background. The present proof explicitly adds the primitive decay and geometric-side dominated-convergence argument needed here. The earlier log's unverified DOI for this paper has been replaced by its verified arXiv link.

Executed `check_bv_radical_passage.py` at 70-digit precision for the compact toy source `h(u)=u^2-(5/3)u^4` on `[-1,1]`. A Faulhaber/Hurwitz-zeta expression for the primitive agrees with the source sum under logarithmic differentiation to maximum absolute discrepancy `3.217312983e-69` at the twelve sampled non-cut points. Scaled primitive values remain bounded in this sample. These are convention checks, not certified asymptotic bounds, a PSWF calculation, or evidence for RH. Results are in `bv_radical_passage_checks.json`.

### Integration, validation and next concrete target

The abstract, status paragraph, Section 20, weighted transfer, centered-sampler application, growing-block discussion, research goals, numerical appendix and affected historical claim dispositions have all been updated together. The complete source compiles with resolved references and no overflow/underflow warnings. Final PDF rendering and inspection are recorded in `v1_validation.json`.

Next, audit the weak-G1-to-G2 interface rather than attempt to prove the discharged source assumption again. A concrete target is the direct reflected-test endpoint correction from v1.1: estimate its additional Weil/graph pairing on the exact common finite object, allowing an auxiliary correction scale smaller than the ambient sampler cutoff. Retain every shell and graph-defect term. In parallel conceptual terms, the stronger G1 target is a uniform estimate on a growing deep block, not another fixed-source domain passage. Neither task is solved by the present theorem.

## Previous checkpoint: September 20, 2026 — complete manuscript v1.3

The complete paper is now **86 pages**, retaining 32 main sections, two appendices and all 72 historical claim dispositions. G1, G2 and RH remain open. This checkpoint removes the remaining tail-correlation, translated-endpoint, inversion-endpoint and local archimedean estimates from the G1 source assumption. The assumption is now only the global radical/closed-form-domain passage.

### Substantive result: the quantitative source estimates now fit together

1. **Corollary 20.9 (tail and endpoint comparison).** The v1.2 endpoint noncancellation makes the already proved modewise co-Poisson tail estimate valid for the actual normalized two-mode combination and its exact value-and-integral repair. Poisson summation at the lower physical endpoint gives its main term as the same endpoint combination with factors `chi_n(c)=1+o(1)`; the `m>=2` radial lattice contributes `O((1+log c)/sqrt(c))` relative error. Therefore the common endpoint of the inversion-even proxy satisfies `B_lambda/B_lambda^+ = 1 + O((1+log c)/sqrt(c))`. If `lambda^2` is an integer, the one-sided cut can delete one source summand, but its size is only `O(B_lambda^+/lambda)` and is absorbed. Thus endpoint comparability is now proved rather than assumed.
2. **Lemma 20.10 (uniform zero-extension correlations).** For a repaired tail `r_lambda` and a zero-extended `H^1` test on an interval of length `L`, differentiating the correlation puts the derivative on the test and uses tail depth `(y-L)_+`. This proves the two-range absolutely continuous derivative bound uniformly. The distributional derivative was written explicitly: its two additional terms are the translated tail multiplied by the two one-sided test traces. Reflection gives the other sign required by the polarized Weil kernel without changing the estimate.
3. **Local archimedean bound.** The exact zero-extension translation inequality is `||tau_x v-v||_2 <= C[x||v'||_2 + sqrt(x)(|v(-L)|+|v(0)|)]`. The endpoint strips give only `O(sqrt(x))`, not the previously asserted first-order vanishing, but division by the archimedean `O(1/x)` kernel is still integrable. This proves the required local term with the full Sobolev/trace factor.

These estimates use the fixed first-slot-linear convention, retain both correlation orientations and retain the endpoint trace terms. No zero list or RH input is used. The existing endpoint-jump/PNT calculation and the conditional continuum G1 implication now depend only on the global domain passage.

### Adversarial domain check and failed shortcut

The standard co-Poisson radical theorem is stated for the even Schwartz class with `h(0)=hat h(0)=0`; see [Connes–Consani, *Spectral triples and zeta-cycles*](https://arxiv.org/pdf/2106.01715) and the summary in [Connes–Consani–Moscovici, arXiv:2310.18423](https://arxiv.org/pdf/2310.18423). The repaired compact prolate source has the two scalar moments but its zero extension has a nonzero one-sided trace at `+-lambda`, so it is not Schwartz. A naive smooth taper is not a solution because it also removes the physical endpoint channel used to normalize G1. Consequently no global radical/form-domain theorem was claimed in this revision. [Historical conclusion superseded by v1.4 above: endpoint preservation by the approximants is not necessary.]

This also identifies the next concrete target: construct an endpoint-preserving decomposition into a Schwartz radical part plus an explicit boundary shell, and prove convergence of the shell in the closed semilocal Weil-form graph norm; alternatively, prove the explicit-formula identity directly for the BV compact source with its endpoint terms retained. Until one of those passages is justified, G1 remains conditional. G2 work and the corrected sampler graph defect are unchanged.

### Validation

The full manuscript compiles without unresolved references, duplicate labels, overflow or underflow warnings. All 86 pages were rendered and visually inspected, with the revised source/domain and correlation pages checked individually. No new numerical experiment was needed: the new step is an exact functional-analytic consequence of the v1.2 tail estimate, plus an explicit endpoint calculation.

## Previous checkpoint: September 20, 2026 — complete manuscript v1.2

The complete paper is now **84 pages**, retaining 32 main sections, two appendices and all 72 historical claim dispositions. This checkpoint supersedes the outstanding source-normalization questions in the v1.1 entry below, which is preserved as history. G1 as a whole, G2, and RH remain open.

### Substantive result: source noncancellation and repair-size bounds

Three results were added in Section 20, pages 33–35:

1. **Lemma 20.4 (endpoint size from exterior energy).** For the real PSWF psi_n,c of L2(-1,1) norm one, n=0 or 4, write theta_n=chi_n^2 for its concentration eigenvalue and b_n=|psi_n,c(1)|. The finite Fourier eigenrelation and Plancherel give the exact exterior identity integral_1^infinity |psi_n,c|^2 = (1-theta_n)/(2 theta_n). The existing radial upper bound is supplemented by a lower bound on the fixed interval [2,3]: Dunster's Bessel expansion becomes a nonvanishing amplitude times cos(c xi - pi/4), whose squared integral has a positive uniform lower bound by one integration by parts. Hence b_n^2 is comparable to c(1-theta_n). Fuchs's fixed-index concentration asymptotic then gives b_n comparable to c^(n/2+3/4) exp(-c), and b_4/b_0 comparable to c^2.
2. **Proposition 20.5 (explicit normalized source).** Set c=2 pi lambda^2 and h_n,lambda(u)=lambda^(-1/2) psi_n,c(u/lambda), with zero extension and interior endpoint traces. Choose a_4=chi_0 h_0,lambda(0), a_0=-chi_4 h_4,lambda(0). The integral vanishes exactly, because integral h_n=chi_n h_n(0). The unit-norm Hermite limit gives finite nonzero coefficient limits. Mode four dominates the endpoint, so B_plus is nonzero for all sufficiently large lambda, |B_plus| is comparable to c^(11/4) exp(-c), and the sum of the individual endpoint magnitudes divided by |B_plus| equals 1+O(c^-2). The exact central value is (chi_0-chi_4)h_0(0)h_4(0), yielding |h_circle(0)|/|B_plus|=O(c^(7/4) exp(-c)), hence O_A(lambda^-A) for every fixed A.
3. **Corollary 20.6 (lower-tail size of the exact repair).** Subtract h_circle(0) times a fixed even bump psi with psi(0)=1 and integral psi=0. Both required scalar constraints become exact and the endpoint is unchanged. Retaining the Poisson zero-value term gives E(psi)(u)=O(sqrt(u)); therefore the correction's lower-tail L2 norm beyond depth S is O_A(|B_plus| lambda^-A exp(-S/2)). This does NOT by itself establish global radical identity or closed-form-domain admissibility.

The two quantitative inequalities formerly assumed at the beginning of Assumption 20.1 have been removed from the assumption and replaced by these proofs. The remaining assumption explicitly retains the global radical/form-domain passage, inversion-even endpoint comparison, uniform polarized correlation estimates and local archimedean estimates. Conditional downstream G1 conclusions remain conditional. No G2 claim was upgraded.

### Inputs checked and adversarial checks

- [Dunster, arXiv:1601.00699v3](https://arxiv.org/pdf/1601.00699v3), equations (3.5)–(3.7), supplies the radial Bessel expansion with envelope-controlled remainder. Version 2 has different equation numbering; the manuscript cites v3. The fixed [2,3] interval keeps the phase derivative bounded away from zero and avoids turning-point issues.
- [Fuchs, J. Math. Anal. Appl. 9 (1964), Theorem 1](https://doi.org/10.1016/0022-247X(64)90017-4) supplies 1-theta_n asymptotic to (4 sqrt(pi) 8^n/n!) c^(n+1/2) exp(-2c). The squared concentration eigenvalue is distinguished from the compressed Fourier eigenvalue chi_n.
- [Connes–Consani–Moscovici, Lemma 7.2](https://arxiv.org/html/2511.22755v1#S7) supplies the fixed-order physical Hermite normalization. Its uniform error also gives convergence of the physical L2 norm to one; unit-norm rescaling therefore preserves the central limits.
- Rejected shortcut: differentiating the leading Fuchs asymptotic without a differentiable remainder would not justify an endpoint asymptotic. The proof instead uses Plancherel and two-sided exterior energy.
- Rejected shortcut: the existing upper exterior-energy bound alone gives only one direction and cannot compare the two modes. The new oscillatory lower bound is essential.
- The source coefficients, finite Fourier scaling, factor two in the exterior half-line energy, powers c^(11/4) and c^(7/4), and the bump's nonzero Poisson zero-value term were checked explicitly. Source normalization is homogeneous; no independently adjusted endpoint fit is used.

### Numerical illustration and validation

Executed `check_prolate_source.py`: an 85-digit, 50-even-Legendre-mode Galerkin calculation at c=10,20,30,40, followed by a 105-digit/65-mode comparison at c=40. The endpoint noncancellation ratio decreases from about 1.00164349 to 1.00006514; the central-value-to-endpoint ratio decreases from about 1.9233e-2 to 3.10538e-14. Increasing dimension and precision preserves the manuscript table's displayed figures. The smallest concentration-loss check is more sensitive and differs at roughly 1e-10 relative precision. These are not interval-certified values or bounds on the infinite-dimensional truncation error. Results are in `prolate_source_checks.json`.

The full source and PDF were updated, all references resolved, and all 84 pages visually checked after rendering. The new proof pages were also inspected individually. The abstract, reduced assumption, downstream source proof, research goals, numerical appendix and historical claim 20.5 disposition were revised together.

### Next concrete target

Prioritize a direct, uniformly normalized derivation of the two-sided tail correlation and its translated endpoint terms, followed by the near-zero archimedean cancellation. Work with the exact normalized source above and the repaired source; keep the test zero extension explicit. A separate domain check is required to justify the global radical identity for the piecewise-supported repaired PSWF source. Endpoint comparability after inversion symmetrization should be verified with one-sided traces at arithmetic cut coincidences, not silently inferred from a pointwise Poisson value. The continuous-remainder subgate remains equation (150), label `eq:g1-continuous-subgate`, in this version.

G2 next steps from v1.1 remain unchanged: a changing test space or direct endpoint correction requires new graph/Weil pairing estimates. Do not reintroduce the disproved bounded endpoint ratio or claim RH from the present source normalization result.

## Previous checkpoint: September 20, 2026 — complete manuscript v1.1

The working paper is **Fixed-Space Prime Compatibility in Burnol's Sonine Quotients**, Alexander Eastwood, version 1.1, 82 pages. It retains 32 main sections, two appendices, and the ledger of all 72 numbered results in the supplied r11 manuscript. The full paper, not a separate research note, is the authoritative deliverable. The PDF and standalone LaTeX source keep their existing filenames so their version history remains continuous.

**Overall status:** No RH proof. G1 still depends on the normalized prolate source and uniform correlation estimates in Assumption 20.1. The corrected sampler has exact endpoint recovery, ordinary Gram convergence, and Weil-form convergence, but its graph defect remains. Version 1.1 proves a further obstruction to one proposed G2 argument.

### Results added in this session

Use the existing conventions: the inner product is linear in its first slot; the inverse Fourier transform has positive exponential; the sampler is centered by the factor (-1)^n. Fix a hypothetical off-line zero rho = 1/2 + mu with 0 < d = Re(mu) < 1/2 and p = 1/2 - conjugate(mu). No off-line zero is asserted to exist. Let J be the corrected sampler on |n| <= 2K, with K >= ceil(exp(2L) L^4), A_rho = iD - mu, and V_L = (A_rho*)^{-1} J. All test spaces in the results below are fixed and finite dimensional, with the paper's holomorphic Hardy outputs and sufficient smoothing.

1. **Lemma 28.5: corrected resolvent endpoint asymptotic.** Uniformly on a bounded input set,
   delta(V_L G) = -H_G(p) exp(-conjugate(mu)L/2)/(1-exp(-conjugate(mu)L)) + O(exp(-nu L/2)) ||G||,
   where nu = min(sigma-1/2, r, 1) > 1/2. This follows from the reflected simple-pole residue, the right Cauchy-pole tail, Fourier truncation, and the exact shell resolvent sum. In particular, exp(conjugate(mu)L/2)(1-exp(-conjugate(mu)L)) delta(V_L G) converges to -H_G(p) in the dual norm of the fixed space.
2. **Lemma 28.6: uniform resolvent Gram bounds.** The ordinary norm of V_L G is uniformly equivalent to the fixed input norm. The proof uses a positive critical-line integral and the norm-small shell correction; it does not use a meromorphic Weil transfer.
3. **Corollary 28.7: the proposed endpoint ratio diverges.** For F_plus = zeta/(s-rho)^m and F_minus = zeta/(s-p)^m, H_plus(p)=0 while H_minus(p) is nonzero. Wherever the denominator is nonzero, |delta(v_minus)/delta(v_plus)| >= c exp((nu-d)L/2). A zero denominator makes the old formula undefined. The resulting two-vector endpoint-annihilating test is unbounded in ordinary norm.
4. **Theorem 28.8: bounded tests from a fixed input space lose the reflected signal.** If v_L = V_L G_L is bounded and delta(v_L)=0, uniform Gram bounds make G_L bounded; the endpoint asymptotic forces H_G_L(p) -> 0. Holomorphic form transfer then gives <W J F_plus, A_rho* v_L> -> 0. This applies to normalized versions of the old divergent test as well. It does not exclude changing input spaces, other endpoint corrections, or other ways of retaining the boundary channel.

The key shell calculation is
delta((A_rho*)^{-1} c_LK) = -(conjugate(mu)/K) sum_{n=K+1}^{2K} 1/(t_n^2 + conjugate(mu)^2) = O(L^2/K^2).
The cancellation between positive and negative Fourier indices must be retained.

### What was checked

- Rechecked the contour orientation, reflected pole, Fourier phase, Cauchy-tail coefficient, first-slot-linear conjugations, and common-cutoff errors in the proof.
- Executed `check_resolvent_endpoints.py`, an explicit rational-transform model with sigma=2, a=4, M=6, mu=0.2+1.3i. It inserts no zeta zeros and computes no Weil form. At L=14 the reflected residue scaling has relative error about 1.87e-5; the endpoint ratio magnitude is about 24,924. This is a floating-point convention check, not proof evidence about RH.
- Compiled the full LaTeX manuscript with resolved references and no duplicate labels or overflow/underflow warnings. Visually inspected all 82 rendered pages, with the new proof pages examined individually.
- Integrated the results into the abstract, Section 28, the continuum-ratio discussion in Section 30, the goals in Section 32, Appendix A, and the historical claim dispositions in Appendix B. G1 claims were not upgraded.

### Next concrete research targets

**G2:** Study a direct endpoint correction of the reflected resolvent test, or a changing input space, with a precise uniformity budget. The direct finite correction w_L = v_minus - delta(v_minus)c_LK has zero endpoint and bounded ordinary norm. Its cross pairing contains the additional exact term
-conjugate(delta(v_minus)) <W J F_plus, A_rho* c_LK>.
At the large sampler shell cutoff, the graph-correction norm is comparable to exp(-dL/2) sqrt(K/L) and diverges. A smaller auxiliary correction inside the same ambient finite space may reduce that derivative cost, but its Weil pairing must be estimated independently. Do not discard this term because the correction is small in ordinary norm. Do not revive the disproved bounded ratio, or apply fixed-space uniform convergence to a growing test family without new estimates.

**G1:** Prove the actual normalized two-mode source's endpoint noncancellation and uniform correlation estimates in Assumption 20.1, including exact-moment repair and domain requirements. The existing radial estimates and finite transfer implications do not alone prove that assumption. A separate concrete target is the continuous-remainder bound in equation (142), which would supply the stated near-Slepian cutoff scale under the source hypothesis.

**Fixed-space route:** The quantitative evaluator inputs in Assumption 2.1 and the closed-operator realization in Assumption 18.1 remain separate obligations. A local sampler or endpoint result does not discharge them.

### Instructions for subsequent research sessions

Continue from the latest full manuscript and this log. Keep a clear distinction between exact identities, proved implications with explicit hypotheses, failed attempts, numerical illustrations, and open inputs. Integrate substantive results throughout the full manuscript, compile and inspect the PDF, and update the existing deliverables and this log. Preserve the same finite D, W, endpoint, cutoff, and first-slot-linear convention in every comparison. Do not infer a norm bound from form convergence. Do not claim RH, positivity transfer, or publication readiness without the complete missing arguments. The user has authorized continued research and hourly attempts, but not publication or messages to other people.
