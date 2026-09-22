# NS-40 source and integration notes (internal working record)

Owner: Astra-2. Read on 2026-09-21 America/Los_Angeles (2026-09-22 UTC).
Analytic assessment and proofs; no numerical or certified-computation claim.
Outcome: the prescribed arithmetic QG input remains unresolved. No strength
relative to RH and no logical independence are established.

## Primary sources checked

| Source | Exact version/location used | URL |
|---|---|---|
| Hasanalizade, Shen, Wong | arXiv:2107.06506v1, Corollary 1.2 (printed p. 2); journal citation already in manuscript | https://arxiv.org/abs/2107.06506v1 |
| Chourasiya, Simonič | arXiv:2507.15184v2, Introduction and Corollary 1, equation (3); original Ingham formula also recorded in its abstract | https://arxiv.org/html/2507.15184v2 |
| Ingham | QJMath 11 (1940), 201–202; original DOI metadata retained, theorem checked through the preceding primary research paper (DOI full text unavailable in this session) | https://doi.org/10.1093/qmath/os-11.1.201 |
| Aryan | arXiv:1902.05473v1, Introduction (1.1), printed p. 1; use only its stated integer-x Landau–Gonek formula | https://arxiv.org/pdf/1902.05473v1 |
| Montgomery | original author-hosted paper, Section 1, theorem (2), pp. 181–182 | https://websites.umich.edu/~hlm/paircor1.pdf |
| Baluyot, Goldston, Suriajaya, Turnage-Butterbaugh | arXiv:2501.14545v3, Section 3, MT (3.1)–(3.2) and correction immediately following | https://arxiv.org/html/2501.14545v3 |

The BGSTB v3 version is pinned deliberately. A preliminary read of v1 led
to the correction; the delivered formula and section numbering were then
checked against v3. The older Acta Arith. theorem remains an inherited
bibliographic item, but NS-40 uses the corrected source. No direct quotations
or third-party full-text copies are archived.

## Integration

- `qg_zero_field.tex`: ready-to-include subsection using the existing preamble.
  Suggested position: after the NS-32/33 subsection, coordinated with NS-39.
- `bibliography_additions.tex`: append inside the existing `thebibliography`.
  The five other citation keys are already defined in v1.50; do not duplicate.
- All new labels and the new citation key begin `ns40-`.
- NS-39 separately discusses the basic cutoff upper bound. Its coordinator
  can cite `ns40-prop-cutoff` instead of repeating the argument. No live
  manuscript/map integration is performed on this branch.
- User-facing assessment: `audits/ns40-qg-zero-field-2026-09-21-v1.html`.
- Claim commit: `2cf5e44` (originally `cde749c` before rebasing);
  initial integration base: `01f68b8` (v1.50), refreshed to `a0e916a`.

## Checks

The actual `./manuscript/build.sh` at the v1.50 baseline produced 246 pages
and 0 undefined/duplicate references. `python3 tools/verify_manifest.py v150`
reported 6 ok, 0 relocated/missing/mismatched.

A temporary copy of the same manuscript was created outside the tracked
worktree, with a clear page followed by the fragment immediately before
`thebibliography`, and the new bibliography item immediately before its
closing command. The same `./manuscript/build.sh` produced 250 pages,
0 undefined/duplicate references, and 0 overfull boxes. The appended position
is a build harness only, not the proposed live location or a new release.

The fragment's mathematical arguments are analytic proofs. A successful
TeX build checks typesetting/references, not their truth. No computational
certificate or two-precision numerical claim is involved.

Independent bounded read-only review by Astra (the NS-34 author) found no
MAJOR/MINOR issue in the separated-band proof, weak-limit corollary, cutoff
bound/scaling/rule, prefix-transfer lemma, or claim scope. The reviewer also
checked the new BGSTB v3 citation directly. The review was pinned to:

- `qg_zero_field.tex`: `284279e6906060ff40f5fce4291103dd04ce73d3e2773a10fc81ad6d90c02485`
- `bibliography_additions.tex`: `0626dc46df3c2753e5005ef338441e313dd8e8ec0075f0e7f1c29839c2ffe4a5`

The remaining classical citation checks, build, and report were Astra-2's
responsibility. The reviewer made no file edits and ran no numerical work.

`SHA256SUMS` inventories the fragment, bibliography, these notes, and the
HTML assessment. It is an incremental NS-40 inventory, not a replacement
for any released version manifest. Verify from repository root with
`shasum -a 256 -c evidence/ns40_qg/SHA256SUMS`.
