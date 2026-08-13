# Betchov + sharp-GN equality incompatibility for incompressible strain

Date: 2026-08-13

Status: **EXACT NONATTAINMENT OF THE FORMAL PRODUCT EXTREMIZER / UNIVERSAL QUANTITATIVE GAP NOT YET PROVED**.

The Betchov strain-shape bound and the scalar sharp Gagliardo--Nirenberg bound can be combined without an `L3` Riesz-transform constant.  More importantly, the formal equality conditions of the combined estimate are incompatible with the Fourier structure of a nonzero incompressible strain field.

---

## 1. Exact `L2` identities for incompressible strain

For a smooth decaying divergence-free velocity field,

\[
S=\frac12(\nabla u+\nabla u^T),
\qquad
\omega=\nabla\times u.
\]

Fourier orthogonality gives

\[
\boxed{
\|S\|_2^2
=\frac12\|\omega\|_2^2
=\frac12E.
}
\]

Applying the same identity after one spatial derivative,

\[
\boxed{
\|\nabla S\|_2^2
=\frac12\|\nabla\omega\|_2^2
=\frac12P.
}
\]

---

## 2. Betchov + determinant + sharp GN source bound

The Betchov relation gives

\[
Q=-4\int\det S\,dx.
\]

For trace-free symmetric `3x3` matrices,

\[
|\det S|
\le
\frac1{3\sqrt6}|S|^3.
\]

Hence

\[
Q
\le
\frac4{3\sqrt6}
\|S\|_3^3.
\]

Apply the sharp scalar GN inequality to the scalar magnitude `sigma=|S|`:

\[
\|S\|_3^3
\le
C_{\rm GN}^3
\|S\|_2^{3/2}
\|\nabla|S|\|_2^{3/2}.
\]

Kato's pointwise inequality gives

\[
|\nabla|S||\le|\nabla S|.
\]

Using the exact `L2` identities,

\[
\boxed{
Q
\le
\frac{C_{\rm GN}^3}{3\sqrt3}
E^{3/4}P^{3/4}.
}
\]

This bound contains no separate `L3` Riesz-transform constant.

---

## 3. Three simultaneous equality requirements

To attain the formal product constant with `Q>0`, a nonzero sequence would have to approach equality in all of the following.

### A. Determinant shape

At almost every strain-active point,

\[
\boxed{
S/|S|
\text{ has eigenvalue shape }
(-2,1,1)/\sqrt6
}
\]

up to rotation, with the source-favorable sign.

### B. Scalar sharp GN

The scalar magnitude

\[
\sigma=|S|
\]

must approach the sharp-GN ground-state optimizer manifold modulo amplitude, translation and dilation.

### C. Kato equality

The gradient inequality must approach equality:

\[
\boxed{
\|\nabla|S|\|_2
/\|\nabla S\|_2
\to1.
}
\]

Writing

\[
S=\sigma\widehat S,
\qquad
|\widehat S|=1,
\]

one has the exact decomposition

\[
\boxed{
|\nabla S|^2
=|\nabla\sigma|^2
+\sigma^2|\nabla\widehat S|^2.
}
\]

Thus Kato near-equality forces the normalized strain-matrix direction `Shat` to become nearly spatially constant in the `sigma^2`-weighted gradient sense.

---

## 4. Exact fixed-shape incompatibility

Suppose exact equality produced a strain field of the form

\[
\boxed{
S(x)=a(x)A
}
\]

with one fixed nonzero symmetric trace-free matrix `A` having

\[
\det A\ne0.
\]

For a divergence-free velocity, every nonzero Fourier strain mode is

\[
\widehat S(\xi)
=\frac{i}{2}
\left(
\xi\otimes\widehat u(\xi)
+\widehat u(\xi)\otimes\xi
\right),
\]

with

\[
\xi\cdot\widehat u(\xi)=0.
\]

For fixed nonzero `xi`, the symmetric matrix

\[
M=\frac12(\xi\otimes v+v\otimes\xi),
\qquad
\xi\cdot v=0,
\]

has eigenvalues

\[
\boxed{
\left(
\frac{|\xi||v|}{2},
-\frac{|\xi||v|}{2},
0
\right).
}
\]

Therefore

\[
\boxed{
\det M=0
}
\]

for every Fourier mode.

But if

\[
\widehat S(\xi)=\widehat a(\xi)A
\]

and `det A !=0`, then every frequency with `ahat(xi) !=0` would have

\[
\det\widehat S(\xi)
e0,
\]

contradicting the incompressible Fourier-mode structure.

Hence

\[
\boxed{
S(x)=a(x)A,
\quad
\det A\ne0,
\quad
S=\operatorname{sym}\nabla u,
\quad
\nabla\cdot u=0
\Longrightarrow
S\equiv0.
}
\]

---

## 5. Why this kills the exact formal extremizer

The positive-source determinant extremizer has fixed matrix shape

\[
A_*
\sim
\operatorname{diag}(-2,1,1),
\]

so

\[
\det A_*\ne0.
\]

Sharp-GN equality gives a nonzero scalar ground-state magnitude.  Kato equality freezes the matrix direction.

Thus exact simultaneous equality would require

\[
S(x)=Q_{\rm GN}(x)A_*
\]

up to the scalar and spatial symmetries, which is forbidden by the Fourier compatibility result above.

Therefore

\[
\boxed{
\text{the formal product constant }
\frac{C_{\rm GN}^3}{3\sqrt3}
\text{ is not attained by any nonzero incompressible strain field.}
}
\]

---

## 6. What is still needed for a universal strict numerical gap

Nonattainment alone does **not** automatically prove a universal number `delta_*>0` such that

\[
Q
\le
(1-\delta_*)
\frac{C_{\rm GN}^3}{3\sqrt3}
E^{3/4}P^{3/4}
\]

for every admissible field.

A maximizing sequence could in principle fail compactness through the sharp-GN symmetry/concentration mechanisms.

To promote exact incompatibility to a uniform gap one needs a near-extremizer compactness/stability argument showing that any sequence approaching the formal constant, after fixing translation/dilation/amplitude, converges strongly enough to the incompatible fixed-shape optimizer.

The sharp-GN variational literature provides the appropriate optimizer/compactness framework, but the matrix-strain compatibility step must be incorporated explicitly.

---

## 7. DSD significance

This is a strong simultaneous-channel collision:

1. scalar magnitude channel demands a GN ground state;
2. strain eigenvalue channel demands `(-2,1,1)`;
3. strain-orientation-gradient channel demands fixed matrix direction;
4. incompressible Fourier admissibility forbids that fixed nonzero determinant strain shape.

Thus four individually admissible/near-optimal descriptions cannot be realized simultaneously by one incompressible velocity field.

This is precisely the type of **residual-class elimination by channel incompatibility** sought in the DSD-assisted proof route.

Status: **EXACT EXTREMIZER COLLISION DERIVED / QUANTITATIVE NEAR-EXTREMIZER GAP NEXT**.
