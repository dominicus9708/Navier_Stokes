# Exact-kernel non-Gaussianity is bounded by weighted global enstrophy

Date: 2026-08-14

Status: **DERIVED. USING THE VELOCITY-REGRESSION AFFINE REFERENCE, THE MATCHED GAUSSIAN HAS EXACTLY THE SAME MEAN AND COVARIANCE AS THE TRUE ADJOINT KERNEL. ITS KL SHAPE DEFECT IS BOUNDED BY A SCALE-CRITICAL `tau^-1/2` GLOBAL-ENSTROPHY ACTION. GLOBAL REGULARITY NOT PROVED.**

## 1. Exact kernel and velocity regression

Let `rho_tau` be the exact backward-age adjoint density and define

\[
m=E_\rho X,
\qquad
Y=X-m,
\qquad
\Sigma=E_\rho[Y\otimes Y].
\]

Let

\[
\bar U=E_\rho U
\]

and define the velocity-regression matrix

\[
\boxed{
M
=
E_\rho[(U-\bar U)\otimes Y]\Sigma^{-1}.
}
\]

Then the exact covariance obeys

\[
\boxed{
\Sigma'
=-M\Sigma-\Sigma M^T+2\nu I.
}
\]

## 2. Regression-affine Gaussian reference has the same covariance

Consider the affine diffusion

\[
 dY_\tau
=
[-\bar U(\tau)-M(\tau)(Y_\tau-m(\tau))]d\tau
+\sqrt{2\nu}\,dW_\tau.
\]

Its mean obeys the same equation as the exact kernel mean,

\[
m'=-\bar U,
\]

and its covariance obeys exactly the same equation

\[
\Sigma'
=-M\Sigma-\Sigma M^T+2\nu I.
\]

Starting from the same terminal delta, its one-time law is therefore precisely the Gaussian

\[
\boxed{
G_\tau=N(m(\tau),\Sigma(\tau))
}
\]

with the **same mean and covariance** as the true kernel.

Thus the KL divergence

\[
\boxed{
\mathfrak D_K(\tau)
=D_{\rm KL}(\rho_\tau\|G_\tau)
}
\]

is exactly the covariance-normalized non-Gaussian shape defect.

## 3. Regression residual is the cheapest affine drift difference

Define

\[
\boxed{
 r_M
=U-\bar U-MY.
}
\]

By least squares,

\[
E_\rho[r_M\otimes Y]=0
\]

and

\[
\boxed{
E_\rho|r_M|^2
=
\min_A E_\rho|U-\bar U-AY|^2.
}
\]

In particular,

\[
\boxed{
E_\rho|r_M|^2
\le
E_\rho|U-\bar U|^2
\le
E_\rho|U|^2.
}
\]

## 4. Girsanov / entropy-defect action bound

The exact diffusion and the regression-affine reference have the same diffusion coefficient `sqrt(2 nu)` and differ in drift by `-r_M`.

Hence, under the standard finite-energy absolute-continuity conditions,

\[
\boxed{
\mathfrak D_K(\tau)
\le
\frac1{4\nu}
\int_0^\tau
E_{\rho_s}|r_M(s)|^2ds.
}
\]

The same inequality can also be obtained from the deterministic relative-entropy production identity.

## 5. Density ceiling plus Sobolev controls the regression action

The exact kernel satisfies the drift-independent ultracontractive ceiling

\[
\boxed{
\|\rho_s\|_\infty
\le C(\nu s)^{-3/2}.
}
\]

For a probability density,

\[
\|\rho\|_{3/2}
\le
\|\rho\|_\infty^{1/3}.
\]

Therefore

\[
\begin{aligned}
E_\rho|U|^2
&=\int\rho|U|^2dx\\
&\le
\|\rho\|_{3/2}\|U\|_6^2\\
&\le
C\|\rho\|_\infty^{1/3}
\|\nabla U\|_2^2.
\end{aligned}
\]

For divergence-free whole-space velocity,

\[
\|\nabla U\|_2^2
=\|\Omega\|_2^2
=:E_\omega.
\]

Hence

\[
\boxed{
E_{\rho_s}|r_M|^2
\le
C(\nu s)^{-1/2}E_\omega(s).
}
\]

## 6. Non-Gaussianity bound by weighted enstrophy

Substituting into the path/entropy action inequality,

\[
\boxed{
\mathfrak D_K(\tau)
\le
C\nu^{-3/2}
\int_0^\tau
s^{-1/2}E_\omega(s)ds.
}
\]

Thus the exact adjoint kernel cannot acquire a fixed non-Gaussian shape defect unless it accumulates a fixed amount of the scale-critical weighted global-enstrophy action

\[
\boxed{
\mathfrak Z_K(\tau)
:=
\int_0^\tau s^{-1/2}E_\omega(s)ds.
}
\]

## 7. Navier--Stokes scaling of the new action

Under terminal first-hitting normalization by vorticity height `W`, normalized age and physical age are related by

\[
s=W\,\delta t,
\]

while normalized and physical enstrophy satisfy

\[
E_{\omega,\rm norm}(s)
=W^{-1/2}E_{\omega,\rm phys}(t).
\]

Therefore

\[
\boxed{
\int s^{-1/2}E_{\omega,\rm norm}(s)ds
=
\int (\delta t)^{-1/2}
E_{\omega,\rm phys}(t)d(\delta t).
}
\]

The quantity is scale critical. This explains why kernel-shape deformation survives the elementary kinetic-energy dissipation budget: the temporal half-power is the remaining critical weight.

## 8. Consequence for the proof tree

Kernel non-Gaussianity is no longer an unspecified transport branch. It is routed to

\[
\boxed{
\text{fixed KL shape defect}
\Longrightarrow
\text{fixed }\tau^{-1/2}\text{-weighted global enstrophy action}.
}
\]

The only remaining question is whether a hypothetical singular first-hitting cascade can repeatedly sustain this critical weighted action on disjoint/nested terminal windows.

If it cannot, the exact kernel remains asymptotically Gaussian in the covariance-normalized sense and the Gaussian/Hermite closure applies.

If it can, the singular survivor is forced into a sharply identified global critical-enstrophy concentration channel rather than a local observation artifact.

Status: **KERNEL SHAPE DEGENERATION REDUCED TO THE CRITICAL WEIGHTED ENSTROPHY ACTION `int tau^-1/2 E_omega` / GLOBAL REGULARITY NOT PROVED.**
