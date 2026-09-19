# M20-005 — Transverse strain action is an exact projective double commutator and enters the vorticity-direction Rayleigh quotient with a positive quadratic term but no standalone Lyapunov sign

Date: 2026-09-19  
Canonical ID: **M20-005**  
Status: **STRAIN-EIGENFRAME PROJECTIVE GEOMETRY / THE M20-002 TRANSVERSE STRAIN CHANNEL IS EXACTLY THE DOUBLE-COMMUTATOR FLOW OF THE RANK-ONE VORTICITY PROJECTOR / ITS SQUARED SIZE IS THE STRAIN EIGENVALUE VARIANCE SEEN BY THE VORTICITY DIRECTION / IN THE MATERIAL EVOLUTION OF THE DIRECTIONAL STRETCHING RAYLEIGH QUOTIENT IT APPEARS WITH A POSITIVE QUADRATIC CONTRIBUTION, BUT PRESSURE-HESSIAN, STRAIN-DIFFUSION, AND VISCOUS PROJECTIVE TERMS CAN COMPENSATE IT / NO MONOTONE CLOSURE YET / GLOBAL REGULARITY UNPROVED**

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Physical projective variables

On the nonzero-vorticity set write

\[
\omega=\rho\xi,
\qquad
\rho=|\omega|,
\qquad
|\xi|=1.
\]

Let

\[
S=\frac12(\nabla u+\nabla u^T)
\]

be the strain tensor.

Define the rank-one vorticity projector

\[
\boxed{
Q:=\xi\otimes\xi.
}
\]

Also define the directional stretching Rayleigh quotient

\[
\boxed{
\gamma:=\xi^TS\xi.
}
\]

The transverse strain vector is

\[
\boxed{
s_\perp
:=
P_\xi^\perp S\xi
=
S\xi-\gamma\xi.
}
\]

Its squared magnitude is the M20-002 strain-eigenframe density.

## 2. Exact projector strain flow

Ignoring viscosity only for this algebraic subsection, the strain part of the vorticity-direction equation is

\[
D_t\xi\big|_S=s_\perp.
\]

Therefore

\[
\begin{aligned}
D_tQ\big|_S
&=
s_\perp\otimes\xi
+
\xi\otimes s_\perp
\\
&=
SQ+QS-2\gamma Q.
\end{aligned}
\]

Since

\[
QSQ=\gamma Q,
\]

we have

\[
\boxed{
D_tQ\big|_S
=
[[S,Q],Q].
}
\]

Thus transverse strain acts on the vorticity axis by a projective double commutator.

## 3. Exact norm identity

For a rank-one projector,

\[
[S,Q]
\]

measures failure of the vorticity axis to be a strain eigenspace.

A direct calculation gives

\[
\boxed{
\|[S,Q]\|_F^2
=
2|s_\perp|^2,
}
\]

and likewise

\[
\boxed{
\|[[S,Q],Q]\|_F^2
=
2|s_\perp|^2.
}
\]

Hence

\[
\boxed{
|s_\perp|^2
=
\frac12\|[S,Q]\|_F^2
=
\frac12\|D_tQ|_S\|_F^2.
}
\]

This is an exact projective-geometric interpretation of the M20-002 strain channel.

## 4. Eigenframe variance form

Let

\[
Se_i=\lambda_i e_i,
\qquad
a_i=(\xi\cdot e_i)^2,
\qquad
\sum_i a_i=1.
\]

Then

\[
\gamma=\sum_i a_i\lambda_i,
\]

and

\[
\boxed{
|s_\perp|^2
=
\sum_i a_i\lambda_i^2-\gamma^2
=
\sum_{i<j}
a_i a_j(\lambda_i-\lambda_j)^2.
}
\]

Thus the projective commutator is exactly the variance of strain eigenvalues sampled by the vorticity-direction weights.

## 5. Material direction equation with viscosity

The exact physical vorticity-direction equation is

\[
D_t\xi
=
s_\perp+v_\perp,
\]

where

\[
D_t:=\partial_t+u\cdot\nabla
\]

and

\[
\boxed{
v_\perp
:=
\frac{\nu}{\rho}
P_\xi^\perp\Delta\omega.
}
\]

Therefore

\[
\boxed{
D_tQ
=
[[S,Q],Q]
+
v_\perp\otimes\xi
+
\xi\otimes v_\perp.
}
\]

The projective dynamics has exactly two material sources:

1. transverse strain;
2. viscous projective diffusion.

Eulerian transport has disappeared because \(D_t\) follows the material motion.

## 6. Strain-only Rayleigh ascent

If S were frozen and viscosity absent, then

\[
\frac d{dt}\gamma
=
2(D_t\xi)\cdot S\xi
=
2s_\perp\cdot S\xi.
\]

Since

\[
S\xi=\gamma\xi+s_\perp
\]

and

\[
s_\perp\cdot\xi=0,
\]

we obtain

\[
\boxed{
\frac d{dt}\gamma\Big|_{\text{frozen }S,\nu=0}
=
2|s_\perp|^2
\ge0.
}
\]

Thus for a fixed symmetric strain tensor, the strain-induced projective flow is the Rayleigh-quotient ascent toward an extensional eigendirection.

This gives the positive quadratic meaning of the transverse strain action.

## 7. Full material derivative of gamma

For evolving S and nonzero viscosity,

\[
\gamma=\xi^TS\xi
\]

gives

\[
D_t\gamma
=
\xi^T(D_tS)\xi
+
2(D_t\xi)\cdot S\xi.
\]

Using

\[
D_t\xi=s_\perp+v_\perp,
\]

we get

\[
\boxed{
D_t\gamma
=
\xi^T(D_tS)\xi
+
2|s_\perp|^2
+
2v_\perp\cdot s_\perp.
}
\]

Thus the positive projective strain term is not isolated from strain-tensor evolution or viscous direction coupling.

## 8. Insert the exact strain equation

For incompressible Navier--Stokes,

\[
\boxed{
D_tS
=
-S^2-\Omega^2-\nabla^2p+\nu\Delta S,
}
\]

where

\[
\Omega
=
\frac12(\nabla u-\nabla u^T).
\]

Because the vorticity direction is the rotation axis of \(\Omega\),

\[
\Omega\xi=0.
\]

Hence

\[
\xi^T\Omega^2\xi=0.
\]

Also

\[
\xi^TS^2\xi
=
|S\xi|^2
=
\gamma^2+|s_\perp|^2.
\]

Substitute into Section 7:

\[
\boxed{
\begin{aligned}
D_t\gamma
&=
-\gamma^2
+
|s_\perp|^2
-
\xi^T(\nabla^2p)\xi
\\
&\quad
+
\nu\,\xi^T(\Delta S)\xi
+
2v_\perp\cdot s_\perp.
\end{aligned}
}
\]

Equivalently,

\[
\boxed{
|s_\perp|^2
=
D_t\gamma
+
\gamma^2
+
\xi^T(\nabla^2p)\xi
-
\nu\,\xi^T(\Delta S)\xi
-
2v_\perp\cdot s_\perp.
}
\]

This is the exact compensation law for the M20 strain-eigenframe payer.

## 9. What the positive term means

The positive term

\[
|s_\perp|^2
\]

measures projective strain rotation.

If S were externally fixed, it would monotonically increase the Rayleigh quotient.

In Navier--Stokes, however, the same quantity is balanced by:

- material change of \(\gamma\);
- the Riccati term \(\gamma^2\);
- the directional pressure Hessian;
- strain diffusion;
- viscous projective cross-coupling.

Therefore

\[
\boxed{
|s_\perp|^2>0
\not\Rightarrow
\text{monotone stretching growth}.
}
\]

## 10. Pressure re-enters only through strain dynamics

M20-001--004 use the curl/vorticity equation and are pressure free at the first-residual level.

M20-005 shows that once the transverse strain channel itself is evolved, the pressure Hessian returns through the strain equation:

\[
-\xi^T\nabla^2p\,\xi.
\]

This is not a contradiction.

It identifies precisely where the nonlocal pressure coupling re-enters the projective proof tree.

## 11. Relation to exact CE-H geometry

On an exact CE-H state satisfying

\[
S\omega=\sigma\omega,
\]

one has

\[
s_\perp=0.
\]

Thus the M20 strain-eigenframe branch is absent on that exact alignment submanifold.

However M20 does not assume that the general terminal hard survivor lies on exact CE-H.

Therefore the correct reading is:

\[
\boxed{
S_{\rm eig}\neq0
\Longrightarrow
\text{departure from exact strain-vorticity eigenalignment}.
}
\]

The separate CE-H branch retains its own viscous/coefficient geometry.

## 12. Quantitative consequence for the M20 strain branch

If M20-002 supplies

\[
\left\langle
1_E|s_\perp|^2
\right\rangle
\ge s_*>0
\]

on a robust high-vorticity set E, then equivalently

\[
\boxed{
\left\langle
1_E\|[S,Q]\|_F^2
\right\rangle
\ge
2s_*.
}
\]

Thus the strain branch has a coordinate-free finite-dimensional detector:

\[
\boxed{
[S,Q]\neq0.
}
\]

This is useful for compactness and finite-window recurrence arguments because it avoids choosing strain eigenvectors through degeneracies.

## 13. Criticality and recurrence firewall

The commutator norm is still a normalized Type-I critical observable.

A compact recurrent state can sustain repeated nonzero

\[
[S,Q]
\]

while pressure/strain/diffusion variables cycle.

Therefore the projective commutator by itself is not a finite ancestral budget.

No global contradiction follows from a recurrent positive floor alone.

## 14. Updated projective strain target

The useful next question is no longer whether transverse strain exists.

It is whether recurrent

\[
[S,Q]\neq0
\]

can remain balanced by the right-hand side of

\[
|s_\perp|^2
=
D_t\gamma+\gamma^2
+\xi^T\nabla^2p\,\xi
-\nu\xi^T\Delta S\,\xi
-2v_\perp\cdot s_\perp
\]

without forcing one of the already typed critical pressure/derivative/transport exits.

This is a compensation/covariance problem, not a new unsigned norm problem.

\[
\boxed{\text{M20-005 COMPLETE; TRANSVERSE STRAIN IS AN EXACT PROJECTIVE DOUBLE-COMMUTATOR WITH POSITIVE RAYLEIGH ASCENT BUT NO STANDALONE LYAPUNOV SIGN.}}
\]

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
