from pathlib import Path
import json,re,zipfile,hashlib,os,shutil
import fitz
B=Path(__file__).resolve().parent;D=B.parent/'v126';D.mkdir(exist_ok=True)
roots=['fixed_space_prime_action_v1.tex','fixed_space_prime_action_v1.pdf','RH_G1_G2_research_log.md','v1_revision_notes.md','v1_validation.json']
s=(B/roots[0]).read_text();old=(B/'input/fixed_space_prime_action_v125.tex').read_text();labels=re.findall(r'\\label\{([^}]+)\}',s);prior=set(re.findall(r'\\label\{([^}]+)\}',old))
assert len(labels)==len(set(labels)) and prior<=set(labels) and len(prior)==505
ledger=s.split('\\section{Integration ledger for the complete previous manuscript}')[1].split('\\end{longtable}')[0]
assert len(re.findall(r'^\s*\d+\.\d+\s*&',ledger,re.M))==72
warn=[x for x in (B/'fixed_space_prime_action_v1.log').read_text().splitlines() if re.search('Warning|Overfull|Underfull|undefined|multiply defined',x)];assert not warn,warn
pdf=fitz.open(B/roots[1]);pages=len(pdf);assert pages==170 and all(p.get_text().strip() for p in pdf)
assert 'version 1.26' in pdf[0].get_text() and 'v1.26' in pdf.metadata['title']
assert json.loads((B/'complete_lambda4_v126_certificate.json').read_text())['status']=='PASS_COMPLETE_ODD_AND_FULL_LAMBDA4'
names=['rank_one_trial.py','directional_tail_repair.py','direction_complement_certificate.py','certify_odd_full_window.py','direction_complement_lemma.tex','localized_error_insert.tex','odd_complement_insert.tex','finish_v126_sign.py','simultaneous_trial.py','posterior_trial.py','mixed_refinement.py','refine_inverse.py','window_scaling_probe.py','joint_remote_gate.py','quantify_head_error.py','complete_lambda4_v126_certificate.json','review_rank_one_trial.md','README_odd_complement.md','package_v126.py','render_v126.py','build_complete_pdf.py']
for pat in ['simultaneous_odd_M4096_s16_normalized*','simultaneous_odd_M4096_s32_normalized*','direction_complement_report_b*.json','directional_odd_M8192_s24*','directional_M8192*progress.txt','rank_one*progress.txt','direction_complement*progress.txt','odd_s16_ordinary_error_progress.txt']:
 names.extend(p.name for p in B.glob(pat) if p.is_file())
newmap={'g2_odd_complement/'+n:B/n for n in sorted(set(names))}
newmap['g2_odd_complement/input/fixed_space_prime_action_v125.tex']=B/'input/fixed_space_prime_action_v125.tex'
for p in (B/'renders_v126').glob('contact*.jpg'):newmap['g2_odd_complement/renders/'+p.name]=p
v=json.loads((B/'v1_validation.json').read_text());v.update({'manuscript_version':'1.26','date':'2026-09-21','pdf_pages':pages,'unique_labels':len(labels),'prior_labels_preserved':len(prior),'historical_claims_accounted_for':72,'latex_warning_lines':warn,'undefined_references':[],'duplicate_labels':[],'visual_review':{'status':'passed','complete_pdf_pages':pages,'all_pages_reviewed_in_contact_sheets':True,'new_proofs_and_tables_reviewed_at_full_size':[1,109,110,111,161],'layout_corrections':'No clipped text or equations; no LaTeX warnings. Current-status statements updated in the reproduction appendix.'},'limitations':'Complete lambda4 form certified positive in both parity sectors. Relative107/250 is not an ordinary spectral gap. Growing-window estimates and RH remain unproved.'})
v['v126_complete_window']={'complete_even_lambda4_sign':True,'complete_odd_lambda4_sign':True,'complete_full_lambda4_sign':True,'full_window_negative_error':0,'old_trial_support':4096,'new_directional_support':8192,'head_dimension':16,'complement_dimension':15,'sigma':'1/1000','s':'429/1000','relative_odd_head_margin':'107/250','directional_verification_bits':[1024,1280],'old_complete_ingredients_bits':768,'complement_replay_bits':[768,896],'complement_replay_reconstructs_old_ingredients':False,'verification_cutoff':65536,'moment_order':64,'adversarial_review':'Passed','exact_fraction_head_identity':'Passed','new_localized_error':'max(sigma-s,0)/(1-sigma) * ||K^(1/2)P_E V^-1||^2','cofinal_convergence_proved':False,'new_G2_uniform_gap_closed':False}
notes=B/'v1_revision_notes.md';nt=notes.read_text().replace('September 21, 2026. Complete working manuscript.','September 21, 2026. Complete170-page working manuscript.',1);notes.write_text(nt)
log=B/'RH_G1_G2_research_log.md';lt=log.read_text();lt=lt.replace('The complete v1.26 LaTeX/PDF integrates', 'The complete170-page v1.26 LaTeX/PDF compiles with no warnings and was visually checked throughout, with the new proof pages inspected individually. It integrates',1);log.write_text(lt)
v['sha256'].update({n:hashlib.sha256((B/n).read_bytes()).hexdigest() for n in roots[:-1]});v['sha256'].update({n:hashlib.sha256(p.read_bytes()).hexdigest() for n,p in newmap.items()})
oldzip=B/'fixed_space_prime_action_v1_bundle.zip';v['source_bundle_sha256']=hashlib.sha256(oldzip.read_bytes()).hexdigest()
with zipfile.ZipFile(oldzip) as z:v['cumulative_bundle_previous_members']=len(z.namelist())
assert v['cumulative_bundle_previous_members']==414
(B/'v1_validation.json').write_text(json.dumps(v,indent=2)+'\n')
readme='''# Complete working manuscript v1.26\n\nAlexander Eastwood — September21,2026 —170pages.\n\nThe PDF and LaTeX at this archive root are both v1.26. The dated filenames below are byte-identical aliases supplied to make the release unambiguous. Older source material is preserved under the historical research subdirectories.\n\nThis revision closes complete positivity at lambda4 (both parity sectors). It does not prove growing-window G2 or RH. New proofs are on pages109–111. The root research log records the failed attempts, complete certificates, assumptions and next target. See g2_odd_complement/README_odd_complement.md for replay instructions.\n'''
(B/'README_v126.md').write_text(readme)
newmap['README_v126.md']=B/'README_v126.md'
tmp=B/'bundle_v126.tmp.zip'
with zipfile.ZipFile(oldzip) as src,zipfile.ZipFile(tmp,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=6) as dst:
 for info in src.infolist():
  if info.filename not in roots and info.filename not in newmap:dst.writestr(info,src.read(info.filename))
 for n in roots:dst.write(B/n,n)
 for n,p in sorted(newmap.items()):dst.write(p,n)
 dst.write(B/roots[0],'fixed_space_prime_action_v1_26.tex');dst.write(B/roots[1],'fixed_space_prime_action_v1_26.pdf')
with zipfile.ZipFile(tmp) as z:
 assert z.testzip() is None and len(z.namelist())==len(set(z.namelist()))
 for n in roots:assert z.read(n)==(B/n).read_bytes()
 assert z.read('fixed_space_prime_action_v1_26.pdf')==z.read('fixed_space_prime_action_v1.pdf')
 assert z.read('fixed_space_prime_action_v1_26.tex')==z.read('fixed_space_prime_action_v1.tex')
 count=len(z.namelist())
os.replace(tmp,oldzip)
paths={'fixed_space_prime_action_v1.tex':'fixed_space_prime_action_v1_26.tex','fixed_space_prime_action_v1.pdf':'fixed_space_prime_action_v1_26.pdf','fixed_space_prime_action_v1_bundle.zip':'fixed_space_prime_action_v1_26_bundle.zip','v1_revision_notes.md':'v1_26_revision_notes.md','RH_G1_G2_research_log.md':'RH_G1_G2_research_log.md','v1_validation.json':'v1_26_validation.json'}
for n,target in paths.items():shutil.copy2(B/n,D/target)
ids=[('fixed_space_prime_action_v1.tex','libfile_917c02e02af48191904626b60b218aeb',26),('fixed_space_prime_action_v1.pdf','libfile_efb5d0e5c444819185f4ed729b225882',26),('v1_revision_notes.md','libfile_d5d8a33f6b8c819198e0be7602c5f6e8',26),('RH_G1_G2_research_log.md','libfile_947acdc341748191ab57ed202c5bb37e',30),('v1_validation.json','libfile_b1cb4075cb548191b44d42cdf44a49a6',27),('fixed_space_prime_action_v1_bundle.zip','libfile_386d5bdf90848191b485e716d0205c09',28)]
(B/'upload_v126_request.json').write_text(json.dumps({'uploads':[{'local_path':str(D/paths[n]),'purpose':'replace_library_file','library_file_id':i,'expected_current_version':ver,'version_reason':'Full v1.26: complete lambda4 positivity, sharp complement gluing and localized growing-window error criterion; G2/RH remain open.'} for n,i,ver in ids]})+'\n')
print(json.dumps({'pages':pages,'labels':len(labels),'prior_labels':len(prior),'historical_claims':72,'warnings':warn,'bundle_members':count,'bundle_bytes':oldzip.stat().st_size,'delivery_path':str(D)},indent=2))
