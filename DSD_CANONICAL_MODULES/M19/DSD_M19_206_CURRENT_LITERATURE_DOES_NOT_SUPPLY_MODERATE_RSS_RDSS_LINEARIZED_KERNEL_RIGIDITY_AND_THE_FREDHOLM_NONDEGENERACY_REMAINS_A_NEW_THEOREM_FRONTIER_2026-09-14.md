# M19-206 — Current literature does not supply moderate RSS/RDSS linearized kernel rigidity; Fredholm nondegeneracy remains a new theorem frontier

**Date:** 2026-09-14  
**Status:** EXTERNAL LITERATURE AUDIT / OPEN THEOREM FRONTIER

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Search target

The active bounded-period problem is no longer generic existence of recurrent tails. It is the much narrower statement:

\[
\boxed{
\text{after time/rotation quotient, exclude nonsymmetry unit/Fredholm kernel modes of moderate RSS/RDSS states.}
}
\]

## 2. Current 2026 rotated-self-similar result

Pineau--Vicol, *On rotated backwards self-similar solutions of the incompressible 3D Navier--Stokes equations* (arXiv:2607.09619, 2026), proves Type-I Liouville results for RSS when the rotation parameter is sufficiently small or sufficiently large, and analogous RDSS results for extreme rotation regimes and scaling factor sufficiently close to one.

The paper explicitly treats the moderate rotation regime only partially; it does not provide a general linearized Fredholm nondegeneracy theorem for all moderate RSS/RDSS profiles.

## 3. Search verdict

A current literature search did not identify a theorem of the form

\[
\ker D_U\mathcal F(U,S,Q_*)
=
E_{sym}
\]

for all Type-I moderate RSS/RDSS profiles, nor a general result excluding all nonsymmetry unit Floquet multipliers in this class.

Therefore the repository must not silently import such a theorem.

## 4. Consequence

The bounded-period hard core remains a genuine analytic frontier:

\[
\boxed{
\mathcal T_{kernel}^{moderate}:
\text{prove symmetry-only kernel/unit spectrum for the compact moderate RSS/RDSS hard set.}
}
\]

Existing external results continue to remove parameter boundary regimes, which is essential for compactification, but they do not close the interior Fredholm problem.

## 5. Next calculation

Use the already established weighted-L2 linear gap to derive a necessary nonlinear-compensation floor for any nonsymmetry unit/kernel mode. This will not yet prove nonexistence, but will isolate the exact quantitative obstruction inside the compact moderate set.