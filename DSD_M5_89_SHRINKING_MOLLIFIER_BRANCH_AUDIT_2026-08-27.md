# DSD M5-89 — Shrinking-Mollifier Branch Audit

Date: 2026-08-27

Status: **FALSE CLOSURE ROUTE PRUNED / UNWEIGHTED CROSSING MASS IN A THIN AMPLITUDE SLAB DOES VANISH, BUT THE NORMALIZED MOLLIFIER GROWS LIKE `1/delta`; AT A REGULAR CROSSING LEVEL THE M5-88 GROWTH-ZONE INTEGRAL CONVERGES TO A FINITE NONZERO COAREA DENSITY RATHER THAN ZERO / SHRINKING THE WEIGHT ALONE CANNOT EXCLUDE THE ENDPOINT / GLOBAL REGULARITY UNPROVED.**

## 1. Question left by M5-88

M5-88 showed that a robust exact positive endpoint requires

\[
\int
[\chi_w(a)]_+
b^2dY
\ge
\frac{c_1}{\nu},
\]

where

\[
\chi_w(a)
=
a w(a)-\frac32W_<(a).
\]

A tempting strategy is to choose a sequence of mollifiers whose positive growth zones shrink to one amplitude value and argue that a vanishingly thin amplitude slab cannot carry an order-one crossing requirement.

This argument is not valid in that form.

---

## 2. Standard shrinking amplitude mollifier

Take

\[
w_\delta(a)
=
\frac1\delta
w_0\left(
\frac{a-\lambda_c}{\delta}
\right),
\]

where `w0` is smooth, nonnegative, compactly supported, and normalized.

Then the cumulative function has the form

\[
W_{\delta,<}(a)
=
W_{0,<}\left(
\frac{a-\lambda_c}{\delta}
\right)
\]

within the translated support convention.

Therefore

\[
\boxed{
\chi_\delta(a)
=
\frac a\delta
w_0\left(
\frac{a-\lambda_c}{\delta}
\right)
-
\frac32
W_{0,<}\left(
\frac{a-\lambda_c}{\delta}
\right).
}
\]

On the rising part of the mollifier the leading positive term has size

\[
O(\delta^{-1}).
\]

Thus shrinking support is accompanied by increasing amplitude weight.

---

## 3. Unweighted slab crossing does vanish

Fix the compact W1 pump class from M5-85.

Let

\[
J_\delta
=
[\lambda_c-C\delta,\lambda_c+C\delta].
\]

For any fixed smooth state,

\[
\int_{a\in J_\delta}b^2dY
\to
\int_{a=\lambda_c}b^2dY
\]

in the volume-measure sense.

The exact level set has zero three-dimensional measure unless it contains a plateau.

If a level set contains a positive-volume plateau, then

\[
\nabla a=0
\]

almost everywhere on that plateau and therefore

\[
b=0
\]

there.

Hence

\[
\boxed{
\int_{a\in J_\delta}b^2dY
\to0.
}
\]

By compactness of the returned local analytic class, the same vanishing can be made uniform after the standard contradiction/subsequence argument.

This statement alone, however, is too weak for M5-88.

---

## 4. Generic regular-level rate is linear, not superlinear

Assume `lambda_c` is a regular value for the limiting state.

Coarea gives

\[
\int_{a\in J_\delta}b^2dY
=
\int_{J_\delta}
\left[
\int_{a=\lambda}
\frac{b^2}{|\nabla a|}dS
\right]d\lambda.
\]

Define the crossing density

\[
\boxed{
H_b(\lambda)
:=
\int_{a=\lambda}
\frac{b^2}{|\nabla a|}dS.
}
\]

At a smooth regular level, `H_b(lambda)` is locally finite and, under a persistent regular foliation, continuous.

Therefore generically

\[
\boxed{
\int_{a\in J_\delta}b^2dY
=
O(\delta),
}
\]

with leading coefficient proportional to `H_b(lambda_c)`.

There is no reason for an `o(delta)` or `O(delta^{1+epsilon})` gain when the level carries genuine crossing.

---

## 5. The mollifier normalization cancels the slab width

Consider the leading weighted term

\[
I_\delta
:=
\int
\frac a\delta
w_0\left(
\frac{a-\lambda_c}{\delta}
\right)b^2dY.
\]

Using coarea,

\[
I_\delta
=
\int
\frac\lambda\delta
w_0\left(
\frac{\lambda-\lambda_c}{\delta}
\right)
H_b(\lambda)d\lambda.
\]

Set

\[
z=\frac{\lambda-\lambda_c}{\delta}.
\]

Then

\[
\boxed{
I_\delta
=
\int
(\lambda_c+\delta z)
 w_0(z)
 H_b(\lambda_c+\delta z)
 dz.
}
\]

At a regular crossing level,

\[
H_b(\lambda_c)>0,
\]

and therefore

\[
\boxed{
I_\delta
\to
\lambda_c H_b(\lambda_c)
\int w_0(z)dz
=
\lambda_c H_b(\lambda_c).
}
\]

Thus the `1/delta` normalization exactly compensates for the `O(delta)` thickness of the amplitude slab.

---

## 6. Consequence for the M5-88 growth-zone term

The cumulative term

\[
\frac32W_{\delta,<}
\]

has order one rather than `1/delta`.

Its contribution over a slab of width `O(delta)` tends to zero at a regular level.

Therefore the leading behavior of the positive growth-zone integral is controlled by the approximate-identity term above.

Schematically,

\[
\boxed{
\int
[\chi_\delta(a)]_+b^2dY
\not\to0
}
\]

when the limiting regular amplitude level carries nonzero crossing density.

It can converge to a finite positive levelwise crossing quantity.

Hence merely shrinking `Z_w` does not contradict the fixed M5-88 lower bound.

---

## 7. What would actually be needed

To make the shrinking-mollifier strategy work, one would need a superlinear slab estimate

\[
\boxed{
\int_{a\in J_\delta}b^2dY
=o(\delta)
}
\]

uniformly at the selected amplitude.

But at a regular level this is essentially equivalent to

\[
H_b(\lambda_c)=0,
\]

which means the selected level has no crossing density.

That is incompatible with using the same level as the carrier of the robust positive crossing unless another mechanism first forces `H_b=0`.

Thus the desired superlinear estimate cannot be assumed as a generic consequence of analyticity or compactness.

---

## 8. Critical levels are not the main obstruction here

M5-88 suggested that critical-level concentration might defeat a thin-band estimate.

The present audit shows a stronger point:

Even at a perfectly regular, smooth, transverse level, the normalized mollifier has exactly the scaling needed to retain a finite crossing contribution as `delta->0`.

Therefore the failure of the shrinking-weight closure is **not** merely a critical-level pathology.

It is built into the natural coarea scaling of the problem.

---

## 9. What survives from M5-88

M5-88 remains useful.

For a fixed admissible mollifier it says that an exact positive endpoint must satisfy

\[
\boxed{
\int_{\mathcal Z_w}
\chi_w(a)b^2dY
\ge
\frac{c_1}{\nu}.
}
\]

Thus crossing is forced into a specific amplitude-growth region determined by the weight.

What is rejected is only the naive inference

\[
\text{make }\mathcal Z_w\text{ thin}
\Longrightarrow
\text{its weighted crossing tends to zero}.
\]

That implication is false at the critical coarea scaling.

---

## 10. Updated viable routes

After this pruning, the promising uses of the trace-free inequality are:

1. derive a **weight-independent** geometric inequality relating crossing density to zero-flux reconnection cost;
2. exploit several fixed weights together with recurrence, rather than a single weight whose width tends to zero;
3. combine the longitudinal strain identity
   \[
   b=e^TSe
   \]
   with vorticity/strain evolution on the exact endpoint;
4. seek a quantitative global constraint from componentwise zero flux that rules out the source/sink-like local model identified in M5-87.

The fourth route most directly addresses the actual missing global condition.

---

## 11. DSD audit

### GREEN

Unweighted crossing mass in a shrinking amplitude slab vanishes.

### GREEN

At a regular crossing level it vanishes generically at exactly linear order in slab width.

### GREEN

The normalized mollifier grows at reciprocal order and therefore retains a finite levelwise crossing contribution.

### GREEN

Shrinking the amplitude weight alone cannot close the positive endpoint.

### RED

Do not assume an `o(delta)` crossing slab bound from W1 analyticity; it would already encode vanishing regular-level crossing.

---

## 12. Next calculation

Return to the global zero-flux condition absent from the punctured radial model.

Use

\[
b=e^TSe
\]

and the exact componentwise identity

\[
\int_{\partial\Omega_{\lambda,k}}U\cdot n\,dS=0
\]

to quantify how positive and negative longitudinal crossing must reconnect inside a globally smooth component.

The relevant target is no longer an amplitude-thickness estimate but a **sign-reconnection / strain-rotation cost** that can be compared with `A_w+G_w`.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
