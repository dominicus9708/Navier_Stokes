# Exact Transverse Eigenaxis Evolution — 2026-08-24

Status: **EXACT POINTWISE/COVARIANT ROTATION IDENTITY / GLOBAL REGULARITY NOT PROVED.**

This note asks a narrower question than the global projective-speed estimate: what can actually rotate the two principal strain axes inside the plane orthogonal to the local vorticity direction?

The answer is sharper than the full strain-space estimate. The direct vorticity-dyad term is exactly transverse-isotropic and cannot rotate those axes. The remaining rotation is carried by tilt coupling, pressure-Hessian anisotropy, viscosity/spatial variation, or motion of the vorticity direction.

## 1. Leray strain equation

The Leray velocity equation is

\[
V_s+\frac12V+\frac12Y\cdot\nabla V+(V\cdot\nabla)V+\nabla\Pi
=\nu\Delta V.
\]

Let

\[
A=\nabla V=S+K,
\]

where `S` is symmetric and `K` antisymmetric. Set

\[
\mathcal D
:=
\partial_s+(V+Y/2)\cdot\nabla.
\]

Differentiating the Leray equation gives

\[
\mathcal DA+A+A^2+\nabla^2\Pi=\nu\Delta A.
\]

Taking the symmetric part,

\[
\boxed{
\mathcal DS+S+S^2+K^2+\nabla^2\Pi
=\nu\Delta S.
}
\]

For vorticity `W=curl V`,

\[
\boxed{
K^2
=\frac14(W\otimes W-|W|^2I).
}
\]

## 2. Decomposition relative to the actual vorticity direction

Where `W != 0`, set

\[
\rho=|W|,
\qquad
\xi=W/\rho,
\qquad
P=I-\xi\otimes\xi.
\]

Write

\[
\boxed{
S
=a\,\xi\otimes\xi
+\xi\otimes b+b\otimes\xi
-\frac a2P
+D,
}
\]

where

\[
a=\xi^TS\xi,
\qquad
b=PS\xi,
\]

and

\[
D=PDP,
\qquad
\operatorname{tr}_{\xi^\perp}D=0.
\]

Thus the compression of `S` to `xi^perp` is

\[
C:=PSP|_{\xi^\perp}
=-\frac a2I_{\xi^\perp}+D.
\]

The two physical transverse strain axes are exactly the two eigenaxes of `D` whenever `D != 0`.

## 3. Covariant derivative in the moving transverse plane

Let

\[
\eta:=\mathcal D\xi.
\]

Since `|xi|=1`,

\[
\eta\perp\xi.
\]

The vorticity-direction equation gives

\[
\eta
=PS\xi+
\frac\nu\rho P\Delta W
=b+
\frac\nu\rho P\Delta W.
\]

Define the covariant transverse derivative of a plane tensor by sandwiching the ordinary material derivative with `P`.

Since

\[
\mathcal DP
=-\eta\otimes\xi-\xi\otimes\eta,
\]

one obtains

\[
\boxed{
P\mathcal D(PSP)P
=P(\mathcal DS)P
-\eta\otimes b-b\otimes\eta.
}
\]

The last two terms are exactly the correction caused by motion of the vorticity-normal plane.

## 4. Exact cancellation of the direct vorticity dyad

On `xi^perp`,

\[
P(W\otimes W)P=0,
\]

and therefore

\[
PK^2P
=-\frac{\rho^2}{4}P.
\]

Hence

\[
\boxed{
\operatorname{dev}_\perp(PK^2P)=0.
}
\]

The direct local `W tensor W` term changes only the transverse isotropic part; it cannot rotate the transverse eigenaxes.

This does **not** mean that the old global projective `sqrt(2)/4` term may simply be deleted: the global compatible-strain projection is nonlocal and may return vorticity effects through the pressure/compatibility sector. The present identity instead shows where that effect must enter locally.

## 5. Algebraic simplification of the S^2 term

In the block decomposition relative to `xi`,

\[
PS^2P
=b\otimes b+C^2.
\]

Because `D` is a trace-free symmetric `2 x 2` tensor,

\[
D^2=\frac{|D|_F^2}{2}I_{\xi^\perp}.
\]

Therefore

\[
C^2
=\frac{a^2}{4}I_{\xi^\perp}
-aD
+D^2
\]

and

\[
\boxed{
\operatorname{dev}_\perp(C^2)=-aD.
}
\]

Thus

\[
\boxed{
\operatorname{dev}_\perp(PS^2P)
=-aD+\operatorname{dev}_\perp(b\otimes b).
}
\]

The `-aD` term is parallel to `D`; it changes the transverse spectral gap but does not rotate its eigenaxes. Only the tilt vector `b` can make the algebraic `S^2` term rotate the transverse frame.

## 6. Exact transverse trace-free evolution

Let

\[
H_\Pi:=\nabla^2\Pi.
\]

Taking the transverse trace-free part of the projected strain equation gives

\[
\boxed{
\begin{aligned}
\nabla_s^\perp D
&=(a-1)D
-\operatorname{dev}_\perp(b\otimes b)\\
&\quad
-\operatorname{dev}_\perp(PH_\Pi P)
+\nu\operatorname{dev}_\perp(P\Delta S P)\\
&\quad
-\operatorname{dev}_\perp(\eta\otimes b+b\otimes\eta),
\end{aligned}
}
\]

where `nabla_s^perp` denotes the covariant material derivative inside the moving plane `xi^perp`.

This is an exact identity wherever `W != 0`.

## 7. Project out the magnitude direction

Whenever `D != 0`, set

\[
\widehat D=D/|D|_F.
\]

Let `Pi_D^perp` denote orthogonal projection in the two-dimensional Hilbert space of transverse symmetric trace-free tensors onto the line perpendicular to `D_hat`.

The parallel term `(a-1)D` disappears after this projection. Therefore

\[
\boxed{
\begin{aligned}
|D|_F|\nabla_s^\perp\widehat D|_F
\le{}&
|\operatorname{dev}_\perp(b\otimes b)|_F\\
&+|\operatorname{dev}_\perp(PH_\Pi P)|_F\\
&+\nu|\operatorname{dev}_\perp(P\Delta S P)|_F\\
&+|\operatorname{dev}_\perp(\eta\otimes b+b\otimes\eta)|_F.
\end{aligned}
}
\]

Since

\[
|\operatorname{dev}_\perp(b\otimes b)|_F
=\frac{|b|^2}{\sqrt2},
\]

and the last term is bounded by a universal constant times `|eta||b|`,

\[
\boxed{
|D|_F|\nabla_s^\perp\widehat D|_F
\lesssim
|b|^2
+|H_{\Pi,\perp}^{dev}|
+\nu|\Delta S_{\perp}^{dev}|
+|\eta||b|.
}
\]

## 8. Physical eigenaxis angular speed

A nonzero transverse trace-free tensor can be written in an orthonormal transported basis as

\[
D=d
\begin{pmatrix}
\cos2\theta&\sin2\theta\\
\sin2\theta&-\cos2\theta
\end{pmatrix}.
\]

Hence

\[
|\nabla_s^\perp\widehat D|_F
=2|\theta_s|.
\]

Therefore

\[
\boxed{
2|D|_F|\theta_s|
\lesssim
|b|^2
+|H_{\Pi,\perp}^{dev}|
+\nu|\Delta S_{\perp}^{dev}|
+|\eta||b|.
}
\]

This is the exact local cost of transverse eigenaxis rotation, up to universal norm-equivalence constants in the last two tensor estimates.

## 9. Pure low-tilt consequence

On a lane where

\[
|b|
\]

and

\[
|\eta|
\]

have small integrated action, substantial transverse eigenaxis rotation cannot be produced by the local algebraic `S^2` or direct `W tensor W` terms.

It must instead be carried by

\[
\boxed{
\text{pressure-Hessian transverse anisotropy}
\quad\lor\quad
\text{viscous/second-derivative strain action}
\quad\lor\quad
\text{tilt action}.
}
\]

Thus the anti-ribbon projective rescue has a sharper local interpretation than the old full projective-speed norm bound.

## 10. Relation to the recurrent covariance action

The updated covariance bridge proves, on a thick bounded-shape residual-quiet recurrent positive-middle core, a positive lower density of transverse eigenaxis variation.

If in addition the active transverse gap stays nondegenerate,

\[
|D|_F\ge D_->0,
\]

then integrating the angular-speed identity over a long interval yields

\[
\boxed{
2D_-\,\operatorname{TV}(\theta_e)
\lesssim
\int
\left(
|b|^2
+|H_{\Pi,\perp}^{dev}|
+\nu|\Delta S_{\perp}^{dev}|
+|\eta||b|
\right)ds.
}
\]

Therefore positive-density anti-ribbon rotation forces positive-density action in pressure anisotropy, second derivatives, or tilt.

If `D` repeatedly approaches zero to rotate cheaply, that is a transverse spectral-degeneracy/shape-turnover branch rather than a nondegenerate pure projective lane.

## 11. What remains

This identity does not yet prove that pressure-Hessian anisotropy is expensive enough to contradict recurrence. The pressure term is precisely where the nonlocal compatible-strain effect hidden inside the old global `P_st` estimate can re-enter.

The next target is therefore much more specific:

\[
\boxed{
\text{bound recurrent transverse pressure-Hessian rotation by}
\quad
\text{local frequency/derivative action}
\lor
\text{remote pressure/turnover action}.
}
\]

If that pressure bridge closes, the `sqrt(2)/4` global projective baseline will no longer be the natural bottleneck for transverse anti-ribbon rotation.

Status: **THE DIRECT VORTICITY-DYAD AND THE AXIS-PRESERVING PART OF `S^2` CANNOT ROTATE THE TRANSVERSE STRAIN EIGENAXES. ON A LOW-TILT NONDEGENERATE CORE, EVERY ANTI-RIBBON EIGENAXIS ROTATION MUST BE PAID BY TRANSVERSE PRESSURE-HESSIAN ANISOTROPY OR VISCOUS/SECOND-DERIVATIVE ACTION. THE REMAINING PROJECTIVE BOTTLENECK HAS BEEN LOCALIZED TO PRESSURE COMPATIBILITY RATHER THAN A GENERIC VORTICITY BASELINE. GLOBAL REGULARITY REMAINS UNPROVED.**