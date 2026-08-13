# Kinetic-energy control of the absolute remote strain and the shrinking mesoscopic interaction radius

Date: 2026-08-13

Status: **DERIVED FAR-STRAIN TAIL FROM `omega=curl u` + FINITE KINETIC ENERGY / MESOSCOPIC LOCALIZATION**.

The far-field common-mode note controlled remote **differences** from the first-hitting `L-infinity` vorticity cap, but left the absolute common strain `S0(t)` as a separate background channel.  Finite kinetic energy gives an additional absolute far-field bound after integrating the vorticity curl onto the strain kernel.

---

## 1. Smooth far cutoff

Let `K` be the strain/vorticity kernel,

\[
|K(z)|\le C|z|^{-3},
\qquad
|\nabla K(z)|\le C|z|^{-4}.
\]

Choose a smooth radial far cutoff `chi_R` satisfying

\[
\chi_R=0\quad(|z|\le R),
\]

\[
\chi_R=1\quad(|z|\ge2R),
\]

and

\[
|\nabla\chi_R|\le C/R.
\]

Define the far strain schematically by

\[
S_{>R}(x)
=\int \chi_R(x-z)K(x-z)\omega(z)dz.
\]

---

## 2. Use `omega=curl u`

For a divergence-free velocity field,

\[
\omega=\nabla\times u.
\]

Integrating by parts transfers the curl derivative to the smooth far kernel/cutoff:

\[
S_{>R}(x)
=\int
\nabla_z\times
[\chi_R(x-z)K(x-z)]\,u(z)dz
\]

up to the fixed tensor/curl index arrangement.

The differentiated far kernel satisfies

\[
\left|
\nabla[\chi_RK]
\right|
\le
C|x-z|^{-4}
\]

on `|x-z|>=R`, including the transition annulus because

\[
R^{-1}|K|
\lesssim R^{-4}.
\]

Therefore Cauchy--Schwarz gives

\[
|S_{>R}(x)|
\le
C
\left(
\int_{|y|\ge R}|y|^{-8}dy
\right)^{1/2}
\|u\|_2.
\]

In three dimensions,

\[
\int_R^\infty r^{-8}r^2dr
\asymp R^{-5}.
\]

Hence

\[
\boxed{
|S_{>R}(x)|
\le
C R^{-5/2}\|u\|_2.
}
\]

This controls the **absolute** smooth far part, not only its difference across a core.

---

## 3. Apply the kinetic-energy inequality

For smooth unforced incompressible Navier--Stokes,

\[
\|u(t)\|_2
\le
\|u_0\|_2.
\]

Thus in physical variables, for every fixed physical distance `L>0`,

\[
\boxed{
|S_{>L}^{\rm phys}(x,t)|
\le
C L^{-5/2}\|u_0\|_2.
}
\]

At a blowup-scale checkpoint with

\[
r=W^{-1/2},
\]

normalized strain is

\[
S^{\rm norm}=r^2S^{\rm phys}=W^{-1}S^{\rm phys}.
\]

Therefore any **fixed physical far field** satisfies

\[
\boxed{
|S_{>L}^{\rm norm}|
\le
C W^{-1}L^{-5/2}\|u_0\|_2
\to0.
}
\]

So fixed macroscopic distances cannot provide an order-one normalized stretching field near a hypothetical singularity.

---

## 4. Normalized-radius form

In normalized variables, let the far cutoff radius be `R`.  Since

\[
\|U\|_2
=r^{-1/2}\|u\|_2
=W^{1/4}\|u\|_2,
\]

the same estimate is

\[
\boxed{
|S_{>R}^{\rm norm}|
\le
C R^{-5/2}W^{1/4}\|u_0\|_2.
}
\]

Take

\[
\boxed{
R(W)=W^\theta
}
\]

with

\[
\boxed{
\frac1{10}<\theta<\frac12.
}
\]

Then

\[
R^{-5/2}W^{1/4}
=W^{1/4-(5/2)\theta}
\to0.
\]

At the same time the corresponding physical radius is

\[
L(W)=rR
=W^{-1/2+\theta}
\to0.
\]

Hence one obtains the two-scale localization

\[
\boxed{
\text{normalized interaction radius }R(W)\to\infty,
\qquad
\text{physical interaction radius }L(W)\to0.
}
\]

---

## 5. Example choice

For

\[
\theta=\frac15,
\]

\[
R(W)=W^{1/5},
\qquad
L(W)=W^{-3/10}.
\]

The normalized far strain obeys

\[
\boxed{
|S_{>R(W)}^{\rm norm}|
\lesssim
W^{-1/4}\|u_0\|_2
\to0.
}
\]

Thus all order-one normalized stretching must arise inside a physical neighborhood of radius `O(W^-3/10)` for this concrete mesoscopic choice.

The exponent `1/5` is not claimed optimal; any `theta in (1/10,1/2)` has the same structural property.

---

## 6. DSD interpretation

The dangerous route now has three nested spatial scales:

1. **natural core:**
   \[
   r=W^{-1/2};
   \]
2. **mesoscopic interaction neighborhood:**
   \[
   L(W)=W^{-1/2+\theta};
   \]
3. **fixed/macroscopic exterior:** negligible after natural normalization.

Thus the adaptive proof search does not need to resolve all of `R3` at the natural scale.  It only has to track the shrinking mesoscopic neighborhood that can still influence the dangerous core at order one.

This formalizes the "highway rather than whole Earth" interpretation: the relevant route widens beyond the core only as much as needed to capture order-one interactions, while the rest of space enters below the normalized resolution threshold.

---

## 7. Remaining intermediate-scale problem

The unresolved spatial burden is now the annular range

\[
\boxed{
W^{-1/2}
\lesssim |x-x_j|
\lesssim
W^{-1/2+\theta}.
}
\]

In normalized coordinates this is

\[
1\lesssim |y|\lesssim W^\theta.
\]

The next question is whether this growing but physically shrinking intermediate region can maintain enough cross-core/projective strain to refill the local strict source gap without paying one of the existing enstrophy/palinstrophy/flux/deformation costs.

Status: **MACROSCOPIC FAR FIELD REMOVED / MESOSCOPIC INTERACTION CASCADE REMAINS**.
