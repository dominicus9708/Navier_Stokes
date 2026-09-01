# DSD M5-537 — Subcritical radial moments place the recurrent velocity in every Lp class strictly above the L3 endpoint

Date: 2026-09-01

Status: **RADIAL-MOMENT/LEBESGUE-ENDPOINT BRIDGE / M5-536 GIVES FINITE VORTICITY MOMENTS `int <y>^alpha |W|^2` FOR EVERY `alpha<1` ON THE INVARIANT HARD COMPONENT / WEIGHTED CALDERON--ZYGMUND TRANSFERS THESE TO `|y|^alpha`-WEIGHTED VELOCITY DIRICHLET CONTROL, AND THE CAFFARELLI--KOHN--NIRENBERG WEIGHTED SOBOLEV INEQUALITY GIVES `U in L^(6/(1+alpha))` / AS `alpha -> 1-`, THE EXPONENT APPROACHES `3+` / TOGETHER WITH THE UNWEIGHTED `L6 cap Linfinity` CONTROL, THE HARD VELOCITY LIES IN EVERY `Lp`, `p>3`, FOR INVARIANT-ALMOST EVERY STATE, WHILE THE EXACT `p=3` ENDPOINT REMAINS UNCONTROLLED BECAUSE IT CORRESPONDS TO THE INFINITE `alpha=1` MOMENT / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Input from M5-536

For `nu`-almost every hard-core state and every

\[
0<\alpha<1,
\]

M5-536 gives

\[
\boxed{
\int_{\mathbb R^3}
(1+|y|^2)^{\alpha/2}
|W(y)|^2dy
<\infty.
}
\]

Moreover the invariant mean of each fixed `alpha` moment is finite.

---

## 2. Weighted Calderon--Zygmund transfer

Because

\[
\nabla U
=\mathcal R W
\]

for a matrix of Riesz transforms and the power weight

\[
|y|^\alpha
\]

belongs to the Muckenhoupt class `A_2` for

\[
-3<\alpha<3,
\]

weighted Calderon--Zygmund gives

\[
\boxed{
\int |y|^\alpha|\nabla U|^2dy
\le
C_\alpha
\int |y|^\alpha|W|^2dy.
}
\]

The regularized weight from M5-536 differs only by a harmless bounded-core modification.

Therefore

\[
\boxed{
\int |y|^\alpha|\nabla U|^2dy
<\infty
\quad\nu\text{-a.e.}
}
\]

for every `alpha<1`.

---

## 3. Weighted Sobolev / Caffarelli--Kohn--Nirenberg inequality

For

\[
0\le\alpha<1,
\]

the scale-compatible weighted Sobolev inequality is

\[
\boxed{
\|U\|_{L^{p_\alpha}}
\le
C_\alpha
\left(
\int |y|^\alpha|\nabla U|^2dy
\right)^{1/2},
}
\]

with

\[
\boxed{
p_\alpha
:=
\frac{6}{1+\alpha}.
}
\]

The scaling check is exact:

\[
1-\frac3{p_\alpha}
=
\frac{1-\alpha}{2}.
\]

M5-523 gives `U(y)->0` uniformly at infinity, so no nonzero constant mode obstructs the homogeneous weighted Sobolev inequality.

---

## 4. Every exponent between 3 and 6

As

\[
\alpha\in(0,1),
\]

we have

\[
p_\alpha\in(3,6).
\]

Conversely, for any

\[
3<p<6,
\]

choose

\[
\boxed{
\alpha
=
\frac6p-1
\in(0,1).
}
\]

Then

\[
\boxed{
U\in L^p(\mathbb R^3)
\quad\nu\text{-a.e.}
}
\]

for every `3<p<6`.

---

## 5. Exponents p>=6

The compact hard hull already satisfies

\[
W\in L^2,
\]

hence by Biot--Savart/Sobolev

\[
U\in L^6.
\]

The Type-I similarity bounds also give

\[
U\in L^\infty.
\]

Interpolation therefore gives

\[
\boxed{
U\in L^p
\qquad
\forall p\in[6,\infty].
}
\]

Combining Sections 4--5,

\[
\boxed{
U_Y\in L^p(\mathbb R^3)
\quad
\forall p>3,
\quad
\nu\text{-a.e. }Y.
}
\]

---

## 6. Invariant mean bounds for fixed p>3

For `3<p<6`, the weighted Sobolev and Calderon--Zygmund estimates imply

\[
\|U\|_p^2
\le
C_p
\mathcal M_{\alpha(p)}
+C_pE,
\]

where

\[
\alpha(p)=\frac6p-1.
\]

M5-536 gives finite invariant mean of `M_alpha`, so

\[
\boxed{
\int
\|U_Y\|_p^2
d\nu(Y)
<\infty
\qquad
\forall p>3.
}
\]

For `p>=6` the same conclusion follows from the uniform `L6` and `Linfinity` caps.

Thus every fixed super-endpoint Lebesgue norm is an integrable observable on the hard invariant component.

---

## 7. The p=3 endpoint corresponds exactly to alpha=1

The relation

\[
p_\alpha=\frac6{1+\alpha}
\]

gives

\[
\alpha=1
\quad\Longleftrightarrow\quad
p=3.
\]

The formal endpoint weighted inequality is

\[
\|U\|_3^2
\lesssim
\int |y||\nabla U|^2dy.
\]

But M5-531--536 show that the corresponding first radial vorticity/Dirichlet moment is infinite on the hard recurrent measure.

Therefore the present method gives

\[
\boxed{
U\in\bigcap_{p>3}L^p
\quad\text{but does not give }U\in L^3.
}
\]

This is a sharp endpoint failure, not merely a missing estimate at some arbitrary exponent.

---

## 8. Relation to known Liouville theory

For exact backward self-similar profiles, classical Liouville theorems such as Tsai's exclude nontrivial profiles under `Lp` assumptions with `p>3`.

However the current hard core is a general recurrent/aperiodic ancient similarity dynamics, not an exact stationary self-similar profile.

The Albritton--Barker ancient Liouville theorem used in M5-527 requires bounded `L3` along a backward sequence.

Therefore

\[
\boxed{
\bigcap_{p>3}L^p
\not\Rightarrow
\text{known general ancient Liouville closure}
}
\]

for the present nonstationary class.

---

## 9. Recurrence gives bounded Lp returns for each fixed p>3

Because

\[
\int\|U\|_p^2d\nu<\infty,
\]

there exists `K_p<infinity` such that

\[
\nu\{Y:\|U_Y\|_p\le K_p\}>0.
\]

Poincare recurrence then gives typical hard orbits infinitely many forward and backward returns to such a bounded-`Lp` set.

Thus for every fixed `p>3`, a typical nontrivial ancient orbit admits backward sequences with

\[
\boxed{
\|U(\theta_n)\|_p\le K_p,
\qquad
\theta_n\to-\infty.
}
\]

The fact that this does not yet trigger a known Liouville theorem highlights the exact special role of `p=3`.

---

## 10. DSD interpretation

The weighted-tail defect and the classical critical Lebesgue endpoint are the same obstruction viewed in two coordinate systems:

\[
\boxed{
\alpha<1
\leftrightarrow
p>3
\quad\text{controlled},
}
\]

\[
\boxed{
\alpha=1
\leftrightarrow
p=3
\quad\text{uncontrolled/infinite}.
}
\]

Thus the current survivor has been reduced to an exact critical endpoint rather than a broad family of possible low-frequency failures.

---

## 11. Highest-value next target

Two routes remain natural.

### Route E1 — endpoint improvement

Search for an additional structural input from the persistent dual/ratchet core that upgrades

\[
\bigcap_{p>3}L^p
\]

to one critical endpoint control such as

\[
L^3,
\quad
L^{3,q}\ (q<\infty),
\quad
\text{or a logarithmically improved }L^{3,\infty}\text{ class}.
\]

Any sufficiently strong endpoint upgrade can reconnect directly to known ancient/regularity Liouville theory.

### Route E2 — weighted endpoint cocycle

Use the exact `alpha=1` moment equation and the M5-532 radial defect balance to show that infinite first-moment recurrence requires a nonzero critical radial flux at infinity incompatible with the spectator-tail decoupling of M5-534--535.

---

## 12. Status

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
