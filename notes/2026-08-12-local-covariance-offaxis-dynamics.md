# Off-axis vorticity energy dynamics relative to the local covariance axis

Date: 2026-08-12

Status: **DERIVED MATRIX DYNAMICS + DSD OFF-DIAGONAL AXIS-CONVERSION BRIDGE / OPEN CONVERSION CONTROL**.

This note evolves the local covariance-axis defect instead of treating it as a purely static descriptor.

The equations below are exact for smooth solutions and smooth moving cutoffs.  Suitable-weak extension of the vorticity-gradient form is not claimed here.

## 1. Vorticity tensor equation

Let

\[
Q=\omega\otimes\omega.
\]

From

\[
(\partial_t+u\cdot\nabla)\omega
=S\omega+\nu\Delta\omega,
\]

we obtain

\[
\boxed{
(\partial_t+u\cdot\nabla)Q
=S\omega\otimes\omega
+\omega\otimes S\omega
+\nu\Delta Q
-2\nu\sum_{k=1}^3
\partial_k\omega\otimes\partial_k\omega.
}
\]

## 2. Moving weighted covariance matrix

Let

\[
\varphi_r(x,t)=\phi_r(x-X(t))
\]

be a smooth moving observation weight and set

\[
\dot X=U(t).
\]

Define the unnormalized vorticity covariance

\[
N_r(t)
=
\int\varphi_rQ\,dx,
\]

and its trace

\[
E_r(t)
=
\operatorname{tr}N_r
=
\int\varphi_r|\omega|^2dx.
\]

Reynolds/local integration by parts gives the exact matrix budget

\[
\boxed{
\begin{aligned}
\dot N_r
&=
\int\varphi_r
(S\omega\otimes\omega
+\omega\otimes S\omega)dx\\
&\quad-2\nu
\int\varphi_r
\sum_k\partial_k\omega\otimes\partial_k\omega dx\\
&\quad+
\int Q\,(u-U)\cdot\nabla\varphi_r dx\\
&\quad+
\nu\int Q\,\Delta\varphi_r dx.
\end{aligned}
}
\]

This is the vorticity-covariance analogue of the moving weighted velocity-variance budget.

No pressure term appears because the vorticity equation eliminates pressure by curl.

## 3. Optimal-axis off-axis energy

Assume `E_r>0` and define

\[
C_r=N_r/E_r.
\]

Let the largest eigenvalue of `N_r` be

\[
\Lambda_1=E_r\mu_1
\]

with a normalized eigenvector `n`, assumed simple at the instant under consideration.

Define

\[
P_\perp=I-n\otimes n,
\qquad
\omega_\perp=P_\perp\omega.
\]

The optimal local off-axis enstrophy is

\[
\boxed{
D_\perp
=E_r-\Lambda_1
=E_r(1-\mu_1)
=\int\varphi_r|\omega_\perp|^2dx.
}
\]

Because the derivative of a simple largest eigenvalue satisfies

\[
\dot\Lambda_1=n^T\dot N_r n,
\]

we have

\[
\dot D_\perp
=\operatorname{tr}\dot N_r-n^T\dot N_rn.
\]

There is no explicit `dot n` term in this eigenvalue derivative formula.

## 4. Exact off-axis budget

Applying `tr(.)-n^T(.)n` to the matrix budget gives

\[
\boxed{
\begin{aligned}
\dot D_\perp
&+2\nu
\int\varphi_r
|\nabla\omega_\perp|^2dx\\
&=
2\int\varphi_r
\omega_\perp\cdot S\omega\,dx\\
&\quad+
\int|\omega_\perp|^2
(u-U)\cdot\nabla\varphi_r dx\\
&\quad+
\nu\int|\omega_\perp|^2
\Delta\varphi_r dx.
\end{aligned}
}
\]

Here `n` is constant with respect to the integration variable inside the single local covariance block at the instant, so

\[
P_\perp\partial_k\omega
=\partial_k(P_\perp\omega)
\]

for the spatial derivative appearing in this budget.

## 5. Self-stretching versus axis-conversion

Decompose

\[
\omega
=(n\cdot\omega)n+\omega_\perp.
\]

Then

\[
\boxed{
\omega_\perp\cdot S\omega
=
\omega_\perp\cdot S\omega_\perp
+(n\cdot\omega)
\omega_\perp\cdot P_\perp Sn.
}
\]

Define the local axis-conversion intensity

\[
\boxed{
\chi_n(x,t)
=|P_\perp S(x,t)n|.
}
\]

The two nonlinear production channels are therefore:

1. **off-axis self stretching**
   \[
   \mathcal S_\perp
   =2\int\varphi_r
   \omega_\perp\cdot S\omega_\perp dx;
   \]
2. **principal-to-off-axis conversion**
   \[
   \mathcal X_n
   =2\int\varphi_r
   (n\cdot\omega)
   \omega_\perp\cdot P_\perp Sn\,dx.
   \]

Thus

\[
2\int\varphi_r\omega_\perp\cdot S\omega
=\mathcal S_\perp+\mathcal X_n.
\]

## 6. Elementary conversion bound

Cauchy--Schwarz gives

\[
\begin{aligned}
|\mathcal X_n|
&\le
2
\left(
\int\varphi_r(n\cdot\omega)^2dx
\right)^{1/2}
\left(
\int\varphi_r
|\omega_\perp|^2\chi_n^2dx
\right)^{1/2}\\
&=
2(E_r\mu_1)^{1/2}
\left(
\int\varphi_r
|\omega_\perp|^2\chi_n^2dx
\right)^{1/2}.
\end{aligned}
\]

In particular, with

\[
\chi_{n,\infty}
=\|\chi_n\|_{L^\infty(\operatorname{supp}\varphi_r)},
\]

\[
\boxed{
|\mathcal X_n|
\le
2E_r
\sqrt{\mu_1(1-\mu_1)}
\chi_{n,\infty}.
}
\]

Hence when the covariance is nearly one-axis (`Pi=1-mu1` small), the direct rate at which strain can populate the off-axis sector is only `O(sqrt(Pi))` times the strain-axis conversion amplitude.

## 7. Axis-conversion geometry

If `n` is an eigenvector of the strain tensor at a point, then

\[
P_\perp Sn=0
\]

and the principal-to-off-axis conversion channel vanishes there.

Thus persistent growth of a nearly one-axis vorticity covariance requires either

- off-axis self stretching; or
- persistent misalignment between the best vorticity axis and the local strain eigenframe.

This adds a new off-diagonal entry to the DSD axis-property matrix:

\[
\boxed{
\text{vorticity principal axis}
\leftrightarrow
\text{strain eigenframe}.
}
\]

## 8. Normalized defect dynamics

Since

\[
\Pi_r=D_\perp/E_r,
\]

wherever `E_r>0`,

\[
\boxed{
\dot\Pi_r
=
\frac{\dot D_\perp}{E_r}
-\Pi_r\frac{\dot E_r}{E_r}.
}
\]

Therefore keeping `Pi_r` from decaying during enstrophy growth requires the off-axis budget to compete not only with its own diffusion, but also with the growth of total local enstrophy.

No closed sign estimate is presently obtained from this identity.

## 9. DSD dynamic matrix block

The local axis block becomes

\[
\boxed{
\mathcal A_{\omega,r}^{\rm dyn}
=
\left(
E_r,
\Pi_r,
\delta_r,
D_\perp,
\mathcal S_\perp,
\mathcal X_n,
\chi_n,
D_{\perp,\nu},
F_{\perp,\rm rel}
\right).
}
\]

where the last entries denote viscous off-axis dissipation and moving-window relative flux.

This is an explicit example of a DSD off-diagonal channel that is already present in the standard Navier--Stokes dynamics rather than added as new physics.

## 10. Next target

The local covariance regularity lemma showed that a residual singularity must keep

\[
\|\omega\|_2\sup_x\Pi_r
\]

unbounded on dangerous scales.

The present budget says this can happen only through

\[
\boxed{
\text{off-axis self stretching}
+\text{vorticity-axis/strain-axis conversion}
+\text{relative scale flux}
}
\]

outweighing off-axis diffusion and the normalization effect of total enstrophy growth.

A useful next inequality would show that one of these production channels forces an already controlled strain, occupancy, or higher-derivative gate.

Status: **OPEN OFF-AXIS PRODUCTION CONTROL**.
