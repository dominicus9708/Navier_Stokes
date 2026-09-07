# DSD M17-356 — Fixed-annulus vortex-tube packing turns winding-length decompactification into flux fragmentation or unbounded reuse

Date: 2026-09-08  
Canonical ID: **M17-356**

Status: **ACTIVE GEOMETRIC PACKING REDUCTION / M17-355 WINDING BRANCH**

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Setting

Work in one record-normalized fixed annulus

\[
A:=\{a<|y|<b\}
\]

on the bounded compact CE-H tail branch.

Let `T` be one regular material vortex tube/flux band whose center-line or representative line has normalized arclength

\[
L_T.
\]

Assume the tube remains inside `A` during the snapshot under consideration.

On the compact field branch,

\[
\boxed{\rho=|W|\le M_\rho<\infty.}
\]

## 2. Exact flux-coordinate volume identity

For oriented vorticity-flux coordinates,

\[
\boxed{
dy=\frac{d\Phi\,ds}{\rho}.
}
\]

Let the tube carry a positive oriented flux band of size

\[
\phi_T:=\int_{\Lambda_T}d\Phi>0.
\]

If every flux line in this band has arclength at least `L_T^{min}` inside the annulus, then counting the tube with multiplicity gives

\[
\int_{\Lambda_T}\int\frac{ds\,d\Phi}{\rho}
\ge
\frac{\phi_TL_T^{min}}{M_\rho}.
\]

Thus the multiplicity-counted tube volume satisfies

\[
\boxed{
\operatorname{Vol}_{mult}(T\cap A)
\ge
\frac{\phi_TL_T^{min}}{M_\rho}.
}
\]

## 3. Bounded spatial reuse implies a length ceiling

Suppose the tube-coordinate map has spatial overlap multiplicity bounded by

\[
N_{reuse}<\infty.
\]

Then

\[
\operatorname{Vol}_{mult}(T\cap A)
\le
N_{reuse}|A|.
\]

Therefore

\[
\boxed{
L_T^{min}
\le
\frac{M_\rho N_{reuse}|A|}{\phi_T}.
}
\]

In particular, if

\[
\phi_T\ge\phi_*>0
\]

and `N_reuse` remains uniformly bounded, the normalized tube length is uniformly bounded.

Hence

\[
\boxed{
L_T\to\infty
}
\]

is impossible under simultaneous fixed positive flux, amplitude compactness, and bounded spatial reuse.

## 4. Exact exits from winding-length decompactification

Therefore an activity-carrying sequence with

\[
L_{T_n}\to\infty
\]

must satisfy at least one of

\[
\boxed{
\phi_{T_n}\to0,
}
\]

or

\[
\boxed{
N_{reuse,n}\to\infty,
}
\]

or leave the compact assumptions through

\[
\boxed{
G_{amplitude/coefficient/tube\ geometry\ decompactification}.
}
\]

Thus

\[
\boxed{
G_{winding/length\ decompactification}
\Longrightarrow
G_{flux\ fragmentation}
\lor
G_{unbounded\ spatial\ reuse}
\lor
G_{field/tube\ decompactification}.
}
\]

## 5. Flux fragmentation means tube number must grow if total positive flux survives

Suppose a retained positively oriented tail family carries total flux

\[
\Phi_{tot}\ge\Phi_*>0
\]

while every individual tube band obeys

\[
\phi_T\le\varepsilon.
\]

Then any disjoint flux partition requires at least

\[
\boxed{
N_{tube}
\ge
\frac{\Phi_*}{\varepsilon}.
}
\]

Therefore the limit

\[
\varepsilon\to0
\]

forces

\[
\boxed{N_{tube}\to\infty.}
\]

Flux fragmentation is thus itself a multiplicity/interface-complexity branch, not a single thin tube escaping for free.

No fixed positive total tail flux is assumed unless it has been allocated by the preceding material-flux branch; otherwise retain `loss of flux allocation` explicitly.

## 6. Relation to M17-355

M17-355 split the bounded/winding tail into:

1. compact same-material loop recurrence;
2. loop replacement/interface/genealogy;
3. winding/length decompactification.

The present module refines item 3:

\[
\boxed{
\begin{aligned}
G_{bounded/winding\ tail}
\Longrightarrow{}&
H_{closed\ loop\ gradient/zero\text{-}level\ payer}\\
&\lor G_{loop\ replacement/interface/genealogy}\\
&\lor G_{flux\ fragmentation}\\
&\lor G_{unbounded\ spatial\ reuse}\\
&\lor G_{field/tube\ decompactification}.
\end{aligned}
}
\]

## 7. Why reuse is not yet a contradiction

A long thin vortex tube may visit the same bounded spatial region many times.  The Eulerian volume does not count those visits separately, while the flux-coordinate Jacobian does.

Thus

\[
N_{reuse}\to\infty
\]

is a genuine way to evade the volume-packing length bound.

Closing it requires a bounded-multiplicity theorem, a director/curvature cost, or an interface/genealogy argument.  None is silently assumed here.

## 8. DSD-theory role

The retained heuristic is to distinguish geometric volume from multiplicity-counted structural volume.  The actual inequality is the exact vortex-flux Jacobian plus elementary packing.

No DSD axiom is used as a PDE assumption.

## 9. Next target

The most concrete remaining geometry is

\[
\boxed{G_{unbounded\ spatial\ reuse}.}
\]

The next calculation should test whether repeatedly reusing a fixed annulus with one material line necessarily forces large total curvature/director variation or vanishing inter-turn separation, and whether either quantity enters an already certified CE-H gradient/interface channel.

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
