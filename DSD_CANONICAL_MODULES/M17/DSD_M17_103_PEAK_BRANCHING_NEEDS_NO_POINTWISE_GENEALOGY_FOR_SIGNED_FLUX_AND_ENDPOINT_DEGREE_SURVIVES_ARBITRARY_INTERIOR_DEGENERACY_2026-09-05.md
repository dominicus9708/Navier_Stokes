# DSD M17-103 — Peak branching needs no pointwise genealogy for signed flux; endpoint degree survives arbitrary interior degeneracy

Date: 2026-09-05
Canonical ID: **M17-103**

Status: **INTERNAL RANK-2 CARRIER-LEVEL GENEALOGY AUDIT / M17-102 STILL LISTS `NONMATCHABLE PEAK BRANCHING` AS A POSSIBLE FAILURE OF CLEAN TYPE-BY-TYPE FLUX MATCHING. FOR THE SIGNED DIRECTOR-AREA CARRIER LEDGER THIS IS TOO CONSERVATIVE. ON EACH ORIENTED FROZEN DIRECTOR-AREA TUBE SEGMENT, THE ALGEBRAIC ZERO DEGREE OF THE ORIGINAL SCALAR PEAK DESCRIPTOR `g=D_xi log rho` IS DETERMINED ONLY BY THE SIGNS OF `g` AT THE TWO ENDPOINTS. THIS DEGREE CAN BE DEFINED AT TRANSVERSE TIMES BY THE SIGNED ROOT SUM AND EXTENDED THROUGH ARBITRARY INTERIOR MULTIPLE ZEROS, CUSPS, MERGERS, SPLITTINGS, AND FINITE-TYPE CHANGES BY THE ENDPOINT FORMULA. IT DOES NOT REQUIRE A UNIQUE POINTWISE PEAK TRACK, A REGULAR `g=0` SURFACE, OR A UNIQUE TYPE CHART AT THE EVENT. THEREFORE NONMATCHABLE POINT GENEALOGY IS NOT ITSELF A SIGNED DIRECTOR-AREA FLUX SOURCE. THE TOP-JET ATLAS OF M17-101/102 REMAINS NECESSARY FOR LOCAL DIFFERENTIAL DESCRIPTORS AND COMPENSATION LAWS, BUT NOT FOR THE CARRIER-LEVEL ALGEBRAIC FLUX INVARIANT. AS LONG AS THE SAME REGULAR `J_xi` TUBE SEGMENT PERSISTS AND ITS ENDPOINTS STAY OFF `g=0` WITH FIXED SIGNS, ALL INTERIOR PEAK GENEALOGY IS RECYCLABLE. A CHANGE OF SIGNED ALGEBRAIC PEAK FLUX REQUIRES ENDPOINT CROSSING, LOSS OF THE DIRECTOR-AREA CARRIER `J_xi=0`, OR DOMAIN/CHART/INTERFACE FAILURE OF THE RETAINED TUBE SEGMENT. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Return to the primary scalar on one tube

Fix an oriented regular director-area tube segment

\[
L_\lambda(\theta)
=\{X_\lambda(s,\theta):s_-\le s\le s_+\}
\]

with

\[
J_\xi\neq0.
\]

Define

\[
\boxed{
f_\lambda(s,\theta)
:=g(X_\lambda(s,\theta),\theta),
\qquad
g=D_\xi\log\rho.
}
\]

Assume only that the endpoint values remain nonzero:

\[
\boxed{
f_\lambda(s_-,\theta)\neq0,
\qquad
f_\lambda(s_+,\theta)\neq0.
}
\]

No assumption is made here that every interior zero is simple or that `grad g!=0`.

---

## 2. Algebraic degree at transverse times

At a time when all interior roots are simple, define

\[
I_\lambda(\theta)
:=\sum_{f_\lambda(s_i,\theta)=0}
\operatorname{sgn}\partial_sf_\lambda(s_i,\theta).
\]

As in M17-100,

\[
\boxed{
I_\lambda(\theta)
=
\frac{
\operatorname{sgn}f_\lambda(s_+,\theta)
-
\operatorname{sgn}f_\lambda(s_-,\theta)
}{2}.
}
\]

The right side is well defined whether or not the current interior zeros are simple.

This suggests the natural extension

\[
\boxed{
\deg_0(f_\lambda;[s_-,s_+])
:=
\frac{
\operatorname{sgn}f_\lambda(s_+)
-
\operatorname{sgn}f_\lambda(s_-)
}{2}.
}
\]

---

## 3. Interior degeneracy cannot change the endpoint degree

Suppose an interior event occurs at `theta_*` where several roots merge, split, become tangent, or acquire higher multiplicity.

The endpoint values remain nonzero and their signs remain fixed.

Then by Section 2,

\[
\boxed{
\deg_0(f_\lambda;[s_-,s_+])
=\text{constant}
}
\]

on both sides of the event and through the event by continuity of the endpoint data.

No matching of individual roots is required.

Thus

\[
\boxed{
\text{pointwise peak genealogy may fail}
\quad\text{while}\quad
\text{carrier-level algebraic degree remains exact}.
}
\]

---

## 4. Examples covered automatically

The endpoint-degree ledger survives all of the following interior events:

\[
\boxed{
\begin{aligned}
&0\leftrightarrow2\text{ fold pair creation/annihilation},\\
&\text{higher finite-order tangency},\\
&\text{cusp-like merger/splitting},\\
&\text{multiple simultaneous peak intersections},\\
&\nabla g=0\text{ singularity of the lowest peak sheet},\\
&\text{finite critical-order change }\nu\to\nu',\\
&\text{loss of unique pointwise peak tracking}.
\end{aligned}
}
\]

These events may drastically change unsigned peak count and type populations, but they do not change the endpoint degree of `g` on the tube.

---

## 5. Why the top-jet atlas is still needed

M17-101/102 are not made redundant.

When

\[
\nabla g=0
\]

or the critical order changes, the original `g=0` sheet may fail to support the local differential geometry needed for

- surface normals;
- inherited positive transverse sheet measures;
- higher-jet tilt laws;
- Riccati compensation margins;
- type-resolved state-space currents.

For these purposes one must lift to the regular finite top-jet chart

\[
\Psi_\nu=D_\xi^{\nu-1}g.
\]

But for the **signed carrier-level flux degree**, the original scalar `g` and its endpoint signs are sufficient.

This separates local differential describability from global algebraic carrier bookkeeping.

---

## 6. Flux-weighted algebraic degree without pointwise matching

Each frozen tube label carries its conserved director-area flux element

\[
d\Phi_J(\lambda).
\]

Define

\[
\boxed{
\mathcal Q_{peak}^{alg}
:=\int_\Lambda
\deg_0(f_\lambda;[s_-,s_+])
\,d\Phi_J(\lambda).
}
\]

If the same tube-label family survives and the endpoint signs remain fixed, then

\[
\boxed{
\frac d{d\theta}\mathcal Q_{peak}^{alg}=0
}
\]

without any need to identify individual peak branches across interior singular events.

Thus the algebraic peak flux is more robust than every pointwise type ledger.

---

## 7. Relation to M17-094 through M17-102

The hierarchy is now:

\[
\boxed{
\begin{array}{ll}
\text{M17-094:}&\text{arbitrary tracked peak weights},\\
\text{M17-097:}&\text{canonical transverse director-area weight},\\
\text{M17-098:}&\text{clean type switches redistribute that weight},\\
\text{M17-099:}&\text{generic tangency is an oriented fold pair},\\
\text{M17-100:}&\text{regular tangencies preserve algebraic degree},\\
\text{M17-101:}&\text{finite singular peak sheets regularize on top jets},\\
\text{M17-102:}&\text{finite type charts share one tube measure},\\
\text{M17-103:}&\text{pointwise genealogy is unnecessary for signed carrier flux}.
\end{array}
}
\]

The progressively stronger carrier-level statement is the endpoint-degree law.

---

## 8. What can actually change the algebraic carrier flux

Since the degree depends only on endpoint signs and the flux weight depends only on the persistent director-area tube, a genuine change requires at least one of the following:

\[
\boxed{
\begin{aligned}
&g(s_-,\theta)=0\text{ or }g(s_+,\theta)=0
&&\text{endpoint crossing},\\
&J_\xi=0
&&\text{loss of the director-area tube carrier},\\
&\text{tube segment or label leaves the retained domain}
&&\text{domain/chart/interface exit}.
\end{aligned}
}
\]

Interior peak branching is absent from this minimal list.

---

## 9. Compact finite-order hard hull consequence

M17-088 gives a finite critical-order bound on the compact analytic peak-floor hull absent endpoint/rank/chart degeneration.

M17-103 shows that even if several finite critical strata collide internally, the signed carrier degree survives without type-by-type matching.

Therefore the candidate nonrecyclable set on that hull contracts to

\[
\boxed{
E_{nonrecyclable}^{R2}
\subset
E_{endpoint}
\cup
E_{J_\xi=0}
\cup
E_{domain/chart/interface}.
}
\]

This is a stronger branch reduction than M17-102.

---

## 10. DSD interpretation

There are two different levels of genealogy:

### point genealogy

Which exact maximum at time `theta_1` becomes which maximum at `theta_2`?

This may be nonunique at branching events.

### carrier genealogy

Does the same director-area tube survive, and what is the algebraic zero degree of `g` between its endpoints?

This remains well defined without resolving individual points.

For conserved-flux auditing, the second is the structurally correct level.

---

## 11. DSD audit

### Audit A — requiring unique peak tracks to prove signed flux conservation
Rejected.

### Audit B — extending type-resolved positive measures through singular events without a jet chart
Still rejected. The stronger result concerns only algebraic carrier flux.

### Audit C — claiming unsigned peak count is conserved
Rejected. It may change arbitrarily by internal pairs.

### Audit D — claiming endpoint degree is a new Navier--Stokes invariant
It is an inherited one-dimensional algebraic intersection invariant conditional on a persistent frozen tube segment and fixed endpoint signs.

### Audit E — suppressing endpoint/rank/interface exits
Rejected. They are now the only minimal carrier-level source classes.

### Audit F — proof status
Interior finite peak genealogy is fully recyclable at the signed director-area carrier level, but endpoint/rank/interface costs are not yet assembled with the rest of the proof frontier.

---

## 12. Updated Rank-2 carrier frontier

The Rank-2 peak/type/tangency hierarchy now satisfies

\[
\boxed{
E_{interior\ peak/type/tangency}^{finite}
\Longrightarrow
\text{signed director-area-flux neutral}.
}
\]

Hence

\[
\boxed{
R_{2,pure-kernel}^{compact\ finite-order}
\Longrightarrow
R_{2}^{persistent\ carrier}
\ \lor\
E_{endpoint}
\ \lor\
E_{J_\xi=0}
\ \lor\
E_{domain/chart/interface}.
}
\]

The next high-value problem is no longer local peak genealogy. It is the **carrier-exit assembly gate**: determine whether endpoint escape, `J_xi->0` rank loss, and chart/interface transfer can recycle the required Rank-2 Riccati compensation and director-area flux indefinitely inside the global recurrent hard hull, or whether one of the already established global transport ledgers assigns a nonrecyclable cost to those exits.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
