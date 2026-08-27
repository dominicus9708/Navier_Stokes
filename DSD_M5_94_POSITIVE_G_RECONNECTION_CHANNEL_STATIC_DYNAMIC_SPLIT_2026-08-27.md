# DSD M5-94 — Positive-G Reconnection Channel: Static/Dynamic Split

Date: 2026-08-27

Status: **FOUR-CHAIN AUDIT OF THE SURVIVING `G>0` ENDPOINT / NORMAL CROSSING AND ANGULAR RECONNECTION ARE RESOLVED AS DISTINCT AXIAL CHANNELS / ZERO-FLUX CANCELLATION SPLITS INTO INTRA-SURFACE SIGN REVERSAL, INTER-SURFACE TOPOLOGICAL CANCELLATION, OR A MIXED MODE / THIS IDENTIFIES TWO DIFFERENT MATHEMATICAL INEQUALITIES NEEDED FOR FINAL RECONNECTION RIGIDITY / GLOBAL REGULARITY UNPROVED.**

## 1. Surviving input after M5-92/M5-93

The exact zero-angular corridor is closed.

On the robust returned upstroke class,

\[
G_w\ge G_*>0.
\]

The remaining exact minimal-payer candidate may still satisfy

\[
X_w
=
\nu(T_w-A_w-G_w)>0,
\]

so

\[
\boxed{T_w>A_w+G_w.}
\]

The purpose of the present audit is to identify what `G` is doing structurally rather than treating it as an unspecified positive remainder.

---

# 2. Formation chain: one full boundary, several surface pieces

Fix one regular positive amplitude value `lambda` and one bounded connected superlevel component

\[
\Omega_{\lambda,k}.
\]

Write its full boundary as

\[
\Gamma
=
\bigsqcup_{j=1}^{N}\Gamma_j.
\]

The component is one formed volume object; the `Gamma_j` are surface subobjects of its full boundary.

Componentwise incompressibility gives only

\[
\boxed{
\sum_{j=1}^N
\int_{\Gamma_j}U\cdot n\,dS
=0.
}
\]

This does not specify how the cancellation is distributed among the `Gamma_j`.

---

# 3. Axial chain: exact normal/tangential decomposition

On a regular level define

\[
q:=U\cdot n,
\qquad
v:=U-qn,
\qquad
v\cdot n=0.
\]

Since `|U|=lambda` on the level,

\[
\boxed{q^2+|v|^2=\lambda^2.}
\]

The crossing variable is

\[
b
=
\frac{|\nabla a|}{\lambda}q.
\]

Using coarea, the two axial quadratic channels have parallel surface forms:

\[
\boxed{
T_w
=
\int
w(\lambda)
\sum_k
\int_{\Gamma_{\lambda,k}}
\frac{|\nabla a|}{\lambda}q^2\,dS\,d\lambda,
}
\]

and

\[
\boxed{
G_w
=
\int
w(\lambda)
\sum_k
\int_{\Gamma_{\lambda,k}}
\frac{|\nabla a|}{\lambda}|v|^2\,dS\,d\lambda.
}
\]

Therefore `T` and `G` are not unrelated defects. They are the normal and tangential pieces of the same amplitude-boundary velocity magnitude.

Indeed

\[
\boxed{
T_w+G_w
=
\int
w(\lambda)
\sum_k
\int_{\Gamma_{\lambda,k}}
\lambda|\nabla a|\,dS\,d\lambda.
}
\]

This recovers the previously used `C=T+G` decomposition in explicitly axial form.

---

# 4. Static aggregation: how can zero flux occur?

For one full boundary,

\[
\sum_j\int_{\Gamma_j}q\,dS=0.
\]

There are exactly three structural possibilities.

## Mode I — intra-surface sign reversal

At least one connected surface `Gamma_j` contains both

\[
q>0
\]

and

\[
q<0.
\]

By continuity there is a nonempty zero set where

\[
q=0.
\]

But `|U|=lambda>0`, so at such points

\[
\boxed{|v|=\lambda.}
\]

Thus a same-surface sign reversal must pass through a purely tangential crossing state.

In axial language:

\[
\boxed{
\text{normal sign reversal on one connected surface}
\Rightarrow
\text{angular channel activation}.
}
\]

This is exact pointwise structure.

It is not yet an integrated lower bound for `G_w`; obtaining such a lower bound requires control of the width/geometry of the sign-transition zone.

## Mode II — inter-surface cancellation

Every connected `Gamma_j` is sign-definite in `q`, but different surface components carry opposite signs.

Then zero full-boundary flux is obtained by cancellation between separate surface pieces.

This is a **topological aggregation channel**: the volume component must have multiple boundary surfaces.

M5-92 proves that the limiting case in which those surfaces are everywhere exactly normal (`G=0`) is impossible.

Therefore any admissible inter-surface cancellation must depart from the exact-normal geometry somewhere in the active structure.

## Mode III — mixed cancellation

Some surfaces reverse sign internally and multiple surfaces also exchange net flux.

Both the angular and topological channels are active.

---

# 5. Static node/residual decomposition

For structural bookkeeping define the unweighted surface mean

\[
\bar q_j
:=
\frac1{|\Gamma_j|}
\int_{\Gamma_j}q\,dS.
\]

Then

\[
q
=
\bar q_j+(q-\bar q_j)
\]

on each surface.

The full zero-flux condition becomes

\[
\boxed{
\sum_j|\Gamma_j|\bar q_j=0.
}
\]

This separates two different crossing modes:

- `q-bar q_j`: within-surface variation/sign reconstruction;
- `bar q_j`: inter-surface mean transport.

For the ordinary surface `L2` crossing energy,

\[
\int_{\Gamma}|q|^2dS
=
\sum_j
\int_{\Gamma_j}|q-\bar q_j|^2dS
+
\sum_j
|\Gamma_j||\bar q_j|^2.
\]

Thus even before inserting the coarea weight, the normal crossing splits exactly into

\[
\boxed{
\text{intra-surface fluctuation}
+
\text{inter-surface mean mode}.}
\]

The final weighted `T_w` requires additional control of `|grad a|/lambda`; the present identity is the structural decomposition that tells us what must be estimated.

---

# 6. What mathematical estimate belongs to each DSD branch?

## Branch I — intra-surface mode

Because the zero-mean or sign-changing part lives on one connected surface, the natural calculation is a surface Poincare/Cheeger-type estimate schematically of the form

\[
\int_{\Gamma_j}|q-\bar q_j|^2
\lesssim
C_{geom}
\int_{\Gamma_j}|\nabla_\Gamma q|^2.
\]

Tangential derivatives of `q=U dot n` are built from derivatives of `U` and of the level geometry, so they should be compared with the formation term `A_w` and the angular channel `G_w`.

The missing issue is uniform control of the relevant surface geometry across the recurrent class.

## Branch II — inter-surface mean mode

Surface Poincare cannot see constants of opposite sign on disconnected boundary pieces.

That mode must be controlled through the **volume between the surfaces**.

M5-92 shows the exact-normal constant-sign limit is impossible by the inner-boundary curvature obstruction.

The quantitative continuation of that argument should estimate how much `A_w` and/or `G_w` is required to deform away from the forbidden mean-curvature law

\[
H=-|\nabla a|/a.
\]

This is a volume/topology stability problem, not a surface Poincare problem.

Hence the desired global reconnection inequality naturally decomposes into two lemmas:

\[
\boxed{
T_{intra}
\lesssim
A+G
}
\]

and

\[
\boxed{
T_{inter}
\lesssim
A+G.
}
\]

Only after both are established can one hope to recover a statewise estimate comparable to

\[
T\le A+G
\]

or another constant strong enough to contradict the positive endpoint.

---

# 7. Dynamical chain

The three static modes are not permanent labels.

A returned W1 trajectory may transition among them.

### Intra -> inter

A connected sign-changing surface may split or a new cavity may form. This requires a critical/topology event in the level-set description.

### Inter -> intra

Boundary components may merge or a sign-definite surface may develop a zero of `q`, activating the angular channel.

### Sign changes on a tracked regular surface

As already audited in M5-91, a sign change requires passage through

\[
q=0,
\]

hence full tangential velocity at that point.

Therefore the dynamical chain records every reconnection as either

\[
\boxed{
\text{angular transition}
\quad\text{or}\quad
\text{critical/topological transition}.}
\]

---

# 8. Four-chain cross-audit verdict

## Formation

Multiple boundary surfaces and same-surface sign structures are both admissible formed states.

## Axial property

`T` and `G` are the normal and tangential projections of the same level-boundary velocity channel.

## Static aggregation

Zero flux does not erase `T`; it partitions `T` into intra-surface fluctuation and inter-surface mean modes.

## Dynamics

Reconnection between these modes necessarily passes through angular or critical/topological transitions.

The central DSD result is therefore

\[
\boxed{
\text{zero-flux reconnection}
=
\text{intra-surface axial reconnection}
\oplus
\text{inter-surface topological reconnection},
}
\]

with a mixed sector allowed.

---

# 9. Updated proof gate

The previous single target

\[
T\le A+G
\]

is now replaced by two more precise targets.

### Gate R1 — surface reconnection inequality

Control the intra-surface normal-crossing variance by tangential/formation geometry.

### Gate R2 — cavity/inter-surface stability inequality

Control the inter-surface mean crossing by quantitative distance from the forbidden M5-92 exact-normal cavity geometry.

If both gates produce constants whose combined coefficient is at most one in the normalized endpoint ledger, then

\[
X_w=\nu(T-A-G)>0
\]

is impossible statewise and no separate accumulation budget is needed.

If the constants are weaker, the resulting remainder must be sent through the static/dynamic recurrence audit rather than declared contradictory.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]