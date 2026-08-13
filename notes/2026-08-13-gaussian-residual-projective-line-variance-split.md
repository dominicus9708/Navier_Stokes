# Gaussian residual vorticity variance = projective defect + signed-line defect

Date: 2026-08-13

Status: **EXACT STATIC-AGGREGATION IDENTITY / RESIDUAL GEOMETRY REFINED**.

The self-consistent Gaussian affine residual closure contains

\[
\mathcal B_\gamma
=\operatorname{Var}_\gamma(S)
+\frac12\operatorname{Var}_\gamma(\Omega).
\]

The vorticity variance itself admits an exact two-channel decomposition into a projective multi-axis defect and a signed-line coherence defect.

---

## 1. Weighted second moment and covariance

Let `gamma` be any probability weight and define

\[
E_\gamma
=\int\gamma|\Omega|^2,
\qquad
m_\gamma
=\int\gamma\Omega.
\]

For `E_gamma>0`, define

\[
C_\gamma
=\frac1{E_\gamma}
\int\gamma\,\Omega\otimes\Omega.
\]

Then

\[
C_\gamma\succeq0,
\qquad
\operatorname{tr}C_\gamma=1.
\]

Let

\[
\lambda_1
=\lambda_{\max}(C_\gamma).
\]

---

## 2. Projective defect

Define

\[
\boxed{
D_{\rm proj,\gamma}
=E_\gamma(1-\lambda_1).
}
\]

This is exactly the least weighted `L2` energy outside the best one-dimensional axis:

\[
D_{\rm proj,\gamma}
=\min_{|n|=1}
\int\gamma|P_{n^\perp}\Omega|^2.
\]

Thus `D_proj=0` iff the weighted vorticity is supported on one unoriented line almost everywhere.

---

## 3. Signed-line / polarity-magnitude defect

Define

\[
\boxed{
D_{\rm line,\gamma}
=E_\gamma\lambda_1-|m_\gamma|^2.
}
\]

This is nonnegative.

Indeed, if

\[
n=\frac{m_\gamma}{|m_\gamma|}
\]

when the mean is nonzero, then

\[
|m_\gamma|^2
=\left(\int\gamma\,n\cdot\Omega\right)^2
\le
\int\gamma(n\cdot\Omega)^2
\le
E_\gamma\lambda_1.
\]

The zero-mean case is immediate.

This defect measures what remains after the best unoriented line has been selected: sign cancellation, amplitude variation, and any mismatch between the first moment and the principal second-moment axis.

---

## 4. Exact variance split

The ordinary weighted vector variance is

\[
\operatorname{Var}_\gamma(\Omega)
=E_\gamma-|m_\gamma|^2.
\]

Insert and subtract `E_gamma lambda_1`:

\[
\boxed{
\operatorname{Var}_\gamma(\Omega)
=
D_{\rm proj,\gamma}
+D_{\rm line,\gamma}.
}
\]

Therefore the self-consistent residual-gradient variance is exactly

\[
\boxed{
\mathcal B_\gamma
=
\operatorname{Var}_\gamma(S)
+\frac12D_{\rm proj,\gamma}
+\frac12D_{\rm line,\gamma}.
}
\]

This is the canonical three-channel residual geometry.

---

## 5. Zero-defect rigidity

If

\[
D_{\rm proj,\gamma}=0
\]

and

\[
D_{\rm line,\gamma}=0,
\]

then

\[
\operatorname{Var}_\gamma(\Omega)=0,
\]

hence

\[
\boxed{
\Omega(y)=m_\gamma
\quad\text{for gamma-a.e. }y.
}
\]

Thus simultaneous projective and signed-line saturation is stronger than projective one-axis alignment alone: it forces an actually constant vorticity vector across the observation window.

Near-zero values give an `L2(gamma)` quantitative closeness to the constant vector `m_gamma` directly from the variance identity.

---

## 6. Relation to older projective and polarity channels

The decomposition distinguishes two situations that the unoriented covariance alone cannot separate.

### Multi-axis branch

\[
D_{\rm proj,\gamma}>0.
\]

This returns to projective covariance, angular palinstrophy, pairwise cross-axis, and Campanato/coherence channels.

### Signed-line branch

\[
D_{\rm proj,\gamma}\approx0,
\qquad
D_{\rm line,\gamma}>0.
\]

The field is nearly one-axis in the projective sense but remains nonconstant because of polarity cancellation and/or magnitude variation along that line.  This returns to oriented-flux, mixed-polarity, magnitude-heterogeneity, and gradient channels.

Thus projective covariance and signed polarity are complementary rather than competing descriptions.

---

## 7. Residual Duhamel consequence

The self-consistent Gaussian residual estimate becomes

\[
\boxed{
\mathfrak R_\gamma
\lesssim
\int
\|F\|\,\|\Omega\|_\infty
(1+\sqrt{\kappa(\Sigma)})
\left[
\operatorname{Var}_\gamma(S)
+\frac12D_{\rm proj,\gamma}
+\frac12D_{\rm line,\gamma}
\right]^{1/2}ds.
}
\]

Hence a large residual defect requires at least one of

\[
\boxed{
\text{non-affine strain}
\quad\text{or}\quad
\text{multi-axis vorticity}
\quad\text{or}\quad
\text{signed-line/polarity-magnitude variation},
}
\]

unless the affine heat weight itself becomes large/ill-conditioned.

---

## 8. DSD interpretation

At the Gaussian observation resolution, unresolved vorticity information separates exactly into

1. departure from a one-dimensional axis; and
2. failure to become one constant signed vector even after that best axis is chosen.

This supplies the missing oriented complement to the projective covariance channel.

Status: **EXACT RESIDUAL-VORTICITY VARIANCE SPLIT / NON-AFFINE STRAIN REMAINS THE DISTINCT HARD RESIDUAL SECTOR**.
