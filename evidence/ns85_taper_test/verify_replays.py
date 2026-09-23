"""Replay finite taper gates; full zero-free or asymptotic statements absent."""
from __future__ import annotations
import hashlib
import json
from pathlib import Path
import sys
from typing import Any
from flint import arb, arb_mat, ctx

HERE=Path(__file__).resolve().parent
KERNEL_PATH=HERE.parent/'v159/ns61/certify_smoothed.py'
sys.path.insert(0,str(KERNEL_PATH.parent))
from certify_smoothed import Kernel, mobius


def main() -> None:
    ctx.prec=384
    low=json.loads((HERE/'taper-256bits.json').read_text())
    high=json.loads((HERE/'taper-384bits.json').read_text())
    cutoff=json.loads((HERE/'taper-cutoff-384bits.json').read_text())
    source=hashlib.sha256((HERE/'certify_taper.py').read_bytes()).hexdigest()
    dependency=hashlib.sha256(KERNEL_PATH.read_bytes()).hexdigest()
    for report in [low,high,cutoff]:
        assert report['source_sha256']==source
        assert report['mobius_source_sha256']==dependency
    assert low['precision_bits']==256 and high['precision_bits']==384
    matches=0
    for left,right in zip(low['rows'],high['rows'],strict=True):
        assert left['N']==right['N'] and left['cell_stop']==right['cell_stop']
        assert left['values'].keys()==right['values'].keys()
        for key in left['values']:
            assert arb(left['values'][key]).overlaps(arb(right['values'][key])),(left['N'],key)
            matches+=1
        v={k:arb(x) for k,x in right['values'].items()}
        assert 0<v['one_atom_fitted_energy']<v['exterior_balanced_energy']<v['complete_energy']
    first,last=high['rows'][-1],cutoff['rows'][0]
    assert first['N']==last['N']==1024
    assert last['cell_stop']==2*first['cell_stop']
    assert cutoff['kernel_cutoff']==2*high['kernel_cutoff']
    cutkeys=['complete_energy','one_atom_fitted_energy','exterior_balanced_energy','sigma1_pairing','eta','prefix_energy_1_to_N']
    for key in cutkeys:
        assert arb(first['values'][key]).overlaps(arb(last['values'][key])),key
    assert arb(last['values']['tail_radius'])<arb(first['values']['tail_radius'])/3
    independent=[]
    for bits,report in [(256,low),(384,high)]:
        ctx.prec=bits
        kernel=Kernel(16,128,24)
        cs=arb_mat([[-mobius(n)*(1-arb(n).log()/arb(16).log())] for n in range(1,17)])
        loads=arb_mat([[kernel.load(n)] for n in range(1,17)])
        gram=arb_mat([[kernel.gram(i,j) for j in range(1,17)] for i in range(1,17)])
        full=2-2*(loads.transpose()*cs)[0,0]+(cs.transpose()*gram*cs)[0,0]
        values=report['rows'][0]['values']
        assert arb(values['complete_energy']).overlaps(full)
        pairing=loads[0,0]-(gram*cs)[0,0]
        eta=sum((cs[n-1,0]/n for n in range(1,17)),arb(0))
        fitted=full-pairing*pairing/gram[0,0]
        balanced=full+2*eta*pairing+eta*eta*gram[0,0]
        assert arb(values['one_atom_fitted_energy']).overlaps(fitted)
        assert arb(values['exterior_balanced_energy']).overlaps(balanced)
        independent.append({'bits':bits,'N':16,'full_gram_error':full.str(65),'one_atom_fitted':fitted.str(65),'exterior_balanced':balanced.str(65)})
    baseline_path=HERE.parent/'v160/ns71/preconditioner-384bits.json'
    baseline=json.loads(baseline_path.read_text())
    old=next(row for row in baseline['rows'] if row['N']==256)
    new=next(row for row in high['rows'] if row['N']==256)
    ratio=arb(new['values']['one_atom_fitted_energy'])/arb(old['energy'])
    assert ratio>3200
    result: dict[str,Any]={'classification':'finite replay checks; no cofinal estimate or independent human audit',
                          'status':'PASS','precision_matches':matches,'same_problem_cutoff_matches':len(cutkeys),
                          'source_sha256':source,'dependency_sha256':dependency,
                          'N256_one_atom_error_over_full_optimum':ratio.str(30),
                          'inherited_optimum_path':str(baseline_path.relative_to(HERE.parents[1])),
                          'inherited_optimum_sha256':hashlib.sha256(baseline_path.read_bytes()).hexdigest(),
                          'independent_Gram_comparisons':independent,'tail_radius_reduced_by_more_than_three':True,
                          'all_errors_positive_and_controls_ordered':True,'RH_proved':False}
    (HERE/'replay-validation.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'status':'PASS','precision_matches':matches,'cutoff_matches':len(cutkeys),'independent_Gram_comparisons':6}))

if __name__=='__main__':
    main()
