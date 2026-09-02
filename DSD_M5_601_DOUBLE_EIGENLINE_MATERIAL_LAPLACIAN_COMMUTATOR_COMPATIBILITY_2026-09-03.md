# DSD M5-601 — Double-eigenline material/Laplacian commutator compatibility

Date: 2026-09-03

Status: **CONDITIONAL ON M5-599. THE GLOBAL DOUBLE-EIGENLINE EQUATIONS CANNOT EVOLVE INDEPENDENTLY: COMMUTING THE SIMILARITY MATERIAL DERIVATIVE WITH THE LAPLACIAN GIVES AN EXACT SECOND-ORDER COMPATIBILITY IDENTITY. ITS TRANSVERSE PROJECTION MUST VANISH POINTWISE. THIS IS AN OVERDETERMINED PDE CONSTRAINT, NOT AN UNSIGNED LOWER BOUND. NO CONTRADICTION HAS YET BEEN EXTRACTED FROM IT. GLOBAL REGULARITY REMAINS UNPROVED.**

## 1. Double-eigenline evolution

On the M5-599/M5-600 branch,

\[
\Delta W=\kappa W,
\]

and

\[
D_BW=\gamma W,
\qquad
\gamma:=\sigma+\kappa-1,
\]

where

\[
D_B=\partial_\theta+B\cdot\nabla,
\qquad
B=U+\frac12y.
\]

## 2. The material derivative and Laplacian do not commute

For any smooth vector field \(V\),

\[
\Delta(B\cdot\nabla V)
=
B\cdot\nabla\Delta V
+2\partial_iB_j\,\partial_{ij}V
+(\Delta B_j)\partial_jV.
\]

Therefore

\[
\boxed{
D_B\Delta V
=
\Delta D_BV
-2\partial_iB_j\,\partial_{ij}V
-(\Delta B_j)\partial_jV.
}
\]

## 3. Apply the commutator to W

From

\[
\Delta W=\kappa W,
\]

we have

\[
D_B\Delta W
=(D_B\kappa)W+\kappa D_BW
=(D_B\kappa+\kappa\gamma)W.
\]

From

\[
D_BW=\gamma W,
\]

we have

\[
\Delta D_BW
=(\Delta\gamma)W
+2\nabla\gamma\cdot\nabla W
+\gamma\Delta W.
\]

Thus

\[
\Delta D_BW
=(\Delta\gamma+\gamma\kappa)W
+2\nabla\gamma\cdot\nabla W.
\]

Substitution into the commutator identity cancels the \(\gamma\kappa W\) terms and gives

\[
\boxed{
(D_B\kappa-\Delta\gamma)W
=
2\nabla\gamma\cdot\nabla W
-2\partial_iB_j\,\partial_{ij}W
-(\Delta B_j)\partial_jW.
}
\]

This is exact.

## 4. Remove the explicit similarity drift

Since

\[
B=U+\frac12y,
\]

we have

\[
\partial_iB_j
=
\partial_iU_j+\frac12\delta_{ij},
\]

and

\[
\Delta B=\Delta U.
\]

For incompressible \(U\) with \(W=\nabla\times U\),

\[
\Delta U=-\nabla\times W.
\]

Therefore

\[
-2\partial_iB_j\partial_{ij}W
=
-2\partial_iU_j\partial_{ij}W
-\Delta W
=
-2\partial_iU_j\partial_{ij}W
-\kappa W,
\]

and

\[
-(\Delta B\cdot\nabla)W
=
(\nabla\times W)\cdot\nabla W.
\]

Hence

\[
\boxed{
(D_B\kappa-\Delta\gamma+\kappa)W
=
2\nabla\gamma\cdot\nabla W
-2\partial_iU_j\partial_{ij}W
+(\nabla\times W)\cdot\nabla W.
}
\]

## 5. Exact transverse compatibility

The left side is parallel to \(W\). Therefore, on \(\{W\ne0\}\),

\[
\boxed{
P_\xi^\perp
\left[
2\nabla\gamma\cdot\nabla W
-2\partial_iU_j\partial_{ij}W
+(\nabla\times W)\cdot\nabla W
\right]
=0.
}
\]

Equivalently, without dividing by \(|W|\),

\[
\boxed{
W\times
\left[
2\nabla\gamma\cdot\nabla W
-2\partial_iU_j\partial_{ij}W
+(\nabla\times W)\cdot\nabla W
\right]
=0.
}
\]

This cross-product form extends smoothly through vorticity zeros.

## 6. Parallel compatibility

Taking the dot product with \(\xi\) gives

\[
\boxed{
\rho(D_B\kappa-\Delta\gamma+\kappa)
=
\xi\cdot
\left[
2\nabla\gamma\cdot\nabla W
-2\partial_iU_j\partial_{ij}W
+(\nabla\times W)\cdot\nabla W
\right].
}
\]

Together with

\[
\boxed{W\cdot\nabla\kappa=0,}
\]

this constrains both material and spatial variation of the viscous multiplier.

## 7. Why this is not another charge argument

M5-598 showed that another positive event-level norm is not enough.

The present identity is different: the transverse component must be **exactly zero**.

A candidate CE-H solution must satisfy simultaneously

\[
\Sigma W=\sigma W,
\]

\[
\Delta W=\kappa W,
\]

\[
W\cdot\nabla\kappa=0,
\]

and the second-order commutator compatibility above.

These equations overdetermine the same finite-enstrophy field.

## 8. DSD firewall

The vanishing transverse commutator is derived from the already assumed double-eigenline equations. It is therefore a necessary compatibility condition, not yet an independent contradiction.

One must still show that the finite-enstrophy recurrent class cannot solve this overdetermined system.

No dimension count or genericity statement is sufficient.

## 9. Next target

There are two promising exact consequences to test:

1. the material-vortex-tube flux law implied by \(D_B\xi=0\) and \(\Delta W=\kappa W\);
2. the evolution of the strain-eigenline relation, which constrains the pressure Hessian and viscous strain Laplacian.

The vortex-tube route is especially attractive because vorticity flux is scale invariant and therefore avoids the summability failure audited in M5-598.

Status: **THE CE-H CLASS NOW SATISFIES A POINTWISE ZERO COMMUTATOR DEFECT IN ADDITION TO BOTH EIGENLINE EQUATIONS. THE NEXT STEP WILL TEST WHETHER THE SCALE-INVARIANT MATERIAL VORTEX-TUBE FLUX CAN RECURRENTLY CLOSE UNDER THIS SYSTEM. GLOBAL REGULARITY REMAINS UNPROVED.**