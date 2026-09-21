from pathlib import Path
import json,zipfile,hashlib,os
B=Path(__file__).resolve().parent
names=['window_resolution_probe.py','head_reduction_audit.py','window_resolution_checkpoint.md','review_window_resolution.md','window_scaling_probe.py','simultaneous_trial.py','posterior_trial.py','mixed_refinement.py','refine_inverse.py','package_resolution_checkpoint.py']
for pattern in ['resolution_l8_*_forms.json','resolution_l8_*_report.json','resolution_l8_*_metric_*.json','resolution_l8_*_constant_head.json']:
 names.extend(p.name for p in B.glob(pattern))
newmap={'g2_window_resolution/'+n:B/n for n in sorted(set(names))}
vpath=B/'v1_validation.json';v=json.loads(vpath.read_text());assert v['manuscript_version']=='1.25'
v['post_v125_resolution']={'manuscript_unchanged':True,'lambda':8,'bits':4096,'arch_series_terms':256,'cuts':[256,384,512],'heads':[64,36,0],'finite_brackets':{'head64_256_384':['5.697e-101','5.755e-101'],'head64_384_512':['1.349e-44','1.363e-44'],'head36_256_384':['1.155e-93','1.168e-93'],'head0_256_384':['9.5263e-42','9.5264e-42'],'head0_384_512':['1.4535e-14','1.4536e-14']},'adversarial_review':'Passed','complete_lambda8_sign':False,'new_G2_gap_closed':False,'scope':'Finite loss persists for scalar physical head. No cofinal or omitted-tail conclusion.'}
v['sha256']['RH_G1_G2_research_log.md']=hashlib.sha256((B/'RH_G1_G2_research_log.md').read_bytes()).hexdigest()
v['sha256'].update({n:hashlib.sha256(p.read_bytes()).hexdigest() for n,p in newmap.items()})
vpath.write_text(json.dumps(v,indent=2)+'\n')
roots=['RH_G1_G2_research_log.md','v1_validation.json'];old=B/'fixed_space_prime_action_v1_bundle.zip';temp=B/'resolution_checkpoint.tmp.zip'
with zipfile.ZipFile(old) as src,zipfile.ZipFile(temp,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=6) as dst:
 for info in src.infolist():
  if info.filename not in roots and info.filename not in newmap:dst.writestr(info,src.read(info.filename))
 for n in roots:dst.write(B/n,n)
 for n,p in newmap.items():dst.write(p,n)
with zipfile.ZipFile(temp) as z:
 assert z.testzip() is None and len(z.namelist())==len(set(z.namelist()))
 assert b'working manuscript, version 1.25' in z.read('fixed_space_prime_action_v1.tex')
 for n,p in newmap.items():assert hashlib.sha256(z.read(n)).hexdigest()==v['sha256'][n]
 print({'members':len(z.namelist()),'bytes':temp.stat().st_size})
os.replace(temp,old)
ids=[('RH_G1_G2_research_log.md','libfile_947acdc341748191ab57ed202c5bb37e',29),('v1_validation.json','libfile_b1cb4075cb548191b44d42cdf44a49a6',26),('fixed_space_prime_action_v1_bundle.zip','libfile_386d5bdf90848191b485e716d0205c09',27)]
(B/'upload_resolution_request.json').write_text(json.dumps({'uploads':[{'local_path':str(B/n),'purpose':'replace_library_file','library_file_id':i,'expected_current_version':ver,'version_reason':'Preserve post-v1.25 finite cutoff/head resolution research; released manuscript remains v1.25.'} for n,i,ver in ids]})+'\n')
