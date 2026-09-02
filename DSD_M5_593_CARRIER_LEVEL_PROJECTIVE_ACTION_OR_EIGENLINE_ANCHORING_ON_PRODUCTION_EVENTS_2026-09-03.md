# DSD M5-593 — Carrier-level projective action or eigenline anchoring on production events

Date: 2026-09-03

Status: **THE M5-592 MARKER DICHOTOMY CAN BE LIFTED TO THE FULL COHERENT PRODUCTION-PAYING CARRIER. THE EXACT IDENTITY `rho^2 |D_B xi|^2 = |P_xi^perp(Sigma W + Delta W)|^2` GIVES A NONNEGATIVE CARRIER ACTION. EITHER THIS ACTION IS POSITIVE ON THE PRODUCTION-LINKED EVENT SET, OR THE ENTIRE ACTIVE PAYER CARRIER SATISFIES THE STRAIN+DIFFUSION EIGENLINE CONDITION ALMOST EVERYWHERE DURING THOSE EVENTS. GLOBAL REGULARITY REMAINS UNPROVED.**

## 1. Why the marker-level statement should be strengthened

M5-592 used two tracked material directions and obtained

\[
\text{same-event projective action}
\lor
\text{exact marker anchoring}.
\]

For a derivative/enstrophy budget, a pointwise representative marker is not sufficient.

M5-590, however, gives a fixed-radius coherent production-paying carrier, so the material direction equation can be integrated over the whole active carrier.

## 2. Exact fieldwise direction identity

On the active set write

\[
W=\rho\xi,
\qquad \rho>0,
\qquad |\xi|=1.
\]

The similarity material derivative is

\[
D_B=\partial_\theta+(U+y/2)\cdot\nabla.
\]

M5-487 gives

\[
D_B\xi
=
\tau+\mathcal D_\xi,
\]

with

\[
\tau=(I-\xi\otimes\xi)\Sigma\xi,
\]

and

\[
\mathcal D_\xi
=
\rho^{-1}(I-\xi\otimes\xi)\Delta W.
\]

Multiplying by \(\rho\),

\[
\boxed{
\rho D_B\xi
=
(I-\xi\otimes\xi)(\Sigma W+\Delta W).
}
\]

Therefore

\[
\boxed{
\rho^2|D_B\xi|^2
=
\left|
(I-\xi\otimes\xi)(\Sigma W+\Delta W)
\right|^2.
}
\]

## 3. Production-carrier action

Let \(\chi_{pay}(y,\theta)\) be a fixed smooth cutoff subordinate to the coherent annular payer carrier from M5-590.

On the positive-measure production-linked dual event set \(\mathcal E_{pd}\), define

\[
\boxed{
\mathfrak A_{car}(\theta)
:=
\mathbf 1_{\mathcal E_{pd}}(\theta)
\int
\chi_{pay}\rho^2|D_B\xi|^2dy.
}
\]

Equivalently,

\[
\mathfrak A_{car}
=
\mathbf 1_{\mathcal E_{pd}}
\int
\chi_{pay}
\left|
P_\xi^\perp(\Sigma W+\Delta W)
\right|^2dy.
\]

This observable is nonnegative and bounded on the compact smooth hull.

## 4. Branch CP — positive carrier projective action

If

\[
\boxed{
\langle\mathfrak A_{car}\rangle>0,
}
\]

then a fixed positive amount of material-direction motion occurs in the **same coherent carrier that pays the finite-depth production**.

Thus production and projective action are no longer merely same-component or same-time phenomena; they overlap spatially in the payer carrier itself.

Because

\[
P_\xi^\perp(\Sigma W+\Delta W)
=A+B,
\]

where

\[
A:=P_\xi^\perp\Sigma W,
\qquad
B:=P_\xi^\perp\Delta W,
\]

this branch carries

\[
\boxed{
\left\langle
\mathbf 1_{\mathcal E_{pd}}
\int\chi_{pay}|A+B|^2
\right\rangle>0.
}
\]

This is the precise same-carrier excess channel to be tested against the palinstrophy ledger.

## 5. Branch CE — zero action forces carrier eigenline anchoring

If

\[
\boxed{
\langle\mathfrak A_{car}\rangle=0,
}
\]

then nonnegativity gives

\[
\mathfrak A_{car}=0
\]

for invariant-almost every production-linked event.

Hence on the payer carrier, almost everywhere on those events,

\[
\boxed{
P_\xi^\perp(\Sigma W+\Delta W)=0.
}
\]

Therefore there exists a scalar field \(\lambda_{eff}\) such that

\[
\boxed{
\Sigma W+\Delta W
=
\lambda_{eff}W
}
\]

on the active payer carrier.

Equivalently,

\[
\boxed{
A=-B.
}
\]

This is now a fieldwise statement, not only a representative-trajectory statement.

## 6. Scalar parallel equation on the anchored carrier

Taking the component along \(\xi\),

\[
\lambda_{eff}
=
\sigma+
\frac{\xi\cdot\Delta W}{\rho}.
\]

The full similarity vorticity equation becomes

\[
\boxed{
D_BW
=(\lambda_{eff}-1)W
}
\]

throughout the anchored payer carrier.

Thus

\[
\boxed{
D_B\log\rho
=
\lambda_{eff}-1
=
\sigma-1+
\frac{\Delta\rho}{\rho}
-|\nabla\xi|^2.
}
\]

All transverse dynamics have been eliminated from the local vector equation; the remaining dynamics is scalar amplitude evolution along the anchored direction field.

## 7. Relation to the M5-547 recycling audit

On the anchored carrier,

\[
A=-B.
\]

Therefore

\[
-\Sigma W\cdot\Delta W
=
-(\xi\cdot\Sigma W)(\xi\cdot\Delta W)
+|A|^2,
\]

while

\[
|\Delta W|^2
=
|\xi\cdot\Delta W|^2+|A|^2.
\]

Thus the transverse projected-Laplacian contribution can be exactly recycled into derivative production, precisely as M5-547 warned.

The improvement here is scope: this recycling identity now holds throughout the actual production-paying carrier on Branch CE.

## 8. What remains after this lift

The hard core is now

\[
\boxed{
\text{CP: same-carrier }|A+B|^2\text{ action}>0
\quad\lor\quad
\text{CE: carrierwise }A=-B.
}
\]

For CP, the next question is whether the positive \(|A+B|^2\) action leaves a non-recyclable remainder in the localized palinstrophy balance.

For CE, the vector problem collapses to the scalar parallel/amplitude budget, together with the noncollinear companion required by M5-591.

Status: **THE PRODUCTIVE PAYER CARRIER IS NOW EITHER GENUINELY PROJECTIVE OR AN EXACT STRAIN+DIFFUSION EIGENLINE REGION. THIS IS THE STRONGEST LOCALIZATION OF THE RATCHET/ANCHOR DICHOTOMY SO FAR. GLOBAL REGULARITY REMAINS UNPROVED.**