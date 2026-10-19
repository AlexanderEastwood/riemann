# PROPOSAL — Higher-Order Wronskian–Transvectant Parseval Hierarchy & Quartic Log-Derivative Jet-Ring Obstruction (`ZERO-GEOMETRY`)

**Wall check:** The Riemann Hypothesis, G2 (global Weil positivity across all test functions), the cofinal signed-arithmetic lower bound in the $B_2$/Stieltjes lane, and both historical missing-original evidence groups in `evidence/MISSING.md` remain **OPEN**. Nothing in this audit claims a proof of RH or global Weil positivity.

---

## 1. Objective & Lane

- **Lane**: `ZERO-GEOMETRY` (single-point Wronskian / log-derivative cumulant transforms, Laguerre–Pólya / Turán inequalities, and jet-ring integrating-factor obstructions).
- **Starting Point**:
  - `audits/next-four-steps-2026-10-15-v1` (Theorems 3A & 3B) and `audits/codex-review-and-all-vector-extension-2026-10-15-v1` proved that clearing the quadratic denominator of $P_1(u) = \frac{1}{4}(\log\phi)''(u)$ at a single coordinate $u$ yields $W_2[\phi](u) = 4\phi(u)^2 P_1(u) = \phi''(u)\phi(u) - (\phi'(u))^2$, whose strip Laplace transform is $-\frac{1}{\pi}\int_{-\infty}^\infty \tau^2 f(z+i\tau)f(z-i\tau)\,d\tau$ (strictly negative on all real slices $z = x \in \mathbb{R}$ for every non-zero real kernel $\phi$, including `NS-101` and `Davenport–Heilbronn`), while clearing $\phi(u)^3$ on the cubic Planat–Solé Jacobi polynomial $8\phi(u)^3 \mathcal{J}_{\mathrm{PS}}(u)$ leaves an irreducible cubic non-divergence remainder $-\frac{19}{2}(\phi'(u))^3$.
- **New Mathematical Targets in This Audit**:
  1. **Complete Order-$2m$ Gauge-Invariant Transvectant / Wronskian Parseval Hierarchy ($m \ge 0$)**:
     For every $m \ge 0$, classify the unique (up to scaling) quadratic $e^{zu}$-gauge-invariant differential polynomial of weight $2m$:
     $$\mathcal{W}_{2m}[\phi](u) := \left.\left(\frac{\partial}{\partial u_1} - \frac{\partial}{\partial u_2}\right)^{2m} \phi(u_1)\phi(u_2)\right|_{u_1=u_2=u} = \sum_{k=0}^{2m} (-1)^k \binom{2m}{k} \phi^{(k)}(u)\,\phi^{(2m-k)}(u).$$
     Prove its exact divergence normal form
     $$\mathcal{W}_{2m}[\psi_z](u) = (-1)^m 2^{2m} \bigl(\psi_z^{(m)}(u)\bigr)^2 + \frac{d}{du}\mathcal{D}_{2m}[\psi_z](u) \qquad (\psi_z(u) = \phi(u)e^{zu})$$
     and its exact vertical-line Parseval identity
     $$\frac{(-1)^m}{2^{2m-1}}\int_{-\infty}^{\infty} \mathcal{W}_{2m}[\phi](u)\,e^{2zu}\,du = 2\int_{-\infty}^{\infty} \bigl(\psi_z^{(m)}(u)\bigr)^2\,du = \frac{1}{\pi}\int_{-\infty}^{\infty} \tau^{2m}\,f(z + i\tau)f(z - i\tau)\,d\tau.$$
  2. **Strict Positivity of the Wronskian–Hankel Moment Matrix $\mathcal{H}_M[\phi](x) \succ 0$ Across Both RH and Off-Line Controls**:
     Prove that for every $M \ge 1$ and every real slice $z = x \in \mathbb{R}$, the $(M+1) \times (M+1)$ Hankel matrix of normalized Wronskian Laplace transforms
     $$\mathcal{H}_M[\phi](x)_{j,k} := \frac{(-1)^{j+k}}{2^{2(j+k)-1}}\int_{-\infty}^{\infty} \mathcal{W}_{2(j+k)}[\phi](u)\,e^{2xu}\,du = \frac{1}{\pi}\int_{-\infty}^{\infty} \tau^{2(j+k)} |f(x+i\tau)|^2\,d\tau \succ 0$$
     is strictly positive definite (satisfying all Turán–Hankel determinant inequalities $\det \mathcal{H}_m[\phi](x) > 0$) for **every** non-zero real kernel $\phi$, including off-line zero controls (`NS-101` and `Davenport–Heilbronn`). Thus no linear or Hankel-determinant combination of quadratic gauge-invariant single-point Wronskians $\mathcal{W}_{2m}[\phi]$ can ever separate RH from off-line zero controls on real slices.
  3. **Exact Quartic Jet-Ring Decomposition of $\phi(u)^4 (\log \phi)^{(4)}(u)$**:
     Prove the exact algebraic identity in $\mathbb{Q}[\phi, \phi', \phi'', \phi''', \phi^{(4)}]$:
     $$16\phi(u)^4 P_3(u) := \phi(u)^4 (\log \phi)^{(4)}(u) = \frac{1}{2}\,\phi(u)^2\,\mathcal{W}_4[\phi](u) - \frac{3}{2}\,\bigl(\mathcal{W}_2[\phi](u)\bigr)^2 = \frac{1}{2}\,\phi(u)^2\,\mathcal{W}_4[\phi](u) - 6\,\bigl(W_2[\phi](u)\bigr)^2,$$
     and the exact quartic divergence normal form:
     $$\phi(u)^4 (\log \phi)^{(4)}(u) = \frac{1}{4}\frac{d^4}{du^4}\!\left(\phi(u)^4\right) - \frac{5}{2}\frac{d^2}{du^2}\!\left(\phi(u)^2(\phi'(u))^2\right) + 2(\phi'(u))^4 - 4\phi(u)^2(\phi''(u))^2.$$

---

**Wall check:** The Riemann Hypothesis, G2 (global Weil positivity), the cofinal signed-arithmetic lower bound, and both historical missing-original evidence groups in `evidence/MISSING.md` remain **OPEN**.
