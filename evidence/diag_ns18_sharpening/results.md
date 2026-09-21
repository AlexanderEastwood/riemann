Diagnostic only — not a complete-ground certificate.

The requested target-scale run used the unchanged archived script:

```sh
.venv/bin/python -B evidence/diag_ns2_semantic_lock/reproduce_ccm.py --M 16 --N 120 --bits 1024 --dps 220 --nzeros 1 --K 128 --out evidence/diag_ns18_sharpening/midpoint_M16_N120_b1024.json
```

The midpoint eigensolve suggests an absolute finite-compression discrepancy
about 2.9250414e-71. Its printed root and gamma fields have only 40 digits and
cannot be subtracted to recover that discrepancy. This is only the planning
scale, not a complete-ground result. The finite value is subsequently
certified independently with interval eigenpair/root gates in evidence/v143/.
The complete interval remains symmetric and does not fix the requested sign
or factor-ten magnitude. No new window or tail metric was introduced.
