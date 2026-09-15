# M19-281 — A bounded-K CE-H corridor absorbs nodal boundary-crossing index into coefficient, amplitude, or interface exits

**Date:** 2026-09-16  
**Status:** CALCULATION / SIGNED-INDEX BRANCH RETURN / CONDITIONAL BOUNDED-K CE-H CORRIDOR

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Purpose

M19-280 proves that on a closed material transverse cross-section the total algebraic winding index is boundary degree and cannot change through purely interior nodal topology turnover.

The only index-change exits retained there are boundary zero/crossing, active-set loss, or material cross-section/representation failure.

M17-283 already contains a stronger time-gate on the compact bounded-K CE-H tangent corridor. This module imports that result into the current M19 signed/index audit.

## 2. M17-283 multiplicative propagation

On the raw intrinsic heat tangent corridor,

\[
\partial_\tau V=\Delta V,
\qquad
\Delta V=K V.
\]

Therefore

\[
\boxed{\partial_\tau V=K V.}
\]

At each fixed spatial point where \(K\) remains locally bounded,

\[
\boxed{
V(x,\tau)
=V(x,\tau_0)
\exp\left(\int_{\tau_0}^{\tau}K(x,s)\,ds\right).
}
\]

Hence

\[
\boxed{
V(x,\tau_0)\neq0
\Longleftrightarrow
V(x,\tau)\neq0
}
\]

through the entire bounded-K CE-H corridor.

## 3. No nodal crossing of a controlled material boundary

Let \(\Gamma(\tau)\) be the material boundary used in M19-280. If it starts in the active set and the bounded-K CE-H representation remains valid, every material boundary label remains active.

A nodal filament cannot cross the boundary while all of the following remain true:

- bounded \(K\);
- CE-H/active-set continuation;
- nondegenerate amplitude representation;
- valid material-domain/interface representation.

Thus

\[
\boxed{
G_{nodal\ crossing\ boundary}
\Longrightarrow
G_{K\text{-}bound\ failure}
\lor
G_{CEH/active\text{-}set\ failure}
\lor
G_{nodal\ amplitude\ degeneration}
\lor
G_{domain/interface\ exit}.
}
\]

This is exactly the branch-return structure of M17-283.

## 4. Consequence for total algebraic index

M19-280 gives

\[
\mathcal I_D(\tau)
=\deg(f/|f|;\partial D(\tau)).
\]

On the bounded-K controlled corridor, the boundary remains active, so

\[
\boxed{\mathcal I_D(\tau)=\text{constant}.}
\]

Purely interior finite-jet nodal events conserve the signed sum, and boundary transfer is unavailable unless one of the explicit hard exits occurs.

Hence the ordinary winding/index route has no independent positive signed source inside the compact bounded-K CE-H corridor.

## 5. Current index-route classification

Combining M17-007, M17-009, M17-010, M17-283, M19-279, and M19-280 gives

\[
\boxed{
\begin{aligned}
\mathcal T_{aper}^{signed/index}\text{ via great-circle winding}
\Longrightarrow{}&
G_{K\text{-}bound\ failure}
\\
&\lor G_{CEH/active\text{-}set\ failure}
\\
&\lor G_{nodal\ amplitude\ degeneration}
\\
&\lor G_{domain/interface/representation}
\\
&\lor G_{winding/reuse/decompactification}.
\end{aligned}
}
\]

The first four are existing analytic/coefficient/interface exits. The final winding/reuse branch has already been reduced by M17-355--356 and M19-019 to critical packing, fragmentation, reuse, or geometry escape rather than a finite one-way signed budget.

Therefore

\[
\boxed{
\text{great-circle algebraic winding is not a standalone realization of the missing signed/index closure gate.}
}
\]

## 6. Scope firewall

M17-283 is conditional on the bounded-K CE-H tangent corridor. This module does not claim nodal membership stationarity for arbitrary Navier--Stokes fields or arbitrary caloric limits.

Outside that corridor, the explicit K-bound/CE-H/amplitude/interface failures remain genuine open branches rather than being declared impossible.

## 7. Strategic consequence

The dynamic recurrent-core frontier should no longer list **ordinary great-circle winding number** as a promising independent positive-mean payer.

The remaining high-value directions are instead:

1. a genuinely signed PDE remainder in the finite-lag production/energy block;
2. a finite-budget boundary/export defect not reducible to a conserved degree;
3. a global scattering-factor/observability rigidity theorem;
4. the independent GMS base-gain and stationary stress-tightness routes.

---

\[
\boxed{\text{M19-281 COMPLETE; BOUNDED-K CE-H WINDING-INDEX TRANSFER RETURNS TO EXISTING HARD EXITS RATHER THAN A NEW SIGNED PAYER.}}
\]
