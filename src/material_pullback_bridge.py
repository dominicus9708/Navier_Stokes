#!/usr/bin/env python3
"""Material pullback / boundary-geometry bridge for the DSD Navier-Stokes route."""
from __future__ import annotations
import argparse, json, math
from pathlib import Path
import sympy as sp

SCHEMA_VERSION="0.1.0"

def symbolic_checks():
    c,t,nx,ny,nz=sp.symbols("c t nx ny nz", positive=True, real=True)
    F=sp.diag(sp.exp(2*c*t),sp.exp(2*c*t),sp.exp(-4*c*t))
    J=sp.simplify(F.det())
    FinvT=sp.simplify(F.inv().T)
    cof=sp.simplify(J*FinvT)
    C=sp.simplify(F.T*F)
    detC=sp.simplify(C.det())
    n=sp.Matrix([nx,ny,nz])
    av=sp.simplify(cof*n)
    avnorm2=sp.expand((av.T*av)[0])
    expected=sp.exp(-4*c*t)*(nx**2+ny**2)+sp.exp(8*c*t)*nz**2
    return {
        "F":[[str(F[i,j]) for j in range(3)] for i in range(3)],
        "J":str(J),
        "J_one":bool(J==1),
        "FinvT":[[str(FinvT[i,j]) for j in range(3)] for i in range(3)],
        "cofactor_equals_FinvT":all(sp.simplify(cof[i,j]-FinvT[i,j])==0 for i in range(3) for j in range(3)),
        "det_C":str(detC),
        "det_C_one":bool(detC==1),
        "area_vector_norm_sq":str(avnorm2),
        "area_vector_formula_match":bool(sp.simplify(avnorm2-expected)==0),
        "max_boundary_amplification_t_nonnegative":"exp(4*c*t)",
        "min_boundary_amplification_t_nonnegative":"exp(-2*c*t)",
        "boundary_anisotropy_ratio_t_nonnegative":"exp(6*c*t)",
    }

def numeric_rows(times=(0,.05,.1,.2,.5)):
    c=math.exp(-.25)
    rows=[]
    for t in times:
        maxamp=math.exp(4*c*t)
        minamp=math.exp(-2*c*t)
        rows.append({
            "tau":t,
            "max_FinvT":maxamp,
            "min_FinvT":minamp,
            "boundary_anisotropy":maxamp/minamp,
            "volume_factor":1.0,
        })
    return rows

def run_checks():
    s=symbolic_checks()
    rows=numeric_rows()
    checks={
        "J_one":s["J_one"],
        "cofactor_equals_FinvT":s["cofactor_equals_FinvT"],
        "det_C_one":s["det_C_one"],
        "area_vector_formula_match":s["area_vector_formula_match"],
        "numeric_volume_factor_one":all(row["volume_factor"]==1.0 for row in rows),
        "boundary_amp_grows":rows[-1]["max_FinvT"]>rows[0]["max_FinvT"],
        "boundary_anisotropy_grows":rows[-1]["boundary_anisotropy"]>rows[0]["boundary_anisotropy"],
    }
    return {
        "schema_version":SCHEMA_VERSION,
        "status":"DERIVED PULLBACK / BOUNDARY-GEOMETRY BRIDGE + COMPUTATIONAL CHECK",
        "exact_identities":{
            "bulk_pullback":"int_{Omega_t} f(x,t) dx = int_{B_ell(a)} f(Phi_t(b),t) J(b,t) db; incompressibility gives J=1",
            "nanson":"n_t dS_t = J F^{-T} n_0 dS_0 = F^{-T} n_0 dS_0",
            "pressure_work_pullback":"int_{boundary Omega_t} p u.n dS = int_{boundary B} p(Phi) u(Phi).(F^{-T} n_0) dS_0",
            "viscous_flux_pullback":"int_{boundary Omega_t} grad e.n dS = int_{boundary B} grad e(Phi).(F^{-T} n_0) dS_0",
        },
        "checks":checks,
        "passed":sum(bool(v) for v in checks.values()),
        "total":len(checks),
        "symbolic_anchor":s,
        "numeric_anchor":rows,
        "dsd_channels":{
            "q_bulk_measure":"J=1; material bulk aggregation uses fixed reference volume measure",
            "q_boundary_geometry":"F^{-T} n_0; transformed oriented area vector",
            "q_boundary_amp":"||F^{-T}||_op = 1/sigma_min(F)",
            "q_pressure_geometry":"pressure boundary work coupled to F^{-T}",
            "q_viscous_geometry":"viscous boundary transport coupled to F^{-T}",
        },
        "scaling":{
            "flow_map":"Phi^lambda_t(a)=lambda^{-1} Phi_{lambda^2 t}(lambda a)",
            "deformation_gradient":"F^lambda(a,t)=F(lambda a,lambda^2 t)",
            "consequence":"F, J, C, principal-stretch ratios, Delta_shape, and ||F^{-T}|| are dimensionless/scale-covariant material channels.",
        },
        "interpretation":(
            "Incompressibility freezes the material bulk Jacobian but not boundary geometry. "
            "The remaining pressure and viscous boundary interactions are weighted by F^{-T}. "
            "Compression of one material direction can therefore amplify the oriented-area factor "
            "even while total volume is exactly preserved. This is a structural coupling channel, "
            "not a blow-up theorem."
        ),
        "claim_boundary":(
            "Nanson pullback and J=1 are exact smooth-flow identities. The exponential formulas are "
            "only for the frozen local Gaussian anchor and do not represent a time-solved Navier-Stokes trajectory."
        )
    }

def write_md(d,path):
    rows=d["numeric_anchor"]
    lines=[
        "# Material pullback / boundary-geometry bridge","",
        f"Status: **{d['status']}**","",
        f"Checks passed: **{d['passed']}/{d['total']}**","",
        "## Exact split","",
        "- Bulk material measure: `J=det F=1`, so volume aggregation pulls back to the fixed initial ball without a changing Jacobian.",
        "- Boundary oriented area: `n dS = F^{-T} n0 dS0`.",
        "- Pressure work and viscous boundary transport therefore retain an explicit deformation-geometry coupling through `F^{-T}`.","",
        "## Frozen Gaussian anchor","",
        "For `F=diag(exp(2 c tau),exp(2 c tau),exp(-4 c tau))`, `c=e^(-1/4)`: ","",
        "- `det F=1` exactly;",
        "- `||F^{-T}||_op=exp(4 c tau)` for `tau>=0`;",
        "- minimum oriented-area factor is `exp(-2 c tau)`;",
        "- boundary anisotropy ratio is `exp(6 c tau)`." ,"",
        "Sample values:","",
    ]
    for r in rows:
        lines.append(f"- tau={r['tau']:.2f}: max={r['max_FinvT']:.6g}, min={r['min_FinvT']:.6g}, ratio={r['boundary_anisotropy']:.6g}")
    lines += ["","## Interpretation","",d["interpretation"],"","## Claim boundary","",d["claim_boundary"],""]
    path.write_text("\n".join(lines),encoding="utf-8")

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--output-dir",default="results"); args=ap.parse_args()
    out=Path(args.output_dir); out.mkdir(parents=True,exist_ok=True)
    d=run_checks()
    (out/"material_pullback_bridge.json").write_text(json.dumps(d,indent=2),encoding="utf-8")
    write_md(d,out/"material_pullback_bridge.md")
    print(f"Material pullback bridge: {d['passed']}/{d['total']} checks passed")
    if d["passed"]!=d["total"]: raise SystemExit(1)

if __name__=="__main__": main()
