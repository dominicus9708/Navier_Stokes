# Gaussian residual variance dynamics and terminal-layer collapse

Date: 2026-08-13

Status: **DERIVED WEIGHTED VARIANCE IDENTITIES + CONDITIONAL TERMINAL COLLAPSE / GLOBAL REGULARITY NOT PROVED**.

The self-consistent Gaussian affine residual state is

\[
\mathcal B_\gamma
=\operatorname{Var}_\gamma(S)
+\frac12\operatorname{Var}_\gamma(\Omega).
\]

This note upgrades that static residual descriptor to a dynamical budget.  The backward affine heat Gaussian provides a singular Poincare coercivity of order `1/(T-s)` near the terminal point.  Consequently residual variance cannot remain order one arbitrarily close to the terminal first-hitting point unless affine deformation or pressure-Hessian variance becomes correspondingly large.

No novelty claim is made without a separate literature-priority audit.

---

## 1. Setup

Fix a terminal first-hitting point at time `T` and use the self-consistent Gaussian affine frame

\[
a'(s)=\int\gamma_s u(a+y,s)\,dy,
\qquad
L(s)=\int\gamma_s\nabla u(a+y,s)\,dy.
\]

Write

\[
r=u(a+y,s)-a'(s)-L(s)y,
\]

so that

\[
\int\gamma_s r=0,
\qquad
\int\gamma_s\nabla r=0,
\qquad
\nabla\cdot r=0.
\]

The vorticity equation in this frame is

\[
\partial_s\Omega+(Ly)\cdot\nabla\Omega
=L\Omega+\nu\Delta\Omega+f_r,
\]

with

\[
f_r=(\Omega\cdot\nabla)r-(r\cdot\nabla)\Omega.
\]

The scalar/matrix-valued Gaussian `gamma_s` is the backward adjoint kernel for the affine advection-diffusion operator.

Define

\[
\bar\Omega=\int\gamma\Omega,
\qquad
V_\omega=\int\gamma|\Omega-\bar\Omega|^2,
\]

\[
\bar S=\int\gamma S=\operatorname{sym}L,
\qquad
V_S=\int\gamma|S-\bar S|_F^2.
\]

Then

\[
\boxed{\mathcal B_\gamma=V_S+\frac12V_\omega.}
\]

---

## 2. Exact vorticity-variance identity

Because the Gaussian solves the backward adjoint equation, affine transport and scalar heat terms cancel in the weighted moment calculation.  The mean obeys

\[
\bar\Omega'
=L\bar\Omega+\int\gamma f_r.
\]

The variance obeys exactly

\[
\boxed{
\begin{aligned}
V_\omega'
={}&-2\nu D_\omega
+2\int\gamma(\Omega-\bar\Omega)\cdot L(\Omega-\bar\Omega)\\
&+2\int\gamma(\Omega-\bar\Omega)\cdot f_r,
\end{aligned}
}
\]

where

\[
D_\omega=\int\gamma|\nabla\Omega|^2.
\]

Only the symmetric part of `L` contributes to the quadratic affine term.

Thus vorticity variance is depleted by diffusion and replenished only by affine covariance stretching or the non-affine residual flux.

---

## 3. Exact strain-variance identity

The strain equation is

\[
D_sS+S^2+A^2=-\nabla^2P+\nu\Delta S.
\]

In the affine frame,

\[
\partial_sS+(Ly)\cdot\nabla S
=\nu\Delta S-r\cdot\nabla S-S^2-A^2-\nabla^2P.
\]

Therefore

\[
\boxed{
\begin{aligned}
V_S'
={}&-2\nu D_S
+\int\gamma|S-\bar S|_F^2\,r\cdot\nabla\log\gamma\\
&-2\int\gamma(S-\bar S):(S^2+A^2+\nabla^2P),
\end{aligned}
}
\]

with

\[
D_S=\int\gamma|\nabla S|_F^2.
\]

Thus strain residual variance can be maintained only by

1. residual transport through the adaptive Gaussian,
2. strain self-interaction,
3. the vorticity-quadratic `A^2` term,
4. pressure-Hessian fluctuation.

---

## 4. Gaussian Poincare becomes singular at the terminal point

Let `Sigma(s)` be the affine heat covariance.  Gaussian Poincare gives

\[
V_\omega\le\lambda_{\max}(\Sigma)D_\omega,
\qquad
V_S\le\lambda_{\max}(\Sigma)D_S.
\]

Assume a bounded accumulated affine-strain branch

\[
\boxed{
K_I:=\int_I|\operatorname{sym}L(s)|\,ds\le K.
}
\]

Then the affine transition singular values are bounded by `e^K`, and

\[
\boxed{
2\nu e^{-2K}(T-s)I
\preceq
\Sigma(s)
\preceq
2\nu e^{2K}(T-s)I.
}
\]

Hence

\[
\boxed{
\nu D_\omega
\ge c_Ke^{-0}\frac{V_\omega}{T-s},
\qquad
\nu D_S
\ge c_K\frac{V_S}{T-s}.
}
\]

The precise harmless constant is absorbed into `c_K>0`.

This is the terminal singular-coercivity mechanism.

---

## 5. First-hitting bounds on non-pressure maintenance terms

On a terminal first-hitting window,

\[
\|\Omega(s)\|_\infty\le1.
\]

Therefore `S` is uniformly bounded in BMO, and for Gaussian covariances of condition number at most `e^{4K}`, John-Nirenberg gives uniform finite weighted moments of the mean-free strain:

\[
\|S-\bar S\|_{L^p(\gamma)}\le C_{p,K}.
\]

The Gaussian creation/annihilation estimate together with

\[
\int\gamma r=0,
\qquad
\int\gamma|\nabla r|^2=\mathcal B_\gamma
\]

gives, schematically,

\[
\|r\cdot\nabla\log\gamma\|_{L^2(\gamma)}
\le C_K\sqrt{\mathcal B_\gamma}.
\]

Consequently the residual-transport, `A^2`, and mean-free cubic-strain terms are bounded by combinations of

\[
C_K,
\qquad
C_K\sqrt{\mathcal B_\gamma},
\qquad
C_K|\bar S|\mathcal B_\gamma.
\]

The affine mean itself is already accounted for in the accumulated affine-strain channel `K_I`.

---

## 6. Pressure-Hessian variance channel

Define

\[
\boxed{
\Pi_P(s)^2
=\int\gamma_s
\left|
\nabla^2P-(\nabla^2P)_{\gamma_s}
\right|_F^2.
}
\]

Because `S-bar S` has zero Gaussian mean,

\[
\left|
2\int\gamma(S-\bar S):\nabla^2P
\right|
\le2\sqrt{V_S}\,\Pi_P.
\]

Using the terminal Poincare coercivity,

\[
2\sqrt{V_S}\,\Pi_P
\le
\frac{c_K}{2(T-s)}V_S
+C_K(T-s)\Pi_P^2.
\]

Thus pressure fluctuation is naturally weighted by the remaining affine heat time.

---

## 7. Combined residual-variance inequality

Combining the previous estimates yields the schematic but typed inequality

\[
\boxed{
\mathcal B_\gamma'
+\frac{c_K}{T-s}\mathcal B_\gamma
\le
C_K
+C_K|\operatorname{sym}L|\mathcal B_\gamma
+C_K(T-s)\Pi_P(s)^2.
}
\]

All constants depend only on the bounded-affine distortion parameter and universal Calderon-Zygmund/Gaussian constants.

The pressure-Hessian term is the only explicitly retained non-affine forcing not already represented by `B_gamma` and the affine mean.

---

## 8. Terminal collapse under a weighted pressure budget

Assume on `[T-delta,T)`

\[
\int_{T-\delta}^{T}|\operatorname{sym}L(s)|ds\le K
\]

and

\[
\boxed{
\int_{T-\delta}^{T}
(T-s)\Pi_P(s)^2ds
\le C_P.
}
\]

An integrating-factor/Gronwall argument for the singular damping inequality gives

\[
\boxed{
\mathcal B_\gamma(s)
\le C_{K,C_P}(T-s)
}
\]

on a sufficiently short terminal sublayer, with the constant uniform along any family satisfying the displayed channel bounds.

This is a conditional uniform terminal-collapse lemma.

---

## 9. Consequence for the Gaussian residual Duhamel defect

The exact residual endpoint bound is

\[
\mathfrak R_\gamma
\le C\int
\|F(T,s)\|\,\|\Omega(s)\|_\infty
(1+\sqrt{\kappa(\Sigma(s))})
\sqrt{\mathcal B_\gamma(s)}\,ds.
\]

On the bounded-affine first-hitting branch all prefactors are bounded, so the terminal-collapse estimate yields

\[
\boxed{
\mathfrak R_{\gamma,[T-\delta,T]}
\le C_{K,C_P}\delta^{3/2}.
}
\]

Thus the residual endpoint defect cannot be generated in an arbitrarily thin terminal layer unless at least one of

\[
\boxed{
\text{affine-deformation concentration}
\quad\text{or}\quad
\text{weighted pressure-Hessian concentration}
}
\]

occurs.

---

## 10. Relation to the four exact residual channels

Because

\[
\mathcal B_\gamma
=D_{S,\rm shape}
+D_{S,\rm amp}
+\frac12D_{\omega,\rm proj}
+\frac12D_{\omega,\rm line},
\]

the terminal collapse is simultaneous for the sum of all four nonnegative channels.

In particular, no one of the four channels can remain order one all the way to the terminal delta-like observation scale while affine distortion and weighted pressure-Hessian forcing remain bounded.

This does not yet exclude order-one residual activity on an earlier portion of every first-hitting window.

---

## 11. Current remaining target

The active question is shifted backward in normalized time:

> Can order-one four-channel Gaussian residual variance be repeatedly regenerated on the earlier part of every first-hitting window while the terminal layer collapses and while all affine/reservoir/projective/energy channels remain compatible?

A next useful step is to combine the present terminal collapse with a time-slicing argument for the exact Duhamel formula, separating

1. an early affine/residual production region, and
2. a terminal Gaussian-collapse region.

If the early region alone must carry a fixed fraction of the endpoint defect, its Gaussian covariance is bounded away from zero and all four channels become ordinary fixed-resolution DSD variables, where cross-window packing and energy/strain budgets can be tested without the terminal degeneracy.

Status: **TERMINAL FOUR-CHANNEL COLLAPSE DERIVED CONDITIONALLY / EARLY-WINDOW REGENERATION REMAINS OPEN**.
