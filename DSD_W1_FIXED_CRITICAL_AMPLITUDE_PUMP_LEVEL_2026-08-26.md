# DSD W1 Fixed Critical-Amplitude Pump Level

Date: 2026-08-26

Status: **THE POSITIVE STRICT-BAND INVARIANT GAIN IS REDUCED TO ONE FIXED NORMALIZED AMPLITUDE LEVEL (OR FIXED SMOOTH MICRO-BAND) WITH POSITIVE MEAN PRESSURE-MINUS-VISCOUS GAIN / IN PHYSICAL VARIABLES THIS LEVEL TRACKS THE TYPE-I AMPLITUDE `1/sqrt(T-t)` / GLOBAL REGULARITY UNPROVED.**

## 1. Strict interior mean gain

There is a fixed interval

\[
I_*=[\lambda_-,\lambda_+]
\Subset(0,A_*)
\]

such that

\[
\boxed{
\int_{I_*}
\bar G(\lambda)d\lambda
\ge c_*>0,
}
\]

where

\[
\bar G(\lambda)
:=
\left\langle
J_P(\lambda)-\nu D_\lambda
\right\rangle_\mu.
\]

## 2. One fixed amplitude level

By averaging, there exists

\[
\boxed{\lambda_c\in I_*}
\]

such that

\[
\boxed{
\bar G(\lambda_c)
\ge
\frac{c_*}{|I_*|}
=:g_c>0
}
\]

for a Lebesgue/regular value. To avoid exceptional level-set issues completely, replace the sharp level by a fixed smooth threshold kernel supported in a small neighborhood of `lambda_c`; the positive mean survives after choosing the neighborhood sufficiently small.

Thus one does not need to choose a new amplitude level at every recurrent event.

## 3. Ergodic/time-average form

Choose an ergodic invariant measure on the minimal W1 set. For the fixed smooth amplitude pump observable `G_c(U)`, Birkhoff gives for almost every orbit representative

\[
\boxed{
\lim_{S\to\infty}
\frac1S\int_0^S G_c(\Phi_sU)ds
=g_c>0.
}
\]

Continuity on the compact finite-parent class also gives recurrent open events with a fixed positive instantaneous threshold.

The fixed-level statement is therefore both statistical and recurrent.

## 4. Physical amplitude scale

The Leray and physical velocities satisfy

\[
u(x,t)=(T_*-t)^{-1/2}U(Y,s).
\]

Hence the fixed normalized amplitude level `lambda_c` corresponds to the physical velocity threshold

\[
\boxed{
L_c(t)
=
\frac{\lambda_c}{\sqrt{T_*-t}}.
}
\]

Thus the same relative amplitude state is pumped repeatedly while its physical amplitude grows at the Type-I rate.

## 5. Spatial scale

Because `lambda_c>0` and the normalized Type-I tail obeys

\[
|U(Y)|\lesssim |Y|^{-1},
\]

the pump is contained in a fixed normalized parent radius. In physical coordinates its spatial diameter is therefore

\[
\boxed{
r_c(t)\asymp\sqrt{T_*-t}.}
\]

The pressure pump is a self-similarly shrinking core event.

## 6. DSD interpretation

The large weak-critical survivor must maintain one fixed state transition:

\[
\boxed{
\text{normalized amplitude }\lambda_c
\xrightarrow{\text{pressure gain} > \text{viscous loss}}
\text{higher-amplitude state}
}
\]

with positive recurrent/time-average action.

The low-amplitude weak-L3 defect is the output carried away in normalized amplitude space by the characteristic drift `lambda'=-lambda/2`.

## 7. Limitation

The physical energy cost of one normalized pump event still has positive scaling exponent and can be summable over shrinking physical stages. Thus fixed-level recurrence alone is not yet a contradiction.

A complete closure needs a genuinely critical theorem controlling the mean gain at this fixed amplitude state.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
