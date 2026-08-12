#!/usr/bin/env python3
"""Algebraic audit of factorial derivative-channel aggregation."""
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path
import numpy as np

SCHEMA_VERSION = "0.1.0"


def factorial_identity(max_k=30):
    err = 0.0
    for k in range(max_k+1):
        for m in range(k+1):
            lhs = math.comb(k,m)/math.factorial(k)
            rhs = 1.0/(math.factorial(m)*math.factorial(k-m))
            err = max(err, abs(lhs-rhs))
    return err


def convolution_audit(seed=9708, n=20):
    rng = np.random.default_rng(seed)
    A = rng.random(n+1)
    B = rng.random(n+1)
    coeff = np.array([sum(A[m]*B[k-m] for m in range(k+1)) for k in range(n+1)])

    # Compare finite polynomial multiplication.
    product = np.convolve(A,B)[:n+1]
    return float(np.max(np.abs(coeff-product)))


def remote_kernel_shape(k, n0=3):
    q = 2.0**(-(k+4))
    exact = q**n0/(1.0-q)
    partial = sum(2.0**(-(k+4)*n) for n in range(n0,80))
    return exact, partial


def scaling_factor(lam, k):
    # For L-infinity-type derivative coefficients:
    # D^k u -> lambda^(k+1), ell^k -> lambda^-k, so A_k -> lambda A_k.
    # B_k has ell^(k+1) * grad D^k u and also -> lambda B_k.
    A_factor = lam**(-k)*lam**(k+1)
    B_factor = lam**(-(k+1))*lam**(k+2)
    return A_factor, B_factor


def run_checks():
    fact_err = factorial_identity()
    conv_err = convolution_audit()
    kernel = {k: remote_kernel_shape(k) for k in (0,1,2,5,10)}
    shape = [kernel[k][0] for k in sorted(kernel)]
    checks = {
        "factorial_binomial_identity": fact_err < 1e-15,
        "cauchy_product_coefficients": conv_err < 1e-12,
        "remote_kernel_geometric_sum": all(abs(a-b)<1e-15 for a,b in kernel.values()),
        "remote_kernel_decreases_with_derivative_order": all(shape[i+1] < shape[i] for i in range(len(shape)-1)),
        "derivative_coefficients_scale_like_velocity": all(
            abs(scaling_factor(lam,k)[0]-lam)<1e-12 and abs(scaling_factor(lam,k)[1]-lam)<1e-12
            for lam in (0.4,2.0,7.0) for k in (0,1,4,9)
        ),
    }
    checks={k:bool(v) for k,v in checks.items()}
    return {
        "schema_version":SCHEMA_VERSION,
        "status":"DERIVED ALGEBRA / GENERATING-FUNCTION AUDIT",
        "checks":checks,
        "passed":sum(checks.values()),"total":len(checks),
        "factorial_identity_max_error":fact_err,
        "convolution_max_error":conv_err,
        "remote_kernel_l1_shape":{str(k):v[0] for k,v in kernel.items()},
        "identity":"N_k <= sum_{m=0}^k A_m B_{k-m}; generating coefficients are the Cauchy product after factorial normalization.",
        "claim_boundary":"This is derivative bookkeeping, not an a-priori analyticity or global regularity estimate."
    }


def write_md(d,path):
    lines=["# Derivative channel generating-function audit","",f"Status: **{d['status']}**","",f"Checks passed: **{d['passed']}/{d['total']}**","",d["identity"],"","Remote pressure kernel l1 shape factors decrease rapidly with derivative order, while the local differentiated transport remains a Cauchy convolution.","","## Claim boundary","",d["claim_boundary"],""]
    path.write_text("\n".join(lines),encoding="utf-8")


def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--output-dir",default="results")
    args=ap.parse_args(); out=Path(args.output_dir); out.mkdir(parents=True,exist_ok=True)
    d=run_checks(); (out/"derivative_channel_generating_gate.json").write_text(json.dumps(d,indent=2),encoding="utf-8"); write_md(d,out/"derivative_channel_generating_gate.md")
    print(f"Derivative generating-function gate: {d['passed']}/{d['total']} checks passed")
    if d["passed"]!=d["total"]: raise SystemExit(1)

if __name__=="__main__": main()
