"""Replay exactly the saved dyadic witnesses at a fresh, higher precision."""
import argparse, json, hashlib, math, time
from pathlib import Path
import numpy as np
from shifted_floor import setup, arb, arb_mat
BASE=Path(__file__).resolve().parent

def pack():
    arrays={};brief=[]
    for lam in (5,6,8):
        for parity in ('even','odd'):
            path=BASE/f'floor_l{lam}_{parity}_N256_b160.json'
            d=json.loads(path.read_text());key=f'l{lam}_{parity}'
            ans=d['attempts'][-1];assert ans['status']=='PASS' and ans['shift']=='8'
            def val(me):return math.ldexp(float(int(me[0])),int(me[1]))
            arrays[key+'_C']=np.array([[val(x) for x in row] for row in ans['C_dyadic']],dtype='<f8')
            arrays[key+'_v']=np.array([val(x) for x in d['trial']['vector_dyadic']],dtype='<f8')
            for i,row in enumerate(ans['C_dyadic']):
                for j,(m,e) in enumerate(row):
                    assert arb(float(arrays[key+'_C'][i,j]))==arb(m)*arb(2)**int(e)
            ans={k:v for k,v in ans.items() if k!='C_dyadic'}
            brief.append({'window':lam,'parity':parity,'parameters':d['parameters'],'tail':d['tail'],'certificate':ans,'trial':{k:v for k,v in d['trial'].items() if k!='vector_dyadic'},'seconds':d['seconds']})
    np.savez_compressed(BASE/'dyadic_witnesses.npz',**arrays)
    (BASE/'initial_certificates.json').write_text(json.dumps(brief,indent=2)+'\n')

def replay(bits):
    source=BASE/'dyadic_witnesses.npz';w=np.load(source,allow_pickle=False);rows=[]
    for lam in (5,6,8):
        for parity in ('even','odd'):
            begin=time.time();key=f'l{lam}_{parity}'
            F,R,U,I,gs,gJ,meta=setup(lam,256,4096,16,bits,parity);nh=F.nrows()
            # This is the exact IEEE754 witness frozen at the first precision.
            C=arb_mat([[arb(float(x)) for x in row] for row in w[key+'_C']])
            v=arb_mat([[arb(float(x))] for x in w[key+'_v']])
            assert C.nrows()==C.ncols()==nh and v.nrows()==nh
            assert all(C[i,j].is_exact() for i in range(nh) for j in range(nh))
            assert all(v[i,0].is_exact() for i in range(nh))
            assert all(C[i,j]==0 for i in range(nh) for j in range(i+1,nh))
            assert all(C[i,i]!=0 for i in range(nh))
            assert gs[0]+8>0
            weighted=arb_mat([[R[i,j]/(gs[i]+8) for j in range(nh)] for i in range(R.nrows())])
            corr=R.transpose()*weighted+U/(gJ+8)
            K=F+8*I;low=K-corr
            Y=C*low*C.transpose();Z=C*K*C.transpose()
            lm=[Y[i,i]-sum((abs(Y[i,j]) for j in range(nh) if i!=j),arb(0)) for i in range(nh)]
            km=[Z[i,i]+sum((abs(Z[i,j]) for j in range(nh) if i!=j),arb(0)) for i in range(nh)]
            assert all(x>arb(999)/1000 for x in lm)
            m=arb(999)/1000
            M=arb(math.ceil(1000*max(float(x.upper()) for x in km))+1)/1000
            # Floating proposals choose rational thresholds only; all proof
            # comparisons are strict outward interval gates.
            assert all(x>m for x in lm) and all(x<M for x in km)
            margin=m/M
            q=(v.transpose()*F*v)[0,0]/(v.transpose()*v)[0,0]
            assert q>0 and q<arb(1)/10**16
            row={'lambda':lam,'parity':parity,'precision_bits':bits,'all_shifted_form_gates_pass':True,
             'ordinary_lower_floor':'-8','frozen_trial_rayleigh_interval':q.str(65),
             'trial_upper_below':'1e-16','trial_negative':False,'tail_shifted_floor':(gs[0]+8).str(65),
             'verified_whitened_lower_m':m.str(45),'verified_whitened_head_upper_M':M.str(45),
             'generalized_certificate_margin_lower':margin.str(45),
             'generalized_margin_definition':'1-lambda_max(corr,K), K=F+8I. Reported m/M is a certified lower bound, not an exact eigenvalue.',
             'seconds':round(time.time()-begin,3)}
            rows.append(row);print(json.dumps(row),flush=True)
    out={'scope':'All six complete parity forms >= -8 I. All six frozen trial quotients positive and <1e-16. No uniform-in-window bound proved.',
      'witness_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),'parameters':{'shift':8,'N':256,'J':4096,'moment_order':16,'tau':'1/10','Z':0,'arch_series_terms':64,'bits':bits},'certificates':rows}
    (BASE/f'replay_b{bits}.json').write_text(json.dumps(out,indent=2)+'\n')

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--pack',action='store_true');p.add_argument('--bits',type=int,default=256);a=p.parse_args()
    if a.pack:pack()
    replay(a.bits)
