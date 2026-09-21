from pathlib import Path
import gzip,hashlib,json,re,zipfile
from pypdf import PdfReader

b=Path(__file__).resolve().parent
old=b.parent/'g2_signed_tail'
entry=(b/'checkpoint_entry.md').read_text()
oldlog=(old/'RH_G1_G2_research_log.md').read_text().removeprefix('# RH manuscript research log\n\n').replace('## Current research checkpoint:','## Previous research checkpoint:',1)
(b/'RH_G1_G2_research_log.md').write_text('# RH manuscript research log\n\n'+entry+'\n'+oldlog)
notes='''# Complete manuscript v1.16 — September 21, 2026

The complete paper is 129 pages, with 32 main sections, two appendices, 407 unique labels and all 72 historical claim dispositions retained.

**Closed fixed-window obligation:** Proposition 20.26 gives a computer-assisted proof of strict coercivity of the complete canonical closed Weil form at lambda=3. Both complex parity sectors and the entire infinite Fourier complement are included. This strengthens the earlier finite-matrix certificates; it does not close growing-window G2 or prove RH.

The proof combines four supported improvements. Proposition 20.22 uses the positive physical weight cosh(x-log3) to reduce the prime-shift norm bound to 2.6890557719..., with all endpoint comparisons certified. Proposition 20.23 retains the increasing tail diagonal and proves inverse order. Proposition 20.24 bounds every remote residual row using exact Fourier moments and a controlled geometric remainder. Proposition 20.25 combines these with the complete signed Schur identity.

For the even sector the head has 257 dimensions, N256/M512/J4096/r80. For the odd sector it has 512 dimensions, N512/M1024/J4096/r100. All finite rows and the infinite remote moment Grams are included. Every pivot of each final interval LDL decomposition is strictly positive. The witnesses are exact frozen dyadic matrices, and their middle residuals are explicitly retained. Independent replays at 896 bits using the identical witnesses reproduce both 768-bit certificates. The reported pivots are not spectral lower bounds; the paper asserts existence, without a numerical value, of a positive complete-form coercivity constant.

The abstract, status, Section 20, Section 32 research goals and appendix are integrated. New material is on pages 67–73, with the reproduction summary on 124. All 129 PDF pages were rendered and visually reviewed, including detailed inspection of the new proof pages. The complete LaTeX build has no warnings or unresolved references. The historical 72-row ledger is unchanged apart from its release heading.

The cumulative bundle retains prior audit/reproducibility material and adds the new proofs, scripts, interval outputs, both exact witnesses, precision replays, internal adverse review and research log. Exploratory failures of weaker sufficient bounds are recorded as failures of those bounds, never as negative Weil-form results. No publication or outside contact occurred.

**Remaining:** a lower error tending to zero along an unbounded window sequence, or sufficiently strong independent ground-space overlap, is still required for G2. At the fixed window the next concrete certificate can use W-aI to establish ground-state ordering and parity, with both diagonal and tail weights shifted consistently. Source-to-ground endpoint stability, the corrected sampler graph defect and full-strip obligations remain separate. Earlier weak G1 and ordinary source-residual results are unchanged. No RH proof is claimed.

'''
oldnotes=(old/'v1_revision_notes.md').read_text().replace('# Complete manuscript v1.15 — September 21, 2026','## Previous release: complete manuscript v1.15 — September 21, 2026',1)
(b/'v1_revision_notes.md').write_text(notes+oldnotes)
t=(b/'fixed_space_prime_action_v1.tex').read_text()
labels=re.findall(r'\\label\{([^}]+)\}',t)
assert len(labels)==len(set(labels))==407
assert len(PdfReader(b/'fixed_space_prime_action_v1.pdf').pages)==129
assert t.count('\\section{')==34
assert not re.search(r'Warning|Overfull|Underfull',(b/'fixed_space_prime_action_v1.log').read_text())
assert set(re.findall(r'\\(?:ref|eqref)\{([^}]+)\}',t))<=set(labels)
certificates=[]
for sector,N,M,r in [('even',256,512,80),('odd',512,1024,100)]:
    for bits in [768,896]:
        name=f'infinite_schur_N{N}_M{M}_J4096_r{r}_{sector}_b{bits}_diagonal.json'
        d=json.loads((b/name).read_text());assert d['ldl']['status']=='positive'
        assert d['ldl']['count']==(N+1 if sector=='even' else N)
        certificates.append(dict(file=name,parity=sector,bits=bits,
                                 witness_sha256=d['witness_uncompressed_sha256'],
                                 ldl=d['ldl']))
    assert certificates[-2]['witness_sha256']==certificates[-1]['witness_sha256']
    w=gzip.decompress((b/f'schur_witness_N{N}_M{M}_{sector}_b768.json.gz').read_bytes())
    assert hashlib.sha256(w).hexdigest()==certificates[-1]['witness_sha256']
val=json.loads((old/'v1_validation.json').read_text())
val['retained_v1_15_results']=val['new_results']
val['retained_v1_15_proof_checks']=val['proof_checks']
val.update(manuscript_version='1.16',pdf_pages=129,unique_labels=407,
 visual_review='All 129 PDF pages rendered and reviewed in nine contact sheets. New proof pages 67–73, title, appendix 124 and final bibliography checked at higher resolution. One incomplete page 75 PNG was rerendered and verified; the PDF build itself has no warnings, unresolved references or overflow.',
 new_results=[
 'Proposition20.22: certified independent positive-weight prime-shift norm bound at lambda3; stronger entire Fourier-tail constants.',
 'Proposition20.23: increasing diagonal domination of the actual tail and inverse-order comparison.',
 'Proposition20.24: explicit directional moment Gram enclosure for every remote residual row, including full parity and scale factors.',
 'Proposition20.25: complete signed Schur sufficient lower bound using diagonal inverse weights and the full remote Gram.',
 'Proposition20.26: computer-assisted strict coercivity of the complete canonical closed Weil form at lambda3, both complex parity sectors and the entire infinite complement.'],
 proof_checks=[
 'Physical positive-weight Schur comparison uses every active prime-power shift; full-length m9 vanishes exactly.',
 'Finite scalar endpoint comparisons use exact rational coefficients and Arb outward enclosures.',
 'Common base-cut losses retained in all increasing diagonal weights; inverse order justified on closed form domain.',
 'Exact dyadic frozen inverse-action witnesses; every intervening residual including middle rounding residual retained.',
 'Complete actual diagonal used on finite rows; divided differences used only for disjoint remote rows.',
 'Remote moment PSD congruence retains source-direction cancellation; cMr count, Hurwitz argument J+1, both signed tails and parity sqrt2 checked.',
 'Archimedean coefficients have explicit uniform exponential-series remainder radii.',
 'All 8,321 parity matrix entries through N64 overlap prior independent integral certificate.',
 'All 257 even and 512 odd LDL pivots certified at 768 bits; same exact witnesses independently replayed at 896 bits.',
 'Coercivity derived by square completion, never inferred from pivot size as a spectral lower bound.',
 'All 72 historical dispositions preserved apart from release headings; no raw-transfer or critical-beta claim restored.'],
 certificates=certificates,
 numerical_illustrations='Exploratory float and finite-output pilots are not proof inputs. Final result is a computer-assisted fixed-window proof using analytic infinite-tail bounds and outward interval arithmetic. Every pivot is enclosed; no numerical spectral gap is asserted.',
 limitations='The signed fixed-window obligation at lambda3 is closed. G2 along unbounded windows and RH are open. No actual-ground/source identification, ground simplicity, endpoint stability, growing-block uniform bound or endpoint-normalized graph estimate follows.')
roots=['fixed_space_prime_action_v1.tex','fixed_space_prime_action_v1.pdf','RH_G1_G2_research_log.md','v1_revision_notes.md']
skip=set(roots+['v1_validation.json','upload_requests.json','upload_receipt.json'])
newfiles=[]
for p in sorted(b.iterdir()):
    if p.name in skip or not p.is_file():continue
    if p.name.startswith('pilot_blocks_'):continue
    if p.name.endswith('_b896.json.gz'):continue
    if p.suffix in ['.py','.md','.tex','.json'] or p.name.endswith('_b768.json.gz'):
        newfiles.append(p.name)
for name in roots:val['sha256'][name]=hashlib.sha256((b/name).read_bytes()).hexdigest()
for name in newfiles:val['sha256']['g2_schur_directional/'+name]=hashlib.sha256((b/name).read_bytes()).hexdigest()
(b/'v1_validation.json').write_text(json.dumps(val,indent=2)+'\n')
roots+=['v1_validation.json']
with zipfile.ZipFile(old/'fixed_space_prime_action_v1_bundle.zip') as z,zipfile.ZipFile(b/'fixed_space_prime_action_v1_bundle.zip','w',zipfile.ZIP_DEFLATED) as out:
    for info in z.infolist():
        if info.filename not in roots:out.writestr(info,z.read(info.filename))
    for name in roots:out.write(b/name,name)
    for name in newfiles:out.write(b/name,'g2_schur_directional/'+name)
with zipfile.ZipFile(b/'fixed_space_prime_action_v1_bundle.zip') as z:
    assert z.testzip() is None
    assert len(z.namelist())==len(set(z.namelist()))
    print('Cumulative bundle:',len(z.namelist()),'members,',round((b/'fixed_space_prime_action_v1_bundle.zip').stat().st_size/1024**2,2),'MiB')
requests=json.loads((old/'upload_requests.json').read_text())
for item in requests['uploads']:
    item['local_path']=str(b/Path(item['local_path']).name)
    item['expected_current_version']+=1
    item['version_reason']='Complete manuscript v1.16: certified positivity of the full canonical Weil form at lambda3, both parity sectors and infinite complement; uniform G2 and RH remain open.'
(b/'upload_requests.json').write_text(json.dumps(requests,indent=2)+'\n')
print('v1.16 checkpoint complete:129pages,407labels, four passed full certificates and exact witnesses.')
