# DSD M5-07 — Radial Morrey Monotonicity Neutrality

Date: 2026-08-26

Status: **M5 SUBSTEP / THE NATURAL SCALE-INVARIANT LOCAL-ENERGY MORREY QUANTITY HAS NO RADIAL SIGN AND IS EXACTLY NEUTRAL ON THE CRITICAL `1/r` SURVIVOR / LOCAL ENERGY EVOLUTION RETAINS SIGN-INDEFINITE CRITICAL BOUNDARY FLUX / PURE RADIAL SCALAR MONOTONICITY IS DEMOTED / GLOBAL REGULARITY UNPROVED.**

## 1. Natural radial critical energy

For a candidate singular center `X*`, define

\[
\boxed{
\mathcal M_2(r,t)
:=
\frac1r
\int_{B_r(X_*)}\frac{|u(x,t)|^2}{2}dx.
}
\]

This quantity is invariant under the Navier--Stokes scaling.

---

## 2. Exact radial derivative

Let

\[
H(r,t)=\int_{B_r(X_*)}\frac{|u|^2}{2}dx.
\]

Then

\[
\partial_rH(r,t)
=
\int_{S_r(X_*)}\frac{|u|^2}{2}dS
\]

for almost every `r`, and therefore

\[
\boxed{
r\partial_r\mathcal M_2
=
\int_{S_r}\frac{|u|^2}{2}dS
-
\mathcal M_2.
}
\]

There is no general sign in this identity.

---

## 3. Critical `1/r` profile is radially neutral

For the model critical geometry

\[
|u(x)|\sim |x-X_*|^{-1},
\]

one has

\[
H(r)\sim c r.
\]

Hence

\[
\boxed{
\mathcal M_2(r)\sim c,
\qquad
r\partial_r\mathcal M_2(r)\sim0.
}
\]

Thus the exact M5 survivor is a fixed/neutral profile for the simplest radial Morrey derivative.

A monotonicity theorem based only on the sign of this derivative cannot exclude the critical family without introducing additional structure.

---

## 4. Local energy evolution does not restore a sign

For smooth Navier--Stokes,

\[
\partial_t\frac{|u|^2}{2}
+
\nabla\cdot
\left[
\left(\frac{|u|^2}{2}+p\right)u
-\nu\nabla\frac{|u|^2}{2}
\right]
=
-\nu|\nabla u|^2.
\]

Integrating over `B_r` gives

\[
\boxed{
\frac{d}{dt}H(r,t)
+
u\int_{B_r}|\nabla u|^2dx
=
-\int_{S_r}
\left(\frac{|u|^2}{2}+p\right)u\cdot n\,dS
+
u\int_{S_r}\partial_n\frac{|u|^2}{2}dS.
}
\]

The pressure/advective boundary flux has no universal sign.

On `u~1/r`, all terms occur at the same critical order required to balance the local energy stored at scale `r` over a parabolic time `r^2`.

Therefore the local-energy equation alone does not create a one-sided radius monotonicity on the survivor.

---

## 5. DSD interpretation

The scalar radial channel

\[
\mathcal M_2(r,t)
\]

records how much critical kinetic energy is present at one radius, but it does not retain enough directional information to distinguish

- pressure inflow from pressure outflow;
- strain-dominated from rotation-dominated geometry;
- cross-characteristic coherence from a neutral `1/r` profile.

DSD therefore classifies pure radial Morrey monotonicity as an **information-reduced channel** for M5.

---

## 6. M5 consequence

The following route is demoted:

\[
\text{cross-radius critical family}
\stackrel{?}{\Longrightarrow}
\text{contradiction from a scalar monotone }\mathcal M_2(r,t).
\]

The survivor is radially neutral for this quantity, and the time evolution reintroduces the same sign-indefinite critical pressure flux already isolated in M5-03.

Thus any useful radius-to-radius theorem must retain additional structure, for example

- angular/directional information;
- pressure-Poisson multipole information;
- vorticity/strain alignment;
- or a genuinely critical compactness/lineage quantity across radius labels.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
