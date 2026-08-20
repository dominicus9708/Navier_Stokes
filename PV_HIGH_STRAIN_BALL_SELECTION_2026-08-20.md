# Quantitative High-Strain Ball Selection — 2026-08-20

Overall status: **GLOBAL PRODUCTION TO LOCAL COMPATIBILITY SELECTION LEMMA — GLOBAL REGULARITY NOT PROVED.**

This note closes the derivative-energy occupancy gap left by `PV_HALF_AMPLITUDE_BALL_SHAPE_BOUND_2026-08-20.md` up to the already isolated annulus/spectral branches.

The inputs are only a strain `L2` bound, a strain Lipschitz bound, and the recurrent H1 production ratio.

---

## 1. A direct L2-Lipschitz upper bound for strain amplitude

Let

\[
E=\|S\|_2^2,
\qquad
L=\|\nabla S\|_\infty,
\qquad
B=\|S\|_\infty.
\]

Choose `x_*` with `|S(x_*)|=B`. On

\[
r=\frac{B}{2L},
\]

Lipschitz continuity gives

\[
|S|\ge\frac B2.
\]

Therefore

\[
E
\ge
\frac{B^2}{4}
\frac{4\pi}{3}
\left(\frac{B}{2L}\right)^3
=
\frac\pi{24}\frac{B^5}{L^3}.
\]

Hence

\[
\boxed{
B
\le
B_*
:=
\left(\frac{24}{\pi}EL^3\right)^{1/5}.
}
\]

This converts the abstract compact-class amplitude ceiling into explicit `L2 + analyticity/Lipschitz` data.

---

## 2. Production forces a high-strain derivative-energy set

Let

\[
P=\|\nabla S\|_2^2,
\qquad
q=N/P>0,
\qquad
C_H=4/\sqrt6.
\]

From the sharp H1 bound,

\[
\frac1P\int |S||\nabla S|^2dx
\ge
\frac q{C_H}.
\]

Define

\[
\boxed{
\beta_*
:=
\frac{q}{C_HB_*}.
}
\]

If `beta_* > 1`, the static bound is already contradicted. Therefore a surviving branch has

\[
0<\beta_*\le1.
\]

Set the absolute high-strain threshold

\[
\boxed{
\sigma
=\frac{q}{2C_H}
=\frac{\beta_*B_*}{2}.
}
\]

Let

\[
E_\sigma=\{|S|\ge\sigma\}.
\]

Using `B <= B_*`, the derivative-energy occupancy satisfies

\[
\boxed{
\frac{\int_{E_\sigma}|\nabla S|^2}{P}
\ge
\frac{\beta_*}{2-\beta_*}.
}
\]

---

## 3. Cover the high-strain set by uniform balls

Set

\[
\boxed{
r=\frac{\sigma}{2L}.}
\]

Choose a maximal disjoint family of balls

\[
B_{r/2}(x_i),
\qquad x_i\in E_\sigma.
\]

Maximality implies the doubled balls `B_r(x_i)` cover `E_sigma`.

On every small disjoint ball,

\[
|S(x)|
\ge
\sigma-L\frac r2
=\frac{3\sigma}{4}.
\]

Thus each such ball contributes at least

\[
\left(\frac{3\sigma}{4}\right)^2
\frac{4\pi}{3}
\left(\frac{r}{2}\right)^3
=
\boxed{
\frac{3\pi}{256}
\frac{\sigma^5}{L^3}
}
\]

to `E=||S||_2^2`.

Therefore the number of selected balls satisfies

\[
N_{ball}
\le
\frac{256EL^3}{3\pi\sigma^5}.
\]

Using

\[
B_*^5=\frac{24}{\pi}EL^3,
\qquad
\sigma=\frac{\beta_*B_*}{2},
\]

this becomes the universal bound

\[
\boxed{
N_{ball}
\le
\frac{1024}{9\beta_*^5}.
}
\]

All explicit dependence on `E` and `L` has cancelled from the covering number once it is expressed through `beta_*`.

---

## 4. One selected ball carries a definite fraction of total derivative energy

Because the balls `B_r(x_i)` cover the high-strain set,

\[
\sum_i
\int_{B_r(x_i)}|\nabla S|^2
\ge
\int_{E_\sigma}|\nabla S|^2.
\]

Hence at least one selected ball, call it `B_r(x_c)`, satisfies

\[
\boxed{
\frac{P_r}{P}
\ge
\alpha_*
:=
\frac{9\beta_*^6}
{1024(2-\beta_*)}.
}
\]

Here

\[
P_r=\|\nabla S\|_{L^2(B_r(x_c))}^2.
\]

Thus recurrent global H1 production produces at least one quantitative high-strain derivative-active core ball.

---

## 5. The selected ball automatically has universal compatibility shape

Since the center lies in `E_sigma`, on the selected ball

\[
|S|
\ge
\sigma-Lr
=\frac\sigma2.
\]

If the positive-middle sector persists throughout the ball, then

\[
g=s_2-s_1
\ge
\frac{|S|}{\sqrt2}
\ge
\boxed{
\frac\sigma{2\sqrt2}.
}
\]

Also

\[
P_\infty\le L^2.
\]

Therefore

\[
\chi
=\frac{r^2P_\infty}{g_-^2}
\le
\frac{(\sigma/2L)^2L^2}{\sigma^2/8}
=2.
\]

Hence

\[
\boxed{\chi\le2}
\]

on the selected ball, exactly as in the half-amplitude construction.

---

## 6. Insert localized compatibility

Let

\[
e=\mathcal E_A(r)
\]

be the annular compatibility leakage of the selected ball.

### Leakage branch

If

\[
\boxed{e\ge\frac16,}
\]

the ball already carries the definite annular derivative/material leakage required by the `H/T` branch.

### Compatible coherent branch

If

\[
0\le e<\frac16,
\]

then, since `chi <= 2`,

\[
\boxed{
\delta_{cov}(e)
\ge
\left[
\sqrt{
\frac{72}{\pi^2}
+
\frac19-rac23e
}
-
\sqrt{
\frac{72}{\pi^2}
}
\right]^2.
}
\]

The local covariance tax is

\[
3g_-\delta_{cov}P_r.
\]

Using

\[
g_-\ge\frac\sigma{2\sqrt2}
=\frac{q}{4\sqrt2C_H}
\]

and

\[
P_r\ge\alpha_*P,
\]

we obtain the whole-profile lower bound on the selected compatibility tax

\[
\boxed{
T_{comp}
\ge
qP\,
\frac{3\sqrt3}{16}
\delta_{cov}(e)
\alpha_*.
}
\]

Here

\[
\alpha_*
=\frac{9\beta_*^6}{1024(2-\beta_*)}.
\]

Thus the compatibility tax is now an explicit fraction of the actual H1 production scale `qP`, expressed only through `beta_*` and the annular error `e`.

---

## 7. Spectral-transition branch

The argument above assumes the positive-middle sector persists throughout the selected high-strain ball.

If it fails while

\[
|S|\ge\sigma/2,
\]

then the strain undergoes an order-one spectral transition at a fixed positive amplitude. This leaves the coherent max-mid sector and enters the middle-zero/non-normality branch quantified by

\[
\Theta_{st}(x),
\qquad
\Theta_{NN}(x),
\qquad
1-\Theta_*\approx0.02337289.
\]

Thus the selected ball always enters one of:

\[
\boxed{
\text{annular leakage }H/T,
}
\]

\[
\boxed{
\text{positive-middle coherent ball with explicit compatibility tax},
}
\]

or

\[
\boxed{
\text{high-amplitude spectral-transition/non-normality branch}.
}
\]

---

## 8. Compact recurrent class

At a Leray recovery/checkpoint time,

\[
q
\ge
q_-:=\frac34+\frac\nu{\kappa_K^+}.
\]

If the class has

\[
E\le E_+,
\qquad
L\le L_+,
\]

then

\[
\boxed{
B_*
\le
\left(
\frac{24}{\pi}E_+L_+^3
\right)^{1/5}
}
\]

and consequently

\[
\boxed{
\beta_*
\ge
\beta_K
:=
\frac{q_-}
{C_H(24E_+L_+^3/\pi)^{1/5}}.
}
\]

If `beta_K > 1`, recurrent survival is impossible already by the static H1 bound. Otherwise the selected-ball occupancy and compatibility tax are uniformly positive functions of `beta_K` and the non-T annular leakage bound.

---

## 9. What remains

The positive-middle coherent branch no longer lacks a derivative-energy occupancy estimate. It now has an explicit selected-ball fraction

\[
\alpha_K
\ge
\frac{9\beta_K^6}{1024(2-\beta_K)}.
\]

The remaining class inputs are reduced to:

\[
E_+,
\qquad
L_+,
\qquad
\kappa_K^+,
\qquad
e_T<1/6.
\]

The first-hitting analyticity/compactness bridge supplies finite `E_+` and `L_+`; the next numerical task is to make those bounds explicit enough to test whether the compatibility-taxed ceiling falls below the Leray recurrence requirement.

Status: **GLOBAL RECURRENT H1 PRODUCTION NOW SELECTS A QUANTITATIVE HIGH-STRAIN DERIVATIVE-ACTIVE BALL. IF THAT BALL DOES NOT LEAK THROUGH ITS ANNULUS AND DOES NOT UNDERGO A HIGH-AMPLITUDE SPECTRAL TRANSITION, IT PAYS AN EXPLICIT COMPATIBILITY TAX THAT IS A POSITIVE FRACTION OF THE TOTAL PRODUCTION SCALE.**