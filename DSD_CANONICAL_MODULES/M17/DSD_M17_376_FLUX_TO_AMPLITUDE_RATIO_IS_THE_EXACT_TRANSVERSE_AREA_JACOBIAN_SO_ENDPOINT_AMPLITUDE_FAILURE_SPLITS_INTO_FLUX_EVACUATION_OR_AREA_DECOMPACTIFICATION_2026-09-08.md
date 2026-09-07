# DSD M17-376 — Flux-to-amplitude ratio is the exact transverse-area Jacobian, so endpoint amplitude failure splits into flux evacuation or area decompactification

Date: 2026-09-08  
Canonical ID: **M17-376**

Status: **ACTIVE AMPLITUDE/FLUX/GEOMETRY SEPARATION IDENTITY**

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Same material tube label

Work in one fixed similarity representation on a regular CE-H material tube label.

Let

\[
\rho=|W|>0
\]

be the similarity vorticity amplitude on the retained carrier and let `dPhi` be the corresponding positively oriented infinitesimal material vorticity flux.

The exact material laws are

\[
\boxed{
D_B\log\rho
=\sigma+\kappa-1,
}
\]

and

\[
\boxed{
D_B\log d\Phi=\kappa.
}
\]

## 2. Exact cancellation of kappa

Subtracting the two equations gives

\[
\boxed{
D_B\log\frac{d\Phi}{\rho}
=1-\sigma.
}
\]

For an infinitesimal flux tube transverse to the vorticity direction,

\[
d\Phi=\rho\,dA_\perp,
\]

so

\[
\boxed{
\frac{d\Phi}{\rho}=dA_\perp.
}
\]

Hence the preceding law is exactly the transverse material-area law

\[
\boxed{
D_B\log dA_\perp=1-\sigma.
}
\]

This is also consistent with

\[
\nabla\cdot B=\frac32
\]

and longitudinal line stretching rate

\[
D_B\log ds=\sigma+\frac12,
\]

because

\[
\frac32-\left(\sigma+\frac12\right)=1-\sigma.
\]

## 3. Endpoint ratio identity

On a material interval `I=[theta_-,theta_+]`, define

\[
R_\Phi:=\frac{d\Phi_+}{d\Phi_-},
\qquad
R_\rho:=\frac{\rho_+}{\rho_-},
\qquad
R_A:=\frac{dA_{\perp,+}}{dA_{\perp,-}}.
\]

Then exactly

\[
\boxed{
R_A=\frac{R_\Phi}{R_\rho}.
}
\]

Equivalently,

\[
\boxed{
\log R_A
=\int_I(1-\sigma)d\theta.
}
\]

Thus amplitude endpoint exposure and flux endpoint exposure differ only by the transverse-area deformation.

## 4. Collapse trichotomy

Suppose the amplitude endpoint ratio collapses:

\[
R_\rho\to0.
\]

There are three quantitative possibilities.

### A. Flux and amplitude collapse comparably

If

\[
c\le\frac{R_\Phi}{R_\rho}\le C,
\]

then

\[
R_A\asymp1.
\]

The amplitude collapse is not an independent new mechanism: it is the same order as the material-flux evacuation.

### B. Amplitude collapses faster than flux

If

\[
\frac{R_\rho}{R_\Phi}\to0,
\]

then

\[
\boxed{R_A\to\infty.}
\]

The tube must undergo transverse-area expansion/decompactification.

### C. Flux collapses faster than amplitude

If

\[
\frac{R_\Phi}{R_\rho}\to0,
\]

then

\[
\boxed{R_A\to0.}
\]

The material transverse area collapses, which is a geometric/rank/interface degeneration rather than a silent amplitude effect.

Thus

\[
\boxed{
G_{amplitude\ endpoint\ collapse}
\Longrightarrow
H_{comparable\ flux\ evacuation}
\lor G_{transverse\ area\ expansion}
\lor G_{transverse\ area\ collapse}.
}
\]

## 5. Growth case

If instead

\[
R_\rho\to\infty,
\]

then the same identity gives

\[
R_A=R_\Phi/R_\rho.
\]

Unless the material flux grows comparably, the transverse area must collapse. If both amplitude and flux grow comparably, the branch is a genuine amplitude/flux growth branch rather than a bounded remote skeleton.

Therefore large endpoint amplitude growth is likewise not an independent untyped exit.

## 6. Consequence for M17-375

M17-375 proved that secular evacuation forces a macroscopic incoming flux fraction into one M17-134 endpoint-failure channel.

For the amplitude-failure channel `B_rho`, the present identity sharpens that channel to

\[
\boxed{
B_\rho
\Longrightarrow
H_{flux\ evacuation}
\lor G_{transverse\ area\ decompactification/collapse}
\lor G_{amplitude/flux\ growth}.
}
\]

Hence a macroscopic positive-flux amplitude failure cannot remain a purely scalar endpoint anomaly.

## 7. Relation to DSD theory

The useful heuristic is channel decomposition: `amplitude`, `flux`, and `geometry` should not be counted as independent when an exact multiplicative identity links them. The actual result is the standard material tube Jacobian identity.

## 8. Audit verdict

**PASS.**

The exact invariant relation is

\[
\boxed{
\frac{d\Phi}{\rho}=dA_\perp,
\qquad
D_B\log dA_\perp=1-\sigma.
}
\]

It removes amplitude endpoint failure as an independent unexplained exit on a regular material tube.

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]