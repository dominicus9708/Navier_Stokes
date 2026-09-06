# DSD M17-283 — Bounded-K CE-H makes nodal membership time-stationary and moving interfaces force corridor failure

Date: 2026-09-06  
Canonical ID: **M17-283**

Status: **NODAL-TIME GATE / ON THE RAW INTRINSIC HEAT TANGENT, THE SIMULTANEOUS RELATIONS `partial_tau V=Delta V` AND `Delta V=K V` GIVE THE POINTWISE ODE `partial_tau V=K V` ON THE ACTIVE SET. IF `K` REMAINS LOCALLY BOUNDED ON A SPACETIME CORRIDOR UP TO A PUTATIVE NODAL TRANSITION, EVERY FIXED SPATIAL POINT THAT IS ACTIVE AT ONE TIME REMAINS ACTIVE THROUGH THE WHOLE CORRIDOR, WITH EXACT MULTIPLICATIVE AMPLITUDE PROPAGATION. CONSEQUENTLY A NODAL INTERFACE CANNOT MOVE THROUGH A FIXED SPATIAL POINT WHILE THE BOUNDED-K CE-H CORRIDOR REMAINS VALID. ANY MOVING NODAL INTERFACE THEREFORE REQUIRES LOSS OF THE K-BOUND, FAILURE OF CE-H/ACTIVE-SET CONTINUATION, NODAL AMPLITUDE DEGENERATION, OR AN EXPLICIT DOMAIN/INTERFACE EXIT. THIS REMOVES `MOVING NODAL INTERFACE` AS AN INDEPENDENT PAYER-FREE COMPACT-TANGENT SURVIVOR. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Raw tangent equations

On the payer-free compact raw tangent corridor we have

\[
\boxed{\partial_\tau V=\Delta V}
\]

and on the CE-H active set

\[
\boxed{\Delta V=K V.}
\]

Hence

\[
\boxed{\partial_\tau V=K V.}
\]

The identity is pointwise wherever the active CE-H representation is valid.

M17-281 already shows that on a compact active cylinder with amplitude floor and bounded lower-order coefficients, `K` is locally bounded.

---

## 2. Fixed spatial point propagation

Fix one spatial point `x` and a time interval

\[
I=[\tau_1,\tau_2]
\]

on which

\[
|K(x,\tau)|\le K_*<\infty
\]

and the active CE-H identity remains valid.

The vector ODE

\[
\partial_\tau V(x,\tau)=K(x,\tau)V(x,\tau)
\]

has the exact solution

\[
\boxed{
V(x,\tau)
=
V(x,\tau_0)
\exp\!\left(
\int_{\tau_0}^{\tau}K(x,s)\,ds
\right).
}
\]

Therefore

\[
\boxed{
V(x,\tau_0)\neq0
\Longrightarrow
V(x,\tau)\neq0
\quad\forall\tau\in I.
}
\]

Moreover

\[
e^{-K_*|\tau-\tau_0|}|V(x,\tau_0)|
\le
|V(x,\tau)|
\le
e^{K_*|\tau-\tau_0|}|V(x,\tau_0)|.
\]

Thus a positive amplitude cannot reach zero in finite rescaled time while `K` remains bounded.

---

## 3. Moving interface implies a corridor failure

Suppose a nodal interface moves through a fixed point `x_*` at time `tau_*`.

Then there are active times approaching the transition with

\[
V(x_*,\tau)\neq0
\]

and a transition time at which

\[
V(x_*,\tau_*)=0,
\]

or conversely a previously nodal point becomes active.

This cannot occur under the bounded-K multiplicative propagation of Section 2.

Hence at least one of the assumptions required for that propagation must fail near the transition:

\[
\boxed{
G_{moving\ nodal\ interface}
\Longrightarrow
G_{K\text{-}bound\ failure}
\lor
G_{CEH/active\text{-}set\ continuation\ failure}
\lor
G_{nodal\ amplitude\ degeneration}
\lor
G_{domain/interface\ exit}.
}
\]

By M17-281, `K`-bound failure on the payer-free compact active lane itself returns to

\[
G_{nodal/amplitude}
\lor
H_{normalized\ palinstrophy/mass\ escape}
\lor
G_{scaled\ ambient/coefficient}
\lor
G_{interface/domain}.
\]

Thus moving nodal geometry is not an independent payer-free endpoint.

---

## 4. Stationarity of active-set membership

Let

\[
\mathcal A(\tau)=\{x:V(x,\tau)\neq0\}.
\]

On any connected spacetime corridor on which `K` is bounded and CE-H extends throughout the active region without an interface exit, every point already in the active set preserves its membership for the duration of the corridor.

Therefore the only way for

\[
\mathcal A(\tau)
\]

to change is through one of the hard exits listed above.

This is the correct DSD statement.

We do **not** claim that an arbitrary vector-valued caloric field has a stationary nodal set.
The stationarity comes from the extra CE-H multiplicative relation

\[
\partial_\tau V=K V
\]

plus bounded `K`.

---

## 5. Relation to M17-282

M17-282 closed bounded regular stationary nodal domains by reducing the positive amplitude to the principal Dirichlet mode.

M17-283 shows that, on the bounded-K payer-free compact CE-H corridor, a nodal domain cannot evade M17-282 merely by moving its boundary.

Therefore the genuinely distinct nodal survivors are narrowed to

\[
\boxed{
G_{unbounded\ nodal\ domain}
\lor
G_{irregular/singular\ nodal\ geometry}
\lor
G_{CEH/coefficient/interface\ failure}.
}
\]

---

## 6. DSD audit

- `partial_tau V=K V` is used only on the active CE-H set.
- Boundedness/integrability of `K` is explicit; it is not assumed through a singular nodal transition for free.
- No general theorem claiming stationary nodal sets for heat equations is invoked.
- A moving interface is not called impossible absolutely; it is shown incompatible with the current bounded-K CE-H corridor.
- The result is therefore a branch-return theorem, not a global nodal theorem.
- Global 3D Navier--Stokes regularity remains unproved.

---

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
