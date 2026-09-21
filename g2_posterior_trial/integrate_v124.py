from pathlib import Path
B=Path(__file__).resolve().parent
s=(B/'input/fixed_space_prime_action_v123.tex').read_text()
s=s.replace('-- v1.23','-- v1.24').replace('manuscript, version 1.23','manuscript, version 1.24').replace('Disposition in v1.23','Disposition in v1.24')
s=s.replace('upper bounds for subsequent degrees.','upper bounds for subsequent degrees. A better frozen finite trial\nnow certifies a strictly positive complete Schur value on the same\npreviously obstructing head direction, with its infinite residual\nfully bounded. The simultaneous head comparison remains open.')
start=s.index('Version 1.23 bounds');end=s.index('\\paragraph{Reading conventions.}',start)
s=s[:start]+r'''Version 1.24 closes the saved one-direction Schur test at
$\lambda=4$: a new frozen finite trial and complete residual
certificate give $3.0930\cdot10^{-20}<S_\infty(v,v)<3.2356\cdot10^{-20}$.
The old first-degree majorant still fails as proved; the improved
trial is verified directly against the full operator. Positivity of
the simultaneous even and odd head matrices and growing-window
uniformity remain open. Weak G1, all 72 historical dispositions,
the physical endpoint and explicit sampler graph defect are
retained. G2 and RH are not proved.

'''+s[end:]
needle='\\begin{proposition}[An ordinary-error target for growing windows]'
assert s.count(needle)==1;s=s.replace(needle,(B/'posterior_insert.tex').read_text()+'\n'+needle)
old=r'''certificate. The next concrete target is a higher inverse degree
with complete remote errors and the monotone head metric of
Proposition~\ref{prop:v123-monotone-head}, or a stronger initial
head certificate. The resulting
Gram must be controlled on the entire even and odd heads. A
finite-prefix or single-direction improvement does not establish
that simultaneous comparison or growing-window uniformity.'''
new=r'''certificate. Proposition~\ref{prop:v124-positive-direction}
now proves a complete positive Schur value on that same head
direction by improving the finite trial and verifying its new
residual. The next concrete target is a simultaneous Gram bound
for improved frozen trials on the entire $17$-dimensional even
and $16$-dimensional odd heads, retaining their correlations in
\eqref{eq:v120-structured-finite-rows}. Verified congruences may
resolve the directions of small head energy. A collection of
positive directional values does not establish the matrix
comparison, and fixed-window work does not establish uniformity
as $\lambda\to\infty$. Higher inverse refinements remain
available if the new complete residual bound is insufficient.'''
assert old in s;s=s.replace(old,new)
needle='\\subsection*{Complete mixed-correlation certificate and head refinement}'
s=s.replace(needle,r'''\subsection*{Complete verification of a new finite trial}
\label{app:v124-posterior}
The cumulative bundle adds \texttt{g2\_posterior\_trial}, containing
\nolinkurl{posterior_trial.py}, its imported helper scripts, the
saved remote-Gram reports, the frozen dyadic corrections and the
independent internal proof/code review. The main certificate uses
\nolinkurl{posterior_witness_M4096_s16.json.gz}; its $4080$ dyadic
pairs define the correction on indices $17$ through $4096$.
The original head vector and support-$256$ solve are unchanged.

The proposal uses $16$ steps of a finite preconditioned conjugate
gradient calculation at $256$ bits. This is only a way of choosing
coefficients. The separate verification routine reconstructs the
exact frozen vector, checks its dimensions and witness hashes,
and evaluates the unshifted complete residual at $768$ or $896$
bits. Its final gate includes the full moment remainder beyond
$J=65536$ and the old complete inner metric. It also checks nine
rows by independent dense assembly and checks the expanded energy
identity. No convergence theorem for the proposing iteration is
needed. A separate four-step trial also passes with lower bound
$2.9028\cdot10^{-20}$; it is not asserted to be the old degree-$4$
inverse polynomial. All trial histories are retained in the log.

'''+needle)
(B/'fixed_space_prime_action_v1.tex').write_text(s)
print('Integrated complete v1.24.')
