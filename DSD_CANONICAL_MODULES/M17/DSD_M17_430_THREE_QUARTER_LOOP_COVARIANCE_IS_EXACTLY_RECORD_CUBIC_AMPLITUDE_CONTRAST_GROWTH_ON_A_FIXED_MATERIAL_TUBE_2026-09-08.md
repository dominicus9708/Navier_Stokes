# DSD M17-430 — Three-quarter loop covariance is exactly record-cubic amplitude-contrast growth on a fixed material tube

Date: 2026-09-08  
Canonical ID: **M17-430**

Status: **ACTIVE AMPLITUDE-CONTRAST / RECORD-SCALE CONVERSION / M17-429 CONSEQUENCE**

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Input from M17-429

For a fixed coherent positive-volume material CE-H tube around a closed regular vortex loop, M17-429 defines

\[
\mathfrak D_\rho
=
\frac{L_\rho J_\rho}{\ell^2}
\ge1,
\]

where

\[
L_\rho=\oint\rho ds,
\qquad
J_\rho=\oint\rho^{-1}ds,
\qquad
\ell=\oint ds.
\]

It proves the exact identity

\[
\boxed{
2(\bar\sigma_\rho-\bar\sigma_{ds})
=
\frac d{d\theta}\log\mathfrak D_\rho.
}
\]

Thus the recurrent covariance is precisely the growth rate of longitudinal amplitude inhomogeneity once the universal material-volume dilation is removed.

## 2. Integrated contrast law

Integrating over `[theta_0,theta_1]`,

\[
\boxed{
\log\frac{\mathfrak D_\rho(\theta_1)}
{\mathfrak D_\rho(\theta_0)}
=
2\int_{\theta_0}^{\theta_1}
(\bar\sigma_\rho-\bar\sigma_{ds})d\theta.
}
\]

If the interval-average covariance is

\[
\frac1{\Delta\theta}
\int_{\theta_0}^{\theta_1}
(\bar\sigma_\rho-\bar\sigma_{ds})d\theta
\ge c>0,
\]

then

\[
\boxed{
\frac{\mathfrak D_\rho(\theta_1)}
{\mathfrak D_\rho(\theta_0)}
\ge e^{2c\Delta\theta}.
}
\]

## 3. Record-scale form

Define the inverse similarity scale ratio

\[
\boxed{
\mathcal R
:=e^{\Delta\theta/2}.
}
\]

Then

\[
e^{2c\Delta\theta}=\mathcal R^{4c},
\]

so

\[
\boxed{
\mathfrak D_\rho(\theta_1)
\ge
\mathfrak D_\rho(\theta_0)\mathcal R^{4c}.
}
\]

For the M17-188 recurrent value

\[
c=\frac34,
\]

this becomes

\[
\boxed{
\mathfrak D_\rho(\theta_1)
\gtrsim
\mathcal R^3.
}
\]

Therefore the numerical `3/4` in M17-188 is not accidental: after conversion from similarity time to inverse record scale, it becomes the ambient three-dimensional cubic exponent.

## 4. Amplitude condition number must also grow cubically

If

\[
0<m_\rho(\theta)
\le\rho(\cdot,\theta)
\le M_\rho(\theta),
\]

M17-429 gives

\[
1\le\mathfrak D_\rho
\le\frac{M_\rho}{m_\rho}.
\]

Hence a retained `3/4` covariance implies

\[
\boxed{
\frac{M_\rho(\theta_1)}{m_\rho(\theta_1)}
\gtrsim
\mathcal R^3.
}
\]

Thus at least one amplitude side must decompactify.

If a normalized amplitude ceiling remains bounded,

\[
M_\rho\le M_*<\infty,
\]

then

\[
\boxed{
m_\rho(\theta_1)\lesssim M_*\mathcal R^{-3}.}
\]

The loop approaches the nodal/amplitude boundary at least at record-cubic contrast rate.

If instead a positive amplitude floor remains,

\[
m_\rho\ge m_*>0,
\]

then

\[
\boxed{M_\rho(\theta_1)\gtrsim m_*\mathcal R^3,}
\]

which is amplitude blow-up/decompactification and leaves the retained compact-amplitude branch.

## 5. Compact amplitude retention closes the fixed-tube recurrent covariance immediately

If both

\[
0<m_*\le\rho\le M_*<\infty
\]

hold on the same fixed positive-volume material tube for arbitrarily large record ratios, then

\[
\mathfrak D_\rho\le M_*/m_*
\]

is uniformly bounded.

Therefore no positive asymptotic mean covariance can persist.

In particular

\[
\boxed{
\left\langle
\bar\sigma_\rho-\bar\sigma_{ds}
\right\rangle=\frac34
}
\]

is incompatible with fixed positive-volume material genealogy plus two-sided amplitude compactness.

This closes that subbranch before any palinstrophy contradiction is needed.

## 6. Relation to the cubic ancestral firewall

The record-cubic law

\[
\mathfrak D_\rho\gtrsim\mathcal R^3
\]

matches the cubic exponent appearing independently in:

- M17-405 raw-`H2` ancestry;
- M17-411 ambient 3D packet capacity;
- M17-425 record-dependent material-label volume.

This does not itself prove a contradiction.

It shows instead that exporting the M17-188 recurrent covariance into a decompactifying fixed-tube branch forces the missing compactness to reappear as an exactly cubic amplitude-contrast defect.

## 7. Topological/analytic interpretation

If the loop states remain spatially precompact in a topology controlling `rho` uniformly and `M_rho` stays bounded, then

\[
m_\rho\to0
\]

forces every convergent subsequence carrying the cubic contrast to approach a state with a nodal point on the loop.

Hence the bounded-amplitude decompactifying covariance branch routes to

\[
\boxed{G_{nodal/amplitude\ loss}.}
\]

If no such compact convergence is available, retain the corresponding state/domain decompactification exit.

## 8. Updated split

For a fixed material positive-volume tube attempting to retain the M17-188 covariance,

\[
\boxed{
\begin{aligned}
H_{positive\ mean\ covariance}
\Longrightarrow{}&
G_{record\text{-}cubic\ amplitude\ contrast}\\
\Longrightarrow{}&
G_{amplitude\ floor\ loss/nodal\ approach}\\
&\lor G_{amplitude\ ceiling\ blowup}\\
&\lor G_{state/domain\ decompactification}.
\end{aligned}
}
\]

Thus natural fixed-tube decompactification does not preserve a free M17-361 palinstrophy payer; the payer is converted into cubic amplitude contrast.

## 9. DSD role

DSD is used only to track conversion of one apparent payer into another and to prevent the same compactness assumption from being counted twice.

The proof consists of the exact M17-429 identity and the similarity-time/record-scale conversion.

## 10. Audit verdict

**PASS as a record-scale sharpening.**

The `3/4` covariance corresponds exactly to record-cubic amplitude-condition-number growth on a fixed material tube.

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
