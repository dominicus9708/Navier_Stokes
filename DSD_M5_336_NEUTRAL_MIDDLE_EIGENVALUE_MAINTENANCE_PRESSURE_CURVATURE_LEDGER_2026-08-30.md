# DSD M5-336 — Neutral Middle-Eigenvalue Maintenance / Pressure–Curvature Ledger

Date: 2026-08-30

Status: **EXACT MATERIAL EQUATION FOR THE NEUTRAL STRAIN EIGENVALUE DERIVED / PLANAR NEUTRAL-AXIS LOCKING REQUIRES VISCOUS CURVATURE, PRESSURE-HESSIAN, PROJECTIVE MISALIGNMENT, OR A QUIESCENT AFFINE-LIKE BALANCE / GLOBAL REGULARITY UNPROVED.**

## 1. Strain evolution

Let

\[
A=\nabla u=S+W,
\qquad
S^T=S,
\qquad
W^T=-W.
\]

For incompressible Navier–Stokes,

\[
\boxed{
D_tS+S^2+W^2+\nabla^2p=\nu\Delta S,
}
\]

where `D_t=partial_t+u dot grad`.

Let `e_2` be a simple normalized eigenvector of `S` with eigenvalue `lambda_2`. Since `S` is symmetric,

\[
\boxed{
D_t\lambda_2=e_2^T(D_tS)e_2.
}
\]

Therefore

\[
D_t\lambda_2
=\nu e_2^T\Delta S e_2
-\lambda_2^2
-e_2^TW^2e_2
-e_2^T(\nabla^2p)e_2.
\]

## 2. Vorticity contribution

In three dimensions,

\[
W^2
=\frac14\bigl(\omega\otimes\omega-|\omega|^2I\bigr).
\]

Hence

\[
e_2^TW^2e_2
=-\frac14|\omega|^2\bigl[1-(\xi\cdot e_2)^2\bigr]
=-\frac14|\omega|^2\sin^2\theta_2.
\]

Thus the exact middle-eigenvalue equation is

\[
\boxed{
D_t\lambda_2
=\nu e_2^T\Delta S e_2
-e_2^T(\nabla^2p)e_2
-\lambda_2^2
+\frac14|\omega|^2\sin^2\theta_2.
}
\]

## 3. Insert the locked planar geometry

On the hard branch from M5-335,

\[
|\lambda_2|\le\delta|S|,
\qquad
\sin\theta_2\le\varepsilon.
\]

Therefore

\[
\lambda_2^2\le\delta^2|S|^2,
\qquad
\frac14|\omega|^2\sin^2\theta_2
\le\frac{\varepsilon^2}{4}|\omega|^2.
\]

The leading maintenance relation is consequently

\[
\boxed{
D_t\lambda_2
=\nu e_2^T\Delta S e_2
-e_2^T(\nabla^2p)e_2
+O(\delta^2|S|^2+\varepsilon^2|\omega|^2).
}
\]

## 4. Maintenance residual

Define

\[
\mathcal M_2
:=
\nu e_2^T\Delta S e_2
-e_2^T(\nabla^2p)e_2.
\]

Then

\[
D_t\lambda_2
=\mathcal M_2
+O(\delta^2|S|^2+\varepsilon^2|\omega|^2).
\]

A long-lived neutral-axis planar state must therefore choose one of the following:

1. **viscous-curvature payer**
   \[
   \nu|e_2^T\Delta S e_2|\text{ is large};
   \]
2. **pressure-Hessian payer**
   \[
   |e_2^T\nabla^2p\,e_2|\text{ is large};
   \]
3. **pressure–curvature cancellation**
   \[
   \nu e_2^T\Delta S e_2\approx e_2^T\nabla^2p\,e_2;
   \]
4. **quiescent planar balance**
   both terms are small and `D_t lambda_2` remains small.

The first case is an `H2/derivative` channel.
The second is a pressure-curvature `H/T` channel.
The third requires a persistent nontrivial covariance between a local second derivative and the nonlocal pressure Hessian.
The fourth is the affine-like hard corridor.

## 5. Why the exact affine anti-model survives this identity

For the exact constant-gradient model

\[
u(x)=Mx,
\]

with planar strain

\[
S=\operatorname{diag}(a,0,-a)
\]

and rotation about `e_2`, one has

\[
\Delta S=0,
\qquad
\lambda_2=0,
\qquad
\sin\theta_2=0.
\]

The compatible quadratic pressure has

\[
e_2^T\nabla^2p\,e_2=0.
\]

Therefore every term in the middle-eigenvalue equation vanishes.

Hence the new identity does **not** falsely exclude the exact affine model.
It identifies precisely why that model is exceptional: it lies in the quiescent planar-balance lane.

## 6. Next reduction target

The remaining hard object is now

\[
\boxed{
\begin{array}{c}
|S|\text{ large},\quad |\lambda_2|\ll|S|,\quad \xi\approx e_2,\\
D_t\xi\approx D_te_2,\\
\nu e_2^T\Delta S e_2-e_2^T\nabla^2p\,e_2\approx0.
\end{array}
}
\]

If derivative/pressure roughness is excluded, this is an increasingly affine-like local geometry.
The next standard step is therefore a quantitative Campanato/affine-coherence test: either the locked planar field is close to a constant-gradient affine rotor on a natural cell, or its spatial variation itself pays an H/T derivative action.

## 7. Scope

This is a structural reduction, not a regularity proof.
No claim is made that pressure-curvature cancellation is impossible at arbitrary critical amplitude.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
