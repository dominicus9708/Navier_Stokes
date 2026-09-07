# DSD M17-344 — Fast material zero crossings thicken multiplier-diffusion density in `kappa` without a spatial regular-level hypothesis

Date: 2026-09-08  
Canonical ID: **M17-344**

Status: **ACTIVE MATERIAL-TIME THICKENING / STRONGER ALTERNATIVE TO THE SPATIAL REGULAR-TUBE SUBBRANCH OF M17-343**

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Why a second thickening mechanism is needed

M17-343 closes the `k`-thickness gate if the spatial zero level has a uniform tube with

\[
|\nabla\kappa|\ge g_*>0.
\]

But a material crossing of `kappa=0` may remain transverse in **time** even when the spatial gradient is small.

The exact material velocity is

\[
h:=D_B\kappa.
\]

The present module uses this time transversality to thicken the M17-342 zero-level diffusion density.

## 2. Large-gradient crossing input

Let the large-gradient crossing activity be

\[
\mathcal C_{grad}([0,T])
=
\int_{E_{grad}}h_-\delta(\kappa)d\Phi d\theta,
\]

with

\[
D_{\Gamma,\kappa}
:=
\int_\Gamma\rho|\nabla\kappa|^2ds
\ge d_*>0
\]

on `E_grad`.

Assume M17-342's positive-density branch:

\[
\boxed{
\liminf_{T\to\infty}\frac{\mathcal C_{grad}([0,T])}{T}
\ge c_g>0.
}
\]

## 3. Finite zero-trace mass versus fast crossings

Define the unweighted zero-trace measure on the same large-gradient population by

\[
\boxed{
Z_{grad}([0,T])
:=
\int_{E_{grad}}\delta(\kappa)d\Phi d\theta.
}
\]

Assume first

\[
\boxed{
\limsup_{T\to\infty}\frac{Z_{grad}([0,T])}{T}
\le M_Z<\infty.
}
\]

If this fails, retain the already typed exit

\[
G_{zero\text{-}level\ trace\ concentration}.
\]

Choose

\[
\boxed{
\eta:=\frac{c_g}{4M_Z}>0.
}
\]

The crossing activity from events with

\[
0<h_-<\eta
\]

is at most

\[
\eta Z_{grad}([0,T])
\le\frac{c_g}{4}T+o(T).
\]

Hence the fast-crossing activity

\[
\mathcal C_{fast}
:=
\int_{E_{grad}\cap\{h_-\ge\eta\}}
h_-\delta(\kappa)d\Phi d\theta
\]

satisfies

\[
\boxed{
\liminf_{T\to\infty}\frac{\mathcal C_{fast}([0,T])}{T}
\ge\frac{3c_g}{4}>0.
}
\]

On simple crossings, `h_- delta(kappa) dtheta` counts one downward passage, so `C_fast` is the material-flux-weighted fast crossing count.

## 4. Compact material-jet ceilings

On the compact all-order same-generation CE-H hull, assume the retained same-material line segment satisfies

\[
\boxed{
|h|\le H_*,
\qquad
|D_Bh|\le J_*,
\qquad
|D_BD_{\Gamma,\kappa}|\le K_*.
}
\]

The first bound is already used in M17-342.

The latter two follow on the compact bounded-line/reuse subbranch from the all-order field bounds plus a fixed material-segment representation. Failure is recorded as

\[
G_{material\ jet/genealogy/decompactification}.
\]

## 5. One fast crossing generates a fixed kappa corridor

Take one downward crossing time `theta_0` satisfying

\[
\kappa(\theta_0)=0,
\qquad
h(\theta_0)\le-\eta,
\qquad
D_{\Gamma,\kappa}(\theta_0)\ge d_*.
\]

Choose

\[
\boxed{
\tau_*
:=
\min\left\{
\frac{\eta}{4J_*},
\frac{d_*}{4K_*},
1
\right\}>0,
}
\]

with the obvious interpretation if one derivative ceiling vanishes.

Then for

\[
|\theta-\theta_0|\le\tau_*,
\]

we have

\[
\boxed{
h(\theta)\le-\frac{3\eta}{4}<0,}
\]

and

\[
\boxed{
D_{\Gamma,\kappa}(\theta)\ge\frac{3d_*}{4}.
}
\]

Thus `kappa(theta)` is strictly decreasing throughout the window.

Define

\[
\boxed{
\delta_*:=\frac{3\eta\tau_*}{4}>0.
}
\]

Then the material trajectory crosses every level

\[
|k|\le\delta_*
\]

inside the window.

## 6. Flux weight is comparable across the short crossing window

The material flux law is

\[
D_B\log d\Phi=\kappa.
\]

Since `kappa(theta_0)=0` and `|h|<=H_*`,

\[
|\kappa(\theta)|\le H_*\tau_*
\]

inside the window.

Therefore

\[
\boxed{
 e^{-H_*\tau_*^2}
\le
\frac{d\Phi(\theta)}{d\Phi(\theta_0)}
\le
e^{H_*\tau_*^2}.
}
\]

Set

\[
c_\Phi:=e^{-H_*\tau_*^2}>0.
\]

## 7. Eventwise lower contribution to the k-level diffusion density

For fixed `|k|<=delta_*`, let `theta_k` be the unique crossing time in the window with

\[
\kappa(\theta_k)=k.
\]

The time coarea identity gives for that label

\[
\int
\delta(k-\kappa(\theta))D_{\Gamma,\kappa}(\theta)d\Phi(\theta)d\theta
=
\frac{D_{\Gamma,\kappa}(\theta_k)d\Phi(\theta_k)}{|h(\theta_k)|}.
\]

Using

\[
D_{\Gamma,\kappa}\ge\frac{3d_*}{4},
\qquad
|h|\le H_*,
\qquad
 d\Phi(\theta_k)\ge c_\Phi d\Phi(\theta_0),
\]

we obtain

\[
\boxed{
\text{contribution at level }k
\ge
c_{evt}\,d\Phi(\theta_0),
}
\]

where

\[
\boxed{
c_{evt}:=\frac{3d_*c_\Phi}{4H_*}>0.}
\]

## 8. Crossing-window overlap audit

Two distinct downward fast crossings of the same material label cannot occur with arbitrarily close centers under the `|D_Bh|<=J_*` ceiling: after one downward crossing the label must return to positive `kappa` before another downward crossing, requiring a sign reversal of `h` and hence a definite material-time separation.

Equivalently, the radius-`tau_*` crossing windows have a uniform finite overlap number

\[
\boxed{N_{ov}<\infty.}
\]

If a fixed-label representation is lost before this statement can be made, retain the genealogy/replacement exit.

Thus summing eventwise lower bounds loses only the fixed factor `N_ov`.

## 9. Uniform corridor lower mean

For every

\[
|k|\le\delta_*,
\]

we obtain

\[
\int_0^T A_{\kappa\kappa}(k,\theta)d\theta
\ge
\frac{c_{evt}}{N_{ov}}
\mathcal C_{fast}([0,T])-O(1).
\]

Therefore

\[
\boxed{
\inf_{|k|\le\delta_*}
\liminf_{T\to\infty}
\frac1T\int_0^T
A_{\kappa\kappa}(k,\theta)d\theta
\ge
\frac{3c_gc_{evt}}{4N_{ov}}>0.
}
\]

This is stronger than a one-level lower bound: a whole fixed `kappa` corridor has positive recurrent multiplier-diffusion density.

## 10. Direct M5-688 consequence

Integrating over `|k|<=delta_*`,

\[
\boxed{
\liminf_{T\to\infty}\frac1T
\int_0^T\int_{-\delta_*}^{\delta_*}
e^{2k}A_{\kappa\kappa}(k,\theta)dkd\theta
\ge c_{diff}>0
}
\]

for an explicit constant `c_diff` depending only on the retained compact-branch constants.

Hence the large-gradient / finite-trace / compact-material-jet branch enters the M5-688 diffusion ledger **without any spatial lower bound on `|grad kappa|` in a full zero-level tube**.

## 11. Updated exits

The remaining alternatives are

\[
\boxed{
G_{zero\text{-}level\ trace\ concentration}
\lor
G_{material\ jet/genealogy\ decompactification}
\lor
G_{low\ line\ residence}
\lor
H_{critical\ spatial\ crossing}
\lor
H_{M5\text{-}688\ diffusion\ payer}.
}
\]

M17-343 remains valid and useful, but M17-344 closes a larger subbranch by using material-time transversality instead of spatial regularity.

## 12. DSD-theory role

The retained DSD heuristic is the separation of spatial and temporal transition channels.  Once that distinction is made, the calculation is ordinary one-dimensional material coarea, compactness, and bounded-overlap counting.

No DSD axiom enters the PDE.

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
