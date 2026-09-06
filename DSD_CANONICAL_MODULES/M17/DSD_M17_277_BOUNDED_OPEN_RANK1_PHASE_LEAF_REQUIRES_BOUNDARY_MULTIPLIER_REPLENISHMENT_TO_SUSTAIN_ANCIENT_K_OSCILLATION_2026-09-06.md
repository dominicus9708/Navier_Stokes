# DSD M17-277 — A bounded open Rank-1 phase leaf requires boundary multiplier replenishment to sustain ancient K oscillation

Date: 2026-09-06  
Canonical ID: **M17-277**

Status: **OPEN-LEAF INTERFACE GATE / M17-276 CLOSES COMPACT BOUNDARYLESS RANK-1 PHASE LEAVES BY PARABOLIC OSCILLATION CONTRACTION. ON A BOUNDED LEAF WITH BOUNDARY, THE SAME SURFACE EQUATION `K_tau=Delta_S K+b_S·grad_S K` HAS AN INTERIOR OSCILLATION ESTIMATE WITH A BOUNDARY-INPUT TERM. REMOTE-PAST INTERIOR OSCILLATION DECAYS GEOMETRICALLY; TO MAINTAIN THE FIXED POSITIVE/NEGATIVE K OSCILLATION REQUIRED BY THE CRITICAL SURVIVOR, A FIXED AMOUNT OF MULTIPLIER OSCILLATION OR FLUX MUST REENTER THROUGH THE LEAF BOUNDARY ON REPEATED TIME WINDOWS. THUS A BOUNDED OPEN RANK-1 LEAF IS NOT AN INDEPENDENT PAYER-FREE SURVIVOR: IT RETURNS TO PHASE-LEAF BOUNDARY/INTERFACE REPLENISHMENT, UNLESS GEOMETRY/DRIFT/K BOUNDS FAIL. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Surface multiplier equation

On a Rank-1 phase leaf `S`, M17-276 gives

\[
\boxed{
\partial_\tau K
=\Delta_SK+b_S\cdot\nabla_SK.
}
\]

Assume `S` is connected and bounded but has nonempty boundary

\[
\partial S\ne\varnothing.
\]

Retain uniform interior geometry and

\[
\|b_S\|_\infty\le B_*,
\qquad
|K|\le K_*.
\]

---

## 2. Interior region

Fix a compact interior subleaf

\[
S'\Subset S
\]

with a fixed positive distance from the boundary.

Standard parabolic kernel/barrier estimates for a bounded uniformly regular surface domain give, over one fixed time `tau_0`,

\[
\boxed{
\operatorname{osc}_{S'}K(\tau+\tau_0)
\le
q\operatorname{osc}_{S}K(\tau)
+C\mathcal B_K([\tau,\tau+\tau_0]),
}
\]

where

\[
0<q<1
\]

and `mathcal B_K` measures boundary value/normal-flux oscillation entering through `partial S` during the window.

The exact norm used for `mathcal B_K` may be chosen according to the boundary formulation; only its vanishing versus nonvanishing role is used here.

---

## 3. Ancient iteration

Iterate from time

\[
-N\tau_0
\]

to the present.

The contribution of the remote-past interior oscillation is bounded by

\[
2K_*q^N\to0.
\]

Hence if

\[
\mathcal B_K([-(m+1)\tau_0,-m\tau_0])\to0
\]

uniformly along all sufficiently remote windows, then

\[
\boxed{
\operatorname{osc}_{S'}K(0)=0.
}
\]

This contradicts a retained interior sign-balanced multiplier carrier.

---

## 4. Boundary replenishment conclusion

Therefore a bounded open leaf carrying fixed ancient positive/negative `K` oscillation must have recurrent nontrivial boundary input:

\[
\boxed{
H_{Rank1\ bounded\ open\ leaf}
\Longrightarrow
G_{phase\text{-}leaf\ boundary/interface\ replenishment}
\lor
G_{leaf\ geometry/drift\ failure}
\lor
G_{K\text{-}spike}.
}
\]

The boundary is an actual interface of the Rank-1 phase patch; it is not counted as a free source.

---

## 5. DSD audit

- Boundaryless mixing from M17-276 is not reused without a boundary term.
- Boundary values and boundary flux are grouped only at the level of an explicit replenishment gate; no sign law is invented.
- Ancient boundedness removes remote-past initial oscillation but not recurrent boundary forcing.
- Global regularity remains unproved.

---

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
