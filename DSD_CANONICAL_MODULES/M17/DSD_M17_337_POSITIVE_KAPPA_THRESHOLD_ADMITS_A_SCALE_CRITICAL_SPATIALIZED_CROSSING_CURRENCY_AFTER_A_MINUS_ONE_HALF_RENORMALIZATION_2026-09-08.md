# DSD M17-337 — Positive kappa threshold admits a scale-critical spatialized crossing currency after a^(-1/2) renormalization

Date: 2026-09-08  
Canonical ID: **M17-337**

Status: **ACTIVE CRITICAL-PHYSICALIZATION CONSTRUCTION**

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Motivation

M17-326 found a record-scale-critical **pure material-flux** crossing currency at `kappa=0`.

M17-327 showed that ordinary enstrophy/spatial physicalization introduces one positive power of the record scale through the line weight.

M17-336 now conditionally forces the transferred zero-current past a fixed positive threshold, in particular `a=3/2`, for large record factors.

At a positive threshold, the threshold value itself supplies exactly the missing scale needed to remove the one-power physicalization loss.

## 2. Spatialized one-sided crossing activity

Let

\[
\rho=|\Omega|
\]

in the current CE-H representation and

\[
h:=D_B\kappa.
\]

For `a>0`, define the enstrophy-weighted downward crossing activity

\[
\boxed{
\mathcal C_{E,-}^{(a)}(I)
:=
\int_I\!\int
h_-\,\delta(\kappa-a)\,\rho^2\,dy\,d\theta.
}
\]

This is a genuine spacetime spatial quantity.

In material vortex-line coordinates, because `kappa` and `h` are line-constant on exact CE-H,

\[
\rho^2dy
\longleftrightarrow
L_\rho\,d\Phi,
\qquad
L_\rho:=\int_\Gamma\rho\,ds,
\]

so equivalently

\[
\boxed{
\mathcal C_{E,-}^{(a)}
=
\int h_-\delta(\kappa-a)L_\rho\,d\Phi\,d\theta.
}
\]

## 3. Scaling of the unrenormalized spatial current

Under a parabolic record scaling by `R`,

\[
\rho_R=R^2\rho,
\qquad
\kappa_R=R^2\kappa,
\qquad
h_R=R^4h,
\]

\[
dy_R=R^{-3}dy,
\qquad
d\theta_R=R^{-2}d\theta.
\]

Transport the positive threshold covariantly:

\[
\boxed{a_R=R^2a.}
\]

Then

\[
\delta(\kappa_R-a_R)
=
R^{-2}\delta(\kappa-a).
\]

Therefore

\[
\begin{aligned}
\mathcal C_{E,-}^{(a_R)}
&\mapsto
R^4\cdot R^{-2}\cdot R^4\cdot R^{-3}\cdot R^{-2}
\mathcal C_{E,-}^{(a)}\\
&=
R\mathcal C_{E,-}^{(a)}.
\end{aligned}
\]

Thus ordinary spatialization is supercritical by exactly one power:

\[
\boxed{
\mathcal C_{E,-}^{(a_R)}
=R\mathcal C_{E,-}^{(a)}.
}
\]

This is the same one-power barrier identified structurally in M17-327.

## 4. Threshold-renormalized spatial currency

Define

\[
\boxed{
\mathcal Q_-^{(a)}(I)
:=
a^{-1/2}
\mathcal C_{E,-}^{(a)}(I).
}
\]

Since

\[
a_R^{-1/2}=R^{-1}a^{-1/2},
\]

we obtain exact cancellation:

\[
\boxed{
\mathcal Q_-^{(a_R)}(I_R)
=
\mathcal Q_-^{(a)}(I).
}
\]

Hence `Q` is a **record-scale-critical spatialized crossing currency**, provided the threshold is transported covariantly with the coefficient scaling.

## 5. Line-coordinate interpretation

Write

\[
\ell_a
:=
\frac{L_\rho}{\sqrt a}.
\]

At the level `kappa=a`,

\[
\boxed{
\mathcal Q_-^{(a)}
=
\int
h_-\delta(\kappa-a)
\ell_a\,d\Phi\,d\theta.
}
\]

Under record scaling,

\[
L_{\rho,R}=RL_\rho,
\qquad
\sqrt{a_R}=R\sqrt a,
\]

so

\[
\boxed{
\ell_{a_R}=\ell_a.
}
\]

Thus the dimensionless residence factor

\[
\boxed{L_\rho/\sqrt a}
\]

is exactly the scale-invariant bridge between pure-flux crossing and spatial/enstrophy crossing at a positive coefficient level.

## 6. Application to the M17-336 resonant current

M17-336 conditionally gives, after exact same-ensemble record transfer and for large `R`,

\[
-\overline G_R(3/2)
\gtrsim R^2d.
\]

The one-sided downward pure-flux activity at that level is at least the magnitude of the signed current.

Therefore, on any branch where the activity-weighted dimensionless line residence satisfies

\[
\boxed{
\frac{L_\rho}{\sqrt{3/2}}
\ge\ell_*>0
}
\]

on a fixed fraction of the downward crossing population,

\[
\boxed{
\mathcal Q_-^{(3/2)}
\gtrsim
\ell_*\times
\text{downward pure-flux crossing activity}.
}
\]

Thus the M17-336 current can be converted into a **spatial and scale-critical** charge without the M17-327 one-power loss.

If the lower residence bound fails, retain the explicit branch

\[
\boxed{
G_{vanishing\ dimensionless\ line\ residence}.
}
\]

## 7. Why a>0 is essential

At `a=0`, the factor

\[
a^{-1/2}
\]

is singular.

Thus M17-337 does not replace the M17-326 zero-level pure-flux currency.

The logic is instead:

\[
\boxed{
\text{zero level: homogeneous pure-flux critical currency}
}
\]

followed, conditionally via M17-336, by

\[
\boxed{
\text{positive level: threshold-renormalized spatial critical currency}.
}
\]

This is why forcing current away from zero is useful.

## 8. PDE accessibility

Unlike the pure-flux current, the spatialized quantity uses the same `rho^2 dy` weight appearing in the M5-683/M5-688 enstrophy-weighted `kappa` current.

Thus `Q` is positioned to interact directly with the constitutive law

\[
h
=L_\rho\kappa+L_\rho\sigma-\kappa+\mathcal R_{geom}
\]

and the pushed diffusion density

\[
A_{\kappa\kappa}(k)
=
\int\delta(k-\kappa)\chi\rho^2|\nabla\kappa|^2dy.
\]

A finite upper budget for `Q` is **not yet established**.

## 9. DSD-theory role

The useful DSD heuristic is to search for a representation-independent descriptor after identifying the exact scaling defect of the previous descriptor.

Here the one-power spatialization defect is compensated by the only local positive coefficient scale available at the crossing level, `sqrt(a)`.

The canonical proof is the explicit scaling calculation; no DSD axiom is used as a PDE hypothesis.

## 10. Updated critical-transfer frontier

M17-327's statement

\[
\text{pure-flux criticality}
\to
\text{one-power loss under spatialization}
\]

is now sharpened:

\[
\boxed{
\text{at }a>0,
\quad
a^{-1/2}\times\text{spatial crossing activity}
\text{ is exactly scale critical}.
}
\]

Therefore the remaining branches are

\[
\boxed{
H_{critical\ spatialized\ positive\text{-}level\ crossing}
\lor
G_{vanishing\ dimensionless\ line\ residence}
\lor
G_{ensemble/genealogy\ transfer}.
}
\]

The next target is to determine whether the M5-682/683 constitutive current supplies a finite or coercive control of this new critical spatial currency.

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
