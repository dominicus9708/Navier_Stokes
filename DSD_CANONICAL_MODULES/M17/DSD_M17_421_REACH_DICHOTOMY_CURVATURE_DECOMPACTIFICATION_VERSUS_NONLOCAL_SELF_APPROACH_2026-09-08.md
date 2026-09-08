# DSD M17-421 — Tubular reach splits into curvature decompactification or nonlocal self-approach, and self-approach is not a palinstrophy payer by geometry alone

Date: 2026-09-08  
Canonical ID: **M17-421**

Status: **ACTIVE GEOMETRY-EXIT CLASSIFICATION / REACH DICHOTOMY / PALINSTROPHY NO-GO**

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Objective

M17-420 closes the retained compact positive-flux exact CE-H closed-loop branch provided tubular reach or an equivalent bounded-overlap own-scale segmentation remains available.

The present module audits the exit

\[
G_{tubular\ reach/self\text{-}clustering}.
\]

The goal is to decide whether reach collapse can itself be converted into a certified palinstrophy payment, or whether it contains a genuinely geometric nonlocal self-approach subbranch.

## 2. Geometric curvature notation

To avoid collision with the CE-H coefficient `kappa`, denote the geometric curvature of a unit-speed vortex loop `Gamma` by

\[
\mathcal K_\Gamma(s)
:=
|\partial_s\xi(s)|,
\qquad
\xi=\frac{\Omega}{|\Omega|}.
\]

The CE-H coefficient remains `kappa` throughout.

## 3. Standard thickness/reach dichotomy

For a smooth embedded closed curve, the radius of the largest embedded normal tube is controlled by two independent mechanisms:

1. the minimum local radius of curvature;
2. a nonlocal doubly-critical self-distance.

Equivalently, up to the standard convention for tube radius,

\[
\boxed{
\operatorname{reach}(\Gamma)
=
\min\left\{
\frac1{\|\mathcal K_\Gamma\|_{L^\infty}},
\frac12 d_{dc}(\Gamma)
\right\}.
}
\]

Here `d_dc` is the minimum distance between distinct doubly-critical points of the curve.

This is the classical thickness decomposition used in the knot-thickness literature (Gonzalez--Maddocks; Cantarella--Kusner--Sullivan).

Therefore

\[
\boxed{
\operatorname{reach}(\Gamma_j)\to0
\Longrightarrow
\|\mathcal K_{\Gamma_j}\|_\infty\to\infty
\quad\lor\quad
d_{dc}(\Gamma_j)\to0.
}
\]

## 4. Curvature branch and loop-state compactness

M17-420 assumes precompactness in a regular loop-state topology strong enough to preserve the analytic finite-jet observables and the geometric loop laws.

If this retained topology contains uniform `C^2` geometry of the loop embedding, then

\[
\sup_j\|\mathcal K_{\Gamma_j}\|_\infty<\infty.
\]

Hence the first reach-collapse mechanism is impossible inside the retained compact branch.

It must be typed as

\[
\boxed{
G_{geometric\ C^2\ loop\text{-}state\ decompactification}.
}
\]

This is stronger and cleaner than attempting to infer a new integral payer from a pointwise curvature spike.

## 5. Vortex-direction gradient identity

For completeness, write

\[
\Omega=\rho\xi,
\qquad
\rho=|\Omega|,
\qquad
|\xi|=1.
\]

Then

\[
\nabla\Omega
=
\xi\otimes\nabla\rho
+
\rho\nabla\xi.
\]

Because `xi · partial_j xi = 0`, the cross term vanishes and

\[
\boxed{
|\nabla\Omega|^2
=
|\nabla\rho|^2
+
\rho^2|\nabla\xi|^2.
}
\]

Since a vortex line has tangent `xi`,

\[
\mathcal K_\Gamma
=|(\xi\cdot\nabla)\xi|
\le |\nabla\xi|.
\]

Thus on a positive-amplitude region `rho >= rho_* > 0`,

\[
\rho_*^2\mathcal K_\Gamma^2
\le
|\nabla\Omega|^2
\]

pointwise wherever the line curvature is evaluated.

## 6. Why a curvature supremum spike does not by itself pay palinstrophy

The estimate in Section 5 is pointwise. A reach collapse caused by

\[
\|\mathcal K_\Gamma\|_\infty\sim r^{-1}
\]

at one point does not by itself provide a lower bound on the spatial measure of the high-curvature set.

A smooth curve can contain a curvature spike of height `r^{-1}` on an arclength interval much shorter than `r^2`; then the one-dimensional bending cost

\[
\int_\Gamma \mathcal K_\Gamma^2ds
\]

need not have a scale-independent lower bound from the supremum alone.

Therefore the inference

\[
\operatorname{reach}\to0
\Longrightarrow
\text{fixed positive palinstrophy payment}
\]

is **not certified without an additional curvature-thickening/modulus hypothesis**.

This is a permanent no-go firewall.

## 7. Flux-family averaged curvature is controlled by palinstrophy when a tube already exists

If a regular positive-flux vortex-tube family `Lambda` exists with

\[
\rho\ge\rho_*>0,
\]

then the flux-coordinate identity from M17-361 gives

\[
d\Phi\,ds=\rho\,dy.
\]

Hence

\[
\int_\Lambda\oint_{\Gamma_\lambda}
\mathcal K_{\Gamma_\lambda}^2ds\,d\Phi
=
\int_{\mathcal T}
\rho |(\xi\cdot\nabla)\xi|^2dy.
\]

Using `rho >= rho_*` and Section 5,

\[
\boxed{
\int_\Lambda\oint
\mathcal K^2ds\,d\Phi
\le
\rho_*^{-1}
\int_{\mathcal T}|\nabla\Omega|^2dy.
}
\]

Thus **averaged** line curvature is a palinstrophy-order quantity on a pre-existing nondegenerate flux tube.

But this estimate cannot be used to prove the existence of that tube when reach itself is collapsing; doing so would be circular.

## 8. Nonlocal self-approach is genuinely independent of curvature energy

Assume now that

\[
\sup_j\|\mathcal K_{\Gamma_j}\|_\infty<\infty
\]

but

\[
d_{dc}(\Gamma_j)\to0.
\]

Then reach collapses because two arclength-distant portions of the same embedded loop approach each other.

There is no purely geometric lower bound forcing

\[
\int_\Gamma\mathcal K^2ds\to\infty.
\]

For example, one may keep two long nearly straight, nearly parallel strands at separation `epsilon -> 0` and connect them away from the near-contact region using arcs with uniformly bounded curvature. The self-distance tends to zero while total squared curvature stays uniformly bounded.

Therefore

\[
\boxed{
G_{nonlocal\ self\text{-}approach}
\not\Rightarrow
G_{palinstrophy\ concentration}
}
\]

from curve geometry alone.

This eliminates a false shortcut from M17-420's reach exit to the M17-307 ledger.

## 9. Exact revised reach split

The tubular-reach exit should therefore be written as

\[
\boxed{
\begin{aligned}
G_{reach\ collapse}
\Longrightarrow{}&
G_{geometric\ curvature/C^2\ decompactification}
\\
&\lor
G_{nonlocal\ doubly\text{-}critical\ self\text{-}approach}.
\end{aligned}
}
\]

Inside a genuinely `C^2`-precompact retained loop family, only the second branch remains.

## 10. Next bridge

The self-approach branch must be tested using the **vortex tube**, not the centerline alone.

If a tube carries retained flux

\[
\Phi\ge\Phi_*>0
\]

and amplitude is bounded above

\[
\rho\le M_\rho,
\]

then every material cross-section satisfies

\[
\boxed{
A\ge\frac{\Phi_*}{M_\rho}.
}
\]

Thus a self-approaching centerline can retain positive flux only if its cross-section keeps a fixed positive area while one geometric transverse clearance collapses.

This points to the next exact split:

\[
\boxed{
G_{self\text{-}approach}
\Longrightarrow
G_{cross\text{-}section\ anisotropy/shape\ decompactification}
\lor
G_{flux/amplitude\ exit}
\lor
G_{normal\text{-}chart/topology\ loss}.
}
\]

This is the target of M17-422.

## 11. DSD audit

The DSD role is only failure-type separation:

- local radius collapse;
- nonlocal injectivity collapse;
- PDE resource payer.

The audit prevents these three logically different statements from being merged.

The reach formula and all differential identities are standard mathematics.

## 12. Audit verdict

**PASS as a reach-exit decomposition and no-go theorem.**

Curvature-driven reach collapse is already geometric decompactification under the retained regular topology. Nonlocal self-approach is not a palinstrophy payer by geometry alone and must be attacked through flux cross-sectional geometry.

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
