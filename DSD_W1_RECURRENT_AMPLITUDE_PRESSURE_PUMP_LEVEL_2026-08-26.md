# DSD W1 Recurrent Amplitude Pressure-Pump Level

Date: 2026-08-26

Status: **THE STRICT INTERIOR AMPLITUDE GAIN BAND IS REFINED TO A RECURRENT REGULAR LEVEL WHERE PRESSURE FLUX EXCEEDS THE ENTIRE THRESHOLDED VISCOUS COST BY A FIXED AMOUNT / INCOMPRESSIBILITY CONVERTS THIS INTO A GAUGE-INVARIANT PRESSURE GAP BETWEEN AMPLITUDE INFLOW AND OUTFLOW SECTORS / GLOBAL REGULARITY UNPROVED.**

## 1. Strict interior gain functional

On a fixed amplitude interval

\[
I_*=[\lambda_-,\lambda_+]
\Subset(0,A_{max}),
\]

define

\[
\mathcal G_I(U)
:=
\int_{I_*}
\bigl[J_P(\lambda)-\nu D_\lambda\bigr]d\lambda.
\]

The previous strict-interior-band result gives positive invariant mean:

\[
\boxed{\langle\mathcal G_I\rangle_\mu>0.}
\]

Because the band is separated from both amplitude boundaries and lies in a finite Leray parent, `G_I` is continuous in the W1 local smooth topology after the standard smooth-level approximation.

Minimal recurrence therefore yields a nonempty recurrent open event where

\[
\boxed{\mathcal G_I(U)\ge g_I>0.}
\]

## 2. One regular pump level

For every such event, there exists a regular level

\[
\lambda_*\in I_*
\]

with

\[
\boxed{
J_P(\lambda_*)-\nu D_{\lambda_*}
\ge
\frac{g_I}{|I_*|}
=:g_{pump}>0.
}
\]

Thus

\[
\boxed{J_P(\lambda_*)>\nu D_{\lambda_*}+g_{pump}.}
\]

This is an instantaneous finite-core amplitude pump.

## 3. Equal geometric crossing fluxes

Let

\[
\Sigma_\lambda=\{|U|=\lambda\},
\qquad
n_\lambda=\frac{\nabla|U|}{|\nabla|U||}.
\]

Because `div U=0` and the superlevel region is bounded for `lambda in I_*`,

\[
\boxed{
\int_{\Sigma_\lambda}U\cdot n_\lambda dS=0.
}
\]

Define

\[
Q_+(\lambda)
:=
\int_{U\cdot n_\lambda>0}U\cdot n_\lambda dS,
\]

\[
Q_-(\lambda)
:=
-\int_{U\cdot n_\lambda<0}U\cdot n_\lambda dS.
\]

Then

\[
\boxed{Q_+=Q_-=:Q_\lambda.}
\]

The plus sector moves toward larger velocity magnitude and is the inflow sector of the superlevel set `|U|>lambda`; the minus sector is the outflow sector.

## 4. Gauge-invariant pressure gap

Define flux-weighted pressure averages

\[
\bar P_{in}
:=
Q_\lambda^{-1}
\int_{U\cdot n_\lambda>0}
P(U\cdot n_\lambda)dS,
\]

and

\[
\bar P_{out}
:=
Q_\lambda^{-1}
\int_{U\cdot n_\lambda<0}
P(-U\cdot n_\lambda)dS.
\]

Then

\[
\boxed{
J_P(\lambda)
=
Q_\lambda(\bar P_{in}-\bar P_{out}).
}
\]

The pressure difference is gauge invariant.

## 5. Fixed pressure advantage on a recurrent pump level

The coarea identity gives

\[
\int_{I_*}|\Sigma_\lambda|d\lambda
=
\int_{\{\lambda_-<|U|<\lambda_+\}}
|\nabla|U||dY,
\]

which is uniformly bounded on the compact W1 finite parent.

Combining the positive integrated gain with this area bound allows selection of a regular pump level for which `J_P/|Sigma_lambda|` has a fixed positive lower bound. Since on the level surface

\[
|U\cdot n_\lambda|\le\lambda_+,
\]

one has

\[
Q_\lambda\le\lambda_+|\Sigma_\lambda|.
\]

Consequently

\[
\boxed{
\bar P_{in}-\bar P_{out}
\ge \Delta P_*>0
}
\]

for a recurrently selected pump level, with `Delta P_*` depending only on the compact W1 band constants.

## 6. DSD pump cycle

The finite-core mechanism can therefore be represented as

\[
\boxed{
\text{higher-pressure amplitude inflow}
\to
\{|U|>\lambda_*\}
\to
\text{lower-pressure amplitude outflow}.
}
\]

Since pressure is a conservative gradient field, this pressure drop cannot be a one-way source around a closed spatial/material cycle. It must be paired with pressure recovery elsewhere in the flow. Thus the recurrent endpoint contains a pressure-pump / pressure-recovery loop rather than an external forcing source.

## 7. Remaining issue

The pump geometry is quantitative, but conservative pressure redistribution can in principle coexist with viscous dissipation and similarity normalization. A complete closure still requires a critical theorem showing that such recurrent finite-core pump cycles cannot sustain the large weak-L3 renormalization anomaly.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
