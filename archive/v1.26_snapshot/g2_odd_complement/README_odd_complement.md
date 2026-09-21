# v1.26: complete positivity at lambda = 4

This checkpoint proves the remaining **complete odd-sector sign** at lambda = 4. Combined with the previously certified complete even sector, the full closed Weil form is positive and its fixed-window negative error is exactly zero. It does not prove G2 or RH and supplies no growing-window estimate.

The successful proof uses:

1. The old frozen sixteen-column odd trial, support 4096, with positive trial energy K and exact complete correction C = r* T^-1 r.
2. An exact dyadic direction v and an outward certificate C <= (1/1000) K on its entire fifteen-dimensional K-orthogonal complement.
3. A new frozen single-direction trial, support 8192, with exactly the same physical head Vv. Its complete Schur lower bound is greater than (429/1000) v*Kv.
4. PSD Cauchy--Schwarz, which proves the simultaneous inequality S >= (107/250) K. Positive complete tail and the existing even certificate give the full form sign.

All omitted residual rows after J = 65536 are bounded by the order-64 moment majorant. The inner odd factors have N = 1536, solve support 2048 and mu = 0.9999999999. They are specific to lambda = 4.

## Replay

Keep this folder alongside the cumulative bundle's `g2_low_schur`, `g2_weighted_signed` and other historical support folders. Use Python with python-flint, NumPy and the dependencies of `assembly_general.py`.

Run from this folder:

```bash
python direction_complement_certificate.py
python directional_tail_repair.py --mode verify --M 8192 --steps 24 --bits 1024
python directional_tail_repair.py --mode verify --M 8192 --steps 24 --bits 1280
python certify_odd_full_window.py
```

These commands use the supplied exact frozen witnesses; do not regenerate candidates when replaying their hashes. Candidate generation is optional proposal work and is not a proof step. The combined certificate independently checks the same physical head using Python Fraction and recomputes both complete directional bounds.

The old complete residual ingredients were reconstructed at 768 bits. The optional complement replay at 896 bits reuses those interval enclosures. The new scalar residual is reconstructed at 1024 and 1280 bits; its inner remote upper bound remains the valid archived 768-bit enclosure. No fresh reconstruction of all old inner ingredients is implied.

`rank_one_trial.py` and the s32 reports describe the earlier unsuccessful support-4096 repair. The s32 filename does not mean 32 steps per column: it records 16 initial steps per column plus a single-direction 16-step repair, followed by rounding. Its complete Young and joint-Gram bounds remain inconclusive. They are retained for research history, not used as positive sign gates. The s32 witness also stores the exact direction used by the successful proof.

`quantify_head_error.py` records the intermediate full-form lower error 1e-43, superseded here by the exact sign. Numerical LDL pivots and the relative margin 0.428 are not ordinary full-operator eigenvalue gaps.

The full manuscript proves a further localized-error criterion for future windows, retaining the physical normalization factor. Its cofinal decay is unproved.
