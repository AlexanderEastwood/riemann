de Bruijn–Newman route — assessed 2026-09-21, closed: no bridge, no angle.

RH ⇔ Λ ≤ 0 ⇔ Λ = 0 (Rodgers–Tao arXiv:1801.05914 gives Λ ≥ 0). Polymath15
(arXiv:1904.12438, Res. Math. Sci. 6 (2019) 31) proves Λ ≤ 0.22 via a barrier
argument; every bound Λ ≤ t_0 + y_0²/2 needs RH verified to height ≥ exp(C/t_0),
so Λ ≤ 0 needs all heights — the same wall as the uniform window floor.

No bridge in either direction between a finite-window Weil certificate and
any Λ ≤ c: H_t (t > 0) has no Euler product, Dirichlet series or explicit
formula, so no Weil-type criterion exists for it; Λ ≤ c for c > 0 says nothing
about the zeros of H_0 = ξ; the only zero-location → Λ bridges (de Bruijn's
strip theorem, the Polymath15 barrier) need uniform-in-height input.

Reproduction (diagnostic, not part of the manuscript): the Polymath15
hypothesis-(iii) barrier verification was regenerated from the original Arb
sources in ~35 s (54×54 stored sums, 171 rectangles, winding number 0,
matching the committed outputs), and `dbn_pointwise_certificate.py` (python-
flint 0.9.0) re-certifies H_t ≠ 0 at three points with published ball radii,
agreeing with the original Arb program to all 20 printed digits. This shows
the project toolchain engages the route; it does not help, because the binding
constraint is rigorous RH verification height, not H_t numerics.

Environment note: `brew install flint` (3.6.0) was performed to compile the
Arb sources; nothing else was installed.
