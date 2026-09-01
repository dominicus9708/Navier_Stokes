# DSD M5-506 — Bounded second derivative forces a uniform third-derivative bound

Date: 2026-09-01

Status: **THIRD-DERIVATIVE RICCATI ITERATION / M5-505 GIVES A UNIFORM `D_2=||grad^2 W||_2^2` CAP ON THE BOUNDED-P BRANCH / THE `m=3` SIMILARITY ENERGY IDENTITY HAS LINEAR COEFFICIENT `7/4` AND DISSIPATION `D_4` / AFTER THE HIGHEST TRANSPORT CANCELLATION, THE EDGE NONLINEAR TERMS ARE LINEAR IN `D_3` WITH COEFFICIENT CONTROLLED BY THE UNIFORM `H^2` NORM, WHILE THE MIDDLE TERMS ARE AT MOST `C D_2^(3/4) D_3^(3/4)` / LOG-CONVEXITY GIVES `D_4 >= D_3^2/D_2`, SO LARGE `D_3` EXPERIENCES A NEGATIVE QUADRATIC RICCATI DRIFT / COMPLETENESS OF THE SIMILARITY TRAJECTORY EXCLUDES CROSSING THE RESULTING FINITE BARRIER / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Input from M5-505

On the bounded-palinstrophy projected-diffusion corridor,

\[
E\le Z_*,
\qquad
P=D_1\le P_*,
\]

and M5-505 gives

\[
\boxed{
D_2
:=
\|\nabla^2W\|_2^2
\le H_*<\infty,
}
\]

where one may take

\[
H_*:=H_{crit}(Z_*,P_*).
\]

Define

\[
\boxed{
D_3=:K=\|\nabla^3W\|_2^2,
}
\]

and

\[
\boxed{
D_4=:L=\|\nabla^4W\|_2^2.
}
\]

---

## 2. Uniform `H^2` control of the low-order coefficients

The lower derivative caps imply

\[
\|W\|_{H^2}^2
\lesssim
Z_*+P_*+H_*.
\]

Hence, by Sobolev embedding in three dimensions,

\[
\boxed{
\|W\|_\infty
\le M_2,
}
\]

for a finite constant `M_2` depending only on the lower-order caps.

Since velocity gradients are Riesz transforms of vorticity,

\[
\|\nabla U\|_{H^2}
\lesssim
\|W\|_{H^2},
\]

and therefore

\[
\boxed{
\|\nabla U\|_\infty
\le C M_2.
}
\]

This is the coefficient control unavailable before M5-505.

---

## 3. General similarity coefficient at derivative order `m`

For an `m`th spatial derivative,

\[
\nabla^m(y\cdot\nabla W)
=
y\cdot\nabla\nabla^mW
+m\nabla^mW.
\]

Thus the dilation contribution to the `D_m` energy is

\[
\frac12
\left(-\frac32+m\right)D_m
=
\frac{2m-3}{4}D_m.
\]

Adding the explicit `+W` term gives

\[
\boxed{
\frac{2m+1}{4}D_m.
}
\]

For `m=3`, this equals

\[
\boxed{
\frac74K.
}
\]

---

## 4. Exact `m=3` energy identity

Apply three spatial derivatives to

\[
\partial_\theta W
+W
+\frac12y\cdot\nabla W
-\Delta W
=
\mathcal N,
\]

with

\[
\mathcal N
=(W\cdot\nabla)U-(U\cdot\nabla)W.
\]

Pair with `grad^3 W` in `L2`.

The diffusion term gives `D_4=L`.

Therefore

\[
\boxed{
\frac12K'
+\frac74K
+L
=
\mathcal N_3.
}
\]

---

## 5. Highest transport cancellation

In

\[
\nabla^3((U\cdot\nabla)W),
\]

the term

\[
U\cdot\nabla\nabla^3W
\]

has one apparent fourth derivative of `W`.

Its pairing with `grad^3 W` vanishes:

\[
\int
(U\cdot\nabla)\nabla^3W:
\nabla^3W\,dy
=0
\]

because

\[
\nabla\cdot U=0.
\]

After this cancellation, no nonlinear factor has derivative order greater than three on `W`.

---

## 6. Edge terms are linear in `K`

The edge Leibniz terms include the schematic products

\[
W\,\nabla^4U\,\nabla^3W
\]

and

\[
\nabla U\,\nabla^3W\,\nabla^3W.
\]

Biot--Savart/Calderon--Zygmund gains one derivative from `W` to `U`, so

\[
\|\nabla^4U\|_2
\lesssim
\|\nabla^3W\|_2
=K^{1/2}.
\]

Therefore

\[
\left|
\int
W\,\nabla^4U\,\nabla^3W
\right|
\lesssim
\|W\|_\infty K
\lesssim
M_2K.
\]

Likewise

\[
\left|
\int
\nabla U\,\nabla^3W\,\nabla^3W
\right|
\lesssim
\|\nabla U\|_\infty K
\lesssim
M_2K.
\]

Thus all edge terms are bounded by

\[
\boxed{
C M_2K.
}
\]

---

## 7. Middle terms are sublinear in `K`

The remaining terms are schematically of the form

\[
\nabla W\,\nabla^2W\,\nabla^3W.
\]

Use

\[
\|\nabla W\|_6
\lesssim
D_2^{1/2},
\]

and interpolation

\[
\|\nabla^2W\|_3
\lesssim
D_2^{1/4}D_3^{1/4}.
\]

Then

\[
\begin{aligned}
\left|
\int
\nabla W\,\nabla^2W\,\nabla^3W
\right|
&\lesssim
D_2^{1/2}
D_2^{1/4}D_3^{1/4}
D_3^{1/2}\\
&=
D_2^{3/4}D_3^{3/4}.
\end{aligned}
\]

Using `D_2<=H_*`,

\[
\boxed{
|I_{mid}|
\le
C H_*^{3/4}K^{3/4}.
}
\]

---

## 8. Audited third-derivative inequality

Combining edge and middle terms,

\[
\boxed{
\frac12K'
+\frac74K
+L
\le
A_3K
+B_3K^{3/4},
}
\]

where

\[
A_3:=CM_2<\infty,
\]

and

\[
B_3:=CH_*^{3/4}<\infty.
\]

No `D_4` term remains on the nonlinear side.

---

## 9. Log-convexity supplies quadratic damping

The Fourier moments satisfy

\[
D_3^2
\le
D_2D_4.
\]

Hence, whenever `K>0`,

\[
\boxed{
L=D_4
\ge
\frac{K^2}{D_2}
\ge
\frac{K^2}{H_*}.
}
\]

Dropping the favorable linear damping `7K/4` gives the simpler inequality

\[
\boxed{
\frac12K'
\le
-\frac{K^2}{H_*}
+A_3K
+B_3K^{3/4}.
}
\]

The negative term is quadratic, while the nonlinear positive terms have powers `1` and `3/4`.

---

## 10. Explicit large-`K` barrier

Choose

\[
\boxed{
K_{crit}
:=
\max\left\{
4A_3H_*,
\left(4B_3H_*\right)^{4/5}
\right\}.
}
\]

If

\[
K\ge K_{crit},
\]

then

\[
A_3K
\le
\frac{K^2}{4H_*},
\]

and

\[
B_3K^{3/4}
\le
\frac{K^2}{4H_*}.
\]

Therefore

\[
\frac12K'
\le
-\frac{K^2}{2H_*},
\]

or

\[
\boxed{
K'
\le
-\frac{K^2}{H_*}.
}
\]

above the barrier.

---

## 11. Completeness excludes barrier crossing

The similarity trajectory exists for every

\[
\theta\in\mathbb R.
\]

Suppose

\[
K(\theta_0)>K_{crit}.
\]

While `K>K_crit`, the preceding inequality makes `K` strictly decrease forward in `theta`; therefore it is at least `K(theta_0)` when followed backward.

Integrating

\[
\left(\frac1K\right)'
=-\frac{K'}{K^2}
\ge
\frac1{H_*}
\]

backward produces a finite-time contradiction with positivity and finiteness of `K` on the complete smooth trajectory.

Hence

\[
\boxed{
D_3(\theta)=K(\theta)
\le
K_{crit}<\infty
\quad
\forall\theta\in\mathbb R.
}
\]

---

## 12. Consequence

M5-505 excluded

\[
D_1\text{ bounded},
\qquad
D_2\text{ unbounded}.
\]

M5-506 now excludes

\[
D_1,D_2\text{ bounded},
\qquad
D_3\text{ unbounded}.
\]

Thus the bounded-palinstrophy branch has climbed one full derivative level without generating a new escape channel.

---

## 13. DSD audit

The key structural reason is the one-derivative smoothing relation between velocity and vorticity:

\[
\nabla U
\sim
\mathcal R W.
\]

After transport cancellation, differentiating the vorticity equation to order `m` does not create a nonlinear `W` derivative higher than order `m`.

At `m=3`, the already-established `H^2` cap is enough to put the edge coefficients in `L-infinity`, and the remaining split derivative term is strictly subquadratic relative to the log-convex dissipative barrier.

This is an internal derivative-hierarchy statement, not a terminal regularity theorem.

---

## 14. Highest-value next target

For `m>=4`, all proper Leibniz splits have both derivative factors below order `m`.

Because the induction hypothesis would give a uniform `H^{m-1}` cap with `m-1>3/2`, Sobolev multiplication should control those proper splits by lower-order constants, while the two edge terms remain linear in `D_m`.

Combined with

\[
D_{m+1}
\ge
\frac{D_m^2}{D_{m-1}},
\]

this suggests an induction:

\[
\boxed{
D_1\text{ bounded}
\Longrightarrow
D_m\text{ bounded for every fixed }m.
}
\]

The next step is to audit that induction without hiding derivative loss in the product estimate.

---

## 15. Status

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
