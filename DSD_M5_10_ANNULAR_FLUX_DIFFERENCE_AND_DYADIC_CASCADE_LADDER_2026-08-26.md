# DSD M5-10 — Annular flux difference and dyadic cascade ladder

Date: 2026-08-26

Status: **EXACT ANNULAR ENERGY-FLUX LEDGER + SCALING AUDIT / REMOVES DOUBLE-COUNTING OF NESTED FLUX / SHOWS A DYADIC CRITICAL CASCADE CAN FIT IN FINITE TIME AND FINITE ENERGY / DOES NOT CLOSE M5.**

## 1. Total energy current

For a smooth Navier--Stokes solution define

\[
e=\frac{|u|^2}{2},
\qquad
J_E=(e+p)u-\nu\nabla e.
\]

The local energy equality is

\[
\partial_t e+\nabla\cdot J_E=-\nu|\nabla u|^2.
\]

For the annulus

\[
A(r,2r)=\{x:r<|x-X_*|<2r\},
\]

define

\[
E_A(r,t)=\int_{A(r,2r)}e\,dx
\]

and the outward flux

\[
\mathcal J_E(r,t)
=\int_{S_r(X_*)}J_E\cdot n\,dS.
\]

Then

\[
\boxed{
\frac{d}{dt}E_A(r,t)
+\nu\int_{A(r,2r)}|\nabla u|^2dx
=
\mathcal J_E(r,t)-\mathcal J_E(2r,t).
}
\]

This is the correct nested-shell ledger: energy crossing several radii is not counted as a new independent source at every radius.

The pressure-gauge constant drops out of each spherical flux because `int_{S_r} u·n dS=0`.

## 2. Critical `1/r` scaling

For the surviving dimensional model

\[
|u|\sim r^{-1},
\]

one has on one dyadic annulus

\[
E_A(r)\sim r,
\]

\[
\int_A|\nabla u|^2dx\sim r^{-1},
\]

and

\[
\mathcal J_E(r)\sim r^{-1}.
\]

The natural parabolic lifetime is

\[
\Delta t_r\sim r^2.
\]

Therefore storage change, integrated viscous loss and integrated flux difference over one natural scale-time all have the same size:

\[
\boxed{
E_A
\sim
r^2 D_A
\sim
r^2\mathcal J_E
\sim
O(r).
}
\]

Thus the exact flux-difference ledger is scale-consistent with the critical survivor.

## 3. Finite total physical cost

For dyadic radii

\[
r_j=2^{-j}r_0,
\]

the per-scale physical energy/loss size is `O(r_j)`. Hence

\[
\boxed{
\sum_{j=0}^\infty r_j<\infty.
}
\]

Removing the double-counting of nested flux does not create an infinite physical-energy or ordinary-dissipation contradiction.

## 4. Dyadic time ladder

Suppose creation/adjustment at scale `r_j` takes a natural parabolic time

\[
\Delta t_j=c\,r_j^2.
\]

Then all smaller-scale formation times satisfy

\[
\sum_{k>j}\Delta t_k
=
c r_j^2\sum_{m=1}^\infty4^{-m}
=
\boxed{\frac c3 r_j^2}.
\]

Thus the entire infinite tail of smaller scales fits inside a time interval comparable to the natural lifetime of the parent scale.

This means ordinary parabolic persistence is fully compatible with a late-time snapshot in which many dyadic critical shells coexist:

\[
\boxed{
\text{outer scale persists}
\quad\text{while}\quad
\text{all smaller scales are formed successively}.
}
\]

A simultaneous cross-radius corridor does not require independent long lifetimes for all of its shells.

## 5. DSD interpretation

The cross-radius family can be formed as a nested lineage rather than as independent parallel objects.

Therefore two false counting rules are excluded:

1. counting the same radial energy current as new energy at every shell;
2. adding one full independent persistence interval for every visible shell.

The correct structure is a **dyadic cascade ladder** with geometrically decreasing stored energy and geometrically decreasing formation times.

## 6. Why this does not prove existence

This calculation is a compatibility/scaling audit, not a construction of a singular Navier--Stokes solution. It shows only that finite total energy, finite total ordinary dissipation, nested local-energy conservation and parabolic timing do not by themselves contradict the cross-radius W1 survivor.

A real M5 closure must exploit information not contained in these bookkeeping facts, such as a vector-geometric obstruction, a critical compactness theorem, or a dynamic loss mechanism stronger than scale-invariant cascade transport.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
