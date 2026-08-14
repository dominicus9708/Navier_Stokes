# Forced enstrophy escalation routes exactly to the positive middle-strain channel

Date: 2026-08-14

Status: **EXACT STRAIN IDENTITY + EXTERNAL MIDDLE-EIGENVALUE ANCHOR / ESCALATION BRANCH TYPED, NOT EXCLUDED**.

## 1. Exact whole-space strain identities

For smooth decaying incompressible flow on `R^3`,

\[
\|S\|_2^2
=\frac12\|\omega\|_2^2.
\]

The strain evolution identity is

\[
\boxed{
\frac d{dt}\|S\|_2^2
=-2\nu\|\nabla S\|_2^2
-4\int_{\mathbb R^3}\det S\,dx.
}
\]

Comparing with the vorticity enstrophy identity gives

\[
\boxed{
\int S\omega\cdot\omega\,dx
=-4\int\det S\,dx.
}
\]

Thus the nonlocal-looking global vortex-stretching production has an exactly local strain-determinant representation after integration over the whole space.

## 2. Positive middle eigenvalue

Let

\[
\lambda_1\le\lambda_2\le\lambda_3,
\qquad
\lambda_1+\lambda_2+\lambda_3=0.
\]

If `lambda_2<=0`, then `det S>=0`, so `-det S<=0` and this region cannot contribute positively to the determinant-side enstrophy production.

If `lambda_2>0`, then

\[
-\det S
=(-\lambda_1)\lambda_2\lambda_3.
\]

Using

\[
(-\lambda_1)\lambda_3
\le\frac12(\lambda_1^2+\lambda_3^2)
\le\frac12|S|^2,
\]

we get

\[
\boxed{
-\det S
\le\frac12\lambda_2^+|S|^2.
}
\]

Hence

\[
\boxed{
\int S\omega\cdot\omega
\le
2\int\lambda_2^+|S|^2.
}
\]

## 3. Apply to a forced enstrophy escalation

Suppose on a time interval `[t_0,t_1]` the global enstrophy rises from `E_0` to `E_1>E_0`, where `E=||omega||_2^2`.

Since `||S||_2^2=E/2`, integration of the strain identity gives

\[
-4\int_{t_0}^{t_1}\int\det S
=
\frac12(E_1-E_0)
+2\nu\int_{t_0}^{t_1}\|\nabla S\|_2^2dt.
\]

Therefore

\[
\boxed{
\int_{t_0}^{t_1}\int\lambda_2^+|S|^2dxdt
\ge
\frac14(E_1-E_0).
}
\]

(up to the fixed normalization convention for enstrophy; the key point is a universal positive constant).

Thus the global enstrophy escalation forced by a fresh Gaussian residual pulse necessarily creates a positive middle-strain production budget of comparable size.

## 4. External regularity anchor

Evan Miller's middle-eigenvalue criterion states that for

\[
\frac2p+\frac3q=2,
\qquad
\frac32<q\le\infty,
\]

a finite-time blow-up requires divergence of the scale-critical quantity

\[
\int_0^{T_*}\|\lambda_2^+(t)\|_{L^q}^pdt.
\]

Primary source: Evan Miller, *A regularity criterion for the Navier-Stokes equation involving only the middle eigenvalue of the strain tensor*, arXiv:1710.05569; final version in Archive for Rational Mechanics and Analysis.

The present result does not improve that theorem by itself. It shows that the DSD/Gaussian residual survivor is forced directly into the same established critical channel.

## 5. Revised branch interpretation

The chain is now

\[
\boxed{
\text{fresh intermediate residual pulse}
\Rightarrow
\text{global enstrophy escalation}
\Rightarrow
\text{positive }\lambda_2\text{ strain production}.
}
\]

Therefore `global enstrophy growth` should no longer be kept as a separate proof-tree branch. It is a quantitative route into the middle-eigenvalue/strain branch already present in the project.

A hypothetical singular survivor must repeatedly activate this channel strongly enough to meet the known scale-critical blow-up necessity.

## 6. Remaining obligation

This routing is not a contradiction. To close the branch one still needs an additional strict margin, for example

- a subcritical gain in the positive-middle-strain spacetime norm;
- geometric depletion/alignment that reduces the determinant production;
- higher-chaos/sparseness forcing that activates a known regularity gate;
- or a compactness/rigidity argument excluding repeated near-critical saturation.

Status: **ENSTROPHY-ESCALATION BRANCH MERGED INTO ESTABLISHED MIDDLE-STRAIN CRITICAL BRANCH / FINAL CRITICAL SATURATION STILL OPEN**.
