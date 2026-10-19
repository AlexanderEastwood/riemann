# Proposal: Analytic Continuity of Legendre Shift & Schur Multiplicity Matrices Across $u=1$ and Extended Four-Prime Horizon up to $a = \frac{1}{2}\log 260$ (`universal-legendre-shift-algebra-and-k4-horizon-2026-10-15-v1`)

> **Wall check**: The Riemann Hypothesis (RH), G2, the cofinal signed-arithmetic lower bound, and both historical missing-original evidence groups in `evidence/MISSING.md` remain **OPEN**.

## 1. Strategic Objective ("Closer to RH — Not Smaller Bounds")

In Milestone 11 (`mellin-jacobi-finite-rank-schur-reduction-2026-10-15-v1`), we established that the restricted translation operator $P_b(T_\tau + T_{-\tau})P_b$ and the Schur support indicator have exact rational polynomial matrices $S_\tau^{(N)}$ and $D_\tau^{(N)}$ in $u = \tau/b$ on the $N$-mode Legendre basis $\mathcal{V}_N = \operatorname{span}\{P_0(x/b), P_2(x/b), \dots, P_{2N-2}(x/b)\}$, and certified them in the single-reflection regime $u \in [1, 2]$. In Milestone 13 (`three-prime-complete-shift-spectrum-and-horizon-2026-10-15-v1`), we introduced the Universal Schur Decomposition on $(-b, b)$ covering both the **two-sided overlap regime** $u \in (0, 1)$ ($\tau \in (0, b)$) and the **single-reflection regime** $u \in [1, 2)$ ($\tau \in [b, 2b)$).

In this Milestone 14 package (`NB-GAIN` / `COEFF` & `NS-61` and `KERNEL-API`), we unify Milestone 11 and Milestone 13 and push the 4-prime preconditioner $B_{\{2,3,5\},\{7\}}$ ($K=4, P_4 = 210$) across **four consecutive internal shift barriers** up to $a = \frac{1}{2}\log 260 \approx 2.780341$ (66 active shifts):

1. **Theorem 1 (`NB-GAIN` / `COEFF` & `NS-61` — Global Analyticity of Legendre Shift & Schur Multiplicity Matrices Across $u=1$ and Universal Kernel-Plus-Positive-Definite Structure on $(0, 2)$)**:
   - While the spatial folded representation on $[0, b]$ exhibits a piecewise regime transition at $\tau = b$ ($u = 1$) where the cut point $|b - \tau|$ bounces off the origin $x = 0$, we prove that in the parity-adapted Legendre polynomial basis $\{\phi_m(t) = \sqrt{\frac{2m+1}{2}} P_m(t)\}$ on $[-1, 1]$ ($m \equiv n \pmod 2$), **both** the shift matrix $S_\tau^{(N)}$ and the Universal Schur Multiplicity Matrix $D_\tau^{(N)} = \langle \phi_m, \psi_\tau \phi_n \rangle$ ($\psi_\tau(x) = \mathbf{1}_{[-b, b-\tau]}(x) + \mathbf{1}_{[\tau-b, b]}(x)$) are given by **one single analytic rational polynomial on the entire interval $u \in [0, 2]$ with zero piecewise branching at $u = 1$**:
     $$(S_\tau^{(N)})_{m, n} = \sqrt{(2m+1)(2n+1)} \int_{-1}^{1 - u} P_m(t) P_n(t + u)\,dt \qquad \forall u \in [0, 2],$$
     $$(D_\tau^{(N)})_{m, n} = \sqrt{(2m+1)(2n+1)} \int_{u - 1}^1 P_m(t) P_n(t)\,dt \qquad \forall u \in [0, 2].$$
   - Furthermore, we prove the **Exact First-Row Polynomial Identity**:
     $$(D_\tau^{(N)})_{0, 2s} = (S_\tau^{(N)})_{0, 2s} = \sqrt{4s+1} \int_{u - 1}^1 P_{2s}(t)\,dt \qquad \forall s \ge 0, \; \forall u \in [0, 2],$$
     so that for $Q_{\tau, -1}^{(N)} = D_\tau^{(N)} - S_\tau^{(N)}$, the first row and column ($P_0$ constant mode) vanish **identically** on $[0, 2]$ ($Q_{\tau, -1}^{(N)} e_0 = 0$), while across all $u \in (0, 2)$:
     - $Q_{\tau, +1}^{(N)} = D_\tau^{(N)} + S_\tau^{(N)} \succ 0$ is strictly positive definite on all $N \times N$ modes ($P_0, P_2, \dots, P_{2N-2}$), and
     - the $(N-1) \times (N-1)$ non-constant block $\widetilde{Q}_{\tau, -1}^{(N)} \succ 0$ is strictly positive definite on $(P_2, P_4, \dots, P_{2N-2})$.

2. **Theorem 2 (`KERNEL-API` + `NB-GAIN` — Crossing Four Internal Primorial Shift Horizons for $K=4$ up to $a = \frac{1}{2}\log 260$ and Super-Exponential $N=4$ Gegenbauer–Bessel Completeness)**:
   - For the 4-prime preconditioner $B_{\{2,3,5\},\{7\}}$ ($K=4, P_4 = 210$), we push the certified coercivity horizon across four internal shifts of $L_{2,3,5,7}$ ($\tau_{15/14}, \tau_{8/7}, \tau_{7/6}, \tau_{6/5}$):
     - **At $\Delta_\alpha = 0$ (zero archimedean shift!)**: Certified up to **$N = 245$ ($a = \frac{1}{2}\log 245 = \log(7\sqrt{5}) \approx 2.750629$, $2b = \log(7/6) \approx 0.154151$, 49 active shifts)**, where the pure-diagonal trace fails ($\operatorname{Tr}_{\mathrm{pure}} = 1.120435 > 1$) while the Sherman–Morrison reduction certifies $\operatorname{Tr}(K_{\mathrm{sherman, even}}) = 0.130324 < 1$ (an **$8.60\times$ reduction**)!
     - **At $\Delta_\alpha = 3/5 = 0.60$**: Certified across $N \in \{245, 250, 252\}$ up to the fourth internal shift **$N = 252$ ($a = \frac{1}{2}\log 252 = \log(6\sqrt{7}) \approx 2.764715$, $2b = \log(6/5) \approx 0.182322$, 56 active shifts)**, reducing $\operatorname{Tr}_{\mathrm{pure}} = 1.387559 > 1$ by **$6.11\times$** to $\operatorname{Tr}(K_{\mathrm{sherman, even}}) = 0.227137 < 1$!
     - **At $\Delta_\alpha = 6/5 = 1.20$**: Certified across $N \in \{252, 255, 260\}$ up to **$N = 260$ ($a = \frac{1}{2}\log 260 = \log(2\sqrt{65}) \approx 2.780341$, $2b = \log(26/21) \approx 0.213574$, 66 active shifts: 34 two-sided and 32 single-reflection)**, reducing $\operatorname{Tr}_{\mathrm{pure}} = 2.292088 > 1$ by **$5.40\times$** to $\operatorname{Tr}(K_{\mathrm{sherman, even}}) = 0.424192 < 1$ and $\operatorname{Tr}(K_{\mathrm{pure, odd}}) = 0.515452 < 1$!
   - At all extended horizons for $K=3$ ($N=42, 45$) and $K=4$ ($N=240, 245, 252, 260$), we certify the exact $N=4$ Gegenbauer–Spherical-Bessel Parseval tail defect $\varepsilon_4^{\mathrm{even/odd}}(b) \le 2.831 \times 10^{-11}$ (and $\le 2.147 \times 10^{-22}$ at $K=4, \Delta_\alpha = 0$), proving that $N=4$ Legendre modes capture essentially $100\%$ of the archimedean operator across the entire extended primorial tower.

---

> **Wall check**: The Riemann Hypothesis (RH), G2, the cofinal signed-arithmetic lower bound, and both historical missing-original evidence groups in `evidence/MISSING.md` remain **OPEN**.
