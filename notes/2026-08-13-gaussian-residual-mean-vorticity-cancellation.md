# Gaussian residual mean-vorticity cancellation and linear four-channel endpoint bound

Date: 2026-08-13

Status: **DERIVED EXACT CANCELLATION + SHARPENED RESIDUAL-VARIANCE DEPENDENCE / GLOBAL REGULARITY NOT PROVED**.

The self-consistent Gaussian affine note bounded the averaged residual source by `sqrt(B_gamma)`.  The self-consistency conditions contain one additional cancellation: the constant Gaussian-mean vorticity cannot contribute to the averaged non-affine source because the residual gradient has zero Gaussian mean.

This upgrades the canonical small-residual dependence from square-root to linear in the four-channel variance.

---

## 1. Setup

Let

\[
r=u-a'-Ly,
\]

with

\[
\int\gamma r=0,
\qquad
\int\gamma\nabla r=0,
\qquad
\nabla\cdot r=0.
\]

Let

\[
\Omega=\omega(a+y,t),
\qquad
\bar\Omega_\gamma=\int\gamma\Omega,
\qquad
\delta\Omega=\Omega-\bar\Omega_\gamma.
\]

The residual vorticity source is

\[
f_r=(\Omega\cdot\nabla)r-(r\cdot\nabla)\Omega.
\]

---

## 2. Exact cancellation of the mean-vorticity stretching term

Split

\[
\Omega=\bar\Omega_\gamma+\delta\Omega.
\]

Because `bar Omega_gamma` is spatially constant,

\[
\int\gamma
(\bar\Omega_\gamma\cdot\nabla)r
=
\bar\Omega_\gamma\cdot
\int\gamma\nabla r
=0.
\]

The transport of the constant part also vanishes because

\[
(r\cdot\nabla)\bar\Omega_\gamma=0.
\]

Hence exactly

\[
\boxed{
\int\gamma f_r
=
\int\gamma(\delta\Omega\cdot\nabla)r
-
\int\gamma(r\cdot\nabla)\delta\Omega.
}
\]

Using `div r=0`, integrate the second term by parts:

\[
\boxed{
\int\gamma f_r
=
\int\gamma(\delta\Omega\cdot\nabla)r
+
\int\gamma\,\delta\Omega\,
(r\cdot\nabla\log\gamma).
}
\]

Thus every averaged residual-source contribution contains the vorticity fluctuation `delta Omega`.

---

## 3. Gaussian `H1` drift estimate in `L2`

For `gamma=N(0,Sigma)` and a Gaussian-mean-zero vector field `r`, the standard Gaussian multiplication/creation estimate gives

\[
\||z|h\|_{L^2(d\gamma_0)}
\le C
\left(
\|h\|_{L^2(d\gamma_0)}
+\|\nabla h\|_{L^2(d\gamma_0)}
\right)
\]

in standard coordinates.  After `y=Sigma^(1/2) z` and Gaussian Poincare,

\[
\boxed{
\|r\cdot\Sigma^{-1}y\|_{L^2(\gamma)}
\le
C\sqrt{\kappa(\Sigma)}
\|\nabla r\|_{L^2(\gamma)}.
}
\]

The precise universal numerical constant is not used below.

---

## 4. Source bound by vorticity variance times non-affinity variance

Define

\[
V_\omega
=\int\gamma|\delta\Omega|^2
\]

and

\[
\mathcal B_\gamma
=\int\gamma|\nabla r|^2.
\]

The stretching residual satisfies

\[
\left|
\int\gamma(\delta\Omega\cdot\nabla)r
\right|
\le
\sqrt{V_\omega}\sqrt{\mathcal B_\gamma}.
\]

The transport residual satisfies

\[
\begin{aligned}
\left|
\int\gamma\delta\Omega\,
(r\cdot\nabla\log\gamma)
\right|
&\le
\sqrt{V_\omega}
\|r\cdot\Sigma^{-1}y\|_{L^2(\gamma)}\\
&\le
C\sqrt{\kappa(\Sigma)}
\sqrt{V_\omega}
\sqrt{\mathcal B_\gamma}.
\end{aligned}
\]

Therefore

\[
\boxed{
\left|
\int\gamma f_r
\right|
\le
C
[1+\sqrt{\kappa(\Sigma)}]
\sqrt{V_\omega\mathcal B_\gamma}.
}
\]

---

## 5. Four-channel identity makes the estimate linear

The exact four-channel residual identity is

\[
\mathcal B_\gamma
=
D_{S,\rm shape}
+D_{S,\rm amp}
+\frac12D_{\omega,\rm proj}
+\frac12D_{\omega,\rm line}.
\]

Since

\[
V_\omega
=D_{\omega,\rm proj}+D_{\omega,\rm line},
\]

we have

\[
\boxed{V_\omega\le2\mathcal B_\gamma.}
\]

Hence

\[
\boxed{
\left|
\int\gamma f_r
\right|
\le
C
[1+\sqrt{\kappa(\Sigma)}]
\mathcal B_\gamma.
}
\]

This is the canonical small-residual endpoint-source estimate.

---

## 6. Sharpened Duhamel residual bound

The exact affine Duhamel formula gives

\[
\mathfrak R_\gamma
=
\left|
\int_{t_0}^T
F(T,s)
\left[\int\gamma_s f_r\right]ds
\right|.
\]

Therefore

\[
\boxed{
\mathfrak R_\gamma
\le
C\int_{t_0}^T
\|F(T,s)\|_{op}
[1+\sqrt{\kappa(\Sigma(s))}]
\mathcal B_\gamma(s)\,ds.
}
\]

On a bounded-affine normalized interval,

\[
\boxed{
\mathfrak R_\gamma
\le
C_K\int_I\mathcal B_\gamma(s)\,ds.
}
\]

Thus an order-one residual endpoint branch requires an order-one accumulated four-channel action; there is no square-root amplification from an arbitrarily small residual variance.

---

## 7. Consequences and limitations

At the earlier endpoint of a terminal-`q` first-hitting step, the vorticity amplitude is at most `1/q` in terminal normalization.  Under bounded Gaussian conditioning this gives a small initial four-channel state of order `q^(-2)`.

The linear residual-source law therefore supports the Osgood pulse interpretation: a large endpoint residual cannot be created directly from a vanishing four-channel state without dynamically growing the residual variance itself.

However, an order-one `B_gamma` may persist for a long normalized ancient interval.  The linear bound alone does not provide a globally summable spacetime budget and therefore does not prove global regularity.

Status: **MEAN-VORTICITY CANCELLATION CLOSED / REPEATED FOUR-CHANNEL ACTION PACKING REMAINS OPEN**.
