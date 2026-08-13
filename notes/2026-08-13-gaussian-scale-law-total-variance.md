# Gaussian scale law of total variance for the residual ladder

Date: 2026-08-13

Status: **EXACT SCALE-ANOVA IDENTITY / NONNEGATIVE BETWEEN-SCALE RESIDUAL LEDGER**.

The Gaussian residual variance at multiple parent scales must not be added naively: the same fine-scale fluctuation can remain visible in every larger Gaussian window.  Gaussian convolution has an exact law of total variance that separates inherited residual from genuinely new between-scale residual.

---

## 1. Hilbert-valued Gaussian variance

For a Hilbert-valued field `g`, define

\[
\mathcal B_\Sigma[g]
=P_\Sigma|g|^2-|P_\Sigma g|^2.
\]

For the Navier--Stokes affine residual,

\[
g=\nabla U.
\]

---

## 2. Add two Gaussian covariance scales

Let

\[
\Sigma_p=\Sigma_c+\Delta\Sigma,
\qquad
\Sigma_c\succeq0,
\qquad
\Delta\Sigma\succeq0.
\]

The Gaussian semigroup property is

\[
P_{\Sigma_p}
=P_{\Delta\Sigma}P_{\Sigma_c}.
\]

Then

\[
\begin{aligned}
\mathcal B_{\Sigma_p}[g]
={}&P_{\Delta\Sigma}P_{\Sigma_c}|g|^2
-|P_{\Delta\Sigma}P_{\Sigma_c}g|^2\\
={}&P_{\Delta\Sigma}
\left(
P_{\Sigma_c}|g|^2-|P_{\Sigma_c}g|^2
\right)\\
&+
\left(
P_{\Delta\Sigma}|P_{\Sigma_c}g|^2
-|P_{\Delta\Sigma}P_{\Sigma_c}g|^2
\right).
\end{aligned}
\]

Therefore exactly

\[
\boxed{
\mathcal B_{\Sigma_p}[g]
=
P_{\Delta\Sigma}\mathcal B_{\Sigma_c}[g]
+
\mathcal B_{\Delta\Sigma}[P_{\Sigma_c}g].
}
\]

Both terms are nonnegative.

---

## 3. Interpretation of the two terms

The first term

\[
P_{\Delta\Sigma}\mathcal B_{\Sigma_c}[g]
\]

is inherited residual: the parent window observes fluctuations that were already unresolved at the child scale.

The second term

\[
\boxed{
\Delta\mathcal B_{c\to p}
=
\mathcal B_{\Delta\Sigma}[P_{\Sigma_c}g]
\ge0
}
\]

is new between-scale residual: even after the child-scale field has been resolved/smoothed, its child-scale representative varies across the parent window.

Thus the correct scale ledger counts `Delta B`, not the raw parent `B` repeatedly.

---

## 4. Iterated ladder

For a nested covariance ladder

\[
0=\Sigma_0\preceq\Sigma_1\preceq\cdots\preceq\Sigma_N,
\]

set

\[
\Delta\Sigma_k=\Sigma_{k+1}-\Sigma_k.
\]

Repeatedly applying the two-scale identity yields a positive decomposition of the terminal variance into inherited/smoothed scale increments.

At a fixed final center, every increment has the form

\[
\boxed{
\Delta\mathcal B_k
=
\mathcal B_{\Delta\Sigma_k}
[P_{\Sigma_k}g]
\ge0.
}
\]

The exact expression contains the appropriate subsequent Gaussian smoothing when all increments are written at one common parent scale; hence no new residual contribution is counted twice.

This is the Gaussian analogue of orthogonal/martingale ANOVA.

---

## 5. Relation to the semigroup curvature identity

Each between-scale residual itself has the square-function representation

\[
\Delta\mathcal B_k
=
\int_0^1
P_{t\Delta\Sigma_k}
\left[
\left|
\nabla P_{(1-t)\Delta\Sigma_k}
P_{\Sigma_k}g\,
\Delta\Sigma_k^{1/2}
\right|^2
\right]dt.
\]

Thus every genuinely new scale increment has its own positive curvature witness in the frequency/spatial band between the child and parent resolutions.

The scale ledger is therefore

\[
\boxed{
\text{new residual at scale step}
\Longrightarrow
\text{positive band-curvature action}.
}
\]

---

## 6. Fourier multiplier form in the isotropic case

For `Sigma=r^2 I`, the integrated spatial variance is

\[
\int\mathcal B_{r^2I}[g](x)dx
=
\int_{\mathbb R^3}
\left(1-e^{-r^2|\xi|^2}\right)
|\widehat g(\xi)|^2d\xi,
\]

up to the Fourier normalization convention.

A between-scale increment from `r` to `R>r` has a positive multiplier comparable to

\[
e^{-r^2|\xi|^2}-e^{-R^2|\xi|^2},
\]

which is concentrated on frequencies between `R^(-1)` and `r^(-1)`.

This makes the almost-orthogonality meaning explicit.

---

## 7. DSD interpretation

Static aggregation across resolutions now has an exact nonnegative chain rule:

\[
\boxed{
\text{parent unresolved state}
=
\text{smoothed inherited unresolved state}
+
\text{new inter-resolution unresolved state}.
}
\]

A parent scale cannot claim a fine-scale residual as a new cost.  Only the between-scale increment is charged again.

---

## 8. Limitation

The identity is exact at a fixed time/center and for a covariance-nested Gaussian ladder.  The self-consistent terminal Gaussian windows used dynamically have centers and affine covariances that may change with time and terminal checkpoint.

A full proof still needs a spacetime packing argument controlling these moving scale increments, or a rigidity result showing that persistent inherited residual cannot support repeated first-hitting amplification.

Status: **GAUSSIAN SCALE DOUBLE-COUNTING REMOVED / MOVING SPACETIME SCALE-INCREMENT PACKING REMAINS OPEN**.
