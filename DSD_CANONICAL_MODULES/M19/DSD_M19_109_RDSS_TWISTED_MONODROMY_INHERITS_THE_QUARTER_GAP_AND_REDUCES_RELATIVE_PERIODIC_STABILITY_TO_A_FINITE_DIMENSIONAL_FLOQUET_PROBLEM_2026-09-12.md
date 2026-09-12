# DSD M19-109 — RDSS twisted monodromy inherits the quarter-gap and reduces relative-periodic stability to a finite-dimensional Floquet problem

Date: 2026-09-12

Status: **ACTIVE M19 CALCULATION / M19-095 QUASI-COMPACTNESS EXTENDED FROM DSS TO RDSS BY A UNITARY HOLONOMY TWIST / UNIT-CIRCLE TWISTED FLOQUET SPECTRUM IS DISCRETE WITH FINITE MULTIPLICITY / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. RDSS orbit

Let a relative-periodic similarity solution satisfy

\[
\boxed{
U(s+S)=Q_*\cdot U(s),
\qquad Q_*\in SO(3),
\qquad S>0.
}
\]

In physical variables this corresponds to a discrete scale-rotation symmetry with

\[
\lambda=e^{S/2}>1.
\]

Let

\[
\mathcal U(s_2,s_1)
\]

denote the linearized vorticity evolution along the orbit.

---

## 2. Ordinary monodromy changes the fiber by rotation

After one period,

\[
\mathcal U(s+S,s)
\]

maps perturbations at `U(s)` to perturbations at the rotated state `Q_* U(s)`.

To compare perturbations in the same fiber, undo the holonomy rotation.

Define the twisted monodromy

\[
\boxed{
\mathcal M_S^{tw}
:=
Q_*^{-1}\mathcal U(s+S,s).
}
\]

Here `Q_*^{-1}` acts by the natural rotation representation on vector/vorticity fields.

The RDSS linear stability problem is therefore the spectrum of

\[
\mathcal M_S^{tw}.
\]

---

## 3. Rotation is unitary

In unweighted vorticity `L2`, and in every radial weighted geometry used in M19,

\[
\boxed{
\|Q_*F\|=\|F\|.
}
\]

Hence left multiplication by `Q_*^{-1}` does not change operator norm, essential norm, compactness, or essential spectral radius.

---

## 4. M19-095 quasi-compact decomposition

M19-095 gives, over any fixed positive time interval on the controlled critical-tail corridor,

\[
\mathcal U(s+S,s)
=
 e^{S\mathcal L_0}
+\mathcal C_S,
\]

with

\[
\mathcal C_S
\]

compact and

\[
\left\|e^{S\mathcal L_0}\right\|
\le e^{-S/4}.
\]

Therefore

\[
\mathcal M_S^{tw}
=
Q_*^{-1}e^{S\mathcal L_0}
+Q_*^{-1}\mathcal C_S.
\]

The second term is compact.

Because the bare generator is rotationally invariant,

\[
Q_*^{-1}e^{S\mathcal L_0}
=e^{S\mathcal L_0}Q_*^{-1},
\]

and its norm remains at most

\[
e^{-S/4}.
\]

Hence

\[
\boxed{
 r_{ess}(\mathcal M_S^{tw})
\le e^{-S/4}<1.
}
\]

---

## 5. Discrete twisted Floquet spectrum

Since the essential spectrum lies strictly inside the unit circle, every twisted Floquet multiplier satisfying

\[
|\mu|>e^{-S/4}
\]

is an isolated eigenvalue of finite algebraic multiplicity, with possible accumulation only toward the essential disk.

In particular, all unit-circle multipliers are discrete:

\[
\boxed{
\sigma(\mathcal M_S^{tw})\cap\{|\mu|=1\}
\text{ consists of finitely many isolated finite-multiplicity eigenvalues.}
}
\]

Thus RDSS has no continuous unit-circle tail spectrum on the retained corridor.

---

## 6. Symmetry multipliers

The relative-periodic time/scaling tangent produces the neutral twisted multiplier

\[
\mu=1.
\]

Rotational symmetry directions compatible with the orbit/isotropy also contribute unit multipliers after the symmetry quotient is undone.

The physical translation, singular-time-shift and Galilean gauge multipliers remain off the unit circle as classified in M19-099, with the appropriate twisted representation.

Therefore the nondegeneracy problem is finite-dimensional:

\[
\boxed{
\ker(I-\mathcal M_S^{tw})
\stackrel{?}{=}
\text{symmetry-generated neutral space}.
}
\]

---

## 7. Consequence for the M19 frontier

Ordinary DSS and RDSS now share the same structural endpoint:

\[
\boxed{
\text{periodic/relative-periodic critical survivor}
\Longrightarrow
\text{finite-dimensional unit-multiplier Fredholm problem}.
}
\]

The rotation holonomy changes the finite-dimensional matrix/eigenvalue problem but not the negative essential spectral bound.

---

## 8. Firewall

A discrete finite-multiplicity unit-circle spectrum does not imply that there are no extra unit multipliers.

Nor does Floquet nondegeneracy imply nonlinear nonexistence of the periodic/RDSS orbit.

Hence

\[
\boxed{
\text{twisted quasi-compactness}
\neq
\text{RDSS Liouville theorem}.
}
\]

---

## 9. Next target

At the zero background the twisted bare monodromy has spectral radius strictly below one.

Therefore a nontrivial RSS/RDSS cannot bifurcate infinitesimally from zero unless the period degenerates to zero or another parameter destroys the gap.

The next calculation should turn this into a quantitative finite-amplitude floor for every periodic/relative-periodic survivor with a fixed positive period floor.

---

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
