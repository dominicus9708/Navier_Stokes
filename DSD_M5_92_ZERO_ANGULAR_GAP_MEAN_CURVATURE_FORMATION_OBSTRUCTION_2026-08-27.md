# DSD M5-92 — Zero-Angular-Gap Mean-Curvature Formation Obstruction

Date: 2026-08-27

Status: **EXACT ZERO-ANGULAR-GAP SUBCORRIDOR CLOSED UNDER THE ACTIVE-BAND SMOOTHNESS/BOUNDEDNESS ASSUMPTIONS / FORMATION + AXIAL + STATIC + DIFFERENTIAL GEOMETRY FORCE A FORBIDDEN INNER-BOUNDARY MEAN-CURVATURE OR A NONZERO NET FLUX / THIS IS AN ALGORITHMIC DSD CROSS-AUDIT WITH A STANDARD GEOMETRIC CALCULATION / GENERAL POSITIVE-G ENDPOINT REMAINS / GLOBAL REGULARITY UNPROVED.**

## 1. Input from M5-91

Assume an exact smooth endpoint on an open positive amplitude band where

\[
G_w=0.
\]

Because the weight is positive on the interior of its active band and the fields are smooth,

\[
U\times\nabla a=0
\]

throughout the corresponding open spatial region.

Write

\[
a=|U|>0,
\qquad
n=\frac{\nabla a}{|\nabla a|}.
\]

On each connected region where `grad a != 0`, continuity gives one sign

\[
\sigma\in\{+1,-1\}
\]

such that

\[
\boxed{U=\sigma a n.}
\]

---

# 2. Formation chain

Choose a regular amplitude value `lambda` in the active band and one bounded connected component

\[
\Omega_{\lambda,k}\subset\{a>\lambda\}.
\]

The fixed positive band is spatially bounded in the W1 cell because the `1/r` tail eventually falls below the band.

Its full smooth boundary may a priori have

1. one outer surface; or
2. one outer surface plus one or more inner surfaces surrounding bounded low-amplitude holes.

These are the only formed smooth bounded possibilities relevant to the present local topology.

---

# 3. Axial chain: zero angular gap fixes the normal field

On every regular level in the open zero-gap band,

\[
U=\sigma a n.
\]

The sign is locally constant and therefore may be pulled through a divergence calculation.

Using incompressibility,

\[
0=\nabla\cdot U
=\sigma\nabla\cdot(an).
\]

Now

\[
\nabla\cdot(an)
=\nabla a\cdot n+a\nabla\cdot n
=|\nabla a|+aH,
\]

where

\[
H:=\nabla\cdot n
\]

is the scalar mean curvature in this convention.

Therefore

\[
\boxed{
H=-\frac{|\nabla a|}{a}<0.
}
\]

This holds pointwise on every regular level surface in the exact zero-angular-gap band.

This is the key axial-to-geometric conversion.

---

# 4. Static aggregation: why an inner boundary would be required

M5-91 already showed that if the full boundary had only one connected surface, then

\[
U\cdot n=\sigma\lambda
\]

has one nonzero constant sign on that surface and

\[
\int_{\Gamma}U\cdot n\,dS
=\sigma\lambda|\Gamma|\ne0.
\]

This violates componentwise incompressibility.

Hence an exact zero-gap candidate would need more than one boundary component so that opposite signed surface fluxes can cancel.

Thus the Formation/Static chains force the candidate toward a bounded internal hole.

---

# 5. Geometric lemma: a bounded hole cannot have H<0 everywhere with outward normal

Let `D` be a bounded smooth region in `R^3` and let `n_D` be its outward normal.

Its boundary cannot satisfy

\[
H_D:=\nabla\cdot n_D<0
\]

everywhere.

A short proof uses the squared distance from an interior point.

Choose `x_0 in D` and let

\[
f(x)=|x-x_0|^2
\]

on `partial D`.

At a point `p` where `f` is maximal, the tangential gradient vanishes and

\[
p-x_0
\]

points in the outward normal direction, so

\[
(p-x_0)\cdot n_D>0.
\]

For the convention `H_D=div n_D`, the surface identity is

\[
\Delta_{\partial D}|x-x_0|^2
=
4-2H_D(x-x_0)\cdot n_D.
\]

At the maximum,

\[
\Delta_{\partial D}f\le0.
\]

Hence

\[
H_D(p)(p-x_0)\cdot n_D(p)\ge2,
\]

and therefore

\[
\boxed{H_D(p)>0.}
\]

So no bounded smooth region has outward mean curvature strictly negative at every boundary point.

---

# 6. Apply the lemma to an inner low-amplitude hole

Suppose `Omega_{lambda,k}` has an inner boundary component surrounding a bounded complementary region `D` with

\[
a<\lambda
\]

on the hole side and

\[
a>\lambda
\]

on the superlevel side.

The direction

\[
n=\frac{\nabla a}{|\nabla a|}
\]

points from the low-amplitude hole toward the high-amplitude superlevel region.

Therefore on this inner boundary, `n` is exactly the **outward normal of the bounded hole `D`**.

But the zero-angular incompressibility relation requires

\[
H=\nabla\cdot n
=-\frac{|\nabla a|}{a}<0
\]

everywhere on that boundary.

This contradicts the bounded-hole geometric lemma.

Hence

\[
\boxed{
\text{no inner boundary component can exist in an exact smooth }G=0\text{ active band.}
}
\]

---

# 7. Return to the outer boundary

Without inner boundary components, the bounded connected superlevel component has only its outer boundary.

On that connected regular surface,

\[
U=\sigma\lambda n
\]

with fixed `sigma`.

Therefore

\[
\int_{\Gamma}U\cdot n\,dS
=
\sigma\lambda|\Gamma|
\ne0,
\]

again contradicting incompressibility.

Thus both possibilities are eliminated:

\[
\boxed{
\begin{array}{rcl}
\text{single boundary}&\Rightarrow&\text{nonzero net flux},\\
\text{multiple boundaries}&\Rightarrow&\text{forbidden inner-boundary curvature}.
\end{array}
}
\]

Consequently

\[
\boxed{
\text{nontrivial bounded smooth positive-amplitude }G=0\text{ endpoint is impossible.}
}
\]

---

# 8. Four-chain DSD audit

## Formation

The punctured source model is rejected, and a smooth internal hole is the only formed alternative after zero-flux aggregation.

**Result: hole branch formed, then passed to cross-audit.**

## Axial property

`G=0` makes the velocity exactly normal and gives

\[
H=-|grad a|/a.
\]

**Result: exact negative-curvature orientation.**

## Static aggregation

One boundary cannot cancel flux; multiple boundaries are required.

**Result: inner hole required.**

## Dynamics

No time argument is needed once the exact static state is impossible.

**Result: endpoint removed statewise.**

## Cross-audit

Formation demands a bounded hole while the axial curvature law forbids such a hole.

Therefore the candidate is rejected at the `F-X-S` cross-interface before recurrence is invoked.

---

# 9. Compactness consequence

Consider the compact returned pump class from M5-57/M5-85 with a fixed positive active band and nontrivial crossing.

If a sequence had

\[
G_{w,n}\to0,
\]

local smooth W1 compactness would produce a limiting active-band state with

\[
U_*\times\nabla a_*=0
\]

and nontrivial retained crossing.

The preceding statewise obstruction excludes that limit, provided the active bounded component persists as supplied by the positive-band pump localization.

Thus the DSD audit supports the next compactness target

\[
\boxed{
G_w\ge G_*>0
}
\]

on a sufficiently small compact recurrent pump neighborhood.

A separate memo should state the exact hypotheses needed for this uniform-gap promotion; the present memo proves the zero-gap state itself impossible.

---

# 10. What is and is not closed

### CLOSED

The exact zero-angular-gap endpoint

\[
G_w=0
\]

with a nontrivial bounded positive-amplitude crossing component.

### NOT CLOSED

The general exact M5-70 endpoint with

\[
G_w>0.
\]

The remaining reconnection can use tangential/oblique velocity and therefore avoids the strict mean-curvature law above.

The next DSD audit should treat `G>0` as a genuine reconnection channel rather than as an error term and ask how its formation/axial/static/dynamic roles interact with `T` and `A_w`.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]