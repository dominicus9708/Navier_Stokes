# Sharpened Compatible Projective-Speed Ceiling — 2026-08-21

Status: **SMOOTH PURE-P_V SPEED BOUND SHARPENED BY AVOIDING INCOMPATIBLE EXTREMA / GLOBAL REGULARITY NOT PROVED.**

The previous explicit projective-speed estimate bounded `lambda=P/E` by using a lower bound on `E`, and then multiplied that upper bound by an independent upper bound on `E`. Those two extrema cannot generally occur simultaneously. This note keeps the common enstrophy variable until the end.

## 1. Start from the exact Sobolev projective ceiling

For

\[
\mathcal V
=P_{st}\left(\frac13\Sigma^2+\frac14\Omega\otimes\Omega\right),
\]

we already have

\[
\frac{\|\mathcal V\|_2}{\|\Sigma\|_2}
\le
\frac13S_3^{-3/4}\lambda^{3/4}E^{1/2}
+\frac{\sqrt2}{4},
\]

where

\[
S_3=3\left(\frac\pi2\right)^{4/3},
\qquad
E=\|\Sigma\|_2^2,
\qquad
\lambda=P/E.
\]

Using the derivative isometries

\[
Z:=\|\Omega\|_2^2=2E,
\qquad
Q:=\|\nabla\Omega\|_2^2=2P,
\]

we obtain the exact algebraic rewrite

\[
\boxed{
\lambda^{3/4}E^{1/2}
=2^{-1/2}Q^{3/4}Z^{-1/4}.
}
\]

This form is the correct one for combining first-hitting derivative tightness with the record-point mass floor.

## 2. Compatible upper bound on Q

If the derivative mass is `epsilon_Q`-tight in `B_{R_Q}` and

\[
K_1=\|\nabla\Omega\|_\infty,
\]

then

\[
(1-\varepsilon_Q)Q
\le
\int_{B_{R_Q}}|\nabla\Omega|^2
\le
\frac{4\pi}{3}K_1^2R_Q^3.
\]

Hence

\[
\boxed{
Q
\le
\frac{4\pi}{3(1-\varepsilon_Q)}K_1^2R_Q^3.
}
\]

## 3. Compatible lower bound on Z

At a first-hitting record point `y_*`, choose

\[
\xi=\Omega(y_*),\qquad |\xi|=1.
\]

For

\[
g(y)=\xi\cdot\Omega(y),
\]

we have

\[
g(y_*)=1,
\qquad
\nabla g(y_*)=0.
\]

If

\[
K_2=\sup_{x,|v|=1}|(v\cdot\nabla)^2\Omega(x)|,
\]

then

\[
g(y_*+h)\ge1-\frac12K_2|h|^2.
\]

Integrating the positive Taylor envelope yields the previously derived sharp record-mass floor

\[
\boxed{
Z
\ge
C_ZK_2^{-3/2},
\qquad
C_Z=\frac{64\sqrt2\pi}{105}
\approx2.70804293.
}
\]

## 4. Compatible projective-speed bound

Insert the Q upper bound and Z lower bound directly into

\[
2^{-1/2}Q^{3/4}Z^{-1/4}.
\]

This gives

\[
\boxed{
C_{V,+}
\le
\frac{\sqrt2}{4}
+C_*K_1^{3/2}K_2^{3/8}
R_Q^{9/4}
(1-\varepsilon_Q)^{-3/4},
}
\]

where

\[
C_*
=
\frac13S_3^{-3/4}2^{-1/2}
\left(\frac{4\pi}{3}\right)^{3/4}
C_Z^{-1/4}.
\]

For the `M0=2` analytic endpoint bounds

\[
K_1\le\frac{2}{\rho_0},
\qquad
K_2\le\frac{4}{\rho_0^2},
\]

and

\[
r_Q=R_Q/\rho_0,
\]

we obtain

\[
\boxed{
C_{V,+}(r_Q,\varepsilon_Q)
\le
0.3535533906
+0.7146986969\,
(1-\varepsilon_Q)^{-3/4}
 r_Q^{9/4}.
}
\]

This replaces the older loose common-radius benchmark

\[
0.3535533906+2.5141113904r^{15/4}.
\]

The improvement is structural, not merely numerical: the vorticity-mass radius `R_Z` drops out of the projective-speed ceiling because the same `Z` cannot be simultaneously minimized in `lambda` and maximized in `E`.

## 5. Updated pure-corridor anti-ribbon closure

Use the rigorously audited moving-ball pure-corridor bound

\[
\frac{\Pi_B}{c_*(2)^2}
\le1.4967761748.
\]

For a common radius `r=R_C/rho0` with `R_Q<=R_C`, survival of the transverse anti-ribbon swap requires

\[
\frac{\Pi_B}{c_*(2)^2}
\ge
T_{swap}^{new}(r)
:=
\frac{2\pi}
{r^2[1+2C_{V,+}^{new}(r)]}.
\]

### Zero derivative tail

For `epsilon_Q=0`, the equality

\[
T_{swap}^{new}(r)=1.4967761748
\]

occurs at

\[
\boxed{r_{swap,new}^{(0)}\approx1.09908244.}
\]

Thus the zero-tail pure low-turnover positive-middle anti-ribbon lane is S-closed throughout

\[
\boxed{r<1.09908244.}
\]

This includes the already-closed frequency-floor region below `0.53193814` and strictly enlarges the direct swap closure interval.

### Quarter derivative tail

For

\[
\varepsilon_Q\le\frac14,
\]

we have

\[
(1-\varepsilon_Q)^{-3/4}\le(3/4)^{-3/4}.
\]

The same equality occurs at

\[
\boxed{r_{swap,new}^{(1/4)}\approx1.06060560.}
\]

Hence under the quarter-tail pure corridor,

\[
\boxed{r<1.06060560
\quad\Longrightarrow\quad
\text{pure positive-middle anti-ribbon stage is S-closed}.}
\]

If `epsilon_Q>1/4`, the branch is already derivative-spatial non-tight and exits the pure P_V lane.

## 6. Near-threshold saturation requirement

For radii just above the new closure threshold, survival requires the actual projective speed to be close to its compatible upper ceiling.

Indeed

\[
C_V
\ge
C_{req}(r)
:=
\frac{\pi c_*(2)^2}{\Pi_Br^2}-\frac12.
\]

Since `c_*(2)>=1` and `Pi_B<=1.4967761748`,

\[
\boxed{
C_V
\ge
\frac{\pi}{1.4967761748\,r^2}-\frac12.
}
\]

Thus immediately above `r_swap,new`, the compatible Q-upper / Z-lower bounds must themselves be nearly saturated. This will be the next rigidity input.

Status: **REMOVING THE INCOMPATIBLE E/LAMBDA EXTREMA IMPROVES THE ROBUST QUARTER-TAIL PURE-P_V S-CLOSURE RADIUS FROM ABOUT `0.856 rho0` TO ABOUT `1.061 rho0`, AND THE ZERO-TAIL RADIUS TO ABOUT `1.099 rho0`. THE REMAINING PURE SURVIVOR MUST NOW BE LARGER THAN THE ANALYTIC STRIP SCALE OR SATURATE THE DERIVATIVE-TIGHTNESS / RECORD-MASS BOUNDS NEAR THE THRESHOLD.**