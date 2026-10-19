# Audit Package: `multiprime-euler-preconditioner-2026-10-15-v1` (Audit-Repaired v2)

**Date:** 2026-10-15  
**Lane:** `KERNEL-API`  
**Precision:** Two-precision (`256`-bit and `384`-bit) ball arithmetic (`flint.arb`, `110/110` overlap checks PASS, exact `SymReal` endpoints in $\mathbb{Q} \oplus \bigoplus_p \mathbb{Q}\log p$, zero decimal tolerances)  
**Verification Artifact:** `verification.json` (`payload.sha256=8936cf81aed7b1572a5eb738e303ed3463168324ab6dcffe1a71d8c88ece2561`, `file_sha256=e9f1257bbc431d9d8c4f898bf050526c998cfbb6c8f8c2d2a02e5d59f29caea6`)  
**Typecheck:** `pyright` clean (`0 errors, 0 warnings, 0 informations`)

> **Wall check:** **RH**, **G2**, the **cofinal signed-arithmetic lower bound**, and **both historical missing-original evidence groups** in `evidence/MISSING.md` remain **OPEN**.

---

## 1. Contents & Audit Repairs (`argon-multiprime-review-2026-10-15-v1` & `argon-m9-campaign-review-2026-10-15-v1`)

All findings from the external reviews `argon-multiprime-review-2026-10-15-v1/verification.json` and `argon-m9-campaign-review-2026-10-15-v1/verification.json` have been incorporated and verified:
1. **`precision`, `remaining_tolerance_logic`, & `repair_inventory` (`verify_multiprime_euler.py`):** Replaced `arb_min` and `arb_max` with exact algebraic ball operations `0.5*(a + b -/+ abs(a - b))` (improving `lambda_min_P0` radii from `~1e-16` to `9.46e-115`), replaced all decimal endpoint tolerances (including `1e-100`) with exact symbolic endpoint representation `SymReal` in $\mathbb{Q} \oplus \bigoplus_p \mathbb{Q}\log p$ (certified by the Fundamental Theorem of Arithmetic and Hermite–Lindemann theorem so exact inputs `0` and `10^-101` remain strictly separated), replaced heuristic `rad_xi0 * 10` root-endpoint padding with rigorous ball evaluation `|F(acb(xi0))| * rad(xi0)`, and archived the full two-precision (`256`-bit and `384`-bit) replay comparison (`110/110` overlap checks PASS) in `verification.json`.
2. **`range` (`PROPOSAL.md`, `derivation.md`):** Explicitly qualified that $f = B_{\mathcal{P}_+, \mathcal{P}_-} h$ ranges over the multi-prime Euler-filtered subspace $\operatorname{Ran}(B_{\mathcal{P}_+, \mathcal{P}_-}) \subsetneq L^2_{\mathrm{pole\text{-}free}}(-a, a)$ and that transferring positivity from $\operatorname{Ran}(B_{\mathcal{P}_+, \mathcal{P}_-})$ to the full pole-free window requires a density/transfer theorem (which remains **OPEN**).
3. **`diagonal` (`PROPOSAL.md`, `derivation.md`, `verify_multiprime_euler.py`):** Clarified $C_{\mathrm{zero}}(\mathcal{P}) = \prod_{p \in \mathcal{P}}(1 + p^{-1})$ as the zero-translation coefficient $[I]L_{\mathcal{P}}$ (which equals the compression isometry constant when $2b_{\mathcal{P}} \le \tau_{\mathrm{iso}}(\mathcal{P})$) and documented that on $L^2(\mathbb{R})$ without spatial truncation $P_{b_{\mathcal{P}}}$, $\sigma_{L_{\mathcal{P}}}(0)\sum_{p \in \mathcal{P}} W_p(0) < 0$.
4. **`horizon` (`PROPOSAL.md`):** Compared the filtered-subspace horizons ($a = \frac{1}{2}\log 10 \approx 1.151293$ here, extended in Milestone 8 to $a = \frac{1}{2}\log 12 \approx 1.242453$ for $B_{2,3}$, $a = \log 6 \approx 1.791759$ for $K=3$, and $a = \log 15 \approx 2.708050$ for $K=4$) against the fixed-window complete $\lambda = 4$ full-space horizon $a = \log 4 \approx 1.386294$.
5. **`parity` (`derivation.md`):** Explicitly stated the self-adjoint, parity-preserving hypothesis on $W$ and included the window projection $P_{b_{\mathcal{P}}}$ on $L^2(-b_{\mathcal{P}}, b_{\mathcal{P}})$.
6. **`orthogonality` (`derivation.md`):** Clarified that the step vectors are pairwise orthogonal *within* each of the 4 positive operator families, and that cross-family inner products are inverted jointly and exactly by the full $M \times M$ Woodbury matrix $M_{\mathrm{wood}} = B + W^* P_0^{-1} W$.
7. **`stale_numbers` (`derivation.md`, `README.md`):** Synchronized every numerical value in `derivation.md` and `README.md` to `verification.json` (`T_even(log 3) = 0.9150349476`, `T_even(1.135) = 0.9960149627`, `T_odd(1.135) = 0.2932931339`, `||K_even||_op(1/2 log 10, M=8) <= 0.9760706672`).

---

## 2. Reproduction

```bash
pyright audits/multiprime-euler-preconditioner-2026-10-15-v1/verify_multiprime_euler.py
.venv/bin/python audits/multiprime-euler-preconditioner-2026-10-15-v1/verify_multiprime_euler.py
shasum -a 256 audits/multiprime-euler-preconditioner-2026-10-15-v1/verification.json
```

---

> **Wall check:** **RH**, **G2**, the **cofinal signed-arithmetic lower bound**, and **both historical missing-original evidence groups** in `evidence/MISSING.md` remain **OPEN**.
