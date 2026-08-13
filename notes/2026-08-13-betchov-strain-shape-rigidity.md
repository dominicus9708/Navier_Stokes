# Betchov strain-shape rigidity: source saturation forces an axisymmetric extensional plane

Date: 2026-08-13

Status: **CLASSICAL BETCHOV IDENTITY + DERIVED SHARP TRACE-FREE MATRIX RIGIDITY / OPEN JOINT SOURCE-GN SATURATION CLOSURE**.

The scalar sharp-GN source estimate constrains the vorticity magnitude.  Independently, the classical Betchov relation constrains the **strain shape** of any source-saturating state.  Combining Betchov with the sharp determinant bound for trace-free symmetric `3x3` matrices shows that maximal positive global vortex stretching requires an axisymmetric strain with one compressive direction and a two-dimensional degenerate extensional plane.

External anchor: R. Betchov, *An inequality concerning the production of vorticity in isotropic turbulence*, Journal of Fluid Mechanics 1 (1956), 497--504.

---

## 1. Betchov relation

For smooth sufficiently decaying incompressible flow on `R3`, let

\[
S=\frac12(\nabla u+\nabla u^T),
\qquad
\omega=\nabla\times u.
\]

The Betchov homogeneity relation is

\[
\boxed{
\int\operatorname{tr}(S^3)dx
=-\frac34
\int\omega\cdot S\omega dx.
}
\]

Write

\[
Q=\int\omega\cdot S\omega dx.
\]

Since `tr S=0`, the eigenvalues satisfy

\[
\lambda_1+\lambda_2+\lambda_3=0
\]

and Newton's identity gives

\[
\operatorname{tr}(S^3)=3\det S.
\]

Therefore

\[
\boxed{
Q=-4\int\det S\,dx.
}
\]

The identity is global; `omega.S.omega=-4 det S` is **not** asserted pointwise.

---

## 2. Sharp determinant bound for trace-free strain

Let `S` be any real symmetric trace-free `3x3` matrix.  For fixed Frobenius norm

\[
|S|^2=\lambda_1^2+\lambda_2^2+\lambda_3^2,
\]

maximize `|lambda1 lambda2 lambda3|` subject to

\[
\lambda_1+\lambda_2+\lambda_3=0.
\]

Lagrange multipliers, or direct reduction with `lambda3=-lambda1-lambda2`, gives equality only when two eigenvalues coincide.  Up to permutation/sign,

\[
(\lambda_1,\lambda_2,\lambda_3)
=(-2a,a,a).
\]

Then

\[
|S|^2=6a^2,
\qquad
|\det S|=2|a|^3.
\]

Hence

\[
\boxed{
|\det S|
\le
\frac{1}{3\sqrt6}|S|^3.
}
\]

Equivalently,

\[
\boxed{
|\operatorname{tr}(S^3)|
\le
\frac1{\sqrt6}|S|^3.
}
\]

---

## 3. Global source bound and equality geometry

Using Betchov,

\[
Q=-4\int\det S.
\]

Therefore

\[
\boxed{
|Q|
\le
\frac{4}{3\sqrt6}
\int|S|^3dx.
}
\]

For **positive** source `Q>0`, the source-favorable sign is

\[
\det S<0.
\]

The pointwise matrix extremizer then has ordered eigenvalues

\[
\boxed{
\lambda_1=-2a,
\qquad
\lambda_2=\lambda_3=a,
\qquad a>0.
}
\]

Thus the source-optimal strain consists of

- one compressive normal direction;
- a two-dimensional degenerate extensional plane.

Near saturation of the global determinant bound requires, in an `|S|^3`-weighted sense,

1. negligible source-opposing `det S>0` contribution;
2. small deviation of the normalized eigenvalue triple from the `(-2,1,1)` orbit.

---

## 4. Strain-shape defect channel

On points with `S!=0`, define the positive-source determinant efficiency

\[
\boxed{
\Theta_S
=
3\sqrt6\,
\frac{(-\det S)_+}{|S|^3}
\in[0,1].
}
\]

Define the strain-shape defect

\[
\boxed{
\delta_S^{\rm shape}=1-\Theta_S.
}
\]

Then

\[
\boxed{
4(-\det S)_+
=
\frac{4}{3\sqrt6}
|S|^3(1-\delta_S^{\rm shape}).
}
\]

A Betchov-source-saturating sequence must drive the `|S|^3`-weighted mean of `delta_S^shape` toward zero.

This is a new DSD diagonal strain-shape channel; it is independent of the vorticity-magnitude sharp-GN ratio.

---

## 5. Relation to the middle eigenvalue

At the positive-source matrix extremizer,

\[
\lambda_2^+=a
=\frac{|S|}{\sqrt6}.
\]

Thus determinant-source saturation necessarily activates the positive-middle-strain channel rather than avoiding it.

The existing middle-eigenvalue regularity criteria therefore remain directly relevant to any residual source-saturating state.

---

## 6. Relation to the axis-conversion channel

Let `e1` be the compressive eigenvector and `e2,e3` span the degenerate extensional plane.  For a unit vorticity/projective axis `n`, write

\[
b_i=(n\cdot e_i)^2.
\]

The exact axis-conversion variance is

\[
\chi_n^2
=\sum_{i<j}b_ib_j(\lambda_i-\lambda_j)^2.
\]

At `(-2a,a,a)`,

\[
\lambda_2-\lambda_3=0
\]

and both remaining gaps have magnitude `3a`.  Therefore

\[
\boxed{
\chi_n^2
=9a^2b_1(1-b_1).
}
\]

Hence strain-driven axis conversion vanishes in two extreme cases:

1. `n` is the compressive normal (`b1=1`);
2. `n` lies entirely in the degenerate extensional plane (`b1=0`).

The second case is source-favorable for vorticity stretching.

---

## 7. Source-favorable vorticity orientation

For exact `(-2a,a,a)` strain,

\[
\gamma(n)
=n^TSn
=a(1-3b_1).
\]

The maximal stretching rate is

\[
\boxed{\gamma_{\max}=a}
\]

and is attained for every vorticity direction in the extensional plane `b1=0`.

If

\[
\gamma\ge(1-\varepsilon)a,
\]

then

\[
1-3b_1\ge1-\varepsilon
\]

so

\[
\boxed{
b_1\le\varepsilon/3.}
\]

Thus simultaneous near-saturation of

1. the determinant strain-shape bound; and
2. pointwise extensional stretching

pushes vorticity into an approximately two-dimensional extensional plane.

---

## 8. New simultaneous-saturation geometry

A residual source-saturating normalized state must now satisfy at least two largely independent near-extremal structures:

### Magnitude side

`rho=|omega|` must approach the sharp Gagliardo--Nirenberg optimizer manifold on the active scale, unless compactness gives a strict GN gap.

### Strain-shape side

The `|S|^3`-weighted strain eigenvalue shape must approach

\[
\boxed{(-2,1,1)}.
\]

If vorticity also realizes the positive extensional rate, it must lie predominantly inside the corresponding two-dimensional extensional plane.

This creates a new rigidity target:

\[
\boxed{
\text{sharp-GN magnitude near extremizer}
+\text{axisymmetric strain near extremizer}
+\text{divergence-free vorticity geometry}
\Longrightarrow
\text{compatible or impossible?}
}
\]

---

## 9. Important boundary

The Betchov identity is global.  Localizing it introduces boundary/transport terms and is not performed silently here.

The determinant shape channel is therefore first used as a **global or buffered-with-explicit-boundary** diagnostic.  It must not be inserted pointwise into the vorticity magnitude equation as though `omega.S.omega=-4 det S` held pointwise.

Status: **SECOND NEAR-EXTREMIZER GEOMETRY IDENTIFIED / JOINT GN--STRAIN RIGIDITY OPEN**.
