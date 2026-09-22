DIAGNOSTIC, NOT A CERTIFICATE.

NS-41 measures odd-sector finite-head weighted-bin feasibility at c'=1 on the existing windows lambda=3,4,6,8. The 256 odd sine modes are automatically orthogonal to the even source. All reported upper witnesses are pure states with each of twenty constraints checked individually on two grids; no mixed/pure equality or energy optimum is claimed.

The user-facing report is [the versioned HTML report](odd-weighted-bin-measurements-2026-09-22-v2.html). Its tables specify each number's scope and direction and print all selected primal and separate dual-eigenvector slacks.

Run from the repository root with the existing virtual environment:

```sh
OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 .venv/bin/python evidence/diag_ns41_odd_feasibility/measure.py 3 4 6 8
OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 .venv/bin/python evidence/diag_ns41_odd_feasibility/refine_energy.py
OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 .venv/bin/python evidence/diag_ns41_odd_feasibility/verify_frozen.py
.venv/bin/python evidence/diag_ns41_odd_feasibility/render_report.py
```

`measure.py` saves interior pure witnesses and a separately labelled float dual. `refine_energy.py` performs a local feasible pure-state improvement at lambda=3,6,8 with all forty grid constraints. Lambda=4 is already below the float energy scale, so no float energy minimization is performed there. Fixed saved vector energies are re-evaluated at 80/120 decimal digits with separate 1024/1280 or 2048/2304-bit assemblies. All are midpoint diagnostics, not ball enclosures.

`verify_frozen.py` evaluates every saved witness directly on both grids without assembling M_b or rerunning the optimizer, and evaluates beta using scipy digamma. The first bin is extended below the original sampled minimum; other edges are frozen. The reference normalization is 800; the deliberately gapped grid covers total interval weight 799.995. No tail completion or tail metric is performed.

No all-Borel WLH, continuum-bin feasibility, cofinal uniformity, positivity, G2 or RH claim follows. The unchanged manuscript build is 246 pages with zero undefined/duplicate references. The inventory records hashes; it is not a certificate.
