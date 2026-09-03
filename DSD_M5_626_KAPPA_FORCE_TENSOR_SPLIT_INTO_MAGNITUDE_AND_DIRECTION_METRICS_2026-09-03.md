# DSD M5-626 — Kappa-force tensor split into magnitude and direction metrics

Date: 2026-09-03

Status: **INTERNAL GEOMETRIC TENSOR DECOMPOSITION / THE FULL CE-H KAPPA-FORCE DIPOLE MATRIX FROM M5-625 SPLITS EXACTLY AS `V = 2 G_mag + 2 G_dir`, WHERE `G_mag_jk=int partial_j rho partial_k rho` AND `G_dir_jk=int rho^2 partial_j xi·partial_k xi` ARE POSITIVE-SEMIDEFINITE MAGNITUDE AND DIRECTION METRICS / BECAUSE `W·nabla kappa=0`, THE GENERALIZED VISCOUS-EIGENVALUE FORCE IS TRANSVERSE TO THE VORTEX LINES ON THE ACTIVE SET / THUS THE STRICTLY POSITIVE THREE-DIRECTIONAL DIPOLE IS GENERATED ENTIRELY BY CROSS-LINE MAGNITUDE/DIRECTION STRUCTURE, NOT BY ALONG-LINE KAPPA VARIATION / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Input from the full tensor virial

M5-625 gives

\[
\boxed{
\mathcal V_{jk}
:=
\int y_k(\mathcal F_\kappa)_jdy
=2\int\partial_jW\cdot\partial_kWdy.
}
\]

On the marked CE-H hull,

\[
\boxed{
\mathcal V\ge v_*I>0.
}
\]

---

## 2. Magnitude-direction derivative identity

Write

\[
W=\rho\xi,
\qquad |\xi|=1.
\]

Then

\[
\partial_jW
=(\partial_j\rho)\xi
+\rho\partial_j\xi.
\]

Because

\[
\xi\cdot\partial_j\xi=0,
\]

we obtain for every pair `j,k`

\[
\boxed{
\partial_jW\cdot\partial_kW
=
(\partial_j\rho)(\partial_k\rho)
+
\rho^2\partial_j\xi\cdot\partial_k\xi.
}
\]

---

## 3. Define the two metric tensors

Define the magnitude-gradient Gram matrix

\[
\boxed{
(\mathcal G_{mag})_{jk}
:=
\int
(\partial_j\rho)(\partial_k\rho)dy,
}
\]

and the weighted direction-gradient Gram matrix

\[
\boxed{
(\mathcal G_{dir})_{jk}
:=
\int
\rho^2\partial_j\xi\cdot\partial_k\xi\,dy.
}
\]

Both are symmetric positive semidefinite.

The full derivative Gram tensor is

\[
\boxed{
\mathcal G_W
=\mathcal G_{mag}+\mathcal G_{dir}.
}
\]

Thus

\[
\boxed{
\mathcal V
=2\mathcal G_{mag}+2\mathcal G_{dir}.
}
\]

This is an exact tensor refinement of

\[
P=P_{mag}+P_{dir}.
\]

---

## 4. Directional form

For every unit vector `e`,

\[
\boxed{
\frac12e^T\mathcal Ve
=
\|(e\cdot\nabla)\rho\|_2^2
+
\int\rho^2|(e\cdot\nabla)\xi|^2dy.
}
\]

Since M5-625 gives

\[
e^T\mathcal Ve\ge v_*,
\]

we have

\[
\boxed{
\|(e\cdot\nabla)\rho\|_2^2
+
\int\rho^2|(e\cdot\nabla)\xi|^2dy
\ge\frac12v_*
\quad\forall |e|=1.
}
\]

Thus **every Euclidean direction** carries either magnitude variation or direction variation of a fixed combined amount.

---

## 5. Kappa force is transverse to vortex lines

M5-600 gives

\[
\boxed{W\cdot\nabla\kappa=0.}
\]

On the active set `W=rho xi`, this is

\[
\boxed{\xi\cdot\nabla\kappa=0.}
\]

Hence

\[
\boxed{\nabla\kappa=P_\xi^\perp\nabla\kappa.}
\]

There the generalized force is

\[
\boxed{
\mathcal F_\kappa
=\rho^2\nabla\kappa
\perp\xi.
}
\]

Therefore all viscous-eigenvalue force acts across vortex lines, never along them.

---

## 6. Level-set geometry

At every regular point of `kappa`,

\[
\nabla\kappa\ne0,
\]

and the level set

\[
\{\kappa=c\}
\]

is locally a surface with normal `nabla kappa`.

Since

\[
W\cdot\nabla\kappa=0,
\]

vortex lines lie tangent to the instantaneous `kappa` level surfaces.

Thus

\[
\boxed{
\text{vortex lines are contained in instantaneous kappa-level surfaces.}
}
\]

The force `F_kappa` is normal to those surfaces.

This gives a quotient-like geometry: `kappa` varies only between vortex lines, not along one line.

---

## 7. Relation to persistent material flux

For an infinitesimal material vortex line/tube label,

\[
D_B\log|\phi|=\kappa.
\]

Because `kappa` is spatially constant along the full instantaneous vortex line, every infinitesimal cross-section based on that same line samples the same instantaneous flux multiplier.

Thus sign changes of `kappa` on a persistent line are whole-line label events rather than isolated point fluctuations along that line.

This strengthens the interpretation of the viscous turnover branch from M5-606/M5-621.

---

## 8. Tensor force cannot be paid by purely along-line magnitude change

Suppose hypothetically that

\[
P_\xi^\perp\nabla\rho=0
\]

and

\[
P_\xi^\perp\nabla\xi=0
\]

throughout the active field.

Then all variation would occur only along vortex lines.

But the kappa force is transverse and its first-moment tensor is uniformly positive definite:

\[
\mathcal V\ge v_*I.
\]

The derivative-metric decomposition shows that a full-rank `V` requires genuine cross-line magnitude and/or direction structure.

This is consistent with the M5-619 non-Beltrami split and makes the cross-line nature quantitative.

---

## 9. A rank firewall

Although

\[
\mathcal G_{mag}+\mathcal G_{dir}\ge\frac12v_*I,
\]

neither `G_mag` nor `G_dir` must be positive definite individually.

For example one may carry one direction through magnitude variation and another through direction variation.

Therefore no conclusion of the form

\[
\mathcal G_{mag}\ge cI
\]

or

\[
\mathcal G_{dir}\ge cI
\]

is made without an additional argument.

---

## 10. Relation to M5-622 forced branch

The M5-622 forcing is

\[
F_\gamma=P_\xi^\perp\nabla(\sigma+\kappa).
\]

The `kappa` part is exactly a cross-line derivative, because

\[
P_\xi^\perp\nabla\kappa=\nabla\kappa.
\]

Thus the branch

\[
|P\nabla\kappa|\ge c
\]

is not a new orientation artifact: it is a fixed `kappa`-level-surface force event.

Combined with the tensor virial, its recurrence must be understood as recurrent reorganization of the cross-vortex-line level-set geometry.

---

## 11. Updated CE-H geometry

A surviving CE-H component must maintain

\[
\boxed{
\mathcal G_{mag}+\mathcal G_{dir}
\ge\frac12v_*I
}
\]

while its vortex lines remain material and tangent to `kappa` level surfaces.

Thus the hard core is no longer merely a collection of material tubes: it is a recurrent three-dimensional family of vortex lines embedded in and moving through a cross-line scalar `kappa` foliation.

---

## 12. Next target

The next high-value calculation is the material evolution of `kappa` level surfaces.

M5-611 already shows

\[
W\cdot\nabla(D_B^m\kappa)=0
\]

for every fixed `m`.

The next question is whether the normal `nabla kappa` has a material transport law analogous to the transverse magnitude gradient and whether its level-surface Jacobian can recur while the material flux cocycle has zero mean.

---

## 13. Firewall

The statement that vortex lines lie in `kappa` level surfaces is instantaneous. A material vortex line may move from one `kappa` value to another because `D_B kappa` need not vanish.

No claim is made that the `kappa` level surfaces themselves are material surfaces.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
