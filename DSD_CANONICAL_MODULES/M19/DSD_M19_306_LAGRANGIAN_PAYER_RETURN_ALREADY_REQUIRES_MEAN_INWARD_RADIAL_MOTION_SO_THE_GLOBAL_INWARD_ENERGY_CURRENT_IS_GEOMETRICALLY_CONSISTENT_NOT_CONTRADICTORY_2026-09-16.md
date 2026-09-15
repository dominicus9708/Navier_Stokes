# M19-306 — Lagrangian payer return already requires mean inward radial motion, so the global inward energy current is geometrically consistent rather than contradictory

**Date:** 2026-09-16  
**Status:** ACTIVE DYNAMIC-CORE CROSS-CHECK / EULERIAN-LAGRANGIAN RADIAL SIGN CONSISTENCY / RADIAL-RETURN CONTRADICTION NO-GO

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Eulerian result from M19-304

The exact full-wedge energy balance gives

\[
\boxed{
\int_0^\infty\mathscr J(z)dz
=
-\mathscr E(0)
-\int_0^\infty\mathscr D(z)dz
<0
}
\]

for every nontrivial retained Type-I wedge.

Thus the depth-integrated radial local-energy current is necessarily inward/negative.

## 2. Historical Lagrangian payer-return identity

M5-596 considers a persistent production-paying material representative satisfying

\[
Y'(\theta)=U(Y,\theta)+\frac12Y.
\]

For

\[
r=|Y|,
\qquad
U_r=U\cdot Y/r,
\]

one has exactly

\[
\frac d{d\theta}\log r
=
\frac12+rac{U_r}{r}.
\]

If the same persistent material representative returns infinitely often to one fixed finite-depth annulus, the endpoint logarithm is bounded and therefore

\[
\boxed{
\left\langle\frac{U_r}{r}\right\rangle_{return}
=-\frac12.
}
\]

The physical velocity must supply mean inward radial motion precisely canceling the outward similarity dilation.

## 3. The Eulerian and Lagrangian signs agree

M19-304 says that the whole wedge must have negative depth-integrated energy transport.

M5-596 says that a recurrent finite-depth production-paying material carrier must have negative mean radial physical velocity relative to the similarity dilation.

These are different observables and one does not algebraically imply the other, but their required signs are compatible:

\[
\boxed{
\text{Eulerian net inward energy transport}
\quad\parallel\quad
\text{Lagrangian mean inward payer motion}.
}
\]

Therefore no contradiction follows from the mere coexistence of recurrent payer returns and inward radial energy transport.

## 4. Wedge-coordinate form of the material return

M5-596 also gives

\[
q'=\frac{U_r}{r}=zF_r
\]

along the selected material trajectory and

\[
\frac{z'}z=-1-2\frac{U_r}{r}.
\]

Thus a finite-depth recurrent payer already samples both signs/strengths needed to counter the similarity drift.

The dynamic wedge is not forced to move monotonically outward in depth.

## 5. Same-marker scalar recurrence does not fix energy current

If the same active marker remains nondegenerate across returns, M5-596 additionally gives

\[
\boxed{
\left\langle
\sigma+rac{\Delta\rho}{\rho}-|\nabla\xi|^2
\right\rangle_{return}=1.
}
\]

On the anchored branch this is

\[
\langle\lambda_{eff}\rangle_{return}=1.
\]

This is a scalar vorticity-amplitude recurrence law.

It does **not** determine the whole-sphere energy current

\[
j=\int_{S^2}\mathcal J_r d\omega,
\]

which additionally depends on velocity-energy transport, pressure work, and viscous energy flux over the sphere.

Hence the historical scalar return balance does not supply one-dimensional slaving `j=F(production)`.

## 6. Marker migration remains a separate branch

If the active representative migrates across the persistent material surface, M5-596 correctly returns to the M5-520--522 surface-current/palinstrophy ledger.

Therefore

\[
\boxed{
\text{payer return}
\Longrightarrow
\text{same-marker inward/scalar balance}
\lor
\text{marker migration/surface-current branch}.
}
\]

Neither alternative presently conflicts with M19-304.

## 7. Consequence for the dynamic frontier

The strategy

\[
\text{recurrent production payer}
+
\text{required inward radial transport}
\Rightarrow
\text{contradiction}
\]

is a NO-GO.

The inward motion is already geometrically required by recurrent finite-depth material return.

The remaining question is more restrictive:

\[
\boxed{
\mathcal T_{phase}^{anchored/current}:
\text{does the anchored/projective production geometry constrain the phase of }j
\text{ strongly enough to forbid the exact return pattern?}
}
\]

## 8. Next target

M5-595 shows the anchored branch reduces to

\[
CE-T\lor CE-H,
\]

but even CE-H leaves scalar amplitude dynamics and a noncollinear companion.

The next audit should test whether either anchored subbranch actually forces `j` to be a single-valued function of the production state. If not, M19-289's hysteresis/factor branch is genuine even inside the anchored subsystem.

---

\[
\boxed{\text{M19-306 COMPLETE; INWARD RADIAL RETURN IS A CONSISTENCY CONDITION, NOT A CLOSURE CONTRADICTION.}}
\]