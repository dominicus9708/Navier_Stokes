# DSD M5-673 — CE-H strain-eigenvalue evolution exposes top-alignment spectral-gap damping

Date: 2026-09-03

Status: **INTERNAL POINTWISE STRAIN-EIGENVALUE DYNAMICS / PROJECTING THE SIMILARITY STRAIN EQUATION ON THE MATERIAL CE-H EIGENLINE AND USING THE LAPLACIAN OF `Sigma xi=sigma xi` GIVES `D_B sigma = Delta sigma-sigma^2-sigma-P_xixi-2 G_sigma`, WHERE `G_sigma=sum_i partial_i xi·(sigma I-Sigma)partial_i xi` / ON TOP-EIGENVALUE ALIGNMENT `G_sigma>=0`, SO A RECURRENT ORDER-ONE POSITIVE AXIAL STRAIN MUST BE SUPPORTED BY PRESSURE-HESSIAN OR POSITIVE STRAIN-LAPLACIAN COMPENSATION IN ADDITION TO THE QUADRATIC/LINEAR DAMPING / ON MIDDLE ALIGNMENT THE GAP TERM IS INDEFINITE / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Similarity strain equation

Recall the CE-H similarity strain equation from M5-624:

\[
\boxed{
D_B\Sigma
+
\Sigma^2
+
\mathcal R^2
+
\Sigma
+
\nabla^2P
=
\Delta\Sigma,
}
\]

where

\[
\mathcal R=\frac12(\nabla U-\nabla U^T)
\]

is the antisymmetric part of the velocity gradient.

CE-H has

\[
\boxed{\Sigma\xi=\sigma\xi,}
\qquad
\boxed{D_B\xi=0.}
\]

Also

\[
\mathcal R\xi=0
\]

because the antisymmetric matrix represents cross product with vorticity and `xi` is parallel to vorticity.

Thus

\[
\xi\cdot\mathcal R^2\xi=0.
\]

---

## 2. Material derivative of the eigenvalue

Since `D_B xi=0`,

\[
D_B\sigma
=D_B(\xi\cdot\Sigma\xi)
=\xi\cdot(D_B\Sigma)\xi.
\]

Project the strain equation onto `xi`:

\[
D_B\sigma
+
\sigma^2
+
\sigma
+
\xi\cdot\nabla^2P\,\xi
=
\xi\cdot\Delta\Sigma\,\xi.
\]

Hence

\[
\boxed{
D_B\sigma
=
\xi\cdot\Delta\Sigma\,\xi
-
\sigma^2-\sigma
-
P_{\xi\xi},
}
\]

where

\[
P_{\xi\xi}:=\xi\cdot\nabla^2P\,\xi.
\]

---

## 3. Laplacian of the eigenline

Apply the Laplacian to

\[
\Sigma\xi=\sigma\xi.
\]

Then

\[
(\Delta\Sigma)\xi
+2\partial_i\Sigma\,\partial_i\xi
+\Sigma\Delta\xi
=
(\Delta\sigma)\xi
+2\partial_i\sigma\,\partial_i\xi
+\sigma\Delta\xi.
\]

Pair with `xi`.

Because

\[
\xi\cdot\partial_i\xi=0
\]

and

\[
\xi\cdot\Sigma=\sigma\xi,
\]

the `Delta xi` terms and the `grad sigma` term cancel, leaving

\[
\xi\cdot\Delta\Sigma\,\xi
+2\xi\cdot(\partial_i\Sigma)\partial_i\xi
=
\Delta\sigma.
\]

---

## 4. Spectral-gap term

Differentiate the eigenline once:

\[
(\partial_i\Sigma)\xi
+(\Sigma-\sigma I)\partial_i\xi
=(\partial_i\sigma)\xi.
\]

Pair with `partial_i xi`:

\[
\partial_i\xi\cdot(\partial_i\Sigma)\xi
+
\partial_i\xi\cdot(\Sigma-\sigma I)\partial_i\xi
=0.
\]

By symmetry of `partial_i Sigma`,

\[
\xi\cdot(\partial_i\Sigma)\partial_i\xi
=
\partial_i\xi\cdot(\sigma I-\Sigma)\partial_i\xi.
\]

Define

\[
\boxed{
\mathcal G_\sigma
:=
\sum_i
\partial_i\xi\cdot(\sigma I-\Sigma)\partial_i\xi.
}
\]

Then

\[
\boxed{
\xi\cdot\Delta\Sigma\,\xi
=
\Delta\sigma-2\mathcal G_\sigma.
}
\]

---

## 5. Exact eigenvalue evolution

Substitute into the projected strain equation:

\[
\boxed{
D_B\sigma
=
\Delta\sigma
-
\sigma^2
-
\sigma
-
P_{\xi\xi}
-
2\mathcal G_\sigma.
}
\]

This is the exact CE-H axial-strain eigenvalue equation.

---

## 6. Top-eigenvalue branch

Suppose `sigma=lambda_1`, the largest strain eigenvalue.

Every `partial_i xi` is transverse to `xi`, and on the transverse plane

\[
\sigma I-\Sigma\ge0.
\]

Therefore

\[
\boxed{\mathcal G_\sigma\ge0.}
\]

If the top eigenvalue is uniformly simple with transverse spectral gap `g>0`, then

\[
\boxed{
\mathcal G_\sigma
\ge
g|\nabla\xi|^2.
}
\]

Thus direction variation creates an additional one-sign damping term in the axial strain equation.

---

## 7. Collision branch

If the top spectral gap tends to zero where direction variation is active, the configuration approaches a top/middle eigenvalue collision.

The trace-free spectrum then approaches

\[
\{\sigma,\sigma,-2\sigma\},
\]

which is precisely the M5-623--624 collision branch.

M5-624 already shows that persistent collision requires pressure-Hessian/viscous compensation of the vorticity-induced eigenvalue splitting.

Thus top alignment splits into

\[
\boxed{
\text{simple-top spectral-gap damping}
\lor
\text{top/middle collision compensation}.
}
\]

---

## 8. Relation to the vorticity maximum

M5-672 gives, along a measurable maximizing selection,

\[
\langle\sigma_*\rangle\ge1.
\]

If the maximizing vorticity direction is top-aligned on a positive-density time set, then the equation

\[
D_B\sigma_*
=
\Delta\sigma_*
-\sigma_*^2-\sigma_*
-P_{\xi\xi,*}
-2\mathcal G_{\sigma,*}
\]

shows that the recurrent order-one positive strain must overcome:

1. quadratic damping `sigma_*^2`;
2. similarity linear damping `sigma_*`;
3. nonnegative spectral-gap damping on the simple-top branch.

Therefore pressure-Hessian and/or positive spatial strain-Laplacian compensation is mandatory.

This is a payer classification, not yet a contradiction.

---

## 9. Middle-eigenvalue branch

If `sigma=lambda_2`, then on the transverse plane one spectral difference is positive and the other negative.

Hence

\[
\mathcal G_\sigma
\]

is indefinite.

Known scale-critical regularity criteria based on `lambda_2^+` do not automatically close an order-one Type-I recurrent middle-strain profile: such a profile sits at the critical logarithmic divergence threshold rather than satisfying the finite criterion.

Therefore positive middle alignment remains a genuine hard branch.

---

## 10. Updated frontier

The high-vorticity recurrent payer now splits into

\[
\boxed{
\begin{aligned}
&\text{simple top alignment}
&&\Rightarrow
\text{spectral-gap damping + pressure/Delta-sigma payer},\\
&\text{top-middle collision}
&&\Rightarrow
\text{M5-624 pressure-viscous compensation},\\
&\text{positive middle alignment}
&&\Rightarrow
\text{critical middle-strain branch}.
\end{aligned}
}
\]

A next useful calculation is to derive a bounded scalar ledger for the positive middle-strain population or a pressure-Hessian identity at the vorticity maximum that couples the first two branches back to the finite-core production budget.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
