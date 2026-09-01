# DSD M5-474 — Bounded critical ratchet lane extracts a marked ancient Navier--Stokes element

Date: 2026-09-01

Status: **CRITICAL-ELEMENT EXTRACTION / IF THE POSITIVE-DENSITY RATCHET LANE AVOIDS GENUINE AMPLITUDE, RELATIVE-FREQUENCY, NORMALIZED-ENSTROPHY, CENTER-ESCAPE, AND REFORMATION ESCALATION, FIRST-HITTING NORMALIZATION PRODUCES A NONTRIVIAL SMOOTH ANCIENT NAVIER--STOKES ELEMENT WITH UNIFORM VORTICITY `L2 cap Linfinity` CONTROL AND A MARKED ORDER-ONE MATERIAL-AXIS RATCHET EVENT / THIS REDUCES THE BOUNDED HARD CORE TO A SPECIAL ANCIENT-SOLUTION RIGIDITY PROBLEM / GENERAL 3D BOUNDED-ANCIENT LIOUVILLE THEORY IS NOT KNOWN, SO GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Bounded ratchet corridor

Take a positive-density subsequence of first-hitting stages `j` satisfying the ratchet alternative of M5-471--473 and excluding the genuine strong branches.

Write

\[
W_j=\|\omega(t_j)\|_\infty,
\qquad
r_j=\sqrt{\nu/W_j}.
\]

Assume on the selected tail:

1. normalized enstrophy is uniformly bounded in each first-hitting stage,
   \[
   Z_k:=\frac{r_k}{\nu^2}\|\omega(t)\|_2^2\le Z_*
   \]
   in the corresponding retained stage windows;
2. the first-hitting center remains in the bounded-center/nesting corridor;
3. stage-wide parent-scale analyticity of M5-392 holds;
4. no unbounded relative-frequency or remote-source escalation occurs;
5. the marked active material carrier stays above a fixed threshold `|omega|>=eta W` through its selected ratchet interval, otherwise the event is routed to the already typed reformation/flux branch.

These are exactly the complement of the strong/noncompact exits being excluded for the present extraction.

---

## 2. Natural first-hitting normalization

Choose a first-hitting maximum point `X_j` at `t_j` and define

\[
Y=\frac{x-X_j}{r_j},
\qquad
\tau=\frac{\nu(t-t_j)}{r_j^2},
\]

\[
V_j(Y,\tau)
:=\frac{r_j}{\nu}
\big(u(X_j+r_jY,t)-c_j\big),
\]

where `c_j` is a harmless Galilean constant, and

\[
\Omega_j=\nabla_Y\times V_j
=\frac{r_j^2}{\nu}\omega.
\]

Then

\[
\boxed{
\partial_\tau V_j+V_j\cdot\nabla V_j
=-\nabla P_j+\Delta V_j,
\qquad
\nabla\cdot V_j=0.
}
\]

At the marked first-hitting point,

\[
\boxed{|\Omega_j(0,0)|=1.}
\]

For every `tau<=0` represented before `t_j`, first-hitting gives

\[
\boxed{\|\Omega_j(\tau)\|_\infty\le1.}
\]

On a fixed number of forward first-hitting stages the cap is at most a fixed power of `q`, hence also uniformly bounded.

---

## 3. Backward normalized enstrophy remains bounded

Consider a fixed negative normalized time `tau=-A`.

The physical time lies only a finite number `m(A)` of first-hitting generations before `j`. If it lies in a stage with natural scale

\[
r_{j-m}=q^{m/2}r_j,
\]

then the same physical enstrophy measured in the `j` normalization is

\[
Z^{(j)}(\tau)
=rac{r_j}{\nu^2}\|\omega(t)\|_2^2
=q^{-m/2}
\left[
\frac{r_{j-m}}{\nu^2}\|\omega(t)\|_2^2
\right].
\]

Therefore the bounded-stage hypothesis yields

\[
\boxed{
\sup_j\sup_{\tau\in[-A,L]}
\|\Omega_j(\tau)\|_2^2
\le C_A Z_*
}
\]

for every fixed finite backward interval and every fixed forward interval `[-A,L]` lying before the hypothetical singular time.

In fact the factor `q^{-m/2}` improves the bound for old stages.

---

## 4. Velocity bounds from vorticity

Modulo the Galilean gauge, whole-space Biot--Savart gives

\[
V_j=\mathcal B\Omega_j.
\]

Split the kernel into near and far pieces. Uniform `Linfinity` vorticity controls the near part and `L2` vorticity controls the far part, giving

\[
\boxed{
\|V_j(\tau)\|_\infty
\le C_A.
}
\]

Moreover for every finite `p>=2`, Calderon--Zygmund and interpolation yield

\[
\boxed{
\|\nabla V_j(\tau)\|_p
\le C_{A,p}.
}
\]

In particular the sequence is locally spatially precompact in `C^{0,alpha}`, and stage-wide analyticity strengthens this to local smooth compactness on compact subcylinders away from the terminal singular boundary.

---

## 5. Time compactness without pressure

The vorticity equation is

\[
\partial_\tau\Omega_j
+\nabla\cdot
(V_j\otimes\Omega_j-\Omega_j\otimes V_j)
=\Delta\Omega_j.
\]

For a compactly supported smooth test field `phi`,

\[
\frac d{d\tau}\int\Omega_j\cdot\phi
=
\int
(V_j\otimes\Omega_j-\Omega_j\otimes V_j):\nabla\phi
+\int\Omega_j\cdot\Delta\phi.
\]

The right side is uniformly bounded on compact backward intervals. Hence test-function pairings are equi-Lipschitz in time.

Together with spatial compactness, a diagonal subsequence converges to

\[
(V_*,\Omega_*)
\]

on

\[
\mathbb R^3\times(-\infty,L_*)
\]

for some fixed positive `L_*` containing the marked ratchet interval.

The limit solves the ordinary viscosity-one Navier--Stokes equations and is smooth for every preterminal compact interval.

---

## 6. Nontriviality and global vorticity class

The first-hitting mark passes to the limit:

\[
\boxed{|\Omega_*(0,0)|=1.}
\]

For every compact backward time interval,

\[
\boxed{
\Omega_*\in
L^\infty_t(L^2_x\cap L^\infty_x).
}
\]

Consequently

\[
V_*\in L^\infty_t(L^6_x\cap L^\infty_x)
\]

on compact backward intervals, modulo the fixed Galilean choice.

This is stronger spatial information than a generic bounded ancient blow-up profile, but it is not presently a known general zero-Liouville class in three dimensions.

---

## 7. Passage of the material ratchet mark

For each selected stage choose a retained material trajectory `Y_j(tau)` inside the active natural carrier and a fixed normalized interval `J` (after a bounded time translation inside the stage) such that

\[
|\Omega_j(Y_j(\tau),\tau)|\ge\eta>0
\]

and

\[
\int_J|D_\tau\xi_j|d\tau\ge\delta_0>0,
\qquad
\xi_j=\Omega_j/|\Omega_j|.
\]

Because `V_j` converges locally in `C^1`, the Lagrangian flow maps converge on `J`. The active lower bound prevents the direction from becoming undefined. Therefore, after a subsequence,

\[
Y_j\to Y_*,
\qquad
\xi_j\to\xi_*
\]

and

\[
\boxed{
\int_J|D_\tau\xi_*|d\tau
\ge\delta_0.
}
\]

Equivalently the ancient element carries the exact action fork

\[
\boxed{
\int_J|\tau_*|d\tau
+
\int_J
\frac{|(I-\xi_*\otimes\xi_*)\Delta\Omega_*|}{|\Omega_*|}d\tau
\ge\delta_0.
}
\]

Thus the limit is not an equilibrium or a trivial constant/parasitic solution.

---

## 8. Relation to known bounded-ancient theory

General three-dimensional mild bounded ancient Navier--Stokes solutions are a classical Liouville hard problem. Known zero-Liouville results require additional structure such as two-dimensionality, axisymmetry/no swirl, periodicity in a symmetry direction, strong critical backward-sequence bounds, or Type-I terminal-trace hypotheses.

The present element has additional internally generated marks:

- finite normalized vorticity enstrophy;
- global vorticity `Linfinity` cap;
- a first-hitting maximum mark;
- a retained material carrier;
- a nonzero projective ratchet action;
- dual-source/genealogy ancestry inherited from the preceding reductions.

No existing theorem is imported unless its exact scope is shown to include this class.

---

## 9. Exact current split

The positive-density ratchet corridor now has the sharper alternative

\[
\boxed{
A_{ratchet}^{dens}
\Longrightarrow
H_{amp/freq/mass}^{strong}
\lor
E_{ratchet}^{ancient},
}

where

\[
E_{ratchet}^{ancient}
:
\quad
\Omega_*\in L^\infty_{loc,t}(L^2\cap L^\infty),
\quad
|\Omega_*(0,0)|=1,
\quad
\mathcal A_{proj}(J)\ge\delta_0.
\]

This is the bounded critical element that must be rigidified next.

---

## 10. Highest-value next targets

There are three concrete possibilities:

1. prove a Liouville theorem for ancient NS with bounded `L2 cap Linfinity` vorticity plus first-hitting/ratchet marks;
2. prove that such an element necessarily has a weak-`L3` / terminal-trace package already covered by the Albritton--Barker route;
3. show that failure of the needed global tail control generates the strong amplitude/frequency/mass branch, completing a concentration-compactness dichotomy.

---

## 11. Status

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
