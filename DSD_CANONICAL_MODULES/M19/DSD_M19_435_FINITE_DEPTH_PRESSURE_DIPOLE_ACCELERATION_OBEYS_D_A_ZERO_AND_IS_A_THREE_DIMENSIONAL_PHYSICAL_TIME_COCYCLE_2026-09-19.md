# M19-435 — Finite-depth pressure-dipole acceleration obeys D a = 0: spatially harmonic on each physical slice but not necessarily frozen in wedge depth

Date: 2026-09-19  
Canonical ID: **M19-435**  
Status: **SCOPE CORRECTION / M19-434 q-INVARIANCE IS EXACT AT THE TERMINAL z=0 FIRST JET / AT FINITE WEDGE DEPTH THE CORRECT DIVERGENCE-FREE LAW FOR A PURE POTENTIAL-DIPOLE ACCELERATION IS (∂q-2z∂z)a=0 / THE DIPOLE COEFFICIENT IS CONSTANT ALONG FIXED-PHYSICAL-TIME RADIAL CHARACTERISTICS BUT MAY EVOLVE IN PHYSICAL TIME / THE FINITE-DEPTH ESCAPE IS A THREE-DIMENSIONAL TIME COCYCLE, NOT A STATIC CONSTANT / GLOBAL REGULARITY UNPROVED**

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Why a correction is needed

M19-434 considers the terminal first jet

\[
C(q,\omega)
=
F_z(0,q,\omega).
\]

At \(z=0\), the fixed-physical-time radial operator

\[
\mathfrak D
=
\partial_q-2z\partial_z
\]

reduces to

\[
\partial_q.
\]

Therefore M19-434 correctly proves that a pure terminal potential dipole

\[
C_{dip}=W_{a(q)}
\]

must satisfy

\[
a_q=0.
\]

However the M19-432 depth-derivative branch concerns

\[
F_z(z_E,q,\omega)
\]

at a finite depth \(z_E>0\).

There the \(-2z\partial_z\) part of \(\mathfrak D\) cannot be omitted.

## 2. Divergence law for the physical acceleration

M5-582 gives

\[
u_s
=
-r^{-3}F_z.
\]

Since \(\nabla\cdot u=0\) for all physical times,

\[
\nabla\cdot u_s=0.
\]

For a degree-minus-three vector coefficient \(Z(z,q,\omega)\),

\[
r^{-3}Z,
\]

the exact fixed-physical-time divergence constraint is

\[
\boxed{
(\mathfrak D-1)Z_r
+
\operatorname{div}_{S^2}Z_T
=
0.
}
\]

Set

\[
Z=W_{a(z,q)}.
\]

## 3. Exact finite-depth dipole transport law

For

\[
W_a
=
a-3(a\cdot\omega)\omega,
\]

we have

\[
(W_a)_r
=
-2(a\cdot\omega),
\]

and

\[
(W_a)_T
=
\nabla_{S^2}(a\cdot\omega).
\]

Since

\[
\Delta_{S^2}(a\cdot\omega)
=
-2(a\cdot\omega),
\]

the divergence constraint becomes

\[
(\mathfrak D-1)
[-2(a\cdot\omega)]
-
2(a\cdot\omega)
=
0.
\]

The zeroth-order pieces cancel, leaving

\[
-2(\mathfrak Da)\cdot\omega=0.
\]

Therefore

\[
\boxed{
\mathfrak Da
=
(\partial_q-2z\partial_z)a
=
0.
}
\]

This is the correct finite-depth potential-dipole law.

## 4. Characteristics are physical-time slices

The characteristic equations of \(\mathfrak D\) are

\[
\frac{dq}{d\lambda}=1,
\qquad
\frac{dz}{d\lambda}=-2z.
\]

Hence

\[
\boxed{
ze^{2q}
=
\text{constant}.
}
\]

But

\[
s=-ze^{2q}.
\]

Therefore the characteristics of \(\mathfrak D\) are exactly fixed physical-time slices.

Thus

\[
\boxed{
\mathfrak Da=0
\Longleftrightarrow
a=a(s)
}
\]

in physical variables.

The dipole coefficient is spatially constant across radius at one physical time, as expected for a harmonic pressure multipole.

It may nevertheless evolve with physical time.

## 5. Exact pressure representation

Let

\[
p_{dip}(x,s)
=
\frac{a(s)\cdot x}{|x|^3}.
\]

Then

\[
\Delta p_{dip}=0
\qquad(x\neq0),
\]

and

\[
\boxed{
\nabla p_{dip}
=
r^{-3}W_{a(s)}.
}
\]

In wedge form,

\[
H_{dip}(z,q,\omega)
=
a(-ze^{2q})\cdot\omega.
\]

Because

\[
\mathfrak Da=0,
\]

the wedge pressure-gradient operator gives

\[
\boxed{
\mathfrak G_2H_{dip}
=
W_{a(s)}.
}
\]

Thus the finite-depth potential-dipole acceleration is exactly the physical-time-dependent harmonic pressure-dipole gradient.

## 6. Terminal limit recovers M19-434

Assume the realized terminal jet has a limit as \(s\uparrow0\).

Then

\[
a(s)\to a_*.
\]

At \(z=0\), the coefficient becomes independent of q:

\[
\boxed{
a(0,q)=a_*.
}
\]

This is precisely M19-434.

Therefore M19-434 is retained without change as the terminal statement.

M19-435 corrects only its use at finite wedge depth.

## 7. The finite-depth dipole is still only three dimensional

Although it can vary in physical time, the dipole sector remains

\[
\boxed{
a(s)\in\mathbb R^3.
}
\]

No angular infinite-dimensional freedom is restored.

The full finite-depth escape is therefore a three-dimensional time cocycle.

At fixed wedge depth z, q-translation samples

\[
s=-ze^{2q},
\]

so recurrent q-history corresponds to a recurrently sampled physical-time dipole history.

## 8. Vorticity invisibility remains exact

For every fixed physical time,

\[
\nabla\times\nabla p_{dip}=0.
\]

Therefore even when

\[
a=a(s)
\]

varies,

\[
\boxed{
\operatorname{curl}
\left[
r^{-3}W_{a(s)}
\right]
=
0
}
\]

at that time.

Hence the M19-433 firewall remains valid:

\[
\boxed{
\text{vorticity/curl equation alone cannot observe the dipole acceleration}.
}
\]

## 9. What time differentiation would reveal

Although the acceleration itself is curl free, differentiating its coefficient in physical time gives

\[
\partial_s
\left[
r^{-3}W_{a(s)}
\right]
=
r^{-3}W_{a'(s)}.
\]

This is again curl free.

Thus repeated time differentiation does not leave the harmonic-gradient sector.

A closure cannot be obtained simply by differentiating the vorticity equation more times.

One must use pressure realization or momentum/stress information.

## 10. Corrected overlap frontier

The finite-depth acceleration branch should be written

\[
\boxed{
Z_E
\Longrightarrow
Z_{curl}
\lor
Z_{dip}^{3D-time}
\lor
Z_{mixed},
}
\]

where

\[
\boxed{
\mathfrak Da_{dip}=0.
}
\]

At the terminal boundary,

\[
Z_{dip}^{3D-time}
\to
a_*\in\mathbb R^3
\]

and M19-434 applies.

## 11. Next target

The next question is now sharply global:

At each finite parent/prelimit time, the whole-space pressure is fixed by the Riesz transform of the Reynolds stress and has no freely added harmonic \(r^{-2}\) dipole at spatial infinity.

Therefore a nonzero limit dipole history \(a(s)\) requires a nonuniform far-field pressure/stress limit under the blow-up sequence.

The next calculation should quantify this defect in terms of the critical Reynolds-stress tail and decide its physical scaling.

\[
\boxed{\text{M19-435 COMPLETE; FINITE-DEPTH PRESSURE-DIPOLE ACCELERATION IS A THREE-DIMENSIONAL PHYSICAL-TIME COCYCLE SATISFYING }\mathfrak Da=0.}
\]

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
