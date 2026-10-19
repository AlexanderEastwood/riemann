# Milestone 17 Audit Package (v2): Infinite-Dimensional High-Mode Operator Lower Bound, Exact Two-Shift Product Defect Algebra, Global Remainder Block-Schur Positivity Certificate on $\mathcal{Q}(A_{\mathrm{arch}}) \subset L^2(-b, b)$, and Matched Davenport–Heilbronn Control Separation

**Date**: 2026-10-15  
**Milestone**: M17 (`infinite-dimensional-tail-floor-and-shift-coupling-defect-2026-10-15-v1`, Revision v2 repaired per `argon-m17-review-2026-10-15-v1`)  
**Lanes**: `WEIL-FLOOR`, `NB-GAIN / COEFF`, and `KERNEL-API`

> **Wall check**: This package does **NOT** prove the Riemann Hypothesis (`RH`), Goal 2 (`G2`), or the cofinal prime-shift lower bound as $a \to \infty$ (or $K \to \infty$). It certifies full-space infinite-dimensional positivity on $\mathcal{Q}(A_{\mathrm{arch}}) \subset L^2(-b, b)$ for $K = 2$ ($\mathcal{P}_2 = \{2, 3\}$) at the **five discrete rational bandwidths** $2b \in \{0.40, 0.42, 0.45, 0.48, 0.50\}$. Both missing-original evidence groups in `evidence/MISSING.md` remain **OPEN**.

---

## Package Contents

- `PROPOSAL.md`: Problem statement, audit directives addressed (`argon-m16-review-2026-10-15-v1` and `argon-m17-review-2026-10-15-v1`), and summary of the four main theorems.
- `derivation.md`: Complete analytic derivations of Theorem 1 (exact two-shift operator product $S_{\tau_1} S_{\tau_2} = S_{\tau_1+\tau_2} + S_{|\tau_2-\tau_1|} - D_{\tau_1,\tau_2}$ and exact finite-rank combined-shift coupling Gram matrix $\mathcal{G}_{\mathrm{comb}, R}^{(N_{\mathrm{leg}}, \mathrm{sector})}(b)$), Theorem 2 (window-localized archimedean frequency splitting, exact holomorphic digamma extension, closed-form Poisson–Bessel tail trace bound, and Laplace–Bessel external kernel enclosure), Theorem 3 (global subtraction $\mathcal{W}_{\mathcal{P}_2}^{\mathrm{full}}(b) \succeq \mathcal{R}_R(b) := \mathcal{W}_{\mathcal{P}_2}^{\mathrm{full}}(b) - \mathcal{A}_{\mathrm{loc}, +, R}(b)$ and full-space Matrix Block-Schur positivity certificate on $\mathcal{Q}(A_{\mathrm{arch}}) \subset L^2(-b, b)$ across the five discrete rational bandwidths $2b \in \{0.40, 0.42, 0.45, 0.48, 0.50\}$), and Theorem 4 (dependency edge `WEIL-FLOOR -> G2` with Stirling rate analysis in $M_0$ and matched Davenport–Heilbronn control separation from `controls/davenport_heilbronn.py`).
- `verify_infinite_tail_floor_and_coupling.py`: Pure `flint.arb` / `flint.acb` dual-precision (`256`-bit and `384`-bit) certificate script (`0 errors, 0 warnings, 0 informations` under `pyright`, zero `numpy` / `mpmath` imports) with full-precision string ball overlap verification (`flint.arb(a["str"])`) and non-overlapping self-test ($1 + 2^{-100}$ vs. $1 + 2^{-101}$).
- `verification.json`: Deterministic certificate output with `446/446` dual-precision full-precision string ball overlap checks passing.

---

## Verification & Cryptographic Hashes

Run from the repository root:

```bash
pyright audits/infinite-dimensional-tail-floor-and-shift-coupling-defect-2026-10-15-v1/verify_infinite_tail_floor_and_coupling.py
.venv/bin/python audits/infinite-dimensional-tail-floor-and-shift-coupling-defect-2026-10-15-v1/verify_infinite_tail_floor_and_coupling.py
```

- **Full-Precision String Ball Overlap Checks (`256`-bit vs. `384`-bit `flint.arb`)**: `446 / 446 PASS`
- **`payload.sha256`**: `ab4ce05962a1692e1c8c967a16b83a4b5f77f707fd1e1e73bdb62a178bd7d1a6`
- **`verification.json` (`file_sha256`)**: `42d1598db4bafc438f0e5a4654327fb5fdb5b6cc1d0ecee91c813677816736aa`

---

> **Wall check**: This package does **NOT** prove `RH`, `G2`, or the cofinal prime-shift lower bound as $a \to \infty$ (or $K \to \infty$). Both missing-original evidence groups in `evidence/MISSING.md` remain **OPEN**.
