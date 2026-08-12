# Projective vorticity dispersion: an axis-choice-free covariance gate

Date: 2026-08-13

Status: **DERIVED COVARIANCE IDENTITY + COROLLARY OF EXTERNAL MILLER CRITERION / GLOBAL REGULARITY NOT PROVED**.

This note removes the need to choose a principal vorticity axis when measuring global directional dispersion. The external regularity theorem is Evan Miller's locally anisotropic vorticity criterion (arXiv:2002.02152). The identities and comparison estimates below are elementary consequences of the vorticity covariance matrix.

No novelty claim is made without a separate literature audit.

## 1. Global covariance and axis defect

Let

\[
E_\omega(t)=\|\omega(t)\|_2^2
\]

and, whenever `E_omega>0`, define

\[
\mathsf C_\omega
=
\frac{1}{E_\omega}
\int_{\mathbb R^3}\omega\otimes\omega\,dx.
\]

Then `C_omega` is symmetric positive semidefinite and

\[
\operatorname{tr}\mathsf C_\omega=1.
\]

Let

\[
\mu_1\ge\mu_2\ge\mu_3\ge0,
\qquad
\mu_1+\mu_2+\mu_3=1,
\]

and retain the previous optimal-axis defect

\[
\Pi_\omega=1-\mu_1.
\]

## 2. Axis-choice-free projective dispersion

Define

\[
\boxed{
\mathcal J_\omega
=1-\operatorname{tr}(\mathsf C_\omega^2).
}
\]

Since

\[
\operatorname{tr}(\mathsf C_\omega^2)
=
\frac{1}{E_\omega^2}
\iint
(\omega(x)\cdot\omega(y))^2\,dx\,dy,
\]

and

\[
|a\times b|^2
=|a|^2|b|^2-(a\cdot b)^2,
\]

we obtain the exact identity

\[
\boxed{
\mathcal J_\omega
=
\frac{
\iint
|\omega(x)\times\omega(y)|^2\,dx\,dy
}{
E_\omega^2
}.
}
\]

Thus `J_omega` is the enstrophy-weighted mean pairwise **projective angular dispersion** of the vorticity field. It is invariant under the sign reversal `omega -> -omega` and does not require a globally oriented vorticity direction.

Equivalently, if `xi=omega/|omega|` where defined,

\[
|\omega(x)\times\omega(y)|^2
=|\omega(x)|^2|\omega(y)|^2
\left[1-(\xi(x)\cdot\xi(y))^2\right].
\]

The angular factor is the squared projective distance between the two vorticity axes.

## 3. Exact comparison with the principal-axis defect

Write

\[
\Pi=\mu_2+\mu_3.
\]

Then

\[
\begin{aligned}
\mathcal J
&=1-\bigl[(1-\Pi)^2+\mu_2^2+\mu_3^2\bigr]\\
&=2\Pi(1-\Pi)+2\mu_2\mu_3.
\end{aligned}
\]

Because

\[
0\le\Pi\le\frac23,
\qquad
0\le\mu_2\mu_3\le\frac{\Pi^2}{4},
\]

we have

\[
\boxed{
\frac23\Pi
\le
\mathcal J
\le
2\Pi.
}
\]

Equivalently,

\[
\boxed{
\frac12\mathcal J
\le
\Pi
\le
\frac32\mathcal J.
}
\]

Hence `Pi` and `J` are uniformly equivalent directional-defect channels, but `J` remains well typed even when the principal eigenvalue is degenerate.

## 4. Relation to effective directional rank

The previously recorded effective rank satisfies

\[
R_{\rm eff}
=\frac{1}{\operatorname{tr}(\mathsf C_\omega^2)}.
\]

Therefore

\[
\boxed{
R_{\rm eff}
=\frac{1}{1-\mathcal J_\omega}.
}
\]

The allowed range is

\[
0\le\mathcal J_\omega\le\frac23,
\qquad
1\le R_{\rm eff}\le3.
\]

`R_eff` is a directional participation statistic on the existing three spatial axes; it is not a spatial-dimension rank change.

## 5. Miller gate without choosing an axis

The previous covariance-axis corollary of Miller's criterion gives the necessary blowup certificate

\[
E_\omega\Pi_\omega
\notin L^2(0,T^*)
\]

for any hypothetical finite-time singularity `T*` in the smooth finite-energy whole-space track.

Since

\[
\Pi_\omega\le\frac32\mathcal J_\omega,
\]

we immediately obtain the axis-choice-free necessary condition

\[
\boxed{
E_\omega\mathcal J_\omega
\notin L^2(0,T^*).
}
\]

Equivalently,

\[
\boxed{
\int_0^{T^*}
\left[
\|\omega(t)\|_2^2
\bigl(1-\operatorname{tr}\mathsf C_\omega(t)^2\bigr)
\right]^2dt
=\infty.
}
\]

This does not strengthen Miller's theorem by itself; it rewrites one consequence in an eigenvector-free form.

## 6. Energy-level corollary

For smooth finite-energy Navier--Stokes flow,

\[
\int_0^{T^*}E_\omega(t)\,dt<\infty.
\]

If

\[
\sup_{t<T^*}
\|\omega(t)\|_2\,\mathcal J_\omega(t)
<\infty,
\]

then

\[
\begin{aligned}
(E_\omega\mathcal J_\omega)^2
&=E_\omega
\bigl(\|\omega\|_2\mathcal J_\omega\bigr)^2\\
&\lesssim E_\omega,
\end{aligned}
\]

so `E_omega J_omega` belongs to `L^2_t`, and the Miller gate is satisfied.

Therefore a hypothetical finite-time singularity must obey

\[
\boxed{
\sup_{t<T^*}
\|\omega(t)\|_2\,\mathcal J_\omega(t)
=\infty.
}
\]

This is the sign-free analogue of the previous principal-axis defect requirement.

## 7. Local weighted version

For the local covariance

\[
\mathsf C_r(x)
=
\frac{
\int\eta_r(x-y)\omega(y)\otimes\omega(y)dy
}{
E_r(x)
},
\]

define

\[
\mathcal J_r(x)=1-\operatorname{tr}(\mathsf C_r(x)^2).
\]

Then exactly

\[
\boxed{
\mathcal J_r(x)
=
\frac{
\iint
\eta_r(x-y)\eta_r(x-z)
|\omega(y)\times\omega(z)|^2\,dy\,dz
}{
E_r(x)^2
}.
}
\]

The same comparison holds:

\[
\frac12\mathcal J_r
\le
\Pi_r
\le
\frac32\mathcal J_r.
\]

Thus the local covariance-axis route can be reformulated as a pairwise projective-dispersion route without choosing an orientation of the local vorticity direction.

## 8. Why this is useful for the active route

The residual singular class must now maintain not merely a large scalar enstrophy, but a temporally concentrated **pairwise cross-axis enstrophy channel**:

\[
E_\omega\mathcal J_\omega
=
\frac{1}{E_\omega}
\iint
|\omega(x)\times\omega(y)|^2dxdy.
\]

This is naturally compatible with geometric-depletion formulations of vortex stretching, where the relative direction of vorticity at different points matters.

The next target is to derive the exact evolution equation for `C_omega` and `J_omega`, separating

1. strain-driven directional mixing,
2. viscous directional mixing/demixing,
3. total enstrophy amplification.

Status: **OPEN PROJECTIVE-DISPERSION DYNAMICS / NO GLOBAL CLOSURE YET**.
