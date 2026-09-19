# M21-009 — A robust projective-alignment separator is not free: finite-thickness K contrast forces commutator-gradient cost, while persistent exact alignment requires transverse pressure-diffusion cancellation

Date: 2026-09-20  
Canonical ID: **M21-009**  
Status: **PROJECTIVE-ALIGNMENT SEPARATOR REDUCTION / THE M21-008 K-APPROX-ZERO SEPARATOR IS MEASURED COORDINATE-FREELY BY C=[Sigma_F,Q] / IF HIGH-K AND LOW-K POPULATIONS OCCUPY FIXED POSITIVE FRACTIONS OF ONE UNIFORMLY POINCARE CELL, POINCARE FORCES A FIXED GRADIENT PACKET OF C, WHICH REDUCES TO STRAIN-GRADIENT PLUS VORTICITY-DIRECTION-GRADIENT ACTIVITY / IF THE LOW-K LAYER HAS VANISHING THICKNESS IT IS AN INTERFACE MICROCARRIER RATHER THAN A BULK SEPARATOR / IF EXACT ALIGNMENT K=0 PERSISTS MATERIALLY, THE M20-006 EVOLUTION FORCES TRANSVERSE PRESSURE-HESSIAN, STRAIN-DIFFUSION, AND VISCOUS-PROJECTIVE TERMS TO CANCEL / THUS K-SEPARATION RETURNS TO EXISTING ANALYTIC OR INTERFACE/TURNOVER FIREWALLS / GLOBAL REGULARITY UNPROVED**

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Coordinate-free separator variable

Define

\[
\boxed{
C:=[\Sigma_F,Q].
}
\]

Then

\[
\boxed{
K=\|C\|_F^2.
}
\]

Thus projective alignment is

\[
K=0
\quad\Longleftrightarrow\quad
C=0,
\]

which means the vorticity direction lies in a strain eigenspace.

No eigenvector choice is required.

## 2. Robust finite-thickness separator hypothesis

Work in a connected normalized cell \(\mathcal C\) with a uniform Poincare inequality.

Assume two measurable subsets:

\[
A_H,\quad A_L\subset\mathcal C,
\]

with fixed positive cell measures and

\[
K\ge k_H>0
\quad\text{on }A_H,
\]

\[
K\le k_L<k_H
\quad\text{on }A_L.
\]

Then

\[
|C|\ge\sqrt{k_H}
\]

on \(A_H\), while

\[
|C|\le\sqrt{k_L}
\]

on \(A_L\).

## 3. Two-population variance lower bound

The scalar field

\[
c:=|C|
\]

has two separated value populations.

Therefore

\[
\boxed{
\int_{\mathcal C}
|c-\bar c_{\mathcal C}|^2
\ge
v_C>0.
}
\]

Poincare gives

\[
\boxed{
\int_{\mathcal C}
|\nabla c|^2
\ge
\frac{v_C}{C_P}
=:g_C>0.
}
\]

Since

\[
|\nabla|C||\le|\nabla C|,
\]

we get

\[
\boxed{
\int_{\mathcal C}
|\nabla C|^2
\ge
g_C>0.
}
\]

A robust bulk alignment separator therefore has fixed normalized derivative cost.

## 4. Differentiate the commutator

Because

\[
C=[\Sigma_F,Q],
\]

we have

\[
\boxed{
\nabla C
=
[\nabla\Sigma_F,Q]
+
[\Sigma_F,\nabla Q].
}
\]

Also

\[
Q=\xi\otimes\xi,
\]

so

\[
\nabla Q
=
\nabla\xi\otimes\xi
+
\xi\otimes\nabla\xi.
\]

Hence

\[
|\nabla Q|
\le
C|\nabla\xi|.
\]

Therefore

\[
\boxed{
|\nabla C|^2
\le
C
\left(
|\nabla\Sigma_F|^2
+
|\Sigma_F|^2|\nabla\xi|^2
\right).
}
\]

## 5. Compact corridor reduction

On the M21 corridor,

\[
|\Sigma_F|\le M_\Sigma.
\]

Thus

\[
\boxed{
g_C
\le
C
\int_{\mathcal C}
\left(
|\nabla\Sigma_F|^2
+
|\nabla\xi|^2
\right).
}
\]

If vorticity amplitude is bounded below on the separator cell,

\[
E\ge e_*>0,
\]

then

\[
|\nabla\xi|^2
\le
e_*^{-1}E|\nabla\xi|^2.
\]

The second term is controlled by the direction-gradient part of palinstrophy.

The first is a strain-gradient / first-vorticity-derivative channel.

Thus

\[
\boxed{
\text{robust bulk K-separator}
\Longrightarrow
P_{\rm pal/strain-grad}.
}
\]

## 6. Low-vorticity escape

If no positive lower bound

\[
E\ge e_*
\]

holds through the separator, the direction-gradient estimate degenerates.

Then the separator has entered

\[
\boxed{
P_{E\text{-bottleneck}}.
}
\]

If this low-vorticity layer has robust thickness and Poincare geometry, M17-447 returns it to a palinstrophy packet.

Otherwise it is a thin-neck / vanishing-measure / geometry-decompactification branch.

## 7. Vanishing-thickness K layer

A projective-alignment set

\[
K\approx0
\]

may have vanishing transverse measure.

Then the two-population variance constant \(v_C\) need not remain fixed.

Such a separator is not a bulk \(K\)-phase.

It is an interface microcarrier.

Therefore retain

\[
\boxed{
P_{K\text{-microinterface}}
}
\]

rather than claiming a bulk gradient floor.

This is analogous to the nodal-volume firewall: a codimension-lower set may organize topology without carrying fixed volume charge.

## 8. Exact material evolution at alignment

M20-006 gives

\[
P_\xi^\perp D_ts_\perp
=
-2\gamma s_\perp
-
h_\perp
+
\nu P_\xi^\perp(\Delta S)\xi
+
P_\xi^\perp(S-\gamma I)v_\perp,
\]

where

\[
s_\perp=P_\xi^\perp S\xi,
\]

and

\[
h_\perp=P_\xi^\perp(\nabla^2p)\xi.
\]

At exact projective alignment,

\[
s_\perp=0.
\]

Hence

\[
\boxed{
P_\xi^\perp D_ts_\perp
=
-h_\perp
+
\nu P_\xi^\perp(\Delta S)\xi
+
P_\xi^\perp(S-\gamma I)v_\perp.
}
\]

## 9. Persistent exact alignment requires cancellation

If a material element remains exactly aligned over a time interval, then

\[
s_\perp\equiv0
\]

and therefore

\[
P_\xi^\perp D_ts_\perp=0.
\]

Thus

\[
\boxed{
h_\perp
=
\nu P_\xi^\perp(\Delta S)\xi
+
P_\xi^\perp(S-\gamma I)v_\perp.
}
\]

Therefore persistent alignment is not dynamically free.

It requires exact cancellation among:

- transverse pressure Hessian;
- strain diffusion;
- viscous projective motion.

These are precisely the already typed M20/M21 analytic channels.

## 10. Near-alignment persistence

If

\[
|s_\perp|\le\varepsilon
\]

for a fixed material interval while the right-hand side of Section 8 has a transverse floor \(f_*>0\), then alignment cannot persist for arbitrarily long normalized time.

A quantitative persistence theorem would require a bound on the material derivative of the forcing terms.

Without that high-jet control, the correct branch is

\[
\boxed{
P_{K\text{-turnover}}
:
\text{rapid projective-alignment entry/exit}.
}
\]

Thus near-alignment survival splits into forcing cancellation or temporal turnover.

## 11. Updated K-separator fork

The M21-008 branch

\[
P_{K\text{-separator}}
\]

reduces to

\[
\boxed{
P_{K\text{-separator}}
\Longrightarrow
P_{\rm pal/strain-grad}
\lor
P_{E\text{-bottleneck}}
\lor
P_{K\text{-microinterface}}
\lor
P_{\rm analytic-cancel}
\lor
P_{K\text{-turnover}}.
}
\]

No new unsigned projective bulk payer remains.

## 12. Structural consequence for the anti-correlation branch

Combining M21-008--009,

\[
C_{\Gamma K}^{-}
\]

can survive without immediately returning to existing analytic derivatives only by using:

- low-vorticity/thin-neck geometry;
- vanishing-measure projective alignment interfaces;
- q/angular phase localization;
- rapid temporal turnover.

Thus the branch has moved from a bulk covariance problem to an interface/localization/occupancy problem.

## 13. Ancestry status

A single snapshot gradient packet is still ancestry-summable under existing palinstrophy/raw-derivative weights.

A contradiction requires persistence, multiplicity, or nonreuse.

Therefore M21-009 does not close the branch.

It identifies the exact geometry that must be shown recurrent or persistent before existing finite derivative budgets become effective.

## 14. Next target

The most global remaining escape is

\[
P_{\rm phase-localization}.
\]

M21-010 should quantify whether the extensional and compressive-projective populations can remain separated in q/angular position throughout the compact depth corridor without generating:

- repeated transition zones;
- q-translation turnover;
- angular patch multiplicity;
- or vanishing occupancy.

This is the finite-depth analogue of the earlier recurrence-versus-interface multiplicity problem.

\[
\boxed{\text{M21-009 COMPLETE; A ROBUST PROJECTIVE-ALIGNMENT SEPARATOR RETURNS TO STRAIN/DIRECTION GRADIENT COST, LOW-VORTICITY OR MICROINTERFACE GEOMETRY, OR PRESSURE-DIFFUSION/TURNOVER COMPENSATION.}}
\]

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
