# Four-lane mathematical & dependency audit (October 14, 2026)

Reviewed public baseline: `2d5638ed3b56ab2375162bb072f4866ad5bdfe6d` (`origin/main`, Manuscript v1.66, 358 pages).
Isolated worktree: `/Users/alex/riemann-worktrees/origin-main-review` (branch `codex/four-lane-audit-20261014`).
Dirty primary workspace `/Users/alex/Documents/ChatGPT/riemann` (`HEAD` at `50f6f21`) preserved untouched.

**Wall check: Same open gap.** Closest results: NS51/53/55/57/58/61/74/78/80/83/87/98/100/101, PR76–81. What changes: three exact algebraic/operator reductions and two narrower structural obstructions (`Known wall` for the linearized two-shift Jacobi moment $B_p(r)$ in `01-jacobi-transfer.md` as a Jacobi-specific invariant, and `Known wall` for pure interior finite-prime-product annihilation $L_{\mathcal{P}} : V_{a-\ell_{\mathcal{P}}} \to V_a$ removing all active window primes). No new cofinal signed-arithmetic lower bound is claimed. **RH, G2, the cofinal signed-arithmetic lower bound, and both historical missing-original evidence groups (`evidence/MISSING.md`) remain OPEN.**

---

## Lane 1 — `NB-GAIN` / `COEFF`: Exact Rational Constants and Untruncated Schur–Rayleigh Equivalence

### 1.1 Exact rational constants for the compact divisor-moment dual (`Proposal 04` / `Review 10`)

Fix the smooth compact profile
$$b(s) = (s-1)^3(2-s)^3(2s-3)\,\mathbf{1}_{[1,2]}(s).$$
In centered coordinates $u = s - 3/2 \in [-1/2, 1/2]$,
$$b(3/2+u) = 2u\left(\frac{1}{4}-u^2\right)^3 = -2u^7 + \frac{3}{2}u^5 - \frac{3}{8}u^3 + \frac{1}{32}u.$$
This is an odd polynomial in $u$ vanishing to third order at $u = \pm 1/2$, so $\int_1^2 b(s)\,ds = 0$ and $b, b', b''$ vanish at $s=1,2$.
For dyadic $N = 2^j \ge 16$, let $\beta_N(t) = b(t/N)$ and
$$\psi_N(t) = -t^2(t\beta_N'(t))' = -N s^2\left[b'(s) + s b''(s)\right]_{s=t/N}.$$

Exact rational polynomial integration (`verify_four_lanes.py`) yields:
1. **Complete $L^2((0,\infty), dt/t^2)$ norm constant**:
   $$C_b = \int_1^2 s^2\left[b'(s) + s b''(s)\right]^2 ds = \frac{6904}{45045} \approx 0.15326895326895326.$$
2. **Exact rational total variation of $b'''$ on $\mathbb{R}$ and alias constant $A_b$**:
   Because $b'''(3/2+u) = -420u^4 + 90u^2 - \frac{9}{4}$ is an even polynomial in $u^2$ and $b^{(4)}(3/2+u) = -60u(28u^2-3)$ vanishes in $(-1/2, 1/2)$ precisely at $u = 0$ and $u^2 = \frac{3}{28}$, the local extrema of $b'''$ on $[1,2]$ are **exact rational numbers**:
   $$b'''(1^+) = b'''(2^-) = -6, \qquad b'''\left(\frac{3}{2}\pm\sqrt{\frac{3}{28}}\right) = -420\left(\frac{9}{784}\right) + 90\left(\frac{3}{28}\right) - \frac{9}{4} = \frac{18}{7}, \qquad b'''\left(\frac{3}{2}\right) = -\frac{9}{4}.$$
   Including the two endpoint jumps $|b'''(1^+)| = |b'''(2^-)| = 6$ of the zero extension,
   $$\operatorname{Var}_{\mathbb{R}}(b''') = 6 + 6 + 2\left(\frac{18}{7} - (-6)\right) + 2\left(\frac{18}{7} - \left(-\frac{9}{4}\right)\right) = \frac{543}{14} \approx 38.785714285714285,$$
   and since $\frac{2\zeta(4)}{(2\pi)^4} = \frac{2(\pi^4/90)}{16\pi^4} = \frac{1}{720}$, the alias bound constant $|\lambda_N(n)| \le A_b (n/N)^3$ ($1 \le n \le N$) is the **exact rational**:
   $$A_b = \frac{1}{720}\cdot\frac{543}{14} = \frac{181}{3360} \approx 0.05386904761904762.$$
3. **Exact diagonal $n^{-4}$-comparison integral**:
   $$I_{\mathrm{diag}} = \int_1^2 s^4 b(s)^2\,ds = \frac{1219}{38798760} \approx 3.1418529870542255 \times 10^{-5}.$$

### 1.2 Untruncated Schur–Rayleigh equivalence on $V_{2N} \cap V_N^\perp$

In `Proposal 04` (`04-proposal-dual.md`), the author truncated $M_N(v) = \sum_{n \le 2N} \lambda_N(n) v_n$ below $K = \lfloor \sqrt{N} \rfloor$ to define $M_N^{\mathrm{hi}}(v)$, paying an extra alias cost $\sqrt{B} A_b N^{-1/4}$ ($B = 1536\zeta(2)^2$) so that $|M_N^{\mathrm{hi}}(v)|^2 \le D_N \|f_v\|^2$ with $D_N = (\sqrt{C_b N} + \sqrt{B}A_b N^{-1/4})^2$.

However, on **any** old-orthogonal synthesis $f_v = \sum_{n=N+1}^{2N} y_n \phi_n \in V_{2N} \cap V_N^\perp$ (where $\phi_n = (I-\Pi_N)a_n$ and $v = (u, y)$ has the exact old refit $u = -G^{-1}C y$), the **untruncated** linear functional $M_N(u, y) = \langle f_v, \psi_N \rangle$ satisfies:
$$M_N(u, y) = \lambda_{\mathrm{old}}^T u + \lambda_{\mathrm{new}}^T y = \left(\lambda_{\mathrm{new}} - C^T G^{-1} \lambda_{\mathrm{old}}\right)^T y =: \tilde{\lambda}_N^T y,$$
where $(\lambda_{\mathrm{new}})_n = b(n/N)$ ($N < n \le 2N$) and $(\tilde{\lambda}_N)_n = \langle \phi_n, \psi_N \rangle$.

Because $\Pi_{2N} - \Pi_N$ is the orthogonal projection onto $V_{2N}\cap V_N^\perp = \operatorname{span}\{\phi_{N+1},\dots,\phi_{2N}\}$ with Gram matrix $S = D - C^T G^{-1} C$, the projection $(\Pi_{2N}-\Pi_N)\psi_N$ has $\phi$-coordinates $w_{\psi_N} := S^{-1}\tilde{\lambda}_N$ and squared norm:
$$\|(\Pi_{2N} - \Pi_N)\psi_N\|_{\mathcal{H}}^2 = \tilde{\lambda}_N^T S^{-1} \tilde{\lambda}_N = w_{\psi_N}^T S w_{\psi_N} \le \|\psi_N\|_{\mathcal{H}}^2 - \|\Pi_N \psi_N\|_{\mathcal{H}}^2 = C_b N - \lambda_{\mathrm{old}}^T G^{-1}\lambda_{\mathrm{old}} \le C_b N.$$
Consequently:
1. **Zero alias-truncation loss on $V_{2N}\cap V_N^\perp$**: For every $v = (-G^{-1}C y, y)$,
   $$|M_N(u, y)|^2 = |\tilde{\lambda}_N^T y|^2 \le \left(\tilde{\lambda}_N^T S^{-1}\tilde{\lambda}_N\right) (y^T S y) \le \left(C_b N - \lambda_{\mathrm{old}}^T G^{-1}\lambda_{\mathrm{old}}\right) \|f_v\|_{\mathcal{H}}^2 \le C_b N \|f_v\|_{\mathcal{H}}^2,$$
   strictly improving $D_N = (\sqrt{C_b N} + \sqrt{B}A_b N^{-1/4})^2$ at every $N$ (at $N=16$, $C_b N \approx 2.4523$ vs. $D_{16} \approx 10.9058$) while retaining all old indices $1 \le m \le N$.
2. **Exact Rayleigh-quotient isomorphism**: For the actual optimizer increment $y = S^{-1} h$ ($h = b_{\mathrm{new}} - C^T G^{-1} b_{\mathrm{old}}$),
   $$M_N(u, y) = \tilde{\lambda}_N^T S^{-1} h = w_{\psi_N}^T h = \langle (\Pi_{2N}-\Pi_N)\psi_N, r_N \rangle = \langle (\Pi_{2N}-\Pi_N)\psi_N, \tau \rangle,$$
   and the subspace Cauchy–Schwarz lower bound on $\Delta_N = h^T S^{-1} h$ is identically the Rayleigh quotient along $w_{\psi_N} = S^{-1}\tilde{\lambda}_N$:
   $$\Delta_N \ge \frac{(w_{\psi_N}^T h)^2}{w_{\psi_N}^T S w_{\psi_N}} = \frac{(\tilde{\lambda}_N^T S^{-1} h)^2}{\tilde{\lambda}_N^T S^{-1} \tilde{\lambda}_N} \ge \frac{|M_N(u,y)|^2}{C_b N}.$$
   This shows why writing $M_N(u,y)$ in optimizer coordinates $(u,y)$ does not bypass $S^{-1}$: the compact dual $\psi_N$ supplies an explicit $O(N)$ upper bound on the denominator $\tilde{\lambda}_N^T S^{-1}\tilde{\lambda}_N \le C_b N$, while the numerator $\tilde{\lambda}_N^T S^{-1} h$ still contains the full inverse Schur complement $S^{-1}$ acting on the corrected target load $h$.
3. **Direct `NS-87` localization at $T = N^6$ without `NS-78`'s $B$ factor**: Setting $\widehat{M}_{N,T} := \tilde{\lambda}_N^T S^{-1} \widehat{h}_{N,T}$ where $\widehat{h}_{N,T} = q_{\mathrm{new}}(T) - C^T G^{-1} q_{\mathrm{old}}(T)$, Cauchy–Schwarz in $S^{-1}$ gives directly:
   $$\frac{|M_N(u,y) - \widehat{M}_{N,T}|}{\sqrt{C_b N}} \le \frac{\|\tilde{\lambda}_N\|_{S^{-1}}}{\sqrt{C_b N}} \|h - \widehat{h}_{N,T}\|_{S^{-1}} \le \|h - \widehat{h}_{N,T}\|_{S^{-1}} \le \sqrt{F_N(T)}.$$

---

## Lane 2 — `KERNEL-API` / `WEIL-FLOOR`: Interior Adjoint Recurrence $L_p : V_{a-\ell} \to V_a$ and the Multi-Prime Support Barrier

### 2.1 Pole-free interior adjoint embedding

Let $I = (-a, a)$ and $V_a = \{f \in L^2(I) : \int_{\mathbb{R}} \log(2+|\xi|)|\widehat{E_a f}(\xi)|^2\,d\xi < \infty\}$.
On compactly supported distributions, decompose the full Weil operator as
$$W = W_0 + K_{\mathrm{pole}}, \qquad W_0 = \alpha(D) - \sum_{n \ge 2} \frac{\Lambda(n)}{\sqrt{n}}(T_{\log n} + T_{-\log n}),$$
where $W_0$ is translation-invariant and $K_{\mathrm{pole}} F(x) = 2\cosh(x/2)\int \cosh(y/2)F(y)\,dy - 2\sinh(x/2)\int \sinh(y/2)F(y)\,dy$.

For any prime $p$ with $\ell = \log p < a$ and $r = p^{-1/2}$, define
$$L_p = (1+r^2)I - r(T_\ell + T_{-\ell}).$$
In `05-euler-api.md`, $L_p$ was applied forward to a hypothetical nullvector $F = E_a f \in V_a$, expanding support to $[-a-\ell, a+\ell]$ and forcing an exterior recompression $\chi L_p F$ that restored $K_{\mathrm{pole}}(\chi L_p F)$ and $[W, \chi] L_p F$.

Instead, consider the **interior adjoint embedding**:
$$L_p : V_{a-\ell} \longrightarrow V_a, \qquad g \longmapsto L_p E_{a-\ell} g \qquad (a > \ell = \log p).$$
1. **Exact support and form-domain preservation**: For every $g \in V_{a-\ell}$, $\operatorname{supp}(L_p E_{a-\ell} g) \subset [-a, a]$, parity is preserved, and $|\widehat{L_p E_{a-\ell} g}(\xi)| \le (1+r)^2 |\widehat{E_{a-\ell} g}(\xi)|$, so $L_p(V_{a-\ell}) \subset V_a$ with **no cutoff $\chi$ and no exterior truncation**.
2. **Exact pole annihilation on $V_{a-\ell}$**: Because $(1+r^2) - 2r\cosh(\ell/2) = 1 + p^{-1} - p^{-1/2}(p^{1/2}+p^{-1/2}) = 0$, $L_p(e^{\pm x/2}) = 0$, whence
   $$K_{\mathrm{pole}}(L_p E_{a-\ell} g) = 0 \quad \text{and} \quad \langle W L_p E_{a-\ell} g, L_p E_{a-\ell} g \rangle = \langle L_p^2 W_0 E_{a-\ell} g, E_{a-\ell} g \rangle \qquad \forall g \in V_{a-\ell}.$$
3. **Exact nullvector projection on $(-a+\ell, a-\ell)$**: If $F = E_a f \in V_a$ is a hypothetical nullvector ($P_a W F = 0$ on $I$), then for every $g \in V_{a-\ell}$,
   $$0 = \langle W F, L_p E_{a-\ell} g \rangle = \langle W_0 F, L_p E_{a-\ell} g \rangle = \langle L_p W_0 F, E_{a-\ell} g \rangle,$$
   so $P_{a-\ell} L_p W_0 F = 0$ on $(-a+\ell, a-\ell)$ with zero pole contribution and with the $p$-chain collapsed via $L_p C_p = (1-r^2)I$.

### 2.2 Theorem (Multi-Prime Interior Support Barrier)

Can a commuting product $L_{\mathcal{P}} := \prod_{p \in \mathcal{P}} L_p : V_{a-\ell_{\mathcal{P}}} \to V_a$ ($\ell_{\mathcal{P}} = \sum_{p \in \mathcal{P}} \log p$) simultaneously maintain a nonempty interior test space ($a > \ell_{\mathcal{P}}$) and annihilate all prime chains $C_q$ active on $I = (-a,a)$?

**Proposition.** *For every $a > 0$ and every finite set of primes $\mathcal{P}$ satisfying $\ell_{\mathcal{P}} = \sum_{p \in \mathcal{P}} \log p < a$, there exists at least one prime $q \notin \mathcal{P}$ such that $\log q < 2a - \ell_{\mathcal{P}} < 2a$, so the $q$-chain $L_{\mathcal{P}}(C_q - I)$ is nontrivially active in the interior equation $P_{a-\ell_{\mathcal{P}}} L_{\mathcal{P}} W_0 F = 0$.*

*Proof.* If $\mathcal{P} = \emptyset$, then $\ell_{\mathcal{P}} = 0$, and for $a > \frac{1}{2}\log 2$ the prime $q=2$ has $\log 2 < 2a$. Suppose $\mathcal{P} \ne \emptyset$ and let $P_{\max} = \max \mathcal{P} \ge 2$. If $\{2, 3, \dots, P_{\max}\} \not\subset \mathcal{P}$, the smallest omitted prime $q < P_{\max}$ satisfies $\log q < \log P_{\max} \le \ell_{\mathcal{P}} < a < 2a - \ell_{\mathcal{P}}$. Otherwise $\mathcal{P}$ contains all primes up to $P_{\max}$, so $\exp(\ell_{\mathcal{P}}) = \prod_{p \in \mathcal{P}} p$.
- If $\mathcal{P} = \{2\}$, then $a > \log 2$ implies $2a > \log 4 > \log 3$, and for $q=3$, $\log 3 < 2a - \log 2$ holds whenever $a > \frac{1}{2}\log 6 \approx 0.89588$ (while on $I = (-a,a)$ itself, $\log 3 \approx 1.09861 < 2\log 2 \approx 1.38629 < 2a$ holds for **every** $a > \log 2$).
- If $|\mathcal{P}| \ge 2$, then $P_{\max} \ge 3$ and $\prod_{p \in \mathcal{P}} p \ge 2 P_{\max}$. By Bertrand's postulate, there is a prime $q \notin \mathcal{P}$ with $P_{\max} < q < 2 P_{\max} \le \prod_{p \in \mathcal{P}} p = e^{\ell_{\mathcal{P}}}$, hence $\log q < \ell_{\mathcal{P}} < a < 2a - \ell_{\mathcal{P}} < 2a$. $\square$

**Consequence (`Known wall` for pure interior finite-prime-product elimination)**: No finite product $L_{\mathcal{P}}$ of interior Euler difference operators can clear all active primes on a finite window without exhausting the window width $a$. Any `KERNEL-API` injectivity proof using $L_p$ must therefore estimate the coupled remaining prime chains $\sum_{q \ne p} (\log q) L_p(C_q - I)$ together with $\alpha(D)$, rather than algebraic elimination alone.

---

## Lane 3 — `ZERO-GEOMETRY`: Tautological Collapse of the Two-Shift Moment $B_p(r)$ in `01-jacobi-transfer.md`

### 3.1 Statement of the Tautological Collapse Theorem

In `01-jacobi-transfer.md` (and `theta-orbit-followup-2026-10-05-v1` / `PR #72`), let $\phi(u) = \Phi(u/2)$ ($L = 2u$), $G(L) = \log \Phi(L/4)$, $P(L) = G'(L)$, $P_1(L) = P'(L)$, $K(p,t) = \phi(p+t)\phi(p-t)$, and
$$A_p(r) = \int_0^\infty K(p,t)\cos(2rt)\,dt, \qquad B_p(r) = \int_0^\infty P(2(p+t))P(2(p-t))K(p,t)\cos(2rt)\,dt.$$
The October 5 reviews derived:
$$\frac{d^2 A_p(r)}{dp^2} + 4r^2 A_p(r) = 16 B_p(r), \tag{1}$$
$$(x^2+r^2)J(x,r) = 32\int_0^\infty p\sinh(2xp) B_p(r)\,dp - x|f(x+ir)|^2, \tag{2}$$
$$\frac{d B_p(r)}{dp} = 2\int_0^\infty K(p,t)\left[(P_+ + P_-)P_+ P_- + P_{1+}P_- + P_+ P_{1-}\right]\cos(2rt)\,dt, \tag{3}$$
and identified $32\int_0^\infty p\sinh(2xp)B_p(r)\,dp \ge x|f(x+ir)|^2$ as the main Jacobi-trajectory lead.

**Theorem (Tautological Collapse of $B_p(r)$).** *For every smooth positive even kernel $\phi : \mathbb{R} \to (0,\infty)$ with rapid decay and Laplace/Fourier transform $f(z) = \int_{\mathbb{R}} \phi(u)e^{zu}\,du$:*
1. *Because $G(2u) = \log\Phi(u/2) = \log\phi(u)$, the chain rule gives $P(2u) = \frac{\phi'(u)}{2\phi(u)}$ and $P_1(2u) = \frac{\phi''(u)\phi(u) - \phi'(u)^2}{4\phi(u)^2}$. Multiplying by $K(p,t) = \phi(p+t)\phi(p-t)$ cancels the denominators identically:*
   $$P(2(p+t))P(2(p-t))K(p,t) \equiv \frac{1}{4}\phi'(p+t)\phi'(p-t), \tag{4}$$
   $$2K(p,t)\left[(P_+ + P_-)P_+ P_- + P_{1+}P_- + P_+ P_{1-}\right] \equiv \frac{1}{4}\left[\phi''(p+t)\phi'(p-t) + \phi'(p+t)\phi''(p-t)\right]. \tag{5}$$
2. *Therefore $B_p(r) \equiv \frac{1}{4}\int_0^\infty \phi'(p+t)\phi'(p-t)\cos(2rt)\,dt$ is simply the bilinear derivative autocorrelation of $\frac{1}{2}\phi'$, whose transform is $g(z) := \int_{\mathbb{R}} \frac{1}{2}\phi'(u)e^{zu}\,du = -\frac{1}{2}z f(z)$. The strip identity (2) is the universal complex product rule:*
   $$8\int_0^\infty p\sinh(2xp) B_p(r)\,dp = \operatorname{Re}\!\left(g'(x+ir)\overline{g(x+ir)}\right) = \frac{1}{4}x|f(x+ir)|^2 + \frac{1}{4}(x^2+r^2)J(x,r). \tag{6}$$
3. *Dividing (2) by $x$ and taking $x \to 0^+$ yields the critical-line limit:*
   $$64\int_0^\infty p^2 B_p(r)\,dp - X(r)^2 = r^2 L_1[X](r), \qquad X(r) = f(ir), \quad L_1[X] = (X')^2 - X X''. \tag{7}$$

### 3.2 Matched control falsification of universal $B_p(r)$ dominance

Because (4)–(7) hold for **every** smooth rapidly decaying even kernel $\phi$ without using the Planat–Solé Jacobi ODE:
- On **Davenport–Heilbronn** at $z = 0.3085 + 85.699i$, (6) holds to `1.76e-97` (`verify_four_lanes.py`).
- On the **`NS-101` reciprocal-dilation control** $\phi_\beta(u) = \frac{3\phi(u) + \phi(u-\beta) + \phi(u+\beta)}{3+2\cosh(\beta/2)}$ at $\beta = 4, r_\beta = \pi/4$, (7) holds to `1.79e-43` and evaluates to:
  $$64\int_0^\infty p^2 B_{\beta,p}(\pi/4)\,dp - X_\beta(\pi/4)^2 = \left(\frac{\pi}{4}\right)^2 L_1[X_\beta](\pi/4) \approx -0.01068524686157 < 0.$$

**Consequence (`Known wall` for the multilinear logarithmic-slope hierarchy)**: Forming multilinear products $P(2u_1)\cdots P(2u_k)\phi(u_1)\cdots\phi(u_k) = 2^{-k}\phi'(u_1)\cdots\phi'(u_k)$ at distinct coordinates $u_1 = p+t, u_2 = p-t$ tautologically erases the rational Jacobi formula for $P(L)$. A non-tautological Jacobi-ODE transfer must substitute the nonlinear polynomial ODE relation among $(a, U, \chi)$ at the **same** clock argument $L = 2u$ (degree $\ge 2$ at a single point), or use a nonlinear Lyapunov/dissipation functional of the single-lattice IVP $U(0) = \Gamma(1/4)^8/(64\pi^4)$.

---

## Lane 4 — Reconciliation of Unpublished Oct 1–5 Local Deliverables

The following completed local audits from `/Users/alex/Documents/ChatGPT/riemann` have been verified and staged into `/Users/alex/riemann-worktrees/origin-main-review/audits/` on branch `codex/four-lane-audit-20261014` (preserving original filenames and byte contents, with no push unless explicitly requested):
1. **October 1 `COEFF` 12-agent review and specialist brief v2**:
   - `audits/coeff-twelve-agent-review-2026-10-01-v1.html`
   - `audits/coeff-specialist-brief-2026-10-01-v2.html`
   - `audits/coeff-twelve-proposals-2026-10-01-v1/01..12-*.md` (all 12 proposal and adversarial review notes, establishing the `Known wall` for universal $n^{-3}$ recovery on $V_{2N}\cap V_N^\perp$ via `NS-61` and the verified compact dual extractor $\psi_N$).
2. **October 5 ten-agent method/transfer review**:
   - `audits/ten-agent-next-input-2026-10-05-v1/` (`BRIEF.md`, `review-record.json`, `next-input-review-2026-10-05-v1.html`, and `reviews/01..10-*.md`, including Reviewer 08's unconditional finite-cluster far-exterior heat-transport bound $|E_{\mathrm{far}}(t)| \le \frac{128}{3}\kappa K m a^2 e^{2aY} M \frac{\log(2+R)+1}{R}\|f\|_2\|g\|_2$ from Polymath15 Theorem 1.5(iv)).
