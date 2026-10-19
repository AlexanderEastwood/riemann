# Milestone 10 Audit — Block-Invariant Cauchy–Poincaré Step-Subspace Interlacing & Crossing the Internal $\log 2$ Shift Barrier (`KERNEL-API`)

**Date:** 2026-10-15  
**Target Lane:** `KERNEL-API`  
**Audit ID:** `multiprime-internal-shift-and-block-interlacing-2026-10-15-v1`

---

## Wall Check (Top of Deliverable)

> **Wall check:** Does this audit prove the Riemann Hypothesis (RH), complete the global archimedean completion (G2), establish the cofinal prime-shift lower bound as $a \to \infty$, or recover the missing historical raw outputs in `evidence/MISSING.md`?  
> **No.** RH, G2, the cofinal signed-arithmetic lower bound as $a \to \infty$, and both historical missing-original evidence groups in `evidence/MISSING.md` (`stage4_run_summary.json` / `stage4_Ticks.json` and `certificate.json` / `verify_log.txt`) remain **OPEN**.

---

## Summary of Certified Theorems & Results

### 1. Theorem 1 — Block-Invariant Step-Subspace Decomposition & $d$-Mode Cauchy–Poincaré Interlacing
- Because $P_0 = V(x) + W B^{-1} W^*$ has step vectors $w_m \in \mathcal{S}_{\mathrm{step}} = \bigoplus_{k=1}^{N_{\mathrm{elem}}} \mathbb{R}\,\mathbf{1}_{I_k}$ and piecewise-constant floor $V(x) = v_k$ on $I_k$, $P_0$ commutes with the orthogonal projection $\Pi_{\mathrm{step}}$ onto $\mathcal{S}_{\mathrm{step}}$ and acts as scalar multiplication by $v_k$ on $\mathcal{S}_{\mathrm{step}}^\perp = \bigoplus_{k=1}^{N_{\mathrm{elem}}} L^2_0(I_k)$.
- By Cauchy–Poincaré interlacing on any $P_0$-orthonormal family $q_1, \dots, q_d \in \mathcal{S}_{\mathrm{step}}$ with $d \times d$ archimedean Gram matrix $G^{(d)}_{ij} = \langle q_i, A_-^{(\Delta_\alpha)} q_j \rangle$,
  $$\|K\|_{\mathrm{op}} = \lambda_1(K) \le \operatorname{Tr}(K) - \operatorname{Tr}(G^{(d)}) + \Lambda_1,$$
  where $\Lambda_1 I_d - G^{(d)} \succ 0$ is certified by Cholesky factorization in `flint.arb`.
- At $a = \frac{1}{2}\log 12 \approx 1.242453$ ($\Delta_\alpha = 0.6$, $n_{\mathrm{sub}} = 5$), moving from $d = 2$ to $d = 4$ improves $\|K_{\mathrm{even}}\|_{\mathrm{op}}$ from `0.999947` to `0.999646`, increasing the certified margin $1 - \|K_{\mathrm{even}}\|_{\mathrm{op}}$ by **$6.7\times$** (`0.000354` vs `0.000053`).

### 2. Theorem 2 — Step-Subspace Gauge-Invariant Asymmetric Schur Weights & Crossing the Internal $\log 2$ Shift Barrier $a \in (\frac{1}{2}\log 12, \frac{1}{2}\log 13]$
- Introducing asymmetric Schur gauge weights $\gamma = (1, 1, 18/25, 39/50, 17/20, 1)$ and $\eta = (41/50, 41/50, 1, 1, 1, 1)$ for the six active shifts $(\tau_{7/6}, \tau_{6/5}, \tau_{3/2}, \tau_{5/3}, \tau_{11/6}, \tau_2)$ leaves the quadratic form on subinterval-constant step pairs **identically invariant** while redistributing the diagonal scalar penalty on $\mathcal{S}_{\mathrm{step}}^\perp$ away from the crowded right endpoint $[\log 2 - b, b]$.
- **384-Bit & 256-Bit `flint.arb` Certification Table Across $a \in [\frac{1}{2}\log 12, \frac{1}{2}\log 13]$:**

| Checkpoint | $a$ | $b$ | $\Delta_\alpha$ | $n_{\mathrm{sub}}$ | $M_{\mathrm{tot}}$ | $N_{\mathrm{elem}}$ | $\lambda_{\min}(P_0)$ | $\|K_{\mathrm{even}}\|_{\mathrm{op}}$ (2-Mode) | $\|K_{\mathrm{even}}\|_{\mathrm{op}}$ (3-Mode) | $\|K_{\mathrm{even}}\|_{\mathrm{op}}$ (4-Mode) | $\|K_{\mathrm{odd}}\|_{\mathrm{op}}$ (2-Mode) | $\|K_{\mathrm{odd}}\|_{\mathrm{op}}$ (3-Mode) | Coercivity $h_{L^2}$ |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| $a = \frac{1}{2}\log 12.00$ ($\log 2$ entry) | `1.242453` | `0.346574` | `0.6` | `5` | `35` | `68` | `0.728681` | `0.999947` | `0.999647` | **`0.999646 < 1`** | `0.925722` | **`0.925701 < 1`** | `2.578e-4` |
| $a = \frac{1}{2}\log 12.25 = \log(7/2)$ | `1.252763` | `0.356883` | `1.0` | `7` | `56` | `110` | `0.122693` | `1.035306` | `1.000014` | **`0.999809 < 1`** | `0.953672` | **`0.950800 < 1`** | `2.346e-5` |
| $a = \frac{1}{2}\log 12.50 = \frac{1}{2}\log(25/2)$ | `1.262864` | `0.366985` | `1.0` | `9` | `72` | `143` | `0.122693` | `1.042455` | `1.000071` | **`0.999812 < 1`** | `0.970600` | **`0.966662 < 1`** | `2.308e-5` |
| $a = \frac{1}{2}\log 12.75 = \frac{1}{2}\log(51/4)$ | `1.272766` | `0.376886` | `1.0` | `11` | `88` | `175` | `0.122693` | `1.047547` | `1.000194` | **`0.999871 < 1`** | `0.987955` | **`0.982400 < 1`** | `1.578e-5` |
| $a = \frac{1}{2}\log 13.00$ ($\tau_{13/6}$ entry) | `1.282475` | `0.386595` | `1.0` | `13` | `104` | `207` | `0.122693` | `1.051589` | `1.000319` | **`0.999906 < 1`** | `1.003276` | **`0.995507 < 1`** | `1.148e-5` |

---

## Reproducibility & Hashes

- **Verifier:** `.venv/bin/python audits/multiprime-internal-shift-and-block-interlacing-2026-10-15-v1/verify_block_interlacing_and_internal_shift.py`
- **Two-Precision Ball Overlap Checks (`256` vs `384` bits):** `30 / 30 PASS`
- **Pyright:** `0 errors, 0 warnings, 0 informations`
- **`verification.json` `payload.sha256`:** `0bd6e9efedbc08baed0629410bad5cf968073133090c310443fbb36af246d4c8`
- **`verification.json` `file_sha256`:** `eea47f75626fed1d4b433d33edbffe44eb3b6d4b9adc4600c7151fb6dbc571c2`

---

## Wall Check (Bottom of Deliverable)

> **Wall check:** Does this audit prove RH, complete G2, establish the cofinal prime-shift lower bound as $a \to \infty$, or recover the missing historical evidence in `evidence/MISSING.md`?  
> **No.** RH, G2, the cofinal signed-arithmetic lower bound as $a \to \infty$, and both missing-original evidence groups in `evidence/MISSING.md` remain **OPEN**.
