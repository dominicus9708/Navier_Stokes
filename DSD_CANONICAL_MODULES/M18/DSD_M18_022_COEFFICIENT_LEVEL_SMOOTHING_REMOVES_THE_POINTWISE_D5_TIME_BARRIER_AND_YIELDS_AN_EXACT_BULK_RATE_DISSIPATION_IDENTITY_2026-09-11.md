# M18-022 — Coefficient-level smoothing removes the pointwise D5 time barrier and yields an exact bulk rate-dissipation identity

**Date:** 2026-09-11  
**Status:** ACTIVE DSD ANALYSIS / BULK-SMOOTHING REDUCTION / TEMPORAL-JET DESCENT

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Purpose

M18-021 showed that differentiating a single level flux

\[
F(s,t)=\int_{\{\kappa=s\}}\rho^2|\nabla\kappa|\,dS
\]

introduces

\[
\rho^2\partial_n h,
\qquad h:=D_t\kappa,
\]

which naturally reaches a third coefficient jet and therefore a D5-type vorticity derivative if controlled pointwise.

This module tests whether that escalation is intrinsic.

The result is:

\[
\boxed{
\text{smooth across coefficient levels first, then differentiate in time; }\nabla h
\text{ disappears by bulk integration by parts.}
}
\]

Thus the pointwise D5 barrier is not universal on a macroscopic coefficient-width branch.

## 2. Smoothed coefficient-level observable

Fix one physical record and a time-independent reference coefficient width

\[
\delta_0>0.
\]

Choose

\[
\psi\in C_c^1((-1,1)),
\qquad
\psi\ge0,
\]

and set

\[
\phi(s):=\psi\!\left(\frac{s}{\delta_0}\right).
\]

Define

\[
\boxed{
B_\phi(t)
:=
\int_{\mathbb R^3}
\phi(\kappa)\rho^2|\nabla\kappa|^2dx.
}
\]

By coarea,

\[
\boxed{
B_\phi(t)=\int_{\mathbb R}\phi(s)F(s,t)\,ds.
}
\]

Hence \(B_\phi\) is a smooth coefficient-level average of the M18-016--021 flux.

## 3. Scaling audit

Under the physical record scaling,

\[
\rho_R=R^2\rho,
\qquad
\kappa_R=R^2\kappa,
\qquad
\nabla\kappa_R=R^3\nabla\kappa,
\]

with

\[
\delta_{0,R}=R^2\delta_0.
\]

Therefore

\[
\boxed{B_{\phi,R}=R^7B_\phi}
\]

and

\[
\boxed{\partial_sB_{\phi,R}=R^9\partial_tB_\phi.}
\]

After time integration, \(B_\phi\) is in the same \(R^{-5}\) ancestry class as the M17-445 first-coefficient-jet/D3 resource.

## 4. Material derivative

Write

\[
g:=|\nabla\kappa|,
\qquad
n:=\frac{\nabla\kappa}{g},
\qquad
h:=D_t\kappa,
\qquad
a_n:=n\cdot(\nabla u)n.
\]

On exact CE-H,

\[
D_t\rho=(\sigma+\nu\kappa)\rho,
\]

and

\[
D_tg=\partial_nh-ga_n.
\]

Since

\[
D_t\phi(\kappa)=\phi'(\kappa)h,
\]

incompressibility gives

\[
\begin{aligned}
\dot B_\phi
={}&
\int \phi' h\rho^2g^2dx\\
&+2\int \phi(\sigma+\nu\kappa-a_n)\rho^2g^2dx\\
&+2\int \phi\rho^2\nabla\kappa\cdot\nabla h\,dx.
\end{aligned}
\]

The last term is the apparent high-jet obstruction.

## 5. Exact removal of \(\nabla h\)

Integrate the last term by parts:

\[
2\int
\phi\rho^2\nabla\kappa\cdot\nabla h\,dx
=
-2\int
h\,\nabla\cdot(\phi\rho^2\nabla\kappa)\,dx.
\]

The divergence is

\[
\boxed{
\nabla\cdot(\phi\rho^2\nabla\kappa)
=
\phi'\rho^2g^2
+
\phi\left(
2\rho\nabla\rho\cdot\nabla\kappa
+
\rho^2\Delta\kappa
\right).
}
\]

Hence

\[
\begin{aligned}
\dot B_\phi
={}&
2\int
\phi(\sigma+\nu\kappa-a_n)\rho^2g^2dx\\
&-
\int
\phi'h\rho^2g^2dx\\
&-
4\int
\phi\rho h\nabla\rho\cdot\nabla\kappa\,dx\\
&-
2\int
\phi\rho^2h\Delta\kappa\,dx.
\end{aligned}
\]

Thus

\[
\boxed{
\nabla h\quad\text{has disappeared completely.}
}
\]

## 6. Weighted-operator compression

Recall

\[
L_\rho\kappa
=
\rho^{-2}\nabla\cdot(\rho^2\nabla\kappa)
=
\Delta\kappa
+2\nabla\log\rho\cdot\nabla\kappa.
\]

Therefore

\[
\boxed{
2\rho\nabla\rho\cdot\nabla\kappa
+
\rho^2\Delta\kappa
=
\rho^2L_\rho\kappa.
}
\]

The last two terms combine to

\[
-2\int
\phi\rho^2hL_\rho\kappa\,dx.
\]

Thus

\[
\boxed{
\dot B_\phi
=
2\int
\phi(\sigma+\nu\kappa-a_n)\rho^2g^2dx
-
\int
\phi'h\rho^2g^2dx
-
2\int
\phi\rho^2hL_\rho\kappa\,dx.
}
\]

## 7. Exact rate-dissipation identity

M17-339 gives

\[
\boxed{
h=L_\rho\kappa+L_\rho\sigma+\mathcal R_{\rm geom}.}
\]

Set

\[
A:=L_\rho\kappa,
\qquad
C:=L_\rho\sigma+\mathcal R_{\rm geom},
\qquad
h=A+C.
\]

The algebraic identity

\[
2hA=A^2+h^2-C^2
\]

is exact.

Therefore

\[
\boxed{
\begin{aligned}
\dot B_\phi
&+
\int\phi\rho^2
\left(
|L_\rho\kappa|^2+|D_t\kappa|^2
\right)dx\\
={}&
2\int
\phi(\sigma+\nu\kappa-a_n)\rho^2|\nabla\kappa|^2dx\\
&-
\int
\phi'(\kappa)(D_t\kappa)\rho^2|\nabla\kappa|^2dx\\
&+
\int
\phi\rho^2
|L_\rho\sigma+\mathcal R_{\rm geom}|^2dx.
\end{aligned}
}
\]

This is the main M18-022 identity.

The left-hand side contains two nonnegative bulk channels:

\[
\boxed{
\rho^2|L_\rho\kappa|^2,
\qquad
\rho^2|D_t\kappa|^2.
}
\]

No third coefficient jet appears.

## 8. Remaining channels

The right-hand side contains only three typed channels.

### A. Strain / normal-stretch channel

\[
\mathcal S_\phi
:=
2\int
\phi(\sigma+\nu\kappa-a_n)\rho^2|\nabla\kappa|^2dx.
\]

If \(|\sigma|+|a_n|+|\kappa|\) is uniformly bounded, this is controlled by \(B_\phi\), whose spacetime resource is already in the \(R^{-5}\) first-coefficient-jet class.

### B. Coefficient-cutoff current

\[
\boxed{
\mathcal C_\phi
:=-\int
\phi'(\kappa)(D_t\kappa)\rho^2|\nabla\kappa|^2dx.
}
\]

This is supported only in the coefficient collars where the cutoff varies. It is not automatically absorbed by the existing first-jet ledger.

### C. Strain/geometry source square

\[
\boxed{
\mathcal R_\phi
:=
\int
\phi\rho^2
|L_\rho\sigma+\mathcal R_{\rm geom}|^2dx.
}
\]

No existing M17/M18 ancestry ledger has yet been certified for this full squared source.

## 9. Conditional consequence

If on a retained macroscopic-width exact CE-H family:

1. strain, normal strain, and coefficient are uniformly compact;
2. the cutoff current is spacetime integrable;
3. the squared strain/geometry source is spacetime integrable;
4. the endpoint values of \(B_\phi\) are controlled;

then the identity gives finite spacetime control of

\[
\boxed{
\iint
\phi\rho^2|D_t\kappa|^2dxdt
}
\]

and

\[
\boxed{
\iint
\phi\rho^2|L_\rho\kappa|^2dxdt.
}
\]

This is conditional; items 2--3 remain open.

## 10. Relation to level-width collapse

The bulk smoothing requires a nontrivial coefficient band.

If the useful level width \(\ell\) collapses, M18-019 already gives, up to the explicit compactness exits,

\[
P_\ell\gtrsim\frac{J}{\ell}
\qquad\text{or}\qquad
\Lambda_{\kappa,\delta}\gtrsim\frac{\delta}{\ell}.
\]

Thus

\[
\boxed{
G_{\rm temporal\ flux\ shape}
\Longrightarrow
G_{\rm level\text{-}width\ collapse}
\lor
G_{\rm bulk\ smoothed\ rate\ identity}.
}
\]

The first branch is already owned by M18-019; the second avoids the pointwise D5 escalation.

## 11. Derivative-order and representation verdict

Every term in the main identity scales as \(R^9\) instantaneously, so the descent is dimensionally consistent.

M18-022 does **not** claim a D4 or D5 ancestry ledger for \(D_t\kappa\). It only shows that the third coefficient jet is absent from the correct bulk-smoothed temporal identity.

M17-339 supplies the exact physical source formula, but the substantive M17-463 rule remains:

\[
\boxed{
\text{exact source provenance}\neq\text{certified payer estimate}.
}
\]

Therefore the source square remains open rather than being assigned to a lower ledger by analogy.

## 12. Updated temporal branch

The M18-021 temporal-flux branch is refined to

\[
\boxed{
\begin{aligned}
G_{\rm temporal\ flux\text{-}shape}
\Longrightarrow{}&
G_{\rm level\text{-}width\ collapse}\\
&\lor G_{\rm coefficient\ cutoff\ current}\\
&\lor G_{\rm strain/geometry\ source\ square}\\
&\lor G_{\rm strain/normal\text{-}stretch\ decompactification}\\
&\lor G_{\rm controlled\ bulk\ coefficient\ rate}.
\end{aligned}
}
\]

The direct D5 branch is therefore demoted from a universal obstruction to a pointwise-level formulation hazard.

## 13. Audit verdict

**Certified:** coefficient-level smoothing removes \(\nabla D_t\kappa\) exactly and produces a genuine bulk rate-dissipation identity with positive \(|D_t\kappa|^2\) and \(|L_\rho\kappa|^2\) channels.

**Not certified:** a finite ancestry ledger for these new rate channels, control of the cutoff current, control of the squared strain/geometry source, an ancestry contradiction, or global regularity.

## 14. Next target

M18-023 should audit

\[
\mathcal C_\phi
=-\int
\phi'(\kappa)(D_t\kappa)\rho^2|\nabla\kappa|^2dx
\]

using adapted cutoffs, collar decomposition, and weighted inequalities.

The goal is to absorb it into the favorable \(\rho^2|D_t\kappa|^2\) rate term plus the existing first-coefficient-jet resource, or else isolate an explicit higher-gradient collar exit without silently moving to D5.
