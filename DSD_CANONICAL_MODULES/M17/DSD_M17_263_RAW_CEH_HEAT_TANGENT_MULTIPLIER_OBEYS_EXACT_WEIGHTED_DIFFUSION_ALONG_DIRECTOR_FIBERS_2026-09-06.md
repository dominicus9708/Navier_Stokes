# DSD M17-263 — Raw CE-H heat-tangent multiplier obeys exact weighted diffusion along director fibers

Date: 2026-09-06  
Canonical ID: **M17-263**

Status: **TANGENT MULTIPLIER EVOLUTION / ON THE RAW CE-H HEAT TANGENT, `V=a xi`, `partial_tau V=Delta V=K V`, AND `xi` IS TIME-INDEPENDENT. THE SCALAR AMPLITUDE SATISFIES `partial_tau a=Delta a-|grad xi|^2 a` WITH STATIC POTENTIAL `q=|grad xi|^2`. DIFFERENTIATING `K=(partial_tau a)/a` AND COMMUTING THE STATIC SCHRODINGER-TYPE OPERATOR `Delta-q` WITH TIME GIVES THE EXACT LAW `partial_tau K=Delta K+2 grad log|a|·grad K=a^{-2} div(a^2 grad K)`. M17-262 ALSO GIVES `grad K in ker D xi`; ON RANK-2 THIS KERNEL IS ONE-DIMENSIONAL. THEREFORE MULTIPLIER EVOLUTION IS A ONE-DIMENSIONAL WEIGHTED PARABOLIC DIFFUSION ALONG THE DIRECTOR FIBER, MODULO FIBER GEOMETRY/COORDINATE JACOBIAN. THIS PROVIDES A TRUE TANGENT-LEVEL DISSIPATIVE LAW RATHER THAN AN UNTYPED COEFFICIENT EXIT. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Raw tangent identities

M17-260 and M17-262 give on an active component

\[
\boxed{
V=a\xi,
\qquad
\partial_\tau\xi=0,
\qquad
\partial_\tau V=\Delta V=KV.
}
\]

The scalar amplitude equation is

\[
\boxed{
\partial_\tau a
=\Delta a-q a,
\qquad
q(z):=|\nabla\xi(z)|^2.
}
\]

Because `xi` is static,

\[
\boxed{\partial_\tau q=0.}
\]

Also

\[
\boxed{
K=\frac{\partial_\tau a}{a}
}
\]

where `a!=0`.

---

## 2. Differentiate the amplitude equation

Let

\[
L:=\Delta-q.
\]

Then

\[
\partial_\tau a=La.
\]

Since `L` is time independent,

\[
\partial_\tau^2a
=L(\partial_\tau a)
=L(Ka).
\]

Expand:

\[
\begin{aligned}
L(Ka)
&=\Delta(Ka)-qKa\\
&=K\Delta a
+a\Delta K
+2\nabla K\cdot\nabla a
-qKa\\
&=K(\Delta a-qa)
+a\Delta K
+2\nabla K\cdot\nabla a\\
&=K^2a
+a\Delta K
+2\nabla K\cdot\nabla a.
\end{aligned}
\]

Thus

\[
\boxed{
\partial_\tau^2a
=K^2a+a\Delta K+2\nabla K\cdot\nabla a.
}
\]

---

## 3. Quotient evolution for K

Differentiate

\[
K=\frac{a_\tau}{a}.
\]

Then

\[
\partial_\tau K
=\frac{a_{\tau\tau}}a
-\left(\frac{a_\tau}{a}\right)^2.
\]

Insert Section 2:

\[
\partial_\tau K
=\Delta K
+2\frac{\nabla a}{a}\cdot\nabla K.
\]

Therefore

\[
\boxed{
\partial_\tau K
=\Delta K
+2\nabla\log|a|\cdot\nabla K.
}
\]

Equivalently,

\[
\boxed{
\partial_\tau K
=a^{-2}\nabla\cdot(a^2\nabla K).
}
\]

This is an exact weighted diffusion equation on every active sign component.

---

## 4. Consistency with the vector equation

The same law follows directly from

\[
\partial_\tau V=KV
\]

and heat commutation:

\[
\partial_\tau^2V
=\Delta(\partial_\tau V)
=\Delta(KV).
\]

The left side is

\[
(K_\tau+K^2)V.
\]

The right side is

\[
(\Delta K)V
+2D_{\nabla K}V
+K\Delta V.
\]

Because M17-262 gives

\[
D_{\nabla K}\xi=0,
\]

we have

\[
D_{\nabla K}V
=(D_{\nabla K}a)\xi,
\]

which is parallel to `V`. Cancelling the common `K^2V` term gives the scalar law above.

---

## 5. Rank-2 fiber reduction

M17-262 gives

\[
\boxed{
\nabla K=\lambda_K t_f,
\qquad
t_f\in\ker D\xi,
\qquad |t_f|=1.
}
\]

Hence

\[
\nabla K\cdot\nabla\log|a|
=(D_{t_f}K)(D_{t_f}\log|a|).
\]

Also

\[
\Delta K
=D_{t_f}^2K
+(\nabla\cdot t_f)D_{t_f}K
\]

locally wherever a smooth unit fiber field is chosen.

Therefore

\[
\boxed{
\partial_\tau K
=D_{t_f}^2K
+\left(
\nabla\cdot t_f
+2D_{t_f}\log|a|
\right)D_{t_f}K.
}
\]

Thus `K` evolves by a one-dimensional parabolic operator along the director fiber.

---

## 6. Fiber-coordinate divergence form

Let `s` be local arclength along a fiber and define a positive local density `m(s,tau)` by

\[
\partial_s\log m
=\nabla\cdot t_f
+2\partial_s\log|a|.
\]

Then locally

\[
\boxed{
\partial_\tau K
=m^{-1}\partial_s(m\partial_sK).
}
\]

No global periodicity or boundary condition is assumed here.

The point is structural: the raw Rank-2 caloric multiplier has a genuine second-order diffusion only in the one surviving fiber direction.

---

## 7. Maximum-principle consequence

On any compact fiber segment on which the drift coefficient

\[
b_f:=\nabla\cdot t_f+2D_{t_f}\log|a|
\]

is bounded and no boundary forcing enters, the scalar equation is uniformly parabolic.

Therefore interior extrema of `K` obey the standard one-dimensional maximum principle:

- a strict interior maximum cannot increase forward without boundary/input effects;
- a strict interior minimum cannot decrease forward without boundary/input effects.

Thus recurrent sign-balanced critical `K` occupancy cannot be treated as a freely regenerated coefficient pattern.

A sustained pattern must be supported by fiber-boundary/interface input, drift degeneration, nodal/amplitude degeneration, or backward growth of the parabolic mode.

---

## 8. Relation to M17-240 and M17-145

M17-240 descends the prelimit material multiplier turnover through the full CE-H constitutive law.

M17-145 derives a weighted diffusion/damping law for a multiplier-gradient fold driver in the nonlinear CE-H system.

M17-263 is distinct:

\[
\boxed{
\text{after the raw heat tangent has formed,}
\quad K\text{ itself obeys an exact weighted diffusion law.}
}
\]

The lower-order nonlinear/geometric recharge terms have disappeared because the tangent has already entered the heat-decoupled, temporally direction-rigid regime.

---

## 9. Next target

The remaining fiberwise compatibility problem is now precise.

On a compact Rank-2 fiber corridor, test whether the following can coexist for all ancient times:

1. bounded non-spiking `K`;
2. fixed sign-balanced critical `K` occupancy from the spectral branch;
3. bounded fiber length and nondegenerate amplitude weight;
4. no fiber-boundary/interface replenishment.

Uniform parabolic oscillation contraction suggests that the answer is no; proving the required coefficient bounds and fiber boundary conditions is the next step.

---

## 10. DSD audit

1. The law is derived only on active sign components where `a!=0`.
2. Nodal crossing is an explicit exit.
3. The one-dimensional reduction uses Rank-2 only after the coordinate-free diffusion law is established.
4. No closed-fiber topology is assumed.
5. The maximum principle is local and does not by itself imply ancient constancy without boundary/coefficient control.
6. Global regularity remains unproved.

---

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
