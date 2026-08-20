# Global Strain-Compatibility Covariance Cap — 2026-08-20

Overall status: **NEW GLOBAL COMPATIBILITY RIGIDITY FOR THE FINAL P_V BRANCH — GLOBAL REGULARITY NOT PROVED.**

This note strengthens the pointwise trace-free covariance cap by using the full Fourier compatibility of an incompressible strain field.

The previous pointwise argument gave

\[
\lambda_{\max}(\overline C(x))\le \frac79.
\]

That bound treats the derivative matrices `partial_k S` mainly as symmetric trace-free matrices. After integrating the covariance over space, the fact that `S=sym grad u` with `div u=0` gives a stronger exact bound.

---

## 1. Integrated covariances

Let

\[
P=\int_{\mathbb R^3}|\nabla S|^2dx.
\]

Define

\[
(\mathbb M_{sp})_{ij}
=\int\langle\partial_iS,\partial_jS\rangle_Fdx,
\]

and

\[
\mathbb M_{rg}
=\int\sum_k(\partial_kS)^2dx.
\]

Then

\[
\operatorname{tr}\mathbb M_{sp}
=\operatorname{tr}\mathbb M_{rg}
=P.
\]

Define the integrated combined covariance

\[
\boxed{
\mathbb C
=\frac{\mathbb M_{sp}+2\mathbb M_{rg}}{3P}.
}
\]

Equivalently, if `Cbar(x)` is the previous pointwise covariance,

\[
\boxed{
\mathbb C
=\frac1P\int |\nabla S|^2\overline C(x)dx.
}
\]

Thus `mathbb C` is the derivative-energy-weighted spatial average of the local covariance.

---

## 2. Fourier form of an incompressible strain mode

For `k != 0`, incompressibility gives

\[
k\cdot\widehat u(k)=0.
\]

The strain Fourier coefficient is

\[
\widehat S(k)
=\frac{i}{2}
\left(k\otimes\widehat u
+\widehat u\otimes k\right).
\]

Write

\[
\widehat k=k/|k|,
\qquad
\widehat a=\widehat u/|\widehat u|,
\qquad
\widehat a\perp\widehat k.
\]

Up to an irrelevant scalar amplitude, every nonzero Fourier strain mode lies in

\[
\mathcal V_k
=
\{\operatorname{sym}(\widehat k\otimes a):a\perp\widehat k\}.
\]

---

## 3. Exact modewise covariance estimate

Fix a unit vector `n`. Set

\[
c=\widehat k\cdot n,
\qquad
d=\widehat a\cdot n.
\]

Because `khat` and `ahat` are orthonormal,

\[
c^2+d^2\le1.
\]

For one mode `A=Shat(k)`,

\[
\frac{|An|^2}{|A|^2}
=\frac12(c^2+d^2).
\]

The mode contribution to the numerator of `n^T mathbb C n` is therefore

\[
|k|^2|A|^2
\left[
c^2+2\frac{|An|^2}{|A|^2}
\right]
\le
|k|^2|A|^2(c^2+1)
\le
2|k|^2|A|^2.
\]

After division by the factor `3P`, Parseval gives

\[
\boxed{
n^T\mathbb Cn\le\frac23.
}
\]

Since this holds for every unit `n`,

\[
\boxed{
\lambda_{\max}(\mathbb C)\le\frac23.
}
\]

This is stronger than the pointwise trace-free ceiling `7/9` after derivative-energy averaging.

---

## 4. Equality is impossible for a nonzero whole-space L2 strain

Modewise equality requires

\[
|\widehat k\cdot n|=1,
\]

so every active Fourier mode must lie on the line parallel to `n`.

A nonzero `L2(R^3)` Fourier transform cannot be supported on a one-dimensional measure-zero line. Hence

\[
\boxed{
S\in L^2(\mathbb R^3),\quad S\ne0
\Longrightarrow
\lambda_{\max}(\mathbb C)<\frac23
}
\]

for every fixed profile, although narrow Fourier cones can approach the supremum.

On a precompact class that excludes angular-frequency escape, this yields a class-dependent strict gap below `2/3`.

---

## 5. Exact fixed-axis covariance tax

For every fixed unit axis `n`, define the derivative-weighted mean of the old `7/9` pointwise defect by

\[
\overline\varepsilon_n
=
\frac1P\int
|\nabla S|^2
\left(
\frac79-n^T\overline C(x)n
\right)dx.
\]

Because the weighted average of `Cbar` is `mathbb C`,

\[
\overline\varepsilon_n
=\frac79-n^T\mathbb Cn.
\]

Therefore

\[
\boxed{
\overline\varepsilon_n\ge\frac19.
}
\]

So a globally coherent fixed axis can never approach the local `7/9` covariance saturation closer than a derivative-weighted defect of `1/9`.

This is an exact compatibility tax, not a compactness heuristic.

---

## 6. Fourier distance of the max-mid line from the compatible strain space

Let

\[
Q_n=\frac{I-3n\otimes n}{\sqrt6}.
\]

This is the normalized fixed-axis max-mid tensor line appearing in the previous H1 saturation geometry.

For a normalized compatible mode

\[
A=\frac{\widehat k\otimes a+a\otimes\widehat k}{\sqrt2},
\qquad a\perp\widehat k,
\]

one finds

\[
Q_n:A
=-\sqrt3
(n\cdot\widehat k)(n\cdot a).
\]

If `theta` is the angle between `khat` and `n`, maximizing over `a` gives

\[
\boxed{
\|P_{\mathcal V_k}Q_n\|
=\sqrt3|\sin\theta\cos\theta|
\le\frac{\sqrt3}{2}.
}
\]

Hence

\[
\boxed{
\operatorname{dist}(Q_n,\mathcal V_k)
\ge\frac12
}
\]

for every nonzero frequency direction.

The incompatibility is even stronger in the one-dimensional limit required by static H1 saturation: if `k parallel n`,

\[
P_{\mathcal V_k}Q_n=0.
\]

Thus the two exact static-saturation requirements

- derivative direction parallel to `n`;
- derivative matrix parallel to `Q_n`;

are Fourier-orthogonal to the incompressible strain space.

---

## 7. Global L2 projection consequence

Let `P_st` denote the orthogonal Fourier projection onto the incompressible strain subspace. For any scalar `m in L2`,

\[
\boxed{
\|(I-P_{st})(mQ_n)\|_2
\ge\frac12\|mQ_n\|_2.
}
\]

Therefore, for any compatible strain field `F`,

\[
\boxed{
\|F-mQ_n\|_2
\ge\frac12\|mQ_n\|_2.
}
\]

In particular, a compatible derivative field cannot be arbitrarily close in `L2` to a fixed-axis max-mid derivative line.

This directly strengthens the earlier exact-saturation nonattainment argument.

---

## 8. Variable-axis dichotomy

Let `n(x)` be the local compressive eigenaxis and let `n0` be any fixed unit vector. Since `Cbar` is positive semidefinite with trace one,

\[
|n^T\overline Cn-n_0^T\overline Cn_0|
\le2|n-n_0|.
\]

Hence

\[
\boxed{
\frac1P\int P(x)n(x)^T\overline C(x)n(x)dx
\le
\frac23
+2D_n,
}
\]

where

\[
D_n
=
\left(
\frac1P\int P(x)|n(x)-n_0|^2dx
\right)^{1/2}.
\]

Consequently, if the moving eigenaxis achieves weighted covariance alignment `2/3+delta`, then every fixed axis satisfies

\[
\boxed{
D_n\ge\frac\delta2.
}
\]

Thus the survivor pays one of two costs:

1. **fixed/coherent axis:** the exact `1/9` covariance tax applies;
2. **alignment above 2/3:** a definite weighted eigenaxis-dispersion cost is mandatory.

The previous near-saturation rigidity already bounds eigenaxis bending by derivative-range defects when the compressive spectral gap is positive. Combining the two converts the old qualitative statement `near saturation -> one-dimensional fixed axis` into a quantitative compatibility loop.

---

## 9. Consequence for the recurrent P_V endgame

The dangerous recurrent branch can no longer use the pointwise `7/9` ceiling as though a coherent max-mid derivative packet could approach it indefinitely.

A non-H/T compact recurrence must instead choose between:

- a coherent axis, in which case the derivative-weighted covariance average is capped by `2/3` and pays at least `1/9` relative to the old pointwise ceiling;
- a varying axis, in which case the required covariance excess above `2/3` forces a quantitative eigenaxis-dispersion/bending burden that can be routed toward the existing `H/T` geometry.

Status: **THE POINTWISE `7/9` COVARIANCE CAP IS NOT THE TRUE COHERENT WHOLE-PROFILE CEILING. FULL INCOMPRESSIBLE STRAIN COMPATIBILITY LOWERS THE INTEGRATED FIXED-AXIS CAP TO `2/3`. THE STATIC MAX-MID ONE-DIMENSIONAL SATURATION LINE IS FOURIER-ORTHOGONAL TO THE COMPATIBLE STRAIN SPACE IN ITS EXACT LIMIT.**