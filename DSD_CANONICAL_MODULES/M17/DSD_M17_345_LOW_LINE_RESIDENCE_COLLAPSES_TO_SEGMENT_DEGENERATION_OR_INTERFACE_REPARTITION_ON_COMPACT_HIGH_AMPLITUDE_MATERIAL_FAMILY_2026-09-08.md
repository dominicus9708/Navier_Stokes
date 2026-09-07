# DSD M17-345 — Low line residence collapses to segment degeneration or interface repartition on a compact high-amplitude material family

Date: 2026-09-08  
Canonical ID: **M17-345**

Status: **ACTIVE LOW-RESIDENCE REDUCTION / SAME-MATERIAL COMPACT BRANCH**

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Input from M17-341

The low-residence event branch is

\[
E_{low}(w_*)
:=
\{\text{downward zero crossings with }L_\rho<w_*\},
\]

where

\[
\boxed{
L_\rho(\Gamma,\theta)
:=
\int_{\Gamma(\theta)}\rho\,ds.
}
\]

M17-341 allows a fixed fraction of the critical zero-crossing activity to lie in `E_low`.

The question is whether `L_rho` can approach zero on the same retained compact high-amplitude material-segment family without another degeneration.

## 2. High-amplitude lower bound

M17-311/312 retain the high-amplitude branch away from the vorticity nodal set.  On the captured segment,

\[
\boxed{
\rho\ge a_*>0.
}
\]

Therefore

\[
\boxed{
L_\rho
\ge
a_*\,\mathcal L(\Gamma),
}
\]

where

\[
\mathcal L(\Gamma):=\int_\Gamma ds
\]

is the retained arclength.

Thus

\[
L_\rho\to0
\quad\Longrightarrow\quad
\mathcal L(\Gamma)\to0
\]

unless the high-amplitude capture itself is lost.

## 3. Compact same-material segment family

Let `K_seg` denote the retained state space of material segments carrying the zero-crossing activity on the branch where:

1. the same material-segment identity survives;
2. endpoints/closure convention is fixed;
3. the segment remains inside the high-amplitude capture region;
4. the all-order CE-H state is compact;
5. no rank/interface replacement occurs.

On this branch, both the segment embedding and `rho` vary continuously with the state, so

\[
L_\rho:K_{seg}\to(0,\infty)
\]

is continuous.

If every state in `K_seg` represents a nondegenerate segment,

\[
\mathcal L(\Gamma)>0,
\]

then compactness gives

\[
\boxed{
L_{min}
:=
\min_{K_{seg}}L_\rho
>0.
}
\]

## 4. Exclusion of the low-residence branch on the compact segment family

Choose

\[
0<w_*<L_{min}.
\]

Then

\[
\boxed{E_{low}(w_*)=\varnothing}
\]

on the compact same-material segment branch.

Hence M17-341's low-residence alternative cannot carry any crossing activity there.

The trichotomy reduces to

\[
\boxed{
H_{critical\ zero\ crossing}
\Longrightarrow
H_{critical\ spatial\ crossing}
\lor
H_{large\ transverse\ multiplier\ gradient}
}
\]

on this fixed-segment compact subbranch.

## 5. What failure of the positive minimum means

If no positive `L_min` exists, there is a sequence of activity-carrying states with

\[
L_{\rho,n}\to0.
\]

Compactness of the ambient CE-H hull gives a convergent subsequence of fields.  Since `rho>=a_*` is retained, the only way the segment integral can vanish is that the material-segment representation itself degenerates:

\[
\boxed{
\mathcal L(\Gamma_n)\to0.
}
\]

or that one of the assumptions defining `K_seg` fails before the limit.

Thus the exact exits are

\[
\boxed{
G_{segment\ collapse}
\lor
G_{amplitude\ threshold\ loss}
\lor
G_{endpoint/interface\ repartition}
\lor
G_{rank/genealogy\ replacement}.
}
\]

`L_rho -> 0` is not retained as an independent unexplained channel.

## 6. Relation to M17-314 bounded-length hypothesis

M17-314 used a uniform **upper** capture-length bound to remove arclength from the negative flux-length moment.

The present result concerns the complementary lower bound.  It does not claim that an arbitrary instantaneous flow-box segment has positive minimum length.

It says only:

\[
\boxed{
\text{compact fixed-identity nondegenerate material segment family}
\Rightarrow
L_\rho\ge L_{min}>0.
}
\]

If the chosen segment convention can shrink or be repartitioned, that is explicitly the interface/genealogy exit rather than a hidden failure of compactness.

## 7. Event-measure formulation

Let `nu` be the downward zero-crossing event measure of M17-341.  On the compact fixed-segment branch,

\[
\nu\{L_\rho<w_*\}=0
\]

for every `w_*<L_min`.

Consequently a positive-density low-residence branch in the long-time event measure implies that the crossing population accumulates on the boundary of the fixed-segment state space.

That boundary is exactly the segment-collapse / threshold / interface / replacement set listed above.

## 8. DSD-theory role

The retained DSD heuristic is the distinction between a quantity becoming small **inside the same structure** and the structure itself ceasing to be the same object.

The mathematical argument is ordinary compactness and continuity of the positive line integral.

No DSD axiom is used as a Navier--Stokes assumption.

## 9. Updated zero-crossing branch

Combining M17-341, M17-344, and the present reduction, the fixed-segment compact branch satisfies

\[
\boxed{
\begin{aligned}
H_{critical\ zero\ crossing}
\Longrightarrow{}&
H_{critical\ spatial\ charge}\\
&\lor H_{M5\text{-}688\ diffusion\ payer}\\
&\lor G_{zero\text{-}trace\ concentration}\\
&\lor G_{segment/interface/genealogy\ degeneration}.
\end{aligned}
}
\]

The next unresolved positive branch is the critical spatial charge `Q_0`; the main nonpositive exits are now explicit geometry/genealogy or zero-trace concentration.

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
