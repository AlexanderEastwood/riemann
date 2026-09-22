# NS-46 / v1.53 — independent integration review

Classification: analytic review and artifact-integrity check. This is not a
numerical certificate, a new signed estimate, or a G2/RH claim. Review date:
2026-09-22. Only this internal review note was edited by the reviewer.

## Pinned inputs

| File | SHA256 |
|---|---|
| `evidence/v153/new_section.tex` | `3690b9c5d584f3f2078759f9067d02c1aa1e0c29846af63c6608d632b4893384` |
| `evidence/ns46_radical_block/coordinator/finite_arc_gram.tex` | `ed8d0093fb1a21e8f81857b4c3f053762a9d22a2a50d38313aec2237df1e701b` |
| `evidence/ns46_radical_block/astra2/complete_block_bounds.tex` | `44307ff1ab01dd6d93b1d287367359cb209bf6166789c30de894f281591bd3d2` |
| `manuscript/fixed_space_prime_action_v1.tex` | `1a392824d45047f8f2d607a0ff9cee7083b62b605172a1102a87f2606d3100c1` |
| `research-map.json` | `f755b11e4f00eef0533f569654cadf11bd7bf544d8ba8796031982b258be730c` |
| `RESEARCH_MAP.md` | `dadbd7a84195aabff62482864c4291116d4e6aeeba5550d340c8140a45aec847` |
| `README.md` | `14bd28a28e468f63b96a9f174717cb9b6e24a505049df07c3eb02914d3c33f2a` |
| `AGENTS.md` | `f526d5f86c2c7331f617c40f4481c244aa56438c530da39db3b1f32881f1b166` |
| `NEXT_STEPS.md` | `0899f53f9ebf7eda199ad7450b2bbd095370b387c882acca62f2cda14a028353` |
| `log/RH_G1_G2_research_log.md` | `f7208348be23ed63f4b150a70251aa12d891b7f863f68ff4bb677e957f90a72c` |
| `log/v1_revision_notes.md` | `44c2a0f44ceb286dfe0016880c65d3527464619830c25f02210f395492575f1f` |
| `evidence/v153/README.md` | `7fc107b5e02a0404165d807b597263c8c5b6fe17bacb7243a49cab0cf749dc07` |
| `evidence/v153/ns46-fine-block-2026-09-22-v1.html` | `f8ccdc12d1e70c13e0d7727f5a295effd17e66b979551ff24e005a9cfa018ca6` |

## Ranked findings

**MAJOR: none.**

**MINOR M1 — resolved: positive-gap scope in integration summaries.**
Earlier map/AGENTS/log/status/board wording omitted the scale of the gap
being excluded. The exact conclusion at `new_section.tex:288` is a ceiling
`gap <= C exp(-lambda²/2000)`, which permits a smaller positive gap. The
final map title and note, `AGENTS.md:89`, both logs at line 12, manuscript
status at line 214, and `NEXT_STEPS.md:78` now specify a uniform or
polynomial positive gap. The map, logs and report explicitly retain the
possibility of a smaller positive gap. The theorem itself did not require
correction. No outstanding actionable finding remains.

**NOTE — the closure is a scoped objective failure.** At
`new_section.tex:280–309`, the result obstructs a uniform or polynomial
positive-coercivity estimate after removing `o(lambda²/log lambda)`
directions. It does not close every positive-gap question, gap-free block
methods, or the complete signed-floor route. At lines 311–327 the missing
uniform signed estimate is explicitly required on the entire form-domain
orthogonal complement, in both parities. Small residuals supply no energy
sign and no complementary lower bound.

## Preservation and mathematical scope

Both reviewed source fragments occur in the new section without any
internal change. The entire new section occurs exactly once, byte for
byte, in the live manuscript. Thus the finite-arc and complete-block
arguments reviewed separately have not lost hypotheses during integration.
The independent `finite_arc_review.md` and `complete_block_review.md`
were inspected; their pinned source hashes agree with this review.

The finite-arc estimate applies to arbitrary complex coefficients and
retains the deteriorating Gram constant. The actual positive Gaussian
source supplies a nonvanishing Fourier arc by continuity; this is an
analytic existence claim, not a certified numerical arc or starting
window. The complete cutoff argument retains all prime rows, both pole
terms, the full uncut tail mass for the Gram loss, and the inverse Gram
factor for arbitrary mixtures. Its vectors lie in the complete operator
domain. No finite compression or quadratic residual is substituted for
the complete operator residual.

The chosen fixed-range lattice gives `m = 2J+1`, where
`J=floor(lambda²/(40000 log lambda))`, and pays the Gram amplification
inside `C exp(-lambda²/2000)`. Exact parity dimensions are `J+1` and `J`.
The actual even source removes at most one even dimension and none in
the odd sector; no unproved source overlap or identification with a
cutoff translate is required. The near-zero spectral count is for the
complete operator and is separate from this source-admissible count.
The dimension argument bounds any coercivity constant on a complement
of codimension less than `m`; it does not determine signs of eigenvalues.

The introduction, new status, README additions, NS-46 board row and log
entries now match these conclusions. The existing gap-free transfer is
credited to v1.18/v1.36 rather than presented as new arithmetic input.
The separately archived fixed-spacing companion is not integrated or
used by this theorem. The v1.53 HTML report was checked for claim scope,
not visual layout; the coordinator owns rendering and packaging.

## Map and build checks

The parsed map contains 57 distinct node IDs, with 22 closed nodes and
exactly one live node, `stepb`. The new closed node `fineradicalrank` is
titled “Uniform or polynomial positive gap after o(lambda²/log lambda)
removed directions”; its note states the exponential ceiling, permits a
smaller positive gap, and leaves the signed floor and gap-free methods
open. Generated map and README diagrams show that same scoped node.

The `circle` node remains `open` with the exact required note:

> measurement lane; closure claims withdrawn after NS-31; geometry and exact identities retained

`git diff --check` passes. The coordinator's final actual build record
reports 269 pages, zero undefined references, zero duplicate references
and zero overfull boxes; its manuscript and section hashes match the
pinned files above. The reviewer inspected that record and independently
checked the source-fragment equality, but did not rerun the build.
Packaging/provenance generation remains the coordinator's responsibility.

## Verdict

The final integration preserves the reviewed analytic result and its
limited closure. M1 is resolved. No new numerical window, effective
finite threshold, energy sign, complementary floor, G2 or RH conclusion
has been introduced by this integration.
