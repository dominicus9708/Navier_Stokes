# DSD M17-293 — The nonnegative director potential canonically admits a positive ground-state transform on regular components

Date: 2026-09-06  
Canonical ID: **M17-293**

Status: **GROUND-STATE EXISTENCE UPGRADE / M17-292 FORMULATED THE DOOB/GROUND-STATE TRANSFORM CONDITIONALLY ON THE EXISTENCE OF A POSITIVE STATIONARY SOLUTION `h` OF `(-Delta+q)h=0`. ON THE REGULAR RAW HEAT-TANGENT COMPONENT, `q=|grad xi|^2>=0` IS LOCALLY SMOOTH/BOUNDED AND THE SCHRODINGER FORM `int(|grad f|^2+qf^2)` IS AUTOMATICALLY NONNEGATIVE. THE AGMON--ALLEGRETTO--PIEPENBRINK PRINCIPLE, OR DIRECT EXHAUSTION WITH POSITIVE ELLIPTIC SOLUTIONS AND HARNACK NORMALIZATION, THEREFORE PRODUCES A POSITIVE SOLUTION `h` ON EACH CONNECTED REGULAR COMPONENT. CONSEQUENTLY THE GROUND-STATE TRANSFORM `a=h u`, `u_tau=h^(-2)div(h^2 grad u)` IS CANONICAL ON THIS LANE RATHER THAN AN OPTIONAL EXTRA ASSUMPTION. THE REMAINING GLOBAL QUESTION IS THE RECURRENCE/CAPACITY OR MARTIN-INFINITY TYPE OF THE WEIGHTED DIFFUSION. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Elliptic operator on the stationary active component

On a regular stationary active/nodal component `D`, define

\[
q(x):=|\nabla\xi(x)|^2\ge0
\]

and

\[
\boxed{P:=-\Delta+q.}
\]

On every compact subdomain of the payer-free tangent corridor, `xi` is smooth by the parabolic/director regularity already established, hence `q` is locally bounded.

For every test function

\[
\varphi\in C_c^\infty(D),
\]

we have

\[
\boxed{
\langle\varphi,P\varphi\rangle
=\int_D|\nabla\varphi|^2dx
+\int_Dq\varphi^2dx
\ge0.
}
\]

Thus `P` is nonnegative in quadratic-form sense.

---

## 2. Positive solution by AAP / exhaustion

For nonnegative Schrödinger operators, the Agmon--Allegretto--Piepenbrink principle identifies quadratic-form nonnegativity with the existence of positive weak solutions/supersolutions under standard local regularity hypotheses.

Here one may also construct `h` directly.

Choose a smooth exhaustion

\[
D_1\Subset D_2\Subset\cdots\Subset D
\]

containing one fixed base point `x_0`.

On each `D_n`, solve a positive elliptic boundary-value problem for `P` and normalize

\[
h_n(x_0)=1.
\]

Local elliptic Harnack and Schauder/compactness estimates give a subsequence converging on every compact subset to

\[
\boxed{
h>0,\qquad Ph=0\text{ in }D.}
\]

Hence

\[
\boxed{
(-\Delta+q)h=0
\quad\Longleftrightarrow\quad
(\Delta-q)h=0.
}

---

## 3. Canonical ground-state transform

The ancient amplitude satisfies

\[
a_\tau=(\Delta-q)a.
\]

Set

\[
\boxed{a=h u.}
\]

Then exactly as in M17-292,

\[
\boxed{
\partial_\tau u
=h^{-2}\nabla\cdot(h^2\nabla u).
}
\]

The natural invariant measure is

\[
\boxed{d\mu_h=h^2dx.}
\]

The multiplier is

\[
\boxed{
K=\partial_\tau\log a
=\partial_\tau\log u.
}
\]

Thus all nonstationary sign-balanced `K` activity is now encoded by a positive ancient solution of a symmetric weighted diffusion.

---

## 4. Criticality remains distinct from existence

Existence of one positive `h` does **not** imply that `P` is critical.

The positive-solution cone may be one-dimensional or highly nonunique; the operator may be critical or subcritical.

Therefore the correct next split remains

\[
\boxed{
H_{weighted\ recurrence/criticality}
\lor
G_{Martin\text{-}infinity/subcritical\ feed}.
}
\]

M17-293 only removes the preliminary uncertainty about whether the ground-state transform can be formed at all on a regular component.

---

## 5. External-theory note

A modern Agmon--Allegretto--Piepenbrink reference is:

S. Buccheri, L. Orsina, A. C. Ponce, *An Agmon-Allegretto-Piepenbrink principle for Schroedinger operators*, arXiv:2111.05913.

The repository uses this only for the general positivity principle; the concrete nonnegative potential `q=|grad xi|^2` makes the form nonnegativity especially transparent.

---

## 6. Next target: capacity formulation

For the transformed symmetric Dirichlet form

\[
\boxed{
\mathcal E_h[\eta]
:=\int_Dh^2|\nabla\eta|^2dx,
}
\]

the next useful question is whether one can construct cutoffs

\[
\eta_R\to1
\]

with

\[
\mathcal E_h[\eta_R]\to0.
\]

Such a cutoff sequence is the natural analytic signature of recurrence/criticality for the ground-state transformed diffusion.

Failure would produce a positive capacity at infinity, i.e. an explicit infinity-feed channel.

---

## 7. DSD audit

- Ground-state **existence** and operator **criticality** are not conflated.
- The exhaustion is only on regular connected active components.
- Nodal singular/interface components remain separate exits.
- No recurrence theorem is yet claimed from `q>=0` alone.
- Global 3D Navier--Stokes regularity remains unproved.

---

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
