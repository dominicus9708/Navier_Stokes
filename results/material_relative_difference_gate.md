# Material-frame relative-difference gate

Status: **DERIVED MATERIAL-FRAME DIFFERENCE BRIDGE + EXACT CHECK**

Checks passed: **8/8**

## Geometry separation

- For the trace-free local model `S=diag(-M,0,M)`, `lambda_2^+=0` but `||F^{-T}||=exp(M t)`.
- Therefore the middle-eigenvalue danger channel does not by itself control material-boundary compression/amplification.
- Keep a separate compression channel `chi=-lambda_1` (or an equivalent full-strain channel).

## Material-frame difference channel

For the tracked material cell, define

`V(b,t)=u(Phi_t(b),t)-u(Phi_t(a),t)`.

This removes uniform translation of the whole cell. Since each label follows the flow,

`dot V = -delta(grad p) + nu delta(Delta u)`.

Thus a pressure gradient that is spatially identical across the small tracked cell also cancels; only pressure-gradient **differences** remain.

Define

`C_rel=ell^(-1) int_{B_ell(a)} |V|^2 db`,

`P_rel=ell int V.delta(grad p) db`,

`V_rel=nu ell int V.delta(Delta u) db`.

Then

`ell^2 d_t C_rel = -2 P_rel + 2 V_rel`.

`C_rel`, `P_rel`, and `V_rel` are invariant under the Navier--Stokes parabolic scaling when the material label and `ell` are scaled together.

## Smooth small-scale expansion

At a smooth point,

`C_rel = (4 pi / 15) ell^4 ||(grad u)F||_F^2 + o(ell^4)`.

Therefore `C_rel -> 0` as `ell -> 0` at smooth points. The normalization remains compatible with critical concentration scaling, but this is not yet a regularity criterion.

## Correction to the previous boundary-geometry emphasis

`F^{-T}` appears explicitly in the pulled-back surface form of pressure and viscous work. However, the same material-cell energy balance can be written as a fixed-reference-ball volume integral using `J=1`, where the explicit `F^{-T}` factor disappears. Geometry is therefore a diagnostic/coupling variable, not an independent new energy source.

## Claim boundary

Exact kinematic, algebraic, and scaling bridge only. No arbitrary-data a-priori bound, blow-up exclusion, or global regularity theorem is claimed.
