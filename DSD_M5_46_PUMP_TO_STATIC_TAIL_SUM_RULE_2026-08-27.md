# DSD M5-46 — Pump-to-Static-Tail Sum Rule

Date: 2026-08-27

Status: **EXACT SAME-TRAJECTORY IDENTITY / THE TERMINAL STATIC-TAIL TRUNCATED ENERGY EQUALS THE TOTAL ANCIENT PRESSURE-MINUS-VISCOUS FORMATION ACTION AT ONE FIXED PHYSICAL THRESHOLD / THIS COMPRESSES THE INTERIOR PUMP AND BOUNDARY DEFECT INTO ONE FINITE-HORIZON LEDGER / GLOBAL REGULARITY UNPROVED.**

## 1. Pump-to-defect cell

Let

\[
\sigma_*:=\lambda_c^2
\]

and let `V_*` be the audited M5-41 ancient-to-terminal cell on

\[
\mathbb R^3\times(-\infty,\sigma_*).
\]

The corresponding W1 normalized amplitude is

\[
\lambda(\sigma)
=\sqrt{\sigma_*-\sigma}.
\]

Thus threshold `|V_*|=1` represents the **same physical velocity threshold** throughout the cell, while in W1 variables it moves from large `lambda` in the remote past through `lambda_c` at the pump anchor to `lambda -> 0` at the terminal boundary.

---

## 2. Fixed-threshold truncated energy

Define

\[
\boxed{
\mathcal E_1(\sigma)
:=
\frac12\int_{\mathbb R^3}
(|V_*(z,\sigma)|^2-1)_+\,dz.
}
\]

Because the active set `|V_*|>1` is contained in a fixed finite normalized ball by the W1 `1/r` envelope, `E_1(sigma)` is finite for every `sigma<sigma_*`.

The exact scaling relation gives

\[
\boxed{
\mathcal E_1(\sigma)
=K\bigl(U^\#(\eta(\sigma));\lambda(\sigma)\bigr),
}
\]

where

\[
K(U;\lambda)=\lambda E_\lambda(U).
\]

Thus the W1 moving-amplitude characteristic becomes a fixed threshold in the physical parabolic cell.

---

## 3. Exact truncated-energy ledger

For smooth `sigma<sigma_*`, testing Navier--Stokes with

\[
V_*\,\mathbf 1_{\{|V_*|>1\}}
\]

in the standard regularized sense gives

\[
\boxed{
\frac{d}{d\sigma}\mathcal E_1
+
\nu D_1^{surf}
=
J_P(1,\sigma).
}
\]

Here

\[
D_1^{surf}
=
\int_{|V_*|>1}|\nabla V_*|^2dz
+
\int_{|V_*|=1}|\nabla |V_*||\,dS
\]

at regular levels, with the usual positive measure interpretation after approximation, and

\[
J_P(1,\sigma)
=
\int_{|V_*|=1}
\Pi\,V_*\cdot n_a\,dS.
\]

Equivalently,

\[
\boxed{
\mathcal E_1'
=J_P(1)-\nu D_1^{surf}.
}
\]

---

## 4. Remote-past boundary condition

M5-43 gives

\[
\|V_*(\sigma)\|_\infty
\le
\frac{M_*}{\sqrt{\sigma_*-\sigma}}.
\]

Hence for sufficiently negative `sigma`,

\[
\|V_*(\sigma)\|_\infty<1
\]

and therefore

\[
\boxed{
\mathcal E_1(\sigma)=0
\qquad\text{for all sufficiently negative }\sigma.
}
\]

Thus there is no hidden initial high-amplitude charge at ancient time `-infinity`.

---

## 5. Terminal static trace

For fixed `z != 0`, as

\[
\sigma\uparrow\sigma_*,
\]

one has

\[
|Y|=\frac{|z|}{\sqrt{\sigma_*-\sigma}}\to\infty.
\]

Hence the punctured terminal trace is the selected W1 tail blow-down from M5-42:

\[
\boxed{
T(z)
=
\frac1{|z|}
\Phi\!\left(
\frac z{|z|},
\log\frac{|z|}{\lambda_c}
\right).
}
\]

The Type-I/tail envelope gives a domination by `C/|z|`. Since

\[
(|z|^{-2}-1)_+
\]

is locally integrable in three dimensions and vanishes outside a finite ball after the envelope is imposed, dominated-convergence/local compactness gives

\[
\boxed{
\mathcal E_1(\sigma)
\longrightarrow
\mathcal E_T
:=
\frac12\int_{\mathbb R^3}
(|T(z)|^2-1)_+dz.
}
\]

The origin is a punctured terminal point, but the `1/r` singularity is integrable for this truncated `L2` quantity.

---

## 6. Exact pump-to-tail sum rule

Integrate the fixed-threshold ledger from the remote past to the terminal time. Using `E_1(-infinity)=0` and the terminal limit gives

\[
\boxed{
\mathcal E_T
=
\int_{-\infty}^{\sigma_*}
\left[
J_P(1,\sigma)
-
\nu D_1^{surf}(\sigma)
\right]d\sigma.
}
\]

Thus the terminal static-tail high-amplitude charge is exactly the total same-trajectory net formation work accumulated during the ancient history.

No separate boundary source is needed.

---

## 7. Pump anchor inside the sum rule

At `sigma=0`, M5-41 selects a recurrent finite-amplitude pump event for which

\[
J_P(1,0)-\nu D_1^{surf}(0)>0
\]

in the audited pump-event formulation.

Hence the sum rule contains a genuine positive interior formation stage.

Later positive and negative contributions may occur before the terminal time. The identity does not assert monotonicity of `E_1`.

---

## 8. Why this is not yet a contradiction

The integral is finite for one fixed threshold-one cell. Under terminal scale recurrence, later nested pump copies correspond to higher and higher **unscaled** amplitude thresholds, not repeated independent threshold-one charges of equal size.

Their contributions to this fixed-threshold ledger can shrink geometrically, so one must not add all recurrent pump copies as independent order-one costs.

Equivalently, a scale-invariant count of all thresholds returns to the `p=3` / critical-clock logarithmic divergence already audited earlier.

Thus M5-46 is an exact compression, not a closure.

---

## 9. DSD interpretation

The whole M5 formation chain can now be written in one scalar same-trajectory ledger:

\[
\boxed{
\text{zero ancient high-amplitude state}
\xrightarrow{\;J_P-\nu D\;}
\text{finite-amplitude pump}
\xrightarrow{\;\text{continued net processing}\;}
\text{static terminal-tail charge }\mathcal E_T.
}
\]

The terminal defect is therefore a fully formed output of the ancient dynamics, not an untyped boundary insertion.

---

## 10. Updated target

A new rigidity theorem could now attack the sum rule directly, for example by proving that a static-tail, terminal-scale-recurrent ancient cell cannot have

\[
\int_{-\infty}^{\sigma_*}
(J_P-\nu D_1^{surf})d\sigma>0
\]

under finite-energy ancestry.

No such sign theorem is presently proved.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
