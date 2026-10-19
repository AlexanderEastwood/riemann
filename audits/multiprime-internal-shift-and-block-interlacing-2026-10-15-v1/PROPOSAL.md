# PROPOSAL — Milestone 10: Block-Invariant Cauchy–Poincaré Step-Subspace Interlacing & Crossing the Internal $\log 2$ Shift Barrier (`KERNEL-API`)

**Date:** 2026-10-15  
**Target Lane:** `KERNEL-API` (Multi-Prime Euler Preconditioner & Internal-Shift Factorization)  
**Audit Directory:** `audits/multiprime-internal-shift-and-block-interlacing-2026-10-15-v1/`

---

## Wall Check (Top of Deliverable)

> **Wall check:** Does this deliverable prove the Riemann Hypothesis (RH), complete the global archimedean completion (G2), establish the cofinal prime-shift lower bound as $a \to \infty$, or recover the missing historical raw outputs in `evidence/MISSING.md`?  
> **No.** RH, G2, the cofinal signed-arithmetic lower bound as $a \to \infty$, and both historical missing-original evidence groups in `evidence/MISSING.md` (`stage4_run_summary.json` / `stage4_Ticks.json` and `certificate.json` / `verify_log.txt`) remain **OPEN**.
>
> **Why this milestone moves us closer to RH (not smaller bounds):**  
> In Milestone 9, we proved that growing the **free Paley–Wiener bandwidth $b = a - c(\mathcal{P}) \to \infty$** is the true cofinal parameter toward RH, and that any increase in $b$ beyond the zero-shift isometric horizon $b_{\mathrm{iso}}(K) = \frac{1}{2}\tau_{\mathrm{iso}}(\mathcal{P}_K)$ forces $2b$ across the internal shifts of $L_{\mathcal{P}}$ itself. In Milestone 8 (`audits/multiprime-three-prime-and-scaling-2026-10-15-v1/`), the 2-prime certification stopped at the exact internal $\log 2$ shift horizon $a = \frac{1}{2}\log 12 = \log(2\sqrt{3}) \approx 1.242453$ ($2b = \log 2 \approx 0.693147$), where two structural walls appeared simultaneously:
> 1. **The Right-Endpoint Shift-Crowding Wall ($V(x) \le 0$ under Symmetric Schur Weights):** At $2b > \log 2$, all six active shifts ($\tau_{7/6}, \tau_{6/5}, \tau_{3/2}, \tau_{5/3}, \tau_{11/6}, \tau_2 = \log 2$) crowd onto the right endpoint $[\log 2 - b, b]$ near $x = b$, causing the symmetric Schur diagonal floor $v_0 - \sum_\tau c_\tau$ to become negative unless $\Delta_\alpha \ge 2.0$.
> 2. **The Multi-Mode Spectral Leakage Wall ($\|K\|_{\mathrm{op}}$ vs. 2-Mode Trace Defect):** As $b\xi_0$ grows past $7$, the Birman–Schwinger operator $K = P_0^{-1/2} A_-^{(\Delta_\alpha)} P_0^{-1/2}$ develops **four** active even modes ($\mu_1, \mu_2, \mu_3, \mu_4$) and **three** active odd modes ($\mu_{1, \mathrm{odd}}, \mu_{2, \mathrm{odd}}, \mu_{3, \mathrm{odd}}$), so the 2-mode even trace bound $\operatorname{Tr}(K_{\mathrm{even}}) - \mu_2$ and 2-mode odd trace bound $\operatorname{Tr}(K_{\mathrm{odd}}) - \mu_{2, \mathrm{odd}}$ both exceed $1$ by $a = \frac{1}{2}\log 13$.
>
> This milestone breaks both walls via two general theorems:
> - **Theorem 1 (Block-Invariant Step-Subspace Decomposition & $d$-Mode Cauchy–Poincaré Interlacing):** Because $P_0 = V(x) + W B^{-1} W^*$ has step vectors $w_m \in \mathcal{S}_{\mathrm{step}} = \bigoplus_{k=1}^{N_{\mathrm{elem}}} \mathbb{R}\,\mathbf{1}_{I_k}$ and piecewise-constant floor $V(x) = v_k$ on $I_k$, $P_0$ commutes with the orthogonal projection $\Pi_{\mathrm{step}}$ onto $\mathcal{S}_{\mathrm{step}}$ and acts as scalar multiplication by $v_k$ on $\mathcal{S}_{\mathrm{step}}^\perp = \bigoplus_{k=1}^{N_{\mathrm{elem}}} L^2_0(I_k)$. By Cauchy–Poincaré interlacing on any $P_0$-orthonormal family $q_1, \dots, q_d \in \mathcal{S}_{\mathrm{step}}$ with $d \times d$ archimedean Gram matrix $G^{(d)}_{ij} = \langle q_i, A_-^{(\Delta_\alpha)} q_j \rangle$,
>   $$\|K\|_{\mathrm{op}} = \lambda_1(K) \le \operatorname{Tr}(K) - \sum_{j=2}^d \mu_j(G^{(d)}) = \operatorname{Tr}(K) - \bigl(\operatorname{Tr}(G^{(d)}) - \mu_1(G^{(d)})\bigr),$$
>   and at $d = N_{\mathrm{elem}}$ this reduces to the exact Block-Invariant Step-Subspace bound $\|K\|_{\mathrm{op}} \le \lambda_{\max}(K_{00}) + \operatorname{Tr}(K_{\perp\perp})$. At $a = \frac{1}{2}\log 12$, moving from $d = 2$ to $d = 4$ increases the certified operator-norm margin by **$6.7\times$** (from `0.000053` to `0.000354`).
> - **Theorem 2 (Step-Subspace Gauge-Invariant Asymmetric Schur Weights & Crossing the Internal $\log 2$ Shift Barrier $a \in (\frac{1}{2}\log 12, \frac{1}{2}\log 13]$):** For any reflection pair $[p_r, q_r] \leftrightarrow [\tau - q_r, \tau - p_r]$ and any gauge weight $\gamma_\tau > 0$, the identity
>   $$2 s c_\tau f(x)f(\tau - x) = -\frac{c_\tau}{\gamma_\tau}f(x)^2 - \gamma_\tau c_\tau f(\tau - x)^2 + c_\tau\left(\frac{1}{\sqrt{\gamma_\tau}}f(x) + s\sqrt{\gamma_\tau}f(\tau - x)\right)^2$$
>   leaves the quadratic form on subinterval-constant step functions **identically invariant** while redistributing the diagonal scalar penalty on $\mathcal{S}_{\mathrm{step}}^\perp$ away from the crowded right endpoint $[\log 2 - b, b]$ onto the uncrowded left interior $[0, \tau/2]$. Using exact rational gauge weights $\gamma = (1, 1, 18/25, 39/50, 17/20, 1)$ and $\eta = (41/50, 41/50, 1, 1, 1, 1)$ with 4-mode even and 3-mode odd Cauchy–Poincaré interlacing in 256-bit and 384-bit `flint.arb`, we certify $B_{2,3}$ across the internal $\log 2$ shift barrier all the way to the $\tau_{13/6} = \log(13/6)$ entry horizon $a = \frac{1}{2}\log 13 \approx 1.282475$.

---

## Deliverables & Acceptance Criteria

1. **`derivation.md`**: Complete self-contained proofs of Theorems 1 and 2.
2. **`verify_block_interlacing_and_internal_shift.py`**: Pure 256-bit and 384-bit `flint.arb` certificate script (two-precision replay per `AGENTS.md` §4, zero float tolerances in ball checks, `pyright` clean).
3. **`verification.json`**: Machine-readable audit payload with canonical `payload.sha256` and `file_sha256`.
4. **`README.md`** and versioned HTML report `audits/multiprime-internal-shift-and-block-interlacing-2026-10-15-v1.html`.
