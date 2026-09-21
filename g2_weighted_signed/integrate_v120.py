from pathlib import Path
import re,shutil
b=Path(__file__).resolve().parent;s=(b/'current/fixed_space_prime_action_v1.tex').read_text();t=s.replace('v1.19','v1.20').replace('version 1.19','version 1.20')
a=t.index('A bounded discrete-Hilbert commutator identifies');z=t.index('\\end{abstract}',a)
t=t[:a]+r'''A bounded discrete-Hilbert commutator identifies the canonical
semilocal Weil operator. Signed Schur certificates prove complete
positivity and ground ordering at $\lambda=3$. At $\lambda=4$,
a one-sided estimate controls the entire Fourier tail $|n|>16$
by its exact positive archimedean energy. A two-sided weighted norm
contraction fails there because of a positive direction. Every complete
eigenfunction has zero physical endpoint. Finite source removal cannot
reduce the unsigned prime norm; logarithmic weighting makes it compact
but not Hilbert--Schmidt. The growing-window signed estimate remains
open; no RH proof is claimed.
'''+t[z:]
a=t.index('Version 1.19 proves');z=t.index('\\paragraph{Reading conventions.}',a)
t=t[:a]+r'''Version 1.20 proves a signed energy bound on both parity sectors
of the complete $\lambda=4$ Fourier tail beyond $16$. It also fixes
the scale needed to turn a weighted sign error into an ordinary form
error. The remaining low-mode Schur sign and growing-window G2 are open.
Weak G1, all 72 historical dispositions and the sampler graph defect
are retained.

'''+t[z:]
needle='The time--frequency geometry suggests a canonical family of candidate projections';assert t.count(needle)==1
t=t.replace(needle,(b/'weighted_signed_insert.tex').read_text()+'\n'+needle,1)
needle='The continuum endpoint is now settled by';assert t.count(needle)==1
goals=r'''Proposition~\ref{prop:v120-lambda4-tail} now proves a signed lower
bound on the entire $\lambda=4$ tail $|n|>16$, retaining its exact
archimedean diagonal. Both complex parity sectors are included.
The immediate fixed-window target is the $33$-dimensional effective
head $F-B^*T^{-1}B$, with its inverse-tail correction rigorously
bounded. Positivity of the raw $33$-dimensional matrix would not suffice.
This leaves a separate growing-window target: a corresponding ordinary
lower error tending to zero. Proposition~\ref{prop:v120-weighted-error}
shows that a dimensionless weighted error must be multiplied by its
arithmetic scale before it can serve that purpose.

The successful one-sided bound does not require a norm contraction:
Proposition~\ref{prop:v120-norm-counterexample} certifies that the
latter fails at the very same cutoff. Nor can the whole weighted
remainder be estimated by an infinite Hilbert--Schmidt sum, by
Proposition~\ref{prop:v120-not-schatten}. Finite-column residual Grams
remain valid. The logarithmic weighted-tail asymptotic in
Proposition~\ref{prop:v120-weighted-tail-asymptotic} is strictly a
fixed-window statement and supplies no uniform joint-limit obstruction.

'''
t=t.replace(needle,goals+needle,1)
needle='\\section{Integration ledger for the complete previous manuscript}';assert t.count(needle)==1
repro=r'''\subsection*{A signed energy certificate at $\lambda=4$}
The directory \texttt{g2\_weighted\_signed} in the cumulative bundle
contains the proof, internal adverse review, exact dyadic witnesses
and interval reports for Proposition~\ref{prop:v120-lambda4-tail}.
\texttt{assembly\_general.py} encloses the actual digamma/trigamma
series with explicit exponential remainders. The separate pole diagonal
is retained. \texttt{certify\_weighted\_tail.py} evaluates the
verified-solve lower matrix, including every row up to $4096$ and the
infinite moment remainder, and verifies every Gershgorin row after an
exact dyadic congruence. The saved solve and congruence witnesses are
reused at higher precision; their origin is not a proof assumption.

\texttt{certify\_weighted\_counterexample.py} verifies the finite
dyadic positive direction disproving the two-sided norm contraction.
\texttt{weighted\_pilot.py} is only a floating-point exploration:
its small negative values at larger windows are unresolved numerical
roundoff, not negative Weil directions. The analytic arguments for
weighted compactness, non-Schatten behavior, fixed-window norm decay
and ordinary-error scaling do not rely on these computations.
The primary-source comparison with \cite{Zhu2026Windows} is contextual;
no external certificate or conjectured decay law is imported.

'''
t=t.replace(needle,repro+needle,1)
bib=r'''\bibitem{Zhu2026Windows}
X. Zhu, \emph{Weil positivity in compact windows: a finite reduction,
certified two-sided bounds, and a Landau--Widom decay law},
arXiv:2608.24827v2 (September 2, 2026).
\url{https://arxiv.org/abs/2608.24827v2}.

'''
t=t.replace('\\end{thebibliography}',bib+'\\end{thebibliography}',1)
labels=re.findall(r'\\label\{([^}]+)\}',t);assert len(labels)==len(set(labels));assert set(re.findall(r'\\label\{([^}]+)\}',s))<=set(labels)
ledger=lambda x:re.findall(r'^\d+\.\d+ &.*$',x,re.M)
assert ledger(t)==ledger(s) and len(ledger(t))==72
(b/'fixed_space_prime_action_v1.tex').write_text(t)
shutil.copy2(b/'evidence/g2_growing_sign/build_complete_pdf.py',b/'build_complete_pdf.py')
print('labels',len(labels),'ledger',len(ledger(t)))
