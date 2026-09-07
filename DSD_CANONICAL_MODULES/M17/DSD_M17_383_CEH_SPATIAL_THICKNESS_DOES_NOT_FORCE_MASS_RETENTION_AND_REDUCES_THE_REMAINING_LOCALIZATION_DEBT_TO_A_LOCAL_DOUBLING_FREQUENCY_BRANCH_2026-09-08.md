# DSD M17-383 — CE-H spatial thickness does not force mass retention and reduces the remaining localization debt to a local doubling/frequency branch

Date: 2026-09-08  
Canonical ID: **M17-383**

Status: **ACTIVE NO-GO / MASS-RETENTION REDUCTION / M17-298 LOCALIZATION AUDIT**

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Input from M17-382

On the exact CE-H branch,

\[
\Delta W=\kappa W,
\qquad
\nabla\cdot W=0.
\]

M17-382 shows that if the intrinsic coefficient scale is

\[
r\sim |\kappa|^{-1/2}
\]

and

\[
r^3|\nabla\kappa|\le G_*,
\]

then a coefficient-core point lies in a genuine own-scale ball

\[
B_{c_*r}(x_0)
\]

on which

\[
|\kappa|\asymp r^{-2}
\]

and hence, for every measurable subball,

\[
\int_{B'}|\Delta W|^2
\asymp
r^{-4}\int_{B'}|W|^2.
\]

The remaining issue is whether a fixed fraction of the outer `L2` mass must remain in a concentric inner ball.

## 2. Normalize one own-scale ball

Let

\[
R=c_*r
\]

and introduce

\[
z=\frac{x-x_0}{r},
\qquad
V(z)=W(x_0+rz),
\qquad
a(z)=r^2\kappa(x_0+rz).
\]

Then

\[
\boxed{\Delta_zV=a(z)V,}
\qquad
\nabla_z\cdot V=0,
\]

with

\[
|a|\asymp1,
\qquad
|\nabla_za|=r^3|\nabla\kappa|\le G_*.
\]

Thus the mass-retention problem is a scale-free local elliptic problem.

## 3. Exact local doubling deficit

Fix

\[
0<\theta<1.
\]

For a nonzero outer mass define

\[
E(s):=\int_{B_s(x_0)}|W|^2dx
\]

and the `theta`-doubling deficit

\[
\boxed{
\mathfrak D_\theta(x_0,R)
:=
\log\frac{E(R)}{E(\theta R)}.
}
\]

Equivalently define the normalized doubling index

\[
\boxed{
\mathfrak N_\theta(x_0,R)
:=
\frac{\mathfrak D_\theta(x_0,R)}{\log(1/\theta)}.
}
\]

This is only a local mass-ratio descriptor; no monotonicity theorem is assumed here.

The desired mass retention

\[
E(\theta R)\ge cE(R)
\]

is exactly equivalent to

\[
\mathfrak D_\theta(x_0,R)\le \log(1/c).
\]

Therefore a uniform bound on the local doubling deficit immediately closes the inner/mid/outer mass-retention step.

## 4. Bounded local doubling gives the M17-251 packet

Suppose

\[
\mathfrak D_\theta(x_0,R)\le D_*<\infty.
\]

Then

\[
\boxed{
E(\theta R)
\ge e^{-D_*}E(R).
}
\]

Since M17-382 gives

\[
|\kappa|\asymp r^{-2}
\]

on the whole own-scale ball,

\[
H(\theta R)
:=
\int_{B_{\theta R}(x_0)}|\Delta W|^2dx
\asymp
r^{-4}E(\theta R).
\]

Hence

\[
\boxed{
r^4\frac{H(\theta R)}{E(R)}
\gtrsim e^{-D_*}.}
\]

Thus bounded local doubling produces the genuine scale-comparable inner/outer packet required by the late M17 packet machinery.

## 5. Coefficient regularity alone cannot bound the doubling deficit

The missing implication

\[
|a|+|\nabla a|\le C
\quad\Longrightarrow\quad
\mathfrak D_\theta\le C'
\]

is false without additional information on the solution.

This can be seen inside the same divergence-free CE-H elliptic class.

Take the normalized constant coefficient

\[
\boxed{\kappa=-1.}
\]

Then

\[
\nabla\kappa=0
\]

and the spatial-thickness hypothesis is satisfied maximally.

Let `psi_l` be a regular scalar Helmholtz mode

\[
\Delta\psi_l=-\psi_l
\]

with spherical-harmonic degree `l`. Near the origin,

\[
\psi_l(x)
=
P_l(x)+O(|x|^{l+2}),
\]

where `P_l` is a nonzero homogeneous harmonic polynomial of degree `l`.

Choose a constant vector `a` so that the leading curl is nonzero and define

\[
\boxed{
W_l:=\nabla\times(\psi_l a).
}
\]

Then

\[
\nabla\cdot W_l=0
\]

and, because curl commutes with the Laplacian,

\[
\boxed{
\Delta W_l=-W_l.
}
\]

Thus `W_l` satisfies exact divergence-free CE-H with constant `kappa=-1`.

Its leading nonzero term has degree `l-1`, so near the origin

\[
|W_l(x)|\sim |x|^{l-1}
\]

in the nondegenerate angular directions and

\[
E_l(s)
\asymp
s^{2l+1}
\]

at sufficiently small fixed normalized radius.

Consequently,

\[
\boxed{
\frac{E_l(\theta R)}{E_l(R)}
\asymp
\theta^{2l+1}
\longrightarrow0
\qquad(l\to\infty).
}
\]

Equivalently,

\[
\boxed{
\mathfrak N_\theta(W_l;0,R)
\to\infty.
}
\]

Hence even `nabla kappa=0` does not yield a uniform own-scale mass-retention constant.

After the physical rescaling `x=r_0 z`, the same family has

\[
\kappa=-r_0^{-2},
\qquad
r_0^3|\nabla\kappa|=0,
\]

so the obstruction exists at every intrinsic coefficient scale.

## 6. Scope of the no-go

The construction above is **not** asserted to be a full Navier--Stokes blow-up profile.

Its role is narrower and rigorous:

> the local hypotheses used by M17-382 — exact CE-H, divergence-free field, correct coefficient scale, and bounded scale-normalized coefficient gradient — do not by themselves imply the required inner/outer `L2` mass retention.

Therefore any future proof of retention must use additional Navier--Stokes dynamics, genealogy, amplitude/flux information, or a quantitative frequency/doubling constraint.

## 7. Revised exact localization split

The M17-382 `mass descent/nodal concentration` exit can now be sharpened to

\[
\boxed{
\begin{aligned}
H_{own\text{-}scale\ spatial\ cell}
\Longrightarrow{}&
H_{bounded\ local\ doubling\Rightarrow packet}\\
&\lor
G_{local\ doubling/frequency\ decompactification}.
\end{aligned}
}
\]

Thus the CE-H part of M17-298 becomes

\[
\boxed{
\begin{aligned}
G_{M17\text{-}298}
\Longrightarrow{}&
H_{true\ scale\text{-}comparable\ packet}\\
&\lor G_{r^3|\nabla\kappa|\ decompactification}\\
&\lor G_{local\ doubling/frequency\ decompactification}\\
&\lor G_{coefficient/interface/domain\ degeneration}.
\end{aligned}
}
\]

The raw-`H2` ownership problem remains closed on the M17-381/382 compact branch; the unresolved inner localization is now a solution-frequency problem rather than a coefficient-scale allocation problem.

## 8. Relation to M17-365/366

M17-365 gives a local Sobolev absorption gate for small critical negative-`kappa` mass, while M17-366 classifies moving critical coefficient concentration.

M17-383 shows that a separate variable is still required even when the coefficient itself is perfectly regular: the solution can have high local vanishing order inside a smooth own-scale coefficient cell.

Therefore `coefficient concentration` and `solution doubling/frequency` must not be silently identified.

A future closure may connect them through the full Navier--Stokes dynamics, but that connection is presently OPEN.

## 9. DSD audit role

The DSD contribution is a dependency audit:

- M17-381 solved scale ownership at measure level;
- M17-382 solved spatial realization of the coefficient scale on the normalized-gradient compact branch;
- M17-383 checks whether spatial realization automatically implies state-mass realization and proves that it does not.

This prevents a hidden replacement of

\[
\text{coefficient thickness}
\]

by

\[
\text{solution mass thickness}.
\]

## 10. Audit verdict

**PASS — necessary no-go and exact frontier refinement.**

The correct next variable is the local doubling/frequency/vanishing-order structure of `W` on M17-382 own-scale cells.

The next high-value task is to determine whether the full CE-H/Navier--Stokes dynamics supplies a quantitative payer for

\[
\mathfrak N_\theta\to\infty,
\]

for example through strain, material transport, genealogy change, amplitude-threshold flux, or another already certified critical ledger.

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
