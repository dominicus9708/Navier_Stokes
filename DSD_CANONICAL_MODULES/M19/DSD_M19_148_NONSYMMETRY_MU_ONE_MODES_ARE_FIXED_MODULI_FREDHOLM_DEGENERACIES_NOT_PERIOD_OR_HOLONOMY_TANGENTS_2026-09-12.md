# DSD M19-148 — Nonsymmetry mu=1 modes are fixed-moduli Fredholm degeneracies, not period or holonomy tangents

Date: 2026-09-12

Status: **ACTIVE M19 CALCULATION / KERNEL BRANCH REFINED / AFTER TIME-ROTATION GAUGE REMOVAL A HOMOGENEOUS MU=1 TWISTED FLOQUET MODE IS A TRUE FIXED-(S,Q_*) RETURN-MAP DEGENERACY / VARIATIONS OF PERIOD OR HOLONOMY SATISFY AN INHOMOGENEOUS AUGMENTED JACOBI BOUNDARY CONDITION AND MUST NOT BE COUNTED AS THE SAME KERNEL / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Relative-periodic orbit

Let

\[
U(s+S)=Q_*U(s).
\]

Define the relative-periodic defect

\[
\boxed{
\mathcal F(U_0,S,Q_*)
:=Q_*^{-1}\Phi_S(U_0)-U_0,
}
\]

where `Phi_S` is the nonlinear similarity-time flow map.

The orbit satisfies

\[
\mathcal F(U_0,S,Q_*)=0.
\]

The state derivative at fixed intrinsic moduli is

\[
D_{U_0}\mathcal F
=\mathcal M_S^{tw}-I.
\]

Thus a homogeneous multiplier-one mode satisfies

\[
\boxed{
(I-\mathcal M_S^{tw})v=0.
}
\]

---

## 2. Vary a genuine RDSS family

Suppose instead that a one-parameter family exists,

\[
\varepsilon\mapsto
(U_0(\varepsilon),S(\varepsilon),Q_*(\varepsilon)).
\]

Differentiate

\[
\mathcal F(U_0(\varepsilon),S(\varepsilon),Q_*(\varepsilon))=0.
\]

Write

\[
v:=U_0'(0),
\qquad
\dot S:=S'(0),
\qquad
\Xi:=Q_*^{-1}Q_*'(0)\in\mathfrak{so}(3).
\]

Then

\[
(\mathcal M_S^{tw}-I)v
+\dot S\,Q_*^{-1}\partial_sU(S)
-\mathcal R_{\Xi}U_0
=0,
\]

up to the fixed sign convention for the infinitesimal group action.

Since

\[
Q_*^{-1}\partial_sU(S)=\partial_sU_0,
\]

we obtain the augmented Jacobi equation

\[
\boxed{
(\mathcal M_S^{tw}-I)v
=-\dot S\,\partial_sU_0
+\mathcal R_{\Xi}U_0.
}
\]

Thus changing period or holonomy produces an **inhomogeneous** right-hand side lying in the exact symmetry tangent space.

---

## 3. Consequence after phase/rotation gauges

Impose standard phase and rotation gauges that remove

\[
\partial_sU_0
\quad\text{and}\quad
\mathcal R_JU_0.
\]

Then a state perturbation satisfying

\[
\boxed{
(\mathcal M_S^{tw}-I)v=0
}
\]

with no symmetry component is not merely a derivative of the orbit moduli.

It is a genuine failure of invertibility of the fixed-moduli return map.

Define the nonsymmetry kernel

\[
\boxed{
K_{nsym}
:=
\ker(I-\mathcal M_S^{tw})/E_{sym}^{\mu=1}.
}
\]

The live kernel theorem is

\[
\boxed{K_{nsym}=\{0\}.}
\]

---

## 4. Scattering representation of a kernel mode

For

\[
v\in K_{nsym},
\qquad
B:=D\mathscr S_Uv,
\]

M19-145 gives

\[
\boxed{
B(q+L)=Q_*^{-1}B(q).
}
\]

Thus the kernel perturbation has exactly the same relative-periodic tail twist as the base state.

After principal-holonomy untwisting,

\[
\widetilde B(q+L)=\widetilde B(q).
\]

Hence `K_nsym` maps by the uniformly observable scattering derivative into a finite-dimensional twisted-periodic tail space.

No positive or polynomial growth is possible because the scattering pullback norm is an exact isometric cocycle norm on the observable hard bundle.

---

## 5. Finite-dimensional Fredholm form

By M19-095/109/131, after symmetry gauges the relevant hard state space is finite-dimensional and the twisted monodromy has essential spectral radius below one.

Therefore

\[
\boxed{
I-\mathcal M_S^{tw}
}

is a Fredholm operator of index zero on the hard complement of the stable essential spectrum.

The kernel problem is therefore a finite-dimensional determinant problem:

\[
\boxed{
\det
\left[
I-M_{hard}(U,S,Q_*)
\right]
\ne0
}

on the symmetry-gauged hard fiber.

This is a substantial dimensional reduction, but it is not yet a sign theorem.

---

## 6. Why generic nondegeneracy is insufficient

A generic orbit in a parameter family may be nondegenerate, but a proof of global regularity cannot assume genericity.

A degenerate isolated relative-periodic orbit may exist without generating a smooth neighboring branch.

Therefore neither

\[
\text{generic Fredholm invertibility}
\]

nor

\[
\text{absence of a visible local branch}
\]

is enough to prove

\[
K_{nsym}=0.
\]

A PDE-specific orientation/sign/index theorem is still required.

---

## 7. Correct kernel frontier

The kernel branch is now exactly

\[
\boxed{
\mathcal T_{kernel}^{nsym}:
\ker(I-\mathcal M_S^{tw})
=E_{sym}^{\mu=1}.
}
\]

For generic nontrivial holonomy, `E_sym^{mu=1}` contains

- the time tangent;
- the rotation tangent about the holonomy axis;

with possible dimension reduction when the profile has isotropy.

For ordinary DSS, all nonzero rotation tangents also sit at `mu=1` and must be removed by the rotation quotient.

---

## 8. Audit verdict

### Certified

1. A fixed-moduli `mu=1` eigenvector is the kernel of the homogeneous twisted return map.
2. Period and holonomy variations satisfy an augmented inhomogeneous Jacobi equation.
3. Therefore modulus variation and nonsymmetry kernel are distinct objects.
4. The remaining kernel is finite-dimensional and observable in a twisted-periodic scattering space.

### Not certified

1. Nonsymmetry kernel triviality.
2. Elliptic neutral-mode exclusion.
3. Moderate RSS/RDSS nonexistence.
4. Global regularity.

---

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
