# Fixed-Space Prime Compatibility

Alexander Eastwood's complete working manuscript, **v1.36**.

**G2 and the Riemann Hypothesis remain open.** The new result is a sharper
conditional reduction; its uniform arithmetic hypothesis is unproved.

## Current manuscript

- [Complete LaTeX](fixed_space_prime_action_v1.tex)
- [Research log and candidate register](RH_G1_G2_research_log.md)
- [Revision notes](v1_revision_notes.md)
- [Checksums and provenance](github_sync/v1.36_manifest.json)

There is one live manuscript at the root. Delivery is **LaTeX only** at the
author's request. No new PDFs are generated or distributed going forward.
The previous v1.35 PDF and superseded supporting files are retained only in
the [archive](archive/README.md) and Git history.

## New in v1.36

A single finite constant `C`, independent of the growing window, in the
complete ordinary-norm lower bound `q_a[f] >= -C ||f||^2` suffices for Weil
positivity. The same is true on the complement of the actual source or the
growing radical block when its complete operator residual tends to zero.
Both parity sectors must be controlled; the physical low-concentration
complement is not automatically this complement.

The proof uses density of all real translates of the Gaussian radical. Any
negative compact test would yield arbitrarily negative normalized tests by
subtracting close ordinary-norm radical approximations. Thus the remaining
signed arithmetic estimate may target a uniform **O(1)** negative error;
proving an **o(1)** error is stronger than necessary.

Also proved: the zero-extended complete Weil operators converge strongly in
resolvent to zero, which does not determine their sign. Persistent bounded
positive comparisons are ruled out under the stated domain and compression
hypotheses. Exact positive and negative countermodels delimit these claims.

- [Proof and novelty report](g2_radical_topology/research_report.md)
- [Proof excerpt](g2_radical_topology/new_section.tex)
- [Independent adversarial review](g2_radical_topology/adversarial_review.md)
- [Exact countermodel checks](g2_radical_topology/check_topology_countermodels.py)
- [Check results](g2_radical_topology/countermodel_results.json)

This is a continuation of the radical route, not a new arithmetic positivity
mechanism. Classical ingredients and nearby literature are distinguished in
the report; worldwide novelty is not claimed. No G2 sign gap was closed.

## Saved-copy status

Canonical ChatGPT file replacements for the v1.36 LaTeX, log and notes failed
during transfer. Those saved copies still represent v1.34; use this repository
for the current v1.36 manuscript. No stale saved-file link is labelled v1.36.

## Reproduction archive status

The complete cumulative historical reproduction ZIP remains unavailable.
Older certificate directories are preserved in `archive/v1.24_snapshot/`;
v1.35 proof materials are in `archive/v1.35/`. Current proof materials above
are complete for this update but do not reconstruct the missing archive.
This repository snapshot is not a complete cumulative reproduction release.

## Validation

The new proofs received independent adversarial review. Countermodel
identities were checked with exact rational arithmetic. The complete source
compiled without warnings before the author changed delivery to LaTeX only.
The already generated v1.36 PDF is not part of this published snapshot.
No numerical computation is presented as a proof of an arithmetic sign.
