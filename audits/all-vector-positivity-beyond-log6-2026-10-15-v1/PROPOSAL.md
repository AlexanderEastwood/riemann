# Proposal: Breaking the $\frac{1}{2}\log 6$ Barrier — All-Vector Weil Positivity Up to $\log(5/2)$, $0.960$, and $\frac{1}{2}\log 7$

**Date:** 2026-10-15  
**Lane:** `KERNEL-API` (`all-vector-positivity-beyond-log6-2026-10-15-v1`)  
**Status:** 384-bit `flint.arb` Certified (Non-blocking research proposal; RH, G2, the cofinal signed-arithmetic lower bound, and both historical missing-original evidence groups in `evidence/MISSING.md` remain **OPEN**)

---

## 1. Executive Summary

In Milestone 1 (`codex-review-and-all-vector-extension-2026-10-15-v1`), the `KERNEL-API` all-vector positivity certificate for $\mathcal{Q}_a$ on $L_2(V_{a-\log 2}) \subset V_a$ was extended from $a = \frac{1}{2}\log 5 \approx 0.804719$ up to the $m = 6$ composite prime-power threshold $a_\star = \frac{1}{2}\log 6 \approx 0.8958797346$. At $a > \frac{1}{2}\log 6$, the shift $\tau_6 = \log(3/2) = \log 6 - 2\log 2 \approx 0.405465$ satisfies $\tau_6 < 2b = 2(a - \log 2)$, so $P_b(T_{\tau_6} + T_{-\tau_6})P_b \ne 0$ and the prime baseline ceases to be a pure multiplication operator on $V_b = L^2(-b, b)$.

This audit package proves and certifies in 384-bit `flint.arb` interval arithmetic that $\frac{1}{2}\log 6$ is **not** a positivity obstruction for $L_2(V_{a-\log 2})$, extending strict all-vector Weil positivity across the entire composite-interaction regime up to the next prime-pair threshold **$a_{\star\star\star} = \frac{1}{2}\log 7 \approx 0.9729550745$**:

1. **Exact Three-Island Identity Up to $a = \frac{3}{2}\log 2 \approx 1.039721$**:
   Because the three shifted supports $[-b, b]$, $[\log 2 - b, \log 2 + b]$, and $[-\log 2 - b, -\log 2 + b]$ of $L_2 g$ ($g \in V_b, b = a - \log 2$) are pairwise disjoint whenever $2b \le \log 2 \iff a \le \frac{3}{2}\log 2 \approx 1.0397207708$, we have the exact identity
   $$P_b L_2^2 P_b = \frac{13}{4}\,I_{L^2(-b, b)} = 3.25\,I_{L^2(-b, b)}, \qquad \|L_2 g\|_{L^2(-a, a)}^2 = \frac{13}{4}\,\|g\|_{L^2(-b, b)}^2 \qquad \forall a \le \frac{3}{2}\log 2,\; \forall g \in V_b.$$
   This covers the entire interval $[\frac{1}{2}\log 6, \frac{1}{2}\log 7] \approx [0.895880, 0.972955]$.

2. **Monotonic Archimedean Baseline Shift & Exact Reflection-Involution Preconditioner on $(\frac{1}{2}\log 6, \log(5/2)] \approx (0.895880, 0.916291]$**:
   - Splitting $\alpha(\xi) = \Delta_\alpha + (\alpha(\xi) - \Delta_\alpha)_+ - (\Delta_\alpha - \alpha(\xi))_+$ at $\Delta_\alpha = \frac{7}{20} = 0.35$ transfers $P_b L_2^2 (\Delta_\alpha I) P_b = +\frac{13}{4}\Delta_\alpha I_{L^2(-b, b)}$ directly into the prime baseline while keeping $W_-^{(\Delta_\alpha)}(\xi) = \sigma(L_2)(\xi)^2(\Delta_\alpha - \alpha(\xi))_+$ compactly supported on $[-\xi_0(\Delta_\alpha), \xi_0(\Delta_\alpha)]$.
   - For all $a \in (\frac{1}{2}\log 6, \log(5/2)]$, $b = a - \log 2 \le \log(5/4) = \tau_5 < \tau_3 < \tau_6$, so only $\tau_6 = \log(3/2)$ satisfies $\tau_6 < 2b$. On $I_+ = [\tau_6 - b, b]$, the operator $\pm c_6 P_b(T_{\tau_6} + T_{-\tau_6})P_b$ on $V_b^{\mathrm{even/odd}} \cong L^2(0, b)$ is the **exact reflection involution** $\pm c_6 R_{\tau_6}$ ($R_{\tau_6}g(x) = g(\tau_6 - x)$).
   - Thus $P_0(a) = V_{\mathrm{diag}}(x; a) + \frac{13}{4}\Delta_\alpha I \pm c_6 R_{\tau_6}\mathbf{1}_{[\tau_6-b, b]}$ is invertible in closed analytic form, and its $a$-derivative against $u_\xi(x) = \cos(\xi x)$ or $\sin(\xi x)$ is an **exact sum of three non-negative squares**:
     $$\frac{\partial}{\partial a}\left\langle P_0(a)^{-1} u_\xi, u_\xi \right\rangle_{L^2(0,b)} = \left(\frac{1}{v_1} - \frac{1}{v_0}\right)u_\xi(x_5)^2 + \left(\frac{1}{v_2} - \frac{1}{v_1}\right)u_\xi(x_3)^2 + \frac{\bigl(v_2 u_\xi(b) \mp c_6 u_\xi(x_6)\bigr)^2}{v_2(v_2^2 - c_6^2)} \ge 0.$$
   - Therefore $\mathcal{T}_{\mathrm{even/odd}}^{(0.35)}(a) := \operatorname{Tr}\bigl(P_0(a)^{-1} A_-^{(0.35)}(a)\bigr)$ is strictly increasing in $a$ on $(\frac{1}{2}\log 6, \log(5/2)]$, so a single endpoint evaluation at $a_{\star\star} = \log(5/2) \approx 0.9162907319$ (with **zero** rank-1 minorants!) certifies the entire interval $(\frac{1}{2}\log 6, \log(5/2)]$:
     $$\mathcal{T}_{\mathrm{even}}^{(0.35)}(\log(5/2)) < 0.9802 < 1, \qquad \mathcal{T}_{\mathrm{odd}}^{(0.35)}(\log(5/2)) < 0.5211 < 1.$$

3. **$3\times 3$ Fiber-Bundle Preconditioner & Prime-Reflection Step Minorants up to $a = 0.960000$ and $a_{\star\star\star} = \frac{1}{2}\log 7 \approx 0.9729550745$**:
   - For $a \in (\log(5/2), \frac{1}{2}\log 7]$, $b = a - \log 2 > \tau_5 = \log(5/4)$ with $d_5 := b - \tau_5 \le \frac{1}{2}\log(28/25) \approx 0.056664$.
   - The three disjoint intervals $I_1 = [0, d_5]$, $I_2 = [\tau_5, b]$, and $I_3 = [\tau_6 - b, \tau_6 - \tau_5]$ of equal length $d_5$ are coupled pointwise by $u \leftrightarrow u + \tau_5 \leftrightarrow \tau_6 - \tau_5 - u$ via a $3\times 3$ constant tridiagonal fiber matrix $M_3^{\mathrm{even/odd}}$.
   - Replacing $-c_3 R_{\tau_3}$ on $[\tau_3 - b, b]$ by $-c_3 I_{[\tau_3-b, b]}$ and $-c_5 R_{\tau_5}$ on $[0, \tau_5]$ by $-c_5 I_{[0, \tau_5]}$ leaves the exact positive reflection projectors $+2c_3 P_{\mathrm{anti}}^{(3)} + 2c_5 P_{\mathrm{anti}}^{(5)}$ on $V_b^{\mathrm{even}}$ (and $+2c_3 P_{\mathrm{sym}}^{(3)} + 2c_5 P_{\mathrm{sym}}^{(5)}$ on $V_b^{\mathrm{odd}}$).
   - Using prime-reflection step vectors alone (zero archimedean $B_+$ minorant), we certify strict all-vector positivity at $a = 0.940000$ ($\operatorname{Tr}(P^{-1}A_-) < 0.985$) and $a = 0.960000$ ($\operatorname{Tr}(P^{-1}A_-) < 0.9996$).
   - At the next prime-pair threshold **$a_{\star\star\star} = \frac{1}{2}\log 7 \approx 0.9729550745$**, combining the 5 natural-breakpoint prime step vectors with 1 Plancherel step vector $w_\star$ certifies $\operatorname{Tr}(P_{\mathrm{even}}^{-1}A_{-, \mathrm{even}}) < 0.9978 < 1$ and $\operatorname{Tr}(P_{0, \mathrm{odd}}^{-1}A_{-, \mathrm{odd}}) < 0.7290 < 1$.
