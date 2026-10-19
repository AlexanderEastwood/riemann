# Milestone 9 Audit Package — Euler-Depleted Weil Explicit Formula Equivalence, Free-Bandwidth Dichotomy, and Davenport–Heilbronn Control Separation (`KERNEL-API` & `WEIL-FLOOR`)

**Date:** 2026-10-15  
**Target Lanes:** `KERNEL-API` & `WEIL-FLOOR`  
**Audit Directory:** `audits/euler-depleted-weil-equivalence-and-dh-control-2026-10-15-v1/`  
**Verification Hashes:**
- `verification.json` `payload.sha256`: `0d81262363891d91e7edb459c085b5d4923298047f2e7a9850ce38af66cf5ab8`
- `verification.json` `file_sha256`: `c023183b5d603e56206dfb6c986744f89ae5cb805f4a9389342682c08409e570`

---

## Wall Check (Top of Deliverable)

> **Wall check:** Does this deliverable prove the Riemann Hypothesis (RH), complete the global archimedean completion (G2), establish the cofinal prime-shift lower bound as $a \to \infty$, or recover the missing historical raw outputs in `evidence/MISSING.md`?  
> **No.** RH, G2, the cofinal signed-arithmetic lower bound as $a \to \infty$, and both historical missing-original evidence groups in `evidence/MISSING.md` (`stage4_run_summary.json` / `stage4_Ticks.json` and `certificate.json` / `verify_log.txt`) remain **OPEN**.

---

## Summary of Certified Results (Replayed at 256-Bit and 384-Bit `flint.arb` — 70/70 Overlap Checks PASS)

1. **Theorem 1 (Euler-Depleted Weil Explicit Formula, Two-Sided Pole Cancellation, & Critical-Strip Zero Preservation):**
   - **Two-Sided Pole Cancellation & Single-Subset Counterexample:** Both $\mathcal{P}_+ \ne \emptyset$ and $\mathcal{P}_- \ne \emptyset$ are necessary and sufficient for $\sigma_{B_{\mathcal{P}_+, \mathcal{P}_-}}(+i/2) = \sigma_{B_{\mathcal{P}_+, \mathcal{P}_-}}(-i/2) = 0$ identically, mapping the **entire** unrestricted Hilbert space $L^2(-b, b)$ into the pole-free subspace of $L^2(-a, a)$ with zero side conditions. Certified by the single-subset counterexample $\mathcal{P}_+ = \{2\}, \mathcal{P}_- = \emptyset$, where $\sigma(+i/2) = 0$ but $\sigma(-i/2) = 1/2 \ne 0$.
   - **Strict Critical-Strip Zero Preservation:** All zeros of $\sigma_{L_{\mathcal{P}}}(\xi)$ lie strictly on the boundary lines $\operatorname{Im}(\xi) = \pm 1/2$ ($\operatorname{Re}(s) \in \{0, 1\}$), where $\zeta(s) \ne 0$. Inside the open critical strip $|\operatorname{Im}(\xi)| = \delta \in [0, 1/2)$,
     $$0 < m_{\mathcal{P}}(\delta) := \prod_{p \in \mathcal{P}} \left(1 - p^{-1/2-\delta}\right)\left(1 - p^{-1/2+\delta}\right) \le \left|\sigma_{L_{\mathcal{P}}}(\xi)\right| \le M_{\mathcal{P}}(\delta) := \prod_{p \in \mathcal{P}} \left(1 + p^{-1/2-\delta}\right)\left(1 + p^{-1/2+\delta}\right).$$
     At the Davenport–Heilbronn off-line ordinate strip $\delta_{DH} = 308517/1000000 \approx 0.308517$, $|\sigma_{L_{\{2,3\}}}(\gamma - i\delta_{DH})| \ge 0.04469959 > 0$ across a rigorous 256-ball cover of $[0, 2\pi/\log 2]$.
   - **Quantitative Fixed-$\mathcal{P}$ Negative-Witness Transfer & Varying-$\mathcal{P}_K$ Distortion:** Certified explicit zero-tail cutoff $R_* = (120 e^{1/2})^{1/3} \approx 5.828485$, hypergeometric amplification $R_0(\delta_0) = {}_0F_1(; 7/2; +\delta_0^2/4) > 1 + \delta_0^2/14 > 1$, differential phase aligner $(c_0 + c_1 \partial_x)$, and varying-$\mathcal{P}_K$ distortion factor $\Upsilon(\mathcal{P}_K, \delta_{DH}) = M_{\mathcal{P}_K}(1/2)/m_{\mathcal{P}_K}(\delta_{DH})$ across $K = 2, \dots, 8$.

2. **Theorem 2 (The Paley–Wiener Free-Bandwidth vs. Zero-Shift Isometric Horizon Dichotomy):**
   - Certified in 256-bit and 384-bit `flint.arb` across all $(3^K - 1)/2$ coprime squarefree divisor pairs of $P_K^\#$ for $K = 2, \dots, 8$ that the **true minimum nonzero internal shift** $\tau_{\min}(\mathcal{P}_K)$ is strictly smaller than the chosen partition shift $\tau_{\mathrm{part}}(\mathcal{P}_{K,+}, \mathcal{P}_{K,-}) = \log(d_+(K)/d_-(K))$ at $K = 5, 6, 8$:
     - $K = 5$: $\tau_{\min} = \log(22/21) \approx 0.046520 < \log(15/14) \approx 0.068993 < \tau_{\mathrm{part}} = \log(55/42) \approx 0.269664$, so $b_{\mathrm{iso}}(\mathcal{P}_5) \approx 0.023260$.
     - $K = 6$: $\tau_{\min} = \log(78/77) \approx 0.012903 < \tau_{\mathrm{part}} = \log(182/165) \approx 0.098061$, so $b_{\mathrm{iso}}(\mathcal{P}_6) \approx 0.006452$.
     - $K = 7, 8$: $\tau_{\min} = \log(715/714) \approx 0.001400$, so $b_{\mathrm{iso}}(\mathcal{P}_7) = b_{\mathrm{iso}}(\mathcal{P}_8) \approx 0.000700$ ($289\times$ smaller than $K=2$).
   - Certified the Bernstein–Paley–Wiener half-mass bandwidth bound $b \ge \frac{\pi}{4\Delta\xi}$ against the boxcar counterexample $g = \mathbf{1}_{[-1, 1]}$ ($b = \Delta\xi = 1$), whose spectral mass on $[-1, 1]$ is $\frac{2}{\pi}\operatorname{Si}(2) - \frac{2\sin^2(1)}{\pi} \approx 0.57126411 > 1/2$ while $\pi/4 < 1 < \pi/2$.

3. **Theorem 3 (Euler-Product Rigidity & Pure `flint.arb` Davenport–Heilbronn Control Separation):**
   - Certified in 256-bit and 384-bit `flint.arb` that on $f_{DH}(s)$ (`controls/davenport_heilbronn.py`), prime-tower collapse fails at $n = 4, 8, 9$ ($\Lambda_{DH}(4) = -(2+\kappa^2)\log 2 \approx -1.442232$, $\Lambda_{DH}(8) = \kappa^3\log 2 \approx +0.015891$, $\Lambda_{DH}(9) = -(2+\kappa^2)\log 3 \approx -2.285884$), composite vanishing fails at $n = 6$ ($\Lambda_{DH}(6) = (1+\kappa^2)\log 6 \approx +1.936356 \ne 0$), and the $K=2$ zero-shift diagonal reverses sign:
     $$C_{\mathrm{diag}, DH}(\{2, 3\}) = \frac{4}{3}\Lambda_{DH}(2) + \Lambda_{DH}(3) - \frac{1}{3}\Lambda_{DH}(6) \approx -0.6949999696 < 0 \quad \text{vs.} \quad C_{\mathrm{diag}, \zeta}(\{2, 3\}) \approx +2.0228085810 > 0.$$
   - Certified purely in 256-bit and 384-bit `flint.arb` (with zero float/numpy dependencies) on concrete 3-mode rational sine packets $g_b \in L^2(-b, b)$ at $b \in \{2, 5/2, 3\}$ that the $B_{2,3}$-preconditioned Weil quadratic form is **strictly negative** on $f_{DH}(s)$ (`-0.0325224810`, `-0.2189462666`, `-0.5232379060 < 0`) while remaining **strictly positive** on $\zeta(s)$ (`+6.8955954621`, `+8.7494420069`, `+5.5185873445 > 0`).

---

## Reproduction Command

```bash
.venv/bin/python audits/euler-depleted-weil-equivalence-and-dh-control-2026-10-15-v1/verify_euler_weil_equivalence_and_dh.py
pyright audits/euler-depleted-weil-equivalence-and-dh-control-2026-10-15-v1/verify_euler_weil_equivalence_and_dh.py
```

---

## Wall Check (Bottom of Deliverable)

> **Wall check:** RH, G2, the cofinal signed-arithmetic lower bound as $a \to \infty$, and both missing-original evidence groups in `evidence/MISSING.md` remain **OPEN**.
