# NS-54 consolidated report — independent bounded review

Internal review note. Scope: the consolidated report's mathematical constants,
claim directions, attribution to the supplied Claude essay, and the separately
identified v1.54 heat update. No new numerical experiment, literature expansion,
arithmetic limit theorem, or signed-floor claim. Only this review file was written;
author files, manuscript, board, map, and Git state were not changed.

## Pinned inputs

| File | SHA256 |
|---|---|
| `audits/ns54-zero-picture-review-2026-09-22-v1.html` (reviewed correction) | `084dd3a6a437b643cda51af8e928aabfd53b9856fc4e83c891eb62ec39a2080e` |
| `evidence/ns54_zero_picture/identity/identity_review.md` | `3a95e1fd8279baecdcebb3ffee4511484c52104a077663e74a33d07280167f47` |
| `evidence/ns54_zero_picture/selberg/selberg_qg_assessment.tex` | `f9f4c43f07c768f32df09df7aa472149a1d4d1220ce6c3ea4dbc30ae99c87b3d` |
| `evidence/ns54_zero_picture/review/map_heat_notes.md` | `7c9e8ecee994b07369eb94e8e21dde9f0f3165b1e16d50dc69edf6d0583d431b` |
| `evidence/ns52_heat_pairs/proof.tex` | `b7f3df5788d9d69051560e84c71cef9835d21e34bc8a18de9bb4b73cffbd5893` |

The coordinating author supplied the essay's original relevant passages verbatim
during this review. The review also compared the cited manuscript formulas at
`f0178e0` and the heat/map update at `bea0ed2`. It does not substitute the
supporting reviewers' paraphrases for the essay on the central attribution issue.

## Ranked findings

**MAJOR: none.**

**MINOR: none outstanding.**

**Resolved MINOR 1 — `audits/ns54-zero-picture-review-2026-09-22-v1.html:48`:
the concluding implication dropped the packet hypothesis.**

At initial report SHA
`9d3fee455bc9fd20a8b54fc66f5625a3753b6d04cc9818692df7d592ceb09d2d`,
after asking for a matched CLT or band law for the complete field, the report said:
“If that match succeeds, it yields a new bounded-level complexity obstruction.”
The matched scalar law alone supplies the QG growth clause. The obstruction to
bounded-level minorants additionally needs source-admissible unit packets with
uniformly bounded original energy and all-Borel domination. The essay itself
included that independent packet input; report M5 correctly explains it. The final
recommendation must preserve it too.

Suggested replacement: “If that match succeeds, it yields the QG growth clause;
together with the separate packet input, it yields a bounded-level complexity
obstruction.” The author applied this replacement verbatim before delivery;
the corrected wording was reread and its final hash pinned above. This resolves
the local scope finding without changing the conditional measure theorem.

## Attribution and scope checks

- The essay explicitly says “Selberg's theorem may prove QG” and calls this a
  falsifiable proposal. The report's title, M3, conditional section, and final
  status treat it as a proposal. They do not attribute a completed QG proof to
  Claude. The substantive objection is to the asserted correspondence with a
  smoothed `S`, the missing normalization/head-family/error transfer, and the
  claimed consequences if only endpoint/Perron terms survive.
- M1 and M2 target statements actually in the essay: unconditional
  ordinate-only sinc terms, subtraction of expected density, and a local-count
  sign test. The real part of one complex-zero term is
  `2 exp(L eta) [eta cos(Ly)+y sin(Ly)]/(eta^2+y^2)`; the stated
  critical-line specialization and the signed-sinc counterexample are correct.
  At fixed window the retained `log|xi|+O_a(1)` term contradicts the proposed
  centered field. The Stieltjes integration-by-parts formula has the correct
  derivative and boundary signs.
- M4 addresses the essay's literal “Every obstruction on the map” assertion.
  The reported positive contraction quotient is exactly the archived enclosure
  `2.05254409540345 < q/D < 2.05254409540346`. The positive NS44 tail
  witnesses refute the stipulated comparison rather than form positivity.
  Read the finding as a correction to the claimed common mechanism of the
  recorded results, not as a proof of logical independence between arithmetic
  phenomena. The report's explanation retains that scope.
- M5 addresses the essay's explicit proposed red status for the entire
  concentration node. Its loss inequality has the correct direction and
  distinguishes bounded level count from unrestricted adaptive counts and
  complete signed operator estimates. Apart from MINOR 1 above, the independent
  packet requirement is explicit. MINOR 1 is now resolved in the concluding
  recommendation as well.

## Constants and conditional implications

- At lambda=6, the first trivial-zero summand is `-1/9720`; the geometric
  majorant gives `-2/19425 <= C_a(0) < -1/9720`. The endpoint vanishes
  because `Lambda(36)=0`, but these corrections and finite-prefix Perron
  terms remain.
- For fixed `a`, averaging the finite cosine polynomial on `[T,2T]` yields
  `Var(B_a)=2 sum_{2<=n<exp(2a)} Lambda(n)^2/n+O_a(1/T)`. No uniformity
  in growing `a` is claimed. This calibration does not disprove a separately
  formulated simultaneous-limit theorem.
- The stated full uncentered weak-limit hypothesis with unbounded negative
  support implies both `D_a/b_a -> infinity` and
  `QC_K/b_a -> infinity` for every fixed `K`. The actual downward levels
  include the global anchor. Near-optimizing grids and compactification of
  their finitely many normalized levels justify the stronger limit without
  an attained optimizer or moment convergence. Tightness then rules out the
  stipulated ZLD lower mass on each fixed positive-fraction depth band, only
  under that full-family hypothesis. No arithmetic Gaussian law is claimed.
- The finite-test, scale, support, and variance restrictions on the cited
  Maples–Rodgers theorem match the frozen primary-source assessment. The
  report correctly calls that theorem unconditional and leaves extensions
  of its methods open.

## Current heat status

The report's internal gap contribution `4/d` is in the explicitly specified
`partial_t H_t=-partial_zz H_t` coordinate. The author also clarified the HTML
derivative notation during this correction. NS52 uses `Z_t(w)=8H_t(2w)`, with coefficient
`kappa=1/4`; in that coordinate the corresponding contribution is `4 kappa/d`.
There is no hidden normalization error in the report. Its caveat about external
zeros prevents an unsupported claim that every complete-system gap increases.

NS52 defines the correctly normalized deformed zero form on the compact smooth
core, counts multiplicity, proves convergence there, and obtains nonnegativity
at a time with all real zeros. It does not provide monotonicity or an extension
to the full original form domain. Its unmatched-zero obstruction is expressly
conditional and scoped to one uniform same-test comparison. The consolidated
report retains those restrictions. The DBN, de Branges, F1, and NB nodes are
indeed open at `bea0ed2`. The report distinguishes that current update from its
v1.53 baseline.

**Disposition:** clean after the verified local correction; no outstanding MAJOR
or MINOR. The consolidated report fairly reviews the essay and preserves the
mathematical scopes checked above. No new arithmetic QG, signed floor, G2, or RH
conclusion follows.
