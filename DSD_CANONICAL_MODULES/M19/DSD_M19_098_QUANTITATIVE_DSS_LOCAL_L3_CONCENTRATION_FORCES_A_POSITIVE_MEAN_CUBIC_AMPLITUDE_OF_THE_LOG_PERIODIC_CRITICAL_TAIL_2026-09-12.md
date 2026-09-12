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
\qquad
c_M:=\exp\bigl(-\exp(M^{1025})\bigr)>0.
\]

This is conditional on existence of the nonzero DSS solution; it is not a general nonexistence theorem.

---

## 2. Similarity variables

Set

\[
x=\sqrt{-t}\,y,
\qquad
s=-\log(-t),
\]

and use the physical velocity relation

\[
u(x,t)=(-t)^{-1/2}U(y,s).
\]

Here the letter in the last formula denotes the velocity `u`, not viscosity.

Then

\[
dx=(-t)^{3/2}dy,
\qquad
|u|^3=(-t)^{-3/2}|U|^3,
\]

so

\[
\boxed{
\int_{|x|<R}|u(x,t)|^3dx
=
\int_{|y|<Y}|U(y,s)|^3dy,
\qquad
Y:=\frac{R}{\sqrt{-t}}.
}
\]

Therefore

\[
\boxed{
\int_{|y|<Y}|U(y,s)|^3dy
\ge
2c_M\log Y-O_M(1).
}
\]

---

## 3. M5-566 critical tail

An unresolved exact DSS survivor has

\[
U(y,s)
=
\frac1r a(q,\omega)+O(r^{-3}),
\qquad
q=\log r-\frac s2,
\]

with

\[
\boxed{
a(q+L,\omega)=a(q,\omega),
\qquad
L=\log\lambda=S/2,
\qquad
a\not\equiv0.}
\]

Define

\[
\boxed{
\mathcal A_3
:=
\int_0^L\int_{S^2}|a(q,\omega)|^3d\omega dq.
}
\]

Since `dr/r=dq`, periodicity gives

\[
\boxed{
\int_{|y|<Y}|U(y,s)|^3dy
=
\frac{\mathcal A_3}{L}\log Y+O(1).
}
\]

Comparison with the quantitative DSS concentration slope yields

\[
\boxed{
\frac{\mathcal A_3}{L}\ge2c_M,
\qquad
\mathcal A_3\ge2c_ML.}
\]

---

## 4. Combine with M19-097

On the certified Pineau--Vicol one-slice application lane,

\[
L\ge\frac{v_*}{A_*}.
\]

Hence

\[
\boxed{
\mathcal A_3
\ge
2c_M\frac{v_*}{A_*}>0.}
\]

Thus the remaining periodic branch has neither arbitrarily small period nor arbitrarily small mean critical amplitude.

---

## 5. No contradiction

A bounded nonzero periodic `1/r` datum naturally produces logarithmic `L3` growth, so the external quantitative concentration theorem is consistent with M5-566.

Also a `1/r` far field belongs to `L^q(R3)` for `q>3`, but this does **not** permit importing steady self-similar Liouville theorems into the time-periodic DSS equation. General backward DSS nonexistence for arbitrary `lambda` remains open in this class.

---

## 6. Reference boundary

External quantitative concentration input:

- T. Barker and C. Prange, *Quantitative Regularity for the Navier--Stokes Equations Via Spatial Concentration*, Communications in Mathematical Physics 385 (2021), Corollary 1.1.

---

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
