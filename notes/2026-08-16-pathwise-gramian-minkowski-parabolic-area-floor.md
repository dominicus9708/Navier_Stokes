# Volume preservation alone gives a pathwise two-dimensional Gramian area floor

Date: 2026-08-16

Status: **EXACT MATRIX CONSEQUENCE OF `det F=1` AND MINKOWSKI'S DETERMINANT INEQUALITY. IT COMPLEMENTS THE DEFORMATION-DEPENDENT `q/J` GRAMIAN BOUND WITH A PURE ELAPSED-TIME FLOOR. GLOBAL REGULARITY NOT PROVED.**

## 1. Pulled-back stochastic diffusion Gramian

Along any realization of the additive-noise incompressible stochastic flow, let

\[
F'(s)=\nabla U(X_s,s)F(s),
\qquad
\det F(s)=1.
\]

Define

\[
\boxed{
C_T
=\int_0^T
F(s)^{-1}F(s)^{-T}ds.
}
\]

Set

\[
A(s)=F(s)^{-1}F(s)^{-T}.
\]

Then `A(s)` is symmetric positive definite and

\[
\boxed{\det A(s)=1.}
\]

---

## 2. Minkowski determinant inequality

For positive semidefinite `3 x 3` matrices, Minkowski's determinant theorem states

\[
\det(A+B)^{1/3}
\ge
\det(A)^{1/3}
+
\det(B)^{1/3}.
\]

Apply this to Riemann sums approximating the integral defining `C_T`. By homogeneity and passage to the limit,

\[
\det\left(\int_0^T A(s)ds\right)^{1/3}
\ge
\int_0^T\det(A(s))^{1/3}ds.
\]

Since `det A(s)=1`,

\[
\boxed{
\det(C_T)^{1/3}
\ge T.
}
\]

Equivalently,

\[
\boxed{
\det C_T
\ge T^3.
}
\]

This requires no strain bound, no affine approximation, and no statistical averaging.

---

## 3. Two largest eigenvalues

Let

\[
0<\mu_1\le\mu_2\le\mu_3
\]

be the eigenvalues of `C_T`.

Because

\[
\mu_1^3
\le
\mu_1\mu_2\mu_3
=
\det C_T,
\]

we have

\[
\mu_1\le(\det C_T)^{1/3}.
\]

Therefore

\[
\mu_2\mu_3
=
\frac{\det C_T}{\mu_1}
\ge
(\det C_T)^{2/3}.
\]

Using `det C_T >= T^3`,

\[
\boxed{
(\mu_2\mu_3)^{1/2}
\ge T.
}
\]

Thus every volume-preserving stochastic trajectory accumulates at least a two-dimensional pulled-back diffusion area proportional to elapsed time.

Equality occurs for the undeformed isotropic case `F(s)=I`, where `C_T=T I`.

---

## 4. Combine with the deformation-dependent area theorem

The preceding pathwise deformation--diffusion theorem independently gives, when

\[
q_p=\|F(T)\|_{op}\ge2,
\qquad
J_p=\int_0^T\|S(X_s,s)\|_{op}^2ds,
\]

\[
(\mu_2\mu_3)^{1/2}
\gtrsim
\frac{q_p}{J_p}.
\]

Therefore

\[
\boxed{
(\mu_2\mu_3)^{1/2}
\gtrsim
\max\left\{
T,
\frac{q_p}{J_p}
\right\}.
}
\]

The two lower bounds control opposite strategies:

- waiting a long time cannot avoid ordinary two-dimensional diffusion area;
- creating a large deformation quickly cannot avoid anisotropic diffusion area unless the pathwise strain-square action is large.

---

## 5. Insert the clean-precursor lifespan

From the clean minimum-enstrophy checkpoint to a coherent crossing,

\[
T=s_c-s_m
\gtrsim
\nu^3E_m^{-2}.
\]

Hence every stochastic history spanning that interval satisfies

\[
\boxed{
(\mu_2\mu_3)^{1/2}
\gtrsim
\nu^3E_m^{-2}.
}
\]

The actual Malliavin covariance contains the factor `2 nu`, so this corresponds to a very large physical/noise two-dimensional smoothing area in the pulled-back material frame.

---

## 6. Interaction with the clean transverse precursor reservoir

At the minimum-enstrophy checkpoint, for every unit direction `e`,

\[
M_{\Pi,e}^2
\lesssim_\nu E_m.
\]

In a deterministic affine Gaussian problem, a two-dimensional covariance area

\[
A_2=(\mu_2\mu_3)^{1/2}
\]

acts on this mixed norm with a smoothing factor proportional to

\[
(\nu A_2)^{-1/2}.
\]

The pure-time floor would then give

\[
(\nu A_2)^{-1/2}M_\Pi
\lesssim
C_\nu E_m^{3/2}.
\]

A final deformation factor `q_p` would leave the schematic necessary condition

\[
q_pE_m^{3/2}\gtrsim1
\]

for an order-one terminal output.

This line is recorded only as the affine-Gaussian heuristic of the exact area floor. In the nonlinear stochastic flow the covariance and deformation are random and correlated; the random-Gramian Malliavin smoothing transfer is still required before this becomes a theorem.

---

## 7. Updated analytic target

The pathwise Gramian now has two exact sources of largeness:

\[
\boxed{
A_2
\gtrsim
\max\{E_m^{-2},q_p/J_p\}.
}
\]

Therefore the remaining probability/analysis problem is sharply isolated:

> convert a random two-dimensional Malliavin covariance area, whose lower bound is pathwise, into a mixed-norm smoothing estimate for the stochastic Cauchy expectation, while charging all correlation terms to the Hessian-generated Malliavin derivative channel.

No additional geometric or temporal escape remains inside the Gramian itself.

Overall status: **PATHWISE DIFFUSION AREA HAS A PURE-TIME FLOOR AND A LARGE-DEFORMATION FLOOR / RANDOM-GRAMIAN MIXED-NORM TRANSFER REMAINS THE SINGLE ANALYTIC BRIDGE.**
