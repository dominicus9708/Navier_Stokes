# M19-303 — Backward Type-I plus parabolic smoothing forces global wedge radial energy-current decay j = O(z^{-3/2})

**Date:** 2026-09-16  
**Status:** ACTIVE DYNAMIC-CORE CALCULATION / SIGNED RADIAL-CURRENT LARGE-z ENDPOINT CERTIFIED / GLOBAL REGULARITY UNPROVED

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Input: backward Type-I ancient velocity

M5-475 gives on the retained ancient branch

\[
\boxed{
\|V(s)\|_\infty\le C(-s)^{-1/2}
}
\]

for large negative time.

Write

\[
T:=-s\gg1.
\]

The goal is to estimate the full gauge-invariant whole-sphere radial local-energy current, not only its convective part.

## 2. Type-I parabolic rescaling

Around time `s=-T`, use Navier--Stokes scaling

\[
U_T(y,\tau)
:=
\sqrt T\,V(\sqrt T\,y,T\tau),
\]

with pressure

\[
P_T(y,\tau)
:=
T\,P(\sqrt T\,y,T\tau).
\]

For `tau` in any compact interval around `-1`, the backward Type-I bound gives

\[
\|U_T(\tau)\|_\infty\le C.
\]

The retained solution is smooth. Standard interior parabolic regularity for the rescaled Navier--Stokes system therefore gives, on smaller compact parabolic cylinders,

\[
\boxed{
\|\nabla_y U_T(-1)\|_\infty\le C_1,
}
\]

with a constant independent of large `T`.

Rescaling back,

\[
\boxed{
\|\nabla V(-T)\|_\infty
\le C_1T^{-1}.
}
\]

More generally the same rescaling gives the expected fixed-order local derivative rates

\[
\|\nabla^kV(-T)\|_\infty
\lesssim_k T^{-(k+1)/2}
\]

on the retained smooth Type-I branch, but only the first derivative is needed below.

## 3. Pressure gauge and local pressure oscillation

Pressure is defined up to a time-dependent additive constant. The whole-sphere pressure energy flux is gauge invariant because incompressibility gives

\[
\int_{S_r}V\cdot n\,dS=0.
\]

Hence on each sphere we may subtract any convenient spatial pressure constant.

The same unit-scale parabolic regularity used in Section 2 gives a uniform local pressure-gradient bound in rescaled variables,

\[
\|\nabla_yP_T(-1)\|_{L^\infty(B_c)}\le C_P.
\]

Therefore in original variables,

\[
\boxed{
\|\nabla P(-T)\|_{L^\infty(B_{c\sqrt T})}
\le C_PT^{-3/2}.
}
\]

For a sphere of physical radius `r` satisfying `r<<sqrt(T)`, choose for example the center value as gauge. Then

\[
\boxed{
\operatorname{osc}_{B_r}P(-T)
\le C_PrT^{-3/2}.
}
\]

Only this oscillatory part contributes to the closed-sphere pressure flux.

## 4. Convert to wedge variables

Use

\[
u=r^{-1}F(z,q,\omega),
\qquad
z=T/r^2,
\qquad
q=\log r.
\]

At fixed `q` and large `z`,

\[
T=zr^2.
\]

M5-475 gives

\[
\boxed{|F|=r|V|\lesssim z^{-1/2}.}
\]

The physical velocity gradient estimate gives

\[
|V||\nabla V|
\lesssim
T^{-1/2}T^{-1}
=T^{-3/2}.
\]

Since the normalized gradient part of the critical energy current is `r^3` times the physical energy gradient, its size is

\[
\boxed{
r^3|\nabla(|V|^2/2)|
\lesssim
r^3T^{-3/2}
=z^{-3/2}.}
\]

## 5. Convective contribution

The normalized energy is

\[
E=\frac12|F|^2=O(z^{-1}).
\]

Therefore

\[
\boxed{EF_r=O(z^{-3/2}).}
\]

## 6. Pressure contribution

The normalized pressure is `H=r^2P`, but only its oscillatory part matters on the closed sphere.

Using Section 3,

\[
r^2\operatorname{osc}_{B_r}P
\lesssim
r^3T^{-3/2}
=z^{-3/2}.
\]

Hence

\[
\boxed{H_{osc}F_r=O(z^{-2}).}
\]

This is smaller than the convective/viscous-gradient order.

Permanent gauge firewall:

\[
\boxed{
\text{no absolute }L^\infty\text{ pressure bound is needed; only closed-sphere pressure oscillation enters.}
}
\]

## 7. Global radial energy-current decay

The normalized wedge energy current has the form

\[
\mathcal J=(E+H)F-\mathfrak G_2E
\]

(up to the fixed viscosity normalization inherited by the wedge formulation).

Sections 4--6 give uniformly on the sphere

\[
|\mathcal J_r|\lesssim z^{-3/2}+z^{-2}.
\]

After sphere integration,

\[
\boxed{
|j(z,Y)|\le C z^{-3/2}
}
\]

uniformly on the retained marked hull for sufficiently large `z`.

Therefore

\[
\boxed{
\sqrt z\,j(z,Y)=O(z^{-1})\to0,
}
\]

and

\[
\boxed{
zj(z,Y)=O(z^{-1/2})\to0.
}
\]

The same bounds hold for q-invariant means and bounded production conditioning:

\[
\boxed{
\sqrt z\,\mathscr J_m(z)\to0,
\qquad
z\mathscr J_m(z)\to0.
}
\]

## 8. Integrability consequences

The current itself is depth-integrable at infinity:

\[
\boxed{
\int_1^\infty|\mathscr J_m(z)|dz<\infty.
}
\]

The derivative estimates also give normalized dissipation

\[
\mathscr D_m(z)=O(z^{-2}),
\]

while the event-boundary term, because the marker generator is bounded on the compact recurrent event construction,

\[
\mathscr B_m(z)=O(z^{-3/2}).
\]

Thus all terms in the integrated M19-300/M19-302 large-z balances are convergent.

## 9. Scope firewall

The derivative decay is not inferred from the Type-I `L-infinity` estimate by algebra alone. It uses the smooth ancient solution plus parabolic rescaling/interior smoothing on a time interval whose length is comparable to `T`.

The pressure estimate is an oscillation estimate in a gauge-invariant closed-sphere flux, not a claim that the absolute pressure has a canonical global `L-infinity` gauge.

## 10. Next consequence

M19-303 closes the large-z endpoint needed by M19-302.

The next step is to integrate the combined-potential identity

\[
(\mathscr E_m+2z\mathscr J_m)'
=
\mathscr D_m+\mathscr J_m+\mathscr B_m
\]

from `z=0` to infinity.

Since

\[
\mathscr E_m(\infty)=0,
\qquad
z\mathscr J_m(\infty)=0,
\]

this will force an exact global signed radial-current/hysteresis compensation identity.

---

\[
\boxed{\text{M19-303 COMPLETE; THE GLOBAL RADIAL ENERGY CURRENT HAS A CERTIFIED ZERO LARGE-z ENDPOINT AT RATE }O(z^{-3/2}).}
\]