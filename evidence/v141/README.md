# v1.41 — CCM semantic lock and centering correction

Certified finite-compression computation at the **existing** lambda=3,
N=120 window, replayed at 768 and 1024 bits. No new window is computed.
G2 and RH remain open.

- `new_section.tex`: exact centering dictionary, certificate and published-window comparison.
- `certify_ccm_semantic_lock.py`: fresh Arb assembly, isolated eigenpairs and interval root gates.
- `ccm_lambda3_N120_b768.json`, `ccm_lambda3_N120_b1024.json`: root brackets and coefficient enclosures.
- `ccm-lambda3-figure.svg`: CCM Figure 1, source: https://arxiv.org/html/2511.22755v1/lambda3.svg ; Alain Connes, Caterina Consani, Henri Moscovici, *Zeta Spectral Triples* (2025), CC BY 4.0 as indicated on the article.
- `requirements.txt`: exact package versions used with Python 3.14.6.

Replay from the repository root:

```
.venv/bin/python evidence/v141/certify_ccm_semantic_lock.py --bits 768
.venv/bin/python evidence/v141/certify_ccm_semantic_lock.py --bits 1024
python3 tools/verify_manifest.py v141
```

Root finding only proposes centers. Acceptance retains all interval errors.
The statements concern unique local roots of the finite compression's ground
transform. They neither enumerate all zeros nor transfer to the complete
ground. NS-14's old script omits the (-1)^n centering phase; its conclusion
is superseded. The original diagnostic is retained as a historical record.


Additional records:

- [Research report](research-report-2026-09-21-v1.html)
- [Build report](build_report.json)
- [Cross-precision comparison](replay_comparison.json)
- [NS-1 availability search](ns1_recovery_status.json)

The original coefficient assembler is SHA-bound in both replay JSON files.
The exact decimal root centers and radii are stored separately from rounded
displays. This pass has no new independent audit; the published CCM values
are the external numerical reference.
