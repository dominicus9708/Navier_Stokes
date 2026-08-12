# Middle strain eigenvalue as a growth channel

Date: 2026-08-12

Status: **DERIVED ALGEBRAIC BOUND + EXTERNAL REGULARITY ANCHOR + OPEN PROOF OBLIGATION**.

## 1. Ordered trace-free strain eigenvalues

Let

\[
\lambda_1\le\lambda_2\le\lambda_3,
\qquad
\lambda_1+\lambda_2+\lambda_3=0.
\]

If `lambda_2 <= 0`, then

\[
-\det S\le0.
\]

If `lambda_2>0`, write

\[
b=\lambda_2>0,
\qquad
c=\lambda_3\ge b,
\qquad
\lambda_1=-(b+c).
\]

Then

\[
-\det S=bc(b+c),
\]

and

\[
|S|^2=(b+c)^2+b^2+c^2
=2(b^2+bc+c^2).
\]

Therefore

\[
\frac12\lambda_2|S|^2-(-\det S)
=b(b^2+bc+c^2)-bc(b+c)
=b^3\ge0.
\]

Hence the general pointwise bound

\[
\boxed{
-\det S
\le
\frac12\lambda_2^+|S|^2
}
\]

holds for ordered trace-free strain eigenvalues.

This is elementary algebra and is not claimed as a new strain regularity theorem.

## 2. Why `lambda_2^+` is structurally relevant

In the strain formulation of incompressible Navier–Stokes, established work relates strain/enstrophy growth to the determinant of `S` and gives regularity/blow-up criteria involving the positive part of the middle eigenvalue.

The DSD application therefore promotes

\[
\lambda_2^+
\]

to an explicit typed danger channel rather than attempting to rediscover the same criterion under a new name.

## 3. Exact Gaussian benchmark

For the current Gaussian control case, the vorticity direction is the middle strain eigenvector and

\[
\lambda_2=4ze^{-|x|^2}.
\]

Thus the positive-middle-eigenvalue region is exactly the upper half-space `z>0` for the benchmark.

On that half-space,

\[
-\det S
=16ze^{-3r^2}
\left[8z^2+\rho^2(2r^2-3)^2\right],
\qquad
\rho^2=x^2+y^2.
\]

Exact cylindrical integration gives

\[
\int_{z>0}(-\det S)dx
=\frac{248\pi}{81}.
\]

The elementary upper bound integrates to

\[
\int_{z>0}\frac12\lambda_2|S|^2dx
=\frac{344\pi}{81}.
\]

Their ratio is

\[
\frac{344}{248}=\frac{43}{31}>1.
\]

This is an exact benchmark verification of the bound, not a time-dependent a-priori estimate.

## 4. DSD interpretation

Keep at least the following channels separately:

\[
\lambda_2^+,
\qquad
|S|^2,
\qquad
-\det S,
\qquad
\gamma_+,
\qquad
|\omega|^2.
\]

The determinant-growth channel and the vorticity-alignment stretching channel are related but not identical pointwise. They must not be collapsed merely because both can diagnose nonlinear amplification.

## 5. Proof target

A conservative proof route can now use two already recognizable external gates:

1. critical velocity control such as `L^infty_t L^3_x`;
2. strain control through suitable scale-critical norms of `lambda_2^+`.

The DSD task is to determine whether the all-center/local/cross-interaction channels can force one of those external gates to remain finite.

The missing statement is therefore not the algebraic bound above, but an a-priori time-space estimate on `lambda_2^+` for arbitrary admissible smooth data.

Status: **OPEN PROOF OBLIGATION**.

## External anchor

Evan Miller, *A Regularity Criterion for the Navier–Stokes Equation Involving Only the Middle Eigenvalue of the Strain Tensor*, Archive for Rational Mechanics and Analysis 235 (2020), 99–139, DOI `10.1007/s00205-019-01419-z`.
