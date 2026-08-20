# Explicit Ball Coherence Constant — 2026-08-20

Overall status: **EXPLICIT REDUCTION OF THE CLASS COHERENCE CONSTANT — GLOBAL REGULARITY NOT PROVED.**

This note turns the abstract coherence constant from `PV_COHERENCE_COMPATIBILITY_GAP_2026-08-20.md` into an explicit bound on a normalized active ball.

---

## 1. Assumptions on the active ball

Let

\[
B_R\subset\mathbb R^3
\]

be a convex normalized active core ball.

Let

\[
w(x)=|\nabla S(x)|^2,
\qquad
P_B=\int_{B_R}w(x)dx.
\]

Assume the positive-middle compressive spectral gap satisfies

\[
\boxed{
s_2-s_1\ge g_->0
}
\]

throughout the active ball, and assume

\[
\boxed{
w(x)\le P_\infty<\infty.}
\]

Let `n(x)` denote the unit compressive eigenaxis.

---

## 2. Eigenaxis bending from covariance defect

The eigenvector derivative formula and the previous range-defect identity give

\[
|\nabla n|^2
\le
\frac9{2g_-^2}
\varepsilon(x)w(x),
\]

where

\[
\varepsilon(x)
=
\frac79-n(x)^T\overline C(x)n(x).
\]

Define

\[
\overline\varepsilon
=
\frac1{P_B}
\int_{B_R}\varepsilon(x)w(x)dx.
\]

Then

\[
\boxed{
\int_{B_R}|\nabla n|^2dx
\le
\frac9{2g_-^2}
\overline\varepsilon P_B.
}
\]

---

## 3. Ball Poincare estimate

Let

\[
\bar n
=\fint_{B_R}n(x)dx.
\]

For a convex set of diameter `2R`, the Payne--Weinberger Poincare estimate gives

\[
\boxed{
\int_{B_R}|n-\bar n|^2dx
\le
\frac{4R^2}{\pi^2}
\int_{B_R}|\nabla n|^2dx.
}
\]

Choose a constant unit vector `n0` in the direction of `bar n` when `bar n != 0`. If `bar n=0`, choose any unit vector.

Because `|n(x)|=1`,

\[
\fint|n-n_0|^2
=2(1-|\bar n|),
\]

while

\[
\fint|n-\bar n|^2
=1-|\bar n|^2.
\]

Hence

\[
\boxed{
\int|n-n_0|^2
\le
2\int|n-\bar n|^2.
}
\]

Therefore

\[
\boxed{
\int_{B_R}|n-n_0|^2dx
\le
\frac{8R^2}{\pi^2}
\int_{B_R}|\nabla n|^2dx.
}
\]

---

## 4. Convert to derivative-weighted axis dispersion

Define

\[
D_*^2
=\inf_{|n_0|=1}
\frac1{P_B}
\int_{B_R}w(x)|n(x)-n_0|^2dx.
\]

Using `w <= P_infinity`,

\[
D_*^2
\le
\frac{P_\infty}{P_B}
\frac{8R^2}{\pi^2}
\int|\nabla n|^2dx.
\]

Insert the eigenaxis-bending bound:

\[
D_*^2
\le
\frac{P_\infty}{P_B}
\frac{8R^2}{\pi^2}
\frac9{2g_-^2}
\overline\varepsilon P_B.
\]

Thus

\[
\boxed{
D_*^2
\le
C_{coh}^{ball}\overline\varepsilon,
}
\]

with

\[
\boxed{
C_{coh}^{ball}
=
\frac{36}{\pi^2}
\frac{R^2P_\infty}{g_-^2}.
}
\]

Numerically,

\[
\frac{36}{\pi^2}
\approx3.647562611.
\]

---

## 5. Explicit covariance defect

From the compatibility/coherence loop,

\[
\overline\varepsilon
\ge
\left(
\sqrt{C_{coh}^{ball}+\frac19}
-\sqrt{C_{coh}^{ball}}
\right)^2.
\]

Hence

\[
\boxed{
\overline\varepsilon
\ge
\left[
\sqrt{
\frac19
+
\frac{36}{\pi^2}
\frac{R^2P_\infty}{g_-^2}
}
-
\sqrt{
\frac{36}{\pi^2}
\frac{R^2P_\infty}{g_-^2}
}
\right]^2.
}
\]

This removes the abstract coherence constant from the formula.

---

## 6. Dimensionless shape parameter

Define

\[
\chi
=\frac{R^2P_\infty}{g_-^2}.
\]

Then

\[
C_{coh}^{ball}
=\frac{36}{\pi^2}\chi
\]

and

\[
\boxed{
\delta_{cov}^{ball}(\chi)
=
\left(
\sqrt{\frac19+\frac{36}{\pi^2}\chi}
-
\sqrt{\frac{36}{\pi^2}\chi}
\right)^2.
}
\]

Examples:

- `chi = 0.01` gives `delta_cov >= 0.0373202`;
- `chi = 0.1` gives `delta_cov >= 0.00737552`;
- `chi = 1` gives `delta_cov >= 0.000833512`;
- `chi = 10` gives `delta_cov >= 0.0000844873`.

The bound remains strictly positive for every finite `chi`.

---

## 7. H1 compatibility tax on the ball

If `s2-s1 >= g_-`, the exact covariance-density decomposition yields the additive loss

\[
\boxed{
N_B
\le
N_{ceiling,B}
-3g_-\delta_{cov}^{ball}(\chi)P_B
}
\]

before any strongest-extensional leakage tax is counted.

In Leray variables, the effective recurrent `P` tax is therefore

\[
\boxed{
\frac34
\quad\longrightarrow\quad
\frac34
+3g_-\delta_{cov}^{ball}(\chi).
}
\]

---

## 8. Remaining numerical inputs

The only inputs still needed to turn this into a number on the recurrent first-hitting class are

\[
R,
\qquad
P_\infty=\|\nabla S\|_{L^\infty(B_R)}^2,
\qquad
g_-.
\]

The first-hitting analyticity/compactness route already supplies finite class bounds for the first two quantities on every fixed parent ball. The remaining task is to extract explicit normalized values, or else route loss of the positive spectral gap back to the middle-zero/non-normality branch quantified in `PV_DOUBLE_SATURATION_SPECTRAL_TRADEOFF_2026-08-20.md`.

Status: **ON A POSITIVE-GAP ACTIVE BALL, THE ABSTRACT AXIS-COHERENCE CONSTANT IS BOUNDED EXPLICITLY BY `(36/pi^2) R^2 P_infinity / g_-^2`. THE COMPATIBILITY COVARIANCE GAP IS THEREFORE AN EXPLICIT FUNCTION OF THREE NORMALIZED CORE QUANTITIES.**