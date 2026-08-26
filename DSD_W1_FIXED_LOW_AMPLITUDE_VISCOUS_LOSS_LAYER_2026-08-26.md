# DSD W1 Fixed Low-Amplitude Viscous-Loss Layer

Date: 2026-08-26

Status: **COMPACT MINIMALITY AND UNIFORM W1 TAIL/PRESSURE CONTROL UPGRADE THE BOUNDARY VALUE `G_BAR(0+)=-NU<Z>` TO A FIXED-WIDTH NEGATIVE LOW-AMPLITUDE LAYER / THE INTERIOR PRESSURE PUMP MUST OVERCOMPENSATE BOTH THIS VISCOUS LOSS AND THE POSITIVE WEAK-L3 DEFECT MASS / GLOBAL REGULARITY UNPROVED.**

## 1. Uniform enstrophy floor on the minimal set

Let

\[
Z(U)=\int|\Omega_U|^2dY.
\]

`Z` is continuous on the compact W1 minimal set. If `Z(U)=0`, then `Omega=0`; with incompressibility, decay, and the whole-space W1 class this forces `U=0`, which is excluded by the equilibrium gate.

Therefore

\[
\boxed{
Z_*:=\min_{U\in M}Z(U)>0.
}
\]

## 2. Uniform low-amplitude limits

The W1 smooth finite core and uniform critical far-tail estimates imply, in the regularized threshold sense,

\[
J_P(\lambda,U)\to0
\]

and

\[
D_\lambda(U)\to Z(U)
\]

as `lambda downarrow0`, uniformly on the compact W1 class.

The pressure convergence uses the finite-core smoothness plus the far estimates `U=O(r^-1)`, `grad P=O(r^-3)` / the repository's pressure-tail localization; the viscous convergence uses the finite enstrophy tail and smooth threshold regularization.

## 3. Fixed negative layer

Hence there exists

\[
\boxed{\lambda_{loss}>0}
\]

such that for all sufficiently small regularized levels in

\[
0<\lambda\le\lambda_{loss},
\]

one has at the invariant-average level

\[
\boxed{
\bar G(\lambda)
=
\left\langle J_P(\lambda)-\nu D_\lambda\right\rangle_\mu
\le
-\frac{\nu Z_*}{2}<0.
}
\]

Thus the low-amplitude boundary is preceded by a genuine viscous-loss layer of fixed normalized width.

## 4. Quantified overcompensation requirement

The total net gain is

\[
\int_0^{A_*}\bar G(\lambda)d\lambda
=\frac{\mathscr R_3}{6}>0.
\]

The low-loss layer contributes at most

\[
\int_0^{\lambda_{loss}}\bar G(\lambda)d\lambda
\le
-\frac{\nu Z_*}{2}\lambda_{loss}.
\]

Therefore the positive part of the interior pump must satisfy

\[
\boxed{
\int_{\lambda_{loss}}^{A_*}
\bar G_+(\lambda)d\lambda
\ge
\frac{\mathscr R_3}{6}
+
\frac{\nu Z_*}{2}\lambda_{loss}.
}
\]

The finite-amplitude pump therefore pays not only the endpoint defect but also the unavoidable low-amplitude viscous loss.

## 5. DSD chain

The realized gain profile has the forced topology

\[
\boxed{
\text{fixed low-amplitude viscous-loss layer}
\longrightarrow
\text{stronger interior pressure-pump layer}
\longrightarrow
\text{upper-amplitude termination}
}
\]

with positive total mass after cancellation.

## 6. Consequence

This strengthens the fixed-pump-level witness and rules out scalar gain profiles that are positive or neutral all the way down to the low-amplitude boundary.

A final closure would require showing that the finite-core pressure Poisson geometry cannot provide the quantified overcompensation demanded above on a compact recurrent W1 class.

No such theorem is proved here.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
