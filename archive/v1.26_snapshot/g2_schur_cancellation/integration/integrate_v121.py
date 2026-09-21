from pathlib import Path
import re

root = Path(__file__).resolve().parent
base = (root / 'input/fixed_space_prime_action_v1.tex').read_text()
s = base.replace('v1.20', 'v1.21').replace('version 1.20', 'version 1.21')

def replace_once(old, new):
    global s
    assert s.count(old) == 1, (old[:100], s.count(old))
    s = s.replace(old, new, 1)

replace_once(r'''remote-row and dimension-aware error bounds. Every complete
eigenfunction has zero physical endpoint. Finite source removal
cannot reduce the unsigned prime norm. The low-mode sign and
growing-window estimate remain open; no RH proof is claimed.''', r'''remote-row and dimension-aware error bounds. Finite-support trials
certify a zero head-error term at this window, leaving the infinite-tail
residual correction open. Strong cancellation persists in the exact
source complement. Every complete eigenfunction has zero physical
endpoint. A cofinal complete-Weil lower error tending to zero would
imply RH directly, but remains unproved.''')

start = s.index(r'\paragraph{Status of this version.}')
end = s.index(r'\paragraph{Reading conventions.}', start)
s = s[:start] + r'''\paragraph{Status of this version.}
Version 1.21 certifies local trial positivity at $\lambda=4$ while
retaining the unresolved correction $S_\infty=K_X-r^*T^{-1}r$.
A separate certificate exhibits strong cancellation off the exact source
at $\lambda=3$. The direct cofinal Weil criterion is distinguished
from the conditional Riesz-operator route. Weak G1, all 72 historical
dispositions, the endpoint conventions and sampler graph defect are
retained. No G2 sign gap is closed; no RH proof is claimed.

''' + s[end:]

replace_once(r'\subsection*{Why a finite source block cannot reduce the unsigned prime norm}',
             (root/'cancellation_insert.tex').read_text() + '\n' +
             r'\subsection*{Why a finite source block cannot reduce the unsigned prime norm}')

anchor = r'''\begin{proposition}[An ordinary-error target for growing windows]'''
# The new propositions refer forward to the ordinary-error statement. Place
# them after that statement and its existing dimension-aware discussion.
assert s.count(anchor)==1
next_anchor = r'\subsection*{'
position = s.index(next_anchor, s.index(r'\label{prop:v120-structured-uniform}'))
s = s[:position] + (root/'schur_insert.tex').read_text() + '\n' + s[position:]

replace_once(r'''The fixed-space route has separate foundational obligations: prove the
quantitative evaluator estimates and give a complete closed-operator
realization if the Riesz-window formulation is retained. These are not
prerequisites for the finite-core exclusion criterion now proved in
Theorem~\ref{thm:v15-finite-metric}; bypassing them there does not prove
them for the Riesz formulation. The shell-sign, uniform metric,
large-support spectral-overlap, and Schur-complement formulations are
alternative targets; none has been shown to follow from weak G1.''', r'''The fixed-space route has separate foundational obligations: prove the
quantitative evaluator estimates and give a complete closed-operator
realization if the Riesz-window formulation is retained. These are not
prerequisites for the finite-core exclusion criterion in
Theorem~\ref{thm:v15-finite-metric}, nor for the direct complete-Weil
route below. Bypassing them does not establish them for the Riesz
formulation. The shell-sign, uniform metric, large-support
spectral-overlap, and Schur-complement formulations are alternative
targets; none has been shown to follow from weak G1.

''' + (root/'rh_route_insert.tex').read_text())

replace_once(r'''overlap on such a family. This is RH-strength: by nested support domains,
even a cofinal sequence of complete lower bounds $-o(1)$ implies
nonnegativity of every compact test. A finite list of certified windows
cannot replace that estimate.''', r'''overlap on such a family. Proposition~\ref{prop:v121-cofinal-rh}
shows why this is RH-strength: even a cofinal sequence of complete
lower bounds $-o(1)$ implies nonnegativity of every compact test.
A finite list of certified windows cannot replace that estimate.''')

replace_once(r'''also need an independent uniform operator-residual bound.

The unsigned-prime shortcut''', r'''also need an independent uniform operator-residual bound.
Proposition~\ref{prop:v121-complement-cancellation} rules out the
claim that substantial cancellation is confined to the single source:
an exactly source-orthogonal finite test has non-prime energy greater
than $0.4$ but positive total energy below $3\cdot10^{-31}$.
This does not disprove complementary positivity; it prevents using
basis or random-vector samples as a uniform dominance argument.

The unsigned-prime shortcut''')

replace_once(r'''bounded. Positivity of the raw $33$-dimensional matrix would not suffice.
This leaves a separate growing-window target:''', r'''bounded. Proposition~\ref{prop:v121-alpha-zero} now certifies the
raw head and specified finite-support trial forms $K_X$ positive in
both parity sectors. This gives local $\alpha_4=0$, without an
infinite-tail transfer for $K_X$. It still does not suffice for the
exact Schur sign because the nonnegative residual inverse correction
must be subtracted, as in \eqref{eq:v121-galerkin-defect}.
This leaves a separate growing-window target:''')

replace_once(r'''The signed head hypothesis and these uniform inverse scales are still
unproved. The completed analytic reduction supplies no additional
fixed-window positivity or G2 sign claim.''', r'''The trial-head hypothesis is now verified in the local cases just
specified, but not along an unbounded window family. The exact low-head
Schur sign and the uniform inverse scales are still unproved. With
$\alpha_\lambda=0$, the remaining target is $e_\lambda\to0$ and
$t_\lambda/\sqrt{\mu_\lambda}\to0$, not merely $t_\lambda\to0$.
Inverse approximation convergence alone does not establish residual
energy convergence. The local trial certificates close this narrow
prerequisite, not a G2 sign gap.''')

replace_once(r'\section{Integration ledger for the complete previous manuscript}\label{app:ledger}',
             (root/'audit_appendix_insert.tex').read_text() + '\n' +
             r'\section{Integration ledger for the complete previous manuscript}\label{app:ledger}')

replace_once(r'''certificate and its exact-source identification; these do not settle
the remaining uniform analytic obligations.''', r'''certificate and its exact-source identification, complete fixed-window
sign certificates, finite-trial positivity and an exact-source
cancellation certificate. These do not settle the remaining uniform
analytic obligations.''')

before = set(re.findall(r'\\label\{([^}]+)\}', base))
after_list = re.findall(r'\\label\{([^}]+)\}', s)
assert before.issubset(set(after_list))
assert len(after_list)==len(set(after_list))
(root/'fixed_space_prime_action_v1.tex').write_text(s)
print('Prior labels:', len(before), 'New total:', len(after_list))
print('New labels:', sorted(set(after_list)-before))
