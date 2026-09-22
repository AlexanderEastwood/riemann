# Fixed-Space Prime Compatibility

Alexander Eastwood's complete working manuscript, **v1.53**.

**G2 and the Riemann Hypothesis remain open.** Nothing in this repository
claims otherwise.

## Navigating this repository

- **[RESEARCH_MAP.md](RESEARCH_MAP.md)** — the whole project as one diagram:
  every idea, which sub-ideas were tried, and which passed or failed.
- **[COMPARISON.md](COMPARISON.md)** — where the certified `lambda = 4`
  window sits relative to published work, with the parameter translation.
- **[REPO_LAYOUT.md](REPO_LAYOUT.md)** — directory layout, branch and tag
  conventions, and how to add a new version.
- **[evidence/MISSING.md](evidence/MISSING.md)** — artifacts the manuscript
  cites that this repository does not yet contain. Read this before relying
  on any computer-assisted claim.
- **[AGENTS.md](AGENTS.md)** — instructions for AI agents contributing here.

```sh
./manuscript/build.sh                     # build the PDF (source validation is not a build)
python3 tools/verify_manifest.py v126     # check a version's artifacts, or --all
python3 tools/make_map.py                 # regenerate RESEARCH_MAP.md
```

## Status at a glance

| | |
|---|---|
| Only positivity result | `W_4 >= 0`, both parity sectors — evidence restored and verified |
| Complete ground at lambda=4 | Simple and even; `0<mu0<2.454e-75`, `mu1>1e-73`; its entire Fourier transform has only real zeros ([certificate](evidence/v140/)) |
| Complete-ground first zero | First positive zero simple and within 8.752082e-33 of gamma_1, at 1024/1280 bits ([v1.43](evidence/v143/)); no discrepancy sign |
| CCM finite benchmark | Eight local lambda=3, N=120 root discrepancies certified at 768/1024 bits; broader reproduction remains diagnostic ([v1.41](evidence/v141/)) |
| Finite floors | `W_λ >= -8·I` at λ = 5, 6, 8, both parities, full infinite tail (`prop:v138-three-floors`) |
| Certified window | half-width `a = log 4 = 1.386`; 1.73× the published Zhu window, 4× the classical range |
| Live mechanism | CCM step (b): identify a limit mechanism for the complete ground |
| Routes proved closed | 22 scoped map nodes; unavailable v1.28 numerical closure separately blocked |
| Evidence gaps | Both remaining groups explicitly not archived; disclosure complete, recovery open — see the ledger |
| G2 | open |
| RH | open, and not claimed |

## Research map

Every idea, which sub-ideas were tried from it, and which passed or failed.
Green = proved · gold = current route · red = closed · purple = blocked · grey = open.
Nodes with a folder icon link to the `evidence/` directory holding their
certificates; the full version with a node-by-node list is
[RESEARCH_MAP.md](RESEARCH_MAP.md).

<!-- research-map:start -->
```mermaid
graph LR
  rh["RH"]
  g1["G1 (weak)<br/><small>thm:v14-radical</small><br/><small>&#128193; evidence/v124/g2_source_certificate</small>"]
  fixedspace["Fixed-space / Burnol Sonine route"]
  g2["G2: cofinal -o(1)<br/><small>prop:v121-cofinal-rh</small>"]
  windows["Fixed-window certificates"]
  w3["lambda=3<br/><small>prop:v116-window-positive</small><br/><small>&#128193; evidence/v124/g2_certificate</small>"]
  w4e["lambda=4 even<br/><small>prop:v125-even-complete</small><br/><small>&#128193; evidence/v126</small>"]
  w4o["lambda=4 odd<br/><small>prop:v126-odd-complement</small><br/><small>&#128193; evidence/v126</small>"]
  w4["W_4 >= 0 both sectors<br/><small>prop:v126-full-window</small><br/><small>&#128193; evidence/v126</small>"]
  w5["lambda=5: stipulated 10^-8 D tail comparison<br/><small>prop:v152-tail-comparison</small><br/><small>&#128193; evidence/ns44_metric_replay</small>"]
  uniform["Uniform mechanism for G2"]
  primenorm["unsigned prime-norm domination<br/><small>prop:v119-prime-essential</small><br/><small>&#128193; evidence/v124/g2_growing_sign</small>"]
  normcontr["norm contraction<br/><small>prop:v120-norm-counterexample</small><br/><small>&#128193; evidence/v124/g2_weighted_signed</small>"]
  schatten["Schatten / Hilbert-Schmidt<br/><small>prop:v132-schatten</small><br/><small>EVIDENCE MISSING</small>"]
  sampling["basis / sampling dominance<br/><small>prop:v121-complement-cancellation</small><br/><small>&#128193; evidence/v124/g2_schur_cancellation</small>"]
  farmaj["scalar far majorant<br/><small>prop:v125-cutoff-cost</small><br/><small>&#128193; evidence/v126/g2_window_resolution</small>"]
  blockmetric["lambda=5 N=25: tested dyadic norm comparison<br/><small>prop:v152-block-comparison</small><br/><small>&#128193; evidence/ns45_block_replay</small>"]
  flattop["flat-top smoothing<br/><small>prop:v132-flat-top</small><br/><small>EVIDENCE MISSING</small>"]
  recipband["reciprocal-band commutation<br/><small>EVIDENCE MISSING</small>"]
  cotlar["Cotlar cross terms / atomization<br/><small>EVIDENCE MISSING</small>"]
  scalarprim["scalar signed primitive<br/><small>cor:v137-scalar-no-go</small><br/><small>&#128193; evidence/v137</small>"]
  concentration["signed weighted concentration<br/><small>prop:v131-concentration</small><br/><small>&#128193; evidence/v152</small><br/><small><b>wall: QG + WLH packet</b></small>"]
  weaken["Target weakening"]
  floor["uniform finite floor suffices<br/><small>prop:v136-bounded-floor</small><br/><small>&#128193; evidence/v136</small>"]
  gapfree["no uniform positive gap exists<br/><small>prop:v135-growing-radical</small><br/><small>&#128193; evidence/v135</small>"]
  floortest["W_lambda >= -8 I at lambda=5,6,8<br/><small>prop:v138-three-floors</small><br/><small>&#128193; evidence/v138</small>"]
  shiftbarrier["bounded shift keeps the exp cutoff barrier<br/><small>prop:v138-shifted-floor</small><br/><small>&#128193; evidence/v138</small>"]
  metablind["Scoped information-loss obstructions<br/><small>thm:v139-probe-relaxation; thm:v139-protected-orbit</small><br/><small>&#128193; evidence/v139</small>"]
  altroutes["Alternative criteria (classical RH equivalents; no finite bridge proved)"]
  circle["circle / Toeplitz-Hankel lens<br/><small>&#128193; evidence/diag_true_symbol</small>"]
  debranges["de Branges / Hermite-Biehler<br/><small><b>wall: screw-kernel positivity = RH; no fixed-window bridge</b></small>"]
  f1["function field / Hodge / F_1<br/><small><b>wall: no intersection form supplied for this window (missing construction)</b></small>"]
  nb["Nyman-Beurling-Baez-Duarte<br/><small>&#128193; evidence/diag_routes/nb</small><br/><small><b>wall: d_N -> 0 = RH; no finite bridge from W_4 to d_N</b></small>"]
  li["Li / Keiper coefficients<br/><small>&#128193; evidence/diag_routes/li</small><br/><small><b>wall: all Li coefficients >= 0 = RH; windowed coefficients are different objects</b></small>"]
  dbn["de Bruijn-Newman (Lambda = 0 iff RH)<br/><small>&#128193; evidence/diag_routes/dbn</small><br/><small><b>wall: Lambda <= 0 = RH; positive-time barrier reproduced, no-bridge not proved</b></small>"]
  ccmmu["W_4 >= 0  <=>  CCM mu_lambda >= 0 for all lambda <= 4"]
  simpleeven4["complete W_4: simple even ground; real-zero transform<br/><small>prop:v140-ground4; cor:v140-real-zeros</small><br/><small>&#128193; evidence/v140</small>"]
  stepb["CCM step (b): finite-compression zeros track zeta zeros (numerical)<br/><small>&#128193; evidence/diag_ns2_semantic_lock</small>"]
  semanticlock["CCM finite-compression semantic lock, lambda=3 N=120<br/><small>lem:v141-centering; prop:v141-ccm-lock</small><br/><small>&#128193; evidence/v141</small>"]
  groundzero4["complete ground zero within 0.1 of gamma_1<br/><small>lem:v142-energy-projection; prop:v142-ground-zero</small><br/><small>&#128193; evidence/v142</small>"]
  groundzero4resolution["first complete zero within 9e-33; archived resolution quantified<br/><small>prop:v143-first-zero-bound; prop:v143-resolution; prop:v143-fixed-window-meaning</small><br/><small>&#128193; evidence/v143</small>"]
  pencilconcentration["pencil loss budget; cofinal obligation retained<br/><small>prop:v144-pencil-concentration</small><br/><small>&#128193; evidence/v144</small>"]
  betaexplicit["exact lattice symbol; varying envelopes<br/><small>prop:v146-beta-explicit</small><br/><small>&#128193; evidence/v146</small>"]
  minorantlevels["bounded-complexity minorants: arithmetic gap remains<br/><small>prop:v146-packet-loss; prop:v146-level-complexity</small><br/><small>&#128193; evidence/v146</small><br/><small><b>wall: ZLD + packet</b></small>"]
  zeroleveldistribution["zero level distribution and packet coverage: open inputs<br/><small>prop:v147-level-separation; ass:v147-zld; prop:v147-depth-measure; prop:v147-broad-packet</small><br/><small>&#128193; evidence/v147</small><br/><small><b>wall: ZLD + packet</b></small>"]
  weightedexactcost["weighted exact cost: peak bound fails at critical levels<br/><small>prop:v149-critical-density; prop:v149-weighted-cost; prop:v149-qc1-insufficient; ass:v149-qg</small><br/><small>&#128193; evidence/v149</small><br/><small><b>wall: QG + WLH packet</b></small>"]
  capacityweight["positive arithmetic weight: critical capacity input<br/><small>lem:v150-weight; prop:v150-critical-energy; ass:v150-cae</small><br/><small>&#128193; evidence/v150</small><br/><small><b>wall: CAE</b></small>"]
  capacityslack["fixed energy loss for the Gaussian arithmetic weight<br/><small>prop:v150-capacity-slack</small><br/><small>&#128193; evidence/v150</small>"]
  inputcomparison["ZLD to QG; CAE is the signed-floor target<br/><small>prop:v151-input-comparison</small><br/><small>&#128193; evidence/v151</small>"]
  capacitychannels["Fixed/sub-endpoint channel deletion with unchanged signed terms<br/><small>prop:ns43-fixed-channel; prop:ns43-moving-channel</small><br/><small>&#128193; evidence/v152</small>"]
  bumpstrength["Restricted bump discrepancy can carry the full zero obstruction<br/><small>prop:ns43-bump-strength</small><br/><small>&#128193; evidence/v152</small>"]
  adaptiveidentity["Unrestricted exact adaptive hierarchy = complement floor<br/><small>ns43-conc-prop-adaptive</small><br/><small>&#128193; evidence/v152</small>"]
  scalarsetshortcut["Scalar set bounds alone determine signed floor: general inference<br/><small>ns43-conc-prop-scalar</small><br/><small>&#128193; evidence/v152</small>"]
  relativeselection["Complete relative selection and entire-transform control<br/><small>prop:ns43-ccm-rayleigh-selection; prop:ns43-ccm-residual-selection</small><br/><small>&#128193; evidence/v152</small><br/><small><b>wall: cofinal separator</b></small>"]
  absoluteselection["Absolute residual/resolvent data alone select ground: abstract inference<br/><small>prop:ns43-ccm-nonselection</small><br/><small>&#128193; evidence/v152</small>"]
  coarseprofile["Single profile from the specified coarse rescaled liminf<br/><small>prop:ns43-ccm-coarse-profile</small><br/><small>&#128193; evidence/v152</small>"]
  fineradicalrank["Uniform or polynomial positive gap after o(lambda²/log lambda) removed directions<br/><small>lem:ns46-finite-arc; ns46-a2-cor-large-block; ns46-a2-cor-rank</small><br/><small>&#128193; evidence/v153</small>"]

  rh --> g1
  rh --> fixedspace
  rh --> g2
  g2 --> windows
  windows --> w3
  windows --> w4e
  windows --> w4o
  windows --> w4
  windows --> w5
  g2 --> uniform
  uniform --> primenorm
  uniform --> normcontr
  uniform --> schatten
  uniform --> sampling
  uniform --> farmaj
  uniform --> blockmetric
  uniform --> flattop
  uniform --> recipband
  uniform --> cotlar
  uniform --> scalarprim
  uniform --> concentration
  g2 --> weaken
  weaken --> floor
  weaken --> gapfree
  floor --> floortest
  floor --> shiftbarrier
  uniform --> metablind
  rh --> altroutes
  altroutes --> circle
  altroutes --> debranges
  altroutes --> f1
  altroutes --> nb
  altroutes --> li
  altroutes --> dbn
  w4 --> ccmmu
  w4 --> simpleeven4
  simpleeven4 --> stepb
  windows --> semanticlock
  simpleeven4 --> groundzero4
  groundzero4 --> groundzero4resolution
  concentration --> pencilconcentration
  concentration --> betaexplicit
  concentration --> minorantlevels
  minorantlevels --> zeroleveldistribution
  zeroleveldistribution --> weightedexactcost
  floor --> capacityweight
  capacityweight --> capacityslack
  capacityweight --> inputcomparison
  capacityweight --> capacitychannels
  capacityweight --> bumpstrength
  concentration --> adaptiveidentity
  concentration --> scalarsetshortcut
  stepb --> relativeselection
  stepb --> absoluteselection
  stepb --> coarseprofile
  gapfree --> fineradicalrank
  concentration -. "QG + WLH packet" .-> floor
  debranges -. "screw-kernel positivity = RH; no fixed-window bridge" .-> rh
  nb -. "d_N -> 0 = RH; no finite bridge from W_4 to d_N" .-> rh
  li -. "all Li coefficients >= 0 = RH; windowed coefficients are different objects" .-> rh
  dbn -. "Lambda <= 0 = RH; positive-time barrier reproduced, no-bridge not proved" .-> rh
  minorantlevels -. "ZLD + packet" .-> floor
  zeroleveldistribution -. "ZLD + packet" .-> floor
  weightedexactcost -. "QG + WLH packet" .-> floor
  capacityweight -. "CAE" .-> floor
  relativeselection -. "cofinal separator" .-> g2

  click g1 "https://github.com/AlexanderEastwood/riemann/tree/main/evidence/v124/g2_source_certificate/" "evidence: evidence/v124/g2_source_certificate" _blank
  click w3 "https://github.com/AlexanderEastwood/riemann/tree/main/evidence/v124/g2_certificate/" "evidence: evidence/v124/g2_certificate" _blank
  click w4e "https://github.com/AlexanderEastwood/riemann/tree/main/evidence/v126/" "evidence: evidence/v126" _blank
  click w4o "https://github.com/AlexanderEastwood/riemann/tree/main/evidence/v126/" "evidence: evidence/v126" _blank
  click w4 "https://github.com/AlexanderEastwood/riemann/tree/main/evidence/v126/" "evidence: evidence/v126" _blank
  click w5 "https://github.com/AlexanderEastwood/riemann/tree/main/evidence/ns44_metric_replay/" "evidence: evidence/ns44_metric_replay" _blank
  click primenorm "https://github.com/AlexanderEastwood/riemann/tree/main/evidence/v124/g2_growing_sign/" "evidence: evidence/v124/g2_growing_sign" _blank
  click normcontr "https://github.com/AlexanderEastwood/riemann/tree/main/evidence/v124/g2_weighted_signed/" "evidence: evidence/v124/g2_weighted_signed" _blank
  click sampling "https://github.com/AlexanderEastwood/riemann/tree/main/evidence/v124/g2_schur_cancellation/" "evidence: evidence/v124/g2_schur_cancellation" _blank
  click farmaj "https://github.com/AlexanderEastwood/riemann/tree/main/evidence/v126/g2_window_resolution/" "evidence: evidence/v126/g2_window_resolution" _blank
  click blockmetric "https://github.com/AlexanderEastwood/riemann/tree/main/evidence/ns45_block_replay/" "evidence: evidence/ns45_block_replay" _blank
  click scalarprim "https://github.com/AlexanderEastwood/riemann/tree/main/evidence/v137/" "evidence: evidence/v137" _blank
  click concentration "https://github.com/AlexanderEastwood/riemann/tree/main/evidence/v152/" "evidence: evidence/v152" _blank
  click floor "https://github.com/AlexanderEastwood/riemann/tree/main/evidence/v136/" "evidence: evidence/v136" _blank
  click gapfree "https://github.com/AlexanderEastwood/riemann/tree/main/evidence/v135/" "evidence: evidence/v135" _blank
  click floortest "https://github.com/AlexanderEastwood/riemann/tree/main/evidence/v138/" "evidence: evidence/v138" _blank
  click shiftbarrier "https://github.com/AlexanderEastwood/riemann/tree/main/evidence/v138/" "evidence: evidence/v138" _blank
  click metablind "https://github.com/AlexanderEastwood/riemann/tree/main/evidence/v139/" "evidence: evidence/v139" _blank
  click circle "https://github.com/AlexanderEastwood/riemann/tree/main/evidence/diag_true_symbol/" "evidence: evidence/diag_true_symbol" _blank
  click nb "https://github.com/AlexanderEastwood/riemann/tree/main/evidence/diag_routes/nb/" "evidence: evidence/diag_routes/nb" _blank
  click li "https://github.com/AlexanderEastwood/riemann/tree/main/evidence/diag_routes/li/" "evidence: evidence/diag_routes/li" _blank
  click dbn "https://github.com/AlexanderEastwood/riemann/tree/main/evidence/diag_routes/dbn/" "evidence: evidence/diag_routes/dbn" _blank
  click simpleeven4 "https://github.com/AlexanderEastwood/riemann/tree/main/evidence/v140/" "evidence: evidence/v140" _blank
  click stepb "https://github.com/AlexanderEastwood/riemann/tree/main/evidence/diag_ns2_semantic_lock/" "evidence: evidence/diag_ns2_semantic_lock" _blank
  click semanticlock "https://github.com/AlexanderEastwood/riemann/tree/main/evidence/v141/" "evidence: evidence/v141" _blank
  click groundzero4 "https://github.com/AlexanderEastwood/riemann/tree/main/evidence/v142/" "evidence: evidence/v142" _blank
  click groundzero4resolution "https://github.com/AlexanderEastwood/riemann/tree/main/evidence/v143/" "evidence: evidence/v143" _blank
  click pencilconcentration "https://github.com/AlexanderEastwood/riemann/tree/main/evidence/v144/" "evidence: evidence/v144" _blank
  click betaexplicit "https://github.com/AlexanderEastwood/riemann/tree/main/evidence/v146/" "evidence: evidence/v146" _blank
  click minorantlevels "https://github.com/AlexanderEastwood/riemann/tree/main/evidence/v146/" "evidence: evidence/v146" _blank
  click zeroleveldistribution "https://github.com/AlexanderEastwood/riemann/tree/main/evidence/v147/" "evidence: evidence/v147" _blank
  click weightedexactcost "https://github.com/AlexanderEastwood/riemann/tree/main/evidence/v149/" "evidence: evidence/v149" _blank
  click capacityweight "https://github.com/AlexanderEastwood/riemann/tree/main/evidence/v150/" "evidence: evidence/v150" _blank
  click capacityslack "https://github.com/AlexanderEastwood/riemann/tree/main/evidence/v150/" "evidence: evidence/v150" _blank
  click inputcomparison "https://github.com/AlexanderEastwood/riemann/tree/main/evidence/v151/" "evidence: evidence/v151" _blank
  click capacitychannels "https://github.com/AlexanderEastwood/riemann/tree/main/evidence/v152/" "evidence: evidence/v152" _blank
  click bumpstrength "https://github.com/AlexanderEastwood/riemann/tree/main/evidence/v152/" "evidence: evidence/v152" _blank
  click adaptiveidentity "https://github.com/AlexanderEastwood/riemann/tree/main/evidence/v152/" "evidence: evidence/v152" _blank
  click scalarsetshortcut "https://github.com/AlexanderEastwood/riemann/tree/main/evidence/v152/" "evidence: evidence/v152" _blank
  click relativeselection "https://github.com/AlexanderEastwood/riemann/tree/main/evidence/v152/" "evidence: evidence/v152" _blank
  click absoluteselection "https://github.com/AlexanderEastwood/riemann/tree/main/evidence/v152/" "evidence: evidence/v152" _blank
  click coarseprofile "https://github.com/AlexanderEastwood/riemann/tree/main/evidence/v152/" "evidence: evidence/v152" _blank
  click fineradicalrank "https://github.com/AlexanderEastwood/riemann/tree/main/evidence/v153/" "evidence: evidence/v153" _blank

  classDef proved fill:#a5d6a7,stroke:#1b5e20,stroke-width:1px,color:#000;
  class g1,windows,w3,w4e,w4o,w4,weaken,floor,gapfree,floortest,shiftbarrier,metablind,ccmmu,simpleeven4,semanticlock,groundzero4,groundzero4resolution,pencilconcentration,betaexplicit,inputcomparison,bumpstrength,adaptiveidentity proved;
  classDef live fill:#ffd54f,stroke:#f57f17,stroke-width:3px,color:#000;
  class stepb live;
  classDef closed fill:#ef9a9a,stroke:#b71c1c,stroke-width:1px,color:#000;
  class w5,primenorm,normcontr,schatten,sampling,farmaj,blockmetric,flattop,recipband,cotlar,scalarprim,capacityslack,capacitychannels,scalarsetshortcut,absoluteselection,coarseprofile,fineradicalrank closed;
  classDef blocked fill:#ce93d8,stroke:#4a148c,stroke-width:1px,color:#000;
  class concentration,debranges,f1,nb,li,dbn,minorantlevels,zeroleveldistribution,weightedexactcost,capacityweight,relativeselection blocked;
  classDef open fill:#cfd8dc,stroke:#37474f,stroke-width:1px,color:#000;
  class rh,fixedspace,g2,uniform,altroutes,circle open;
  subgraph Legend
    direction LR
    lg_live["current route (gold)"]:::live
    lg_closed["closed route"]:::closed
    lg_proved["proved"]:::proved
    lg_open["open"]:::open
    lg_blocked["blocked"]:::blocked
  end
```
<!-- research-map:end -->

## Current manuscript

- [Complete LaTeX](manuscript/fixed_space_prime_action_v1.tex)
- [Research log and candidate register](log/RH_G1_G2_research_log.md)
- [Revision notes](log/v1_revision_notes.md)
- [Checksums and provenance](manifest/v1.53_manifest.json)

One live manuscript; delivery is **LaTeX only** at the author's request.
Prior versions are reachable by tag (`v1.24`, `v1.34` … `v1.38`).

## New in v1.53

[NS-46, jointly with Astra-2](evidence/v153/), proves a larger complete near-zero
block: dimension asymptotic to **lambda²/(20000 log lambda)** and full operator
residual at most **C exp(-lambda²/2000)**. The construction changes from widely
spaced translates to increasingly close translates inside a fixed interval.
A finite-arc interpolation proof explicitly pays for the deteriorating Gram.

The block has exact even/odd dimensions. Removing o(lambda²/log lambda)
directions cannot leave a positive uniform or polynomial gap. This is a stronger
rank obstruction, **not a complementary lower floor**. It determines no energy
sign and gives no certified finite starting window. The gap-free uniform-floor
route remains open. No new numerical window, tail metric, G2 or RH claim.

[Assessment, proof and review scope](evidence/v153/ns46-fine-block-2026-09-22-v1.html).
The joint result is reviewed in [PR #24](https://github.com/AlexanderEastwood/riemann/pull/24)
and builds on the merged v1.52. Archived reports retain their prepublication checkpoint status.

## New in v1.52 (PR #21)

[NS-43/44/45](evidence/v152/) add two fresh, narrowly scoped comparison
certificates and complete analytic proofs for route selection. At the existing
lambda=5 window, both parity witnesses have positive Weil energy but violate
`10^-8 D`. The existing N=25 dyadic norm comparison has rational Rayleigh
bounds **1.364** and **2093/1500**, both above one. These replace missing proof
inputs for those comparisons; they do not recover historical artifacts or
establish a negative Weil direction.

The capacity proof extends the fixed-loss obstruction to all fixed prime-power
channels and omitted channels uniformly below the endpoint. Exact adaptive
concentration is an equivalent floor target; scalar set bounds can miss signed
operator information. CCM needs a complete relative selection estimate and
entire-transform control. Abstract residual/resolvent and coarse-profile
shortcuts close only under their stated hypotheses. CCM step (b) stays the sole
gold node; the circle lane remains open. No G2 or RH result.

[Route assessment and scope](evidence/v152/ns43-route-assessment-2026-09-22-v1.html).
The v1.52 change is reviewed in PR #21 and builds on the merged v1.51 work in PR #20. Archived reports retain their prepublication checkpoint status.

## New in v1.51

[NS-39](evidence/v151/) gives one proposition comparing the three open inputs:
ZLD implies QG's growth clause on the same prescribed family, with lower cost
`κ θ² D / (2K)`; packet feasibility remains separate. The complete corrected
zero field gives the positive-weight potential exactly. CAE is precisely the
uniform complement-floor target in those coordinates. No new signed estimate,
arithmetic independence, G2 or RH result follows.

[NS-38](evidence/ns38_archival_disclosure/ns38-archival-disclosure-2026-09-22-v3.html)
uses explicit disclosure for both missing evidence groups; no originals were
recovered. The five v1.35 scientific files are present and match legacy hashes.
The two new measurement records are separate diagnostics:
[NS-41 odd feasible states](evidence/diag_ns41_odd_feasibility/) and
[NS-42 transformed energies](evidence/diag_ns42_energy_budget/).
Neither is cited as a bound. NS-40's QG literature assessment is coordinated
separately in [PR #19](https://github.com/AlexanderEastwood/riemann/pull/19).

## New in v1.50

NS-34 chooses the explicit positive Gaussian arithmetic radical as the
weight in the physical prime-shift/Picone identity. Its exact pole mass is
1/sqrt(3); the complete energy identity retains the odd pole and exterior
edges. For this weight, a fixed fractional loss of transformed energy,
or omission of the prime-2 channel alone, forces a capacity error growing
like exp(gamma*lambda^2), up to O(lambda log lambda). The source constraint
is imposed exactly in a two-dimensional even test space; odd parity is
covered separately.

The closed result concerns those weakened lower comparisons. The full
coefficient-one comparison remains the named open input CAE, equivalent
to the existing uniform complement-floor target in these coordinates.
A different weight is not excluded. No numerical experiment, new window
or tail metric; G2 and RH remain open. See [v1.50](evidence/v150/).

## New in v1.49

PR #14's v1.48 candidate is held for major review findings. The valid
weighted bound eta >= [c' QC_K - Q]+ is restated self-contained. Negative
critical values make the exact continuous level-density peak infinite;
the finite histogram peak is a different quantity. QC_1 growth alone is
also insufficient: a full-support countermodel has QC_1~D/2 but QC_2->0.
The corrected cofinal input is Exact Level Quantization Growth (QG), plus
admissible bounded-energy weighted packets; a QC_1/K law needs a separate
shape hypothesis. Both inputs remain open. No new computation, window or
tail metric. G2 and RH remain open. See [v1.49](evidence/v149/) and the
[PR #14 review](audits/2026-09-21-v1.48-pr14-v3.html).

## New in v1.47

NS-29 separates the measure of every interval of symbol levels from the
Fourier coverage and original energy of a physical packet. Cumulative
sublevel bounds do not imply the required density. The exact zero expansion
provides a precise named open input, ZLD, with endpoint and trivial terms
retained. The zero theorems assessed do not supply that value distribution.
Depth growth yields only local widths with window-dependent constants;
broad Fourier pulses have energy log X + O(1). Both uniform level measure
and bounded-energy packet coverage remain open. The route stays blocked,
not closed; G2 and RH remain open. See [v1.47](evidence/v147/).

## New in v1.46

The exact lattice-symbol identity retains the strict prime-power endpoint,
trivial zeros and Perron remainder. Its envelopes vary; the comb is an
explicit-formula representation, not a new positivity mechanism. The
numerical illustration checks 40 low samples and 14 deep-trough/centroid
locations with explicit summation and zero-count conventions.

The minorant analysis proves local packet bounds and a conditional linear
level-count inequality. Positive spill and original packet energy must be
retained. Uniform arithmetic level distribution and bounded packet energy
remain unproved, so the route stays **blocked, not closed**. The concentration
criterion remains valid; G2 and RH remain open. See [v1.46](evidence/v146/).

## New in v1.45

Audit MINOR M1/M2 wording corrections: inherited 320/768/896-bit inputs are
separated from the new 1024/1280-bit gates, and the direct-bound limitation
is paired with the separate frozen-trial transfer floor, about 6.65e-38.
No enclosure changed. See [v1.45](evidence/v145/).

## New in v1.44

NS-24 translates the weighted concentration inequality to exact pencil
directions: the relative minorant loss must be at most
`nu_k + eta_a ||v_k||^2/q+[v_k]`, with source admissibility and all mixture
cross terms retained. This is a fixed-window head condition. The complete
criterion still needs cofinal uniform control; uniformly bounded errors
already suffice under v1.36's hypotheses. The twelve small lambda=4 N=48
values are cited only as diagnostics. No new computation or concentration
bound is claimed, and the v1.43 enclosure is unchanged. G2 and RH stay open.

## New in v1.43

NS-19 closes with a two-sided enclosure of the complete first positive
lambda=4 zero and a precise resolution statement. The radius is
`sqrt(C_ell*rho)/0.0016 < 8.752082e-33 < 9e-33`. The missing lower-energy
transfer would require a Rayleigh gap about `3.2032e-153` (relative
`1.3055e-78`), plus a suitably centered trial for a gamma-centered result.
The finite N=120 discrepancy of about `+2.92504e-71` is separately
certified and does not transfer to the complete ground. This is a limit
of the displayed archived bounds, not a failure of the object or a
universal no-go theorem. No new window or tail metric; G2 and RH stay open.

## New in v1.42

One local zero of the **complete** lambda=4 ground transform is now
certified within 0.1 of the first zeta ordinate. It is unique and simple
in that interval. The complete even-sector separator 1e-67 makes an
energy-projection bound small enough to transfer endpoint and derivative
signs. The old global separator is too coarse for the same test.

All 4097 trial coefficients and the archived infinite-tail bounds are
retained. Both 1024/1280-bit replays and a second implementation pass.
No new window is computed. This does not determine the discrepancy's sign,
order earlier zeros, or establish cofinal convergence. G2 and RH remain
open. [Proof and replay](evidence/v142/).

## New in v1.41

The existing lambda=3, N=120 compression reproduces the first eight local
zero discrepancies in CCM §6 Figure 1, with interval eigenpair/root gates
replayed at 768 and 1024 bits. The first discrepancy is approximately
1.582329697193127e-34, matching their rounded 1.6e-34.

This identifies the missing `(-1)^n` centering phase in the prior NS-14
script. Its sinc-lattice conclusion is withdrawn; the old run is preserved
with a correction. The new result is finite-dimensional and supplies no
complete-ground zero locations or cofinal convergence. G2 and RH remain open.
The literature comparison is integrated and both missing evidence groups
remain OPEN. [Proof and replay](evidence/v141/).

## New in v1.39

Two precise meta-obstructions delimit information-losing estimates. The
optimal full-histogram mass-cap bound, and a mass/height/variation
relaxation, cannot supply a cofinal finite floor for the actual symbol.
A separate spectral-rotation theorem preserves any finite head and its
complete operator action while exposing the divergent negative multiplier
edge. Its conjugates need not remain multiplication operators.

The unrestricted slogan “every location-insensitive estimate fails” is
false; an exact positive counterexample and a ten-route coverage audit
are included. These results do not close G2 or prove RH.

[Proof, exact checks and scope audit](evidence/v139/).

## New in v1.38

v1.36 reduced G2 to a **uniform finite floor**: one constant `C_*` with
`W_λ >= -C_*·I` along a cofinal family suffices, with no decay required.
v1.38 tests that reduction directly instead of seeking another positivity
certificate.

With a common shift `δ = 8`, head cutoff `N = 256`, remote cutoff
`J = 4096`, moment order 16, and **no tail-metric prerequisite** (`Z = 0`),
both complete parity forms are certified at λ = 5, 6, 8:

    -8  <=  inf σ(W_λ^±)  <  1e-16

The lower bound retains the complete infinite Fourier tail; the upper
bound is a certified finite-support trial quotient. By support
consistency the floor holds for every `1 < λ <= 8`. The same exact dyadic
witnesses pass at 160 and 256 bits.

The shift is what makes it affordable: the remote cutoff needs
`N+1 > L·exp(M_φ − δ)`, so `δ = 8` buys a factor `e^8`. But
`prop:v138-shifted-floor` proves any *bounded* shift keeps the exponential
barrier of `prop:v125-cutoff-cost`; escaping it in this comparison would
need `δ` to grow like `M_φ ~ λ`, which is uninformative. The certificate's
generalized margin falls from 0.84 to 0.10 (odd) across the three windows.
**That decrease measures enclosure headroom, not the sign of the physical
edge** — no cofinal lower estimate is asserted, and no G2 gap is closed.

- [certificates, 160 and 256 bits](evidence/v138/)

## New in v1.37

v1.36 showed that one uniform finite ordinary lower floor on the complete
small-residual complement would suffice. v1.37 tests whether the older
scalar primitive estimate could meet this weaker target.

It cannot: for the exact arithmetic symbol, its optimal scalar error
`a Delta(beta_a)` tends to infinity. The pointwise infimum of `beta_a`
also tends to minus infinity. Both conclusions are unconditional.

The proof uses a nonnegative frequency probe whose Fourier transform
vanishes at the two physical cutoff endpoints. Under RH its pairing with
the exact symbol retains a negative cutoff side lobe around a zero.
Any bounded cofinal scalar certificate would itself imply RH via v1.36,
then contradict that pairing. The linear rates are RH-conditional; no
unconditional linear rate is asserted.

The probe is not a physical squared Paley–Wiener transform, so these scalar
obstructions do not refute positivity of the physical form. The signed
concentration estimate, retaining favorable and unfavorable levels jointly,
remains open in both parities. No G2 sign gap was closed.

- [Proof and novelty report](evidence/v137/research_report.md)
- [Proof excerpt](evidence/v137/new_section.tex)
- [Independent adversarial review](evidence/v137/adversarial_review.md)
- [Probe checks](evidence/v137/check_probe.py) · [results](evidence/v137/probe_results.json)

The ingredients are classical; worldwide novelty is not claimed. Numerical
quadrature is diagnostic and not a proof.

## The `lambda = 4` evidence

The original v1.26 reproduction bundle has been recovered and committed
under [`evidence/v126/`](evidence/v126/): 468 files, byte-identical to the
archived ZIP (SHA-256 `ccdb8eaa…82d8f`, independently re-verified). It
includes both final certificate directories:

- [complete even sector — `g2_simultaneous`](evidence/v126/g2_simultaneous/)
- [complete odd sector — `g2_odd_complement`](evidence/v126/g2_odd_complement/)

Final proof gates using the saved ingredients, witness bindings and the
exact shared-head equality were replayed successfully. This did not
regenerate witnesses or rerun every residual assembly; RESTORED in the
ledger records availability, not a fresh independent audit of every
computation. Provenance and per-file checksums:
[`manifest/README_v126_evidence_recovery.md`](manifest/README_v126_evidence_recovery.md).

## License

Apache-2.0 — see [LICENSE](LICENSE).
