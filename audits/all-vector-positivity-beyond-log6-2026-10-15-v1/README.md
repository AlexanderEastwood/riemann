# Audit Package: `all-vector-positivity-beyond-log6-2026-10-15-v1`

## Contents
- `PROPOSAL.md` — Executive summary and theorem statements breaking the $a = \frac{1}{2}\log 6 \approx 0.895880$ barrier up to $a = \log(5/2) \approx 0.916291$, $a = 0.940$, $a = 0.960$, and the next prime-pair threshold $a = \frac{1}{2}\log 7 \approx 0.972955$.
- `derivation.md` — Full mathematical derivations of:
  1. **Theorem 1**: Exact Three-Island Identity $P_b L_2^2 P_b = \frac{13}{4}I_{L^2(-b,b)}$ for all $a \le \frac{3}{2}\log 2 \approx 1.039721$.
  2. **Theorem 2**: Monotonic archimedean baseline shift $\Delta_\alpha = \frac{7}{20} = 0.35$, exact reflection-involution preconditioner $P_0(a)$, and sum-of-squares $a$-monotonicity certifying the entire interval $a \in (\frac{1}{2}\log 6, \log(5/2)]$.
  3. **Theorem 3**: $3\times 3$ fiber-bundle preconditioner, prime-reflection step minorants ($+2c_3 P_{\mathrm{anti/sym}}^{(3)} + 2c_5 P_{\mathrm{anti/sym}}^{(5)}$), and the 4-step midpoint-moment enclosure certifying $a = 0.940$, $a = 0.960$, and $a = \frac{1}{2}\log 7$.
- `verify_beyond_log6.py` — 384-bit `flint.arb` verification script with exact `SymReal` symbolic cut-point algebra ($\mathbb{Q} + \sum_{p \in \{2,3,5,7\}} \mathbb{Q}\log p$, zero decimal tolerances; `pyright` clean: 0 errors, 0 warnings).
- `verification.json` — Machine-readable 384-bit `flint.arb` enclosures and trace margins (`file_sha256 = c5585c649d2d763dd58ddb5a8f1d91c7266b32a12280a361ce93c344d4a0b95a`).
- `../all-vector-positivity-beyond-log6-2026-10-15-v1.html` and `../all-vector-positivity-beyond-log6-2026-10-15-v2.html` — Styled HTML reports (`v1` preserved untouched; `v2` updated with exact `SymReal` cut-point algebra and certified endpoint ball remainder).

## Reproduction
```bash
/Users/alex/riemann-worktrees/origin-main-review/.venv/bin/python audits/all-vector-positivity-beyond-log6-2026-10-15-v1/verify_beyond_log6.py
pyright audits/all-vector-positivity-beyond-log6-2026-10-15-v1/verify_beyond_log6.py
```
