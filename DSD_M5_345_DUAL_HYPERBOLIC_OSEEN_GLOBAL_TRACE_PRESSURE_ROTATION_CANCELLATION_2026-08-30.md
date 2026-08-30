# DSD M5-345 — Dual-Hyperbolic Oseen Global Trace: Pressure/Rotation Cancellation

Date: 2026-08-30

Status: **EXACT GLOBAL OSEEN H1 IDENTITY / PRESSURE-HESSIAN AND ROTATION ARE ORIENTATION-REDISTRIBUTION CHANNELS, NOT GLOBAL ENERGY PAYERS / DUAL-HYPERBOLIC GLOBAL BUDGET REDUCED TO COMPRESSIVE STRAIN VS DIFFUSION / GLOBAL REGULARITY UNPROVED.**

## 1. Setup

Let the constrained Oseen field satisfy

\[
H_t+(u\cdot\nabla)H+\nabla\pi_H=\nu\Delta H,
\qquad \nabla\cdot H=0.
\]

Write

\[
G:=\nabla H,
\qquad
C_H:=G^TG\ge0,
\qquad
\nabla u=S+W,
\]

with `S^T=S`, `W^T=-W`.

Differentiating the Oseen equation gives

\[
D_tG+G\nabla u+\nabla^2\pi_H=\nu\Delta G.
\]

## 2. Exact covariance equation

Since `C_H=G^TG`,

\[
\boxed{
D_tC_H
=
\nu\Delta C_H
-2\nu\sum_m(\partial_mG)^T(\partial_mG)
-SC_H-C_HS
+[W,C_H]
-\mathcal P_H,
}
\]

where

\[
\mathcal P_H
:=(\nabla^2\pi_H)G+G^T(\nabla^2\pi_H).
\]

The commutator `[W,C_H]` is symmetric and traceless.

## 3. Trace equation

Taking the trace,

\[
D_t|G|^2
=
\nu\Delta|G|^2
-2\nu|\nabla G|^2
-2S:C_H
-2\nabla^2\pi_H:G.
\]

The rotation channel disappears pointwise from the trace.

## 4. Global pressure cancellation

Integrate on `R^3`. Because `div u=0`, the transport term vanishes. The Laplacian trace term vanishes by decay/finite-energy approximation.

For the pressure term,

\[
\int_{\mathbb R^3}\partial_{ik}\pi_H\,\partial_kH_i\,dx
=-\int_{\mathbb R^3}\partial_k\pi_H\,\partial_k(\partial_iH_i)\,dx
=0.
\]

Therefore

\[
\boxed{
\frac12\frac d{dt}\|\nabla H\|_2^2
+\nu\|\nabla^2H\|_2^2
=-\int_{\mathbb R^3}S:C_H\,dx.
}
\]

This is exactly Huang's Oseen-gradient production identity in whole-space form.

## 5. Spectral sign

Let

\[
S=S_+-S_-,
\qquad S_\pm\ge0,
\]

be the spectral positive/negative parts. Since `C_H>=0`,

\[
-S:C_H
=S_-:C_H-S_+:C_H
\le S_-:C_H.
\]

Hence positive Oseen production can only be supplied by compressive strain:

\[
\boxed{
(-S:C_H)_+
\le S_-:C_H.
}
\]

## 6. Formation/axis interpretation

The four local terms in the covariance equation have different roles:

- `-SC_H-C_HS`: true hyperbolic amplification/attenuation;
- `-2nu sum (dG)^T(dG)`: true dissipative loss;
- `[W,C_H]`: orientation redistribution only;
- `P_H`: pressure-driven orientation/spatial redistribution, but zero global H1 work.

Thus the global dual-hyperbolic budget is not a four-payer problem. It is exactly

\[
\boxed{
\text{compressive parent strain}
\quad\leftrightarrow\quad
\text{Oseen diffusion}.
}
\]

Rotation and pressure matter only for how `C_H` is placed relative to the strain eigenframe.

## 7. Consequence for the atom branch

Any endpoint-atom/full-tail construction forcing

\[
\int (\mathcal P_H)_+\,dt=\infty
\]

forces a non-summable compressive alignment action

\[
\boxed{
\int\!\int S_-:C_H\,dxdt=\infty.
}
\]

If this alignment is not maintained, the missing payment must appear as orientation redistribution (rotation/eigenframe/pressure) or local spatial flux, which belongs to the existing H/T reformation ledgers. If it is maintained, the dual-hyperbolic amplifier remains the hard branch.

## 8. Firewall

Do not count the pressure Hessian as an independent global Oseen-H1 energy payer. It cancels exactly after whole-space integration.

Do not count rigid rotation as a global Oseen-H1 payer. Its commutator has zero trace.

These channels can only prevent persistent compressive alignment by redistributing the Oseen derivative frame.

## 9. Audit verdict

### PROVED

- exact `C_H` equation;
- exact global Oseen H1 identity;
- pressure-Hessian global cancellation;
- rotation trace cancellation;
- positive production requires compressive strain.

### OPEN

- exclusion of persistent compressive alignment at arbitrary critical amplitude;
- conversion of alignment redistribution into a globally non-summable H/T contradiction;
- global regularity.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]