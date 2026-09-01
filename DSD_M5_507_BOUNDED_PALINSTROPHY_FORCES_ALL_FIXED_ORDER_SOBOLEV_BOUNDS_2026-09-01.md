# DSD M5-507 — Bounded palinstrophy forces uniform Sobolev bounds at every fixed derivative order

Date: 2026-09-01

Status: **ALL-ORDER BOUNDED-DERIVATIVE INDUCTION / M5-505 AND M5-506 PROVIDE THE BASE CAPS `D_2<infinity` AND `D_3<infinity` WHEN `D_1=P` IS UNIFORMLY BOUNDED / FOR EVERY `m>=4`, THE HIGHEST TRANSPORT TERM CANCELS, THE TWO EDGE LEIBNIZ TERMS ARE LINEAR IN `D_m`, AND EVERY PROPER SPLIT CONTAINS ONLY DERIVATIVES OF ORDER AT MOST `m-1`; THE AVAILABLE `H^(m-1)` CAP CONTROLS THOSE PRODUCTS IN `L2` BECAUSE THE RESIDUAL SOBOLEV REGULARITIES SUM TO `m-2>=2>3/2` / THUS `1/2 D_m' + c_m D_m + D_(m+1) <= A_m D_m + B_m D_m^(1/2)` / LOG-CONVEXITY `D_(m+1)>=D_m^2/D_(m-1)` CREATES A QUADRATIC RICCATI BARRIER AT EVERY ORDER / INDUCTION GIVES A FINITE UNIFORM CAP FOR EACH FIXED `D_m` / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Derivative hierarchy

For every integer `m>=0`, define

\[
\boxed{
D_m(\theta)
:=
\|\nabla^mW(\theta)\|_2^2.
}
\]

The first levels are

\[
D_0=E,
\qquad
D_1=P,
\qquad
D_2=H,
\qquad
D_3=K.
\]

On the bounded-palinstrophy branch,

\[
D_0\le Z_*,
\qquad
D_1\le P_*.
\]

M5-505 gives a finite uniform cap

\[
D_2\le M_2^{(D)}.
\]

M5-506 gives a finite uniform cap

\[
D_3\le M_3^{(D)}.
\]

These form the induction base.

---

## 2. Exact linear similarity coefficient at order `m`

Differentiate the similarity vorticity equation `m` times and pair with `grad^m W`.

As recorded in M5-506,

\[
\nabla^m(y\cdot\nabla W)
=
y\cdot\nabla\nabla^mW
+m\nabla^mW.
\]

Hence the dilation contribution is

\[
\frac{2m-3}{4}D_m.
\]

Adding the explicit `+W` term gives

\[
\boxed{
c_mD_m,
\qquad
c_m:=\frac{2m+1}{4}>0.
}
\]

The diffusion term is

\[
\boxed{D_{m+1}}.
\]

Therefore

\[
\boxed{
\frac12D_m'
+c_mD_m
+D_{m+1}
=\mathcal N_m.
}
\]

---

## 3. Highest transport derivative cancels

For the advection term,

\[
\nabla^m((U\cdot\nabla)W)
\]

contains

\[
U\cdot\nabla\nabla^mW.
\]

Its energy pairing vanishes:

\[
\int
(U\cdot\nabla)\nabla^mW:
\nabla^mW\,dy
=0
\]

because

\[
\nabla\cdot U=0.
\]

Thus the nonlinear ledger loses no derivative at its highest transport term.

---

## 4. Stretching Leibniz structure

The differentiated stretching term has schematic expansion

\[
\nabla^m(W\cdot\nabla U)
=
\sum_{a=0}^m
C_{m,a}
(\nabla^aW)
(\nabla^{m-a+1}U).
\]

Because Biot--Savart gains one derivative,

\[
\nabla^{m-a+1}U
\sim
\mathcal R\nabla^{m-a}W.
\]

Thus the two edge cases are:

### `a=0`

\[
W\,\nabla^{m+1}U
\sim
W\,\nabla^mW.
\]

### `a=m`

\[
\nabla^mW\,\nabla U.
\]

Both pair with `grad^m W` and are therefore bounded by

\[
\boxed{
C
\left(
\|W\|_\infty
+
\|\nabla U\|_\infty
\right)D_m.
}
\]

The uniform `H^2` bound already obtained at M5-505 controls these coefficients.

---

## 5. Advection commutator structure

After removing the cancelled highest transport term,

\[
[\nabla^m,U\cdot\nabla]W
\]

is a sum over

\[
1\le a\le m
\]

of products

\[
(\nabla^aU)
(\nabla^{m-a+1}W).
\]

Again,

\[
\nabla^aU
\sim
\mathcal R\nabla^{a-1}W.
\]

For `a=1`, the term is an edge term

\[
\nabla U\,\nabla^mW
\]

and is linear in `D_m` after energy pairing.

For `a>=2`, both vorticity derivative orders are at most `m-1`.

---

## 6. Proper Leibniz splits contain only lower derivatives

Assume inductively that for some `m>=4`,

\[
\boxed{
D_j\le M_j<\infty
\quad\text{for every }0\le j\le m-1.
}
\]

Then `W` has a uniform global `H^(m-1)` bound.

Consider a proper stretching split

\[
1\le a\le m-1.
\]

Its two vorticity factors have derivative orders

\[
a
\quad\text{and}\quad
m-a.
\]

Under the `H^(m-1)` cap, these belong respectively to

\[
H^{m-1-a}
\quad\text{and}\quad
H^{a-1}.
\]

The residual Sobolev regularities sum to

\[
(m-1-a)+(a-1)
=
\boxed{m-2}.
\]

For `m>=4`,

\[
m-2\ge2>\frac32.
\]

Hence the standard three-dimensional Sobolev multiplication estimate gives

\[
\boxed{
\|(
\nabla^aW)(\nabla^{m-a}W)\|_2
\le C_{m,a}\,
\|W\|_{H^{m-1}}^2.
}
\]

The same count applies to every proper advection-commutator split.

Thus no proper split requires `D_m` or `D_(m+1)` for its coefficient control.

---

## 7. Nonlinear estimate at general order

Pairing the proper split products with `grad^m W` gives a factor

\[
D_m^{1/2}.
\]

The edge terms contribute linearly in `D_m`.

Therefore there are finite constants

\[
A_m<\infty,
\qquad
B_m<\infty
\]

depending only on the already-established lower-order caps such that

\[
\boxed{
|\mathcal N_m|
\le
A_mD_m
+B_mD_m^{1/2}.
}
\]

Substituting into the exact energy identity,

\[
\boxed{
\frac12D_m'
+c_mD_m
+D_{m+1}
\le
A_mD_m
+B_mD_m^{1/2}.
}
\]

This is the induction inequality.

---

## 8. Fourier log-convexity at general order

The derivative moments satisfy

\[
\boxed{
D_m^2
\le
D_{m-1}D_{m+1}.
}
\]

Under the induction hypothesis

\[
D_{m-1}\le M_{m-1},
\]

we obtain

\[
\boxed{
D_{m+1}
\ge
\frac{D_m^2}{M_{m-1}}.
}
\]

Dropping the favorable linear similarity damping gives

\[
\boxed{
\frac12D_m'
\le
-\frac{D_m^2}{M_{m-1}}
+A_mD_m
+B_mD_m^{1/2}.
}
\]

Again the dissipative term is quadratic in `D_m`, while every positive nonlinear term has smaller power.

---

## 9. Explicit induction barrier

Define

\[
\boxed{
M_m
:=
\max\left\{
4A_mM_{m-1},
\left(4B_mM_{m-1}\right)^{2/3}
\right\}.
}
\]

If

\[
D_m\ge M_m,
\]

then

\[
A_mD_m
\le
\frac{D_m^2}{4M_{m-1}},
\]

and

\[
B_mD_m^{1/2}
\le
\frac{D_m^2}{4M_{m-1}}.
\]

Therefore

\[
\frac12D_m'
\le
-\frac{D_m^2}{2M_{m-1}},
\]

or

\[
\boxed{
D_m'
\le
-\frac{D_m^2}{M_{m-1}}.
}
\]

above the barrier.

---

## 10. Complete-trajectory contradiction at each order

Every ancient similarity trajectory is defined for all

\[
\theta\in\mathbb R.
\]

If at some time

\[
D_m(\theta_0)>M_m,
\]

then while above the barrier the quantity decreases strictly forward and therefore stays at least `D_m(theta_0)` when followed backward.

Integrating

\[
\left(\frac1{D_m}\right)'
\ge
\frac1{M_{m-1}}
\]

backward gives a finite-time contradiction.

Hence

\[
\boxed{
D_m(\theta)
\le M_m
\quad
\forall\theta\in\mathbb R.
}
\]

This closes the induction step.

---

## 11. Induction conclusion

The base levels are

\[
D_0\le Z_*,
\qquad
D_1\le P_*,
\]

with M5-505 giving `D_2` and M5-506 giving `D_3`.

Applying the preceding argument successively for

\[
m=4,5,6,\dots
\]

gives

\[
\boxed{
\forall m<\infty,
\quad
\sup_{\theta\in\mathbb R}
\|\nabla^mW(\theta)\|_2^2
<\infty.
}
\]

The bound depends on `m`; no uniform-in-`m` analytic or Gevrey radius is claimed.

---

## 12. Pointwise derivative consequence

For each fixed integer `j>=0`, choose `m` sufficiently large that Sobolev embedding applies.

The all-order `L2` derivative caps imply

\[
\boxed{
\sup_{\theta\in\mathbb R}
\|\nabla^jW(\theta)\|_\infty
<\infty
}
\]

for every fixed `j`.

Thus the bounded-palinstrophy survivor is globally smooth in similarity space with uniform bounds at every preassigned finite derivative order.

Again, the constants may grow rapidly with `j`.

---

## 13. DSD firewall

This result does **not** imply compactness on the whole spatial domain.

Uniform global Sobolev bounds can coexist with translation/remote-tail loss of compactness.

For example, a bounded smooth packet may move to larger and larger spatial radii while keeping every Sobolev norm bounded.

Therefore M5-507 excludes a derivative/frequency escalation on the bounded-P branch, but it does not exclude

\[
H_{tail}^{remote-E},
\]

terminal spatial-tail genealogy, or other spatial concentration-compactness defects.

The remaining obstruction has moved from **regularity amplitude** to **spatial recurrence/tightness**.

---

## 14. Updated compact survivor

Combining M5-504--507 gives

\[
\boxed{
\mathcal C_{ax+projdiff}
\Longrightarrow
H_{tail}^{remote-Sob}
\lor
\mathcal C_{Sob}^{all},
}
\]

where

\[
\boxed{
\mathcal C_{Sob}^{all}
:
\forall m<\infty,
\quad
\sup_\theta D_m(\theta)<\infty,
}
\]

and the component still carries the positive projected-diffusion and axial-production recurrence inherited from M5-499--501.

Thus there is no intermediate derivative hierarchy left between bounded palinstrophy and all fixed-order Sobolev boundedness.

---

## 15. Highest-value next target

The natural next split is spatial tightness of this all-order Sobolev-bounded hull.

### Tight case

If the vorticity family is uniformly tight in one sufficiently strong Sobolev norm, global Rellich compactness upgrades the hull from local smooth compactness to global strong compactness.

This may permit a strict recurrence or terminal-limit argument unavailable under mere local compactness.

### Non-tight case

If strong Sobolev tightness fails, then an all-order smooth packet/derivative structure repeatedly escapes to remote similarity radii.

That should be compared directly with M5-496's `H_tail^(remote-E)` and M5-481--483's terminal dilation genealogy.

The next calculation should therefore audit **global Sobolev compactness modulo spatial tail escape**.

---

## 16. Status

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
