# Accelerating mean-frame symmetry for moving local cells

Date: 2026-08-12

Status: **DERIVED COORDINATE IDENTITY + DSD FRAME REFINEMENT**.

## 1. Time-dependent translation

Let `X(t)` be any sufficiently smooth spatial translation path and set

\[
x=y+X(t).
\]

Define

\[
v(y,t)=u(y+X(t),t)-\dot X(t)
\]

and

\[
q(y,t)=p(y+X(t),t)+\ddot X(t)\cdot y.
\]

A direct calculation gives

\[
\partial_t v+(v\cdot\nabla)v
=-\nabla q+\nu\Delta v,
\qquad
\nabla\cdot v=0.
\]

Thus an accelerating translational frame preserves the force-free incompressible Navier--Stokes form after the uniform inertial acceleration is absorbed into a linear pressure term.

## 2. Use the material-cell mean as frame velocity

For a restartable material cell, choose

\[
\dot X(t)=\bar U(a,\ell,t),
\]

where `bar U` is the cell-mean velocity.

Then the translated velocity is precisely the mean-centered local velocity field, and the coherent translation of the whole cell is removed from the internal dynamics.

The frame acceleration changes the pressure gradient by the same spatially uniform vector at every point. Therefore

\[
\nabla q-\overline{\nabla q}
=
\nabla p-\overline{\nabla p}.
\]

Hence the differential pressure channel `P_osc` is frame invariant under this construction.

## 3. Consequence for the path channel

A separate path-excursion channel is useful for visualization in the original Eulerian frame, but it is not a fundamental source of regularity difficulty: one can translate to the moving mean frame and hold the observation center fixed there.

The genuine bridge obstruction is then reduced to

1. deformation of the material cell relative to a ball;
2. internal oscillation of velocity;
3. differential near pressure;
4. viscous and strain/vorticity couplings.

Accordingly, `K_path` is demoted from a primary danger channel to a coordinate/coverage bookkeeping channel.

## 4. Remaining caveat

The identity above is exact for smooth solutions. To invoke a published epsilon-regularity theorem formulated for suitable weak solutions and fixed cylinders, the transformed local energy inequality and pressure integrability have to be carried through carefully. The linear pressure correction is locally integrable, but this compatibility must be written as a rigorous bridge lemma rather than assumed.

Status: **OPEN BRIDGE LEMMA FOR WEAK/SUITABLE FORMULATION**.
