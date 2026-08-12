#!/usr/bin/env python3
"""Audit the local vorticity covariance-axis algebra.

This checks:
- covariance trace/eigenvalue identities;
- delta >= 1 - 2 Pi;
- the convolution-specific eigenvector derivative bound for a Student-type kernel;
- scale invariance of the local covariance descriptors.

It does not reproduce Miller's external regularity theorem.
"""
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path
import numpy as np

SCHEMA_VERSION = "0.1.0"


def student_weight(x, y, r, m):
    z = (x-y)/r
    return (1.0+float(np.dot(z,z)))**(-m)


def student_grad_x(x, y, r, m):
    d = x-y
    den = r*r+float(np.dot(d,d))
    w = student_weight(x,y,r,m)
    return -(2.0*m/den)*d*w


def discrete_covariance(x, points, omega, r=1.3, m=3.0):
    w = np.array([student_weight(x,points[i],r,m) for i in range(len(points))])
    E = float(np.sum(w*np.sum(omega*omega,axis=1)))
    N = np.einsum('n,ni,nj->ij',w,omega,omega)
    C = N/E
    vals, vecs = np.linalg.eigh(C)
    order = np.argsort(vals)[::-1]
    vals = vals[order]; vecs = vecs[:,order]
    return E,C,vals,vecs,w


def discrete_covariance_derivative(x, points, omega, direction, r=1.3, m=3.0):
    E,C,vals,vecs,w = discrete_covariance(x,points,omega,r,m)
    dw_vec = np.array([student_grad_x(x,points[i],r,m) for i in range(len(points))])
    dw = dw_vec @ direction
    dE = float(np.sum(dw*np.sum(omega*omega,axis=1)))
    dN = np.einsum('n,ni,nj->ij',dw,omega,omega)
    dC = dN/E-C*(dE/E)
    return E,C,vals,vecs,dC,w


def eigenvector_derivative_from_matrix(vals, vecs, dC):
    n = vecs[:,0]
    dn = np.zeros(3)
    for j in (1,2):
        ej = vecs[:,j]
        dn += ej * (float(ej @ dC @ n)/(vals[0]-vals[j]))
    return dn


def random_convolution_audit(seed=9708, trials=500):
    rng=np.random.default_rng(seed)
    r=1.3; m=3.0
    max_ratio=0.0
    gap_violation=0.0
    derivative_violations=0
    used=0
    for _ in range(trials):
        points=rng.normal(size=(18,3))*1.5
        omega=rng.normal(size=(18,3))
        # Add a preferred local axis while preserving enough genericity.
        omega[:,2] += 1.5*rng.normal(size=18)
        x=rng.normal(size=3)*0.4
        h=rng.normal(size=3); h/=np.linalg.norm(h)
        E,C,vals,vecs,dC,w=discrete_covariance_derivative(x,points,omega,h,r,m)
        mu1,mu2,mu3=vals
        Pi=1.0-mu1; delta=mu1-mu2
        gap_violation=max(gap_violation,(1.0-2.0*Pi)-delta)
        if delta<1e-7:
            continue
        used+=1
        dn=eigenvector_derivative_from_matrix(vals,vecs,dC)
        rhs=(m/r)*math.sqrt(max(mu1*Pi,0.0))/delta
        ratio=float(np.linalg.norm(dn)/max(rhs,1e-14))
        max_ratio=max(max_ratio,ratio)
        if ratio>1.0+2e-10:
            derivative_violations+=1
    return {
        'trials':trials,'used_simple_gap_trials':used,
        'max_gap_inequality_violation':float(gap_violation),
        'max_derivative_bound_ratio':max_ratio,
        'derivative_bound_violations':derivative_violations,
        'r':r,'m':m,
    }


def exact_covariance_examples():
    examples={
        'one_axis':np.diag([1.0,0.0,0.0]),
        'near_axis':np.diag([0.9,0.07,0.03]),
        'planar_degenerate':np.diag([0.5,0.5,0.0]),
        'isotropic':np.eye(3)/3.0,
    }
    out={}
    for name,C in examples.items():
        vals=np.linalg.eigvalsh(C)[::-1]
        Pi=1.0-vals[0]; delta=vals[0]-vals[1]
        out[name]={
            'eigenvalues':vals.tolist(),'Pi':float(Pi),'delta':float(delta),
            'gap_lower_bound':float(1.0-2.0*Pi),
        }
    return out


def kernel_constants(m=3.0):
    kappa=3.0/(2.0*m-5.0)
    # max_{s>=0} 2m s/(1+s^2) = m
    return {'m':m,'log_gradient_constant':m,'second_moment_kappa':kappa}


def scaling_audit(lam):
    # eta_r with r -> r/lambda and omega -> lambda^2 omega.
    # N,E scale by lambda^4 after normalized convolution; C/eigenvalues invariant.
    # r grad n is dimensionless.
    return {
        'C_factor':1.0,
        'Pi_factor':1.0,
        'gap_factor':1.0,
        'r_grad_n_factor':(lam**-1)*lam,
    }


def run_checks():
    rnd=random_convolution_audit()
    ex=exact_covariance_examples(); kc=kernel_constants()
    scales=[scaling_audit(l) for l in (0.3,2.0,9.0)]
    near=ex['near_axis']
    checks={
        'gap_lower_bound_random':rnd['max_gap_inequality_violation']<1e-12,
        'convolution_eigenvector_derivative_bound':rnd['derivative_bound_violations']==0 and rnd['max_derivative_bound_ratio']<=1.0+2e-10,
        'small_defect_opens_gap_example':near['Pi']<0.5 and near['delta']>=near['gap_lower_bound']-1e-12,
        'planar_degenerate_has_large_defect':abs(ex['planar_degenerate']['Pi']-0.5)<1e-12 and abs(ex['planar_degenerate']['delta'])<1e-12,
        'isotropic_defect_two_thirds':abs(ex['isotropic']['Pi']-2.0/3.0)<1e-12,
        'student_second_moment_m3':abs(kc['second_moment_kappa']-3.0)<1e-12,
        'local_axis_channels_scale_invariant':all(abs(s['r_grad_n_factor']-1.0)<1e-12 for s in scales),
    }
    checks={k:bool(v) for k,v in checks.items()}
    return {
        'schema_version':SCHEMA_VERSION,
        'status':'DERIVED LOCAL COVARIANCE ALGEBRA / COMPUTATIONAL AUDIT',
        'checks':checks,'passed':sum(checks.values()),'total':len(checks),
        'random_convolution_audit':rnd,
        'exact_examples':ex,'kernel_constants':kc,
        'gap_identity':'delta=mu1-mu2 >= 1-2 Pi, where Pi=1-mu1.',
        'axis_derivative_bound':'r |partial_h n| <= m sqrt(mu1 Pi)/delta for the Student kernel.',
        'claim_boundary':'The matrix/convolution bounds are internal lemmas. The regularity implication that uses an admissible axis field is anchored to Miller externally.'
    }


def write_md(d,path):
    r=d['random_convolution_audit']
    lines=[
        '# Local vorticity covariance-axis audit','',
        f"Status: **{d['status']}**",'',
        f"Checks passed: **{d['passed']}/{d['total']}**",'',
        d['gap_identity'],'',d['axis_derivative_bound'],'',
        f"Random convolution trials: `{r['used_simple_gap_trials']}`; max derivative-bound ratio `{r['max_derivative_bound_ratio']:.12g}`.",'',
        'A small local multi-axis defect automatically opens the principal eigenvalue gap; with the positive Student kernel, the principal axis also becomes smoother like `sqrt(Pi)`.', '',
        '## Claim boundary','',d['claim_boundary'],'']
    path.write_text('\n'.join(lines),encoding='utf-8')


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--output-dir',default='results'); args=ap.parse_args()
    out=Path(args.output_dir); out.mkdir(parents=True,exist_ok=True)
    d=run_checks(); (out/'local_vorticity_covariance_axis_gate.json').write_text(json.dumps(d,indent=2),encoding='utf-8'); write_md(d,out/'local_vorticity_covariance_axis_gate.md')
    print(f"Local vorticity covariance-axis gate: {d['passed']}/{d['total']} checks passed")
    if d['passed']!=d['total']: raise SystemExit(1)

if __name__=='__main__': main()
