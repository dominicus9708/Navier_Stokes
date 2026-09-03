# DSD M17-008 — Axisymmetric no-swirl is an exact regular model of the material-winding CE-H branch

Date: 2026-09-03
Canonical ID: **M17-008**

Status: **EXTERNAL/INTERNAL FIREWALL / THE RANK-ONE GREAT-CIRCLE, MATERIAL-DIRECTOR, NODAL-WINDING GEOMETRY IS NOT IN ITSELF A BLOW-UP SIGNATURE. CLASSICAL AXISYMMETRIC NAVIER--STOKES FLOW WITHOUT SWIRL REALIZES THE SAME LOCAL CE-H STRUCTURE: `W = omega_theta e_theta`, THE AZIMUTHAL DIRECTION IS MATERIAL, THE STRAIN MAP PRESERVES `e_theta`, AND THE VECTOR LAPLACIAN PRESERVES `e_theta`. THIS CLASS IS CLASSICALLY GLOBALLY REGULAR. THEREFORE ANY PROOF THAT DECLARES GREAT-CIRCLE WINDING OR MATERIAL NODAL FILAMENTS CONTRADICTORY WOULD ALSO FALSELY EXCLUDE A KNOWN REGULAR CLASS. THE CORRECT TARGET IS CLASSIFICATION: EITHER THE GENERAL RANK-ONE CE-H SURVIVOR REDUCES TO AN AXISYMMETRIC/NO-SWIRL-LIKE REGULAR CLASS, OR IT MUST USE ADDITIONAL NON-AXISYMMETRIC NODAL/STRAIN DEGENERATION / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Classical axisymmetric no-swirl form

In cylindrical coordinates `(r,theta,z)`, take an axisymmetric velocity without swirl:

\[
U=u_r(r,z,t)e_r+u_z(r,z,t)e_z,
\qquad
u_\theta=0.
\]

The vorticity has only the azimuthal component

\[
\boxed{
W=\omega_\theta(r,z,t)e_\theta.
}
\]

Thus the vorticity direction is

\[
\boxed{\xi=e_\theta.}
\]

As a map into `S^2`, `e_theta` lies on the equatorial great circle and winds once around the symmetry axis.

The vorticity amplitude vanishes on the regular axis with the usual axis-compatible order, so the phase winding is tied to a nodal set exactly of the type isolated in M17-005--007.

---

## 2. Material direction freezing

In a no-swirl flow,

\[
\frac{d\theta}{dt}=0
\]

along particle trajectories.

Since `e_theta` depends only on the angular coordinate,

\[
\boxed{D_t e_\theta=0.}
\]

The similarity-coordinate statement is the corresponding

\[
\boxed{D_B\xi=0.}
\]

Thus the director-freezing condition of CE-H is exactly realized.

---

## 3. Strain eigenline

Because the field is axisymmetric,

\[
\frac1r\partial_\theta U
=\frac{u_r}{r}e_\theta.
\]

Therefore

\[
(W\cdot\nabla)U
=\omega_\theta\frac1r\partial_\theta U
=\frac{u_r}{r}\omega_\theta e_\theta.
\]

Hence

\[
\boxed{
(W\cdot\nabla)U=\sigma W,
\qquad
\sigma=\frac{u_r}{r}.
}
\]

Equivalently,

\[
\boxed{\Sigma W=\sigma W.}
\]

So the CE-H strain eigenline is also exact in the no-swirl axisymmetric class.

---

## 4. Laplacian eigenline

For an azimuthal vector field

\[
W=\omega_\theta e_\theta,
\]

the vector Laplacian is

\[
\boxed{
\Delta W
=\left(\Delta-\frac1{r^2}\right)\omega_\theta\,e_\theta.
}
\]

Therefore wherever `omega_theta != 0`,

\[
\boxed{
\Delta W=\kappa W,
\qquad
\kappa
=\frac{(\Delta-r^{-2})\omega_\theta}{\omega_\theta}.
}
\]

Thus the CE-H Laplacian eigenline is again realized exactly.

---

## 5. Great-circle phase and winding

In Cartesian coordinates,

\[
e_\theta=(-\sin\theta,\cos\theta,0).
\]

Hence the great-circle phase is

\[
\psi=\theta+\frac\pi2
\]

up to orientation.

Around a loop linking the symmetry axis,

\[
\boxed{
\frac1{2\pi}\oint d\psi=1.
}
\]

Therefore a nonzero phase-winding number and a codimension-two vorticity-zero defect are fully compatible with regular Navier--Stokes dynamics.

---

## 6. External regularity firewall

Global regularity of smooth three-dimensional axisymmetric Navier--Stokes flow **without swirl** is classical (Ukhovskii--Yudovich / Ladyzhenskaya tradition and subsequent formulations).

Thus the implication

\[
\text{material great-circle winding}
\Rightarrow
\text{contradiction}
\]

is false.

Likewise

\[
\text{regular material nodal filament}
\Rightarrow
\text{contradiction}
\]

is false.

These structures occur in a known globally regular class.

---

## 7. What distinguishes the remaining hard branch

M17 must therefore identify what a hypothetical singular rank-one CE-H state does **beyond** the regular no-swirl template.

Candidates include:

1. non-axisymmetric geometry of the nodal-filament network;
2. nodal creation/reconnection through degenerate analytic events;
3. `x_3`-dependent semilinear coupling in the M17-004 system that is not reducible to an axisymmetric meridional structure;
4. strain/eigenline interactions incompatible with the scalar no-swirl vorticity-ratio maximum principle.

The rank-one problem is now a classification problem, not a topology-exclusion problem.

---

## 8. Canonical target

The correct branch tree is

\[
\boxed{
R_1^{great-circle}
\Longrightarrow
R_{regular-model}
\ \lor\ 
T_{nodal}^{deg}
\ \lor\ 
G_{nonaxis}^{rank1}.
}
\]

- `R_regular-model`: axisymmetric/no-swirl-like geometry, expected to be regular if a genuine reduction can be proved.
- `T_nodal^deg`: nodal topology changes through degenerate zeros.
- `G_nonaxis^rank1`: persistent non-axisymmetric great-circle geometry with no nodal turnover; this is the genuine classification gap.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
