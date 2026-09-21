# Fixed-Space Prime Compatibility

Alexander Eastwood's complete working manuscript, **v1.37**.

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
| Only positive result | `W_4 >= 0`, both parity sectors — evidence restored and verified |
| Certified window | half-width `a = log 4 = 1.386`; 1.73× the published Zhu window, 4× the classical range |
| Live mechanism | signed weighted concentration, even sector (`prop:v131-concentration`) |
| Routes proved closed | 10 |
| Evidence gaps | 2 of 4 tracked groups open — see the ledger |
| G2 | open |
| RH | open, and not claimed |

## Current manuscript

- [Complete LaTeX](manuscript/fixed_space_prime_action_v1.tex)
- [Research log and candidate register](log/RH_G1_G2_research_log.md)
- [Revision notes](log/v1_revision_notes.md)
- [Checksums and provenance](manifest/v1.37_manifest.json)

One live manuscript; delivery is **LaTeX only** at the author's request.
Prior versions are reachable by tag (`v1.24`, `v1.34` … `v1.37`).

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
