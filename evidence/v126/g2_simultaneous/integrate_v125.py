from pathlib import Path
B=Path(__file__).resolve().parent
s=(B/'input/fixed_space_prime_action_v124.tex').read_text()
s=s.replace('-- v1.24','-- v1.25').replace('working manuscript, version 1.24','working manuscript, version 1.25').replace('Disposition in v1.24','Disposition in v1.25')
s=s.replace('certify a zero head-error term at this window, leaving the infinite-tail\nresidual correction open.', 'certify a zero head-error term at this window.')
s=s.replace('A better frozen finite trial\nnow certifies a strictly positive complete Schur value on the same\npreviously obstructing head direction, with its infinite residual\nfully bounded. The simultaneous head comparison remains open.', 'Energy-scaled frozen trials now certify positivity of the entire even\nform at this window, with all residual cross-Grams and every omitted\nrow retained. The odd sector remains open. The present scalar far\nmajorant requires exponentially growing cutoffs as the window grows.')
a=s.index('Version 1.24 closes');b=s.index('\\paragraph{Reading conventions.}',a)
s=s[:a]+r'''Version 1.25 proves positivity of the complete even Weil form at
$\lambda=4$, using a simultaneous $17$-column certificate and all
infinite-tail corrections. Its certified generalized relative margin
exceeds $0.62629$. This is a fixed-window sign, not an ordinary
spectral-gap number or a cofinal estimate. The odd-sector test remains
inconclusive. The growing-window analysis proves an exponential
cutoff cost for the current scalar diagonal far bound; it is not
an impossibility theorem for other methods. Weak G1, all 72 historical
dispositions, the physical endpoint and explicit sampler graph defect
are retained. G2 and RH are not proved.

'''+s[b:]
needle='\\begin{proposition}[An ordinary-error target for growing windows]'
assert needle in s;s=s.replace(needle,(B/'simultaneous_insert.tex').read_text()+'\n'+needle,1)
s=s.replace('The complete low-mode Schur sign at $\\lambda=4$ is still open.', 'These first-degree bounds do not settle the complete low-mode Schur\nsign. The later simultaneous certificate proves the even-sector sign\nat $\\lambda=4$; the odd-sector sign remains open.')
s=s.replace('The larger-window tail sign is now established, but full positivity\nat $\\lambda=4$ still requires the signed effective matrix on', 'The larger-window tail sign reduces full positivity at $\\lambda=4$\nto the signed effective matrix on')
s=s.replace('It has $17$ even and $16$ odd coordinates. It is not the raw finite', 'It has $17$ even and $16$ odd coordinates.\nProposition~\\ref{prop:v125-even-complete} below settles the complete\neven sector; the odd sector remains open. It is not the raw finite',1)
s=s.replace('These estimates control how the low-mode inverse correction can be\ncertified. They do not establish its arithmetic sign at $\\lambda=4$\nor along growing windows. The signed head bound and the quantitative\ninverse factors in \\eqref{eq:v120-structured-uniform} remain the\nunproved inputs; positivity of the already certified tail alone does\nnot provide either one.', 'These estimates control certification of the low-mode correction.\nThe simultaneous certificate above settles the complete even form at\n$\\lambda=4$. The odd sign and the corresponding growing-window\nhead/inverse estimates remain unproved; positivity of a remote tail\nalone does not supply them.')
s=s.replace('The immediate fixed-window target is the $33$-dimensional effective\nhead $F-B^*T^{-1}B$, with its inverse-tail correction rigorously\nbounded.', 'The effective head $F-B^*T^{-1}B$ has $33$ dimensions.\nProposition~\\ref{prop:v125-even-complete} certifies its entire\n$17$-dimensional even sector and hence the complete even form.\nThe $16$-dimensional odd sector is still a fixed-window target.')
a=s.index('now proves a complete positive Schur value on that same head\ndirection',s.index('\\section',s.index('\\section{',s.index('\\begin{document}'))))
b=s.index('\nThe successful one-sided bound',a)
s=s[:a]+r'''proves a complete positive value on the saved head direction.
Proposition~\ref{prop:v125-even-complete} extends this to the entire
even head through frozen energy-scaled trials and a simultaneous
complete Gram bound. The odd-head trials tested so far remain
inconclusive; they do not give a negative Weil vector. The primary
next target is the cofinal ordinary-error estimate, rather than a
longer finite list of certified windows.

Proposition~\ref{prop:v125-cutoff-cost} identifies a structural cost:
with the present scalar far majorant, its inner cutoff must grow
exponentially in $\lambda$. The fresh threshold table gives the
window dependence explicitly. A viable family must either control
the associated head dimensions, conditioning and residual Grams at
that cost, or improve the signed far estimate before constructing
the growing inner heads. Finite-only scaling diagnostics in the
research log do not provide the missing complete witnesses.

The trial-head hypothesis is not yet verified along an unbounded
window family. With $\alpha_\lambda=0$, the remaining target is
$e_\lambda\to0$ and $t_\lambda/\sqrt{\mu_\lambda}\to0$, retaining
all ordinary-energy and dimension factors. Inverse approximation
convergence alone does not establish those limits. The complete
even sign at one window closes a local obligation, not G2 or RH.
''' +s[b:]
appendix=r'''\subsection*{Simultaneous even certificate and window scaling}
\label{app:v125-simultaneous}
The cumulative bundle adds \texttt{g2\_simultaneous}. Its main
\texttt{simultaneous\_trial.py} verifier reconstructs the frozen
$17$-column even trial and evaluates all complete residual Grams;
\texttt{complete\_margin.py} certifies the exact rational generalized
margin. Both use the same witness at $768$ and $896$ bits.
The optional \texttt{joint\_remote\_gate.py} retains one common
remote Gram and its cross block. The complete inner tail certificate
and its original exact witnesses are retained unchanged.

The odd trials and the unscaled even trial are retained as
inconclusive experiments in the log. They are not sign certificates.
All trial heads are checked for full rank; midpoint proposals never
replace outward evaluation in a proof gate. The recorded $LDL^*$
pivots are coordinate pivots, not ordinary spectral gaps.

\texttt{window\_scaling\_probe.py} freshly evaluates the analytic
far-cut thresholds at $320$ and $384$ bits. Its separate finite
Galerkin study uses windows $3,4,5,6,8$, heads through $\lambda^2$
and fixed retained/test cuts $256/384$. It records the finite
Schur correction, dimensionless margins and conditioning. Modes
beyond $384$ are absent from that diagnostic; it is not an execution
of the complete-tail pipeline at the larger windows. Every finite
tail used in its elimination must pass its own positive interval
gate. Complete window-specific inner certificates remain necessary
before interpreting such measurements as bounds for G2.

'''
needle='\\subsection*{Complete verification of a new finite trial}'
assert needle in s;s=s.replace(needle,appendix+needle,1)
(B/'fixed_space_prime_action_v1.tex').write_text(s)
print('Integrated v1.25')
