# Fixed-Space Prime Compatibility

Alexander Eastwood's complete working manuscript, **v1.35 (195 pages)**.

**G2 and the Riemann Hypothesis remain open.** No sign is inferred from the
new near-zero spectral count.

## Current manuscript

- [Complete PDF](fixed_space_prime_action_v1.pdf)
- [Complete LaTeX](fixed_space_prime_action_v1.tex)
- [Research log and candidate register](RH_G1_G2_research_log.md)
- [Revision notes](v1_revision_notes.md)
- [Checksums and provenance](github_sync/v1.35_manifest.json)

## New in v1.35

A uniformly conditioned physical lattice of translated radical sources gives
an ordinary operator-residual bound `C log(lambda) exp(-lambda/100)` on a
block of dimension proportional to `log(lambda)`. An odd subblock survives
removal of any number of even image columns. This rules out positive
uniform/polynomial gaps on the specified complements; it does not establish
the asymptotic nonnegativity required by G2.

The exact continuum symbol now covers both complex parity sectors. Their
signed concentration estimates remain unproved.

- [Proof and novelty report](g2_growing_radical/research_report.md)
- [Proof excerpt](g2_growing_radical/new_section.tex)
- [Independent adversarial review](g2_growing_radical/adversarial_review.md)
- [Diagnostic script](g2_growing_radical/check_growing_radical.py)

The radical construction is classical. This is a quantified continuation of
the earlier fixed-rank obstruction, not a newly claimed positivity mechanism
or a worldwide novelty claim. Diagnostics are not interval certificates.

## Saved-copy status

The canonical ChatGPT file replacements for v1.35 failed during byte transfer.
Those stable download links still identify v1.34; the validated v1.35 snapshot
is available from this repository. No Library version number was advanced or
invented, and the previous files were not overwritten by partial data.

## Reproduction archive status

**The full v1.34 cumulative reproduction archive remains unavailable.** Its
download returned a temporary server error. Older certificate directories
from the repository's v1.24 snapshot are preserved. The v1.35 proof materials
above are complete for this update, but do not reconstruct the missing
historical archive. This is not a complete cumulative reproduction release.

## Build

```bash
latexmk -pdf -interaction=nonstopmode -halt-on-error fixed_space_prime_action_v1.tex
```

The complete PDF was rebuilt, compiled without warnings and visually checked.
PDF bytes may vary with build timestamps. Source and artifact hashes are
recorded in the manifest.
