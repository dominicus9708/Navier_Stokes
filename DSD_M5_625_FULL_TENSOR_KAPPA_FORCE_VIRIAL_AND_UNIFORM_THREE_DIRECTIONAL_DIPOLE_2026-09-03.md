# DSD M5-625 — Full tensor kappa-force virial and uniform three-directional dipole

Date: 2026-09-03

Status: **INTERNAL TENSOR VIRIAL UPGRADE / THE GENERALIZED CE-H KAPPA FORCE `F_kappa=-2 div T` HAS THE EXACT FIRST-MOMENT MATRIX `int y_k (F_kappa)_j = 2 int partial_j W·partial_k W` / THE RIGHT SIDE IS THE SPATIAL-DERIVATIVE GRAM MATRIX, POSITIVE DEFINITE FOR EVERY NONZERO `L2(R3)` FIELD BECAUSE A ZERO DIRECTIONAL DERIVATIVE WOULD MAKE THE FIELD TRANSLATION-INVARIANT ALONG A LINE AND THEREFORE NON-L2 UNLESS ZERO / COMPACTNESS OF THE MARKED NONZERO HULL UPGRADES THIS TO A UNIFORM POSITIVE LOWER BOUND IN EVERY DIRECTION / THE KAPPA FORCE THEREFORE HAS A GENUINELY THREE-DIRECTIONAL DIPOLE, NOT MERELY ONE POSITIVE RADIAL TRACE / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Generalized kappa stress

Use the globally smooth stress tensor from M5-615--616,

\[
\boxed{
\mathbb T_{jk}
=
\partial_jW\cdot\partial_kW
-
\frac12
\left(
|\nabla W|^2+W\cdot\Delta W
\right)\delta_{jk}.
}
\]

Define

\[
\boxed{
(\mathcal F_\kappa)_j
:=-2\partial_k\mathbb T_{jk}.
}
\]

On the active set where

\[
\Delta W=\kappa W,
\]

this agrees with

\[
\mathcal F_\kappa=|W|^2\nabla\kappa.
\]

The stress formulation remains meaningful across the nodal set.

---

## 2. First-moment tensor

Multiply the force by `y_l` and integrate over `R3`.

Using the terminal-tail decay to remove the boundary term,

\[
\int y_l(\mathcal F_\kappa)_jdy
=-2\int y_l\partial_k\mathbb T_{jk}dy
=2\int\mathbb T_{jl}dy.
\]

Therefore

\[
\boxed{
\mathcal V_{jl}
:=
\int y_l(\mathcal F_\kappa)_jdy
=2\int\mathbb T_{jl}dy.
}
\]

---

## 3. The isotropic stress term cancels globally

The Rayleigh identity gives

\[
\int W\cdot\Delta Wdy=-P,
\]

while

\[
\int|\nabla W|^2dy=P.
\]

Hence

\[
\int
\left(
|\nabla W|^2+W\cdot\Delta W
\right)dy=0.
\]

Thus the isotropic part of the integrated stress disappears and

\[
\boxed{
\int\mathbb T_{jl}dy
=
\int\partial_jW\cdot\partial_lWdy.
}
\]

Consequently

\[
\boxed{
\mathcal V_{jl}
=
2\int\partial_jW\cdot\partial_lWdy.
}
\]

This is the full tensor form of the scalar M5-607 virial.

---

## 4. Positive-semidefinite structure

For every vector `e in R3`,

\[
e_j\mathcal V_{jl}e_l
=2\int|(e\cdot\nabla)W|^2dy.
\]

Therefore

\[
\boxed{
\mathcal V\ge0
}
\]

as a symmetric matrix.

Its trace is

\[
\operatorname{tr}\mathcal V
=2P,
\]

recovering M5-607.

---

## 5. Strict positivity for nonzero whole-space L2 fields

Suppose for a nonzero vector `e`,

\[
\int|(e\cdot\nabla)W|^2dy=0.
\]

Then

\[
(e\cdot\nabla)W=0
\]

almost everywhere, hence everywhere by smoothness.

Thus `W` is constant along every line parallel to `e`.

If `W` is nonzero at one point, it remains nonzero along the entire infinite line through that point, contradicting

\[
W\in L^2(\mathbb R^3).
\]

Therefore any nonzero whole-space CE-H state satisfies

\[
\boxed{
\int|(e\cdot\nabla)W|^2dy>0
\quad\forall |e|=1.
}
\]

Hence

\[
\boxed{\mathcal V>0}
\]

is positive definite.

---

## 6. Uniform compact-hull lower bound

Define

\[
\lambda_{min}(W)
:=
\min_{|e|=1}
2\int|(e\cdot\nabla)W|^2dy.
\]

The map

\[
(W,e)\mapsto
2\int|(e\cdot\nabla)W|^2dy
\]

is continuous on the product of

- the marked globally strong compact hull;
- the unit sphere `S2`.

M5-618 and the persistent carrier mark exclude `W=0`.

Since the value is strictly positive at every point of this compact product,

\[
\boxed{
\lambda_{min}(W)
\ge v_*>0
}
\]

uniformly on the marked CE-H component.

Equivalently,

\[
\boxed{
\mathcal V(W)\ge v_*I.
}
\]

---

## 7. Directional force-dipole law

For every unit vector `e`,

\[
\boxed{
\int
(e\cdot y)(e\cdot\mathcal F_\kappa)dy
=
2\|(e\cdot\nabla)W\|_2^2
\ge v_*.
}
\]

At the same time, the zero-net-force identity gives

\[
\boxed{
\int e\cdot\mathcal F_\kappa\,dy=0.
}
\]

Thus in **every spatial direction** the signed force must have separated positive and negative contributions with a fixed first-moment gap.

The earlier M5-616 separated-lobe conclusion is therefore not merely one-coordinate or trace-level: CE-H supports a full three-directional force-dipole architecture.

---

## 8. Finite-core localization

The endpoint spectator tail has vanishing high-Sobolev influence and the generalized force is built from derivatives up to third order.

Therefore for sufficiently large fixed `R_core`, the tensor moment outside `B_Rcore` is uniformly small.

Hence one may retain, after shrinking `v_*` by a fixed factor,

\[
\boxed{
\int_{B_{R_{core}}}
(e\cdot y)(e\cdot\mathcal F_\kappa)dy
\ge\frac12v_*
\quad\forall |e|=1.
}
\]

Thus the three-directional force architecture is a finite-active-core phenomenon rather than a tail artifact.

---

## 9. Relation to M5-617 coherent packets

M5-617 showed that a quantitative force lobe can be lifted, using compact derivative caps and Taylor thickening, to a nearby coherent nonzero-vorticity packet.

The tensor virial now forces such signed force structure in every direction.

However one may **not** infer six mutually distinct material-flux packets simply by choosing `+/-` lobes along three axes; the same coherent packet may contribute to several directional moments.

The valid conclusion is geometric rank, not packet count.

---

## 10. Consequence for lower-dimensional escape

A surviving CE-H state cannot have an exact translation-invariant direction.

In particular, any attempted reduction in which all active structure depends on only two Euclidean coordinates is incompatible with whole-space `L2` unless the solution is zero.

This does not exclude axisymmetric no-swirl flows: their fields vary through the cylindrical basis and are not translation invariant along a fixed Cartesian direction in the required sense.

---

## 11. Updated rigidity package

A nonzero marked CE-H state now has simultaneously

\[
\boxed{
\begin{aligned}
&\int\mathcal F_\kappa=0,\\
&\int y\otimes\mathcal F_\kappa
=2\int(\nabla W)^T\nabla W,\\
&\int y\otimes\mathcal F_\kappa\ge v_*I,\\
&\|W\times\operatorname{curl}W\|_2\ge b_*>0.
\end{aligned}
}
\]

So both the generalized viscous-eigenvalue force and the non-Beltrami geometry are genuinely full-dimensional.

---

## 12. Next target

The M5-623 simple-gap branch contains a finite-core `nabla Sigma` charge, while this note gives a positive-definite `nabla W` Gram tensor.

The next useful comparison is whether the strain-derivative source can be bounded/coercively attributed to the same derivative Gram tensor through the Biot–Savart/Riesz operator, or whether a harmonic-cancellation branch remains.

A second target is to apply the tensor virial to the forced `P nabla kappa` branch of M5-622.

---

## 13. Firewall

Positive definiteness of the first-moment tensor is not a monotonicity statement and is not itself a contradiction.

No packet multiplicity is inferred from matrix rank alone.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
