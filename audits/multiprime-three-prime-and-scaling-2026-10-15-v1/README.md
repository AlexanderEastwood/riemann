# Milestone 8 Audit Package: `multiprime-three-prime-and-scaling-2026-10-15-v1`

**Date:** 2026-10-15  
**Lanes:** `KERNEL-API`, `ZERO-GEOMETRY`, and `COEFF` / `NB-GAIN` (`NS-61`)  
**Precision:** Two-precision (`256`-bit and `384`-bit) ball arithmetic (`flint.arb`, `64/64` overlap checks PASS, exact `SymReal` endpoints in $\mathbb{Q} \oplus \bigoplus_p \mathbb{Q}\log p$, zero decimal tolerances)  
**Typecheck:** `pyright` clean (`0 errors, 0 warnings, 0 informations`)

> **Wall check:** **RH**, **G2**, the **cofinal signed-arithmetic lower bound**, and **both historical missing-original evidence groups** in `evidence/MISSING.md` remain **OPEN**.

---

## Contents
1. `PROPOSAL.md` — Executive summary, mandatory Wall Check, subspace/horizon qualifications, and statements of Theorems 1–5.
2. `derivation.md` — Complete mathematical proofs of:
   - **Theorem 1 (`KERNEL-API`):** Möbius Parity Coherence & Complete Multi-Prime Tower Collapse for general $K$-prime split-pole preconditioners $L_{\mathcal{P}}$.
   - **Theorem 2 (`KERNEL-API`):** Primorial Balanced-Partition Isometric Horizons $a_{\mathrm{iso}}(K) = \log d_+(K)$ for $K \in \{2, 3, 4\}$ ($\mathcal{P}_2 = \{2, 3\}$, $\mathcal{P}_3 = \{2, 3, 5\}$, $\mathcal{P}_4 = \{2, 3, 5, 7\}$) with zero-minorant continuum certificates on $(\frac{1}{2}\log 6, \log 3]$, $(\frac{1}{2}\log 30, \log 6]$, and $(\frac{1}{2}\log 210, \log 15]$ on $\operatorname{Ran}(B_{\mathcal{P}_{K,+}, \mathcal{P}_{K,-}})$.
   - **Theorem 3 (`KERNEL-API`):** Certified extension of $B_{2,3}$ across $(\frac{1}{2}\log 10, \frac{1}{2}\log 12]$ up to the internal $\log 2$-shift horizon $a = \frac{1}{2}\log 12 = \log(2\sqrt{3}) \approx 1.2424533249$ at $\Delta_\alpha = 3/5 = 0.60$ via Pure-Diagonal + Symmetric/Antisymmetric Reflection Step-Minorants and the 2-Mode Cauchy–Poincaré Second-Eigenvalue Defect Bound (`0` Plancherel vectors, `0` Taylor expansions).
   - **Theorem 4 (`ZERO-GEOMETRY`):** Multi-Order Stieltjes–Hankel Defect & Angle Blind-Cone Elimination covering the entire order-2 blind cone $\phi \in [\pi/6, \pi/2]$ ($\beta \le \sqrt{3}\alpha$).
   - **Theorem 5 (`COEFF` / `NB-GAIN`, `NS-61`):** Gegenbauer–Bessel Finite-$N$ Mellin–Jacobi Completeness & Super-Exponential Tail Decay Bound on $L^2(0, b)$ across $K = 2, 3, 4$.
3. `verify_multiprime_scaling.py` — Two-precision (`256`-bit and `384`-bit) `flint.arb` ball arithmetic verification script with exact `SymReal` endpoints and zero `numpy`/`scipy`/`mpmath` dependencies (`pyright` clean: `0 errors, 0 warnings, 0 informations`).
4. `verification.json` — Certified `256`-bit and `384`-bit numerical output (`payload.sha256=3421d81e7effd58b3512e5e62695d243e6b9ed26e6edede22686b52fbb45b625`, `file_sha256=532bb2c677aee87cbaf71ba4f05db6289786a5a0f8aa69ed5e969b9fa07d4f1b`).

## Reproduction
```bash
pyright audits/multiprime-three-prime-and-scaling-2026-10-15-v1/verify_multiprime_scaling.py
.venv/bin/python audits/multiprime-three-prime-and-scaling-2026-10-15-v1/verify_multiprime_scaling.py
shasum -a 256 audits/multiprime-three-prime-and-scaling-2026-10-15-v1/verification.json
```

## Open-Status Disclosure
**RH**, **G2** (global Weil positivity across all test functions), the **cofinal signed-arithmetic lower bound**, and **both historical missing-original evidence groups** in `evidence/MISSING.md` remain **OPEN**.
