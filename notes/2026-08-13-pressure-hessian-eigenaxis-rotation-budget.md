# Pressure-Hessian budget for compressive eigenaxis rotation at first hitting

Date: 2026-08-13

Status: **DERIVED GLOBAL `L2` PRESSURE-HESSIAN BOUND + ROTATION-RESERVOIR COROLLARY / GLOBAL ENSTROPHY SUMMABILITY STILL OPEN**.

The compressive-eigenaxis identity leaves an off-diagonal pressure Hessian as one mechanism that can rotate the hard biaxial extensional plane.  At first-hitting normalization this pressure channel is controlled in global `L2` by the normalized global enstrophy reservoir.

Thus rapid eigenaxis rotation cannot be attributed to an arbitrary untyped pressure term: it must be paid by global normalized vorticity mass, normal-vorticity leakage, or a high-derivative viscous channel.

---

## 1. Pressure Poisson source

For smooth incompressible Navier--Stokes,

\[
-\Delta p
=\partial_i u_j\,\partial_j u_i
=\operatorname{tr}[(\nabla u)^2].
\]

With

\[
\nabla u=S+A
\]

and symmetric/skew orthogonality,

\[
\operatorname{tr}[(\nabla u)^2]
=\operatorname{tr}(S^2)+\operatorname{tr}(A^2).
\]

Since

\[
A^2=\frac14(\omega\otimes\omega-|\omega|^2I),
\]

\[
\operatorname{tr}(A^2)=-\frac12|\omega|^2.
\]

Therefore

\[
\boxed{
-\Delta p
=|S|^2-\frac12|\omega|^2.
}
\]

---

## 2. Hessian as a zero-order Calderon--Zygmund transform of the quadratic source

On `R3`,

\[
\nabla^2p
=\mathcal R_{ij}
\left(
|S|^2-\frac12|\omega|^2
\right)
\]

up to sign/operator convention, where `R_ij` is a matrix of second-order Riesz transforms.

Hence

\[
\boxed{
\|\nabla^2p\|_2
\le
C
\left\|
|S|^2-\frac12|\omega|^2
\right\|_2.
}
\]

By the triangle inequality,

\[
\|\nabla^2p\|_2
\le
C(\|S\|_4^2+\|\omega\|_4^2).
\]

---

## 3. Replace strain `L4` by vorticity `L4`

The strain is a zero-order singular-integral transform of vorticity, so for `1<p<infinity`,

\[
\|S\|_p\le C_p\|\omega\|_p.
\]

At `p=4`,

\[
\boxed{
\|\nabla^2p\|_2
\le C\|\omega\|_4^2.
}
\]

This is a standard global pressure-Hessian estimate.

---

## 4. First-hitting normalization

On a first-hitting normalized window,

\[
\boxed{\|\Omega\|_\infty\le1.}
\]

Let

\[
\mathfrak E=\|\Omega\|_2^2.
\]

Interpolation gives

\[
\|\Omega\|_4^4
\le
\|\Omega\|_\infty^2\|\Omega\|_2^2
\le
\mathfrak E.
\]

Therefore

\[
\|\Omega\|_4^2
\le
\mathfrak E^{1/2}
=\|\Omega\|_2.
\]

Thus the normalized pressure satisfies

\[
\boxed{
\|\nabla^2P\|_2
\le C\|\Omega\|_2
=C\mathfrak E^{1/2}.
}
\]

So a large global `L2` pressure Hessian requires a large normalized global enstrophy reservoir.

---

## 5. Insert into the compressive-axis rotation identity

For a simple compressive strain eigenvector `n`, eigengap

\[
g=\lambda_2-\lambda_1>0,
\]

the exact pointwise inequality is

\[
\begin{aligned}
g|D_tn|
\le{}&
|P_{n^\perp}(\nabla^2P)n|\\
&+\frac14|\Omega\cdot n||\Omega_\perp|\\
&+\nu|P_{n^\perp}(\Delta S)n|.
\end{aligned}
\]

Suppose on a local observation region `B`,

\[
g\ge g_0>0.
\]

Integrating and using Cauchy--Schwarz on the pressure and viscous terms gives

\[
\boxed{
\begin{aligned}
g_0\int_B|D_tn|
\le{}&
C|B|^{1/2}\|\Omega\|_2\\
&+\frac14
\int_B|\Omega\cdot n||\Omega_\perp|\\
&+C\nu|B|^{1/2}\|\Delta\Omega\|_2.
\end{aligned}
}
\]

The last step uses that `Delta S` is another zero-order singular-integral transform of `Delta Omega`.

---

## 6. Covariance form of the normal-vorticity leakage

If `n` is approximately constant on `B`, define

\[
E_B=\int_B|\Omega|^2,
\]

\[
c_-=\frac1{E_B}\int_B|\Omega\cdot n|^2.
\]

Then

\[
\int_B|\Omega_\perp|^2
=E_B(1-c_-).
\]

Therefore

\[
\boxed{
\int_B|\Omega\cdot n||\Omega_\perp|
\le
E_B\sqrt{c_-(1-c_-)}.
}
\]

Hence

\[
\boxed{
\begin{aligned}
g_0\int_B|D_tn|
\le{}&
C|B|^{1/2}\mathfrak E^{1/2}\\
&+\frac14E_B\sqrt{c_-(1-c_-)}\\
&+C\nu|B|^{1/2}\|\Delta\Omega\|_2.
\end{aligned}
}
\]

---

## 7. Biaxial hard-branch interpretation

For

\[
S\approx a(I-3n\otimes n),
\]

the eigengap is

\[
g\approx3a.
\]

Maximal affine covariance coupling requires

\[
c_-\ll1.
\]

Thus, in the source-optimal extensional-plane branch, the vorticity leakage term is depleted.

Large material rotation of the compressive axis must then come from

\[
\boxed{
\text{large normalized global enstrophy}
\quad\text{or}\quad
\text{large }\|\Delta\Omega\|_2
\quad\text{or}\quad
\text{loss of extensional-plane covariance}.
}
\]

This types the previously unstructured pressure-rotation escape.

---

## 8. Spacetime version

On a normalized time interval `I`, integrate the spatial estimate:

\[
\begin{aligned}
g_0
\int_I\int_B|D_tn|
\lesssim{}&
|B|^{1/2}
\int_I\mathfrak E(s)^{1/2}ds\\
&+
\int_I E_B(s)\sqrt{c_-(s)(1-c_-(s))}ds\\
&+
\nu|B|^{1/2}
\int_I\|\Delta\Omega(s)\|_2ds.
\end{aligned}
\]

If the interval length is bounded, Cauchy--Schwarz converts the last term to the existing V2 spacetime channel.

The first term is a normalized global-enstrophy-time reservoir; whether repeated blow-up-scaled windows can pay it indefinitely remains open because the physical energy-dissipation weight shrinks with the natural scale.

---

## 9. Claim boundary

This estimate does not show that the pressure-Hessian channel is small.  It only converts it into a previously recognizable global normalized-enstrophy reservoir.

It also uses a global `L2` pressure estimate; a sharper local pressure-Hessian decomposition may improve the result.

Status: **PRESSURE-HESSIAN ROTATION TYPED BY GLOBAL ENSTROPHY / V2 / NORMAL LEAKAGE; SUMMABILITY CLOSURE OPEN**.
