# Affine-subtracted low-to-high reproduction locality

Date: 2026-08-19

Status: **SCALE-LOCALITY ESTIMATE FOR THE REMAINING CRITICAL PACKET GENEALOGY. AFTER REMOVING TRANSLATION AND ACCOUNTING FOR THE LOW-BAND AFFINE STRAIN, DISTANT LOWER-FREQUENCY ANCESTORS COUPLE TO A HIGH-FREQUENCY NATURAL CELL WITH GEOMETRIC POWERS OF L/K. GLOBAL REGULARITY NOT PROVED.**

## 1. Critical packet scaling

Let a lower-frequency packet have characteristic frequency `L` and a target child packet have frequency `K`, with

\[
L\ll K.
\]

For a natural critical packet,

\[
|u_L|\sim L,
\qquad
|\nabla u_L|\sim L^2,
\qquad
|\nabla^2u_L|\sim L^3,
\]

while for the target packet

\[
|u_K|\sim K,
\qquad
|\omega_K|\sim K^2,
\qquad
|S_K|\sim K^2.
\]

The natural target vorticity-production scale is

\[
|S_K\omega_K|\sim K^4.
\]

## 2. Remove translation

On the target spatial cell of radius `K^-1`, expand the low field around the moving center `x_*`:

\[
u_L(x)
=u_L(x_*)
+A_L(x-x_*)
+r_L(x),
\qquad
A_L=\nabla u_L(x_*).
\]

The constant translation is removed by the moving/Galilean frame and cannot amplify vorticity.

## 3. Low affine strain is quadratically suppressed

The low affine strain satisfies

\[
|S_L|\lesssim L^2.
\]

Its direct stretching of the target vorticity is

\[
|S_L\omega_K|
\lesssim
L^2K^2.
\]

Relative to the target natural source scale `K^4`,

\[
\boxed{
\frac{|S_L\omega_K|}{K^4}
\lesssim
\left(\frac LK\right)^2.
}
\]

Thus a critical lower-frequency parent many octaves below `K` cannot supply an order-one fraction of the target stretching unless its amplitude exceeds the natural critical packet scaling, which is already a stronger-amplitude/common-strain branch.

## 4. Low residual after affine subtraction is cubically suppressed

Taylor's theorem on the `K^-1` cell gives

\[
|\nabla r_L|
\lesssim
K^{-1}\|\nabla^2u_L\|_\infty
\lesssim
\frac{L^3}{K}.
\]

Therefore residual low-band strain acting on `omega_K` has size

\[
\lesssim
\frac{L^3}{K}K^2
=L^3K.
\]

Relative to `K^4`,

\[
\boxed{
\frac{|\nabla r_L|\,|\omega_K|}{K^4}
\lesssim
\left(\frac LK\right)^3.
}
\]

The reverse high-low derivative coupling has the same or better scale separation when measured against the target `K^4` vorticity-production scale.

## 5. Dyadic ancestor sum

For dyadic ancestors

\[
L_m=2^{-m}K,
\]

the affine stretching fractions satisfy

\[
\sum_{m\ge1}
\left(\frac{L_m}{K}\right)^2
=\sum_{m\ge1}4^{-m}<\infty,
\]

and the affine-subtracted residual fractions satisfy the still smaller sum

\[
\sum_{m\ge1}8^{-m}<\infty.
\]

Consequently, if a fixed fraction of target source is assigned to lower-frequency ancestors obeying the natural packet amplitude bounds, then a fixed fraction must already come from a bounded octave neighborhood of `K`.

Schematically,

\[
\boxed{
\text{order-one child source}
\Longrightarrow
\text{parent/partner frequency }L\gtrsim cK
}
\]

unless one enters a stronger-amplitude affine strain or nonlocal concentration branch already priced elsewhere.

## 6. Genealogy consequence

The final critical radial stack is therefore a finite-range reproduction chain in log-frequency.  Very old low-frequency ancestors may persist in the critical norm, but they cannot directly perform the order-one stretching needed to create an arbitrarily higher natural child.

Hence the remaining dynamical wall is specifically

\[
\boxed{
\text{adjacent/finite-octave heterochiral, radially transferring,
shape-modulated reproduction.}
}
\]

This makes the relation to renormalized Type-I/ancient dynamics more precise: each `O(1)` interval in logarithmic frequency must contain genuine new local nonlinear organization rather than reusing a remote ancestor field.

## 7. Limitation

The estimate gives scale locality but not contraction.  Adjacent critical packets have `L/K=O(1)`, so their nonlinear coupling remains order one and can in principle balance viscosity.  This is exactly the remaining unit-cell critical wall.

Status: **REMOTE-ANCESTOR DIRECT REPRODUCTION REMOVED / FINAL STACK IS FINITE-RANGE IN LOG-FREQUENCY / ADJACENT CRITICAL REPRODUCTION REMAINS.**