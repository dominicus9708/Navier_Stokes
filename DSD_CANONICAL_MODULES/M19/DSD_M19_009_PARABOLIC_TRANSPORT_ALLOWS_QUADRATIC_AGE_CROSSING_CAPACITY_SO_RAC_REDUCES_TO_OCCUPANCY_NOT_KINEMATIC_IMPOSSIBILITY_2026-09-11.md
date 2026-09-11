# M19-009 — Parabolic transport allows quadratic age crossing capacity, so R-AC reduces to occupancy rather than kinematic impossibility

**Date:** 2026-09-11  
**Status:** CALCULATION / RETURN-CROSSING KINEMATICS / PARABOLIC CAPACITY / OCCUPANCY FRONTIER

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Purpose

M19-008 shows that plain descendant-scale returns must satisfy approximately

\[
M_k\gtrsim K_k^2J_k^{1/2}
\]

to produce the sufficient ancestral return weight.

A tempting next step is to argue that a coherent carrier cannot make that many crossings in a controlled parent-time interval.

That argument is false if parabolic scaling is treated correctly.

The present module derives the crossing capacity. A descendant-scale carrier can make up to order

\[
K_k^2
\]

parabolic crossing attempts in one order-one parent-time interval.

This is exactly the reciprocal of the \(K_k^{-2}\) age penalty.

Therefore the missing R-AC theorem is not a simple kinematic upper bound on the number of return opportunities. It is an **occupancy theorem**: why should a fixed fraction of the available descendant-scale time slots actually carry the required ancestry return?

## 2. Abstract crossing-count lemma

Let \(z(t)\) be a scalar shell coordinate along a material trajectory.

Suppose one completed outward/inward return requires \(z\) to traverse a coordinate separation at least \(\Delta_z>0\) twice.

Then if \(M\) completed returns occur on \([a,b]\),

\[
\boxed{
2\Delta_z(M-1)
\le
\operatorname{Var}_{[a,b]}z.
}
\]

If \(z\) is absolutely continuous,

\[
\operatorname{Var}z
\le
\int_a^b|\dot z(t)|dt,
\]

so

\[
\boxed{
M
\le
1+
\frac1{2\Delta_z}
\int_a^b|\dot z(t)|dt.
}
\]

This is the correct generic geometric counting statement.

It does not yet fix the scale of \(\dot z\).

## 3. Parent and descendant scales

Let the parent length scale be normalized to one.

An age-\(k\) descendant has scale

\[
\boxed{
r_k=K_k^{-1},
\qquad
K_k=q^{k/2}.
}
\]

A controlled descendant-scale shell has physical/parent-coordinate thickness

\[
\boxed{
\Delta x_k\asymp K_k^{-1}.
}
\]

Under Navier--Stokes scaling, an order-one descendant-normalized velocity corresponds in parent coordinates to

\[
\boxed{
|u_{parent}|\asymp K_k.
}
\]

Therefore a typical controlled traversal time is

\[
\boxed{
\Delta t_k
\asymp
\frac{\Delta x_k}{|u_{parent}|}
\asymp
K_k^{-2}.
}
\]

This is the same parabolic time factor appearing in the M18 age penalty.

## 4. Fixed shell coordinate calculation

Define a descendant-normalized shell coordinate

\[
\boxed{
z_k(t)
:=
K_k\big(X(t)-c_k(t)\big)\cdot e_k
}
\]

for a controlled local direction \(e_k\), center \(c_k(t)\), and material trajectory \(X(t)\).

A fixed descendant-shell crossing has

\[
\Delta_z\asymp1.
\]

Differentiating,

\[
\dot z_k
=
K_k\big(u(X(t),t)-\dot c_k(t)\big)\cdot e_k
+
\text{controlled frame terms}.
\]

On a compact descendant-normalized transport branch,

\[
|u-\dot c_k|\lesssim K_k
\]

in parent units. Hence

\[
\boxed{
|\dot z_k|\lesssim K_k^2
}
\]

up to the already typed frame/geometry exits.

Over a parent-time interval of length \(T=O(1)\),

\[
\operatorname{Var}z_k
\lesssim
K_k^2T.
\]

The crossing lemma therefore gives

\[
\boxed{
M_k\lesssim K_k^2
}
\]

for controlled transversal crossings in an order-one parent-time window.

## 5. The upper capacity matches the ancestry requirement

M19-008 requires

\[
M_k
\gtrsim
K_k^2J_k^{1/2}
\]

if the return threshold is to be obtained through plain current-epoch episodes.

The kinematic capacity is

\[
M_k^{cap}\asymp K_k^2.
\]

Thus the capacity/requirement ratio is

\[
\boxed{
\frac{M_k^{req}}{M_k^{cap}}
\asymp
J_k^{1/2}.
}
\]

On the bounded normalized-enstrophy corridor, \(J_k\) is not an arbitrarily large independent quantity; it lies inside the retained normalized resource bounds.

Therefore the required order of multiplicity is **not forbidden by parabolic transport capacity**.

## 6. Slot formulation

Partition an order-one parent-time interval into descendant parabolic slots of length

\[
\Delta t_k\asymp K_k^{-2}.
\]

The number of available slots is

\[
\boxed{
N_k^{slot}\asymp K_k^2.
}
\]

Let

\[
N_k^{act}
\]

be the number of slots carrying an effective ancestry return episode.

On the plain-episode branch,

\[
M_k\asymp N_k^{act}
\]

up to bounded multiplicity/overlap constants.

Define the occupancy fraction

\[
\boxed{
\delta_k
:=
\frac{N_k^{act}}{N_k^{slot}}
\asymp
\frac{M_k}{K_k^2}.
}
\]

Then the return density becomes, at the scaling level,

\[
\boxed{
\mathfrak R_k
\lesssim
\delta_k
}
\]

for plain episodes, while saturation of the controlled dwell bound gives comparability.

The sufficient closure target therefore asks for roughly

\[
\boxed{
\delta_k
\gtrsim
J_k^{1/2}
}
\]

rather than an impossible number of temporal slots.

## 7. Reinterpret the M18-054 deficiency

Recall

\[
a_k
=\frac{\mathfrak R_k}{J_k^{1/2}}.
\]

On the plain controlled passage branch,

\[
\boxed{
a_k
\sim
\frac{\delta_k}{J_k^{1/2}}
}
\]

up to the certified comparability constants.

Hence the M18-054 surviving condition

\[
a_k\to0
\]

in cubic-mass density is not primarily a statement that returns are kinematically impossible.

It is a statement that

\[
\boxed{
\text{the fraction of available descendant parabolic slots carrying ancestral return is too small relative to }J_k^{1/2}.
}
\]

R-AC is therefore an occupancy/correlation problem.

## 8. Trapping branch

If one episode has enhanced residence

\[
\eta_{k,\ell}=K_k^2d_{k,\ell}\gg1,
\]

then several nominal parabolic slots are occupied by one long-lived event.

Thus the slot language naturally includes trapping:

\[
\boxed{
\text{return mass}
=
\text{many occupied slots by repeated crossings}
+
\text{many occupied slots by long residence}.
}
\]

The distinction is genealogical/topological, not one of total time occupancy.

## 9. Why bounded speed alone cannot close R-AC

A false argument would be

\[
\text{bounded normalized speed}
\Rightarrow
M_k=O(K_k)
\Rightarrow
\text{insufficient return}.
\]

The correct parabolic calculation is

\[
\boxed{
\text{shell width }K_k^{-1},
\quad
\text{parent velocity }K_k,
\quad
\text{crossing time }K_k^{-2},
\quad
M_k^{cap}=O(K_k^2).
}
\]

Thus bounded descendant dynamics permits exactly the quadratic number of temporal opportunities needed to cancel the quadratic age penalty.

No contradiction comes from transport capacity alone.

## 10. New precise R-AC target

The missing theorem can now be stated as an occupancy lower bound.

On a cubic-mass-bearing family one would need to establish, for example,

\[
\boxed{
\delta_k
\gtrsim
J_k^{1/2}
}
\]

on a subset carrying divergent cubic mass, or an equivalent long-residence statement.

Failure is the sharpened endpoint

\[
\boxed{
G_{ancestral\ slot\ occupancy\ deficiency}.
}
\]

This is more precise than generic `genealogy loss` or `return deficiency`.

## 11. Next calculation

The existing recurrence information is formulated mainly in similarity/logarithmic time, whereas \(\delta_k\) counts occupation of descendant **linear parabolic-time slots** inside a fixed parent interval.

M19-010 should compare these time coordinates exactly.

The key question is whether positive-density recurrence in similarity time implies positive occupancy density in the \(K_k^2\) affine descendant-time slots.

If it does not, the exact time-coordinate mismatch becomes the remaining R-AC bridge.

---

\[
\boxed{\text{M19-009 COMPLETE; R-AC REDUCED TO PARABOLIC SLOT OCCUPANCY.}}
\]
