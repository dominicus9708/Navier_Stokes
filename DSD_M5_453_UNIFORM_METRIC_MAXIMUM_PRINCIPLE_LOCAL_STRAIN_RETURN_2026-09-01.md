# DSD M5-453 — Uniform-metric maximum principle and return to local strain

Date: 2026-09-01

Status: **A UNIFORMLY ELLIPTIC AFFINE-PULLBACK METRIC DOES NOT ABSORB THE FIRST-HITTING VORTICITY GROWTH / THE TRANSFORMED VORTICITY OBEYS AN EXACT VECTOR MAXIMUM-PRINCIPLE INEQUALITY, SO GEOMETRIC FIRST-HITTING GROWTH FORCES LINEAR-IN-GENERATION POSITIVE ACTION OF THE TRANSFORMED LOCAL STRAIN / THE BOUNDED-METRIC BRANCH THEREFORE RETURNS TO A LOCAL CRITICAL-STRAIN PROBLEM RATHER THAN FORMING A NEW QUIET TERMINAL / GLOBAL REGULARITY REMAINS UNPROVED.**

Use the corrected M5-451 system

\[
\partial_\tau\eta+(w\cdot\nabla)\eta
=(\nabla w)\eta+\nabla\cdot(G(\tau)\nabla\eta),
\]

with

\[
\nabla\cdot w=0,
\qquad
G=G^T>0,
\qquad
cI\le G\le CI.
\]

Because `G` depends only on time,

\[
\frac12(\partial_\tau+w\cdot\nabla)|\eta|^2
=
\eta^T S_w\eta
+\nabla\cdot\left(G\nabla\frac{|\eta|^2}{2}\right)
-(\nabla\eta):G(\nabla\eta),
\]

where

\[
S_w:=\frac12(\nabla w+\nabla w^T).
\]

At a spatial maximum of `|eta|^2`, the anisotropic diffusion contribution is nonpositive. Therefore

\[
\boxed{
D^+\log\|\eta(\tau)\|_\infty
\le
\sup_x\lambda_{\max}(S_w(x,\tau)).
}
\]

Now assume the affine deformation remains uniformly bounded:

\[
\|F(\tau)\|+\|F(\tau)^{-1}\|\le K_F.
\]

Since

\[
\Omega=F\eta,
\]

we have

\[
K_F^{-1}\|\Omega\|_\infty
\le
\|\eta\|_\infty
\le
K_F\|\Omega\|_\infty.
\]

Across `L` first-hitting generations,

\[
\|\Omega(t_{j+L})\|_\infty=q^L\|\Omega(t_j)\|_\infty.
\]

Hence

\[
\frac{\|\eta(t_{j+L})\|_\infty}{\|\eta(t_j)\|_\infty}
\ge K_F^{-2}q^L.
\]

Integrating the maximum-principle inequality gives

\[
\boxed{
\int_{t_j}^{t_{j+L}}
\sup_x\lambda_{\max}(S_w(x,t))dt
\ge
L\log q-2\log K_F.
}
\]

Thus for arbitrarily long late blocks the transformed local strain pays a positive order-one action per first-hitting generation.

Consequences:

1. bounded affine deformation cannot itself hide the repeated vorticity amplification;
2. removing the outer affine field merely transfers the payer to `S_w`;
3. by M5-452, `S_w` is again controlled by a uniform metric Biot-Savart/CZ law from `eta`;
4. the uniformly elliptic branch is therefore a local critical-strain recurrence problem, not a separate regularity theorem.

Firewall: this does not exclude the local critical-strain recurrence. Standard 3D Navier-Stokes itself has the same critical obstruction when the metric is constant. The result is a routing theorem, not global closure.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]