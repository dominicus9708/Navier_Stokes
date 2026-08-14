# Affine-cancellation cost for the residual stretching source

Date: 2026-08-14

Status: **DERIVED: BOUNDED ACCUMULATED AFFINE STRAIN CANNOT REPEATEDLY HIDE A VANISHING RESIDUAL STRETCH SOURCE / TOTAL-STRAIN GEOMETRY INHERITS A FIXED SOURCE FRACTION**.

The exact residual stretching source is

\[
J_{\rm str}(s)=\int\gamma\,\delta S\,\delta\Omega,
\]

with

\[
S=\bar S+\delta S,
\qquad
\bar S=\operatorname{sym}L.
\]

The previous source-to-axis bridge typed `delta S delta Omega` into directional stretch or axis conversion of the fluctuating vorticity direction.  A potential loophole is cancellation by the spatially constant affine mean `bar S`.  This note shows that such cancellation is too expensive on a bounded-affine branch when the residual peak tends to zero.

---

## 1. Weighted total-strain lower bound

At points with `delta Omega != 0`, let

\[
n=\frac{\delta\Omega}{|\delta\Omega|}.
\]

Then

\[
\delta S\,\delta\Omega
=S\,\delta\Omega-\bar S\,\delta\Omega.
\]

Using

\[
|a+b|^2\ge\frac12|a|^2-|b|^2,
\]

we obtain

\[
|S\delta\Omega|^2
\ge
\frac12|\delta S\delta\Omega|^2
-|\bar S|^2|\delta\Omega|^2.
\]

After Gaussian averaging,

\[
\boxed{
\int\gamma|S\delta\Omega|^2
\ge
\frac12\int\gamma|\delta S\delta\Omega|^2
-|\bar S|^2V_\omega.
}
\]

If the stretching source is efficient at time `s`,

\[
|J_{\rm str}|
\ge
\eta\sqrt{V_\omega B},
\]

then Jensen/Cauchy gives

\[
\int\gamma|\delta S\delta\Omega|^2
\ge
\eta^2V_\omega B.
\]

Therefore

\[
\boxed{
\int\gamma|S\delta\Omega|^2
\ge
V_\omega
\left(
\frac{\eta^2}{2}B-|\bar S|^2
\right).
}
\]

Hence at every efficient-source time one has a dichotomy:

### Total-strain branch

If

\[
|\bar S|^2
\le
\frac{\eta^2}{4}B,
\]

then

\[
\boxed{
\int\gamma|S\delta\Omega|^2
\ge
\frac{\eta^2}{4}V_\omega B.
}
\]

### Affine-cancellation branch

Otherwise

\[
\boxed{
|\bar S|
\ge
\frac\eta2\sqrt B.
}
\]

---

## 2. Integrated affine cancellation has a `1/sqrt(m)` cost

Let `I_A` be the subset of a responsible first-hitting interval on which the affine-cancellation branch is used.  Let

\[
m=\sup_I B.
\]

Suppose the stretching source carried on `I_A` has fixed absolute budget

\[
\int_{I_A}|J_{\rm str}(s)|ds
\ge\rho_A>0.
\]

Since

\[
|J_{\rm str}|
\le
\sqrt{V_\omega V_S}
\le
C B,
\]

we have

\[
\int_{I_A}B(s)ds
\ge
c\rho_A.
\]

On `I_A`,

\[
|\bar S|\ge c_\eta\sqrt B.
\]

Because `B<=m`,

\[
\sqrt B\ge\frac{B}{\sqrt m}.
\]

Therefore

\[
\boxed{
\int_{I_A}|\bar S(s)|ds
\ge
c_{\eta,\rho_A}\,m^{-1/2}.
}
\]

This lower bound diverges whenever

\[
m\to0.
\]

---

## 3. Contradiction with the bounded-affine branch

The bounded-affine covariance/deformation branch assumes a uniform accumulated affine-strain bound on each responsible window,

\[
\boxed{
\int_I|\operatorname{sym}L(s)|ds
=\int_I|\bar S(s)|ds
\le K.
}
\]

Consequently, for sufficiently small residual peak `m`, the affine-cancellation subset cannot carry any fixed positive fraction of the endpoint stretching-source budget.

More quantitatively, if

\[
\int_{I_A}|\bar S|ds\le K,
\]

then

\[
\boxed{
\rho_A
\le C_{K,\eta}\sqrt m.
}
\]

Thus

\[
\boxed{
m\to0
\Longrightarrow
\text{affine cancellation can hide only }o(1)
\text{ of the residual stretching source}.}
\]

---

## 4. Consequence: total strain inherits the source geometry

Suppose the full residual stretching source contributes a fixed endpoint amount while

\[
m\to0
\]

on a uniformly bounded-affine sequence of first-hitting windows.

The affine-cancellation part is `o(1)`.  Therefore a fixed fraction of the stretching-source budget must occur on the total-strain branch, where

\[
\int\gamma|S\delta\Omega|^2
\gtrsim
V_\omega B.
\]

For the fluctuating-vorticity direction `n`,

\[
|Sn|^2
=(n^TSn)^2
+|(I-n\otimes n)Sn|^2.
\]

Hence the surviving source is routed to at least one of

\[
\boxed{
\text{total directional strain along }n
}
\]

or

\[
\boxed{
\text{total-strain axis conversion of }n.
}
\]

The remaining issue is that `n` is the direction of `delta Omega`, not automatically the total/material vorticity direction.  A separate longitudinal/transverse decomposition relative to the Gaussian mean vorticity resolves most of this ambiguity.

---

## 5. Critical-ridge implication

On the surviving low-curvature corridor,

\[
m=W^{-1/3}\Lambda,
\qquad
\Lambda\to\infty,
\]

while the low-amplitude branch still has

\[
m\to0
\]

whenever `Lambda=o(W^(1/3))`.

Then any attempt to use affine cancellation for a fixed stretching-source fraction costs

\[
\int|\bar S|ds
\gtrsim
W^{1/6}\Lambda^{-1/2},
\]

which diverges throughout the genuinely vanishing residual regime.

Therefore the bounded-affine assumption itself forces the residual stretching source to become visible in the total strain geometry.

Status: **AFFINE-MEAN CANCELLATION OF A FIXED VANISHING RESIDUAL STRETCH SOURCE IS EXCLUDED / TOTAL-STRAIN STRETCH-OR-CONVERSION WITNESS SURVIVES**.
