# M18-079 — Lineage transfer has no certified sign law with the amplitude-area potential difference; the natural instantaneous potential is the surface Poisson field psi

**Date:** 2026-09-11  
**Status:** CE-H EDGE-CONSTITUTIVE AUDIT / GRADIENT-FLOW SHORTCUT RETIRED / SURFACE-POISSON POTENTIAL ISOLATED

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Purpose

M18-078 introduces the exact material coordinate

\[
\Lambda_\Sigma
:=
\log(\rho A_\Sigma),
\qquad
D_B\Lambda_\Sigma=\kappa.
\]

M18-077 leaves a finite-lineage cycle problem. A natural gradient-flow guess is that transfer between persistent lineages `a` and `b` might obey a sign law involving

\[
\Delta\Lambda_{ab}
:=
\Lambda_b-\Lambda_a.
\]

For example one might hope for

\[
j_{ab}\Delta\Lambda_{ab}\le0
\]

or the opposite fixed sign.

Such a law would turn the finite lineage graph into a dissipative network and strongly constrain cycle currents.

The present audit finds no such law in the CE-H equations. The instantaneous redistributive current is controlled instead by the surface Poisson potential \(\psi\), where

\[
J_G=\nabla_\Sigma\psi,
\qquad
-\Delta_\Sigma\psi=\kappa\rho.
\]

Thus the amplitude-area gradient-flow shortcut must be retired unless an additional history-to-current constitutive theorem is proved.

---

## 2. Two different kinds of potential

There are now two exact scalar objects.

### Material-history coordinate

\[
\boxed{
\Lambda_\Sigma=\log(\rho A_\Sigma),
\qquad
D_B\Lambda_\Sigma=\kappa.
}
\]

This records time-integrated coefficient history along one material surface element.

### Instantaneous surface Poisson potential

M18-076 gives

\[
\boxed{
J_G=\nabla_\Sigma\psi,
\qquad
-\Delta_\Sigma\psi=\kappa\rho.
}
\]

This is determined at one time by the instantaneous coefficient-amplitude source and the current surface geometry/boundary condition.

The first object is temporal and Lagrangian.
The second is spatial and elliptic.

They are not the same potential.

---

## 3. No algebraic relation identifies grad Lambda with the current

The exact identities provide

\[
D_B\Lambda_\Sigma=\kappa
\]

and

\[
J_G=\nabla_\Sigma\psi.
\]

They do **not** provide

\[
J_G=-M\nabla_\Sigma\Lambda_\Sigma
\]

for any positive mobility `M`, nor any discrete lineage analogue

\[
j_{ab}=-M_{ab}(\Lambda_b-\Lambda_a).
\]

The operations are different:

\[
D_B\Lambda_\Sigma
\quad\text{versus}\quad
\nabla_\Sigma\Delta_\Sigma^{-1}(\kappa\rho).
\]

Therefore no fixed sign of

\[
j_{ab}\Delta\Lambda_{ab}
\]

follows from the known CE-H equations.

---

## 4. History-offset firewall

The current \(J_G\) at a fixed time depends on the instantaneous source

\[
\kappa\rho
\]

and surface geometry.

By contrast, \(\Lambda_\Sigma\) contains the integrated history

\[
\Lambda_\Sigma(\theta)
=
\Lambda_\Sigma(\theta_0)
+
\int_{\theta_0}^{\theta}\kappa\,d\tau.
\]

Hence two material elements can have the same instantaneous \(\kappa,\rho\) source environment but different accumulated \(\Lambda_\Sigma\) offsets due to their earlier histories.

An instantaneous current law cannot acquire a universal sign against those history offsets without an additional theorem tying the histories together.

Thus

\[
\boxed{
\text{instantaneous CE-H current}
\not\Rightarrow
\text{gradient flow in }\Lambda_\Sigma.
}
\]

---

## 5. Local Poisson example shows sign independence

On a controlled local surface chart, suppress curvature corrections for the sign audit and consider the scalar Poisson model

\[
-\Delta\psi=s,
\qquad
s:=\kappa\rho.
\]

Then

\[
J_G=\nabla\psi.
\]

The direction of flux through a chosen interface is determined by the normal derivative

\[
\partial_n\psi,
\]

which is a nonlocal functional of `s` and the patch boundary geometry.

The material-history values \(\Lambda_a,\Lambda_b\) do not enter this elliptic problem.

Changing their past offsets while keeping the same instantaneous source does not change \(\partial_n\psi\).

Therefore a universal sign law between interface current and \(\Delta\Lambda_{ab}\) is not an identity of the CE-H system.

---

## 6. The natural instantaneous positive pairing

Although \(\Lambda\) does not provide the current potential, \(\psi\) does.

Because

\[
J_G=\nabla_\Sigma\psi,
\]

one has

\[
\boxed{
\int_\Sigma J_G\cdot\nabla_\Sigma\psi\,dA
=
\int_\Sigma|J_G|^2dA
\ge0.
}
\]

Using

\[
-\Delta_\Sigma\psi=\kappa\rho
\]

and Dirichlet boundary conditions in the projected Hodge problem,

\[
\boxed{
\int_\Sigma\psi\,\kappa\rho\,dA
=
\int_\Sigma|\nabla_\Sigma\psi|^2dA
=
\|J_G\|_2^2.
}
\]

Thus the exact instantaneous conjugate pair is

\[
\boxed{
\psi
\quad\leftrightarrow\quad
\kappa\rho,
}
\]

not

\[
\Lambda
\quad\leftrightarrow\quad
J_G.
\]

---

## 7. Why the positive Poisson pairing is not yet a monotone state law

The identity

\[
\int\psi\kappa\rho
=
\|J_G\|_2^2
\]

is coercive at one time, but it does not say that

\[
\|J_G\|_2^2
=
-\frac{d}{d\theta}\mathcal F
\]

for a bounded state functional \(\mathcal F\).

The surface geometry, source \(\kappa\rho\), and Poisson solution \(\psi\) all evolve.

Differentiating the Dirichlet energy introduces time derivatives of the source and metric/domain terms.

No sign for those terms is currently certified.

Therefore the Poisson energy is a local coercive norm, not yet a Lyapunov functional.

---

## 8. Lineage graph is not automatically a finite-volume discretization of the surface Poisson problem

One might try to assign to each lineage vertex the average

\[
\psi_i
\]

and interpret edge transfer as a conductance law

\[
j_{ij}=G_{ij}(\psi_j-\psi_i).
\]

This is not currently justified.

The persistent lineage graph records material genealogical relationships, while the surface Poisson equation lives on a local Frobenius patch.

Graph adjacency need not coincide with a fixed spatial partition adjacency, and transfer events may occur on different patches and at different times.

Thus

\[
\boxed{
\text{surface elliptic gradient law}
\not\Rightarrow
\text{lineage-graph resistor law}.
}
\]

A spatial-to-genealogical realization theorem would be needed.

---

## 9. Consequence for the mean-cycle branch

For

\[
G_{cycle}^{mean},
\]

M18-077 gives a nonzero cycle-space mean current.

The \(\Lambda\)-difference route does not exclude it.

The Poisson potential can only exclude it if one proves that the lineage cycle is realized by a closed chain of simultaneous/compatible surface patches on which the current is globally exact in one common potential.

No such common-patch realization is currently established.

Hence

\[
\boxed{
G_{cycle}^{mean}
\text{ remains open as a conservative lineage circulation branch}.
}
\]

---

## 10. Consequence for the reversible branch

For

\[
G_{cycle}^{rev},
\]

there is positive unsigned transfer variation but zero signed mean.

Neither \(\Lambda\) nor the instantaneous \(\psi\) pairing creates one-way drift.

The branch can in principle alternate between opposite current configurations while returning both material-history and Poisson energies.

Therefore the reversible branch remains compatible with recurrent dynamics at the present level.

---

## 11. Corrected gradient-flow target

The gradient-flow route should be reformulated.

The next useful theorem would not be

\[
j_{ab}\sim-(\Lambda_b-\Lambda_a).
\]

Instead it would be one of:

### A. Common-surface realization

Show that a recurrent lineage cycle is realized inside one connected controlled Frobenius surface network with one globally defined \(\psi\).

Then exactness of \(d\psi\) may constrain closed spatial cycles.

### B. Dynamic Poisson energy law

Derive an evolution identity for

\[
\mathcal E_\psi
:=
\frac12\int_\Sigma|\nabla_\Sigma\psi|^2dA
\]

and determine whether recurrent nonzero current forces a signed or dissipative drift after all metric/source terms are inserted.

### C. Graph realization of the Dirichlet form

Prove that the lineage transfer graph is a controlled quotient of the surface-current geometry, producing a positive conductance form on graph edges.

Any of these would add genuinely new information.

---

## 12. DSD classification update

The attempted amplitude-area gradient route is retired:

\[
\boxed{
\Delta\Lambda_{ab}
\not\Rightarrow
\operatorname{sign}(j_{ab}).
}
\]

The current route is sharpened to

\[
\boxed{
J_G
=
\nabla_\Sigma(-\Delta_\Sigma)^{-1}(\kappa\rho).
}
\]

Thus the unresolved circulation problem is primarily a **spatial-realization / time-dependent Dirichlet-form problem**, not an amplitude-potential problem.

---

## 13. Audit verdict

### Certified

1. No CE-H identity currently gives a sign law between lineage transfer and \(\Delta\Lambda_{ab}\).
2. \(\Lambda\) is a Lagrangian history coordinate, whereas the current is controlled by an instantaneous elliptic potential.
3. The natural instantaneous potential is \(\psi\), satisfying
   \[
   -\Delta_\Sigma\psi=\kappa\rho,
   \qquad
   J_G=\nabla_\Sigma\psi.
   \]
4. The positive pairing
   \[
   \int\psi\kappa\rho=\|J_G\|_2^2
   \]
   is exact.
5. This pairing is not yet the derivative of a bounded Lyapunov functional.
6. The lineage graph is not automatically a finite-volume discretization of the Frobenius surface Poisson problem.
7. Both mean-cycle and reversible-cycle branches remain open.

### Still open

- common-surface realization of a lineage cycle;
- evolution law for the surface Poisson Dirichlet energy;
- graph conductance realization;
- self-helicity/twist and surface geometry branches;
- ancestry, remote, and critical roots;
- global 3D Navier--Stokes regularity.

## 14. Next target

M18-080 should audit the time derivative of

\[
\boxed{
\mathcal E_\psi
=
\frac12\int_{\Sigma(\theta)}|\nabla_\Sigma\psi|^2dA
}
\]

on a controlled material Frobenius patch.

The purpose is not to assume monotonicity but to identify every term generated by:

- source evolution \(D_B(\kappa\rho)\);
- material metric deformation;
- moving boundary/domain geometry;
- the CE-H strain eigenvalue;
- surface-current boundary flux.

If the derivative is sign-indefinite, record the exact compensating channels rather than forcing a false Lyapunov structure.
