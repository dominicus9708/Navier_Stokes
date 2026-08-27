# DSD M5-160 — Exact Fast-Normal Volterra Slaving with Radius Loss

Date: 2026-08-27

Status: **P1_B^S NORMAL GATE / THE FAST NORMAL VARIABLE HAS AN EXACT TERMINAL-VALUE VOLTERRA REPRESENTATION WITH KERNEL WIDTH `O(e^{-tau})`, SO THE GROWING NORMAL MODE IS ELIMINATED AND THE FAST CHANNEL IS SLAVED TO CROSS-SECTION DATA / THE RIGOROUS ESTIMATE IS A FUTURE-ENVELOPE, REDUCED-ANALYTIC-RADIUS BOUND RATHER THAN A SAME-NORM POINTWISE AMPLITUDE BOUND / THIS REPAIRS THE CONDITIONAL STEP IN M5-159 WITHOUT REINTRODUCING THE M5-152 ANALYTICITY ERROR / GLOBAL REGULARITY UNPROVED.**

---

## 1. Starting equation

Use the M5-154 relative-vorticity equation on Branch `P1_B^S`:

\[
K_s+K_\tau
=e^{-\tau}
\left[
4\nu K_{\tau\tau}
-6\nu K_\tau
+D_\times K
-\mathcal N_\tau K
\right],
\]

where

\[
D_\times:=\nu(2+\Delta_{S^2})
\]

is the constant-coefficient cross-section viscous/zeroth-order operator and `N_tau` is the first-order-or-lower relative transport/stretching/Biot--Savart operator.

---

## 2. Fast variable

Define

\[
\boxed{
J:=K-4\nu e^{-\tau}K_\tau,
\qquad
R:=J-K=-4\nu e^{-\tau}K_\tau.
}
\]

Then

\[
\boxed{
K_\tau=-\frac{e^\tau}{4\nu}R.
}
\]

Differentiate `J`:

\[
J_\tau
=K_\tau+4\nu e^{-\tau}K_\tau
-4\nu e^{-\tau}K_{\tau\tau}.
\]

Substituting the equation for `K_{tau tau}` gives

\[
\boxed{
J_\tau+K_s
=e^{-\tau}
\left[
-2\nu K_\tau
+D_\times K
-\mathcal N_\tau K
\right].
}
\]

Since `J=K+R`, this becomes

\[
\boxed{
R_\tau
-a(\tau)R
=F(\tau),
}
\]

with

\[
\boxed{
a(\tau)=\frac{e^\tau}{4\nu}+\frac12}
\]

and

\[
\boxed{
F(\tau)
:=-K_s
+e^{-\tau}
\left(D_\times K-\mathcal N_\tau K\right).
}
\]

---

## 3. Flat terminal condition removes the growing mode

The homogeneous equation

\[
R_\tau-a(\tau)R=0
\]

has solution

\[
R_h(\tau)
=C
\exp\left(
\frac{e^\tau}{4\nu}+rac\tau2
\right).
\]

This is exactly the fast growing normal branch already seen in M5-146/147.

The flat same-tail condition implies `R` is superalgebraically small as `tau->infinity`, so the homogeneous coefficient must vanish.

Therefore `R` is the unique terminal-value particular solution.

---

## 4. Exact Volterra representation

Solving backward from normal infinity gives

\[
\boxed{
R(\tau)
=-
\int_\tau^\infty
G(\tau,\sigma)
F(\sigma)\,d\sigma,
}
\]

where

\[
\boxed{
G(\tau,\sigma)
=
\exp\left[
-\frac{e^\sigma-e^\tau}{4\nu}
-\frac{\sigma-\tau}{2}
\right].
}
\]

This formula is exact.

---

## 5. Kernel width

For `sigma>=tau`, convexity gives

\[
e^\sigma-e^\tau
\ge e^\tau(\sigma-\tau).
\]

Hence

\[
G(\tau,\sigma)
\le
\exp\left[
-\left(
\frac{e^\tau}{4\nu}+rac12
\right)(\sigma-\tau)
\right].
\]

Therefore

\[
\boxed{
\int_\tau^\infty G(\tau,\sigma)d\sigma
\le
\frac1{e^\tau/(4\nu)+1/2}
\le4\nu e^{-\tau}.
}
\]

So the fast normal channel samples only a future `tau` window of width

\[
\boxed{O(e^{-\tau}).}
\]

---

## 6. Analytic Banach scale

Let `X_delta` denote a cross-section analytic norm with radius `delta` in the pair-flow/time and angular variables.

M5-155 permits Cauchy estimates only with radius loss:

\[
\|K_s\|_{X_{\delta_1}}
\le
C(\delta_0-\delta_1)^{-1}
\|K\|_{X_{\delta_0}},
\]

and similarly

\[
\|D_\times K\|_{X_{\delta_2}}
\le
C(\delta_1-\delta_2)^{-2}
\|K\|_{X_{\delta_1}}.
\]

The first-order relative coupling satisfies on the compact W1 shell class

\[
\|\mathcal N_\tau K\|_{X_{\delta_2}}
\le
C_N(\delta_1-\delta_2)^{-1}
\|K\|_{X_{\delta_1}}.
\]

Fix

\[
0<\delta_2<\delta_1<\delta_0.
\]

Define the future analytic envelope

\[
\boxed{
M_{\delta_0}(\tau)
:=
\sup_{\sigma\ge\tau}
\|K(\sigma)\|_{X_{\delta_0}}.
}
\]

Flatness plus the M5-155 reduced-strip interpolation implies this envelope tends to zero after passing to an admissible reduced radius.

---

## 7. Rigorous slaving estimate

Insert the Cauchy estimates into the exact Volterra formula.

One obtains

\[
\boxed{
\|R(\tau)\|_{X_{\delta_2}}
\le
C_{sl}
 e^{-\tau}
M_{\delta_0}(\tau)
}
\]

for all sufficiently large `tau`, where `C_sl` depends only on `nu`, the fixed radius gaps and the compact W1 coefficient bounds.

More explicitly, the `K_s` contribution is `O(e^-tau) M`, while the already externally weighted `D_x K-NK` contribution is `O(e^-2tau) M`.

Thus

\[
\boxed{
J-K=O(e^{-\tau})
\quad\text{in a reduced analytic radius, relative to the future analytic envelope.}
}
\]

---

## 8. Consequence for the normal derivative

Since

\[
K_\tau=-\frac{e^\tau}{4\nu}R,
\]

the preceding estimate gives only

\[
\boxed{
\|K_\tau(\tau)\|_{X_{\delta_2}}
\le
C
M_{\delta_0}(\tau).
}
\]

This is a tame future-envelope estimate.

It is **not** a same-norm pointwise estimate

\[
\|K_\tau\|\le C\|K\|.
\]

That stronger statement would require an additional comparison between the future analytic envelope and the instantaneous lower-radius norm.

---

## 9. Why M5-159 must be refined

M5-159 proposed the schematic pointwise slaving estimate

\[
\|J-K\|
\lesssim
 e^{-\tau}
(\|A_sK\|+\|\Lambda K\|+\|K\|).
\]

The exact Volterra calculation confirms the `e^-tau` slaving scale, but the direct rigorous consequence from the present inputs is the future-envelope/radius-loss estimate of Section 7.

Therefore the final Rayleigh-quotient frequency inequality in M5-159 remains **conditional** until the envelope-to-instantaneous comparison is either proved or avoided.

This is a correction of strength, not a reversal of the commutator-only transfer result.

---

## 10. DSD four-chain audit

### Formation — GREEN

`J` and `R` are exact algebraic transforms of the same relative-vorticity field.

### Axis — GREEN

The fast normal direction is isolated from cross-section frequency.  The Volterra kernel acts only in `tau`.

### Static aggregation — GREEN

The fast growing homogeneous mode is removed by the already formed flat terminal condition; it is not counted as an additional branch afterward.

### Dynamics — GREEN / YELLOW

Exact Volterra slaving is GREEN.

Same-norm pointwise slaving is YELLOW and must not be used without a new comparison lemma.

### Cross-audit — GREEN

The radius loss required by M5-152/M5-155 is explicit, preventing the old compact-analyticity shortcut from re-entering.

---

## 11. Updated next gate

There are now two admissible ways forward:

1. prove an envelope-to-instantaneous comparison at selected normal depths and close the M5-159 frequency quotient there; or
2. formulate the spectral-transfer argument directly in a nested analytic-envelope norm so that no pointwise comparison is needed.

The second route is preferred because it does not ask flat functions to satisfy an artificial local monotonicity property.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
