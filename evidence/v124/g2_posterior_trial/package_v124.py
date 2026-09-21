from pathlib import Path
import json,re,zipfile,hashlib,os
import fitz
B=Path(__file__).resolve().parent
roots=['fixed_space_prime_action_v1.tex','fixed_space_prime_action_v1.pdf','RH_G1_G2_research_log.md','v1_revision_notes.md','v1_validation.json']
s=(B/roots[0]).read_text();old=(B/'input/fixed_space_prime_action_v123.tex').read_text()
labels=re.findall(r'\\label\{([^}]+)\}',s);prior=set(re.findall(r'\\label\{([^}]+)\}',old))
assert len(labels)==len(set(labels)) and prior<=set(labels) and len(prior)==490
ledger=s.split('\\section{Integration ledger for the complete previous manuscript}')[1].split('\\end{longtable}')[0]
assert len(re.findall(r'^\s*\d+\.\d+\s*&',ledger,re.M))==72
warnings=[x for x in (B/'fixed_space_prime_action_v1.log').read_text().splitlines() if re.search('Warning|Overfull|Underfull|undefined|multiply defined',x)]
assert not warnings,warnings
pdf=fitz.open(B/roots[1]);assert len(pdf)==162
assert all(p.get_text().strip() for p in pdf)
names=['posterior_trial.py','posterior_insert.tex','integrate_v124.py','render_v124.py','package_v124.py','build_complete_pdf.py','adversarial_posteriori_refinement.md','posterior_integration_review.md','posterior_replay_README.md','refine_inverse.py','mixed_refinement.py']
for steps in [4,16]:
 names.append(f'posterior_witness_M4096_s{steps}.json.gz')
 for bits in [768,896]:
  report=f'posterior_check_M4096_s{steps}_J65536_b{bits}.json'
  assert json.loads((B/report).read_text())['status']=='PASS_COMPLETE_DIRECTION'
  names.append(report)
for bits in [768,896]:names.append(f'mixed_probe_J65536_b{bits}.json')
newmap={'g2_posterior_trial/'+n:B/n for n in names}
newmap['g2_posterior_trial/input/fixed_space_prime_action_v123.tex']=B/'input/fixed_space_prime_action_v123.tex'
for p in (B/'renders_v124').glob('contact*.jpg'):newmap['g2_posterior_trial/renders/'+p.name]=p
v=json.loads((B/'v1_validation.json').read_text())
v.update({'manuscript_version':'1.24','date':'2026-09-21','pdf_pages':162,'unique_labels':len(labels),'prior_labels_preserved':len(prior),'historical_claims_accounted_for':72,'latex_warning_lines':warnings,'undefined_references':[],'duplicate_labels':[],'visual_review':{'status':'passed','complete_pdf_pages':162,'all_pages_reviewed_in_contact_sheets':True,'new_proofs_and_tables_reviewed_at_full_size':[1,105,106,107,154,155],'layout_corrections':'No clipped text or equations; no remaining LaTeX warning.'},'limitations':'One complete even Schur direction at lambda=4 is now certified positive. Full even and odd head matrix signs and growing-window uniformity remain open. No G2 or RH proof.'})
v['v124_posterior_trial']={'proved':['Exact complete residual verification of any finite trial in the operator domain.','Strict positivity of the complete Schur form on the unchanged archived even head vector, including every infinite residual row.'],'bits':[768,896],'candidate_bits':256,'candidate_steps':[4,16],'M':4096,'J':65536,'moment_order':64,'main_complete_lower':'3.0930e-20','main_complete_upper':'3.2356e-20','main_inverse_correction_upper':'1.424889e-21','supplementary_four_step_lower':'2.9028e-20','complete_one_direction_sign':True,'complete_lambda4_sign':False,'growing_window_uniformity':False,'finite_powers_are_complete_powers':False,'independent_checks':['Dense assembly of nine rows','Expanded energy identity','Frozen dyadic and certificate provenance guards'],'adversarial_review':'Passed; printed remote-Gram upper tightened to make rounded table reproducible.'}
v['sha256'].update({n:hashlib.sha256((B/n).read_bytes()).hexdigest() for n in roots[:-1]})
v['sha256'].update({n:hashlib.sha256(p.read_bytes()).hexdigest() for n,p in newmap.items()})
oldzip=B/'fixed_space_prime_action_v1_bundle.zip';v['source_bundle_sha256']=hashlib.sha256(oldzip.read_bytes()).hexdigest()
with zipfile.ZipFile(oldzip) as z:v['cumulative_bundle_previous_members']=len(z.namelist())
(B/'v1_validation.json').write_text(json.dumps(v,indent=2)+'\n')
tmp=B/'bundle_v124.tmp.zip'
with zipfile.ZipFile(oldzip) as src,zipfile.ZipFile(tmp,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=6) as dst:
 for info in src.infolist():
  if info.filename not in roots and info.filename not in newmap:dst.writestr(info,src.read(info.filename))
 for n in roots:dst.write(B/n,n)
 for n,p in sorted(newmap.items()):dst.write(p,n)
with zipfile.ZipFile(tmp) as z:
 assert z.testzip() is None and len(z.namelist())==len(set(z.namelist()))
 for n in roots:assert z.read(n)==(B/n).read_bytes()
 count=len(z.namelist())
os.replace(tmp,oldzip)
print(json.dumps({'pages':162,'prior_labels':len(prior),'labels':len(labels),'historical_claims':72,'bundle_members':count,'bundle_bytes':oldzip.stat().st_size,'warnings':warnings},indent=2))
ids=[('fixed_space_prime_action_v1.tex','libfile_917c02e02af48191904626b60b218aeb',24),('fixed_space_prime_action_v1.pdf','libfile_efb5d0e5c444819185f4ed729b225882',24),('v1_revision_notes.md','libfile_d5d8a33f6b8c819198e0be7602c5f6e8',24),('RH_G1_G2_research_log.md','libfile_947acdc341748191ab57ed202c5bb37e',27),('v1_validation.json','libfile_b1cb4075cb548191b44d42cdf44a49a6',24),('fixed_space_prime_action_v1_bundle.zip','libfile_386d5bdf90848191b485e716d0205c09',25)]
request={'uploads':[{'local_path':str(B/n),'purpose':'replace_library_file','library_file_id':i,'expected_current_version':ver,'version_reason':'Full v1.24: certified positive complete Schur direction with a frozen finite trial, all remote rows, and preserved audit history.'} for n,i,ver in ids]}
(B/'library_upload_v124_request.json').write_text(json.dumps(request)+'\n')
