# DSD M17-452 — The flux-arclength probability has mean normalized amplitude `O(R^-1)` and identifies the diffuse-flux baseline

Date: 2026-09-09  
Canonical ID: **M17-452**

Status: **ACTIVE DIFFUSE-FLUX BASELINE THEOREM / M17-450--451 PROBABILITY FORM**

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Setup

Use the M17-450 retained parent-length positive-flux tube on a fixed normalized record-time window.

\[
\ell_R\ge c_\ell R,
\qquad
\Phi_R\ge\Phi_*>0,
\qquad
E_{tube,R}\le E_I.
\]

Let `rho_R=|Omega_R|` in coherent tube coordinates `(z,A_z)`.

## 2. Canonical flux-arclength probability

Because the positive flux through every coherent cross-section equals `Phi_R`,

\[
\int_{\Gamma_R}\int_{A_z}\rho_R\,dA\,dz
=
\ell_R\Phi_R.
\]

Define

\[
\boxed{
d\mu_R
:=
\frac{\rho_R\,dA\,dz}{\ell_R\Phi_R}.
}
\]

Then

\[
\mu_R(\mathcal T_R)=1.
\]

This measure samples the tube according to positive vorticity flux and arclength simultaneously.

## 3. Mean normalized amplitude

The expectation of `rho_R` under `mu_R` is

\[
\begin{aligned}
\mathbb E_{\mu_R}[\rho_R]
&=
\frac1{\ell_R\Phi_R}
\int_{\mathcal T_R}\rho_R^2dx\\
&=
\frac{E_{tube,R}}{\ell_R\Phi_R}.
\end{aligned}
\]

Therefore

\[
\boxed{
\mathbb E_{\mu_R}[\rho_R]
\le
\frac{C E_I}{\Phi_*R}.
}
\]

Thus the natural flux-weighted amplitude scale on a parent-length positive-flux tube is at most `O(R^-1)`.

## 4. Quantile estimate

For every `L>0`, Markov's inequality gives

\[
\mu_R\!\left(
\rho_R\ge\frac{L}{R}
\right)
\le
\frac{R}{L}
\mathbb E_{\mu_R}[\rho_R].
\]

Hence

\[
\boxed{
\mu_R\!\left(
\rho_R\ge\frac{L}{R}
\right)
\le
\frac{C}{L}.
}
\]

Equivalently, for every fixed quantile level `0<delta<1`, there exists `C_delta` independent of `R` such that at least `1-delta` of the flux-arclength probability lies in

\[
\boxed{
\rho_R\le \frac{C_\delta}{R}.
}
\]

## 5. Relation to M17-451

M17-451 fixed an amplitude threshold `a>0` and proved that its positive-flux arclength participation is `O(R^-1)` in average.

M17-452 is stronger in scaling form: it shows that the threshold carrying order-one flux-arclength probability itself moves down to the record-dependent level

\[
\boxed{
a_R\asymp R^{-1}.}
\]

Thus fixed-threshold high-amplitude loss is not merely qualitative; the whole retained flux population has a canonical diffuse-amplitude baseline.

## 6. Area consistency

If a cross-section carries flux `Phi_*` at typical normalized amplitude `rho ~ R^-1`, then its required normalized area is naturally

\[
\mathfrak A\sim R.
\]

This agrees exactly with M17-450:

\[
\mathfrak A_{H,R}\gtrsim cR.
\]

Hence the pair

\[
\boxed{
\rho_{flux}\sim R^{-1},
\qquad
\mathfrak A\sim R
}
\]

is the minimal enstrophy-compatible diffuse-flux scaling for a parent-length positive-flux loop.

## 7. Mesoscopic transverse scale

The associated transverse participation radius is

\[
\Lambda_\perp\sim \mathfrak A^{1/2}\sim R^{1/2}
\]

in own-scale units.

Thus the minimal survivor is not an own-scale compact tube. It is already mesoscopic:

\[
\boxed{
1\ll \Lambda_\perp\sim R^{1/2}\ll R.
}
\]

If the shrinking physical own scale is `r=R^-1`, this corresponds formally to transverse physical scale

\[
\ell_\perp\sim rR^{1/2}=R^{-1/2},
\]

intermediate between the own scale `R^-1` and parent scale `1`.

## 8. Updated survivor interpretation

The late-loop amplitude branch should therefore be read as

\[
\boxed{
G_{diffuse\ positive\ flux\ on\ a\ mesoscopic\ transverse\ scale}
}
\]

rather than as an unexplained arbitrary loss of amplitude.

Further survival can still use:

1. area growth beyond the baseline `A ~ R`;
2. scale-free shape/spectral degeneration;
3. coefficient-action redistribution inside the diffuse population;
4. time occupation thinning;
5. scale-map/chart/topology/genealogy loss.

## 9. Audit verdict

**PASS — the retained parent-length positive-flux branch has a canonical diffuse-flux baseline.**

Bounded record enstrophy forces flux-arclength mean amplitude `O(R^-1)` and transverse area/radius scales `R` / `R^{1/2}` respectively.

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
