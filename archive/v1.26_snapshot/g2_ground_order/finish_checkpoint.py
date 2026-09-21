from pathlib import Path
import os,gzip,hashlib,json,re,zipfile
import fitz
b=Path(__file__).resolve().parent;old=b.parent/'g2_schur_directional'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
t=(b/'fixed_space_prime_action_v1.tex').read_text();labels=re.findall(r'\\label\{([^}]+)\}',t)
assert len(labels)==len(set(labels))==410
assert set(re.findall(r'\\(?:ref|eqref)\{([^}]+)\}',t))<=set(labels)
assert len(fitz.open(b/'fixed_space_prime_action_v1.pdf'))==132
assert t.count('\\section{')==34
assert len(re.findall(r'^\d+\.\d+ &',t,re.M))==72
assert not re.search(r'Warning|Overfull|Underfull',(b/'fixed_space_prime_action_v1.log').read_text())
entry=(b/'checkpoint_entry.md').read_text()
entry+='\n**Completed validation:** 132 pages, 410 unique labels, 32 main sections, two appendices and all 72 historical dispositions. The whole PDF was rendered and visually inspected, with new proof pages 73–75 and changed front/reproduction pages checked at larger scale. The final LaTeX build has no warnings, unresolved references or overflow. A truncated contact-sheet PNG was regenerated; the PDF itself was intact.\n'
oldlog=(old/'RH_G1_G2_research_log.md').read_text().removeprefix('# RH manuscript research log\n\n').replace('## Current research checkpoint:','## Previous research checkpoint:',1)
(b/'RH_G1_G2_research_log.md').write_text('# RH manuscript research log\n\n'+entry+'\n'+oldlog)
notes='''# Complete manuscript v1.17 — September 21, 2026

The complete paper is 132 pages, with 32 main sections, two appendices, 410 unique labels and all 72 historical claim dispositions retained.

**Closed an additional fixed-window obligation:** Proposition 20.27 proves that the complete canonical Weil operator at lambda=3 has a simple even ground state, with 0<mu0<3.644e-38 and mu1>1e-36. Every other even eigenvalue exceeds1e-34. Corollary 20.28 proves ordinary ground-angle sine less than .01931 for the exact normalized P64 p3. The earlier finite-matrix and new complete-operator angle bounds are carefully distinguished.

The proof applies signed interval LDL to lower Schur forms for W-aI, shifting every actual diagonal and every inverse weight. The same exact dyadic inverse-action witnesses pass at 768 and 896 bits: one negative and256 positive even pivots at a=1e-34, and512 positive odd pivots at a=1e-36. A separately certified finite-supported trial has full-form Rayleigh quotient below3.644e-38. That matching direction is essential: a negative pivot of a lower matrix alone does not prove a negative direction of the exact operator. Closed-form square completion, compact resolvent, min--max and prior complete positivity supply the spectral conclusion.

The source-overlap estimate uses the stronger even threshold and an exact finite correction of the rational trial. The v1.13 exact P64-source error transfers the angle by normalization geometry, with an additional error below4e-36. It does not transfer a tiny energy by an ordinary-norm perturbation estimate. No actual-ground endpoint control follows, and the earlier N64 relative endpoint error remains unchanged.

The abstract, status, Section20 proof, Section32 goals, reproduction appendix and bibliography are integrated. The full PDF was rendered and visually inspected, including new proof pages73–75. The final build has no warnings, overflow, or unresolved references. All old labels and all72 ledger dispositions are retained.

The cumulative reproducibility bundle includes the exact inputs, analytic dependencies, signed pivot enclosures, both precision replays, scalar and trial certifiers, internal adverse review and persistent log. A truncated prior ZIP was repaired from the valid older archive and intact v1.16 evidence verified against recorded hashes. The new archive is atomically completed and checked before saving.

**Remaining:** independently justified bounds along unbounded windows, with an error tending to zero or adequate quantitative ground-space overlap, are still required for G2. A larger physical-window block certificate is the next concrete test. Endpoint stability, uniform source-block control, the corrected sampler graph defect and full-strip obligations remain separate. No growing-window G2 gap was closed; no RH proof is claimed. No publication or outside contact occurred.

'''
oldnotes=(old/'v1_revision_notes.md').read_text().replace('# Complete manuscript v1.16 — September 21, 2026','## Previous release: complete manuscript v1.16 — September 21, 2026',1)
(b/'v1_revision_notes.md').write_text(notes+oldnotes)
certs=[]
for parity,N,M,r,a,count,neg in [('even',256,512,80,'1e-34',257,1),('odd',512,1024,100,'1e-36',512,0)]:
 for bits in [768,896]:
  name=f'shift_{a}_N{N}_M{M}_J4096_r{r}_{parity}_b{bits}_diagonal.json';d=json.loads((b/name).read_text())
  assert d['ldl']['status']=='inertia_certified' and d['ldl']['count']==count and d['ldl']['negative_count']==neg
  assert len(d['pivot_enclosures'])==count
  certs.append(dict(file=name,parity=parity,threshold=a,bits=bits,ldl=d['ldl'],witness_sha256=d['witness_uncompressed_sha256']))
 assert certs[-1]['witness_sha256']==certs[-2]['witness_sha256']
 assert hashlib.sha256(gzip.decompress((old/f'schur_witness_N{N}_M{M}_{parity}_b768.json.gz').read_bytes())).hexdigest()==certs[-1]['witness_sha256']
trial=json.loads((b/'full_trial_certificate.json').read_text());assert all(trial['checks'].values())
val=json.loads((old/'v1_validation.json').read_text())
val['retained_v1_16_results']=val['new_results'];val['retained_v1_16_proof_checks']=val['proof_checks'];val['retained_v1_16_certificates']=val['certificates']
val.update(manuscript_version='1.17',date='2026-09-21',pdf_pages=132,unique_labels=410,
 visual_review='All132 pages rendered and visually reviewed; new proof73–75, title, goals and reproduction appendix checked at larger scale. A truncated contact-sheet PNG was regenerated. Final build has no warnings, unresolved references or overflow.',
 new_results=[
 'Proposition20.27: computer-assisted complete lambda3 ground ordering: simple even ground,0<mu0<3.644e-38,mu1>1e-36, all other even eigenvalues>1e-34.',
 'Corollary20.28: exact normalized P64 p3 and rational candidate have sine angle<.01931 to actual whole-operator ground.',
 'Verified finite-supported correction with exact full-form Rayleigh identity beta=alpha-E/(1+q^2), beta<3.644e-38.'],
 proof_checks=[
 'Every diagonal and tail inverse weight shifted; same exact dyadic Z retains its finite middle residual.',
 'All finite rows recomputed and infinite remote moment Gram retained with shifted inverse denominator.',
 'Signed LDL continues through negative pivots; each pivot excludes0.',
 'Even lower inertia1 at1e-34 and odd lower inertia0 at1e-36 verified at768 and896bits with identical witnesses.',
 'Negative lower-form pivot not treated as actual negative direction; independent finite-supported Rayleigh trial supplies existence.',
 'Closed-form square completion transfers negative index and kernels; minmax and compact resolvent give global simplicity/parity.',
 'Exact finite-correction Rayleigh identity independently verified; ordinary overlap uses complete even threshold, not compression gap.',
 'Exact projected-source coefficient certificate imported with candidate hash check; normalized-distance geometry below4e-36.',
 'All prior labels,72 ledger dispositions, endpoint convention, Fourier cut and explicit sampler graph defect retained.'],
 certificates=certs,
 numerical_illustrations='Final spectral claims are computer-assisted fixed-window results combining exact analytic identities, infinite-tail bounds and outward interval certificates. Failed odd1e-34 and ineffective full-residual/gap tests remain exploratory in log.',
 limitations='Growing-window G2 and RH remain open. No unprojected-source identification, ground-state endpoint comparison, uniform source block or endpoint-normalized graph estimate follows.',
 archive_repair='Prior saved v1.16 ZIP was truncated. Recovered cumulative archive from valid v1.15 plus37 hash-verified v1.16 artifacts and intact root documents; recovered ZIP42113921bytes,118members,allCRCpass. Current archive uses atomic completion and independent verification.')
roots=['fixed_space_prime_action_v1.tex','fixed_space_prime_action_v1.pdf','RH_G1_G2_research_log.md','v1_revision_notes.md']
newfiles=['certify_shifted_inertia.py','certify_trial_reuse.py','certify_ground_overlap_constants.py','ground_overlap_scalar_certificate.json','full_trial_certificate.json','g2_finite_candidate.json','g2_finite_certificate.json','ground_order_derivation.md','ground_order_insert.tex','certified_trial_reuse.md','REPRODUCE_v117.md','checkpoint_entry.md','integrate_v117.py','finish_checkpoint.py']
newfiles += [p.name for p in sorted(b.glob('shift_*.json'))]
for n in roots:val['sha256'][n]=sha(b/n)
for n in newfiles:val['sha256']['g2_ground_order/'+n]=sha(b/n)
(b/'v1_validation.json').write_text(json.dumps(val,indent=2)+'\n')
roots+=['v1_validation.json']
base=old/'fixed_space_prime_action_v1_bundle_recovered.zip'
assert base.stat().st_size==42113921
with zipfile.ZipFile(base) as z:assert z.testzip() is None
output=b/'fixed_space_prime_action_v1_bundle.zip';tmp=b/'bundle_complete.tmp'
with open(tmp,'wb') as f:
 with zipfile.ZipFile(base) as z,zipfile.ZipFile(f,'w',zipfile.ZIP_DEFLATED) as out:
  for info in z.infolist():
   if info.filename not in roots:out.writestr(info,z.read(info.filename))
  for n in roots:out.write(b/n,n)
  for n in newfiles:out.write(b/n,'g2_ground_order/'+n)
 f.flush();os.fsync(f.fileno())
os.replace(tmp,output)
fd=os.open(b,os.O_RDONLY);os.fsync(fd);os.close(fd)
with zipfile.ZipFile(output) as z:
 assert z.testzip() is None
 assert len(z.namelist())==len(set(z.namelist()))
 members=len(z.namelist())
summary=dict(bytes=output.stat().st_size,sha256=sha(output),members=members,crc='PASS')
(b/'bundle_integrity.json').write_text(json.dumps(summary,indent=2)+'\n')
requests=json.loads((old/'upload_requests.json').read_text())
for item in requests['uploads']:
 item['local_path']=str(b/Path(item['local_path']).name)
 item['expected_current_version']+=1
 item['version_reason']='Complete manuscript v1.17: certified complete lambda3 simple even ground, spectral ordering and exact projected-source ordinary overlap. Growing-window G2 and RH remain open; cumulative evidence archive repaired.'
(b/'upload_requests.json').write_text(json.dumps(requests,indent=2)+'\n')
print(json.dumps(summary));print('132pages;410labels;72ledger dispositions;four passed shifted certificates.')
