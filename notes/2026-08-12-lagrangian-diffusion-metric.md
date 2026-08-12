# Lagrangian diffusion metric: exact bridge and coordinate-cancellation audit

Date: 2026-08-12

Status: **DERIVED MATERIAL-COORDINATE BRIDGE + ROUTE PRUNING**.

## 1. Exact material-coordinate equation on the smooth lifespan

Let

\[
x=\Phi(a,t),
\qquad
F=D_a\Phi,
\qquad
J=\det F=1,
\]

and

\[
U(a,t)=u(\Phi(a,t),t),
\qquad
P(a,t)=p(\Phi(a,t),t).
\]

Material differentiation absorbs explicit advection.  With

\[
A=F^{-1}F^{-T},
\]

the smooth equation becomes

\[
\boxed{
\partial_tU
=-F^{-T}\nabla_aP
+\nu\operatorname{div}_a(A\nabla_aU),
}
\]

and incompressibility becomes

\[
\operatorname{div}_a(F^{-1}U)=0.
\]

`A` is symmetric positive definite and

\[
\det A=1.
\]

Also

\[
\dot A=-2F^{-1}SF^{-T}.
\]

These are exact material-coordinate identities while the flow map remains a sufficiently regular diffeomorphism.

## 2. Important correction: `A` does not create extra physical viscosity

Because

\[
\nabla_aU=(\nabla_xu)F,
\]

we have the pointwise identity

\[
\boxed{
(\nabla_aU)A(\nabla_aU)^T
=
(\nabla_xu)(\nabla_xu)^T.
}
\]

Therefore

\[
\boxed{
\sum_i(\nabla_aU_i)^TA(\nabla_aU_i)
=|\nabla_xu|^2.
}
\]

The apparently enhanced diffusion coefficient in a compressed reference direction is exactly accompanied by the corresponding transformation of the reference gradient.  Likewise, a small eigenvalue of `A` does not by itself represent physical loss of viscosity.

Thus the phrase **deformation–viscosity compensation** is retained only as a coordinate-level cancellation identity, not as a new stabilizing physical mechanism.

## 3. Frozen Gaussian example

For

\[
F=\operatorname{diag}(e^{2c\tau},e^{2c\tau},e^{-4c\tau}),
\qquad c=e^{-1/4},
\]

one has

\[
A=\operatorname{diag}(e^{-4c\tau},e^{-4c\tau},e^{8c\tau}).
\]

Although the third reference-coordinate diffusion coefficient becomes large, the transformed gradient changes simultaneously so that the metric-weighted dissipation is exactly the original physical dissipation.

## 4. Routes rejected

The following are rejected as proof mechanisms:

1. `det A=1` implies a new uniform viscous coercivity;
2. `tr A>=3` implies enhanced physical dissipation;
3. a large eigenvalue of `A` alone regularizes the flow;
4. a small eigenvalue of `A` alone identifies a physical weak-viscosity direction.

All fail because `A` and `grad_a U` are linked by the exact coordinate transformation.

Status: **FAILED ROUTES / ALGEBRAICALLY PRUNED**.

## 5. What remains useful

The Lagrangian transformation still has two genuine organizational advantages:

1. the explicit nonlinear advection term disappears;
2. a moving/deforming physical fluid region is represented on a fixed material reference domain.

The price is that pressure, incompressibility, and diffusion acquire coefficients depending on `F`.

Therefore any actual proof gain must come from a new estimate for the **coupled transformed system**

\[
(U,P,F),
\]

not from `A` eigenvalues considered in isolation.

This remains compatible with the DSD four-layer bookkeeping: the matrix channels are useful for preserving structural information, but no coordinate artifact is promoted to a new physical damping term.
