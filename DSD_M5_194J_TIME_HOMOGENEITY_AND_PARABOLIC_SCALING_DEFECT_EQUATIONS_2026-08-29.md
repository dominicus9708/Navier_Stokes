# DSD M5-194J — Time, Homogeneity, and Parabolic Scaling-Defect Equations

Date: 2026-08-29

Parent: `DSD_M5_194I_TYPE_I_LIMIT_TO_SVERAK_PREREQUISITE_LEDGER_2026-08-29.md`

Status: **EXACT DEFECT SYSTEM DERIVED / THE TIME DEFECT AND PARABOLIC SCALING DEFECT BOTH SOLVE THE LINEARIZED NAVIER--STOKES SYSTEM AROUND THE ANCIENT SURVIVOR / THE PURE SPATIAL `(-1)`-HOMOGENEITY DEFECT IS FORCED BY THE TIME DEFECT / TYPE-I SIZE CONTROL DOES NOT MAKE ANY OF THESE DEFECTS SUBCRITICAL / IF THE PARABOLIC SCALING DEFECT VANISHED IDENTICALLY UP TO THE REGULAR TERMINAL TIME, THE FIRST-HITTING NONTRIVIALITY WOULD BE IMPOSSIBLE / THEREFORE A NONTRIVIAL SURVIVOR MUST RETAIN A FORMED SCALING DEFECT UNLESS A SECOND BACKWARD LIMIT IS TAKEN / NEXT FRONTIER IS DEFECT PERSISTENCE IN SIMILARITY TIME / GLOBAL REGULARITY UNPROVED.**

---

## 1. Ancient Navier--Stokes equation

Let the fixed-center ancient survivor satisfy

\[
\partial_\tau U
-\Delta U
+(U\cdot\nabla)U
+\nabla P=0,
\qquad
\nabla\cdot U=0
\]

on

\[
\mathbb R^3\times(-\infty,0].
\]

Define the linearized Navier--Stokes operator around `U` by

\[
\boxed{
\mathcal L_U V
:=
\partial_\tau V
-\Delta V
+(U\cdot\nabla)V
+(V\cdot\nabla)U.
}
\]

All vector defects below are divergence free.

---

## 2. Time defect

Define

\[
\boxed{
\mathcal T
:=\partial_\tau U.
}
\]

Differentiate Navier--Stokes in time. Then

\[
\boxed{
\mathcal L_U\mathcal T
+\nabla(\partial_\tau P)=0,
\qquad
\nabla\cdot\mathcal T=0.
}
\]

Thus the time defect solves the homogeneous linearized Navier--Stokes system.

This is exact and requires no homogeneity assumption.

Stationarity is precisely

\[
\boxed{\mathcal T=0.}
\]

---

## 3. Parabolic scaling defect

Navier--Stokes is invariant under

\[
U^{(\lambda)}(y,\tau)
:=
\lambda U(\lambda y,\lambda^2\tau),
\]

\[
P^{(\lambda)}(y,\tau)
:=
\lambda^2P(\lambda y,\lambda^2\tau).
\]

Differentiate this solution family at `lambda=1`.

The velocity scaling defect is

\[
\boxed{
\mathcal Z
:=
\left.\partial_\lambda U^{(\lambda)}\right|_{\lambda=1}
=
U+y\cdot\nabla U+2\tau\partial_\tau U.
}
\]

The corresponding pressure defect is

\[
\boxed{
\Pi_Z
:=
2P+y\cdot\nabla P+2\tau\partial_\tau P.
}
\]

Differentiating the Navier--Stokes equation along the exact scaling symmetry yields

\[
\boxed{
\mathcal L_U\mathcal Z
+\nabla\Pi_Z=0,
\qquad
\nabla\cdot\mathcal Z=0.
}
\]

Hence the parabolic scaling defect also solves the homogeneous linearized system.

Exact parabolic self-similarity is equivalent to

\[
\boxed{\mathcal Z=0.}
\]

---

## 4. Pure spatial `(-1)`-homogeneity defect

Define

\[
\boxed{
\mathcal H
:=
U+y\cdot\nabla U.
}
\]

Then

\[
\boxed{
\mathcal Z
=\mathcal H+2\tau\mathcal T.
}
\]

Let

\[
\Pi_H:=2P+y\cdot\nabla P.
\]

Using the equations for `mathcal Z` and `mathcal T`, together with

\[
\mathcal L_U(2\tau\mathcal T)
=
2\mathcal T
+2\tau\mathcal L_U\mathcal T,
\]

we obtain

\[
\boxed{
\mathcal L_U\mathcal H
+\nabla\Pi_H
=-2\mathcal T.
}
\]

Thus spatial homogeneity is not dynamically independent of stationarity.

The exact stationary homogeneous regime requires simultaneously

\[
\boxed{
\mathcal T=0,
\qquad
\mathcal H=0.
}
\]

Then automatically

\[
\mathcal Z=0.
\]

Conversely, `mathcal Z=0` alone gives parabolic self-similarity, not physical-time stationarity.

This distinction prevents the stationary Šverák classification from being substituted directly for a parabolic self-similar theorem.

---

## 5. Vorticity defect system

Let

\[
\Omega=\nabla\times U.
\]

The vorticity equation is

\[
\partial_\tau\Omega
-\Delta\Omega
+(U\cdot\nabla)\Omega
-(\Omega\cdot\nabla)U=0.
\]

### 5.1 Time-vorticity defect

Define

\[
K:=\partial_\tau\Omega.
\]

Differentiation gives

\[
\boxed{
\partial_\tau K
-\Delta K
+(U\cdot\nabla)K
+(\mathcal T\cdot\nabla)\Omega
-(K\cdot\nabla)U
-(\Omega\cdot\nabla)\mathcal T
=0.
}
\]

### 5.2 Scaling-vorticity defect

Since the vorticity scaling is

\[
\Omega^{(\lambda)}(y,\tau)
=\lambda^2\Omega(\lambda y,\lambda^2\tau),
\]

we have

\[
\boxed{
\mathcal Z_\Omega
:=\nabla\times\mathcal Z
=
2\Omega+y\cdot\nabla\Omega+2\tau\partial_\tau\Omega.
}
\]

The pressure disappears from this formulation.

If a future estimate proves

\[
\mathcal Z_\Omega=0
\]

and separately controls the curl-free divergence-free part of `mathcal Z` through the inherited Morrey/gauge conditions, then one may hope to recover

\[
\mathcal Z=0.
\]

This pressure-free route may be more economical than attacking the velocity defect directly.

---

## 6. Type-I scaling does not make the defects small

The inherited ancient vorticity bound is

\[
\|\Omega(\tau)\|_\infty
\lesssim |\tau|^{-1}
\qquad(\tau\to-\infty).
\]

A scale-compatible velocity magnitude is

\[
|U|\sim |\tau|^{-1/2}
\]

on spatial scale

\[
|y|\sim |\tau|^{1/2}.
\]

At this scaling,

\[
|y\cdot\nabla U|\sim|U|,
\]

and a natural time derivative has size

\[
|\partial_\tau U|\sim|\tau|^{-3/2}.
\]

Therefore

\[
|2\tau\partial_\tau U|\sim|\tau|^{-1/2},
\]

which is the same size as both `U` and `y·nabla U`.

Hence

\[
\boxed{
\text{Type-I decay gives no automatic small factor in }\mathcal Z.
}
\]

The same is true of `mathcal H` and the naturally normalized `mathcal T`.

This is another endpoint-criticality statement: scaling symmetry places the defect at exactly the same order as the field.

---

## 7. Terminal-time obstruction to an exact self-similar survivor

The extracted first-hitting ancient solution is regular at its normalized terminal time and satisfies

\[
|\Omega(y_*,0)|=1.
\]

Suppose nevertheless that

\[
\mathcal Z\equiv0
\]

on the ancient interval and the scaling identity extends to `tau=0` by the recorded regularity.

Then for every `lambda>0`,

\[
U(y,0)
=
\lambda U(\lambda y,0).
\]

Thus `U(\cdot,0)` is spatially homogeneous of degree `-1`.

But a degree `-1` vector field which is smooth at the scaling center `y=0` must vanish identically. Indeed, for any fixed `y`,

\[
U(y,0)=\lambda U(\lambda y,0),
\]

and sending `lambda -> 0` while using boundedness near the origin gives

\[
U(y,0)=0.
\]

Therefore

\[
\Omega(y,0)=0,
\]

contradicting

\[
|\Omega(y_*,0)|=1.
\]

Hence

\[
\boxed{
\text{the nontrivial first-hitting ancient survivor cannot itself satisfy }\mathcal Z\equiv0.
}
\]

This does **not** rule out a second, backward renormalized limit becoming self-similar. It only says that the terminally normalized ancient survivor is not already that object.

---

## 8. Relation to known self-similar nonexistence results

Nečas--Růžička--Šverák proved triviality of backward self-similar profiles in `L^3(R^3)`.

Tsai later proved that a backward Leray self-similar weak solution satisfying the local energy estimates in a cylinder is identically zero.

These results strengthen the same gate:

\[
\boxed{
\text{if a future backward renormalization produces an exact self-similar limit}\
\text{and the inherited local energy class passes to it, that limit is forced to zero.}
}
\]

However, `DSD_RENORMALIZED_RECURRENCE_SELF_SIMILARITY_BOUNDARY_AUDIT_2026-08-25.md` already established that snapshot recurrence and the first-hitting scaling factor do not imply full spacetime DSS/self-similarity.

Thus the missing ingredient is still defect vanishing or coherent spacetime recurrence, not the absence of an external Liouville theorem.

---

## 9. DSD verdict

### EXACTLY DERIVED

\[
\boxed{
\mathcal L_U\mathcal T+\nabla P_\tau=0
}
\]

\[
\boxed{
\mathcal L_U\mathcal Z+\nabla\Pi_Z=0
}
\]

\[
\boxed{
\mathcal L_U\mathcal H+\nabla\Pi_H=-2\mathcal T
}
\]

with

\[
\mathcal Z=\mathcal H+2\tau\mathcal T.
\]

### CLOSED

- treating spatial homogeneity and time stationarity as one assumption;
- claiming Type-I decay automatically makes the scaling defect small;
- claiming the already extracted terminally nontrivial ancient solution is itself exactly backward self-similar.

### SURVIVES

- backward similarity-time extraction of a second limit;
- proving that every recurrent alpha-limit has zero scaling defect;
- proving sufficient compactness for time-translated similarity profiles;
- excluding periodic/DSS alpha-limits with existing or adapted Liouville theorems;
- if a formed nonzero defect persists, return to the generic dynamic critical-drift endpoint.

---

## 10. Next audit target: defect persistence in similarity time

Set

\[
s=-\log(-\tau),
\qquad
\xi=\frac{y}{\sqrt{-\tau}},
\]

and define the backward similarity field

\[
V(\xi,s)
:=\sqrt{-\tau}\,U(y,\tau).
\]

Then

\[
\partial_s V
\]

is the similarity-time representation of the parabolic scaling defect.

The next calculation should derive the exact rescaled equation and translate the inherited bounds into similarity variables.

The decisive fork will be:

\[
\boxed{
\begin{cases}
\partial_sV\to0
&\Rightarrow\text{stationary Leray alpha-limit, external Liouville route},\\
\partial_sV\not\to0
&\Rightarrow\text{formed dynamic/periodic/recurrent scaling defect persists.}
\end{cases}
}
\]

This is now a more precise continuation target than attempting Šverák's stationary `(-1)`-homogeneous classification directly on `U`.
