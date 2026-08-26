# DSD M5-41 — Audited Pump-Anchored Ancient-to-Terminal Cell

Date: 2026-08-27

Status: **AUDIT CORRECTION / THE PREVIOUS IDENTIFICATION OF A `lambda_j -> 0` BOUNDARY SEQUENCE WITH A FIRST-HIT SEQUENCE WAS TOO STRONG / THE CORRECT SAME-TRAJECTORY OBJECT IS AN ANCIENT-TO-TERMINAL CELL ANCHORED AT A FIXED POSITIVE NORMALIZED PUMP LEVEL `lambda_c` / GLOBAL REGULARITY UNPROVED.**

## 1. Audit correction

The previous version of M5-41 simultaneously imposed

\[
\lambda_j:=L_j\sqrt{T_*-t_j}\to0
\]

and treated `t_j` as first-hit/formation times for a fixed positive excess level.

This is not justified in general.

The earlier amplitude-state analysis already identifies the correct topology:

- the defect is **formed** at a strict interior normalized amplitude band;
- one may choose a fixed level
  \[
  \boxed{\lambda_c\in(\lambda_-,\lambda_+)}
  \]
  at which the invariant mean pressure-minus-viscous gain is positive;
- the same fixed physical threshold is then transported toward
  \[
  \lambda=L\sqrt{T_*-t}\downarrow0
  \]
  as the singular time is approached.

Thus finite-amplitude formation and zero-amplitude boundary storage are two different stages of one amplitude characteristic.

---

## 2. Pump-event sequence

Choose recurrent pump-active W1 times

\[
s_j\to\infty
\]

at which the fixed normalized threshold `lambda_c` satisfies a strict positive gain condition, schematically

\[
\boxed{
J_P(\lambda_c,s_j)
-\nu D_{\lambda_c}(s_j)
\ge g_c>0.
}
\]

Let

\[
t_j:=T_*-e^{-s_j}.
\]

Define the corresponding physical threshold

\[
\boxed{
L_j:=\lambda_c e^{s_j/2}
=\frac{\lambda_c}{\sqrt{T_*-t_j}}.
}
\]

Then

\[
L_j\to\infty
\]

while exactly

\[
\boxed{
L_j\sqrt{T_*-t_j}=\lambda_c.
}
\]

This is the correct scaling relation for the formation event.

---

## 3. Physical parabolic rescaling

Define

\[
\boxed{
V_j(z,\sigma)
:=
L_j^{-1}
 u\!\left(
 X_*+\frac z{L_j},
 t_j+\frac{\sigma}{L_j^2}
 \right).
}
\]

Each `V_j` solves the same 3D incompressible Navier--Stokes equation with viscosity `nu`.

The original singular time `T_*` appears at

\[
\sigma_*^{(j)}
=L_j^2(T_*-t_j)
=\lambda_c^2.
\]

Hence the forward horizon is **fixed**, not collapsing:

\[
\boxed{\sigma_* = \lambda_c^2>0.}
\]

The desired same-trajectory limit therefore lives on

\[
\boxed{
\mathbb R^3\times(-\infty,\lambda_c^2).
}
\]

---

## 4. Exact relation to the recurrent W1 orbit

For

\[
t=t_j+\frac\sigma{L_j^2},
\]

one has

\[
T_*-t
=e^{-s_j}
\frac{\lambda_c^2-\sigma}{\lambda_c^2}.
\]

Therefore

\[
Y
=\frac z{\sqrt{\lambda_c^2-\sigma}},
\]

and

\[
s
=s_j
+\log\frac{\lambda_c^2}{\lambda_c^2-\sigma}.
\]

Let

\[
U_j^\#(Y,\eta):=U(Y,s_j+\eta).
\]

Then exactly

\[
\boxed{
V_j(z,\sigma)
=
(\lambda_c^2-\sigma)^{-1/2}
U_j^\#\!\left(
\frac z{\sqrt{\lambda_c^2-\sigma}},
\log\frac{\lambda_c^2}{\lambda_c^2-\sigma}
\right).
}
\]

W1 compactness and recurrence allow a subsequence for which

\[
U_j^\#\to U^\#
\]

on compact `(Y,eta)` sets, where `U^#` is a complete recurrent W1 trajectory.

Hence

\[
\boxed{
V_*(z,\sigma)
=
(\lambda_c^2-\sigma)^{-1/2}
U^\#\!\left(
\frac z{\sqrt{\lambda_c^2-\sigma}},
\log\frac{\lambda_c^2}{\lambda_c^2-\sigma}
\right)
}
\]

for

\[
\sigma<\lambda_c^2.
\]

Thus the limit is an ancient-to-terminal Navier--Stokes cell generated exactly from one complete W1 orbit.

---

## 5. Meaning of the anchor time `sigma=0`

At the pump anchor,

\[
\sigma=0,
\]

one has

\[
V_*(z,0)
=\lambda_c^{-1}U^\#(z/\lambda_c,0).
\]

Therefore threshold `|V|=1` corresponds exactly to the W1 amplitude level

\[
|U|=\lambda_c.
\]

The positive W1 net gain at `lambda_c` becomes a positive threshold-one physical/rescaled formation rate.

Indeed the scale-critical threshold quantity

\[
K(U;\lambda)=\lambda E_\lambda(U)
\]

satisfies along the physical-amplitude characteristic

\[
\frac{dK}{ds}
=\lambda(J_P-\nu D_\lambda).
\]

Since

\[
\frac{ds}{d\sigma}\Big|_{\sigma=0}
=\lambda_c^{-2},
\]

the pump condition gives a fixed positive normalized formation rate at `sigma=0`.

Thus the M5-23--40 threshold-Hodge / direction-compression constraints should be attached to **pump-active events**, not to an unjustified `lambda_j->0` first-hit sequence.

---

## 6. Forward evolution to the boundary defect

For the same physical threshold `L_j`, the corresponding W1 normalized amplitude at rescaled time `sigma` is

\[
\boxed{
\lambda(\sigma)
=\sqrt{\lambda_c^2-\sigma}.
}
\]

Hence

\[
\lambda(0)=\lambda_c,
\]

while

\[
\boxed{
\lambda(\sigma)\downarrow0
\qquad
(\sigma\uparrow\lambda_c^2).
}
\]

Therefore one and the same rescaled cell realizes the DSD formation chain

\[
\boxed{
\text{finite-amplitude pump at }\sigma=0
\longrightarrow
\text{amplitude-characteristic transport}
\longrightarrow
\text{zero-amplitude boundary defect as }\sigma\uparrow\lambda_c^2.
}
\]

This is the correct same-trajectory object.

---

## 7. Backward ancient behavior

As

\[
\sigma\to-\infty,
\]

one has

\[
\log\frac{\lambda_c^2}{\lambda_c^2-\sigma}\to-\infty,
\]

while the complete W1 orbit remains in a compact bounded class. Therefore

\[
\|V_*(\sigma)\|_\infty
\lesssim
(\lambda_c^2-\sigma)^{-1/2}
\to0.
\]

Thus the pump-to-defect cell is ancient backward and locally vanishing in the remote past.

---

## 8. Relation to standard Type-I ancient compactness

The existence of ancient limits under Type-I rescaling is consistent with the known Albritton--Barker framework. The W1-specific addition is the exact recurrent inverse-Leray representation and the identification of two distinguished stages in the same cell:

1. a fixed positive normalized pump event;
2. the later low-amplitude critical boundary defect.

The strong-`L^3` Liouville theorem is still not automatically applicable because the inherited `1/r` tail remains weak-critical.

---

## 9. Correct updated target

The endpoint is no longer

\[
\text{rule out an arbitrary first-hit ancient terminal cell}.
\]

It is now the more structured problem

\[
\boxed{
\text{rule out a pump-anchored ancient-to-terminal cell}
}
\]

with all of the following:

- complete recurrent W1 ancestry;
- fixed positive finite-amplitude gain at `sigma=0`;
- threshold-Hodge / direction-compression formation geometry at the pump;
- static critical `1/r` far-field ancestry;
- transport of the same physical threshold toward `lambda->0`;
- positive critical boundary defect as `sigma -> lambda_c^2`;
- local backward decay as `sigma -> -infinity`.

No contradiction is proved here.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
