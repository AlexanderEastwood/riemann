# NS-46 / v1.53 review record

Classification: independent analytic review and integration checks; not a
numerical certificate or a proof of the remaining signed floor.

## Source proofs and independence

Astra Main supplied the finite-arc Gram estimate. Astra-2 independently checked
that input and supplied the complete cutoff residual, normalization, parity,
source-codimension and spectral-count argument. Separate assisting reviewers
examined both source proofs and the integrated summaries. Their records are
archived under `evidence/ns46_radical_block/review/` and individually pinned by
`provenance.json`.

The finite-arc source has SHA256
`ed8d0093fb1a21e8f81857b4c3f053762a9d22a2a50d38313aec2237df1e701b`.
The complete-block source has SHA256
`44307ff1ab01dd6d93b1d287367359cb209bf6166789c30de894f281591bd3d2`.
Both are embedded without alteration in `new_section.tex`; that complete
section is embedded verbatim once in the live manuscript.

## Ranked review outcome

MAJOR: none within the reviewed new proofs and integration.

MINOR, resolved: several short map/status/log summaries said that a positive gap
was excluded without specifying its scale. The proved ceiling is
`C exp(-lambda²/2000)`. A smaller positive gap is compatible with the theorem.
The affected summaries now say uniform or polynomial positive gap, and the
map/log/report explicitly retain the possibility of a smaller positive gap.
The original formal theorem already gave the correct ceiling. Both pinned
source proofs remain unchanged.

NOTE: all constants and the eventual starting threshold are analytic. No
finite numerical threshold or floating-point illustration is being promoted
to a certificate. The complete signed complementary floor remains open.

The source reviews specifically checked the full Gram loss `1-chi²`, the
complete all-prime residual and both poles, operator domains, coefficient
amplification, exact parity dimensions, the actual source codimension, and
the absence of a sign inference from a symmetric near-zero interval.

## Integration and prior art

The pre-existing v1.18 gap-free block transfer and v1.36 complementary-floor
criterion already handle a growing block. Repeating those implications would
not constitute a new route. The new content is the finite-Gram estimate and
the resulting rank/residual balance. The stale v1.18 prose saying every growing
block residual was still open was qualified to distinguish arbitrary blocks
from the explicit v1.35 and new v1.53 constructions.

The README status row was synchronized with the existing map: CCM step (b) is
the sole live/gold node; the circle retains its exact open measurement-lane
note. Only the new scoped uniform/polynomial positive-gap strategy closes.
The general concentration and signed-floor inputs do not close.

Astra-2's optional fixed-spacing companion and literature notes are archived
as separate author material. They are neither integrated into v1.53 nor used
in the reviewed dense-block theorem; the bounded integration review does not
claim an independent review of that optional companion.

## Actual validation

`./manuscript/build.sh` built 269 pages, with zero undefined references,
zero duplicate references and zero overfull boxes. Source label and bibliography
key uniqueness also passed. `build_report.json` pins the integrated manuscript
and fragment hashes. Prior manifests v1.50, v1.51 and v1.52 passed at 6/6, 6/6
and 9/9; v1.52's 33 external artifacts and certificate bindings also passed.
The new artifact hashes and new incremental manifest are integrity checks,
not numerical proof gates. No new Python or numerical code was added.
