# DSD M5-379 — Circulation-cancellation reservoir thickness: palinstrophy H or thin-sheet T

Date: 2026-08-31

Status: **ON THE SATURATED AFFINE-SHIELD CORRIDOR, CANCELLING A FIXED FRACTION OF THE GROWING DESCENDANT CIRCULATION UNDER THE FIRST-HITTING VORTICITY CAP REQUIRES AN O(d^2) OPPOSITE-SIGNED FLUX CROSS-SECTION / IF THAT RESERVOIR HAS LONGITUDINAL THICKNESS ell, VECTOR POINCARE ON THE COMBINED SHIELD WINDOW FORCES NORMALIZED LOCAL PALINSTROPHY >= c ell/r / CONSEQUENTLY A NO-H SUBSEQUENCE CAN USE OPPOSITE-SIGN CANCELLATION ONLY BY COLLAPSING THE RESERVOIR TO THICKNESS O(r), PRODUCING AN ASPECT RATIO d/r ~ r^(-1/5) -> infinity / THUS CIRCULATION DISPOSAL ROUTES TO PALINSTROPHY H OR ANISOTROPIC SHEET/FRAGMENT/SPATIAL T / GLOBAL REGULARITY UNPROVED.**

---

## 1. Purpose

M5-356--359 showed that the saturated affine-shield circulation

\[
\Gamma_j\asymp r_j^{-2/5}
\]

grows toward late first-hitting stages and cannot be changed cheaply on the same material loop.

M5-359 retained a possible sequential-renewal route in which an old descendant meets an opposite-signed circulation reservoir and ceases to be a quiet coherent descendant.

The present note asks a more geometric question:

\[
\boxed{
\text{How thick can a cancellation reservoir be if the derivative/palinstrophy H channel is assumed absent?}
}
\]

The answer is: only natural-scale thickness `O(r_j)` is compatible with a uniform normalized palinstrophy ceiling. Since the transverse shield size is much larger, this forces a sheet-like T degeneration.

---

## 2. Saturated shield scales

Use the established saturated affine-shield scaling

\[
W_j\asymp \frac{\nu}{r_j^2},
\qquad
 d_j\asymp r_j^{4/5}.
\]

A coherent shield cross-section carries circulation

\[
\boxed{
|\Gamma_j|\asymp W_jd_j^2.
}
\]

Indeed

\[
W_jd_j^2
\asymp
\nu r_j^{-2}r_j^{8/5}
\asymp
\nu r_j^{-2/5}.
\]

Fixed viscosity factors are harmless for the present scale argument.

---

## 3. Fixed-fraction cancellation forces shield-scale transverse area

Suppose an opposite-signed reservoir is required to cancel a fixed fraction

\[
\kappa|\Gamma_j|,
\qquad 0<\kappa<1,
\]

of the descendant flux.

Before the next first-hitting level, the vorticity amplitude is bounded by a fixed multiple of `W_j`:

\[
|\omega|\le C_qW_j.
\]

Let `Sigma_-` be a transverse section of the opposite reservoir carrying the cancellation-ready signed flux. Then

\[
\kappa|\Gamma_j|
\le
\int_{\Sigma_-}|\omega\cdot n|dS
\le
C_qW_j|\Sigma_-|.
\]

Using `|Gamma_j| ~ W_j d_j^2`,

\[
\boxed{
|\Sigma_-|
\ge c(\kappa,q)d_j^2.
}
\]

Thus a fixed fraction of the shield circulation cannot be cancelled by a single vanishing-area filament while the first-hitting amplitude cap is retained.

The opposite reservoir must occupy a shield-scale transverse area, possibly distributed among bounded-overlap components.

---

## 4. Define the reservoir thickness

Let `ell_j` denote an effective longitudinal thickness of the cancellation-ready reservoir inside a common window of diameter `O(d_j)`.

Quantitatively, retain the branch on which the opposite-signed set `E_-` satisfies

\[
\boxed{
|E_-|
\ge
c_- d_j^2\ell_j,
\qquad
0<\ell_j\le C d_j.
}
\]

If no such common window exists, the reservoir is already spatially non-tight/exported and belongs to

\[
T_{\rm spatial/remote}.
\]

If the flux is distributed among an unbounded number of vanishing components without a comparable effective thickness, that is retained as

\[
T_{\rm fragment/microshape}.
\]

Thus `ell_j` is used only on the coherent/bounded-overlap cancellation corridor.

---

## 5. Positive descendant volume

The old saturated descendant contains a same-sign coherent set `E_+` of shield-scale volume

\[
\boxed{
|E_+|
\ge c_+d_j^3
}
\]

on the retained occupancy corridor, with

\[
|\omega|\ge c_WW_j
\]

and a fixed signed direction relative to the cancellation flux.

If this occupancy degenerates, the branch is already

\[
H_{\rm micro/occ}
\lor
T_{\rm shape}.
\]

Hence the present calculation treats the complementary energy-bearing coherent descendant.

---

## 6. Vector variance created by opposite-sign capacity

Choose a common ball/window `B_j` of diameter comparable to `d_j` containing fixed portions of `E_+` and `E_-`.

On `E_+` and `E_-`, the vorticity vectors differ by order `W_j` because the signed fluxes are oppositely oriented and both retain fixed amplitude fractions.

For two measurable sets of volumes `m_+` and `m_-` inside a finite window of volume `M`, the elementary two-population variance bound gives

\[
\int_{B_j}|\omega-\bar\omega_{B_j}|^2dx
\gtrsim
W_j^2\frac{m_+m_-}{M}.
\]

Here

\[
m_+\gtrsim d_j^3,
\qquad
m_-\gtrsim d_j^2\ell_j,
\qquad
M\asymp d_j^3.
\]

Therefore

\[
\boxed{
\int_{B_j}|\omega-\bar\omega_{B_j}|^2dx
\gtrsim
W_j^2d_j^2\ell_j.
}
\]

This estimate remains valid if the opposite reservoir is distributed among finitely/boundedly many components; only the total occupied volume matters.

---

## 7. Poincare forces palinstrophy proportional to thickness

Vector Poincare on a window of diameter `d_j` gives

\[
\int_{B_j}|\omega-\bar\omega_{B_j}|^2dx
\lesssim
 d_j^2
\int_{B_j}|\nabla\omega|^2dx.
\]

Combining with Section 6,

\[
\boxed{
\int_{B_j}|\nabla\omega|^2dx
\gtrsim
W_j^2\ell_j.
}
\]

This is notable: the transverse shield radius cancels out of the lower bound.

Now use

\[
W_j\asymp\frac\nu{r_j^2}.
\]

Define the natural-scale normalized local palinstrophy

\[
\boxed{
\mathfrak P_j(B_j)
:=
\frac{r_j^3}{\nu^2}
\int_{B_j}|\nabla\omega|^2dx.
}
\]

Then

\[
\boxed{
\mathfrak P_j(B_j)
\gtrsim
\frac{\ell_j}{r_j}.
}
\]

This is the central quantitative result.

---

## 8. No-H forces natural-thickness cancellation sheets

Assume a no-palinstrophy-H subsequence with

\[
\mathfrak P_j(B_j)\le P_*<\infty.
\]

Then Section 7 gives

\[
\boxed{
\ell_j
\le C P_* r_j.
}
\]

But the transverse cancellation area has radius/diameter comparable to `d_j`:

\[
d_j\asymp r_j^{4/5}.
\]

Therefore its transverse-to-thickness aspect ratio satisfies

\[
\boxed{
\frac{d_j}{\ell_j}
\gtrsim
\frac{d_j}{r_j}
\asymp
r_j^{-1/5}
\to\infty.
}
\]

Thus an opposite-sign reservoir that avoids derivative/palinstrophy H must become asymptotically sheet-like.

This is not a bounded-geometry natural partner.

It is precisely an anisotropic shape/compactness turnover:

\[
\boxed{T_{\rm sheet/shape}.}
\]

---

## 9. Add the transport-distance gate

M5-359 gives the material contraction bound

\[
\int_{I_j}\|\nabla u(t)\|_\infty dt
\ge
\log\frac{\delta_j}{Cr_j},
\]

where `delta_j` is the distance to a cancellation-ready opposite reservoir.

Under first-hitting scaling,

\[
\int_{I_j}\|\nabla u\|_\infty dt
=
\int_{\widehat I_j}
\|\nabla_YU_j\|_\infty d\tau.
\]

Hence on a bounded normalized-stage no-gradient-H corridor,

\[
\|\nabla_YU_j\|_\infty\le G_*,
\qquad
|\widehat I_j|\le L_*,
\]

we have

\[
\int_{I_j}\|\nabla u\|_\infty dt
\le G_*L_*.
\]

Consequently any reservoir that is to enter cancellation range within one stage must satisfy

\[
\boxed{
\delta_j\le C e^{G_*L_*}r_j
=O(r_j).
}
\]

Therefore a no-gradient-H cancellation reservoir cannot remain at intermediate or shield distance and be recruited in one stage.

It must already be naturally close, or the event is

\[
T_{\rm spatial/export}.
\]

---

## 10. Combined no-H circulation-disposal routing

On the coherent saturated shield corridor, disposing of a fixed fraction of the old circulation by opposite-sign cancellation now has the exhaustive routing

\[
\boxed{
\text{fixed-fraction circulation cancellation}
\Longrightarrow
H_{\rm Lip/log}
\lor
H_{\rm pal/der}
\lor
T_{\rm spatial/remote}
\lor
T_{\rm sheet/fragment/shape}.
}
\]

In particular, on a simultaneous no-gradient-H and no-palinstrophy-H subsequence,

\[
\boxed{
\text{cancellation disposal}
\Longrightarrow
T_{\rm spatial/remote}
\lor
T_{\rm sheet/fragment/shape}.
}
\]

Thus the sequential-renewal loophole from M5-358--359 does not return to a new bounded-geometry cancellation leaf.

It is pushed entirely into the T-family if H is suppressed.

---

## 11. Relation to M5-357 finite memory

M5-357 showed that repeated no-H affine turnover cannot leave all expelled descendants quietly persistent because each quiet descendant carries scale-independent kinetic-energy occupancy

\[
\Gamma_j^2d_j\asymp1.
\]

M5-358 correctly blocked the false inference that positive-density descendant loss automatically creates growing tree width.

The present result respects that firewall.

It does **not** claim branching.

Instead it shows that one of the main sequential-disposal mechanisms, opposite-sign cancellation, has only two outcomes at late scale:

- derivative/palinstrophy H;
- increasingly anisotropic/spatial T.

Hence sequential renewal can remain width-one, but it cannot remain geometrically quiet.

---

## 12. DSD audit

### Derived

- fixed-fraction cancellation flux plus the first-hitting amplitude cap forces opposite transverse area `>= c d_j^2`;
- a coherent reservoir of thickness `ell_j` creates vector variance `>= c W_j^2 d_j^2 ell_j`;
- Poincare gives normalized palinstrophy `>= c ell_j/r_j`;
- uniform no-H palinstrophy therefore forces `ell_j=O(r_j)`;
- the resulting aspect ratio diverges like at least `r_j^(-1/5)`;
- bounded normalized Lipschitz action forces one-stage cancellation reservoirs to lie within `O(r_j)` material distance.

### Explicit exits

- missing common window -> spatial/remote T;
- unbounded fragmentation -> fragment/microshape T;
- vanishing old-descendant occupancy -> H_micro or shape T;
- large normalized Lipschitz action -> H_Lip;
- large normalized palinstrophy -> H_der.

### Forbidden inference

Do not interpret the sheet-like T branch as impossible merely because its aspect ratio diverges. A hypothetical singular flow may generate sheets. A separate T-rigidity or finite-charge theorem is still required.

---

## 13. Updated frontier on the saturated circulation lane

Combining M5-351, M5-356, M5-357, M5-359, M5-378 and the present note gives schematically

\[
\boxed{
\text{late saturated affine-shield continuation}
\Longrightarrow
H_{\rm freq/cap/Lip/pal}
\lor
T_{\rm spatial/remote/sheet/shape/dynamic}.
}
\]

If all H mechanisms are uniformly suppressed, repeated circulation renewal is forced into increasingly anisotropic or non-tight T geometry.

The next target is therefore a T-side rigidity question:

\[
\boxed{
\text{Can an }O(r_j)\text{-thick, }d_j\text{-wide sheet with }d_j/r_j\to\infty
\text{ persist/reform at positive generation density under finite energy and incompressibility?}
}
\]

---

## 14. Audit verdict

### NEW QUANTITATIVE BRIDGE

\[
\boxed{
\mathfrak P_j
\gtrsim
\frac{\ell_j}{r_j}.
}
\]

### NO-H CONSEQUENCE

\[
\boxed{
\ell_j=O(r_j),
\qquad
\frac{d_j}{\ell_j}\gtrsim r_j^{-1/5}\to\infty.
}
\]

### STILL OPEN

- exclusion of the sheet/fragment/spatial T branch;
- a non-reusable finite global T charge;
- full global regularity.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
