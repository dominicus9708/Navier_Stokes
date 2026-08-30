# DSD M5-321 — R3 Full-Time Endpoint Energy Measure and Shrinking-Ball Atom Extraction

Date: 2026-08-30

Parent: `DSD_M5_320_ATOMIC_ENERGY_MEASURE_FULL_TAIL_RIGIDITY_SCOPE_AND_PARENT_OSEEN_SECOND_ORDER_BUDGET_TARGET_2026-08-30.md`

Status: **PROVED STANDARD BRIDGE / FOR A SMOOTH UNFORCED FINITE-ENERGY R3 NAVIER--STOKES BRANCH APPROACHING A FINITE TERMINAL TIME, COMPACTLY SUPPORTED LOCAL ENERGY PAIRINGS HAVE A FULL-TIME LIMIT, DEFINING A UNIQUE ENDPOINT KINETIC-ENERGY RADON MEASURE / IF A SHRINKING FAMILY OF BALLS WITH CENTERS CONVERGING TO a CARRIES A UNIFORM POSITIVE ENERGY FLOOR ALONG t_j -> T_*, THEN THE ENDPOINT MEASURE HAS AN ATOM OF AT LEAST THAT MASS AT a / THIS CLOSES THE ATOM-EXTRACTION PART OF THE SCREENED-ROTOR BRIDGE / GLOBAL REGULARITY UNPROVED.**

---

## 1. Setting

Let

\[
u\in C^\infty([t_b,T_*)\times\mathbb R^3)
\]

be a smooth unforced incompressible Navier--Stokes solution with

\[
\sup_{t_b<t<T_*}\|u(t)\|_2\le E_*<\infty
\]

and

\[
\int_{t_b}^{T_*}\|\nabla u(t)\|_2^2dt<\infty.
\]

These are the standard smooth-branch energy bounds.

We prove that

\[
|u(t,x)|^2dx
\]

has a unique full-time weak-* limit as `t -> T_*` against compactly supported tests.

---

## 2. Local energy pairing

Fix

\[
\varphi\in C_c^\infty(\mathbb R^3).
\]

Define

\[
F_\varphi(t)
:=\frac12\int\varphi(x)|u(t,x)|^2dx.
\]

The smooth local energy identity gives

\[
\begin{aligned}
F_\varphi(t)-F_\varphi(s)
&=\int_s^t\int
\frac{|u|^2}{2}u\cdot\nabla\varphi
+p\,u\cdot\nabla\varphi\,dxdt\\
&\quad+\nu\int_s^t\int
\frac{|u|^2}{2}\Delta\varphi\,dxdt
-\nu\int_s^t\int
\varphi|\nabla u|^2dxdt.
\end{aligned}
\]

Only compact-support constants depending on `varphi` appear.

---

## 3. L3 and pressure-flux integrability

By Sobolev and interpolation in `R^3`,

\[
\|u(t)\|_3^4
\le
\|u(t)\|_2^2\|u(t)\|_6^2
\le
C E_*^2\|\nabla u(t)\|_2^2.
\]

Hence

\[
\boxed{
\int_{t_b}^{T_*}\|u(t)\|_3^4dt<\infty.
}
\]

For `s<t<T_*`, Holder in time gives

\[
\int_s^t\|u(\tau)\|_3^3d\tau
\le
(t-s)^{1/4}
\left(
\int_s^t\|u(\tau)\|_3^4d\tau
\right)^{3/4}.
\]

Therefore this cubic flux tends to zero as `s,t -> T_*`.

The whole-space pressure satisfies

\[
p=\mathcal R_i\mathcal R_j(u_i u_j)
\]

up to a time-dependent additive constant, and

\[
\|p(t)\|_{3/2}
\le C\|u(t)\|_3^2.
\]

Since

\[
\int |p||u|
\le
\|p\|_{3/2}\|u\|_3
\le C\|u\|_3^3,
\]

the pressure flux has the same terminal integrability.

---

## 4. Viscous terms vanish on short terminal intervals

The dissipation tail satisfies

\[
\int_s^t\|\nabla u\|_2^2d\tau\to0
\qquad
(s,t\to T_*).
\]

The lower-order viscous term is bounded by

\[
C_\varphi (t-s)E_*^2.
\]

Thus every term in

\[
F_\varphi(t)-F_\varphi(s)
\]

tends to zero as `s,t -> T_*`.

Hence

\[
\boxed{
F_\varphi(t)
\text{ is Cauchy as }t\uparrow T_*.
}
\]

---

## 5. Full-time endpoint measure

Define

\[
\Lambda(\varphi)
:=\lim_{t\uparrow T_*}
\int\varphi|u(t)|^2dx.
\]

For nonnegative `varphi`,

\[
0\le\Lambda(\varphi)
\le E_*^2\|\varphi\|_\infty.
\]

By the Riesz representation theorem, there is a unique finite nonnegative Radon measure

\[
\boxed{
\mu_*\in\mathcal M^+(\mathbb R^3)
}
\]

such that

\[
\boxed{
|u(t,x)|^2dx
\stackrel{*}{\rightharpoonup}
\mu_*
\quad\text{as }t\uparrow T_*
}
\]

against every compactly supported continuous test function.

The convergence is along the full time variable, not merely a subsequence.

---

## 6. Shrinking-ball energy floor

Assume there are

\[
t_j\uparrow T_*,
\qquad
X_j\to a,
\qquad
d_j\downarrow0
\]

such that

\[
\boxed{
\int_{B_{d_j}(X_j)}|u(t_j,x)|^2dx
\ge c_0>0.
}
\]

Fix any `R>0`.

For all sufficiently large `j`,

\[
B_{d_j}(X_j)
\subset
\overline B_R(a).
\]

Therefore

\[
\int_{\overline B_R(a)}|u(t_j)|^2dx
\ge c_0.
\]

---

## 7. Portmanteau gives atomic mass

For weak convergence of finite nonnegative measures and a closed set `F`,

\[
\limsup_{j\to\infty}\mu_j(F)
\le
\mu_*(F).
\]

Take

\[
\mu_j=|u(t_j)|^2dx,
\qquad
F=\overline B_R(a).
\]

Then

\[
\boxed{
\mu_*(\overline B_R(a))
\ge c_0
}
\]

for every `R>0`.

Because `mu_*` is finite, continuity from above gives

\[
\mu_*(\{a\})
=
\lim_{R\downarrow0}\mu_*(\overline B_R(a)).
\]

Hence

\[
\boxed{
\mu_*(\{a\})\ge c_0>0.
}
\]

This is a genuine point energy atom.

---

## 8. Relation to the center branch

The atom extraction requires

\[
X_j\to a.
\]

On the current proof tree, failure of center convergence/nesting is already a center-turnover branch.

Therefore on the no-center-turnover corridor the affine-shield energy floor yields a genuine atom rather than an energy packet escaping to spatial infinity.

Thus

\[
\boxed{
\text{saturated affine shield}
+
\text{no center turnover}
\Longrightarrow
\text{endpoint energy atom}.
}
\]

---

## 9. Consequence for the Huang 2026 route

M5-320 left three gaps:

1. atom extraction;
2. `T^3 -> R^3` transfer of the atomic full-tail rigidity theorem;
3. finiteness of the parent-only delayed Oseen H2 budget.

This note closes gap 1.

The remaining atomic route is therefore

\[
\boxed{
\mu_*(\{a\})>0
\stackrel{?}{\Longrightarrow}_{\mathbb R^3}
\text{full-tail Oseen saturation}
\Longrightarrow
\mathfrak R_u=\infty,
}
\]

which must then be compared with an independently proved finite parent Oseen budget on the no-H/T corridor.

---

## 10. Audit verdict

### Proved

- full-time endpoint kinetic-energy measure exists for the smooth finite-energy `R^3` preterminal branch;
- any convergent shrinking-ball energy floor produces a genuine point atom;
- the saturated screened-rotor geometry therefore really is an atomic-energy scenario whenever the tracked centers converge.

### Still open

- R3 extension/localization of Huang's atomic full-tail theorem;
- parent Oseen delayed H2 budget finiteness;
- routing when centers escape rather than converge.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
