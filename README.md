# Fixed-Space Prime Compatibility

Alexander Eastwood's complete working manuscript, **v1.34 (192 pages)**.

**G2 and the Riemann Hypothesis remain open.** This repository records proved reductions, scoped certificates, failed approaches, and unresolved obligations; it does not claim an RH proof.

## Current manuscript

- [Complete PDF](fixed_space_prime_action_v1.pdf)
- [Complete LaTeX source](fixed_space_prime_action_v1.tex)
- [Research log and candidate register](RH_G1_G2_research_log.md)
- [Revision notes](v1_revision_notes.md)
- [Snapshot checksums and provenance](github_sync/v1.34_manifest.json)

The PDF in this commit was rebuilt from the unchanged saved v1.34 LaTeX source. It compiles cleanly to 192 pages and was visually checked. It is not a byte-for-byte copy of the saved signed PDF.

## Reproduction archive status

**The full v1.34 cumulative reproduction archive has not yet been uploaded.** Its download returned a temporary server error. The existing certificate directories and historical files from the repository's v1.24 snapshot are preserved, but they are not the complete v1.34 evidence archive. Do not treat this manuscript sync as a complete reproduction release.

The 207,224,098-byte cumulative ZIP is intended for a GitHub release attachment, not an ordinary Git blob. Its pending status is recorded in the snapshot manifest.

## Build

With a suitable TeX Live installation and latexmk:

```bash
latexmk -pdf -interaction=nonstopmode -halt-on-error fixed_space_prime_action_v1.tex
```

Generated PDF bytes can vary with build timestamps and provenance metadata. Source hashes and provenance are recorded in the manifest. This sync made no mathematical changes and performed no new mathematical certification.
