# Audit Package: Two-Sided Positive-Shift Step-Rank-1 Minorant & Crossing the First Internal Primorial Horizons for $K=3$ and $K=4$ (`three-prime-complete-shift-spectrum-and-horizon-2026-10-15-v1`)

> **Wall check**: The Riemann Hypothesis (RH), G2, the cofinal signed-arithmetic lower bound, and both historical missing-original evidence groups in `evidence/MISSING.md` remain **OPEN**.

## Package Overview

- **Package ID**: `three-prime-complete-shift-spectrum-and-horizon-2026-10-15-v1`
- **Lane**: `KERNEL-API`
- **Precision**: Two-precision (`256`-bit and `384`-bit) `flint.arb` / `flint.acb` ball arithmetic (`91/91` two-precision ball overlap checks PASS, zero float tolerances in ball checks).
- **Hashes**:
  - `payload.sha256` = `18f48ec26ec50f1f5c39c6ffdc4f10f88a1f7f67994854c0c650d0627832e2c7`
  - `verification.json` `file_sha256` = `868a9663bc975d6bd29ff6fe177ed344d7e9530cf89caaf0693792e76f1bdcf2`

## Summary of Certified Theorems

1. **Theorem 1 (`KERNEL-API` — Universal Schur Decomposition, Two-Sided Positive-Shift Step-Rank-1 Minorant, and Single Aggregated Sherman–Morrison Trace Reduction)**:
   - Establishes that for every active shift $\tau_r \in (0, 2b)$ with $c_r > 0$ (across both the two-sided overlap regime $0 < \tau_r < b$ and the single-reflection regime $b \le \tau_r < 2b$), the Schur operator $M_{\tau_r}^+ \succeq 0$ maps $\mathbf{1}_{[-b, b]}$ to $2 c_r \psi_r(x)$, where $\psi_r(x) = \mathbf{1}_{[0, b - \tau_r]}(x) + \mathbf{1}_{[\tau_r - b, b]}(x) \in \mathcal{S}_{\mathrm{step}}$.
   - Summing over all positive shifts $c_r > 0$ yields the exact rank-1 step minorant $M_{\mathrm{pos}}^+ \succeq \frac{2}{S_{\mathrm{pos}}} |\Psi_{\mathrm{pos}}\rangle \langle \Psi_{\mathrm{pos}}|$ with **zero loss on the constant mode $\mathbf{1}_{[0, b]}$**, **zero additional cuts**, and the closed-form Sherman–Morrison trace identity $\operatorname{Tr}(K_{\mathrm{sherman, even}}) = \operatorname{Tr}(K_{\mathrm{pure, even}}) - \frac{(2/S_{\mathrm{pos}}) I_{\mathrm{pos}}}{1 + (2/S_{\mathrm{pos}}) J_{\mathrm{pos}}}$.
2. **Theorem 2 (`KERNEL-API` — Crossing the First Internal Primorial Horizons for $K=3$ and $K=4$ up to the Second Internal Horizons)**:
   - **$K=3$ ($B_{\{2,3\},\{5\}}$) at $\Delta_\alpha = 0$**: Certifies coercivity across $N \in \{36, 37, 38, 39, 40, 41, 42\}$ ($a \in [\log 6, \frac{1}{2}\log 42]$). At $N = 40, 41, 42$ where the pure-diagonal trace fails ($\operatorname{Tr}_{\mathrm{pure}} = 1.030545, 1.467972, 2.400252 > 1$), Theorem 1 certifies $\operatorname{Tr}(K_{\mathrm{sherman, even}}) = 0.458404, 0.530367, 0.626834 < 1$.
   - **$K=3$ ($B_{\{2,3\},\{5\}}$) at $\Delta_\alpha = 3/5 = 0.60$**: Certifies coercivity across $N \in \{42, 43, 44, 45\}$ up to the second internal shift horizon $a = \frac{1}{2}\log 45 = \log(3\sqrt{5})$ ($2b = \log(3/2)$, 18 active shifts), reducing $\operatorname{Tr}_{\mathrm{pure}} = 2.768965 > 1$ at $N=45$ to $\operatorname{Tr}(K_{\mathrm{sherman, even}}) = 0.931891 < 1$.
   - **$K=4$ ($B_{\{2,3,5\},\{7\}}$) at $\Delta_\alpha = 0$**: Certifies coercivity across $N \in \{225, 240\}$ from $a_{\mathrm{iso}}(4) = \log 15$ up to the second internal shift horizon $a = \frac{1}{2}\log 240 = \log(4\sqrt{15})$ ($2b = \log(8/7)$, 43 active shifts), reducing $\operatorname{Tr}_{\mathrm{pure}} = 0.448470$ at $N=240$ by $4.42\times$ to $\operatorname{Tr}(K_{\mathrm{sherman, even}}) = 0.101574 < 1$.

## Replay Instructions

```bash
pyright audits/three-prime-complete-shift-spectrum-and-horizon-2026-10-15-v1/verify_three_prime_complete_spectrum.py
.venv/bin/python audits/three-prime-complete-shift-spectrum-and-horizon-2026-10-15-v1/verify_three_prime_complete_spectrum.py
```

---

> **Wall check**: The Riemann Hypothesis (RH), G2, the cofinal signed-arithmetic lower bound, and both historical missing-original evidence groups in `evidence/MISSING.md` remain **OPEN**.
