# DSD M19-115 — Nontrivial RSS must live in a two-sided rotation-anisotropy compensation band

Date: 2026-09-12

Status: **ACTIVE M19 CALCULATION / PINEAU--VICOL ADJOINT-WEIGHT IDENTITY RECAST AS A NECESSARY TWO-SIDED COMPENSATION LAW FOR EVERY NONZERO RSS / SMALL ROTATION FAILS BECAUSE ANISOTROPY CANNOT GROW ENOUGH, LARGE ROTATION FAILS WHEN THE REFINED AXISYMMETRY ESTIMATE MAKES THE COMPENSATED PRODUCT TOO SMALL / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. RSS rotation operator

Use the rotation operator

\[
\boxed{
\mathcal R U
:=
JU-(Jy\cdot\nabla)U.
}
\]

The RSS profile equation is

\[
\alpha\mathcal RU
+\frac12U
+\frac12(y\cdot\nabla)U
-\Delta U
+(U\cdot\nabla)U
+\nabla P
=0.
\]

Pineau--Vicol work under the Type-I profile bound

\[
|U(y)|\le\frac{C_{U,0}}{1+|y|}
\]

and derive higher derivative/pressure bounds with constants depending on `C_{U,0}` but not on `alpha`.

---

## 2. Weighted head-pressure identity

Their adjoint-kernel construction gives a strictly positive weight `w` satisfying

\[
L^*w=0,
\]

with two-sided Gaussian bounds independent of `alpha`.

The RSS head-pressure equation yields

\[
\boxed{
\int_{\mathbb R^3}|\Omega|^2w\,dy
=
\alpha\int_{\mathbb R^3}Ew\,dy,
}
\]

where

\[
E
=\frac12\partial_\theta\bigl(|U|^2+U\cdot y\bigr).
\]

The angular derivative can be bounded by the rotational defect:

\[
|E(y)|
\lesssim
(1+|y|)|\mathcal RU(y)|
\]

with Type-I-dependent constants.

Using the Gaussian comparison weight `mu=e^{-|y|^2/4}`, Pineau--Vicol obtain a bound of the form

\[
\boxed{
\int|\Omega|^2w
\le
C_0\,|\alpha|\,\|\mathcal RU\|_{L^2_\mu},
}
\]

where `C_0` is independent of `alpha`.

---

## 3. Nontriviality gives a positive weighted-enstrophy floor

Their local-enstrophy smallness criterion says that, for a Type-I profile with fixed bound `C_{U,0}`, there exist

\[
\bar R>0,
\qquad
c_\Omega>0
\]

such that sufficiently small

\[
\|\Omega\|_{L^2(B_{\bar R})}
\]

forces

\[
U\equiv0.
\]

Therefore every nontrivial RSS profile must satisfy

\[
\|\Omega\|_{L^2(B_{\bar R})}
\ge c_\Omega.
\]

The Gaussian lower bound for `w` on the fixed ball gives

\[
\boxed{
\int|\Omega|^2w\,dy
\ge d_0>0,
}
\]

where `d_0` depends only on the retained Type-I corridor, not on `alpha`.

---

## 4. Lower compensation bound

Combine Sections 2 and 3:

\[
d_0
\le
C_0|\alpha|\,\|\mathcal RU\|_{L^2_\mu}.
\]

Hence every nonzero RSS obeys

\[
\boxed{
|\alpha|\,\|\mathcal RU\|_{L^2_\mu}
\ge c_0
:=\frac{d_0}{C_0}>0.
}
\]

This is a parameter-independent **compensation floor**.

A nonzero RSS cannot have both small rotation rate and small rotational anisotropy.

---

## 5. Independent upper compensation bound

The profile equation itself gives

\[
\alpha\mathcal RU
=
\Delta U
-\frac12U
-\frac12y\cdot\nabla U
-(U\cdot\nabla)U
-\nabla P.
\]

The Type-I higher-derivative and pressure bounds of the retained RSS corridor are independent of `alpha` and decay sufficiently fast for the Gaussian norm.

Therefore

\[
\boxed{
|\alpha|\,\|\mathcal RU\|_{L^2_\mu}
\le C_1(C_{U,0}).
}
\]

Thus every nontrivial RSS must satisfy the two-sided band

\[
\boxed{
0<c_0
\le
|\alpha|\,\|\mathcal RU\|_{L^2_\mu}
\le C_1<\infty.
}
\]

---

## 6. Small-rotation interpretation

The Type-I derivative bounds also give

\[
\|\mathcal RU\|_{L^2_\mu}
\le C_R
\]

independently of `alpha`.

Hence

\[
c_0
\le
|\alpha|C_R.
\]

So

\[
\boxed{
|\alpha|\ge c_0/C_R.
}
\]

This recovers the structural reason small rotation is impossible: a compact Type-I profile cannot increase its rotational anisotropy quickly enough to keep the product above the compensation floor.

---

## 7. Large-rotation interpretation

The two-sided band alone allows

\[
\|\mathcal RU\|_{L^2_\mu}
\sim |\alpha|^{-1}.
\]

This is why a crude large-`alpha` argument is insufficient.

Pineau--Vicol prove the stronger statement that for sufficiently large `|alpha|`,

\[
\boxed{
|\alpha|\,\|\mathcal RU\|_{L^2_\mu}
\ll1
}
\]

with constants controlled by the Type-I bound.

That contradicts the compensation floor

\[
|\alpha|\,\|\mathcal RU\|_{L^2_\mu}
\ge c_0.
\]

Thus both extreme-rate exclusions can be viewed through one common quantity.

---

## 8. Moderate hard core

The unresolved RSS class therefore satisfies

\[
\boxed{
|\alpha|\,\|\mathcal RU\|_{L^2_\mu}
\asymp 1
}
\]

at the scale fixed by the Type-I constants.

This identifies the genuine moderate-rotation hard core:

- not close enough to the nonrotating profile for perturbative small-alpha Liouville;
- not axisymmetric enough for rapid-rotation averaging;
- rotational torque and anisotropy compensate at order one.

---

## 9. Reference

External identities and estimates used here are from:

- Ben Pineau and Vlad Vicol, *On rotated backwards self-similar solutions of the incompressible 3D Navier--Stokes equations*, arXiv:2607.09619v2, 2026, especially the weighted head-pressure identity and the small/large rotation arguments.

---

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
