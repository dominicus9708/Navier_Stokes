# High-order covariance to base-vorticity anisotropy: Fourier bridge

Date: 2026-08-13

Status: **DERIVED FOURIER BRIDGE + COROLLARY OF EXTERNAL MILLER CRITERION / GLOBAL REGULARITY NOT PROVED**.

This note closes the previously open typing gap between a high-derivative covariance axis and the original-vorticity anisotropic regularity criterion.

The external theorem is Evan Miller, Theorem 1.6 in *A locally anisotropic regularity criterion for the Navier--Stokes equation in terms of vorticity* (Proc. AMS Series B 8 (2021), arXiv:2002.02152). It allows a unit vector field `v(x,t)` varying in space and time provided its **spatial** gradient is bounded, and it gives regularity when `v x omega` lies in the critical `L_t^4 L_x^2` class.

The Fourier interpolation below is derived here; no novelty claim is made without a separate literature audit.

## 1. High-derivative covariance axis

For derivative order `k>=1`, let

\[
E_k
=\sum_{I\in\{1,2,3\}^k}\|\partial_I\omega\|_2^2,
\]

\[
C_k
=\frac{1}{E_k}
\sum_I
\int(\partial_I\omega)\otimes(\partial_I\omega)dx,
\]

and let `n_k(t)` be a principal eigenvector of `C_k(t)`.

Define

\[
\Pi_k
=1-\mu_1(C_k).
\]

Then exactly

\[
\boxed{
\sum_I
\|n_k\times\partial_I\omega\|_2^2
=E_k\Pi_k.
}
\]

Because `n_k` depends only on time, not on space,

\[
\nabla_x n_k=0.
\]

A measurable principal-eigenvector selection is sufficient for Miller's spatial-gradient hypothesis; at eigenvalue degeneracies one may choose a measurable maximizer.

## 2. Fourier low/high split

Let `P_{<=K}` and `P_{>K}` be sharp Fourier projections.

Since

\[
\widehat\omega(\xi)=i\xi\times\widehat u(\xi),
\]

we have

\[
\|P_{\le K}(n_k\times\omega)\|_2^2
\le
\|P_{\le K}\omega\|_2^2
\le
K^2\|u\|_2^2.
\]

For the high-frequency part,

\[
\begin{aligned}
\|P_{>K}(n_k\times\omega)\|_2^2
&\le
K^{-2k}
\int|\xi|^{2k}
|n_k\times\widehat\omega(\xi)|^2d\xi\\
&=K^{-2k}E_k\Pi_k.
\end{aligned}
\]

The equality uses the ordered derivative identity

\[
\sum_{I\in\{1,2,3\}^k}
\xi_{i_1}^2\cdots\xi_{i_k}^2
=|\xi|^{2k}.
\]

Orthogonality of the Fourier projections gives

\[
\boxed{
\|n_k\times\omega\|_2^2
\le
A K^2+B K^{-2k},
}
\]

where

\[
A=\|u\|_2^2,
\qquad
B=E_k\Pi_k.
\]

## 3. Optimize the frequency threshold

For `A,B>0`, the minimizing threshold satisfies

\[
K^{2k+2}=\frac{kB}{A}.
\]

The minimum is

\[
\boxed{
\|n_k\times\omega\|_2^2
\le
c_k
A^{k/(k+1)}
B^{1/(k+1)},
}
\]

with

\[
\boxed{
c_k=(k+1)k^{-k/(k+1)}.}
\]

The zero cases follow by a limiting argument.

## 4. Replace principal defect by projective defect

The covariance comparison gives

\[
\Pi_k\le\frac32J_k.
\]

Let

\[
D_k=E_kJ_k.
\]

Then

\[
B=E_k\Pi_k
\le\frac32D_k.
\]

Hence

\[
\boxed{
\|n_k\times\omega\|_2^4
\le
C_k^{\rm br}
\|u\|_2^{4k/(k+1)}
D_k^{2/(k+1)},
}
\]

where

\[
C_k^{\rm br}
=c_k^2\left(\frac32\right)^{2/(k+1)}.
\]

The kinetic-energy equality keeps `||u||_2` uniformly bounded by the initial energy.

## 5. Miller corollary

Miller's Theorem 1.6 applies with

\[
v(x,t)=n_k(t),
\]

because this vector field is unit length and has

\[
\nabla_xv=0.
\]

Therefore the sufficient condition

\[
\boxed{
D_k^{2/(k+1)}
\in L^1(0,T^*)
}
\]

implies

\[
\int_0^{T^*}
\|n_k(t)\times\omega(t)\|_2^4dt<\infty,
\]

and hence excludes finite-time blowup.

Equivalently, a hypothetical finite-time singularity must satisfy, for every derivative order `k` for which the covariance construction is used,

\[
\boxed{
D_k^{2/(k+1)}
\notin L^1(0,T^*).
}
\]

This is a **derived sufficient condition**, not a claim that the required integrability is automatically available.

## 6. The especially useful `k=1` bridge

For `k=1`,

\[
c_1=2
\]

and

\[
\boxed{
\|n_1\times\omega\|_2^4
\le
6\|u\|_2^2D_1.
}
\]

Therefore

\[
\boxed{
D_1\in L^1(0,T^*)
\Longrightarrow
\text{regularity}.
}
\]

This is the first high-derivative covariance level because

\[
E_1=\|\nabla\omega\|_2^2
\]

is palinstrophy and `C_1` is the gradient covariance.

Importantly, the ordinary kinetic-energy budget controls

\[
\int E_0dt=\int\|\omega\|_2^2dt,
\]

not `int E_1 dt`; therefore this bridge does **not** make regularity automatic.

## 7. Combine with the `k=0` energy-weighted projective identity

At base order,

\[
D_0=E_0J_0
\]

and

\[
\boxed{
\dot D_0
+2\nu E_1(J_1+\Delta_0^2)
\le
2\sqrt5\sqrt{D_0}\,\|S\omega\|_2.
}
\]

Since

\[
E_1J_1=D_1,
\]

integration gives

\[
2\nu\int_0^tD_1(s)ds
\le
D_0(0)
+2\sqrt5
\int_0^t\sqrt{D_0}\,\|S\omega\|_2ds.
\]

Therefore

\[
\boxed{
\int_0^{T^*}
\sqrt{D_0(t)}\,\|S\omega(t)\|_2dt
<\infty
\Longrightarrow
D_1\in L^1(0,T^*)
\Longrightarrow
\text{regularity}.
}
\]

Thus a hypothetical blowup must satisfy the stronger geometrically weighted source divergence

\[
\boxed{
\int_0^{T^*}
\sqrt{D_0(t)}\,\|S\omega(t)\|_2dt
=\infty.
}
\]

Because

\[
\sqrt{D_0}
=\|\omega\|_2\sqrt{J_0},
\]

the source is automatically depleted as the base vorticity covariance approaches a one-axis projective state.

## 8. Relation to the local projective geometry target

The remaining base source is

\[
\sqrt{D_0}\,\|S\omega\|_2.
\]

The global factor `sqrt(J_0)` captures aggregate axis alignment, but the singular Biot--Savart stretching kernel is sensitive to **local** direction alignment.

Therefore the next strengthening is to replace or supplement the global factor by the dyadic local pairwise projective spectrum

\[
\mathcal P_{r_j}
=
\int E_{r_j}^2J_{r_j},
\]

which was shown to equal a smoothed pairwise `|omega(x) x omega(y)|^2` channel at physical scale `r_j`.

Status: **ACTIVE BASE PROJECTIVE-DEPLETION ROUTE / OPEN DYADIC SINGULAR-KERNEL CLOSURE**.
