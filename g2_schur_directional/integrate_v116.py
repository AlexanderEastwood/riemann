from pathlib import Path
import re

b=Path(__file__).resolve().parent
old=b.parent/'g2_signed_tail'
original=(old/'fixed_space_prime_action_v1.tex').read_text()
t=original.replace('v1.15','v1.16').replace('version 1.15','version 1.16')
start=t.index('A bounded discrete-Hilbert commutator identifies')
end=t.index('\\end{abstract}',start)
t=t[:start]+r'''A bounded discrete-Hilbert commutator identifies the canonical
semilocal Weil operator and Fourier core. Positive weighting of the
prime shifts, diagonal inverse bounds and moment-preserving residual
estimates now certify the complete Weil form at $\lambda=3$, including
both parity sectors and the entire Fourier complement. Exact dyadic
witnesses and interval arithmetic verify the signed finite Schur bounds.
This fixed-window certificate supplies no growing-window lower estimate.
G2 remains open; no RH proof is claimed.
'''+t[end:]
start=t.index('Version 1.15 proves')
end=t.index('\\paragraph{Reading conventions.}',start)
t=t[:start]+r'''Version 1.16 closes the signed head/complement positivity test at
$\lambda=3$. The proof includes the full infinite tail and independent
higher-precision replays of exact witnesses. Earlier ordinary source-mass,
Rayleigh and operator-residual results are retained. A lower estimate
along unbounded windows, or sufficient quantitative ground-state overlap,
is still missing. The physical endpoint, corrected sampler graph defect
and all 72 historical dispositions are preserved.

'''+t[end:]
start=t.index('At $\\lambda=3$ this replaces the earlier sufficient tail cutoff')
end=t.index('This is a quantitative omitted-tail theorem',start)
weighted=(b/'weighted_prime_inverse_insert.tex').read_text()
weighted=weighted[:weighted.index('This yields a directional residual certificate')]
t=t[:start]+weighted+'\n'+t[end:]
t=t.replace('This is a quantitative omitted-tail theorem, not full Weil positivity.',
'''The preceding tail estimates alone do not establish full Weil positivity.
The complete signed certificate below also controls the effective head.''',1)
t=t.replace('''The sharper estimate may be used in its place. With $Q_N=I-P_N$
and $\\Gamma_{\\lambda,N}>0$ denoting either proved lower bound, write''',
'''For the signed correction use $Q_N=I-P_N$ and let
$\\Gamma_{\\lambda,N}>0$ denote any of the proved tail bounds. Write''',1)
needle='Let\n\\[\n \\mathcal V_\\lambda:=\\operatorname{Var}(p_\\lambda)'
assert needle in t
directional=(b/'directional_schur_insert.tex').read_text().replace('prop:v116-weighted-tail','prop:v116-diagonal-inverse')
certificate=(b/'fixed_window_insert.tex').read_text().replace('prop:v116-weighted-tail','prop:v116-diagonal-inverse')
t=t.replace(needle,directional+'\n'+certificate+'\n'+needle,1)
start=t.index('The remaining spectral task is the signed finite-core correction')
end=t.index('\\paragraph{What is established by the sampler correction.}',start)
t=t[:start]+r'''Proposition~\ref{prop:v116-window-positive} now closes the signed
head/complement test at $\lambda=3$ for both parity sectors and the
entire closed form. Positive weighted prime bounds and the increasing
tail diagonal are essential to its verified inverse-action estimate;
the residual's directional moments control every omitted row.
The remaining G2 spectral task is a lower bound tending to zero along
unbounded windows, or sufficient quantitative source-to-ground overlap.
One fixed-window certificate does not establish either.

A concrete next spectral test applies the same certificate to a shifted
operator to count its low levels and compare the even and odd bottoms.
The complete diagonal and the tail weights must both be shifted, and
an inertia bound must be combined with an actual trial quotient before
asserting ground-state ordering. Subsequent larger-window certificates
will need a uniform error budget; several near-zero modes may have to
be treated together. Endpoint stability for a source-to-ground comparison,
the sampler graph defect and full-strip normalization remain separate
obligations. The fixed-window gap is closed; G2 and RH remain open.


'''+t[end:]
t=t.replace('''bounds. No new head matrix, inverse-action correction or full-window
positivity was certified.''','''bounds. That v1.15 calculation did not certify a head matrix or its
inverse-action correction; the complete certificate below now does so
at the same physical window.''',1)
needle='\\section{Integration ledger for the complete previous manuscript}'
extra=r'''\subsection*{Complete fixed-window certificate and its reproduction}
Proposition~\ref{prop:v116-window-positive} is certified by
\texttt{g2\_schur\_directional/certify\_infinite\_schur.py}, using
the coefficient assembly in \texttt{assembly.py} and the scalar check
\texttt{certify\_weighted\_prime\_tail.py}. The bundle contains both
exact dyadic inverse-action witnesses, all positive LDL pivot enclosures,
and 768-bit and 896-bit replay reports. Its reproduction guide gives
the complete commands and analytic dependencies. The frozen witnesses
are unchanged between the two precision runs.

All finite output rows through $J=4096$ are enclosed, and the moment
inequality bounds every row beyond $J$. Thus the result is not an
extrapolation from finite eigenvalues. The finite Fourier entries through
$N=64$ were also checked against the earlier independent interval
integration: all 8,321 even and odd entries overlap their reference
enclosures. This consistency check supplements, but does not replace,
the analytic coefficient identities and series-remainder proof.

The successful result certifies complete fixed-window positivity.
It does not report a numerical lower eigenvalue, a simple ground state,
an exact source-to-ground endpoint comparison, or a bound for unbounded
windows. Internal adversarial review checked the inverse order, dyadic
freezing residual, parity factors, remote Gram and form-domain passage;
this is not external peer review or proof-assistant verification.
Exploratory failures of weaker sufficient bounds are preserved in the
research log and are not presented as negative Weil-form results.

'''
assert needle in t
t=t.replace(needle,extra+needle,1)
labels=re.findall(r'\\label\{([^}]+)\}',t)
assert len(labels)==len(set(labels))
refs=set(re.findall(r'\\(?:ref|eqref)\{([^}]+)\}',t))
assert refs<=set(labels),refs-set(labels)
assert t.count('\\section{')==34
def ledger(s):
    p=s.index('\\section{Integration ledger')
    return s[s.index('\\begin{longtable}',p):s.index('\\end{longtable}',p)]
assert ledger(t).replace('v1.16','v1.15')==ledger(original)
(b/'fixed_space_prime_action_v1.tex').write_text(t)
print('Integrated v1.16:',len(labels),'unique labels, 34 sections; all historical ledger rows preserved.')
