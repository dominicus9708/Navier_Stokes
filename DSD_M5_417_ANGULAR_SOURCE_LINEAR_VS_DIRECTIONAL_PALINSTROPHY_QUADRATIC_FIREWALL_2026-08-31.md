# DSD M5-417 — Angular source is linear while directional palinstrophy is quadratic: strict-gap firewall

Date: 2026-08-31

Status: **THE NATURAL MISALIGNED SOURCE FORCES A QUANTITATIVE TRANSVERSE-PALINSTROPHY FLOOR, BUT THE SCALING OF THE TWO EFFECTS IS DIFFERENT / BIOT--SAVART STRETCHING IS FIRST ORDER IN THE ANGULAR DEFECT WHILE THE DIRECTIONAL/PALINSTROPHY COST IS SECOND ORDER / AN ANCHORED POINCARE ARGUMENT GIVES `P_perp >= c A_nat^2`, NOT A UNIVERSAL LINEAR COERCIVE DOMINATION OF THE STRETCHING ACTION / THEREFORE THE M5-394 DUAL-FLUX GEOMETRY ALONE CANNOT JUSTIFY A BLANKET STRICT NONLINEAR-EFFICIENCY GAP AGAINST VISCOSITY / THE NEXT TARGET MUST USE PERSISTENCE, NONREUSE, OR CRITICAL-ELEMENT RIGIDITY IN ADDITION TO ONE-SNAPSHOT MISALIGNMENT / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Purpose

M5-416 localizes any near-efficient formed source to the natural phase-space window.

The apparent next possibility is to hope that the forced misalignment of the M5-394 companion automatically makes nonlinear stretching strictly less efficient than critical viscous dissipation.

This note audits that hope before using it.

The key fact is a mismatch of homogeneity in the angular defect:

- the Biot--Savart stretching source is linear in the transverse/angular component;
- the associated directional/palinstrophy cost is quadratic.

This prevents a naive universal strict gap.

---

## 2. Natural normalized geometry

Work at one first-hitting stretching event in the normalized variables of M5-362/M5-394.

Let

\[
|\Omega|\le1,
\qquad
|\Omega(0)|=1,
\qquad
\xi_0:=\Omega(0).
\]

Assume a fixed natural annulus

\[
A=\{c_1\le |Y|\le c_2\}
\]

carries productive angular source action

\[
\boxed{
\mathcal A_{nat}
:=
\int_A
\frac{|\Omega(Y)|\sin\theta(Y)}{|Y|^3}\,dY
\ge a_*>0.
}
\]

Here `a_*` is a fixed fraction of the normalized first-hitting stretching floor `c_gamma`.

---

## 3. Replace the angle by a transverse vorticity component

Define the transverse component relative to the main carrier direction

\[
\boxed{
F(Y)
:=(I-\xi_0\otimes\xi_0)\Omega(Y).
}
\]

Then exactly

\[
\boxed{
|F(Y)|
=|\Omega(Y)|\sin\theta(Y).
}
\]

Since `|Y|` is bounded above and below on the fixed annulus,

\[
\mathcal A_{nat}
\le C_A\int_A |F(Y)|\,dY.
\]

Thus

\[
\boxed{
\|F\|_{L^1(A)}
\ge c_A a_*.
}
\]

By finite annulus volume,

\[
\boxed{
\|F\|_{L^2(A)}
\ge c_2 a_*.
}
\]

This avoids introducing a separately chosen pointwise angle `delta_0`: the productive source itself directly yields a transverse-vector mass floor.

---

## 4. The main core provides an anchor

At the center,

\[
F(0)=0.
\]

M5-392 gives the normalized Lipschitz bound

\[
\|\nabla\Omega\|_\infty\le C_1.
\]

Hence on a sufficiently small fixed core ball `B_rho(0)`,

\[
|F(Y)|\le C_1|Y|.
\]

Choose `rho` small enough, depending only on the fixed first-hitting constants, that

\[
\boxed{
\|F\|_{L^2(B_\rho)}
\le
\frac12 c_2 a_*.
}
\]

If this choice requires `rho` smaller when `a_*` is smaller, this dependence is retained explicitly; no uniform positive angle is invented.

---

## 5. Anchored Poincare inequality

Let `D` be one fixed connected bounded domain containing both `B_rho(0)` and the productive annulus `A`.

A Poincare inequality with control on the anchor subset gives

\[
\|F\|_{L^2(D)}
\le
C_D
\left(
\|\nabla F\|_{L^2(D)}
+
\|F\|_{L^2(B_\rho)}
\right).
\]

Since the annulus contribution is at least `c_2 a_*` while the anchor contribution is at most half that amount,

\[
\boxed{
\|\nabla F\|_{L^2(D)}
\ge c_D' a_*.
}
\]

Therefore the transverse palinstrophy obeys

\[
\boxed{
\mathcal P_\perp
:=
\int_D |\nabla F|^2dY
\ge
c_P a_*^2.
}
\]

This is a direct source-action-to-palinstrophy inequality.

---

## 6. Relation to the full vorticity palinstrophy

Because `F` is a fixed orthogonal projection of `Omega`,

\[
|\nabla F|
\le
|\nabla\Omega|.
\]

Hence

\[
\boxed{
\int_D|\nabla\Omega|^2dY
\ge
c_Pa_*^2.
}
\]

This is consistent with, and slightly reorganizes, the M5-377/M5-394 local-capacity lower bound.

The gain is that the lower bound is expressed directly in terms of the productive angular-source action.

---

## 7. Linear versus quadratic angular scaling

Consider a small angular perturbation of an otherwise aligned source packet, with typical angular defect `delta`.

The Biot--Savart angular factor satisfies

\[
\sin\theta\sim\delta,
\]

so the productive stretching contribution is first order:

\[
\boxed{
\mathcal A_{nat}\sim\delta.
}
\]

By contrast, the transverse component satisfies `F=O(delta)`, hence its gradient energy is quadratic:

\[
\boxed{
\mathcal P_\perp\sim\delta^2.
}
\]

The rigorous inequality of Section 5 has exactly this structure:

\[
\boxed{
\mathcal P_\perp
\gtrsim
\mathcal A_{nat}^2.
}
\]

It does **not** give

\[
\mathcal P_\perp
\gtrsim
\mathcal A_{nat}
\]

with a universal coefficient independent of the source action.

---

## 8. Consequence for a viscosity-dominance attempt

The first-hitting magnitude growth needs a normalized positive stretching action of order `a_*`.

The geometric source argument guarantees a directional derivative cost of order at least `a_*^2`.

For small `a_*`,

\[
a_*^2\ll a_*.
\]

Therefore the geometry alone cannot establish a universal inequality of the schematic form

\[
\boxed{
\text{productive nonlinear action}
\le
(1-\varepsilon)
\times
\text{viscous critical dissipation}
}
\]

for a fixed `epsilon>0` merely from the existence of a misaligned companion.

Any such result would need additional information beyond one-snapshot angular separation.

---

## 9. Why first-hitting fixes do not automatically repair the gap

For a fixed geometric first-hitting ratio `q>1` and a fixed normalized stage-length ceiling `L_*`, one has

\[
a_*\gtrsim\frac{\log q}{L_*}.
\]

Thus `a_*` is not literally tending to zero inside one fixed implementation.

However the present lower bound still compares unknown geometric constants and an integrated palinstrophy floor against a pointwise/time-integrated stretching requirement.

There is no proved inequality showing that the resulting palinstrophy coefficient exceeds the nonlinear production coefficient.

Moreover the local palinstrophy need not act at the exact vorticity maximum at the same instant; it may be spatially displaced in the source/transition region.

Therefore no stagewise viscosity contradiction follows from the positive lower bound alone.

---

## 10. Exact magnitude-equation interpretation

Where `omega=a xi` with `a=|omega|>0`,

\[
\xi\cdot\Delta\omega
=
\Delta a-a|\nabla\xi|^2.
\]

Thus

\[
(\partial_t+u\cdot\nabla)\log a
=
\gamma
+
\nu\frac{\Delta a}{a}
-
\nu|\nabla\xi|^2.
\]

At a spatial maximum of `a`, `Delta a<=0`, giving

\[
D^+\log W
\le
\gamma
-
\nu|\nabla\xi|^2
\quad\text{at the maximizing point whenever the direction is defined smoothly there.}
\]

This identity shows the desired local depletion mechanism.

But M5-394 only forces a directional turn somewhere across the natural source network; it does not force the full `|grad xi|^2` lower bound at the maximizing point itself.

That spatial mismatch is another reason the integrated source-palinstrophy floor cannot be inserted directly as a pointwise maximum-principle penalty.

---

## 11. Scope-safe conclusion

The valid new statement is

\[
\boxed{
\text{natural productive angular source}
\Longrightarrow
\mathcal P_\perp
\gtrsim
\mathcal A_{nat}^2.
}
\]

The invalid stronger statement is

\[
\boxed{
\text{natural productive angular source}
\Longrightarrow
\text{universal strict nonlinear/viscous efficiency gap}.
}
\]

The second implication remains unproved and is not assumed.

---

## 12. What information could repair the gap

There are three plausible upgrades.

### A. Temporal persistence

If the same angular-source configuration persists for a fixed fraction of the natural time, parabolic diffusion may transport the transverse derivative cost into the main core strongly enough to obtain a sharper dynamic inequality.

### B. Nonreuse

If each new source action forces a fresh transverse-gradient/capacity region not chargeable to prior events, the quadratic cost can accumulate in a scale-time orthogonal ledger.

### C. Critical-element rigidity

If near-minimal throughput localizes to one compact natural main/companion cluster by M5-416, classify the ancient/recurrent solutions that can realize equality or near-equality in the relevant production estimates.

The one-snapshot angle estimate alone is insufficient.

---

## 13. DSD audit verdict

### DERIVED

\[
\boxed{
\mathcal P_\perp
\gtrsim
\mathcal A_{nat}^2.
}
\]

### FIREWALL

- angular stretching is first-order in direction defect;
- directional/palinstrophy cost is second-order;
- the derivative cost is not forced pointwise at the vorticity maximum;
- therefore no blanket strict viscosity-dominance constant is available from dual-flux geometry alone.

### NEXT TARGET

Temporal persistence or critical-element rigidity, not another static angle estimate.

### CURRENT STATUS

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
