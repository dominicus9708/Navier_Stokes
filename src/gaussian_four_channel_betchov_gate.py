#!/usr/bin/env python3
"""Audit exact Gaussian residual decompositions and Betchov orbit identity.

This checks finite-dimensional/weighted algebra only. It does not prove global
regularity or the analytical Gaussian Duhamel estimate.
"""
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

import numpy as np

SCHEMA_VERSION = "0.1.0"


def weighted_mean(w, x):
    return np.tensordot(w, x, axes=(0, 0))


def vorticity_split(seed=9708, n=80):
    rng = np.random.default_rng(seed)
    w = rng.random(n); w /= w.sum()
    om = rng.normal(size=(n, 3))
    m = weighted_mean(w, om)
    E = float(np.sum(w * np.sum(om * om, axis=1)))
    M2 = np.einsum('n,ni,nj->ij', w, om, om)
    C = M2 / E
    lam = float(np.linalg.eigvalsh(C)[-1])
    var = E - float(np.dot(m, m))
    dproj = E * (1.0 - lam)
    dline = E * lam - float(np.dot(m, m))
    return {
        'variance': var,
        'projective_plus_line': dproj + dline,
        'projective': dproj,
        'line': dline,
        'abs_error': abs(var - dproj - dline),
    }


def strain_basis():
    # Orthonormal basis for trace-free symmetric 3x3 matrices.
    E = []
    E.append(np.diag([1., -1., 0.]) / math.sqrt(2.0))
    E.append(np.diag([1., 1., -2.]) / math.sqrt(6.0))
    A = np.zeros((3,3)); A[0,1]=A[1,0]=1/math.sqrt(2.0); E.append(A)
    A = np.zeros((3,3)); A[0,2]=A[2,0]=1/math.sqrt(2.0); E.append(A)
    A = np.zeros((3,3)); A[1,2]=A[2,1]=1/math.sqrt(2.0); E.append(A)
    return np.stack(E)


def strain_split(seed=2026, n=90):
    rng = np.random.default_rng(seed)
    w = rng.random(n); w /= w.sum()
    coeff = rng.normal(size=(n, 5))
    m = weighted_mean(w, coeff)
    E = float(np.sum(w * np.sum(coeff * coeff, axis=1)))
    M2 = np.einsum('n,ni,nj->ij', w, coeff, coeff)
    evals, evecs = np.linalg.eigh(M2 / E)
    mu = float(evals[-1])
    A = evecs[:, -1]
    a = coeff @ A
    R = coeff - a[:, None] * A[None, :]
    dshape_direct = float(np.sum(w * np.sum(R * R, axis=1)))
    dshape = E * (1.0 - mu)
    damp = E * mu - float(np.dot(m, m))
    var = E - float(np.dot(m, m))
    abar = float(np.sum(w * a))
    Rbar = weighted_mean(w, R)
    vara = float(np.sum(w * (a - abar) ** 2))
    amp_relation = damp + float(np.dot(Rbar, Rbar))
    return {
        'variance': var,
        'shape_plus_amp': dshape + damp,
        'shape_covariance': dshape,
        'shape_direct': dshape_direct,
        'amp': damp,
        'scalar_amp_variance': vara,
        'amp_plus_mean_residual_sq': amp_relation,
        'variance_abs_error': abs(var - dshape - damp),
        'shape_abs_error': abs(dshape - dshape_direct),
        'amp_variance_abs_error': abs(vara - amp_relation),
    }


def betchov_identity(seed=13, n=50000):
    rng = np.random.default_rng(seed)
    maxerr = 0.0
    mineff = 2.0
    maxeff = -1.0
    examples = []
    x_min = 1 / math.sqrt(2.0)
    x_max = math.sqrt(2.0 / 3.0)
    for k in range(n):
        x = rng.uniform(x_min, x_max)
        # y+z=x and yz=x^2-1/2.
        disc = max(0.0, 2.0 - 3.0*x*x)
        y = 0.5 * (x - math.sqrt(disc))
        z = 0.5 * (x + math.sqrt(disc))
        lam = np.array([-x, y, z])
        lb = np.array([-math.sqrt(2/3), 1/math.sqrt(6), 1/math.sqrt(6)])
        d2 = float(np.sum((lam - lb) ** 2))
        eta = 3*math.sqrt(6) * x * (x*x - 0.5)
        rhs = 0.5*d2*(3.0-d2)**2
        err = abs((1.0-eta) - rhs)
        maxerr = max(maxerr, err)
        mineff = min(mineff, eta); maxeff = max(maxeff, eta)
        if k < 3:
            examples.append({'x': x, 'd2': d2, 'eta': eta, 'deficit_formula': rhs})
    return {
        'max_abs_error': maxerr,
        'min_efficiency': mineff,
        'max_efficiency': maxeff,
        'examples': examples,
    }


def cubic_transfer_proxy(seed=77, n=100):
    # Verify exact moment identities behind the transfer, not the universal inequality constant.
    rng = np.random.default_rng(seed)
    w = rng.random(n); w /= w.sum()
    coeff = rng.normal(size=(n, 5))
    m = weighted_mean(w, coeff)
    E = float(np.sum(w*np.sum(coeff*coeff, axis=1)))
    M2 = np.einsum('n,ni,nj->ij', w, coeff, coeff)
    evals, evecs = np.linalg.eigh(M2/E)
    mu = float(evals[-1]); A=evecs[:,-1]
    a=coeff@A; R=coeff-a[:,None]*A[None,:]
    abar=float(np.sum(w*a)); Rbar=weighted_mean(w,R)
    dshape=E*(1-mu); damp=E*mu-float(np.dot(m,m))
    vara=float(np.sum(w*(a-abar)**2))
    return {
        'var_a': vara,
        'damp_plus_Rbar2': damp+float(np.dot(Rbar,Rbar)),
        'dshape': dshape,
        'damp': damp,
        'var_a_le_shape_plus_amp': vara <= dshape+damp+1e-12,
        'identity_error': abs(vara-damp-float(np.dot(Rbar,Rbar))),
    }


def run_checks():
    vo=vorticity_split(); st=strain_split(); be=betchov_identity(); cu=cubic_transfer_proxy()
    checks={
        'vorticity_variance_exact_split': vo['abs_error'] < 1e-12,
        'vorticity_defects_nonnegative': vo['projective'] >= -1e-12 and vo['line'] >= -1e-12,
        'strain_variance_exact_split': st['variance_abs_error'] < 1e-12,
        'strain_shape_direct_equals_covariance': st['shape_abs_error'] < 1e-12,
        'strain_amp_variance_identity': st['amp_variance_abs_error'] < 1e-12,
        'strain_defects_nonnegative': st['shape_covariance'] >= -1e-12 and st['amp'] >= -1e-12,
        'betchov_distance_efficiency_exact': be['max_abs_error'] < 1e-11,
        'betchov_efficiency_in_unit_interval': be['min_efficiency'] >= -1e-12 and be['max_efficiency'] <= 1+1e-12,
        'cubic_transfer_amp_variance_relation': cu['identity_error'] < 1e-12,
        'scalar_amp_variance_bounded_by_two_strain_defects': bool(cu['var_a_le_shape_plus_amp']),
    }
    checks={k:bool(v) for k,v in checks.items()}
    return {
        'schema_version': SCHEMA_VERSION,
        'status': 'GAUSSIAN FOUR-CHANNEL RESIDUAL + BETCHOV ORBIT ALGEBRA AUDIT',
        'checks': checks,
        'passed': sum(checks.values()), 'total': len(checks),
        'vorticity': vo, 'strain': st, 'betchov': be, 'cubic_proxy': cu,
        'central_residual_identity': 'B_gamma = D_S_shape + D_S_amp + 1/2 D_w_proj + 1/2 D_w_line',
        'betchov_identity': '1-eta_det = (d_B^2/2)*(3-d_B^2)^2',
        'claim_boundary': 'Finite-dimensional and weighted second-moment algebra only; analytical Duhamel/compactness statements are documented separately.'
    }


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--output-dir',default='results'); args=ap.parse_args()
    out=Path(args.output_dir); out.mkdir(parents=True,exist_ok=True)
    d=run_checks()
    (out/'gaussian_four_channel_betchov_gate.json').write_text(json.dumps(d,indent=2),encoding='utf-8')
    (out/'gaussian_four_channel_betchov_gate.md').write_text(
        '# Gaussian four-channel/Betchov audit\n\n'
        f"Checks passed: **{d['passed']}/{d['total']}**\n\n"
        f"Residual identity: `{d['central_residual_identity']}`\n\n"
        f"Betchov identity: `{d['betchov_identity']}`\n\n"
        '## Claim boundary\n\n'+d['claim_boundary']+'\n',encoding='utf-8')
    print(f"Gaussian four-channel/Betchov: {d['passed']}/{d['total']} checks passed")
    if d['passed'] != d['total']: raise SystemExit(1)

if __name__=='__main__': main()
