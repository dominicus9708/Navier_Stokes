# M19-210 — Authoritative correction: tail-to-core lower observability cannot exclude a kernel whose necessary condition is a lower severity threshold

**Date:** 2026-09-14  
**Status:** AUTHORITATIVE CORRECTION / DIRECTIONAL FIREWALL

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Correction target

M19-209 correctly observed that the existing tail bounds do not close the moderate kernel problem, but it suggested background tail-to-core lower observability as a potentially decisive comparison with the M19-208 kernel threshold.

That direction must be corrected.

## 2. Kernel threshold is a lower bound

M19-208 proves the necessary condition

\[
\boxed{
\text{nonsymmetry kernel}
\Longrightarrow
\frac{K\Gamma W}{\nu}\ge\chi_*>0.
}
\]

Therefore a lower estimate of the form

\[
K\ge c\,\mathcal N(A)
\]

cannot contradict kernel existence. It only supplies another lower floor and may make the necessary condition easier to satisfy.

## 3. What weighted contraction would actually need

To exclude kernels by the M19-207 weighted contraction mechanism one needs an **upper-smallness** statement strong enough to give

\[
\boxed{
\frac{K\Gamma W}{\nu}<\chi_*.
}
\]

No such uniform smallness estimate is currently certified on the moderate finite-amplitude RSS/RDSS hard set. Indeed that set was obtained precisely after small/extreme parameter and low-activity regimes had already been removed.

## 4. Revised role of background tail observability

A quantitative tail-to-core lower observability theorem remains structurally useful for identifying nonvanishing background activity and norm equivalence, but it is **not** the missing kernel-rigidity theorem for the contraction route.

Thus the principal bounded-period frontier is not merely a missing observability constant. It is genuine finite-amplitude Fredholm rigidity/sign structure beyond smallness-based contraction.

## 5. Permanent firewall

\[
\boxed{
\text{lower activity floor}
\neq
\text{upper smallness needed for contraction}.
}
\]

This correction supersedes any reading of M19-209 that treats a tail-to-core lower bound alone as sufficient to close the kernel branch.

## 6. Updated kernel frontier

The moderate RSS/RDSS problem now reads:

\[
\boxed{
\mathcal T_{kernel}^{finite\text{-}amp}:
\text{exclude nonsymmetry unit/Fredholm kernels without assuming small nonlinear activity.}
}
\]

This requires a signed, index, topological, or profile-specific PDE mechanism not yet supplied by the current weighted contraction estimates.