# M19-220 — Zero-q holonomy-fixed labels reduce to axisymmetric or cyclic angular sectors, but divergence-free kinematics do not force vanishing

**Date:** 2026-09-14  
**Status:** ACTIVE CALCULATION / ANGULAR HOLONOMY CLASSIFICATION + KINEMATIC NO-GO

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Zero-q resonance law

M19-214 gives the exact RDSS kernel resonance

\[
\kappa L-m\alpha=2\pi n,
\qquad m,n\in\mathbb Z,
\]

where \(\alpha\) is the physical holonomy rotation angle and \(m\) is an integer angular momentum label.

In the zero-q sector,

\[
\kappa=0.
\]

Hence every zero-q kernel channel must satisfy

\[
\boxed{
 m\alpha\in2\pi\mathbb Z.
}
\]

Equivalently, its scattering label is fixed by the holonomy rotation:

\[
Q_*^{-1}B=B.
\]

## 2. Irrational holonomy angle

Assume

\[
\frac{\alpha}{2\pi}\notin\mathbb Q.
\]

Then

\[
m\alpha=2\pi n
\]

with integers \(m,n\) implies

\[
\boxed{m=0,\qquad n=0.}
\]

Therefore a continuous angular scattering label fixed by \(Q_*\) is fixed by the dense subgroup

\[
\{R_{\mathbf a}(k\alpha):k\in\mathbb Z\}
\]

of axial rotations. Continuity then gives invariance under the full axial circle:

\[
\boxed{
R_{\mathbf a}(\beta)B=B
\qquad\forall\beta\in\mathbb R.
}
\]

Thus for irrational holonomy every zero-q kernel label is axisymmetric about the holonomy axis.

## 3. Rational holonomy angle

Assume instead

\[
\frac{\alpha}{2\pi}=\frac pk,
\qquad \gcd(p,k)=1.
\]

Then

\[
m\alpha\in2\pi\mathbb Z
\]

is equivalent to

\[
\boxed{k\mid m.}
\]

Hence the fixed angular sector is the \(C_k\)-invariant sector:

\[
\boxed{
m\in k\mathbb Z.}
\]

This need not be axisymmetric. Rational holonomy permits angular aliasing at multiples of the cyclic order.

The ordinary DSS case \(\alpha=0\) is the extreme case: holonomy imposes no angular restriction at all.

## 4. Exact divergence-free form on the sphere

For a zero-q label write

\[
b(\omega)=b_r(\omega)\omega+b_T(\omega),
\qquad b_T\cdot\omega=0.
\]

M19-218 gives

\[
\boxed{
b_r+\operatorname{div}_{S^2}b_T=0.
}
\]

Use the Hodge decomposition of a smooth tangential vector field on \(S^2\):

\[
\boxed{
b_T=\nabla_{S^2}f+\omega\times\nabla_{S^2}g.
}
\]

The toroidal part is divergence free, so

\[
\operatorname{div}_{S^2}b_T
=\Delta_{S^2}f.
\]

Therefore

\[
\boxed{
b_r=-\Delta_{S^2}f.
}
\]

The integral constraint

\[
\int_{S^2}b_r\,d\omega=0
\]

is automatic because the spherical Laplacian has zero integral.

Hence every zero-q divergence-free leading label is parameterized kinematically by two scalar angular potentials:

\[
\boxed{
(f,g)
\longmapsto
b=
-(\Delta_{S^2}f)\omega
+\nabla_{S^2}f
+\omega\times\nabla_{S^2}g.
}
\]

Constants in \(f,g\) are irrelevant.

## 5. Holonomy restriction on the Hodge potentials

The holonomy-fixed condition may be imposed directly on \(f\) and \(g\).

For irrational \(\alpha/2\pi\), both potentials may be taken axisymmetric:

\[
f=f(\vartheta),
\qquad
g=g(\vartheta)
\]

in polar angle \(\vartheta\) about the holonomy axis.

For rational \(\alpha/2\pi=p/k\), their Fourier expansions contain only azimuthal indices

\[
\boxed{m\in k\mathbb Z.}
\]

Thus M19-220 gives an explicit angular normal form for the zero-q leading label.

## 6. Kinematics alone leave many nonzero labels

The Hodge formula immediately supplies nonzero smooth examples satisfying all leading kinematic constraints.

For example, any nonconstant smooth axisymmetric scalar \(f\) with \(g=0\) gives

\[
b=
-(\Delta_{S^2}f)\omega
+\nabla_{S^2}f,
\]

which is nonzero and divergence free.

Likewise any nonconstant smooth axisymmetric \(g\) with \(f=0\) gives the toroidal field

\[
b=\omega\times\nabla_{S^2}g.
\]

Therefore even in the strongest irrational-holonomy case,

\[
\boxed{
\text{q-invariance}
+
\text{holonomy invariance}
+
\nabla\cdot W_0=0
\not\Longrightarrow
b=0.
}
\]

This is a genuine kinematic NO-GO.

## 7. Relation to the finite hard bundle

The ambient holonomy-fixed divergence-free sector is infinite dimensional. The certified hard bundle intersects it in only a finite-dimensional subspace because the hard bundle itself is finite dimensional.

Thus the actual zero-q problem is not to eliminate every Hodge pair \((f,g)\). It is to prove that the **finite-dimensional realized hard intersection** contains only exact-symmetry directions and hence vanishes after quotient.

For irrational holonomy this realized intersection lies entirely in the axisymmetric angular sector. For rational holonomy it lies in the corresponding cyclic sector.

## 8. Revised zero-q theorem

Combining M19-219 and M19-220, the theorem target becomes

\[
\boxed{
\mathcal T_{q0}^{section-ang}:
\begin{array}{l}
\text{there is no nonzero nonsymmetry invariant hard section whose constant scattering label}\\
\text{lies in the holonomy-fixed divergence-free Hodge sector described above.}
\end{array}
}
\]

This is substantially narrower than an arbitrary linearized-kernel problem.

## 9. What remains analytic

No purely representation-theoretic or incompressibility argument closes the sector.

A successful next step must use one of:

1. the full linearized Navier--Stokes equation in the interior;
2. a signed pairing between the invariant section and the evolving background;
3. unique continuation from the homogeneous \(r^{-1}\) boundary label into the compact core;
4. a theorem identifying every such invariant hard section with an exact rotation/time symmetry.

## 10. Firewall

Axisymmetry of the **perturbation label** does not make the RDSS background axisymmetric.

Therefore classical axisymmetric Navier--Stokes regularity results cannot be imported directly: the perturbation solves a linearized equation with coefficients supplied by the generally non-axisymmetric background.

\[
\boxed{
\text{axisymmetric zero-q tangent}
\neq
\text{axisymmetric Navier--Stokes solution}.
}
\]

---

\[
\boxed{
\text{M19-220: ZERO-Q CANDIDATES ARE ANGULARLY CLASSIFIED, BUT A NEW INTERIOR RIGIDITY MECHANISM IS STILL REQUIRED.}
}
\]
