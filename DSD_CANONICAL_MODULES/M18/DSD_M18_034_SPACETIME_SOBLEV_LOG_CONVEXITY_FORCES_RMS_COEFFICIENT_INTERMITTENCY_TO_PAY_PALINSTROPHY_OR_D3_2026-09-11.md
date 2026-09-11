# M18-034 — Spacetime Sobolev log-convexity forces RMS coefficient intermittency to pay palinstrophy or D3

**Date:** 2026-09-11  
**Status:** ACTIVE DSD ANALYSIS / HEAVY-TAIL DESCENT / STANDARD-RESOURCE RECONNECTION

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Purpose

M18-033 isolated an RMS-tail intermittency branch in which

\[
K_H^{\rm eff}
\gg
K_P^{\rm eff}.
\]

At the coefficient-distribution level this can be realized by raw-H2 charge on very large coefficient values carrying small weighted mass.

This module asks whether such a branch is genuinely outside the existing derivative ledgers.

The answer is no at the first level of audit: standard Sobolev log-convexity gives an exact spacetime inequality

\[
\boxed{
q_H^2\le q_Pq_{J_3}.
}
\]

Therefore large raw-H2 with small palinstrophy necessarily forces large D3 spacetime charge.

## 2. Snapshot Fourier interpolation

Define at one time

\[
P(t):=\|D\Omega(t)\|_2^2,
\]

\[
H(t):=\|D^2\Omega(t)\|_2^2,
\]

\[
J_3(t):=\|D^3\Omega(t)\|_2^2.
\]

Fourier Cauchy--Schwarz gives

\[
\boxed{
H(t)^2
\le
P(t)J_3(t).
}
\]

Equivalently,

\[
H(t)
\le
P(t)^{1/2}J_3(t)^{1/2}.
\]

No CE-H assumption is needed for this interpolation inequality.

## 3. Spacetime interpolation

Integrate over a record interval \(I\):

\[
q_H
:=
\int_IH(t)dt
\le
\int_I
P(t)^{1/2}J_3(t)^{1/2}dt.
\]

Cauchy--Schwarz in time gives

\[
q_H
\le
q_P^{1/2}q_{J_3}^{1/2},
\]

where

\[
q_P:=\int_IPdt,
\qquad
q_{J_3}:=\int_IJ_3dt.
\]

Hence

\[
\boxed{
q_H^2
\le
q_Pq_{J_3}.
}
\]

This is the main M18-034 inequality.

## 4. Exact heavy-tail descent

If \(q_P>0\), then

\[
\boxed{
q_{J_3}
\ge
\frac{q_H^2}{q_P}.
}
\]

Thus a raw-H2 payment cannot coexist with arbitrarily small palinstrophy and bounded D3 charge.

The coefficient heavy-tail interpretation of M18-033 therefore has the derivative-resource split

\[
\boxed{
G_{\rm RMS\ coefficient\ tail}
\Longrightarrow
G_{\rm palinstrophy\ payment}
\lor
G_{\rm D3\ spacetime\ concentration}.
}
\]

The split is quantitative rather than merely qualitative.

## 5. Effective coefficient form

Recall from M18-032

\[
K_P^{\rm eff}
=m
=rac{q_P}{q_E},
\]

and

\[
K_H^{\rm eff}
=s
=\left(\frac{q_H}{q_E}\right)^{1/2}.
\]

Define the D3-to-energy effective coefficient scale

\[
\boxed{
K_3^{\rm eff}
:=
\left(
\frac{q_{J_3}}{q_E}
\right)^{1/3}.
}
\]

This scales like a coefficient because \(q_{J_3}/q_E\) scales as \(R^6\).

Divide the inequality

\[
q_H^2\le q_Pq_{J_3}
\]

by \(q_E^2\):

\[
s^4
\le
m(K_3^{\rm eff})^3.
\]

Therefore

\[
\boxed{
K_3^{\rm eff}
\ge
s\left(\frac{s}{m}\right)^{1/3}
}
\]

when \(m>0\).

In the RMS-intermittent regime

\[
\frac{s}{m}\to\infty,
\]

the effective D3 scale must exceed the RMS coefficient scale by the factor

\[
(s/m)^{1/3}.
\]

Thus coefficient RMS intermittency is simultaneously a derivative-frequency intermittency.

## 6. Relation to M18-033 tail threshold

M18-033 showed that in the L1/RMS intermittent branch, at least half of raw-H2 lies above coefficient magnitude

\[
L_*
=
\frac{s^2}{2A_1}.
\]

M18-034 adds that if the corresponding palinstrophy charge remains small, the D3 spacetime charge must grow at least like

\[
q_H^2/q_P.
\]

Therefore the heavy coefficient tail is not an unpriced geometric object: it either contributes to the lower-order palinstrophy channel or produces higher derivative-frequency cost already visible to the certified D3 ledger.

## 7. Ancestry comparison

The two fallback ledgers are

\[
\boxed{
\sum_mR_m^{-1}q_{P,m}<\infty
}
\]

and

\[
\boxed{
\sum_mR_m^{-5}q_{J_3,m}<\infty.
}
\]

The interpolation lower bound gives

\[
\boxed{
R_m^{-5}q_{J_3,m}
\ge
R_m^{-5}
\frac{q_{H,m}^2}{q_{P,m}}.
}
\]

Thus a record cannot simultaneously keep

- raw-H2 large,
- palinstrophy strongly suppressed,
- and D3 parent cost small

without satisfying a precise scaling tradeoff.

This does not yet force either ancestry series to diverge.

## 8. Optimization between P and D3

For a fixed raw-H2 charge \(q_H\), the two generic parent costs are

\[
C_P:=R^{-1}q_P,
\qquad
C_3:=R^{-5}q_{J_3}.
\]

The interpolation constraint is

\[
q_Pq_{J_3}\ge q_H^2.
\]

If one asks for the smallest possible value of the larger of the two parent costs, balance

\[
R^{-1}q_P
=R^{-5}q_{J_3}.
\]

Together with equality in the interpolation constraint, this gives

\[
q_P=Rq_H,
\qquad
q_{J_3}=R^{-1}? 
\]

The displayed naive balancing mixes normalized record dimensions incorrectly if \(R\) is treated inside one already normalized record. Therefore no new representation-dependent hybrid currency is declared here.

The correct audit rule is to keep the two certified parent ledgers separate and apply the exact record map before optimization.

This section records an important firewall: do not manufacture a mixed ancestry norm by balancing powers of \(R\) inside one record coordinate system.

## 9. Stronger standard-energy route when effective coefficient is controlled

If the palinstrophy branch is selected and \(K_P^{\rm eff}\) is not sufficiently large, M18-032 upgrades it to the positive-R standard-energy ledger.

Therefore the RMS-tail branch now has the nested structure

\[
\boxed{
\begin{aligned}
G_{\rm RMS\ coefficient\ intermittency}
\Longrightarrow{}&
G_{P}\n\\
&\lor G_{D3},
\end{aligned}
}
\]

and the \(G_P\) branch further gives

\[
\boxed{
G_P
\Longrightarrow
G_{\rm standard\ energy\ contradiction}
\lor
G_{K_P^{\rm eff}\text{-growth}}
\lor
G_{\rm genealogy\ loss}.
}
\]

Thus only the D3-dominated intermittent branch remains genuinely high-order after all lower-order descents are attempted.

## 10. Correction of scope

M18-033 called RMS-tail intermittency a genuine coefficient heavy-tail endpoint because coefficient-distribution information alone does not give a positive tail-mass fraction.

M18-034 refines that statement:

\[
\boxed{
\text{it is a genuine coefficient-distribution endpoint, but not an unpriced PDE-resource endpoint}.}
\]

The PDE Sobolev hierarchy already prices it through \(P\) or D3.

## 11. Audit verdict

### Certified

1. \(q_H^2\le q_Pq_{J_3}\) on every smooth record interval.
2. Large raw-H2 with small palinstrophy forces large D3 spacetime charge.
3. RMS coefficient intermittency implies an even larger effective D3 frequency scale when the signed palinstrophy coefficient remains small.
4. The M18-033 heavy-tail branch reconnects to certified derivative resources.

### Not certified

1. Divergence of either the palinstrophy or D3 ancestry series.
2. A lower-order descent for the D3-dominated intermittent branch.
3. Bounded-overlap/non-reuse for the selected tail records.
4. ROOT-CERT or non-CE-H closure.
5. Global 3D Navier--Stokes regularity.

## 12. Next target

M18-035 should now audit the D3-dominated branch economically against the positive-R standard-energy and coefficient-effective scales.

The key question is whether repeated D3-dominated intermittency can occur with

\[
R_m^{-5}q_{J_3,m}
\]

summable while simultaneously producing the effective coefficient growth required to evade the lower-order palinstrophy/standard-energy route, or whether this forces a precise scale-separation/genealogy mismatch.