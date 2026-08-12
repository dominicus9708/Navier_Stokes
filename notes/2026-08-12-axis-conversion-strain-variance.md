# Axis-conversion intensity as strain-eigenvalue variance

Date: 2026-08-12

Status: **DERIVED AXIS-MATRIX IDENTITY + DSD OFF-DIAGONAL DECOMPOSITION / OPEN DYNAMIC CONTROL**.

This note refines the principal-to-off-axis vorticity conversion channel

\[
\chi_n=|P_{n^\perp}Sn|
\]

appearing in the local covariance-axis dynamics.

## 1. Exact variance identity

Let `S` be symmetric with ordered eigenpairs

\[
S e_i=\lambda_i e_i,
\qquad i=1,2,3,
\]

and let `n` be any unit vector.  Define

\[
\boxed{
b_i=(n\cdot e_i)^2,
\qquad
b_i\ge0,
\qquad
\sum_i b_i=1.
}
\]

Since

\[
\chi_n^2
=|Sn|^2-(n\cdot Sn)^2,
\]

we obtain

\[
\chi_n^2
=
\sum_i\lambda_i^2b_i
-
\left(\sum_i\lambda_i b_i\right)^2.
\]

Using the elementary weighted-variance identity,

\[
\boxed{
\chi_n^2
=
\sum_{i<j}
b_i b_j(\lambda_i-\lambda_j)^2.
}
\]

Thus the axis-conversion intensity is exactly the variance of the strain eigenvalues sampled by the directional weights of `n`.

## 2. Zero-conversion characterization

The identity gives

\[
\chi_n=0
\]

if and only if all strain eigenvalues carrying nonzero `b_i` are equal.

In particular, for a simple strain spectrum,

\[
\boxed{
\chi_n=0
\Longleftrightarrow
n\text{ is a strain eigenvector}.
}
\]

If `S` has a degenerate eigenspace, any `n` inside that eigenspace also gives zero conversion.

Hence strain can rotate/populate the off-axis vorticity sector only when the vorticity covariance axis samples **different strain eigenvalues**.

## 3. Universal range bound

Because the weighted variance of numbers in an interval is at most one quarter of the squared range,

\[
\boxed{
\chi_n
\le
\frac{\lambda_3-\lambda_1}{2}.
}
\]

For incompressible strain,

\[
\lambda_1+\lambda_2+\lambda_3=0.
\]

One has

\[
(\lambda_3-\lambda_1)^2
\le
2|S|^2,
\]

so

\[
\boxed{
\chi_n
\le
\frac{|S|}{\sqrt2}.
}
\]

This is only an upper bound; it does not control the off-axis conversion without information about the vorticity-axis defect and strain magnitude.

## 4. Relation to the conversion production term

The local covariance dynamics contains

\[
\mathcal X_n
=2\int\varphi
(n\cdot\omega)
\omega_\perp\cdot P_\perp Sn\,dx.
\]

The previous Cauchy bound was

\[
|\mathcal X_n|
\le
2E_r\sqrt{\mu_1(1-\mu_1)}
\|\chi_n\|_\infty.
\]

Substituting the variance identity shows that conversion requires three ingredients simultaneously:

1. a nonzero principal vorticity component `mu_1`;
2. a nonzero off-axis covariance defect `Pi=1-mu_1`;
3. a mismatch between the vorticity principal axis and distinct strain eigendirections.

Thus near the one-axis limit,

\[
|\mathcal X_n|
=O(\sqrt\Pi)
\]

even before any strain regularity estimate is invoked.

## 5. Two-gap decomposition

Writing the ordered gaps

\[
g_{12}=\lambda_2-\lambda_1,
\qquad
 g_{23}=\lambda_3-\lambda_2,
\]

we have

\[
\lambda_3-\lambda_1=g_{12}+g_{23}
\]

and

\[
\boxed{
\chi_n^2
=
 b_1b_2 g_{12}^2
+b_2b_3 g_{23}^2
+b_1b_3(g_{12}+g_{23})^2.
}
\]

This keeps the two strain-gap channels typed separately.

The `lambda_2^+` regularity criterion does not directly control either gap, so this conversion channel must not be collapsed into the middle-eigenvalue channel.

## 6. DSD axis-property matrix

At a point, retain

\[
\boxed{
\mathsf A_{\omega S}
=
\left(
\mu_1,\Pi,
 b_1,b_2,b_3,
\lambda_1,\lambda_2,\lambda_3,
 g_{12},g_{23},
\chi_n
\right).
}
\]

Interpretation:

- `b_i`: diagonal directional participation of the vorticity covariance axis in the strain eigenframe;
- `g_ij`: strain-axis separation;
- `b_i b_j g_ij^2`: off-diagonal axis-conversion channels;
- `chi_n`: their aggregate conversion amplitude.

This is an exact instance of the axis-property / channel-matrix viewpoint.

## 7. Residual-class consequence

A residual singular cascade that must maintain multi-axis vorticity content cannot rely on principal-to-off-axis conversion unless it also maintains significant strain-axis variance along the vorticity principal axis.

Hence the dynamic residual branch becomes

\[
\boxed{
\text{off-axis self stretching}
\quad\text{or}\quad
\text{strain-eigenvalue-gap weighted axis mixing}.
}
\]

The second branch can fail either because

- the strain eigenvalues become locally degenerate, or
- the vorticity covariance axis aligns with a strain eigenspace.

Both suppress direct axis conversion.

## 8. Open target

A useful next estimate would connect the time/space integral of

\[
\sum_{i<j}b_i b_j(\lambda_i-\lambda_j)^2
\]

to one of the existing finite/critical quantities:

- middle-eigenvalue norms;
- palinstrophy;
- local covariance defect;
- higher-derivative sparseness;
- or moving-sphere dissipation.

No such arbitrary-data estimate is established here.

Status: **OPEN STRAIN-GAP / AXIS-MIXING CONTROL**.
