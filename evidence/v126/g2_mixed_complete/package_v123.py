from pathlib import Path
import json,re,zipfile,hashlib,os
import fitz
B=Path(__file__).resolve().parent
roots=['fixed_space_prime_action_v1.tex','fixed_space_prime_action_v1.pdf','RH_G1_G2_research_log.md','v1_revision_notes.md','v1_validation.json']
s=(B/roots[0]).read_text();old=(B/'input/fixed_space_prime_action_v122.tex').read_text()
labels=re.findall(r'\\label\{([^}]+)\}',s);prior=set(re.findall(r'\\label\{([^}]+)\}',old))
assert len(labels)==len(set(labels)) and prior<=set(labels) and len(prior)==478
ledger=s.split('\\section{Integration ledger for the complete previous manuscript}')[1].split('\\end{longtable}')[0]
assert len(re.findall(r'^\s*\d+\.\d+\s*&',ledger,re.M))==72
warnings=[x for x in (B/'fixed_space_prime_action_v1.log').read_text().splitlines() if re.search('Warning|Overfull|Underfull|undefined|multiply defined',x)]
assert not warnings,warnings
pdf=fitz.open(B/roots[1]);assert len(pdf)==160
assert all(p.get_text().strip() for p in pdf)
names=['refine_inverse.py','mixed_refinement.py','mixed_directional_check.py','mixed_complete_insert.tex','integrate_v123.py','package_v123.py','build_complete_pdf.py','adversarial_mixed_refinement.md','mixed_complete_integration_review.md','finite_polynomial_diagnostics_J65536_b768.json','mixed_directional_witness_J65536.json']
for bits in [768,896]:
 for stem in ['mixed_probe','mixed_vectors','mixed_directional']:names.append(f'{stem}_J65536_b{bits}.json')
newmap={'g2_mixed_complete/'+n:B/n for n in names}
newmap['g2_mixed_complete/input/fixed_space_prime_action_v122.tex']=B/'input/fixed_space_prime_action_v122.tex'
for p in (B/'renders_v123').glob('contact*.jpg'):newmap['g2_mixed_complete/renders/'+p.name]=p
v=json.loads((B/'v1_validation.json').read_text())
v.update({'manuscript_version':'1.23','date':'2026-09-21','pdf_pages':160,'unique_labels':len(labels),'prior_labels_preserved':len(prior),'historical_claims_accounted_for':72,'latex_warning_lines':warnings,'undefined_references':[],'duplicate_labels':[],'visual_review':{'status':'passed','complete_pdf_pages':160,'all_pages_reviewed_in_contact_sheets':True,'new_proofs_and_tables_reviewed_at_full_size':[1,102,103,104,105,153],'layout_corrections':'No clipped text or equations; no remaining LaTeX warning.'},'limitations':'No G2 sign gap closed. Complete first-degree majorant with saved initial head certificate is proved too large on one direction, including its exact induced head update. Higher-degree complete corrections and full head/growing-window signs remain open.'})
v['v123_mixed_refinement']={'proved':['Complete directional mixed remainder including omitted input and output.','Complete far-energy lower by optimizing the omitted norm.','First-degree scalar-head majorant failure on an archived exact actual Weil direction.','Monotone full inverse upper bounds retaining the induced positive head metric.','First-degree failure even with its exact induced head update for baseline M0=muI.','Finite-probe matrix lower bound with explicit omitted pairing error.'],'directional_bits':[768,896],'J':65536,'moment_order':64,'scalar_majorant_lower':'6.7609e-20','updated_head_majorant_lower':'6.6588e-20','trial_upper':'6.4693e-20','complete_lambda4_sign':False,'growing_window_uniformity':False,'finite_higher_degree_experiments':'diagnostic only; remote excursions not certified','adversarial_review':'Passed including separate addendum for the stronger metric-Cauchy failure gate.'}
v['sha256'].update({n:hashlib.sha256((B/n).read_bytes()).hexdigest() for n in roots[:-1]})
v['sha256'].update({n:hashlib.sha256(p.read_bytes()).hexdigest() for n,p in newmap.items()})
oldzip=B/'fixed_space_prime_action_v1_bundle.zip';v['source_bundle_sha256']=hashlib.sha256(oldzip.read_bytes()).hexdigest()
with zipfile.ZipFile(oldzip) as z:v['cumulative_bundle_previous_members']=len(z.namelist())
(B/'v1_validation.json').write_text(json.dumps(v,indent=2)+'\n')
tmp=B/'bundle_v123.tmp.zip'
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
print(json.dumps({'pages':160,'prior_labels':len(prior),'labels':len(labels),'historical_claims':72,'bundle_members':count,'bundle_bytes':oldzip.stat().st_size,'warnings':warnings},indent=2))
ids=[('fixed_space_prime_action_v1.tex','libfile_917c02e02af48191904626b60b218aeb',23),('fixed_space_prime_action_v1.pdf','libfile_efb5d0e5c444819185f4ed729b225882',23),('v1_revision_notes.md','libfile_d5d8a33f6b8c819198e0be7602c5f6e8',23),('RH_G1_G2_research_log.md','libfile_947acdc341748191ab57ed202c5bb37e',26),('v1_validation.json','libfile_b1cb4075cb548191b44d42cdf44a49a6',23),('fixed_space_prime_action_v1_bundle.zip','libfile_386d5bdf90848191b485e716d0205c09',24)]
request={'uploads':[{'local_path':str(B/n),'purpose':'replace_library_file','library_file_id':i,'expected_current_version':ver,'version_reason':'Full v1.23: complete mixed-correlation obstruction, monotone head refinement, and preserved audit history.'} for n,i,ver in ids]}
(B/'library_upload_v123_request.json').write_text(json.dumps(request)+'\n')
