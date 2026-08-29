# DSD M5-281 — Remote Satellite Parabolic Point-Picking and Ambient-Strain Fork

Date: 2026-08-30

Parent: `DSD_M5_280_H_AND_CAMPANATO_ESCALATION_COMMON_REMOTE_SATELLITE_REDUCTION_2026-08-30.md`

Status: **SATELLITE NORMALIZATION / `Lambda_R -> infinity` PROVIDES ENOUGH SPACE-SCALE SEPARATION FOR A PARABOLIC DOUBLING/POINT-PICKING ARGUMENT / ONE MAY RESELECT A REMOTE SATELLITE POINT AND ITS VORTICITY-NATURAL SCALE SO THAT THE RESCALED VORTICITY IS NONZERO AT THE ORIGIN AND UNIFORMLY BOUNDED ON ARBITRARILY LARGE BACKWARD PARABOLIC CYLINDERS WHILE THE ORIGINAL TRACKED CORE ESCAPES TO SPATIAL INFINITY / VORTICITY CONTROL ALONE DOES NOT GIVE VELOCITY COMPACTNESS BECAUSE A LARGE CURL-FREE/DIVERGENCE-FREE HARMONIC STRAIN COMPONENT MAY REMAIN / THE SATELLITE FRONTIER THEREFORE SPLITS INTO BOUNDED-AMBIENT-STRAIN DETACHED ANCIENT COMPACTNESS OR AN AMBIENT-STRAIN H EXIT / GLOBAL REGULARITY UNPROVED.**

---

## 1. Satellite data from M5-280

Take a sequence of normalized ancient/W1 snapshots with satellite points `(Y_n,s_n)` and vorticity amplitudes

\[
m_n:=|\Omega(Y_n,s_n)|>0.
\]

Define the vorticity-natural scale

\[
\ell_n:=m_n^{-1/2}.
\]

The remote-satellite condition is

\[
\boxed{
\frac{|Y_n|}{\ell_n}	o\infty.
}
\]

Equivalently, with

\[
Q_n:=m_n^{1/2}=\ell_n^{-1},
\]

we have

\[
\boxed{Q_n|Y_n|\to\infty.}
\]

This is exactly the large distance-times-curvature parameter required by a doubling point-selection argument.

---

## 2. Work in genuine Navier–Stokes ancient variables

Use the global RG ancient solution from M5-274 whenever the branch has reached that stage, or equivalently perform the same calculation in the corresponding physical first-hitting variables before the similarity drift is introduced.

Write the genuine Navier–Stokes ancient variables as

\[
u(x,t),
\qquad
\omega=\nabla\times u.
\]

Let the satellite point be `(x_n,t_n)` with

\[
q_n:=|\omega(x_n,t_n)|^{1/2}
\]

and let `d_n` denote its distance from the tracked main-core center in the same variables.

The satellite condition is invariant under Navier–Stokes scaling:

\[
\boxed{q_nd_n\to\infty.}
\]

---

## 3. Backward parabolic point-picking lemma

Fix any sequence

\[
A_n\to\infty
\]

so slowly that

\[
A_n=o(q_nd_n).
\]

Consider the backward parabolic neighborhood of `(x_n,t_n)` and apply the standard doubling selection to the quantity

\[
Q(x,t):=|\omega(x,t)|^{1/2}.
\]

If within the candidate parabolic ball there exists a point with

\[
Q>2Q_{current},
\]

move to that point and repeat.

At each move the new natural radius is at most half the old one. Therefore the total spatial displacement is bounded by a geometric series of the form

\[
\lesssim
\frac{A_n}{q_n}
\left(1+\frac12+\frac14+\cdots\right)
\lesssim
\frac{2A_n}{q_n}.
\]

Since

\[
A_n/(q_nd_n)\to0,
\]

the final selected point remains remote from the main core:

\[
\boxed{
\frac{d_n^*}{\ell_n^*}\to\infty.
}
\]

The iteration terminates because the vorticity is finite on each smooth preterminal slice / retained first-hitting interval.

Thus one obtains `(x_n^*,t_n^*)` and

\[
q_n^*:=|\omega(x_n^*,t_n^*)|^{1/2}
\]

such that

\[
q_n^*\ge q_n
\]

and

\[
\boxed{
|\omega(x,t)|
\le4(q_n^*)^2
}
\]

on the backward parabolic cylinder

\[
\boxed{
B_{A_n/q_n^*}(x_n^*)
\times
[t_n^*-A_n^2/(q_n^*)^2,\,t_n^*].
}
\]

Only backward time is used, so no positive future lifespan relative to the satellite scale is required.

---

## 4. Satellite-centered scaling

Define

\[
\widetilde u_n(z,\sigma)
:=
(q_n^*)^{-1}
 u\left(
 x_n^*+\frac{z}{q_n^*},
 t_n^*+\frac{\sigma}{(q_n^*)^2}
 \right),
\]

with corresponding vorticity

\[
\widetilde\omega_n(z,\sigma)
=
(q_n^*)^{-2}
\omega\left(
 x_n^*+\frac{z}{q_n^*},
 t_n^*+\frac{\sigma}{(q_n^*)^2}
 \right).
\]

Then

\[
\boxed{
|\widetilde\omega_n(0,0)|=1,
}
\]

and

\[
\boxed{
|\widetilde\omega_n(z,\sigma)|\le4
}
\]

on

\[
B_{A_n}\times[-A_n^2,0].
\]

Since

\[
A_n\to\infty,
\]

the vorticity normalization itself is sufficient for a **global backward vorticity cap on every fixed compact cylinder after diagonalization**.

The tracked main core lies at normalized distance

\[
q_n^*d_n^*\to\infty,
\]

so it disappears to spatial infinity in the satellite frame.

---

## 5. What the vorticity cap controls

On every fixed satellite cylinder, the local vorticity is uniformly bounded:

\[
\|\widetilde\omega_n\|_{L^\infty}\le4.
\]

This controls the rotational part of the velocity gradient.

However it does **not** control the full local strain from remote sources.

A divergence-free and curl-free vector field may have a nontrivial harmonic gradient.  For example, locally a trace-free linear field

\[
h(z)=Sz,
\qquad
\operatorname{tr}S=0,
\]

has

\[
\nabla\times h=0
\]

while

\[
|\operatorname{sym}\nabla h|=|S|
\]

can be arbitrarily large.

Therefore the implication

\[
\boxed{
\|\widetilde\omega_n\|_\infty\le4
\Longrightarrow
\text{velocity compactness}
}
\]

is false without an additional local-energy/strain normalization.

This is an essential firewall.

---

## 6. Near-vorticity / harmonic-strain decomposition

Fix one satellite ball `B_R`.

Using a cutoff on `B_{2R}`, decompose the velocity gradient schematically into

\[
\boxed{
\nabla\widetilde u_n
=
\mathcal R(\chi\widetilde\omega_n)
+
H_n,
}
\]

where

- the first term is the local Biot–Savart/Riesz contribution from bounded vorticity;
- `H_n` is curl-free and divergence-free/harmonic on the inner ball, incorporating remote vorticity and the local velocity gauge.

For every finite `p`, the local term is uniformly bounded in `L^p(B_R)` by the vorticity cap.

Hence all failure of local gradient compactness beyond that controlled term is concentrated in

\[
H_n.
\]

Define the scaled ambient-strain measure, for example,

\[
\boxed{
\mathcal S_{amb,n}(R)
:=
\|\operatorname{sym}H_n\|_{L^2(B_R)}
}
\]

or its fixed-cylinder `L^p/C^k` strengthening used by the retained compactness topology.

---

## 7. Ambient-strain fork

There are two cases.

### A. Ambient strain is locally bounded

For every fixed `R,T`, suppose

\[
\boxed{
\sup_n
\mathcal S_{amb,n}(R,T)<\infty.
}
\]

After one constant Galilean normalization of the velocity on each selected cylinder, local div-curl/elliptic estimates give uniform velocity derivative bounds on smaller cylinders.

Together with the vorticity cap and the Navier–Stokes equation, standard parabolic bootstrapping supplies a diagonal subsequence converging to a smooth ancient satellite solution

\[
\widetilde u_\infty
\]

on

\[
\mathbb R^3\times(-\infty,0],
\]

with

\[
\boxed{
|\widetilde\omega_\infty(0,0)|=1.
}
\]

The original tracked core has escaped to infinity, so this is a **detached nontrivial ancient satellite**.

### B. Ambient strain is not locally bounded

If the harmonic/remote strain component loses compactness on some fixed normalized satellite cylinder, then the satellite construction has exposed a new derivative/strain concentration at a smaller or comparable active scale.

This is precisely another H-type event:

\[
\boxed{H_{ambient}.}
\]

Thus

\[
\boxed{
S_{remote}
\Longrightarrow
\text{detached ancient satellite}
\lor H_{ambient}.
}
\]

---

## 8. Relation to dynamic turnover

The point-picking construction assumes the satellite can be observed through a backward local cylinder.

If the required local packet cannot be kept inside the moving observation cylinder because of material crossing, pressure transfer, center replacement, or localization correction, that failure is already a dynamic T event.

Hence the full satellite route is more accurately

\[
\boxed{
S_{remote}
\Longrightarrow
T_{dynamic}
\lor H_{ambient}
\lor A_{detached},
}
\]

where `A_detached` denotes the nontrivial detached ancient satellite class.

---

## 9. What is known and what remains

The detached limit has strong local properties:

\[
|\widetilde\omega|\le4,
\qquad
|\widetilde\omega(0,0)|=1,
\]

and is smooth on every fixed backward compact cylinder under case A.

What is **not** yet automatic is a global critical velocity bound such as

\[
\sup_{t<0}\|\widetilde u(t)\|_{L^{3,\infty}}<\infty
\]

or a terminal Besov condition sufficient to reapply M5-276.

The original global weak-critical mass may escape to infinity under satellite recentering, and the harmonic component must be normalized carefully.

Therefore the detached satellite is a real new compactness object, not yet a Liouville contradiction.

---

## 10. Updated master frontier

Combining M5-280 and this note gives

\[
\boxed{
\text{singular tower}
\Longrightarrow
T_{dynamic}
\lor H_{ambient}
\lor A_{detached}.
}
\]

The H branch has been sharpened recursively: an H escalation either becomes a typed turnover, exposes an even more local ambient-strain failure, or generates a separated normalized ancient satellite.

The next high-leverage target is the detached class:

> determine whether the satellite limit inherits a weak-`L^3` restart/coherence property, or a localized Type-I/Morrey bound sufficient for a Liouville theorem, despite the original main core and global tail escaping to infinity.

This is strictly narrower than the original H/T tree.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
