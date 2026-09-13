# M19 Current Frontier

**Date:** 2026-09-14  
**Current tip:** **M19-254**  
**Status:** ACTIVE CALCULATION / WHOLE-SPACE TRANSPARENT MOVING-SPHERE + GALILEAN CRITICAL-PAYER FRONTIER / APERIODIC SIGNED FRONTIER OPEN / FINAL ROOT-PROOF CERTIFICATION OPEN

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Canonical policy

M18 remains the frozen audit/reduction family. M19 is the active calculation/closure family. Detailed derivations remain in numbered modules; this file records the current obligations and scope firewalls.

## 2. Global proof tree still open

The repository-wide singularity reduction and `ROOT-CERT` are not finished. Historical non-CE-H branches

\[
CP\!-\!E,\quad CP\!-\!S,\quad CE\!-\!T,\quad Migration
\]

remain unresolved, as do parent-to-late-branch alignment/nonreuse checks and the final beginning-to-end independent audit.

## 3. Aperiodic frontier

M19-196--201 force positive simultaneous W1 severity mean on the retained recurrent-hard lane but do not produce a signed/global contradiction. Therefore

\[
\boxed{\mathcal T_{aper}^{signed}}
\]

remains OPEN.

## 4. Historical bounded-period cavity branch — M19-211--252

M19-211--230 reduced finite hard resonance/adjoint realization to a compact finite-cavity Fredholm problem. M19-231--252 analyzed the imposed no-slip cavity: core/escape, boundary-vorticity localization, shear payer, \(\nu/R\) layer, macroscopic rigidity, Gaussian pressure coupling, passive wall impedance, sublinear shell rigidity, and frozen toroidal/poloidal unit-mode gaps.

M19-253 corrected the whole-space interpretation:

\[
\boxed{\text{no-slip cavity exclusion}\not\Rightarrow\text{whole-space transparent-sphere exclusion}.}
\]

The numbered cavity modules are retained as valid auxiliary diagnostics inside their stated boundary hypotheses, but wall-specific payers/gaps are not the canonical Clay-(A) frontier.

Potentially portable after rederivation are the bulk scaling/curl ideas, weighted energy bookkeeping with the correct fluxes, exact pressure identities, and critical-background asymptotics.

## 5. M19-253 — transparent moving observation sphere

The active geometric object is

\[
\Omega_R(t)=B_R(X(t))\subset\mathbb R^3,
\qquad S_R(t)=\partial B_R(X(t)),
\]

with fixed radius \(R\), boundary velocity \(\dot X\), and no wall boundary condition.

For \(e=|u|^2/2\),

\[
\boxed{
\frac d{dt}\int_{\Omega_R(t)}e
+\nu\int_{\Omega_R(t)}|\nabla u|^2
=
-\int_{S_R(t)}
\left[e(u-\dot X)\cdot n+p\,u\cdot n-\nu\partial_ne\right]dS.
}
\]

The sphere creates no wall dissipation. It records actual advective, pressure, and viscous exchange. Net relative volume flux is zero,

\[
\boxed{\int_{S_R(t)}(u-\dot X)\cdot n\,dS=0,}
\]

while local inward/outward flux need not vanish.

At hypothetical singular scales the canonical primitive is a smooth moving cutoff or a Galilean parabolic cylinder, not a sharp trace.

## 6. M19-253 — exact Galilean epsilon floor

For constant velocity \(V\), define

\[
Q_r^V(z_0)=
\{t_0-r^2<t<t_0,
\ |x-x_0-V(t-t_0)|<r\},
\]

\[
C_V(r)=r^{-2}\int_{Q_r^V}|u-V|^3,
\qquad
D_V(r)=r^{-2}\int_{Q_r^V}|p-(p)_{B_r^V(t)}|^{3/2}.
\]

Standard one-scale epsilon regularity plus exact Galilean covariance gives, by contraposition,

\[
\boxed{
\mathcal T_{GMS}^{\varepsilon}:
\quad z_0\text{ singular}
\Longrightarrow
\forall V,\ \forall r\ll1,
\quad C_V(r)+D_V(r)\ge\varepsilon_*.
}
\]

Equivalently,

\[
\boxed{\inf_{V\in\mathbb R^3}[C_V(r)+D_V(r)]\ge\varepsilon_* .}
\]

This is an inherited reformulation of standard epsilon regularity, not a new epsilon-regularity theorem.

Time-dependent accelerated tracking is separate: \(V(t)=\dot X(t)\) produces the pressure correction \(\dot V(t)\cdot y\).

## 7. M19-254 — exact critical payer and unweighted NO-GO

Finite energy gives the standard whole-space currencies

\[
u\in L_t^\infty L_x^2\cap L_t^2\dot H_x^1,
\qquad
u\in L_{x,t}^{10/3},
\qquad
p\in L_{x,t}^{5/3}.
\]

From the epsilon floor and Hölder, for every fixed constant \(V\),

\[
\boxed{
F_V(r):=
\int_{Q_r^V}
\left(|u-V|^{10/3}+|p|^{5/3}\right)
\ge c\varepsilon_*^{10/9}r^{5/3}.
}
\]

Thus

\[
\boxed{H_V(r):=r^{-5/3}F_V(r)\ge c\varepsilon_*^{10/9}.}
\]

The physical cost \(r^{5/3}\) is geometrically summable on dyadic scales, and the cylinders are nested. Consequently ordinary unweighted \(L^{10/3}+L^{5/3}\) integrability does not contradict the singularity floor. For invoking the global finite-energy integrability it is enough to take the permitted frame \(V=0\).

This is the M19-254 NO-GO:

\[
\boxed{
\text{unweighted finite spacetime integrability}
\not\Rightarrow
\mathcal T_{GMS}^{select}.}
\]

## 8. M19-254 — logarithmically divergent critical Morrey payer

Because the normalized floor holds at every sufficiently small scale,

\[
\int_0^{r_0}H_V(r)\frac{dr}{r}=\infty.
\]

With the backward parabolic distance to the Galilean centerline

\[
\rho_V(x,t)=
\max\left(|x-x_0-V(t-t_0)|,\sqrt{t_0-t}\right),
\]

Tonelli gives the exact kernel identity

\[
\int_0^{r_0}r^{-5/3}F_V(r)\frac{dr}{r}
=
\frac35\int_{Q_{r_0}^V}
\left(|u-V|^{10/3}+|p|^{5/3}\right)
\left(\rho_V^{-5/3}-r_0^{-5/3}\right)dxdt.
\]

Therefore every genuine singular point must satisfy, for every fixed constant \(V\),

\[
\boxed{
\mathcal P_{GMS}^{log}:
\quad
\int_{Q_{r_0}^V(z_0)}
\frac{|u-V|^{10/3}+|p|^{5/3}}
{\rho_V^{5/3}}\,dxdt
=\infty.
}
\]

This is scale invariant and is the first explicitly non-summable whole-space payer extracted from the transparent moving-sphere route.

## 9. New active theorem target

The previous selection target

\[
\mathcal T_{GMS}^{select}
\]

is sharpened to a weighted target:

\[
\boxed{
\mathcal T_{GMS}^{weight}:
\text{existing certified whole-space DSD ledgers force }
\mathcal P_{GMS}^{log}<\infty
\text{ for at least one constant }V.
}
\]

If this is proved for a hypothetical singular point, it contradicts M19-254 immediately. At present

\[
\boxed{\mathcal T_{GMS}^{weight}\text{ is OPEN}.}
\]

The next calculation is to compare the M17/M19 whole-space ancestry weights and dissipation/palinstrophy ledgers directly with the parabolic kernel \(\rho_V^{-5/3}\).

## 10. Permanent firewalls added by M19-253--254

\[
\boxed{\text{sharp moving-sphere identity}\neq\text{singular-scale validity without trace control}},
\]

\[
\boxed{\text{constant Galilean tracking}\neq\text{accelerated tracking without pressure correction}},
\]

\[
\boxed{\text{moving-frame optimization}\neq\text{subcriticality at a singular point}},
\]

\[
\boxed{\text{positive scale-invariant epsilon floor}\neq\text{divergent unweighted physical cost}},
\]

\[
\boxed{\text{nested-scale lower bounds}\neq\text{disjoint-annulus lower bounds}},
\]

\[
\boxed{\text{even natural disjoint }r^{5/3}\text{ payers}\neq\text{contradiction with finite unweighted spacetime norm}},
\]

\[
\boxed{\text{unweighted integrability}\neq\text{finiteness of the }\rho_V^{-5/3}\text{ critical weighted integral}}.
\]

## 11. Live theorem complex

Whole-space moving-observation branch:

\[
\boxed{\mathcal T_{GMS}^{weight}}
\]

OPEN.

Aperiodic branch:

\[
\boxed{\mathcal T_{aper}^{signed}}
\]

OPEN.

Historical cavity/Fredholm branch remains an auxiliary comparison branch. Global regularity remains unproved.