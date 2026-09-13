# M19-238 — The macroscopic bulk limit has no relative-periodic L2 vorticity and reduces to potential flow or scaled-derivative decompactification

**Date:** 2026-09-14  
**Status:** ACTIVE CALCULATION / BULK-RETURN INVISCID LIMIT + CURL RIGIDITY

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Input from the boundary-layer reduction

M19-237 shows that the local no-slip layer at an expanding spectator boundary is asymptotically consistent and therefore cannot itself exclude the escape branch.

The remaining question is the return of the bulk amplitude feeding that layer.

Let \(w_j\) be the normalized cavity unit modes from M19-231--237 on \(B_{R_j}\), \(R_j\to\infty\), and set

\[
\boxed{
x:=\frac y{R_j},
\qquad
V_j(x,s):=R_j^{3/2}w_j(R_jx,s).}
\]

Then

\[
\int_0^{S_j}\|V_j(s)\|_{L^2(B_1)}^2ds=1.
\]

Hence, after subsequence extraction,

\[
V_j\rightharpoonup V
\]

weakly in \(L^2\) on one period.

## 2. Rescaled equation

The primal linearized equation becomes

\[
\boxed{
\begin{aligned}
\partial_sV_j
={}&\frac\nu{R_j^2}\Delta_xV_j
-\frac12(x\cdot\nabla_x)V_j
-\frac12V_j\\
&-\frac1{R_j}U_j(R_jx,s)\cdot\nabla_xV_j
-(V_j\cdot\nabla_y)U_j(R_jx,s)
-\nabla_xP_j,
\end{aligned}}
\]

with a correspondingly rescaled pressure \(P_j\).

On every compact annulus

\[
0<\rho_0\le|x|\le\rho_1<1,
\]

the retained remote bounds give

\[
\frac1{R_j}U_j(R_jx,s)=O(R_j^{-2}),
\qquad
\nabla_yU_j(R_jx,s)=O(R_j^{-2}).
\]

Also M19-232 gives

\[
\int_0^{S_j}\|\nabla_xV_j\|_2^2ds
=R_j^2
\int_0^{S_j}\|\nabla_yw_j\|_2^2ds
=O(R_j^2).
\]

Therefore the rescaled viscous term tends to zero in \(H^{-1}_{loc}\):

\[
\left\|
\frac\nu{R_j^2}\Delta_xV_j
\right\|_{H^{-1}}
\lesssim
\frac\nu{R_j^2}\|\nabla_xV_j\|_2
=O(R_j^{-1})\to0.
\]

Thus on every compact subset of the punctured unit ball, any weak macroscopic bulk limit satisfies the inviscid similarity-Stokes equation

\[
\boxed{
\partial_sV
+\frac12(x\cdot\nabla)V
+\frac12V
+\nabla P=0,
\qquad
\nabla\cdot V=0.
}
\]

The no-slip boundary condition is not inherited by this outer equation; it is carried by the M19-237 thin layer.

## 3. Curl equation of the outer bulk

Let

\[
Z:=\nabla_x\times V.
\]

Whenever the rescaled vorticities

\[
Z_j:=\nabla_x\times V_j
\]

are locally bounded in \(L^2\) on a compact punctured annulus, one may pass to the curl equation and obtain

\[
\boxed{
\partial_sZ
+\frac12(x\cdot\nabla)Z
+Z=0.
}
\]

This transport equation has the explicit solution

\[
\boxed{
Z(s,x)
=e^{-s}Z(0,e^{-s/2}x)
}
\]

after fixing the time origin.

## 4. Relative periodicity rules out every L2 rotational bulk mode

The cavity modes satisfy an exact relative-periodic return. After subsequence extraction,

\[
S_j\to S>0,
\qquad
Q_j\to Q\in SO(3),
\]

and the outer limit inherits

\[
Z(S,x)=\mathcal R_QZ(0,x)
\]

with the usual simultaneous action on vector and spatial arguments.

Because rotations preserve centered balls and the Euclidean norm, define

\[
E(\rho):=\int_{B_\rho}|Z(0,x)|^2dx.
\]

The explicit transport formula gives

\[
\begin{aligned}
\int_{B_\rho}|Z(S,x)|^2dx
&=e^{-2S}
\int_{B_\rho}|Z(0,e^{-S/2}x)|^2dx\\
&=e^{-S/2}E(\rho e^{-S/2}).
\end{aligned}
\]

Relative periodicity gives the same quantity as \(E(\rho)\). Hence

\[
\boxed{
E(\rho)
=e^{-S/2}E(\rho e^{-S/2}).
}
\]

But

\[
E(\rho e^{-S/2})\le E(\rho).
\]

Since \(e^{-S/2}<1\),

\[
E(\rho)
\le e^{-S/2}E(\rho),
\]

and therefore

\[
\boxed{E(\rho)=0.}
\]

Thus

\[
\boxed{Z\equiv0}
\]

on every region where the macroscopic vorticity limit is locally \(L^2\).

This is an exact inviscid curl rigidity, not an energy estimate.

## 5. Consequence: regular macroscopic bulk is potential flow

On the punctured three-dimensional ball, curl-free and divergence-free fields are locally harmonic gradients. Hence

\[
\boxed{
V=\nabla\Phi,
\qquad
\Delta\Phi=0
}
\]

on every regular macroscopic bulk component.

For such a field,

\[
\frac12(x\cdot\nabla)V+rac12V
=\frac12\nabla(x\cdot\nabla\Phi).
\]

Therefore the entire inviscid bulk equation becomes a gradient identity

\[
\nabla\left(
\partial_s\Phi
+\frac12x\cdot\nabla\Phi
+P
\right)=0.
\]

The pressure can absorb this expression.

Hence the regular potential sector is not excluded by the outer inviscid equation alone.

Permanent firewall:

\[
\boxed{
\text{outer curl rigidity}
\neq
\text{outer velocity vanishing}.}
\]

## 6. The alternative is scaled-derivative decompactification

The original physical vorticity currency is controlled:

\[
\int\|\eta_j\|_2^2ds=O(1).
\]

But under the macroscopic scaling,

\[
\boxed{
\int|Z_j|^2dx
=R_j^2\int|\eta_j|^2dy.
}
\]

Therefore M19-234's small physical interior vorticity does not automatically give a uniform rescaled \(L^2\) curl bound.

If no locally \(L^2\)-bounded curl subsequence exists on a macroscopic annulus, then

\[
\boxed{
R_j^2
\int_{\rho_0R_j\le|y|\le\rho_1R_j}|\eta_j|^2dy
\to\infty
}
\]

along a further subsequence for some \(0<\rho_0<\rho_1<1\).

This is a new typed escape:

\[
\boxed{\text{scaled-derivative decompactification}.}
\]

It may occur even though the unscaled physical vorticity mass in that annulus tends to zero.

## 7. Bulk-return dichotomy

The M19-237 bulk-return problem therefore splits into

\[
\boxed{
\mathcal T_{cav}^{bulk-return}
\subset
\mathcal T_{pot}^{match}
\cup
\mathcal T_{scaled-deriv}.
}
\]

Here

\[
\boxed{
\mathcal T_{pot}^{match}:
\text{classify/exclude harmonic-potential macroscopic bulk modes matched to the }\nu/R\text{ no-slip layer and relative return},
}
\]

while

\[
\boxed{
\mathcal T_{scaled-deriv}:
\text{control or reclassify macroscopic rescaled-vorticity decompactification}.}
\]

## 8. Relation to the original hard/scattering problem

A singular rotational macroscopic limit can evade the local \(L^2\)-curl rigidity. Such a singularity would correspond to an additional scale appearing between the fixed core and the cavity radius after macroscopic rescaling.

It must not be silently identified with the existing finite hard scattering modes without a scale-map/spectral-membership theorem.

Likewise, the potential sector is invisible to the curl rigidity and can be sustained locally by pressure. Its elimination, if true, must come from global matching, boundary return, or the original whole-space/scattering constraints.

## 9. New next target

The cleanest next calculation is the potential sector because it has no rotational bulk obstruction. One should decompose the harmonic bulk into spherical multipoles and impose the relative-periodic rotation plus the M19-237 boundary-layer matching. If the matching selects only exact translation/rotation symmetry tangents, the nonsymmetry escape branch would collapse to \(\mathcal T_{scaled-deriv}\).

---

\[
\boxed{\text{M19-238 COMPLETE: REGULAR MACROSCOPIC ROTATIONAL BULK IS EXCLUDED; ESCAPE REDUCES TO POTENTIAL MATCHING OR SCALED-DERIVATIVE DECOMPACTIFICATION.}}
\]
