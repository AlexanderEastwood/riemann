from pathlib import Path
import hashlib,json,re,zipfile
from pypdf import PdfReader

b=Path(__file__).resolve().parent
old=b.parent/'g2_deep_next'
entry=(b/'checkpoint_entry.md').read_text()
for a,z in [('All123','All 123'),('has392','has 392'),('The72','The 72'),('pages65','pages 65'),('and73','and 73'),('on118','on 118'),('Section20','Section 20'),('Section32','Section 32'),('even257','even 257'),('odd256','odd 256')]:entry=entry.replace(a,z)
(b/'checkpoint_entry.md').write_text(entry)
oldlog=(old/'RH_G1_G2_research_log.md').read_text().removeprefix('# RH manuscript research log\n\n').replace('## Current research checkpoint:','## Previous research checkpoint:',1)
(b/'RH_G1_G2_research_log.md').write_text('# RH manuscript research log\n\n'+entry+'\n'+oldlog)

notes='''# Complete manuscript v1.15 — September 21, 2026

The full manuscript is 123 pages, with 32 main sections, two appendices, 392 unique labels and all 72 historical dispositions retained.

**Closed prerequisites:** Lemma 20.27 proves a nonzero ordinary L2 limit of the exact repaired source and its polynomial Fourier projection. Proposition 20.28 proves their actual full semilocal Weil operator residual is O(lambda^6 exp(-2*pi*lambda^2/3)). Their ordinarily normalized Rayleigh values and centered residuals therefore tend to zero. This uses the existing uniformly quantified Sobolev G1 and Fourier coefficient-tail results, with a new output split. The exponentially large auxiliary output cutoff does not change the actual polynomial source cutoff. No effective threshold at lambda=3 is asserted.

**Sharper infinite complement:** Proposition 20.21 retains the weighted degree of physical prime shifts, the decaying negative pole Fourier tail, and the limiting archimedean commutator. At lambda=3 the complete omitted Fourier complement beyond N=256 is bounded below by 0.0148 times the norm squared; the even complement has bound 1.5867. The exact scalar evaluations were enclosed with 256-bit Arb arithmetic and independently rerun. This is not a certificate for the remaining finite head or its Schur correction.

**Remaining G2 target:** Equation 181 keeps the exact signed Schur complement and improves its verified-solve bound by retaining the residual Gram matrix R*R/Gamma before taking a scalar norm. The sign of this corrected finite head remains open. The revised overlap calibration now uses proved source residual/Rayleigh inputs, but still requires an independent quantitative lowest-eigenspace overlap. Tiny residual alone does not exclude a negative level orthogonal to the source. No G2 sign gap or RH proof is claimed.

The source, first-slot-linear convention, physical endpoint, Fourier cut, logarithmic diagonal and corrected sampler graph defect are preserved. The new ordinary residual does not become a small endpoint-normalized residual and does not control a growing prolate block. Source-to-ground endpoint stability, graph/full-strip comparison and the alternative arithmetic shell sign remain separate obligations.

The abstract, status, Section 20, Section 32 and appendix are updated throughout. The main additions are on pages 65–68 and 73–76; the scalar certificate summary is on page 118. All pages were rendered and reviewed, with close inspection of the new proof pages. The final LaTeX build has no warnings, unresolved references or overfull/underfull boxes. The bibliography was compacted to avoid a one-entry final page. The historical ledger is unchanged apart from version headings.

Two internal reviewers checked the new operator residual; the tail constants and parity were separately audited. This is not external referee verification. The bundle preserves all earlier evidence and adds the derivations, proof inserts, review reports, interval checker and output, and the v1.15 reproduction guide.

Next: a directional inverse-action certificate for the lambda=3,N=256 head and its infinite complement, retaining the full error Gram matrix. A proof of G2 additionally needs growing-window lower control.

'''
oldnotes=(old/'v1_revision_notes.md').read_text().replace('# Complete manuscript v1.14 — September 21, 2026','## Previous release: complete manuscript v1.14 — September 21, 2026',1)
(b/'v1_revision_notes.md').write_text(notes+oldnotes)

guide=b/'G2_v115_Research_and_Reproduction.md'
g=guide.read_text()
for a,z in [('is123','is 123'),('Proposition20','Proposition 20'),('Lemma20','Lemma 20'),('Equation181','Equation 181'),('Lemma7','Lemma 7'),('Python3','Python 3'),('python-flint0.9','python-flint 0.9'),('FLINT3.6','FLINT 3.6')]:g=g.replace(a,z)
guide.write_text(g)

t=(b/'fixed_space_prime_action_v1.tex').read_text()
labels=re.findall(r'\\label\{([^}]+)\}',t)
assert len(labels)==len(set(labels))==392
assert len(PdfReader(b/'fixed_space_prime_action_v1.pdf').pages)==123
assert t.count('\\section{')==34
assert not re.search(r'Warning|Overfull|Underfull',(b/'fixed_space_prime_action_v1.log').read_text())
refs=set(re.findall(r'\\(?:eqref|ref)\{([^}]+)\}',t))
assert refs<=set(labels),refs-set(labels)
val=json.loads((old/'v1_validation.json').read_text())
val['retained_v1_14_results']=val['new_results']
val['retained_v1_14_proof_checks']=val['proof_checks']
val.update(manuscript_version='1.15',pdf_pages=123,unique_labels=392,
 visual_review='All 123 pages rendered and visually inspected in eight contact sheets. New material pages65–68,73–76 and final bibliography inspected at higher resolution. Isolated incomplete PNGs regenerated. Final complete render verifies every page; no clipping/overlap observed. No LaTeX warnings or unresolved references.',
 new_results=[
 'Proposition20.21: explicit sharp complete and even Fourier-tail lower bounds; at lambda3,N256 the entire omitted complement is positive.',
 'Lemma20.27: exact Hermite/co-Poisson source limit in ordinary L2 with O(lambda^-1/2) error, including source normalization and repair; source and polynomial projection norms bounded away from zero.',
 'Proposition20.28: full actual operator residual O(lambda^6 exp(-2pi lambda^2/3)) for source and its literal polynomial Fourier projection; normalized Rayleigh and centered residual prerequisites proved.',
 'Equation181: exact Schur verified-solve identity with directional residual Gram lower bound before scalarization.',
 'Updated conditional overlap calibration: residual/ground overlap tending to zero would suffice; no overlap lower bound proved.'],
 proof_checks=[
 'Fixed-mode Hermite sup approximation transferred to unit normalization via squared-norm expansion.',
 'Correct limiting scalar4pi/sqrt3, exact source moments, inversion-even co-Poisson limit and nonzero ordinary norm.',
 'Uniform full Sobolev estimate used by duality for arbitrary output cutoffs, including modezero; no sqrtM summation loss.',
 'Graph tail retains complete logarithmic diagonal and bounded commutator; weighted Chebyshev O(lambda) constants.',
 'High-low Hilbert–Schmidt bound lambda^2 N/M; auxiliary output M distinct from actual source cutoff.',
 'Prime degree exact on physical interval, zero full-length m9 shift removed only as an L2 zero operator.',
 'Binet exact remainder, trigamma sum and finite-L complete diagonal constants retained.',
 'Tail pole scale and even-sector positive Hilbert matrix verified in both centered and unshifted Fourier phases.',
 'Two independent internal residual audits; separate adverse tail review and repeated scalar Arb check.',
 'Tiny residual explicitly not used to infer bottom ordering or endpoint-normalized control.',
 'All72 historical dispositions retained apart from version headings.'],
 numerical_illustrations='New results analytic. New scalar256-bit Arb bounds independently evaluated; no new finite head or Schur certificate. Earlier finite matrix/source certificates retained without reruns.',
 limitations='Ordinary mass/Rayleigh/full residual prerequisites closed; no G2 sign gap or RH proof. Positive omitted tail does not establish signed effective head. No growing-block operator control, endpoint-normalized graph bound, practical asymptotic residual threshold or lowest-eigenspace overlap is established.')
val['sharp_tail_constants']=json.loads((b/'sharp_tail_constants.json').read_text())
val['primary_input'].extend([
 {'title':'CCM,Zeta Spectral Triples,Lemma7.2','url':'https://arxiv.org/html/2511.22755v1','used':'Uniform fixed-mode Hermite approximation; exact normalization and ordinary co-Poisson norm convergence derived in current proof.'},
 {'title':'NIST DLMF5.9.15','url':'https://dlmf.nist.gov/5.9.E15','used':'Exact Binet digamma formula.'},
 {'title':'NIST DLMF5.15.1','url':'https://dlmf.nist.gov/5.15.E1','used':'Convergent trigamma series.'}])
newfiles=['G2_v115_Research_and_Reproduction.md','operator_residual_derivation.md','residual_insert.tex','sharp_arch_tail.md','sharp_tail_insert.tex','adversarial_review.md','operator_residual_independent_audit.md','check_sharp_tail_constants.py','sharp_tail_constants.json','checkpoint_entry.md','integrate_v115.py','finish_checkpoint.py']
roots=['fixed_space_prime_action_v1.tex','fixed_space_prime_action_v1.pdf','RH_G1_G2_research_log.md','v1_revision_notes.md']
for name in roots:val['sha256'][name]=hashlib.sha256((b/name).read_bytes()).hexdigest()
for name in newfiles:val['sha256']['g2_signed_tail/'+name]=hashlib.sha256((b/name).read_bytes()).hexdigest()
(b/'v1_validation.json').write_text(json.dumps(val,indent=2)+'\n')
roots+=['v1_validation.json']
with zipfile.ZipFile(old/'fixed_space_prime_action_v1_bundle.zip') as z,zipfile.ZipFile(b/'fixed_space_prime_action_v1_bundle.zip','w',zipfile.ZIP_DEFLATED) as out:
 for info in z.infolist():
  if info.filename not in roots:out.writestr(info,z.read(info.filename))
 for name in roots:out.write(b/name,name)
 for name in newfiles:out.write(b/name,'g2_signed_tail/'+name)
with zipfile.ZipFile(b/'fixed_space_prime_action_v1_bundle.zip') as z:
 assert z.testzip() is None
 assert len(z.namelist())==len(set(z.namelist()))
 print('Cumulative bundle members:',len(z.namelist()))
print('v1.15 assembled:123 pages;392 labels; full history retained.')
