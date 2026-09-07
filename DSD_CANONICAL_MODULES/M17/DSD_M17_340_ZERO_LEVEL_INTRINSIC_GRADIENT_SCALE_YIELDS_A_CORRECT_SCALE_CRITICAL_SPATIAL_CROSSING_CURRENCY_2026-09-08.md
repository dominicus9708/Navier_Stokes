# DSD M17-340 — Zero-level intrinsic gradient scale yields a correct scale-critical spatial crossing currency

Date: 2026-09-08  
Canonical ID: **M17-340**

Status: **ACTIVE REPRESENTATION-CORRECTED CRITICAL PHYSICALIZATION CANDIDATE**

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Corrected starting point

M17-338 salvages the zero-level directed crossing currency by the exact physical/similarity dictionary:

\[
\mathcal C_{\Phi,-}^{0}
=
\int
(h^{ph})_-\delta(\kappa^{ph})\,d\Phi\,dt
=
\int
(h^{sim})_-\delta(\kappa^{sim})\,d\Phi\,d\theta.
\]

This quantity is record-scale critical.

Ordinary spatialization multiplies the pure flux measure by a line-enstrophy residence factor and loses one scale power.  M17-337 tried to repair that loss with a positive threshold; M17-338 quarantined that route because it mixed physical and similarity coefficients.

The present module stays entirely at the homogeneous physical zero level.

## 2. Physical parabolic dimensions

Under

\[
\Omega_R(x,t)=R^2\Omega(Rx,R^2t),
\]

we have

\[
\rho_R=R^2\rho,
\qquad
\kappa_R=R^2\kappa,
\qquad
h_R=D_t\kappa_R=R^4h,
\]

and

\[
\nabla\kappa_R=R^3\nabla\kappa.
\]

Also

\[
dx_R=R^{-3}dx,
\qquad
dt_R=R^{-2}dt,
\]

and at zero

\[
\delta(\kappa_R)=R^{-2}\delta(\kappa).
\]

The intrinsic inverse-length quantity

\[
\boxed{
q_\kappa:=|\nabla\kappa|^{1/3}
}
\]

scales as

\[
q_{\kappa,R}=Rq_\kappa.
\]

## 3. Corrected spatial critical currency

On the nondegenerate zero-gradient branch, define

\[
\boxed{
\mathcal Q_0(I)
:=
\int_I\!\int
h_-\delta(\kappa)
\rho^2
|\nabla\kappa|^{-1/3}
\,dx\,dt.
}
\]

Its scaling exponent is

\[
R^4
\cdot R^{-2}
\cdot R^4
\cdot R^{-1}
\cdot R^{-3}
\cdot R^{-2}
=R^0.
\]

Therefore

\[
\boxed{
\mathcal Q_{0,R}(I_R)
=
\mathcal Q_0(I).
}
\]

This is a genuine **spatial and record-scale-critical** zero-level crossing currency.

No positive similarity threshold is used.

## 4. Vortex-line coordinate form

On exact CE-H,

\[
D_\xi\kappa=0,
\qquad
D_\xi h=0.
\]

In a regular vortex flow box,

\[
\rho^2dx=\rho\,d\Phi\,ds.
\]

Hence

\[
\boxed{
\mathcal Q_0
=
\int
h_-\delta(\kappa)
\mathcal L_{crit}(\lambda,t)
\,d\Phi\,dt,
}
\]

where

\[
\boxed{
\mathcal L_{crit}
:=
\int_{\Gamma_\lambda}
\rho|\nabla\kappa|^{-1/3}ds.
}
\]

The line factor is dimensionless:

\[
\rho\mapsto R^2\rho,
\qquad
|\nabla\kappa|^{-1/3}\mapsto R^{-1}|\nabla\kappa|^{-1/3},
\qquad
ds\mapsto R^{-1}ds.
\]

Thus

\[
\boxed{\mathcal L_{crit,R}=\mathcal L_{crit}.}
\]

This is the corrected scale-invariant line-residence bridge.

## 5. Degenerate-gradient firewall

The definition above uses

\[
|\nabla\kappa|^{-1/3}.
\]

If

\[
\nabla\kappa=0
\quad\text{on the zero crossing set},
\]

the nondegenerate formula cannot simply be imported.

Record the explicit exit

\[
\boxed{G_{degenerate\ transverse\ zero\text{-}gradient}.}
\]

Because M17-313 gives `grad kappa perp Omega`, this degeneracy concerns the transverse coefficient profile, not a hidden longitudinal derivative.

## 6. Relation to ordinary line weight and diffusion

Define the ordinary physical line-enstrophy weight

\[
L_\rho
:=
\int_\Gamma\rho\,ds,
\]

and the line multiplier-gradient charge

\[
D_{\Gamma,\kappa}
:=
\int_\Gamma
\rho|\nabla\kappa|^2ds.
\]

Using the probability measure

\[
\frac{\rho ds}{L_\rho}
\]

and convexity of `x -> x^{-1/6}`, Jensen gives

\[
\frac{\mathcal L_{crit}}{L_\rho}
=
\frac1{L_\rho}
\int\rho
\left(|\nabla\kappa|^2\right)^{-1/6}ds
\ge
\left(
\frac{D_{\Gamma,\kappa}}{L_\rho}
\right)^{-1/6}.
\]

Therefore

\[
\boxed{
\mathcal L_{crit}
\ge
L_\rho^{7/6}
D_{\Gamma,\kappa}^{-1/6}.
}
\]

This inequality is itself scale invariant.

## 7. Meaning of a small critical line residence

Suppose the zero-crossing population has a lower line-weight branch

\[
L_\rho\ge L_*>0.
\]

Then

\[
\mathcal L_{crit}\to0
\]

can occur only if

\[
D_{\Gamma,\kappa}\to\infty.
\]

Thus failure to transfer the pure-flux crossing currency into `Q_0` is not free:

\[
\boxed{
\text{vanishing critical line residence}
\Longrightarrow
\text{large transverse multiplier-gradient line charge}
}
\]

apart from the separate branch `L_rho -> 0`.

## 8. Relation to the M5-683 diffusion density

At the physical zero level, the spatial multiplier-diffusion density is

\[
A_{\kappa\kappa}^{ph}(0,t)
=
\int
\delta(\kappa)
\chi\rho^2|\nabla\kappa|^2dx.
\]

In vortex-line coordinates this is precisely the flux integral of

\[
D_{\Gamma,\kappa}
\]

over zero-level labels, up to the high-amplitude cutoff convention.

Thus the two possible failures of a positive `Q_0` lower bound are now typed as

\[
\boxed{
G_{vanishing\ line\ enstrophy\ residence}
\lor
H_{large\ zero\text{-}level\ multiplier\ diffusion}.
}
\]

This is a direct bridge to the physical constitutive law of M17-339.

## 9. What remains unproved

M17-340 establishes the correct scale-critical **form** of a spatialized zero-crossing currency.

It does not yet prove a uniform positive lower bound for `Q_0` from the M17-326 pure-flux crossing charge, because the dimensionless line factor may degenerate.

It also does not prove a finite global upper budget for `Q_0`.

Therefore

\[
\boxed{
\text{critical spatialization}
\not\Rightarrow
\text{contradiction}.
}
\]

## 10. DSD-theory role

The useful DSD heuristic is to replace a representation-dependent compensator by an intrinsic quantity with exactly the missing dimension.

At the homogeneous zero level the local transverse coefficient gradient supplies that intrinsic scale.

The proof itself is standard parabolic scaling, vortex coordinates, and Jensen's inequality.

## 11. Updated zero-current frontier

On the regular zero-gradient branch,

\[
\boxed{
H_{critical\ pure\text{-}flux\ zero\ crossing}
\Longrightarrow
H_{critical\ spatial\ zero\ crossing}
\lor
G_{vanishing\ line\ residence}
\lor
H_{large\ multiplier\text{-}gradient\ charge}.
}
\]

The next target is to quantify this trichotomy under the M17-314 high-amplitude bounded-length population and test whether the `large multiplier-gradient` branch can be charged to the already isolated M5-688/M17-196 payer ledger.

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
