# Proposal: Two-Precision `flint.arb`/`flint.acb` Candidate-Mechanism Screen Across `WEIL-FLOOR`, `KERNEL-API`, and `NB-GAIN` (`cofinal-candidate-mechanisms-screen-2026-10-16-v1`, Repaired per Review)

**Wall check:** Same open gap. Closest results: `WEIL-FLOOR`, `NS24/39/43`, `NB-GAIN` (`NS53/61/83/87/98`), and `ZERO-GEOMETRY` (`NS100/101`). We still need a bound that remains valid as the window grows ($b \to \infty$ or $N \to \infty$), retaining every signed arithmetic contribution and coupling. `RH`, `G2`, and both missing-original evidence groups in `evidence/MISSING.md` remain **OPEN**. `M17 v2` remains **PAUSED**.

---

## 1. Exact Target & Scope

This bounded candidate-testing package (`audits/cofinal-candidate-mechanisms-screen-2026-10-16-v1/`) executes a deterministic, two-precision (`256`-bit and `384`-bit `flint.arb` / `flint.acb`, zero `numpy`/`scipy`/`mpmath` imports) quantitative screen of the six post-`v18` candidate mechanisms cataloged in the two pre-computation 5-item arithmetic assessments:
- [`audits/nb-full-residual-arithmetic-assessment-2026-10-16-v1.html`](file:///Users/alex/riemann-worktrees/origin-main-review/audits/nb-full-residual-arithmetic-assessment-2026-10-16-v1.html) (Candidates **A**, **B**, **C** for `NB-GAIN`)
- [`audits/weil-floor-cofinal-arithmetic-assessment-2026-10-16-v1.html`](file:///Users/alex/riemann-worktrees/origin-main-review/audits/weil-floor-cofinal-arithmetic-assessment-2026-10-16-v1.html) (Candidates **I**, **II/IIb**, **III** for `WEIL-FLOOR` and `KERNEL-API`)

In addition to screening the six candidates, this package establishes and certifies two exact analytic identities in `WEIL-FLOOR`:
1. **Theorem 1 (Boundary-Free Dual-Pole Chebyshev–Legendre Identity for $T_{\mathrm{arith}}(a) - T_{\mathrm{pole}}(a)$ in Both Parities)**: proves that in both even and odd parities on $L^2(-a,a)$, subtracting the exact polar operator $T_{\mathrm{pole}}(a)$ from the signed prime-power shift sum $T_{\mathrm{arith}}(a)$ corresponds to subtracting the dual pole generator $x + \log x - 1$ from Chebyshev's $\psi(x)$, with **identically zero Stieltjes integration-by-parts boundary terms** at both $u = 0$ ($\widetilde{R}_\psi(1) = 0$) and $u = 2$ ($\widetilde{C}_{m,n}(2) = 0$).
2. **Theorem 2 (Closed-Form Odd Pole Moment of the Position-Weighted Gaussian Radical $x\,h(x)$ vs. Critical-Zero Derivative $\Xi'(\gamma_1)$)**: proves by differentiating the Mellin identity `eq:v150-mellin` (`evidence/v150/capacity_weight.tex`) at $z = 1$ that the odd position-weighted Gaussian radical $f_{\mathrm{pos}}(x) = x\,h(x)$ has a strictly positive closed-form odd pole moment $\int_{\mathbb{R}} x\sinh(x/2)h(x)\,dx = \frac{1}{\sqrt{3}}\bigl(1 + \frac{\gamma_E - \log(4\pi)}{2}\bigr) = +0.01333431378871523222883\dots > 0$ and couples to simple critical-line zeros via $\widehat{f_{\mathrm{pos}}}(\gamma_k) = +\frac{2i}{\sqrt{3}}\Xi'(\gamma_k) \ne 0$, while recording its compressed 8-mode Legendre residual on $V_8^{\mathrm{odd}}(-a,a)$ across $\lambda \in \{2, 3, 5, 8\}$.

---

## 2. Five-Item Pre-Computation Gate Alignment (Corrected per Review)

| Item | Requirement | Implementation in `verify_cofinal_candidate_mechanisms.py` |
| :--- | :--- | :--- |
| **1. Exact expression** | Full unpreconditioned Weil compression $\mathsf{W}_\lambda^{(8)} = P_8\bigl(A_{\mathrm{arch}}^{\mathrm{full}}(a) + T_{\mathrm{pole}}(a) - T_{\mathrm{arith}}(a)\bigr)P_8$ on $V_8^{\mathrm{even}/\mathrm{odd}}(-a,a)$ (`WEIL-FLOOR`), and in `NB-GAIN`: old-space squared error $E_N^{(2)} = 2 - b_{\mathrm{old}}^\top G_N^{-1} b_{\mathrm{old}}$, corrected new-block load $h_N = b_{\mathrm{new}} - C_N^\top G_N^{-1} b_{\mathrm{old}}$, Schur complement $H_N = D_N - C_N^\top G_N^{-1} C_N$, and dyadic step gain $\Delta_N = E_N^{(2)} - E_{2N}^{(2)} = h_N^\top H_N^{-1} h_N$. | Exact `flint.arb` matrices for $\lambda \in \{2, 3, 5, 8\}$ (up to 26 prime-power shifts, $k \le 61$) and $N \in \{4, 8, 16, 32\}$ via `Kernel` from `evidence/v159/ns61/certify_smoothed.py`. |
| **2. Coefficient hypotheses** | Exact $\Lambda(k)/\sqrt{k}$ weights (`WEIL-FLOOR`), NS57 perturbation $\delta_2 = -\frac{\log 2}{100}$ (`KERNEL-API`), and true vs. NS74-perturbed Beurling loads $\beta \in \{1/2, 1/2 + 10^{-2}\}$ (`NB-GAIN`). | All signed coefficients retained; zero positive-weight or diagonal-only surrogates. |
| **3. Uniform range** | Fixed benchmark windows $\lambda \in \{2, 3, 5, 8\}$ ($a = \log\lambda$) and finite dyadic prefix dimensions $N \in \{4, 8, 16, 32\}$. | Exact two-precision (`256`-bit and `384`-bit) ball certificates with `176/176` string-reconstructed `.overlaps()` checks. |
| **4. Estimating method** | Exact Stieltjes / Legendre polynomial integration (`int_u_poly_exp`), ball Cholesky (`cholesky_lower_arb`) including Weyl perturbation enclosures $(2|\delta_2|)I_8 \pm B_{\delta_2} \succ 0$, `arb_mat.solve(..., algorithm="precond")`, automatic differentiation (`acb_series`), and explicit `lem:v150-weight` tail enclosures for $n \ge 12$ and $x \ge 3.5$. | Zero floating-point tolerances or midpoint eigenvalue assertions (`.contains(0)` and `> arb(0)` only). |
| **5. Remaining transfer & scope** | Does the tested mechanism yield a window-independent lower bound $q_a[f] \ge -C_*\|f\|_2^2$ as $a \to \infty$ or cofinal decrease $E_N^{(2)} \to 0$ as $N \to \infty$? | **Disclosed honestly as OPEN**: compressed 8-mode residuals and finite-shell ($V_{[4,8]}^{\mathrm{even}}$) ratios do not enclose $V_8(-a,a)^\perp$, four finite sizes $N \in \{4, 8, 16, 32\}$ cannot establish convergence or persistent gain, and the $a \to \infty$ / $N \to \infty$ signed arithmetic transfers remain open. |

---

## 3. Non-Goal & Pause Disclosure

- Does **not** claim a new `NS` research row in `NEXT_STEPS.md`, a new theorem node in `PROOF_GRAPH.md`, or a manuscript version bump.
- Does **not** thaw `M17 v2` (`audits/Weil-Floor-Preconditioned-Archimedean-2026-10-15-v2/`) or any paused lane (`WEIL-FLOOR`, `KERNEL-API`, `NB-GAIN`).
- Keeps `RH`, `G2`, and both historical missing-original evidence groups in `evidence/MISSING.md` explicitly **OPEN**.
