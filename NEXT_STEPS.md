# Next steps — shared task board

One line per task. **Claim a task by writing your name in `owner` before you
start, in its own small commit**, so the other agent does not duplicate it.
Update `status` in the same commit as the work. Keep done items; record the
version that did them. Nothing here is a claim about G2 or RH.

Status vocabulary: `open` · `claimed` · `in-progress` · `done (vN.NN)` ·
`closed — no angle` · `blocked (reason)`.

| ID | task | owner | status | done when |
|---|---|---|---|---|
| NS-1 | Recover the two OPEN evidence groups: v1.28 λ=5 disproof (`g2_lambda5_transfer`, `g2_block_metric`); v1.31–v1.34 concentration/closures (`g2_weighted_concentration`, `g2_schatten_no_go`, `g2_nested_commutator`, `g2_primitive_transport`) → `evidence/v128/`, `evidence/v131..134/` + manifests | Codex (Astra) | disclosure completed by NS-38; original recovery OPEN | Post-v1.43 search refreshed remote refs and release assets and checked local source locations and saved records; no missing originals recovered. The recorded source is fixed_space_prime_action_v1_34_bundle.zip, library version 37 (207224098 bytes); no library connector is available and the accessible web session is signed out. Need an accessible original archive or the six original directories with dependencies and provenance. See evidence/MISSING.md and evidence/v131/recovery_provenance.json; report-only recovery is insufficient. |
| NS-2 | Semantic lock: reproduce one CCM §6 numerical value (arXiv:2511.22755) from `assembly_general.py`; report value, precision, any normalization discrepancy (a discrepancy is the better outcome) | Claude (diagnostic); Codex (interval certificate) | done (v1.41) | Broader CCM section 6 reproduction retained in evidence/diag_ns2_semantic_lock/: 170 midpoint diagnostic values at two precisions. Eight lambda=3, N=120 local root discrepancies additionally certified in evidence/v141/ at 768/1024 bits, with exact centering dictionary; first discrepancy 1.582329697193127e-34. Common positive scale and identity shift are invisible to the zero comparison; no complete-ground transfer. |
| NS-3 | Manuscript positioning: cite Zhu (2608.24827) and Groskin (2607.02828); add the `a = log λ` translation table beside the λ=4 result; cite Zhu at `prop:v125-cutoff-cost` as the same doubly-exponential family; add the CCM `μ_λ` paragraph from `COMPARISON.md` | Claude (drafts); Codex (integration) | done (v1.41) | Zhu/Groskin citations, a=log(lambda) translation table beside lambda=4, scoped cutoff-cost comparison and CCM infimum paragraph integrated. Drafts retained; NS-6 remains separately drafted. |
| NS-4 | Meta-obstruction for arithmetic-blind estimates | Astra | done (v1.39) | Two scoped theorems (`thm:v139-probe-relaxation`, `thm:v139-protected-orbit`); blanket "all ten closures" claim refuted by explicit positive counterexample |
| NS-4b | Coverage table: which of the ten closures each v1.39 theorem covers, which it does not, and why; check the live concentration mechanism is outside both theorems' classes | Claude (analysis); Codex (reconciliation) | done (analysis; retained v1.41) | Detailed ten-route coverage table in evidence/diag_ns4b_coverage/ retained alongside evidence/v139/adversarial_review.md sections 6-7. Probe-relaxation covers 1 of 10; protected-orbit covers 0 of 10 as recorded; concentration lies outside both. Manuscript links both analyses; table insert remains a draft. |
| NS-5 | Certify simple-even ground of the **complete** `W_4` (CCM Thm 5.10 / CvS Thm 6.1 hypothesis) with the `prop:v117` machinery; numerically the gap is 8 orders (`evidence/diag_circle_split/`) | Astra | done (v1.40) | `prop:v140-ground4`, `cor:v140-real-zeros`: 1024/1280-bit complete shifted inertia; 0<mu0<2.454e-75, mu1>1e-73; complete ground transform has only real zeros |
| NS-6 | Krein–Langer / truncated-moment framing of the wall (in `COMPARISON.md` addendum) → integrate into the goals section | Claude (draft); Codex (integration) | done (v1.42; qualified continuation/identification framing); source draft: `evidence/drafts/v141_inserts/determinacy_insert.tex` (anchor: after the paragraph following `prop:v121-cofinal-rh`; cites `Suzuki2026` (present), `KreinLanger2014`, `BasorEhrhardt2002` (both in `bib_inserts.tex`, references verified via Crossref)) | one paragraph in the manuscript, cited |
| NS-7 | Toeplitz-plus-Hankel asymptotics for the certified small eigenvalues | Claude; Codex (NS-36 reconciliation) | done (finite diagnostics only; asymptotic route open) | The KMS/line-symbol claim is retracted. Correct-symbol finite compressions show cancellation in a deep block, with cutoff dependence and distinct parity counts. Literal Toeplitz-plus-Hankel structure and an applicable asymptotic theorem remain unproved. See evidence/diag_ns36_corrections/circle-lane-current-reading-2026-09-22-v1.html. |
| NS-8 | Nyman–Beurling–Báez-Duarte assessment + `d_N` table | Claude | closed — no angle | `evidence/diag_routes/nb/`; d_N certified to N=600; no finite equivalent; Burnol Thm 3.1 recorded as semantic lock |
| NS-9 | Li / Keiper assessment + `λ_n` table + support analysis | Claude | closed — no angle | `evidence/diag_routes/li/`; Li class ∩ PW_a = {0}; corollary W_4≥0 ⇒ λ_n^{[log 16]} ≥ 0 |
| NS-10 | de Bruijn–Newman assessment + one Polymath15 reproduction | Claude | closed — no angle | `evidence/diag_routes/dbn/`: no bridge in either direction; barrier verification reproduced from scratch; arXiv id is 1904.12438 |
| NS-11 | de Branges / Hermite–Biehler route | Claude | closed — no angle | dictionary recorded in `COMPARISON.md`; no positivity mechanism (Suzuki 2606.09096, Conrey–Li) |
| NS-12 | Function-field / Hodge / F_1 route | Claude | closed — no angle | nothing finite transfers; the operator side gave NS-5 |
| NS-14 | CCM step (b) at finite λ: compute the real zeros of `ξ̂_3` and `ξ̂_4` from the certified ground vectors (NS-5 makes them provably real) and compare with γ_1, γ_2, … = 14.13, 21.02, 25.01, …; also the zero spacing vs λ | Claude; Codex (centering correction) | closed — corrected finite-compression diagnostic | The sinc-lattice conclusion is withdrawn. zeros.py omits the (-1)^n centering phase; see evidence/diag_ns14_zeros/results-v2.md. Broader CCM diagnostic and eight certified N=120 local root checks are retained. Original N=256 files are preserved. Complete-ground zero enumeration and cofinal Xi convergence remain open; v1.42 separately encloses one complete lambda=4 zero within 0.1 of gamma_1. |
| NS-17 | Reconcile remaining NS-3/NS-6 drafts (`evidence/drafts/v141_inserts/`) with the live tex: retain the v1.41 window table, Zhu/Groskin citations and CCM paragraph already integrated; assess the unintegrated determinacy paragraph and its Krein–Langer / Basor–Ehrhardt references; collapse duplicate `Zhu2026` / `Zhu2026Windows` bibitems | Codex (Astra) | done (v1.42) | Five inserts at the requested anchors; single Zhu2026 bibitem. Continuation/determinacy and Toeplitz-Hankel claims qualified to avoid unsupported implications; diagnostics labelled. Build and PR recorded in the v1.42 report. |
| NS-13 | Standing rule: do **not** compute λ = 10, 12 windows or floors past λ=8 | — | rule | `prop:v121-cofinal-rh`, `prop:v138-shifted-floor` |
| NS-15 | Review current evidence, dependencies and active work; recommend the next NS to tackle | Codex | done (v1.40 review; no new result) | Recommend NS-2 next: reproduce CCM section 6 at lambda=sqrt(12), N=120, with the exact normalization dictionary, two-precision replay and a discrepancy statement. NS-14 is already in progress; NS-4b's table and concentration exclusion already exist in v139/adversarial_review.md sections 6–7. Follow with NS-3/6, correcting the stale comparison; retain NS-1 as blocked. The next analytic target remains a uniform finite signed-concentration floor in both parities, with all couplings controlled. |
| NS-16 | Integrate the saved v1.41 candidate with current main, preserve later diagnostics and retractions, rebuild and verify manifests, then publish the authorized merge | Codex (Astra) | done (v1.41) | Saved candidate integrated with current main; later diagnostics and retractions retained byte-for-byte; manuscript builds to 215 pages with 0 undefined/duplicate references; current evidence manifest verifies. Main and v1.41 publication authorized by the user. NS-1 stays OPEN; no new windows or G2/RH claim. |
| NS-18 | Test complete-ground Fourier-zero transfer at existing lambda=4: budget spectral separation and full residual/tail errors near the first zeta ordinate; certify a unique local zero if the bounds permit, otherwise identify the precise limiting bound | Codex (Astra) | done (v1.42); signed follow-up replaced by NS-19 | Complete unique local zero within 0.1 of gamma_1 certified at 1024/1280 bits in v1.42. User ended the sign/factor-ten pursuit; NS-19 records the stronger first-zero enclosure and precise resolution gap without claiming the signed target. |
| NS-19 | Quantify the archived resolution of the complete lambda=4 first-zero enclosure and the missing lower-energy input | Codex (Astra) | done (v1.43) | Complete first positive zero lies in gamma_1 +/- 8.752082e-33 at 1024/1280 bits. Limiting direct budget is C_ell*rho, not sqrt(rho/b). A lower-energy transfer at 1e-71 needs rho-l <= 3.2032006e-153 (safe sufficient 3.2031e-153; relative 1.3055e-78); absent, and a suitably centered trial would still be required. Explicit propositions scope the resolution floor to the displayed archived estimates. Failure of the bounds, not of the object; no complete sign, cofinal, G2 or RH claim. |
| NS-20 | Arithmetic decomposition of the first three pencil surpluses at lambda=3,4,6 | Claude (diagnostic); Codex (NS-36 reconciliation) | done (diagnostic; conclusions corrected by NS-31/36) | The total decomposition is algebraically explicit; numerical evaluation uses midpoints. The psi(1/4) assembly folds a Lorentzian into its continuum piece and must be converted to the shifted-symbol split. Small primes dominate the O(1) budget but do not determine the tiny surplus: the lambda=3 m=8 term is 1.66e-25 against q=4.242e-38. Corrected level-column values and precision limitations are in the NS-36 current reading; no sign mechanism follows. |
| NS-21 | Lobe-mass / pencil-surplus comparisons in the six deepest finite-head directions | Claude (diagnostic); Codex (NS-36 reconciliation) | done (diagnostic; blanket closure withdrawn) | The displayed samples demand constants as large as about 1e98 (and about 1e104 for an any-lobe variant). These are large finite ratios, not a proof that no finite uniform constant exists. The claimed counterexample to every variant is withdrawn. No asymptotic relation or failure of the physical form is established. |
| NS-22 | Comb-following minorant losses on the existing even heads | Claude (diagnostic); Codex (NS-36 reconciliation) | done (diagnostic; obstruction claim withdrawn) | Restricted-family optimizations do not lower-bound the loss of all minorants. The sampled tail charge is not global (beta_8(130060.425)=-8.812 below -8.050); D2 used the wrong monotonicity; D3 used different matrix/validation quantizers. The corrected D2 model gives lambda=4 eta about 3.157 instead of 3.332, still without a valid global tail. No necessary cofinal level growth follows. |
| NS-23 | Adversarial audit of v1.43: prop:v143-first-zero-bound, prop:v143-resolution, prop:v143-fixed-window-meaning and lem:v143-evaluator-dual; check every hypothesis is stated, every constant traces to an archived enclosure, the sign conventions, and that no sentence overstates | Claude (sub-agent) | done (audit merged 2026-09-21) | `audits/2026-09-21-v1.43.md`: no MAJOR; MINOR M1 (statement should say which hypotheses are inherited at 320/768/896 bits), M2 (pair the 'lower bound alone does not reduce the direct bound' sentence with the frozen-trial floor 6.65e-38), M3 (NS-19 row rounding, fixed here); all replays byte-identical |

| NS-24 | Translate eq:v131-weighted-concentration to the q/q+ pencil class and distinguish fixed-window demands from cofinal control | Codex (Astra) | done (v1.44) | prop:v144-pencil-concentration: minorant loss L[v_k]/q+[v_k] <= nu_k + eta_a norm(v_k)^2/q+[v_k] for source-admissible directions; mixtures require diag(nu)-R+eta G >= 0 on ker b. The diagnostic raw head is not source-compressed. The local test is finite-window; the full criterion remains cofinal, with uniformly bounded errors already sufficient under v1.36 hypotheses. Diagnostic thresholds not certified. No new run, window, tail metric or G2/RH claim; stopped at this finding. |

| NS-25 | Resolve audit v1.43 MINOR M1/M2 only in v1.45: state inherited precision levels and pair the lower-bound limitation with the frozen-trial floor | Codex (Astra) | done (v1.45) | Minimal statement/wording corrections in tex, COMPARISON and both logs; actual build and reference counts; no new numerical claim. |
| NS-26 | Derive the exact explicit-formula identity for beta_a and its lattice samples; resolve cutoff and correction terms, and check the ten saved u samples without RH | Codex (Astra) | done (v1.46) | Exact unconditional Perron identity with strict endpoint; varying lattice envelopes, not an exact comb; forty low samples plus fourteen deep-trough/centroid locations reproduced to better than 1e-6; explicit Gaussian/desmoothing convention and sufficient zero counts recorded. No new window or bound. |

| NS-27 | Prove or delimit the fixed-window even-sector obstruction for step minorants with bounded level complexity, after NS-26 | Codex (Astra) | done (v1.46: scoped bounds and precise gap) | Packet loss includes positive spill/original energy; explicit concentration and source projection. Conditional eta >= c D/(2K)-Q needs a uniform arithmetic level distribution and bounded-energy packet, absent from v1.37/NS-22. J-trough floors satisfy eta >= d_(J+1), but cofinal multiplicity is unproved. Route remains blocked, not closed; G2/RH open. |
| NS-28 | Twenty-bin uniform and level-measure-weighted feasibility / energy diagnostics | Claude (diagnostic); Codex (NS-36 reconciliation) | done (diagnostic; primal and asymptotic conclusions corrected) | Dual values are lower estimates; upper estimates require an independently feasible witness. Several original pure vectors fail constraints. The blanket c=0.5 infeasibility claim is false: mixed witnesses attain c=0.529336 at lambda=4 and c=0.537511 at lambda=8. A repaired lambda=3 weighted witness is source-projected at diagnostic level (Q about 2.43e-9). Finite-bin feasibility is not the all-Borel hypothesis, and four windows establish no cofinal bounded Q, monotonicity, or level-count threshold. See the NS-36 current reading and its separately scoped lambda=4 replay. |

| NS-29 | Separate arithmetic level-set measure from bounded-energy packet spread in eq:v146-level-density; reduce the measure input to the exact zero expansion and assess unconditional zero theorems and v1.37 depth growth | Codex (Astra) | done (v1.47: named open inputs and scoped reduction) | prop:v147-level-separation separates band increments from packet coverage; ass:v147-zld is the exact corrected-zero value-distribution input. Depth growth gives only window-dependent widths; broad pulses have energy log X + O(1). Both uniform arithmetic distribution and bounded-energy packet coverage remain open; no reduction from standard zero theorems/conjectures established, no logical-independence claim. Route blocked, G2/RH open; actual build 237 pages, 0 undefined/duplicate references. |


| NS-32 | Review PR #14 / prop:v148-weighted-levels: proof, bounded-density hypothesis, constants, source projection and claim sweep; merge/tag only if no MAJOR findings | Codex (Astra) | done (revised PR #14 held: 3 MAJOR findings) | audits/2026-09-21-v1.48-pr14-v3.html reviews f3611ef: invalid K rearrangements; lambda=4 returned state fails bin feasibility (0.636<1); aligned-bin maximum is not the full concentration function. Original biconditional/density issues acknowledged in revision; exact weighted-cost implication and uniform constant pass. Revised head builds to 239 pages, 0 undefined/duplicate; no merge/tag. Projection check named, not run. |
| NS-33 | Assess the weighted quantization scalar as an exact corrected-zero statement; identify the right cofinal input in v1.49 after NS-32 | Codex (Astra) | done (v1.49: wrong peak bound; exact-cost input open) | prop:v149-critical-density proves an unbounded continuous peak at negative critical values; prop:v149-weighted-cost retains the exact QC_K implication. QC_1 growth does not suffice (full-support countermodel); ass:v149-qg names fixed-K exact-cost growth plus separate admissible bounded-energy WLH. No cofinal input proved, no new computation; 242-page build, 0 undefined/duplicate. G2/RH open. |
| NS-30 | v1.48 candidate (PR #14, Claude): level-measure-weighted form of the level-count bound | Claude | withdrawn — PR #14 closed unmerged after audit NS-32 (three MAJOR: K rearrangements, infeasible lambda=4 state at c'=1, aligned-bin maximum used as M(h)); the valid part is prop:v149-weighted-cost | never merged; version number retired |
| NS-31 | Adversarial review of Claude's circle/symbol diagnostics, object identity, pencil precision, source normalization, concentration scope, constrained dual feasibility, projection, retractions and map claims through NS-30 | Codex (Astra) | done (audit 2026-09-22 v2; v1.49 integration base) | Nine MAJOR and six MINOR findings, with independent quadrature, all dual constraint slacks, source projection repair and 120/180-digit replay. Report: audits/circle-symbol-lane-2026-09-22-v2.html; diagnostics: evidence/diag_ns31_audit/. c=0.5 feasible at lambda=4,8; charged tails invalid; symbol and deep-block counts survive; source-projected lambda=3 weighted witness costs 2.4299922e-9. Build 242 pages, 0 undefined/duplicate. Audit PR only, no merge; G2/RH open. |

| NS-34 | Test an explicit positive comparison weight in the exact prime-shift/Picone capacity identity for the uniform finite-floor target; retain source constraint, both parities and cross terms; prove a scoped bound or record the precise obstruction | Codex (Astra) | done (v1.50: exact identities and scoped loss obstruction) | Positive Gaussian arithmetic weight, exact pole mass 1/sqrt(3), full/exterior Picone identity. Fixed energy-fraction loss or deleting prime-2 forces eta >= kappa*delta*exp(gamma*lambda^2)-O(lambda log lambda), in both source-admissible parity sectors. Full critical comparison CAE remains open and equivalent to the uniform-floor target; no physical negative direction. No new window/tail metric/numerics. Independent NS-37 review: no unresolved MAJOR/MINOR. Actual build 246 pages, 0 undefined/duplicate references; G2/RH remain open. |
| NS-35 | Onboard Astra-2: read the required research record, coordinate task ownership and integration base with active sessions, and record the current boundaries before accepting research work | Astra-2 | done (onboarding at v1.49; no new result) | Required reading completed in the requested order: AGENTS, all research-map closure notes, board through NS-33, v1.49 status and the six specified concentration/zero/quantization statements, and PR14-v3 audit. Coordinated with both active Astra tasks; main at 70eb2bb is the integration base. NS-31 and NS-34 remain with their owners. Actual build: 242 pages, 0 undefined/duplicate references; v1.49 manifest 7/7. No new mathematical claim or manuscript version; G2/RH remain open. |
| NS-37 | Independently review NS-34's positive Gaussian comparison-weight draft: Mellin normalization, radical action, Picone domain/convergence, parity/pole signs, exterior split, exact source projection, and the explicit prime-2 obstruction | Astra-2 | done (v1.50 draft audit; no new result) | audits/ns37-capacity-weight-2026-09-21-v2.html: no MAJOR; both MINORs resolved in revised draft SHA256 bf309b2d55f565f2ffde564a22108df96f5dfb6a09fb8051c8bee3a70d0d8fff. Normalization, domain, both parities, source constraint, cross terms and constants checked analytically. Original/revised snapshots preserved. No numerics or author-worktree edits. Baseline v1.49 build 242 pages, 0 undefined/duplicate; manifest 7/7; this is not a v1.50 integration build. Fixed-energy-loss comparison fails; the full critical route and G2/RH remain open. |

Coordination, 2026-09-21 (Astra-2 onboarding): the NS-31 reviewer reports the audit complete in PR #16 on `audit/2026-09-22-circle-lane`, unmerged. The main Astra session confirmed NS-34 is claimed at `38324b5` on `codex/bounded-capacity-weight`: the positive Gaussian arithmetic radical in the prime-shift/Picone identity, targeting a uniform finite floor, including the obstruction to discarding a fixed fraction of the transformed energy. That argument and its prospective v1.50 manuscript scope remain Astra's. Astra-2 owns only NS-35 here; no further research task has been assigned. The local onboarding branch is `codex/astra2-onboarding`; its standalone claim is `3e150fc`.

Coordination, 2026-09-21: the zero-transfer task was originally claimed as NS-17 at `2e5364b`; concurrent main allocated that number to documentation. It is now NS-18, with the original claim preserved in history. The coarse NS-18 result is recorded in v1.42; its signed sharpening was superseded by the completed NS-19 resolution accounting (v1.43). NS-17 is now integrated at all five requested anchors, with explicit claim qualifications.

Task-ID reconciliation: the pencil-concentration translation was locally claimed as NS-20 (66c8ae3); concurrent main allocated NS-20 through NS-23 to other work. This completed result is NS-24 (v1.44). All concurrent claims are retained; the proposition and build are unchanged.

Task-ID reconciliation, 2026-09-21: local claim 070fe7f used NS-31/32 for PR #14 review and the v1.49 follow-up. Concurrent user assignment reserves NS-31 for the circle/symbol-lane audit. This task therefore uses NS-32 (PR review) and NS-33 (weighted zero input); original claims remain in history.

| NS-36 | Reconcile the circle-lane record after NS-31 and test the unresolved lambda=4, c'=1 finite-bin feasibility claim with the source constraint | Codex (NS-31 reviewer); Astra-2 (independent read-only review) | done (NS-36 diagnostic correction, 2026-09-22; no manuscript version) | Original reports preserved; map/board/introductions corrected. New lambda=4 raw pure witness: bin ratio 2.8474, midpoint Q=4.0522e-18; projected against two source approximations: ratios 2.7853/2.7806, Q=4.0589e-18. Exact repaired-source orthogonality remains uncertified. An any-source mixed-state construction has ratio above 1.12 and numerical Q budget 0.36464. Astra-2 reviewed the finite algebra and scope. Actual build 242 pages, 0 undefined/duplicate; no new window, all-Borel/cofinal, G2 or RH claim. |
| NS-40 | Assess fixed-K quantization growth for the complete corrected zero field: zero counts/density, Ingham, Montgomery, Landau-Gonek, and prescribed cutoff dependence | Astra-2 | done (analytic assessment; integration pending, no new version) | evidence/ns40_qg/ and audits/ns40-qg-zero-field-2026-09-21-v1.html: separated-band and infinite-support weak-limit conditions imply QG; exact cutoff scaling and an integer diluting rule refute uniformity over arbitrary head rules. Prescribed-family QG, prefix error/band masses and separate packet input remain open; no RH-strength or independence claim. Corrected BGSTB v3 citation; bounded peer review has no MAJOR/MINOR. Baseline build 246 pages; temporary fragment build 250 pages; both 0 undefined/duplicate. No live manuscript/map edits. |
| NS-38 | Resolve archival overclaims for the two NS-1 evidence groups: recover originals or explicitly mark every unsupported archival assertion and update evidence/MISSING.md | Codex (Astra Main) | completed by disclosure (no version bump) | Both NS-1 groups explicitly NOT ARCHIVED at affected manuscript claims and evidence/MISSING.md; original recovery remains OPEN. V1.29/v1.30 companion gaps also disclosed; five v1.35 scientific files verified present against legacy hashes. No original numerical gate replayed. |
| NS-39 | Express CAE through the corrected zero field and compare fixed-window/cofinal ZLD, QG and CAE with every hypothesis explicit | Codex (Astra Main) | completed (v1.51; review PR) | Exact corrected-zero-field potential and signed energy; ZLD implies QG growth on the same prescribed family with kappa theta² D/(2K), not independent packet feasibility. CAE exactly equals the complement-floor target. General measure countermodels do not establish arithmetic independence; universal-head QG is false independently of CAE truth. No new signed bound, G2 or RH claim. |
| NS-42 | Measure transformed energy, variance and potential budgets on the first three deep pencil directions in both parities at existing lambda=3,4 | Codex (NS-42 measurement) | completed (diagnostic; no version bump) | Twelve N=48 vectors frozen; direct squared-edge, variance, exterior and signed-potential integrals at two quadrature orders; even source orthogonality not assumed; artifacts in evidence/diag_ns42_energy_budget/. Tiny midpoint q is not resolved by direct quadrature and nothing here is a bound. |

| NS-41 | Odd-sector weighted-bin feasibility at c'=1 on existing windows lambda=3,4,6,8; save every constraint slack and recheck fixed-witness energies at high precision | Codex (NS-41 measurement) | done (diagnostic 2026-09-22; no version bump) | Four fixed pure odd N=256 witnesses pass all 20 weighted bins on original/refined grids; selected energies 4.2549055e-9, 1.5286030e-18, 2.0533131e-3, 5.7198372e-5, not minima. All primal/dual-eigenvector slacks printed separately; 80/120-digit fixed-energy replays and independent direct-transform checks. Odd parity needs no even-source projection. evidence/diag_ns41_odd_feasibility/; build 246 pages, 0 undefined/duplicate. No certificate, all-Borel/cofinal, G2 or RH claim. |

| NS-43 | Prioritize remaining complete-space routes and prove or delimit specific blocked-node closures: capacity comparison, CCM ground selection and source-sensitive concentration | Codex Astra Main with assisting agents | completed (v1.52) | Proved fixed/moving prime-channel loss obstruction; exact adaptive concentration equivalence and scalar countermodel; complete CCM relative-selection criteria and scoped nonselection/coarse-scale obstructions. Independent reviews, no new cofinal signed floor. |

| NS-44 | Rebuild one finite-support counterexample to the already stipulated lambda=5 tail comparison Q16 W Q16 >= 1e-8 Q16 D Q16 in both parities | Codex Astra Main; assisting-agent review | completed (v1.52) | New exact dyadics on indices 17..128; fresh 320/448 Arb gates and independent signed assembly. Positive q/D=6.4235e-18 even, 1.1128e-17 odd contradict 1e-8D. Only this comparison closes; original witness recovery stays OPEN. |

| NS-45 | Rebuild a finite witness obstruction to the already tested lambda=5, N=25 dyadic block-norm criterion | Assisting agent NS42; Codex Astra Main review | completed (v1.52) | New exact dyadic pair certificates at 320/448 on first three existing N=25 blocks. Rational Rayleigh 341/250 even, 2093/1500 odd exceed 1. Metric-existence dichotomy avoids an unused block-inertia claim; only this partition comparison closes. |

| NS-46 | Test a growing translated-radical block as a route to the uniform complete floor: prove a new complementary estimate or identify the exact quantitative obstruction, retaining both parities and all cross terms | Astra Main + Astra-2; assisting-agent prior-art and review | done (v1.53; no floor proved) | Fixed-range fine translates yield rank ~lambda²/(20000 log lambda) and full residual C exp(-lambda²/2000), paying the finite Gram cost. Exact parity/source counts; independent proofs and reviews. Uniform or polynomial positive-gap strategies after o(lambda²/log lambda) removal are excluded. Existing gap-free floor transfer was not repackaged as a new estimate; complete complementary signed floor remains open. |

| NS-47 | Construct an explicit geometric-algebra / graded Dirac representation of the complete Weil form and test a lower bound uniform in growing windows; retain both parities, source and exterior terms | Codex (Astra RH1) | in progress — first analytic checkpoint; uniform floor open | evidence/ns47_clifford_weil/: exact signed Clifford lift and closed positive edge block; contraction demand equals CAE, unproved. Scoped obstruction: no single ordinary-L2 closable positive square plus bounded remainder; any such one-sided lower comparison forces its factor bounded. Both complete parities; fixed-window factors and other completions not excluded. Independent review: 0 outstanding MAJOR/MINOR. Base 24f4ab5 builds 265 pages; isolated draft 270 pages, 0 undefined/duplicate references. No version assigned, new window, tail metric, or G2/RH claim. |

| NS-48 | Part A: audit the high-level v1.51 conclusions, fixed-window scope, ten scoped closures, three open inputs, alternative criteria and RH-conditional dependencies | Astra-3 | done (audit; no version bump) | audits/2026-09-22-conclusions-review.md Part A: four MAJOR interpretation findings; fixed-window certificates and v1.51 implications remain scoped and intact. Pinned v1.51 build 250 pages, 0 undefined/duplicate; v126/140/143/151 manifests pass. No gate replay; audit pinned to the original v1.51 snapshot. |
| NS-49 | Part B: assess at most three untried arithmetic-sensitive routes with published prior art and first falsifiable steps | Astra-3 | done (route assessment; no version bump) | Same audit Part B: ordinary pair statistics and naive monotonicity/linear heat shortcuts fail their first tests; kernel exclusion and nonlinear deformation remain open, with explicit first lemmas and published prior art. No new arithmetic sign estimate, window, tail metric, G2 or RH claim. |

| NS-50 | Attempt a direct uniform cofinal CAE estimate through exact physical-space localization of the complete signed Weil form; determine the full cross-term error and its arithmetic dependence | Astra-3; separate-agent adversarial review | reviewed analytic checkpoint; CAE OPEN | evidence/ns50_cae_localization/: exact signed localization remainder; bounded or theta<1 absorption fails by a specialization of NS47, reproved from v1.51 dense near-radicals. Odd sector already source admissible. Critical theta=1 remains exactly CAE; capping supplies no new bound. Separate AI review: 0 MAJOR, 1 MINOR parity-label defect corrected and verified in localization-v2.tex; originals preserved. Current main build 269 pages; corrected isolated integration 273; both 0 undefined/duplicate. No new window, tail metric or manuscript version. |

Coordination, 2026-09-22 (Astra-3): Alex explicitly assigned NS-43/44 to this audit. The existing unmerged `codex/ns43-route-selection` uses those IDs for different work. Coordinator assigned this audit NS-48/49 because NS-43/44/45 are already used by PR #21, NS-46 by the growing-radical task and NS-47 by the separate factorization task. NS-43/44 remain aliases from the user request only; no existing task is overwritten. Audit base is v1.51 at `b0baadf`, branch `audit/2026-09-22-conclusions`.

| NS-51 | Derive the complete-domain nullvector equation and test the screw-operator injectivity reduction, including endpoint regularity and both parities | Codex Astra RH1; independent domain review | done (v1.54; API open) | Exact nullvector iff affine screw potential on the complete form domain. Rank-one logarithmic-torsion countermodel defeats generic H0¹ bootstrap, not arithmetic injectivity. Independent review: 0 MAJOR/MINOR. No new window/tail metric or G2/RH claim. |
| NS-52 | Derive symmetry-paired zero contributions under heat deformation and test cancellation at a collision, with support dependence retained | Codex Astra RH1; heat-route agent and independent cross-review | done (v1.54; arithmetic transport open) | Correct Xi heat coefficient 1/4; exact finite cluster transport retains exterior-zero term. Support cost grows; unmatched real deformed zero conditionally forbids uniform same-test comparison. That hypothesis is not verified. No general heat closure, new window/tail metric or G2/RH claim. |
| NS-53 | Reopen constructive Nyman–Beurling approximation: exact arithmetic block residual update and sufficient convergence condition without imposing the sharp rate | Codex Astra RH1; approximation-route agent and independent cross-review | done (v1.54; RBC open) | Exact residualized Schur-complement gain and unconditional harmonic-trace lower bound; exact divisor cells. Any convergence rate suffices, but asymptotic corrected correlation lower bound remains unproved. No convergence/failure, G2 or RH claim. |
| NS-54 | Adversarial review of Claude's zero-picture interpretation and Selberg-to-QG proposal: corrected symbol, zero-field law and scaling, packet/closure claims, and heat-flow monotonicity | Astra Main + Astra-2; independent identity, proof and report reviews | done (review only; arithmetic transfer open) | audits/ns54-zero-picture-review-2026-09-22-v1.html: five MAJOR essay deductions and three MINOR corrections; full unbounded-left normalized law conditionally forces QC_K/b to infinity and defeats fixed-fraction ZLD. Actual arithmetic law and independent packet input absent. Independent proof review clean; report packet qualification corrected and verified. Current v1.54 build 278 pages, 0 undefined/duplicate references and overfull boxes; no manuscript version, new window/tail metric or G2/RH claim. |

| NS-55 | Test arithmetic uniqueness beyond the affine screw-potential kernel reformulation: first-crossing, finite-shift and nonlocal uniqueness mechanisms on the complete domain, retaining both parities | Codex Astra RH1; three assisting agents and cross-reviews | done (v1.55; API open) | Exact local-UCP counterexamples for the actual prime-shift operator, including parity/source constraints; no whole-window nullvector. Full semigroup fails ordinary-cone positivity. Restricted prime-free-cell uniqueness and first-zero support saturation delimit the usable geometry; full dilation retains unestimated signed prime/pole terms. No new window/tail metric, uniform floor, G2 or RH claim. Build 285 pages, 0 undefined/duplicate references. |

| NS-57 | Integrate finite prime-weight controls, first-zero windows, bounded-floor stability and fixed-direction sensitivity | Codex, Continue solving toward RH | done (v1.56; original arithmetic sign open) | evidence/v156/: complete-domain analytic implications in both parities, exact scalar compensation, conditional spectral limit, and pattern-dependent lambda_* = O(sqrt(log(1/epsilon))) upper bound. Twelve exact Maxima checks; local integration audit only, no independent review. Complete build and manifest results in validation.json. No negative original Weil direction, new window/tail metric, uniform floor, API, G2 or RH proof. |
| NS-58 | Test an arithmetic boundary constraint for a hypothetical first-zero nullvector using the exact polarized radical identities | Codex, Continue solving toward RH | done (v1.57; stop condition reached, API open) | Complete weak-domain pairing derived with both poles and every exterior prime row. Vanishing for all translated radicals is exactly the original null equation. Altered-weight controls acquire a necessarily nonzero forcing profile; its compact map has no uniform lower bound on the full fixed-window unit sphere. No new independent sign or rigidity estimate. Proof, exact checks, local self-review and build validation in evidence/v157/. |

| NS-59 | Test the NS-53 raw-correlation gain bound against the complete projected Nyman–Beurling blocks, then attempt an independently justified arithmetic bound for a sharper denominator or explicit block quotient | Codex, Continue solving toward RH | done (v1.58; lower correlation input open) | Adjacent norm bound and complete Mellin identity; unconditional raw difference Gram norm O_epsilon(N^(-5/3+epsilon)). Near-N^(-2) power norm is equivalent to Lindelof; fixed-logarithmic raw bounds are impossible. Scope excludes projected/selected-direction bounds. Arb 256/384 finite trace-loss and coordinate-cost gates, exact Maxima checks, local self-review and build in evidence/v158/. No convergence, G2 or RH claim. |

| NS-60 | Test explicit old-space corrections for the NB adjacent-difference blocks, distinguishing raw norm obstructions from projected and actual-residual bounds | Codex, Continue solving toward RH | done (local v1.59 draft; optimal correlation open) | evidence/v159/ns60/: exact averaged-grid correction, all cross terms and a positive-square comparison with optimal projection. Fixed-log N^(-2) norms are excluded for Q_N <= N^alpha, fixed alpha < 1. Optimal/selected-direction bounds remain open; separate finite scan is diagnostic. |

| NS-61 | Test one additional Mellin integration in NB: prove the smoothed criterion with its tail space, derive an unconditional difference-block budget, and examine the transformed correlation requirement | Codex, Continue solving toward RH | done (local v1.59 draft; lower correlation input open) | evidence/v159/ns61/: fixed q=2 criterion with a bounded off-line-zero functional; positive average identity and trace <= 3*kappa/(8*N^2). Exact endpoint moments and full remainder do not give a cofinal lower bound. Complete Arb Grams at 256/384 bits, cutoff replay and independent physical integrals; stop condition reached. |

| NS-62 | Test whether Mellin smoothing repairs the canonical sharp Mobius interpolant; retain the exact target and use a localized dual witness | Codex, Continue solving toward RH | done (local v1.59 draft; scoped full-sequence and cone exclusions) | evidence/v159/ns62/: localized Laguerre witness preserves nonconvergence of the full canonical integer sequence through any number of integrations. Selected subsequences and optimal coefficients are not excluded. The nonnegative difference cone fails by its forced sixth coefficient -1/5. Exact checks and full proofs; scoped stop condition reached. |

| NS-63 | Check fixed versus increasing Mellin smoothing: retain the RH zero obstruction at fixed order and test whether relative errors can vanish for a fixed finite span when the order grows | Codex, Continue solving toward RH | done (local v1.59 draft; fixed-order criterion retained) | evidence/v159/ns63/: every fixed smoothing order preserves the RH criterion. Increasing the order lets one fixed atom achieve relative squared error ~D0^2/(8r) unconditionally, while absolute squared error diverges. Arb finite controls at two precisions and full tails; moving-norm convergence is not RH evidence. |

| NS-64 | Construct an explicit dual separator for the positive smoothed-difference cone and quantify its finite local gap, keeping the claim separate from signed NB approximation | Codex, Continue solving toward RH | done (local v1.59 draft; explicit cone witness) | evidence/v159/ns64/: complete six-function local Gram and exact dual separator. Arb 256/384 certifies five positive projection coefficients and a full-space cone-distance lower bound > 0.00228323; local equality only. 39 exact Maxima checks. Signed approximation and RH remain open. |

| NS-65 | Test ordinary Cesaro averaging of the canonical sharp interpolant after Mellin integration; identify whether averaging removes the existing critical-zero obstruction | Codex, Continue solving toward RH | done (local v1.59 draft; fixed-average obstruction) | evidence/v159/ns65/: a fixed number of ordinary arithmetic Cesaro averages leaves the critical-zero pole and full-sequence nonconvergence after any Mellin integration order. Growing averages, logarithmic tapers and selected subsequences remain outside scope. 39 exact checks. |

| NS-66 | Test a weaker norm-growth target for the once-smoothed canonical interpolant: combine its exact exterior matching with Abel summation and zero evaluation | Codex, Continue solving toward RH | done (local v1.59 draft; subpolynomial bound open) | evidence/v159/ns66/: for each fixed r>=1, log(1+canonical error norm)/log N tends to beta_star-1/2. Complete support lower bound and Bochner-Abel upper bound prove the reformulation. A bounded cofinal subsequence suffices for RH; none is proved. 29 exact checks, including complete physical Abel identities and exterior interpolation. |

| NS-67 | Test direct cancellation in the fixed once-smoothed canonical error, retaining the complete boundary/integral identity and seeking an independent growth estimate | Codex, Continue solving toward RH | done (v1.60; arithmetic input open) | Complete divisor cells, full tails, polynomial-cutoff growth equivalence and centered Abel conditioning <4.617. Two precisions, independent Gram checks and cutoff replay; internal arithmetic growth remains open. |

| NS-68 | Test a single multiplicative-annulus response and its positive renewal equation as a possible independent canonical growth estimate | Codex, Continue solving toward RH | done (v1.60; arithmetic input open) | Exact positive renewal with weighted q_theta<1; integer scalar forcing bound remains RH-equivalent. Critical weighted total energy is infinite, not D_N. Two-precision finite checks through 2,097,152 Mobius coefficients. |

| NS-69 | Test the actual signed endpoint remainder for optimized smoothed NB residuals, rather than its absolute coefficient-mass budget | Codex, Continue solving toward RH | done (v1.60; arithmetic input open) | Exact signed optimized remainder and factor-18 smaller allowance. Actual remainder exceeds model at N=64,128; two endpoint directions retain only 3.3% of gain at N=128. Complete cross terms and projected finite gains certified. |

| NS-70 | Test whether the elementary q=2 Gram background admits a uniformly small arithmetic correction; repair any diagonal-regularity mismatch before judging the comparison | Codex, Continue solving toward RH | done (v1.60; arithmetic input open) | Explicit d/max cusp correction repairs adjacent power and is exactly diagonal in difference coordinates. Both uniform all-coefficient comparisons remain impossible; selected actual directions remain open. Complete two-precision constants and cutoff replay. |

| NS-71 | Test the repaired elementary Gram only as a preconditioner for the actual optimized residual, retaining the true projected energy in every gain quotient | Codex, Continue solving toward RH | done (v1.60; arithmetic input open) | Repaired projected-kernel direction captures 97.06% of optimal gain at N=256 versus 38.41% for raw correlation; squared error reduction 8.08% versus optimum 8.33%. Complete 256/384-bit and doubled-cutoff checks. Cofinal numerator/cost input remains open. |

| NS-72 | Derive a complete local differential-energy representation of the repaired elementary kernel and a curvature minorant for the actual selected numerator | Codex, Continue solving toward RH | done (v1.61; cofinal arithmetic bound open) | Whole-line causal factor and local energy; exact model interpolation; uniform curvature comparison. Linear direction rule captures 97.63% of full gain at N=256. Complete Arb replays and 41 exact checks. |

| NS-73 | Test whether the successful curvature direction has a simple signed Mobius/log-taper coefficient explanation, using complete projected arithmetic energies | Codex, Continue solving toward RH | done (v1.61; finite template control) | Three physical Mobius/log-taper directions and their complete optimized span retain 83.66% of gain at N=256 versus 97.63% for curvature. Ten exact checks; no asymptotic template exclusion. |

| NS-74 | Construct a nearby unitary deformation with the same full Gram geometry and an explicit nonzero approximation floor; test what finite gain efficiency can distinguish | Codex, Continue solving toward RH | done (v1.61; altered-family control) | Explicit unitary Blaschke deformation preserves all complete Gram entries and has positive floor (2 beta-1)(1-beta)^2/beta^6. Finite statistics approach the original as beta decreases to 1/2. Sixteen exact checks and complete finite replay; no original-family error floor. |

| NS-75 | Test correction coefficients from the actual optimized residual divisor sums; retain exact derivative jumps and full projected energy | Codex, Continue solving toward RH | done (v1.62; finite control) | Complete divisor-log identity and jump measure; unit-step failure at all tested blocks. Optimized three-direction gain is 56.02% at N=256 versus curvature 97.63%. No general asymptotic feedback exclusion. |

| NS-76 | Identify the complete continuous-dilation relaxation in Hardy space and derive its exact q=2 inner-factor distance, retaining the distinction from integer dilation closure | Codex, Continue solving toward RH | done (v1.62; exact continuous relaxation) | Complete tail-to-Hardy unitary; exact q=2 Blaschke distance and invisible component. Strict integer/continuous closure separation with certified witness >0.00111713. No equality of positive target distances assumed. |

| NS-77 | Bound the continuous q=2 inner-factor defect in terms of hypothetical off-critical zero tails, and determine the scope of finite-height information | Codex, Continue solving toward RH | done (v1.62; complete continuous tail bound) | D_cont^2 <= (8/3) S2^3 + 5 S4. Published zero verification and complete counting tail imply D_cont^2 < 2.08e-32. External input only; no integer upper bound, new verified height, or zero-distance proof. |

| NS-78 | Derive a complete norm comparison with reciprocal-integer residual samples and independently replay the actual optimized norm through divisor cells | Codex, Continue solving toward RH | done (v1.63; cofinal sum open) | Uniform complete reciprocal-knot comparison; exact divisor inversion; complete physical and sample tails. Independent full norm checks at N=16,64,256. No vanishing cofinal arithmetic sum. |

| NS-79 | Test tail-balanced divisor feedback suggested by the complete sampling norm, with separate raw and projected gains | Codex, Continue solving toward RH | done (v1.63; finite balanced control) | Exact exterior preservation sacrifices the last jump. At N=256 balanced three-span captures 59.97% and endpoint-augmented span 71.18%, below curvature 97.63%. Two of fifteen raw unit steps decrease error; no uniform descent. |

| NS-80 | Transfer the complete arithmetic sampling norm to a uniform projected-Gram preconditioner bound and quantify its finite-block descent guarantee | Codex, Continue solving toward RH | done (v1.63; uniform finite-block theorem) | Full arithmetic sampling Gram gives uniform projected condition ratio <=21. One ideal step captures >=21/121 of block gain; twenty capture >97.79%. No fast inverse or cofinal relative gain bound. |

| NS-81 | Bound ordinary smoothed integer Gram conditioning from finite reciprocal samples and replace the infinite arithmetic comparator with an explicitly sufficient finite cutoff | Codex, Continue solving toward RH | done (v1.64; effective but impractical bound) | Coefficient recovery gives ordinary Gram condition O(N^4 log^2 N). Full sample-tail bound yields sufficient finite cutoff 2^16(N+1)^6 and projected condition <=42. Huge comparator not assembled; no cofinal decay or practical implementation. |

| NS-82 | Retain the analytic logarithmic tail as a rank-two form to reduce the sufficient finite-comparator cutoff | Codex, Continue solving toward RH | done (v1.65; analytic tail retained) | Rank-two physical tail and full remainder yield projected condition <=9 and sufficient cutoff 8435244 for 512 total atoms. Scalar certificates only; comparator and iterations not run. No cofinal decay. |

| NS-83 | Derive the critical-zero lower bound for fixed Mellin smoothing and test which cofinal relative-gain estimates remain possible | Codex, Continue solving toward RH | done (v1.66; fixed-order rate restriction) | Complete Burnol dual-vector adaptation gives positive logarithmic lower liminf at every fixed smoothing order. Constant relative contraction at every sufficiently large doubling is excluded; weaker nonsummable arithmetic gain remains open. Certified zero-subset constant has no finite-N onset. |

| NS-84 | Review every registered conclusion and current evidence/audit status; persist Alex’s per-turn review requirement | Codex, Continue solving toward RH | done (review; manuscript v1.66 unchanged) | Record scope and findings against the current main commit; correct stale summaries without silently upgrading missing evidence or implying a fresh proof audit. |

| NS-85 | Test complete logarithmically tapered Mobius approximants and identify which arithmetic estimate a slower-rate candidate actually requires | Codex, Continue solving toward RH | done (finite control; arithmetic rate open) | Retain the full physical norm and tails; distinguish fixed coefficients from optimized fits, diagnostics from certificates, and finite behavior from an asymptotic bound. Stop rather than claim a new rate from a finite table. |

| NS-86 | Derive complete optimized-residual optimality in arithmetic potential coordinates; test a signed identity for aggregate gain and retain the exact remainder | Codex, Continue solving toward RH | done (finite control; cofinal input open) | Exact optimized Muntz quadrature and full observation-tail bound; raw convolution-square correction fails the unit-step test at N=4,16. At N=16, damping plus old-space refitting captures 27.31% of full N-to-N^2 gain. All tails retained; no asymptotic estimate or manuscript version bump. |

| NS-87 | Localize the optimized arithmetic observations jointly and certify their implication for full block gain | Codex, Continue solving toward RH | done (localization; arithmetic lower bound open) | Joint complete-tail gain certificate and explicit safe step; T=N^6 preserves the logarithmic relative-gain scale by NS81/83. Finite N=32 certificate retains >95.98% of available gain. No new arithmetic lower bound, effective onset, fast inverse or manuscript version. |

| NS-88 | Test whether optimized multiplicative normal equations force an energy-scale arithmetic numerator | Codex, Continue solving toward RH | done (upper envelope; arithmetic growth open) | Exact successive-increment identity, complete next-size and cumulative upper-error bounds. Eventual energy/j^p numerator lower bound excluded for p<1; p=1 remains possible only at coefficient <=1/sqrt(2). Finite defect changes sign and gain capture dips to 0.3256%. No cofinal lower growth or error-decay theorem. |

| NS-89 | Construct the optimal tail-normalized upper certificate and quantify its complete error cost | Codex, Continue solving toward RH | done (constructive upper certificate; decay open) | Original fixed-seed obstruction test stopped before publication. Focus on explicit approximants, complete upper error, and what remains missing for the logarithmic upper-rate candidate. No new lower-bound result or cofinal decay inferred. |

| NS-90 | Test a signed Mobius inversion estimate for the actual optimized finite arithmetic observations and its complete gain cost | Codex, Continue on PR42 arithmetic lower gain | done (attempt recorded; manuscript v1.66 unchanged) | Prime main terms cancel exactly after old-space orthogonality. Complete signed numerator is positive at N16,256, but the tested termwise absolute lower bound is negative; its divisor allowance diverges with cutoff at fixed N under the stated nonzero-tail hypothesis. No linked-cutoff or cofinal exclusion, lower gain, or new finite efficiency result. Full projected costs inherited from NS73. See evidence/ns90_mobius_gain. |

| NS-91 | Preserve joint arithmetic cancellation by a first primitive and endpoint correction; test a uniform route beyond the finite bound | Codex, Continue on PR42 grouped lower gain | done (finite bound and attempt recorded; uniform estimate open) | Joint first-primitive dyadic bound includes every omitted interval; old-space correction removes 0<t<N. Certifies relative gain >0.02821 at N256, on the known NS73 direction. Grouped tail negligible at N^6. NS78 inversion plus normal equations reduces the proposed quadratic rewrite to the same missing numerator. No cofinal lower gain; see evidence/ns91_joint_abel. |
| NS-92 | Derive and test a direct arithmetic upper bound on the selected true cost, retaining the signed gain condition | Codex, Continue on PR42 after NS91 | done (complete cost bound and finite step; uniform input open) | NS61 average gives a scalar upper budget from signed Mobius tails and a feasible endpoint-only step. At N256 the physical 1/16 step reduces full error by >1.57%; the cheap budget certifies >0.0443% for 1/512. Seven scalar checks through N65536 are not a uniform bound. Elementary oscillation control gives only O(N); no cofinal gain or new best error. See evidence/ns92_arithmetic_cost. |

| NS-93 | Test a concrete averaged arithmetic estimate for the selected cost and gain, retaining all signed correlations and projection losses | Codex | done (signed estimate remains open; manuscript unchanged) | Bounded diagonal; complete absolute-product cost grows at least linearly for dyadic N>=2048, so averaging does not repair that bound. Signed averaged cost and actual numerator remain unproved. Two-precision finite decomposition and eight Maxima checks; evidence/ns93_averaged_cost. |
| NS-94 | Check the tangent-circle inversion and exterior similarity-point proposal in ordinary coordinates and Maxima | Codex | done (exact geometric check; no RH inference) | Read the linked Zhao handout, which does not define exterior similarity. Separate and successive inversions checked; equal counts and infinity persist in a symmetric off-line control. Nonnegative power-product statistic still requires an arithmetic vanishing proof. 23 Maxima checks; evidence/ns94_circle_inversion. |

| NS-95 | Test the N-to-N^2 product-index grouping against the complete joint arithmetic gain, retaining old-space projection, missing indices and complete costs | Codex | done (construction tested; cofinal lower bound open) | Free signed lift captures 99.83% of full gain at N16 to 256 versus NS86's 27.31%; its large-prime coefficient restriction and missing gain are exact. All-residual comparison fails under a prime-pair hypothesis; actual-target bound remains open. Complete 256/384-bit and cutoff replays, physical norms and 18 Maxima checks; evidence/ns95_square_product. |

| NS-96 | Test a genuine LCM divisor-square positivity replacement for square-scale signed gain, including complete real Mellin moments and the old-space refit | Codex | complete; scoped result, v1.66 unchanged | Both complete signs have fixed error floors. After unrestricted old refitting the projected PSD cone equals the signed LCM span; nonzero residual-pairing matrix indefinite. Extra rank/trace constraints not covered. Actual cofinal lower gain remains open. [Proof and checks](evidence/ns96_lcm_square/) |

## Historical continuation targets after NS-66 (tested in NS-67–71)

1. **Canonical boundary/integral cancellation.** Keep one Mellin integration
   fixed and use the complete identity in `eq:ns66-bochner-abel`. Attempt a
   direct subpolynomial bound on the norm, or a bounded cofinal subsequence,
   retaining the target, boundary term, integral and every cross term. The
   existing triangle estimate assumes an RH-level Mertens bound and is not
   the missing estimate. Stop if the proposed input merely restates a
   zero-free half-plane or assumes the desired norm bound. A finite table
   cannot establish boundedness of a cofinal subsequence.
2. **Actual optimized correlations.** The denominator in
   `eq:ns61-gain` is now elementary. Obtain a lower estimate for the actual
   residual correlations with a non-summable relative contraction sequence.
   The endpoint formula keeps its signed remainder; the current coefficient-
   mass triangle bound is vacuous on the certified blocks. Do not insert
   target loads, positive-cone arguments, or a changing norm in place of
   those optimized signed correlations. Stop if no independent arithmetic
   estimate survives the complete remainder.

The scoped tests above are now recorded in NS-67–71. The underlying
arithmetic estimates remain open. Publication and merge/tag approval were
given on September 23; check the latest remote state and PRs before work.

## Open continuation targets after NS-71 (not yet claimed)

1. **Selected arithmetic numerator and cost.** Use the explicit repaired
   kernel only to choose coefficients. Bound the actual model-inverted
   numerator relative to E_N and the true energy on that chosen direction,
   as in `prop:ns71-selected-input`. A nonsummable contraction along dyadic
   blocks suffices. The certified 97.06% finite gain fraction at N=256 does
   not provide either cofinal estimate. Do not assume the all-coefficient
   comparison excluded in NS-70.
2. **Internal canonical cancellation.** The two complete Abel vectors have
   a uniform conditioning bound after explicit centering. A useful new
   estimate must act inside the signed integral or divisor-cell response.
   The positive renewal inverse transfers the same forcing power; it cannot
   manufacture the still-missing RH-equivalent arithmetic bound.

Claim a separate row before taking either target forward. No bounded
cofinal canonical subsequence or asymptotic NB contraction is established.

## Open continuation after NS-74

Geometry now supplies an explicit curvature functional and a local coefficient
rule, but its actual numerator and selected cost still lack cofinal bounds.
The same-Gram control shows that no finite efficiency threshold repairs this
missing arithmetic step. A further attempt must use information that the
inserted inner-factor control changes, or prove a genuinely cofinal estimate.
Do not replace this with larger finite blocks or another uniform all-vector
Gram comparison. The three tested Mobius templates are a finite control only.

## Open continuation after NS-77

The exact continuous defect is extremely small under existing published
finite-height information, but can still be positive. Continuous and integer
closures are strictly different, so an approximation theorem for the relaxed
space does not transfer automatically. The actual integer limiting error
and cofinal curvature contraction remain open. A useful next estimate must
control the integer residual with complete signed arithmetic information;
local cancellation of its derivative jumps did not provide descent.

## Open continuation after NS-80

The complete arithmetic sample sum is an explicit equivalent norm, and its
inverse formulas expose all finite-support divisor constraints. Prove a
cofinal decay bound for that complete signed quantity, or bound available
block gain relative to the entire current error. Uniform efficiency within
a finite block is now available if the full arithmetic comparator can be
applied, but it does not supply convergence or a fast algorithm. The tested
endpoint tail repair does not explain the curvature rule's finite success.

## Open continuation after NS-81

Numerical conditioning of ordinary integer Grams has a polynomial bound,
and the arithmetic comparator has an explicit finite realization in
principle. The displayed sufficient cutoff is deliberately impractical;
sharpening it would be an algorithmic task, not an RH convergence proof.
The mathematical priority remains a cofinal bound on the complete signed
arithmetic sample sum, or available gain relative to the entire error.

## Open continuation after NS-82

The sharper finite comparator is still an algorithmic construction, not a
convergence theorem. Prioritize cofinal signed arithmetic decay or a lower
bound on available gain relative to the full error. An implementation may
be useful later, but repeated finite efficiency tests alone cannot close RH.

## Open continuation after NS-83

Do not aim for a uniform fraction of the full error per doubling: the
critical-zero lower bound excludes it even after any fixed smoothing order.
A genuinely estimated actual-residual gain of size a/j, 0<a<=1, or a weaker
nonsummable scale remains a possible sufficient target. Merely restating
its sufficiency is already covered by NS53/59. No pointwise upper bound
on each individual block gain, asymptotic equality, or decay is established.

## Open continuation after NS-87

The complete observation tail can now be removed from the logarithmic
relative-gain target at a sufficient polynomial physical cutoff N^6.
Prove a lower bound for the resulting signed finite arithmetic observation
energy of the actual optimized residual, relative to its full error.
All old-space projection terms and the actual Gram remain. A positive lower
liminf of j*A_(N^6)/E_N on N=2^j would suffice; it is unproved and not
asserted necessary. Repeating this sufficiency or another finite efficiency
table would not supply the missing arithmetic estimate.

## Open continuation after NS-88

The scalar dilation route has a complete upper-error envelope. The missing
input is divergence of its cumulative normalized absolute defect S_J,
or a lower growth S_J >= a log J - b with a>0 for a quantitative upper rate.
Neither is proved or asserted necessary. Exact normal equations only
supply an upper overlap bound, and the generic identities survive the
NS74 control. A proof must use the original signed arithmetic expression.
Do not assume an energy-size or energy/sqrt(j) lower defect: both are
excluded for this construction. The finite envelope is not a new best
finite error bound, and another finite table is not a substitute for growth.

## Open continuation after NS-89

Stay on the upper-bound construction. Exact zero-exterior coefficients lose
at most a factor 1.144579 compared with the unrestricted optimum for every
N>=256. This permits searching within that normalized family without losing
a logarithmic exponent. The explicit full certificate is the signed finite
divisor-cell energy plus the complete main tail and remainder cross term.
Prove an independent uniform upper estimate for it along an explicit family;
do not substitute another lower-bound obstruction, a finite table, or the
rate-transfer comparison itself for that missing decay theorem. Ordinary
Gram solves still determine the optimized finite witnesses; no fast or
closed-form cofinal coefficient rule is supplied.

## Open continuation after NS-90

The primary target is still NS87/PR42: lower-bound the full joint signed
finite arithmetic observation energy relative to the actual optimized
error. The Mobius/log-taper test does not supply this lower bound. Its
prime main terms cancel; exterior normalization and divisor forcing must
be bounded together. Absolute-value separation is vacuous in the two
certified tests and deteriorates with cutoff at fixed N under a nonzero
residual-tail hypothesis. This does not exclude the direction, another
combined estimate, or the cofinal cutoff N^6. Do not repeat NS73 efficiency
tables or NS89 normalization as a new decay theorem.


## Open continuation after NS-91

The first-primitive grouped bound repairs the NS90 absolute-value estimate
at the tested sizes. Its corrected compensator vanishes before N, and its
complete absolute dyadic tail is negligible at T=N^6. What remains is an
independent bound on the finite arithmetic margin relative to the true
projected cost. With rho_N = B_N(N^6)/E_N and kappa_N = K_N/E_N, a sufficient
target is rho_N < log 2 and (log 2-rho_N)^2/kappa_N >= a/j on N=2^j,
eventually, for fixed a>0. No such estimate is proved. Neither a constant
finite percentage nor bounded raw/canonical norms may be assumed.

The proposed divisor-defect quadratic rewrite is NS78 inversion followed
by substitution. On the normal-equation space it is beta^2 times the same
numerator, not a new sign theorem. Do not repackage that identity as a
solution. This does not close arithmetic estimates of the expression.
The full PR42 joint-observation route remains the primary alternative to
this single selected direction. Both historical original-evidence gaps
remain open; manuscript v1.66 is unchanged.

## Open continuation after NS-92

The selected true cost now has a sufficient scalar upper budget from the
signed Mobius suffixes T_N(x): U_N <= kappa*log(2)*integral(T_N(x)^2 dx).
This is a proved full-space inequality; boundedness of its arithmetic
factor is not proved. The elementary block-oscillation estimate gives
only O(N), and square-root cancellation must not be assumed. The seven
finite scalar checks are not a uniform estimate or evidence that RH holds.

Compatible lower numerator and upper cost estimates are still required.
For this stronger sufficient budget, b_N >= epsilon E_N and bounded
integral(T_N^2) would give a/j relative gain via NS83. They are not asserted
necessary. Preserve useful old-space cancellation when seeking a sharper
cost estimate: at N256 the scalar budget is about 60.74 times the true
projected cost. Its eventual failure would not close PR42's full route.
The explicit endpoint-only finite step is a feasible certificate, not a
cofinal algorithm or a new best approximation. Both historical original
evidence gaps remain open; manuscript v1.66 unchanged.

## Open continuation after NS-93/94

Averaged descent would follow from a positive mean actual numerator margin
and a bounded mean signed cost on growing ranges of doubling indices.
This is an application of the existing criterion, not a new theorem of
arithmetic cancellation. The scalar cost diagonal is uniformly bounded;
the needed upper bound for its signed off-diagonal Mobius correlations
remains open. Full productwise absolute separation is now excluded as a
way to prove that bounded average: its majorant grows at least linearly.
This does not exclude signed estimates, the smaller projected cost or the
full PR42 joint observation route. Do not extrapolate the finite averages.

The tangent-circle geometry detects off-line locations but cannot turn
reflection symmetry or equal counts into their absence. The exterior
similarity point depends only on the circle parameters. The nonnegative
power-product zero sum is a possible coordinate language, not an arithmetic
estimate: vanishing at every finite height is still RH-equivalent. A future
geometric argument must supply a special property of zeta beyond the
symmetries shared by the exact polynomial control. No broad geometric
impossibility is claimed. Both historical evidence gaps remain open.

## Open continuation after NS-95

The full N-to-N^2 lower-gain target remains open. Freeing all signed
product weights repairs the prescribed correction's finite loss, but
retains exact coefficient restrictions at large primes and a nonzero
complementary gain. A lower-gain requirement on this restricted family is
stronger than the full PR42 target, not equivalent to it. Its finite efficiency gives
no persistent lower fraction of the actual error.

The next useful estimate must bound the actual-target signed observations
relative to E_N, in the free lift or with the complementary block retained.
Do not identify old products with the full squared-size index set, regard
the product-pairing matrix as positive, invoke the all-residual comparison
refuted here, or substitute another larger efficiency table. The exact
square identity is not retained after arbitrary reweighting and old refit.
A compatible small fixed gain per squaring remains a sufficient unproved
target; fixed gain every doubling is excluded. No new manuscript version.

## Open continuation after NS-96

The pointwise-positive LCM replacement cannot serve as the entire
coefficient rule with either global sign. Free old-space refitting removes
those particular floors, but then PSD mixtures generate the full signed
LCM span. Do not infer a positive numerator from the matrix constraint,
or carry the pure-rule floors over to refitted approximants.

Retain the full signed PR42 observation problem or the explicitly
restricted NS95 actual-target problem. A useful estimate must jointly
control the actual numerator and complete projected cost relative to E_N.
If imposing an additional trace, diagonal or rank constraint on an LCM
square, first show that it survives the old refit and quantify the cost
of the cancellation. NS96 does not exclude such constrained constructions,
and provides no uniform lower gain for them. No further finite efficiency
table is prescribed. The tail and original historical evidence gaps have
exactly their prior status; no new manuscript version.

## Lanes

```
lane/concentration     the live mechanism (prop:v131-concentration)
lane/bounded-floor     v1.36 reduction; floors certified through λ=8
lane/semantic-lock     NS-2
lane/circle-toeplitz   NS-7  (Claude)
lane/odd-sector        odd-parity obligations
lane/window-scaling    window behaviour; closed to new windows by NS-13
```

Add a row before starting anything not listed. Remove nothing.
