# M19-208 — Moderate RSS/RDSS nonsymmetry kernels require an order-one joint W1 product K Gamma W over nu

**Date:** 2026-09-14  
**Status:** ACTIVE CALCULATION / KERNEL-SEVERITY REDUCTION

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Background size from W1 quantities

M19-064 gives the Biot--Savart/strain estimates

\[
M_U\lesssim K^{1/3}Z^{1/3},
\qquad
M_S\lesssim (KZ)^{1/3},
\]

where

\[
K=\|\Omega\|_\infty,
\qquad
Z=\|\Omega\|_2^2.
\]

M19-192 gives the optimized instantaneous W1 enstrophy ceiling

\[
Z\lesssim K^{1/2}(\Gamma W)^{3/2}.
\]

Therefore both background sizes satisfy

\[
\boxed{
M_U\lesssim(K\Gamma W)^{1/2},
\qquad
M_S\lesssim(K\Gamma W)^{1/2}.
}
\]

## 2. Insert into the weighted nonlinear compensation

M19-207 bounds the nonlinear compensation by

\[
\Lambda_{NL}
\le
C_A L_w M_U
+C_B\nu^{-1}M_S^2
\]

with constants absorbing the pressure and lower-order weighted terms.

For any fixed pressure-compatible A2 weight chosen in the optimized family, one has

\[
L_w=C_w\nu^{-1/2},
\qquad
c_{gap}=c_w>0.
\]

Hence

\[
\boxed{
\Lambda_{NL}
\le
A_w\left(\frac{K\Gamma W}{\nu}\right)^{1/2}
+B_w\left(\frac{K\Gamma W}{\nu}\right).
}
\]

## 3. Kernel threshold

A nonsymmetry unit/kernel mode requires \(\Lambda_{NL}\) to compensate at least the weighted linear gap. Thus, with

\[
x:=\left(\frac{K\Gamma W}{\nu}\right)^{1/2},
\]

one must have

\[
B_wx^2+A_wx\ge c_w.
\]

The positive root

\[
x_*=
\frac{-A_w+\sqrt{A_w^2+4B_wc_w}}{2B_w}
\]

(with the obvious linear interpretation if \(B_w=0\)) is strictly positive. Therefore

\[
\boxed{
\frac{K\Gamma W}{\nu}
\ge
\chi_*:=x_*^2>0
}
\]

is a necessary condition for a nonsymmetry kernel.

## 4. RSS and RDSS interpretation

For RSS, rotation preserves \(K,\Gamma,W\), so this is a stationary order-one severity floor throughout the co-rotating orbit.

For RDSS, the integrated unit-mode inequality implies at minimum that the period cannot remain entirely in the subthreshold region \(K\Gamma W<\chi_*\nu\). Thus every kernel-degenerate RDSS period contains a superthreshold state, and quantitative norm-equivalence/occupation bounds can strengthen this to a positive period fraction.

## 5. Consequence

The moderate relative-periodic kernel frontier is now confined to a doubly non-small set:

- rotation/scale parameters lie in the moderate compact region left by external Liouville theorems;
- the joint W1 product satisfies the order-one lower bound above.

This still does not prove kernel nonexistence, but removes the low-activity part of the moderate compact set.