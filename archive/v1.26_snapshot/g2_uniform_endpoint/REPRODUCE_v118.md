# Reproduce v1.18: continuum endpoints and complement reduction

The root TeX/PDF files contain the complete manuscript. The cumulative archive preserves prior exact inputs, interval certificates and historical audits. This revision adds analytic proofs, not a new numerical sign certificate.

1. Read the new physical decomposition, zero boundary trace theorem, Fejer endpoint corollary and graph-trace proposition in Section 20. Their derivation and internal checks are in `actual_ground_endpoint_derivation.md`, `adversarial_endpoint_review.md`, and `primary_source_and_endpoint_audit.md` in this directory.
2. Check the exact scalar normalization against Chen–Weth Theorem 1.1 and the common-core proof. The restricted logarithmic Laplacian is different from the spectral logarithm of the Dirichlet Laplacian. Its normalization here is one half of the cited operator.
3. Verify the boundedness bootstrap before applying the bounded-solution boundary theorem of Hernandez-Santamaria, Lopez Rios and Saldana, Theorem 1.1. All hypotheses are listed in the proof; no endpoint condition is assumed beforehand.
4. Optionally run `python3 check_log_kernel_normalization.py` with mpmath installed. `log_kernel_normalization_checks.json` records the 90-decimal diagnostic. This is only a consistency check, not interval certification or a replacement for the exact integral proof.
5. Check `gap_free_block_insert.tex` and `adversarial_uniform_bound.md`. The sharp constant comes from a one-variable maximization and a two-dimensional witness. The complementary arithmetic sign is an unproved input, explicitly labeled in the manuscript.
6. Compile the root manuscript using `latexmk -pdf -interaction=nonstopmode -halt-on-error fixed_space_prime_action_v1.tex`. The saved revision has 137 pages. The source retains all 410 earlier labels, adds 13, and preserves all 72 historical ledger rows.

The Fejer rate concerns a positive filter at fixed window. It does not replace the literal sharp Fourier cut used elsewhere or supply a joint finite-cut/window endpoint estimate. Every complete eigenfunction has zero continuous physical trace, so a nonzero continuum ground-to-source endpoint comparison must not be reinstated.

The preceding v1.17 complete lambda=3 positivity, simple ground and ordinary overlap certificates are retained. G2's unbounded-window sign estimate and RH remain unproved.
