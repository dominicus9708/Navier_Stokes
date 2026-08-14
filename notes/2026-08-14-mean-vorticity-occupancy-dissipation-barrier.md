# Mean-vorticity occupancy dissipation barrier

Date: 2026-08-14

Status: **DERIVED ON THE BOUNDED-CONDITION, BOUNDED-ACCUMULATED-AFFINE BRANCH. A TERMINAL ORDER-ONE GAUSSIAN MEAN VORTICITY CREATED FROM THE ADAPTIVE PRECURSOR FORCES A STRONGER GLOBAL-ENSTROPHY OCCUPANCY COST. GLOBAL REGULARITY NOT PROVED.**

## 1. Co-affine Gaussian mean equation

Let

\[
\bar\Omega(t)=\int\gamma_t\Omega(t)
\]

be the self-consistent Gaussian mean vorticity. Its exact affine/residual equation is

\[
\bar\Omega'=L\bar\Omega+J,
\]

where

\[
J=\int\gamma f_r,
\qquad
|J|\lesssim_K B.
\]

Let `F` be the affine propagator,

\[
\partial_tF=L F.
\]

On the bounded accumulated-affine branch,

\[
\|F(t,s)\|+\|F(t,s)^{-1}\|\le C_K.
\]

Define the co-affine mean

\[
Z(t)=F(0,t)\bar\Omega(t).
\]

Then

\[
\boxed{Z'(t)=F(0,t)J(t),}
\]

and hence, whenever

\[
B(t)\le m,
\]

we have

\[
\boxed{|Z'(t)|\le C_Km.}
\]

## 2. Terminal and precursor values

At terminal first hitting the Gaussian covariance collapses to zero, so

\[
\bar\Omega(0)=\Omega(x_*,0),
\qquad
|\bar\Omega(0)|=1.
\]

Thus

\[
|Z(0)|=1.
\]

At the previous adaptive first-hitting checkpoint,

\[
\|\Omega\|_\infty\le q^{-1},
\]

so

\[
|\bar\Omega(t_-)|\le q^{-1}
\]

and therefore

\[
|Z(t_-)|\le C_Kq^{-1}.
\]

For large `q`, the affine homogeneous precursor cannot account for terminal order-one mean vorticity on the bounded-affine branch. An order-one residual mean contribution is necessary.

## 3. Backward Lipschitz occupancy

Write backward time

\[
\tau=-t\ge0.
\]

From `|Z'|<=C_Km` and `|Z(0)|=1`,

\[
|Z(-\tau)|
\ge
1-C_Km\tau.
\]

Choose a fixed small `c_K>0` such that

\[
C_Kc_K\le\frac12.
\]

Then for

\[
0\le\tau\le c_Km^{-1},
\]

we have

\[
\boxed{|Z(-\tau)|\ge\frac12.}
\]

Because the affine propagator and its inverse are bounded,

\[
\boxed{|ar\Omega(-\tau)|\ge c_K>0}
\]

on the same terminal interval.

More quantitatively one may retain

\[
|ar\Omega(-\tau)|
\ge c_K(1-C_Km\tau)_+.
\]

Thus a terminal order-one Gaussian mean cannot appear in a time much shorter than `m^-1` when the residual source is bounded by `m`.

## 4. Mean vorticity forces global normalized enstrophy occupancy

Let

\[
E_\omega(\tau)=\|\Omega(-\tau)\|_{L^2(\mathbb R^3)}^2.
\]

On the bounded-condition affine/Gaussian branch,

\[
\Sigma(\tau)\asymp_K\tau I,
\]

so

\[
\|\gamma_\tau\|_\infty
\lesssim_K\tau^{-3/2}.
\]

By Cauchy--Schwarz/Jensen,

\[
|\bar\Omega(\tau)|^2
\le
\int\gamma_\tau|\Omega|^2
\le
\|\gamma_\tau\|_\infty E_\omega(\tau).
\]

Therefore

\[
\boxed{
E_\omega(\tau)
\gtrsim_K
\tau^{3/2}|\bar\Omega(\tau)|^2.
}
\]

Using the terminal occupancy interval,

\[
\begin{aligned}
\int_0^{c_K/m}E_\omega(\tau)d\tau
&\gtrsim_K
\int_0^{c_K/m}
\tau^{3/2}(1-C_Km\tau)^2d\tau\\
&=
\boxed{c_Km^{-5/2}}.
\end{aligned}
\]

This is two powers of the natural radius stronger than the residual-gradient-variance lower bound because it charges the order-one Gaussian mean itself, not merely an `O(m)` fluctuation variance.

## 5. Physical kinetic-energy dissipation price

Under terminal first-hitting normalization, normalized and physical enstrophy-time integrals satisfy

\[
\int E_{\omega,\rm phys}(t)dt
=
W^{-1/2}
\int E_\omega(s)ds.
\]

Hence the physical viscous dissipation spent on this terminal mean-vorticity occupancy satisfies

\[
\boxed{
D_{\rm phys}^{\rm mean}
\gtrsim_{K,\nu}
W^{-1/2}m^{-5/2}.
}
\]

For the surviving residual normalization

\[
m=W^{-1/3}\Lambda,
\qquad
\Lambda\to\infty,
\qquad
m\to0,
\]

this becomes

\[
\boxed{
D_{\rm phys}^{\rm mean}
\gtrsim
W^{1/3}\Lambda^{-5/2}.
}
\]

## 6. New survival threshold

Choose a disjoint sequence of adaptive first-hitting steps. Finite total kinetic-energy dissipation implies that the per-step lower bound must tend to zero along every surviving infinite sequence. Therefore

\[
W^{1/3}\Lambda^{-5/2}\to0.
\]

Equivalently,

\[
\boxed{
\frac{\Lambda}{W^{2/15}}\to\infty.
}
\]

Thus every branch with

\[
\Lambda\lesssim W^{2/15}
\]

is excluded asymptotically on the bounded-affine terminal-mean branch.

In particular, the previously identified scalar sharpness family

\[
\Lambda=W^\beta,
\qquad
0<\beta<\frac{2}{15}-2\varepsilon,
\]

cannot survive once the order-one terminal Gaussian mean occupancy is included.

## 7. Natural-radius interpretation

The minimum time needed for an `O(m)` residual source to create terminal order-one mean is

\[
\tau_m\asymp m^{-1}.
\]

The associated Gaussian radius is

\[
\boxed{
R_m=\sqrt{\tau_m}=m^{-1/2}
=W^{1/6}\Lambda^{-1/2}.
}
\]

At the threshold

\[
\Lambda\sim W^{2/15},
\]

this becomes

\[
R_m\sim W^{1/10}.
\]

Thus the exponent `2/15` is not accidental: it is exactly the point at which the mean-vorticity creation radius crosses the previous `W^(1/10)` mesoscopic affine-mean threshold.

The old scalar critical family `m R^2 ~ 1` is precisely this mean-creation radius.

## 8. What remains after the new barrier

A surviving bounded-affine cascade must now satisfy simultaneously

\[
\boxed{
\Lambda\gg W^{2/15},
\qquad
m=W^{-1/3}\Lambda\to0,
}
\]

so its terminal mean-vorticity creation time and radius obey

\[
\tau_m=m^{-1}\ll W^{1/5},
\qquad
R_m\ll W^{1/10}.
\]

Therefore the strict-mesoscopic long-duration mean-generation branch is closed. Any surviving terminal mean creation is forced into a smaller, increasingly high-Reynolds nonlinear region.

This does not by itself exclude

\[
W^{2/15}\ll\Lambda\ll W^{1/3}.
\]

That remaining range corresponds to an even shorter mean-creation time and must be treated by the turnover/high-chaos/projective dynamics rather than another static volume estimate.

Status: **THE PREVIOUS SHARP FAMILY IS REMOVED BY ORDER-ONE MEAN-VORTICITY OCCUPANCY; SURVIVAL NOW REQUIRES `Lambda >> W^(2/15)` AND FORCES MEAN CREATION BELOW THE `W^(1/10)` SCALE / GLOBAL REGULARITY NOT PROVED.**
