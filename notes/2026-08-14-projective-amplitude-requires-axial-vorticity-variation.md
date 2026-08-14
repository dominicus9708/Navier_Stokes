# Projective mean-amplitude source requires axial vorticity variation

Date: 2026-08-14

Status: **EXACT ALGEBRAIC SHARPENING FOR THE QUADRATIC FIRST-CHAOS VORTICITY CORE. THE `Ab` CONTRIBUTION TO MEAN-VORTICITY MAGNITUDE VANISHES FOR A STATE WITH NO VORTICITY VARIATION ALONG THE MEAN AXIS. GLOBAL REGULARITY NOT PROVED.**

## 1. Core notation

Let the centered first-chaos residual vorticity be

\[
\eta(z)=Az,
\qquad
\operatorname{tr}A=0.
\]

The constant-shift quadratic-core source is

\[
J_{Ab}=Ab,
\qquad
b=-\frac12c(A),
\]

where

\[
c(A)=\nabla\times(Az).
\]

Let

\[
e=\frac{\bar\Omega}{|\bar\Omega|}
\]

be the instantaneous Gaussian mean-vorticity axis.

We are interested specifically in the radial/amplitude contribution

\[
e\cdot J_{Ab}.
\]

## 2. Extract the exactly line-aligned part

Set

\[
a=A^Te,
\qquad
\alpha=e\cdot a=e^TAe,
\qquad
a_0=a-\alpha e.
\]

Then

\[
a_0\perp e.
\]

Define

\[
A_0=e a_0^T,
\qquad
E=A-A_0.
\]

The exactly line-aligned field is

\[
\eta_0=e(a_0\cdot z).
\]

Its curl is

\[
c_0:=c(A_0)=a_0\times e
\]

up to the fixed orientation convention, and

\[
A_0c_0=0.
\]

Moreover, because `e^T A0=a0^T`,

\[
e^TE=\alpha e^T.
\]

Thus the row of `E` parallel to the mean axis contains only the scalar axial derivative `alpha`.

## 3. Exact first-order cancellation

Expand

\[
e\cdot A c(A)
=
e^T(A_0+E)(c_0+c(E)).
\]

The pure aligned term vanishes. The two terms linear in `E` satisfy the vector identity

\[
\boxed{
 a_0\cdot c(E)+e^TEc_0
=c_0\cdot Ee.
}
\]

Because `c0` is perpendicular to `e`, only the transverse part of `Ee` enters this expression.

The remaining quadratic term is

\[
e^TEc(E)=\alpha\,e\cdot c(E).
\]

Therefore

\[
\boxed{
 e\cdot A c(A)
=
c_0\cdot Ee
+
\alpha\,e\cdot c(E).
}
\]

## 4. Axial-variation bound

The curl map is linear and obeys

\[
|c(E)|\lesssim\|E\|_F.
\]

Also

\[
|c_0|=|a_0|\le\|A\|_F,
\qquad
|\alpha|\le|Ae|,
\qquad
|Ee|\le|Ae|+|A_0e|.
\]

But

\[
A_0e=e(a_0\cdot e)=0,
\]

so

\[
Ee=Ae.
\]

Since `||E|| <= C ||A||`,

\[
|e\cdot A c(A)|
\lesssim
\|A\|_F|Ae|.
\]

Using `b=-c(A)/2`,

\[
\boxed{
|e\cdot J_{Ab}|
\lesssim
\|A\|_F|Ae|.
}
\]

Define

\[
V_\omega=\|A\|_F^2,
\qquad
V_{\rm ax}=|Ae|^2.
\]

Then

\[
\boxed{
|e\cdot J_{Ab}|
\lesssim
\sqrt{V_\omega V_{\rm ax}}.
}
\]

## 5. Exact slow/2D cancellation

The vector

\[
Ae
]

is the coefficient of variation of the first-chaos vorticity in the mean-axis spatial direction. In physical Gaussian coordinates it corresponds, up to the radius factor, to

\[
\partial_e\delta\Omega.
\]

Therefore

\[
Ae=0
\]

means that the first-chaos vorticity core has no dependence on the mean-axis coordinate.

The amplitude estimate then gives the exact cancellation

\[
\boxed{
Ae=0
\quad\Longrightarrow\quad
 e\cdot J_{Ab}=0.
}
\]

Thus an exactly slow/2D3C first-chaos state can rotate or rearrange other components, but cannot create Gaussian mean-vorticity magnitude through the `Ab` mechanism.

## 6. Dimensionless axial share

Define

\[
\Theta=\frac{V_\omega}{B},
\qquad
\Xi_{\rm ax}=\frac{V_{\rm ax}}{V_\omega}.
\]

Then

\[
\boxed{
|e\cdot J_{Ab}|
\lesssim
B\Theta\sqrt{\Xi_{\rm ax}}.
}
\]

If this amplitude lane carries a fixed order-one terminal action on an interval with `B<=m`, the rearrangement argument gives

\[
D_{\rm phys}^{\rm amp}
\gtrsim
\Lambda^{-3/2}
(\Theta\sqrt{\Xi_{\rm ax}})^{-5/2}.
\]

Thus an infinite disjoint amplitude-producing cascade can survive only if

\[
\boxed{
\Lambda^{3/5}\Theta\sqrt{\Xi_{\rm ax}}
\to\infty.
}
\]

The relevant projective defect for mean-amplitude growth is therefore not arbitrary transverse variance. It is specifically an axial three-dimensionality defect.

## 7. Relation to rapid-rotation resonance

This algebraic identity matches the rotating-wave reduction:

- slow modes have no variation along the rotation/mean-vorticity axis;
- exact fast-fast resonant forcing of a slow output has zero helical coupling;
- the local quadratic-core amplitude source likewise vanishes when its axial-variation coefficient vanishes.

Therefore both the Fourier/helical and Gaussian/Hermite descriptions identify the same remaining requirement:

\[
\boxed{
\text{order-one terminal mean amplification}
\Rightarrow
\text{persistent axial 3D defect}.
}
\]

Controlling the time persistence of this axial defect is now the low-Hermite endgame target.

Status: **`Ab` MEAN-AMPLITUDE ROUTED TO AXIAL VORTICITY VARIATION / EXACT SLOW CORE CANNOT AMPLIFY THE MEAN / REMAINING LOW-HERMITE ESCAPE = PERSISTENT AXIAL 3D DEFECT UNDER FAST ROTATION / GLOBAL REGULARITY NOT PROVED.**
