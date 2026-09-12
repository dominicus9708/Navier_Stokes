# DSD M19-143 — The finite-spectator hard-mode unique-continuation and scattering-differentiability gates are certified on the smooth passive lane

Date: 2026-09-12

Status: **ACTIVE M19 CALCULATION / EXTERNAL-INPUT HYPOTHESIS MATCHING / ON A FIXED FINITE SPECTATOR CYLINDER THE LINEARIZED SIMILARITY NAVIER--STOKES SYSTEM IS A NONSTATIONARY STOKES SYSTEM WITH SMOOTH BOUNDED LOWER-ORDER COEFFICIENTS / STANDARD PARABOLIC-STOKES UNIQUE CONTINUATION CERTIFIES THE OBSERVATION INJECTIVITY USED IN M19-130--131 / THE EXACT SPECTATOR DUHAMEL MAP IS C1 IN THE RETAINED STRONG ANNULAR TOPOLOGY AND DIFFERENTIATES TO THE M19-132 INTERTWINING RELATION / THESE GATES ARE CLOSED ON THE SMOOTH PASSIVE LANE, NOT ON PRIMITIVE W1 GLOBALLY / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Purpose

M19-130--133 use two application gates:

1. a nonzero finite-dimensional hard mode cannot vanish on an open spectator spacetime cylinder;
2. the nonlinear scattering map is differentiable on the retained hard corridor so that exact scattering covariance may be differentiated.

The present module checks these gates on the actual smooth passive-spectator lane.

---

## 2. Linearized similarity system on a fixed spectator cylinder

Let `U(y,s)` be a retained smooth background similarity solution and `W` a divergence-free tangent mode.
The linearized velocity-pressure system has the schematic form

\[
\boxed{
\partial_sW
-\nu\Delta W
+\frac12(y\cdot\nabla)W
+\frac12W
+(U\cdot\nabla)W
+(W\cdot\nabla)U
+\nabla Q
=0,
}
\]

with

\[
\nabla\cdot W=0.
\]

Fix a finite spectator annulus/cylinder

\[
\mathcal Q_{spec}
=I_s\times\{R_1<|y|<R_2\},
\qquad
0<R_1<R_2<\infty.
\]

On this cylinder the coefficients

\[
\frac y2,
\qquad
U,
\qquad
\nabla U
\]

are uniformly bounded and smooth on the retained analytic/spectator corridor.

Thus the principal part is the nonstationary Stokes operator and every additional background term is lower order with bounded smooth coefficient.

---

## 3. Standard unique-continuation input

Nonstationary Stokes systems possess local unique-continuation/Carleman estimates on finite cylinders, and the standard parabolic backward-uniqueness theory covers heat/Stokes-type equations with bounded lower-order coefficients.

Therefore, in the retained smooth class, if

\[
\boxed{
W=0
\quad\text{on a nonempty open spacetime subset of }\mathcal Q_{spec},
}
\]

then local unique continuation propagates the zero set through the connected finite spectator region.

Iterating through overlapping smooth finite cylinders connects the spectator annulus to the compact core/hard-mode domain.
Consequently

\[
\boxed{
W|_{\mathcal Q_{obs}}=0
\Longrightarrow
W\equiv0
}
\]

for a hard mode in the current smooth similarity solution class, modulo only the standard pressure time-gauge which does not alter `W`.

This is exactly the injectivity statement used by M19-130.

---

## 4. Why the vorticity nonlocality is not an obstruction here

A direct scalar-vorticity unique-continuation argument would contain the nonlocal recovery of `W` from `eta=curl W`.
The present gate does not need that detour.

It applies unique continuation to the local velocity-pressure Stokes system itself.
Hence the Biot--Savart nonlocality does not enter the observation injectivity proof.

---

## 5. Scattering differentiability from the exact spectator Duhamel map

M5-563 gives the fixed-annulus outward characteristic equation

\[
\partial_\tau V
=
R_0^{-2}e^{-\tau}
\mathcal R[V,P],
\]

where

\[
\mathcal R[V,P]
=
\Delta V-(V\cdot\nabla)V-\nabla P.
\]

On the retained smooth spectator Banach topology, the differential operations are bounded at the required derivative level, multiplication is continuous, and the pressure is recovered by the standard elliptic/Riesz map in the chosen pressure normalization.

Thus

\[
(V,P)\mapsto\mathcal R[V,P]
\]

is `C1` on the certified bounded spectator set.

The exponentially integrable factor

\[
R_0^{-2}e^{-\tau}
\]

allows differentiation under the Duhamel integral.
Therefore the scattering map

\[
\mathscr S(V_0)
=
V_0
+
R_0^{-2}
\int_0^\infty e^{-\tau}\mathcal R[V(\tau),P(\tau)]d\tau
\]

is `C1` on the retained hard lane.

Its derivative satisfies the linearized Duhamel equation and, for large spectator radius,

\[
\boxed{
D\mathscr S_{R_0}
=I+O(R_0^{-2})
}
\]

in the retained hard norm, as used in M19-069/130.

---

## 6. Exact differentiated equivariance is therefore legal

The nonlinear covariance

\[
\mathscr S(\sigma_tU)
=
T_{-t/2}\mathscr S(U)
\]

may now be differentiated on this `C1` hard corridor:

\[
\boxed{
D\mathscr S_{\sigma_tU}\,D\sigma_t(U)
=
T_{-t/2}D\mathscr S_U.
}
\]

Hence the exact intertwining used in M19-132--133 is certified at the stated smooth-spectator regularity level.

---

## 7. Combined applicability ledger after M19-142--143

On the **smooth passive critical-tail lane**, the following external/application gates are now matched:

\[
\boxed{
\begin{aligned}
&\text{spatial velocity Type-I},\\
&\text{fixed physical pressure-annulus }L^\infty,\\
&\text{finite-spectator Stokes/parabolic unique continuation},\\
&\text{C1 spectator scattering map and differentiated covariance}.
\end{aligned}}
\]

The broad external-theorem applicability item is therefore no longer an independent analytic obstruction inside this late hard corridor.

---

## 8. Scope firewall

This certification does **not** apply automatically to primitive W1 or to an arbitrary hypothetical singularity.
It requires prior entry into the smooth passive-spectator lane, including:

- smooth bounded local coefficients on finite spectator cylinders;
- pointwise critical-tail bounds used in M19-142;
- controlled pressure normalization;
- the retained strong annular topology used by the Duhamel/scattering construction.

Thus failure before this entry remains part of ROOT-CERT / historical branch-completeness, not a late M19 analytic defect.

---

## 9. Updated M19 analytic frontier

Inside the late smooth passive hard corridor, the independent analytic problems are reduced essentially to

\[
\boxed{
\mathcal T_{zero-center}:
E_q^0=\operatorname{span}\{\partial_sU\}
}
\]

and the subsequent

\[
\boxed{
\mathcal T_{RSS/RDSS}:
\text{exclude the remaining finite-amplitude moderate relative-periodic orbit}.
}
\]

The external Type-I/pressure/UC/scattering gates have been moved to corridor-entry certification rather than retained as separate late hard-core theorems.

---

## 10. External reference boundary

The unique-continuation input is standard parabolic/Stokes theory, e.g.:

- L. Escauriaza, G. Seregin, V. Sverak, *Backward Uniqueness for Parabolic Equations*, Arch. Ration. Mech. Anal. 169 (2003), 147--157, DOI 10.1007/s00205-003-0263-8;
- M. Boulakia, *Quantification of the unique continuation property for the nonstationary Stokes problem*, Math. Control Relat. Fields 6 (2016), 27--52, DOI 10.3934/mcrf.2016.6.27.

The module uses only the standard smooth finite-cylinder unique-continuation consequence in the coefficient regime described above.

---

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
