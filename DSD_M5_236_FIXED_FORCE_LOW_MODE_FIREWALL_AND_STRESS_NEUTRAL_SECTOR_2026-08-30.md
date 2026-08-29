# DSD M5-236 — Fixed-Force Low-Mode Firewall and Stress-Neutral Sector

Date: 2026-08-30

Parent: `DSD_M5_235_RECURRENT_RADIAL_STRAIN_IDENTITY_AND_BRANCH_MERGER_2026-08-30.md`

Status: **SCOPE FIREWALL / THE POINT-FORCE VECTOR FIXES ONLY THE NET SPHERICAL MOMENTUM-STRESS FLUX AND ZERO TORQUE FIXES ONLY THE CORRESPONDING ANTISYMMETRIC FIRST MOMENT / THESE FINITE-DIMENSIONAL CHARGES DO NOT DETERMINE THE FULL RECURRENT SPHERICAL STRAIN PROFILE / EXISTING LARGE-SPACE STATIONARY UNIQUENESS AND LANDAU ASYMPTOTIC RESULTS REMAIN PERTURBATIVE / THE LARGE FIXED-FORCE STRESS-NEUTRAL HIGH-MODE SECTOR IS A GENUINE OPEN STATIONARY ENDPOINT / GLOBAL REGULARITY UNPROVED.**

---

## 1. Fixed point-force equation

The stationary branch obtained in M5-227 satisfies on the whole space in distributions

\[
\boxed{
-\nu\Delta T
+(T\cdot\nabla)T
+\nabla P
=b\,\delta_0,
\qquad
\nabla\cdot T=0.
}
\]

The point-force vector is the spherical momentum-stress flux

\[
\boxed{
b
=
\int_{S_r}\mathbb S(T,P)n\,dS,
}
\]

independent of `r`.

M5-227 also gives exact zero torque.

---

## 2. Log-cylinder stress coefficient

Write

\[
T=r^{-1}\Phi(y,\theta),
\qquad
P=r^{-2}\Pi(y,\theta).
\]

The stationary stress has degree `-2`:

\[
\mathbb S(T,P)
=
r^{-2}\mathbb S_\Phi(y,\theta).
\]

Hence

\[
\boxed{
b
=
\int_{S^2}
\mathbb S_\Phi(y,\theta)\theta
\,d\theta
}
\]

for every `y`.

Thus fixed point force supplies exactly three scalar constraints on each log cell.

Zero torque supplies another three first-moment constraints.

These are finite-dimensional moment conditions.

---

## 3. Force-neutral stress sector

Define the force projection

\[
\mathcal P_F[\mathbb S_\Phi]
:=
\int_{S^2}\mathbb S_\Phi\theta\,d\theta.
\]

Then the fixed-force condition is

\[
\mathcal P_F[\mathbb S_\Phi]=b.
\]

Any perturbation `delta S` satisfying

\[
\boxed{
\int_{S^2}\delta\mathbb S\,\theta\,d\theta=0
}
\]

is invisible to the force charge.

Likewise the zero-torque condition removes only the corresponding torque-visible moments.

The intersection of these kernels is still infinite dimensional.

Therefore

\[
\boxed{
\text{fixed force + zero torque}
\not\Rightarrow
\text{Landau spherical stress shape}.
}
\]

---

## 4. Dilation tangent is force neutral

Every dilation `D_hT` solves the same point-force problem because the Dirac forcing is exactly scale invariant in three dimensions.

Differentiate the force identity in `h` at zero.

For the dilation tangent

\[
\mathcal H_T
=T+x\cdot\nabla T,
\]

one obtains

\[
\boxed{
\delta b[\mathcal H_T]=0.
}
\]

Thus the nontrivial scale generator identified in M5-228 is automatically a **fixed-force-neutral linearized mode**.

It lives precisely in the sector not controlled by the three force coordinates.

---

## 5. Relation to Landau-family modes

For the Landau family the natural parameter variations change the point-force vector `b` in magnitude and/or orientation.

Those modes are excluded by the fixed-force condition.

Therefore a surviving nonzero

\[
\mathcal H_T
\]

cannot be dismissed as the ordinary Landau parameter tangent.

It would represent a genuinely new fixed-force kernel direction.

---

## 6. Literature scope

Known stationary results establish uniqueness/stability or Landau asymptotics under small critical data/force assumptions.

The large-amplitude problem

\[
|T(x)|\le C|x|^{-1}
\]

with arbitrary `C` and fixed point force is not covered by those perturbative uniqueness results.

Likewise the existing stationary DSS bifurcation analysis near Landau solutions supplies partial nondegeneracy and numerical evidence, not a full arbitrary-large fixed-force classification.

Therefore the implication

\[
\boxed{
-\nu\Delta T+(T\cdot\nabla)T+\nabla P=b\delta_0,
\quad |T|\lesssim1/r
\Rightarrow
T=\text{Landau}(b)
}
\]

is not imported as a theorem.

---

## 7. Consequence for M5-235

M5-235 gives a fixed recurrent strain-energy floor on the surviving stationary branch.

The force and torque charges do not control the force-neutral higher spherical/logarithmic modes that can carry this strain.

Thus

\[
\boxed{
\text{large recurrent strain}
+
\text{fixed force}
}

remains compatible at the level of currently proved identities.

The correct remaining stationary object is

\[
\boxed{
\text{large-amplitude fixed-force stationary solution}
+
\text{nontrivial stress-neutral dilation mode}.
}
\]

---

## 8. DSD verdict

### CLOSED SHORTCUT

Net force cannot be used as if it determined the entire spherical strain/stress field.

### SURVIVING STATIONARY SECTOR

An infinite-dimensional fixed-force/zero-torque neutral sector remains.

### STRATEGIC CONSEQUENCE

Further progress on this branch requires either:

1. a true arbitrary-large fixed-force uniqueness/nondegeneracy theorem;
2. a new PDE identity controlling the stress-neutral sector;
3. or returning to the residual-active branch, which is not subject to the stationary classification bottleneck.

The next audit follows option 3.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]