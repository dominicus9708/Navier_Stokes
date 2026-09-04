# DSD M17-097 — Director-area flux tubes give a canonical inherited weight to transverse Rank-2 peak sheets

Date: 2026-09-05
Canonical ID: **M17-097**

Status: **INTERNAL RANK-2 INHERITED PEAK-WEIGHT GATE / M17-094 DELIBERATELY USED ONLY BOOKKEEPING WEIGHTS BECAUSE NO CANONICAL PEAK COUNTING MEASURE HAD BEEN DERIVED. ON THE PURE-TRANSVERSE-KERNEL BRANCH, HOWEVER, THE NONZERO DIVERGENCE-FREE DIRECTOR-AREA CURRENT `J_xi=|J_xi| k` IS ALREADY A FROZEN-IN CAUCHY FLUX. WHERE A PEAK SHEET `g=D_xi log rho=0` IS TRANSVERSE TO `J_xi`, EQUIVALENTLY `D_k g != 0`, EACH FROZEN DIRECTOR-AREA FLUX TUBE INTERSECTS THE PEAK SHEET LOCALLY IN A UNIQUE POINT AND ITS CONSERVED FLUX SUPPLIES A GEOMETRIC PEAK WEIGHT. FOLLOWING THE SAME FLUX TUBE AND SLIDING ALONG `k` TO REMAIN ON `g=0` GIVES THE CANONICAL RELATIVE SPEED `alpha_J=-D_B g/D_k g=-D_xi(sigma+kappa)/D_k g` AT A PEAK. THE CURVATURE-NORMALIZED TYPE VARIABLE THEN OBEYS `D_J Z_nu=S_nu^crit-alpha_J_abs D_k Z_nu` WITH THE SIGNED FORM BELOW. THIS REMOVES THE ARBITRARY WEIGHT ON THE TRANSVERSE SUBBRANCH. THE COMPLEMENT `D_k g=0` IS AN EXPLICIT DIRECTOR-AREA-TANGENCY BRANCH, NOT COVERED BY THIS WEIGHT. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Existing director-area flux

On Rank 2 define

\[
\boxed{
J_\xi^k
=\frac12\varepsilon^{kij}
\xi\cdot(\partial_i\xi\times\partial_j\xi).
}
\]

M17-026 gives

\[
\boxed{\nabla\cdot J_\xi=0}
\]

and the Cauchy law

\[
\boxed{
D_BJ_\xi
=(\nabla B)J_\xi
-\frac32J_\xi.
}
\]

Equivalently, the two-form

\[
\boxed{\beta_\xi:=\iota_{J_\xi}dV}
\]

is frozen into the similarity material flow:

\[
\boxed{
(\partial_\theta+\mathcal L_B)\beta_\xi=0.
}
\]

Thus director-area flux through material cross-sections is an already established invariant.

---

## 2. Pure-kernel frame

On the full-rank pure-transverse-kernel branch,

\[
\boxed{
J_\xi=|J_\xi|k,
\qquad
(k\cdot\nabla)\xi=0,
\qquad
|J_\xi|>0.
}
\]

Let

\[
\boxed{g:=D_\xi\log\rho.}
\]

A linewise amplitude peak lies on the critical set

\[
\boxed{g=0.}
\]

Let `S(theta)` be a smooth local component of this peak sheet.

---

## 3. Transversality to director-area flux

The director-area current crosses the peak sheet iff

\[
J_\xi\cdot n_S\neq0.
\]

Since `J_xi` is parallel to `k` and `n_S` is parallel to `grad g`, this is equivalent to

\[
\boxed{D_k g\neq0.}
\]

When this holds, the implicit function theorem gives a unique local intersection of each nearby director-area flux tube with `S(theta)`.

Thus the peak sheet can be parametrized by frozen director-area flux-tube labels rather than by an arbitrary counting label.

---

## 4. Canonical flux weight

Choose an orientation on a connected transverse component so that

\[
J_\xi\cdot n_S>0.
\]

The induced peak-sheet measure is

\[
\boxed{
d\Phi_J
:=J_\xi\cdot n_S\,dA.
}
\]

This is the director-area flux carried by the corresponding tube bundle.

Because `beta_xi` is frozen in and closed, the flux assigned to a fixed tube label is conserved while the regular tube and chart survive.

Hence `dPhi_J` is a **geometrically inherited peak weight**, not an invented maximum-counting measure.

If the orientation is reversed, both the signed measure and all signed currents below reverse together.

---

## 5. Canonical intersection velocity

A director-area tube is transported by `B`.
To remain on the moving peak sheet, allow the intersection point to slide along the same tube by

\[
\alpha_Jk.
\]

The peak condition must remain zero:

\[
0=(D_B+\alpha_JD_k)g.
\]

Therefore

\[
\boxed{
\alpha_J
=-\frac{D_Bg}{D_kg}.
}
\]

M17-040 gives

\[
D_Bg
=D_\xi(\sigma+\kappa)
-\left(\sigma+\frac12\right)g.
\]

At a peak `g=0`,

\[
\boxed{
\alpha_J
=-\frac{D_\xi(\sigma+\kappa)}{D_kg}.
}
\]

Thus the flux-tube-labelled peak derivative is

\[
\boxed{
D_J^*
:=D_B+\alpha_JD_k.
}
\]

---

## 6. Canonical dynamics of the normalized critical type

M17-093 gives

\[
D_BZ_\nu
=S_\nu^{crit},
\]

where

\[
S_\nu^{crit}
=\frac{D_\xi^{\nu+1}(\sigma+\kappa)}{|b|^{\nu+1}}.
\]

Therefore along the director-area-flux-labelled peak track,

\[
\boxed{
D_J^*Z_\nu
=S_\nu^{crit}
-\frac{D_\xi(\sigma+\kappa)}{D_kg}
D_kZ_\nu.
}
\]

Define

\[
\boxed{
S_{\nu,J}
:=
S_\nu^{crit}
-\frac{D_\xi(\sigma+\kappa)}{D_kg}
D_kZ_\nu.
}
\]

Then

\[
\boxed{D_J^*Z_\nu=S_{\nu,J}.}
\]

No arbitrary relative velocity remains on this transverse subbranch.

---

## 7. Flux-weighted type distribution

Let `Lambda_nu` be a fixed family of director-area flux-tube labels whose intersections with the peak sheet remain regular and type `nu` on a time interval.

Define

\[
\boxed{
F_\nu^J(z,\theta)
:=\int_{\Lambda_\nu}
\delta(z-Z_\nu(\lambda,\theta))
\,d\Phi_J(\lambda).
}
\]

Define

\[
\boxed{
G_\nu^J(z,\theta)
:=\int_{\Lambda_\nu}
S_{\nu,J}(\lambda,\theta)
\delta(z-Z_\nu(\lambda,\theta))
\,d\Phi_J(\lambda).
}
\]

Because the flux measure is fixed on the frozen tube labels,

\[
\boxed{
\partial_\theta F_\nu^J
+\partial_zG_\nu^J
=0
}
\]

distributionally on every interval with no tube-label birth/death, type switch, tangency, rank loss, or chart exit.

This is the inherited-weight upgrade of M17-094.

---

## 8. Event source in the nonpersistent case

If the transverse tube-sheet intersection is created or destroyed, if the type changes, if `D_k g -> 0`, if `J_xi -> 0`, or if the chart exits, the correct equation is

\[
\boxed{
\partial_\theta F_\nu^J
+\partial_zG_\nu^J
=\mathcal B_\nu^J.
}
\]

The source `B_nu^J` records those geometric events.

Cross-type cancellation is not automatic; it requires matching the outgoing and incoming tube labels through the event.

---

## 9. New explicit tangency branch

The inherited weight fails precisely when

\[
\boxed{D_k g=0.}
\]

At such a point the director-area current lies tangent to the peak sheet.

This is not a failure of Rank 2 because

\[
J_\xi\neq0
\]

may still hold.
It is a **director-area/peak-sheet tangency** and must be retained as a separate branch.

Thus

\[
\boxed{
R_{2,peak}
\Longrightarrow
R_{2,peak}^{J\text{-}transverse}
\ \lor\
T_{J\parallel peak}.
}
\]

---

## 10. Relation to M17-094

M17-094 used fixed bookkeeping weights because no inherited weight was yet available.

M17-097 shows that on `D_k g != 0`, the arbitrary weights can be replaced by the existing director-area flux.

Therefore the correct hierarchy is

\[
\boxed{
\text{arbitrary tracked population}
\supset
\text{director-area-flux-labelled transverse population}.
}
\]

M17-094 remains necessary for tangency/interface populations and for audits where no flux-tube parametrization is available.

---

## 11. DSD audit

### Audit A — using point-counting as a physical measure
Closed on the transverse subbranch by `dPhi_J`.

### Audit B — taking absolute director-area flux across orientation changes
Avoided. Work on an orientation-fixed connected component; orientation/tangency events are separate.

### Audit C — forgetting that the peak is not material
Avoided by the explicit slide speed `alpha_J` along the frozen director-area tube.

### Audit D — applying the flux measure at `D_k g=0`
Rejected. This is the explicit tangency branch.

### Audit E — claiming a sign for `G_nu^J(0)`
Rejected. The source `S_{nu,J}` remains signed.

### Audit F — proof status
A canonical Rank-2 peak weight is obtained on the transverse subbranch, but no irrecoverable type-turnover cost is yet proved.

---

## 12. Updated Rank-2 frontier

On a transverse peak sheet,

\[
\boxed{
D_kg\neq0
}
\]

provides the inherited weight

\[
\boxed{d\Phi_J=J_\xi\cdot n_S\,dA}
\]

and the exact type current

\[
\boxed{
G_\nu^J
=\int S_{\nu,J}\delta(z-Z_\nu)d\Phi_J.
}
\]

The next question is whether the `Z_nu=0` type-turnover flux and the Riccati compensation margin can both be maintained with this same director-area flux population, or whether recurrent compensation requires passage into the tangency/event source.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
