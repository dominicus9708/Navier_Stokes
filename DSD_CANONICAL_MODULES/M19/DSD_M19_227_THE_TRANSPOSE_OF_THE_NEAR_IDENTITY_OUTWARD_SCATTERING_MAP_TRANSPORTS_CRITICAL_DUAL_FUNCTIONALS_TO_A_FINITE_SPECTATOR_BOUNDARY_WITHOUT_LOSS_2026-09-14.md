# M19-227 — The transpose of the near-identity outward scattering map transports critical dual functionals to a finite spectator boundary without loss

**Date:** 2026-09-14  
**Status:** ACTIVE CALCULATION / ADJOINT-SCATTERING TRANSPOSE REDUCTION

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Purpose

M19-226 shows that arbitrary global relative-periodic adjoint realization cannot be assumed because its compatibility condition is the same Green pairing that detects the primal kernel.

However M19-069 already proves an independent fact in the remote passive spectator corridor: the linearized outward scattering map is near identity.

This module dualizes that theorem. The result localizes the unresolved adjoint obstruction to the finite spectator boundary/interior interface.

## 2. Primal near-identity scattering map

On the strong spectator space X used in M19-069,

\[
D\mathscr S_{R_0}
=I+K_{R_0},
\]

with

\[
\boxed{
\|K_{R_0}\|_{X\to X}
\le
\varepsilon_{R_0},
\qquad
\varepsilon_{R_0}
=O(R_0^{-2}).
}
\]

For sufficiently large R_0,

\[
\varepsilon_{R_0}<1,
\]

so D S_{R_0} is invertible by the Neumann series.

## 3. Transpose map on the dual spectator space

Let X^* be the Banach dual. The transpose satisfies

\[
\boxed{
(D\mathscr S_{R_0})^*
=I+K_{R_0}^*.
}
\]

Moreover

\[
\|K_{R_0}^*\|_{X^*\to X^*}
=
\|K_{R_0}\|_{X\to X}
\le
\varepsilon_{R_0}.
\]

Hence

\[
\boxed{
(D\mathscr S_{R_0})^*
\text{ is invertible whenever }
\varepsilon_{R_0}<1.
}
\]

The dual norm obeys

\[
\boxed{
(1-\varepsilon_{R_0})\|\lambda\|_{X^*}
\le
\|(D\mathscr S_{R_0})^*\lambda\|_{X^*}
\le
(1+\varepsilon_{R_0})\|\lambda\|_{X^*}.
}
\]

Thus the remote spectator conveyor neither destroys nor creates a dual critical functional.

## 4. Critical sphere pairing defines a dual functional

For a sufficiently regular adjoint critical angular datum C, define on the critical scattering trace

\[
\boxed{
\lambda_C(B)
:=
\int_{S^2}B(\omega)\cdot C(\omega)\,d\omega.
}
\]

In the retained strong spectator/scattering topology, assume the sphere trace is continuous; then lambda_C belongs to X^* on the finite-dimensional hard scattering subspace, and by Hahn--Banach it may be extended continuously to the ambient X if needed.

For the canonical dual C_B of M19-225,

\[
\lambda_{C_B}(B)>0
\]

for every nonzero zero-q primal label B.

## 5. Pull the dual datum to a finite spectator boundary

Given a far-field dual functional lambda_infty, define its finite-boundary pullback

\[
\boxed{
\lambda_{R_0}
:=(D\mathscr S_{R_0})^*\lambda_\infty.
}
\]

Then

\[
\lambda_{R_0}(H_0)
=
\lambda_\infty(D\mathscr S_{R_0}H_0)
\]

for every already realizable spectator perturbation H_0.

Near identity gives

\[
\boxed{
\lambda_{R_0}
=
\lambda_\infty+O_{X^*}(R_0^{-2})
}
\]

and uniform norm comparability.

Conversely, every finite-boundary dual functional in X^* has a unique far-field dual image via

\[
((D\mathscr S_{R_0})^*)^{-1}.
\]

Therefore no independent adjoint cokernel is generated in the passive remote tail.

## 6. Relation to a physical adjoint field

The transpose construction is rigorously a dual-functional statement. Under sufficient smoothness, it is the functional-analytic transpose of the linearized Duhamel conveyor and corresponds formally to integrating the adjoint characteristic equation inward from infinity to the spectator boundary.

However this module does not claim that the resulting finite-boundary functional is already represented by a global whole-space relative-periodic adjoint velocity field.

That latter realization requires crossing the finite spectator boundary and solving the interior adjoint return problem.

Permanent distinction:

\[
\boxed{
\text{remote adjoint transport}
\neq
\text{global relative-periodic adjoint realization}.
}
\]

## 7. Main reduction

M19-226 left open where the prescribed dual datum could fail.

M19-227 removes the remote passive tail as the source of that failure:

\[
\boxed{
\text{critical dual datum at infinity}
\Longleftrightarrow
\text{nondegenerate dual functional at a sufficiently remote finite spectator boundary}
}
\]

through an invertible near-identity transpose map.

Hence the remaining obstruction is entirely at

\[
\boxed{
\text{finite spectator boundary}
\longleftrightarrow
\text{interior relative-periodic core}.
}
\]

## 8. Updated zero-q theorem target

The noncircular zero-q target becomes

\[
\boxed{
\mathcal T_{q0}^{int-adj}:
\text{classify the finite-boundary dual functionals that extend through the interior to relative-periodic adjoint states.}
}
\]

A successful theorem need not realize every critical C. It must show, by a mechanism independent of the primal kernel assumption, that the extension space contains a functional nonorthogonal to every nonzero hard zero-q B, or else directly rule out the primal invariant section.

## 9. Certified / not certified

### Certified

1. The transpose of the remote linearized scattering map is I+O(R_0^-2).
2. It is invertible for sufficiently large spectator radius under the same strong-norm gate as M19-069.
3. Critical sphere-pairing functionals are therefore transported to/from the finite spectator boundary without norm collapse.
4. The remote tail contributes no new independent dual obstruction.

### Not certified

1. Extension of the finite-boundary dual functional through the full interior.
2. Relative-periodic physical adjoint realization.
3. Zero-q kernel exclusion.
4. Nonzero-q finite-resonance exclusion.
5. Global regularity.

## 10. Next target

Write the finite-spectator interior problem as a period-map Fredholm problem with boundary trace. Determine whether the existing hard observability/unique-continuation machinery gives a nontrivial statement about the adjoint extension space beyond the tautological kernel/cokernel duality.
