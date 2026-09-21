# Reproducing v1.15

The complete manuscript is 123 pages. Proposition 20.21 proves the sharp infinite Fourier-tail bound; Lemma 20.27 and Proposition 20.28 prove ordinary norm normalization and the actual full operator residual. Equation 181 retains the signed Schur identity and its residual Gram bound. G2 is not proved.

The analytic proofs are in `sharp_tail_insert.tex` and `residual_insert.tex`. Their derivations are in `sharp_arch_tail.md` and `operator_residual_derivation.md`. Read `adversarial_review.md` and `operator_residual_independent_audit.md` for the internal checks and limitations. The persistent research log records the next task and all historical attempts.

Run the new scalar interval check with Python 3, python-flint 0.9 and FLINT 3.6:

```bash
python3 check_sharp_tail_constants.py
```

In the original runtime, python-flint was available through `PYTHONPATH=/workspace/scratch/0cd0bd59ceda/deps/python_flint`. On another system install an equivalent version normally. The result is `sharp_tail_constants.json`; its PASS status certifies only the outward interval evaluations of the proved analytic constants. It does not certify the finite Schur correction or RH.

Compile the complete manuscript with TeX Live and latexmk:

```bash
latexmk -pdf -interaction=nonstopmode -halt-on-error fixed_space_prime_action_v1.tex
```

The mathematical dependency is the existing uniform Sobolev G1 statement, the high-frequency coefficient bound, and the canonical closed Weil operator of v1.14. The normalized Hermite approximation comes from Connes–Consani–Moscovici, Lemma 7.2: <https://arxiv.org/html/2511.22755v1>. The sharp diagonal inequalities use the exact primary identities <https://dlmf.nist.gov/5.9.E15> and <https://dlmf.nist.gov/5.15.E1>. The extension and bootstrap estimates are proved in the manuscript.

The earlier finite matrix/source certificates are preserved without unnecessary reruns. No numerical threshold is claimed for the new asymptotic residual estimate. A tiny source residual does not imply a positive bottom eigenvalue. The next certificate must control `F-B*T^(-1)B`, preferably retaining `R*R/Gamma` rather than replacing it with a scalar penalty.
