# Optimal global vorticity-axis gate from the covariance matrix

Date: 2026-08-12

Status: **DERIVED COROLLARY OF EXTERNAL LOCALLY-ANISOTROPIC CRITERION + DSD AXIS-MATRIX GATE**.

This note extracts an exact optimal-axis consequence from Evan Miller's locally anisotropic vorticity criterion.

The external theorem is Miller's; the covariance minimization below is elementary linear algebra.

## 1. Global vorticity directional covariance

For a time at which

\[
E_\omega(t)=\|\omega(t)\|_2^2>0,
\]

define

\[
\boxed{
\mathsf C_\omega(t)
=
\frac{
\int_{\mathbb R^3}
\omega(x,t)\otimes\omega(x,t)dx
}{
E_\omega(t)
}.
}
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

be its eigenvalues.

## 2. Exact best constant axis

For any unit vector `n`,

\[
|n\times\omega|^2
=|\omega|^2-(n\cdot\omega)^2.
\]

Integrating gives

\[
\begin{aligned}
\|n\times\omega\|_2^2
&=E_\omega
-
n^T
\left(
\int\omega\otimes\omega dx
\right)n\\
&=E_\omega
\left(
1-n^T\mathsf C_\omega n
\right).
\end{aligned}
\]

The Rayleigh principle therefore yields

\[
\boxed{
\min_{|n|=1}
\|n\times\omega\|_2^2
=
E_\omega(1-\mu_1).
}
\]

Any principal eigenvector corresponding to `mu_1` is an optimal global vorticity axis.

## 3. DSD planarity / three-dimensionality defect

Define

\[
\boxed{
\Pi_\omega(t)=1-\mu_1(t).
}
\]

Since `mu_1>=1/3`,

\[
0\le\Pi_\omega\le\frac23.
\]

Interpretation:

- `Pi_omega=0`: vorticity is aligned with one global axis almost everywhere in the enstrophy-weighted sense;
- small `Pi_omega`: nearly one-axis vorticity distribution;
- larger `Pi_omega`: more enstrophy lies outside every single global axis.

This is a **directional participation descriptor**, not a change of spatial rank.

A complementary effective directional rank may be recorded as

\[
R_{\rm eff}
=
\frac{1}{\operatorname{tr}(\mathsf C_\omega^2)},
\qquad
1\le R_{\rm eff}\le3.
\]

It is a static diagnostic only; Miller's theorem uses `Pi_omega` through the cross-vorticity norm, not `R_eff`.

## 4. External theorem permits the time-dependent optimal constant axis

Miller's theorem allows a unit vector field `n(x,t)` that is essentially bounded in spacetime and whose **spatial** gradient is locally bounded.

A direction that is constant in space but allowed to depend measurably on time has

\[
\nabla_x n=0.
\]

Therefore, at each time, choose a measurable principal eigenvector of `C_omega(t)` (or an arbitrarily close measurable minimizer at degenerate times).

Miller's criterion then applies with this optimal time-dependent global axis.

## 5. Necessary blow-up certificate

Miller's theorem implies that a finite-time blowup at `T*` requires

\[
\int_0^{T^*}
\|n(t)\times\omega(t)\|_2^4dt
=\infty
\]

for the admissible axis choice.

Using the optimal axis,

\[
\boxed{
\int_0^{T^*}
\left[
E_\omega(t)\Pi_\omega(t)
\right]^2dt
=\infty.
}
\]

Equivalently,

\[
\boxed{
E_\omega\Pi_\omega
\notin L^2(0,T^*).
}
\]

This is scale critical:

- `E_omega=||omega||_2^2` scales like `lambda`;
- `Pi_omega` is dimensionless;
- squaring and multiplying by `dt -> lambda^-2 dt` leaves the integral invariant.

## 6. Compare with the energy-level dissipation bound

The kinetic-energy equality/inequality gives

\[
\int_0^{T^*}E_\omega(t)dt<\infty
\]

on the smooth finite-energy whole-space track.

Since

\[
0\le\Pi_\omega\le\frac23,
\]

the blowup certificate says the same geometric defect is simultaneously

\[
E_\omega\Pi_\omega
\in L^1(0,T^*)
\]

but

\[
E_\omega\Pi_\omega
\notin L^2(0,T^*).
\]

Thus a residual blowup requires temporal concentration of the **multi-axis enstrophy component**, not just of total enstrophy.

## 7. Exact benchmark geometries

### One-axis vorticity

If

\[
\omega(x)=f(x)e_3,
\]

then

\[
\mathsf C_\omega=e_3\otimes e_3,
\qquad
(\mu_1,\mu_2,\mu_3)=(1,0,0),
\]

and

\[
\Pi_\omega=0.
\]

### Isotropic directional covariance

If

\[
\mathsf C_\omega=\frac13I,
\]

then

\[
\Pi_\omega=\frac23.
\]

### Planar isotropic directional covariance

If

\[
\mathsf C_\omega
=\operatorname{diag}(1/2,1/2,0),
\]

then

\[
\Pi_\omega=\frac12
\]

and the principal axis is degenerate.  This illustrates why a large principal-eigenvalue gap is not automatic even when the vorticity lies in a two-dimensional directional subspace.

## 8. Relation to the local-axis gluing problem

The global covariance gate requires no spatial gluing because the optimal axis is constant in space at each time.

It does **not** replace the local-axis criterion: a flow may have no useful single global axis while still being locally close to a smoothly varying two-dimensional structure.

Therefore use two levels:

1. **global axis matrix** `C_omega(t)` — exact and immediately compatible with Miller's theorem;
2. **local covariance axis field** — potentially stronger, but requires eigenvector-gap/gluing control.

## 9. DSD axis-property interpretation

The matrix

\[
\mathsf C_\omega
\]

is an axis-property matrix on the existing three realized spatial axes.

- diagonal/eigenvalue data: how enstrophy is distributed among best-fit directions;
- principal eigenvector: best-fit global vorticity axis;
- `Pi_omega`: off-axis enstrophy fraction;
- eigenvalue gap `mu_1-mu_2`: stability/uniqueness of the best-fit axis.

The matrix must not be interpreted as creating new dimensions.

## 10. Residual-class update

Any hypothetical blowup must now satisfy the additional exact external-anchored requirement

\[
\boxed{
\int_0^{T^*}
[E_\omega(t)\Pi_\omega(t)]^2dt
=\infty.
}
\]

Hence a residual configuration cannot regularize merely by collapsing its vorticity into a nearly one-axis global structure fast enough to offset enstrophy growth.

The next target is to construct the analogous **moving local covariance matrix** and determine when its principal axis can be patched into an admissible spatially Lipschitz direction field.

Status: **OPEN LOCAL COVARIANCE AXIS-FIELD BRIDGE**.
