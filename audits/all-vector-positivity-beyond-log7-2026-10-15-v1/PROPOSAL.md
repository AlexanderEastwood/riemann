# PROPOSAL — All-Vector Positivity Beyond $a = \frac{1}{2}\log 7$ up to the 3-Point Fiber Closure Horizon $a_{\star\star\star\star} = \frac{1}{2}\log(15/2) \approx 1.007452$

**Wall check:** The Riemann Hypothesis, G2 (global Weil positivity across all test functions), the cofinal signed-arithmetic lower bound in the $B_2$/Stieltjes lane, and both historical missing-original evidence groups in `evidence/MISSING.md` remain **OPEN**. Nothing in this audit claims a proof of RH or global Weil positivity.

---

## 1. Objective & Lane

- **Lane**: `KERNEL-API` (finite-$a$ operator-theoretic Weil positivity via the prime-2 preconditioner $L_2 = I + c_2 S_2 + c_4 S_4$ on $V_b = L^2(-b, b)$, $b = a - \log 2$).
- **Starting Point**:
  - `audits/all-vector-positivity-beyond-log6-2026-10-15-v1` certified strict all-vector Weil positivity $Q_a(L_2 h) \ge \mu_{\min}(a)\|h\|_{L^2(-b,b)}^2$ ($\mu_{\min}(a) > 0$) across the entire interval $a \in (\frac{1}{2}\log 6, \log(5/2)] \approx (0.895880, 0.916291]$, at $a = 0.940000$ and $a = 0.960000$, and at the $m = 7$ prime-pair entry threshold $a_{\star\star\star} = \frac{1}{2}\log 7 \approx 0.9729550745$.
- **New Target in This Audit**:
  1. **Exact 3-Point Fiber Closure Theorem up to $a_{\star\star\star\star} = \frac{1}{2}\log(15/2) \approx 1.0074515103$**:
     Prove that for all $a \in (\frac{1}{2}\log 7, \frac{1}{2}\log(15/2)]$:
     - Only $n \in \{2, 3, 4, 5, 7\}$ have $\log n < 2a$ (since $\frac{1}{2}\log 8 = \frac{3}{2}\log 2 \approx 1.039721 > a_{\star\star\star\star}$).
     - The $m = 5$ shift support $[0, d_5]$ ($d_5 = a + \log 2 - \log 5$) and $m = 6$ reflection support $[x_6, b]$ ($x_6 = \log 3 - a$) remain disjoint on $(0, b)$ with $d_5 \le x_6$, achieving exact saturation $d_5 = x_6$ at $a_{\star\star\star\star} = \frac{1}{2}\log(15/2) = \frac{1}{2}(\log 3 + \log 5 - \log 2) \approx 1.0074515103$.
     - The newly active $m = 7$ prime shift $\tau_7 = \log(7/4) \approx 0.559616 > b$ acts on $L^2(0, b)$ purely as the reflection $\mp c_7 R_{\tau_7}$ supported on $[x_7, b] = [\tau_7 - b, b]$ ($c_7 = \frac{\log 7}{2\sqrt{7}}$), decomposing via $I \mp R_{\tau_7} = 2 P_{\mathrm{anti/sym}}^{(7)}$.
     - For $a > \log(8/3) = 3\log 2 - \log 3 \approx 0.980829$, where $b > \tau_3 = \log(4/3)$ ($s_3 := b - \tau_3 > 0$), the $m = 3$ reflection $R_{\tau_3}$ acts on $[0, \tau_3]$ and the $m = 3$ shift coupling on $[0, s_3] \cup [\tau_3, b]$ decomposes into $-c_3 \mathbf{1}_{[0, s_3] \cup [\tau_3, b]} + 2c_3 P_{\mathrm{diff}}^{(3, \mathrm{shift})}$.
     - Consequently, the baseline operator $P_0(a)$ retains a closed $3 \times 3$ tridiagonal fiber structure on $(0, b)$ with determinant-graded inverse $(P_{0,\mathrm{odd}}^{-1})_{ij} = \det(\gamma_{ij})(P_{0,\mathrm{even}}^{-1})_{ij}$ all the way up to $a_{\star\star\star\star} = \frac{1}{2}\log(15/2) > 1.0$!
  2. **Smooth 2-Mode Positive-Semidefinite Loewner Plancherel Minorant and Courant–Fischer 2-Mode Deflated Trace Theorem in 384-Bit Ball Arithmetic**:
     Construct a smooth rank-2 Plancherel step minorant $(w_1, w_2)$ with linear profile $w_2(x) = 1 - 2(x/b)$ on $[\xi_1, \infty)$ ($\xi_1 = 8.8 > \xi_{\Delta\alpha} \approx 8.0372408860$) using the pointwise positive-semidefinite outer-product integrand $M(\omega) = \frac{2}{\pi}\sigma(L_2)(\omega)^2 \mathbf{c}(\omega)\mathbf{c}(\omega)^T \succeq 0$ and piecewise monotonicity of $1/(\alpha(\omega) - \Delta\alpha)$ on $[\omega_k, \omega_{k+1}] \subset [\xi_1, \Xi]$ plus Plancherel's identity on $[\Xi, \infty)$, yielding a certified $2 \times 2$ Loewner upper bound $0 \prec D_{\mathrm{pl}} \preceq D_{\mathrm{pl}}^{\mathrm{upper}}$. Combine this with the Courant–Fischer 2-Mode Deflated Trace Theorem over the exact negative-weight domain $[0, \xi_{\Delta\alpha}]$ ($\alpha(\xi_{\Delta\alpha}) = \Delta\alpha = 0.25$) to certify $\mathcal{T}_{\mathrm{even}}^{\mathrm{defl}}(a) := \operatorname{Tr}(T_{\mathrm{even}}) - \mu_2(C_2) < 1$ and $\mathcal{T}_{\mathrm{odd}}(a) < 1$.
  3. **384-Bit `flint.arb` Certificates Across Four Landmarks in $(\frac{1}{2}\log 7, \frac{1}{2}\log(15/2)]$**:
     - Checkpoint 1: $a = \log(8/3) = 3\log 2 - \log 3 \approx 0.9808292530$ ($\tau_3 = \log(4/3)$ full reflection saturation $x_3 = 0$),
     - Checkpoint 2: $a = 0.9900000000$ (simultaneous $m = 3$ shift + reflection and $m = 7$ reflection),
     - Checkpoint 3: **Unit-Length Landmark $a = 1.0000000000$** ($2a = 2.0$, support $[-1, 1]$ on $V_1$),
     - Checkpoint 4: **3-Point Fiber Closure Horizon $a_{\star\star\star\star} = \frac{1}{2}\log(15/2) \approx 1.0074515103$** ($d_5 = x_6$ exact saturation).

---

## 2. Falsifiability & Verification Criteria

All claims are verified deterministically by `verify_beyond_log7.py` in 384-bit `flint.arb` (`PREC_BITS = 384`) and serialized to `verification.json`:
1. Exact fiber closure assertions (`abs((mids[j2] - mids[i]) - tau5) < 10^{-90}`, `abs((mids[i] + mids[j6]) - tau6) < 10^{-90}`, and equal subinterval lengths `< 10^{-90}`) on all partitions.
2. Certified strict positivity $P_0^{\mathrm{lower}}(a) \succ 0$ via exact $1 \times 1, 2 \times 2, 3 \times 3$ fiber determinants in 384-bit `flint.arb`.
3. Certified strict trace contraction $\mathcal{T}_{\mathrm{even}}^{\mathrm{defl}}(a) = \operatorname{Tr}(T_{\mathrm{even}}) - \mu_2(C_2) < 1$ and $\mathcal{T}_{\mathrm{odd}}(a) < 1$ using the 2-mode Loewner upper-bound matrix $D_{\mathrm{pl}}^{\mathrm{upper}} \succeq D_{\mathrm{pl}}$ over the exact negative-weight domain $[0, \xi_{\Delta\alpha}]$.
4. `pyright` clean (`0 errors, 0 warnings`).

---

**Wall check:** The Riemann Hypothesis, G2 (global Weil positivity), the cofinal signed-arithmetic lower bound, and both historical missing-original evidence groups in `evidence/MISSING.md` remain **OPEN**.
