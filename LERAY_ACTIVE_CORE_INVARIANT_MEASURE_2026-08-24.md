# Leray Active-Core Invariant Measure — 2026-08-24

Status: **NONZERO RECURRENT-STATE REDUCTION / GLOBAL REGULARITY NOT PROVED.**

This note turns the restricted ancient survivor into a compact dynamical-systems problem in Leray variables.

## 1. Leray trajectory

Let

\[
T=-\tau,
\qquad
Y=y/\sqrt T,
\qquad
s=-\log T,
\]

and

\[
V(Y,s)=\sqrt T\,U(y,\tau),
\qquad
W(Y,s)=T\,\Omega(y,\tau).
\]

The restricted ancient estimates give

\[
\sup_s
\left(
\|V(s)\|_6+
\|V(s)\|_\infty+
\|W(s)\|_2+
\|W(s)\|_\infty
\right)<\infty.
\]

The equation is autonomous:

\[
V_s+\frac12V+\frac12Y\cdot\nabla V+(V\cdot\nabla)V+\nabla\Pi=\nu\Delta V,
\qquad \nabla\cdot V=0.
\]

Because the trajectory is smooth and uniformly bounded in the preceding norms, standard interior parabolic smoothing on every fixed cylinder gives, for each fixed `R,m`,

\[
\sup_s\|V(s)\|_{C^m(B_R)}<\infty.
\]

Hence the orbit is precompact in `C^m_loc` after passing to a diagonal topology.

## 2. First-hitting recurrence times are relatively dense in Leray time

At the inherited backward first-hitting times `tau_m`,

\[
c_-q^m\le |\tau_m|\le c_+q^m,
\]

and

\[
\|\Omega(\tau_m)\|_\infty=q^{-m}.
\]

Therefore the Leray vorticity amplitude satisfies

\[
\boxed{
c_-\le \|W(s_m)\|_\infty\le c_+,}
\]

where

\[
s_m=-\log|\tau_m|.
\]

Moreover

\[
0<s_m-s_{m+1}
=\log\frac{|\tau_{m+1}|}{|\tau_m|}
\le
G_+:=\log\left(q\frac{c_+}{c_-}\right).
\]

Thus the active first-hitting checkpoints are relatively dense as `s -> -infinity`.

## 3. Positive-density thick-core windows

At each checkpoint choose a point `Y_m` where the Leray vorticity reaches its maximum. No-`T` similarity-scale center control keeps

\[
|Y_m|\le R_*.
\]

Uniform local derivative bounds imply constants

\[
r_*>0,
\qquad
\delta_*>0,
\qquad
w_*>0
\]

such that on a Leray-time interval of length at least `delta_*` adjacent to each sufficiently late checkpoint,

\[
|W(Y,s)|\ge w_*
\]

on a ball of radius `r_*` contained in a fixed ball `B_{R_0}`.

Consequently for a fixed nonnegative cutoff `chi` equal to one on `B_{R_0}`,

\[
F(V(s)):=\int\chi|W(s)|^2dY
\]

satisfies

\[
F(V(s))\ge f_*>0
\]

on a set of Leray times with lower density at least

\[
\boxed{
d_*\ge \min\{1,\delta_*/G_+\}>0.}
\]

Hence

\[
\boxed{
\liminf_{S\to\infty}
\frac1S\int_{-S}^0F(V(s))ds
\ge d_*f_*>0.
}
\]

This prevents the active Leray orbit from becoming statistically trivial.

## 4. Krylov-Bogolyubov measure on the orbit closure

Let `K` be the compact local orbit closure of the Leray trajectory and define the empirical measures

\[
\mu_S
=\frac1S\int_{-S}^0\delta_{V(s)}ds.
\]

Compactness gives a weakly convergent subsequence

\[
\mu_{S_n}\rightharpoonup\mu.
\]

Autonomy and continuity of the Leray flow in the local smooth topology imply that `mu` is invariant.

The local observable `F` is continuous, so

\[
\boxed{
\int_KF\,d\mu
\ge d_*f_*>0.
}
\]

Thus `mu` is not the Dirac mass at zero and assigns positive mass to nonzero active-core states.

## 5. Poincare recurrence gives a nonzero recurrent state

Poincare recurrence for the invariant probability measure implies that `mu`-almost every state is recurrent.

Since `F>0` on a set of positive `mu`-measure, there exists a recurrent state `V_*` with

\[
\boxed{F(V_*)>0.}
\]

Therefore the residual singular branch forces an actual nonzero recurrent complete Leray solution, not merely a sequence of unrelated ancient snapshots.

## 6. Classification of the recurrent target

The surviving dynamical target is now

\[
\boxed{
\text{nonzero recurrent bounded Leray trajectory}
}
\]

with

\[
V\in L_s^\infty(L_x^6\cap L_x^\infty),
\qquad
W\in L_s^\infty(L_x^2\cap L_x^\infty),
\]

plus the inherited first-hitting/projective restrictions.

There are three subcases:

1. stationary recurrent state;
2. periodic recurrent state;
3. genuinely aperiodic recurrent state.

A stationary state belongs to `L^6` and is excluded by the classical Tsai/Nečas-Ružička-Šverák backward-self-similar Liouville theory.

The general periodic `L^6` but non-`L^3` case is not removed by the currently identified periodic-profile theorem, whose clean hypothesis is global `L^3`; near-identity DSS exclusions cover only an additional restricted scaling range.

Thus the honest final target is

\[
\boxed{
\text{periodic non-}L^3
\quad\lor\quad
\text{aperiodic recurrent bounded Leray dynamics}.
}
\]

Status: **FIRST-HITTING RECURRENCE + LOCAL COMPACTNESS PRODUCE AN INVARIANT PROBABILITY MEASURE WITH POSITIVE ACTIVE-CORE MASS, HENCE A NONZERO RECURRENT LERAY STATE. STATIONARY RECURRENCE IS EXCLUDED BY KNOWN SELF-SIMILAR LIOUVILLE THEORY; THE REMAINDER IS PERIODIC NON-L3 OR GENUINELY APERIODIC RECURRENCE. GLOBAL REGULARITY REMAINS UNPROVED.**