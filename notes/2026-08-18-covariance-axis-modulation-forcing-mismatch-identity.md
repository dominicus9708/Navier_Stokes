# Covariance-axis modulation is forced by nonlinear input or viscous derivative-covariance mismatch

Date: 2026-08-18

Status: **EXACT COVARIANCE EVOLUTION / SHAPE-MODULATION PRICE. AN ORDER-ONE CHANGE OF THE PROJECTIVE COVARIANCE MATRIX C CANNOT OCCUR FOR FREE EVEN IF THE SCALAR PROJECTIVE DEFECT J REMAINS CONSTANT: IT REQUIRES NONLINEAR/SCALE-MOTION FORCING OR THE SAME NEIGHBORING-DERIVATIVE COVARIANCE MISMATCH ALREADY PRESENT AS A POSITIVE VISCOUS DISSIPATION TERM. GLOBAL REGULARITY NOT PROVED.**

## 1. Covariance variables

For a vector field `w` representing vorticity or a forced band/localized vorticity component, define

\[
E=\|w\|_2^2,
\qquad
N=\int w\otimes w\,dx,
\qquad
C=N/E.
\]

At the next derivative level define

\[
E_1=\|\nabla w\|_2^2,
\qquad
N_1=\sum_j\int \partial_jw\otimes\partial_jw\,dx,
\qquad
C_1=N_1/E_1.
\]

Let `F` denote the non-diffusive forcing after the skew-adjoint transport has been removed.  For the unprojected vorticity equation at derivative order zero, `F=S w`; for a moving band, projection/commutator/motion terms are included in `F`.

Define

\[
A=\int F\otimes w\,dx,
\qquad
Q=\operatorname{tr}A,
\qquad
B=A/E,
\qquad
q=Q/E,
\qquad
r=E_1/E.
\]

## 2. Exact energy and covariance equations

Skew transport drops out of the integrated second moments.  Diffusion gives the next derivative covariance.  Hence

\[
\boxed{
\dot E=2Q-2\nu E_1,
}
\]

\[
\boxed{
\dot N=A+A^T-2\nu N_1.
}
\]

Differentiate `C=N/E`:

\[
\begin{aligned}
\dot C
&=B+B^T-2qC
-2\nu\frac{E_1}{E}C_1
+2\nu\frac{E_1}{E}C.
\end{aligned}
\]

Therefore

\[
\boxed{
\dot C
=B+B^T-2qC
-2\nu r(C_1-C).
}
\]

This identity tracks the full covariance matrix, not only the scalar defect `J=1-tr(C^2)`.

## 3. Pointwise modulation-rate bound

Cauchy--Schwarz gives

\[
\|A\|_F\le\|F\|_2E^{1/2},
\qquad
|Q|\le\|F\|_2E^{1/2}.
\]

Since `||C||_F<=tr C=1`,

\[
\boxed{
\|\dot C\|_F
\lesssim
\frac{\|F\|_2}{{\sqrt E}}
+2\nu\frac{E_1}{E}\|C_1-C\|_F.
}
\]

Thus projective-axis rotation / covariance-shape modulation has only two causes:

1. nonlinear / moving-scale forcing;
2. viscous transfer toward a different derivative-level covariance.

## 4. Integrated modulation price

On an occupancy-controlled normalized interval where

\[
0<e_0\le E(t)\le e_1<\infty,
\]

an order-one covariance displacement

\[
\|C(t_1)-C(t_0)\|_F\ge\delta
\]

implies

\[
\delta
\lesssim
\int_{t_0}^{t_1}\frac{\|F\|_2}{\sqrt E}dt
+2\int_{t_0}^{t_1}\nu\frac{E_1}{E}\|C_1-C\|_Fdt.
\]

Cauchy--Schwarz on the viscous term gives

\[
\boxed{
\delta
\lesssim
\int\frac{\|F\|_2}{\sqrt E}dt
+2
\left(\int\nu\frac{E_1}{E}dt\right)^{1/2}
\left(\int\nu\frac{E_1}{E}\|C_1-C\|_F^2dt\right)^{1/2}.
}
\]

The final factor is the normalized form of the positive neighboring-covariance mismatch already present in the energy-weighted projective dissipation identity.

## 5. Consequence for scale-to-scale shape modulation

A reproduction cascade may try to evade the asymptotic-DSS gate while keeping the scalar projective dispersion `J` approximately fixed, simply by rotating the preferred projective axis or changing the anisotropic covariance shape.

The exact identity above prevents this from being an unpriced modulation:

\[
\boxed{
\text{order-one covariance modulation}
\Rightarrow
\text{order-one nonlinear/scale forcing}
\quad\lor\quad
\text{viscous derivative-covariance mismatch action}.
}
\]

Thus constant-`J` axis rotation is a typed forcing/dissipation branch, not a hidden free degree of freedom.

## 6. Remaining shape variables

The covariance matrix does not encode all packet shape information.  Modulation that preserves `C` may still occur through

- signed-line / polarity-magnitude structure;
- higher Hermite moments;
- helical composition;
- spatial location / packet arrangement.

Those channels are covered separately by the exact variance split, high-Hermite descent, equal-helical-injection identity, and phase-space / moving-band ledgers.

Status: **FULL COVARIANCE AXIS MODULATION PRICED BY NONLINEAR FORCING OR VISCOUS C1-C MISMATCH / CONSTANT-J ROTATION LOOPHOLE CLOSED / GLOBAL REGULARITY NOT PROVED.**