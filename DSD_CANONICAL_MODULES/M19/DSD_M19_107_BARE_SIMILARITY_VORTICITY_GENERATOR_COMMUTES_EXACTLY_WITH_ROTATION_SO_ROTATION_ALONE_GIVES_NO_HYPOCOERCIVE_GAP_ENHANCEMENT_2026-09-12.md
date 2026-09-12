# DSD M19-107 — Bare similarity-vorticity generator commutes exactly with rotation, so rotation alone gives no hypocoercive gap enhancement

Date: 2026-09-12

Status: **ACTIVE M19 CALCULATION / EXACT COMMUTATOR IDENTITY / THE ROTATING BARE LINEAR SEMIGROUP FACTORS INTO OU-DIFFUSION TIMES A UNITARY ROTATION / ALL ALPHA-DEPENDENCE IN RSS/RDSS RIGIDITY MUST THEREFORE COME FROM BACKGROUND/NONLINEAR GEOMETRY, NOT FROM THE BARE LINEAR GAP / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Bare vorticity generator

Use

\[
\boxed{
\mathcal L_0
=\nu\Delta-1-\frac12y\cdot\nabla.
}
\]

For a rotation generator

\[
\mathcal J_AF
=AF-(Ay)\cdot\nabla F,
\qquad A^T=-A,
\]

consider the rotating bare operator

\[
\mathcal L_{0,\alpha}
=\mathcal L_0+\alpha\mathcal J_A.
\]

---

## 2. Exact commutation

The Laplacian is rotationally invariant, hence

\[
[\Delta,\mathcal J_A]=0.
\]

Dilation and rotation also commute:

\[
[y\cdot\nabla,\mathcal J_A]=0.
\]

The scalar multiplication term commutes trivially.

Therefore

\[
\boxed{
[\mathcal L_0,\mathcal J_A]=0.
}
\]

This is exact and parameter independent.

---

## 3. Semigroup factorization

Because the generators commute,

\[
\boxed{
 e^{t(\mathcal L_0+\alpha\mathcal J_A)}
=
e^{t\mathcal L_0}e^{t\alpha\mathcal J_A}.
}
\]

In every radial `L2` geometry retained in M19-105,

\[
 e^{t\alpha\mathcal J_A}
\]

is unitary.

Hence

\[
\boxed{
\left\|e^{t(\mathcal L_0+\alpha\mathcal J_A)}\right\|
=
\left\|e^{t\mathcal L_0}\right\|.
}
\]

In particular the bare vorticity quarter-gap remains exactly

\[
\boxed{
\left\|e^{t(\mathcal L_0+\alpha\mathcal J_A)}\right\|_{L^2\to L^2}
\le e^{-t/4}
}
\]

with no improvement and no degradation from `alpha`.

---

## 4. No bare hypocoercive enhancement

Hypocoercive enhancement requires a skew part that does not commute with the dissipative/confining part so that repeated commutators transfer undamped directions into damped ones.

Here

\[
[\mathcal L_0,\mathcal J_A]=0,
\]

so the standard commutator mechanism is absent.

Therefore

\[
\boxed{
\text{large rotation rate alone cannot improve the bare similarity spectral gap.}
}
\]

Likewise small rotation cannot weaken it at the bare level.

---

## 5. Where alpha-dependence can enter

For an RSS/RDSS background the full linearized operator is schematically

\[
\mathcal L_{full,\alpha}
=
\mathcal L_0
+\alpha\mathcal J_A
+\mathcal K_U.
\]

The only place where rotation-rate effects can alter stability/coercivity is through the interaction

\[
\boxed{
[\mathcal J_A,\mathcal K_U],
}
\]

or through the `alpha`-dependence of the nonlinear background profile `U` itself.

If the background is exactly axisymmetric with respect to the same rotation axis, then

\[
[\mathcal J_A,\mathcal K_U]=0
\]

at the symmetry level as well, and the direct dynamic effect of `alpha` degenerates further.

Thus extreme-rotation Liouville theorems necessarily exploit more than the bare OU gap.

---

## 6. Moderate-rotation firewall

M19-105--107 now show:

1. radial energy sees rotation as exactly skew;
2. no positive stationary anisotropic weight can make rotation uniformly damping;
3. bare OU/diffusion commutes with rotation and receives no hypocoercive enhancement.

Hence

\[
\boxed{
\text{moderate RSS/RDSS closure must use rotation-background interaction, not rotation alone.}
}
\]

---

## 7. Next target

The most informative next calculation is to use the one-slice Type-I speed floor of M19-096 on an exact RSS orbit.

For RSS,

\[
\partial_sU=\alpha\mathcal J_AU,
\]

so the singular-survivor speed floor becomes a direct lower bound on `|alpha|` unless the rotational orbit itself degenerates toward an axisymmetric profile.

This gives a quantitative bridge between the external one-slice regularity theorem and the rotated-self-similar parameter.

---

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
