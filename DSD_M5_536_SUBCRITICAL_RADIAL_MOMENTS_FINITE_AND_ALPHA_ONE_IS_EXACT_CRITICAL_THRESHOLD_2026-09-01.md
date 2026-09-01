# DSD M5-536 — All subcritical radial enstrophy moments are finite; alpha=1 is the exact invariant critical threshold

Date: 2026-09-01

Status: **EXACT RADIAL CRITICALITY / FOR EVERY `0<alpha<1`, THE REGULARIZED WEIGHT `w_alpha=(1+|y|^2)^(alpha/2)` RETAINS A STRICT SIMILARITY DAMPING COEFFICIENT `(1-alpha)/2` / M5-523 AND M5-535 MAKE THE FAR-FIELD ADVECTION AND STRAIN COEFFICIENTS ARBITRARILY SMALL COMPARED WITH THIS DAMPING, WHILE THE BOUNDED CORE CONTRIBUTIONS REMAIN FINITE / USING CONCAVE TRUNCATIONS OF `w_alpha` AND INVARIANT AVERAGING GIVES A TRUNCATION-UNIFORM BOUND ON THE MEAN `alpha`-MOMENT / MONOTONE CONVERGENCE THEN IMPLIES FINITE `alpha`-MOMENT FOR INVARIANT-ALMOST EVERY STATE, FOR EVERY `alpha<1` / M5-531 SIMULTANEOUSLY GIVES INFINITE FIRST MOMENT, SO THE SURVIVING WEIGHTED DEFECT SITS EXACTLY AT THE RADIAL EXPONENT `alpha=1` / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Weighted moment

Fix

\[
0<\alpha<1.
\]

Define

\[
\boxed{
w_\alpha(y)
:=(1+|y|^2)^{\alpha/2}.
}
\]

The desired moment is

\[
\mathcal M_\alpha(Y)
:=
\int w_\alpha(y)|W_Y(y)|^2dy.
\]

It is not assumed finite a priori.

---

## 2. Similarity linear coefficient

Let

\[
h=|W|^2.
\]

From the local similarity enstrophy balance,

\[
\partial_\theta h
+\frac12h
+\nabla\cdot\left[\left(U+\frac y2\right)h-\nabla h\right]
=2q-2p,
\]

where

\[
q=W\cdot\Sigma W,
\qquad
p=|\nabla W|^2.
\]

For a smooth weight `w`, integration gives

\[
\boxed{
\begin{aligned}
\frac d{d\theta}\int wh
={}&
-\frac12\int wh
+\frac12\int (y\cdot\nabla w)h\\
&+
2\int wq
-2\int wp
+
\int(\nabla w\cdot U)h
+
\int(\Delta w)h.
\end{aligned}
}
\]

For `w_alpha`,

\[
y\cdot\nabla w_\alpha
=
\alpha
\frac{|y|^2}{1+|y|^2}
w_\alpha
\le
\alpha w_\alpha.
\]

Therefore the linear similarity terms obey

\[
\boxed{
-\frac12\int w_\alpha h
+\frac12\int(y\cdot\nabla w_\alpha)h
\le
-\frac{1-\alpha}{2}
\mathcal M_\alpha.
}
\]

The coefficient is strictly negative precisely when `alpha<1`.

---

## 3. Truncation for possibly infinite moments

Choose smooth increasing concave functions `psi_N` such that

\[
\psi_N(s)=s
\quad\text{for }s\le N,
\]

\[
\psi_N(s)=2N
\quad\text{for }s\ge3N,
\]

and

\[
0\le\psi_N'\le1,
\qquad
\psi_N''\le0.
\]

Set

\[
\boxed{
w_{\alpha,N}:=\psi_N(w_\alpha).
}
\]

Concavity with `psi_N(0)=0` after a harmless extension implies

\[
s\psi_N'(s)\le\psi_N(s).
\]

Hence

\[
\boxed{
y\cdot\nabla w_{\alpha,N}
\le
\alpha w_{\alpha,N}.
}
\]

Also

\[
|\nabla w_{\alpha,N}|
\le
C_\alpha
\frac{w_{\alpha,N}}{1+|y|},
\]

and because `psi_N''<=0`,

\[
\Delta w_{\alpha,N}
\le
\psi_N'(w_\alpha)\Delta w_\alpha
\le C_\alpha,
\]

uniformly in `N`.

Define

\[
M_{\alpha,N}
:=
\int w_{\alpha,N}h.
\]

This is finite and bounded as an observable for each fixed `N`.

---

## 4. Choose the far field where nonlinear coefficients are small

Let

\[
c_\alpha:=\frac{1-\alpha}{2}>0.
\]

By M5-535, choose `R_alpha` so large that

\[
\boxed{
\sup_Y\sup_{|y|>R_\alpha}|\Sigma_Y(y)|
\le\frac{c_\alpha}{16}.
}
\]

By M5-523, enlarge `R_alpha` if needed so that

\[
\boxed{
\sup_Y\sup_{|y|>R_\alpha}
\frac{|U_Y(y)|}{1+|y|}
\le\frac{c_\alpha}{16C_\alpha}.
}
\]

These bounds are uniform on the invariant hard component.

---

## 5. Far-field stretching is absorbable

On `|y|>R_alpha`,

\[
|q|
\le
|\Sigma|h.
\]

Therefore

\[
2\int_{|y|>R_\alpha}
w_{\alpha,N}|q|
\le
\frac{c_\alpha}{8}
M_{\alpha,N}^{far}.
\]

The core stretching contribution is uniformly bounded because `w_alpha` is bounded on `B_{R_alpha}` and the hull has uniform smooth/enstrophy bounds:

\[
\boxed{
2\int_{|y|\le R_\alpha}
w_{\alpha,N}|q|
\le C_{\alpha,core}.
}
\]

---

## 6. Far-field advection is absorbable

Using

\[
|\nabla w_{\alpha,N}|
\le
C_\alpha
\frac{w_{\alpha,N}}{1+|y|},
\]

we obtain outside `R_alpha`

\[
\left|
\int
(\nabla w_{\alpha,N}\cdot U)h
\right|_{far}
\le
\frac{c_\alpha}{16}
M_{\alpha,N}^{far}.
\]

The core advection contribution is again uniformly bounded:

\[
\boxed{
\left|
\int_{|y|\le R_\alpha}
(\nabla w_{\alpha,N}\cdot U)h
\right|
\le C_{\alpha,core}.
}
\]

---

## 7. Weight-Laplacian term

The uniform bound

\[
\Delta w_{\alpha,N}
\le C_\alpha
\]

gives

\[
\boxed{
\int(\Delta w_{\alpha,N})h
\le
C_\alpha E
\le
C_\alpha Z_*.
}
\]

The dissipative term

\[
-2\int w_{\alpha,N}p
\]

has the favorable sign and may simply be dropped for an upper differential inequality.

---

## 8. Uniform dissipative differential inequality

Combining Sections 2--7 gives

\[
\frac d{d\theta}M_{\alpha,N}
\le
-c_\alpha M_{\alpha,N}
+
\frac{3c_\alpha}{16}M_{\alpha,N}^{far}
+
C_\alpha^*.
\]

Since

\[
M_{\alpha,N}^{far}
\le M_{\alpha,N},
\]

we obtain, after weakening constants,

\[
\boxed{
\frac d{d\theta}M_{\alpha,N}
\le
-\kappa_\alpha M_{\alpha,N}
+C_\alpha^*,
}
\]

with

\[
\kappa_\alpha>0
\]

independent of the truncation level `N`.

For example one may take a fixed fraction of `1-alpha` after the preceding absorptions.

---

## 9. Invariant averaging

Because `M_{alpha,N}` is a bounded differentiable observable on the invariant component,

\[
\int
\frac d{d\theta}M_{\alpha,N}
d\nu
=0.
\]

Averaging the differential inequality gives

\[
0
\le
-\kappa_\alpha
\int M_{\alpha,N}d\nu
+C_\alpha^*.
\]

Hence

\[
\boxed{
\int M_{\alpha,N}d\nu
\le
\frac{C_\alpha^*}{\kappa_\alpha}
}
\]

uniformly in `N`.

---

## 10. Remove the truncation

As `N -> infinity`,

\[
w_{\alpha,N}\uparrow w_\alpha.
\]

By monotone convergence,

\[
\boxed{
\int_{\widehat{\mathfrak H}}
\mathcal M_\alpha(Y)d\nu(Y)
<\infty.
}
\]

Therefore

\[
\boxed{
\mathcal M_\alpha(Y)<\infty
\quad
\text{for }\nu\text{-almost every }Y.
}
\]

---

## 11. Simultaneously for every alpha<1

Apply the preceding result to the countable set of rational exponents

\[
\alpha\in\mathbb Q\cap(0,1).
\]

Intersect the corresponding full-measure sets.

For any real

\[
0<\alpha<1,
\]

choose a rational

\[
\alpha<\beta<1.
\]

Since

\[
(1+|y|^2)^{\alpha/2}
\le
1+(1+|y|^2)^{\beta/2},
\]

finiteness of `M_beta` implies finiteness of `M_alpha`.

Thus there is one full-measure invariant set on which

\[
\boxed{
\mathcal M_\alpha<\infty
\qquad
\forall\alpha<1.
}
\]

---

## 12. Compare with the first moment

M5-531 gives on the same nontrivial recurrent component

\[
\boxed{
\mathcal M_1
=
\int |y||W|^2dy
=
\infty
\quad\nu\text{-a.e.}
}
\]

Therefore

\[
\boxed{
\begin{aligned}
&\int(1+|y|^2)^{\alpha/2}|W|^2dy<\infty
&&\forall\alpha<1,\\
&\int |y||W|^2dy=\infty
&&\text{at }\alpha=1,
\end{aligned}
\qquad\nu\text{-a.e.}
}
\]

The radial critical exponent is exactly `alpha=1`.

---

## 13. Why alpha=1 is structurally special

For a homogeneous weight `|y|^alpha`, the similarity linear contribution is

\[
\frac{\alpha-1}{2}
\int |y|^\alpha|W|^2dy.
\]

Hence

- `alpha<1`: strict linear damping;
- `alpha=1`: exact cancellation;
- `alpha>1`: linear growth.

The infinite first moment identified in M5-531 is therefore not an arbitrary weighted failure.

It occurs exactly at the scaling-neutral radial exponent of the similarity enstrophy equation.

---

## 14. Updated hard core

The recurrent compact survivor is now constrained by

\[
\boxed{
\text{all-order unweighted smooth compactness}
+
\text{all subcritical radial moments finite}
+
\text{critical first radial moment infinite}.
}
\]

Together with M5-533--535, this critical moment is carried by a low-amplitude, low-strain remote dust reservoir that is asymptotically decoupled from the active finite-lineage core.

---

## 15. Highest-value next target

The exact threshold suggests studying a logarithmically softened critical weight, for example

\[
\boxed{
w_{1,\gamma}(y)
:=
\frac{|y|}{[\log(e+|y|)]^\gamma}.
}
\]

Such a weight is still almost critical but acquires a weak positive damping from the logarithmic derivative.

If invariant averaging proves finiteness for every `gamma>0`, while the pure `|y|` moment remains infinite, the tail is forced into a sharp logarithmic endpoint analogous to weak-`L3` criticality.

This is the next natural calculation.

---

## 16. Status

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
