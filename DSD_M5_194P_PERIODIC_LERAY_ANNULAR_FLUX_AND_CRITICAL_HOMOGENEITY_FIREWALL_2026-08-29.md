# DSD M5-194P — Periodic Leray Annular Flux and Critical-Homogeneity Firewall

Date: 2026-08-29

Parent: `DSD_M5_194O_PERIODIC_ALPHA_SMALL_PERIOD_EXCLUSION_AND_NONSUMMABLE_TAIL_AUDIT_2026-08-29.md`

Status: **NEGATIVE EXPORT-SHORTCUT FIREWALL / A PERIODIC NONSUMMABLE CRITICAL TAIL DOES NOT BY ITSELF FORCE POSITIVE MATERIAL EXPORT THROUGH LARGE SPHERES / THE LERAY EQUATION CONTAINS AN INTRINSIC SIMILARITY-DRIFT ENERGY FLUX `Y|V|^2/4` / FOR AN EXACT `(-1)`-HOMOGENEOUS VELOCITY TAIL, THE SIMILARITY-DRIFT DIVERGENCE CANCELS THE BULK `-|V|^2/4` TERM POINTWISE / THUS A ZERO-MATERIAL-FLUX CRITICAL HALO IS NOT EXCLUDED BY THE PERIOD-AVERAGED ENERGY LEDGER / THE REMAINING PERIODIC OBSTRUCTION IS AN ASYMPTOTIC-HOMOGENEITY / CRITICAL-HALO PROBLEM, RECONNECTING TO THE M5-194 COMMON-TAIL BACKWARD-UNIQUENESS FRONTIER / GLOBAL REGULARITY UNPROVED.**

---

## 1. Purpose

M5-194O showed that a nonzero periodic similarity alpha-limit surviving the known Liouville theorems must, on the spatial Type-I branch, carry a nonsummable critical `L^3` tail.

The natural next hope is:

> If the tail repeats every similarity period, must it be replenished by a nonzero material flux through infinitely many large spheres, allowing the branch to be charged to the existing positive-frequency export ledger?

The answer is **not from the periodic Leray energy balance alone**.

The reason is that similarity coordinates contain a geometric scaling flux distinct from physical material transport.

---

## 2. Periodic Leray equation

The backward similarity profile solves

\[
V_s-\Delta V
+\frac12V
+\frac12(Y\cdot\nabla)V
+(V\cdot\nabla)V
+\nabla P=0,
\]

\[
\nabla\cdot V=0.
\]

Let

\[
e:=|V|^2.
\]

Dot the equation with `V`.

The terms become

\[
V_s\cdot V=\frac12\partial_s e,
\]

\[
-\Delta V\cdot V
=|\nabla V|^2-rac12\Delta e,
\]

\[
\frac12V\cdot V=\frac12e,
\]

and

\[
\frac12(Y\cdot\nabla V)\cdot V
=\frac14Y\cdot\nabla e
=\nabla\cdot\left(\frac14Ye\right)-\frac34e.
\]

The nonlinear and pressure terms are

\[
(V\cdot\nabla V)\cdot V
=\nabla\cdot\left(\frac12eV\right),
\]

\[
\nabla P\cdot V=\nabla\cdot(PV).
\]

Therefore

\[
\boxed{
\frac12\partial_s e
+|\nabla V|^2
-\frac14e
+\nabla\cdot\mathcal F=0,
}
\]

with total similarity-energy flux

\[
\boxed{
\mathcal F
=-\frac12\nabla e
+\frac14Ye
+\frac12eV
+PV.
}
\]

---

## 3. Flux decomposition

Separate

\[
\boxed{
\mathcal F
=\mathcal F_{diff}
+\mathcal F_{sim}
+\mathcal F_{mat},
}
\]

where

\[
\mathcal F_{diff}:=-\frac12\nabla e,
\]

\[
\boxed{
\mathcal F_{sim}:=\frac14Ye,
}
\]

and

\[
\boxed{
\mathcal F_{mat}:=\left(\frac12e+P\right)V.
}
\]

The crucial DSD distinction is

\[
\boxed{
\mathcal F_{sim}
\ne
\text{physical material export}.
}
\]

It is generated solely by the time-dependent similarity coordinate transformation.

---

## 4. Full-period ball balance

Assume

\[
V(s+S)=V(s).
\]

Integrate over one period and a ball `B_R`.

The time derivative cancels:

\[
\int_0^S\partial_s e\,ds=0.
\]

Thus

\[
\boxed{
\int_0^S\int_{B_R}
\left(
|\nabla V|^2-\frac14|V|^2
\right)dYds
+
\int_0^S\int_{\partial B_R}
\mathcal F\cdot n\,dSds
=0.
}
\]

Equivalently,

\[
\boxed{
\mathcal J_{mat}(R)
=
-\mathcal J_{sim}(R)
-\mathcal J_{diff}(R)
-\mathcal B(R),
}
\]

where

\[
\mathcal B(R)
:=
\int_0^S\int_{B_R}
\left(
|\nabla V|^2-\frac14|V|^2
\right),
\]

and `J_*` denote the corresponding period-integrated boundary fluxes.

There is no sign forcing `J_mat(R)` to be positive.

---

## 5. Critical `1/r` scale ledger

For the borderline spatial tail

\[
|V(Y,s)|\sim R^{-1}
\qquad(|Y|\sim R),
\]

we have

\[
e\sim R^{-2}.
\]

The similarity-drift boundary density satisfies

\[
\mathcal F_{sim}\cdot n
=\frac14R e
\sim R^{-1}.
\]

Since the sphere has area `~R^2`,

\[
\boxed{
\int_{\partial B_R}
\mathcal F_{sim}\cdot n
\sim R.
}
\]

Meanwhile the bulk energy has the same order:

\[
\int_{B_R}e\sim R.
\]

By contrast, if `nabla V ~ R^-2`, the exterior dissipation contribution has lower radial order.

Therefore a linearly growing similarity flux is exactly natural at the critical `1/r` tail scale.

It cannot be automatically interpreted as physical export.

---

## 6. Exact homogeneity cancellation

The criticality becomes transparent before integration.

Combine the bulk scaling term and similarity-drift divergence:

\[
-\frac14e
+\nabla\cdot\left(\frac14Ye\right).
\]

Since

\[
\nabla\cdot(Ye)
=3e+Y\cdot\nabla e,
\]

we obtain

\[
\boxed{
-\frac14e
+\nabla\cdot\left(\frac14Ye\right)
=
\frac14\left(
2e+Y\cdot\nabla e
\right).
}
\]

Now suppose the velocity is exactly `(-1)`-homogeneous in space:

\[
V(\lambda Y,s)=\lambda^{-1}V(Y,s).
\]

Then

\[
e(\lambda Y,s)=\lambda^{-2}e(Y,s),
\]

so Euler's homogeneous-function identity gives

\[
Y\cdot\nabla e=-2e.
\]

Therefore

\[
\boxed{
2e+Y\cdot\nabla e=0.
}
\]

Hence

\[
\boxed{
-\frac14e
+\nabla\cdot\mathcal F_{sim}=0
}
\]

pointwise.

This is an exact critical-homogeneity cancellation.

---

## 7. Homogeneity-defect variable

Define the scalar energy homogeneity defect

\[
\boxed{
\mathcal H_e
:=
2|V|^2
+Y\cdot\nabla|V|^2.
}
\]

Then the local periodic Leray energy equation can be rewritten as

\[
\boxed{
\frac12\partial_s|V|^2
+|\nabla V|^2
+\frac14\mathcal H_e
+\nabla\cdot
\left(
\mathcal F_{diff}+\mathcal F_{mat}
\right)
=0.
}
\]

This removes the coordinate scaling flux from the explicit boundary ledger and replaces it with the bulk homogeneity defect.

Thus the correct question is not

\[
\text{does the critical tail require material export?}
\]

but

\[
\boxed{
\text{does the critical tail have a nonzero accumulated homogeneity defect?}
}
\]

If the tail becomes asymptotically homogeneous, `H_e` can tend to zero while the nonsummable tail remains.

---

## 8. Explicit zero-material-flux model warning

Consider at the scale-ledger level a tangential critical field with

\[
V_r=0,
\qquad
|V|\sim r^{-1}.
\]

Then the convective kinetic-energy flux

\[
\frac12|V|^2V_r
\]

vanishes identically.

If the pressure radial flux is also absent or cancels and the profile is exactly homogeneous, the scaling part of the energy budget can still balance without a positive material-energy export.

This is a mechanism-level warning, not a claim that such a field is an exact periodic Navier--Stokes profile.

It proves that tail criticality alone is insufficient to charge the branch to `T_export`.

---

## 9. Relation to earlier common-tail audits

M5-194A--G found that a critical common tail

\[
B_T\sim r^{-1}
\]

is exactly the first-order endpoint at which scalar Carleman absorption loses its spatial small factor.

The present periodic-tail calculation reaches the same scale from a different direction:

\[
\boxed{
\text{periodic nonsummable tail}
\to
\text{possible asymptotic }(-1)\text{ homogeneity}
\to
\text{zero similarity homogeneity defect}
\to
\text{no forced material export}.
}
\]

Thus the periodic/DSS branch and the critical backward-uniqueness branch are not independent endgames. They meet at the same `1/r` common-tail geometry.

---

## 10. DSD verdict

### CLOSED

The shortcut

\[
\boxed{
\text{periodic nonsummable critical tail}
\Longrightarrow
\text{positive physical material export at large radius}
}
\]

is invalid from the period-averaged Leray energy balance alone.

The similarity coordinate drift can carry the critical scaling budget.

### REDUCED

A periodic large-period survivor must now do one of the following:

1. have a nontrivial asymptotic homogeneity defect `H_e`, which may be chargeable through physical/diffusive flux or derivative-tail terms;
2. approach an asymptotically `(-1)`-homogeneous critical halo, in which the scaling defect vanishes.

### SURVIVING HARD ENDPOINT

The second case is the harder one and reconnects directly to the existing critical common-tail problem:

\[
\boxed{
\text{periodic active core}
+
\text{asymptotically homogeneous }1/r\text{ halo}.
}
\]

This is not closed by the current material-export ledger.

---

## 11. Next audit target

The next calculation should derive an annular equation for the **homogeneity defect itself** or, more directly, for the vector scaling generator

\[
\boxed{
\mathcal G[V]
:=V+(Y\cdot\nabla)V.
}
\]

For an exact `(-1)`-homogeneous spatial tail,

\[
\mathcal G[V]=0.
\]

The task is to determine whether a periodic Leray profile can have

\[
\mathcal G[V]\to0
\quad\text{as }|Y|\to\infty
\]

while maintaining the nonzero recurrent checkpoint core.

If such asymptotic spatial homogeneity forces the periodic tail into a classified stationary/rotating finite-dimensional profile, the periodic branch may close.

If not, the precise remaining object is a **time-periodic angular profile on the sphere with `1/r` radial scaling**, which should be written as the next sphere-cylinder endpoint system.
