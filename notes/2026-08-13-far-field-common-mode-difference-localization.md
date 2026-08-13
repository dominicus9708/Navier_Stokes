# Far-field common-mode versus local difference: localization from the first-hitting `L-infinity` amplitude cap

Date: 2026-08-13

Status: **DERIVED FAR-FIELD DIFFERENCE LOCALIZATION / DSD COMMON-MODE SEPARATION**.

On first-hitting normalized windows the vorticity amplitude satisfies `||Omega||_infinity<=1` throughout the amplification interval.  This is enough to localize the **variation** of the remote strain, even when the remote strain's absolute constant part is not uniformly controlled by global enstrophy.

This is a direct DSD-style distinction between a common background channel and the local describability difference that actually varies across the dangerous core.

---

## 1. Strain kernel

The strain is a zero-order singular integral of vorticity,

\[
S(x)=\operatorname{p.v.}\int K(x-z)\Omega(z)dz,
\]

with a matrix kernel satisfying schematically

\[
|K(z)|\le C|z|^{-3},
\qquad
|\nabla K(z)|\le C|z|^{-4}.
\]

The kernel itself is borderline nonintegrable at infinity against merely bounded vorticity:

\[
\int_R^\infty r^{-3}r^2dr
=\int_R^\infty r^{-1}dr.
\]

Therefore no false claim

\[
\|\Omega\|_\infty\Rightarrow\|S\|_\infty
\]

is made.

---

## 2. Remote difference is absolutely integrable

Fix a dangerous center `x0` and radius `R`.  For

\[
|x-x_0|\le r,
\qquad
r\le R/4,
\]

consider only source points with

\[
|z-x_0|\ge R.
\]

The mean-value theorem gives

\[
|K(x-z)-K(x_0-z)|
\le
C|x-x_0||z-x_0|^{-4}.
\]

On a first-hitting normalized window,

\[
\|\Omega\|_\infty\le1.
\]

Hence

\[
\begin{aligned}
|S_{>R}(x)-S_{>R}(x_0)|
&\le
C|x-x_0|
\int_{|z-x_0|\ge R}
|z-x_0|^{-4}dz\\
&\le
C\frac{|x-x_0|}{R}.
\end{aligned}
\]

Therefore

\[
\boxed{
\sup_{B_r(x_0)}
|S_{>R}(x)-S_{>R}(x_0)|
\le
C\frac rR.
}
\]

This requires no normalized global `L2` vorticity bound.

---

## 3. Common-mode representation

Inside the dangerous core define

\[
\boxed{
S_0(t)=S_{>R}(x_0,t).
}
\]

Then

\[
\boxed{
S_{>R}(x,t)
=S_0(t)+\mathcal R_R(x,t),
}
\]

with

\[
\boxed{
\|\mathcal R_R\|_{L^\infty(B_r)}
\le C r/R.
}
\]

Thus an arbitrarily complicated remote vorticity field enters the local dangerous core, to first order, through one symmetric trace-free matrix `S0(t)` plus a controllably small spatial-difference channel.

---

## 4. Source decomposition

Let

\[
E_C=\int_C|\Omega|^2dy,
\qquad
C_C=\frac1{E_C}\int_C\Omega\otimes\Omega dy
\]

for a local core `C subset B_r`.

Then

\[
\int_C\Omega\cdot S_{>R}\Omega
=
E_C\operatorname{tr}(S_0C_C)
+
\int_C\Omega\cdot\mathcal R_R\Omega.
\]

The variation term obeys

\[
\boxed{
\left|
\int_C\Omega\cdot\mathcal R_R\Omega
\right|
\le
C\frac rR E_C.
}
\]

Since `S0` is trace free, the covariance-gap identity gives

\[
\boxed{
|E_C\operatorname{tr}(S_0C_C)|
\le
E_C|S_0|_F
\sqrt{\frac23-J_C}.
}
\]

Thus the remote field has exactly two local effects:

1. a **common affine strain channel** `S0(t)`;
2. an arbitrarily small **local difference channel** `O(r/R)`.

---

## 5. Relation to material/affine deformation

A common local velocity gradient does not represent fine-scale spatial information inside the core.  Its symmetric part accumulates material deformation and its antisymmetric part rotates the local frame.

The existing material/Lagrangian channels already measure this through deformation matrices and condition numbers.

Thus the remote common mode should be typed through a dimensionless accumulated background-strain channel, schematically

\[
\boxed{
\mathcal K_{\rm bg}(I)
=\int_I|S_0(s)|ds.
}
\]

- bounded `K_bg`: the remote affine action is a controlled deformation/background channel;
- unbounded `K_bg`: the residual route has entered a typed large-strain/deformation branch.

No claim is made that a general time-dependent affine transform leaves the isotropic Navier--Stokes Laplacian unchanged; the existing Lagrangian/metric notes keep the resulting anisotropic metric explicit.

---

## 6. Stronger than the previous `L2` remote-tail estimate in one respect

The earlier bounded-normalized-enstrophy estimate gave

\[
|S_{>R}(x_0)|=O(R^{-3/2}),
\]

and variation `O(R^-5/2)`.

That result controls the **absolute remote strain** but requires global normalized `L2` vorticity.

The present estimate gives only the **difference**

\[
S_{>R}(x)-S_{>R}(x_0)=O(r/R)
\]

but requires only the first-hitting amplitude cap `||Omega||_infinity<=1`.

The two statements are complementary and must not be conflated.

---

## 7. DSD interpretation

This is a literal application of a describability-difference principle.

The proof does not reconstruct the whole remote field.  At the current local resolution it retains only

\[
\boxed{
\text{remote common mode}
+
\text{remote local difference}.
}
\]

The common mode is one low-dimensional axis/deformation channel; the difference decays as the observation buffer grows.

Hence the adaptive proof search can ignore remote details that act identically across the current dangerous segment, while still retaining their net deformation effect.

Status: **REMOTE DIFFERENCE LOCALIZED WITHOUT GLOBAL ENSTROPHY / COMMON AFFINE MODE REMAINS ACTIVE**.
