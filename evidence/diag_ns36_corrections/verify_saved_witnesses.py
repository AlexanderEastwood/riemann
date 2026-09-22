"""NS-36 diagnostic cross-check of frozen vectors, energies and source approximations.

Rechecks saved decimal coefficients instead of trusting optimization status.
All level masses remain float quadratures, not interval bounds.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

import mpmath as mp
import numpy as np
from flint import ctx

ROOT = Path(__file__).resolve().parents[2]
OUT = Path(__file__).resolve().parent
sys.path[:0] = [str(ROOT/'evidence/v124/g2_schur_cancellation'), str(OUT)]
from assembly_general import block, sequences
from feasibility_repair import matrices


def main() -> None:
    mp.mp.dps = 130
    base = json.loads((OUT/'feasibility_grid1.json').read_text())
    first = json.loads((OUT/'source_projection_M90_d130_grid1.json').read_text())
    second = json.loads((OUT/'source_projection_M110_d170_grid2.json').read_text())
    sources = [mp.matrix(row['source']['normalized_cosine_coefficients']) for row in (first, second)]
    source_distance = min(mp.norm(sources[0]-sources[1]),mp.norm(sources[0]+sources[1]))
    ctx.prec = 1024
    _,b,d,_ = sequences(4,264,1024)
    wb = block(list(range(257)),list(range(257)),'even',b,d)
    w = mp.matrix([[mp.mpf(wb[i,j].str(140,radius=False)) for j in range(257)] for i in range(257)])
    vectors = {'raw':base['raw_pure_search']['best']['vector_decimal'],
               'projected_M90':first['projected_vector_decimal'],
               'projected_M110':second['projected_vector_decimal']}
    payload: dict[str,Any] = {'status':'DIAGNOSTIC, NOT A CERTIFICATE',
        'source_direction_distance':mp.nstr(source_distance,40), 'vectors':{}}
    for name,coefficients in vectors.items():
        v = mp.matrix(coefficients)
        norm = mp.norm(v)
        v /= norm
        payload['vectors'][name] = {'frozen_norm_error':mp.nstr(abs(norm-1),25),
            'energy_130dps':mp.nstr((v.T*w*v)[0],45),
            'overlap_source_M110':mp.nstr(abs((sources[1].T*v)[0]),30), 'grid':{}}
    for refinement in (1,2):
        masses,reference,_,_,_ = matrices(refinement)
        for name,coefficients in vectors.items():
            v = np.array([float(value) for value in coefficients])
            v /= np.linalg.norm(v)
            measured = np.array([v@m@v for m in masses])
            ratios = measured/reference
            payload['vectors'][name]['grid'][str(refinement)] = {
                'min_ratio':float(min(ratios)), 'all_ratios':ratios.tolist(),
                'all_slacks':(measured-reference).tolist()}
            assert min(ratios) > 2.7, 'Witness no longer has the claimed feasibility margin'
    print(json.dumps(payload,indent=2),flush=True)
    (OUT/'saved_witness_checks.json').write_text(json.dumps(payload,indent=2)+'\n')


if __name__=='__main__':
    main()
