# Strain-gradient projective covariance and advection-H depletion

Date: 2026-08-19

Status: **DERIVED EXACT LOCAL MATRIX REPRESENTATION + ANISOTROPY DEPLETION BOUND / GLOBAL REGULARITY NOT PROVED**.

This note compresses the remaining advection-driven `H` channel into a positive semidefinite gradient-direction covariance matrix.

---

## 1. Gradient covariance matrix

For each strain component `S_ab`, let

\[
g^{ab}=\nabla S_{ab}.
\]

Define the positive semidefinite matrix

\[
\boxed{
G_S
=\sum_{a,b}g^{ab}\otimes g^{ab}.
}
\]

Then

\[
\operatorname{tr}G_S
=|\nabla S|^2.
\]

The exact advection identity from the previous note becomes

\[
\boxed{
\langle(u\cdot\nabla)S,-\Delta S\rangle
=
\int\operatorname{tr}(S G_S)\,dx.
}
\]

Thus the Eulerian advection contribution to the strain `H1` ledger is a contraction between the strain matrix and the covariance of the directions in which strain itself varies.

---

## 2. Normalized projective gradient state

Where `|nabla S|>0`, define

\[
\boxed{
C_{\nabla S}
=\frac{G_S}{|\nabla S|^2}.
}
\]

Then `C_{nabla S}` is positive semidefinite with

\[
\operatorname{tr}C_{\nabla S}=1.
\]

Define the projective dispersion

\[
\boxed{
J_{\nabla S}
=1-\operatorname{tr}(C_{\nabla S}^2).
}
\]

For a three-dimensional trace-one positive matrix,

\[
0\le J_{\nabla S}\le\frac23.
\]

- rank-one gradient direction: `J_{nabla S}=0`;
- isotropic gradient covariance `C_{nabla S}=I/3`: `J_{nabla S}=2/3`.

This convention matches the earlier projective-covariance idea, but here maximal dispersion corresponds to isotropy of strain-gradient directions.

---

## 3. Exact isotropic cancellation

Because the strain is trace free,

\[
\operatorname{tr}S=0.
\]

Hence

\[
\operatorname{tr}\left(S\frac13I\right)=0.
\]

Therefore

\[
\operatorname{tr}(S G_S)
=|\nabla S|^2
\operatorname{tr}\left[S\left(C_{\nabla S}-\frac13I\right)\right].
\]

By Frobenius Cauchy--Schwarz,

\[
\boxed{
|\operatorname{tr}(S G_S)|
\le
|S|\,|\nabla S|^2
\left|C_{\nabla S}-\frac13I\right|_F.
}
\]

But

\[
\left|C_{\nabla S}-\frac13I\right|_F^2
=
\operatorname{tr}(C_{\nabla S}^2)-\frac13
=
\frac23-J_{\nabla S}.
\]

Thus

\[
\boxed{
|\operatorname{tr}(S G_S)|
\le
|S|\,|\nabla S|^2
\sqrt{\frac23-J_{\nabla S}}.
}
\]

This is an exact anisotropy-depletion factor.

If the strain-gradient directions become isotropic,

\[
J_{\nabla S}\to\frac23,
\]

the advection contribution to `H1` production is depleted.

Hence advection-saturated `H` requires persistent gradient-direction anisotropy.

---

## 4. Strain-eigenframe loading

Let `e_i` be the strain eigenvectors and define

\[
\boxed{
b_i=e_i^TC_{\nabla S}e_i,\qquad b_i\ge0,\quad\sum_i b_i=1.}
\]

Then exactly

\[
\boxed{
\operatorname{tr}(S G_S)
=|\nabla S|^2
\sum_{i=1}^3\lambda_i b_i.
}
\]

Since the strain `H1` energy equation contains the negative of this advection contraction, advection-driven derivative growth requires bias toward the compressive eigenframe.

On the near-planar middle-strain saturation geometry

\[
\lambda_1\simeq-\lambda_3,
\qquad
\lambda_2\simeq0,
\]

we obtain schematically

\[
-\operatorname{tr}(S G_S)
\simeq
\lambda_3|\nabla S|^2(b_1-b_3).
\]

Thus the dangerous branch requires

\[
\boxed{
b_1>b_3}
\]

with a quantitatively non-small compressive-direction bias.

---

## 5. New typed H channel

The remaining advection derivative channel is therefore not adequately represented by the scalar palinstrophy alone.

A minimally complete local state is

\[
\boxed{
\left(
|\nabla S|^2,
C_{\nabla S},
J_{\nabla S},
(b_1,b_2,b_3)
\right).
}
\]

This separates:

1. derivative magnitude;
2. projective directional dispersion;
3. loading relative to the strain eigenframe.

The dangerous advection-H mechanism requires simultaneously

\[
\boxed{
\text{large derivative magnitude}
+\text{non-isotropic gradient covariance}
+\text{compressive eigenframe bias}.
}
\]

---

## 6. Relation to Fourier triad gate

The physical-space covariance condition and the previous Fourier angular factor are complementary.

- Fourier collinearity suppresses the coefficient `u_hat(p) dot q`;
- physical-space isotropy suppresses `tr(S G_S)` by trace-freeness;
- dangerous advection-H therefore needs structured, nontrivial directional organization in both representations rather than arbitrary high-frequency noise.

No uncertainty-principle theorem coupling these two projective defects is yet proved.

Such a coupling would be a plausible next nonrepeatability target.

Status: **ADVECTION H COMPRESSED TO A PROJECTIVE STRAIN-GRADIENT COVARIANCE; ISOTROPIC GRADIENT STATES ARE EXACTLY DEPLETED; DANGEROUS BRANCH REQUIRES COMPRESSIVE ANISOTROPIC GRADIENT LOADING**.
