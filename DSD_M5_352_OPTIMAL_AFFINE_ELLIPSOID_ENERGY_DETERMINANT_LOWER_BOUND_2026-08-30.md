# DSD M5-352 — Optimal Affine Ellipsoid Energy Lower Bound via `det(grad u)`

Date: 2026-08-30

Status: **SHAPE-DEGENERACY AUDIT / FULL-RANK AFFINE CORE CANNOT EVADE FINITE-ENERGY CAPACITY BY VOLUME-PRESERVING ANISOTROPY / OPTIMAL ENERGY LOWER BOUND CONTROLLED BY `|det M|^(2/3)` / ONLY RANK-DEFICIENT AFFINE GEOMETRY REMAINS AS SHAPE ESCAPE / GLOBAL REGULARITY UNPROVED.**

## 1. Problem

M5-351 routed a saturated affine core to fixed-fraction material turnover because the available affine-support volume shrinks generation by generation.

A possible objection is that an incompressible material population need not stay ball-like. It may deform into a long thin ellipsoid while preserving volume.

This note optimizes the affine kinetic energy over **all ellipsoidal shapes of fixed volume**.

## 2. Affine field on an ellipsoid

Let

\[
E=A B_1
\]

be a centered ellipsoid, with `A` invertible. Let

\[
u(x)=Mx
\]

be an affine velocity after subtracting the local translation.

Changing variables `x=Ay`,

\[
\int_E|Mx|^2dx
=
|\det A|
\int_{B_1}|MAy|^2dy.
\]

By rotational symmetry of the unit ball,

\[
\int_{B_1}|By|^2dy
=c_3\operatorname{tr}(B^TB).
\]

Therefore

\[
\boxed{
\int_E|Mx|^2dx
=c_3|\det A|\,\|MA\|_F^2.
}
\]

## 3. Determinant lower bound

For any `3 x 3` matrix `B` with singular values `sigma_1,sigma_2,sigma_3`,

\[
\|B\|_F^2
=\sigma_1^2+\sigma_2^2+\sigma_3^2
\ge3(\sigma_1\sigma_2\sigma_3)^{2/3}.
\]

Hence

\[
\boxed{
\|B\|_F^2\ge3|\det B|^{2/3}.
}
\]

Apply this to `B=MA`:

\[
\|MA\|_F^2
\ge3|\det M|^{2/3}|\det A|^{2/3}.
\]

Thus

\[
\int_E|Mx|^2dx
\ge
3c_3|\det M|^{2/3}|\det A|^{5/3}.
\]

Since

\[
|E|=|B_1||\det A|,
\]

we obtain the shape-independent bound

\[
\boxed{
\int_E|Mx|^2dx
\ge
c_E |E|^{5/3}|\det M|^{2/3}.
}
\]

The constant `c_E>0` is dimensional only.

## 4. Optimality

The AM--GM bound is saturated when the singular values of `MA` are equal.

Thus the optimal ellipsoid has axes inversely proportional to the singular values of `M`:

\[
a_i\propto\sigma_i(M)^{-1}
\]

up to the common factor fixing the volume.

Therefore the determinant lower bound is not a rough ball estimate. It is the **optimal affine kinetic-energy lower bound over all ellipsoidal shapes of the prescribed volume**.

## 5. Finite-energy consequence

If a coherent material population has fixed volume `V_mat>0`, incompressibility preserves that volume.

If it remains in a full-rank affine state with gradient `M(t)`, then

\[
E_0
\ge
\int_{E(t)}|u-c(t)|^2dx
\ge
c_E V_{mat}^{5/3}|\det M(t)|^{2/3}.
\]

Hence

\[
\boxed{
|\det M(t)|
\le
C E_0^{3/2}V_{mat}^{-5/2}.
}
\]

A fixed material population therefore cannot remain affine while `|det M| -> infinity`, regardless of how anisotropically it deforms.

## 6. Formation-axis interpretation

The previous shape alternative

\[
\text{ball-like contraction}
\lor
\text{anisotropic shape escape}
\]

is too coarse.

The correct split is

\[
\boxed{
\text{full-rank affine geometry}
\lor
\text{rank-deficient affine geometry}.
}
\]

For full rank, all ellipsoidal shape choices are already included in the determinant energy lower bound.

Thus a shape escape can avoid the finite-energy capacity only if

\[
\boxed{\det M\approx0}
\]

or if the affine approximation/occupancy itself breaks down.

## 7. Relation to material turnover

Combine with M5-351.

A persistent coherent material population has fixed volume. On a generic full-rank dual-hyperbolic branch, growth of the affine gradient makes `|det M|` grow, which is incompatible with finite kinetic energy.

Therefore before this happens the branch must undergo at least one of

- material export/replacement;
- loss of affine coherence;
- rank-degenerate transition `det M ~ 0`;
- occupancy collapse.

Hence anisotropy is no longer an unrestricted fourth escape.

## 8. Firewall

The determinant is that of the **full velocity gradient** `M=grad u`, not the strain determinant `det S` used in the Betchov identity.

Do not identify these two quantities.

If `det M=0`, this estimate loses coercivity even when `|M|` is large; the rank-deficient branch must be audited separately.

## 9. Audit verdict

### PROVED

- exact affine ellipsoid energy formula;
- optimal shape-independent lower bound `E >= c V^(5/3)|det M|^(2/3)`;
- full-rank affine material persistence cannot be rescued by anisotropic deformation under finite energy.

### OPEN

- rank-deficient `det M ~ 0` affine corridor;
- non-ellipsoidal/fragmented occupancy degeneration;
- repeated turnover contradiction;
- global regularity.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]