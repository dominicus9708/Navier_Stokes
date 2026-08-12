# Moving observer sphere and deforming material-region bridge

Date: 2026-08-12

Status: **DERIVED KINEMATIC BRIDGE + COMPUTATIONAL CHECK + OPEN PROOF TARGET**.

This note replaces the idea that all local spherical diagnostics must remain tied to one fixed Eulerian origin. The global physical domain remains `R^3`. What moves is the local analysis center and, separately, the material neighborhood carried by the fluid.

## 1. Two different moving local objects

Let `a` be an initial material label and let the flow map satisfy

\[
\frac{d}{dt}\Phi_t(a)=u(\Phi_t(a),t),
\qquad
\Phi_0(a)=a.
\]

Define the moving center

\[
X(a,t)=\Phi_t(a).
\]

For a local scale `ell>0`, keep two distinct objects.

### 1.1 Co-moving spherical observation window

\[
S^{\rm obs}_\ell(a,t)
=
\{x:|x-X(a,t)|=\ell\}.
\]

It translates with the fluid center but is deliberately kept spherical. It is not a material boundary: fluid may cross it.

### 1.2 Material cell

\[
\Omega^{\rm mat}_\ell(a,t)
=
\Phi_t(B_\ell(a)).
\]

This region follows the same fluid particles. It may stretch, rotate, shear, and fold while the solution remains smooth.

The pair

\[
S^{\rm obs}_\ell(a,t)
\leftrightarrow
\Omega^{\rm mat}_\ell(a,t)
\]

separates pure translation from genuine deformation.

## 2. Exact deformation-gradient identities

Set

\[
F(a,t)=D_a\Phi_t(a).
\]

For a smooth solution,

\[
\frac{dF}{dt}
=
(\nabla u)(X(a,t),t)F.
\]

Let

\[
J(a,t)=\det F(a,t).
\]

Liouville's formula gives

\[
\frac{dJ}{dt}
=(\nabla\cdot u)(X(a,t),t)J.
\]

Hence incompressibility and `J(a,0)=1` imply

\[
\boxed{J(a,t)=1}
\]

throughout the smooth lifespan. Therefore material volume is preserved:

\[
|\Omega^{\rm mat}_\ell(a,t)|=|B_\ell(a)|.
\]

This does **not** imply shape preservation.

## 3. Strain, rotation, and shape

Write

\[
\nabla u=S+\Omega,
\]

with

\[
S=\frac12(\nabla u+\nabla u^T),
\qquad
\Omega=\frac12(\nabla u-\nabla u^T).
\]

For a material line element `Fv`,

\[
\frac{d}{dt}|Fv|^2
=2(Fv)^T S(Fv).
\]

The antisymmetric rotation tensor contributes no instantaneous change of length because

\[
v^T\Omega v=0.
\]

Define the right Cauchy-Green tensor

\[
C=F^TF.
\]

Then

\[
\frac{dC}{dt}=2F^TSF.
\]

Thus the actual shape difference between the co-moving spherical reference and the material cell is strain-driven.

## 4. DSD local deformation channel

Let

\[
U=(F^TF)^{1/2}
\]

be the right stretch tensor. For a volume-preserving smooth flow, its principal stretches satisfy

\[
\sigma_1\sigma_2\sigma_3=1.
\]

Introduce the first rotation-insensitive bridge quantity

\[
\boxed{
\Delta_{\rm shape}(a,t)
=
\|\log U(a,t)\|_F
}
\]

with `Delta_shape=0` for a locally rigid co-translation/rotation and positive value for anisotropic strain.

This is a **BRIDGE DEFINITION**, not an existing regularity criterion.

The DSD moving local block is provisionally

\[
\mathcal M(a,\ell,t)
=
\bigl(
X,F,J,C,\sigma_1,\sigma_2,\sigma_3,
\Delta_{\rm shape},
\lambda_1,\lambda_2,\lambda_3,
\lambda_2^+,
\Omega
\bigr),
\]

and later receives pressure, vorticity-alignment, and critical `L^3` channels from the existing proof pipeline.

## 5. Exact Gaussian benchmark at an advecting point

Use the current divergence-free Gaussian `z` seed and choose

\[
a=(0,0,1/2).
\]

At `t=0`, writing

\[
c=e^{-1/4},
\]

one obtains

\[
u(a,0)=(0,0,4c),
\]

so the local center is moving in the positive `z` direction.

At the same point,

\[
S(a,0)=\operatorname{diag}(2c,2c,-4c),
\qquad
\Omega(a,0)=0.
\]

The ordered strain eigenvalues are

\[
(-4c,2c,2c),
\]

whose sum is zero.

For the frozen local-gradient visualization only,

\[
F_{\rm fr}(\tau)
=
\operatorname{diag}
\left(
 e^{2c\tau},
 e^{2c\tau},
 e^{-4c\tau}
\right).
\]

Its determinant is exactly

\[
\det F_{\rm fr}=1.
\]

Thus two directions expand while one contracts, with exact volume preservation.

The local shape gap is

\[
\Delta_{\rm shape}^{\rm fr}(\tau)
=
2\sqrt6\,e^{-1/4}|\tau|,
\]

and for `tau>=0` the principal-stretch aspect ratio is

\[
\frac{\sigma_{\max}}{\sigma_{\min}}
=e^{6e^{-1/4}\tau}.
\]

This frozen-gradient construction is not a time-integrated Navier-Stokes solution. It is a local deformation witness at the initial instant.

## 6. Direct link to the middle-eigenvalue channel

At the benchmark point,

\[
\lambda_2^+=2e^{-1/4}>0.
\]

Therefore the material-cell picture gives a geometric meaning to the already retained middle-eigenvalue danger channel: `lambda_2>0` means that at least two principal strain directions are locally expanding while incompressibility forces compensating contraction in the remaining direction.

This does not by itself prove that `lambda_2^+` becomes singular or remains bounded. It only places the existing strain criterion in the moving-cell DSD representation.

## 7. Translation completeness through material labels

A fixed-origin spherical diagnostic is not translation complete. While the solution remains smooth, however, the flow map is a bijective material labeling of space. Therefore an all-center Eulerian family may equivalently be indexed by initial material labels:

\[
\{x_0\in\mathbb R^3\}
\longleftrightarrow
\{a\in\mathbb R^3\}
\]

through `x=Phi_t(a)`.

This suggests replacing a preferred-origin quantity by a Lagrangian all-label/all-scale family

\[
\boxed{
\mathcal D_{\rm Lag}(t)
=
\sup_{a\in\mathbb R^3}
\sup_{\ell>0}
\mathcal D(a,\ell,t)
}
\]

for a future regularity-relevant local descriptor `D`.

This reparameterization does not reduce the mathematical quantifiers by itself; it removes the artificial fixed-origin bias and lets the diagnostic move with the candidate concentration region.

## 8. Material transport of local aggregates

For any sufficiently smooth scalar channel `f`, Reynolds transport on the material cell gives

\[
\frac{d}{dt}
\int_{\Omega^{\rm mat}_\ell(a,t)}f\,dx
=
\int_{\Omega^{\rm mat}_\ell(a,t)}
\left(D_tf+f\nabla\cdot u\right)dx.
\]

For incompressible flow this reduces to

\[
\boxed{
\frac{d}{dt}
\int_{\Omega^{\rm mat}_\ell(a,t)}f\,dx
=
\int_{\Omega^{\rm mat}_\ell(a,t)}D_tf\,dx
}
\]

and is the natural dynamic bridge from fixed-time Static Aggregation to a moving DSD lineage.

## 9. What this changes in the proof strategy

The local analysis target is no longer just

\[
D(x_0,\ell,t)
\]

on fixed balls. It becomes a paired moving diagnostic:

\[
\boxed{
D_{\rm obs}(a,\ell,t)
\quad\text{versus}\quad
D_{\rm mat}(a,\ell,t)
}
\]

where the first is measured on a co-moving spherical reference window and the second on the same material cell after deformation.

The difference can separate:

- translation;
- rigid rotation;
- anisotropic strain;
- pressure redistribution;
- vorticity alignment/stretching;
- nonlinear cross-coupling.

## 10. Current proof boundary

Established here:

- exact flow-map/Jacobian identities for a smooth incompressible flow;
- exact volume preservation while smooth;
- exact strain-only instantaneous length change;
- exact Gaussian initial deformation witness;
- a reproducible moving/material-cell baseline.

Still open:

- time evolution of these channels for an actual Navier-Stokes trajectory;
- all-label/all-scale bounds for arbitrary admissible smooth data;
- a coercive implication from the moving DSD block to an established regularity criterion;
- an a-priori estimate preventing unbounded accumulated strain/pressure/vorticity coupling.

The moving-cell representation is therefore a structural refinement of the proof search, not a regularity proof.
