# DSD M17-287 — An ancient spectral core requires R^7 backward derivative feed or explicit spatial-infinity boundary input

Date: 2026-09-06  
Canonical ID: **M17-287**

Status: **ANCIENT DERIVATIVE-FEED GATE / A SCALE-COMPARABLE RAW HEAT TANGENT RETAINS NONZERO TIME-ZERO LAPLACIAN CHARGE ON A FIXED CORE. MOVING TWO SPATIAL DERIVATIVES FROM THE PRESENT FIELD TO THE BACKWARD HEAT KERNEL GIVES THE SCALING `||Delta p_T||_2 ~ T^(-7/4)` IN THREE DIMENSIONS. HENCE, WHEN THE CUTOFF REPRESENTATION HAS NO NONVANISHING BOUNDARY TERM AT SPATIAL INFINITY, A FIXED NONZERO PRESENT `Delta V` REQUIRES BACKWARD L2 MASS AT LEAST `T^(7/2)` IN SQUARED NORM. WITH DIFFUSION RADIUS `R~sqrt(T)`, THIS IS THE CRITICAL GROWTH `M(R)>=c R^7`. IF THE CUTOFF BOUNDARY TERMS DO NOT VANISH, THAT FAILURE IS ITSELF AN EXPLICIT SPATIAL-INFINITY FEED. THUS AN UNBOUNDED NODAL SURVIVOR CANNOT BE SUPPORTED BY MERE VOLUME-SCALE `R^3` MASS; IT REQUIRES R^7-TYPE DERIVATIVE FEED OR A STRONGER FAR-FIELD INPUT. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Retained raw Laplacian charge

On the scale-comparable compact root packet, after normalization there is a fixed core `B_0` such that

\[
\boxed{
\int_{B_0}|\Delta V(z,0)|^2dz\ge h_0>0.
}
\]

Since `B_0` has fixed finite volume, there exists a point

\[
z_*\in B_0
\]

with

\[
\boxed{|\Delta V(z_*,0)|\ge c_0>0.}
\]

The tangent is caloric:

\[
\partial_\tau V=\Delta V.
\]

---

## 2. Cutoff backward representation

Fix `T>0` and a large cutoff radius `R`.

Let `chi_R` equal one on `B_R` and vanish outside `B_{2R}`.
Apply the adjoint heat-kernel identity between times `-T` and `0` to `chi_R V` and move the two spatial derivatives defining `Delta V(z_*,0)` onto the heat kernel.

Schematically,

\[
\boxed{
\Delta V(z_*,0)
=
\int_{\mathbb R^3}\Delta p_T(z_*-y)\chi_R(y)V(y,-T)dy
+\mathcal B_{R,T},
}
\]

where `B_{R,T}` is supported in the cutoff annulus and consists of the standard commutator/boundary terms involving `grad chi_R`, `Delta chi_R`, the heat kernel, and `V`/`grad V` over the intermediate spacetime cylinder.

This form keeps the spatial-infinity assumption explicit.

---

## 3. Infinity-boundary split

There are two cases.

### Case A — nonvanishing far-boundary input

If for some fixed `T`

\[
\limsup_{R\to\infty}|\mathcal B_{R,T}|>0,
\]

retain

\[
\boxed{G_{explicit\ spatial\text{-}infinity\ boundary\ feed}.}
\]

This is already the desired classification: the present spectral core is being maintained by information entering from arbitrarily large tangent radius.

### Case B — boundary term vanishes

If

\[
\mathcal B_{R,T}\to0,
\]

then the global backward representation is legitimate in the relevant weighted class:

\[
\boxed{
\Delta V(z_*,0)
=
\int\Delta p_T(z_*-y)V(y,-T)dy.
}
\]

---

## 4. Three-dimensional kernel scaling

The heat kernel is

\[
p_T(x)=(4\pi T)^{-3/2}e^{-|x|^2/(4T)}.
\]

Two derivatives add one factor `T^-1`, while the `L2` norm of the heat kernel scales as `T^-3/4`.

Therefore

\[
\boxed{
\|\Delta p_T\|_{L^2(\mathbb R^3)}
=C_\Delta T^{-7/4}.
}
\]

If `V(-T)` is global `L2`, Cauchy--Schwarz gives

\[
c_0
\le
C_\Delta T^{-7/4}\|V(-T)\|_2.
\]

Hence

\[
\boxed{
\|V(-T)\|_2
\ge c T^{7/4},
}
\]

or in mass form

\[
\boxed{
\|V(-T)\|_2^2
\ge c T^{7/2}.
}
\]

M17-284 already says global `L2` boundedness is impossible; M17-287 quantifies how quickly a finite global norm would have to grow backward.

---

## 5. Gaussian-weighted version

If the global `L2` norm is infinite but the heat-kernel pairing is finite, use a Gaussian weight on the diffusion scale.

For a fixed small constant `c_g>0`, define

\[
\boxed{
\mathcal M_G(T)
:=
\int_{\mathbb R^3}
 e^{-c_g|y-z_*|^2/T}
 |V(y,-T)|^2dy.
}
\]

Weighted Cauchy--Schwarz with the Gaussian decay of `Delta p_T` gives

\[
\boxed{
|\Delta V(z_*,0)|
\le C T^{-7/4}\mathcal M_G(T)^{1/2}.
}
\]

Therefore

\[
\boxed{
\mathcal M_G(T)\ge c T^{7/2}.
}
\]

If even this Gaussian-weighted quantity is infinite, retain the stronger exit

\[
\boxed{G_{super\text{-}Gaussian\ spatial\ mass\ feed}.}
\]

---

## 6. Diffusion-radius form

Set

\[
R:=\sqrt T.
\]

Then

\[
T^{7/2}=R^7.
\]

Thus the ancient spectral core requires

\[
\boxed{
\mathcal M_G(R^2)\gtrsim R^7
}
\]

unless an explicit far-boundary term survives.

The exponent `7` is the dimension-three `L2` mass exponent associated with retaining a second spatial derivative at the present time under backward heat propagation:

\[
3+2\times2=7.
\]

---

## 7. Why mere volume growth is insufficient

A bounded-amplitude background on a radius-`R` ball carries only volume-scale mass

\[
O(R^3).
\]

The derivative-feed requirement is instead

\[
\boxed{O(R^7).}
\]

Therefore the spatial-infinity survivor cannot be described merely as a passive bounded coherent background.
It needs either

1. amplitude growth at infinity/backward time;
2. a much stronger derivative-carrying far field;
3. or nonvanishing cutoff boundary input.

This sharply strengthens M17-284's qualitative global decompactification statement.

---

## 8. DSD audit

- No unrestricted backward heat-kernel representation is assumed for arbitrary infinite-growth ancient solutions.
- The cutoff boundary remainder is retained as an explicit branch.
- The `R^7` conclusion applies when that remainder vanishes and the relevant Gaussian pairing is finite.
- Infinite Gaussian-weighted mass is classified as an even stronger infinity-feed exit, not silently discarded.
- The theorem does not yet convert the `R^7` feed into an original-shell contradiction; that bridge is the next task.
- Global 3D Navier--Stokes regularity remains unproved.

---

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
