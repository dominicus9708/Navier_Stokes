# M19-280 — Total algebraic winding on a material cross-section is boundary degree; interior nodal turnover has zero net signed index

**Date:** 2026-09-16  
**Status:** CALCULATION / TOPOLOGICAL DEGREE AUDIT / SIGNED-INDEX NO-GO ON CLOSED MATERIAL CROSS-SECTIONS

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Purpose

M19-279 shows that the winding number of a regular material nodal filament is frozen, while the regular nodal-Jacobian multiplier is an exact coboundary. The only remaining way for winding to contribute to the M19-271 signed/index target would be through topology-changing degenerate nodal events.

This module tests the strongest natural signed quantity: the **total algebraic winding index** piercing one material transverse cross-section.

The result is another exact conservation law. Interior nodal creation, annihilation, merger, splitting, or reconnection can rearrange local indices, but cannot change their signed sum while the material boundary stays in the active set.

## 2. Material cross-section

Work in the great-circle branch

\[
f=W_1+iW_2.
\]

Let \(D(\theta)\) be a smoothly transported material two-disk and let

\[
\Gamma(\theta)=\partial D(\theta).
\]

Assume on a time interval \(I\):

1. \(f\neq0\) on \(\Gamma(\theta)\) for every \(\theta\in I\);
2. the disk remains a valid transverse cross-section for the nodal network except possibly at isolated interior degenerate events;
3. the boundary is transported by the CE-H material flow.

On the active boundary define

\[
\zeta:=\frac{f}{|f|}=e^{i\psi}:\Gamma(\theta)\to S^1.
\]

## 3. Boundary degree is materially frozen

On the active CE-H branch,

\[
D_B\xi=0.
\]

In the fixed great-circle frame this means that the phase value attached to every material boundary point is constant modulo \(2\pi\). If \(\Phi_\theta\) denotes the material flow map from \(\Gamma(0)\) to \(\Gamma(\theta)\), then

\[
\boxed{
\zeta(\Phi_\theta(a),\theta)=\zeta(a,0)
}
\]

for every boundary label \(a\).

Therefore the maps \(\zeta|_{\Gamma(\theta)}\) are conjugate by an orientation-preserving material reparametrization of the circle, and

\[
\boxed{
\deg\bigl(\zeta|_{\Gamma(\theta)}\bigr)
=\deg\bigl(\zeta|_{\Gamma(0)}\bigr)
=:N_{\partial D}.
}
\]

Hence

\[
\boxed{D_BN_{\partial D}=0}
\]

in the topological sense.

## 4. Interior index sum

At a regular time, suppose the nodal set intersects \(D(\theta)\) transversely in finitely many points

\[
p_1,\ldots,p_m.
\]

Each point has a local Brouwer/phase index

\[
\operatorname{ind}(p_a)
=\frac1{2\pi}\oint_{\gamma_a}d\psi
\in\mathbb Z,
\]

where \(\gamma_a\) is a sufficiently small positively oriented loop around \(p_a\) inside the disk.

The standard degree decomposition for a map \(D\to\mathbb R^2\) with no boundary zero gives

\[
\boxed{
\sum_{a=1}^{m}\operatorname{ind}(p_a)
=
\deg\bigl(f/|f|;\Gamma(\theta)\bigr)
=N_{\partial D}.
}
\]

Thus the signed total nodal winding through the material disk is fixed.

## 5. Degenerate interior events cannot create net algebraic index

At an interior topology-changing time, the individual regular zeros may cease to be defined or may merge/split. M17-009 proves that such events have finite analytic jet order on the compact hard hull.

However the boundary map remains nonzero and continuous throughout the event under the present assumptions. Topological degree is homotopy invariant, so the boundary degree cannot jump.

Therefore the signed sum of the regular indices immediately before and after the event must agree:

\[
\boxed{
\sum_a\operatorname{ind}(p_a)_{\,before}
=
\sum_b\operatorname{ind}(p_b)_{\,after}.
}
\]

Consequently any interior pair creation/annihilation or reconnection carries zero net algebraic index change.

For example, a newly created collection must satisfy

\[
\boxed{
\sum_{new}\operatorname{ind}=0
}
\]

unless an index crosses the material boundary or the boundary active condition fails.

## 6. Exact index-change exits

A change of total signed index on the material cross-section therefore requires at least one of

\[
\boxed{
G_{nodal\ crossing\ boundary}
}
\]

or

\[
\boxed{
G_{boundary\ zero/active\ loss}
}
\]

or

\[
\boxed{
G_{material\ cross\text{-}section/representation\ loss}.
}
\]

Purely interior finite-jet topology turnover is not an algebraic index source.

## 7. Relation to M19-271

The natural signed index observable

\[
\mathcal I_D(\theta)
:=\sum_{p_a\in D(\theta)}\operatorname{ind}(p_a)
\]

satisfies

\[
\boxed{
\mathcal I_D(\theta)=N_{\partial D}=\text{constant}
}
\]

on the closed material branch.

Hence

\[
\boxed{
\mathcal I_D\circ\sigma_h-\mathcal I_D=0.
}
\]

It cannot produce the strictly positive invariant-mean remainder required by M19-271.

The **unsigned** turnover

\[
\sum_a|\operatorname{ind}(p_a)|
\]

may still grow or fluctuate, but M17-006 and M17-009 already show why this is not a fixed energetic quantum: the \(\rho^2\) weight vanishes at the nodal core and finite-jet events are unsigned.

Thus unsigned topological activity remains an occupancy/complexity branch, not a signed closure resource.

## 8. Consequence for the dynamic-core frontier

The great-circle winding candidate is now reduced to

\[
\boxed{
\begin{aligned}
\text{winding/index route}
\Longrightarrow{}&
\text{conserved regular index}
\\
&\lor\text{zero-net interior turnover}
\\
&\lor G_{boundary/representation\ defect}
\\
&\lor G_{winding/reuse/decompactification}.
\end{aligned}
}
\]

Therefore ordinary algebraic winding does **not** realize the missing \(\mathcal T_{aper}^{signed/index}\) on a closed material core.

Any successful signed/index route must use a different object, for example:

- a boundary-crossing/export index with an independently finite total budget;
- a non-topological signed PDE defect coupled to the finite-lag event;
- or a genuinely global factor/observability rigidity theorem.

## 9. Audit firewall

This result does not claim that the entire three-dimensional nodal network has one globally defined scalar index without choosing a cross-section. The certified statement is cross-section-wise and requires a material boundary that remains in the active set.

If that condition fails, record the corresponding boundary/representation defect explicitly rather than importing index conservation.

---

\[
\boxed{\text{M19-280 COMPLETE; INTERIOR NODAL TOPOLOGY TURNOVER HAS ZERO NET SIGNED INDEX ON A CLOSED MATERIAL CROSS-SECTION.}}
\]
