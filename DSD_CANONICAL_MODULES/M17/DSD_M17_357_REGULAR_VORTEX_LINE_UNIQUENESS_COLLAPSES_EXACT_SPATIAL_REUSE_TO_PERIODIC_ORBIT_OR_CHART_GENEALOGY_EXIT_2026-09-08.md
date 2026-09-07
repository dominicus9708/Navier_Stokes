# DSD M17-357 — Regular vortex-line uniqueness collapses exact spatial reuse to periodic orbit or chart/genealogy exit

Date: 2026-09-08  
Canonical ID: **M17-357**

Status: **ACTIVE GEOMETRIC CORRECTION OF M17-356 REUSE BRANCH**

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Setting

Work on the retained regular high-amplitude CE-H family, where

\[
\rho=|W|\ge a_*>0
\]

and the director

\[
\xi:=W/|W|
\]

is smooth. At a fixed time, a vortex line is an integral curve

\[
\boxed{\gamma'(s)=\xi(\gamma(s)),\qquad |\gamma'(s)|=1.}
\]

Because `xi` is `C1` on the compact active region, the autonomous ODE has local uniqueness.

## 2. Exact self-intersection implies periodicity

Suppose one vortex line satisfies

\[
\gamma(s_1)=\gamma(s_2),\qquad s_2>s_1.
\]

Set

\[
T:=s_2-s_1>0.
\]

Both maps

\[
s\mapsto\gamma(s+s_1)
\]

and

\[
s\mapsto\gamma(s+s_2)
\]

solve the same autonomous ODE and have the same value at `s=0`. By uniqueness,

\[
\boxed{\gamma(s+T)=\gamma(s)}
\]

wherever both sides are defined, and by continuation along the complete retained orbit this is the primitive closed-orbit alternative after reducing `T` if necessary.

Hence

\[
\boxed{
\text{a regular vortex line cannot exactly reuse one spatial point without becoming periodic.}
}
\]

Likewise two distinct regular vortex lines cannot intersect: if they meet at one point, ODE uniqueness makes them the same integral curve.

## 3. Fundamental vortex-line coordinates

For an open/nonperiodic vortex line, choose arclength only once along its injective image.

For a periodic vortex line with primitive period `T_gamma`, use

\[
s\in\mathbb R/T_\gamma\mathbb Z
\]

rather than counting repeated laps.

Thus a coherent vortex-tube coordinate chart should be taken on a **fundamental orbit domain**. In such a chart, the map

\[
(\lambda,s)\mapsto y
\]

is injective modulo the explicit periodic identification, provided the label transversal itself is chosen without repeated intersections of the same orbit.

If no such finite coherent label atlas survives, record instead

\[
\boxed{G_{tube\ chart/transversal/genealogy\ decompactification}.}
\]

This is a chart/interface problem, not physical volume reuse.

## 4. Correction to the M17-356 multiplicity factor

M17-356 introduced a spatial overlap multiplicity `N_reuse` and allowed

\[
\operatorname{Vol}_{mult}\le N_{reuse}|A|.
\]

For a fundamental regular vortex-tube chart there is no independent exact-overlap multiplicity. Distinct coordinates map to distinct physical points, except for the periodic identification already quotiented out.

Therefore on the coherent fundamental branch the correct bound is simply

\[
\boxed{
\operatorname{Vol}(T\cap A)\le |A|.
}
\]

The exact flux Jacobian remains

\[
dy=\frac{d\Phi\,ds}{\rho}.
\]

If the tube carries flux

\[
\phi_T\ge\phi_*>0
\]

and

\[
\rho\le M_\rho,
\]

then for the fundamental arclength inside the annulus,

\[
\operatorname{Vol}(T\cap A)
\ge
\frac{\phi_*L_T^{fund}}{M_\rho}.
\]

Hence

\[
\boxed{
L_T^{fund}
\le
\frac{M_\rho|A|}{\phi_*}.
}
\]

Thus fixed positive flux plus amplitude compactness already gives a primitive/fundamental length ceiling on a coherent regular tube.

## 5. Closed periodic orbit branch

If exact reuse occurs, Section 2 returns the geometry to a closed vortex orbit.

Repeated traversal of the same primitive loop does not create new geometric length. It is merely repeated parameterization.

Therefore the correct object is the primitive loop, which routes to the already existing branch

\[
\boxed{H_{same\ material\ closed\ loop}.}
\]

If that loop remains compact and recurrent with comparable line weight and flux, M17-188 applies and forces the `3/4` strain--amplitude covariance and associated gradient occupancy.

Thus exact spatial reuse is not a new late-tail survivor.

## 6. Near reuse is not exact multiplicity

A nonperiodic line may pass arbitrarily close to an earlier strand without intersecting it.

Those strands occupy distinct physical points. Consequently they are counted separately by the injective flux-coordinate volume integral. There is no factor `N_reuse` discount merely because the strands are close in Euclidean distance.

For a positive-flux tube band, arbitrarily close repeated strands can evade a uniform tubular-neighborhood separation only if at least one of the following degenerates:

\[
\boxed{
G_{transverse\ tube\ shape/aspect\ ratio},
}
\]

\[
\boxed{
G_{flux\ fragmentation},
}

\[
\boxed{
G_{tube\ chart/interface/genealogy}.
}
\]

No uniform tube-thickness theorem is silently assumed; the point is only that **near recurrence is not exact coordinate multiplicity**.

## 7. Corrected winding decompactification split

Combining M17-355--357, on a coherent regular tube family with fixed positive flux and compact amplitude,

\[
\boxed{
\begin{aligned}
G_{winding/length\ decompactification}
\Longrightarrow{}&
H_{same\ material\ closed\ loop}\\
&\lor G_{flux\ fragmentation}\\
&\lor G_{transverse\ tube\ geometry\ decompactification}\\
&\lor G_{tube\ chart/interface/genealogy\ decompactification}.
\end{aligned}
}
\]

The separate branch

\[
G_{unbounded\ exact\ spatial\ reuse}
\]

is therefore retired on the regular coherent-chart branch.

## 8. DSD-theory role

The useful heuristic is the distinction between a represented multiplicity and genuine structural multiplicity. The mathematical correction itself is only ODE uniqueness plus the exact vortex-flux coordinate Jacobian.

No DSD axiom is used as a PDE hypothesis.

## 9. Audit verdict

**PASS as a correction/refinement of M17-356.**

M17-356's packing identity remains valid, but its `unbounded spatial reuse` escape is not an independent physical branch after passage to fundamental regular vortex-line coordinates.

The remaining high-value branches are now flux fragmentation, transverse tube-geometry degeneration, and tube-chart/interface/genealogy turnover.

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
