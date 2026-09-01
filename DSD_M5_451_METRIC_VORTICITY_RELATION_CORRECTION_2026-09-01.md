# DSD M5-451 — Metric velocity-vorticity relation after affine pullback

Date: 2026-09-01

Status: **SCOPE CORRECTION TO M5-450 / THE PULLED-BACK VORTICITY EQUATION IS ALGEBRAICALLY CORRECT, BUT THE NEW VORTICITY VARIABLE IS NOT THE EUCLIDEAN CURL OF THE PULLED-BACK VELOCITY / THE EXACT CLOSURE LAW IS `eta = curl_y(C w)` WITH `C=F^T F=G^{-1}` / THEREFORE THE SURVIVING UNIFORMLY ELLIPTIC BRANCH IS A METRIC COUPLED NAVIER-STOKES-TYPE SYSTEM, NOT STANDARD NS WITH ONLY ANISOTROPIC DIFFUSION / GLOBAL REGULARITY REMAINS UNPROVED.**

Let the inner strained vorticity equation be

\[
\partial_\tau\Omega +(v+Az)\cdot\nabla_z\Omega
=(\nabla_zv+A)\Omega+\Delta_z\Omega,
\]

with `A=A^T`, `tr A=0`. Let

\[
F'=AF,\qquad \det F=1,
\]

and define

\[
z=F(\tau)y,\qquad v(z,\tau)=F(\tau)w(y,\tau),\qquad \Omega(z,\tau)=F(\tau)\eta(y,\tau).
\]

Then, as recorded in M5-450,

\[
\boxed{
\partial_\tau\eta+(w\cdot\nabla_y)\eta
=(\nabla_yw)\eta+\nabla_y\cdot(G\nabla_y\eta),
}
\]

where

\[
G=F^{-1}F^{-T},\qquad G=G^T>0,\qquad \det G=1.
\]

The correction is the velocity-vorticity closure. In general,

\[
\eta\neq \nabla_y\times w.
\]

Define

\[
C:=F^TF=G^{-1}.
\]

The physical velocity one-form satisfies

\[
v\cdot dz=(Fw)\cdot(Fdy)=(Cw)\cdot dy.
\]

Taking the exterior derivative, or checking directly for constant-in-space `F`, gives the exact pulled-back vorticity relation

\[
\boxed{
\eta=\nabla_y\times(Cw).
}
\]

Also

\[
\boxed{\nabla_y\cdot w=0.}
\]

Thus the closed transformed system is

\[
\boxed{
\begin{cases}
\partial_\tau\eta+(w\cdot\nabla)\eta
=(\nabla w)\eta+\nabla\cdot(G\nabla\eta),\\
\eta=\nabla\times(Cw),\\
\nabla\cdot w=0,\\
C=G^{-1},\quad \det C=\det G=1.
\end{cases}
}
\]

If the deformation condition number stays bounded, then

\[
cI\le G,C\le CI,
\]

so all Euclidean and metric quadratic norms are uniformly equivalent. However one must not import a standard Navier-Stokes Biot-Savart identity without accounting for `C`.

DSD firewall:

1. M5-450's cancellation of the affine transport/stretch terms remains valid.
2. The phrase 'anisotropic NS obtained only by replacing the Laplacian' is withdrawn.
3. Any rigidity argument must use the metric curl law `eta=curl(Cw)`.
4. Uniform ellipticity gives norm equivalence but not global regularity.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]