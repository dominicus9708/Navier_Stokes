# DSD M19-111 — After phase and rotation quotient, the RDSS fixed-point problem is identity-minus-compact and branch creation requires an extra unit multiplier or compactness loss

Date: 2026-09-12

Status: **ACTIVE M19 CALCULATION / FREDHOLM-CONTINUATION FORMULATION OF THE PERIODIC/RELATIVE-PERIODIC HARD CORE / NONTRIVIAL BRANCH CREATION OR TERMINATION INSIDE A COMPACT PARAMETER CORRIDOR REQUIRES LOSS OF QUOTIENT NONDEGENERACY, I.E. AN EXTRA UNIT FLOQUET MULTIPLIER / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Twisted Poincare fixed-point equation

For parameter

\[
p=(S,Q_*)
\]

or equivalently a scale/rotation parameterization such as `(S,alpha,A)`, let

\[
\mathcal P_p:X\to X
\]

be the twisted period map on a retained smooth vorticity phase space `X`:

\[
\mathcal P_p(\omega_0)
=Q_*^{-1}\omega(S;\omega_0).
\]

A DSS/RDSS orbit corresponds to

\[
\boxed{
F(p,\omega)
:=
\omega-\mathcal P_p(\omega)
=0.
}
\]

Positive-time parabolic smoothing makes the nonlinear part of `P_p` compact on bounded smooth corridors after the standard localization/tail controls of M19-095.

Thus

\[
\boxed{
F(p,\cdot)
=
I-\text{compact}
}
\]

in the Fredholm sense on the retained quotient phase space.

---

## 2. Remove exact symmetry kernels first

Before testing invertibility one must quotient/fix gauges for:

- similarity-time phase;
- spatial rotations compatible with the orbit;
- center position and blowup-time gauges already classified as noncenter similarity modes.

After these symmetry conditions, write

\[
X_{red}
\]

for the reduced phase space.

The derivative is

\[
D_\omega F
=I-\mathcal M_p^{tw},
\]

where

\[
\mathcal M_p^{tw}
\]

is the twisted monodromy.

M19-109 places its essential spectrum strictly inside the unit disk.

Therefore

\[
D_\omega F:X_{red}\to X_{red}
\]

is Fredholm of index zero.

---

## 3. Nondegeneracy criterion

On the reduced phase space,

\[
D_\omega F
\]

is invertible exactly when

\[
\boxed{
1\notin
\sigma(\mathcal M_p^{tw}|_{X_{red}}).
}
\]

Equivalently, there is no extra symmetry-transverse unit Floquet multiplier.

This is the periodic/RDSS version of the M19 extra-center theorem.

If invertible, the implicit-function theorem gives a unique local solution branch

\[
\omega=\omega(p)
\]

through that point.

Hence a nondegenerate branch cannot simply start or stop at an interior parameter value.

---

## 4. How a new branch can appear

Inside a parameter region where the retained a priori bounds remain compact, a nontrivial periodic/RDSS branch can be created or destroyed only if at least one of the following occurs:

1. **extra unit multiplier**
   \[
   1\in\sigma(\mathcal M_p^{tw}|_{X_{red}});
   \]
2. **loss of compactness/a priori bounds**, so the Fredholm corridor itself fails;
3. **parameter-boundary entry**, where the branch enters from outside the parameter domain under study.

Therefore

\[
\boxed{
\text{interior saddle-node / pitchfork / isola turning point}
\Longrightarrow
\text{extra unit Floquet multiplier}
}
\]

after the exact symmetries have been quotiented.

---

## 5. No-small-solution result revisited

M19-110 gives a neighborhood of the zero profile containing no nontrivial DSS/RDSS solution when

\[
S\ge S_*>0.
\]

Thus a surviving branch cannot be born by an infinitesimal bifurcation from zero in that corridor.

Combined with M19-111, a disconnected finite-amplitude branch would have to be sustained by:

- an interior fold/degeneracy with an extra unit multiplier;
- a loss of compactness;
- or entry from another parameter boundary.

This sharply narrows the topology of a possible moderate-parameter survivor.

---

## 6. Degree formulation

Because the fixed-point equation is identity minus compact, a Leray--Schauder degree can be assigned on bounded open sets containing no boundary solutions.

At the zero profile, M19-110 gives

\[
I-D\mathcal P_p(0)
\]

invertible for `S>=S_*`, so the local degree is well defined and nonzero.

A complete global degree computation is not supplied here.

However the framework shows exactly what would be needed to exclude disconnected nonzero components: a priori compactness plus invariance of the reduced fixed-point degree from a parameter region known to contain no nontrivial solutions.

---

## 7. Major structural consequence

The periodic/RDSS Liouville problem and the aperiodic extra-center problem are not fully independent.

The same spectral obstruction appears in both:

\[
\boxed{
\text{extra zero-growth center direction}
\longleftrightarrow
\text{extra unit Floquet multiplier on a periodic/RDSS orbit}.
}
\]

Thus proving the symmetry-only-center theorem uniformly on the compact recurrent corridor would also remove the standard local mechanism by which moderate RSS/RDSS branches are born or turn.

---

## 8. Firewall

Nondegeneracy alone does not exclude a pre-existing global branch that enters through a parameter boundary or escapes every a priori compact set.

Therefore

\[
\boxed{
\text{no extra unit multiplier}
\neq
\text{global RDSS nonexistence}
}
\]

without a continuation/compactness argument.

---

## 9. Next target

The highest-value next theorem is now a continuation bridge:

\[
\boxed{
\mathcal T_{cont}:
\begin{array}{l}
\text{on a connected moderate parameter corridor,}\
\text{if all periodic/RDSS solutions are uniformly compact and quotient-nondegenerate,}\
\text{and one boundary parameter region is Liouville-empty,}\
\text{then the entire corridor is Liouville-empty.}
\end{array}
}
\]

This would merge the periodic hard core with the same extra-center theorem already needed for aperiodic recurrence.

---

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
