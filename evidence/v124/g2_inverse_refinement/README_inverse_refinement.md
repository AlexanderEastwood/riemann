# Reproduce v1.22 inverse refinement

Run from this directory after extracting the cumulative bundle. Requires Python, python-flint (Arb), and LaTeX for the full PDF.

```sh
python3 refine_inverse.py --mode constants --bits 320
python3 refine_inverse.py --mode constants --bits 384
python3 refine_inverse.py --mode probe --bits 768 --J 65536
python3 refine_inverse.py --mode probe --bits 896 --J 65536
python3 integrate_v122.py
python3 build_complete_pdf.py
```

The scripts reuse the archived g2_low_schur exact witnesses and assembly. Large65536-coefficient caches are reproducible in about2minutes and are omitted from this increment. The complete original bundle and its earlier evidence remain preserved. The smaller exploratory probe reports are retained, with their inconclusive scope explicit.

The directional gate is ONE far-energy bound. It is not the full low-mode Schur sign, a mixed-term certificate, a uniform-window estimate, or RH.
