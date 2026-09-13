# M19-252 — High angular or Floquet frequency strengthens the frozen shell boundary determinant

**Date:** 2026-09-14  
**Status:** ACTIVE CALCULATION / FREQUENCY-DECOMPACTIFICATION AUDIT

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Purpose

M19-250 leaves scaled derivative/frequency/profile decompactification as the only escape from regular shell rigidity. M19-251 then proves that the frozen bare half-space shell has no unit poloidal mode.

This module asks whether very large tangential or Floquet frequency can defeat the frozen boundary determinant. It cannot: both frequencies strengthen the determinant separation.

## 2. Frozen Oseen factor

For tangential Fourier magnitude \(k\ge0\), the homogeneous viscous exponent \(\alpha\) satisfies

\[
F(\alpha)=0,
\]

where

\[
\boxed{
F(\alpha)
=
\lambda
-\nu(\alpha^2-k^2)
+\frac R2\alpha
+\frac12.
}
\]

Equivalently,

\[
\boxed{
\nu\alpha^2
-\frac R2\alpha
-\left(\nu k^2+\lambda+\frac12\right)=0.
}
\]

For a unit/Floquet mode write

\[
\lambda=i\omega,
\qquad
\omega\in\mathbb R.
\]

## 3. There is exactly one decaying viscous root

The quadratic discriminant is

\[
\boxed{
\Delta_\alpha
=
\frac{R^2}{4}
+4\nu\left(\nu k^2+\frac12+i\omega\right).
}
\]

Its real part is

\[
\operatorname{Re}\Delta_\alpha
=
\frac{R^2}{4}+4\nu^2k^2+2\nu
>
\frac{R^2}{4}.
\]

For the principal square root,

\[
\operatorname{Re}\sqrt{\Delta_\alpha}
=
\sqrt{\frac{|\Delta_\alpha|+\operatorname{Re}\Delta_\alpha}{2}}
>
\frac R2.
\]

Hence the two roots

\[
\alpha_\pm
=
\frac{R/2\pm\sqrt{\Delta_\alpha}}{2\nu}
\]

satisfy

\[
\boxed{
\operatorname{Re}\alpha_+>0,
\qquad
\operatorname{Re}\alpha_-<0.
}
\]

Therefore there is exactly one decaying viscous Oseen root for every

\[
k\ge0,
\qquad
\omega\in\mathbb R.
\]

Large radial oscillation does not create an additional decaying degree of freedom with which to satisfy no-slip.

## 4. Exact determinant modulus

The pressure harmonic has exponent \(k\), and M19-251 shows that the no-slip determinant can vanish only if the viscous root collides with the pressure root, equivalently if

\[
F(k)=0.
\]

But

\[
\boxed{
F(k)
=
\frac12+rac{Rk}{2}+i\omega.
}
\]

Thus

\[
\boxed{
|F(k)|^2
=
\left(\frac12+rac{Rk}{2}\right)^2+\omega^2.
}
\]

In particular,

\[
\boxed{|F(k)|\ge\frac12.}
\]

The lower bound is uniform in

\[
R,
\qquad k,
\qquad\omega.
\]

## 5. High tangential frequency increases the separation

For fixed \(\omega\),

\[
|F(k)|
\ge
\frac12+rac{Rk}{2}.
\]

In a spherical-harmonic sector of degree \(\ell\), the local physical tangential wavenumber is

\[
k_\ell\sim\frac{\sqrt{\ell(\ell+1)}}R.
\]

Therefore

\[
\boxed{
\operatorname{Re}F(k_\ell)
\sim
\frac12+rac12\sqrt{\ell(\ell+1)}.
}
\]

As \(\ell\to\infty\), the boundary determinant moves farther from zero. Thus angular-frequency decompactification is not a bare local resonance mechanism.

## 6. High Floquet frequency also increases the separation

For fixed \(k\),

\[
|F(k)|
\ge|\omega|.
\]

Hence

\[
\boxed{
|\omega|\to\infty
\Longrightarrow
|F(k)|\to\infty.
}
\]

A large temporal/Floquet frequency therefore cannot generate a frozen bare unit boundary mode. It strengthens the local complementing condition.

## 7. Consequence for the decompactification frontier

The M19-250 decompactification branch cannot be interpreted simply as

\[
\text{large }\ell
\quad\text{or}\quad
\text{large }|\omega|
\Longrightarrow
\text{new local unit resonance}.
\]

The frozen shell calculation says the opposite.

Thus any actual decompactifying cavity survivor must exploit something absent from the frozen model, such as

\[
\boxed{
\begin{array}{l}
\text{variable-coefficient radial mode conversion},\\
\text{curvature-sensitive low angular sectors},\\
\text{global multiscale/pseudospectral coupling},\\
\text{or loss of the localization/resolvent control needed to compare the actual shell with the frozen determinant.}
\end{array}}
\]

## 8. Low/high angular split for the next calculation

The determinant gap grows like \(\ell/2\) in high spherical harmonics, whereas geometric curvature corrections are only order one at the inner Oseen scale and lower for the tangential/angular couplings.

This suggests a useful split:

\[
\boxed{
\ell\gg1:
\text{determinant-dominated high-angular sector},
}
\]

\[
\boxed{
\ell=O(1):
\text{finite low-angular sector requiring exact spherical/curvature analysis}.
}
\]

The high-angular branch should be perturbatively stable once the shell localization norm is made precise. The genuinely delicate branch is therefore finite low angular complexity plus global radial/multiscale coupling.

## 9. Scope firewall

The frequency gap is a property of the frozen local Oseen--Stokes determinant. It does not yet prove a variable-coefficient global resolvent estimate.

Therefore

\[
\boxed{
\text{high-frequency frozen determinant gap}
\neq
\text{full cavity high-frequency exclusion without localization control}.
}

Nevertheless it removes the idea that frequency blow-up by itself can create the missing unit resonance.
