"""Integrate supported mixed-correction results into the complete v1.22."""
from pathlib import Path
B=Path(__file__).resolve().parent
s=(B/'input/fixed_space_prime_action_v122.tex').read_text()
s=s.replace('-- v1.22','-- v1.23').replace('manuscript, version 1.22','manuscript, version 1.23').replace('Disposition in v1.22','Disposition in v1.23')
s=s.replace('iteration, with finite-prefix bounds retaining all remote rows.','iteration, with finite-prefix bounds retaining all remote rows.\nComplete mixed-term estimates rule out the first inverse degree\nwith the saved head certificate, including its positive update.\nRetaining that update gives a monotone family of complete inverse\nupper bounds for subsequent degrees.')
start=s.index('Version 1.22 sharpens');end=s.index('\\paragraph{Reading conventions.}',start)
s=s[:start]+r'''Version 1.23 bounds the complete mixed correlations on the saved
$\lambda=4$ trial and proves that the first inverse polynomial with
the saved initial head certificate cannot certify that direction,
even after its full positive update. The failure
is of a particular upper bound, not of Weil positivity. A stronger
head-matrix update gives monotone complete inverse bounds and a
finite-probe enclosure with all omitted correlations retained.
The full low Schur sign and growing-window estimates remain open.
Weak G1, all 72 historical dispositions, the physical endpoint and
the explicit sampler graph defect are retained. No G2 sign gap is
closed; no RH proof is claimed.

'''+s[end:]
needle='\\begin{proposition}[An ordinary-error target for growing windows]'
assert s.count(needle)==1;s=s.replace(needle,(B/'mixed_complete_insert.tex').read_text()+'\n'+needle)
old=r'''inverse correction. The next concrete target is to evaluate the
refined mixed term in \eqref{eq:v122-refined-structured}, enclosing
its remote correlations jointly, and then control the simultaneous
Gram on the entire head. Scalar direction bounds alone do not
establish that matrix comparison.'''
new=r'''inverse correction. Proposition~\ref{prop:v123-first-majorant-fails}
now proves that its first-polynomial scalar-head bound fails after
the complete mixed term is included. Corollary~\ref{cor:v123-updated-first-fails}
also excludes its exact positive head update with the saved initial
certificate. The next concrete target is a higher inverse degree
with complete remote errors and the monotone head metric of
Proposition~\ref{prop:v123-monotone-head}, or a stronger initial
head certificate. The resulting
Gram must be controlled on the entire even and odd heads. A
finite-prefix or single-direction improvement does not establish
that simultaneous comparison or growing-window uniformity.'''
assert old in s;s=s.replace(old,new)
needle='\\subsection*{Parity inverse refinement and its directional gate}'
assert s.count(needle)==1
s=s.replace(needle,r'''\subsection*{Complete mixed-correlation certificate and head refinement}
\label{app:v123-mixed}
The cumulative bundle retains the exact outer and inner witnesses
from the preceding revision. The new files in
\texttt{g2\_mixed\_complete} are:
\begin{itemize}[nosep]
\item \nolinkurl{mixed_refinement.py}, for retained mixed vectors,
complete first-polynomial upper enclosures, and explicitly separate
higher-degree finite-prefix diagnostics;
\item \nolinkurl{mixed_directional_check.py}, for the complete
directional lower certificate of
Proposition~\ref{prop:v123-first-majorant-fails};
\item \nolinkurl{mixed_directional_witness_J65536.json}, specifying
the exact $496$-component probe by integer numerators over $2^{160}$;
\item the $768$- and $896$-bit interval reports and the independent
internal adverse review of the mixed, monotone-head and probe bounds.
\end{itemize}
The inner witness SHA-256 is checked against the saved positive-tail
report. The prefix inverse and its head pairings use the actual
unshifted residual and consistently shifted inner factors. The
certified probe norm is retained rather than rounded to one.
Both remote input and remote first-polynomial output enter the
error estimate. Replaying the analytic and interval inequality is
the sign certificate; a small floating residual is not.

The higher-polynomial experiments are retained in the research log.
Their positive finite-prefix margins do not certify the corresponding
complete corrections and are not used as propositions in this paper.
The strengthened head bound is proved analytically; its simultaneous
application to the full $\lambda=4$ Schur matrix remains open.

'''+needle)
(B/'fixed_space_prime_action_v1.tex').write_text(s)
print('Complete v1.23 integrated.')
