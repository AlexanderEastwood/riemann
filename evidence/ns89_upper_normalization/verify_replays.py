"""Verify source binding, exact witnesses, and complete upper-bound replays."""
from __future__ import annotations

from fractions import Fraction
import hashlib
import json
from pathlib import Path
from typing import Any

from flint import arb, ctx

HERE=Path(__file__).resolve().parent


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def read(name: str) -> dict[str,Any]:
    return json.loads((HERE/name).read_text())


def main() -> None:
    ctx.prec=384
    a,b,k=[read(name) for name in ["check-256bits.json","check-384bits.json","check-cutoff-384bits.json"]]
    for data in [a,b,k]:
        assert data["source_sha256"]==digest(HERE/"certify.py")
        assert data["kernel_sha256"]==digest(HERE.parent/"v159/ns61/certify_smoothed.py")
    counts={"Gram_precision_values":0,"Gram_cutoff_values":0,"physical_precision_values":0,
            "physical_Gram_energy_overlaps":0,"physical_cutoff_energy_overlaps":0}
    for left,right in zip(a["rows"],b["rows"]):
        assert left["N"]==right["N"]
        assert left["rational_coefficients"]==right["rational_coefficients"]
        for key,x in left["values"].items():
            assert arb(x).overlaps(arb(right["values"][key])),key
            counts["Gram_precision_values"]+=1
    last=b["rows"][-1];cut=k["rows"][0]
    assert last["N"]==cut["N"]==256
    assert last["rational_coefficients"]==cut["rational_coefficients"]
    for key,x in last["values"].items():
        assert arb(x).overlaps(arb(cut["values"][key])),key
        counts["Gram_cutoff_values"]+=1
    for row in b["rows"]:
        coefficients=[Fraction(s) for s in row["rational_coefficients"]]
        assert sum((c/n for n,c in enumerate(coefficients,1)),Fraction(0))==0
        assert all(row["gates"].values())
    assert arb(last["values"]["rate_transfer_factor"])<arb("1.144579")
    assert arb(last["values"]["uniform_rate_transfer_factor"])<arb("3.270466")
    assert arb(last["values"]["explicit_trial_error"])<arb("0.000014144")
    assert arb(last["values"]["relative_normalization_cost"])<arb("0.000088342")
    pa,pb,pk=[read(name) for name in ["physical-256bits.json","physical-384bits.json","physical-cutoff-384bits.json"]]
    for data,input_name,gram in [(pa,"check-256bits.json",a),(pb,"check-384bits.json",b),(pk,"check-cutoff-384bits.json",k)]:
        assert data["source_sha256"]==digest(HERE/"physical.py")
        assert data["input_sha256"]==digest(HERE/input_name)
        for row,g in zip(data["rows"],gram["rows"]):
            assert row["N"]==g["N"]
            assert arb(row["values"]["complete_energy_enclosure"]).overlaps(arb(g["values"]["explicit_trial_error"]))
            assert arb(g["values"]["explicit_trial_error"])<arb(row["values"]["complete_upper_certificate"])
            counts["physical_Gram_energy_overlaps"]+=1
    for left,right in zip(pa["rows"],pb["rows"]):
        for key,x in left["values"].items():
            assert arb(x).overlaps(arb(right["values"][key]))
            counts["physical_precision_values"]+=1
    assert arb(pb["rows"][-1]["values"]["complete_energy_enclosure"]).overlaps(arb(pk["rows"][0]["values"]["complete_energy_enclosure"]))
    counts["physical_cutoff_energy_overlaps"]+=1
    assert arb(pk["rows"][0]["values"]["tail_radius"])<arb(pb["rows"][-1]["values"]["tail_radius"])
    assert arb(pb["rows"][-1]["values"]["complete_upper_certificate"])<arb("0.000014144")
    maxima=(HERE/"exact-checks-output.txt").read_text()
    assert "PASS: 12 exact checks" in maxima and "#0:" not in maxima
    result={"status":"PASS","checks":counts,
            "identical_exact_rational_witnesses_across_all_replays":True,
            "N256_full_upper_below":"0.000014144",
            "all_N_at_least_256_normalized_over_original_at_most":"1.144579",
            "Maxima_exact_checks":12,"cofinal_upper_decay_proved":False,
            "source_sha256":digest(Path(__file__))}
    (HERE/"replay-validation.json").write_text(json.dumps(result,indent=2)+"\n")
    print(json.dumps(result,indent=2))


if __name__=="__main__":
    main()
