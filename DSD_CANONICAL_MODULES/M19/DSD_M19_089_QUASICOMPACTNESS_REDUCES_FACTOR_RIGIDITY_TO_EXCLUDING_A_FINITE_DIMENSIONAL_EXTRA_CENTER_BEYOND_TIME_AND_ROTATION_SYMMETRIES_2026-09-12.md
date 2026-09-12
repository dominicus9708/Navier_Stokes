# DSD M19-089 — Quasi-compactness reduces factor rigidity to excluding a finite-dimensional extra center beyond time and rotation symmetries

Date: 2026-09-12

Status: **ACTIVE M19 CALCULATION / CONDITIONAL ON COMPLETION OF THE M19-088 QUASI-COMPACTNESS BOOKKEEPING / EXACT SYMMETRY CENTER SEPARATED / APERIODIC FACTOR REQUIRES AN ADDITIONAL FINITE-DIMENSIONAL CENTER DIRECTION / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Input

M19-075--076 identified the exact symmetry directions:

\[
E^c_{sym}(Y)
=
\operatorname{span}\{\partial_\theta U_Y\}
\oplus
T_{U_Y}(SO(3)\cdot U_Y).
\]

M19-076 showed that rotational modulation is energy-neutral in the retained radial Hilbert geometry.

M19-087 found a pressure-free vorticity quarter-gap.

M19-088 gives the quasi-compactness route

\[
\lambda_{ess}<0,
\]

conditional on completing the stated core-domain compactness bookkeeping.

Hence every zero/nonnegative interior cocycle bundle is finite-dimensional.

---

## 2. Quotient the rotational symmetry

Let

\[
\widehat{\mathcal H}
:=\mathcal H/SO(3)
\]

be a local rotational slice of the recurrent hull.

The exact rotational neutral modes are removed by the modulation conditions of M19-076.

The surviving symmetry center is therefore the flow direction

\[
\boxed{
Z_t(Y)=\partial_\theta U_Y.
}
\]

Let

\[
E^c_q(Y)
\]

be the center bundle in the rotational quotient.

Quasi-compactness implies

\[
\boxed{
1\le \dim E^c_q(Y)<\infty.
}
\]

---

## 3. Define the extra center

Split

\[
\boxed{
E^c_q(Y)
=
\operatorname{span}\{Z_t(Y)\}
\oplus E^c_{extra}(Y),
}
\]

where the second summand is chosen by a smooth or measurable transverse gauge on the recurrent component.

The live analytic target becomes

\[
\boxed{
E^c_{extra}(Y)=\{0\}.
}
\]

This is much smaller than the earlier infinite-dimensional formal scattering-center problem.

---

## 4. Why one-dimensional quotient center would close the aperiodic factor

Assume

\[
E^c_{extra}=0.
\]

Then the recurrent dynamics, after removing stable directions and rotations, has only the time-flow center direction.

The corresponding local center manifold is one-dimensional wherever the vector field is nonzero.

A smooth autonomous flow on a one-dimensional compact recurrent component can only consist of equilibria or periodic orbits; it cannot support an irrational multi-frequency quasiperiodic flow.

Therefore the scattering factor

\[
\mathscr S(\sigma_tY)=T_{-t/2}\mathscr S(Y)
\]

cannot be a nonzero aperiodic recurrent translation factor.

Schematically,

\[
\boxed{
E^c_q=\operatorname{span}\{\partial_\theta U\}
\Longrightarrow
\text{stationary or periodic recurrence only}.
}
\]

The stationary and periodic/DSS branches were already separately routed in the historical tail tree.

Thus the genuinely new weak-critical aperiodic survivor would disappear.

---

## 5. Why aperiodicity forces extra center

Conversely, suppose the recurrent hull carries a nontrivial aperiodic scattering factor.

After rotational quotient, a one-dimensional center generated only by the flow cannot carry an additional independent recurrent phase.

Hence a nonperiodic recurrent factor requires

\[
\boxed{
\dim E^c_q\ge2,
}
\]

or equivalently

\[
\boxed{
E^c_{extra}\neq0.
}
\]

This should be understood as a center-manifold consequence of the quasi-compact smooth corridor, not as an abstract statement about arbitrary topological flows.

Without the finite-dimensional/quasi-compact reduction, M19-061's irrational-torus countermodels remain valid.

---

## 6. New form of the theorem frontier

The earlier target

\[
\text{exclude an infinite-dimensional aperiodic q-translation factor}
\]

is replaced by

\[
\boxed{
\mathcal T_{extra-center}:
E^c_{extra}=0.
}
\]

Thus the dominant analytic problem is no longer at infinity.

It is an interior finite-dimensional center-index problem.

---

## 7. What would prove it

M19-087 gives for every complete zero-center perturbation

\[
\left\langle
\frac{\mathcal C_U[W]}{\|\eta\|_2^2}
\right\rangle
=
\frac14
+\nu
\left\langle
\frac{\|\nabla\eta\|_2^2}{\|\eta\|_2^2}
\right\rangle.
\]

Therefore any extra center direction must receive at least a quarter-unit of persistent average compensation from the compact interior background operator.

The next calculation should turn this into a finite-dimensional trace/Ky-Fan budget after the exact symmetry directions have been removed.

A sufficient condition would be a strict transverse numerical-abscissa estimate

\[
\boxed{
\sup_{e\perp E^c_{sym},\ \|e\|=1}
\left\langle
\mathfrak r_U(e)
\right\rangle
<0,
}
\]

or, more invariantly, negativity of the top transverse center Lyapunov exponent.

---

## 8. Firewall

Quasi-compactness alone does not prove `E_extra=0`.

Finite-dimensional autonomous systems can support aperiodic recurrent tori once the center dimension is at least two.

Thus

\[
\boxed{
\text{finite-dimensional center}
\neq
\text{one-dimensional center}.
}
\]

The remaining problem is real and cannot be removed by a dimensionality slogan.

---

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
