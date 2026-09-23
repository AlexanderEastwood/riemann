# v1.59 local checkpoint — NS-60–66

RH, G2, the original Weil floor and the optimized NB correlation input remain open.
This version is a local draft on top of the unpublished v1.58 checkpoint.
Version numbering and integration must be rechecked before publication.

## Results and scope

- **Exact identities / proved implications:** explicit Euler-grid correction
  with every mixed term; fixed smoothed NB criterion; positive adjacent
  averages; raw trace at most `3*kappa/(8*N^2)`; full projected gain;
  endpoint correlation formula and complete remainder.
- **Scoped proved exclusions:** uniform logarithmic norms for the specified
  Euler correction with sublinear-power grid product; full canonical sharp
  Mobius sequence after Mellin smoothing; the nonnegative smoothed-difference
  coefficient cone; using relative convergence in a changing smoothing norm
  as an RH test. Optimal coefficients and selected canonical subsequences are
  outside the sharp-sequence exclusion.
- **Certified finite computations:** complete q=2 Grams through index 64,
  with a proved Bernoulli/Hurwitz remainder; 256/384-bit replays, doubled
  series cutoff, independent positive-cell integrals; a separate one-atom
  changing-norm control with complete quadrature tails.
- **Open input:** a cofinal lower contraction estimate for the actual optimized
  residual in one fixed smoothing norm. Neither a small finite error nor the
  positive shapes of the atoms supplies this estimate.

`proof.tex` is integrated verbatim in the live manuscript. Its components are
in `ns60/` through `ns66/`. The diagnostic scans remain separately
labelled in `../diag_ns60_nb_corrections/` and `../diag_ns61_smoothed_nb/`.
No diagnostic truncation enters a proof or an interval gate.

## Replay

From the repository root, with the configured Python environment. The
certified Python dependency is pinned in `requirements-replay.txt`; optional
diagnostic packages are separately pinned in `requirements-diagnostics.txt`.
The exact tested runtime versions are in `runtime-provenance.json`.

Replay commands:

```sh
PYTHONDONTWRITEBYTECODE=1 python evidence/v159/ns61/certify_smoothed.py --bits 256 --output /tmp/smoothed-256.json
PYTHONDONTWRITEBYTECODE=1 python evidence/v159/ns61/certify_smoothed.py --bits 384 --output /tmp/smoothed-384.json
PYTHONDONTWRITEBYTECODE=1 python evidence/v159/ns61/certify_smoothed.py --bits 256 --cutoff 256 --output /tmp/smoothed-cutoff256.json
PYTHONDONTWRITEBYTECODE=1 python evidence/v159/ns61/check_physical_gram.py --bits 256 --output /tmp/physical-256.json
PYTHONDONTWRITEBYTECODE=1 python evidence/v159/ns61/check_physical_gram.py --bits 384 --output /tmp/physical-384.json
PYTHONDONTWRITEBYTECODE=1 python evidence/v159/ns61/verify_replays.py
PYTHONDONTWRITEBYTECODE=1 python evidence/v159/ns63/certify_one_atom.py --bits 256 --output /tmp/one-atom-256.json
PYTHONDONTWRITEBYTECODE=1 python evidence/v159/ns63/certify_one_atom.py --bits 384 --output /tmp/one-atom-384.json
PYTHONDONTWRITEBYTECODE=1 python evidence/v159/ns63/check_q2_anchor.py --bits 256 --output /tmp/anchor-256.json
PYTHONDONTWRITEBYTECODE=1 python evidence/v159/ns63/check_q2_anchor.py --bits 384 --output /tmp/anchor-384.json
PYTHONDONTWRITEBYTECODE=1 python evidence/v159/ns63/verify_replays.py
PYTHONDONTWRITEBYTECODE=1 python evidence/v159/ns64/certify_separator.py --bits 256 --output /tmp/separator-256.json
PYTHONDONTWRITEBYTECODE=1 python evidence/v159/ns64/certify_separator.py --bits 384 --output /tmp/separator-384.json
PYTHONDONTWRITEBYTECODE=1 python evidence/v159/ns64/verify_replays.py
maxima --very-quiet -b evidence/v159/ns66/exact-checks.mac
maxima --very-quiet -b evidence/v159/ns65/exact-checks.mac
maxima --very-quiet -b evidence/v159/ns64/exact-checks.mac
maxima --very-quiet -b evidence/v159/ns60/exact-checks.mac
maxima --very-quiet -b evidence/v159/ns61/exact-checks.mac
maxima --very-quiet -b evidence/v159/ns62/exact-checks.mac
maxima --very-quiet -b evidence/v159/ns63/exact-checks.mac
./manuscript/build.sh
python tools/verify_manifest.py v159
```

The verifier checks the saved outputs and their source hashes; to audit a
fresh run, compare its enclosures with the saved JSONs. All matrix solves
use Arb's certified preconditioned algorithm. No `approx` solve or midpoint
inversion is used. The physical-integral and one-atom quadrature checks include
the full omitted interval to infinity.

The HTML report and local self-review are the readable entry points. No
independent review is claimed. The evidence is incremental, not a cumulative
bundle of previous releases.

The q=2 anchor compares the one-atom Mellin quadrature with the separate
Gram/load formula at both precisions. Its r=1 tail is deliberately coarse;
it checks normalization and is not used for the high-accuracy finite claims.

NS-64 supplies the explicit dual separator for the nonnegative coefficient
cone. Its complete six-function local Gram includes the entire x>1 tail
exactly. The local cone distance is attained and is a lower bound for the
full-space cone distance, with no equality claim for the latter. The current
readable report and self-review are the v2 HTML files; v1 files preserve
the earlier checkpoint before this quantitative witness.

NS-65 excludes fixed ordinary Cesaro iterates of the canonical sharp rule.
NS-66 supplies its weaker fixed-order norm-growth criterion: the exponent
is exactly beta_star-1/2. A direct subpolynomial bound or bounded cofinal
subsequence is a new stated open target, not a bound established here.
The analytic implications are separate from their finite exact checks.
