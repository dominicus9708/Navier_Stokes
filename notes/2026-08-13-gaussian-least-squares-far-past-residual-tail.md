# Gaussian least-squares affine regression and integrable far-past residual tail

Date: 2026-08-13

Status: **EXACT GAUSSIAN REGRESSION IDENTITY + FINITE-KINETIC-ENERGY FAR-PAST TAIL / GLOBAL REGULARITY NOT PROVED**.

The self-consistent Gaussian affine representative has an additional exact property: it is the Gaussian least-squares affine regression of the velocity itself.  This converts the far-past residual Duhamel source into an integrable `tau^(-5/4)` tail using only finite kinetic energy and bounded affine distortion.

Combined with the terminal residual-variance collapse, the residual branch is confined to a fixed intermediate normalized-time annulus.

---

## 1. Self-consistent affine representative

Let `gamma=N(0,Sigma)` in coordinates `y=x-a(s)`, and define

\[
a'(s)=\int\gamma_s(y)u(a+y,s)dy,
\]

\[
L(s)=\int\gamma_s(y)\nabla u(a+y,s)dy.
\]

Set

\[
r(y,s)=u(a+y,s)-a'(s)-L(s)y.
\]

The previous Gaussian construction gives

\[
\int\gamma r=0,
\qquad
\int\gamma\nabla r=0.
\]

---

## 2. Gaussian Stein identity makes `L` the velocity-regression slope

For a centered Gaussian with covariance `Sigma`, integration by parts gives the matrix Stein identity

\[
\boxed{
\int\gamma(y)\,[u(a+y)-a']\,y^Tdy
=
\left(\int\gamma\nabla u(a+y)dy\right)\Sigma.
}
\]

Therefore

\[
\boxed{
L
=
\left[
\int\gamma(u-a')y^T
\right]\Sigma^{-1}.
}
\]

This is exactly the normal equation for minimizing

\[
\int\gamma|u-b-My|^2dy
\]

over a translation `b` and matrix `M`.

Hence

\[
\boxed{
(a',L)
=\arg\min_{b,M}
\int\gamma|u-b-My|^2dy.
}
\]

In particular, comparing with the admissible choice `b=0`, `M=0`,

\[
\boxed{
\int\gamma|r|^2dy
\le
\int\gamma|u(a+y,s)|^2dy.
}
\]

---

## 3. Finite kinetic energy bounds the Gaussian residual velocity

Because `gamma` is a probability density,

\[
\int\gamma|u(a+y,s)|^2dy
\le
\|\gamma_s\|_\infty
\|u(s)\|_2^2.
\]

Kinetic-energy dissipation gives

\[
\|u(s)\|_2\le\|u_0\|_2.
\]

Thus

\[
\boxed{
\|r(s)\|_{L^2(\gamma_s)}
\le
\|\gamma_s\|_\infty^{1/2}
\|u_0\|_2.
}
\]

This estimate is independent of global vorticity/enstrophy size.

---

## 4. Residual vorticity source average

The residual source is

\[
f_r
=\nabla\cdot(r\otimes\Omega-\Omega\otimes r).
\]

At first hitting,

\[
\|\Omega(s)\|_\infty\le1.
\]

Integration by parts gives

\[
\left|
\int\gamma f_rdy
\right|
\le
C\int\gamma
|r|\,|\Sigma^{-1}y|dy.
\]

By Cauchy-Schwarz,

\[
\boxed{
\left|
\int\gamma f_rdy
\right|
\le
C
\|r\|_{L^2(\gamma)}
\left(\operatorname{tr}\Sigma^{-1}\right)^{1/2}.
}
\]

Insert the least-squares energy estimate:

\[
\boxed{
\left|
\int\gamma f_rdy
\right|
\le
C\|u_0\|_2
\|\gamma\|_\infty^{1/2}
\left(\operatorname{tr}\Sigma^{-1}\right)^{1/2}.
}
\]

---

## 5. Bounded affine distortion gives the `tau^(-5/4)` law

Let

\[
\tau=T-s.
\]

Assume the accumulated symmetric affine strain on the relevant past interval is bounded by `K`.  Then the affine heat covariance satisfies

\[
2\nu e^{-2K}\tau I
\preceq
\Sigma(s)
\preceq
2\nu e^{2K}\tau I.
\]

Therefore

\[
\|\gamma_s\|_\infty^{1/2}
\le C_Ke^{0}(\nu\tau)^{-3/4},
\]

and

\[
\left(\operatorname{tr}\Sigma(s)^{-1}\right)^{1/2}
\le C_K(\nu\tau)^{-1/2}.
\]

Consequently

\[
\boxed{
\left|
\int\gamma_sf_rdy
\right|
\le
C_K\|u_0\|_2\,
u^{-5/4}\tau^{-5/4}.
}
\]

The exponent `5/4` is strictly larger than one.

---

## 6. Far-past Duhamel tail is integrable

The endpoint residual Duhamel term contains the affine transition factor `F(T,s)`.  Under the same accumulated affine-distortion bound,

\[
\|F(T,s)\|_{op}\le e^K.
\]

Hence for any `R>0`,

\[
\begin{aligned}
\mathfrak R_{\gamma,\,T-s\ge R}
&\le
C_K\|u_0\|_2\nu^{-5/4}
\int_R^\infty\tau^{-5/4}d\tau\\
&\le
C_K\|u_0\|_2\nu^{-5/4}R^{-1/4}.
\end{aligned}
\]

Thus

\[
\boxed{
\mathfrak R_{\gamma,\,T-s\ge R}
\le
C_K\|u_0\|_2\nu^{-5/4}R^{-1/4}.
}
\]

For any prescribed epsilon, one can choose a finite normalized backward horizon `R=R(epsilon,K,nu,||u0||2)` so that the entire older residual tail is below epsilon.

---

## 7. Combine with terminal collapse

The companion terminal-collapse lemma gives, under bounded affine distortion and weighted pressure-Hessian budget,

\[
\mathfrak R_{\gamma,\,0<T-s<\delta}
\le C_{K,C_P}\delta^{3/2}.
\]

Choose `delta` small and `R` large so that both tails are at most `epsilon`.

If the exact first-hitting residual branch requires an endpoint defect `R_gamma>=c0`, with `2epsilon<c0`, then a fixed fraction must come from

\[
\boxed{
\delta\le T-s\le R.
}
\]

This interval has

- covariance bounded above and below;
- no terminal delta degeneration;
- no ancient-past tail;
- bounded affine condition number;
- first-hitting vorticity amplitude cap.

Therefore the genuinely dangerous residual production is confined to a fixed-resolution compact Gaussian annulus in normalized spacetime.

---

## 8. DSD interpretation

The result prunes both temporal extremes.

Very old information is suppressed by the combination

\[
\boxed{
\text{finite kinetic energy}
+\text{Gaussian least-squares residual}
+\text{broad affine heat kernel}.
}
\]

Very recent information is suppressed by

\[
\boxed{
\text{Gaussian Poincare terminal coercivity}
+\text{bounded pressure/affine maintenance}.
}
\]

Hence a large unresolved contribution must already be present at a finite parent resolution.

This is precisely the adaptive-describability interpretation: unresolved information cannot hide indefinitely at either infinitely coarse or infinitely fine temporal resolution.

---

## 9. Current target

The residual branch is now reduced to an intermediate normalized-time annulus.  The next step is to use compactness on this annulus to show that a persistent order-one residual defect has a nontrivial limiting four-channel state, and then test that limit against

- Betchov/GN source efficiency;
- biaxial compression-diffusion;
- projective covariance;
- pressure-Hessian/eigenframe rotation;
- exact Cauchy I/V amplification.

Status: **FAR-PAST RESIDUAL TAIL CLOSED ON BOUNDED-AFFINE BRANCH / INTERMEDIATE-ANNULUS COMPACTNESS-RIGIDITY IS THE ACTIVE FRONTIER**.
