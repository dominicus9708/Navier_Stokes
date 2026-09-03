# DSD M5-638 — Zero-kappa level-surface normal dynamics and neighboring-level spacing recover the 3/2 material-volume law

Date: 2026-09-03

Status: **INTERNAL RELABELING-SURFACE GEOMETRY / ON THE RELABELING ZERO-LEVEL BRANCH `D_B kappa=f(kappa,theta)` WITH `f(0,theta)=0`, A REGULAR ZERO-KAPPA LEVEL SURFACE IS MATERIAL. ITS NORMAL GRADIENT OBEYS `D_B log|grad kappa| = f_kappa(0,theta)-sigma_n-1/2`, ITS MATERIAL AREA ELEMENT OBEYS `D_B log dA_0 = 1-sigma_n`, AND THE NORMAL SPACING TO A NEIGHBORING KAPPA LEVEL OBEYS `D_B log d_perp = sigma_n+1/2`. THEREFORE `dA_0 d_perp` EXPANDS EXACTLY AT RATE `3/2`. THE ZERO-LEVEL SHEATH PROBLEM IS THUS ANOTHER EXACT FORM OF MATERIAL-VOLUME EXPANSION: A PERSISTENT ZERO-LEVEL SURFACE CAN SURVIVE, BUT A FIXED POSITIVE-THICKNESS MATERIAL SHEATH AROUND IT CANNOT REMAIN BOUNDED WITHOUT LABEL TURNOVER. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Relabeling zero-level branch

Assume

\[
D_B\kappa=f(\kappa,\theta)
\]

and the synchronized persistent level is

\[
\boxed{\kappa=0.}
\]

For zero to remain a level history,

\[
\boxed{f(0,\theta)=0.}
\]

At regular points of the zero level, let

\[
n:=\frac{\nabla\kappa}{|\nabla\kappa|}.
\]

Since `W·grad kappa=0`, the vortex-line direction is tangent to the zero-kappa surface.

---

## 2. Gradient transport

For any scalar `kappa`,

\[
D_B\nabla\kappa
=\nabla(D_B\kappa)-(\nabla B)^T\nabla\kappa.
\]

On the relabeling branch,

\[
\nabla(D_B\kappa)
=f_\kappa(\kappa,\theta)\nabla\kappa.
\]

Hence on `kappa=0`,

\[
D_B\nabla\kappa
=f_\kappa(0,\theta)\nabla\kappa
-(\nabla B)^T\nabla\kappa.
\]

Taking the logarithmic norm gives

\[
D_B\log|\nabla\kappa|
=f_\kappa(0,\theta)-n\cdot(\nabla B)n.
\]

Because

\[
\nabla B=\nabla U+\frac12I
\]

and the antisymmetric part vanishes in the quadratic form,

\[
n\cdot(\nabla B)n
=n\cdot\Sigma n+\frac12.
\]

Define

\[
\sigma_n:=n\cdot\Sigma n.
\]

Then

\[
\boxed{
D_B\log|\nabla\kappa|
=f_\kappa(0,\theta)-\sigma_n-\frac12.
}
\]

---

## 3. Material zero-level surface area

A material surface area element with unit normal `n` obeys

\[
D_B\log dA
=\nabla\cdot B-n\cdot(\nabla B)n.
\]

Since

\[
\nabla\cdot B=\frac32,
\]

we get

\[
\boxed{
D_B\log dA_0
=1-\sigma_n.
}
\]

Thus bounded recurrent zero-level surface area would force mean normal strain `sigma_n=1` on that specific material surface patch.

---

## 4. Neighboring level spacing

Consider a nearby relabeling level separation `delta kappa`.

Linearizing the scalar ODE around zero,

\[
D_B(\delta\kappa)
=f_\kappa(0,\theta)\delta\kappa.
\]

At regular points, its physical normal spacing is infinitesimally

\[
d_\perp\sim\frac{|\delta\kappa|}{|\nabla\kappa|}.
\]

Therefore

\[
D_B\log d_\perp
=f_\kappa(0,\theta)
-\left[f_\kappa(0,\theta)-\sigma_n-\frac12\right],
\]

so

\[
\boxed{
D_B\log d_\perp
=\sigma_n+\frac12.
}
\]

The scalar relabeling exponent cancels from the physical spacing law.

---

## 5. Exact sheath-volume law

Multiply the material surface area by the neighboring-level normal thickness:

\[
dV_{sheath}\sim dA_0\,d_\perp.
\]

Then

\[
D_B\log dV_{sheath}
=(1-\sigma_n)+(\sigma_n+\tfrac12)
=\frac32.
\]

Hence

\[
\boxed{
D_B\log(dA_0d_\perp)=\frac32.
}
\]

This exactly reproduces the global material-volume expansion law.

---

## 6. Interpretation

The zero-kappa level itself is a lower-dimensional material object and can in principle remain part of the persistent flux skeleton.

But any positive-thickness material neighborhood formed by neighboring kappa levels expands exponentially in similarity volume.

Therefore a fixed bounded Eulerian sheath around a persistent zero-level surface cannot be composed of the same material level labels forever.

One must have

\[
\boxed{
\text{persistent zero-level surface}
+
\text{cross-level material sheath turnover}.
}
\]

This is the kappa-level version of M5-633.

---

## 7. Relation to transverse-magnitude geometry

M5-637 sends the remaining non-Beltrami charge away from the first-order-flat zero-level maximum and toward its surrounding sheath/turnover population.

M5-638 now shows that such a sheath is necessarily material-throughflow rather than a fixed thick material tube.

Thus the transverse-magnitude channel from M5-622 should be studied on a **renewing Eulerian sheath around a persistent material kappa surface**, not on one recurrent positive-volume material parcel.

---

## 8. Firewall

The formula for `d_perp` is a regular-level, infinitesimal neighboring-level calculation. It does not apply across critical points where `grad kappa=0` without a separate singular-level analysis.

No contradiction is claimed from the `3/2` expansion; it is used only to classify the required turnover geometry.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]