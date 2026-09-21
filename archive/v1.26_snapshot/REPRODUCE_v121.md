# Complete manuscript v1.21 reproduction

Build the complete PDF with:

    latexmk -pdf -interaction=nonstopmode -halt-on-error fixed_space_prime_action_v1.tex

New exact certificates are in g2_schur_cancellation. With python-flint and mpmath installed, from that directory run:

    python3 certify_finite_K.py --bits 768
    python3 certify_finite_K.py --bits 896
    python3 check_cancellation_subspace.py --bits 768
    python3 check_cancellation_subspace.py --bits 896

The frozen witnesses and existing coefficient enclosures are included. Witness proposal is not a proof assumption. The exact-source transfer uses the archived pswf_source_certificate.json, whose proof and full reproduction are retained in the earlier g2_source_certificate directory.

The local alpha4=0 results do not certify the infinite Schur sign. The source-complement example has small positive energy and demonstrates strong cancellation; it is not a negative Weil vector. No cofinal G2 sign or RH proof is claimed.

All prior evidence entries are retained. Original root manuscript files are updated; Library version history and the history/v1.20 directory preserve the immediately prior text, notes and validation. Earlier audit reports remain historical records rather than current release summaries.
