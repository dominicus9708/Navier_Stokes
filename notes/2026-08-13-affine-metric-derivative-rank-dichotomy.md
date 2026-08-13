# Affine metric versus derivative covariance: anisotropic viscous cost or derivative-rank reduction

Date: 2026-08-13

Status: **EXACT COVARIANCE IDENTITY + DERIVED RANK-REDUCTION DICHOTOMY / DYNAMIC LOW-DIMENSIONAL RIGIDITY OPEN**.

The affine-frame vorticity equation contains the uniformly/anisotropically elliptic diffusion matrix

\[
A(s)=F(s)^{-1}F(s)^{-T},
\qquad
\det A=1.
\]

When the coarse affine deformation becomes badly conditioned, `A` develops a very strong diffusion direction and a very weak one.  This note shows that a solution can avoid paying a correspondingly large viscous cost only by concentrating its **spatial derivative covariance** into the weak-diffusion subspace.

This is the direct bridge from the affine-deformation branch to the existing derivative-covariance hierarchy.

---

## 1. Spatial derivative covariance

For a sufficiently regular transformed vorticity `W`, define

\[
P(s)=\int |\nabla W|^2dz.
\]

When `P>0`, define the spatial derivative covariance

\[
\boxed{
R(s)
=\frac1{P(s)}
\left[
\int \partial_iW\cdot\partial_jW\,dz
\right]_{i,j=1}^3.
}
\]

Then

\[
R=R^T,
\qquad
R\succeq0,
\qquad
\boxed{\operatorname{tr}R=1.}
\]

Thus `R` is a trace-one positive semidefinite matrix describing which **spatial derivative axes** carry the palinstrophy of `W`.

This differs from the previously used covariance of the **vorticity-vector components**.  The two objects must not be conflated.

---

## 2. Exact anisotropic diffusion identity

The transformed viscous dissipation at derivative order zero is

\[
D_A(s)
=\int \nabla W:A(s)\nabla W\,dz.
\]

Because `A` is spatially constant,

\[
\begin{aligned}
D_A
&=\sum_{i,j}A_{ij}
\int \partial_iW\cdot\partial_jW\,dz\\
&=P\,\operatorname{tr}(AR).
\end{aligned}
\]

Hence exactly

\[
\boxed{
D_A=P\operatorname{tr}(AR).
}
\]

This is a static-aggregation pairing between the diffusion metric and the derivative covariance.

---

## 3. Resolve in the diffusion eigenbasis

Let

\[
A e_i=\lambda_i e_i,
\qquad
0<\lambda_1\le\lambda_2\le\lambda_3.
\]

Define

\[
\boxed{
r_i=e_i^TRe_i\ge0.}
\]

Because `tr R=1`,

\[
\boxed{r_1+r_2+r_3=1.}
\]

The diffusion identity becomes

\[
\boxed{
\frac{D_A}{P}
=\lambda_1r_1+\lambda_2r_2+\lambda_3r_3.
}
\]

Therefore

\[
\boxed{
r_3\le\frac{D_A}{\lambda_3P}.}
\]

Since both `lambda_2` and `lambda_3` are at least `lambda_2`,

\[
\boxed{
r_2+r_3
\le
\frac{D_A}{\lambda_2P}.}
\]

More generally, every spectral subspace on which `A>=Lambda I` carries at most a fraction

\[
\boxed{
\frac{D_A}{\Lambda P}
}
\]

of the total spatial derivative energy.

---

## 4. Relation to the affine singular values

Let the singular values of `F` be

\[
\sigma_1\ge\sigma_2\ge\sigma_3>0,
\qquad
\sigma_1\sigma_2\sigma_3=1.
\]

Then the eigenvalues of

\[
A=F^{-1}F^{-T}
\]

are

\[
\boxed{
\lambda_1=\sigma_1^{-2},
\qquad
\lambda_2=\sigma_2^{-2},
\qquad
\lambda_3=\sigma_3^{-2}.
}
\]

If

\[
\kappa(F)=\sigma_1/\sigma_3\to\infty,
\]

volume preservation forces

\[
\sigma_1\to\infty,
\qquad
\sigma_3\to0
\]

along a subsequence, and hence

\[
\boxed{
\lambda_1\to0,
\qquad
\lambda_3\to\infty.
}
\]

The middle eigenvalue may tend to zero, remain order one, or diverge.

---

## 5. Instantaneous derivative-rank dichotomy

Suppose the normalized effective diffusion ratio satisfies

\[
\boxed{
D_A/P\le M
}
\]

at a sequence of states for which

\[
\lambda_3\to\infty.
\]

Then

\[
\boxed{r_3\to0.}
\]

Thus the spatial derivative covariance loses its component in the strongest-diffusion direction and becomes asymptotically supported in a two-dimensional spatial subspace.

If in addition

\[
\lambda_2\to\infty,
\]

then

\[
\boxed{r_2+r_3\to0,}
\]

so

\[
\boxed{r_1\to1.}
\]

The derivative covariance becomes asymptotically rank one.

Hence

\[
\boxed{
\text{highly anisotropic }A
\Longrightarrow
\text{large viscous cost}
\quad\text{or}\quad
\text{derivative-rank reduction}.
}
\]

---

## 6. Spacetime version

Let

\[
I_\Lambda
=\{s:\lambda_3(s)\ge\Lambda\}.
\]

The strong-axis derivative energy is

\[
P_3(s)
=\int |e_3(s)\cdot\nabla W|^2dz
=P(s)r_3(s).
\]

Since

\[
D_A(s)\ge\lambda_3(s)P_3(s),
\]

we obtain

\[
\boxed{
\int_{I_\Lambda}P_3(s)ds
\le
\frac1\Lambda
\int_{I_\Lambda}D_A(s)ds.
}
\]

Therefore, if the total anisotropic viscous budget remains bounded while

\[
\lambda_3\to\infty
\]

uniformly on a nondegenerate time window, then

\[
\boxed{
e_3(s)\cdot\nabla W\to0
\quad\text{in }L^2_{s,z}.}
\]

If `lambda_2` also diverges uniformly, both strong-axis derivatives vanish in spacetime `L2`.

If the large eigenvalue occurs only on a time set whose measure collapses, that is a **temporal affine-deformation concentration** branch and must be tracked separately.

---

## 7. Low-dimensional interpretation and its limit

If the strongest diffusion eigenvector converges to a fixed direction `n` and

\[
n\cdot\nabla W=0,
\]

then the limiting field depends on at most two spatial coordinates.  This is a derivative-level dimensional reduction, not a claim that the vector field has only two components.

Likewise, two independent vanishing directional derivatives reduce the spatial dependence to one coordinate.

However, the eigenvectors of `A(s)` may rotate with time.  The present covariance estimate alone does not prove that a fixed spatial direction becomes ignorable.  A dynamic rigidity step is still needed to control the temporal motion of the strong-diffusion eigenspaces.

---

## 8. Relation to residual counter-deformation

The previous exact factorization is

\[
H=FG.
\]

If `F` becomes very anisotropic but full material deformation `H` remains bounded, then `G` must become comparably anisotropic.

At the same time, the affine frame carries diffusion metric

\[
A=F^{-1}F^{-T}.
\]

Thus the counter-deformation branch must simultaneously manage

1. large residual deformation `G`, and
2. a highly anisotropic diffusion metric `A`.

Avoiding the latter's viscous cost forces the derivative covariance `R` to collapse toward the weak-diffusion subspace.

This is a substantially more restrictive state than a generic large-deformation event.

---

## 9. DSD/static-aggregation interpretation

The exact pairing

\[
\boxed{
D_A/P=\operatorname{tr}(AR)
}

is a natural two-block static aggregate:

- `A`: axis property supplied by the coarse affine geometry;
- `R`: distribution of spatial derivative content among those axes.

A large axis weight is harmless only if the corresponding derivative channel becomes absent/negligible.

Thus the next DSD state vector for the counter-deformation branch should retain

\[
\boxed{
(\lambda_1,\lambda_2,\lambda_3;
 r_1,r_2,r_3;
 \kappa(F),\kappa(G),\kappa(H);D_A/P).
}
\]

---

## 10. Remaining proof-producing target

The next step is to exploit the dynamic incompatibility between

- residual counter-deformation requiring large strain in the affine frame;
- derivative covariance avoiding strong-diffusion directions;
- and the nonlinear vorticity stretching needed for repeated first-hitting amplification.

A particularly promising refinement is to track the **rotation of the strong-diffusion eigenspace**.  Persistent rotation while its directional derivative stays small may force more than one independent directional derivative to vanish, while little rotation approaches a fixed lower-dimensional flow geometry.

Status: **ANISOTROPIC-DIFFUSION / DERIVATIVE-RANK DICHOTOMY CLOSED / EIGENSPACE-ROTATION RIGIDITY OPEN**.
