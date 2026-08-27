# DSD M5-172 — Exact Riccati Tracking of the Nonautonomous Stable Principal Root

Date: 2026-08-28

Status: **P1_B^S PRINCIPAL-LAG MODEWISE RESULT / THE EXACT PRINCIPAL CO-MOVING MODE EQUATION REDUCES TO A RICCATI FLOW FACTORED BY THE TWO M5-167 FROZEN ROOTS / THE FLAT-SELECTED BRANCH TRACKS THE SLOW ROOT WITH ERROR `O_kappa(a)` FOR EACH MODE SATISFYING THE SUPPORT CONDITION `a A_mode <= kappa` / THIS IS GREEN MODEWISE, BUT IT DOES NOT BY ITSELF IMPLY THE M5-171 MEAN DIRICHLET-QUOTIENT CORRIDOR `a N <= kappa`, BECAUSE A SMALL AMOUNT OF SPECTRAL MASS MAY LIE ABOVE THE SUPPORT CORRIDOR / THE MEAN-TO-SUPPORT STEP IS EXPLICITLY YELLOW / GLOBAL REGULARITY UNPROVED.**

---

## 1. Exact principal mode equation

Set

\[
a=e^{-\tau}.
\]

For the principal relative-vorticity equation, take a genealogical Fourier mode `omega` and a spherical harmonic of degree `ell`.

Write its scalar amplitude as `f(tau)` and define

\[
\boxed{
y:=\frac{f_\tau}{f}-i\omega.}
\]

The exact principal mode equation gives

\[
\boxed{
4\nu a y_\tau
+4\nu a y^2
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

For frozen `a`, M5-167 defines

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
-i\omega,
\]

so the exact nonautonomous equation is

\[
\boxed{y_\tau=-(y-y_-)(y-y_+).}
\]

---

## 3. Deviation from the slow root

Let

\[
\delta:=y-y_-(a(\tau)).
\]

Then

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

Since `Q(a,y_-(a))=0` and `a_tau=-a`, implicit differentiation gives

\[
Q_y(y_-)_\tau-aQ_a=0.
\]

At the minus root,

\[
Q_y=-\sqrt D.
\]

Also the frozen equation gives

\[
aQ_a=y_-+i\omega=\lambda_s.
\]

Hence

\[
\boxed{
(y_-)_\tau
=-\frac{\lambda_s}{\sqrt D}.
}
\]

---

## 5. Fast/slow gap

For sufficiently small `a`,

\[
\boxed{
\operatorname{Re}\Delta
=
\frac{\operatorname{Re}\sqrt D}{4\nu a}
\ge
\frac{c_0}{a}.
}
\]

The principal square-root branch has positive real part, and the real part stays uniformly away from zero at fixed finite parabolic mode size.

---

## 6. Modewise fixed parabolic support corridor

For one scalar mode define

\[
\mathfrak A_{\ell,\omega}
\simeq
1+4\omega^2+\ell(\ell+1).
\]

Fix

\[
\boxed{a\mathfrak A_{\ell,\omega}\le\kappa<\infty.}
\]

Then the explicit root formula gives

\[
|\lambda_s|\le C_\kappa,
\]

and therefore

\[
\boxed{
|(y_-)_\tau|
\le C_\kappa.
}
\]

This is a **support condition for the individual mode**.  It is not the same statement as the mean Dirichlet-quotient condition `a N <= kappa`.

---

## 7. Stable Volterra tracking

The flat selection removes the growing homogeneous solution of

\[
\delta_\tau
=
\Delta\delta-\delta^2-(y_-)_\tau.
\]

The stable branch therefore has a future-Volterra representation with kernel decay rate `Re Delta >= c_0/a`.

Its kernel mass is `O(a)`.  A small-ball bootstrap yields

\[
\boxed{
|\delta(\tau)|
\le C_\kappa a
}
\]

for each mode remaining in the fixed support corridor.

Hence

\[
\boxed{
\operatorname{Re}\frac{f_\tau}{f}
=
\operatorname{Re}\lambda_s+O_\kappa(a)
}
\]

modewise.

---

## 8. What is GREEN

M5-167 gives frozen principal frequency-monotone damping.

M5-172 now proves that for every individual mode satisfying

\[
a\mathfrak A_{\ell,\omega}\le\kappa,
\]

the exact nonautonomous stable rate differs from the frozen rate by only `O_kappa(a)`.

Thus there is no hidden fast-normal frequency-production channel **inside a fixed spectral support corridor**.

---

## 9. Mean-to-support audit — YELLOW

The M5-171 corridor is

\[
\boxed{a\mathcal N\le\kappa}
\]

with

\[
\mathcal N
=
\frac{\langle AF,F\rangle}{\|F\|^2}.
\]

This controls only a spectral mean.

It does **not** imply

\[
aA\le\kappa
\]

on every mode in the support.

A very small amount of mass may occur at much larger frequency while the mean remains within the corridor.

Therefore the following inference is forbidden:

\[
\boxed{
a\mathcal N\le\kappa
\not\Rightarrow
\text{all modes satisfy }aA_{mode}\le\kappa.
}
\]

The previous draft of M5-172 implicitly crossed this boundary in its quotient-level interpretation.  That overreach is removed here.

---

## 10. What may still absorb the high-frequency dust

The exact Dirichlet-quotient derivative contains the positive spectral variance

\[
\mathcal V
:=
\frac{\|(A-\mathcal N)F\|^2}{\|F\|^2}.
\]

Modes far above the mean make `V` large.

Therefore the natural remaining route is a spectral split:

1. low/support corridor: use the GREEN modewise M5-172 tracking;
2. high-frequency dust: use the positive variance and the stronger frozen principal damping to absorb the tail;
3. variable first-order coupling: use M5-163 and Young splitting against the same variance.

This split has not yet been completed quantitatively.

---

## 11. DSD audit

### Formation — GREEN

The Riccati variable and frozen roots are actual modewise objects.

### Axis — GREEN

Modewise frequency support and mean frequency are now explicitly separated.

### Static aggregation — CORRECTED

A mean frequency bound is no longer promoted into a support bound.

### Dynamics — GREEN modewise / YELLOW after aggregation

Stable root tracking is GREEN for each mode in a fixed support corridor.  The aggregate quotient step remains YELLOW.

### Cross-audit — GREEN after correction

The correction prevents a disguised `mean -> support` circular shortcut.

---

## 12. Next target

Prove the spectral-split estimate

\[
\boxed{
\text{low modewise tracking}
+
\text{high-mode variance absorption}
+
\text{first-order commutator control}
\Rightarrow
\mathcal N_\tau
\le C_\kappa a(1+\mathcal N)
}
\]

under the mean corridor `a N <= kappa`.

If this succeeds, M5-171 closes `P1_B^S`.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
