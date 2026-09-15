# M19-305 — Production-conditioned total inward/hysteresis payment is automatically bounded by the full wedge inward budget, so global excess closure is a NO-GO

**Date:** 2026-09-16  
**Status:** ACTIVE DYNAMIC-CORE AUDIT / GLOBAL-EXCESS NO-GO / LOCAL PHASE-RIGIDITY FRONTIER

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Two exact integrated identities

M19-304 gives the unconditioned law

\[
\boxed{
-\int_0^\infty\mathscr J(z)dz
=
\mathscr E(0)
+
\int_0^\infty\mathscr D(z)dz.
}
\]

For the bounded production marker `0<=m_h<=1`, it also gives

\[
\boxed{
-\int_0^\infty
\left(
\mathscr J_m(z)+\mathscr B_m(z)
\right)dz
=
\mathscr E_m(0)
+
\int_0^\infty\mathscr D_m(z)dz.
}
\]

## 2. Conditioning cannot increase terminal energy or dissipation

Because

\[
0\le m_h\le1,
\]

and both terminal energy density and wedge dissipation are nonnegative,

\[
\boxed{
0\le\mathscr E_m(0)\le\mathscr E(0),
}
\]

and

\[
\boxed{
0\le
\int_0^\infty\mathscr D_mdz
\le
\int_0^\infty\mathscr Ddz.
}
\]

Therefore

\[
\boxed{
0
\le
-\int_0^\infty(\mathscr J_m+\mathscr B_m)dz
\le
-\int_0^\infty\mathscr Jdz.
}
\]

The conditioned inward/hysteresis requirement is always contained within the exact total wedge inward-current budget.

## 3. Exact budget fraction

If the unconditioned wedge is nontrivial, define

\[
\boxed{
\rho_m
:=
\frac{
\mathscr E_m(0)+\int_0^\infty\mathscr D_mdz
}{
\mathscr E(0)+\int_0^\infty\mathscr Ddz
}.
}
\]

Then

\[
0\le\rho_m\le1
\]

and the two exact identities imply

\[
\boxed{
\int_0^\infty
(\mathscr J_m+\mathscr B_m)dz
=
\rho_m
\int_0^\infty\mathscr Jdz.
}
\]

Thus the fixed-lag production conditioning selects a fraction of the exact full-wedge inward budget; it cannot demand more in total than the full wedge possesses.

## 4. Global-excess contradiction is impossible at this level

A proposed closure of the form

\[
\text{conditioned event requires more total signed transport than exists globally}
\]

cannot follow from the present energy identities, because the exact PDE gives the opposite inequality automatically.

Therefore

\[
\boxed{
\mathcal T_{radial}^{global\ excess}
\text{ is a NO-GO.}
}
\]

This removes the `excess` half of the provisional M19-304 target `T_radial^{excess/rigidity}`.

## 5. What can still be contradictory

The global integral is compatible by construction, but local distribution can remain rigidly incompatible.

Possible surviving mechanisms are:

1. a finite-depth sign/location constraint on `J_m` that prevents the required inward payment from occurring where the exact ODE needs it;
2. one-dimensional slaving that forces `B_m=0` while simultaneously forbidding the necessary radial-current phase relation;
3. an anchored/projective production geometry incompatible with the required depth-current reversal;
4. a recurrent-factor theorem excluding the joint production/current hysteresis loop;
5. a local critical regularity theorem triggered by the current-reversal geometry.

These are phase/geometry/rigidity mechanisms, not total-budget mechanisms.

## 6. Relation to M19-301

M19-301 showed a positive local depth lobe either fits inside the finite terminal budget or forces depth replenishment.

M19-305 explains why that replenishment can be globally affordable: after full-depth integration the conditioned payment is exactly bounded by the unconditioned inward wedge budget.

Thus quantified replenishment is useful as a localization witness, but not by itself as a global exhaustion contradiction.

## 7. Revised dynamic frontier

The dynamic branch is now reduced to

\[
\boxed{
\mathcal T_{phase}^{prod-current-depth}:
\text{exclude the local phase arrangement of production, radial-current reversal, and hysteresis required by the exact wedge balance.}
}
\]

The broad global-budget route is closed as a NO-GO.

A natural next test is the M5-592 anchored branch: determine whether exact strain--diffusion anchoring constrains the production/current/depth phase strongly enough to force one-dimensional slaving or an impossible current reversal.

---

\[
\boxed{\text{M19-305 COMPLETE; GLOBAL CONDITIONED TRANSPORT EXCESS IS IMPOSSIBLE, SO ONLY LOCAL PHASE/RIGIDITY CAN CLOSE THE DYNAMIC BRANCH.}}
\]