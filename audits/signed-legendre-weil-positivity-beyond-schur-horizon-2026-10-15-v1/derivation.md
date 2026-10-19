# Derivation — Exact Signed Legendre Weil Positivity Beyond the Unsigned Schur Horizon & Universal Reflection Kernel Strictness (`WEIL-FLOOR` & `NB-GAIN` / `COEFF`)

## Wall Check & Open-Status Disclosure

- **Does this milestone prove the Riemann Hypothesis (RH)?** **No (`OPEN`).**
- **Does this milestone prove `G2` or the cofinal prime-shift lower bound as $a \to \infty$ ($K \to \infty$, $N_{\mathrm{leg}} \to \infty$)?** **No (`OPEN`).** Certifying strict positive definiteness of the finite-rank signed Legendre Weil matrices $W_{\mathrm{signed}}^{(4, \mathrm{even})}(b) - \varepsilon_4^{\mathrm{even}}(b) I_4 \succ 0$ and $W_{\mathrm{signed}}^{(4, \mathrm{odd})}(b) - \varepsilon_4^{\mathrm{odd}}(b) I_4 \succ 0$ up to $N = 50$ ($K = 3$, 23 active shifts) and $N = 380$ ($K = 4$, 175 active shifts) at $\Delta_\alpha = 0$ proves that the breakdown of the unsigned Schur potential $V_a(x)$ is an artifact of discarding the positive-definite reflection sum $\Delta_{\mathrm{Schur}}^{(N)}(b) = \sum |c_r| Q_{\tau_r, \operatorname{sgn}(c_r)}^{(N)} \succ 0$, and establishes positivity on the **finite 8-dimensional Legendre polynomial subspace** $\mathcal{V}_4^{\mathrm{even}} \oplus \mathcal{V}_4^{\mathrm{odd}}$. Per `argon-m16-review` Finding 4, because the signed shifts $S_{\tau_r}^{(4)}$ are projected onto $\mathcal{V}_4^{\mathrm{even}} \oplus \mathcal{V}_4^{\mathrm{odd}}$, subtracting $\varepsilon_4^{\mathrm{even/odd}}(b) I_4$ bounds only the low-frequency archimedean tail $\Pi_{\perp,4} A_-^{(0)}(b)\Pi_{\perp,4}$ and does **not** control off-block signed shift couplings $\Pi_4 S_{\tau_r}\Pi_{\perp,4}$ or $\Pi_{\perp,4} S_{\tau_r}\Pi_{\perp,4}$ on full $L^2(-b,b)$ (which is addressed for $2b \in \{0.40, 0.42, 0.45, 0.48, 0.50\}$ in Milestone 17). Extending signed positivity simultaneously to all Legendre degrees $N_{\mathrm{leg}} \to \infty$ and cofinally as $K \to \infty$ remains **OPEN**.
- **Missing-original evidence disclosure**: Both historical missing-original evidence groups documented in `evidence/MISSING.md` (`src/verify_phase2.py` and `final_weil_check.py`) remain **OPEN**.

---

## 1. Theorem 1: Universal Indicator Completion-of-the-Square, All-Degree Polynomial Reflection Strictness & Exact Signed-vs-Unsigned Legendre Decomposition

### 1.1 Single-Integral Indicator Completion of the Square Across $u = 1$

Let $b > 0$ and let $\tau \in (0, 2b)$ be an active shift with normalized shift parameter $u = \tau / b \in (0, 2)$. On $L^2(-b, b)$, the symmetric translation operator $S_\tau + S_{-\tau}$ acts via
$$((S_\tau + S_{-\tau}) f)(t) = \mathbf{1}_{(-b, b-\tau)}(t) f(t+\tau) + \mathbf{1}_{(-b+\tau, b)}(t) f(t-\tau),$$
and its quadratic form is
$$\langle f, (S_\tau + S_{-\tau}) f \rangle_{L^2(-b, b)} = 2 \int_{-b}^{b-\tau} f(t) f(t+\tau)\,dt.$$

**Lemma 1.1 (Global Indicator Support Identity Across $u = 1$).**
*For every $\tau \in (0, 2b)$, the support multiplicity weight $w_\tau(t)$ of $S_\tau + S_{-\tau}$ on $(-b, b)$ is given globally by the sum of two indicator functions:*
$$w_\tau(t) := \mathbf{1}_{(-b, b-\tau)}(t) + \mathbf{1}_{(-b+\tau, b)}(t) \qquad \forall t \in (-b, b).$$

*Proof.*
- When $\tau \in (0, b)$ ($u \in (0, 1)$, two-sided shift regime), we have $-b + \tau < b - \tau$, so the two intervals $(-b, b-\tau)$ and $(-b+\tau, b)$ overlap on $(-b+\tau, b-\tau)$. Their indicator sum equals $2$ on $(-b+\tau, b-\tau)$ and $1$ on $(-b, -b+\tau) \cup (b-\tau, b)$.
- When $\tau \in [b, 2b)$ ($u \in [1, 2)$, single-reflection shift regime), we have $b - \tau \le -b + \tau$, so the two intervals $(-b, b-\tau)$ and $(-b+\tau, b)$ are disjoint. Their indicator sum equals $1$ on $(-b, b-\tau) \cup (-b+\tau, b)$ and $0$ on $[b-\tau, -b+\tau]$.
In both cases, $w_\tau(t) = \mathbf{1}_{(-b, b-\tau)}(t) + \mathbf{1}_{(-b+\tau, b)}(t)$ holds identically on $(-b, b)$ without any piecewise branching at $\tau = b$. $\square$

**Proposition 1.2 (Universal Single-Integral Completion of the Square).**
*Let $D_\tau f(t) := w_\tau(t) f(t)$ be the multiplication operator by $w_\tau(t)$ on $L^2(-b, b)$, and for $\sigma \in \{+1, -1\}$ let $M_{\tau, \sigma} := D_\tau + \sigma(S_\tau + S_{-\tau})$. Then for every $\tau \in (0, 2b)$ and every $f \in L^2(-b, b)$:*
$$\langle f, M_{\tau, \sigma} f \rangle_{L^2(-b, b)} = \int_{-b}^{b-\tau} \left(f(t) + \sigma f(t+\tau)\right)^2\,dt \ge 0.$$

*Proof.* By Lemma 1.1 and the substitution $s = t + \tau$ in the second integral:
$$\langle f, D_\tau f \rangle_{L^2(-b, b)} = \int_{-b}^{b-\tau} f(t)^2\,dt + \int_{-b+\tau}^{b} f(s)^2\,ds = \int_{-b}^{b-\tau} \left(f(t)^2 + f(t+\tau)^2\right)\,dt.$$
Adding $\sigma \langle f, (S_\tau + S_{-\tau}) f \rangle_{L^2(-b, b)} = 2\sigma \int_{-b}^{b-\tau} f(t) f(t+\tau)\,dt$ yields
$$\langle f, (D_\tau + \sigma(S_\tau + S_{-\tau})) f \rangle_{L^2(-b, b)} = \int_{-b}^{b-\tau} \left(f(t)^2 + 2\sigma f(t) f(t+\tau) + f(t+\tau)^2\right)\,dt = \int_{-b}^{b-\tau} \left(f(t) + \sigma f(t+\tau)\right)^2\,dt \ge 0.$$
In normalized coordinates $x = t/b \in [-1, 1]$ with orthonormal Legendre basis $\widetilde{P}_m(x) = \sqrt{\frac{2m+1}{2}} P_m(x)$, for any same-parity pair $m \equiv n \pmod 2$:
$$\left(Q_{\tau, \sigma}^{(N)}\right)_{m, n} = \left(D_\tau^{(N)} + \sigma S_\tau^{(N)}\right)_{m, n} = \frac{\sqrt{(2m+1)(2n+1)}}{2} \int_{-1}^{1-u} \left(P_m(x) + \sigma P_m(x+u)\right)\left(P_n(x) + \sigma P_n(x+u)\right)\,dx.$$
Because the integration limits $[-1, 1-u]$ depend smoothly on $u = \tau/b \in [0, 2]$, the Legendre Gram matrices $S_\tau^{(N)}$, $D_\tau^{(N)}$, and $Q_{\tau, \sigma}^{(N)} = D_\tau^{(N)} + \sigma S_\tau^{(N)}$ are single global rational polynomial matrices on all of $u \in [0, 2]$. $\square$

---

### 1.2 All-Degree Polynomial Reflection Strictness Theorem

Let $e_m(t) = \sqrt{\frac{2m+1}{2b}} P_m(t/b)$ ($m \ge 0$) be the orthonormal Legendre polynomial basis of $L^2(-b, b)$, and let
$$\mathcal{V}_N^{\mathrm{even}} := \operatorname{span}\{e_0, e_2, \dots, e_{2N-2}\}, \qquad \mathcal{V}_N^{\mathrm{odd}} := \operatorname{span}\{e_1, e_3, \dots, e_{2N-1}\}.$$
By parity $P_m(-x) = (-1)^m P_m(x)$, both $S_\tau + S_{-\tau}$ and $D_\tau$ commute with the parity reflection $(Pf)(t) = f(-t)$ and therefore block-diagonalize across $\mathcal{V}_N^{\mathrm{even}} \oplus \mathcal{V}_N^{\mathrm{odd}}$. Specifically, for any $m, n$ of the same parity ($m \equiv n \pmod 2$) and $u = \tau/b \in [0, 2]$:
$$(S_\tau)_{m, n} = \sqrt{(2m+1)(2n+1)} \int_{-1}^{1-u} P_m(x) P_n(x+u)\,dx,$$
$$(D_\tau)_{m, n} = \sqrt{(2m+1)(2n+1)} \int_{-1}^{1-u} P_m(x) P_n(x)\,dx = \sqrt{(2m+1)(2n+1)} \int_{u-1}^{1} P_m(x) P_n(x)\,dx.$$

**Theorem 1.3 (All-Degree Polynomial Reflection Kernel Strictness).**
*For every integer $N \ge 1$ and every $u = \tau/b \in (0, 2)$, the $N \times N$ reflection projection matrices $Q_{\tau, \sigma}^{(N, \mathrm{even})} = D_\tau^{(N, \mathrm{even})} + \sigma S_\tau^{(N, \mathrm{even})}$ and $Q_{\tau, \sigma}^{(N, \mathrm{odd})} = D_\tau^{(N, \mathrm{odd})} + \sigma S_\tau^{(N, \mathrm{odd})}$ satisfy:*
1. **Positive-shift reflection ($\sigma = +1$)**: Both $Q_{\tau, +1}^{(N, \mathrm{even})} \succ 0$ and $Q_{\tau, +1}^{(N, \mathrm{odd})} \succ 0$ are **strictly positive definite on $\mathbb{R}^N$**.
2. **Negative-shift reflection ($\sigma = -1$)**:
   - On the even sector $\mathcal{V}_N^{\mathrm{even}}$, $\ker\left(Q_{\tau, -1}^{(N, \mathrm{even})}\right) = \mathbb{R} e_0$ is strictly the 1-dimensional constant subspace, and the $(N-1) \times (N-1)$ lower-right block $\widetilde{Q}_{\tau, -1}^{(N, \mathrm{even})} \succ 0$ on $\operatorname{span}\{e_2, \dots, e_{2N-2}\}$ is **strictly positive definite on $\mathbb{R}^{N-1}$** (for all $N \ge 2$).
   - On the odd sector $\mathcal{V}_N^{\mathrm{odd}}$, $Q_{\tau, -1}^{(N, \mathrm{odd})} \succ 0$ is **strictly positive definite on all of $\mathbb{R}^N$**.

*Proof.* Let $f \in \mathcal{V}_N^{\mathrm{even}} \oplus \mathcal{V}_N^{\mathrm{odd}}$ be a polynomial of degree $\le 2N-1$ such that $\langle f, M_{\tau, \sigma} f \rangle_{L^2(-b, b)} = 0$. By Proposition 1.2,
$$\int_{-b}^{b-\tau} \left(f(t) + \sigma f(t+\tau)\right)^2\,dt = 0.$$
Since $u = \tau/b \in (0, 2)$, the interval $(-b, b-\tau)$ has strictly positive length $2b - \tau = b(2 - u) > 0$. Since $f(t) + \sigma f(t+\tau)$ is a polynomial in $t$, its vanishing on the non-degenerate interval $(-b, b-\tau)$ implies that it vanishes identically on all of $\mathbb{R}$:
$$f(t+\tau) = -\sigma f(t) \qquad \forall t \in \mathbb{R}.$$
Iterating twice gives $f(t + 2\tau) = f(t)$ for all $t \in \mathbb{R}$. Since $\tau > 0$, any periodic polynomial on $\mathbb{R}$ must be a constant polynomial $f(t) \equiv c \in \mathbb{R}$.
- If $\sigma = +1$, then $f(t+\tau) = -f(t)$ forces $c = -c \implies c = 0$, so $f \equiv 0$. Thus $\ker(M_{\tau, +1}) \cap \mathbb{R}[t] = \{0\}$, proving $Q_{\tau, +1}^{(N, \mathrm{even})} \succ 0$ and $Q_{\tau, +1}^{(N, \mathrm{odd})} \succ 0$ on $\mathbb{R}^N$.
- If $\sigma = -1$, then $f(t+\tau) = f(t)$ is satisfied by every constant $f(t) \equiv c$ and by no non-constant polynomial. Thus $\ker(M_{\tau, -1}) \cap \mathbb{R}[t] = \mathbb{R} e_0$. Since $\mathcal{V}_N^{\mathrm{even}} \ominus \mathbb{R} e_0 = \operatorname{span}\{e_2, \dots, e_{2N-2}\}$ and $\mathcal{V}_N^{\mathrm{odd}} = \operatorname{span}\{e_1, \dots, e_{2N-1}\}$ both have zero intersection with $\mathbb{R} e_0$, $\widetilde{Q}_{\tau, -1}^{(N, \mathrm{even})} \succ 0$ on $\mathbb{R}^{N-1}$ and $Q_{\tau, -1}^{(N, \mathrm{odd})} \succ 0$ on $\mathbb{R}^N$. $\square$

---

### 1.3 Exact Signed-vs-Unsigned Legendre Decomposition

For a primorial preconditioner $B_{\mathcal{P}_+, \mathcal{P}_-}$ ($\mathcal{P}_K = \mathcal{P}_+ \sqcup \mathcal{P}_-$) on $[-a, a]$ with free bandwidth $b = a - c(\mathcal{P}_K)$ and archimedean shift $\Delta_\alpha \ge 0$, let $A_{\Delta_\alpha}^{(N, \mathrm{sector})}(b)$ denote the $N \times N$ archimedean floor defect matrix on $\mathcal{V}_N^{\mathrm{sector}}$ ($\mathrm{sector} \in \{\mathrm{even}, \mathrm{odd}\}$).
- The **Exact Signed Legendre Weil Matrix** on $\mathcal{V}_N^{\mathrm{sector}}$ is:
  $$W_{\mathrm{signed}}^{(N, \mathrm{sector})}(b) := \left(C_{\mathrm{diag}}(\mathcal{P}_K) + c_0(\mathcal{P}_K) \Delta_\alpha\right) I_N + \sum_{0 < \tau_r < 2b} c_r S_{\tau_r}^{(N, \mathrm{sector})} - A_{\Delta_\alpha}^{(N, \mathrm{sector})}(b).$$
- The **Unsigned Schur Legendre Matrix** (the Legendre projection of $V_a(x) - A_{\Delta_\alpha}$) on $\mathcal{V}_N^{\mathrm{sector}}$ is:
  $$W_{\mathrm{unsigned}}^{(N, \mathrm{sector})}(b) := \left(C_{\mathrm{diag}}(\mathcal{P}_K) + c_0(\mathcal{P}_K) \Delta_\alpha\right) I_N - \sum_{0 < \tau_r < 2b} |c_r| D_{\tau_r}^{(N, \mathrm{sector})} - A_{\Delta_\alpha}^{(N, \mathrm{sector})}(b).$$

**Corollary 1.4 (Exact Schur Reflection Discrepancy Identity).**
*For every $N \ge 1$ and $\mathrm{sector} \in \{\mathrm{even}, \mathrm{odd}\}$,*
$$W_{\mathrm{signed}}^{(N, \mathrm{sector})}(b) - W_{\mathrm{unsigned}}^{(N, \mathrm{sector})}(b) = \Delta_{\mathrm{Schur}}^{(N, \mathrm{sector})}(b) := \sum_{0 < \tau_r < 2b} |c_r| Q_{\tau_r, \operatorname{sgn}(c_r)}^{(N, \mathrm{sector})} \succeq 0.$$
*Moreover, by Theorem 1.3, $\Delta_{\mathrm{Schur}}^{(N, \mathrm{odd})}(b) \succ 0$ is strictly positive definite whenever at least one shift $\tau_r < 2b$ is active, and $\Delta_{\mathrm{Schur}}^{(N, \mathrm{even})}(b) \succ 0$ is strictly positive definite whenever at least one positive shift ($c_r > 0, \tau_r < 2b$) is active.*

---

## 2. Theorem 2: Certified Signed Legendre Positivity at $\Delta_\alpha = 0$ Across 175 Active Shifts vs. Unsigned Schur Breakdown & Davenport–Heilbronn Indefiniteness

### 2.1 Infinite-Dimensional Archimedean Tail Subtraction at $\Delta_\alpha = 0$

At $\Delta_\alpha = 0$ (zero archimedean shift), the archimedean multiplier $(0 - \alpha(\xi))_+ = (-\alpha(\xi))_+$ is supported on $(-\xi_0, \xi_0)$ where $\xi_0 \approx 6.2898359888369028$ solves $\operatorname{Re}\psi(\frac{1}{4} + \frac{i\xi_0}{2}) = \log \pi$. By the Gegenbauer–Spherical-Bessel Parseval identity (Milestone 11, Theorem 1), the full infinite-dimensional archimedean trace on $L^2_{\mathrm{even}}(-b, b)$ and $L^2_{\mathrm{odd}}(-b, b)$ equals
$$\operatorname{Tr}(A_{\mathrm{even}}(b)) = \frac{b}{\pi} \int_0^{\xi_0} \sigma_{L_{\mathcal{P}_K}}(\xi) (-\alpha(\xi)) \left(1 + \operatorname{sinc}(2b\xi)\right)\,d\xi,$$
$$\operatorname{Tr}(A_{\mathrm{odd}}(b)) = \frac{b}{\pi} \int_0^{\xi_0} \sigma_{L_{\mathcal{P}_K}}(\xi) (-\alpha(\xi)) \left(1 - \operatorname{sinc}(2b\xi)\right)\,d\xi,$$
and the infinite-dimensional tail orthogonal to $\mathcal{V}_4^{\mathrm{even}} \oplus \mathcal{V}_4^{\mathrm{odd}}$ has operator norm bounded by the exact Parseval tail trace
$$\varepsilon_4^{\mathrm{sector}}(b) := \operatorname{Tr}(A_{\mathrm{sector}}(b)) - \operatorname{Tr}\left(A_0^{(4, \mathrm{sector})}(b)\right) > 0.$$
Subtracting $\varepsilon_4^{\mathrm{sector}}(b) I_4$ from $W_{\mathrm{signed}}^{(4, \mathrm{sector})}(b)$ yields the tail-corrected matrix
$$W_{\mathrm{signed, tail}}^{(4, \mathrm{sector})}(b) := W_{\mathrm{signed}}^{(4, \mathrm{sector})}(b) - \varepsilon_4^{\mathrm{sector}}(b) I_4.$$

### 2.2 Certified Results for $K = 3$ ($B_{\{2,3\},\{5\}}$, $P_3 = 30$) and $K = 4$ ($B_{\{2,3,5\},\{7\}}$, $P_4 = 210$) at $\Delta_\alpha = 0$

Using two-precision (`256`-bit and `384`-bit) `flint.arb` ball arithmetic:
- Positive definiteness $\lambda_{\min}(W_{\mathrm{signed, tail}}^{(4, \mathrm{sector})}(b)) \ge \lambda_{\mathrm{lb}} > 0$ is certified via exact `flint.arb` Cholesky factorization of $W_{\mathrm{signed, tail}}^{(4, \mathrm{sector})}(b) - \lambda_{\mathrm{lb}} I_4 = L L^T$.
- Indefiniteness $\lambda_{\min}(W_{\mathrm{unsigned}}^{(4, \mathrm{sector})}(b)) \le R(v) < 0$ is certified via exact `flint.arb` evaluation of the Rayleigh quotient $R(v) = \langle v, W_{\mathrm{unsigned}}^{(4, \mathrm{sector})}(b) v \rangle / \langle v, v \rangle$ on a rational witness vector $v \in \mathbb{Q}^4$.

| Family | $N$ | $2b = \log(N/P_K)$ | Active Shifts | $\lambda_{\min}^{\mathrm{cert}}(W_{\mathrm{signed, tail}}^{(4, \mathrm{even})})$ | $\lambda_{\min}(W_{\mathrm{unsigned}}^{(4, \mathrm{even})})$ | $\lambda_{\min}^{\mathrm{cert}}(W_{\mathrm{signed, tail}}^{(4, \mathrm{odd})})$ | $\lambda_{\min}(W_{\mathrm{unsigned}}^{(4, \mathrm{odd})})$ | $\varepsilon_4^{\mathrm{even}}(b)$ |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| $K=3$ | $36$ | $0.182322$ | $7$ | $+2.5866 > 0$ | $+1.6915 > 0$ | $+3.2725 > 0$ | $+2.1402 > 0$ | $1.31 \times 10^{-16}$ |
| $K=3$ | $40$ | $0.287682$ | $12$ | $+1.3585 > 0$ | $-0.0113 < 0$ | $+3.0172 > 0$ | $+0.7195 > 0$ | $6.32 \times 10^{-15}$ |
| $K=3$ | $42$ | $0.336472$ | $14$ | $+0.8327 > 0$ | $-0.6930 < 0$ | $+2.9080 > 0$ | $+0.3216 > 0$ | $2.46 \times 10^{-14}$ |
| $K=3$ | $45$ | $0.405465$ | $18$ | $+0.3767 > 0$ | $-1.9037 < 0$ | $+2.8138 > 0$ | $-0.9194 < 0$ | $1.29 \times 10^{-13}$ |
| $K=3$ | $50$ | $0.510826$ | $23$ | $+0.0590 > 0$ | $-3.8341 < 0$ | $+2.2765 > 0$ | $-2.7789 < 0$ | $9.81 \times 10^{-13}$ |
| $K=4$ | $225$ | $0.068993$ | $21$ | $+4.5861 > 0$ | $+3.6010 > 0$ | $+4.7397 > 0$ | $+3.8632 > 0$ | $3.65 \times 10^{-20}$ |
| $K=4$ | $240$ | $0.133531$ | $43$ | $+4.3102 > 0$ | $+0.7177 > 0$ | $+4.2694 > 0$ | $+0.9508 > 0$ | $9.82 \times 10^{-18}$ |
| $K=4$ | $252$ | $0.182322$ | $56$ | $+3.8138 > 0$ | $-1.4046 < 0$ | $+4.0028 > 0$ | $-0.8473 < 0$ | $1.57 \times 10^{-16}$ |
| $K=4$ | $260$ | $0.213574$ | $66$ | $+3.5332 > 0$ | $-3.0460 < 0$ | $+4.0555 > 0$ | $-2.7419 < 0$ | $6.36 \times 10^{-16}$ |
| $K=4$ | $300$ | $0.356675$ | $107$ | $+1.3709 > 0$ | $-9.3573 < 0$ | $+4.1686 > 0$ | $-8.5378 < 0$ | $4.97 \times 10^{-14}$ |
| $K=4$ | $350$ | $0.510826$ | $152$ | $+0.3304 > 0$ | $-17.0094 < 0$ | $+3.6865 > 0$ | $-15.8239 < 0$ | $1.18 \times 10^{-12}$ |
| $K=4$ | $380$ | $0.593064$ | $175$ | $+0.2343 > 0$ | $-21.1335 < 0$ | $+1.5961 > 0$ | $-19.9004 < 0$ | $4.76 \times 10^{-12}$ |

### 2.3 Davenport–Heilbronn Control Separation on Signed Legendre Matrices

For any Dirichlet series $F(s) = \sum_{n=1}^\infty a_n n^{-s}$ with generalized von Mangoldt coefficients $\Lambda_D(n)$ defined by $\sum_{d \mid n} \Lambda_D(d) a_{n/d} = a_n \log n$, the preconditioned arithmetic shift operator $L_{\mathcal{P}_K}(-W_D)$ on $L^2(-b, b)$ ($2b < \log 2$) has exact shift expansion
$$L_{\mathcal{P}_K}(-W_D) = Q_D(1) I + \sum_{1 < q < e^{2b}} Q_D(q) (S_{\log q} + S_{-\log q}),$$
where, because $\operatorname{supp}(L_{\mathcal{P}_K}) \subset [1/P_K, P_K]$, only integers $2 \le n \le 2 P_K$ can produce shifts $q = rn$ or $q = r/n$ in $(1/2, 2)$:
$$Q_D(q) = -\sum_{r \in \operatorname{supp}(L_{\mathcal{P}_K})} \sum_{n=2}^{2 P_K} \ell_r \frac{\Lambda_D(n)}{\sqrt{n}} \left(\delta_{q, rn} + \delta_{q, r/n}\right).$$
- For Riemann $\zeta(s)$ ($\Lambda_\zeta(n) = \Lambda(n)$), this truncated Dirichlet convolution agrees identically with the infinite-tower Euler collapse formula (`build_q_terms_arb`) for every $q \in [1, 2)$.
- For the Davenport–Heilbronn function $L_{DH}(s)$ under $K = 3$ ($\mathcal{P}_3 = \{2, 3, 5\}$, $P_3 = 30$), $C_{\mathrm{diag}, DH}(\{2, 3, 5\}) = \frac{6}{5} C_{\mathrm{diag}, DH}(\{2, 3\}) \approx -0.834000 < 0$, and across all $N \in \{36, 40, 42, 45, 50\}$ both even and odd signed arithmetic Legendre matrices $W_{\mathrm{arith}, DH}^{(4, \mathrm{even})}(b)$ and $W_{\mathrm{arith}, DH}^{(4, \mathrm{odd})}(b)$ have strictly negative $(0, 0)$ diagonal entries and certified minimum eigenvalues $\lambda_{\min} \in [-2.5105, -1.0558] < 0$.
