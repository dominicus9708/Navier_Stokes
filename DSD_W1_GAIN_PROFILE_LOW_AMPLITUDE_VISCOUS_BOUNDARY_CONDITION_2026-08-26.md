# DSD W1 Gain-Profile Low-Amplitude Viscous Boundary Condition

Date: 2026-08-26

Status: **THE ABSTRACT SCALAR GAIN PROFILE IS GIVEN ITS FIRST NONTRIVIAL NAVIER--STOKES REALIZATION CONSTRAINT / AT ZERO NORMALIZED AMPLITUDE PRESSURE WORK VANISHES WHILE THRESHOLDED VISCOSITY TENDS TO ENSTROPHY, SO `G_BAR(0+)=-NU<Z><0` / POSITIVE TOTAL DEFECT MASS THEREFORE FORCES AN INTERIOR SIGN CHANGE AND OVERCOMPENSATING PRESSURE-PUMP BAND / GLOBAL REGULARITY UNPROVED.**

## 1. Gain profile

Recall

\[
\bar G(\lambda)
:=
\left\langle
J_P(\lambda)-\nu D_\lambda
\right\rangle_\mu.
\]

The total mass is

\[
\boxed{
\int_0^{A_*}\bar G(\lambda)d\lambda
=\frac{\mathscr R_3}{6}>0.
}
\]

## 2. Pressure work vanishes at zero amplitude

The threshold pressure work may be written

\[
J_P(\lambda)
=-\int_{\{|U|>\lambda\}}U\cdot\nabla P\,dY.
\]

Under the W1 smooth core and critical far decay, `U dot grad P` is integrable. Passing to `lambda downarrow0`,

\[
J_P(0+)
=-\int_{\mathbb R^3}U\cdot\nabla P\,dY.
\]

Using `div U=0`,

\[
\int U\cdot\nabla P
=
\lim_{R\to\infty}
\int_{|Y|=R}P\,U\cdot n\,dS.
\]

The W1 tail has `U=O(R^-1)`, `P=O(R^-2)` modulo the gauge, so the sphere term is `O(R^-1)` and vanishes. Therefore

\[
\boxed{J_P(0+)=0.}
\]

## 3. Viscous threshold tends to enstrophy

The thresholded viscous term is

\[
D_\lambda
=
\int_{\{|U|>\lambda\}}|\nabla U|^2dY
+\lambda\int_{\{|U|=\lambda\}}|\nabla|U||dS
\]

for regular levels / in the smooth-truncation limit.

As `lambda downarrow0`, the second term vanishes under the W1 tail bounds and the first tends to

\[
\int|\nabla U|^2dY.
\]

For divergence-free whole-space fields with the W1 decay,

\[
\int|\nabla U|^2dY
=
\int|\Omega|^2dY
=:Z.
\]

Hence

\[
\boxed{D_0=Z>0}
\]

on every nontrivial W1 state.

## 4. Negative low-amplitude gain

Therefore statewise at the boundary,

\[
G_U(0+)
=J_P(0+)-\nu D_0
=-\nu Z(U).
\]

Averaging gives

\[
\boxed{
\bar G(0+)
=-\nu\langle Z\rangle_\mu
<0.
}
\]

This is the first realization constraint on `bar G` that is not contained in the abstract scalar reconstruction algebra.

## 5. Forced sign change

At the upper common amplitude ceiling,

\[
\bar G(A_*)=0
\]

in the natural one-sided/smoothed sense. But the total gain mass is positive:

\[
\int_0^{A_*}\bar G
=\mathscr R_3/6>0.
\]

Since `bar G` starts strictly negative, it must become strictly positive on an interior amplitude set.

Thus

\[
\boxed{
\text{low-amplitude viscous-loss layer}
\longrightarrow
\text{interior pressure-pump layer}
\longrightarrow
\text{upper-amplitude termination}.
}
\]

The positive interior pump must overcompensate both the low-amplitude viscous loss and the positive defect mass.

## 6. Endpoint expansion

Since

\[
\bar K'(\lambda)=-2\bar G(\lambda),
\]

the low-amplitude boundary condition gives formally

\[
\boxed{
\bar K(\lambda)
=
\frac{\mathscr R_3}{3}
+2\nu\langle Z\rangle_\mu\,\lambda
+o(\lambda).
}
\]

Because

\[
\bar C=\bar K+2\lambda\bar G,
\]

the linear terms cancel:

\[
\boxed{
\bar C(\lambda)
=
\frac{\mathscr R_3}{3}+o(\lambda).
}
\]

Thus the weak-L3 coefficient is flat to first order at the low-amplitude boundary even though the hidden gain profile is strictly viscous there.

## 7. Consequence for scalar toy profiles

An arbitrary positive scalar gain profile satisfying only `K>=0`, `C>=0`, and positive total mass need not be Navier--Stokes realizable. It must additionally satisfy the low-amplitude viscous boundary condition above.

The earlier toy profile with positive `G(0)` is therefore a valid algebraic nonclosure example but **not** a Navier--Stokes realization candidate.

## 8. Remaining target

A final closure could follow from proving that the required sign-changing profile cannot be realized together with the pressure Poisson equation, incompressibility, recurrent compactness, and the vorticity/stretching constraints.

No such theorem is proved here.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
