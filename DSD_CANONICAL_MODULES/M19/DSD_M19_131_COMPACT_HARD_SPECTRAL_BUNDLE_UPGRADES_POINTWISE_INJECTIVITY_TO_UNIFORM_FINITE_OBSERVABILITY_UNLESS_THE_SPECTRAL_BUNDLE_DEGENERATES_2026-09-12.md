# DSD M19-131 — Compact hard spectral bundle upgrades pointwise injectivity to uniform finite observability unless the spectral bundle degenerates

Date: 2026-09-12

Status: **ACTIVE M19 CALCULATION / THE M19-130 OBSERVABILITY GAP CLOSES CONDITIONALLY UNDER A UNIFORM SPECTRAL-SEPARATION BUNDLE / POINTWISE UNIQUE-CONTINUATION INJECTIVITY PLUS COMPACTNESS GIVES A UNIFORM LOWER SINGULAR VALUE / FAILURE IS ROUTED TO SPECTRAL-BUNDLE DEGENERATION OR THE UNIQUE-CONTINUATION APPLICATION GATE / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Setup

Let `K` be the compact recurrent/periodic background corridor after all retained gauges.

For each background `U in K`, let

\[
E_h(U)
\]

be the finite-dimensional hard spectral space obtained from the quasi-compact vorticity cocycle / twisted Floquet map.

Assume a fixed spectral contour separates this hard space from the rest of the spectrum uniformly over `K`.
Then the Riesz projections

\[
P_h(U)
\]

depend continuously on `U`, and

\[
\boxed{\dim E_h(U)=m}
\]

is constant on each connected component of `K`.

This uniform spectral separation is the new explicit application gate.

---

## 2. Pointwise observation injectivity

M19-130 provides, under the retained parabolic unique-continuation gate, an observation operator

\[
\mathcal O_U:E_h(U)\to Y_{spec}
\]

such that

\[
\boxed{\mathcal O_Uv=0\Longrightarrow v=0.}
\]

For fixed `U`, finite dimensionality gives

\[
\sigma(U)
:=
\inf_{\substack{v\in E_h(U)\\\|v\|=1}}
\|\mathcal O_Uv\|_{Y_{spec}}
>0.
\]

The missing issue in M19-130 was whether `sigma(U)` can approach zero along a compact sequence of backgrounds.

---

## 3. Compact unit-sphere bundle

Define the unit hard bundle

\[
\mathbb S(E_h)
:=
\{(U,v):U\in K,\ v\in E_h(U),\ \|v\|=1\}.
\]

Because `K` is compact and `P_h(U)` varies continuously with constant finite rank, the unit-sphere bundle is compact.

Assume the observation map

\[
(U,v)\mapsto\mathcal O_Uv
\]

is continuous in the retained spectator topology.

Then

\[
F(U,v):=\|\mathcal O_Uv\|_{Y_{spec}}
\]

is a continuous strictly positive function on the compact set `S(E_h)`.

Therefore

\[
\boxed{
\inf_{(U,v)\in\mathbb S(E_h)}
\|\mathcal O_Uv\|_{Y_{spec}}
=:c_{obs}>0.
}
\]

Equivalently,

\[
\boxed{
\|v\|\le c_{obs}^{-1}\|\mathcal O_Uv\|_{Y_{spec}}
\qquad
(U\in K,\ v\in E_h(U)).
}
\]

Thus pointwise injectivity automatically upgrades to corridor-uniform quantitative observability once the hard spaces form a continuous finite-rank spectral bundle.

---

## 4. Finite observable reduction uniformly over the corridor

M19-130 selected finitely many scalar observables for each fixed background.
The selection may initially depend on `U`.

For every `U_0 in K`, finite dimensionality and injectivity allow one to choose scalar functionals

\[
\ell_{U_0,1},\ldots,\ell_{U_0,m_{U_0}}
\]

on `Y_spec` such that

\[
\mathbf O_{U_0}(U_0):E_h(U_0)\to\mathbb C^{m_{U_0}}
\]

has full column rank.

By continuity of the spectral projection and observation map, the same finite family stays full rank on a neighborhood `N(U_0)`.

Compactness of `K` gives a finite subcover

\[
K\subset\bigcup_{a=1}^N N(U_a).
\]

Stack all scalar functionals from these finitely many neighborhoods into one global finite vector observation

\[
\boxed{
\mathbf O_U:E_h(U)\to\mathbb C^M.
}
\]

This map is injective on every fiber.
Applying the compact unit-sphere argument again yields

\[
\boxed{
\sigma_{min}(\mathbf O_U)\ge c_{fin}>0
\qquad\text{uniformly for }U\in K.
}
\]

Therefore a **single finite set of spectator/scattering observables** suffices on the whole compact hard corridor.

---

## 5. What can make uniform observability fail

The compactness proof shows that failure cannot occur silently.
If there exists

\[
U_n\in K,\qquad
v_n\in E_h(U_n),\qquad
\|v_n\|=1,
\qquad
\|\mathcal O_{U_n}v_n\|\to0,
\]

then at least one retained hypothesis fails:

1. **spectral-bundle degeneration**: the chosen spectral contour is hit, the hard rank changes, or the spectral projection loses continuity;
2. **background compactness loss**: `U_n` leaves the certified compact corridor;
3. **observation continuity loss**: the finite spectator/scattering map leaves its controlled topology;
4. **unique-continuation/application failure**: a nonzero hard mode can vanish on the observation cylinder because the required regularity/pressure/coefficient gate is not certified.

Thus

\[
\boxed{
G_{obs-fail}
\Longrightarrow
G_{spectral-degeneration}
\lor
G_{compactness-loss}
\lor
G_{observation-gate-loss}
\lor
G_{UC-gate-loss}.
}
\]

---

## 6. Relation to the transverse spectral theorem

The most important failure, spectral-bundle degeneration, is not a new independent root.
A hard eigenvalue crossing the separating contour or a rank change produces a near-threshold spectral mode.

Hence the observability frontier merges with the already live transverse spectral frontier:

\[
\boxed{
\mathcal T_{obs}
\subset
\mathcal T_{transverse}
\cup
\text{application-gate certification}.
}
\]

So, under the uniform spectral-separation and unique-continuation gates, the independent `uniform observability theorem` proposed after M19-130 is no longer needed as a separate analytic theorem.

---

## 7. Consequence for the M19 hard core

On a compact bounded-period RSS/RDSS corridor with a uniformly separated finite hard spectrum,

\[
\boxed{
\text{finite-dimensional interior hard mode}
\Longleftrightarrow
\text{uniformly visible finite spectator/scattering signature}
}
\]

in the quantitative one-sided sense

\[
\boxed{
\|v\|\lesssim \|\mathbf O_Uv\|.
}
\]

This does not eliminate the hard mode.
It removes loss of observability as an independent escape mechanism.

The principal analytic obstruction is again the existence of the hard transverse mode itself.

---

## 8. New live frontier

After this reduction the major analytic menu is sharpened to

\[
\boxed{
\mathcal T_{transverse}:
E_{\perp}^{\ge0}=0
}
\]

and

\[
\boxed{
\mathcal T_{relative-periodic}:
\text{exclude the remaining finite-amplitude moderate RSS/RDSS orbit itself}.
}
\]

Uniform observability is conditional bookkeeping once the spectral bundle and UC gates are certified.

---

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
