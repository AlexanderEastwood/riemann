# v1.40 — complete lambda=4 simple even ground

Certified computation and proof for NS-5. The complete operator has a
simple even ground, with 0 < mu0 < 2.454e-75 and mu1 > 1e-73.
Connes–van Suijlekom Theorem 6.1 then gives only real zeros for the entire
Fourier transform of that complete ground. G2 and RH remain open.

Start with [REPRODUCE.md](REPRODUCE.md), then the
[mathematical report](research_report.md) and
[independent adversarial review](adversarial_review.md).

- [Proof source](new_section.tex)
- [Certificate verifier](certify_ground4.py): new gates at 1024 and 1280 bits
- [Independent checker](check_independent.py): exact norms and principal determinants
- [Independent results](independent_checks.json)
- [Build report](build_report.json): 213 pages, zero undefined/duplicate references
- [Manifest](../../manifest/v1.40_manifest.json)

Complete older residual enclosures are reused from evidence/v126/;
these files contain only the new proof, computations, and review.
