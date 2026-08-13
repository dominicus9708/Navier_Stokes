# Uniform Fourier spectral-angle gap between incompressible strain modes and the Betchov source-optimal shape

Date: 2026-08-13

Status: **EXACT FOURIER SUBSPACE DISTANCE = 1/2 / QUANTITATIVE NEAR-EXTREMIZER TOOL**.

The Betchov determinant extremizer has normalized strain shape

\[
A_*
=\frac1{\sqrt6}
\operatorname{diag}(-2,1,1),
\qquad
|A_*|_F=1.
\]

Every individual Fourier mode of an incompressible strain belongs to a very different matrix subspace.  The angle between `A_*` and that subspace has a uniform positive lower bound.  The exact distance is `1/2`.

---

## 1. Compatible Fourier strain subspace

For `xi!=0`, let

\[
e=\xi/|\xi|.
\]

Because

\[
\xi\cdot\widehat u(\xi)=0,
\]

write the velocity direction as

\[
v\in e^\perp.
\]

Ignoring the harmless factor `i|xi|`, the Fourier strain matrix has the form

\[
\frac12(e\otimes v+v\otimes e).
\]

Choose an orthonormal basis `v1,v2` of `e^perp`.  A Frobenius-orthonormal basis of the compatible matrix subspace is

\[
\boxed{
E_a(e)
=\frac1{\sqrt2}
(e\otimes v_a+v_a\otimes e),
\qquad a=1,2.
}
\]

Define

\[
\boxed{
\mathcal R_e
=\operatorname{span}\{E_1(e),E_2(e)\}.
}
\]

Every unit matrix in `R_e` has the pure-shear eigenvalue shape

\[
\boxed{
(-1/\sqrt2,0,1/\sqrt2).
}
\]

---

## 2. Projection of a fixed symmetric matrix

For any symmetric Frobenius-unit matrix `A`,

\[
\langle A,E_a(e)\rangle_F
=\sqrt2\,e^TAv_a.
\]

Therefore

\[
\begin{aligned}
\|P_{\mathcal R_e}A\|_F^2
&=2\sum_{a=1}^2(e^TAv_a)^2\\
&=2\left(
|Ae|^2-(e^TAe)^2
\right).
\end{aligned}
\]

The bracket is the variance of the eigenvalues of `A` under the directional weights `b_i=(e.e_i)^2`.

---

## 3. Evaluate for the source-optimal shape

For `A_*`, the eigenvalues are

\[
\lambda_1=-2/\sqrt6,
\qquad
\lambda_2=\lambda_3=1/\sqrt6.
\]

Let

\[
b=(e\cdot e_1)^2.
\]

Because the positive eigenvalue is doubly degenerate,

\[
|A_*e|^2-(e^TA_*e)^2
=b(1-b)(\lambda_2-\lambda_1)^2.
\]

Now

\[
(\lambda_2-\lambda_1)^2
=\left(\frac3{\sqrt6}\right)^2
=\frac32.
\]

Hence

\[
\|P_{\mathcal R_e}A_*\|_F^2
=3b(1-b).
\]

The maximum occurs at

\[
b=1/2,
\]

giving

\[
\boxed{
\sup_e
\|P_{\mathcal R_e}A_*\|_F^2
=\frac34.
}
\]

Since `|A_*|=1`,

\[
\boxed{
\inf_e
\operatorname{dist}(A_*,\mathcal R_e)^2
=1-\frac34
=\frac14.
}
\]

Therefore

\[
\boxed{
\operatorname{dist}(A_*,\mathcal R_e)
\ge\frac12
\quad\text{for every unit }e.
}
\]

Rotating `A_*` does not change the result.

---

## 4. Field-level `L2` consequence

Fix any rotation `R` and let

\[
A_R=RA_*R^T.
\]

Let `f in L2(R3)` be scalar.  For any divergence-free velocity with strain `S`, Fourier compatibility gives

\[
\widehat S(\xi)\in\mathcal R_{\xi/|\xi|}
\]

for almost every nonzero `xi`.

At each frequency,

\[
|\widehat S(\xi)-\widehat f(\xi)A_R|
\ge
\frac12|\widehat f(\xi)|.
\]

Integrating by Plancherel,

\[
\boxed{
\|S-fA_R\|_2
\ge
\frac12\|f\|_2.
}
\]

Thus the formal fixed-shape Betchov extremizer manifold lies a uniform positive distance away from the closed linear space of incompressible strain fields.

---

## 5. Why this is stronger than nonattainment

The previous equality-incompatibility lemma only showed

\[
fA_R\notin\mathcal S_{\rm inc}
\]

for nonzero `f`, where `S_inc` is the incompressible strain space.

The present result gives the quantitative statement

\[
\boxed{
\frac{
\operatorname{dist}(fA_R,\mathcal S_{\rm inc})
}{\|fA_R\|_2}
\ge\frac12.
}
\]

Therefore a near-extremizer contradiction does not need infinitesimal precision.  It is enough to show that simultaneous near-equality in

1. determinant shape;
2. sharp GN magnitude;
3. Kato matrix-direction freezing

forces the strain within relative `L2` distance strictly below `1/2` from one fixed rotated source-optimal shape.

---

## 6. Remaining orientation-modulation issue

Determinant near-equality alone allows the local source-optimal eigenframe to rotate with `x`.  The Kato defect

\[
\|\nabla S\|_2^2
-\|\nabla|S|\|_2^2
=\int|S|^2|\nabla\widehat S|^2
\]

penalizes such rotation.

To use the `1/2` spectral gap, one still needs a quantitative weighted-Poincare/modulation lemma showing that small matrix-direction gradient on a sharp-GN near-extremizer magnitude forces

\[
\widehat S(x)
\]

to stay close, on the `L2`-dominant region, to one fixed rotation of `A_*`.

The scalar near-extremizer compactness supplies the needed connected one-bubble weight; the present spectral result supplies the final fixed positive incompatibility distance.

Status: **EXACT 1/2 SPECTRAL GAP CLOSED / WEIGHTED ORIENTATION MODULATION NEXT**.
