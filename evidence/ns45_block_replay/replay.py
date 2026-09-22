"""Fresh NS-45 dyadic witnesses for the existing lambda=5 N=25 block criterion.

Proposals use floating point only. Gates use fresh Arb coefficients and exact
frozen dyadics at two precisions, including signed-index pairing expansions.
No full block inertia is asserted or needed for the metric dichotomy.
"""
from __future__ import annotations
import argparse
from fractions import Fraction
import hashlib
import json
import os
import sys
import tempfile
from pathlib import Path
from typing import Any
os.environ.setdefault('OPENBLAS_NUM_THREADS','1')
os.environ.setdefault('VECLIB_MAXIMUM_THREADS','1')
import numpy as np
from scipy.linalg import cholesky, solve_triangular, svd
from flint import arb, arb_mat, ctx
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'evidence/v124/g2_schur_cancellation'))
import assembly_general as assembly
OUT=Path(__file__).resolve().parent
BLOCKS=[list(range(26,51)),list(range(51,101)),list(range(101,201))]
PAIRS=[(0,1),(0,2),(1,2)]
FREEZE_BITS=60


def fresh_sequences(bits: int) -> tuple[Any,Any,Any,Any]:
    """Rebuild analytic coefficient balls with a temporary, empty cache."""
    with tempfile.TemporaryDirectory(prefix='ns45-coeff-') as scratch:
        previous=assembly.B
        try:
            assembly.B=Path(scratch)
            result=assembly.sequences(5,200,bits,K=96)
            assert len(result)==4
            return result[0],result[1],result[2],result[3]
        finally:
            assembly.B=previous


def propose() -> None:
    """Float solves/SVD only propose exact dyadics and rational lower entries."""
    path=OUT/'witnesses.json'
    if path.exists():
        raise RuntimeError('Frozen witnesses already exist; replay with --verify.')
    _,bs,ds,_=fresh_sequences(192)
    records: dict[str,Any]={}
    for parity in ('even','odd'):
        diag=[]; chols=[]
        for rows in BLOCKS:
            wb=assembly.block(rows,rows,parity,bs,ds)
            wf=np.array([[float(wb[i,j].mid()) for j in range(len(rows))] for i in range(len(rows))])
            diag.append(wf); chols.append(cholesky(wf,lower=True))
        pieces=[]
        for j,k in PAIRS:
            wb=assembly.block(BLOCKS[j],BLOCKS[k],parity,bs,ds)
            cross=np.array([[float(wb[r,c].mid()) for c in range(len(BLOCKS[k]))] for r in range(len(BLOCKS[j]))])
            matrix=solve_triangular(chols[j],cross,lower=True)
            matrix=solve_triangular(chols[k],matrix.T,lower=True).T
            left,values,right=svd(matrix,full_matrices=False)
            x=solve_triangular(chols[j].T,left[:,0],lower=False)
            y=solve_triangular(chols[k].T,right[0,:],lower=False)
            x/=np.linalg.norm(x);y/=np.linalg.norm(y)
            ints_x=[int(round(float(v)*2**FREEZE_BITS)) for v in x]
            ints_y=[int(round(float(v)*2**FREEZE_BITS)) for v in y]
            h_numerator=max(0,int(np.floor(values[0]*1000))-2)
            pieces.append({'blocks':[j,k],'x_indices':BLOCKS[j],'y_indices':BLOCKS[k],
                'x_numerators':ints_x,'y_numerators':ints_y,'denominator_power_of_two':FREEZE_BITS,
                'H_numerator':h_numerator,'H_denominator':1000,
                'proposal_singular_value_only':float(values[0])})
            print('PROPOSAL',parity,j,k,'sv',values[0],'H',h_numerator,'/1000',flush=True)
        ray=2*sum((Fraction(p['H_numerator'],p['H_denominator']) for p in pieces),Fraction(0))/3
        if ray<=1:
            raise RuntimeError(f'First-three proposed rational Rayleigh gate fails in {parity}: {ray}')
        records[parity]={'pairs':pieces,'rayleigh_vector':[1,1,1],
                         'rayleigh_numerator':ray.numerator,'rayleigh_denominator':ray.denominator}
    path.write_text(json.dumps({'lambda':5,'tail_start':25,'blocks':BLOCKS,
        'classification':'exact dyadic proposals and rational comparison matrix; no gate proved by proposal',
        'parities':records},indent=2)+'\n')


def signed_pairing(rows_x: list[int], numerators_x: list[int], rows_y: list[int],
                   numerators_y: list[int], exponent: int, parity: str, bs: Any, ds: Any) -> Any:
    """Bilinear pairing via explicit +/- Fourier coordinates, not block()."""
    sign=1 if parity=='even' else -1
    indices_x=rows_x+[-n for n in rows_x]
    indices_y=rows_y+[-n for n in rows_y]
    positive_x=[arb(n)/(arb(2)**exponent*arb(2).sqrt()) for n in numerators_x]
    positive_y=[arb(n)/(arb(2)**exponent*arb(2).sqrt()) for n in numerators_y]
    xx=positive_x+[sign*v for v in positive_x]
    yy=positive_y+[sign*v for v in positive_y]
    total=arb(0)
    for i,n in enumerate(indices_x):
        bn=bs[abs(n)] if n>0 else -bs[abs(n)]
        for j,m in enumerate(indices_y):
            bm=bs[abs(m)] if m>0 else -bs[abs(m)]
            entry=ds[abs(n)] if n==m else (bn-bm)/(n-m)
            total+=xx[i]*yy[j]*entry
    return total


def verify() -> None:
    """Every proof gate uses balls or exact rational/integer arithmetic."""
    path=OUT/'witnesses.json';document=json.loads(path.read_text())
    assert document['lambda']==5 and document['tail_start']==25 and document['blocks']==BLOCKS
    assert set(document['parities'])=={'even','odd'}
    runs=[]
    for bits in (320,448):
        _,bs,ds,_=fresh_sequences(bits)
        for parity,record in document['parities'].items():
            assert parity in ('even','odd') and record['rayleigh_vector']==[1,1,1]
            ray_sum=Fraction(0);checked_pairs=[]
            assert [tuple(p['blocks']) for p in record['pairs']]==PAIRS
            for pair in record['pairs']:
                j,k=pair['blocks']; rows_x=pair['x_indices'];rows_y=pair['y_indices']
                assert rows_x==BLOCKS[j] and rows_y==BLOCKS[k]
                exponent=pair['denominator_power_of_two']; nx=pair['x_numerators'];ny=pair['y_numerators']
                assert exponent==FREEZE_BITS and all(type(n) is int for n in nx+ny)
                assert len(nx)==len(rows_x) and len(ny)==len(rows_y)
                x=arb_mat([[arb(n)/arb(2)**exponent] for n in nx])
                y=arb_mat([[arb(n)/arb(2)**exponent] for n in ny])
                wjj=assembly.block(rows_x,rows_x,parity,bs,ds)
                wkk=assembly.block(rows_y,rows_y,parity,bs,ds)
                wjk=assembly.block(rows_x,rows_y,parity,bs,ds)
                ex=(x.transpose()*wjj*x)[0,0];ey=(y.transpose()*wkk*y)[0,0]
                cross=(x.transpose()*wjk*y)[0,0]
                hh=Fraction(pair['H_numerator'],pair['H_denominator'])
                assert hh>=0
                h=arb(hh.numerator)/hh.denominator
                gap=cross**2-h**2*ex*ey
                assert ex>0 and ey>0 and gap>0
                sx=signed_pairing(rows_x,nx,rows_x,nx,exponent,parity,bs,ds)
                sy=signed_pairing(rows_y,ny,rows_y,ny,exponent,parity,bs,ds)
                sc=signed_pairing(rows_x,nx,rows_y,ny,exponent,parity,bs,ds)
                signed_gap=sc**2-h**2*sx*sy
                assert sx>0 and sy>0 and signed_gap>0
                assert (ex-sx).contains(0) and (ey-sy).contains(0) and (cross-sc).contains(0)
                ratio=abs(cross)/(ex*ey).sqrt()
                assert ratio>h
                digits=int(bits*.30103)-10
                values={'energy_x':ex,'energy_y':ey,'cross_pairing':cross,'coupling_ratio':ratio,
                    'squared_gate_gap':gap,'signed_energy_x':sx,'signed_energy_y':sy,
                    'signed_cross_pairing':sc,'signed_squared_gate_gap':signed_gap,
                    'energy_x_assembly_difference':ex-sx,'energy_y_assembly_difference':ey-sy,
                    'cross_assembly_difference':cross-sc}
                item={'blocks':[j,k],'H_numerator':hh.numerator,'H_denominator':hh.denominator,
                      **{name:value.str(digits) for name,value in values.items()},
                      'gates':{'both_energies_strictly_positive':True,'normalized_coupling_strictly_above_H':True,
                               'signed_index_energies_strictly_positive':True,'signed_index_squared_gate_positive':True,
                               'all_three_assemblies_overlap':True}}
                checked_pairs.append(item);ray_sum+=hh
                print(bits,parity,j,k,'ratio',ratio.str(15),'H',str(hh),'positive squared gap',gap.str(10),flush=True)
            ray=2*ray_sum/3
            assert ray.numerator==record['rayleigh_numerator'] and ray.denominator==record['rayleigh_denominator']
            assert ray>1
            runs.append({'bits':bits,'parity':parity,'pairs':checked_pairs,
                         'exact_rayleigh_numerator':ray.numerator,'exact_rayleigh_denominator':ray.denominator,
                         'exact_rayleigh_strictly_above_one':True})
            print('EXACT RAYLEIGH',bits,parity,str(ray),'>1',flush=True)
    sources=['evidence/v124/g2_schur_cancellation/assembly_general.py','evidence/ns45_block_replay/replay.py']
    certificate={'classification':'CERTIFIED COMPUTATION: fresh strict interval gates at two precisions',
        'scope':'Existing lambda=5 N=25 partition; first three blocks 26:50,51:100,101:200, both parities; failure of the norm comparison only',
        'not_original_recovery':True,'full_block_inertia_not_asserted':True,
        'logic':'If 0<M_j<=T_jj exist, each T_jj is positive definite and the verified positive-energy pair ratios lower-bound beta_jk(T); the exact rational H has Rayleigh quotient >1. Otherwise the prerequisite metrics do not exist. In either case the specified criterion cannot hold.',
        'analytic_series_terms':96,'fresh_assembly':True,
        'witness_sha256':hashlib.sha256(path.read_bytes()).hexdigest(),
        'source_sha256':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in sources},'runs':runs}
    (OUT/'certificate.json').write_text(json.dumps(certificate,indent=2)+'\n')


def main() -> None:
    if not __debug__:
        raise RuntimeError('Do not disable the interval proof gates with Python -O.')
    parser=argparse.ArgumentParser();parser.add_argument('--propose',action='store_true');parser.add_argument('--verify',action='store_true');args=parser.parse_args()
    if args.propose:propose()
    if args.verify:verify()
    if not args.propose and not args.verify:parser.error('choose --propose and/or --verify')

if __name__=='__main__':main()
