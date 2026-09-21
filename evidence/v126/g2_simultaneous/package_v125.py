from pathlib import Path
import json,re,zipfile,hashlib,os
import fitz
B=Path(__file__).resolve().parent
roots=['fixed_space_prime_action_v1.tex','fixed_space_prime_action_v1.pdf','RH_G1_G2_research_log.md','v1_revision_notes.md','v1_validation.json']
s=(B/roots[0]).read_text();old=(B/'input/fixed_space_prime_action_v124.tex').read_text()
labels=re.findall(r'\\label\{([^}]+)\}',s);prior=set(re.findall(r'\\label\{([^}]+)\}',old))
assert len(labels)==len(set(labels)) and prior<=set(labels) and len(prior)==496
ledger=s.split('\\section{Integration ledger for the complete previous manuscript}')[1].split('\\end{longtable}')[0]
assert len(re.findall(r'^\s*\d+\.\d+\s*&',ledger,re.M))==72
warnings=[x for x in (B/'fixed_space_prime_action_v1.log').read_text().splitlines() if re.search('Warning|Overfull|Underfull|undefined|multiply defined',x)]
assert not warnings,warnings
pdf=fitz.open(B/roots[1]);assert len(pdf)==166 and all(p.get_text().strip() for p in pdf)
names=['simultaneous_trial.py','joint_remote_gate.py','quantify_head_error.py','complete_margin.py','window_scaling_probe.py','replay_finite_margin.py','simultaneous_insert.tex','integrate_v125.py','render_v125.py','package_v125.py','document_v125.py','build_complete_pdf.py','adversarial_simultaneous_review.md','adversarial_window_scaling_review.md','simultaneous_integration_review.md','simultaneous_replay_README.md','window_scaling_report.md','posterior_trial.py','mixed_refinement.py','refine_inverse.py','mixed_probe_J65536_b768.json','mixed_probe_J65536_b896.json']
for pattern in ['simultaneous_*_witness.json.gz','simultaneous_*_ingredients_b*.json','simultaneous_*_report_b*.json','simultaneous_*_ordinary_error_b*.json','simultaneous_*_joint_lower_b*.json','complete_even_relative_margin_b*.json','window_scaling_far_cuts_b*.json','window_scaling_l8_metric_witness_b4096.json','window_scaling_l8_margin_bracket_b4096.json','window_scaling_l*_even_r256_o384_b4096.json']:
 names.extend(p.name for p in B.glob(pattern))
names=sorted(set(names));newmap={'g2_simultaneous/'+n:B/n for n in names}
newmap['g2_simultaneous/input/fixed_space_prime_action_v124.tex']=B/'input/fixed_space_prime_action_v124.tex'
newmap['g2_low_schur/low_witness_odd_M256_b768.json.gz']=B/'recovered/g2_low_schur/low_witness_odd_M256_b768.json.gz'
for p in (B/'renders_v125').glob('contact*.jpg'):newmap['g2_simultaneous/renders/'+p.name]=p
for bits in [768,896]:
 assert json.loads((B/f'simultaneous_even_M4096_s16_normalized_report_b{bits}.json').read_text())['status']=='PASS_COMPLETE_HEAD'
 assert json.loads((B/f'complete_even_relative_margin_b{bits}.json').read_text())['status']=='PASS_COMPLETE_EVEN_RELATIVE_MARGIN'
window_records=[json.loads((B/f'window_scaling_l{lam}_even_r256_o384_b4096.json').read_text()) for lam in [3,4,5,6,8]]
v=json.loads((B/'v1_validation.json').read_text())
v.update({'manuscript_version':'1.25','date':'2026-09-21','pdf_pages':166,'unique_labels':len(labels),'prior_labels_preserved':len(prior),'historical_claims_accounted_for':72,'latex_warning_lines':warnings,'undefined_references':[],'duplicate_labels':[],'visual_review':{'status':'passed','complete_pdf_pages':166,'all_pages_reviewed_in_contact_sheets':True,'new_proofs_and_tables_reviewed_at_full_size':[1,107,108,109,157,158,159,161],'layout_corrections':'No clipped text/equations or LaTeX warnings. Updated historical-disposition heading and Galerkin spelling without pagination change.'},'limitations':'Complete even lambda4 form certified positive. Odd lambda4 remains inconclusive; growing-window complete estimates remain open. Finite scaling probes are not complete-tail certificates. No G2 or RH proof.'})
v['v125_simultaneous']={'complete_even_lambda4_sign':True,'complete_lambda4_both_parities_sign':False,'growing_window_uniformity':False,'witness_support':4096,'verification_cutoff':65536,'moment_order':64,'candidate_bits':512,'candidate_steps':16,'head_dimension':17,'replay_bits':[768,896],'certified_generalized_margin_lower':'62629/100000','minimum_coordinate_pivot_lower':'0.7645944101','joint_remote_optional_bits':768,'joint_remote_hypothesis':'0 <= L_Y <= Y*Y; A0>0','new_analytic_result':'Current scalar far bound forces N+1 > L exp(M_phi/(1-c)), with asymptotic exponential rate at least1/(1-c).','method_scope':'This cutoff cost is not a lower bound for every possible proof.','adversarial_review':'Passed after explicit nonnegative lower-Gram hypothesis correction.','numerical_reliability':'New safe LDL uses x*x rather than generic interval power to avoid false-inconclusive NaNs; proof gates remain outward interval arithmetic.'}
v['v125_window_scaling']={'cuts':[256,384],'bits':4096,'full_remote_certificate_available_in_this_probe':False,'finite_tail_and_head_positive':[r['lambda'] for r in window_records if r['finite_tail_sign_certified'] and r['finite_head_sign_interval_certified']],'lambda8_finite_margin_certified_bracket':['5.697e-101','5.755e-101'],'finite_margin_diagnostics':{str(r['lambda']):r['dimensionless_generalized_margin_FINITE'] for r in window_records},'scope':'Separate finite numerical diagnostic. Complete certificate above remains lambda4 even only.'}
v['sha256'].update({n:hashlib.sha256((B/n).read_bytes()).hexdigest() for n in roots[:-1]})
v['sha256'].update({n:hashlib.sha256(p.read_bytes()).hexdigest() for n,p in newmap.items()})
oldzip=B/'fixed_space_prime_action_v1_bundle.zip';v['source_bundle_sha256']=hashlib.sha256(oldzip.read_bytes()).hexdigest()
with zipfile.ZipFile(oldzip) as z:v['cumulative_bundle_previous_members']=len(z.namelist())
assert v['cumulative_bundle_previous_members']==336
(B/'v1_validation.json').write_text(json.dumps(v,indent=2)+'\n')
tmp=B/'bundle_v125.tmp.zip'
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
print(json.dumps({'pages':166,'prior_labels':len(prior),'labels':len(labels),'historical_claims':72,'bundle_members':count,'bundle_bytes':oldzip.stat().st_size,'warnings':warnings},indent=2))
ids=[('fixed_space_prime_action_v1.tex','libfile_917c02e02af48191904626b60b218aeb',25),('fixed_space_prime_action_v1.pdf','libfile_efb5d0e5c444819185f4ed729b225882',25),('v1_revision_notes.md','libfile_d5d8a33f6b8c819198e0be7602c5f6e8',25),('RH_G1_G2_research_log.md','libfile_947acdc341748191ab57ed202c5bb37e',28),('v1_validation.json','libfile_b1cb4075cb548191b44d42cdf44a49a6',25),('fixed_space_prime_action_v1_bundle.zip','libfile_386d5bdf90848191b485e716d0205c09',26)]
request={'uploads':[{'local_path':str(B/n),'purpose':'replace_library_file','library_file_id':i,'expected_current_version':ver,'version_reason':'Full v1.25: complete even lambda4 sign certificate, relative margin, joint remote bound and growing-window cost audit.'} for n,i,ver in ids]}
(B/'library_upload_v125_request.json').write_text(json.dumps(request)+'\n')
