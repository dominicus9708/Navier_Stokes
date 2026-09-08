# DSD M17-431 — Record-cubic amplitude contrast yields only a logarithmic certified strain-gradient payer and returns to the inverse-record palinstrophy firewall

Date: 2026-09-08  
Canonical ID: **M17-431**

Status: **ACTIVE AMPLITUDE-CONTRAST TO STRAIN-GRADIENT AUDIT / PALINSTROPHY NO-GO AT DIRECT LINE-ESTIMATE LEVEL**

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Input from M17-430

On a fixed material CE-H loop, retaining the M17-188 mean covariance `3/4` through an inverse similarity record ratio `R` forces

\[
\boxed{
\mathfrak D_\rho\gtrsim R^3,
}
\]

where

\[
\mathfrak D_\rho
=
\frac{L_\rho J_\rho}{\ell^2}
\le
\frac{M_\rho}{m_\rho}.
\]

Hence the longitudinal amplitude condition number must grow at least cubically.

The present question is whether this cubic contrast automatically upgrades the branch to the more favorable M17-307 inverse-record palinstrophy contradiction.

The direct line estimate does not do so.

## 2. Relative material amplitude is driven only by strain contrast

For exact CE-H similarity vorticity,

\[
D_B\log\rho
=
\sigma+\kappa-1.
\]

M17-313 gives

\[
D_\xi\kappa=0,
\]

so `kappa` is constant along each connected regular vortex loop at each time.

Let `a` and `b` be two material points on the same material loop. Then

\[
\boxed{
\frac d{d\theta}
\log\frac{\rho(a,\theta)}{\rho(b,\theta)}
=
\sigma(a,\theta)-\sigma(b,\theta).
}
\]

Thus coefficient diffusion and the universal similarity decay cancel from relative amplitude evolution.

## 3. Oscillation inequality

Define

\[
A_\rho(\theta)
:=
\operatorname{osc}_{\Gamma(\theta)}\log\rho.
\]

Material transport of the loop gives

\[
\boxed{
A_\rho(\theta_1)
\le
A_\rho(\theta_0)
+
\int_{\theta_0}^{\theta_1}
\operatorname{osc}_{\Gamma(\theta)}\sigma\,d\theta.
}
\]

Since

\[
\mathfrak D_\rho
\le
\frac{M_\rho}{m_\rho}
=
e^{A_\rho},
\]

M17-430 implies, modulo the fixed initial contrast,

\[
\boxed{
\int_{\theta_0}^{\theta_1}
\operatorname{osc}_\Gamma\sigma\,d\theta
\gtrsim
3\log R-C_0.
}
\]

## 4. Direct conversion to tangential strain gradient

At each time,

\[
\operatorname{osc}_\Gamma\sigma
\le
\oint_\Gamma|\partial_s\sigma|ds
\le
\ell(\theta)^{1/2}
\|\partial_s\sigma\|_{L^2(ds)}.
\]

Hence in general

\[
\boxed{
\int_{\theta_0}^{\theta_1}
\|\partial_s\sigma\|_2^2d\theta
\ge
\frac{
\left(3\log R-C_0\right)^2
}{
\int_{\theta_0}^{\theta_1}\ell(\theta)d\theta
}.
}
\]

This is the representation-safe direct line estimate.

If one assumes the most favorable bounded-length subbranch

\[
\ell(\theta)\le\ell^*,
\]

and uses

\[
\Delta\theta=2\log R,
\]

then

\[
\boxed{
\int_{\theta_0}^{\theta_1}
\|\partial_s\sigma\|_2^2d\theta
\gtrsim
c\log R.
}
\]

If the loop length itself decompactifies, the denominator only becomes larger and this direct estimate weakens.

## 5. Relation to palinstrophy

On exact CE-H,

\[
|\nabla\sigma|
\le
|\nabla\Sigma|,
\]

and globally for divergence-free velocity

\[
\|\nabla\Sigma\|_2^2
=
\frac12\|\nabla W\|_2^2.
\]

As in M17-361, a positive-flux family carrying the line-gradient lower bound uniformly can therefore be converted to a normalized global palinstrophy payer.

Even granting this favorable family conversion with no additional loss, the directly certified record dependence is only

\[
\boxed{
P_R^{norm}\gtrsim c\log R.
}
\]

No record-linear factor is obtained from amplitude contrast alone.

## 6. Cross-generation audit

M17-307 gives the first-generation ancestral palinstrophy currency

\[
\boxed{
\sum_mR_m^{-1}
\int_I\|\nabla\Omega_m\|_2^2ds
<\infty.
}
\]

A descendant lower bound of order `log R_m` therefore contributes only

\[
\boxed{
R_m^{-1}\log R_m.
}
\]

For geometric record scales,

\[
\sum_mR_m^{-1}\log R_m<\infty.
\]

Thus

\[
\boxed{
\text{record-cubic amplitude contrast}
\not\Rightarrow
\text{palinstrophy contradiction}
}
\]

through the direct one-loop oscillation/Poincare route.

## 7. What would be sufficient

To defeat the M17-307 firewall after M17-431, one still needs at least one genuinely stronger mechanism, for example:

\[
\boxed{
N_m^{ind}\gtrsim \frac{R_m}{\log R_m}
}
\]

independent positive-flux contrast packets of the above strength at record `m`, or a stronger per-packet gradient payer of record-linear order, or a nonsummable residence enhancement after representation-safe parent-to-record mapping.

This is a threshold statement, not a claim that such enhancement is impossible.

## 8. Updated branch

The fixed-material-tube decompactification line is now

\[
\boxed{
\begin{aligned}
H_{3/4\ covariance}
&\Longrightarrow
G_{R^3\ amplitude\ contrast}\\
&\Longrightarrow
G_{\log R\ direct\ strain\text{-}gradient\ occupancy}\\
&\Longrightarrow
G_{R^{-1}\log R\ ancestral\ firewall},
\end{aligned}
}
\]

unless multiplicity, residence, amplitude, nodal, interface, or genealogy structure supplies an additional nonsummable enhancement.

## 9. DSD role

DSD is used only to audit whether an apparently cubic geometric/amplitude defect really becomes a cubic PDE resource.

It does not: the direct standard estimate converts cubic contrast in amplitude ratio into logarithmic accumulated strain-gradient occupancy.

## 10. Audit verdict

**PASS as a no-go/threshold module.**

The direct attempt to use M17-430 to bypass the cubic raw-`H2` firewall through M17-307 palinstrophy still falls short on geometric records.

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
