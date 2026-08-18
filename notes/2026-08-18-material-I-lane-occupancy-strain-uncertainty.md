# Material I-lane occupancy--strain uncertainty for compact multiplicity

Date: 2026-08-18

Status: **DERIVED FOR THE INVISCID MATERIAL CONTRIBUTION ON A THICK I-LANE. IF THE ACTUAL VORTICITY TRACKS THIS CONTRIBUTION WITHOUT LARGE VISCOUS CANCELLATION, PHYSICAL ENERGY DISSIPATION TIMES CRITICAL `L_t^2L_x^3` STRAIN ACTION IS BOUNDED BELOW BY `c N^(5/3)/K`. LARGE CANCELLATION ROUTES TO THE V/V2 BRANCH. GLOBAL REGULARITY NOT PROVED.**

## 1. Material I contribution

Use the deep compact checkpoint

\[
q=K,
\qquad
\|\Omega_-\|_\infty\le K^{-1}
\]

in terminal-normalized variables.

On the I-lane define

\[
z(a,s)=F(a,s)\Omega_-(a).
\]

For

\[
e_z=z/|z|,
\qquad
a_z=e_z^TSe_z,
\]

we have exactly

\[
\frac d{ds}|z|=a_z|z|.
\]

Assume a thick I-lane label set `A` with

\[
|A|\asymp N_I,
\]

and terminal amplification

\[
|z(a,s_c)|\gtrsim1,
\qquad
|z(a,s_-)|\lesssim K^{-1}.
\]

## 2. Spacetime lower bound

For each label,

\[
\int|a_z||z|ds
\ge
\left||z(s_c)|-|z(s_-)|\right|
\gtrsim1.
\]

Integrating over labels gives

\[
\int ds\int_A|a_z||z|da
\gtrsim N_I.
\]

Cauchy--Schwarz in label-time yields

\[
\left(
\int ds\int_A|z|^2da
\right)
\left(
\int ds\int_A|a_z|^2da
\right)
\gtrsim N_I^2.
\]

Since `|a_z|<=|S|` and the material flow preserves volume,

\[
\int_{X(A,s)}|S|^2dx
\le
|X(A,s)|^{1/3}\|S(s)\|_3^2
\asymp
N_I^{1/3}\|S(s)\|_3^2.
\]

Therefore

\[
\boxed{
\left(
\int ds\int_A|z|^2da
\right)
\left(
\int\|S(s)\|_3^2ds
\right)
\gtrsim
N_I^{5/3}.
}
\]

This is independent of the duration of the deep amplification interval.

## 3. Convert to actual enstrophy when cancellation is small

The actual vorticity along the labels is

\[
\Omega(X(a,s),s)=z(a,s)+V(a,s),
\]

where `V` is the viscous Cauchy defect accumulated from the deep checkpoint.

On a sublane where

\[
|V(a,s)|\le\theta|z(a,s)|
\]

with fixed `theta<1` on the spacetime portion carrying a fixed fraction of the `z^2` action,

\[
|\Omega|^2\gtrsim|z|^2.
\]

Hence

\[
\int E_{norm}(s)ds
\gtrsim
\int ds\int_A|z|^2da.
\]

Under terminal scaling `W=K^2`, physical kinetic-energy dissipation satisfies

\[
D_{phys}
:=\nu\int E_{phys}(t)dt
=\frac\nu K\int E_{norm}(s)ds.
\]

The strain norm

\[
\mathcal S_3=\int\|S\|_3^2dt
\]

is scale invariant. Consequently

\[
\boxed{
D_{phys}\,\mathcal S_3
\gtrsim
c_\nu\frac{N_I^{5/3}}{K}.
}
\]

## 4. Cancellation branch

If the tracking condition fails on a substantial portion of the `z^2` action, then

\[
|V|\gtrsim|z|
\]

there. This is not an independent cheap escape: by the exact Cauchy-defect formula it requires a correspondingly large deformation-weighted `Delta Omega` history and routes back to the V/V2/material-condition-number branch already retained in the proof graph.

## 5. Interpretation

Long preparation time alone cannot make a thick I-lane multiplicity free. Avoiding physical enstrophy occupancy forces stronger strain; avoiding strain by spreading amplification in time forces occupancy; cancelling the inviscidly amplified contribution requires viscous derivative rewriting.

The product lower bound becomes order one at the multiplicity scale

\[
N_I\sim K^{3/5}.
\]

Below that scale it is still compatible with a Zeno cascade, so this does not close the compact lane.

Status: **I-LANE LONG-GENEALOGY COST SHARPENED TO OCCUPANCY--STRAIN PRODUCT OR VISCOUS CANCELLATION / GLOBAL REGULARITY NOT PROVED.**