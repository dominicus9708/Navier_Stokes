# DSD M5-8 — Spherical cross-radius Hodge coercivity

Date: 2026-08-26

Status: **DERIVED COERCIVITY LEMMA / CROSS-RADIUS CRITICAL MASS CANNOT HAVE BOTH SMALL RADIAL VARIATION AND SMALL ANGULAR-VORTICITY ACTION / DOES NOT BY ITSELF CLOSE M5 / GLOBAL REGULARITY UNPROVED.**

## 1. Log-radius profile

Fix a physical time and a center `X_*`. Write

\[
x-X_*=r\theta,\qquad r=e^\rho,\qquad \theta\in S^2,
\]

and define the scale-critical profile

\[
F(\theta,\rho)=r\,u(X_*+r\theta).
\]

Decompose

\[
F=F_r\theta+F_T,
\qquad F_T\cdot\theta=0.
\]

For a smooth divergence-free whole-space field, the flux through every sphere vanishes:

\[
\boxed{\int_{S^2}F_r(\theta,\rho)\,d\theta=0.}
\]

## 2. Exact incompressibility identity

Using the spherical divergence formula,

\[
\boxed{
\partial_\rho F_r+F_r+\operatorname{div}_{S^2}F_T=0.
}
\]

Thus radial scale variation and tangential angular divergence are not independent channels.

## 3. Exact vorticity identity

Let `omega=curl u`. Direct spherical-coordinate calculation gives

\[
\boxed{
r^2\omega
=(\operatorname{curl}_{S^2}F_T)\,\theta
+\theta\times
(\partial_\rho F_T-\nabla_{S^2}F_r).
}
\]

Define the scale-critical spherical vorticity charge

\[
\mathcal Q_\omega(\rho)
:=
\|\operatorname{curl}_{S^2}F_T\|_{L^2(S^2)}^2
+
\|\partial_\rho F_T-\nabla_{S^2}F_r\|_{L^2(S^2)}^2.
\]

Then

\[
\mathcal Q_\omega(\rho)
=r^4\int_{S^2}|\omega(r\theta)|^2d\theta
=r^2\int_{S_r}|\omega|^2dS.
\]

## 4. Coercivity on the sphere

Because `F_r` has zero mean on `S^2`, scalar Poincare gives

\[
\|F_r\|_2
\le C\|\nabla_{S^2}F_r\|_2.
\]

From the vorticity identity,

\[
\|\nabla_{S^2}F_r\|_2
\le
\|\partial_\rho F_T\|_2
+
\mathcal Q_\omega^{1/2}.
\]

Hence

\[
\|F_r\|_2
\le C\bigl(
\|\partial_\rho F\|_2
+\mathcal Q_\omega^{1/2}
\bigr).
\]

For tangential vector fields on `S^2`, there are no nonzero harmonic one-forms, so the Hodge--Poincare estimate gives

\[
\|F_T\|_2
\le C\bigl(
\|\operatorname{div}_{S^2}F_T\|_2
+\|\operatorname{curl}_{S^2}F_T\|_2
\bigr).
\]

Using incompressibility,

\[
\operatorname{div}_{S^2}F_T
=-F_r-\partial_\rho F_r,
\]

and the preceding estimate yields

\[
\|F_T\|_2
\le C\bigl(
\|\partial_\rho F\|_2
+\mathcal Q_\omega^{1/2}
\bigr).
\]

Therefore

\[
\boxed{
\|F(\rho)\|_{L^2(S^2)}^2
\le
C\left(
\|\partial_\rho F(\rho)\|_{L^2(S^2)}^2
+\mathcal Q_\omega(\rho)
\right).
}
\]

Equivalently,

\[
\boxed{
\mathcal Q_\omega(\rho)
+\|\partial_\rho F(\rho)\|_2^2
\ge c\|F(\rho)\|_2^2.
}
\]

## 5. Cubic critical mass forces formation action

Under the retained Type-I envelope `|F|<=A_0`,

\[
\int_{S^2}|F|^3d\theta
\le
A_0\|F\|_2^2.
\]

Hence

\[
\boxed{
\mathcal Q_\omega(\rho)
+\|\partial_\rho F(\rho)\|_2^2
\ge
\frac{c}{A_0}
\int_{S^2}|F|^3d\theta.
}
\]

Thus every log-radius scale carrying nontrivial critical cubic mass must pay through at least one of two channels:

1. **radial reformation:** `partial_rho F` is non-small;
2. **angular/vorticity action:** `Q_omega` is non-small.

There is no third lane in which a nonzero critical shell is simultaneously radially coherent and angularly/vortically trivial.

## 6. Integrated form

For any log-radius interval `I`,

\[
\boxed{
\int_I
\left(
\mathcal Q_\omega
+\|\partial_\rho F\|_2^2
\right)d\rho
\ge
\frac{c}{A_0}
\int_I\int_{S^2}|F|^3d\theta\,d\rho.
}
\]

The vorticity part is exactly a weighted physical enstrophy:

\[
\boxed{
\int_I\mathcal Q_\omega d\rho
=
\int_{e^I}|x-X_*|\,|\omega(x)|^2dx.
}
\]

The radial part is the corresponding scale-variation action of the critical profile `r u`.

## 7. DSD interpretation

M5-5 through M5-7 showed that the surviving obstruction is not one isolated packet but a cross-radius critical family. This lemma states that such a family cannot be represented by a featureless scalar `1/r` amplitude alone.

Its persistence across logarithmic radius necessarily carries structural information in one or both of

\[
\boxed{
\partial_\rho(r u)
}
\]

and

\[
\boxed{
r^2\omega.
}
\]

Thus cross-radius coherence has a quantitative vector-geometric formation cost.

## 8. Why this does not yet close M5

Neither

\[
\int |x-X_*||\omega|^2dx
\]

at a fixed late time nor the radial formation action is known to have a uniform finite bound strong enough to contradict logarithmically many critical shells. In fact the retained W1 corridor can accommodate logarithmic growth of such scale-critical quantities.

Therefore M5 is not closed here.

The next question is whether a genuinely scale-critical **physical-time** ledger, rather than a fixed-time radial ledger, can control this cross-radius action.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
