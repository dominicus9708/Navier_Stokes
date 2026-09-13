# M19-245 — The no-slip layer has a passive Dirichlet-to-Neumann impedance and cannot self-replenish unit return

**Date:** 2026-09-14  
**Status:** ACTIVE CALCULATION / BOUNDARY-LAYER IMPEDANCE REDUCTION

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Purpose

M19-237 identified the natural no-slip layer thickness

\[
d_{BL}\asymp\frac\nu R
\]

and the leading profile

\[
f(z)=1-e^{-z},
\qquad
z=\frac{R}{2\nu}(R-r).
\]

M19-244 shows that on the radial-free critical branch the order-one Gaussian background-transport defect disappears, leaving the poloidal boundary-return channel as the main shell mechanism.

This module converts the M19-237 profile into a leading Dirichlet-to-Neumann law and its associated dissipation.

## 2. Outer tangential amplitude and inner matching

Let \(d=R-r\ge0\) be inward distance from the sphere and let

\[
z=\frac{R}{2\nu}d.
\]

Let \(a_T(s,\omega)\) denote the outer tangential velocity amplitude to which the inner layer matches. The leading tangential inner profile is

\[
\boxed{
w_T(d,s,\omega)
=a_T(s,\omega)\left(1-e^{-z}\right).
}
\]

Then

\[
w_T(0)=0,
\qquad
w_T(d)\to a_T
\quad(z\to\infty).
\]

## 3. Leading Dirichlet-to-Neumann law

Because

\[
\partial_d z=\frac{R}{2\nu},
\]

we have

\[
\partial_d w_T
=
\frac{R}{2\nu}a_Te^{-z}.
\]

The outward normal derivative on \(S_R\) is \(\partial_n=\partial_r=-\partial_d\). Hence

\[
\boxed{
\partial_nw_T\big|_{S_R}
=-\frac{R}{2\nu}a_T.
}
\]

Equivalently, the leading boundary-layer Dirichlet-to-Neumann operator is the negative scalar impedance

\[
\boxed{
\Lambda_{BL}(R)
=-\frac{R}{2\nu}I
}
\]

on the tangential outer amplitude.

The sign is dissipative: an outer tangential amplitude produces an opposing boundary shear.

## 4. Exact leading normal-gradient dissipation

At leading order,

\[
|\partial_dw_T|^2
=
\frac{R^2}{4\nu^2}|a_T|^2e^{-2z}.
\]

Using

\[
dd=\frac{2\nu}{R}dz,
\qquad
\int_0^\infty e^{-2z}dz=\frac12,
\]

the viscous normal-gradient dissipation per unit boundary area is

\[
\begin{aligned}
\nu\int_0^\infty|\partial_dw_T|^2dd
&=
\nu\frac{R^2}{4\nu^2}|a_T|^2
\frac{2\nu}{R}\frac12\\
&=
\frac R4|a_T|^2.
\end{aligned}
\]

Therefore

\[
\boxed{
\mathcal D_{BL}^{(0)}(s)
=
\frac R4
\int_{S_R}|a_T(s,\omega)|^2dS.
}
\]

Curvature corrections are relatively \(O(\nu/R^2)\) across the \(d\sim\nu/R\) layer and are lower order in the expanding-cavity limit.

## 5. Boundary shear and M19-235 are quantitatively compatible

The same leading profile gives

\[
\boxed{
\int_{S_R}|\partial_nw_T|^2dS
=
\frac{R^2}{4\nu^2}
\int_{S_R}|a_T|^2dS.
}
\]

M19-235 requires, along an escaping unit mode,

\[
\liminf_{j\to\infty}
\frac1{R_j}
\int_0^{S_j}\int_{S_{R_j}}|\partial_nw_j|^2dSds
\ge\frac1{8\nu^2}.
\]

If the leading layer profile carries the asymptotic boundary shear, then necessarily

\[
\boxed{
\liminf_{j\to\infty}
R_j
\int_0^{S_j}\int_{S_{R_j}}|a_{T,j}|^2dSds
\ge\frac12.
}
\]

Consequently its leading viscous layer dissipation satisfies

\[
\boxed{
\liminf_{j\to\infty}
\int_0^{S_j}\mathcal D_{BL,j}^{(0)}(s)ds
\ge\frac18.
}
\]

This is consistent with, but does not exhaust, the total M19-232 viscous currency

\[
\nu\int_0^{S_j}\|\nabla w_j\|_2^2ds
\to\frac14.
\]

The constants therefore fit the same boundary-layer architecture rather than contradicting it.

## 6. The no-slip layer is passive

The leading inner ODE

\[
f_{zz}+f_z=0
\]

contains no positive-energy source. The layer receives an outer amplitude \(a_T\), enforces \(w_T=0\) at the wall, and pays the positive dissipation

\[
\frac R4\|a_T\|_{L^2(S_R)}^2.
\]

Thus

\[
\boxed{
\text{the }\nu/R\text{ no-slip layer is a passive dissipative load, not a unit-return source.}
}
\]

A relative unit multiplier must therefore replenish this loss from the outer shell/bulk coupling.

## 7. Floquet/time and angular effects are subleading in the inner normal scale

The leading inner diffusion and similarity-normal-drift terms are both of order

\[
\frac{R^2}{\nu}.
\]

By contrast, an \(O(1)\) relative-period frequency, fixed angular derivative, or remote \(O(r^{-2})\) background gradient enters at order \(O(1)\) or smaller before rescaling.

Hence these effects perturb the leading impedance only at relative order \(O(\nu/R^2)\) under the retained bounded-frequency/angular-mode assumptions.

This statement is a scale separation, not yet a uniform operator-resolvent theorem. If angular frequency or time frequency decompactifies with \(R\), that is instead assigned to the existing scaled-derivative/frequency decompactification branch.

## 8. Consequence for the radial-free shell frontier

Combining M19-244 and the passive impedance law:

- leading radial transport cannot replenish the shell when \(A_r=0\);
- the inner no-slip layer itself only dissipates;
- remote bulk strain/mixing is lower order at coefficient level;
- therefore an \(O(1)\)-period unit return must use a nontrivial radial/poloidal outer-shell pressure transfer, or leave the bounded-frequency/compact shell regime.

The refined target is

\[
\boxed{
\mathcal T_{shell}^{pol-work}:
\text{quantify the radial/poloidal pressure work required to replenish the passive }\nu/R\text{ boundary impedance over one period.}
}
\]

## 9. Scope firewall

The leading impedance law does not by itself exclude a coupled cavity eigenmode. A nonnormal outer shell can in principle feed a passive boundary layer while maintaining an exact relative-periodic return.

Therefore

\[
\boxed{
\text{passive boundary impedance}
\neq
\text{global unit-multiplier exclusion}.
}
\]

The next step is a localized distance-to-wall energy moment that exposes the amount of pressure/radial work required for such replenishment.
