# DSD M5-194W — Local Leray Energy Pairing and Orthogonal-Shape Firewall

Date: 2026-08-29

Parent: `DSD_M5_194V_LERAY_SHAPE_SPEED_FOUR_CHANNEL_PDE_LEDGER_2026-08-29.md`

Status: **EXACT LOCAL ENERGY IDENTITIES + NEGATIVE SCALAR-CLOSURE FIREWALL / THE NONLINEAR AND SPATIAL-HOMOGENEITY CHANNELS HAVE EXACT VELOCITY-PAIRINGS GIVEN BY BOUNDARY KINETIC FLUX AND A BULK/BOUNDARY SCALING BALANCE / HOWEVER LARGE `L2` SHAPE CHANNELS CAN BE NEARLY ORTHOGONAL TO `V` AND THEREFORE INVISIBLE TO THIS SINGLE SCALAR ENERGY PROBE / SMALL BOUNDARY FLUX DOES NOT BY ITSELF FORCE SMALL NONLINEAR OR HOMOGENEITY-DEFECT NORMS / THE NEXT PROBE MUST USE VORTICITY/STRAIN DYNAMICS RATHER THAN VELOCITY ENERGY ALONE / GLOBAL REGULARITY UNPROVED.**

---

## 1. Setup

Use the Leray equation

\[
V_s
=
\Delta V
-\frac12\mathcal G_x[V]
-(V\cdot\nabla)V
-\nabla P,
\]

where

\[
\mathcal G_x[V]
:=V+(Y\cdot\nabla)V,
\qquad
\nabla\cdot V=0.
\]

Fix a ball `B_R` and write

\[
e=|V|^2.
\]

The goal is to determine what the velocity-energy pairing sees of the two unresolved shape channels from M5-194V.

---

## 2. Nonlinear transport pairing

By incompressibility,

\[
(V\cdot\nabla V)\cdot V
=\frac12V\cdot\nabla e
=\frac12\nabla\cdot(eV).
\]

Therefore

\[
\boxed{
\int_{B_R}
(V\cdot\nabla V)\cdot V\,dY
=
\frac12
\int_{\partial B_R}
e(V\cdot n)\,dS.
}
\]

Thus the component of nonlinear transport parallel to `V` is exactly a boundary kinetic-energy flux.

On a no-material-flux/quiet-boundary corridor this scalar pairing can be small.

But this says nothing about the norm

\[
\|V\cdot\nabla V\|_{L^2(B_R)}.
\]

---

## 3. Spatial homogeneity-defect pairing

Compute

\[
\int_{B_R}
\mathcal G_x[V]\cdot V
=
\int_{B_R}e
+
\frac12\int_{B_R}Y\cdot\nabla e.
\]

Use

\[
\nabla\cdot(Ye)=3e+Y\cdot\nabla e.
\]

Hence

\[
\int_{B_R}Y\cdot\nabla e
=
R\int_{\partial B_R}e\,dS
-3\int_{B_R}e\,dY.
\]

Therefore

\[
\boxed{
\int_{B_R}
\mathcal G_x[V]\cdot V\,dY
=
\frac R2
\int_{\partial B_R}|V|^2dS
-
\frac12
\int_{B_R}|V|^2dY.
}
\]

For an exactly degree-`-1` field on the ball-annulus geometry this is the expected critical scaling balance.

Again the identity measures only the component of `G_x[V]` in the `V` direction.

---

## 4. Pressure pairing

Since `div V=0`,

\[
\boxed{
\int_{B_R}\nabla P\cdot V\,dY
=
\int_{\partial B_R}P(V\cdot n)\,dS.
}
\]

Thus pressure does no bulk work in the velocity-energy pairing; it contributes only through the boundary.

This does not make the local pressure-gradient norm small.

A large harmonic pressure gradient can be nearly orthogonal to the velocity while maintaining small boundary work.

---

## 5. Diffusion pairing

Integration by parts gives

\[
\boxed{
\int_{B_R}\Delta V\cdot V\,dY
=
-\int_{B_R}|\nabla V|^2dY
+
\int_{\partial B_R}\partial_nV\cdot V\,dS.
}
\]

Unlike the transport and pressure terms, diffusion has a sign-definite interior contribution.

This is why the derivative channel is already naturally costed by the existing `H1`/dissipation ledgers.

---

## 6. Exact local Leray energy identity

Dot the full equation with `V` and combine the previous formulas.

One obtains

\[
\boxed{
\begin{aligned}
\frac12\frac d{ds}
\int_{B_R}|V|^2dY
+\int_{B_R}|\nabla V|^2dY
-\frac14\int_{B_R}|V|^2dY\\
+
\int_{\partial B_R}
\left[
-\partial_nV\cdot V
+\frac R4|V|^2
+\frac12|V|^2(V\cdot n)
+P(V\cdot n)
\right]dS
=0.
\end{aligned}
}
\]

This is the ball version of the global similarity-energy balance derived in M5-194P.

---

## 7. Quiet-boundary implication is only scalar

Suppose on a pure core corridor all boundary terms are small in the integrated energy ledger.

Then the identity constrains

\[
\frac d{ds}\int_{B_R}|V|^2,
\qquad
\int_{B_R}|\nabla V|^2,
\qquad
\int_{B_R}|V|^2.
\]

It does **not** produce an estimate of the form

\[
\|V\cdot\nabla V\|_2
\lesssim
\left|
\int(V\cdot\nabla V)\cdot V
\right|
\]

or

\[
\|\mathcal G_x[V]\|_2
\lesssim
\left|
\int\mathcal G_x[V]\cdot V
\right|.
\]

Such estimates are false without an angle/coercivity condition.

---

## 8. Orthogonal-shape countermechanism

Let `F` be any vector field on `B_R` with

\[
\langle F,V\rangle_{L^2(B_R)}=0.
\]

Then its contribution to the velocity-energy derivative vanishes even if

\[
\|F\|_2
\]

is arbitrarily large.

The same geometry can occur for the rotation-orthogonal shape components of

\[
V\cdot\nabla V,
\qquad
\mathcal G_x[V],
\qquad
\nabla P.
\]

Therefore

\[
\boxed{
\text{small scalar energy work}
\not\Rightarrow
\text{small shape forcing}.
}
\]

This is exactly analogous to M5-194U's finite-descriptor invisibility, now seen directly inside the PDE energy identity.

---

## 9. Consequence for the nonlinear channel

On the pure no-turnover boundary corridor, a large nonlinear channel with small boundary kinetic flux must satisfy approximately

\[
\boxed{
(V\cdot\nabla V)
\text{ is largely }L^2\text{-orthogonal to }V.
}
\]

Such an orthogonal nonlinear action changes direction/shape rather than total local kinetic energy at first order.

This makes the strain/vorticity/projective variables the correct next probe.

It cannot be classified as material export merely from the velocity-energy ledger.

---

## 10. Consequence for the homogeneity channel

Likewise, if

\[
\|\mathcal G_x[V]\|_2
\]

is large but the exact scalar balance

\[
\frac R2\int_{\partial B_R}|V|^2
-
\frac12\int_{B_R}|V|^2
\]

is small, then most of the spatial scale-shape defect is orthogonal to `V`.

Thus the core may strongly change its spatial organization while retaining an almost critical scalar energy scaling.

This is a genuine shape mode, not detected by energy scaling alone.

---

## 11. DSD verdict

### PROVED

- exact velocity pairings for nonlinear transport, spatial homogeneity defect, pressure, and diffusion;
- exact local Leray energy identity;
- boundary-quietness controls scalar work, not full forcing norms.

### CLOSED

The hoped shortcut

\[
\boxed{
\text{quiet boundary}
\Longrightarrow
N_R,H_R,P_R\text{ small}
}
\]

is false without an additional alignment/coercivity theorem.

### REDUCED

A large unresolved shape channel that avoids boundary/energy payment must act substantially in a direction orthogonal to the local velocity.

This points directly to vorticity/strain orientation dynamics.

---

## 12. Next audit target

Take curl of the Leray equation:

\[
\boxed{
\Omega_s
-
\Delta\Omega
+
\Omega
+
\frac12(Y\cdot\nabla)\Omega
+(V\cdot\nabla)\Omega
-(\Omega\cdot\nabla)V
=0.
}
\]

The next calculation should derive the local enstrophy pairing and split the two nonlinear vorticity channels into

- advective boundary transport;
- interior stretching/Betchov production.

Unlike velocity energy, the stretching term survives in the bulk and is already tied to the repository's strain/projective geometry.

This is the natural bridge from descriptor-invisible shape speed to the existing Betchov/H/projective ledgers.
