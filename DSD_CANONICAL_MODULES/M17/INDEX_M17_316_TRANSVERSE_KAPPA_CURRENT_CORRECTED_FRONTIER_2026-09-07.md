# M17 corrected frontier companion — through M17-316

Date: 2026-09-07  
Status: **AUTHORITATIVE COMPANION FOR THE TRANSVERSE-`KAPPA` CURRENT FRONTIER AFTER M17-313**

This companion supplements the M17-314 corrected frontier and records the two immediate downstream repairs.

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## M17-315 — corrected interpretation of M17-147

The exact full-gradient equation for

\[
G=\nabla\kappa
\]

survives M17-313, but exact CE-H imposes

\[
\boxed{G\cdot\xi=0.}
\]

Thus `G` is purely transverse.

Under the M17-147 quiet high-jet reduction,

\[
D_BG
=
L_\rho G
+\left(2\nabla^2\log\rho-\frac32I\right)G
+o(1).
\]

At an interior maximum of `|G|`, only the largest Hessian eigenvalue on `xi^perp` matters:

\[
\boxed{
\lambda_\perp(\log\rho)
:=
\max_{v\perp\xi,|v|=1}
 v\cdot\nabla^2\log\rho\,v.
}
\]

If

\[
\lambda_\perp\le\frac34-\delta,
\]

then order-one transverse `|grad kappa|` cannot be recurrently regenerated in the controlled quiet interior.

Therefore M17-147 is retained as a **transverse coefficient-convexity gate**, not as a longitudinal generic-fold theorem.

## M17-316 — constitutive diffusion is exactly transverse

M5-682 gives

\[
h=D_B\kappa
=L_\rho\kappa+L_\rho\sigma-\kappa+\mathcal R_{geom},
\]

with

\[
L_\rho f=\rho^{-2}\nabla\cdot(\rho^2\nabla f).
\]

Because

\[
\nabla\kappa=P_\perp\nabla\kappa,
\qquad
P_\perp=I-\xi\otimes\xi,
\]

one has the exact identity

\[
\boxed{
L_\rho\kappa
=
\rho^{-2}\nabla\cdot
\left(
\rho^2P_\perp\nabla\kappa
\right).
}
\]

Thus the CE-H multiplier diffusion is purely cross-vortex in divergence form.

At `kappa=0`,

\[
\boxed{
h
=
\rho^{-2}\nabla\cdot(\rho^2P_\perp\nabla\kappa)
+L_\rho\sigma
+\mathcal R_{geom}.}
\]

The quantitative material current from M17-314 therefore has no longitudinal coefficient-recharge channel.

Likewise M5-683's positive diffusion term satisfies

\[
A_{\kappa\kappa}
=
\int\delta(k-\kappa)
\chi\rho^2
|P_\perp\nabla\kappa|^2dy,
\]

and its mixed term uses only transverse strain gradient:

\[
\nabla\kappa\cdot\nabla\sigma
=
\nabla\kappa\cdot P_\perp\nabla\sigma.
\]

Therefore the current late coefficient branch is

\[
\boxed{
\begin{aligned}
H_{\overline G(0)<0}
\Longrightarrow{}&
H_{transverse\ kappa\ diffusion}\\
&\lor H_{transverse\ strain\ work}\\
&\lor H_{CEH\ geometry}\\
&\lor H_{cutoff/nodal\ transition}\\
&\lor G_{boundary/noncompact/import}.
\end{aligned}
}
\]

## Current audit firewall

- `D_xi kappa` is identically zero on exact regular CE-H.
- Nonzero full `grad kappa` remains allowed but is purely transverse.
- M17-144--146 cannot be used to claim order-one longitudinal `kappa` fold recharge.
- M17-147 full-gradient PDE survives only with transverse reinterpretation.
- Pure-flux and enstrophy-weighted `kappa` currents remain distinct measures.
- M17-304 remains superseded by M17-306.
- Global regularity remains unproved.

## Next target

The next calculation should combine

\[
\boxed{\overline G_{flux}(0)\le-d_{flux}<0}
\]

with the transverse constitutive law and determine whether the exact M5-682/683/688 PDE can sustain a fixed same-material zero-level current without forcing

\[
\boxed{
\lambda_\perp(\nabla^2\log\rho)\ge\frac34-o(1),
}

persistent transverse strain work, nodal concentration, or noncompact boundary import.
