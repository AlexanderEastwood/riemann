from pathlib import Path
import re,json,hashlib,os,zipfile,gzip
import fitz
b=Path(__file__).resolve().parent;old=b/'current'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def write(p,s):
 with open(p,'w') as f:f.write(s);f.flush();os.fsync(f.fileno())
t=(b/'fixed_space_prime_action_v1.tex').read_text();s=(old/'fixed_space_prime_action_v1.tex').read_text();labels=re.findall(r'\\label\{([^}]+)\}',t)
assert len(labels)==len(set(labels))==442
assert set(re.findall(r'\\label\{([^}]+)\}',s))<=set(labels)
assert set(re.findall(r'\\(?:ref|eqref)\{([^}]+)\}',t))<=set(labels)
ledger=lambda x:re.findall(r'^\d+\.\d+ &.*$',x,re.M)
assert ledger(t)==ledger(s) and len(ledger(t))==72 and t.count('\\section{')==34
assert not re.search('Warning|Overfull|Underfull',(b/'fixed_space_prime_action_v1.log').read_text())
with fitz.open(b/'fixed_space_prime_action_v1.pdf') as d:
 assert len(d)==143 and all(p.get_text().strip() for p in d)
certs=[]
for par in ['even','odd']:
 name=f'weighted_tail_l4_s16_{par}_b320.json';p=b/name;report=json.loads(p.read_text());assert report['status']=='PASS' and report['all_Gershgorin_rows_positive']
 witness=f'weighted_witness_l4_s16_{par}_b256.json.gz';assert hashlib.sha256(gzip.decompress((b/witness).read_bytes())).hexdigest()==report['witness_sha256']
 report['reproduction_witness']=witness
 write(p,json.dumps(report,indent=2)+'\n');certs.append(report)
assert json.loads((b/'weighted_norm_counterexample.json').read_text())['status']=='PASS'
entry=(b/'checkpoint_entry.md').read_text()+'\n**Completed validation:** v1.20 has143 pages,442 unique labels,32 main sections,two appendices and the unchanged72-claim historical ledger. All431 prior labels remain. Both320-bit frozen-witness parity replays pass every sign gate, with lower Gershgorin margins above0.9999999999. Every PDF page was rendered and visually reviewed; new proof pages90–93,title,research-goal page127 and reproduction page137 received detailed review. The final LaTeX build has no warnings, unresolved references or overflow. The cumulative archive is checked for CRC and exact hashes of all current deliverables and new evidence.\n'
oldlog=(old/'RH_G1_G2_research_log.md').read_text().removeprefix('# RH manuscript research log\n\n').replace('## Current research checkpoint:','## Previous research checkpoint:',1)
write(b/'RH_G1_G2_research_log.md','# RH manuscript research log\n\n'+entry+'\n'+oldlog)
notes='''# Complete manuscript v1.20 — September 21, 2026

The complete manuscript has143 pages,442 unique labels,32 main sections,two appendices and all72 historical claim dispositions. All431 prior labels and the physical endpoint, literal Fourier cut, logarithmic diagonal and sampler graph defect are retained.

**New signed estimate:** Proposition20.47 proves QW4(f,f)>=10^-8 sum(-A_n)|f_n|^2 for every complex closed-form vector with literal Fourier support|n|>16. The exact archimedean diagonal is positive there, with a proved lower bound>1.7940. The entire infinite tail in both parity sectors is included. This closes a larger fixed-window tail-sign obligation; it does not establish full lambda4 positivity or growing-window G2.

The certificate retains the actual prime,pole and archimedean entries. A positive physical weight gives a prime upper bound<4.624042316766478. Signed verified solves use heads17..512 and17..1536, with every residual through4096 and explicit infinite moment remainders. Frozen exact dyadic solve and congruence witnesses pass320-bit interval verification of every Gershgorin row. The same witnesses were generated at256 bits; even256 was also replayed under the final gates. This is internal computer-assisted validation, not an outside referee check.

Proposition20.48 certifies a positive dyadic trial with energy/archimedean-energy ratio>2.05254. Thus the two-sided weighted remainder norm contraction fails even though the one-sided sign bound succeeds. It is not a negative Weil direction.

Proposition20.44 proves the sharp weighted-error conversion -eta*C/(1+eta), preventing a dimensionless error from being mistaken for the ordinary error required by G2. Proposition20.45 proves the weighted prime operator and the exact weighted remainder are compact but in no finite Schatten class; a whole-tail Frobenius budget is therefore invalid, while finite-column residual Grams remain valid. Proposition20.46 proves the sharp logarithmic weighted-tail asymptotic at fixed window, explicitly without a uniform joint-limit inference.

The abstract,status,Section20,research goals,reproduction appendix and bibliography are integrated. The PDF is compiled without warnings and visually reviewed throughout, including detailed new-proof checks. The cumulative bundle contains proof scripts, exact witnesses, interval reports, exploratory diagnostics, adverse review and the persistent log. The log records an early discarded pole-denominator coding error and the subsequent exact comparison and all-row gate corrections; no invalid intermediate is presented as a result.

**Remaining:** full lambda4 positivity requires the signed effective head F-B*T^-1*B on17 even+16 odd coordinates. Raw finite-matrix positivity is insufficient. Uniform signed control along growing windows remains RH-strength and is still open. No growing-window G2 sign gap was closed; no RH proof is claimed. No publication or outside contact occurred.

'''
write(b/'v1_revision_notes.md',notes+(old/'v1_revision_notes.md').read_text().replace('# Complete manuscript v1.19 — September 21, 2026','## Previous release: complete manuscript v1.19 — September 21, 2026',1))
v=json.loads((old/'v1_validation.json').read_text())
for k in ['new_results','proof_checks','certificates']:v['retained_v1_19_'+k]=v.get(k)
v.update(manuscript_version='1.20',date='2026-09-21',pdf_pages=143,unique_labels=442,
 visual_review='Every page rendered and visually reviewed; new proof90–93,title,research goals127,reproduction137 inspected in detail. No final LaTeX warning or overflow.',
 new_results=['Complete signed energy control at lambda4 on literal|n|>16, both parity sectors and every infinite tail row included.','Certified two-sided weighted norm contraction failure from a positive dyadic direction.','Sharp ordinary-error conversion eta*C/(1+eta).','Weighted prime/remainder compactness without any finite Schatten class.','Sharp fixed-window logarithmic weighted-tail norm asymptotic, with no joint-limit claim.'],
 proof_checks=['Every prime-bound candidate dominated by the selected exact upper endpoint.','Exact separate pole and archimedean diagonals.','Analytic arch floor at index17 positive.','Complete signed finite residual rows and infinite moment Gram.','All rows of dyadic-congruence Gershgorin inequalities positive at320 bits.','Identical saved witness hashes in both precision replays.','Complex parity decomposition covers the entire literal tail.','All431 old labels and72ledgerrows retained.'],
 certificates=certs,
 limitations='Fixed lambda4 tail only: effective low head and growing-window G2/RH remain open. No uniform recurrence bound or infinite Hilbert-Schmidt budget.',
 internal_adversarial_review='Independent agent reviewed analytic proofs, source normalization, signed shifted diagonal, parity and all interval gates. Corrections are recorded in the log.',
 primary_sources=v.get('primary_sources',[])+[{'url':'https://arxiv.org/html/2511.22755v1','use':'Actual Fourier matrix conventions, already used in the manuscript.'},{'url':'https://arxiv.org/abs/2608.24827v2','use':'Contextual comparison with finite-window certification and pointwise-comb barrier; no certificate imported.'}])
roots=['fixed_space_prime_action_v1.tex','fixed_space_prime_action_v1.pdf','RH_G1_G2_research_log.md','v1_revision_notes.md']
newfiles=['weighted_signed_insert.tex','adversarial_weighted_review.md','assembly_general.py','certify_weighted_tail.py','certify_weighted_counterexample.py','weighted_pilot.py','weighted_pilot.json','weighted_norm_counterexample.json','weighted_tail_l4_s16_even_b256.json','weighted_tail_l4_s16_even_b320.json','weighted_tail_l4_s16_odd_b320.json','weighted_witness_l4_s16_even_b256.json.gz','weighted_witness_l4_s16_odd_b256.json.gz','sequences_v2_l4_J256_b256.json','sequences_v2_l4_J4096_b256.json','sequences_v2_l4_J4096_b320.json','checkpoint_entry.md','REPRODUCE_v120.md','integrate_v120.py','build_complete_pdf.py','finish_checkpoint.py']
for n in roots:v['sha256'][n]=sha(b/n)
for n in newfiles:v['sha256']['g2_weighted_signed/'+n]=sha(b/n)
write(b/'v1_validation.json',json.dumps(v,indent=2)+'\n');roots+=['v1_validation.json']
base=old/'fixed_space_prime_action_v1_bundle.zip';assert sha(base)=='7760e07a2928876e9b9e5d5ecbfc356b6ba3057364ca7183593717a25690ab7b'
with zipfile.ZipFile(base) as z:assert z.testzip() is None and len(z.namelist())==160
outpath=b/'fixed_space_prime_action_v1_bundle.zip';tmp=b/'bundle_complete.tmp'
with open(tmp,'wb') as f:
 with zipfile.ZipFile(base) as z,zipfile.ZipFile(f,'w',zipfile.ZIP_DEFLATED) as out:
  for info in z.infolist():
   if info.filename not in roots:out.writestr(info,z.read(info.filename))
  for n in roots:out.write(b/n,n)
  for n in newfiles:out.write(b/n,'g2_weighted_signed/'+n)
 f.flush();os.fsync(f.fileno())
os.replace(tmp,outpath)
with zipfile.ZipFile(outpath) as z:
 assert z.testzip() is None and len(z.namelist())==len(set(z.namelist()))==160+len(newfiles)
 for n in roots:assert hashlib.sha256(z.read(n)).hexdigest()==sha(b/n)
 for n in newfiles:assert hashlib.sha256(z.read('g2_weighted_signed/'+n)).hexdigest()==sha(b/n)
summary={'bytes':outpath.stat().st_size,'sha256':sha(outpath),'members':160+len(newfiles),'crc':'PASS','current_hashes':'PASS'};write(b/'bundle_integrity.json',json.dumps(summary,indent=2)+'\n')
ids=[('fixed_space_prime_action_v1.tex','libfile_917c02e02af48191904626b60b218aeb',19),('fixed_space_prime_action_v1.pdf','libfile_efb5d0e5c444819185f4ed729b225882',19),('v1_revision_notes.md','libfile_d5d8a33f6b8c819198e0be7602c5f6e8',19),('RH_G1_G2_research_log.md','libfile_947acdc341748191ab57ed202c5bb37e',20),('v1_validation.json','libfile_b1cb4075cb548191b44d42cdf44a49a6',19),('fixed_space_prime_action_v1_bundle.zip','libfile_386d5bdf90848191b485e716d0205c09',20)]
write(b/'upload_requests.json',json.dumps({'uploads':[{'local_path':str(b/n),'purpose':'replace_library_file','library_file_id':i,'expected_current_version':ver,'version_reason':'Complete v1.20: certified signed energy estimate on both full lambda4 Fourier tails beyond16; weighted-error scaling and compactness limits. Low head and growing-window G2 remain open.'} for n,i,ver in ids]},indent=2)+'\n')
print(json.dumps(summary));print('143pages;442labels;72ledgerrows;both320-bit complete-tail certificatesPASS')
