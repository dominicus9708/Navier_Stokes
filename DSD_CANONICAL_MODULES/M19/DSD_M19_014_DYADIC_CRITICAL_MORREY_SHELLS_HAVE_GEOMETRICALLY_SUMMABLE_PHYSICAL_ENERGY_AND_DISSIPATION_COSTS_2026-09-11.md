# M19-014 — Dyadic critical Morrey shells have geometrically summable physical energy and dissipation costs

**Date:** 2026-09-11  
**Status:** CALCULATION / R-CRITICAL ENERGY ECONOMICS / SUMMABILITY FIREWALL / RIGIDITY REQUIREMENT

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Purpose

M19-013 rewrites the critical \(1/R\) normalized velocity tail as the parent-scale Morrey condition

\[
\mathcal A_u(x,r,t)
:=
\frac1r
\int_{r<|z-x|<2r}|u(z,t)|^2dz
\gtrsim1.
\]

The next question is whether infinitely many such shells contradict finite physical kinetic energy.

They do not.

The shell cost is proportional to \(r\), so geometrically nested critical shells have a geometrically summable physical-energy cost.

The same phenomenon occurs for a scale-invariant parabolic dissipation event.

Thus R-critical cannot be closed by simply summing standard energy or standard dissipation across geometric scales.

## 2. One critical shell

Assume

\[
\boxed{
\mathcal A_u(x_*,r,t)
\ge a_*>0.
}
\]

Then by definition

\[
\boxed{
\int_{r<|x-x_*|<2r}|u(x,t)|^2dx
\ge
a_*r.
}
\]

The scale-invariant Morrey payment \(a_*\) therefore corresponds to physical kinetic energy of size \(r\).

## 3. Geometrically nested disjoint shells

Let

\[
r_n=2^{-n}r_0.
\]

Use disjoint annuli, for example

\[
A_n
:=
\{r_n<|x-x_*|<2r_n\}.
\]

After choosing every other dyadic index if necessary to avoid boundary overlap, the shells are pairwise disjoint.

If

\[
\mathcal A_u(x_*,r_n,t)
\ge a_*
\]

for all selected \(n\), then

\[
\int_{A_n}|u|^2dx
\ge
a_*r_n.
\]

Summing,

\[
\sum_n\int_{A_n}|u|^2dx
\ge
a_*\sum_nr_n.
\]

But

\[
\sum_nr_n
=r_0\sum_n2^{-n}
<\infty.
\]

Hence the required total physical energy is finite:

\[
\boxed{
\sum_n a_*r_n
<\infty.
}
\]

Therefore an infinite nested family of order-one critical Morrey shells is compatible with finite kinetic energy.

## 4. This is not a double-counting issue

The shells above can be chosen spatially disjoint.

Thus the failure is not caused by rerecording the same region repeatedly.

Even genuinely disjoint critical shells have summable physical costs because the shell energy itself shrinks linearly with the shell radius.

This is a true homogeneity obstruction.

## 5. Ball version

If instead

\[
\frac1r\int_{B_r(x_*)}|u|^2dx
\ge m_*>0
\]

at every dyadic radius, the ball energies are nested and therefore cannot be summed directly.

Passing to annular differences either yields a subsequence of annuli with comparable critical mass or shows that the energy is concentrated more strongly toward the center.

Neither alternative gives an immediate finite-energy contradiction.

The annular formulation is therefore the cleaner additive representation of the critical tail.

## 6. Model critical profile

A magnitude profile

\[
|u(x)|\sim\frac{c}{|x|}
\]

has

\[
\int_{r<|x|<2r}|u|^2dx
\sim Cc^2r.
\]

Thus

\[
\mathcal A_u(r)\sim Cc^2
\]

uniformly across scales, while

\[
\int_{|x|<r_0}|u|^2dx
\sim Cc^2r_0<\infty.
\]

This is the exact model behind the summability calculation.

No claim is made that this scalar magnitude model is itself an exact Navier--Stokes solution.

## 7. Parabolic dissipation has the same physical scaling

Consider the scale-invariant local dissipation quantity

\[
\boxed{
\mathcal D_u(x_*,r,t_*)
:=
\frac1r
\int_{t_*-r^2}^{t_*}
\int_{B_r(x_*)}|\nabla u|^2dxdt.
}
\]

If

\[
\mathcal D_u\ge d_*>0,
\]

then the physical spacetime dissipation in that cylinder is at least

\[
\boxed{
\int_{Q_r}|\nabla u|^2
\ge d_*r.
}
\]

Again the physical cost is proportional to \(r\).

For geometrically shrinking disjoint/bounded-overlap parabolic cells,

\[
\sum_nd_*r_n<\infty.
\]

Thus the finite global kinetic-energy dissipation identity is also compatible with recurrent order-one scale-invariant dissipation on a geometric scale ladder.

## 8. Relation to the R-AC firewall

The same general mechanism appears in R-AC:

\[
\boxed{
\text{order-one normalized critical payment}
\quad\mapsto\quad
\text{geometrically shrinking physical cost}.
}
\]

For R-critical the relevant homogeneity is visible directly in space:

\[
E(A_r)\sim r.
\]

Therefore simply finding more disjoint scales does not solve the root.

## 9. What would be needed instead

A successful R-critical closure must use something stronger than the total finite energy/dissipation budget, for example:

1. rigidity of an ancient profile with persistent critical Morrey tail;
2. exclusion of the corresponding low-frequency \(\dot H^{-1}\) structure;
3. a monotonicity or unique-continuation mechanism coupling different scales;
4. a stress/flux identity whose critical tail coefficient cannot persist without an external source;
5. a stronger integrability/tightness theorem that improves \(1/R\) decay.

This module does not assert that any of these is presently available.

## 10. Exact critical economics

The useful summary is

\[
\boxed{
\mathcal A_u(r)\sim1
\quad\Longleftrightarrow\quad
E(A_r)\sim r.
}
\]

and

\[
\boxed{
\mathcal D_u(r)\sim1
\quad\Longleftrightarrow\quad
D(Q_r)\sim r.
}
\]

Since

\[
\sum_nr_n<\infty,
\]

both standard parent budgets are too weak to exclude a geometric critical cascade.

## 11. Next calculation

The next highest-value calculation is to identify what the critical Morrey tail means spectrally.

The normalized identity

\[
\|U\|_2^2
=\|\Omega\|_{\dot H^{-1}}^2
\]

shows that kinetic tail energy is a negative-order vorticity resource.

M19-015 should separate:

\[
\boxed{
\text{large-radius critical tail}
\to
\text{infrared }\dot H^{-1}\text{ mass}
\lor
\text{high-frequency/oscillatory tail}.
}
\]

The second alternative should be compared with the already typed high-remote-frequency / remote-satellite root.

---

\[
\boxed{\text{M19-014 COMPLETE; STANDARD ENERGY AND DISSIPATION DO NOT CLOSE R-CRITICAL.}}
\]
