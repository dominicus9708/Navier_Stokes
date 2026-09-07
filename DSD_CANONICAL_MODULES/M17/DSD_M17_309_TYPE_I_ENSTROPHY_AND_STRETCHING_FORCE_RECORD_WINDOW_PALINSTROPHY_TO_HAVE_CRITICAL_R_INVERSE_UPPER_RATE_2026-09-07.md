# DSD M17-309 — Type-I enstrophy and stretching force each record window to carry at most the critical `R^-1` ancestral palinstrophy rate

Date: 2026-09-07  
Canonical ID: **M17-309**

Status: **RECORD-WINDOW SATURATION GATE / M17-307 PROVES THAT AN ORDER-ONE SECOND-GENERATION PALINSTROPHY PAYMENT COSTS ONLY `R_m^-1` IN THE FIRST ANCIENT ELEMENT. M17-308 SHOWS THAT THIS IS THE EXACT SUPERCRITICAL SCALING EXPONENT. THE PRESENT MODULE ADDS A DYNAMICAL UPPER BOUND: M5-475/477 GIVE `E(t)=||Omega(t)||_2^2 <= C(-t)^-1/2` AND STRETCHING PRODUCTION `|Q(t)|<=C(-t)^-3/2`. INTEGRATING THE ENSTROPHY IDENTITY OVER ANY GEOMETRIC BACKWARD WINDOW `[-bT,-aT]` YIELDS `int P(t)dt <= C T^-1/2`. WITH `T=R^2`, THIS IS EXACTLY `C/R`. AFTER M5-478 BLOW-DOWN, EVERY FIXED SECOND-GENERATION TIME ANNULUS HAS UNIFORM `O(1)` PALINSTROPHY. THEREFORE A FIXED DESCENDANT PAYMENT DOES NOT MERELY FIT THE FINITE ANCESTRAL BUDGET; IT SATURATES THE NATURAL TYPE-I PALINSTROPHY RATE ON THAT RECORD WINDOW. THE CRITICAL WEIGHTED WINDOW QUANTITY `R int P dt` IS SCALE-INVARIANT AND MAY REMAIN ORDER ONE ON INFINITELY MANY RECORDS, SO NO SUMMATION CONTRADICTION FOLLOWS. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. First ancient enstrophy identity

Let

\[
E(t):=\|\Omega(t)\|_2^2,
\qquad
P(t):=\|\nabla\Omega(t)\|_2^2.
\]

For the first marked ancient element,

\[
\boxed{
\frac12E'(t)+P(t)=Q(t),
}
\]

where

\[
Q(t):=\int S\Omega\cdot\Omega\,dx.
\]

M5-475/477 give, for sufficiently large negative time,

\[
\boxed{
E(t)\le C(-t)^{-1/2},
}
\]

and

\[
\boxed{
|Q(t)|\le C(-t)^{-3/2}.
}
\]

---

## 2. Geometric backward window

Fix

\[
0<a<b<\infty
\]

and for large `T` define

\[
\boxed{
J_T:=[-bT,-aT].
}
\]

Integrate the enstrophy identity from `-bT` to `-aT`:

\[
\int_{J_T}P(t)dt
=
\int_{J_T}Q(t)dt
-
\frac12\left[E(-aT)-E(-bT)\right].
\]

Since the left side is nonnegative,

\[
\int_{J_T}P(t)dt
\le
\int_{J_T}|Q(t)|dt
+
\frac12E(-aT)
+
\frac12E(-bT).
\]

The endpoint terms obey

\[
E(-aT)+E(-bT)
\le C_{a,b}T^{-1/2}.
\]

Also

\[
\int_{-bT}^{-aT}(-t)^{-3/2}dt
=
2\left((aT)^{-1/2}-(bT)^{-1/2}\right)
\le C_{a,b}T^{-1/2}.
\]

Therefore

\[
\boxed{
\int_{J_T}P(t)dt
\le C_{a,b}T^{-1/2}.
}
\]

This is a dynamical rate, not merely a consequence of global integrability.

---

## 3. Convert to record radius

Set

\[
T=R^2.
\]

Then

\[
\boxed{
\int_{-bR^2}^{-aR^2}
\|\nabla\Omega(t)\|_2^2dt
\le
\frac{C_{a,b}}{R}.
}
\]

Thus the `R^-1` ancestry factor found in M17-307 is not only the exact scaling conversion; it is also the **natural Type-I upper rate** of the first ancient palinstrophy on a record window.

---

## 4. Uniform second-generation fixed-window palinstrophy

Use the record blow-down

\[
\Omega_R(y,s)=R^2\Omega(Ry,R^2s).
\]

For the fixed normalized interval

\[
I=[-b,-a],
\]

M17-308 gives

\[
\int_I\|\nabla\Omega_R(s)\|_2^2ds
=R
\int_{-bR^2}^{-aR^2}
\|\nabla\Omega(t)\|_2^2dt.
\]

Insert Section 3:

\[
\boxed{
\int_I\|\nabla\Omega_R(s)\|_2^2ds
\le C_{a,b}.
}
\]

Hence every record cell has a **uniform fixed-window palinstrophy ceiling**.

This is consistent with the local smooth compactness of M5-478 but is stronger in bookkeeping: the constant is obtained directly from the first-generation Type-I enstrophy identity and record scaling.

---

## 5. Spacetime enstrophy is also uniformly bounded on fixed record windows

The Type-I enstrophy rate gives

\[
\int_{-bR^2}^{-aR^2}E(t)dt
\le
C\int_{aR^2}^{bR^2}\tau^{-1/2}d\tau
\le C_{a,b}R.
\]

Since

\[
\int_I\|\Omega_R(s)\|_2^2ds
=R^{-1}
\int_{-bR^2}^{-aR^2}E(t)dt,
\]

we obtain

\[
\boxed{
\int_I\|\Omega_R(s)\|_2^2ds
\le C_{a,b}.
}
\]

Thus both normalized enstrophy and normalized palinstrophy remain order at most one on every fixed second-generation record window.

---

## 6. A fixed descendant payment forces critical ancestral saturation

Suppose on an infinite record subsequence `R_m` one has a fixed lower payment

\[
\boxed{
\int_I\|\nabla\Omega_{R_m}(s)\|_2^2ds
\ge c_*>0.
}
\]

Scaling back gives

\[
\boxed{
\int_{-bR_m^2}^{-aR_m^2}
\|\nabla\Omega(t)\|_2^2dt
\ge
\frac{c_*}{R_m}.
}
\]

Combining with Section 3,

\[
\boxed{
\frac{c_*}{R_m}
\le
\int_{J_{R_m}}P(t)dt
\le
\frac{C_*}{R_m}.
}
\]

Thus repeated order-one descendant payments force the first ancient palinstrophy to **saturate the exact critical `R^-1` record-window rate**.

---

## 7. Define the record-critical palinstrophy activity

Define

\[
\boxed{
\Pi_R
:=
R
\int_{-bR^2}^{-aR^2}
P(t)dt.
}
\]

Equivalently,

\[
\boxed{
\Pi_R
=
\int_{-b}^{-a}
\|\nabla\Omega_R(s)\|_2^2ds.
}
\]

Hence `Pi_R` is exactly record-scale invariant.

Sections 3--6 give

\[
0\le\Pi_R\le C_{a,b},
\]

and an order-one descendant payer gives

\[
\Pi_{R_m}\ge c_*>0.
\]

This is the correct critical observable replacing an attempted unweighted sum of descendant palinstrophy.

---

## 8. Why critical saturation is not a contradiction

The first-generation global finite palinstrophy is

\[
\sum_m
\int_{J_{R_m}}P(t)dt
<\infty
\]

for finite-overlap geometric record windows.

But if

\[
\int_{J_{R_m}}P(t)dt
\asymp R_m^{-1},
\]

then

\[
\sum_mR_m^{-1}<\infty
\]

because `R_m` grows geometrically.

Therefore

\[
\boxed{
\Pi_{R_m}\asymp1
\text{ on infinitely many records}
}
\]

is fully compatible with M5-477.

The finite budget and critical recurrence coexist because the physical cost of each older record decays geometrically.

---

## 9. Consequence for the next proof target

The palinstrophy lane has now been reduced to a sharp endpoint:

\[
\boxed{
\text{repeated second-generation payment}
\Longrightarrow
\text{critical record-window saturation }\Pi_{R_m}\gtrsim1.
}
\]

A further contradiction cannot come from summing `Pi_R` as a positive resource.

It must instead use structure of the saturated record cells, for example:

1. critical `L_t^2L_x^3` vorticity/strain transfer;
2. velocity `L3` endpoint structure;
3. CE-H critical `kappa` coefficient rigidity;
4. a signed critical flux/production relation;
5. strict scale descent or nodal forcing.

---

## 10. DSD audit

- The palinstrophy upper rate uses the exact enstrophy identity and the M5-477 stretching bound.
- Endpoint enstrophy terms are retained; no monotonicity of enstrophy is assumed.
- The `R^-1` rate is both dimensionally and dynamically justified.
- Uniform second-generation palinstrophy is not confused with a globally finite sum across generations.
- Critical saturation is not called a contradiction.
- No external theorem is used.
- Global regularity remains unproved.

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
