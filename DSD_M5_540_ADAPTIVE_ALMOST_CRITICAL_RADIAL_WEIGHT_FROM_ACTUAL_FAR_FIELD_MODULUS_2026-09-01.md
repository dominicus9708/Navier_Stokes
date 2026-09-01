# DSD M5-540 — The actual far-field modulus yields a finite adaptive almost-critical radial moment stronger than every power-subcritical moment

Date: 2026-09-01

Status: **ADAPTIVE ENDPOINT IMPROVEMENT / M5-539 SHOWS THAT NO PREASSIGNED LOGARITHMIC OR LORENTZ ENDPOINT FOLLOWS WITHOUT A RATE FOR THE FAR-FIELD DECAY / HOWEVER M5-523 AND M5-535 PROVIDE AN ACTUAL UNIFORM MODULUS `epsilon_far(R)->0` FOR VELOCITY-OVER-RADIUS AND STRAIN / CHOOSING A SLOWLY VARYING DEFICIT `delta(log R)` THAT MAJORIZES THIS MODULUS AND DEFINING `w(R)=R exp(-int delta dlogR)` PRODUCES AN ALMOST-CRITICAL WEIGHT / THE SIMILARITY LINEAR PART DISSIPATES `delta w |W|^2`, WHILE FAR STRETCHING, ADVECTION, AND WEIGHT-LAPLACIAN ERRORS ARE ABSORBED / INVARIANT AVERAGING THEREFORE GIVES FINITE MOMENT WITH WEIGHT `w_tilde=delta w`, WHICH GROWS FASTER THAN `R^(1-epsilon)` FOR EVERY FIXED `epsilon>0` BUT REMAINS `o(R)` / THE HARD TAIL IS THUS NARROWER THAN EVERY POWER-SUBCRITICAL CLASS YET STILL MAY FAIL THE PURE FIRST MOMENT / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Actual far-field modulus

Define

\[
\boxed{
\varepsilon_{far}(R)
:=
\sup_{Y\in\widehat{\mathfrak H}}
\sup_{|y|>R}
\left(
|\Sigma_Y(y)|
+
\frac{|U_Y(y)|}{1+|y|}
\right).
}
\]

M5-523 and M5-535 give

\[
\boxed{
\varepsilon_{far}(R)\to0
\qquad(R\to\infty).
}
\]

No universal rate is assumed.

---

## 2. Pass to logarithmic radius

Let

\[
\rho=\log(e+R).
\]

Take a smooth positive function

\[
\delta(\rho)
\]

such that for all sufficiently large `rho`,

\[
\boxed{
\delta(\rho)
\ge
C\varepsilon_{far}(e^\rho)
+
\frac1{1+\rho},
}
\]

and

\[
\delta(\rho)\downarrow0.
\]

By taking a smooth dyadic/logarithmic majorant, one may additionally arrange

\[
|\delta'(\rho)|
\le C\delta(\rho)
\]

without changing the asymptotic properties needed below.

The explicit `1/(1+rho)` term guarantees

\[
\boxed{
\int^{\infty}\delta(\rho)d\rho
=\infty.
}
\]

---

## 3. Adaptive near-critical weight

Define for large `r`

\[
A(\rho)
:=
\int_{\rho_0}^{\rho}\delta(\eta)d\eta,
\]

and

\[
\boxed{
w(r)
:=
r e^{-A(\log r)}.
}
\]

Regularize smoothly on the bounded core.

Then

\[
\boxed{
\frac{d\log w}{d\log r}
=1-\delta(\log r).
}
\]

Thus

\[
r w'(r)
=
(1-\delta)w.
\]

The similarity linear term becomes

\[
\boxed{
-\frac12w
+
\frac12r w'
=
-\frac12\delta w.
}
\]

So the weight retains a weak but strictly positive damping deficit determined by the actual far-field modulus.

---

## 4. The weight is strictly between every power and the critical first moment

Because

\[
\delta(\rho)\to0,
\]

Cesaro averaging gives

\[
A(\rho)=o(\rho).
\]

Therefore for every fixed

\[
\epsilon>0,
\]

\[
\log\frac{w(r)}{r^{1-\epsilon}}
=
\epsilon\log r-A(\log r)
\to\infty.
\]

Hence

\[
\boxed{
w(r)\gg r^{1-\epsilon}
\qquad
\forall\epsilon>0.
}
\]

On the other hand,

\[
\frac{w(r)}r
=e^{-A(\log r)}	o0
\]

because `int delta = infinity`.

Thus

\[
\boxed{
r^{1-\epsilon}\ll w(r)\ll r.
}
\]

---

## 5. Weight derivatives

Using logarithmic differentiation,

\[
w'(r)
=
\frac{1-\delta}{r}w.
\]

A second differentiation gives

\[
\Delta w
=
\frac{w}{r^2}
\left[
2-3\delta+\delta^2-\delta'
\right]
\]

up to the harmless bounded-core regularization.

Hence for large `r`,

\[
\boxed{
|\nabla w|
\le C\frac wr,
}
\]

and

\[
\boxed{
|\Delta w|
\le C\frac{w}{r^2}.
}
\]

Because

\[
\delta(\log r)
\ge\frac1{1+\log r}
\gg r^{-2},
\]

we may choose the far-field starting radius so that

\[
\boxed{
\frac{C}{r^2}
\le
\frac1{16}\delta(\log r)
}
\]

there.

---

## 6. Truncate the weight

As in M5-536, use increasing concave truncations

\[
w_N=\psi_N(w)
\]

so that all weighted observables are finite and the derivative inequalities survive with constants independent of `N`.

Set

\[
M_{w,N}
:=
\int w_N|W|^2dy.
\]

The linear similarity contribution is bounded above by

\[
-\frac12
\int
\delta w_N|W|^2dy
\]

outside a fixed core, modulo a bounded core correction.

---

## 7. Absorb far-field stretching

By construction of `delta`, for sufficiently large radius,

\[
|\Sigma(y)|
\le c\delta(\log|y|)
\]

with the constant chosen small relative to the linear damping.

Therefore

\[
2w_N|W\cdot\Sigma W|
\le
\frac18
\delta w_N|W|^2
\]

in the far field.

The core stretching contribution is uniformly bounded.

---

## 8. Absorb far-field advection

Similarly,

\[
|\nabla w_N\cdot U|
\le
C\frac{|U|}{|y|}w_N
\le
\frac18
\delta w_N
\]

for sufficiently large radius.

Again the bounded-core contribution is uniformly finite.

---

## 9. Weight-Laplacian error

Section 5 gives

\[
|\Delta w_N|
\le
C\frac{w_N}{r^2}
\le
\frac18\delta w_N
\]

in the far field.

The bounded-core part is controlled by the global enstrophy cap.

The genuine palinstrophy term

\[
-2\int w_N|\nabla W|^2
\]

has favorable sign and need not be used.

---

## 10. Differential inequality

Collecting the preceding estimates gives

\[
\boxed{
\frac d{d\theta}M_{w,N}
\le
-c
\int
\delta(\log(e+|y|))
\,w_N(y)
|W|^2dy
+C_w,
}
\]

where

\[
c>0,
\qquad
C_w<\infty
\]

are independent of `N`.

Unlike the power-subcritical case, the damping coefficient tends to zero at infinity, so this does **not** directly bound `M_w` itself.

This distinction is essential.

---

## 11. Invariant averaging

Average against the invariant hard measure.

The truncated derivative has zero mean, so

\[
\boxed{
\int
\left[
\int
\delta(\log(e+|y|))
w_N(y)|W_Y(y)|^2dy
\right]
d\nu(Y)
\le C.
}
\]

Let `N -> infinity` and use monotone convergence.

Define

\[
\boxed{
\widetilde w(r)
:=
\delta(\log(e+r))
w(r).
}
\]

Then

\[
\boxed{
\int_{\widehat{\mathfrak H}}
\left[
\int
\widetilde w(|y|)|W_Y(y)|^2dy
\right]
d\nu(Y)
<\infty.
}
\]

Hence

\[
\boxed{
\int
\widetilde w(|y|)|W_Y(y)|^2dy
<\infty
\quad\nu\text{-a.e.}
}
\]

---

## 12. The controlled weight is stronger than every power-subcritical weight

We have

\[
\widetilde w(r)
=
\delta(\log r)
r e^{-A(\log r)}.
\]

Because

\[
\delta(\rho)\ge\frac1{1+\rho},
\]

we have

\[
\log\delta(\rho)=o(\rho).
\]

Together with

\[
A(\rho)=o(\rho),
\]

this gives, for every `epsilon>0`,

\[
\boxed{
\frac{\widetilde w(r)}{r^{1-\epsilon}}
\to\infty.
}
\]

At the same time,

\[
\boxed{
\frac{\widetilde w(r)}r
=
\delta e^{-A}
\to0.
}
\]

Therefore

\[
\boxed{
r^{1-\epsilon}\ll\widetilde w(r)\ll r
\qquad
\forall\epsilon>0.
}
\]

The new finite moment is strictly stronger than every fixed power-subcritical moment from M5-536.

---

## 13. Endpoint interpretation

The hard component now satisfies

\[
\boxed{
\int\widetilde w(|y|)|W|^2dy<\infty
}
\]

for an adaptive almost-critical weight `w_tilde`, while

\[
\boxed{
\int |y||W|^2dy=\infty.
}
\]

Thus the gap to the true endpoint is no longer an arbitrary power.

It is a slowly varying defect determined by the actual far-field nonlinear modulus of the compact hull.

---

## 14. Firewall

The function `w_tilde` is not a universal logarithmic weight.

Its slowly varying factor depends on the actual decay modulus

\[
\varepsilon_{far}(R)
\]

of the hard hull.

Therefore M5-540 does not by itself place `U` in a standard Lorentz or Orlicz class covered by a known theorem.

It proves an adaptive near-endpoint improvement only.

---

## 15. Highest-value next target

Translate the adaptive weighted vorticity control into a corresponding **adaptive velocity endpoint** by a weighted Caffarelli--Kohn--Nirenberg/Hardy--Littlewood--Sobolev estimate.

The target is a scale-critical distribution bound stronger than the bare statement

\[
U\in\bigcap_{p>3}L^p
\]

but weaker than `L3`, with the slowly varying gauge explicitly inherited from `w_tilde`.

Then compare that gauge with known endpoint regularity/Liouville criteria.

---

## 16. Status

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
