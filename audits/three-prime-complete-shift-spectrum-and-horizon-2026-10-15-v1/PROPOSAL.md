# Proposal: Two-Sided Positive-Shift Step-Rank-1 Minorant & Crossing the First Internal Primorial Horizons for $K=3$ and $K=4$ (`three-prime-complete-shift-spectrum-and-horizon-2026-10-15-v1`)

> **Wall check**: The Riemann Hypothesis (RH), G2, the cofinal signed-arithmetic lower bound, and both historical missing-original evidence groups in `evidence/MISSING.md` remain **OPEN**.

## 1. Strategic Objective ("Closer to RH — Not Smaller Bounds")

In Milestone 8 (`multiprime-three-prime-and-scaling-2026-10-15-v1`), the primorial balanced-partition Euler-factor preconditioners $B_{\mathcal{P}_{K,+},\mathcal{P}_{K,-}}$ were certified up to their **first internal preconditioner shift horizons** $a_{\mathrm{iso}}(K) = \log d_+(K)$ ($a_{\mathrm{iso}}(2) = \log 3$, $a_{\mathrm{iso}}(3) = \log 6 = \frac{1}{2}\log 36$, $a_{\mathrm{iso}}(4) = \log 15 = \frac{1}{2}\log 225$) using the pure-diagonal Schur weight $V_a(x)$. While $K=2$ ($B_{2,3}$) was subsequently pushed beyond $a_{\mathrm{iso}}(2) = \log 3$ up to $\frac{1}{2}\log 13 \approx 1.282475$ in Milestones 8 and 10 using single-reflection step minorants $Q_{\tau, s_\tau}$ for shifts in the **single-reflection regime** $\tau \in [b, 2b)$, a fundamental structural obstacle arises for $K \ge 3$:

As $K$ grows, the complete reduced-fraction shift spectrum of $L_{\mathcal{P}_K}(-W_{\mathrm{arith}})$ contains an increasing number of **external combination shifts** $\tau_r = \log r$ that lie in the **two-sided overlap regime** $0 < \tau_r < b$ (where both $x + \tau_r \in [-b, b]$ and $x - \tau_r \in [-b, b]$ for $|x| < b - \tau_r$). Because a two-sided translation $x \mapsto x \pm \tau_r$ does not act as an involution on $[\tau_r - b, b]$, previous single-reflection minorants could not be applied to $\tau_r \in (0, b)$. Worse still, when a shift $\tau_r \in (0, b)$ has a **positive coefficient** $c_r > 0$ ($s_r = +1$), the pure-diagonal Schur weight $V_a(x)$ replaces the stabilizing positive shift $+c_r(T_{\tau_r} + T_{-\tau_r})$ with a **double negative penalty** $-2 c_r$ on $[0, b - \tau_r]$.

In this Milestone 13 package (`KERNEL-API`), we resolve this obstacle across all regimes $\tau_r \in (0, 2b)$ and cross the first internal primorial shift horizons for both $K = 3$ ($B_{\{2,3\},\{5\}}$) and $K = 4$ ($B_{\{2,3,5\},\{7\}}$):

1. **Theorem 1 (`KERNEL-API` — Universal Schur Decomposition, Two-Sided Positive-Shift Step-Rank-1 Minorant, and Single Aggregated Sherman–Morrison Trace Reduction)**:
   - We prove that for **every** shift $\tau_r \in (0, 2b)$ (across **both** the two-sided overlap regime $0 < \tau_r < b$ and the single-reflection regime $b \le \tau_r < 2b$) with positive coefficient $c_r > 0$ ($s_r = +1$), the positive semidefinite Schur operator
     $$M_{\tau_r}^+ := c_r \bigl(\mathbf{1}_{[-b, b - \tau_r]} + \mathbf{1}_{[\tau_r - b, b]}\bigr) I + c_r P_b (T_{\tau_r} + T_{-\tau_r}) P_b \succeq 0$$
     maps the constant function $\mathbf{1}_{[-b, b]}$ to $(M_{\tau_r}^+ \mathbf{1}_{[-b, b]})(x) = 2 c_r \psi_r(x)$ on $[0, b]$, where
     $$\psi_r(x) := \mathbf{1}_{[0, b - \tau_r]}(x) + \mathbf{1}_{[\tau_r - b, b]}(x) \in \mathcal{S}_{\mathrm{step}}$$
     is a step function on the existing cut partition $\{0, b - \tau_r, \tau_r - b, b\} \cap [0, b]$!
   - Summing over all positive active shifts $c_r > 0$ and applying operator Cauchy–Schwarz to $M_{\mathrm{pos}}^+ := \sum_{c_r > 0} M_{\tau_r}^+ \succeq 0$ at the constant test vector $\mathbf{1}_{[0, b]}$ yields the **exact aggregated rank-1 step minorant**:
     $$M_{\mathrm{pos}}^+ \succeq \frac{2}{S_{\mathrm{pos}}} |\Psi_{\mathrm{pos}}\rangle \langle \Psi_{\mathrm{pos}}| \succeq 0,$$
     where $\Psi_{\mathrm{pos}}(x) = \sum_{c_r > 0} c_r \psi_r(x) \in \mathcal{S}_{\mathrm{step}}$ and $S_{\mathrm{pos}} = \sum_{c_r > 0} c_r (2b - \tau_r) = \int_0^b \Psi_{\mathrm{pos}}(x)\,dx > 0$.
   - This rank-1 minorant achieves **exact equality (zero loss) on the constant mode $\mathbf{1}_{[0, b]}$**, requires **zero additional cuts**, acts **entirely inside the step subspace $\mathcal{S}_{\mathrm{step}}$**, vanishes identically on $\mathcal{S}_{\mathrm{step}}^\perp$, and yields the closed-form **Sherman–Morrison trace identity**:
     $$\operatorname{Tr}(K_{\mathrm{sherman, even}}) = \operatorname{Tr}(K_{\mathrm{pure, even}}) - \frac{\frac{2}{S_{\mathrm{pos}}} I_{\mathrm{pos}}}{1 + \frac{2}{S_{\mathrm{pos}}} J_{\mathrm{pos}}},$$
     where $J_{\mathrm{pos}} = \langle \Psi_{\mathrm{pos}}, V_a^{-1} \Psi_{\mathrm{pos}} \rangle_{L^2(0, b)}$ and $I_{\mathrm{pos}} = \langle V_a^{-1} \Psi_{\mathrm{pos}}, M_{\Delta_\alpha}^{\mathrm{even}} V_a^{-1} \Psi_{\mathrm{pos}} \rangle_{L^2(0, b)}$.

2. **Theorem 2 (`KERNEL-API` — Crossing the First Internal Primorial Horizons for $K=3$ and $K=4$ up to the Second Internal Horizons)**:
   - **For $K = 3$ ($B_{\{2,3\},\{5\}}$, $P_3 = 30$) at $\Delta_\alpha = 0$ (zero archimedean shift!)**:
     We push the certified coercivity horizon from the first internal shift $a_{\mathrm{iso}}(3) = \frac{1}{2}\log 36 = \log 6 \approx 1.791759$ ($N = 36$, 7 shifts) across $\tau_{6/5}, \tau_{37/30}, \tau_{19/15}, \tau_{13/10}, \tau_{30/23}, \tau_{15/11}, \tau_{41/30}$ up to **$a = \frac{1}{2}\log 42 = \log\sqrt{42} \approx 1.868835$** ($N = 42$, $2b = \log(7/5)$, 14 active shifts: 7 two-sided and 7 single-reflection). At $N = 40, 41, 42$ ($\Delta_\alpha = 0$), the pure-diagonal trace fails ($\operatorname{Tr}_{\mathrm{pure}} = 1.030545, 1.467972, 2.400252 > 1$), whereas Theorem 1 certifies $\operatorname{Tr}(K_{\mathrm{sherman, even}}) = 0.458404, 0.530367, 0.626834 < 1$!
   - **For $K = 3$ ($B_{\{2,3\},\{5\}}$) at $\Delta_\alpha = 3/5 = 0.60$**:
     We push $K = 3$ all the way up to the **second internal shift horizon $a = \frac{1}{2}\log 45 = \log(3\sqrt{5}) \approx 1.903331$** ($N = 45$, $2b = \log(3/2) \approx 0.405465$, **18 active shifts**: 8 two-sided and 10 single-reflection). Across $N = 42, 43, 44, 45$ ($\Delta_\alpha = 0.60$), the pure-diagonal trace fails ($\operatorname{Tr}_{\mathrm{pure}} = 1.131822, 1.465187, 2.002820, 2.768965 > 1$), whereas Theorem 1 certifies $\operatorname{Tr}(K_{\mathrm{sherman, even}}) = 0.643630, 0.715016, 0.812353, 0.931891 < 1$!
   - **For $K = 4$ ($B_{\{2,3,5\},\{7\}}$, $P_4 = 210$) at $\Delta_\alpha = 0$ (zero archimedean shift!)**:
     We push the certified coercivity horizon from the first internal shift $a_{\mathrm{iso}}(4) = \frac{1}{2}\log 225 = \log 15 \approx 2.708050$ ($N = 225$, 21 shifts) across the first internal shift $\tau_{15/14} = \log(15/14)$ and 21 additional external shifts all the way up to the **second internal shift horizon $a = \frac{1}{2}\log 240 = \log(4\sqrt{15}) \approx 2.740319$** ($N = 240$, $2b = \log(8/7) \approx 0.133531$, **43 active shifts**: 21 two-sided and 22 single-reflection), reducing the certified even trace by **$4.42\times$** from $\operatorname{Tr}_{\mathrm{pure}} = 0.448470$ to $\operatorname{Tr}(K_{\mathrm{sherman, even}}) = 0.101574 < 1$!

---

> **Wall check**: The Riemann Hypothesis (RH), G2, the cofinal signed-arithmetic lower bound, and both historical missing-original evidence groups in `evidence/MISSING.md` remain **OPEN**.
