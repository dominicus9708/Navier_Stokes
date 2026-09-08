# DSD M17-429 — Exact loop covariance is the logarithmic defect of effective material-tube volume and vanishes under natural similarity dilation

Date: 2026-09-08  
Canonical ID: **M17-429**

Status: **ACTIVE MATERIAL-VOLUME / COVARIANCE REINTERPRETATION / M17-188 AND M17-361 DECOMPACTIFICATION AUDIT**

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Scope

M17-188 obtains the recurrent closed-loop covariance

\[
\left\langle \bar\sigma_\rho-\bar\sigma_{ds}\right\rangle=\frac34
\]

when the same material loop returns with comparable geometric length, enstrophy line weight, and thin-tube flux.

M17-361 converts the resulting tangential-gradient payer into global palinstrophy on a retained positive-flux loop family.

M17-424 later proves that any fixed positive-volume material tube must decompactify in similarity space because incompressibility preserves physical volume while the similarity map expands volume like `e^{3 theta/2}`.

The present module determines exactly what happens to the M17-188 covariance when that natural material-volume dilation is retained rather than suppressed by compact recurrence.

## 2. Exact M17-188 logarithmic laws

For a closed regular material CE-H vortex loop `Gamma(theta)`, let

\[
\ell:=\oint_\Gamma ds,
\qquad
L_\rho:=\oint_\Gamma \rho\,ds,
\]

and let `Phi` denote the oriented flux of a coherent infinitesimal material tube label around that loop.

M17-188 gives

\[
\frac d{d\theta}\log\ell
=
\bar\sigma_{ds}+\frac12,
\]

\[
\frac d{d\theta}\log L_\rho
=
\kappa-\frac12+2\bar\sigma_\rho,
\]

and

\[
\frac d{d\theta}\log\Phi=\kappa.
\]

Subtracting the flux law and twice the length law from the line-weight law gives

\[
\frac d{d\theta}
\log\frac{L_\rho}{\Phi\ell^2}
=
2(\bar\sigma_\rho-\bar\sigma_{ds})-\frac32.
\]

Hence

\[
\boxed{
\bar\sigma_\rho-\bar\sigma_{ds}
=
\frac34
+
\frac12\frac d{d\theta}
\log\frac{L_\rho}{\Phi\ell^2}.
}
\]

This identity is exact on the stated regular CE-H material loop.

## 3. Effective tube volume

Define

\[
\boxed{
V_{eff}
:=
\frac{\Phi\ell^2}{L_\rho}.
}
\]

Then Section 2 becomes

\[
\boxed{
\frac d{d\theta}\log V_{eff}
=
\frac32
-2(\bar\sigma_\rho-\bar\sigma_{ds}).
}
\]

Thus the loop covariance is precisely the defect between the universal similarity material-volume expansion exponent `3/2` and the growth exponent of `V_eff`.

If `V_eff` is recurrent/comparable, its long-time logarithmic growth vanishes and one recovers M17-188:

\[
\left\langle \bar\sigma_\rho-\bar\sigma_{ds}\right\rangle
=
\frac34.
\]

If instead `V_eff` grows with the natural material-volume rate `e^{3 theta/2}`, the mean covariance vanishes.

## 4. Comparison with the actual infinitesimal tube volume

For one coherent infinitesimal flux tube label, define

\[
J_\rho:=\oint_\Gamma \rho^{-1}ds.
\]

The similarity-space volume of the differential tube band is

\[
\boxed{
dV_{tube}=d\Phi\,J_\rho.
}
\]

The corresponding effective differential volume is

\[
\boxed{
dV_{eff}
=
d\Phi\,\frac{\ell^2}{L_\rho}.
}
\]

By Cauchy--Schwarz,

\[
\ell^2
=
\left(\oint 1\,ds\right)^2
\le
\left(\oint \rho\,ds\right)
\left(\oint \rho^{-1}ds\right)
=
L_\rho J_\rho.
\]

Therefore

\[
\boxed{
dV_{eff}\le dV_{tube}.
}
\]

Define the amplitude-inhomogeneity factor

\[
\boxed{
\mathfrak D_\rho
:=
\frac{dV_{tube}}{dV_{eff}}
=
\frac{L_\rho J_\rho}{\ell^2}
\ge1.
}
\]

If along the loop

\[
0<m_\rho\le\rho\le M_\rho<\infty,
\]

then

\[
\boxed{
1\le\mathfrak D_\rho\le\frac{M_\rho}{m_\rho}.
}
\]

Hence bounded amplitude condition number makes actual and effective tube volume uniformly comparable.

## 5. Material incompressibility cancels the universal `3/4`

For a fixed physical material differential tube band, incompressibility preserves physical volume.

Under

\[
y=x/\sqrt{-t},
\qquad
\theta=-\log(-t),
\]

similarity volume therefore satisfies

\[
\boxed{
\frac d{d\theta}\log dV_{tube}=\frac32.
}
\]

Since

\[
dV_{eff}=dV_{tube}/\mathfrak D_\rho,
\]

we have

\[
\frac d{d\theta}\log dV_{eff}
=
\frac32
-
\frac d{d\theta}\log\mathfrak D_\rho.
\]

Comparing with Section 3 gives the sharper exact identity

\[
\boxed{
2(\bar\sigma_\rho-\bar\sigma_{ds})
=
\frac d{d\theta}\log\mathfrak D_\rho.
}
\]

Thus, on a fixed positive-volume material tube, the M17-188 covariance is not an independent recurrent geometric payer.

It is exactly half the logarithmic growth rate of longitudinal amplitude inhomogeneity.

## 6. Consequence for bounded-amplitude-ratio material tubes

Suppose

\[
\sup_\theta\frac{M_\rho(\theta)}{m_\rho(\theta)}<\infty.
\]

Then `mathfrak D_rho` is bounded, so on any sequence of long intervals

\[
\frac1T
\log\frac{\mathfrak D_\rho(\theta_0+T)}{\mathfrak D_\rho(\theta_0)}
\to0.
\]

Therefore

\[
\boxed{
\left\langle
\bar\sigma_\rho-\bar\sigma_{ds}
\right\rangle
=0
}
\]

for the natural fixed-material-tube dilation branch.

Hence the positive recurrent `3/4` covariance of M17-188 cannot coexist with all of:

1. one fixed positive-volume material tube label;
2. unbroken exact regular CE-H genealogy;
3. the natural incompressible material-volume law;
4. a uniformly bounded amplitude condition number.

At least one of these must fail.

## 7. Reinterpretation of the M17-361 palinstrophy payer

M17-188 uses

\[
|\bar\sigma_\rho-\bar\sigma_{ds}|
\le
\frac{\ell^2}{4\pi^2L_\rho}
\|\partial_s\sigma\|_2
\|\partial_s\rho\|_2.
\]

A positive time-mean covariance therefore forces tangential gradient occupancy only when the covariance itself stays positively bounded away from zero.

Section 5 shows that, for a fixed material tube,

\[
\bar\sigma_\rho-\bar\sigma_{ds}
=\frac12(\log\mathfrak D_\rho)'.
\]

Consequently the M17-361 payer has the refined interpretation

\[
\boxed{
\text{positive recurrent loop covariance}
\Longrightarrow
\text{amplitude-inhomogeneity growth}
\Longrightarrow
\text{gradient occupancy},
}
\]

not

\[
\text{natural fixed-tube decompactification}
\Longrightarrow
\text{uniform positive palinstrophy density}.
\]

The latter implication is invalid.

## 8. Updated decompactifying-loop split

The retained loop branch now has the sharper split

\[
\boxed{
\begin{aligned}
G_{loop/tube\ decompactification}
\Longrightarrow{}&
G_{natural\ fixed\ material\ volume\ dilation}\\
&\lor G_{amplitude\ condition\ number\ decompactification}\\
&\lor G_{selected\ material\ label\ turnover}\\
&\lor G_{nodal/interface/CEH/domain\ loss}.
\end{aligned}
}
\]

The first branch does not force the M17-361 palinstrophy payer: its universal `3/2` material-volume dilation exactly cancels the `3/4` covariance after the effective-volume correction.

## 9. DSD role

DSD is used only to demand payer-equivalence and to separate material volume, flux, line weight, and amplitude-inhomogeneity channels.

All formulas above are ordinary material-flow, flux-coordinate, Cauchy--Schwarz, and exact CE-H line identities.

## 10. Audit verdict

**PASS as a correction/refinement of the decompactifying-loop use of M17-188/M17-361.**

The recurrent covariance is an effective-volume defect. It cannot be exported unchanged from the compact recurrent loop branch into the natural fixed-material-tube decompactification branch.

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
