# Fixed-time Carleson packing of low-curvature Gaussian residual states

Date: 2026-08-14

Status: **EXACT FIXED-TIME SCALE PACKING CLOSED ON THE LOW-CURVATURE BRANCH / ONLY THE SCALE-TIME TRANSPORT BETWEEN MOVING FIRST-HITTING WINDOWS REMAINS**.

The previous two notes established:

1. for a proportional Gaussian split, a low-curvature parent creates a fixed fraction of genuinely new between-scale residual;
2. this new information has nonvanishing local spatial occupancy.

At a fixed physical/normalized time, the exact global law of total variance is already enough to sum the low-curvature active sets across all geometric Gaussian scales.  No additional Carleson conjecture is needed at fixed time.

---

## 1. Geometric covariance ladder

Fix a positive covariance `Sigma_0` and a constant

\[
0<c<1.
\]

Define

\[
\boxed{
\Sigma_{k+1}=c\Sigma_k.
}
\]

For a fixed field `g(x)` at one fixed time define

\[
B_k(x)
:=
\mathcal B_{\Sigma_k}[g](x)
=P_{\Sigma_k}|g|^2(x)-|P_{\Sigma_k}g(x)|^2.
\]

The genuinely new increment from the child scale `Sigma_{k+1}` to the parent `Sigma_k` is

\[
\boxed{
\Delta_k(x)
:=
\mathcal B_{(1-c)\Sigma_k}
[P_{c\Sigma_k}g](x).
}
\]

The exact Gaussian total-variance law gives

\[
B_k
=P_{(1-c)\Sigma_k}B_{k+1}
+\Delta_k.
\]

---

## 2. Exact global telescoping

Gaussian convolution preserves spatial integrals.  Therefore

\[
\boxed{
\int\Delta_kdx
=
\|P_{\Sigma_{k+1}}g\|_2^2
-
\|P_{\Sigma_k}g\|_2^2.
}
\]

Summing over a finite ladder,

\[
\boxed{
\sum_{k=m}^{n}
\int\Delta_kdx
=
\|P_{\Sigma_{n+1}}g\|_2^2
-
\|P_{\Sigma_m}g\|_2^2
\le
\|g\|_2^2.
}
\]

Hence over the full geometric ladder,

\[
\boxed{
\sum_k\int\Delta_kdx
\le
\|g\|_2^2.
}
\]

---

## 3. Low-curvature active set

Let the whitened derivative energy be

\[
K_k(x)
:=
P_{\Sigma_k}
\left|
(\nabla g)\Sigma_k^{1/2}
\right|_F^2(x).
\]

Fix a curvature-ratio threshold

\[
K_0<\infty.
\]

Define the low-curvature active set

\[
\boxed{
A_k
:=
\{x:B_k(x)>0,\ K_k(x)\le K_0B_k(x)\}.
}
\]

The exact OU/Hermite calculation from the preceding note gives on `A_k`

\[
\boxed{
\Delta_k(x)
\ge
\eta_{c,K_0}B_k(x),
\qquad
\eta_{c,K_0}=(1-c)^{K_0}>0.
}
\]

---

## 4. Fixed-time scale-Carleson bound

Integrating only over the active sets and summing,

\[
\begin{aligned}
\eta_{c,K_0}
\sum_k\int_{A_k}B_kdx
&\le
\sum_k\int_{A_k}\Delta_kdx\\
&\le
\sum_k\int_{\mathbb R^3}\Delta_kdx\\
&\le
\|g\|_2^2.
\end{aligned}
\]

Therefore

\[
\boxed{
\sum_k\int_{A_k}B_k(x)dx
\le
\eta_{c,K_0}^{-1}\|g\|_2^2.
}
\]

This is an exact fixed-time spatial-scale packing estimate for all low-curvature Gaussian residual states.

For the Navier--Stokes application take

\[
\boxed{g=\nabla U.}
\]

Then

\[
\boxed{
\sum_k\int_{A_k}\mathcal B_{\Sigma_k}(x)dx
\le
C_{c,K_0}\|\nabla U\|_2^2.
}
\]

---

## 5. Level-set form

For any residual threshold

\[
\lambda>0,
\]

define

\[
A_{k,\lambda}
=A_k\cap\{B_k\ge\lambda\}.
\]

Then

\[
\lambda|A_{k,\lambda}|
\le
\int_{A_{k,\lambda}}B_kdx.
\]

Hence

\[
\boxed{
\sum_k
|A_{k,\lambda}|
\le
\frac{C_{c,K_0}}{\lambda}
\|g\|_2^2.
}
\]

For `g=grad U`,

\[
\boxed{
\sum_k
|A_{k,\lambda}|
\le
\frac{C_{c,K_0}}{\lambda}
\|\nabla U\|_2^2.
}
\]

Thus low-curvature residual states above a fixed level cannot occupy large volume on many Gaussian scales at the same time.

---

## 6. Weighted level-set / layer-cake version

Since

\[
B_k(x)=\int_0^\infty
\mathbf 1_{\{B_k(x)>\lambda\}}d\lambda,
\]

the packing identity can also be written as

\[
\boxed{
\int_0^\infty
\sum_k
|A_k\cap\{B_k>\lambda\}|d\lambda
\le
C_{c,K_0}\|g\|_2^2.
}
\]

This makes the Carleson-type structure explicit: the scale multiplicity is integrable after weighting by the actual residual amplitude.

---

## 7. High-curvature complement

The complement of `A_k` is

\[
\boxed{
K_k>K_0B_k.
}
\]

For `g=grad U`, in an isotropic parent of radius `R_k`,

\[
K_k=R_k^2D_{g,k}.
\]

Thus every active point at every scale obeys the exact dichotomy

\[
\boxed{
\text{low curvature}
\Rightarrow
\text{fixed-time scale packing},
}

or

\[
\boxed{
\text{high curvature}
\Rightarrow
R_k^2D_{g,k}>K_0B_k.
}
\]

So there is no longer an untyped fixed-time low-curvature scale cascade.

---

## 8. Why moving dangerous centers are not a fixed-time problem

A hypothetical singular sequence does not remain at one fixed time.  It uses first-hitting windows

\[
(t_j,x_j,W_j)
\]

with changing amplitudes, centers, and natural scales.

The estimate above controls all Gaussian scales of **one field `g(\cdot,t)` at the same time**.  It does not directly compare

\[
B_{\Sigma_j}[\nabla U(\cdot,t_j)](x_j)
\]

with

\[
B_{\Sigma_{j+1}}[\nabla U(\cdot,t_{j+1})](x_{j+1}).
\]

Therefore the remaining obstruction is not spatial overlap by itself.  It is the nonlinear evolution needed to move a residual state from one time slice to the next.

---

## 9. Corrected frontier

The earlier wording “Carleson/almost-orthogonal spacetime packing remains open” can now be sharpened.

### Closed

At any fixed time:

\[
\boxed{
\sum_k\int_{A_k}B_kdx
\le C\|g\|_2^2.
}
\]

Thus the spatial-scale Carleson ledger is closed on the low-curvature branch.

### Still open

One must compare a static child scale of the field at time `t` with the dynamically evolved natural child state at a later time.

Schematically the missing object is a scale-time commutator

\[
\boxed{
\mathcal C
=
P_{c\Sigma(t)}g(t)
-
\text{transport/evolution of }g
\text{ to the corresponding child time}.
}
\]

If this commutator is small, the fixed-time contraction/packing should transfer to the moving first-hitting cascade.  If it is large, its Duhamel source must be charged to nonlinear stretching, pressure, affine deformation, or diffusion.

Status: **FIXED-TIME LOW-CURVATURE SPATIAL-SCALE PACKING CLOSED / ACTIVE FRONTIER = SCALE-TIME COMMUTATOR BETWEEN STATIC GAUSSIAN DESCENT AND NAVIER--STOKES EVOLUTION**.
