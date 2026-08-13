# Fixed-ratio curvature descent from the Gaussian residual square function

Date: 2026-08-13

Status: **DERIVED POSITIVE-INTEGRAND SCALE DICHOTOMY / DERIVATIVE PACKING OPEN**.

The Gaussian residual square-function identity writes

\[
\mathcal B_\Sigma
=\int_0^1 Q_\Sigma(t)dt,
\]

with

\[
Q_\Sigma(t)
=P_{t\Sigma}
\left[
\left|
\nabla^2P_{(1-t)\Sigma}U\,\Sigma^{1/2}
\right|_F^2
\right]
\ge0.
\]

The positivity yields a simple but useful scale dichotomy: an order-one residual either has a curvature witness at a fixed smaller scale or concentrates its square-function mass near a scale endpoint.

---

## 1. Split the internal scale parameter

Fix

\[
0<\delta<\frac12.
\]

Write

\[
[0,1]
=[0,\delta]
\cup[\delta,1-\delta]
\cup[1-\delta,1].
\]

Let

\[
\mathcal E_{\rm edge}
=\int_0^\delta Q_\Sigma(t)dt
+\int_{1-\delta}^1Q_\Sigma(t)dt.
\]

---

## 2. Edge-concentration branch

If

\[
\boxed{
\mathcal E_{\rm edge}
\ge\frac12\mathcal B_\Sigma,
}
\]

then at least one endpoint interval contains at least one quarter of the total residual square-function mass.

This is typed as an endpoint derivative concentration:

- `t near 0`: curvature of a strongly smoothed descendant remains large at the parent center;
- `t near 1`: nearly unsmoothed curvature is large under an almost-parent Gaussian average.

No fixed-ratio descent is claimed in this branch.  It is a high-derivative / endpoint-concentration channel.

---

## 3. Middle-scale branch

If

\[
\mathcal E_{\rm edge}
<\frac12\mathcal B_\Sigma,
\]

then

\[
\int_\delta^{1-\delta}Q_\Sigma(t)dt
\ge\frac12\mathcal B_\Sigma.
\]

The interval length is `1-2 delta`, so there exists

\[
t_*\in[\delta,1-\delta]
\]

with

\[
\boxed{
Q_\Sigma(t_*)
\ge
\frac{\mathcal B_\Sigma}{2(1-2\delta)}.
}
\]

The derivative field in this witness is smoothed by covariance

\[
\Sigma_{\rm child}
=(1-t_*)\Sigma.
\]

Therefore, in every eigen-direction,

\[
\delta\Sigma
\preceq
\Sigma_{\rm child}
\preceq
(1-\delta)\Sigma.
\]

For a well-conditioned parent Gaussian with characteristic length `R`, the child length obeys

\[
\boxed{
\sqrt\delta\,R
\lesssim
R_{\rm child}
\lesssim
\sqrt{1-\delta}\,R.
}
\]

Thus the middle branch produces a curvature witness at a strict fixed fraction of the parent scale.

---

## 4. Repeated descent

If the middle branch repeats `N` times with the same `delta`, then the descendant scales satisfy

\[
R_N
\le
(1-\delta)^{N/2}R_0.
\]

Hence reaching a terminal natural scale `O(1)` from parent scale `R_0` requires only

\[
\boxed{
N
=O_\delta(\log R_0)
}
\]

fixed-ratio descents.

At every descent, one obtains a positive curvature witness.  If the descent fails at any stage, the failure is an endpoint derivative-concentration event.

This produces a finite-depth scale tree on the active mesoscopic ladder.

---

## 5. DSD interpretation

A residual channel at one resolution cannot remain an untyped unresolved object.

It must either

\[
\boxed{
\text{move to a child resolution by a fixed factor}
}
\]

or

\[
\boxed{
\text{concentrate derivative activity at a scale endpoint}.
}
\]

Thus the residual scale graph has controlled edge lengths rather than arbitrary jumps.

---

## 6. Limitation

The curvature witnesses obtained at different scales are not yet proved to occupy orthogonal Fourier bands or disjoint spacetime regions.  Therefore summing their lower bounds may still double-count the same derivative event.

The next target is an almost-orthogonality / Carleson packing statement for the middle-scale witnesses, with endpoint concentration retained as the complementary high-derivative branch.

Status: **FIXED-RATIO SCALE DESCENT CLOSED / CURVATURE-WITNESS ALMOST-ORTHOGONALITY REMAINS OPEN**.
