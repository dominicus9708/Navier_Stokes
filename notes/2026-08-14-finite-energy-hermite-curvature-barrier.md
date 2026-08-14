# Finite-energy Hermite curvature barrier for Gaussian gradient residuals

Date: 2026-08-14

Status: **DERIVED SCALE-DEPENDENT CURVATURE BARRIER / ORDER-ONE LOW-CURVATURE RESIDUAL REMOVED FROM THE NON-AFFINE MESOSCOPIC WINDOW / VANISHING CRITICAL RIDGE REMAINS OPEN**.

This note uses a fact not exploited in the previous residual Poincare analysis: the Gaussian residual

\[
\mathcal B_\Sigma
=P_\Sigma|\nabla U|^2-|P_\Sigma\nabla U|^2
\]

is the variance of a field which is itself the gradient of a **finite-energy velocity**.

After whitening the Gaussian, Hermite degree links velocity energy, residual-gradient variance, and curvature exactly.  This produces a scale-dependent uncertainty inequality.  At mesoscopic radii above `W^(1/10)`, an order-one residual cannot stay in low Hermite degree: finite kinetic energy forces it into high curvature.

No novelty claim is made without a separate literature-priority audit.

---

## 1. Gaussian whitening

Let `gamma_Sigma` be a centered Gaussian of covariance `Sigma>0` around center `a`, and define

\[
L=P_\Sigma(\nabla U)(a),
\qquad
B=\mathcal B_\Sigma(a)
=\int\gamma_\Sigma|\nabla U-L|^2dx.
\]

Set

\[
z=\Sigma^{-1/2}(x-a),
\qquad
F(z)=U(a+\Sigma^{1/2}z).
\]

Under the standard Gaussian `gamma` in `z`,

\[
\nabla_zF=(\nabla_xU)\Sigma^{1/2}.
\]

Define the mean-free whitened gradient

\[
H(z)
=\nabla_zF-(L\Sigma^{1/2})
=(\nabla U-L)\Sigma^{1/2}.
\]

Let

\[
A=\int|H|_F^2d\gamma.
\]

Then

\[
\boxed{
\lambda_{\min}(\Sigma)B
\le A
\le\lambda_{\max}(\Sigma)B.
}
\]

---

## 2. Hermite decomposition of the velocity

Expand the vector field `F` into standard Gaussian Hermite chaoses:

\[
F=\sum_{n\ge0}F_n,
\]

where `F_n` has total Hermite degree `n`.

The constant part of `grad_z F` comes only from `F_1`.  Therefore

\[
H
=\sum_{n\ge2}\nabla F_n.
\]

Orthogonality and the Ornstein--Uhlenbeck eigenvalue identity give

\[
\boxed{
A
=\sum_{n\ge2}n\|F_n\|_{L^2(\gamma)}^2.
}
\]

Let

\[
E_2
=\sum_{n\ge2}\|F_n\|_{L^2(\gamma)}^2.
\]

Clearly

\[
E_2\le\int|F|^2d\gamma.
\]

For the whitened Hessian,

\[
C
:=\int|D_z^2F|_F^2d\gamma
=\sum_{n\ge2}n(n-1)\|F_n\|_2^2.
\]

Thus

\[
C+A
=\sum_{n\ge2}n^2\|F_n\|_2^2.
\]

---

## 3. Exact Hermite interpolation inequality

Cauchy--Schwarz on the sequence of Hermite energies yields

\[
A^2
=\left(
\sum_{n\ge2}n\|F_n\|_2^2
\right)^2
\le
\left(\sum_{n\ge2}\|F_n\|_2^2\right)
\left(\sum_{n\ge2}n^2\|F_n\|_2^2\right).
\]

Therefore

\[
\boxed{
C
\ge
\frac{A^2}{E_2}-A.
}
\]

This is the central spectral uncertainty inequality: a fixed amount of gradient variance can have small curvature only if enough velocity energy is available in the corresponding Gaussian window.

---

## 4. Bound the Gaussian velocity energy by global kinetic energy

Let

\[
R=(\det\Sigma)^{1/6}
\]

be the Gaussian volume radius.  Since

\[
\|\gamma_\Sigma\|_\infty
=(2\pi)^{-3/2}R^{-3},
\]

we have

\[
E_2
\le
\int\gamma_\Sigma|U|^2dx
\le
C R^{-3}\|U\|_2^2.
\]

Therefore

\[
\boxed{
C
\ge
c\,
\frac{A^2R^3}{\|U\|_2^2}
-A.
}
\]

---

## 5. Convert the whitened Hessian to physical curvature

Because

\[
D_z^2F
=(\Sigma^{1/2})^T(D_x^2U)\Sigma^{1/2}
\]

in the two spatial derivative indices,

\[
|D_z^2F|_F^2
\le
\lambda_{\max}(\Sigma)^2|D_x^2U|_F^2.
\]

Define

\[
D_g
:=
\int\gamma_\Sigma|D_x^2U|_F^2dx
=
\int\gamma_\Sigma|\nabla(\nabla U-L)|_F^2dx.
\]

Then

\[
D_g
\ge
\frac{C}{\lambda_{\max}(\Sigma)^2}.
\]

Combining the previous bounds gives

\[
\boxed{
D_g
\ge
c\,
\frac{\lambda_{\min}(\Sigma)^2}
{\lambda_{\max}(\Sigma)^2}
\frac{B^2R^3}{\|U\|_2^2}
-
\frac{B}{\lambda_{\max}(\Sigma)}.
}
\]

On a covariance family of condition number at most `K`, this simplifies to

\[
\boxed{
D_g
\ge
c_K\frac{B^2R^3}{\|U\|_2^2}
-C_K\frac{B}{R^2}.
}
\]

The second term is of ordinary Gaussian-Poincare size.  The first term is a new finite-energy curvature term.

---

## 6. Dimensionless Hermite-energy ratio

Introduce

\[
\boxed{
\Xi_E
:=
\frac{BR^5}{\|U\|_2^2}.
}
\]

Relative to the Poincare scale `B/R^2`, the new curvature term is larger by a factor comparable to `Xi_E`.

Hence

\[
\boxed{
\Xi_E\gg1
\Longrightarrow
D_g\gg_K\frac{B}{R^2}.
}
\]

Interpretation:

- `Xi_E << 1`: enough velocity energy exists for the residual to live predominantly in low Hermite degree;
- `Xi_E ~ 1`: critical Hermite-energy saturation;
- `Xi_E >> 1`: low-degree support is impossible, so the residual is forced into high Hermite degree and therefore high curvature.

---

## 7. Terminal first-hitting normalization

At terminal vorticity level

\[
W=\|\omega(T)\|_\infty,
\qquad
r=W^{-1/2},
\]

the normalized velocity satisfies

\[
\|U\|_2^2
=r^{-1}\|u\|_2^2
\le
C(u_0)W^{1/2}.
\]

Therefore

\[
\boxed{
\Xi_E
\gtrsim
\frac{BR^5}{W^{1/2}}.
}
\]

The low-curvature branch must consequently satisfy

\[
\boxed{
BR^5
\lesssim
W^{1/2}
}
\]

up to bounded-affine constants.

Equivalently,

\[
\boxed{
B(R)
\lesssim
W^{1/2}R^{-5}.
}
\]

This is the **finite-energy Hermite ridge**.

---

## 8. Consequence for the non-affine mesoscopic window

Recall the unresolved bounded-affine spatial band

\[
W^{1/10+\varepsilon}
\ll R
\ll
W^{1/6-\varepsilon}.
\]

For a fixed-positive residual

\[
B\ge b_*>0,
\]

at the lower edge

\[
\Xi_E
\gtrsim
b_*W^{5\varepsilon}.
\]

Thus throughout every scale satisfying

\[
R\gg W^{1/10},
\]

an order-one residual has

\[
\boxed{
\Xi_E\to\infty.
}
\]

Therefore an order-one residual in the non-affine mesoscopic window cannot remain a low-curvature/Poincare-saturating inertial state.  It is automatically retyped as a **high-Hermite / high-curvature event**.

This is stronger than the separate bounded-vorticity and BMO Poincare-gap lemmas because it applies directly to the full gradient residual and the gain grows with scale.

---

## 9. Amplitude-scale critical ridge

Write

\[
R=W^\theta,
\qquad
B=W^{-\beta}.
\]

The low-curvature Hermite ridge is

\[
W^{-\beta}W^{5\theta}
\lesssim
W^{1/2},
\]

hence

\[
\boxed{
\beta
\gtrsim
5\theta-\frac12.
}
\]

At the two current scale boundaries:

### Lower boundary

\[
\theta=\frac1{10}
\quad\Longrightarrow\quad
\beta\gtrsim0.
\]

So order-one residual is only critical exactly at the `W^(1/10)` boundary.

### Upper boundary

\[
\theta=\frac16
\quad\Longrightarrow\quad
\beta\gtrsim\frac13.
\]

So at the `W^(1/6)` ceiling a low-curvature residual must have size at most

\[
\boxed{B\lesssim W^{-1/3}.}
\]

This exactly matches the independent residual-peak/dissipation lower threshold derived previously.

The two calculations therefore meet at the same endpoint:

\[
\boxed{
(R,B)
\sim
(W^{1/6},W^{-1/3}).
}
\]

This is a new critical-wall identification inside the present proof route.

---

## 10. Revised residual geometry

The old non-affine inertial window allowed, in principle, an order-one residual throughout

\[
W^{1/10}\ll R\ll W^{1/6}.
\]

The finite-energy Hermite barrier sharpens this to an amplitude-dependent corridor:

\[
\boxed{
W^{1/10}\ll R\ll W^{1/6},
\qquad
W^{-1/3}\lesssim B(R)\lesssim W^{1/2}R^{-5}
}
\]

for a surviving low-curvature residual route.

Consequences:

1. fixed-positive/order-one residual is expelled from the low-curvature mesoscopic branch;
2. the surviving branch must decay in amplitude as the active scale grows;
3. the smallest allowed peak `W^(-1/3)` can occur only near the upper `W^(1/6)` scale ceiling;
4. any violation of the ridge becomes a high-curvature/Hermite event rather than an ordinary inertial residual.

---

## 11. Relation to the residual diffusion term

Pointwise in the Gaussian weight,

\[
|\nabla(\nabla U)|_F^2
=|\nabla S|_F^2
+\frac12|\nabla\Omega|^2.
\]

Hence

\[
D_g
=D_S+\frac12D_\omega.
\]

The combined four-channel variance equation

\[
B=V_S+\frac12V_\omega
\]

therefore has viscous contribution

\[
\boxed{-2\nu D_g.}
\]

Thus the Hermite curvature barrier enters the exact residual dynamics directly; it is not merely a static diagnostic.

However the present Osgood production bounds can still dominate this diffusion during sufficiently short inertial pulses, so a complete regularity contradiction is not yet obtained.

---

## 12. Current remaining target

The genuinely unresolved bounded-affine branch is now concentrated near the critical amplitude-scale ridge

\[
\boxed{
BR^5\sim W^{1/2}
}

with endpoint

\[
\boxed{
R\sim W^{1/6},
\qquad
B\sim W^{-1/3}.
}

The next proof-producing question is whether a residual pulse can move along this ridge while simultaneously satisfying

1. the Osgood growth law;
2. Gaussian total-variance scale packing;
3. the first-hitting vorticity cap;
4. pressure-parent localization;
5. finite physical dissipation;
6. the Hermite interpolation near-equality conditions.

A quantitative incompatibility among those conditions would remove the last low-curvature non-affine corridor.

Status: **ORDER-ONE LOW-CURVATURE MESOSCOPIC RESIDUAL REMOVED / SURVIVING LOW-CURVATURE ROUTE COLLAPSED TO THE VANISHING HERMITe-ENERGY RIDGE `B R^5 ~ W^(1/2)`**.
