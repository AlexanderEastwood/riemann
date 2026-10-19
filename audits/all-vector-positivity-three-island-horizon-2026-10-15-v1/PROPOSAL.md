# PROPOSAL — Klein 4-Group Dihedral Fiber Closure & All-Vector Positivity up to the Exact Three-Island Isometric Horizon $a_{\star\star\star\star\star} = \frac{3}{2}\log 2 = \frac{1}{2}\log 8 \approx 1.039721$

**Wall check:** The Riemann Hypothesis, G2 (global Weil positivity across all test functions), the cofinal signed-arithmetic lower bound in the $B_2$/Stieltjes lane, and both historical missing-original evidence groups in `evidence/MISSING.md` remain **OPEN**. Nothing in this audit claims a proof of RH or global Weil positivity.

---

## 1. Objective & Lane

- **Lane**: `KERNEL-API` (finite-$a$ operator-theoretic Weil positivity via the prime-2 preconditioner $L_2 = \frac{3}{2}I - \frac{1}{\sqrt{2}}(T_{\log 2} + T_{-\log 2})$ on $V_b = L^2(-b, b)$, $b = a - \log 2$).
- **Starting Point**:
  - `audits/all-vector-positivity-beyond-log7-2026-10-15-v1` certified strict all-vector positivity up to the 3-point fiber closure horizon $a_{\star\star\star\star} = \frac{1}{2}\log(15/2) \approx 1.0074515103$, where $d_5 = x_6 = \frac{1}{2}\log(27/20)$.
- **New Mathematical Discoveries & Targets in This Audit**:
  1. **Klein 4-Group ($\mathbb{Z}_2 \times \mathbb{Z}_2$) Dihedral Fiber Closure Theorem on $(\frac{1}{2}\log(15/2), \frac{3}{2}\log 2]$**:
     When $a > \frac{1}{2}\log(15/2)$, the $m = 5$ shift support $[0, d_5]$ ($d_5 = b - \tau_5$) and $m = 6$ reflection support $[x_6, b]$ ($x_6 = \tau_6 - b$) overlap on $[x_6, d_5]$. We prove that because
     $$x_6 + d_5 = (\tau_6 - b) + (b - \tau_5) = \tau_6 - \tau_5 = \log(6/5) \approx 0.1823215568 \qquad \forall\, a \in \mathbb{R},$$
     and because the conjugacy relation
     $$R_{\tau_6} \circ T_{-\tau_5} \circ R_{\tau_6}(x) = \tau_6 - (\tau_6 - x - \tau_5) = x + \tau_5 = T_{\tau_5}(x)$$
     holds identically in the affine orthogonal group $O(1) = \mathbb{R} \rtimes \{\pm 1\}$, the overlap region $[x_6, d_5] \cup [\tau_6 - d_5, b]$ is closed under both $T_{\tau_5}$ and $R_{\tau_6}$ and decomposes into **closed 4-point Klein 4-group ($\mathbb{Z}_2 \times \mathbb{Z}_2$) fibers**
     $$(x,\; y = x + \tau_5,\; x' = (\tau_6 - \tau_5) - x,\; y' = \tau_6 - x)$$
     that block-diagonalize under $(x, y) \mapsto \frac{1}{\sqrt{2}}(x \pm x', y \pm y')$ into two $2 \times 2$ blocks
     $$B_\pm = \begin{pmatrix} v_x & -c_5 \pm c_6 \\ -c_5 \pm c_6 & v_y \end{pmatrix}.$$
     Moreover, because the $m = 3$ reflection $R_{\tau_3}g(x) = g(\tau_3 - x)$ has exact support $[0, \tau_3]$ when $b > \tau_3$ ($a > \log(8/3)$), only the single $m = 3$ shift $T_{-\tau_3}$ acts on $(\tau_3, b]$, preserving $v_y = c_0 + \frac{13}{4}\Delta\alpha - c_3 - c_7$ and ensuring $\det(B_-) = v_x v_y - (c_5 + c_6)^2 > 0$ across the entire regime without asymmetric Schur weights.
  2. **Courant–Fischer 2-Mode Deflated Trace Theorem & Exact Fubini–Plancherel Identity for $\langle \psi_r, W_p \rangle$**:
     As $a$ increases past $0.990$, the raw trace $\mathrm{Tr}(P(a)^{-1}A_-(\Delta\alpha)) = \sum_{j \ge 1} \lambda_j(K)$ crosses $1$ only because the second eigenvalue $\lambda_2(K) \in [0.012, 0.031]$ adds to $\lambda_1(K) < 1$ (while on $L^2(0, b)$ the true second eigenvalue of $A(a)$ is $\lambda_2(A(a)) \in [3.77, 4.71] \gg \lambda_1(A(a)) \in [0.004, 0.056]$). Using the Courant–Fischer Min-Max Theorem on any 2D step trial subspace $\mathrm{span}\{u_1, u_2\} = P(a)^{1/2}\mathrm{span}\{\psi_1, \psi_2\}$ together with the exact Fubini–Plancherel formula for $\langle \psi_r, W_p \rangle_{L^2(0,b)}$ on $[0, \xi_1]$, we certify a rigorous lower bound $\lambda_2(K) \ge \mu_2 := \lambda_{\min}(G^{-1}M) > 0$, proving:
     $$\lambda_{\max}\!\left(P(a)^{-1/2} A_-(\Delta\alpha) P(a)^{-1/2}\right) = \lambda_1(K) \le \mathcal{T}_{\mathrm{defl}}(a) := \mathrm{Tr}\!\left(P(a)^{-1} A_-(\Delta\alpha)\right) - \mu_2 < 1.$$
  3. **Exact Triple Coincidence at the Three-Island Isometric Horizon $a_{\star\star\star\star\star} = \frac{3}{2}\log 2 = \frac{1}{2}\log 8 \approx 1.0397207708$**:
     Prove that at $a = \frac{3}{2}\log 2 = \frac{1}{2}\log 8$:
     - $2b = \log 2$ (exact saturation of Theorem 1's Three-Island Isometric Core $P_b L_2^2 P_b = \frac{13}{4} I_{L^2(-b,b)}$),
     - $2a = \log 8$ (exact boundary where prime-power $n = 2^3 = 8$ enters $V_a$),
     - $x_6 - s_3 = (\tau_6 - b) - (b - \tau_3) = \tau_6 + \tau_3 - 2b = \log 2 - 2b = 0$ (exact meeting of the $m = 3$ shift domain $[0, s_3]$ and the $m = 6$ reflection endpoint $x_6 = s_3 = \log 3 - \frac{3}{2}\log 2 \approx 0.0588915178$).
  4. **Universal Prime-2 Poisson Collapse Theorem for All $a > \log 2$**:
     Prove that for every $a > \log 2$ (including $a > \frac{3}{2}\log 2$ where $2b > \log 2$ and arbitrarily high powers $2^m$ enter $V_a$), the finite prime-2 sum $\sum_{m \ge 1, m\log 2 < 2a} \frac{\log 2}{2^{m/2}} P_b L_2 S_{m\log 2} L_2 P_b$ collapses **identically** to the 3-term operator
     $$-\log 2\, P_b \left(L_2^2 - \frac{1}{2} L_2\right) P_b = -\frac{5\log 2}{2} I_{L^2(-b,b)} + \frac{5\log 2}{2\sqrt{2}} P_b S_{\log 2} P_b - \frac{\log 2}{2} P_b S_{2\log 2} P_b,$$
     and verify this identity in 384-bit `flint.arb` across multiple windows beyond $\frac{3}{2}\log 2$ ($a \in \{1.10, 1.25, 1.50, 2.00\}$).
  5. **384-Bit `flint.arb` All-Vector Positivity Certificates on $(\frac{1}{2}\log(15/2), \frac{3}{2}\log 2]$**:
     Certify strict all-vector positivity $\mathcal{T}_{\mathrm{defl}}(a) < 1$ and $\mathcal{T}_{\mathrm{odd}}(a) < 1$ in 384-bit ball arithmetic at:
     - $a = 1.0150000000$,
     - $a = 1.0250000000$,
     - $a = 1.0320000000$,
     - $a_{\star\star\star\star\star} = \frac{3}{2}\log 2 = \frac{1}{2}\log 8 \approx 1.0397207708$ (**Exact Three-Island Isometric Horizon**).

---

**Wall check:** The Riemann Hypothesis, G2 (global Weil positivity), the cofinal signed-arithmetic lower bound, and both historical missing-original evidence groups in `evidence/MISSING.md` remain **OPEN**.
