# Threshold-perimeter selection from palinstrophy

Date: 2026-08-13

Status: **DERIVED COAREA / PALINSTROPHY SELECTION LEMMA**.

A fragmented material-pruning core may try to avoid a controlled material-surface flux argument by developing a very complicated threshold boundary.  This note shows that one can choose a threshold with controlled perimeter unless the local palinstrophy is already critically large.

---

## 1. Axial vorticity threshold band

Fix a constant unit axis `n` on a local ball

\[
B_r=B_r(x_0)
\]

and define

\[
\alpha=n\cdot\omega.
\]

Let

\[
W=\|\omega\|_\infty
\]

and choose fixed constants

\[
0<b_1<b_2<1.
\]

Consider the positive oriented threshold band

\[
\boxed{
 b_1W<h<b_2W.
}
\]

For almost every `h`, the superlevel set

\[
C_h=\{x\in B_r:\alpha(x)>h\}
\]

has a regular/BV relative boundary whose interior level-surface area is

\[
P_h
=\mathcal H^2(B_r\cap\{\alpha=h\}).
\]

---

## 2. Coarea identity

The coarea formula gives

\[
\boxed{
\int_{b_1W}^{b_2W}P_hdh
=
\int_{B_r\cap\{b_1W<\alpha<b_2W\}}
|\nabla\alpha|dx.
}
\]

Since `n` is constant,

\[
|\nabla\alpha|
\le|\nabla\omega|.
\]

Therefore

\[
\int_{b_1W}^{b_2W}P_hdh
\le
|B_r|^{1/2}
\left(
\int_{B_r}|\nabla\omega|^2dx
\right)^{1/2}.
\]

Let

\[
P_B=\int_{B_r}|\nabla\omega|^2dx.
\]

Because the threshold interval has width

\[
(b_2-b_1)W,
\]

there exists `h_* in (b_1W,b_2W)` such that

\[
\boxed{
P_{h_*}
\le
\frac{|B_r|^{1/2}}
{(b_2-b_1)W}
P_B^{1/2}.
}
\]

---

## 3. Natural-scale form

Write

\[
|B_r|^{1/2}=c_3^{1/2}r^{3/2}.
\]

Then

\[
\boxed{
\frac{P_{h_*}}{r^2}
\le
\frac{c_3^{1/2}}{b_2-b_1}
\frac{P_B^{1/2}}{Wr^{1/2}}.
}
\]

At the natural vorticity radius

\[
r=aW^{-1/2},
\]

we have

\[
W^2r=W^{3/2}a.
\]

Hence

\[
\boxed{
\frac{P_{h_*}}{r^2}
\le
C_{a,b_1,b_2}
\left(
\frac{P_B}{W^{3/2}}
\right)^{1/2}.
}
\]

Define the scale-invariant local palinstrophy channel

\[
\boxed{
\mathcal P_{\rm nat}
=\frac{P_B}{W^{3/2}}.
}
\]

Then one usable threshold always satisfies

\[
\boxed{
P_{h_*}/r^2
\lesssim
\mathcal P_{\rm nat}^{1/2}.
}
\]

---

## 4. Converse: all rough thresholds force palinstrophy

Suppose instead that every regular threshold in the band obeys

\[
P_h\ge\Lambda r^2.
\]

Then coarea gives

\[
(b_2-b_1)W\Lambda r^2
\le
|B_r|^{1/2}P_B^{1/2}.
\]

Squaring,

\[
P_B
\ge
c_{b_1,b_2}\Lambda^2W^2r.
\]

At `r=aW^-1/2`,

\[
\boxed{
P_B
\ge
c_{a,b_1,b_2}
\Lambda^2W^{3/2}.
}
\]

Thus large threshold-interface complexity is not a free geometric branch; it is a critical palinstrophy branch.

---

## 5. Relation to material pruning

The pruning/overlap route should not insist on one predetermined vorticity threshold.

Instead use the band `[b_1W,b_2W]` and choose `h_*` by this lemma.

Then:

- if `P_nat` is large, the branch has already paid a critical palinstrophy cost;
- if `P_nat` is moderate, a threshold core with natural `O(r^2)` boundary area exists and can be used in the material-overlap / flux-amplification geometry.

This removes the arbitrary choice of a wildly fragmented threshold as an escape route.

---

## 6. Important boundary term

The quantity `P_h` above is the **interior level-surface area** inside `B_r`.

If one uses the truncated set `C_h cap B_r` as a material object, its total boundary also contains the part on `partial B_r`.

That spherical truncation boundary is a chosen observation/localization boundary, not a material threshold interface, and must be typed separately.  In a material-tube application one should either

1. work with a threshold component whose relevant boundary is internal; or
2. include the localization-boundary flux as an additional already-known shell/transport channel.

No artificial cancellation is assumed.

---

## 7. Next bridge

Combine the selected controlled-perimeter threshold with the normalized inter-window overlap

\[
\mathcal O_{j\to j+1}
=
\frac{|C_{j+1}\cap X(C_j)|}{|C_{j+1}|}.
\]

High overlap should, after slicing, produce a large old-material surface patch on many oriented cross-sections.  Its boundary complexity is then controlled by the material image of the selected threshold interface unless Lagrangian deformation is large.

This is the remaining overlap-to-flux bridge.

Status: **OPEN HIGH-OVERLAP SLICING / MATERIAL-PATCH FLUX CLOSURE**.
