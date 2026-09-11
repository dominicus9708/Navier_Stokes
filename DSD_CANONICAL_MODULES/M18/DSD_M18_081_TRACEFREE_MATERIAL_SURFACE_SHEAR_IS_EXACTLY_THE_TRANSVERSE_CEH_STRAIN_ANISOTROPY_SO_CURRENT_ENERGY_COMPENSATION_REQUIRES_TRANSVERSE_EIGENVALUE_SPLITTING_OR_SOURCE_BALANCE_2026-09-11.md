# M18-081 — Tracefree material-surface shear is exactly the transverse CE-H strain anisotropy, so current-energy compensation requires transverse eigenvalue splitting or source balance

**Date:** 2026-09-11  
**Status:** CE-H SURFACE-SHEAR IDENTIFICATION / TRANSVERSE EIGENVALUE-SPLITTING ROUTE / NO NEW GEOMETRIC CURRENCY

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Purpose

M18-080 derives the exact controlled-patch identity

\[
\boxed{
\mathcal E_\psi'
=
\int_\Sigma
\psi\rho(D_B\kappa+\kappa^2)dA
+
\int_\Sigma
\mathring K_\Sigma(J_G,J_G)dA,
}
\]

where

\[
\mathcal E_\psi
=
\frac12\int_\Sigma|J_G|^2dA
\]

and \(\mathring K_\Sigma\) is the tracefree tangential material deformation of the vortex-transverse surface.

The present question is whether \(\mathring K_\Sigma\) is a genuinely new geometric variable.

On CE-H it is not.

Because the vorticity direction \(\xi\) is a strain eigenvector, the transverse plane \(\xi^\perp\) is invariant under the symmetric strain tensor. The tracefree surface shear is exactly the anisotropic part of the ambient strain restricted to that plane.

---

## 2. CE-H strain eigenline

On CE-H,

\[
\boxed{
\Sigma\xi=\sigma\xi.
}
\]

Since \(\Sigma\) is symmetric, for every

\[
v\perp\xi
\]

one has

\[
\xi\cdot\Sigma v
=
v\cdot\Sigma\xi
=
\sigma v\cdot\xi
=0.
\]

Therefore

\[
\boxed{
\Sigma(\xi^\perp)\subset\xi^\perp.
}
\]

The transverse plane is an invariant two-dimensional strain subspace.

---

## 3. Transverse strain decomposition

Let

\[
\Sigma_\perp
:=
\Sigma|_{\xi^\perp}.
\]

Incompressibility gives

\[
\operatorname{tr}\Sigma=0.
\]

Hence

\[
\boxed{
\operatorname{tr}\Sigma_\perp=-\sigma.
}
\]

Decompose

\[
\boxed{
\Sigma_\perp
=-\frac\sigma2I_\perp
+
\mathring\Sigma_\perp,
}
\]

where

\[
\operatorname{tr}\mathring\Sigma_\perp=0.
\]

The tensor

\[
\mathring\Sigma_\perp
\]

measures transverse eigenvalue splitting/shear inside the plane orthogonal to vorticity.

---

## 4. Eigenvalue form

Choose an orthonormal eigenbasis

\[
e_2,e_3\in\xi^\perp
\]

with transverse eigenvalues

\[
\lambda_2,
\qquad
\lambda_3.
\]

Then

\[
\lambda_2+\lambda_3=-\sigma.
\]

Write

\[
\delta_\perp
:=
\frac{\lambda_2-\lambda_3}{2}.
\]

Then

\[
\boxed{
\lambda_2=-\frac\sigma2+\delta_\perp,
\qquad
\lambda_3=-\frac\sigma2-\delta_\perp.
}
\]

and

\[
\boxed{
\mathring\Sigma_\perp
=\delta_\perp
(e_2\otimes e_2-e_3\otimes e_3).
}
\]

Thus

\[
\boxed{
|\mathring\Sigma_\perp|^2
=2\delta_\perp^2.
}
\]

---

## 5. Whole strain norm decomposition

Using the three strain eigenvalues

\[
\sigma,
\quad
-\frac\sigma2+\delta_\perp,
\quad
-\frac\sigma2-\delta_\perp,
\]

one obtains

\[
\begin{aligned}
|\Sigma|^2
&=
\sigma^2
+
\left(-\frac\sigma2+\delta_\perp\right)^2
+
\left(-\frac\sigma2-\delta_\perp\right)^2\\
&=
\frac32\sigma^2
+2\delta_\perp^2.
\end{aligned}
\]

Therefore

\[
\boxed{
|\Sigma|^2
=
\frac32\sigma^2
+
|\mathring\Sigma_\perp|^2.
}
\]

This is the CE-H specialization of the general tracefree strain decomposition.

---

## 6. Material-surface deformation

The material surface is normal to

\[
n=\xi.
\]

Its symmetric tangential deformation contains

1. the restriction of the ambient physical/similarity strain to \(\xi^\perp\); and
2. the isotropic similarity dilation contribution.

The latter is proportional to the transverse metric and therefore contributes only to the trace.

M18-080 already identifies the surface trace as

\[
\operatorname{tr}K_\Sigma
=1-\sigma.
\]

Consequently, after removing the trace,

\[
\boxed{
\mathring K_\Sigma
=
\mathring\Sigma_\perp.
}
\]

Thus the tracefree surface shear is not a new independent geometric currency.

---

## 7. Substitute into the Poisson-current energy law

M18-080 becomes

\[
\boxed{
\mathcal E_\psi'
=
\int_\Sigma
\psi\rho(D_B\kappa+\kappa^2)dA
+
\int_\Sigma
\mathring\Sigma_\perp(J_G,J_G)dA.
}
\]

In the transverse eigenbasis,

\[
J_G=J_2e_2+J_3e_3,
\]

so

\[
\boxed{
\mathring\Sigma_\perp(J_G,J_G)
=
\delta_\perp(J_2^2-J_3^2).
}
\]

Hence

\[
\boxed{
\mathcal E_\psi'
=
\int_\Sigma
\psi\rho(D_B\kappa+\kappa^2)dA
+
\int_\Sigma
\delta_\perp(J_2^2-J_3^2)dA.
}
\]

This is the exact strain-anisotropy form.

---

## 8. Axisymmetric-transverse strain subbranch

If

\[
\boxed{
\delta_\perp=0,
}
\]

then

\[
\lambda_2=\lambda_3=-\frac\sigma2
\]

and the surface-shear compensation vanishes pointwise:

\[
\boxed{
\mathring\Sigma_\perp=0.
}
\]

The current-energy identity reduces to

\[
\boxed{
\mathcal E_\psi'
=
\int_\Sigma
\psi\rho(D_B\kappa+\kappa^2)dA.
}
\]

On a compact recurrent patch family with zero mean derivative,

\[
\boxed{
\left\langle
\int_\Sigma
\psi\rho(D_B\kappa+\kappa^2)dA
\right\rangle=0.
}
\]

Thus a transversely axisymmetric CE-H strain cannot use surface anisotropy to support recurrent current-energy cycling.

---

## 9. Persistent compensation requires transverse anisotropy

Suppose the recurrent source-evolution contribution has nonzero mean magnitude:

\[
\left|
\left\langle
\int
\psi\rho(D_B\kappa+\kappa^2)dA
\right\rangle
\right|
\ge c_{src}>0.
\]

Then recurrence of \(\mathcal E_\psi\) forces

\[
\boxed{
\left|
\left\langle
\int
\mathring\Sigma_\perp(J_G,J_G)dA
\right\rangle
\right|
\ge c_{src}.
}
\]

Hence the branch must carry persistent correlation between

- transverse strain anisotropy; and
- the orientation of the redistributive current.

This is more specific than merely requiring nonzero strain.

---

## 10. Quantitative current-weighted anisotropy floor

Pointwise,

\[
\left|
\mathring\Sigma_\perp(J_G,J_G)
\right|
\le
\|\mathring\Sigma_\perp\|_{op}|J_G|^2.
\]

Therefore, if

\[
\|J_G\|_2^2
\]

has a fixed recurrent lower bound and the compensation term has fixed nonzero mean, then the `J_G^2`-weighted transverse anisotropy cannot vanish in mean.

Schematically,

\[
\boxed{
\left\langle
\int
\|\mathring\Sigma_\perp\|_{op}|J_G|^2dA
\right\rangle
\ge c_{src}.
}
\]

The exact lower bound is correlation-weighted; one cannot remove the \(|J_G|^2\) weight without an additional current-distribution theorem.

---

## 11. Relation to existing strain payers

CE-H already satisfies

\[
P_\xi^\perp\Sigma\xi=0,
\]

so the earlier transverse-strain vector payer of CP-S/CE-T vanishes.

The present object is different:

\[
\boxed{
\mathring\Sigma_\perp
}
\]

acts **within** the transverse plane rather than tilting \(\xi\) out of its strain eigendirection.

Therefore it was not priced by the old `A=P_\xi^\perp\Sigma W` channel.

Nevertheless it is part of the ordinary ambient strain tensor and obeys

\[
\boxed{
|\mathring\Sigma_\perp|^2
\le|\Sigma|^2.
}
\]

Hence any fixed-volume/time thickening of a pointwise anisotropy lower bound can be priced by the standard strain/enstrophy norm through Calderon--Zygmund equivalence.

As in M18-059, such an unsigned price is classification, not automatic global closure.

---

## 12. No new surface-shear root

M18-080 introduced a seemingly new branch

\[
G_{tracefree\ surface\ shear}.
\]

The present module shows

\[
\boxed{
G_{tracefree\ surface\ shear}
=
G_{transverse\ CEH\ strain\ anisotropy}.
}
\]

Thus no fourth geometric surface currency is needed.

The branch belongs to the existing CE-H strain/coefficient geometry.

---

## 13. Updated cycle-current compensation route

The lineage-cycle branch now has the exact recurrent balance

\[
\boxed{
\left\langle G_{\kappa\text{-}source}\right\rangle
+
\left\langle G_{\perp\text{-}strain\ anisotropy}\right\rangle
=0,
}
\]

where

\[
G_{\kappa\text{-}source}
:=
\int\psi\rho(D_B\kappa+\kappa^2)dA,
\]

and

\[
G_{\perp\text{-}strain\ anisotropy}
:=
\int\mathring\Sigma_\perp(J_G,J_G)dA.
\]

The surviving compact current cycle must therefore either

1. balance coefficient-source evolution against transverse strain anisotropy;
2. make both means vanish separately;
3. or lose the controlled surface/recurrence hypotheses.

---

## 14. Highest-value next target

The next calculation should attack the coefficient-source term

\[
\boxed{
G_{\kappa\text{-}source}
=
\int\psi\rho(D_B\kappa+\kappa^2)dA.
}
\]

Two questions are critical.

### A. Coboundary reduction

Can

\[
\int\psi\rho D_B\kappa
\]

be integrated by parts in material time using the elliptic relation without introducing uncontrolled \(D_B\psi\) and geometry terms?

### B. Sign from the Poisson source

Can the \(\kappa^2\) term be related to the positive pairing

\[
\int\psi\kappa\rho
=
\|J_G\|_2^2
\]

under any sign-separation or sheath/core information already obtained in M18-069--070?

A successful answer could convert the current-cycle problem into a coefficient/strain covariance constraint.

---

## 15. Audit verdict

### Certified

1. CE-H makes \(\xi^\perp\) an invariant strain plane.
2. The transverse restriction has trace \(-\sigma\).
3. Its tracefree part is the transverse eigenvalue-splitting tensor.
4. The tracefree material-surface deformation is exactly this transverse strain anisotropy:
   \[
   \mathring K_\Sigma=\mathring\Sigma_\perp.
   \]
5. The M18-080 current-energy law contains no new independent surface-shear currency.
6. Axisymmetric transverse strain removes the geometric compensation term entirely.
7. Nonzero recurrent source compensation requires current-weighted transverse strain anisotropy.
8. This anisotropy is an ambient-strain component but is distinct from the old vorticity-tilt strain channel.

### Still open

- sign/coboundary structure of the coefficient-source term;
- persistent transverse anisotropy compensation;
- mean/reversible lineage cycles;
- self-helicity/twist and geometry-loss branches;
- ancestry, remote, and critical roots;
- global 3D Navier--Stokes regularity.

## 16. Next target

M18-082 should audit

\[
\int\psi\rho(D_B\kappa+\kappa^2)dA
\]

using only provenance-safe CE-H identities.

Do not expand the geometric remainder in \(D_B\kappa\) termwise unless an earlier module has certified the formula.
