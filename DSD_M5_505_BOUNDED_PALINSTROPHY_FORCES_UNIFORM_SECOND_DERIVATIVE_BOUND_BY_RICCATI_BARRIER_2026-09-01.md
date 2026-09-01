# DSD M5-505 — Bounded palinstrophy forces a uniform second-derivative bound by a similarity Riccati barrier

Date: 2026-09-01

Status: **BOUNDED-P DERIVATIVE LEDGER / APPLYING TWO SPATIAL DERIVATIVES TO THE SIMILARITY VORTICITY EQUATION GIVES THE EXACT BALANCE `1/2 H' + 5/4 H + K = N_H`, WHERE `H=||Delta W||_2^2` AND `K=||grad Delta W||_2^2` / AFTER COMMUTATOR CANCELLATION OF THE HIGHEST TRANSPORT TERM, CALDERON--ZYGMUND, SOBOLEV, AND FOURIER LOG-CONVEXITY GIVE `1/2 H' + 5/4 H + 1/2 K <= C(E^(1/2)P^(1/2)+P^(2/3))H + C P^(7/3)` / IF `E<=Z_*` AND `P<=P_*`, THEN `K>=H^2/P_*`, PRODUCING A QUADRATIC RICCATI DAMPING / BECAUSE EACH ANCIENT SIMILARITY TRAJECTORY EXISTS FOR ALL `theta in R`, NO FINITE SMOOTH TRAJECTORY CAN CROSS ABOVE THE POSITIVE RICCATI ROOT: BOUNDED PALINSTROPHY THEREFORE FORCES A UNIFORM GLOBAL `H` CAP / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Input and notation

Use the similarity vorticity equation

\[
\partial_\theta W
+W
+\frac12(y\cdot\nabla)W
-\Delta W
=
\mathcal N,
\]

where

\[
\mathcal N
:=
(W\cdot\nabla)U
-(U\cdot\nabla)W,
\]

with

\[
\nabla\cdot U=0,
\qquad
\nabla\cdot W=0.
\]

Define

\[
E:=\|W\|_2^2,
\qquad
P:=\|\nabla W\|_2^2,
\]

\[
\boxed{
H:=\|\Delta W\|_2^2
=\|\nabla^2W\|_2^2,
}
\]

and

\[
\boxed{
K:=\|\nabla\Delta W\|_2^2
=\|\nabla^3W\|_2^2.
}
\]

The whole-space equalities are understood through the full derivative tensor/Plancherel identity.

M5-505 analyzes the M5-501 bounded-palinstrophy branch

\[
\boxed{
E\le Z_*<\infty,
\qquad
P\le P_*<\infty.
}
\]

---

## 2. Apply the Laplacian

Apply `Delta` to the similarity equation:

\[
\partial_\theta\Delta W
+\Delta W
+\frac12\Delta(y\cdot\nabla W)
-\Delta^2W
=
\Delta\mathcal N.
\]

Use the commutator identity

\[
\boxed{
\Delta(y\cdot\nabla W)
=
y\cdot\nabla\Delta W
+2\Delta W.
}
\]

Take the `L2` inner product with `Delta W`.

---

## 3. Exact linear coefficient

The time term is

\[
\frac12H'.
\]

The explicit `+Delta W` term contributes

\[
H.
\]

For the dilation term,

\[
\frac12
\int
\Delta W\cdot
\left(y\cdot\nabla\Delta W+2\Delta W\right)dy.
\]

Since

\[
\int
\Delta W\cdot(y\cdot\nabla\Delta W)dy
=
-\frac32H,
\]

we get

\[
\frac12
\left(-\frac32H+2H\right)
=
\frac14H.
\]

Therefore the total linear similarity damping is

\[
\boxed{
H+\frac14H
=
\frac54H.
}
\]

The diffusion term gives

\[
\boxed{K}.
\]

---

## 4. Exact second-derivative balance

Define

\[
\mathcal N_H
:=
\int
\Delta\mathcal N\cdot\Delta W\,dy.
\]

Then

\[
\boxed{
\frac12H'
+\frac54H
+K
=
\mathcal N_H.
}
\]

This is the next derivative ledger after M5-501.

---

## 5. Nonlinear commutator structure

Expand

\[
\Delta\left((W\cdot\nabla)U\right)
\]

and

\[
\Delta\left((U\cdot\nabla)W\right).
\]

In the transport part, the highest term

\[
U\cdot\nabla\Delta W
\]

cancels in the energy pairing because

\[
\nabla\cdot U=0.
\]

The remaining terms have the schematic forms

\[
(\nabla U)(\nabla^2W)(\nabla^2W),
\]

\[
(\nabla W)(\nabla^2U)(\nabla^2W),
\]

and

\[
W(\nabla^3U)(\nabla^2W).
\]

Thus no uncontrolled highest-order transport derivative remains.

---

## 6. Estimate the first commutator class

Using Holder,

\[
I_1
\lesssim
\|\nabla U\|_3
\|\nabla^2W\|_6
\|\nabla^2W\|_2.
\]

Calderon--Zygmund and Sobolev give

\[
\|\nabla U\|_3
\lesssim
\|W\|_3,
\]

\[
\|\nabla^2W\|_6
\lesssim
K^{1/2}.
\]

Also

\[
\|W\|_3
\lesssim
E^{1/4}P^{1/4}.
\]

Therefore

\[
I_1
\lesssim
E^{1/4}P^{1/4}H^{1/2}K^{1/2}.
\]

By Young,

\[
\boxed{
I_1
\le
\varepsilon K
+C_\varepsilon E^{1/2}P^{1/2}H.
}
\]

---

## 7. Estimate the mixed second-derivative class

For the terms containing one `grad W` and one `grad^2 U`,

\[
I_2
\lesssim
\|\nabla W\|_3
\|\nabla^2U\|_6
\|\nabla^2W\|_2.
\]

Calderon--Zygmund gives

\[
\|\nabla^2U\|_6
\lesssim
\|\nabla W\|_6
\lesssim
H^{1/2}.
\]

Interpolation gives

\[
\|\nabla W\|_3
\lesssim
P^{1/4}H^{1/4}.
\]

Hence

\[
I_2
\lesssim
P^{1/4}H^{5/4}.
\]

Fourier log-convexity gives

\[
\boxed{
H^2\le PK.
}
\]

Therefore

\[
P^{1/4}H^{5/4}
\le
P^{7/8}K^{5/8}.
\]

Young with exponents `8/5` and `8/3` yields

\[
\boxed{
I_2
\le
\varepsilon K
+C_\varepsilon P^{7/3}.
}
\]

---

## 8. Estimate the highest stretching class

For

\[
W(\nabla^3U)(\nabla^2W),
\]

use

\[
I_3
\lesssim
\|W\|_6
\|\nabla^3U\|_3
\|\nabla^2W\|_2.
\]

Sobolev gives

\[
\|W\|_6
\lesssim
P^{1/2}.
\]

Calderon--Zygmund and interpolation give

\[
\|\nabla^3U\|_3
\lesssim
\|\nabla^2W\|_3
\lesssim
H^{1/4}K^{1/4}.
\]

Thus

\[
I_3
\lesssim
P^{1/2}H^{3/4}K^{1/4}.
\]

Young with exponents `4` and `4/3` gives

\[
\boxed{
I_3
\le
\varepsilon K
+C_\varepsilon P^{2/3}H.
}
\]

---

## 9. Audited `H` inequality

Choose the Young parameters so that the total absorbed part is at most `K/2`.

Then

\[
\boxed{
\frac12H'
+\frac54H
+\frac12K
\le
C_2
\left(
E^{1/2}P^{1/2}
+P^{2/3}
\right)H
+C_3P^{7/3}.
}
\]

This is the audited second-derivative inequality.

Under

\[
E\le Z_*,
\qquad
P\le P_*,
\]

set

\[
A_*
:=
C_2
\left(
Z_*^{1/2}P_*^{1/2}
+P_*^{2/3}
\right),
\]

and

\[
B_*
:=
C_3P_*^{7/3}.
\]

Then

\[
\boxed{
\frac12H'
+\frac54H
+\frac12K
\le
A_*H+B_*.
}
\]

---

## 10. Log-convexity converts third derivatives into quadratic damping

The derivative moments satisfy

\[
H^2\le PK.
\]

If `H>0`, then `P>0`; using `P<=P_*`,

\[
\boxed{
K
\ge
\frac{H^2}{P}
\ge
\frac{H^2}{P_*}.
}
\]

Substitute into the `H` inequality:

\[
\frac12H'
\le
-\frac{1}{2P_*}H^2
+
\left(A_*-\frac54\right)H
+B_*.
\]

Equivalently,

\[
\boxed{
H'
\le
-\frac1{P_*}H^2
+b_*H
+2B_*,
}
\]

where

\[
b_*
:=
2\left(A_*-\frac54\right).
\]

This is a scalar Riccati upper inequality with a negative quadratic leading term.

---

## 11. Positive Riccati root

Let `H_crit` be the positive root of

\[
-\frac1{P_*}H^2
+b_*H
+2B_*=0.
\]

Explicitly,

\[
\boxed{
H_{crit}
=
\frac{P_*}{2}
\left(
 b_*
+
\sqrt{
 b_*^2
+
\frac{8B_*}{P_*}
}
\right).
}
\]

Because the square root is at least `|b_*|`, this root is nonnegative.

For every

\[
H>H_{crit},
\]

the right side of the Riccati inequality is strictly negative.

For sufficiently large `H`, it is bounded above by

\[
-c_*H^2
\]

for some `c_*>0` depending only on `Z_*` and `P_*`.

---

## 12. Complete similarity trajectories cannot cross the barrier

Each ancient hull trajectory is defined for

\[
s<0.
\]

Since

\[
\theta=-\log(-s),
\]

this corresponds to a complete similarity trajectory

\[
\boxed{
\theta\in\mathbb R.
}
\]

Suppose for contradiction that at some `theta_0`,

\[
H(\theta_0)>H_{crit}.
\]

While `H>H_crit`, the differential inequality forces `H` to decrease in forward similarity time.

Hence going backward from `theta_0`, `H` cannot cross downward through `H_crit`; instead it remains at least `H(theta_0)`.

On that backward interval, the negative quadratic term provides

\[
H'\le-c_0H^2
\]

for some `c_0>0` after fixing the level `H(theta_0)>H_crit`.

Integrating

\[
\left(\frac1H\right)'
=-\frac{H'}{H^2}
\ge c_0
\]

backward forces `1/H` to become nonpositive after a finite amount of backward similarity time, contradicting the existence of a finite smooth `H` on the complete trajectory.

Therefore

\[
\boxed{
H(\theta)
\le H_{crit}
\quad\text{for every }\theta\in\mathbb R.
}
\]

Thus bounded palinstrophy forces a uniform second-derivative cap.

---

## 13. Consequence for the M5-501 branch

M5-501 had suggested that under bounded `P`, one should derive the `H` ledger and determine whether a new unbounded second-derivative branch appears.

M5-505 shows that it does **not** appear independently:

\[
\boxed{
P\le P_*<\infty
\Longrightarrow
H\le H_{crit}(Z_*,P_*)<\infty.
}
\]

Therefore

\[
\boxed{
\text{bounded }P
+
\text{unbounded }H
}
\]

is excluded on a complete smooth similarity hull trajectory.

This is stronger than the M5-501 mean threshold.

---

## 14. Projected-diffusion consequence

The projected-diffusion branch has

\[
\langle H\rangle
\ge h_{proj}>0.
\]

M5-505 now places that recurrent positive second-derivative cost inside the finite interval

\[
0<h_{proj}
\le
\langle H\rangle
\le
H_{crit}(Z_*,P_*).
\]

Thus the bounded-P survivor must support a quantitatively nonzero but globally bounded second-derivative reservoir.

It cannot evade the derivative ledger by sending `H` to infinity while keeping `P` bounded.

---

## 15. DSD audit and firewall

The Riccati barrier uses all of the following:

1. whole-space Sobolev/Calderon--Zygmund estimates;
2. the global caps `E<=Z_*` and `P<=P_*`;
3. smooth finite derivative quantities at each similarity time;
4. completeness of the ancient similarity trajectory for all `theta in R`.

It does **not** prove

- bounded original physical derivatives at a hypothetical singular time;
- compactness at the terminal boundary `s=0`;
- disappearance of the terminal Dirichlet tail;
- or global regularity of Navier--Stokes.

The statement is internal to the normalized ancient similarity hull.

---

## 16. Updated derivative frontier

Combining M5-504 and M5-505 gives the sharper split

\[
\boxed{
\mathcal C_{ax+projdiff}
\Longrightarrow
H_{tail}^{remote-Sob}
\lor
\mathcal C_{bounded-P,H}^{proj},
}
\]

where

\[
\mathcal C_{bounded-P,H}^{proj}
:
\quad
P\le P_*,
\qquad
H\le H_{crit}(Z_*,P_*),
\qquad
\langle H\rangle\ge h_{proj}>0.
\]

The unbounded derivative hierarchy has been isolated entirely into the remote Sobolev-cascade branch.

---

## 17. Highest-value next target

The next calculation should test whether the Riccati mechanism iterates.

For

\[
D_m=\|\nabla^mW\|_2^2,
\]

one expects the linear similarity coefficient

\[
\frac{2m+1}{4}D_m
\]

and dissipation `D_{m+1}`.

If the nonlinear commutator can be estimated using already bounded lower derivative levels and the log-convex relation

\[
D_m^2\le D_{m-1}D_{m+1},
\]

then bounded `P` may force uniform bounds for every fixed `D_m` by induction.

That would collapse the bounded derivative corridor to an all-order globally Sobolev-bounded similarity hull and leave the remaining obstruction in recurrence/tail geometry rather than derivative escalation.

---

## 18. Status

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
