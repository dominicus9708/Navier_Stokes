# Exact Gaussian dyadic variance scale partition

Date: 2026-08-16

Status: **EXACT FIXED-TIME POSITIVE SCALE PARTITION / OVERLAPPING-TIME INTEGRATION HAS NO SCALE DOUBLE COUNTING / BRIDGE FROM A POINTWISE CROSSING SEED TO A DYADIC INCREMENT REMAINS CONDITIONAL ON LOW-CURVATURE/SPATIAL OCCUPANCY. GLOBAL REGULARITY NOT PROVED.**

## 1. Gaussian local variance

Let

\[
g_r(x)=(2\pi r^2)^{-3/2}e^{-|x|^2/(2r^2)}
\]

and, for an L2 scalar/vector/matrix field `f`, define the Gaussian local variance

\[
V_f(r,x)
=(g_r*|f|^2)(x)-|(g_r*f)(x)|^2.
\]

Its spatial integral is

\[
\mathcal V_f(r)
:=\int_{\mathbb R^3}V_f(r,x)dx.
\]

Because `g_r` has unit mass,

\[
\int g_r*|f|^2dx=\|f\|_2^2.
\]

With the convention

\[
\widehat g_r(\xi)=e^{-r^2|\xi|^2/2},
\]

Plancherel gives

\[
\|g_r*f\|_2^2
=\int e^{-r^2|\xi|^2}|\widehat f(\xi)|^2d\xi.
\]

Hence

\[
\boxed{
\mathcal V_f(r)
=\int
\left(1-e^{-r^2|\xi|^2}\right)
|\widehat f(\xi)|^2d\xi.
}
\]

Thus the Gaussian variance at scale `r` is a cumulative high-frequency quantity, not a band-local quantity.

## 2. Positive dyadic increment

Define

\[
\Delta\mathcal V_f(r)
:=\mathcal V_f(r)-\mathcal V_f(r/2).
\]

Then

\[
\boxed{
\Delta\mathcal V_f(r)
=
\int
\left(
 e^{-r^2|\xi|^2/4}
-e^{-r^2|\xi|^2}
\right)
|\widehat f(\xi)|^2d\xi
\ge0.
}
\]

The multiplier is concentrated at frequencies `|xi| ~ 1/r`, so this is an exact positive heat-band analogue of a Littlewood--Paley shell.

## 3. Exact telescoping over all dyadic scales

Let

\[
r_k=2^k r_0,
\qquad k\in\mathbb Z.
\]

Because

\[
\mathcal V_f(r)\to0\quad(r\downarrow0),
\]

and, for `f in L2`,

\[
\mathcal V_f(r)\to\|f\|_2^2\quad(r\to\infty),
\]

we obtain

\[
\boxed{
\sum_{k\in\mathbb Z}
\Delta\mathcal V_f(r_k)
=\|f\|_2^2.
}
\]

There is no cross-scale double counting at the increment level.

## 4. Apply to the DSD residual descriptor

For incompressible velocity `u`, let

\[
S=\operatorname{sym}\nabla u,
\qquad
\omega=\nabla\times u.
\]

Define the spatially integrated Gaussian residual descriptor

\[
\mathcal B(r)
=
\mathcal V_S(r)
+\frac12\mathcal V_\omega(r).
\]

Its dyadic increment is

\[
\Delta\mathcal B(r)
=
\Delta\mathcal V_S(r)
+\frac12\Delta\mathcal V_\omega(r)
\ge0.
\]

For divergence-free whole-space fields,

\[
\|S\|_2^2=\frac12\|\omega\|_2^2.
\]

Therefore, writing

\[
E(t)=\|\omega(t)\|_2^2,
\]

we get the exact identity

\[
\boxed{
\sum_{k\in\mathbb Z}
\Delta\mathcal B(r_k,t)
=E(t).
}
\]

Equivalently, whenever `E(t)>0`,

\[
\boxed{
\sum_k
\frac{\Delta\mathcal B(r_k,t)}{E(t)}
=1.
}
\]

Thus the normalized dyadic residual increments form an exact probability distribution over Gaussian scales at each fixed time.

## 5. Spacetime packing with arbitrary temporal overlap

Because all terms are nonnegative, Tonelli gives for every time interval `I`

\[
\boxed{
\sum_k
\int_I\Delta\mathcal B(r_k,t)dt
=
\int_I E(t)dt.
}
\]

Likewise

\[
\boxed{
\sum_k
\int_I
\frac{\Delta\mathcal B(r_k,t)}{E(t)}dt
=|I|
}
\]

on the set where `E>0`.

Therefore nested or overlapping time intervals do not create a scale-overlap problem once the residual is represented by positive dyadic Gaussian increments.

This is stronger and cleaner than summing the cumulative variances `B(r)` themselves, which would double count the same high-frequency content at every coarser scale.

## 6. Why this is relevant to the renormalization loop

The current frontier permits repeated critical crossings at smaller physical scales. A fixed physical high-frequency packet can contribute to the cumulative variance `B(r)` at many coarser Gaussian scales, so episodewise sums of `B(r)` are not legitimate.

The present identity says that genuinely new scale-local fluctuation must appear in the increments

\[
\Delta\mathcal B(r_k).
\]

Hence a repeated residual-seed branch can reuse the same fluctuation across nested episodes only if that seed is carried by frequencies far above the current core scale. Such a frequency mismatch is exactly the existing high-frequency / derivative escape.

On the complementary bounded-derivative, low-curvature branch, a fixed fraction of any source-active residual seed should lie in a bounded number of dyadic increments near the core scale. Then the exact partition provides the desired scale orthogonality.

## 7. Remaining local bridge

The exact identity is global in the Gaussian center `x`, whereas the dangerous crossing is tracked at one adaptive center.

To turn a pointwise/local seed

\[
B(r,x_*)
\]

into a lower bound for

\[
\Delta\mathcal B(r)
\]

one still needs a local occupancy statement. The existing proof tree already supplies the correct dichotomy:

1. **low-curvature / spatially persistent seed:** comparable residual variance occupies a core-sized set of centers, producing a global band increment;
2. **failure of spatial persistence:** the seed has large spatial derivative/high Hermite curvature and returns to the derivative branch.

Thus the missing part is not scale orthogonality itself; the exact scale partition is now available. The live issue is quantitative localization of each source-active crossing into one or finitely many dyadic increments.

Status: **EXACT POSITIVE GAUSSIAN SCALE PARTITION DERIVED / SCALE DOUBLE COUNTING REMOVED AT THE INCREMENT LEVEL / POINTWISE-TO-BAND OCCUPANCY BRIDGE REMAINS TO BE QUANTIFIED / GLOBAL REGULARITY NOT PROVED.**
