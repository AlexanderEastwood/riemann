# October 14, 2026 Four-Lane Audit — Index & Reproducibility Record

- **Styled HTML report**: [`../four-lane-audit-2026-10-14-v1.html`](../four-lane-audit-2026-10-14-v1.html)
- **Complete mathematical derivation**: [`derivation.md`](derivation.md)
- **Proposal & control-screen gate record**: [`PROPOSAL.md`](PROPOSAL.md)
- **Deterministic verification script**: [`verify_four_lanes.py`](verify_four_lanes.py)
- **Verification output**: [`verification.json`](verification.json)

**Wall check: Same open gap** overall (`NB-GAIN`, `KERNEL-API`, `ZERO-GEOMETRY`), with two narrower **Known walls** proved and verified:
1. **`ZERO-GEOMETRY` (`01-jacobi-transfer.md` / `PR #72` two-shift moment $B_p(r)$)**: Because $2P(2u) = \phi'(u)/\phi(u)$, the product $P(2(p+t))P(2(p-t))\phi(p+t)\phi(p-t) \equiv \frac{1}{4}\phi'(p+t)\phi'(p-t)$ cancels the denominator identically and erases the Planat–Solé Jacobi ODE. Its strip identity is the universal complex product rule for $g(z) = -\frac{1}{2}z f(z)$, its $x \to 0^+$ limit is $64\int_0^\infty p^2 B_p(r)\,dp - X(r)^2 = r^2 L_1[X](r)$, and the `NS-101` control violates the required lower bound at $\beta=4, r_\beta=\pi/4$ ($-0.01068525 < 0$).
2. **`KERNEL-API` (`05-euler-api.md` interior prime-chain elimination)**: While the interior adjoint embedding $L_p : V_{a-\ell} \to V_a$ ($\ell = \log p < a$) eliminates both the smooth cutoff $\chi$ and the rank-2 pole operator $K_{\mathrm{pole}}$ ($K_{\mathrm{pole}} L_p = 0$), Chebyshev/Bertrand prime bounds prove that for every $a > 0$ and every prime subset $\mathcal{P}$ with $\ell_{\mathcal{P}} = \sum_{p \in \mathcal{P}} \log p < a$, at least one prime $q \notin \mathcal{P}$ satisfies $\log q < 2a - \ell_{\mathcal{P}} < 2a$ and remains active in the window.

In **Lane 1 (`NB-GAIN` / `COEFF`)**, the compact dual extractor $\psi_N(t) = -t^2(t\beta_N'(t))'$ from the October 1 12-agent review has exact rational constants
$$C_b = \frac{6904}{45045}, \qquad \operatorname{Var}_{\mathbb{R}}(b''') = \frac{543}{14}, \qquad A_b = \frac{181}{3360}, \qquad I_{\mathrm{diag}} = \frac{1219}{38798760},$$
and on $V_{2N}\cap V_N^\perp$ its untruncated pairing $M_N(u,y) = (\lambda_{\mathrm{new}} - C^T G^{-1}\lambda_{\mathrm{old}})^T y = \tilde{\lambda}_N^T y$ satisfies $\tilde{\lambda}_N^T S^{-1}\tilde{\lambda}_N \le C_b N - \lambda_{\mathrm{old}}^T G^{-1}\lambda_{\mathrm{old}} \le C_b N$ without low-old alias truncation at $K = \lfloor\sqrt{N}\rfloor$. This establishes exact algebraic isomorphism with the Schur-complement Rayleigh quotient along $w_{\psi_N} = S^{-1}\tilde{\lambda}_N$ and transfers `NS-87`'s $T=N^6$ localization without `NS-78`'s $B = 1536\zeta(2)^2$ factor.

In **Lane 4 (Local Audit Reconciliation)**, the unpublished October 1 `COEFF` 12-agent review (`coeff-twelve-agent-review-2026-10-01-v1.html`, `coeff-specialist-brief-2026-10-01-v2.html`, `audits/coeff-twelve-proposals-2026-10-01-v1/`) and October 5 ten-agent review (`audits/ten-agent-next-input-2026-10-05-v1/`, including the Polymath15 Theorem 1.5(iv) finite-cluster far-tail heat bound) are staged in this isolated worktree branch (`codex/four-lane-audit-20261014`).

## Reproducibility

```sh
.venv/bin/python audits/four-lane-audit-2026-10-14-v1/verify_four_lanes.py
.venv/bin/python -m unittest controls.test_controls
pyright audits/four-lane-audit-2026-10-14-v1/verify_four_lanes.py
```

**Explicit open-status disclosure**: **RH**, **G2**, the **cofinal signed-arithmetic lower bound**, and **both historical missing-original evidence groups** in `evidence/MISSING.md` remain **OPEN**.
