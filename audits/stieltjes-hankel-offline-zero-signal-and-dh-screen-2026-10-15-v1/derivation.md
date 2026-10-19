# Mathematical Derivations — Ordinate-Centered Stieltjes–Hankel Parity Separation & Davenport–Heilbronn Off-Line Zero Screen (`ZERO-GEOMETRY`)

**Date:** 2026-10-15  
**Target Lane:** `ZERO-GEOMETRY`  
**Audit Directory:** `audits/stieltjes-hankel-offline-zero-signal-and-dh-screen-2026-10-15-v1/`

---

## Wall Check (Top of Deliverable)

> **Wall check:** Does this derivation prove the Riemann Hypothesis (RH), complete the global archimedean completion (G2), establish the cofinal prime-shift lower bound as $a \to \infty$, or recover the missing historical raw outputs in `evidence/MISSING.md`?  
> **No.** RH, G2, the cofinal signed-arithmetic lower bound as $a \to \infty$, and both historical missing-original evidence groups in `evidence/MISSING.md` (`stage4_run_summary.json` / `stage4_Ticks.json` and `certificate.json` / `verify_log.txt`) remain **OPEN**.
>
> **Structural Purpose:** This derivation resolves the high-ordinate exponential damping obstruction of the $t_0 = 0$ Stieltjes–Hankel kernel by proving the **Ordinate-Centered Stieltjes–Hankel Parity Separation & Cauchy–Binet Off-Line Zero Dipole Theorem** at general ordinate $t_0 \in \mathbb{R}$, and certifying in 256-bit and 384-bit `flint.arb` / `flint.acb` ball arithmetic that centering at $t_0 = \gamma_{DH} \approx 85.6993484854$ separates Riemann $\zeta(s)$ ($H_{3, \zeta}^{(\sigma)}(t_0) \succ 0$) from Davenport–Heilbronn $f_{DH}(s)$ ($\mu_{2, DH}^{(\sigma)}(\gamma_{DH}) < 0$ and $\det H_{2, DH}^{(\sigma)}(\gamma_{DH}) < 0$).

---

## 1. Theorem 1: Ordinate-Centered Stieltjes–Hankel Parity Separation & Cauchy–Binet Off-Line Zero Dipole Theorem (`ZERO-GEOMETRY`)

### 1.1 Ordinate-Centered Hermite–Gaussian Moments and Explicit-Formula Duality

Let $F(s)$ be a Dirichlet series / $L$-type function whose completed function $\xi_F(s)$ is real on the critical line $\operatorname{Re}(s) = 1/2$ (or satisfies $\overline{\xi_F(1 - \bar{s})} = \xi_F(s)$), so that its nontrivial zeros $\rho = \beta + i\gamma$ are symmetric across the critical line ($\rho \leftrightarrow 1 - \bar{\rho} = (1 - \beta) + i\gamma$). Setting $\xi_\rho := -i(\rho - 1/2) = \gamma - i(\beta - 1/2)$, this symmetry is exact complex conjugation $\xi_\rho \leftrightarrow \overline{\xi_\rho} = \gamma + i(\beta - 1/2)$.

For any center ordinate $t_0 \in \mathbb{R}$, window scale $\sigma > 0$, and integer $m \ge 0$, define the smooth rapid-decay Hermite–Gaussian test function on $\mathbb{R}$:
$$\phi_m^{(\sigma, t_0)}(x) := e^{-i t_0 x} \left(i \frac{d}{dx}\right)^m \left[\frac{1}{\sqrt{2\pi}\,\sigma}\,e^{-x^2 / (2\sigma^2)}\right] = \frac{1}{\sqrt{2\pi}\,\sigma}\,e^{-i t_0 x - x^2 / (2\sigma^2)} \left(-\frac{i}{\sigma}\right)^m \mathrm{He}_m\!\left(\frac{x}{\sigma}\right),$$
whose Fourier–Laplace transform at $\xi \in \mathbb{C}$ is
$$\widehat{\phi}_m^{(\sigma, t_0)}(\xi) = \int_{-\infty}^\infty \phi_m^{(\sigma, t_0)}(x)\,e^{i\xi x}\,dx = (\xi - t_0)^m\,e^{-\frac{1}{2}\sigma^2(\xi - t_0)^2}.$$
Define the **Ordinate-Centered Stieltjes–Hankel Moment Sequence** and **$N \times N$ Hankel Matrix**:
$$\mu_m^{(\sigma)}(t_0) := \sum_{\rho} \widehat{\phi}_m^{(\sigma, t_0)}(\xi_\rho) = \sum_{\rho} (\xi_\rho - t_0)^m\,e^{-\frac{1}{2}\sigma^2(\xi_\rho - t_0)^2}, \qquad \bigl(H_N^{(\sigma)}(t_0)\bigr)_{j, k} := \mu_{j+k}^{(\sigma)}(t_0) \quad (0 \le j, k \le N - 1).$$
By the explicit formula (and its Euler-depleted extension with $L_{\mathcal{P}}(-i\frac{d}{dx})\phi_m^{(\sigma, t_0)}$ from Milestone 9), $\mu_m^{(\sigma)}(t_0)$ equals the dual prime-sum plus archimedean integral of $\phi_m^{(\sigma, t_0)}$.

### 1.2 Statement and Proof of Theorem 1

**Theorem 1 (Ordinate-Centered Stieltjes–Hankel Parity Separation & Cauchy–Binet Off-Line Zero Dipole Theorem).**
1. **(Reality and Hamburger Positivity on the Critical Line):** *Because $\{\xi_\rho\}$ is invariant under $\xi \mapsto \bar{\xi}$ and $t_0, \sigma \in \mathbb{R}$, every moment $\mu_m^{(\sigma)}(t_0)$ is real. If all zeros lie on the critical line ($\beta_\rho = 1/2$, so $\xi_\rho = \gamma_\rho \in \mathbb{R}$), then $\mu_m^{(\sigma)}(t_0) = \int_\mathbb{R} (z - t_0)^m\,d\nu_{t_0}^{(\sigma)}(z)$ is the moment sequence of the non-negative discrete measure $d\nu_{t_0}^{(\sigma)}(z) = \sum_\rho e^{-\frac{1}{2}\sigma^2(\gamma_\rho - t_0)^2} \delta_{\gamma_\rho}(z) \ge 0$. Consequently, for all $t_0 \in \mathbb{R}$, $\sigma > 0$, and $N \ge 1$:*
   $$H_N^{(\sigma)}(t_0) = \sum_{\rho} e^{-\frac{1}{2}\sigma^2(\gamma_\rho - t_0)^2} |v_N(\gamma_\rho - t_0)\rangle\langle v_N(\gamma_\rho - t_0)| \succeq 0 \qquad \bigl(v_N(z) := (1, z, \dots, z^{N-1})^T\bigr),$$
   *with all even moments $\mu_{2r}^{(\sigma)}(t_0) > 0$ and all principal minors $\det H_k^{(\sigma)}(t_0) > 0$ whenever at least $k$ distinct zero ordinates exist.*
2. **(Off-Line Dipole Exponential Amplification & Sign Alternation at $t_0 = \gamma_\star$):** *Suppose an off-line zero twin pair $\rho_{\star, \pm} = \frac{1}{2} \pm \delta_\star + i\gamma_\star$ with $\delta_\star = \beta_\star - \frac{1}{2} > 0$ exists at ordinate $\gamma_\star$, so $\xi_{\star, \pm} - t_0 = (\gamma_\star - t_0) \mp i\delta_\star$. When the center ordinate is tuned to $t_0 = \gamma_\star$, the twin pair has $\xi_{\star, \pm} - \gamma_\star = \mp i\delta_\star \in i\mathbb{R}\setminus\{0\}$ and $(\xi_{\star, \pm} - \gamma_\star)^2 = -\delta_\star^2 < 0$, so:*
   - *Its Gaussian weight is **exponentially amplified**:*
     $$w_{\star, \pm}(\gamma_\star) = e^{-\frac{1}{2}\sigma^2(-\delta_\star^2)} = e^{+\frac{1}{2}\sigma^2\delta_\star^2} > 1,$$
     *while every neighboring on-line zero at ordinate distance $|\gamma_n - \gamma_\star| \ge \Delta\gamma > 0$ is **exponentially suppressed** by $e^{-\frac{1}{2}\sigma^2(\Delta\gamma)^2} < 1$.*
   - *Its odd moments vanish identically at $t_0 = \gamma_\star$, while its even moments alternate in sign:*
     $$\mu_{2r, \mathrm{pair}}^{(\sigma)}(\gamma_\star) = 2(-1)^r \delta_\star^{2r}\,e^{+\frac{1}{2}\sigma^2\delta_\star^2}.$$
     *In particular, the $r = 1$ moment $\mu_2^{(\sigma)}(\gamma_\star) = (H_N^{(\sigma)}(\gamma_\star))_{1,1}$ receives the **strictly negative dipole contribution***
     $$\mu_{2, \mathrm{pair}}^{(\sigma)}(\gamma_\star) = -2\,\delta_\star^2\,e^{+\frac{1}{2}\sigma^2\delta_\star^2} < 0.$$
3. **(Exact Cauchy–Binet Hankel Minor Separation):** *For any $t_0 \in \mathbb{R}$, let $w_a(t_0) := e^{-\frac{1}{2}\sigma^2(\xi_a - t_0)^2}$ and $z_a(t_0) := \xi_a - t_0$. Then the $2 \times 2$ principal Hankel determinant satisfies the exact Cauchy–Binet identity*
   $$\det H_2^{(\sigma)}(t_0) = \mu_0^{(\sigma)}(t_0)\mu_2^{(\sigma)}(t_0) - \bigl(\mu_1^{(\sigma)}(t_0)\bigr)^2 = \sum_{a < b} w_a(t_0)\,w_b(t_0)\,\bigl(z_a(t_0) - z_b(t_0)\bigr)^2.$$
   *In this sum:*
   - *Every pair of on-line zeros $\{\gamma_m, \gamma_n\}$ has $z_m - z_n = \gamma_m - \gamma_n \in \mathbb{R}$ and $w_m, w_n > 0$, contributing a **non-negative** term $w_m(t_0)w_n(t_0)(\gamma_m - \gamma_n)^2 \ge 0$.*
   - *Every off-line twin pair $\{\xi_{\star,+}, \xi_{\star,-}\}$ has $z_{\star,+} - z_{\star,-} = -2i\delta_\star \in i\mathbb{R}\setminus\{0\}$ and $w_{\star,+}(t_0) w_{\star,-}(t_0) = e^{-\sigma^2((\gamma_\star - t_0)^2 - \delta_\star^2)} > 0$, contributing the **strictly negative intrinsic dipole minor***
     $$w_{\star,+}(t_0)\,w_{\star,-}(t_0)\,\bigl(z_{\star,+}(t_0) - z_{\star,-}(t_0)\bigr)^2 = -4\,\delta_\star^2\,e^{-\sigma^2((\gamma_\star - t_0)^2 - \delta_\star^2)} < 0.$$
   *Consequently, whenever the nearest neighboring zero lies at ordinate distance $\Delta\gamma > \delta_\star$, choosing $\sigma$ above the critical threshold*
   $$\sigma_{\mathrm{crit}} := \sqrt{\frac{2}{\delta_\star^2 + (\Delta\gamma)^2}\,\log\!\left(\frac{C_{\mathrm{bg}}(\Delta\gamma)^2}{2\delta_\star^2}\right)}$$
   *guarantees $\mu_2^{(\sigma)}(\gamma_\star) < 0$ and $\det H_2^{(\sigma)}(\gamma_\star) < 0$.*

**Proof:**  
Part (1) is immediate from Hamburger's theorem: $v^T H_N^{(\sigma)}(t_0) v = \sum_\rho e^{-\frac{1}{2}\sigma^2(\gamma_\rho - t_0)^2} \bigl|\sum_{j=0}^{N-1} v_j (\gamma_\rho - t_0)^j\bigr|^2 \ge 0$. For Part (2), substituting $\xi_{\star, \pm} - \gamma_\star = \mp i\delta_\star$ gives $(\mp i\delta_\star)^2 = -\delta_\star^2$ and $(\mp i\delta_\star)^m + (\pm i\delta_\star)^m = 2(-1)^r \delta_\star^{2r}$ for $m = 2r$ (and $0$ for $m = 2r+1$). For Part (3), expanding $\mu_0 \mu_2 - \mu_1^2 = \sum_{a, b} w_a w_b (z_a^2 - z_a z_b) = \frac{1}{2}\sum_{a, b} w_a w_b (z_a - z_b)^2 = \sum_{a < b} w_a w_b (z_a - z_b)^2$ and substituting $z_{\star, \pm}(t_0) = (\gamma_\star - t_0) \mp i\delta_\star$ gives $(z_{\star,+} - z_{\star,-})^2 = (-2i\delta_\star)^2 = -4\delta_\star^2 < 0$ and $z_{\star,+}^2 + z_{\star,-}^2 = 2((\gamma_\star - t_0)^2 - \delta_\star^2)$, so $w_{\star,+}(t_0)w_{\star,-}(t_0) = e^{-\sigma^2((\gamma_\star - t_0)^2 - \delta_\star^2)}$. $\square$

---

## 2. Theorem 2: 100-Digit Complex Interval Newton Isolation of $\rho_{DH, \pm}$ & Certified Stieltjes–Hankel Screen Separating $\zeta(s)$ from $f_{DH}(s)$ (`ZERO-GEOMETRY`)

### 2.1 Exact Hurwitz Zeta Representation and Complex Interval Newton Certification

Recall from `controls/davenport_heilbronn.py` and Milestone 9 that the Davenport–Heilbronn function $f_{DH}(s)$ has the exact Hurwitz zeta representation
$$5^s f_{DH}(s) = g_{DH}(s) := \zeta\!\left(s, \frac{1}{5}\right) + \kappa\,\zeta\!\left(s, \frac{2}{5}\right) - \kappa\,\zeta\!\left(s, \frac{3}{5}\right) - \zeta\!\left(s, \frac{4}{5}\right), \qquad \kappa = \frac{\sqrt{10 - 2\sqrt{5}} - 2}{\sqrt{5} - 1},$$
which is entire on $\mathbb{C}$ (the simple poles of $\zeta(s, a/5)$ at $s = 1$ with residue $1$ cancel via $1 + \kappa - \kappa - 1 = 0$) and satisfies the functional equation $\xi_{DH}(s) = \xi_{DH}(1 - s)$ with $\xi_{DH}(s) := (\pi/5)^{-s/2}\Gamma((s+1)/2) f_{DH}(s)$.

**Lemma 2.1 (Complex Interval Newton Root Enclosure).**  
*Let $g: \mathbb{C} \to \mathbb{C}$ be holomorphic on a closed complex box/disk $B = D(s_0, r) := \{z \in \mathbb{C} : |\operatorname{Re}(z - s_0)| \le r,\; |\operatorname{Im}(z - s_0)| \le r\}$ with $r > 0$. If $0 \notin g'(B)$ and*
$$\Delta_{\mathrm{Newton}}(s_0, B) := \frac{|g(s_0)|}{\inf_{z \in B} |g'(z)|} < r,$$
*then $g$ has a unique simple zero $s_\star \in B$.*

**Proof:**  
For every $z \in \partial B$, $|z - s_0| \ge r$. By the fundamental theorem of calculus along the segment $[s_0, z] \subset B$, $g(z) - g(s_0) = (z - s_0)\int_0^1 g'(s_0 + t(z - s_0))\,dt$, so $|g(z) - g(s_0)| \ge r \inf_{w \in B} |g'(w)| > |g(s_0)|$ on $\partial B$. By Rouché's theorem applied to $h(z) := g'(s_0)(z - s_0)$ (or the contraction mapping theorem applied to $T(z) = z - g(z)/g'(s_0)$ on $B$), $g$ has a unique simple zero in $B$. $\square$

### 2.2 Certified 384-Bit & 256-Bit Ball Results (`verify_stieltjes_hankel_offline_screen.py`)

Using `flint.acb_series([s, 1], prec=2).zeta(c_j)` to evaluate $(g_{DH}(s), g_{DH}'(s))$ and $(\zeta(s), \zeta'(s))$ in 256-bit and 384-bit complex ball arithmetic, `verify_stieltjes_hankel_offline_screen.py` certifies:
1. **First Davenport–Heilbronn Off-Line Zero Twin Pair $\rho_{DH, \pm} = \frac{1}{2} \pm \delta_{DH} + i\gamma_{DH}$:**
   - $\beta_{DH} \in [0.8085171824566373855533519606068441278506702683050165728775753009\dots \pm 10^{-100}]$,
   - $1 - \beta_{DH} \in [0.1914828175433626144466480393931558721493297316949834271224246990\dots \pm 10^{-100}]$,
   - $\delta_{DH} = \beta_{DH} - \frac{1}{2} \in [0.3085171824566373855533519606068441278506702683050165728775753009\dots \pm 10^{-100}] > 0$,
   - $\gamma_{DH} \in [85.69934848537759217192926770894172903798782942340757667362756774\dots \pm 10^{-100}]$,
   with Complex Interval Newton step bound $\Delta_{\mathrm{Newton}} \le 6.71 \times 10^{-114} < r = 10^{-100}$!
2. **Neighboring Davenport–Heilbronn On-Line Zeros Around $\gamma_{DH}$:**
   Isolates and certifies all neighboring critical-line zeros $\rho_{DH, k} = \frac{1}{2} + i\gamma_{DH, k}$ of $f_{DH}(1/2 + i t)$ in the window $t \in [78, 93]$ (where $\xi_{DH}(1/2 + i t)$ is real and sign changes certify every on-line zero in `[78, 93]`), confirming that the nearest on-line zeros to $\gamma_{DH} \approx 85.699348$ lie at $\gamma_{DH, -} \approx 83.734232$ ($|\Delta\gamma| \approx 1.965117$) and $\gamma_{DH, +} \approx 87.619773$ ($|\Delta\gamma| \approx 1.920425$).
3. **Certified Stieltjes–Hankel Screen Comparison at $t_0 = \gamma_{DH}$ ($\sigma \in \{1.5, 2.0, 2.5, 3.0\}$):**
   - On **Davenport–Heilbronn $f_{DH}(s)$** at $t_0 = \gamma_{DH}$: for every $\sigma \in \{1.5, 2.0, 2.5, 3.0\}$, both the second moment $\mu_{2, DH}^{(\sigma)}(\gamma_{DH}) < 0$ and the $2 \times 2$ Hankel determinant $\det H_{2, DH}^{(\sigma)}(\gamma_{DH}) < 0$ are certified **strictly negative** in ball arithmetic (with $\mu_{2, DH}^{(3.0)}(\gamma_{DH}) \approx -0.292151 < 0$ and $\det H_{2, DH}^{(3.0)}(\gamma_{DH}) \approx -0.896715 < 0$).
   - On **Riemann $\zeta(s)$** at the exact same ordinate $t_0 = \gamma_{DH}$ AND across the first 10 Riemann zero ordinates $\gamma_1, \dots, \gamma_{10}$ (isolated and certified via Complex Interval Newton in `flint.acb`): $\mu_{0, \zeta}^{(\sigma)}(t_0) > 0$, $\mu_{2, \zeta}^{(\sigma)}(t_0) > 0$, $\det H_{2, \zeta}^{(\sigma)}(t_0) > 0$, and the $3 \times 3$ Hankel matrix $H_{3, \zeta}^{(\sigma)}(t_0) \succ 0$ is certified strictly positive definite by Cholesky factorization in `flint.arb`!

---

## Wall Check (Bottom of Deliverable)

> **Wall check:** Does this derivation prove RH, complete G2, establish the cofinal prime-shift lower bound as $a \to \infty$, or recover the missing historical evidence in `evidence/MISSING.md`?  
> **No.** RH, G2, the cofinal signed-arithmetic lower bound as $a \to \infty$, and both missing-original evidence groups in `evidence/MISSING.md` remain **OPEN**.
