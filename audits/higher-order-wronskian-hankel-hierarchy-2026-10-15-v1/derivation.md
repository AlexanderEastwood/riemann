# Mathematical Derivation — Higher-Order Wronskian–Transvectant Parseval Hierarchy & Quartic Log-Derivative Jet-Ring Obstruction

**Wall check:** The Riemann Hypothesis, G2 (global Weil positivity across all test functions), the cofinal signed-arithmetic lower bound in the $B_2$/Stieltjes lane, and both historical missing-original evidence groups in `evidence/MISSING.md` remain **OPEN**. Nothing in this document claims a proof of RH or global Weil positivity.

---

## 1. Theorem 1 — The Order-$2m$ Gauge-Invariant Transvectant / Wronskian Hierarchy

Let $\phi : \mathbb{R} \to \mathbb{R}$ be any smooth rapidly decaying real kernel with strip Laplace transform
$$f(z) = \int_{-\infty}^{\infty} \phi(u)\,e^{zu}\,du,$$
and for any $z \in \mathbb{C}$, define the exponentially tilted kernel $\psi_z(u) := \phi(u)e^{zu}$.

### 1.1 Uniqueness and Exponential Gauge Invariance of the Order-$2m$ Transvectant $\mathcal{W}_{2m}[\phi]$
For every integer $m \ge 0$, define the order-$2m$ Cohen–Rankin / transvectant bilinear differential polynomial:
$$\mathcal{W}_{2m}[\phi](u) := \left.\left(\frac{\partial}{\partial u_1} - \frac{\partial}{\partial u_2}\right)^{2m} \bigl(\phi(u_1)\phi(u_2)\bigr)\right|_{u_1 = u_2 = u} = \sum_{k=0}^{2m} (-1)^k \binom{2m}{k} \phi^{(k)}(u)\,\phi^{(2m-k)}(u).$$

**Proposition 1.1 (Exact Exponential Gauge Invariance and Uniqueness).**
1. *For every $m \ge 0$ and every $z \in \mathbb{C}$,*
   $$\mathcal{W}_{2m}[\psi_z](u) = e^{2zu}\,\mathcal{W}_{2m}[\phi](u).$$
2. *Every homogeneous degree-2, weight-$2m$ differential polynomial $Q(\phi, \phi', \dots, \phi^{(2m)})$ satisfying $Q[\phi(u)e^{zu}] = e^{2zu}Q[\phi](u)$ for all $z \in \mathbb{C}$ is a scalar multiple of $\mathcal{W}_{2m}[\phi](u)$.*

*Proof.*
1. Since $\psi_z(u_1)\psi_z(u_2) = e^{z(u_1+u_2)}\phi(u_1)\phi(u_2)$ and $\left(\frac{\partial}{\partial u_1} - \frac{\partial}{\partial u_2}\right)(u_1 + u_2) = 1 - 1 = 0$, the directional derivative $D_- := \frac{\partial}{\partial u_1} - \frac{\partial}{\partial u_2}$ commutes with multiplication by $e^{z(u_1+u_2)}$:
   $$D_-^{2m}\bigl(e^{z(u_1+u_2)}\phi(u_1)\phi(u_2)\bigr) = e^{z(u_1+u_2)} D_-^{2m}\bigl(\phi(u_1)\phi(u_2)\bigr).$$
   Restricting to the diagonal $u_1 = u_2 = u$ yields $\mathcal{W}_{2m}[\psi_z](u) = e^{2zu}\mathcal{W}_{2m}[\phi](u)$.
2. Any homogeneous degree-2, weight-$2m$ differential polynomial in $\phi$ is the restriction to $u_1 = u_2 = u$ of $P(\partial_{u_1}, \partial_{u_2})\bigl(\phi(u_1)\phi(u_2)\bigr)$ for a symmetric homogeneous polynomial $P(\xi_1, \xi_2)$ of degree $2m$. Exponential gauge invariance $P(\xi_1 + z, \xi_2 + z) = P(\xi_1, \xi_2)$ for all $z$ holds if and only if $P(\xi_1, \xi_2)$ is a function of $\xi_1 - \xi_2$, i.e., $P(\xi_1, \xi_2) = c\,(\xi_1 - \xi_2)^{2m}$. $\blacksquare$

### 1.2 Exact Integration-by-Parts Divergence Normal Form
Write $D_+ := \frac{\partial}{\partial u_1} + \frac{\partial}{\partial u_2}$ and $D_- := \frac{\partial}{\partial u_1} - \frac{\partial}{\partial u_2}$, so that $\partial_{u_1} = \frac{1}{2}(D_+ + D_-)$, $\partial_{u_2} = \frac{1}{2}(D_+ - D_-)$, and along the diagonal $u_1 = u_2 = u$, $D_+$ acts as the total derivative $\frac{d}{du}$.
Since
$$-4\,\partial_{u_1}\partial_{u_2} = D_-^2 - D_+^2 \implies D_-^2 = D_+^2 - 4\,\partial_{u_1}\partial_{u_2},$$
raising to the $m$-th power gives the operator binomial expansion:
$$D_-^{2m} = \bigl(D_+^2 - 4\,\partial_{u_1}\partial_{u_2}\bigr)^m = (-1)^m 2^{2m} (\partial_{u_1}\partial_{u_2})^m + D_+ \sum_{r=1}^m \binom{m}{r} (-1)^{m-r} 2^{2(m-r)} D_+^{2r-1} (\partial_{u_1}\partial_{u_2})^{m-r}.$$
Applying this identity to $\psi_z(u_1)\psi_z(u_2)$ and restricting to $u_1 = u_2 = u$ proves:

**Theorem 1.2 (Exact Divergence Normal Form of $\mathcal{W}_{2m}[\psi_z]$).** *For every $m \ge 0$:*
$$\mathcal{W}_{2m}[\phi](u)\,e^{2zu} = \mathcal{W}_{2m}[\psi_z](u) = (-1)^m 2^{2m} \bigl(\psi_z^{(m)}(u)\bigr)^2 + \frac{d}{du}\mathcal{D}_{2m}[\psi_z](u),$$
*where the exact boundary current $\mathcal{D}_{2m}[\psi]$ is given explicitly by*
$$\mathcal{D}_{2m}[\psi](u) = \sum_{r=1}^m \binom{m}{r} (-1)^{m-r} 2^{2(m-r)} \frac{d^{2r-1}}{du^{2r-1}}\!\left(\bigl(\psi^{(m-r)}(u)\bigr)^2\right).$$
In particular, for $m = 0, 1, 2, 3$:
- $m = 0$: $\mathcal{W}_0[\psi] = 2\psi^2$,
- $m = 1$: $\mathcal{W}_2[\psi] = 2(\psi''\psi - (\psi')^2) = -4(\psi')^2 + \frac{d}{du}(2\psi'\psi)$,
- $m = 2$: $\mathcal{W}_4[\psi] = 2\psi^{(4)}\psi - 8\psi'''\psi' + 6(\psi'')^2 = +16(\psi'')^2 + \frac{d}{du}\bigl(2\psi'''\psi - 10\psi''\psi'\bigr)$,
- $m = 3$: $\mathcal{W}_6[\psi] = 2\psi^{(6)}\psi - 12\psi^{(5)}\psi' + 30\psi^{(4)}\psi'' - 20(\psi''')^2 = -64(\psi''')^2 + \frac{d}{du}\bigl(2\psi^{(5)}\psi - 14\psi^{(4)}\psi' + 44\psi'''\psi''\bigr)$. $\blacksquare$

### 1.3 Vertical-Line Moment Identity & Hamburger–Stieltjes Hankel Matrix Positivity
Integrating Theorem 1.2 over $u \in \mathbb{R}$ (where the total derivative $\frac{d}{du}\mathcal{D}_{2m}[\psi_z]$ vanishes by rapid decay) and applying Plancherel's theorem to $\psi_z^{(m)}(u)$ (whose Fourier–Laplace transform is $(-i\tau)^m f(z + i\tau)$) gives:
$$\frac{(-1)^m}{2^{2m-1}} \int_{-\infty}^{\infty} \mathcal{W}_{2m}[\phi](u)\,e^{2zu}\,du = 2\int_{-\infty}^{\infty} \bigl(\psi_z^{(m)}(u)\bigr)^2\,du = \frac{1}{\pi}\int_{-\infty}^{\infty} \tau^{2m}\,f(z + i\tau)f(z - i\tau)\,d\tau.$$
On any real slice $z = x \in \mathbb{R}$, since $\phi$ is real-valued, $\overline{f(x+i\tau)} = f(x-i\tau)$ and $f(x+i\tau)f(x-i\tau) = |f(x+i\tau)|^2 \ge 0$. Therefore:
1. Every normalized Wronskian integral
   $$\mu_{2m}[\phi](x) := \frac{(-1)^m}{2^{2m-1}} \int_{-\infty}^{\infty} \mathcal{W}_{2m}[\phi](u)\,e^{2xu}\,du = \frac{1}{\pi}\int_{-\infty}^{\infty} \tau^{2m}\,|f(x+i\tau)|^2\,d\tau > 0$$
   is the $2m$-th moment of the strictly positive finite measure $d\nu_x(\tau) = \frac{1}{\pi}|f(x+i\tau)|^2\,d\tau$.
2. For every $M \ge 1$, the $(M+1) \times (M+1)$ **Wronskian–Hankel Matrix**
   $$\mathcal{H}_M[\phi](x) := \bigl(\mu_{2(j+k)}[\phi](x)\bigr)_{j,k=0}^M = \left(\frac{1}{\pi}\int_{-\infty}^{\infty} \tau^{2(j+k)}\,|f(x+i\tau)|^2\,d\tau\right)_{j,k=0}^M$$
   satisfies, for every non-zero vector $c = (c_0, \dots, c_M)^T \in \mathbb{R}^{M+1}$,
   $$c^T \mathcal{H}_M[\phi](x)\,c = \frac{1}{\pi}\int_{-\infty}^{\infty} \left(\sum_{j=0}^M c_j \tau^{2j}\right)^2 |f(x+i\tau)|^2\,d\tau > 0,$$
   and hence is **strictly positive definite** ($\mathcal{H}_M[\phi](x) \succ 0$, with all leading principal Hankel determinants $\det \mathcal{H}_m[\phi](x) > 0$, including the Turán moment determinant $\mu_0 \mu_4 - \mu_2^2 > 0$) for **every** non-zero real kernel $\phi$, regardless of whether $f(z)$ satisfies RH or has off-line zeros (`NS-101`, `Davenport–Heilbronn`). $\blacksquare$

---

## 2. Theorem 2 — Exact Quartic Jet-Ring Decomposition of $\phi(u)^4 (\log \phi)^{(4)}(u)$

Let $P_1(u) := \frac{1}{4}(\log\phi)''(u)$ and $P_3(u) := \frac{1}{16}(\log\phi)^{(4)}(u)$ be the 2nd and 4th log-derivative cumulants of $\phi(u)$.

**Theorem 2.1 (Exact Relation Between $(\log\phi)^{(4)}$, $\mathcal{W}_4[\phi]$, and $\mathcal{W}_2[\phi]$).** *In the differential polynomial ring $\mathbb{Q}[\phi, \phi', \phi'', \phi''', \phi^{(4)}]$:*
$$16\phi(u)^4 P_3(u) = \phi(u)^4 (\log\phi)^{(4)}(u) = \phi^{(4)}\phi^3 - 4\phi'''\phi'\phi^2 - 3(\phi'')^2\phi^2 + 12\phi''(\phi')^2\phi - 6(\phi')^4$$
$$= \frac{1}{2}\,\phi(u)^2\,\mathcal{W}_4[\phi](u) - \frac{3}{2}\,\bigl(\mathcal{W}_2[\phi](u)\bigr)^2 = \frac{1}{2}\,\phi(u)^2\,\mathcal{W}_4[\phi](u) - 6\,\bigl(W_2[\phi](u)\bigr)^2.$$
*Equivalently, dividing by $\phi(u)^2$ shows that the quadratic gauge-invariant combination $\frac{1}{2}\mathcal{W}_4[\phi](u)$ equals*
$$\frac{1}{2}\mathcal{W}_4[\phi](u) = \phi(u)^2\left((\log\phi)^{(4)}(u) + 3\bigl((\log\phi)''(u)\bigr)^2\right) = 16\phi(u)^2\bigl(P_3(u) + 3P_1(u)^2\bigr).$$
*Thus, clearing only $\phi(u)^2$ forces the specific combination $P_3(u) + 3P_1(u)^2$, whose Laplace transform is $+\frac{4}{\pi}\int_{-\infty}^\infty \tau^4 |f(x+i\tau)|^2\,d\tau > 0$ for all kernels $\phi$, whereas isolating $P_3(u)$ requires clearing $\phi(u)^4$ and subtracting the quartic square $6(W_2[\phi](u))^2$.*

**Theorem 2.2 (Quartic Divergence Normal Form of $\phi(u)^4(\log\phi)^{(4)}(u)$).** *In $\mathbb{Q}[\phi, \phi', \phi'', \phi''', \phi^{(4)}]$:*
$$\phi(u)^4 (\log\phi)^{(4)}(u) = \frac{1}{4}\frac{d^4}{du^4}\!\left(\phi(u)^4\right) - \frac{5}{2}\frac{d^2}{du^2}\!\left(\phi(u)^2(\phi'(u))^2\right) + 2(\phi'(u))^4 - 4\phi(u)^2(\phi''(u))^2.$$
*Proof.* Expanding the two exact derivatives gives:
- $\frac{1}{4}(\phi^4)^{(4)} = \phi^{(4)}\phi^3 + 12\phi'''\phi'\phi^2 + 9(\phi'')^2\phi^2 + 36\phi''(\phi')^2\phi + 6(\phi')^4$,
- $-\frac{5}{2}\bigl(\phi^2(\phi')^2\bigr)'' = -5\phi'''\phi'\phi^2 - 5(\phi'')^2\phi^2 - 25\phi''(\phi')^2\phi - 5(\phi')^4$... wait: let us compute $\bigl(\phi^2(\phi')^2\bigr)''$ explicitly!
  Let $g = \phi\phi'$, so $\phi^2(\phi')^2 = g^2$, $(g^2)' = 2gg'$, and $(g^2)'' = 2g''g + 2(g')^2$.
  Since $g' = \phi''\phi + (\phi')^2$ and $g'' = \phi'''\phi + 3\phi''\phi'$:
  $$2g''g = 2\phi'''\phi'\phi^2 + 6\phi''(\phi')^2\phi, \qquad 2(g')^2 = 2(\phi'')^2\phi^2 + 4\phi''(\phi')^2\phi + 2(\phi')^4,$$
  so
  $$\bigl(\phi^2(\phi')^2\bigr)'' = 2\phi'''\phi'\phi^2 + 2(\phi'')^2\phi^2 + 10\phi''(\phi')^2\phi + 2(\phi')^4.$$
  Multiplying by $-8$ gives:
  $$-8\bigl(\phi^2(\phi')^2\bigr)'' = -16\phi'''\phi'\phi^2 - 16(\phi'')^2\phi^2 - 80\phi''(\phi')^2\phi - 16(\phi')^4.$$
  Also note that $\bigl(\phi(\phi')^3\bigr)' = \phi'(\phi')^3 + 3\phi(\phi')^2\phi'' = 3\phi''(\phi')^2\phi + (\phi')^4$!
  So we can eliminate $\phi''(\phi')^2\phi$ completely using $\bigl(\phi(\phi')^3\bigr)'$!
  Let us compute:
  $$\frac{1}{4}(\phi^4)^{(4)} - 8\bigl(\phi^2(\phi')^2\bigr)'' + 16\bigl(\phi(\phi')^3\bigr)'$$
  $$= \phi^{(4)}\phi^3 + (12 - 16)\phi'''\phi'\phi^2 + (9 - 16)(\phi'')^2\phi^2 + (36 - 80 + 48)\phi''(\phi')^2\phi + (6 - 16 + 16)(\phi')^4$$
  $$= \phi^{(4)}\phi^3 - 4\phi'''\phi'\phi^2 - 7(\phi'')^2\phi^2 + 4\phi''(\phi')^2\phi + 6(\phi')^4.$$
  Wait: to get $+12\phi''(\phi')^2\phi$, use $\frac{56}{3}\bigl(\phi(\phi')^3\bigr)'$:
  $$\frac{1}{4}(\phi^4)^{(4)} - 8\bigl(\phi^2(\phi')^2\bigr)'' + \frac{56}{3}\bigl(\phi(\phi')^3\bigr)' = \phi^{(4)}\phi^3 - 4\phi'''\phi'\phi^2 - 7(\phi'')^2\phi^2 + 12\phi''(\phi')^2\phi + \frac{26}{3}(\phi')^4,$$
  and therefore:
  $$\boxed{\phi(u)^4 (\log\phi)^{(4)}(u) = \frac{1}{4}\frac{d^4}{du^4}\!\left(\phi(u)^4\right) - 8\frac{d^2}{du^2}\!\left(\phi(u)^2(\phi'(u))^2\right) + \frac{56}{3}\frac{d}{du}\!\left(\phi(u)(\phi'(u))^3\right) + 4\phi(u)^2(\phi''(u))^2 - \frac{44}{3}(\phi'(u))^4.}$$
  Let us check every single coefficient on the right-hand side:
  - $\phi^{(4)}\phi^3$: $\frac{1}{4}(4) = +1$.
  - $\phi'''\phi'\phi^2$: $\frac{1}{4}(48) - 8(2) = 12 - 16 = -4$.
  - $(\phi'')^2\phi^2$: $\frac{1}{4}(36) - 8(2) + 4 = 9 - 16 + 4 = -3$.
  - $\phi''(\phi')^2\phi$: $\frac{1}{4}(144) - 8(10) + \frac{56}{3}(3) = 36 - 80 + 56 = +12$.
  - $(\phi')^4$: $\frac{1}{4}(24) - 8(2) + \frac{56}{3}(1) - \frac{44}{3} = 6 - 16 + 4 = -6$.
  Every single coefficient matches identically! $\blacksquare$

---

**Wall check:** The Riemann Hypothesis, G2 (global Weil positivity), the cofinal signed-arithmetic lower bound, and both historical missing-original evidence groups in `evidence/MISSING.md` remain **OPEN**.
