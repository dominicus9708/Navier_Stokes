# DSD M17-209 — Positive unbounded kappa forces intrinsic-scale amplitude growth or kappa-gradient concentration

Date: 2026-09-06  
Canonical ID: **M17-209**

Status: **POSITIVE-KAPPA INTRINSIC-SCALE GATE / CE-H IMPLIES `(1/2) Delta rho^2 = |grad W|^2 + kappa rho^2`. IF `kappa(x0)=K>0` AND KAPPA STAYS ABOVE `K/2` ON AN INTRINSIC BALL OF RADIUS `L/sqrt(K)`, THE SPHERICAL MEAN OF `rho^2` OBEYS A RADIAL DIFFERENTIAL INEQUALITY AND MUST GROW BY THE FACTOR `sinh(L)/L`. THEREFORE A RELATIVE-THICK/NEAR-PEAK PACKET THAT CANNOT SUPPORT THIS AMPLITUDE GROWTH MUST DROP KAPPA BY ORDER `K` WITHIN DISTANCE `O(K^-1/2)`, FORCING `|grad kappa| >= c K^(3/2)`. POSITIVE-KAPPA BLOWUP IS THUS NOT A FREE BOUNDED-PACKET EXIT: IT ROUTES TO AMPLITUDE THINNESS/GROWTH OR MULTIPLIER-GRADIENT CONCENTRATION. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Scalar amplitude identity

On CE-H,

\[
\Delta W=\kappa W.
\]

Let

\[
f:=|W|^2=\rho^2.
\]

Then

\[
\frac12\Delta f
=|\nabla W|^2+W\cdot\Delta W
=|\nabla W|^2+\kappa f.
\]

Hence

\[
\boxed{
\Delta f
=2|\nabla W|^2+2\kappa f
\ge2\kappa f.
}
\]

At an interior local maximum of `f`, this immediately implies

\[
\boxed{
\kappa\le-\frac{|\nabla W|^2}{\rho^2}\le0.
}
\]

Thus strictly positive kappa cannot occur at an interior amplitude maximum.

---

## 2. Positive-kappa persistence ball

Suppose

\[
\boxed{\kappa(x_0)=K>0.}
\]

Fix `L>0` and set the intrinsic radius

\[
\boxed{r_K:=\frac{L}{\sqrt K}.}
\]

Assume first that

\[
\boxed{
\kappa(x)\ge\frac K2
\qquad\forall x\in B_{r_K}(x_0).
}
\]

Then throughout the ball

\[
\boxed{\Delta f\ge K f.}
\]

---

## 3. Spherical-mean growth

Let

\[
m(r):=\fint_{\partial B_r(x_0)}f\,dS.
\]

The spherical-mean identity gives

\[
m''(r)+\frac2r m'(r)
=\fint_{\partial B_r}\Delta f\,dS
\ge K m(r),
\]

with

\[
m(0)=f(x_0),\qquad m'(0)=0.
\]

The radial equality solution

\[
y''+\frac2r y'=Ky,
\qquad y(0)=f(x_0),\ y'(0)=0
\]

is

\[
y(r)=f(x_0)\frac{\sinh(\sqrt K r)}{\sqrt K r}.
\]

Standard ODE comparison therefore yields

\[
\boxed{
m(r)\ge f(x_0)\frac{\sinh(\sqrt K r)}{\sqrt K r}.}
\]

At the intrinsic radius,

\[
\boxed{
m(r_K)\ge f(x_0)\frac{\sinh L}{L}.}
\]

Consequently

\[
\boxed{
\sup_{B_{r_K}(x_0)}\rho^2
\ge
\frac{\sinh L}{L}\rho(x_0)^2.
}
\]

---

## 4. Gradient alternative

If the persistence condition fails, there exists

\[
x_1\in B_{r_K}(x_0)
\]

with

\[
\kappa(x_1)<\frac K2.
\]

By the mean-value theorem along a segment joining `x0` and `x1`,

\[
\sup_{B_{r_K}(x_0)}|\nabla\kappa|
\ge
\frac{K/2}{r_K}
=\frac1{2L}K^{3/2}.
\]

Therefore

\[
\boxed{
\kappa(x_0)=K>0
\Longrightarrow
\left[
\sup_{B_{L/\sqrt K}}\rho^2
\ge\frac{\sinh L}{L}\rho(x_0)^2
\right]
\lor
\left[
\sup_{B_{L/\sqrt K}}|\nabla\kappa|
\ge\frac{K^{3/2}}{2L}
\right].
}
\]

---

## 5. Relative-thick / near-peak consequence

Suppose the marked high-kappa point lies in a packet class satisfying a local peak-comparability bound

\[
\boxed{
\sup_{B_{L/\sqrt K}(x_0)}\rho^2
\le C_{amp}\rho(x_0)^2.
}
\]

Choose `L` so that

\[
\frac{\sinh L}{L}>C_{amp}.
\]

Then the amplitude-growth alternative is impossible, and hence

\[
\boxed{
\sup_{B_{L/\sqrt K}(x_0)}|\nabla\kappa|
\ge c(C_{amp})K^{3/2}.
}
\]

Thus positive unbounded kappa on an amplitude-comparable packet necessarily creates multiplier-gradient concentration at the natural elliptic scale `K^-1/2`.

---

## 6. Relation to existing M17/M5 charges

The M5-687 positive diffusion density is

\[
\rho^2|\nabla\kappa|^2.
\]

M17-209 gives a pointwise/intrinsic-scale mechanism capable of making this density large when positive kappa is large and the amplitude is not simultaneously becoming relatively thin.

However, converting the pointwise lower bound into a fixed integrated `D_kappa` cost requires a thickness/regularity estimate for the high-gradient set. That step is not silently assumed.

Thus the valid split is

\[
\boxed{
G_{\kappa,+\infty}
\Longrightarrow
G_{amplitude\ growth/thin}
\lor
G_{\nabla\kappa\ concentration}.
}
\]

---

## 7. DSD audit

- The spherical-mean argument uses only the scalar identity for `rho^2`; no scalar maximum principle is incorrectly applied to a vector component.
- The `K^(3/2)` gradient lower bound is a supremum statement; no positive-volume lower bound is claimed without an additional thickness theorem.
- Positive kappa is excluded only at interior amplitude maxima, not everywhere in a packet.
- Global regularity remains unproved.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
