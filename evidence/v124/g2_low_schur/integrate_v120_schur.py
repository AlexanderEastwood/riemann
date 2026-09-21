from pathlib import Path
import re,shutil,json
B=Path(__file__).parent;src=(B/'current/fixed_space_prime_action_v1.tex').read_text();s=src
anchor='The time--frequency geometry suggests a canonical family of candidate projections'
assert s.count(anchor)==1
s=s.replace(anchor,(B/'structured_inverse_insert.tex').read_text()+'\n'+anchor)
s=s.replace('The growing-window signed estimate remains\nopen; no RH proof is claimed.','A structured inverse bound retains the\ncertified tail metric in the low-mode correction and makes its remote\nand growing-dimension costs explicit. The growing-window signed estimate\nremains open; no RH proof is claimed.')
s=s.replace('the scale needed to turn a weighted sign error into an ordinary form\nerror. The remaining low-mode Schur sign and growing-window G2 are open.', 'the scale needed to turn a weighted sign error into an ordinary form\nerror. This Schur revision proves a structured inverse estimate, its\ncomplete remote-row bound and a dimension-aware ordinary-error criterion.\nThe far-tail inverse has certified geometric upper approximations.\nThe low-mode Schur sign and growing-window G2 remain open.')
anchor2='The successful one-sided bound does not require a norm contraction:'
assert s.count(anchor2)==1
s=s.replace(anchor2,'''Proposition~\\ref{prop:v120-structured-inverse} now reuses the signed
factorization to bound the actual inverse-tail correction, including
all remote rows through \\eqref{eq:v120-structured-finite-rows}.
Proposition~\\ref{prop:v120-structured-uniform} identifies the sufficient
ordinary error $\\alpha_\\lambda+e_\\lambda^2+
 t_\\lambda^2/\\mu_\\lambda$. Its operator norms concern the entire
growing head; individual source or column bounds do not suffice.
Proposition~\\ref{prop:v120-inverse-polynomial} additionally gives
convergent upper bounds for the complete far inverse, with certified
constants at $\\lambda=4$. Its signed polynomial evaluations are the
next concrete refinement of the low-mode correction.
The signed head hypothesis and these uniform inverse scales are still
unproved. The completed analytic reduction supplies no additional
fixed-window positivity or G2 sign claim.

'''+anchor2)
anchor3='\\section{Integration ledger for the complete previous manuscript}'
assert s.count(anchor3)==1
s=s.replace(anchor3,'''\\subsection*{Structured low-mode inverse bounds and their scope}
The low-mode investigation retains the exact $\\lambda=4$ matrix,
$E_{16}$ and the previously certified complete tail. The scripts
\\texttt{certify\\_low\\_schur.py} and
\\texttt{structured\\_low\\_schur.py} evaluate the coarse and structured
inverse bounds, respectively. All original arithmetic diagonals,
normalized parity factors and infinite residual moment bounds remain.
The saved tail witnesses are used as exact dyadics; their hashes and
previously certified congruence margins are checked before reuse.
The outer residual belongs to $\\mathsf W_4$, whereas the reused inner
factors belong to $\\mathsf W_4-10^{-8}D$. Inverse order justifies
that distinction.

These experiments have not certified the low Schur sign. Failed
lower enclosures and their exact diagnostic witnesses are kept in the
research log, not asserted as negative Weil directions. The script \\texttt{certify\\_far\\_inverse.py} verifies the
strict far-inverse constants at 320 and 384 bits; the proof includes
the upper archimedean diagonal bound and the exact pole scale.
The analytic
results of Propositions~\\ref{prop:v120-structured-inverse} and
\\ref{prop:v120-structured-uniform} are proved directly above and
do not rely on the success of a numerical positivity gate.

'''+anchor3)
s=re.sub(r'\\begin\{abstract\}.*?\\end\{abstract\}',lambda m:r"""\begin{abstract}
We study fixed-space prime actions on Burnol's Sonine quotients and
finite Weil forms. Source covariance, compact Mellin division and
Fredholm reduction identify arithmetic boundary and range defects.
For the repaired fixed-order prolate source, tail, endpoint, correlation
and domain estimates establish weak G1. Its polynomial Fourier
projection recovers the physical endpoint and has an exponentially
small ordinary operator residual. These estimates do not identify
the lowest eigenspace or control a growing source block.

The centered Hardy sampler with an endpoint shell preserves ordinary
Gram and Weil-form limits while retaining an explicit graph defect.
Reflected tests and sharp cuts expose endpoint and complex-strip
obstructions. A finite-core metric criterion bypasses the global
arithmetic operator realization. Full-space projection preserves
strip-product bounds and Weil transfer, but its signed commutator
remains uncontrolled.

For the canonical semilocal Weil operator, signed Schur certificates
prove complete positivity and ground ordering at $\lambda=3$.
At $\lambda=4$ the entire tail $|n|>16$ is bounded below by its
positive archimedean energy. A structured inverse estimate retains
this certified tail metric in the low-mode correction, with complete
remote-row and dimension-aware error bounds. Every complete
eigenfunction has zero physical endpoint. Finite source removal
cannot reduce the unsigned prime norm. The low-mode sign and
growing-window estimate remain open; no RH proof is claimed.
\end{abstract}""",s,flags=re.S)
old=set(re.findall(r'\\label\{([^}]+)\}',src));new=re.findall(r'\\label\{([^}]+)\}',s)
assert old.issubset(new) and len(new)==len(set(new))
assert s.count('\\section{')==src.count('\\section{')
assert 'Complete working manuscript, version 1.20' in s
(B/'fixed_space_prime_action_v1.tex').write_text(s)
shutil.copy2(B/'evidence/g2_weighted_signed/build_complete_pdf.py',B/'build_complete_pdf.py')
print('All',len(old),'old labels preserved; now',len(new),'unique labels; version1.20 retained.')
