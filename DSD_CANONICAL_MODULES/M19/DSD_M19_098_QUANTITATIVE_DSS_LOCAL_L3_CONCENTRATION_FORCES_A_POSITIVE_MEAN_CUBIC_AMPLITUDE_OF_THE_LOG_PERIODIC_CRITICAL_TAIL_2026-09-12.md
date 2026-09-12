# DSD M19-098 — Quantitative DSS local-L3 concentration forces a positive mean cubic amplitude of the log-periodic critical tail

Date: 2026-09-12

Status: **ACTIVE M19 CALCULATION / EXTERNAL QUANTITATIVE DSS CONCENTRATION MATCHED TO THE M5-566 LOG-PERIODIC TAIL / NONZERO DSS MUST CARRY A POSITIVE CUBIC-MASS SLOPE IN LOG RADIUS / CONSISTENT WITH, NOT CONTRADICTORY TO, THE CRITICAL TAIL / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. External input

Barker--Prange prove that if a nonzero backward `lambda`-DSS Navier--Stokes solution is smooth on `R3 x (-infinity,0)` and belongs continuously to `L^p(R3)` for some `p>=3`, then for a constant `M>1` and sufficiently large radii relative to `sqrt(-t)`,

\[
\int_{|x|<R}|u(x,t)|^3dx
\ge
c_M\log\left(\frac{R^2}{M^{802}|t|}\right),
\]

where

\[
\boxed{c_M:=\exp\bigl(-\exp(M^{1025})\bigr)>0.}
\]

This is a quantitative consequence conditional on existence of the nonzero DSS solution, not a general DSS nonexistence theorem.

---

## 2. Similarity variables

Use

\[
x=\sqrt{-t}\,y,
\qquad
u_{vel}(x,t)=(-t)^{-1/2}U(y,s),
\qquad
s=-\log(-t),
\]

where `u_vel` denotes the physical velocity `u` and is written this way only to avoid confusion with the viscosity symbol in plain-text rendering.

Then

\[
dx=(-t)^{3/2}dy,
\qquad
|u|^3=(-t)^{-3/2}|U|^3,
\]

and therefore

\[
\boxed{
\int_{|x|<R}|u(x,t)|^3dx
=
\int_{|y|<Y}|U(y,s)|^3dy,
\qquad
Y:=\frac{R}{\sqrt{-t}}.
}
\]

The quantitative lower bound becomes

\[
\boxed{
\int_{|y|<Y}|U(y,s)|^3dy
\ge
2c_M\log Y-O_M(1).
}
\]

---

## 3. M5-566 critical tail

An unresolved exact DSS survivor on the passive spectator lane has

\[
U(y,s)
=
\frac1r a(q,\omega)+O(r^{-3}),
\]

with

\[
q=\log r-\frac s2,
\qquad
\omega=\frac y{|y|},
\]

and

\[
\boxed{
a(q+L,\omega)=a(q,\omega),
\qquad
L=\log\lambda=S/2,
\qquad
a\not\equiv0.}
\]

---

## 4. Cubic mass slope

At leading order,

\[
|U|^3dy
\sim
|a(q,\omega)|^3\frac{dr}{r}d\omega.
\]

Define

\[
\boxed{
\mathcal A_3
:=
\int_0^L\int_{S^2}|a(q,\omega)|^3d\omega dq.
}
\]

Periodicity gives

\[
\boxed{
\int_{|y|<Y}|U(y,s)|^3dy
=
\frac{\mathcal A_3}{L}\log Y+O(1)
}
\]

as `Y -> infinity`.

Comparing the logarithmic slopes yields

\[
\boxed{
\frac{\mathcal A_3}{L}\ge2c_M,
}
\]

or equivalently

\[
\boxed{
\mathcal A_3\ge2c_ML.}
\]

Thus the nonzero periodic critical tail is quantitatively nontrivial in mean cubic mass.

---

## 5. Combine with M19-097

On the certified Pineau--Vicol one-slice application lane, M19-097 gives

\[
L\ge\frac{v_*}{A_*}.
\]

Consequently

\[
\boxed{
\mathcal A_3
\ge
2c_M\frac{v_*}{A_*}>0.}
\]

This is conditional on the combined hypotheses of the external DSS concentration theorem and the M19-096/097 Type-I/pressure gate.

---

## 6. No contradiction

A bounded nonzero periodic `1/r` datum naturally produces logarithmic `L3` growth. Hence the quantitative concentration theorem is structurally consistent with M5-566.

Also,

\[
\boxed{U\in L^q(\mathbb R^3),\ q>3}
\]

for a `1/r` far field does **not** permit importing a steady self-similar Liouville theorem into the time-periodic DSS equation. General backward DSS nonexistence for arbitrary `lambda` remains open in this class.

---

## 7. Refined DSS hard core

On the combined certified lane an unresolved DSS survivor must satisfy

\[
\boxed{
\begin{aligned}
&a(q+L)=a(q),\\
&L\ge L_*>0,\\
&a\not\equiv0,\\
&\frac1L\int_0^L\int_{S^2}|a|^3d\omega dq\ge2c_M.
\end{aligned}}
\]

Thus the remaining periodic branch has neither arbitrarily small period nor arbitrarily small mean critical amplitude.

---

## 8. Reference boundary

External quantitative concentration input:

- T. Barker and C. Prange, *Quantitative Regularity for the Navier--Stokes Equations Via Spatial Concentration*, Communications in Mathematical Physics 385 (2021), Corollary 1.1.

---

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
