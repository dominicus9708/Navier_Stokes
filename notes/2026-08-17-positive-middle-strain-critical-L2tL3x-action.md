# Positive-middle strain pays a critical `L_t^2 L_x^3` action

Date: 2026-08-17

Status: **DERIVED FROM THE EXACT ENSTROPHY IDENTITY, GLOBAL BETCHOV, HOLDER/GAGLIARDO--NIRENBERG, AND OPTIMIZATION OVER PALINSTROPHY. EVERY CLEAN-PRECURSOR TO COHERENT-CROSSING EPISODE PAYS A LOGARITHMIC SCALE-CRITICAL `L_t^2L_x^3` ACTION OF THE POSITIVE MIDDLE STRAIN EIGENVALUE. LARGE PALINSTROPHY CANNOT REMOVE THIS COST. GLOBAL REGULARITY NOT PROVED.**

## 1. Setup

Let

\[
E(t)=\|\omega(t)\|_2^2,
\qquad
P(t)=\|\nabla\omega(t)\|_2^2,
\]

and let the ordered strain eigenvalues be

\[
\lambda_1\ge\lambda_2\ge\lambda_3.
\]

Define

\[
M(t):=\int_{\mathbb R^3}\lambda_2^+(x,t)|S(x,t)|^2dx.
\]

For smooth decaying incompressible whole-space flow,

\[
\frac12E'+\nu P=Q,
\qquad
Q=\int\omega\cdot S\omega dx,
\]

and global Betchov gives

\[
Q=-4\int\det S\,dx
\le 2M(t).
\]

Hence on an interval `[t_m,t_c]` with `E>0`,

\[
2\int_{t_m}^{t_c}\frac{M}{E}dt
\ge
\frac12\log\frac{E_c}{E_m}
+\nu\int_{t_m}^{t_c}\frac{P}{E}dt.
\]

Set

\[
H:=\frac12\log\frac{E_c}{E_m},
\qquad
D:=\int_{t_m}^{t_c}\frac{P}{E}dt,
\qquad
A:=\int_{t_m}^{t_c}\frac{M}{E}dt.
\]

Then

\[
\boxed{2A\ge H+\nu D.}
\]

## 2. Upper-bound the productive action by the critical middle-strain norm

By Holder,

\[
M
\le
\|\lambda_2^+\|_3\,\||S|^2\|_{3/2}
=
\|\lambda_2^+\|_3\,\|S\|_3^2.
\]

For a divergence-free whole-space velocity field, Calderon--Zygmund/Fourier equivalence gives

\[
\|S\|_2\asymp\|\omega\|_2=E^{1/2},
\]

and

\[
\|\nabla S\|_2\lesssim\|\nabla\omega\|_2=P^{1/2}.
\]

The three-dimensional interpolation estimate

\[
\|S\|_3^2
\lesssim
\|S\|_2\,\|\nabla S\|_2
\]

therefore yields

\[
\boxed{
M(t)
\lesssim
\|\lambda_2^+(t)\|_3
E(t)^{1/2}P(t)^{1/2}.
}
\]

Divide by `E` and integrate. Cauchy--Schwarz in time gives

\[
\boxed{
A
\lesssim
L^{1/2}D^{1/2},
}
\]

where

\[
\boxed{
L:=\int_{t_m}^{t_c}\|\lambda_2^+(t)\|_3^2dt.
}
\]

## 3. Eliminate the palinstrophy ledger

Combine

\[
H+\nu D\le 2A
\]

with

\[
A\le C L^{1/2}D^{1/2}.
\]

Then

\[
H+\nu D
\le
C_*L^{1/2}D^{1/2},
\]

so

\[
L
\ge
c_*
\frac{(H+\nu D)^2}{D}.
\]

For `D>0`,

\[
\frac{(H+\nu D)^2}{D}
=
\frac{H^2}{D}+2\nu H+\nu^2D.
\]

The right-hand side is minimized at

\[
D=H/\nu,
\]

and its minimum is

\[
4\nu H.
\]

Therefore

\[
\boxed{
L
\gtrsim
\nu H
=
\frac\nu2\log\frac{E_c}{E_m}.
}
\]

Equivalently,

\[
\boxed{
\int_{t_m}^{t_c}
\|\lambda_2^+(t)\|_{L_x^3}^2dt
\gtrsim
\nu\log\frac{E_c}{E_m}.
}
\]

The exact numerical constant depends only on the standard Fourier/Calderon--Zygmund and interpolation constants used above.

## 4. Insert the clean-precursor/coherent-crossing ratio

The existing clean-precursor and coherent-core bounds give, for fixed `0<beta<4`,

\[
E_m\lesssim\frac{R^\beta}{\sqrt W},
\qquad
E_c\gtrsim R^3,
\]

while the Gaussian affine-core energy barrier gives

\[
\sqrt W\gtrsim R^5(\log R)^{5/2}.
\]

Hence

\[
\frac{E_c}{E_m}
\gtrsim
R^{8-\beta}(\log R)^{5/2}.
\]

Thus

\[
\boxed{
\int_{t_m}^{t_c}
\|\lambda_2^+(t)\|_3^2dt
\gtrsim
c_{\nu,\beta}\log R
+c_\nu\log\log R-O(1).
}
\]

In particular the cost diverges at least logarithmically as `R -> infinity`.

## 5. Scaling

Strain scales as inverse time under Navier--Stokes scaling. Consequently

\[
\boxed{
\|\lambda_2^+\|_{L_t^2L_x^3}
}
\]

is scale invariant:

\[
2/2+3/3=2.
\]

Thus the productive branch has now been converted into a standard critical function-space quantity rather than a custom enstrophy-weighted action.

## 6. Why large derivative concentration does not evade the bound

The quantity

\[
D=\int P/E
\]

was not assumed small. It was optimized out exactly.

If `D` is too small, the logarithmic enstrophy gain forces a large productive action. If `D` is too large, the viscous term itself increases the required `Q/E` action. The minimum occurs at `D ~ H/nu` and still leaves

\[
L\gtrsim\nu H.
\]

Therefore the old escape

\[
\text{productive strain}\to\text{arbitrarily large palinstrophy}
\]

does not remove the critical middle-strain cost.

## 7. Limitation and next target

This is not by itself a contradiction. A hypothetical singular solution may have

\[
\int^{T^*}\|\lambda_2^+(t)\|_3^2dt=\infty.
\]

The new advantage is that the final nonrepeatability problem is now expressed in one standard scale-critical norm.

The next question is whether the special spatial organization already proved for each coherent episode permits a scale-frequency packing estimate for the productive part of `lambda_2^+` which is stronger than arbitrary divergence of the full critical norm.

Status: **PRODUCTIVE STRAIN -> LOGARITHMIC CRITICAL `L_t^2L_x^3` ACTION / PALINSTROPHY OPTIMIZED OUT / CROSS-SCALE PACKING STILL OPEN / GLOBAL REGULARITY NOT PROVED.**