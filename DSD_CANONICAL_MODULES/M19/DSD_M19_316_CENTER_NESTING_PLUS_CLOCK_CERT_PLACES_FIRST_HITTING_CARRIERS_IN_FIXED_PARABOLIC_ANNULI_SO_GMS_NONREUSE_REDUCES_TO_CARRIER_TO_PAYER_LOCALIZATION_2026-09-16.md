# M19-316 — Center nesting plus CLOCK-CERT places first-hitting carriers in fixed parabolic annuli, so GMS nonreuse reduces to carrier-to-payer localization

**Date:** 2026-09-16  
**Status:** CONDITIONAL PHYSICAL-INCIDENCE THEOREM / ANNULAR FIRST-HITTING GEOMETRY / GMS LOCALIZATION REDUCTION

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Purpose

M19-315 isolates the GMS palinstrophy transfer obstruction as a scale-nonreuse / incidence problem.

M18-038--039 show that generic late payer events need an EVENT-ANNULAR / LOG-ALIGN bridge.

For the original first-hitting carriers, however, the physical singular history already provides stronger geometry. This module records that geometry precisely.

## 2. First-hitting scales

Let

\[
W_{j+1}=qW_j,
\qquad
r_j=\sqrt{\nu/W_j}.
\]

Then

\[
r_{j+1}=q^{-1/2}r_j.
\]

Let `t_j` and `X_j` denote the first-hitting time and center at level `W_j`.

## 3. Center nesting

M18-043 reimports the M5-399 dichotomy

\[
G_{center\ turnover}
\Longrightarrow
G_{center\ nesting}
\lor
S_{remote}^{formed}.
\]

On the center-nested branch there is one physical candidate singular center `X_*` satisfying

\[
\boxed{
|X_j-X_*|\le C_X r_j.
}
\]

The remote-satellite branch remains a separate global root and is not absorbed here.

## 4. Clock certificate

M18-044 defines

\[
\tau_j:=W_j(t_{j+1}-t_j)
\]

and shows that a bounded normalized strain ceiling gives a positive lower stage clock.

If the surviving upper-clock certificate also holds,

\[
0<\tau_-\le\tau_j\le\tau_+<\infty.
\]

Then, with blow-up time `T^*`,

\[
\Theta_j
:=
W_j(T^*-t_j)
=
\sum_{n=0}^\infty q^{-n}\tau_{j+n}.
\]

Therefore

\[
0<\Theta_-\le\Theta_j\le\Theta_+<\infty.
\]

Since `W_j=nu/r_j^2`,

\[
\boxed{
\frac{\Theta_-}{\nu}r_j^2
\le
T^*-t_j
\le
\frac{\Theta_+}{\nu}r_j^2.
}
\]

Thus every first-hitting time lies at parabolic distance comparable to `r_j` from the terminal singular time.

## 5. Fixed parabolic annulus placement

Combine Sections 3 and 4.

For the parabolic distance

\[
\rho_*(x,t)
:=
\max\{|x-X_*|,\sqrt{T^*-t}\},
\]

one has

\[
\boxed{
c_*r_j
\le
\rho_*(X_j,t_j)
\le
C_*r_j
}
\]

for fixed positive constants on the center-nested CLOCK-CERT corridor.

Hence the first-hitting carriers are automatically located in fixed-ratio parabolic annuli around the candidate singular point.

This is stronger than the generic EVENT-ANNULAR statement of M18-038 for arbitrary late payer events.

## 6. Stage-time annularity

Because

\[
t_{j+1}-t_j
=\frac{\tau_j}{W_j}
\asymp r_j^2,
\]

the entire first-hitting stage has the correct parabolic time thickness.

The stages are disjoint in physical time by construction.

Therefore, after a fixed enlargement, the family of stage-time windows is a bounded-overlap parabolic annular family in the temporal coordinate.

Spatial localization of a specific derivative payer inside the stage remains separate.

## 7. What this solves

On the retained corridor, no additional LOG-ALIGN theorem is needed merely to place the first-hitting carrier at the correct physical singular scale.

Thus the M19-315 nonreuse gate reduces from

\[
\text{time alignment}
+
\text{center alignment}
+
\text{payer localization}
\]

to

\[
\boxed{
\text{payer localization only},
}
\]

provided CLOCK-CERT and center nesting remain valid.

## 8. What remains open

The GMS epsilon floor is a nested-cylinder statement.

The first-hitting carrier is an annularly placed nontrivial vorticity structure.

It is not yet proved that the scale-invariant GMS payment is carried by a fixed palinstrophy amount in that same annular carrier.

The missing implication is

\[
\boxed{
\mathcal T_{GMS}^{carrier\to pal}:
H_V(r_j)\ge c_*
\Longrightarrow
r_j\int_{\mathcal A_j^{phys}}|D^2u|^2dxdt
\ge c_1>0
}
\]

for an annular/stage region `A_j^{phys}` tied to the first-hitting carrier, with bounded reuse.

This is a genuine localization theorem, not a clock theorem.

## 9. Branch firewall

The conclusion is conditional on

1. center nesting rather than formed remote satellite;
2. bounded normalized strain for the lower clock;
3. the upper stage-clock certificate or an explicit routing of its failure.

If any of these fail, the branch returns to the existing remote/Type-II/CLOCK-CERT root complex.

## 10. Strategic consequence

The highest-value GMS calculation is now local:

- subtract a Galilean/local mean velocity on the first-hitting annular carrier;
- use the first-hitting vorticity/enstrophy cap to control local velocity integrability;
- use a local pressure decomposition to separate nearby nonlinear pressure from harmonic far-field pressure;
- test whether the singular CKN/GMS floor forces a critical palinstrophy payment in the same stage.

If successful, M19-315's `r`-weighted Carleson packing becomes applicable without a separate LOG-ALIGN bridge.

---

\[
\boxed{\text{M19-316 COMPLETE; ON THE CENTER-NESTED CLOCK-CERT CORRIDOR, GMS NONREUSE IS NOW A CARRIER-TO-PAYER LOCALIZATION PROBLEM.}}
\]