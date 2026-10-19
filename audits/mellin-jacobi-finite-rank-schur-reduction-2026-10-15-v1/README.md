# Milestone 11 Audit — Mellin–Jacobi–Legendre Finite-Rank Gram–Schur Reduction & Exact Polynomial Shift Matrices (`NB-GAIN` / `COEFF` & `NS-61`)

**Date:** 2026-10-15  
**Target Lanes:** `NB-GAIN`, `COEFF`, `NS-61`  
**Audit ID:** `mellin-jacobi-finite-rank-schur-reduction-2026-10-15-v1`

---

## Wall Check (Top of Deliverable)

> **Wall check:** Does this audit prove the Riemann Hypothesis (RH), complete the global archimedean completion (G2), establish the cofinal prime-shift lower bound as $a \to \infty$, or recover the missing historical raw outputs in `evidence/MISSING.md`?  
> **No.** RH, G2, the cofinal signed-arithmetic lower bound as $a \to \infty$, and both historical missing-original evidence groups in `evidence/MISSING.md` (`stage4_run_summary.json` / `stage4_Ticks.json` and `certificate.json` / `verify_log.txt`) remain **OPEN**.

---

## Summary of Certified Theorems & Results

### 1. Theorem 1 — Gegenbauer–Spherical-Bessel Parseval Identity & Finite-$N$ Archimedean Tail Reduction
- **Exact Parity-Split Gegenbauer Parseval Identities:** For all $z \in \mathbb{C}$,
  $$\sum_{r=0}^\infty (4r+1) j_{2r}(z)^2 = \frac{1}{2}\bigl(1 + \operatorname{sinc}(2z)\bigr), \qquad \sum_{r=0}^\infty (4r+3) j_{2r+1}(z)^2 = \frac{1}{2}\bigl(1 - \operatorname{sinc}(2z)\bigr).$$
- **Super-Exponential Mode Concentration ($N = 1, 2, 3, 4$, 384-Bit & 256-Bit `flint.arb`):**

| Checkpoint | $b$ | $\Delta_\alpha$ | $\varepsilon_2^{\mathrm{even}}$ ($N=2$) | $\varepsilon_3^{\mathrm{even}}$ ($N=3$) | $\varepsilon_4^{\mathrm{even}}$ ($N=4$) | $N=4$ Captured Fraction | $\|K_{\mathrm{even}}\|_{\mathrm{op}}$ ($N=4$) vs Trace |
|---|---:|---:|---:|---:|---:|---:|---:|
| $K=2$ ($b_{\mathrm{iso}}(2) = \frac{1}{2}\log(3/2)$) | `0.202733` | `0.0` | `1.133e-6` | `6.431e-11` | `1.472e-15` | `0.9999999999999987` | `0.575342` < `0.576109` |
| $K=3$ ($b_{\mathrm{iso}}(3) = \frac{1}{2}\log(6/5)$) | `0.091161` | `0.0` | `8.560e-10` | `2.644e-15` | `3.054e-21` | `0.999999999999999999996` | `0.171908` < `0.171915` |
| $K=4$ ($b_{\mathrm{iso}}(4) = \frac{1}{2}\log(15/14)$) | `0.034496` | `0.0` | `1.908e-13` | `1.185e-20` | `<= 6.924e-24` | `1.000000000000000000000` | `0.050907` < `0.050907` |
| $K=2$ ($a = \frac{1}{2}\log 12$, $b = \frac{1}{2}\log 2$) | `0.346574` | `0.6` | `4.813e-3` | `3.610e-5` | `1.086e-7` | `0.9999999645` | `0.904612` < `0.949587` |

### 2. Theorem 2 — Exact Rational Polynomial Shift Matrices $S_\tau^{(N)}$ & Legendre–Schur Reflection Projection Minorant
- **Closed-Form Rational Polynomial Identities in $u = \tau/b \in [0, 2]$:**
  $$\bigl(S_\tau\bigr)_{0,0} = 2 - u, \qquad \bigl(S_\tau\bigr)_{0,2} = -\frac{\sqrt{5}}{2}u(u-1)(u-2), \qquad \bigl(S_\tau\bigr)_{2,2} = 2 - 5u + \frac{5}{2}u^3 - \frac{3}{8}u^5,$$
  $$\bigl(S_\tau\bigr)_{1,1} = 2 - 3u + \frac{1}{2}u^3, \qquad \bigl(S_\tau\bigr)_{1,3} = \sqrt{21}\left(-u + \frac{5}{2}u^2 - \frac{3}{2}u^3 + \frac{1}{8}u^5\right), \qquad \bigl(S_\tau\bigr)_{3,3} = 2 - 7u + 7u^3 - \frac{21}{8}u^5 + \frac{5}{16}u^7.$$
  Verified against symbolic Bonnet–Legendre polynomial integration at $u \in \{1/5, 1/2, 1, 7/5, 9/5\}$ with zero discrepancy inside $10^{-77}$ (256-bit) and $10^{-113}$ (384-bit) balls.
- **Legendre–Schur Reflection Projection Gram Matrix $Q_{\tau, +1}^{(N)} \succ 0$:**
  At $b = 1/4, \tau_{3/2} = \log(3/2)$ ($u \approx 1.621860$), the $3 \times 3$ and $4 \times 4$ Legendre reflection projection Gram matrices $Q_{\tau, +1}^{(N)} = \frac{1}{2}(D_\tau^{(N)} + \frac{1}{2}S_\tau^{(N)})$ are certified strictly positive definite in `flint.arb` with Cholesky pivots `0.532545`, `0.183567`, `0.194450`, and `0.072220`.

---

## Reproducibility & Hashes

- **Verifier:** `.venv/bin/python audits/mellin-jacobi-finite-rank-schur-reduction-2026-10-15-v1/verify_mellin_jacobi_schur_reduction.py`
- **Two-Precision Ball Overlap Checks (`256` vs `384` bits):** `40 / 40 PASS`
- **Pyright:** `0 errors, 0 warnings, 0 informations`
- **`verification.json` `payload.sha256`:** `f9f077b3c599f4d7c52c56635aadca81a4e388820bae032355f5af8113d9e0cc`
- **`verification.json` `file_sha256`:** `99d7b549efb7849fdc729a9c24b265ba250bba76a5976cac0bce982dfc390588`

---

## Wall Check (Bottom of Deliverable)

> **Wall check:** Does this audit prove RH, complete G2, establish the cofinal prime-shift lower bound as $a \to \infty$, or recover the missing historical evidence in `evidence/MISSING.md`?  
> **No.** RH, G2, the cofinal signed-arithmetic lower bound as $a \to \infty$, and both missing-original evidence groups in `evidence/MISSING.md` remain **OPEN**.
