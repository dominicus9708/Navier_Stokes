# M19-433 — Harmonic pressure-dipole acceleration is invisible to vorticity and blocks a curl-only closure of the depth-derivative branch

Date: 2026-09-19  
Canonical ID: **M19-433**  
Status: **PRESSURE-DIPOLE FIREWALL FOR THE M19-432 z-DERIVATIVE BRANCH / DEGREE-minus-3 ADMITS A NONZERO DIVERGENCE-FREE CURL-FREE POTENTIAL DIPOLE / THIS MODE IS EXACTLY THE GRADIENT OF THE CRITICAL l=1 r^-2 PRESSURE DIPOLE / VORTICITY OR CURL OBSERVABILITY ALONE CANNOT CONTROL THE FULL PARABOLIC ACCELERATION / WHOLE-SPACE REALIZATION FIXES THE DIPOLE COEFFICIENT BUT DOES NOT FORCE IT TO ZERO / GLOBAL REGULARITY UNPROVED**

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Input from M19-432

On the deformation escape at the residual-slope energy maximum, M19-432 leaves the depth-derivative branch

\[
\boxed{
\mathscr V_z(z_E)
=
\left\langle
\|F_z(z_E)\|_2^2
\right\rangle
\ge
v_z^E>0.
}
\]

M5-582 identifies

\[
\boxed{
u_s
=
-r^{-3}F_z.
}
\]

A tempting next step is to curl the wedge momentum equation and argue that a large acceleration must generate a large vorticity-time derivative or stretching event.

That implication has a nontrivial kernel.

## 2. A harmonic dipole potential

Fix a constant vector

\[
a\in\mathbb R^3,
\qquad
a\neq0,
\]

and define

\[
\boxed{
\phi_a(x)
:=
\frac{a\cdot x}{|x|^3}.
}
\]

Since

\[
\phi_a
=
-a\cdot\nabla\frac1{|x|},
\]

it is harmonic away from the origin:

\[
\boxed{
\Delta\phi_a=0
\qquad
(x\neq0).
}
\]

Its gradient is

\[
\boxed{
\nabla\phi_a
=
r^{-3}
W_a(\omega),
}
\]

with

\[
\boxed{
W_a(\omega)
=
a-3(a\cdot\omega)\omega.
}
\]

## 3. The potential dipole is divergence free and curl free

Because it is a gradient,

\[
\boxed{
\nabla\times
\left(
r^{-3}W_a
\right)
=
0.
}
\]

Because the potential is harmonic,

\[
\boxed{
\nabla\cdot
\left(
r^{-3}W_a
\right)
=
\Delta\phi_a
=
0.
}
\]

Thus

\[
\boxed{
r^{-3}W_a
}
\]

is a nonzero vector field which is simultaneously

- divergence free;
- curl free;
- homogeneous of degree \(-3\);
- smooth on every punctured annulus.

Therefore a degree-minus-three divergence-free acceleration is **not** determined by its curl.

## 4. Exact pressure-dipole identification

Write

\[
\phi_a
=
r^{-2}(a\cdot\omega).
\]

This is exactly an \(l=1\) critical pressure dipole.

Its gradient is

\[
\nabla
\left[
r^{-2}(a\cdot\omega)
\right]
=
r^{-3}
\left[
a-3(a\cdot\omega)\omega
\right].
\]

Hence the vorticity-invisible acceleration kernel is precisely

\[
\boxed{
\text{gradient of the }r^{-2},\ l=1\text{ pressure-dipole sector}.
}
\]

It is not a new unrelated construction.

## 5. Consequence for the wedge z-derivative

Suppose a component of the wedge acceleration coefficient has

\[
F_z^{dip}(z,q,\omega)
=
c(z,q)W_a(\omega)
\]

with the compatible radial/log structure.

Then the corresponding physical acceleration contribution is

\[
-r^{-3}F_z^{dip}.
\]

Its curl contribution can vanish in the exact homogeneous dipole limit while its L2 sphere norm is nonzero.

Therefore

\[
\boxed{
\|F_z\|_2>0
\not\Rightarrow
\|\operatorname{curl}(r^{-3}F_z)\|_2>0
}
\]

without removal of the harmonic pressure-dipole sector.

In particular, the vorticity equation alone cannot observe this component.

## 6. Relation to M5-134

M5-134 audits exactly the leading critical pressure dipole in the realized whole-space tail factor.

Its conclusion is:

\[
\boxed{
\text{same realized velocity tail}
\Longrightarrow
\text{same pressure-dipole coefficient}.
}
\]

Thus the dipole is not a freely adjustable same-tail gauge variable.

However M5-134 explicitly warns that

\[
\boxed{
\text{dipole coefficient fixed}
\not\Rightarrow
\text{dipole coefficient }=0.
}
\]

Therefore whole-space pressure realization removes arbitrary fiber freedom but does not eliminate the vorticity-invisible dipole channel.

## 7. Relation to the leading pressure resonance audit

M19-135 shows that the zero-q \(l=1\) leading pressure solvability condition cancels structurally by double-divergence homogeneity.

Hence the ordinary pressure Poisson equation does not supply an automatic condition forcing the dipole coefficient to vanish.

The two historical facts are consistent:

- the punctured elliptic problem has an \(l=1\) harmonic kernel;
- whole-space realization selects its coefficient;
- the currently known compatibility identities do not force that selected coefficient to be zero.

## 8. Scope of the firewall

The field

\[
r^{-3}W_a
\]

is **not** asserted to be a complete ancient Navier--Stokes acceleration by itself.

Nor is a freely chosen pressure dipole allowed inside the realized solution.

The point is narrower and exact:

\[
\boxed{
\text{divergence-free + curl/vorticity information}
\text{ has a nontrivial degree-minus-three harmonic-gradient kernel}.
}
\]

Therefore a proof that attempts to close the M19-432 depth-derivative branch using only the vorticity equation is incomplete unless it separately controls this pressure-dipole sector.

## 9. Correct dynamic split of the depth derivative

The depth-derivative branch must be audited as

\[
\boxed{
Z_E
\Longrightarrow
Z_{curl}
\lor
Z_{dip}
\lor
Z_{mixed},
}
\]

where

\[
Z_{curl}
:
\text{acceleration visible in the vorticity/curl equation},
\]

and

\[
Z_{dip}
:
\text{critical harmonic pressure-dipole acceleration},
\]

with the mixed branch carrying both.

Only the first part can be attacked directly by vorticity-production overlap.

The second requires a pressure-realization/tightness or dipole-rigidity theorem.

## 10. Strategic consequence for the overlap program

M19-430 localized energy and enstrophy witnesses to one compact wedge corridor.

M19-431--432 showed that the energy maximum can escape direct vorticity overlap through tangent deformation/acceleration.

M19-433 now identifies an explicit PDE reason why the acceleration escape cannot be removed by curl alone:

\[
\boxed{
\text{pressure-dipole acceleration is invisible to vorticity}.
}
\]

Therefore the desired bounded-corridor coupling theorem must be genuinely **momentum + pressure + vorticity coupled**.

A pure energy–curl estimate cannot be sufficient.

## 11. Next target

The pressure-dipole mode is finite dimensional.

This is useful.

The next calculation should project the wedge momentum equation onto the three-dimensional harmonic-dipole basis

\[
W_{e_1},W_{e_2},W_{e_3}
\]

and derive the q/z evolution of its coefficient.

If the coefficient is a bounded recurrent coboundary or is fixed in z by the realized pressure-tail factor, the dipole escape may be frozen or removed.

If not, it becomes a precisely typed three-dimensional dynamic factor rather than an uncontrolled pressure field.

\[
\boxed{\text{M19-433 COMPLETE; CURL-ONLY OVERLAP IS BLOCKED BY A FINITE-DIMENSIONAL HARMONIC PRESSURE-DIPOLE ACCELERATION KERNEL.}}
\]

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
