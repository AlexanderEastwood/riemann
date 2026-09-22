# v1.52 — NS-43/44/45: scoped closures and remaining estimates

Classification: **exact identities, proved implications with explicit hypotheses,
certified computations, and named open inputs**. No diagnostic is a proof input.
This is a substantive local draft based on PR #20, not a merged or tagged version.
No new window, tail metric, G2 or RH claim.

- `route_selection.tex` is the complete new section, embedded verbatim in the
  self-contained live manuscript. It includes the two new certified propositions,
  fixed and moving prime-channel loss obstructions, the strength check on a
  proposed bump-discrepancy estimate, adaptive concentration equivalence and
  scalar countermodel, and complete CCM selection criteria and scoped obstructions.
- `comparison_replays.tex` gives the two certified statements and their proofs.
- `ns43-route-assessment-2026-09-22-v1.html` gives the versioned route assessment.
- `provenance.json` indexes the new author proofs, independent reviews and all
  external NS-44/45 artifacts by size and SHA256. The v1.52 manifest covers this
  directory; the verifier below checks the external index as well.
- `build_report.json` records the actual integrated build, not source validation.
- `review_record.md` records coordinated reviews and resolved findings.

## Two precise comparison closures

[NS-44](../ns44_metric_replay/) freezes new exact dyadics on indices 17 through 128.
Fresh Arb 320/448-bit gates prove both Weil energies positive, but q/D is below
7e-18 even and 12e-18 odd, contradicting the stipulated 1e-8D lower comparison.

[NS-45](../ns45_block_replay/) uses the first three blocks 26:50, 51:100, 101:200
of the existing lambda=5, N=25 partition. New pair witnesses yield exact comparison
Rayleigh quotients 341/250 and 2093/1500, both greater than one. If positive smaller
metrics exist, their block energies are positive and the norm obstruction applies;
if they do not, the criterion fails its prerequisite. No full-block inertia claim
is needed. Both parities have fresh 320/448-bit and signed-index gates.

The verifiers use the same audited analytic coefficient builder, with fresh empty
caches and enclosed infinite-series remainders. Independent parity/sign assemblies
are not a second analytic derivation of the kernel. Floats only proposed frozen
vectors and are not proof dependencies. Optimized Python that disables assertions
is rejected. These are **new replacement certificates**, not recovered v1.27/v1.28
artifacts. Both historical NS-1 recovery groups remain OPEN in `evidence/MISSING.md`.

## Scope of the analytic work

The full coefficient-one capacity estimate remains open. The new channel theorem
only excludes deleting fixed/sub-endpoint prime channels while retaining the
specified Gaussian weight and the other signed terms. The restricted bump input
is not proved and, for the exhibited probe, would already exclude off-line zeros.

The complete unrestricted adaptive operator hierarchy is equivalent to the same
complement-floor target. Its compactness proof is at each fixed physical window;
it gives no effective number of levels or new arithmetic estimate. Scalar set
extrema fail in an exact nonarithmetic countermodel; no actual Paley–Wiener or
zeta-field nonimplication is claimed. QG plus its separate packet input concerns
bounded-complexity obstruction, not positivity.

CCM needs a complete relative separator/selection estimate plus entire-transform
control. The absolute-residual countermodel is explicitly abstract and is not
support-consistent arithmetic. The coarse rescaled limit theorem explicitly uses
the full both-parity Weil form; finer scales remain open. CCM step (b) is the sole
gold node and circle retains its exact open measurement-lane note.

## Checks and reproduction

From the repository root:

```sh
.venv/bin/python evidence/ns44_metric_replay/replay.py --verify
.venv/bin/python evidence/ns45_block_replay/replay.py --verify
python3 evidence/v152/verify_artifacts.py
python3 tools/verify_manifest.py v152
./manuscript/build.sh
```

Replay uses the frozen witnesses; do not overwrite them with new proposals.
The review and build record state which checks were independently repeated.
Earlier v1.50/v1.51 manifests remain unchanged. Existing PRs #18–20 remain open.
