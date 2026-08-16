# Pathwise Malliavin deformation--diffusion area bound without a spatial-affine hypothesis

Date: 2026-08-16

Status: **EXACT PATHWISE MATRIX THEOREM FOR THE ADDITIVE-NOISE STOCHASTIC FLOW. THE ROTATION-INDEPENDENT AFFINE DEFORMATION--DIFFUSION AREA ARGUMENT EXTENDS TO EACH ARBITRARY NAVIER--STOKES STOCHASTIC TRAJECTORY. THE REMAINING STEP IS A MALLIAVIN/SEMIGROUP TRANSFER FROM THE RANDOM GRAMIAN TO A PRECURSOR SMOOTHING ESTIMATE. GLOBAL REGULARITY NOT PROVED.**

## 1. Stochastic flow derivative along one history

Consider the smooth pre-singular incompressible stochastic flow

\[
dX_s=U(X_s,s)ds+\sqrt{2\nu}\,dW_s.
\]

Fix one Brownian realization and one starting label. Because the noise is additive, its spatial derivative is zero. Therefore the flow derivative

\[
F(s)=D_aX_s
\]

obeys pathwise

\[
\boxed{F'(s)=L(s)F(s),\qquad L(s)=\nabla U(X_s,s).}
\]

Incompressibility gives

\[
\boxed{\det F(s)=1.}
\]

Thus, for the matrix geometry alone, every nonlinear stochastic trajectory is a time-dependent volume-preserving affine matrix path.

No assumption that `grad U` is spatially constant is used below.

---

## 2. Pulled-back noise Gramian

Set the initial time to zero for notation and let the final time be `T`. Define

\[
\boxed{
C_T
=\int_0^T
F(s)^{-1}F(s)^{-T}ds.
}
\]

This is the same accumulated metric that appears in the exact affine heat calculation, but it is now defined pathwise along a completely nonlinear stochastic trajectory.

Let

\[
A_T=F(T)^{-1}F(T)^{-T}.
\]

Write

\[
h(s)=\|\operatorname{sym}L(s)\|_{op},
\qquad
H(s)=\int_s^T h(\tau)d\tau.
\]

---

## 3. Backward singular-value comparison is pathwise

Let

\[
\Phi(T,s)=F(T)F(s)^{-1}.
\]

Since only the symmetric part of `L` changes singular values,

\[
\sigma_{\min}(\Phi(T,s))
\ge e^{-H(s)}.
\]

For every vector `z`,

\[
F(s)^{-T}z
=\Phi(T,s)^TF(T)^{-T}z.
\]

Hence

\[
|F(s)^{-T}z|
\ge
e^{-H(s)}|F(T)^{-T}z|.
\]

Therefore, pathwise in Loewner order,

\[
\boxed{
F(s)^{-1}F(s)^{-T}
\succeq
e^{-2H(s)}A_T.
}
\]

Integrating,

\[
\boxed{
C_T\succeq c_HA_T,
\qquad
c_H=\int_0^T e^{-2H(s)}ds.
}
\]

This step is identical to the affine proof but uses only the one-dimensional-in-time matrix ODE along the selected path.

---

## 4. Replace c_H by pathwise strain-square action

Define

\[
K=\int_0^T h(s)ds,
\qquad
J=\int_0^T h(s)^2ds.
\]

Because

\[
\frac d{ds}e^{-H(s)}
=h(s)e^{-H(s)},
\]

we have

\[
\int_0^T h(s)e^{-H(s)}ds
=1-e^{-K}.
\]

Cauchy--Schwarz gives

\[
(1-e^{-K})^2
\le
Jc_H.
\]

Let the final largest singular stretch be

\[
\boxed{q_p=\|F(T)\|_{op}.}
\]

Since `q_p<=e^K`,

\[
1-e^{-K}\ge1-q_p^{-1}.
\]

Thus

\[
\boxed{
c_H
\ge
\frac{(1-q_p^{-1})^2}{J}.}
\]

Again, there is no spatial-affine hypothesis.

---

## 5. Two-dimensional pulled-back diffusion area

Let the singular values of `F(T)` be

\[
\sigma_1=q_p\ge\sigma_2\ge\sigma_3>0.
\]

Since their product is one, the two largest eigenvalues of

\[
A_T=F(T)^{-1}F(T)^{-T}
\]

have product exactly

\[
\boxed{q_p^2.}
\]

Let

\[
0<\mu_1\le\mu_2\le\mu_3
\]

be the eigenvalues of `C_T`. From `C_T>=c_H A_T`, min--max gives

\[
\boxed{
\mu_2\mu_3
\ge
c_H^2q_p^2.
}
\]

Hence

\[
\boxed{
(\mu_2\mu_3)^{1/2}
\ge
\frac{(1-q_p^{-1})^2}{J}
q_p.
}
\]

For `q_p>=2`,

\[
\boxed{
(\mu_2\mu_3)^{1/2}
\gtrsim
\frac{q_p}{J}.
}
\]

This is the pathwise nonlinear deformation--diffusion area theorem.

---

## 6. Identification with the Malliavin covariance

For additive noise, the Malliavin derivative of the terminal position with respect to a noise impulse at time `s` is

\[
D_s^{\rm Mall}X_T
=\sqrt{2\nu}\,\Phi(T,s).
\]

Therefore the terminal Malliavin covariance is

\[
\begin{aligned}
\mathcal M_T
&=2\nu\int_0^T
\Phi(T,s)\Phi(T,s)^Tds\\
&=2\nu F(T)
\left[\int_0^T F(s)^{-1}F(s)^{-T}ds\right]
F(T)^T.
\end{aligned}
\]

Thus exactly

\[
\boxed{
\mathcal M_T
=2\nu F(T)C_TF(T)^T.
}
\]

Equivalently,

\[
\boxed{
C_T
=(2\nu)^{-1}
F(T)^{-1}\mathcal M_TF(T)^{-T}.
}
\]

So the matrix `C_T` is not merely an affine-coordinate artifact. It is the terminal Malliavin covariance pulled back to the initial/material tangent space.

---

## 7. Consequence for active stochastic Cauchy histories

The stochastic-Cauchy active-tail lemma gives, on an active history contributing order one to a terminal coherent point,

\[
q_p\gtrsim q_\beta.
\]

Therefore every such history satisfies

\[
\boxed{
(\mu_2(C_T)\mu_3(C_T))^{1/2}
\gtrsim
\frac{q_\beta}{J_p}
}
\]

where

\[
J_p
=\int\|S(X_s,s)\|_{op}^2ds.
\]

Multiplying by `nu` gives the corresponding two-dimensional noise-area scale.

Thus a large-deformation history cannot simultaneously have

- small pathwise strain-square action; and
- small transverse accumulated diffusion area.

The deformation--diffusion compensation is pathwise and survives arbitrary spatial non-affinity and arbitrary eigendirection rotation.

---

## 8. What this removes

Previously the rotation-independent `J times precursor` theorem was available only for a spatially affine linear PDE, and the full proof required a nonlinear affine-comparison theorem.

The present result shows that the **matrix geometric half** of that theorem needs no such comparison:

\[
\boxed{
\text{large full nonlinear stochastic deformation}
\Longrightarrow
\text{large pathwise pulled-back Malliavin diffusion area unless }J_p\text{ is large}.
}
\]

Therefore spatial non-affinity cannot evade the deformation--diffusion area relation itself.

---

## 9. Precise remaining analytic bridge

What is still missing is not a matrix comparison. It is a probabilistic smoothing inequality converting the random pathwise Gramian into control of the weighted Cauchy expectation

\[
\boxed{
\Omega_T(x)
=E\left[F(T)\Omega_-(A_T(x))\right].
}
\]

In the exact affine model `C_T` is deterministic and the endpoint law is Gaussian, giving the mixed-norm heat estimate immediately.

In the nonlinear flow `C_T` and `F(T)` are random and correlated with the stochastic ancestor position and with `Omega_-`. A proof needs a Malliavin/Bismut/integration-by-parts estimate that retains the two-dimensional Gramian gain despite these correlations.

A target estimate would schematically have the form

\[
\boxed{
|E[F(T)f(A_T)]|
\lesssim
E\left[
\frac{q_p^{1/2}J_p^{1/2}}
{\nu^{1/2}}
\mathcal R_{\Pi}(f;\varpi)
\right]
+\text{controlled Malliavin-derivative errors},
}
\]

where `R_Pi` is a transverse precursor reservoir descriptor. The error terms must be expressed in the already active deformation-weighted palinstrophy / Hessian / residual-score channels.

---

## 10. Updated frontier

The former `nonlinear affine transfer` problem is sharpened to

\[
\boxed{
\textbf{random-Gramian Malliavin smoothing transfer}
}
\]

because the deformation--diffusion area theorem itself is already fully nonlinear and pathwise.

The hoped-for final structure is

\[
\boxed{
\text{large Cauchy deformation}
\Rightarrow
\begin{cases}
J_p\text{ large},\\
\text{large Malliavin diffusion area}\to\text{large precursor reservoir},\\
\text{or Malliavin transfer error}\to\text{weighted derivative/Hessian channel}.
\end{cases}
}
\]

Overall status: **SPATIAL-AFFINE ASSUMPTION REMOVED FROM THE MATRIX DEFORMATION--DIFFUSION BARRIER / FINAL BRIDGE = RANDOM MALLIAVIN GRAMIAN TO PRECURSOR SMOOTHING.**
