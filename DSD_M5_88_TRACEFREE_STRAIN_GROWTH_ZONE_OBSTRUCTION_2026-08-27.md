# DSD M5-88 — Trace-Free Strain Growth-Zone Obstruction

Date: 2026-08-27

Status: **NEW POINTWISE INCOMPRESSIBILITY BOUND + AMPLITUDE LOCALIZATION / THE CROSSING VARIABLE `b` IS THE LONGITUDINAL TRACE-FREE STRAIN / A POSITIVE EXACT ENDPOINT MUST PLACE AN ORDER-ONE AMOUNT OF CROSSING INSIDE THE AMPLITUDE ZONE WHERE `a w(a) > (3/2) W_<(a)` / OUTSIDE THAT GROWTH ZONE THE BULK STRAIN COST ALREADY DOMINATES THE CROSSING CHANNEL / GLOBAL REGULARITY UNPROVED.**

## 1. Crossing is longitudinal strain

Let

\[
a:=|U|>0,
\qquad
e:=\frac Ua,
\]

and let

\[
S
:=
\frac12
\left(
\nabla U+(\nabla U)^T
\right)
\]

be the rate-of-strain tensor.

Since

\[
\partial_i a
=e_j\partial_iU_j,
\]

we have

\[
\begin{aligned}
b
&:=
U\cdot\nabla\log a\\
&=
\frac{U_i\partial_i a}{a}\\
&=
e_i e_j\partial_iU_j.
\end{aligned}
\]

The antisymmetric part of `grad U` vanishes under contraction with `e tensor e`. Therefore

\[
\boxed{
b=e^TSe.}
\]

Thus the M5 crossing variable is exactly the longitudinal normal strain measured along the velocity direction.

---

## 2. Trace-free matrix inequality in three dimensions

Incompressibility gives

\[
\operatorname{tr}S
=\nabla\cdot U
=0.
\]

Fix a unit vector `e` and prescribe

\[
e^TSe=b.
\]

Among all symmetric trace-free `3 x 3` matrices with this longitudinal entry, the Frobenius norm is minimized by

\[
\operatorname{diag}
\left(
b,-\frac b2,-\frac b2
\right)
\]

in a basis whose first vector is `e`.

Hence

\[
\boxed{
|S|^2
\ge
b^2+2\left(\frac b2\right)^2
=
\frac32 b^2.
}
\]

Because the symmetric and antisymmetric parts are orthogonal,

\[
|\nabla U|^2
=|S|^2+|\Omega|^2
\ge|S|^2.
\]

Therefore

\[
\boxed{
|\nabla U|^2
\ge
\frac32b^2.
}
\]

Equivalently,

\[
\boxed{
b^2\le\frac23|\nabla U|^2.}
\]

This is pointwise and uses only three-dimensional incompressibility.

---

## 3. Recall the M5 amplitude weights

Let

\[
w\ge0
\]

be the fixed mollifier and define its cumulative weight

\[
\boxed{
W_<(a)
:=
\int_0^a w(\lambda)d\lambda.
}
\]

M5-56 gives the bulk-gradient term

\[
\boxed{
A_w
=
\int W_<(a)|\nabla U|^2dY.
}
\]

M5-78 gives the crossing channel

\[
\boxed{
T
=
\int a\,w(a)b^2dY.
}
\]

The angular gap is

\[
G_w\ge0.
\]

---

## 4. Lower-bound the bulk cost by longitudinal strain

Apply the pointwise trace-free inequality inside `A_w`:

\[
\boxed{
A_w
\ge
\frac32
\int W_<(a)b^2dY.
}
\]

Therefore

\[
\begin{aligned}
T-A_w
&\le
\int
\left[
a w(a)
-\frac32W_<(a)
\right]
b^2dY.
\end{aligned}
\]

Define the amplitude growth function

\[
\boxed{
\chi_w(a)
:=
a w(a)-\frac32W_<(a).
}
\]

Then

\[
\boxed{
T-A_w
\le
\int\chi_w(a)b^2dY.
}
\]

---

## 5. Insert the exact positive endpoint identity

M5-71 gives at exact minimal-payer saturation

\[
X_w
=\nu(T-A_w-G_w).
\]

Hence

\[
\frac{X_w}{\nu}+G_w
=T-A_w.
\]

Combining with the previous inequality,

\[
\boxed{
\int\chi_w(a)b^2dY
\ge
\frac{X_w}{\nu}+G_w.
}
\]

On the robust returned upstroke,

\[
X_w\ge c_1>0,
\]

so

\[
\boxed{
\int\chi_w(a)b^2dY
\ge
\frac{c_1}{\nu}+G_w
>0.
}
\]

Thus the sign of `chi_w` becomes a genuine endpoint geometry condition.

---

## 6. Only the positive growth zone can pay

Define

\[
\boxed{
\mathcal Z_w
:=
\left\{
a>0:
\chi_w(a)>0
\right\}
=
\left\{
a>0:
 a w(a)>\frac32W_<(a)
\right\}.
}
\]

Since the negative part of `chi_w` can only reduce the full integral,

\[
\boxed{
\int
[\chi_w(a)]_+b^2dY
\ge
\frac{X_w}{\nu}+G_w.
}
\]

In particular, on every robust exact returned pump,

\[
\boxed{
\int_{a\in\mathcal Z_w}
\chi_w(a)b^2dY
\ge
\frac{c_1}{\nu}.
}
\]

Therefore an order-one amount of longitudinal crossing is forced into the growth zone `Z_w`.

The endpoint cannot distribute its crossing arbitrarily over the entire active amplitude band.

---

## 7. Logarithmic interpretation of the growth zone

Where

\[
W_<(a)>0,
\]

we have

\[
\frac{a w(a)}{W_<(a)}
=
\frac{d\log W_<}{d\log a}.
\]

Hence

\[
\boxed{
\mathcal Z_w
=
\left\{
\frac{d\log W_<}{d\log a}
>\frac32
\right\}.
}
\]

Thus positive endpoint pumping requires crossing in the part of amplitude space where the cumulative mollifier weight grows faster than the power law

\[
W_<\sim a^{3/2}.
\]

The exponent `3/2` is not chosen by hand. It is the sharp three-dimensional trace-free longitudinal-strain constant.

---

## 8. Immediate exclusion criterion for a weight

If one could choose an admissible positive-crossing weight satisfying

\[
\boxed{
 a w(a)
\le
\frac32W_<(a)
}
\]

throughout all amplitudes carrying the returned crossing, then

\[
\chi_w\le0
\]

there and the preceding positive lower bound would be impossible.

Hence such a weight would exclude the exact positive minimal-payer endpoint immediately.

For the current compactly supported mollifier away from zero, however, the cumulative weight begins at zero at the lower support edge. A smooth positive rise necessarily creates a region with

\[
\chi_w>0.
\]

Therefore the present M5-57 mollifier does not close the endpoint by this criterion alone.

---

## 9. What compact support forces

Suppose

\[
w\in C_c^\infty((0,\infty)),
\qquad
w\not\equiv0.
\]

Let `lambda_0>0` be the lower edge of its support.

Then

\[
W_<(\lambda_0)=0.
\]

As the weight rises from zero, the logarithmic growth rate of `W_<` must exceed any fixed finite power threshold somewhere arbitrarily near the rising edge.

Consequently

\[
\boxed{
\mathcal Z_w\ne\varnothing.
}
\]

The endpoint is therefore forced toward the lower rising flank of the amplitude mollifier.

This identifies a previously hidden dependence of the minimal-payer endpoint on the chosen amplitude averaging geometry.

---

## 10. A new route through weight design

The anchor first-hit difference

\[
E_{\lambda_c}(t_c)-E_{\lambda_c}(t_-)>0
\]

is continuous in `lambda`.

Hence there exists a positive amplitude neighborhood `J` of `lambda_c` on which the endpoint difference remains positive.

This gives some freedom to redesign `w` inside `J` while retaining a positive averaged pump.

The new target is to determine whether one can choose a family of admissible weights such that

1. the averaged pump remains quantitatively positive;
2. the growth zones `Z_w` become arbitrarily small or move through `J`;
3. W1 analytic compactness prevents the fixed order-one crossing required by
   \[
   \int_{Z_w}\chi_wb^2\ge c_1/\nu
   \]
   from following those shrinking/moving zones.

If so, the exact endpoint would be excluded without estimating pressure further.

---

## 11. DSD audit

### GREEN

`b=e^TSe` exactly.

### GREEN

Three-dimensional incompressibility gives the sharp pointwise inequality

\[
|\nabla U|^2\ge\frac32b^2.
\]

### GREEN

A positive exact endpoint forces an order-one amount of crossing into the amplitude growth zone `a w>(3/2)W_<`.

### GREEN

This condition is pressure free and component free.

### YELLOW

Every compactly supported positive mollifier has a nonempty growth zone near its lower rising edge, so one fixed current weight does not produce a contradiction.

### YELLOW

A multi-weight or moving-weight argument must preserve the robust positive pump while controlling how crossing can concentrate in amplitude.

### RED

No contradiction has yet been obtained from the growth-zone localization alone.

---

## 12. Next calculation

Quantify the maximum crossing that can fit into a narrow amplitude interval using W1 local analytic bounds and the coarea/volume geometry.

If for an interval `J_delta` of amplitude width `delta` one can prove

\[
\int_{a\in J_\delta}b^2dY
\le C\delta^\alpha
\]

with some `alpha>0` uniformly on the compact returned pump class, then a family of weights with shrinking growth zones would contradict the fixed lower requirement

\[
\int_{Z_w}\chi_wb^2dY
\ge c_1/\nu.
\]

The key technical issue is whether critical-level concentration can defeat such an amplitude-thickness estimate.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
