# Dynamic local-variance gate against tight Type-II persistence

Date: 2026-08-19

Status: **DERIVED LOCAL ENERGY STRUCTURE + CONDITIONAL TYPE-II-TO-T REDUCTION / GLOBAL REGULARITY NOT PROVED**.

This note uses the dynamic first-hitting normalization to test whether a bounded-radius normalized core can remain shape-persistent while the scale-rate `a(s)` tends to zero.

---

## 1. Dynamic normalized local energy equation

In dynamic variables,

\[
\partial_sU
+a(U+y\cdot\nabla U)
+(U-c)\cdot\nabla U
=-\nabla P+\nu\Delta U,
\qquad \nabla\cdot U=0.
\]

Let

\[
e=\frac12|U|^2,
\qquad
b=U-c+a y.
\]

Since

\[
\nabla\cdot b=3a,
\]

the local energy equation is

\[
\boxed{
\partial_s e
+\nabla\cdot\left(be+PU-\nu\nabla e\right)
=a e-\nu|\nabla U|^2.
}
\]

Globally, when all fluxes vanish,

\[
\boxed{
\frac12\frac d{ds}\|U\|_2^2
=\frac a2\|U\|_2^2-\nu\|\nabla U\|_2^2.
}
\]

This is exactly the physical kinetic-energy identity rewritten in dynamic scaling.

---

## 2. Local moving-mean variance

Let `phi_R` be a smooth cutoff/weight concentrated on a normalized radius `R`, and choose the weighted mean

\[
\bar U_R
=\frac{\int\phi_RU}{\int\phi_R}.
\]

Write

\[
v=U-\bar U_R,
\qquad
V_R=\int\phi_R|v|^2,
\qquad
D_R=\int\phi_R|\nabla U|^2.
\]

The derivative of the weighted mean does not contribute directly to the variance because

\[
\int\phi_Rv=0.
\]

After inserting the local energy equation and collecting the cutoff, pressure, relative-advection, center-motion and scale-drift shell terms, the variance equation has the exact typed form

\[
\boxed{
\frac12V_R'
+\nu D_R
=\frac a2V_R
+\mathcal F_R,
}
\]

where `F_R` is a shell/material-turnover functional supported where the cutoff changes. Its components are ordinary local-energy fluxes and the scale-drift shell flux `a y`.

This note treats a large `F_R` as the existing bounded-radius transport branch `T*`.

---

## 3. Weighted Poincare coercivity

For the weighted-mean-zero field `v`,

\[
\boxed{
V_R\le C_P R^2 D_R,
}
\]

for a cutoff-dependent fixed Poincare constant `C_P`.

Thus a spatially tight velocity-variance core has a definite viscous loss rate.

---

## 4. Stage-length bound under low turnover

Let `I=[s_0,s_1]` be a geometric first-hitting stage with

\[
\int_I a(s)ds=A_q=\frac12\log q.
\]

Suppose the normalized core is persistent in the sense

\[
0<V_-\le V_R(s)\le V_+<\infty
\]

on `I`, and its endpoint variance changes by at most

\[
|V_R(s_1)-V_R(s_0)|\le\kappa_V.
\]

Assume also that shell/material turnover is subdominant, for example

\[
\left|\int_I\mathcal F_Rds\right|
\le\eta\nu\int_I D_Rds+F_0,
\qquad 0\le\eta<1.
\]

Integrating the variance equation and using Poincare gives

\[
(1-\eta)\nu\frac{V_-}{C_PR^2}|I|
\le
\frac12A_qV_+
+F_0+\frac12\kappa_V.
\]

Hence

\[
\boxed{
L_I=|I|
\le
\frac{C_PR^2}{(1-\eta)\nu V_-}
\left(
\frac12A_qV_+ +F_0+\frac12\kappa_V
\right).
}
\]

For a genuinely recurrent tight core with uniformly controlled ratios and negligible shell flux, this simplifies schematically to

\[
\boxed{
L_I\lesssim \frac{R^2}{\nu}.
}
\]

---

## 5. Lower bound on the average scale-rate

Since

\[
\bar a_I=\frac{A_q}{L_I},
\]

the previous estimate yields

\[
\boxed{
\bar a_I\gtrsim \frac{\nu}{R^2}
}
\]

up to fixed persistence/flux constants.

Therefore a bounded-radius, shape-persistent, low-turnover core cannot have

\[
\bar a_I\to0.
\]

In particular, the dynamically normalized Type-II scenario `a -> 0` must activate at least one of:

1. increasing normalized core radius `R -> infinity` (`T`);
2. order-one shell/material flux (`T`);
3. loss of recurrent local variance;
4. derivative/high-frequency escape needed to invalidate the compact-core assumptions (`H`).

---

## 6. Relation to the frozen-profile Liouville gate

This estimate gives a quantitative route to the same qualitative conclusion as the steady-profile Liouville argument, but before taking an exact stationary limit.

A tight, low-turnover, recurrent core has an average scale-rate bounded away from zero. Hence any compact limit of such stages is pushed toward a positive-rate backward self-similar or recurrent rescaled dynamics rather than a zero-rate steady Type-II profile.

If the full profile additionally freezes and the limiting positive scale-rate converges, the existing backward self-similar Liouville theorems apply under their integrability/local-energy hypotheses.

If the scale-rate or profile does not converge, the survivor is explicitly a scale/profile-turnover branch and must be handled by the finite-Hermite/projective action bookkeeping.

---

## 7. Current significance

The shape-persistence loophole is now split into:

\[
\boxed{
\text{tight + low turnover}
\Longrightarrow
\bar a\gtrsim\nu/R^2,
}
\]

while

\[
\boxed{
\bar a\to0
\Longrightarrow
T\text{ or }H\text{ or loss of recurrence}.
}
\]

Thus genuinely persistent Type-II behavior cannot remain both spatially tight and transport-inactive.

Status: **TIGHT LOW-TURNOVER TYPE-II PERSISTENCE REDUCED TO T/H; POSITIVE-RATE COMPACT RECURRENCE / FINITE-MODE PHASE MOTION REMAINS OPEN.**