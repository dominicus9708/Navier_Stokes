# Angular-palinstrophy threshold for vortex stretching versus viscosity

Date: 2026-08-13

Status: **DERIVED ONE-VARIABLE SOURCE/DISSIPATION OPTIMIZATION / OPEN CONSTANT-AND-LOCALIZATION CLOSURE**.

The magnitude-direction source gap can be compared directly with viscous enstrophy dissipation.  This produces a sharp optimization in the *total palinstrophy variable* for the derived upper bound and identifies an additional saturation ratio.

---

## 1. Input inequality

Let

\[
E=\|\omega\|_2^2,
\qquad
P=\|\nabla\omega\|_2^2,
\]

and let

\[
A=P_{\rm ang}
=P-\|\nabla|\omega|\|_2^2
\ge0.
\]

The source-depletion inequality is

\[
\boxed{
|Q|
\le
C_*E^{3/4}(P-A)^{3/4},
}
\]

where

\[
Q=\int\omega\cdot S\omega dx.
\]

The enstrophy identity is

\[
\frac12\dot E+\nu P=Q.
\]

---

## 2. Optimize the source/dissipation ratio over `P`

For fixed positive `E,A`, define

\[
R(P)
=
\frac{C_*E^{3/4}(P-A)^{3/4}}
{\nu P},
\qquad P>A.
\]

Set

\[
x=P/A>1.
\]

Then

\[
R(P)
=
\frac{C_*}{\nu}
E^{3/4}A^{-1/4}
\frac{(x-1)^{3/4}}{x}.
\]

The scalar factor has derivative zero at

\[
\boxed{x=4.}
\]

Indeed

\[
\frac{d}{dx}
\left[
\frac34\log(x-1)-\log x
\right]
=0
\Longleftrightarrow
\frac{3}{4(x-1)}=\frac1x
\Longleftrightarrow x=4.
\]

The maximum value is

\[
\boxed{
\max_{x>1}
\frac{(x-1)^{3/4}}x
=
\frac{3^{3/4}}4.
}
\]

Therefore

\[
\boxed{
\sup_{P>A}R(P)
\le
\frac{3^{3/4}}4
\frac{C_*}{\nu}
E^{3/4}A^{-1/4}.
}
\]

---

## 3. Viscous-dominance threshold

If

\[
\frac{3^{3/4}}4
\frac{C_*}{\nu}
E^{3/4}A^{-1/4}
<1,
\]

then

\[
Q<\nu P
\]

for every admissible total palinstrophy `P>A`.

Equivalently, the sufficient threshold is

\[
\boxed{
A
>
\frac{27C_*^4}{256\nu^4}
E^3.
}
\]

Under this inequality,

\[
\boxed{\dot E<0.}
\]

Thus sufficiently large **angular palinstrophy relative to `E^3`** makes vorticity-direction variation dissipatively dominant regardless of how much additional magnitude palinstrophy is present.

This is a source/dissipation statement, not by itself a global regularity theorem.

---

## 4. Necessary condition for nondecreasing enstrophy

Conversely, if

\[
\dot E\ge0,
\]

then necessarily

\[
Q\ge\nu P.
\]

The derived source bound therefore forces

\[
\boxed{
A
\le
\frac{27C_*^4}{256\nu^4}
E^3.
}
\]

Hence any dangerous enstrophy-growth phase must keep the angular/projective part of palinstrophy below a fixed multiple of `E^3`.

---

## 5. Saturation ratio

For fixed `E,A`, the derived upper bound is most favorable to stretching only when

\[
\boxed{P=4A.}
\]

Equivalently,

\[
\boxed{
\eta_{\rm ang}=A/P=1/4.
}
\]

Therefore a sequence that attempts to saturate the present source-versus-viscosity estimate must satisfy the additional rigidity condition

\[
\boxed{
P/A\to4
}
\]

along with near-equality in Hölder, the strain/vorticity singular-integral estimate, interpolation, and scalar Sobolev.

This adds one more independent simultaneous-saturation requirement.

---

## 6. Natural-scale projective consequence

On a thick natural core,

\[
A
\ge
A_B
\gtrsim
W^{3/2}J_B.
\]

Write the normalized global enstrophy

\[
\boxed{
\mathfrak e
=\frac{E}{\sqrt W}.
}
\]

Then

\[
E^3
=\mathfrak e^3W^{3/2}.
\]

A nondecreasing enstrophy phase must therefore obey schematically

\[
\boxed{
J_B
\lesssim
\nu^{-4}\mathfrak e^3
}
\]

up to fixed thickness/intensity constants and the analytical source constant `C_*`.

Thus projective roughness, normalized global enstrophy, and enstrophy growth cannot vary independently.

---

## 7. Current use in the rigidity program

The relevance is not merely the threshold itself.  A bounded renormalized residual state that keeps enstrophy production near viscous balance must simultaneously approach several equality/saturation regimes:

1. `P/A` near `4`;
2. scalar Sobolev near saturation for `rho=|omega|`;
3. `L2-L6` interpolation near saturation;
4. strain/vorticity `L3` singular-integral coupling near saturation;
5. thick-core projective lower bound not too strong;
6. far/background strain unable to refill the deficit without satisfying its covariance alignment condition.

The next rigidity question is whether a divergence-free vorticity field with non-small projective roughness can satisfy these saturation requirements simultaneously on a normalized dangerous window.

Status: **OPEN SIMULTANEOUS-EQUALITY RIGIDITY / CONSTANT TRACKING**.
