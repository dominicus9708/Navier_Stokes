# DSD M5-172 — Exact Riccati Tracking of the Nonautonomous Stable Principal Root

Date: 2026-08-28

Status: **P1_B^S PRINCIPAL-LAG RESOLUTION / THE EXACT PRINCIPAL CO-MOVING MODE EQUATION REDUCES TO A RICCATI FLOW FACTORED BY THE TWO M5-167 FROZEN ROOTS / THE FLAT-SELECTED BRANCH TRACKS THE SLOW ROOT WITH ERROR `O_kappa(a)` ON EVERY FIXED PARABOLIC CORRIDOR `a A <= kappa` BECAUSE THE FAST/SLOW GAP IS `~a^-1` WHILE THE SLOW ROOT ITSELF CHANGES AT ONLY `O_kappa(1)` RATE / THIS REMOVES THE MAIN NONAUTONOMOUS VOLTERRA-LAG OBSTRUCTION INSIDE THE FIRST-HITTING CORRIDOR / GLOBAL REGULARITY UNPROVED.**

---

## 1. Exact principal mode equation

Set

\[
a=e^{-\tau}.
\]

For the principal relative-vorticity equation, take a genealogical Fourier mode `omega` and a spherical harmonic of degree `ell`.

Write its scalar amplitude as `f(tau)`.

Define

\[
\boxed{
y:=\frac{f_\tau}{f}-i\omega.}
\]

The exact principal mode equation gives

\[
\boxed{
4\nu a y_\tau
+
4\nu a y^2
-(1+6\nu a)y
+\nu a c_\ell
-i\omega
=0,
}
\]

where

\[
c_\ell:=2-\ell(\ell+1).
\]

---

## 2. Frozen roots factor the exact Riccati equation

For frozen `a`, M5-167 defines the two roots

\[
y_\pm(a)
=
\frac{A_a\pm\sqrt D}{8\nu a},
\qquad
A_a:=1+6\nu a,
\]

with

\[
D
=
A_a^2
-16\nu^2a^2c_\ell
+16i\nu a\omega.
\]

Therefore

\[
4\nu a(y-y_-)(y-y_+)
=
4\nu a y^2
-(1+6\nu a)y
+\nu a c_\ell
-i\omega.
\]

Hence the **exact nonautonomous** equation is

\[
\boxed{
y_\tau=-(y-y_-)(y-y_+).}
\]

No frozen approximation is used in this identity.

---

## 3. Equation for deviation from the slow root

Let

\[
\delta:=y-y_-(a(\tau)).
\]

Since

\[
y-y_+=\delta-(y_+-y_-),
\]

we get

\[
\boxed{
\delta_\tau
=
\Delta\,\delta
-\delta^2
-(y_-)_\tau,
}
\]

where

\[
\boxed{
\Delta:=y_+-y_-=
\frac{\sqrt D}{4\nu a}.
}
\]

The positive real part of `Delta` is the fast/slow separation rate.

---

## 4. Exact derivative of the frozen slow root

Let

\[
Q(a,y)
:=
4\nu a y^2
-(1+6\nu a)y
+\nu a c_\ell
-i\omega.
\]

Since

\[
Q(a,y_-(a))=0,
\]

implicit differentiation with `a_tau=-a` gives

\[
Q_y(y_-)_\tau-aQ_a=0.
\]

At the minus root,

\[
Q_y
=
8\nu a y_--(1+6\nu a)
=-\sqrt D.
\]

Moreover the frozen equation itself gives

\[
aQ_a
=
y_-+i\omega
=\lambda_s,
\]

where

\[
\lambda_s:=y_-+i\omega
\]

is the M5-167 frozen stable growth rate.

Therefore

\[
\boxed{
(y_-)_\tau
=-\frac{\lambda_s}{\sqrt D}.
}
\]

This identity is exact.

---

## 5. Gap estimate

The M5-167 square-root formula gives

\[
\operatorname{Re}\sqrt D>0.
\]

For sufficiently small `a`, uniformly on every fixed finite parabolic corridor,

\[
\boxed{
\operatorname{Re}\Delta
=
\frac{\operatorname{Re}\sqrt D}{4\nu a}
\ge
\frac{c_0}{a}
}
\]

with `c_0>0` depending only on viscosity and the fixed corridor convention.

Thus deviations from the slow manifold evolve on the fast normal scale `O(a)`.

---

## 6. Fixed parabolic corridor

Let the cross-frequency operator have scalar mode size

\[
\mathfrak A_{\ell,\omega}
\simeq
1+4\omega^2+\ell(\ell+1).
\]

Fix

\[
\boxed{a\mathfrak A_{\ell,\omega}\le\kappa<\infty.}
\]

The explicit slow-root formula then gives

\[
|\lambda_s|\le C_\kappa
\]

for sufficiently small `a`.

Since `|sqrt D|` stays bounded away from zero in this corridor,

\[
\boxed{
|(y_-)_\tau|
\le C_\kappa.
}
\]

---

## 7. Stable Volterra tracking

The equation

\[
\delta_\tau
=\Delta\delta-\delta^2-(y_-)_\tau
\]

has a growing homogeneous branch because `Re Delta ~ a^-1`.

The already-audited flat selection removes that branch.

Thus the stable solution has a future-Volterra representation schematically

\[
\delta(\tau)
=
\int_\tau^\infty
\exp\left[-\int_\tau^\sigma\Delta(r)dr\right]
\left[(y_-)_\sigma+\delta(\sigma)^2\right]d\sigma.
\]

The exponential kernel has total mass

\[
\boxed{O(a)}
\]

because `Re Delta >= c_0/a` and `a=e^-tau` changes only relatively by `O(a)` across one kernel width.

A standard small-ball bootstrap therefore gives, for sufficiently small `a`,

\[
\boxed{
|\delta(\tau)|
\le
C_\kappa a.
}
\]

The quadratic `delta^2` term is absorbed by the same contraction.

---

## 8. Consequence for the exact principal growth rate

The actual principal logarithmic growth rate is

\[
\frac{f_\tau}{f}
=i\omega+y
=
\lambda_s+\delta.
\]

Hence on every fixed parabolic corridor

\[
\boxed{
\operatorname{Re}\frac{f_\tau}{f}
=
\operatorname{Re}\lambda_s
+O_\kappa(a).
}
\]

M5-167 proves that `Re lambda_s` is monotone nonincreasing in cross frequency.

Therefore the exact nonautonomous principal evolution differs from a frequency-monotone damping family only by a diagonal scalar error of size `O_kappa(a)` on the sub-parabolic corridor.

---

## 9. Dirichlet-quotient implication

A diagonal modewise perturbation bounded by `C_kappa a` cannot generate a leading parabolic frequency drift.

In a quotient derivative it contributes at most a covariance error controlled by

\[
C_\kappa a
\times
\text{spectral spread}.
\]

The positive principal spectral-variance term from M5-166/M5-170 absorbs the spread-dependent part by Young splitting, leaving only

\[
\boxed{C_\kappa a(1+\mathcal N)}
\]

at the quotient level.

Thus M5-172 removes the **nonautonomous principal-lag** obstruction inside the M5-171 fixed corridor.

The only remaining contribution to the corridor inequality is the actual variable first-order relative coupling, already of the same permitted order by the M5-163 commutator estimate.

---

## 10. DSD audit

### Formation — GREEN

The Riccati variable is formed from an actual nonzero scalar principal mode; zeros are handled by interval decomposition/continuity and do not create a new branch.

### Axis — GREEN

Frozen root, actual nonautonomous rate, and fast deviation are kept distinct.

### Static aggregation — GREEN

The `O_kappa(a)` tracking error is not treated as a new dissipative budget; it is only an error in the principal quotient generator.

### Dynamics — GREEN on each fixed parabolic corridor

The future Volterra selection is exactly the already-accepted flat/stable branch condition.

### Cross-audit — GREEN

No Gaussian spectral envelope or backward amplification product is used.

---

## 11. Remaining step

Combine:

1. M5-172 principal nonautonomous tracking;
2. M5-163 first-order commutator estimate;
3. the M5-166 Dirichlet-quotient variance absorption;

to write the explicit corridor inequality

\[
\boxed{
\mathcal N_\tau
\le
C_\kappa a(1+\mathcal N)
\qquad(a\mathcal N\le\kappa).
}
\]

Once this bookkeeping lemma is GREEN, M5-171 closes `P1_B^S`.

`P1_B^P` remains separate.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
