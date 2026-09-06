# DSD M17-265 — Bounded open Rank-2 fibers require persistent boundary multiplier replenishment

Date: 2026-09-06  
Canonical ID: **M17-265**

Status: **OPEN-FIBER BOUNDARY RETURN GATE / M17-263 REDUCES THE RAW RANK-2 CE-H HEAT-TANGENT MULTIPLIER TO A ONE-DIMENSIONAL UNIFORMLY PARABOLIC EQUATION ALONG EACH NONDEGENERATE FIBER. M17-264 CLOSES THE COMPACT CLOSED-FIBER CASE BY ANCIENT OSCILLATION CONTRACTION. FOR A BOUNDED OPEN FIBER, THE SAME PARABOLIC MIXING ESTIMATE HAS ONE ADDITIONAL TERM: BOUNDARY TRACE OSCILLATION/INPUT. IF THE M17-233/234 CRITICAL SIGN-BALANCED MULTIPLIER MAINTAINS A FIXED INTERIOR OSCILLATION FOR ANCIENT TIMES, THEN THAT OSCILLATION CANNOT BE SUPPORTED ONLY BY INITIAL DATA FROM THE REMOTE PAST, BECAUSE THE INTERIOR MEMORY CONTRACTS GEOMETRICALLY. A FIXED AMOUNT OF MULTIPLIER CONTRAST MUST THEREFORE REENTER THROUGH THE FIBER ENDPOINTS ON REPEATED FINITE WINDOWS. HENCE BOUNDED OPEN FIBERS DO NOT FORM A NEW FREE SURVIVOR: THEY RETURN TO A FIBER-BOUNDARY/INTERFACE REPLENISHMENT CHANNEL, UNLESS DRIFT, AMPLITUDE, RANK, OR COEFFICIENT CONTROL FAILS. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Fiber equation and corridor

On a bounded open director fiber with arclength coordinate

\[
s\in(0,L),
\]

M17-263 gives

\[
\boxed{
\partial_\tau K
=\partial_s^2K+b_f(s,\tau)\partial_sK.
}
\]

Assume

\[
0<L_-\le L\le L_+<\infty,
\]

\[
|b_f|\le B_*<\infty,
\]

and

\[
|K|\le K_*<\infty
\]

for all ancient times on the retained active corridor.

Nodal/amplitude degeneration, drift blowup, rank loss, and coefficient spike remain explicit exits.

---

## 2. Fixed interior sign-balance gives a fixed oscillation floor

The M17-233/234 coefficient branch supplies, after fixing the non-spike threshold and the sign-balance parameters, positive constants

\[
\delta_K>0,
\qquad
\eta_K>0
\]

such that at the retained observation times the multiplier has both a positive and a negative interior population of nontrivial measure.

In particular the fiberwise/interior oscillation satisfies

\[
\boxed{
\operatorname{osc}_{I_{int}}K
\ge\delta_K
}
\]

on a fixed interior subinterval

\[
I_{int}\Subset(0,L)
\]

unless the sign-balanced population has already exited through fiber splitting/interface geometry.

The exact value of `delta_K` is irrelevant; only its fixed positivity matters.

---

## 3. Parabolic memory contraction with boundary forcing

For a scalar uniformly parabolic equation on a bounded interval with bounded drift, the solution on a fixed interior subinterval after a fixed time `tau_0>0` is represented by

1. a strictly positive interior transition kernel acting on earlier data;
2. boundary Poisson kernels acting on the endpoint traces.

Consequently there exist fixed constants

\[
0<q<1,
\qquad
C_b<\infty
\]

depending only on

\[
L_-,L_+,B_*,I_{int}
\]

such that

\[
\boxed{
\operatorname{osc}_{I_{int}}K(\tau+\tau_0)
\le
q\,\operatorname{osc}_{(0,L)}K(\tau)
+C_b\,\mathcal B_K([\tau,\tau+\tau_0]),
}
\]

where `mathcal B_K` measures the oscillation of the two endpoint traces over that time window, for example

\[
\boxed{
\mathcal B_K(I)
:=
\operatorname{osc}
\left\{
K(0,t),K(L,t):t\in I
\right\}.
}
\]

Any equivalent boundary-input norm can be used in later quantitative bookkeeping.

---

## 4. Remote-past initial data cannot sustain fixed present oscillation

Iterate the estimate over `N` consecutive backward windows.

Using

\[
\operatorname{osc}K\le2K_*,
\]

we obtain schematically

\[
\operatorname{osc}_{I_{int}}K(0)
\le
2K_*q^N
+C_b\sum_{m=0}^{N-1}q^m
\mathcal B_{K,m},
\]

where `mathcal B_{K,m}` is the boundary-input size on the corresponding past window.

Let `N->infinity`.

If all boundary-input windows satisfied

\[
\mathcal B_{K,m}\le\varepsilon,
\]

then

\[
\operatorname{osc}_{I_{int}}K(0)
\le
\frac{C_b}{1-q}\varepsilon.
\]

Choose

\[
\varepsilon
<\frac{(1-q)\delta_K}{2C_b}.
\]

This contradicts the fixed interior oscillation floor

\[
\operatorname{osc}_{I_{int}}K(0)\ge\delta_K.
\]

Therefore

\[
\boxed{
\text{fixed ancient interior sign balance}
\Longrightarrow
\text{recurrent fixed-size fiber-boundary multiplier input}.
}
\]

---

## 5. Interpretation as interface/replenishment

The endpoints of an open director fiber are not fictitious boundaries introduced by a cutoff.

They indicate at least one of the following:

1. the retained Rank-2 active patch ends;
2. the fiber meets a nodal/amplitude-degenerate set;
3. the fiber enters another component or packet;
4. the compact director chart ceases to be valid;
5. material/coefficient data enter from outside the retained fiber segment.

Thus a fixed boundary trace oscillation is canonically a

\[
\boxed{
G_{fiber\ boundary/interface\ replenishment}
}
\]

rather than a free internal multiplier source.

---

## 6. No-flux or periodic endpoint conditions reduce to M17-264

If the two endpoints are identified periodically, the fiber is closed and M17-264 applies.

If an actual boundary condition eliminates multiplier contrast input, such as a homogeneous no-flux condition compatible with the fiber equation, the boundary term in Section 3 vanishes and the same ancient oscillation contraction forces spatial constancy.

Thus the only bounded-open-fiber survivor is genuine boundary/interface replenishment.

---

## 7. Updated fiber split

Combining M17-264 and M17-265,

\[
\boxed{
G_{bounded\ Rank2\ fiber}
\Longrightarrow
\bot
\lor
G_{fiber\ boundary/interface\ replenishment}
\lor
G_{nodal/amplitude\ degeneration}
\lor
G_{drift/geometry\ blowup}
\lor
G_{rank\ loss}
\lor
G_{K\text{-}spike}.
}
\]

The symbol `bot` denotes the closed/no-input compact-fiber contradiction.

Therefore bounded fiber topology itself is no longer an independent hard endpoint.

---

## 8. What remains genuinely new

The fiber geometry not covered by M17-264/265 is principally

\[
\boxed{
G_{fiber\ length\ decompactification}.
}
\]

On very long or noncompact fibers, a bounded drift-diffusion equation can support spatially varying bounded profiles without a finite-endpoint source, so no compact oscillation contraction is asserted there.

This is the next director-fiber target.

---

## 9. DSD audit

1. The boundary estimate is used only on a bounded open interval.
2. Boundary trace variation is not identified with physical energy cost yet; it is an interface/replenishment certificate.
3. The fiber endpoints must correspond to actual active-chart/interface exits, not arbitrary artificial cutoffs, before physical interpretation is attached.
4. Fixed sign-balanced interior oscillation is imported from the critical coefficient branch.
5. No claim is made for unbounded fibers.
6. Global regularity remains unproved.

---

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
