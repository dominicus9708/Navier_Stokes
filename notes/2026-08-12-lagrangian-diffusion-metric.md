# Lagrangian diffusion metric and deformation–viscosity compensation

Date: 2026-08-12

Status: **DERIVED MATERIAL-COORDINATE BRIDGE + DSD AXIS-MATRIX INTERPRETATION + OPEN ALIGNMENT OBLIGATION**.

## 1. Exact material-coordinate equation on the smooth lifespan

Let

\[
x=\Phi(a,t),
\qquad
F=D_a\Phi,
\qquad
J=\det F=1,
\]

and define

\[
U(a,t)=u(\Phi(a,t),t),
\qquad
P(a,t)=p(\Phi(a,t),t).
\]

Since material differentiation absorbs advection,

\[
\partial_tU
=-F^{-T}\nabla_aP
+\nu(\Delta_xu)\circ\Phi.
\]

Using the Piola transform and `J=1`, introduce

\[
\boxed{
A=F^{-1}F^{-T}.
}
\]

Then componentwise

\[
\boxed{
\partial_tU
=-F^{-T}\nabla_aP
+\nu\operatorname{div}_a(A\nabla_aU).
}
\]

The incompressibility constraint becomes

\[
\operatorname{div}_a(F^{-1}U)=0.
\]

Thus in material coordinates:

- nonlinear advection disappears from the explicit evolution operator;
- deformation moves into `F^{-T}` in the pressure term;
- deformation also moves into the anisotropic diffusion metric `A`.

## 2. Axis-matrix properties

`A` is symmetric positive definite and

\[
\boxed{
\det A=(\det F)^{-2}=1.
}
\]

If the singular values of `F` are

\[
s_1,s_2,s_3,
\qquad
s_1s_2s_3=1,
\]

then the eigenvalues of `A` are

\[
s_1^{-2},s_2^{-2},s_3^{-2}.
\]

Therefore a compressed material direction obtains a larger reference-coordinate diffusion weight, while a stretched direction obtains a smaller one.

This is the precise deformation–viscosity compensation mechanism.

## 3. Metric evolution

From

\[
\dot F=(\nabla_xu)F
\]

and

\[
S=\frac12(\nabla u+\nabla u^T),
\]

one obtains

\[
\boxed{
\dot A
=-2F^{-1}SF^{-T}.
}
\]

The determinant remains one because `tr S=0`.

This gives an explicit DSD dynamic matrix channel: strain changes the reference diffusion metric without changing its determinant.

## 4. Viscous energy in the reference axes

The physical dissipation pulls back as

\[
\boxed{
\int_{\Omega_t}|\nabla_xu|^2dx
=
\int_{B}
\sum_i
(\nabla_aU_i)^T
A
(\nabla_aU_i)\,da.
}
\]

Let

\[
A e_j=\alpha_j e_j,
\qquad
\alpha_j>0,
\qquad
\prod_j\alpha_j=1.
\]

Define gradient-alignment weights

\[
w_j
=
\frac{
\sum_i |\nabla_aU_i\cdot e_j|^2
}{
|\nabla_aU|^2
},
\qquad
\sum_jw_j=1.
\]

Then the local effective diffusion multiplier is

\[
\boxed{
\kappa_{\rm eff}
=
\sum_j\alpha_jw_j.
}
\]

Hence deformation alone does not determine whether viscosity is strengthened or weakened.  The orientation of the velocity-gradient energy relative to the eigenvectors of `A` is essential.

## 5. Frozen Gaussian anchor

For the existing local Gaussian deformation

\[
F=\operatorname{diag}
(e^{2c\tau},e^{2c\tau},e^{-4c\tau}),
\qquad
c=e^{-1/4},
\]

we have

\[
A=\operatorname{diag}
(e^{-4c\tau},e^{-4c\tau},e^{8c\tau}).
\]

Thus the direction compressed by `e^{-4c tau}` receives diffusion weight

\[
e^{8c\tau},
\]

while the two stretched directions receive

\[
e^{-4c\tau}.
\]

The compensation is therefore very strong in the compressed direction, but diffusion becomes weak along the stretched directions.

## 6. Why `det A=1` is not enough

AM--GM gives

\[
\operatorname{tr}A\ge3.
\]

However this does not imply

\[
A\ge cI
\]

with a universal positive `c`, because one eigenvalue can approach zero while another grows.

Therefore the route

\[
\det A=1
\Longrightarrow
\text{uniform viscous coercivity}
\]

is a **FAILED ROUTE** at the algebraic level.

The retained route is the alignment-sensitive one:

\[
\boxed{
\text{A dangerous material configuration must combine large stretch with persistent gradient alignment into the weak-diffusion eigendirections.}
}
\]

## 7. DSD interpretation

This bridge fits the four-paper DSD structure naturally:

- **Formation Axiom System:** keep deformation, pressure, diffusion, and gradient-alignment channels typed separately;
- **축 속성공리계:** `F` and `A` describe properties/relations of the three realized spatial axes without increasing spatial rank;
- **Static Aggregation:** aggregate eigenvalues `alpha_j` and weights `w_j` without collapsing them prematurely to `tr A`;
- **Structural Reorganization Dynamics:** evolve `A` by `dot A=-2F^{-1}SF^{-T}` and track its coupling to gradient orientation.

A scalar such as `tr A` is insufficient because it loses the alignment information that determines `kappa_eff`.

## 8. Next proof target

The next question is whether the weak-diffusion alignment can persist strongly enough to support critical concentration.

Candidate channel:

\[
\Gamma_{\rm weak}
=
\frac{
\sum_{j:\alpha_j<1}
(1-\alpha_j)w_j
}{
\sum_jw_j
}.
\]

More conservatively, retain the full tuple

\[
(\alpha_1,\alpha_2,\alpha_3;w_1,w_2,w_3)
\]

until a coercive inequality is proved.

A useful proof would show that either

1. gradients are forced into compressed/high-diffusion directions often enough for viscosity to dominate, or
2. persistent alignment with stretched/weak-diffusion directions forces another already controlled DSD channel (pressure, vorticity alignment, or oscillation) to violate a compatibility condition.

No such arbitrary-data theorem is presently established here.

Status: **OPEN PROOF OBLIGATION**.
