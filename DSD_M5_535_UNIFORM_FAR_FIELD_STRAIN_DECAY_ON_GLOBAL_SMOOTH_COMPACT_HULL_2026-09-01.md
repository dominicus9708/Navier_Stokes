# DSD M5-535 — Global smooth compactness and vorticity tightness force uniform far-field strain decay

Date: 2026-09-01

Status: **FAR-FIELD RIESZ DECAY / M5-533 GIVES UNIFORM VANISHING OF `W` AND ALL FIXED VORTICITY DERIVATIVES AT LARGE SIMILARITY RADIUS, WHILE M5-508 GIVES UNIFORM `L2` TAIL TIGHTNESS / USING THE PRINCIPAL-VALUE CANCELLATION OF THE STRAIN RIESZ KERNEL NEAR EACH REMOTE POINT AND AN `L2` CORE/TAIL SPLIT FOR THE NONLOCAL PART, THE FULL STRAIN — NOT ONLY THE CONTRIBUTION OF REMOTE VORTICITY TO A FIXED CORE — VANISHES UNIFORMLY AS `|y| -> infinity` / THIS PROVIDES THE SMALL FAR-FIELD COEFFICIENT NEEDED FOR SUBCRITICAL RADIAL-MOMENT DAMPING / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Strain as a singular integral of vorticity

For divergence-free velocity,

\[
\Sigma
=
\mathcal R[W],
\]

where `mathcal R` denotes a matrix-valued Calderon--Zygmund/Riesz operator with kernel

\[
K_1(z)
\sim |z|^{-3}
\]

and the standard mean-zero principal-value cancellation.

The goal is to prove

\[
\boxed{
\sup_{Y\in\widehat{\mathfrak H}}
\sup_{|x|>R}
|\Sigma_Y(x)|
\to0.
}
\]

---

## 2. Near-field principal-value part

Fix a remote point `x` and split

\[
\Sigma(x)
=
\operatorname{p.v.}
\int_{|z-x|<1}K_1(x-z)W(z)dz
+
\int_{|z-x|\ge1}K_1(x-z)W(z)dz.
\]

By the cancellation of `K_1`, the near part may be written schematically as

\[
\int_{|\eta|<1}
K_1(\eta)
\left[W(x-\eta)-W(x)\right]d\eta.
\]

Since

\[
|W(x-\eta)-W(x)|
\le
|\eta|
\sup_{B_1(x)}|\nabla W|,
\]

we get

\[
\begin{aligned}
|\Sigma_{near}(x)|
&\le
C
\sup_{B_1(x)}|\nabla W|
\int_{|\eta|<1}|\eta|^{-2}d\eta\\
&\le
C
\sup_{B_1(x)}|\nabla W|.
\end{aligned}
\]

M5-533 gives

\[
\boxed{
\sup_Y
\sup_{|x|>R}
\sup_{B_1(x)}|\nabla W_Y|
\to0.
}
\]

Therefore the principal-value near part vanishes uniformly at infinity.

---

## 3. Far integral: central core contribution

Take `|x|=X` large and split the far integral further into

\[
|z|<X/2
\]

and

\[
|z|\ge X/2.
\]

On the central region,

\[
|x-z|\ge X/2.
\]

Hence

\[
\begin{aligned}
|\Sigma_{core}(x)|
&\le
CX^{-3}
\int_{|z|<X/2}|W(z)|dz\\
&\le
CX^{-3}
|B_{X/2}|^{1/2}
\|W\|_2\\
&\le
C Z_*^{1/2}X^{-3/2}.
\end{aligned}
\]

Thus

\[
\boxed{
\sup_Y|\Sigma_{core}(x)|
\lesssim X^{-3/2}
\to0.
}
\]

---

## 4. Far integral: remote `L2` contribution

On

\[
|z|\ge X/2,
\qquad
|x-z|\ge1,
\]

Cauchy--Schwarz gives

\[
\begin{aligned}
|\Sigma_{tail}(x)|
&\le
C
\left(
\int_{|z|\ge X/2}|W(z)|^2dz
\right)^{1/2}
\left(
\int_{|x-z|\ge1}|x-z|^{-6}dz
\right)^{1/2}\\
&\le
C
E_{tail}(X/2)^{1/2}.
\end{aligned}
\]

The second kernel integral is finite and independent of `x`.

M5-508 gives uniform tail tightness:

\[
\sup_Y E_{tail}^Y(X/2)	o0.
\]

Therefore

\[
\boxed{
\sup_Y|\Sigma_{tail}(x)|
\to0.
}
\]

---

## 5. Main conclusion

Combining the near, central-core, and remote-tail parts,

\[
\boxed{
\lim_{R\to\infty}
\sup_{Y\in\widehat{\mathfrak H}}
\sup_{|x|>R}
|\Sigma_Y(x)|
=0.
}
\]

Thus the full strain field vanishes uniformly at remote similarity radius.

This is stronger than M5-534, which estimated only the influence of the remote tail on one fixed bounded core.

---

## 6. Velocity-to-radius coefficient

M5-523 already gives

\[
\sup_Y\sup_{|x|>R}|U_Y(x)|\to0.
\]

Therefore automatically

\[
\boxed{
\sup_Y\sup_{|x|>R}
\frac{|U_Y(x)|}{|x|}
\to0.
}
\]

The two far-field coefficients appearing in a homogeneous radial-moment equation are therefore both small:

\[
|\Sigma(x)|\ll1,
\qquad
\frac{|U(x)|}{|x|}\ll1.
\]

---

## 7. Higher derivatives

The same near-cancellation plus core/tail splitting can be iterated using the M5-533 bounds on higher derivatives of `W`.

For every fixed `j`,

\[
\boxed{
\sup_Y\sup_{|x|>R}
|\nabla^j\Sigma_Y(x)|
\to0
}
\]

provided the corresponding singular-integral cancellation is written at order `j`.

Only the zeroth strain decay is needed in the next moment calculation.

---

## 8. DSD consequence

The infinite first-moment tail is simultaneously

1. low amplitude;
2. low local derivative;
3. low local strain;
4. weakly coupled back to the bounded core.

Thus its survival is not based on hidden order-one nonlinear activity at arbitrarily remote radii.

It is a genuinely diffuse critical spatial distribution.

---

## 9. Highest-value next target

For

\[
0<\alpha<1,
\]

consider the regularized radial weight

\[
w_\alpha(y)
=(1+|y|^2)^{\alpha/2}.
\]

The similarity linear terms satisfy

\[
\frac12 y\cdot\nabla w_\alpha
-\frac12w_\alpha
\le
-\frac{1-\alpha}{2}w_\alpha.
\]

At large radius, M5-535 makes the weighted stretching and advection coefficients arbitrarily smaller than this damping.

Therefore invariant averaging of truncated `w_alpha` moments should give a finite bound for every `alpha<1`, whereas M5-531 says the `alpha=1` moment is infinite almost everywhere.

This would identify `alpha=1` as the exact radial critical exponent of the surviving defect.

---

## 10. Status

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
