# DSD M19-098 — Quantitative DSS local-L3 concentration forces a positive mean cubic amplitude of the log-periodic critical tail

Date: 2026-09-12

Status: **ACTIVE M19 CALCULATION / EXTERNAL QUANTITATIVE DSS CONCENTRATION MATCHED TO THE M5-566 LOG-PERIODIC TAIL / NONZERO DSS MUST CARRY A POSITIVE CUBIC-MASS SLOPE IN LOG RADIUS / CONSISTENT WITH, NOT CONTRADICTORY TO, THE CRITICAL TAIL / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. External input

A quantitative regularity theorem of Barker--Prange and its DSS corollary show the following qualitative structure.

If a nonzero backward `lambda`-DSS Navier--Stokes solution is smooth on `R3 x (-infinity,0)` and belongs continuously to `L^p(R3)` for some `p>=3`, then it obeys a Type-I bound and there exists a constant `M>1` such that, for sufficiently large radii relative to `sqrt(-t)`,

\[
\int_{|x|<R}|u(x,t)|^3dx
\ge
c_M
\log\left(\frac{R^2}{M^{802}|t|}\right),
\]

where

\[
\boxed{
c_M:=\exp\bigl(-\exp(M^{1025})\bigr)>0.
}
\]

The explicit constant is extremely small but positive.

This result is conditional on existence of the nonzero DSS solution; it is not a nonexistence theorem.

---

## 2. Convert to similarity variables

Use

\[
x=\sqrt{-t}\,y,
\qquad
u(x,t)=(-t)^{-1/2}U(y,s),
\qquad
s=-\log(-t).
\]

Here `u(x,t)` is the velocity field; in ordinary notation the displayed middle relation is

\[
u(x,t)=(-t)^{-1/2}U(y,s).
\]

Then

\[
dx=(-t)^{3/2}dy,
\qquad
|u|^3=(-t)^{-3/2}|U|^3,
\]

so the cubic integral is scale invariant:

\[
\boxed{
\int_{|x|<R}|u(x,t)|^3dx
=
\int_{|y|<Y}|U(y,s)|^3dy,
\qquad
Y:=\frac{R}{\sqrt{-t}}.
}
\]

Therefore the DSS concentration lower bound becomes

\[
\boxed{
\int_{|y|<Y}|U(y,s)|^3dy
\ge
c_M\log\left(\frac{Y^2}{M^{802}}\right)
=
2c_M\log Y-O_M(1).
}
\]

---

## 3. Insert the M5-566 critical tail

M5-566 shows that an unresolved exact DSS survivor on the passive spectator lane must have

\[
U(y,s)
=
\frac1r
 a\left(q,\omega\right)
+O(r^{-3}),
\]

where

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
L=\log\lambda=S/2.
}
\]

Moreover `a` is nonzero.

---

## 4. Cubic mass of the critical tail

At leading order,

\[
|U|^3dy
\sim
r^{-3}|a(q,\omega)|^3r^2drd\omega.
\]

Since

\[
\frac{dr}{r}=dq,
\]

we obtain

\[
\boxed{
\int_{1<|y|<Y}|U(y,s)|^3dy
=
\int^{\log Y-s/2}
\int_{S^2}|a(q,\omega)|^3d\omega dq
+O(1).
}
\]

Define the cubic mass per log period

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

---

## 5. Compare the slopes

The external lower bound requires

\[
\liminf_{Y\to\infty}
\frac1{\log Y}
\int_{|y|<Y}|U|^3dy
\ge 2c_M.
\]

The tail asymptotic gives the left side as

\[
\frac{\mathcal A_3}{L}.
\]

Hence

\[
\boxed{
\frac{\mathcal A_3}{L}
\ge
2c_M.
}
\]

Equivalently,

\[
\boxed{
\mathcal A_3
\ge
2c_M L.
}
\]

Thus the nonzero critical amplitude is quantitatively nontrivial in mean cubic mass.

---

## 6. Combine with M19-097

M19-097 gives, on the certified one-slice-Type-I application lane,

\[
L=\frac S2\ge \frac{v_*}{A_*}.
\]

Therefore

\[
\boxed{
\mathcal A_3
\ge
2c_M\frac{v_*}{A_*}>0.
}
\]

This gives a fixed positive lower bound on cubic amplitude per period, conditional on the combined hypotheses of the external concentration theorem and the M19-096/097 application gate.

---

## 7. Why this is not a contradiction

A bounded nonzero periodic critical datum naturally produces logarithmic growth of the similarity `L3` mass.

Thus the quantitative concentration theorem is structurally consistent with M5-566.

It sharpens the surviving DSS tail but does not eliminate it.

In particular,

\[
\boxed{
U\in L^q(\mathbb R^3),\ q>3,
}

for a `1/r` far field does not allow one to import a steady self-similar Liouville theorem into the time-periodic DSS equation.

Backward DSS nonexistence for arbitrary `lambda` remains open in this class.

---

## 8. New DSS hard-core description

On the combined certified lane, an unresolved DSS survivor must satisfy all of

\[
\boxed{
\begin{aligned}
&a(q+L)=a(q),\\
&L\ge L_*>0,\\
&a\not\equiv0,\\
&\frac1L\int_0^L\int_{S^2}|a|^3\,d\omega dq\ge2c_M.
\end{aligned}
}
\]

Thus the remaining periodic branch has neither an arbitrarily small period nor an arbitrarily small mean critical amplitude.

---

## 9. Reference boundary

External quantitative concentration input:

- T. Barker and C. Prange, *Quantitative Regularity for the Navier--Stokes Equations Via Spatial Concentration*, Communications in Mathematical Physics 385 (2021), especially Corollary 1.1.

The paper explicitly treats nonzero backward DSS as a conditional possibility rather than claiming general nonexistence.

---

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
