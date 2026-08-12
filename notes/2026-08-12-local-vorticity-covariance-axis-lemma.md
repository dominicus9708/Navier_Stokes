# Local vorticity covariance axis: gap, smoothness, and anisotropic regularity bridge

Date: 2026-08-12

Status: **DERIVED MATRIX/GLUING LEMMA + COROLLARY OF EXTERNAL MILLER CRITERION / OPEN DYNAMIC PLANARIZATION**.

This note closes a strong form of the local-axis gluing problem left by the locally anisotropic vorticity track.  The external regularity theorem is Miller's; the covariance/eigenvector estimates below are derived here from elementary symmetric-matrix perturbation and convolution estimates.

No novelty claim is made without a separate literature audit.

## 1. Choose a positive smooth scale kernel

Fix

\[
m>\frac52
\]

and let

\[
\eta_r(z)
=c_m r^{-3}
\left(1+\frac{|z|^2}{r^2}\right)^{-m},
\qquad
\int_{\mathbb R^3}\eta_r(z)dz=1.
\]

This kernel is positive everywhere, smooth, radial, and has finite second moment.

Its logarithmic gradient satisfies

\[
\boxed{
|\nabla\log\eta_r(z)|
=\frac{2m|z|}{r^2+|z|^2}
\le\frac{m}{r}.
}
\]

Its normalized second moment is

\[
\boxed{
\int |z|^2\eta_r(z)dz
=\kappa_m r^2,
\qquad
\kappa_m=\frac{3}{2m-5}.
}
\]

## 2. Local vorticity covariance matrix

At a time when `omega` is not identically zero, define

\[
E_r(x)
=\int\eta_r(x-y)|\omega(y)|^2dy>0,
\]

\[
N_r(x)
=\int\eta_r(x-y)\omega(y)\otimes\omega(y)dy,
\]

and

\[
\boxed{
C_r(x)=\frac{N_r(x)}{E_r(x)}.
}
\]

Then `C_r` is symmetric positive semidefinite with

\[
\operatorname{tr}C_r=1.
\]

Let

\[
\mu_1\ge\mu_2\ge\mu_3\ge0
\]

be its eigenvalues and define

\[
\boxed{
\Pi_r(x)=1-\mu_1(x),
\qquad
\delta_r(x)=\mu_1(x)-\mu_2(x).
}
\]

The local best-axis identity is

\[
\boxed{
\min_{|n|=1}
\int\eta_r(x-y)|n\times\omega(y)|^2dy
=E_r(x)\Pi_r(x).
}
\]

## 3. Small planarity defect automatically opens the principal gap

Since

\[
\mu_2+\mu_3=\Pi_r,
\]

we have

\[
\mu_2\le\Pi_r.
\]

Therefore

\[
\boxed{
\delta_r
=\mu_1-\mu_2
\ge
(1-\Pi_r)-\Pi_r
=1-2\Pi_r.
}
\]

Consequently

\[
\Pi_r\le\varepsilon_0<\frac12
\]

implies a uniform simple principal eigenvalue with

\[
\delta_r\ge1-2\varepsilon_0>0.
\]

Thus the two bad events

\[
\text{nearly one-axis covariance}
\quad\text{and}\quad
\text{top-eigenvalue degeneracy}
\]

cannot occur simultaneously.

## 4. Sharpened derivative estimate for the optimal axis

Assume the principal eigenvalue is simple and choose a normalized principal eigenvector `n_r(x)` locally.

For a unit spatial direction `h`, differentiate

\[
C_r n_r=\mu_1n_r.
\]

After projecting onto `n_r^perp`,

\[
(\mu_1I-C_r)\partial_h n_r
=P_\perp(\partial_hC_r)n_r.
\]

Hence

\[
|\partial_hn_r|
\le
\delta_r^{-1}
\|P_\perp(\partial_hC_r)n_r\|.
\]

The derivative of the normalization term in `C_r=N_r/E_r` is parallel to `n_r` after applying `C_r n_r=mu_1 n_r`, so it vanishes under `P_perp`.  Thus

\[
P_\perp(\partial_hC_r)n_r
=
\frac1{E_r}
\int
(\partial_h\eta_r)(x-y)
(\omega\cdot n_r)
P_\perp\omega\,dy.
\]

Using

\[
|\partial_h\eta_r|
\le\frac mr\eta_r
\]

and Cauchy--Schwarz,

\[
\begin{aligned}
\|P_\perp(\partial_hC_r)n_r\|
&\le
\frac mr
\left(
\frac1{E_r}
\int\eta_r(\omega\cdot n_r)^2
\right)^{1/2}
\left(
\frac1{E_r}
\int\eta_r|P_\perp\omega|^2
\right)^{1/2}\\
&=
\frac mr
\sqrt{\mu_1(1-\mu_1)}.
\end{aligned}
\]

Therefore

\[
\boxed{
r|\nabla n_r|_{\rm op}
\le
m
\frac{\sqrt{\mu_1\Pi_r}}{\delta_r}.
}
\]

In particular, if

\[
\Pi_r\le\varepsilon_0<\frac12,
\]

then

\[
\boxed{
r|\nabla n_r|_{\rm op}
\le
\frac{m\sqrt{\Pi_r}}{1-2\varepsilon_0}.
}
\]

This is stronger than the crude derivative bound `O(1/(r delta))`: the best axis becomes automatically smoother as the local covariance becomes more one-dimensional.

## 5. Global orientation when the defect is uniformly below one half

Suppose for a fixed time and radius

\[
\sup_x\Pi_r(x)\le\varepsilon_0<\frac12.
\]

Then the principal eigenspace is a smooth one-dimensional line field over `R^3` with a uniform spectral gap.

Because `R^3` is contractible, this real line bundle is trivial.  Hence one can choose a global smooth unit orientation `n_r(x)` (up to a global sign), with the derivative bound above.

For time-dependent data, choose the orientation measurably in time; Miller's criterion requires spatial regularity of `n`, not time differentiability.

## 6. Compare the local best axes to the pointwise vorticity

Let

\[
\varepsilon(t)
=\sup_x\Pi_{r(t)}(x,t)
\le\varepsilon_0<\frac12.
\]

Write `n(x)=n_r(x)` and let

\[
L(t)=\|\nabla n(\cdot,t)\|_\infty.
\]

For any `x,y`,

\[
|n(y)\times\omega(y)|
\le
|n(x)\times\omega(y)|
+|n(y)-n(x)|\,|\omega(y)|.
\]

Squaring, averaging in `x` with `eta_r(x-y)`, and then integrating in `y` gives

\[
\begin{aligned}
\|n\times\omega\|_2^2
&\le
2\int E_r(x)\Pi_r(x)dx\\
&\quad+
2L^2
\left(
\int |z|^2\eta_r(z)dz
\right)
\|\omega\|_2^2.
\end{aligned}
\]

Since

\[
\int E_r(x)dx=\|\omega\|_2^2
\]

and

\[
Lr
\le
\frac{m\sqrt{\varepsilon}}{1-2\varepsilon_0},
\]

we obtain

\[
\boxed{
\|n\times\omega\|_2^2
\le
C_{m,\varepsilon_0}
\varepsilon(t)
\|\omega(t)\|_2^2,
}
\]

where one admissible explicit constant is

\[
\boxed{
C_{m,\varepsilon_0}
=2+
\frac{2m^2\kappa_m}{(1-2\varepsilon_0)^2}.
}
\]

## 7. Corollary through Miller's locally anisotropic criterion

Assume a radius function `r(t)>0` such that

\[
r^{-1}\in L^\infty_{\rm loc}([0,T^*))
\]

and

\[
\varepsilon(t)
=
\sup_x\Pi_{r(t)}(x,t)
\le\varepsilon_0<\frac12.
\]

If additionally

\[
\boxed{
\sup_{t<T^*}
\varepsilon(t)\|\omega(t)\|_2
<\infty,
}
\]

then

\[
\begin{aligned}
\|n\times\omega\|_2^4
&\le
C_{m,\varepsilon_0}^2
\varepsilon^2\|\omega\|_2^4\\
&=
C_{m,\varepsilon_0}^2
(\varepsilon\|\omega\|_2)^2
\|\omega\|_2^2.
\end{aligned}
\]

The finite-energy dissipation bound gives

\[
\int_0^{T^*}\|\omega(t)\|_2^2dt<\infty.
\]

Hence

\[
\int_0^{T^*}\|n\times\omega\|_2^4dt<\infty.
\]

Miller's external locally anisotropic criterion then precludes finite-time blowup.

Therefore the present route yields the sufficient condition

\[
\boxed{
\sup_x\Pi_{r(t)}(x,t)<\frac12
\quad\text{and}\quad
\sup_t\Bigl[
\|\omega(t)\|_2
\sup_x\Pi_{r(t)}(x,t)
\Bigr]<\infty
\Longrightarrow
\text{regularity through }T^*.
}
\]

The constants and technical time-measurable eigenvector selection can be polished further; the mechanism is the key result of this note.

## 8. Residual trichotomy

A hypothetical singular flow must evade the preceding local-axis gate.  At dangerous times/scales it therefore requires at least one of:

### A. Multi-axis covariance branch

\[
\sup_x\Pi_r\not<\frac12
\]

(or the stronger energy-weighted small-defect condition fails).

The vorticity is intrinsically multi-axis at some location.

### B. Quantitatively insufficient planarization

The defect remains below `1/2` but

\[
\|\omega\|_2\sup_x\Pi_r
\]

becomes unbounded.

The axis exists smoothly, but off-axis enstrophy decays too slowly relative to enstrophy growth.

### C. Shrinking-scale / locality branch

The useful radius collapses so violently that the spatial gradient requirement cannot be controlled on the needed intervals.  For the natural radius `r~||omega||_infinity^{-1/2}`, this does not obstruct Miller's local-in-time spatial-gradient requirement on compact subintervals before `T*`, but endpoint estimates must still be handled carefully.

## 9. DSD interpretation

The local axis-property block is now

\[
\boxed{
\mathcal A_{\omega,r}
=
(E_r,\mu_1,\mu_2,\mu_3,
\Pi_r,\delta_r,n_r,r|\nabla n_r|).
}
\]

This is a direct axis-property matrix on the existing three spatial axes.

- `Pi_r`: local multi-axis participation;
- `delta_r`: axis identifiability/stability;
- `n_r`: best local vorticity axis;
- `r|grad n_r|`: scale-normalized axis variation.

The exact inequality

\[
\delta_r\ge1-2\Pi_r
\]

shows that small multi-axis defect automatically makes the axis identifiable.

## 10. Next target

The major remaining question is now dynamic rather than geometric:

\[
\boxed{
\text{Can a residual singular cascade force }
\|\omega\|_2\sup_x\Pi_{r(t)}
\to\infty
\text{ while also evading sparseness, strain, and higher-derivative gates?}
}
\]

A useful next estimate should connect the local covariance defect `Pi_r` to the existing occupancy/overlap matrix and the vorticity-direction diffusion channel.

Status: **OPEN DYNAMIC MULTI-AXIS PERSISTENCE ESTIMATE**.
