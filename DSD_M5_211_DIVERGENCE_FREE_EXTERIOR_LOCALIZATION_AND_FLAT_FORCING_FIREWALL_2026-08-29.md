# DSD M5-211 — Divergence-Free Exterior Localization and Flat-Forcing Firewall

Date: 2026-08-29

Parent: `DSD_M5_210_POLYNOMIAL_WEIGHT_COMMON_TAIL_TRANSPORT_VS_STRETCHING_AUDIT_2026-08-29.md`

Status: **LOCALIZATION CONSTRUCTION GREEN / CLOSURE SHORTCUT RED / A FIXED-EXTERIOR SAME-TAIL DIFFERENCE CAN BE CONVERTED BY CUTOFF + BOGOVSKII CORRECTION INTO A GLOBAL DIVERGENCE-FREE FIELD WITH UNIFORMLY BOUNDED EXTENDED BACKGROUND COEFFICIENTS; THE PRICE IS A COMPACT-ANNULUS SOURCE WHICH IS FLAT TO ALL ORDERS AT THE TERMINAL TIME / HOWEVER `FLAT SOURCE + ZERO TERMINAL DATA` DOES NOT IMPLY ZERO SOLUTION, SO THE LEI–YANG–YUAN HOMOGENEOUS BU THEOREM CANNOT BE USED TO DELETE THE SOURCE / A SPATIAL WEIGHT-SEPARATION OR COUPLED LOCAL STOKES CARLEMAN ESTIMATE IS STILL REQUIRED / GLOBAL REGULARITY UNPROVED.**

---

## 1. Fixed exterior corridor

Fix

\[
R>0
\]

and let

\[
\Omega_R:=\{|x-x_*|>R\}.
\]

For two same-tail physical realizations define

\[
Z=u^V-u^W,
\qquad q=p^V-p^W.
\]

The earlier audit gives on every fixed exterior cylinder near `T_*`:

\[
\boxed{
Z(\cdot,T_*)=0,
\qquad
q(\cdot,T_*)=0
}
\]

in the punctured smooth sense, and for every finite `m,k,N`,

\[
\boxed{
\|\partial_t^m\nabla^kZ(t)\|_{L^\infty(A_R)}
+
\|\partial_t^m\nabla^kq(t)\|_{L^\infty(A_R)}
=O((T_*-t)^N)
}
\]

on any fixed compact annulus `A_R` away from `x_*`.

The individual backgrounds and their derivatives are uniformly bounded there.

---

## 2. Divergence-free localization

Choose a smooth radial cutoff `chi_R` such that

\[
\chi_R=0\quad\text{on }B_R(x_*),
\qquad
\chi_R=1\quad\text{outside }B_{2R}(x_*).
\]

Then

\[
\nabla\cdot(\chi_RZ)=\nabla\chi_R\cdot Z
\]

is supported in

\[
A_R:=B_{2R}(x_*)\setminus B_R(x_*).
\]

Let `B_R^{Bog}` denote a fixed Bogovskii right inverse of divergence on the annulus and set

\[
b_R
:=
\mathcal B_R(\nabla\chi_R\cdot Z).
\]

Define

\[
\boxed{Y_R:=\chi_RZ-b_R.}
\]

Then

\[
\boxed{\nabla\cdot Y_R=0.}
\]

Moreover,

\[
Y_R=Z
\quad\text{outside }B_{2R},
\]

while `Y_R` vanishes in the inner region up to the annular Bogovskii support.

Because the Bogovskii operator is fixed and bounded on the fixed annulus, terminal flatness of `Z` implies terminal flatness of `b_R` and all finite derivatives required below.

---

## 3. Local velocity-pressure equation before projection

The relative equation is

\[
Z_t-\nu\Delta Z
+(u^V\cdot\nabla)Z
+(Z\cdot\nabla)u^W
+\nabla q=0,
\qquad
\nabla\cdot Z=0.
\]

Apply the localization above **before** the Leray projection.

The pressure term satisfies

\[
\chi_R\nabla q
=
\nabla(\chi_Rq)-q\nabla\chi_R.
\]

After global Leray projection, the first term disappears and the second is an annular source.

All cutoff commutators from

\[
\Delta(\chi_RZ),
\qquad
\partial_t b_R,
\qquad
\Delta b_R,
\]

and all coefficient-replacement terms are likewise supported in the fixed annular zone before projection.

---

## 4. Bounded global coefficient extensions

Since `u^V,u^W` are uniformly smooth on the fixed exterior, extend them through `B_R` to divergence-free global fields

\[
U_R^V,
\qquad
U_R^W
\]

such that

\[
U_R^{V,W}=u^{V,W}
\quad\text{outside }B_{2R}
\]

and

\[
\boxed{
\|U_R^{V,W}\|_{L^\infty_{t,x}}
+
\|\nabla\times U_R^{V,W}\|_{L^\infty_{t,x}}
\le C_R<\infty
}
\]

on the terminal window.

This is a fixed-domain extension problem and does not inherit the Type-I singularity at `x_*`.

Consequently `Y_R` obeys a global equation of the schematic form

\[
\boxed{
\partial_tY_R-\nu\Delta Y_R
+\mathbb P\nabla\cdot
(U_R^V\otimes Y_R+Y_R\otimes U_R^W)
=F_R.
}
\]

The pre-projection source is built from finitely many annular terms containing

\[
Z,\nabla Z,q,b_R,\nabla b_R
\]

with fixed smooth coefficients.

---

## 5. The source is terminal-flat

For every finite `N` and finite Sobolev order needed by the polynomial CZ estimate,

\[
\boxed{
\|F_R(t)\|_{H^m_{weighted}}
=O_R((T_*-t)^N)
\quad\text{for every }N.
}
\]

This is much stronger than merely

\[
F_R(T_*)=0.
\]

Thus the localization successfully trades

\[
\text{singular global background}
\]

for

\[
\boxed{
\text{bounded global background}
+
\text{terminal-flat annular forcing}.
}
\]

Status: **GREEN reduction.**

---

## 6. Critical firewall: flat forcing is not zero forcing

It is tempting to apply homogeneous backward uniqueness and argue that an all-order flat source is negligible.

That implication is false.

Even the scalar ODE

\[
y'(t)=f(t),
\qquad y(0)=0,
\]

with a nonzero flat function such as

\[
f(t)=e^{-1/t^2}
\quad(t>0)
\]

has a nonzero solution

\[
y(t)=\int_0^tf(s)ds
\]

which is itself flat at `t=0`.

The same phenomenon exists for forced heat equations.

Therefore

\[
\boxed{
F_R\text{ flat to all orders}
+
Y_R(T_*)=0
\not\Rightarrow
Y_R\equiv0.
}
\]

A homogeneous BU theorem cannot simply delete `F_R`.

---

## 7. Why the polynomial weight does not automatically separate the annular source

A true localization Carleman argument usually exploits a **parameterized spatial weight gap**:

\[
\Phi_{target}>\Phi_{source}
\]

so that the source is exponentially suppressed as the Carleman parameter grows.

The Lei–Yang–Yuan spatial factor

\[
(1+|x|^2)^{-k}
\]

has a fixed algebraic exponent, with the CZ-divergence lemma restricted to

\[
k<\frac52.
\]

There is no arbitrarily large spatial separation parameter analogous to a standard spatial Carleman exponent.

Translating the center of the polynomial weight far into the exterior can make the fixed annular source numerically small, but the target region then also moves to spatial infinity. This yields decay information, not exact vanishing at one fixed exterior point.

Thus

\[
\boxed{
\text{polynomial CZ compatibility}
\neq
\text{spatial source-separation Carleman mechanism}.
}
\]

---

## 8. What localization actually accomplishes

The useful consequence is narrower but important:

1. the Type-I singularity can be removed from the coefficient field on a fixed exterior;
2. pressure can be converted into an annular forcing plus a global Leray term;
3. every localization error is terminal-flat and lives at finite radius;
4. the remaining obstacle is no longer weak-`L^3` criticality.

It is instead

\[
\boxed{
\text{boundary-condition-free terminal BU for a bounded-coefficient
Oseen–Stokes / parabolic–elliptic system on a fixed exterior.}
}
\]

This returns to the M5-183 target, now with the role of the Lei–Yang–Yuan polynomial estimate precisely delimited.

---

## 9. DSD audit

### Formation — GREEN

The cutoff, Bogovskii correction, coefficient extensions, and annular forcing are finite ordinary PDE objects.

### Axis — GREEN

Coefficient singularity and localization forcing are separated.

### Static aggregation — GREEN

Terminal flatness is not promoted to exact source vanishing.

### Dynamics — YELLOW

A genuine source-separating exterior Stokes Carleman / BU estimate is still needed.

### Cross-audit — GREEN

This closes the false shortcut `flat commutator forcing => homogeneous BU` while preserving the useful bounded-coefficient reduction.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]