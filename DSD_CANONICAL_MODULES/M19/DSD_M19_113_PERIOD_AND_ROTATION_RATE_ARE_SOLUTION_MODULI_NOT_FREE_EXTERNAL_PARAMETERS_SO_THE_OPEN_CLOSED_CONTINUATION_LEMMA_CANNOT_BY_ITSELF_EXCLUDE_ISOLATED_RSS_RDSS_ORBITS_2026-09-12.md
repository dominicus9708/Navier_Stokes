# DSD M19-113 — Period and rotation rate are solution moduli, not free external parameters, so the open-closed continuation lemma cannot by itself exclude isolated RSS/RDSS orbits

Date: 2026-09-12

Status: **ACTIVE M19 AUDIT CORRECTION INSIDE THE CALCULATION PHASE / M19-111--112 FREDHOLM CONTINUATION REMAINS VALID FOR A GENUINE EXTERNAL PARAMETER FAMILY, BUT `S` AND `ALPHA` OF RSS/RDSS ARE GENERALLY UNKNOWN MODULI SELECTED BY THE ORBIT / THEY CANNOT BE TREATED AS ARBITRARY EXTERNAL PARAMETERS WITHOUT AN AUGMENTED SOLVABILITY ANALYSIS / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. The issue

M19-111--112 formulated a useful identity-minus-compact continuation principle for a fixed-point equation

\[
F(p,\omega)=0
\]

with a genuine external parameter `p`.

It is tempting to put

\[
p=S
\]

or

\[
p=\alpha
\]

for DSS/RDSS/RSS and then argue that nondegeneracy gives a local graph over those parameters.

That step is not automatic.

For the original autonomous Navier--Stokes similarity flow:

- the period `S` of a periodic orbit is an **unknown of the orbit**;
- the rotation drift `alpha` of a relative equilibrium/relative periodic orbit is a **group-velocity modulus** selected by the solution.

They are not externally prescribed coefficients of the original PDE.

---

## 2. Standard periodic-orbit sanity check

For an autonomous finite-dimensional ODE, a hyperbolic periodic orbit is isolated up to time phase.

Its period is generally isolated as well.

There is no family of nearby periodic orbits with every nearby period.

Therefore any argument claiming

\[
\text{hyperbolic/nondegenerate periodic orbit}
\Longrightarrow
\text{solution for all nearby }S
\]

must be wrong unless another true external parameter is present.

This sanity check applies equally to the similarity Navier--Stokes flow.

---

## 3. Why the naive fixed-period implicit-function argument fails

Consider

\[
F(S,\omega_0)
=
\Phi_S(\omega_0)-\omega_0,
\]

where `Phi_S` is the autonomous flow map.

At a periodic orbit,

\[
D_{\omega}F
=
\mathcal M_S-I
\]

has the time-tangent kernel

\[
\partial_s\omega.
\]

One cannot simply quotient that kernel and then regard `S` as an external free parameter without also tracking the corresponding phase/cokernel solvability condition.

The correct periodic-orbit formulation uses an **augmented system**:

\[
\boxed{
\begin{cases}
\Phi_S(\omega)-\omega=0,\\
\mathcal G(\omega)=0,
\end{cases}
}
\]

where `G` is a phase condition and `S` is itself an unknown.

The derivative is taken with respect to

\[
(S,\omega),
\]

not merely `omega` with `S` held as a free external continuation coordinate.

A nondegenerate periodic orbit is then locally isolated modulo phase, exactly as expected.

---

## 4. Relative periodic/RDSS case

For RDSS one must augment further by the rotation holonomy/group phase.

Schematically the unknowns are

\[
(S,Q_*,\omega),
\]

subject to

\[
Q_*^{-1}\Phi_S(\omega)-\omega=0
\]

plus phase and rotation gauge conditions.

Likewise RSS solves a relative-equilibrium equation in which

\[
\alpha
\]

is an unknown group velocity, not a free external physical coefficient.

Thus isolated relative equilibria or relative periodic orbits may occur at isolated values of `alpha` or `(S,Q_*)` without requiring an extra unit Floquet multiplier beyond the standard symmetry directions.

---

## 5. Correct scope of M19-112

The open-closed continuation lemma remains valid if one truly has an **external parameter family of equations** or a parameterized reduced problem for which:

1. the parameter is prescribed independently of the orbit;
2. the reduced derivative with respect to the state is invertible;
3. the solution set is compact.

But the lemma cannot be applied directly to the endogenous orbit moduli

\[
S,\alpha,Q_*
\]

of the single autonomous Navier--Stokes similarity equation.

Therefore the proposed shortcut

\[
\text{one empty alpha/S value}
+\text{nondegeneracy}
\Rightarrow
\text{all RSS/RDSS absent}
\]

is **not certified**.

---

## 6. What survives from M19-111

The following statements remain valid and useful:

- the twisted monodromy is identity-minus-compact/Fredholm after symmetry bookkeeping;
- an extra unit multiplier marks a genuine loss of periodic-orbit nondegeneracy;
- saddle-node or other branch degeneracies in a genuine external continuation problem require such a kernel;
- local bifurcation from the zero profile is blocked by M19-110 on a positive-period corridor.

What is withdrawn is only the overstrong claim that intrinsic period/group-velocity moduli can be used as free connected external parameters to eliminate all isolated orbits.

---

## 7. Revised periodic/RDSS frontier

The periodic hard core therefore remains

\[
\boxed{
\text{finite-amplitude isolated RSS/RDSS orbits may exist even if their twisted unit multiplier is symmetry-only.}
}
\]

To exclude them one needs a true Liouville/virial/monotonicity argument, or a valid external-parameter degree framework not presently supplied.

Thus the periodic/RDSS theorem does **not** collapse completely into the extra-center theorem.

---

## 8. Permanent correction

Add the firewall

\[
\boxed{
\text{orbit period/group drift}
\neq
\text{free external PDE parameter}.
}
\]

This prevents misuse of abstract continuation theory in later modules.

---

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
