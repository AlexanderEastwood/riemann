# Milestone 12 Audit — Ordinate-Centered Stieltjes–Hankel Parity Separation & Davenport–Heilbronn Off-Line Zero Screen (`ZERO-GEOMETRY`)

**Date:** 2026-10-15  
**Target Lane:** `ZERO-GEOMETRY`  
**Audit ID:** `stieltjes-hankel-offline-zero-signal-and-dh-screen-2026-10-15-v1`

---

## Wall Check (Top of Deliverable)

> **Wall check:** Does this audit prove the Riemann Hypothesis (RH), complete the global archimedean completion (G2), establish the cofinal prime-shift lower bound as $a \to \infty$, or recover the missing historical raw outputs in `evidence/MISSING.md`?  
> **No.** RH, G2, the cofinal signed-arithmetic lower bound as $a \to \infty$, and both historical missing-original evidence groups in `evidence/MISSING.md` (`stage4_run_summary.json` / `stage4_Ticks.json` and `certificate.json` / `verify_log.txt`) remain **OPEN**.

---

## Summary of Certified Theorems & Results

### 1. Theorem 1 — Ordinate-Centered Stieltjes–Hankel Parity Separation & Cauchy–Binet Off-Line Zero Dipole Theorem
- **On-Line Hamburger Positivity:** For all zeros on the critical line ($\beta = 1/2$, $\xi_\rho = \gamma \in \mathbb{R}$), the ordinate-centered Gaussian-regularized Hankel matrix $(H_N^{(\sigma)}(t_0))_{j,k} = \mu_{j+k}^{(\sigma)}(t_0) = \sum_\rho (\gamma_\rho - t_0)^{j+k} e^{-\frac{1}{2}\sigma^2(\gamma_\rho - t_0)^2}$ is strictly positive definite for all $t_0 \in \mathbb{R}$ and $\sigma > 0$.
- **Off-Line Dipole Exponential Amplification & Cauchy–Binet Negativity:** At the ordinate $t_0 = \gamma_\star$ of an off-line zero twin pair $\rho_{\star, \pm} = \frac{1}{2} \pm \delta_\star + i\gamma_\star$ ($\delta_\star > 0$), $\xi_{\star, \pm} - \gamma_\star = \mp i\delta_\star \in i\mathbb{R}\setminus\{0\}$, so:
  - Its Gaussian weight is **exponentially amplified** by $e^{+\frac{1}{2}\sigma^2\delta_\star^2} > 1$ while neighboring on-line zeros at distance $|\gamma_n - \gamma_\star| \ge \Delta\gamma$ are **exponentially suppressed** by $e^{-\frac{1}{2}\sigma^2(\Delta\gamma)^2} < 1$.
  - Its contribution to $\mu_2^{(\sigma)}(\gamma_\star) = (H_N^{(\sigma)}(\gamma_\star))_{1,1}$ is strictly negative: $\mu_{2, \mathrm{pair}}^{(\sigma)}(\gamma_\star) = -2\delta_\star^2 e^{+\frac{1}{2}\sigma^2\delta_\star^2} < 0$.
  - Its intrinsic Cauchy–Binet $2 \times 2$ Hankel minor is strictly negative: $w_{\star,+} w_{\star,-}(\xi_{\star,+} - \xi_{\star,-})^2 = -4\delta_\star^2 e^{+\sigma^2\delta_\star^2} < 0$.

### 2. Theorem 2 — 100-Digit Complex Interval Newton Isolation of $\rho_{DH, \pm}$ & Certified Stieltjes–Hankel Screen (`flint.arb` / `flint.acb`)
- **First Davenport–Heilbronn Off-Line Zero Twin Pair (384-Bit & 256-Bit Complex Interval Newton):**
  - $\beta_{DH, +} = 0.8085171824566373855533519606068441278506702683050165728775753009\dots \pm 10^{-100}$
  - $\beta_{DH, -} = 1 - \beta_{DH, +} = 0.1914828175433626144466480393931558721493297316949834271224246990\dots \pm 10^{-100}$
  - $\delta_{DH} = \beta_{DH, +} - \frac{1}{2} = 0.3085171824566373855533519606068441278506702683050165728775753009\dots > 0$
  - $\gamma_{DH} = 85.69934848537759217192926770894172903798782942340757667362756774\dots \pm 10^{-100}$
- **Ordinate-Centered Stieltjes–Hankel Screen at $t_0 = \gamma_{DH} \approx 85.6993484854$:**

| $\sigma$ | Dipole Amplification $e^{+\frac{1}{2}\sigma^2\delta_{DH}^2}$ | $f_{DH}$: $\mu_{2, DH}^{(\sigma)}(\gamma_{DH})$ | $f_{DH}$: $\det H_{2, DH}^{(\sigma)}(\gamma_{DH})$ | $\zeta$: $\mu_{2, \zeta}^{(\sigma)}(\gamma_{DH})$ | $\zeta$: $\det H_{2, \zeta}^{(\sigma)}(\gamma_{DH})$ | $\zeta$: $H_{3, \zeta}^{(\sigma)}(\gamma_{DH}) \succ 0$ |
|---:|---:|---:|---:|---:|---:|---:|
| `1.5` | `1.113022` | **`-0.155261 < 0`** | **`-0.348542 < 0`** | `+0.432482 > 0` | `+0.089563 > 0` | **PASS (Cholesky)** |
| `2.0` | `1.209876` | **`-0.228356 < 0`** | **`-0.552598 < 0`** | `+0.152612 > 0` | `+0.002918 > 0` | **PASS (Cholesky)** |
| `2.5` | `1.346416` | **`-0.256285 < 0`** | **`-0.690133 < 0`** | `+0.051225 > 0` | `+0.000036 > 0` | **PASS (Cholesky)** |
| `3.0` | `1.534681` | **`-0.292151 < 0`** | **`-0.896716 < 0`** | `+0.014209 > 0` | `+8.299e-8 > 0` | **PASS (Cholesky)** |

---

## Reproducibility & Hashes

- **Verifier:** `.venv/bin/python audits/stieltjes-hankel-offline-zero-signal-and-dh-screen-2026-10-15-v1/verify_stieltjes_hankel_offline_screen.py`
- **Two-Precision Ball Overlap Checks (`256` vs `384` bits):** `86 / 86 PASS`
- **Pyright:** `0 errors, 0 warnings, 0 informations`
- **`verification.json` `payload.sha256`:** `5f92799ba267db25456dec483411fc1c3c877840e5395ad01b89656dd02bad59`
- **`verification.json` `file_sha256`:** `f293bb6fb79e01bf5a3c27c1dfdcfe3b3d78efb8aaf1d7879797db284d288deb`

---

## Wall Check (Bottom of Deliverable)

> **Wall check:** Does this audit prove RH, complete G2, establish the cofinal prime-shift lower bound as $a \to \infty$, or recover the missing historical evidence in `evidence/MISSING.md`?  
> **No.** RH, G2, the cofinal signed-arithmetic lower bound as $a \to \infty$, and both missing-original evidence groups in `evidence/MISSING.md` remain **OPEN**.
