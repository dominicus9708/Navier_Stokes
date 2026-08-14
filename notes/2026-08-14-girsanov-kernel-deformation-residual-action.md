# Girsanov control of exact-kernel deformation by residual transport action

Date: 2026-08-14

Status: **DERIVED UNDER THE STANDARD ABSOLUTE-CONTINUITY / FINITE-ENERGY HYPOTHESES FOR THE SMOOTH PRE-SINGULAR DIFFUSIONS. THE KL DEFORMATION OF THE TRUE ADJOINT KERNEL FROM ITS MATCHED AFFINE GAUSSIAN IS BOUNDED BY AN EXACT KERNEL-WEIGHTED RESIDUAL-VELOCITY ACTION. KERNEL NON-GAUSSIANITY IS THEREFORE NOT A FREE ESCAPE. GLOBAL REGULARITY NOT PROVED.**

## 1. Exact backward-age diffusion

Use backward age

\[
\tau=T-s.
\]

The exact adjoint density is the one-time law of the diffusion

\[
\boxed{
 dX_\tau
=-U(X_\tau,T-\tau)d\tau
+\sqrt{2\nu}\,dW_\tau,
\qquad
X_0=x_*.
}
\]

Its density is

\[
\rho_\tau(x)=K(x,T-\tau;x_*,T).
\]

Define its mean

\[
 m_K(\tau)=E[X_\tau]
\]

and the exact kernel-weighted velocity and gradient means

\[
\boxed{
\bar U_K(\tau)=\int\rho_\tau U\,dx,
\qquad
L_K(\tau)=\int\rho_\tau\nabla U\,dx.
}
\]

Incompressibility gives `tr L_K=0`.

The kernel mean obeys

\[
\boxed{
 m_K'(\tau)=-\bar U_K(\tau).
}
\]

## 2. Matched affine reference diffusion

Define the time-dependent affine reference drift

\[
\boxed{
 b_{\rm aff}(x,\tau)
=-\bar U_K(\tau)
-L_K(\tau)(x-m_K(\tau)).
}
\]

Let `Y_tau` solve

\[
 dY_\tau
=b_{\rm aff}(Y_\tau,\tau)d\tau
+\sqrt{2\nu}\,dW_\tau,
\qquad
Y_0=x_*.
\]

Because the coefficients are affine and deterministic once the terminal point and solution are fixed, the law of `Y_tau` is Gaussian. Its mean is exactly `m_K(tau)` and its covariance `Sigma_aff` solves

\[
\boxed{
\Sigma_{\rm aff}'
=-L_K\Sigma_{\rm aff}
-\Sigma_{\rm aff}L_K^T
+2\nu I,
\qquad
\Sigma_{\rm aff}(0)=0.
}
\]

Thus this is the exact affine-Gaussian reference naturally associated with the true kernel-weighted first two velocity-gradient descriptors.

## 3. Residual drift

Define the kernel-centered affine residual velocity

\[
\boxed{
 r_K(x,\tau)
=U(x,T-\tau)
-\bar U_K(\tau)
-L_K(\tau)(x-m_K(\tau)).
}
\]

Then

\[
\boxed{
\int\rho_\tau r_Kdx=0,
\qquad
\int\rho_\tau\nabla r_Kdx=0.
}
\]

The exact and affine backward-age drifts differ by

\[
\boxed{
 b_{\rm exact}-b_{\rm aff}=-r_K.
}
\]

## 4. Path-space relative entropy

Let `P` be the path law of `X` on `[0,tau]` and `P_aff` the path law of `Y`.

For two diffusions with the same nondegenerate diffusion coefficient `sqrt(2 nu) I` and the same initial point, Girsanov's theorem gives, under the standard finite-energy/Novikov hypotheses,

\[
\boxed{
D_{\rm KL}(P\|P_{\rm aff})
=
\frac1{4\nu}
E_P\int_0^\tau
|r_K(X_s,s)|^2ds.
}
\]

Since the one-time marginal is a measurable projection of path space, relative entropy decreases under projection. Therefore

\[
\boxed{
D_{\rm KL}(\rho_\tau\|\gamma_{{\rm aff},\tau})
\le
\frac1{4\nu}
\int_0^\tau
\int\rho_s(x)|r_K(x,s)|^2dxds,
}
\]

where `gamma_aff,tau` is the endpoint affine Gaussian law.

Define the exact residual transport action

\[
\boxed{
\mathfrak A_{\rm tr}(\tau)
:=
\frac1{4\nu}
\int_0^\tau
\langle|r_K|^2\rangle_{K,s}ds.
}
\]

Then simply

\[
\boxed{
D_{\rm KL}(K_\tau\|G_{{\rm aff},\tau})
\le
\mathfrak A_{\rm tr}(\tau).
}
\]

## 5. Small transport action gives quantitative kernel closeness

Pinsker's inequality gives

\[
\boxed{
\|K_\tau-G_{{\rm aff},\tau}\|_{L^1}
\le
\sqrt{2\mathfrak A_{\rm tr}(\tau)}.
}
\]

Hence every bounded observable `F` satisfies

\[
\boxed{
|\langle F\rangle_K-\langle F\rangle_{G_{\rm aff}}|
\le
\|F\|_\infty
\sqrt{2\mathfrak A_{\rm tr}}.
}
\]

In particular, on a terminal first-hitting interval where

\[
\|\Omega\|_\infty\le1,
\]

the Gaussian and exact-kernel vorticity means differ by at most

\[
\boxed{
|\bar\Omega_K-\bar\Omega_{G_{\rm aff}}|
\le
\sqrt{2\mathfrak A_{\rm tr}}.
}
\]

Thus a large discrepancy in the tracked mean vorticity requires non-negligible residual transport action.

For unbounded observables such as strain, total-variation control alone is insufficient; a truncation/moment or entropy-inequality step is still required. That issue is typed separately rather than hidden.

## 6. Large kernel deformation is a residual-velocity event

Conversely, if for some fixed `delta>0`

\[
D_{\rm KL}(K_\tau\|G_{{\rm aff},\tau})\ge\delta,
\]

then necessarily

\[
\boxed{
\int_0^\tau
\langle|r_K|^2\rangle_{K,s}ds
\ge
4\nu\delta.
}
\]

Therefore the exact kernel cannot become strongly non-Gaussian relative to the matched affine process without accumulating a definite amount of residual transport energy along the same transition law.

This converts the qualitative `kernel deformation` escape into a quantitative action channel.

## 7. Relation to the exact kernel source state

The exact kernel-weighted stretching decomposition is

\[
\langle S\Omega\rangle_K
=
\bar S_K\bar\Omega_K
+J_K,
\qquad
|J_K|\le B_K/\sqrt2.
\]

The present result adds a distinct transport-geometry ledger:

\[
\boxed{
\text{source size}: B_K,
\qquad
\text{kernel deformation}: \mathfrak A_{\rm tr}.
}
\]

Thus nonlinear transport has two possible effects, neither free:

1. it changes the physical stretching state, measured by `B_K`;
2. it deforms the transition density away from the affine Gaussian, measured by `A_tr`.

It does **not** create an additional vorticity source beyond stretching.

## 8. Remaining conversion problem

The new inequality does not yet prove that

\[
\mathfrak A_{\rm tr}
\]

is globally summable in physical variables. The residual velocity action is critical and can be concentrated on large spatial scales.

The next target is therefore to connect

\[
\langle|r_K|^2\rangle_K
\]

to one of the already finite/packed quantities:

- kernel-weighted gradient variance `B_K` through a Poincare/log-Sobolev bound;
- global kinetic energy through the kernel density ceiling and a controlled affine subtraction;
- high-Hermite / shell transport when such a functional inequality fails.

This is now a precise functional-geometric problem rather than an unspecified nonlinear mixing branch.

Status: **KERNEL NON-GAUSSIANITY CHARGED TO EXACT RESIDUAL TRANSPORT ACTION BY GIRSANOV + DATA PROCESSING / SMALL ACTION IMPLIES TOTAL-VARIATION CLOSENESS TO THE MATCHED AFFINE GAUSSIAN / REMAINING STEP = CONVERT RESIDUAL TRANSPORT ACTION TO THE EXISTING DISSIPATION OR HIGH-CURVATURE LEDGER / GLOBAL REGULARITY NOT PROVED.**
