# Smooth Double-Saturation Large-Core Closure — 2026-08-21

Status: **SMOOTH-ONLY EXTENSION OF THE PURE P_V S-CLOSED REGION / GLOBAL REGULARITY NOT PROVED.**

This note combines two independent necessary conditions on the same finite smooth first-hitting stage:

1. record-time absolute dissipation forces a sufficiently large strain amplitude if the stage is to survive;
2. anti-ribbon projective survival near the swap threshold forces enstrophy to remain close to the record-point minimum.

The two requirements are incompatible on an explicit interval.

## 1. Corridor used in this note

Retain the previously audited broad pure moving-ball corridor, so

\[
\frac{\Pi_B}{c_*(2)^2}\le1.4967761748,
\qquad
c_*(2)\ge1.
\]

Also impose the local record-ball low-turnover thresholds

\[
\eta\le\frac12,
\qquad
\widehat f\le\frac18,
\qquad
\widehat\kappa\le\frac18.
\]

Failure of these local inequalities is not declared regular: it exits this subcorridor into record-core boundary/material turnover or endpoint reshaping.

The derivative/enstrophy tail parameter is denoted by `epsilon_Q`; the robust case below uses

\[
\varepsilon_Q\le\frac14.
\]

## 2. Survival of the record-time dissipation gate forces high strain

The record-time absolute dissipation gate gives the necessary condition

\[
\frac{71}{168}(1-\eta)
\frac{\nu K_{2,+}}
{B_S(B_S^2+1/2)}
\le
\frac14+\widehat f+\widehat\kappa.
\]

Use

\[
\eta\le\frac12,
\qquad
\frac14+\widehat f+\widehat\kappa\le\frac12.
\]

For `M0=2`, take the valid analytic Hessian ceiling

\[
K_{2,+}=4/\rho_0^2,
\qquad
\rho_0^2=\frac{\nu/2}{c_*(2)^2}.
\]

Hence

\[
\nu K_{2,+}=8c_*(2)^2\ge8.
\]

Therefore survival requires

\[
B_S(B_S^2+1/2)
\ge
\frac{71}{21}c_*(2)^2
\ge
\frac{71}{21}.
\]

Let `B_crit` be the positive solution of

\[
\boxed{
B_{\rm crit}(B_{\rm crit}^2+1/2)=\frac{71}{21}.
}
\]

Numerically,

\[
\boxed{
B_{\rm crit}\approx1.390052946851672.
}
\]

Thus every survivor in this record-pure subcorridor satisfies

\[
\boxed{B_S\ge B_{\rm crit}.}
\]

## 3. High strain forces enstrophy above the Taylor minimum

The explicit second-Taylor Biot-Savart estimate is

\[
B_S
\le
C_{BS}K_2^{3/7}Z^{2/7},
\]

with

\[
C_{BS}
=\frac{7\,2^{13/14}3^{2/7}}{16\pi^{2/7}}
\approx0.821832758154486.
\]

Hence

\[
Z
\ge
\left(\frac{B_S}{C_{BS}}\right)^{7/2}K_2^{-3/2}.
\]

Since the actual `K_2` does not exceed `K_{2,+}`,

\[
K_2^{-3/2}\ge K_{2,+}^{-3/2}.
\]

The record-point Taylor minimum is

\[
Z_{\min}
=C_ZK_{2,+}^{-3/2},
\qquad
C_Z=\frac{64\sqrt2\pi}{105}
\approx2.708042933734623.
\]

Therefore every record-dissipation survivor obeys

\[
\boxed{
\frac{Z}{Z_{\min}}
\ge
\Gamma_Z
:=
\frac1{C_Z}
\left(\frac{B_{\rm crit}}{C_{BS}}\right)^{7/2}.
}
\]

Numerically,

\[
\boxed{
\Gamma_Z
\approx2.323871370291439.
}
\]

This lower bound uses only `c_*(2)>=1`; a larger actual analyticity denominator strengthens it.

## 4. Anti-ribbon survival gives the opposite enstrophy constraint

The sharpened compatible projective-speed estimate can be written

\[
C_V
\le
c_0+D_{\max}(r,\varepsilon_Q)
\left(\frac{Q}{Q_{\max}}\right)^{3/4}
\left(\frac{Z}{Z_{\min}}\right)^{-1/4},
\]

where

\[
c_0=\frac{\sqrt2}{4},
\]

and, for `M0=2`,

\[
D_{\max}(r,\varepsilon_Q)
=0.7146986969\,
(1-\varepsilon_Q)^{-3/4}r^{9/4}.
\]

The moving-ball upper time and anti-ribbon lower time imply the necessary projective speed

\[
C_V
\ge
C_{\rm req}(r)
:=
\frac{\pi c_*(2)^2}{\Pi_Br^2}-\frac12.
\]

Using

\[
c_*(2)^2/\Pi_B\ge1/1.4967761748
\]

gives the conservative lower bound

\[
\boxed{
C_{\rm req}(r)
\ge
\frac{\pi}{1.4967761748\,r^2}-\frac12.
}
\]

Define

\[
\Theta(r,\varepsilon_Q)
=
\frac{
\left[\frac{\pi}{1.4967761748\,r^2}-\frac12-c_0\right]_+
}
{D_{\max}(r,\varepsilon_Q)}.
\]

Because `Q/Q_max<=1`, survival forces

\[
\boxed{
\frac{Z}{Z_{\min}}
\le
\Theta(r,\varepsilon_Q)^{-4}.
}
\]

## 5. Explicit double-saturation contradiction

The record-dissipation branch requires

\[
Z/Z_{\min}\ge\Gamma_Z,
\]

while projective survival requires

\[
Z/Z_{\min}\le\Theta^{-4}.
\]

Hence the subcorridor is S-closed whenever

\[
\boxed{
\Theta(r,\varepsilon_Q)^{-4}<\Gamma_Z.
}
\]

### Quarter-tail robust case

For

\[
\varepsilon_Q\le\frac14,
\]

the equality

\[
\Theta(r,1/4)^{-4}=\Gamma_Z
\]

occurs at

\[
\boxed{
r_{DS}^{(1/4)}
\approx1.0982016691.
}
\]

Therefore

\[
\boxed{
r<1.0982016691
\quad\Longrightarrow\quad
\text{this double-pure positive-middle P_V subcorridor is S-closed}.
}
\]

This strictly extends the direct quarter-tail anti-ribbon threshold

\[
1.06060560
\]

by using the incompatibility between the high strain needed to evade record dissipation and the low enstrophy needed to saturate projective speed.

### Zero derivative tail

For

\[
\varepsilon_Q=0,
\]

the same equality occurs at

\[
\boxed{
r_{DS}^{(0)}
\approx1.1363810659.
}
\]

Thus on the zero-tail record-pure subcorridor the direct smooth S-closed interval extends beyond the previous anti-ribbon radius `1.09908244` to about

\[
\boxed{1.13638107\,\rho_0.}
\]

## 6. What survives

A stage beyond the new double-saturation threshold must activate at least one of:

1. record-ball boundary/material flux above the chosen local threshold;
2. record-ball endpoint reshaping above the chosen local threshold;
3. derivative spatial tail beyond the stated `epsilon_Q` corridor;
4. sufficiently large common analytic-scale radius;
5. or a still tighter simultaneous saturation of strain, palinstrophy, enstrophy and projective speed.

No compact or ancient limit is used.

Status: **THE LARGE-CORE PURE P_V EXTERNAL-TIGHTROPE HAS BEEN NARROWED FURTHER BY A DIRECT INCOMPATIBILITY: EVADING RECORD-TIME DISSIPATION REQUIRES ENSTROPHY AT LEAST `2.32387` TIMES THE RECORD TAYLOR MINIMUM, WHILE ANTI-RIBBON SURVIVAL NEAR THE PROJECTIVE THRESHOLD REQUIRES ENSTROPHY TO REMAIN BELOW THAT LEVEL.**