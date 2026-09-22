# NS-54 / Astra-2 verification record

Date: 2026-09-22 UTC. Analytic work only; no new numerical window, tail metric, interval gate, or certified arithmetic distribution.

## Frozen ownership and provenance

- Team base: `f0178e0`; standalone joint task claim: `ccd722bf2b0e6fd6f0133f5b9220fed130b2c325`.
- Owned output: `evidence/ns54_zero_picture/selberg/` only.
- Proof/assessment supplied for independent review with SHA256 `f9f4c43f07c768f32df09df7aa472149a1d4d1220ce6c3ea4dbc30ae99c87b3d`; unchanged after dispatch.
- No edits to the board, research map, live manuscript, another author's files, or Git history. No commit or push by Astra-2.
- External citations are primary author papers. `sources.md` records theorem numbers, page locations and hypotheses. A later independent review, if received, is to be archived separately by the integrating author; this record does not claim that review has passed.

## Actual builds

Temporary directory: `/private/tmp/riemann-ns54-selberg-preview/`.

1. Copied the pinned live `.tex` and its unchanged `manuscript/build.sh`, then ran `./manuscript/build.sh`. Result: **269 pages; zero undefined/duplicate references**.
2. Inserted `selberg_qg_assessment.tex` immediately before the temporary copy's bibliography and appended `bibliography_additions.tex` inside it. Ran the same build script. Result: **273 pages; zero undefined/duplicate references; zero overfull boxes**. No LaTeX error or undefined control sequence was found in the final log.

The second build is a temporary integration test, not a change to the live manuscript or a new manuscript version. Its bibliography and cross-reference checks pass against the stated base. Temporary compiler outputs are not archived as research evidence.

## Analytical verification

- Differentiating `V_x` gives the exact negative cosine prime term with coefficient `-2`; the continuum term has sign `+2I_x`.
- Fixed-window covariance calculation uses distinct positive frequencies and has constants dependent on the fixed window; no interchange with a growing-window limit.
- Quantitative transfer restores CDF error, centering, scale, exceptional mass and the prescribed uniform observation measure.
- Anchored-grid proof accommodates nonattainment of the infimum, at-most-K grids and atoms of the limiting law; it uses open intervals with positive limiting mass, not moment convergence.
- Global depth divided by scale diverges under the full unbounded-left limit. Tightness then contradicts any fixed-positive-fraction ZLD. This is a conditional deduction, not arithmetic ZLD refutation.
- Packet domination and bounded original energy remain separate. The actual arithmetic Gaussian law and necessary uniform remainder are not supplied.

## HTML verification

`ns54-selberg-qg-review-2026-09-22-v1.html` is a separately versioned styled document, Georgia body, approximately 680px content width, inline CSS only. Opened in the in-app browser and visually checked at its narrow viewport, including the conditional theorem box. Formula subscripts and all conclusion lines are readable without horizontal clipping. The tab is retained as a deliverable.

This directory's `SHA256SUMS` pins the five author artifacts using repository-relative paths. The integrating author owns any release manifest and final merged-state build.
