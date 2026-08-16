# Local Gaussian seed -> dyadic band increment or palinstrophy

Date: 2026-08-16

Status: **DERIVED POINTWISE-TO-GLOBAL SCALE BRIDGE. A LOCAL GAUSSIAN RESIDUAL SEED AUTOMATICALLY OCCUPIES A PARENT-SCALE BALL; THE RESULTING GLOBAL CUMULATIVE VARIANCE IS EITHER CARRIED BY A DYADIC GAUSSIAN BAND INCREMENT OR BY PALINSTROPHY/HIGH-FREQUENCY CONTENT. GLOBAL REGULARITY NOT PROVED.**

## 1. Pair representation of Gaussian variance

For

\[
V_f(r,x)
=(g_r*|f|^2)(x)-|(g_r*f)(x)|^2,
\]

one has the exact identity

\[
\boxed{
V_f(r,x)
=
\frac12
\iint
 g_r(x-y)g_r(x-z)
 |f(y)-f(z)|^2\,dy\,dz.
}
\]

This removes the local mean from all localization comparisons.

## 2. Parent Gaussian dominates a shifted child Gaussian

Fix `x_*` and suppose

\[
|x-x_*|\le r.
\]

A direct Gaussian comparison gives

\[
\boxed{
g_{2r}(x-y)\ge c_0 g_r(x_*-y)}
\]

for all `y`, with an absolute `c_0>0`.

Indeed, writing `z=x_*-y` and `h=x-x_*`,

\[
\frac{g_{2r}(x-y)}{g_r(x_*-y)}
=
\frac18
\exp\left[
\frac{4|z|^2-|z+h|^2}{8r^2}
\right],
\]

and

\[
4|z|^2-|z+h|^2
=3|z|^2-2z\cdot h-|h|^2
\ge-\frac43|h|^2.
\]

Thus for `|h|<=r` the ratio is bounded below by a universal constant.

Applying the comparison to both kernels in the pair formula yields

\[
\boxed{
V_f(2r,x)
\ge c_0^2 V_f(r,x_*)
\qquad(|x-x_*|\le r).
}
\]

Hence a pointwise child-scale variance cannot be supported at only one center: it automatically creates parent-scale occupancy on a ball of volume comparable to `r^3`.

Integrating over that ball,

\[
\boxed{
\mathcal V_f(2r)
:=\int V_f(2r,x)dx
\ge c r^3 V_f(r,x_*).
}
\]

## 3. Cumulative variance versus one dyadic increment

From the exact Gaussian dyadic partition, for a fixed `M>1` one may split the Fourier representation of `\mathcal V_f(2r)` into

\[
|\xi|\le M/r
\quad\text{and}\quad
|\xi|>M/r.
\]

On the compact multiplier region `|xi|<=M/r`, the parent dyadic increment multiplier

\[
e^{-r^2|\xi|^2}-e^{-4r^2|\xi|^2}
\]

is bounded below, up to a constant depending only on `M`, by the cumulative multiplier

\[
1-e^{-4r^2|\xi|^2}.
\]

On the high-frequency region,

\[
\int_{|\xi|>M/r}|\widehat f(\xi)|^2d\xi
\le
\frac{r^2}{M^2}
\|\nabla f\|_2^2.
\]

Therefore

\[
\boxed{
\mathcal V_f(2r)
\le
C_M\Delta\mathcal V_f(4r)
+C\frac{r^2}{M^2}\|\nabla f\|_2^2.
}
\]

For any fixed convenient `M`, constants can be absorbed and we may write schematically

\[
\boxed{
\mathcal V_f(2r)
\lesssim
\Delta\mathcal V_f(4r)
+r^2\|\nabla f\|_2^2.
}
\]

## 4. Apply to strain + vorticity DSD residual

Let

\[
B_r(x)
=V_S(r,x)+\frac12V_\omega(r,x).
\]

Let

\[
\Delta\mathcal B(4r)
=
\Delta\mathcal V_S(4r)
+\frac12\Delta\mathcal V_\omega(4r).
\]

Because `S` is a zero-order singular integral of `omega`,

\[
\|\nabla S\|_2
\lesssim\|\nabla\omega\|_2.
\]

Writing

\[
P=\|\nabla\omega\|_2^2,
\]

Sections 2 and 3 combine to give

\[
\boxed{
 r^3 B_r(x_*)
\lesssim
\Delta\mathcal B(4r)
+r^2P.
}
\]

This is the desired local-to-scale bridge.

## 5. Spacetime form

For an episode whose Gaussian radius remains comparable to `r` on a time interval `I`, the same estimate holds at every time for the moving adaptive center `x_*(t)`:

\[
\boxed{
 r^3\int_I B_r(x_*(t),t)dt
\lesssim
\int_I\Delta\mathcal B(4r,t)dt
+r^2\int_I P(t)dt.
}
\]

No assumption that different episode intervals are disjoint is needed.

## 6. Consequence for nested critical crossings

The recent-source frontier gives a residual-seed branch with a positive lower bound on

\[
\int_I B_r(x_*(t),t)dt.
\]

The present bridge says that such a seed must be realized as

\[
\boxed{
\text{new scale-local Gaussian band action}
\quad\lor\quad
\text{palinstrophy/high-derivative action}.
}
\]

If one selects a subsequence of physical core radii separated by a fixed dyadic factor, the `Delta B` terms belong to distinct positive Gaussian bands. By the exact scale partition,

\[
\sum_k\int\Delta\mathcal B(r_k,t)dt
\le
\int E(t)dt.
\]

Thus temporal nesting can no longer make the **same residual fluctuation** pay for infinitely many separated scales.

The only way to reuse cumulative residual variance without occupying new dyadic increments is to push it far above the current Gaussian frequency, and the `r^2 P` term records exactly that derivative escape.

## 7. Claim boundary

This closes the pointwise-to-band localization gap for the residual seed at the level of a band-or-palinstrophy dichotomy.

It does not yet prove global regularity because the physical lower cost assigned to each new band can decrease rapidly with the core scale and can remain summable on a super-separated cascade.

Consequently the residual branch is now scale-orthogonal, but the separate symmetric affine/productive-strain branch can still migrate to higher physical frequencies while paying summable energy costs.

Status: **POINTWISE RESIDUAL SEED -> POSITIVE DYADIC BAND OR PALINSTROPHY / RESIDUAL SCALE REUSE CLOSED / REMAINING NONREPEATABILITY WALL SHIFTS TO THE MIGRATING SYMMETRIC-STRAIN AMPLIFIER.**
