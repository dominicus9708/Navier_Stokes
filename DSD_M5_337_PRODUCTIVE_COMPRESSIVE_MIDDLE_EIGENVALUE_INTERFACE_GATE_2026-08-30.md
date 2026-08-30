# DSD M5-337 — Productive/Compressive Middle-Eigenvalue Interface Gate

Date: 2026-08-30

Status: **BIPOLAR DETERMINANT COMPENSATION AND PLANAR-COMPRESSIVE ATOM STATES REDUCED, UNDER NO-REMOTE-TURNOVER, TO A MIDDLE-EIGENVALUE SPACE/TIME INTERFACE / INTERFACE PAYS STRAIN GRADIENT OR MIDDLE-EIGENVALUE MATERIAL-DERIVATIVE ACTION / THE LATTER ROUTES TO PRESSURE-CURVATURE OR H2 BY M5-336 / GLOBAL REGULARITY UNPROVED.**

## 1. Structural input

Two independent exact requirements are now present near a hypothetical singular endpoint:

1. First-hitting/enstrophy amplification requires recurrent positive determinant production, equivalently a productive `lambda_2>0` sector.
2. Endpoint energy-atom Oseen rigidity requires nonsummable compressive strain action; by M5-334 this is either already in the positive-middle sector, in `lambda_2<0`, or in `|lambda_2|<<|S|` near-planar states.

The only new issue is therefore coexistence of productive and nonproductive/compressive middle-eigenvalue states.

## 2. Occupied middle-eigenvalue states

Work in one normalized connected parent cylinder

\[
Q=B_R\times I
\]

with fixed `R` and fixed normalized time length, on a no-remote-turnover branch.

After excluding amplitude concentration as an H event, assume a fixed normalized strain cap. Then a fixed amount of critical `L_x^3` action yields, by a standard level-set extraction, positive-measure occupied subsets.

Thus on dangerous recurrent cells one may extract either simultaneous or space-time separated subsets

\[
E_+\subset Q,
\qquad
E_c\subset Q,
\]

with positive normalized measure and a fixed spectral gap such that

\[
\lambda_2\ge a_0>0
\quad\text{on }E_+,
\]

while either

\[
\lambda_2\le-a_0
\quad\text{on }E_c
\]

or, for the planar branch,

\[
|\lambda_2|\le\delta a_0
\quad\text{on }E_c.
\]

If such states cannot be retained in a common bounded parent, that failure is precisely a spatial/center/material `T` exit.

## 3. Scalar interface lower bound

Let

\[
f=\lambda_2(S).
\]

Eigenvalues of symmetric matrices are 1-Lipschitz with respect to the matrix norm, so almost everywhere

\[
\boxed{
|\nabla f|\le|\nabla S|.
}
\]

Positive-measure subsets on which `f` differs by a fixed amount force a fixed variance:

\[
\boxed{
\int_Q|f-f_Q|^2\,dxdt\ge c(a_0,|E_+|,|E_c|)>0.
}
\]

Use a parabolic Poincare inequality in a material coordinate chart on the bounded no-T parent. Since the Lagrangian map is bi-Lipschitz on a fixed normalized cell unless a transport/Lipschitz T event occurs,

\[
\int_Q|f-f_Q|^2
\le
C_R
\left[
\int_Q|\nabla f|^2
+
\int_Q|D_tf|^2
\right].
\]

Therefore

\[
\boxed{
\int_Q|\nabla S|^2
+\int_Q|D_t\lambda_2|^2
\ge c_*>0.
}
\]

Hence every productive/compressive coexistence cell pays either a spatial strain-gradient action or a middle-eigenvalue material-derivative action.

## 4. Spatial interface branch

If

\[
\int_Q|\nabla S|^2\ge c_*/2,
\]

then the productive/compressive transition itself creates a fixed scale-invariant derivative cost.

Repeated non-summable occurrence is an `H_{grad}` action.
If the transition layer leaves the fixed parent or is continually replaced, it is a `T` event.

Thus the spatial bipolar interface is not a new terminal leaf.

## 5. Temporal/material interface branch

If instead

\[
\int_Q|D_t\lambda_2|^2\ge c_*/2,
\]

insert the exact M5-336 identity

\[
D_t\lambda_2
=\nu e_2^T\Delta S e_2
-e_2^T\nabla^2p\,e_2
-\lambda_2^2
+\frac14|\omega|^2\sin^2\theta_2.
\]

On the near-planar locked corridor, the last two terms are lower order.
Therefore a fixed material interface cost requires at least one of

\[
\boxed{
\nu\Delta S,
\qquad
\nabla^2p,
\qquad
\text{loss of neutral-axis locking},
\qquad
\text{state replacement/turnover}
}
\]

to pay a fixed scale-invariant action.

These are respectively derivative-H, pressure-H/T, stretch/tilt, or dynamic-T channels already present in the master tree.

## 6. Bipolar determinant branch collapses structurally

M5-334 showed that a nonintegrable `lambda_2<0` determinant contribution requires a nonintegrable compensating positive determinant contribution.

The present interface gate shows that, if those two populations remain in the same bounded parent without remote escape, their coexistence itself forces H/T interface action.

Thus

\[
\boxed{
C_{det\text{-}bipolar}
\Longrightarrow
H_{interface}\lor T_{separation}.
}
\]

## 7. Planar atom branch also joins the same interface

A neutral-axis planar atom state has `lambda_2 approximately 0`.
A singular first-hitting tower still needs productive positive-middle episodes.

Therefore, unless the productive population escapes to a different parent (`T`), the planar state and productive state generate the same `lambda_2` interface and hence the same H/T cost.

This leaves only a possible **fully separated productive/compressive architecture**, which is by definition a transport/remote-coherence problem rather than a new local spectral branch.

## 8. Scope

The material-coordinate Poincare step assumes the bounded no-T parent has enough Lagrangian regularity on the fixed normalized cylinder. If that bi-Lipschitz control fails, the failure is itself assigned to the dynamic/Lipschitz T branch; it is not silently discarded.

No contradiction is claimed from a single interface event. The gain is proof-tree reduction:

\[
\boxed{
\text{productive + atom-compressive coexistence}
\Longrightarrow
H\lor T.
}
\]

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
