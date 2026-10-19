# Audit Package: Analytic Continuity of Legendre Shift & Schur Multiplicity Matrices Across $u=1$ and Extended Four-Prime Horizon up to $a = \frac{1}{2}\log 260$ (`universal-legendre-shift-algebra-and-k4-horizon-2026-10-15-v1`)

> **Wall check**: The Riemann Hypothesis (RH), G2, the cofinal signed-arithmetic lower bound, and both historical missing-original evidence groups in `evidence/MISSING.md` remain **OPEN**.

## Package Overview

- **Package ID**: `universal-legendre-shift-algebra-and-k4-horizon-2026-10-15-v1`
- **Lanes**: `NB-GAIN` / `COEFF` & `NS-61` and `KERNEL-API`
- **Precision**: Two-precision (`256`-bit and `384`-bit) `flint.arb` / `flint.acb` ball arithmetic (`243/243` full-precision string ball overlap checks PASS, zero float tolerances in ball checks, exact `SymReal` symbolic cut partitioning, zero `numpy`/`scipy`/`mpmath` imports).
- **Hashes**:
  - `payload.sha256` = `5b86a9fe9e5631fd947ba7300b671c6f48646161c76fdf562671d6a83b4d8659`
  - `verification.json` `file_sha256` = `ecf82b46dffb127106edb725330e9de6839ce810851c76021e6884a27725add9`
- **Scope Qualification**: Theorem 1 certifies finite-rank $N=4$ Legendre polynomial shift and Schur multiplicity matrices across $u \in (0, 2)$, whereas Theorem 2 certifies full-space $L^2(-b,b)$ Sherman–Morrison trace positivity $\operatorname{Tr}(K_{\mathrm{sherman,even}}) < 1$ and $\operatorname{Tr}(K_{\mathrm{pure,odd}}) < 1$ across the $K=4$ primorial shift horizons up to $a = \frac{1}{2}\log 260$. Untruncated spatial archimedean completion at larger bandwidths $2b \in [\log 2, 1.50]$ is addressed in Milestones 16 and 17.

## Summary of Certified Theorems

1. **Theorem 1 (`NB-GAIN` / `COEFF` & `NS-61` — Global Analyticity of Legendre Shift & Schur Multiplicity Matrices Across $u=1$ and Universal Kernel-Plus-Positive-Definite Structure on $(0, 2)$)**:
   - Establishes that in the parity-adapted Legendre polynomial basis $\{\phi_m(t) = \sqrt{\frac{2m+1}{2}} P_m(t)\}$ on $[-1, 1]$ ($m \equiv n \pmod 2$), both the shift matrix $S_\tau^{(N)}$ and the Universal Schur Multiplicity Matrix $D_\tau^{(N)} = \langle \phi_m, \psi_\tau \phi_n \rangle$ are given by **one single analytic rational polynomial on the entire interval $u \in [0, 2]$** (spanning both the two-sided overlap regime $u \in (0, 1)$ and the single-reflection regime $u \in [1, 2]$) with **zero piecewise branching at $u = 1$**.
   - Certifies the Exact First-Row Polynomial Identity $(D_\tau^{(N)})_{0, 2s} = (S_\tau^{(N)})_{0, 2s}$ for all $s \ge 0$ and all $u \in [0, 2]$, and certifies via exact `flint.arb` Cholesky factorization across 8 points in $(0, 2)$ that $Q_{\tau, +1}^{(4)} = D_\tau^{(4)} + S_\tau^{(4)} \succ 0$ on $\mathbb{R}^4$ and $\widetilde{Q}_{\tau, -1}^{(4)} = (D_\tau^{(4)} - S_\tau^{(4)})_{r,s \in \{1,2,3\}} \succ 0$ on $\mathbb{R}^3$.
2. **Theorem 2 (`KERNEL-API` + `NB-GAIN` — Crossing Four Internal Primorial Shift Horizons for $K=4$ up to $a = \frac{1}{2}\log 260$ and Super-Exponential $N=4$ Gegenbauer–Bessel Completeness)**:
   - Certifies $K = 4$ ($B_{\{2,3,5\},\{7\}}$, $P_4 = 210$) across four internal shift horizons ($\tau_{15/14}, \tau_{8/7}, \tau_{7/6}, \tau_{6/5}$):
     - Up to $N = 245$ ($a = \frac{1}{2}\log 245 \approx 2.750629$, 49 active shifts) at $\Delta_\alpha = 0$ (`tr_sherman = 0.130324 < 1` vs `tr_pure = 1.120435 > 1`),
     - Up to $N = 252$ ($a = \frac{1}{2}\log 252 \approx 2.764715$, 56 active shifts) at $\Delta_\alpha = 0.60$ (`tr_sherman = 0.227137 < 1` vs `tr_pure = 1.387559 > 1`),
     - Up to $N = 260$ ($a = \frac{1}{2}\log 260 \approx 2.780341$, 66 active shifts: 34 two-sided and 32 single-reflection) at $\Delta_\alpha = 1.20$ (`tr_sherman = 0.424192 < 1`, `tr_odd = 0.515452 < 1` vs `tr_pure = 2.292088 > 1`),
     - With $N=4$ Gegenbauer–Spherical-Bessel Parseval tail defect $\varepsilon_4^{\mathrm{even/odd}}(b) \le 2.831 \times 10^{-11}$ across all extended checkpoints.

## Replay Instructions

```bash
pyright audits/universal-legendre-shift-algebra-and-k4-horizon-2026-10-15-v1/verify_universal_legendre_and_k4.py
.venv/bin/python audits/universal-legendre-shift-algebra-and-k4-horizon-2026-10-15-v1/verify_universal_legendre_and_k4.py
```

---

> **Wall check**: The Riemann Hypothesis (RH), G2, the cofinal signed-arithmetic lower bound, and both historical missing-original evidence groups in `evidence/MISSING.md` remain **OPEN**.
