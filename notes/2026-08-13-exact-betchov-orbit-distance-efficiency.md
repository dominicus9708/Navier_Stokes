# Exact distance-to-Betchov-orbit formula for trace-free strain determinant efficiency

Date: 2026-08-13

Status: **EXACT FINITE-DIMENSIONAL IDENTITY / STRAIN-SHAPE STRICT GAP**.

For a normalized trace-free symmetric `3x3` strain shape on the positive-vortex-stretching determinant branch, the loss in the sharp determinant efficiency is an exact polynomial of the Frobenius distance to the Betchov orbit.

This removes the need for a qualitative compactness statement at the finite-dimensional strain-shape level.

---

## 1. Normalized strain shape

Let

\[
A=A^T,
\qquad
\operatorname{tr}A=0,
\qquad
|A|_F=1.
\]

Let its ordered eigenvalues be

\[
\lambda_1\le\lambda_2\le\lambda_3.
\]

On the source-positive Betchov branch assume

\[
\det A\le0.
\]

The determinant inequality is

\[
\boxed{
-\det A
\le
\frac1{3\sqrt6}.
}
\]

Define the normalized determinant efficiency

\[
\boxed{
\eta_{\det}(A)
=3\sqrt6\,[-\det A]
\in[0,1].
}
\]

---

## 2. Betchov orbit

Let

\[
A_B
=\frac1{\sqrt6}
\operatorname{diag}(-2,1,1).
\]

The full Betchov orbit is

\[
\boxed{
\mathcal O_B
=\{RA_BR^T:R\in SO(3)\}.
}
\]

Define

\[
\boxed{
d(A)
=\operatorname{dist}_F(A,\mathcal O_B).}
\]

Because both matrices are symmetric, orthogonal conjugation aligns eigenvectors optimally.  Thus the distance is the Euclidean distance between the ordered eigenvalue triples.

---

## 3. Distance is determined by the compressive eigenvalue

Write

\[
x=-\lambda_1>0.
\]

Since `tr A=0`,

\[
\lambda_2+\lambda_3=x.
\]

Since `|A|_F=1`,

\[
\lambda_2^2+\lambda_3^2=1-x^2.
\]

The Betchov eigenvalue vector is

\[
\left(-\sqrt{\frac23},\frac1{\sqrt6},\frac1{\sqrt6}\right).
\]

Therefore

\[
\begin{aligned}
d^2
&=2-2\langle\lambda,\lambda_B\rangle\\
&=2-2\sqrt{\frac32}\,x.
\end{aligned}
\]

Hence

\[
\boxed{
\sqrt{\frac32}\,x
=1-\frac{d^2}{2}.
}
\]

---

## 4. Determinant in terms of `x`

Using the trace and norm constraints,

\[
\lambda_2\lambda_3
=\frac{x^2-(1-x^2)}{2}
=x^2-\frac12.
\]

Thus on the negative-determinant branch

\[
\boxed{
-\det A
=x\left(x^2-\frac12\right).
}
\]

The branch begins at `x=1/sqrt(2)` where the determinant is zero and ends at

\[
x=\sqrt{\frac23}
\]

at the Betchov extremizer.

---

## 5. Exact distance-efficiency identity

Set

\[
z=\frac{d^2}{2}.
\]

Then

\[
x=\sqrt{\frac23}(1-z).
\]

Substitution gives

\[
\eta_{\det}
=(1-z)(1-8z+4z^2)
=1-9z+12z^2-4z^3.
\]

Therefore

\[
\boxed{
1-\eta_{\det}
=z(3-2z)^2.
}
\]

Since `z=d^2/2`,

\[
\boxed{
1-\eta_{\det}(A)
=
\frac{d(A)^2}{2}
\left[3-d(A)^2\right]^2.
}
\]

This is exact.

---

## 6. Immediate strict-gap corollary

If

\[
d(A)\ge\delta>0,
\]

then

\[
\boxed{
\eta_{\det}(A)
\le
1-rac{\delta^2}{2}(3-\delta^2)^2.
}
\]

Thus a coherent strain shape that remains a fixed distance from the Betchov orbit has an explicit source-efficiency deficit.

No functional-analytic compactness argument is required for this finite-dimensional step.

---

## 7. Combine with Gaussian strain-shape variance

The Gaussian residual state contains

\[
D_{S,\rm shape}.
\]

If this is small, the local strain field is close in weighted `L2` to scalar multiples of one dominant normalized strain shape `A_*`.

The coherent-shape branch then splits:

### B1 — Betchov-near shape

\[
\operatorname{dist}(A_*,\mathcal O_B)\ll1.
\]

This is the genuine biaxial compression/extensional-plane branch.  The existing compression-diffusion, precursor-reservoir, covariance-normal-depletion, and eigenaxis-rotation channels apply.

### B2 — Betchov-far shape

\[
\operatorname{dist}(A_*,\mathcal O_B)\ge\delta.
\]

Then the exact formula forces a determinant/source efficiency loss

\[
\boxed{
1-\eta_{\det}(A_*)
\ge
\frac{\delta^2}{2}(3-\delta^2)^2.
}
\]

Thus strain-shape coherence alone is not dangerous; only coherence near the Betchov orbit avoids a finite-dimensional determinant deficit.

---

## 8. Relation to the four-channel residual state

The hard residual route is now refined to

\[
\boxed{
D_{S,\rm shape}\text{ large}
}
\]

or, if `D_S,shape` is small,

\[
\boxed{
A_*\text{ Betchov-near}
}
\]

or

\[
\boxed{
\text{strict determinant source deficit}.
}
\]

The Betchov-near case is already the affine compression-diffusion branch isolated in the current frontier.

---

## 9. Claim boundary

The distance-efficiency identity is finite-dimensional and exact.

To convert small `D_S,shape` into a quantitative bound on the **spatially averaged cubic determinant** one additionally needs a stability estimate for the cubic determinant under weighted `L2/L3` strain-shape perturbations.  First-hitting BMO gives the required finite higher moments in principle, but that functional estimate is kept as the next separate step rather than hidden in the present identity.

Status: **EXACT BETCHOV SHAPE GAP CLOSED / WEIGHTED CUBIC TRANSFER FROM SHAPE VARIANCE IS NEXT**.
