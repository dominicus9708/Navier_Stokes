# M18-080 — Surface-Poisson Dirichlet-energy evolution cancels isotropic area stretch and reduces to kappa-source evolution plus tracefree surface shear

**Date:** 2026-09-11  
**Status:** EXACT PULLED-BACK DIRICHLET-ENERGY EVOLUTION / TWO-DIMENSIONAL CONFORMAL CANCELLATION / SIGN-COMPENSATION AUDIT

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Purpose

M18-079 identifies the natural instantaneous current potential on a controlled Frobenius CE-H patch:

\[
\boxed{
J_G=\nabla_\Sigma\psi,
\qquad
-\Delta_\Sigma\psi=\kappa\rho.
}
\]

The positive instantaneous pairing is

\[
\int_\Sigma\psi\kappa\rho\,dA
=
\int_\Sigma|\nabla_\Sigma\psi|^2dA.
\]

The open question is whether the Dirichlet energy

\[
\boxed{
\mathcal E_\psi
:=
\frac12\int_{\Sigma(\theta)}
|\nabla_\Sigma\psi|^2dA
}
\]

has a one-sign evolution law.

Pulling the material patch back to a fixed reference domain gives an exact answer.

The isotropic material-area stretch cancels from the two-dimensional Dirichlet form, while the source derivative simplifies by the CE-H amplitude law to

\[
\rho(D_B\kappa+\kappa^2).
\]

The only geometric deformation term left is the tracefree tangential surface strain.

The result is exact on a controlled material patch but sign-indefinite.

---

## 2. Fixed reference material coordinates

Let

\[
F_\theta:\Sigma_0\to\Sigma(\theta)
\]

be the material parametrization of one controlled Frobenius patch, before any surface/domain degeneration.

Pull all fields back to the fixed reference domain \(\Sigma_0\).

Let

\[
g(\theta)
\]

be the induced two-dimensional metric and

\[
d\mu_g
\]

its area measure.

The Dirichlet bilinear form is

\[
\boxed{
a_\theta(u,v)
:=
\int_{\Sigma_0}
 g^{ij}(\theta)
 \partial_i u\,\partial_j v
 \,d\mu_g.
}
\]

The source functional is

\[
\boxed{
\ell_\theta(v)
:=
\int_{\Sigma_0}
(\kappa\rho)v\,d\mu_g.
}
\]

The Hodge-gradient potential is characterized weakly by

\[
\boxed{
a_\theta(\psi,v)=\ell_\theta(v)
\qquad\forall v\in H_0^1(\Sigma_0).}
\]

---

## 3. Abstract derivative identity

Define

\[
\mathcal E_\psi
:=
\frac12a_\theta(\psi,\psi).
\]

Differentiate:

\[
\mathcal E_\psi'
=
a_\theta(\psi,\psi')
+
\frac12a_\theta'(\psi,\psi).
\]

Differentiate the weak elliptic equation and test with \(v=\psi\):

\[
a_\theta'(\psi,\psi)
+
a_\theta(\psi',\psi)
=
\ell_\theta'(\psi).
\]

By symmetry,

\[
a_\theta(\psi',\psi)=a_\theta(\psi,\psi').
\]

Therefore

\[
\boxed{
\mathcal E_\psi'
=
\ell_\theta'(\psi)
-
\frac12a_\theta'(\psi,\psi).
}
\]

This is the exact shape/material derivative formula in fixed reference coordinates.

---

## 4. Material area rate

On the vortex-transverse CE-H surface, M18-078 gives the material-area rate

\[
\boxed{
D_B\log dA
=1-\sigma.
}
\]

Set

\[
h:=1-\sigma.
\]

Then the pulled-back area measure satisfies

\[
\boxed{
\partial_\theta d\mu_g
=h\,d\mu_g.
}
\]

---

## 5. Exact source-functional cancellation

Let

\[
s:=\kappa\rho.
\]

For a fixed test function on the material reference domain,

\[
\ell_\theta'(v)
=
\int
v\,[D_Bs+hs]\,d\mu_g.
\]

Now

\[
D_Bs
=
\rho D_B\kappa
+
\kappa D_B\rho.
\]

The CE-H amplitude equation is

\[
D_B\rho
=(\sigma+\kappa-1)\rho.
\]

Hence

\[
D_Bs
=
\rho D_B\kappa
+
\kappa(\sigma+\kappa-1)\rho.
\]

Add the area term

\[
hs=(1-\sigma)\kappa\rho.
\]

The strain and similarity terms cancel exactly:

\[
\boxed{
D_B(\kappa\rho)
+(1-\sigma)\kappa\rho
=
\rho(D_B\kappa+\kappa^2).
}
\]

Therefore

\[
\boxed{
\ell_\theta'(\psi)
=
\int_\Sigma
\psi\rho(D_B\kappa+\kappa^2)dA.
}
\]

No termwise decomposition of the CE-H geometric remainder is used.

---

## 6. Tangential metric deformation tensor

Let

\[
K_\Sigma
\]

be the symmetric tangential material deformation tensor of the surface metric, defined by

\[
\frac12D_Bg_{ij}
=(K_\Sigma)_{ij}.
\]

Then

\[
\operatorname{tr}_gK_\Sigma
=h
=
1-\sigma.
\]

The inverse metric evolves by

\[
D_Bg^{ij}
=-2(K_\Sigma)^{ij}.
\]

Therefore

\[
a_\theta'(\psi,\psi)
=
\int_\Sigma
\left[
-2K_\Sigma^{ij}
+h g^{ij}
\right]
\partial_i\psi\partial_j\psi\,dA.
\]

---

## 7. Two-dimensional conformal cancellation

Because the surface is two-dimensional, decompose

\[
K_\Sigma
=
\mathring K_\Sigma
+
\frac h2g,
\]

where

\[
\operatorname{tr}_g\mathring K_\Sigma=0.
\]

Then

\[
-2K_\Sigma+h g
=
-2\mathring K_\Sigma.
\]

Thus

\[
\boxed{
a_\theta'(\psi,\psi)
=
-2
\int_\Sigma
\mathring K_\Sigma
(\nabla_\Sigma\psi,\nabla_\Sigma\psi)
\,dA.
}
\]

The isotropic area-stretch part cancels exactly.

This is the infinitesimal two-dimensional conformal invariance of the Dirichlet energy.

---

## 8. Exact Dirichlet-energy evolution law

Insert Sections 5 and 7 into the abstract derivative formula:

\[
\boxed{
\frac{d}{d\theta}\mathcal E_\psi
=
\int_\Sigma
\psi\rho(D_B\kappa+\kappa^2)dA
+
\int_\Sigma
\mathring K_\Sigma
(\nabla_\Sigma\psi,\nabla_\Sigma\psi)dA.
}
\]

Equivalently, since

\[
J_G=\nabla_\Sigma\psi,
\]

\[
\boxed{
\mathcal E_\psi'
=
\int_\Sigma
\psi\rho(D_B\kappa+\kappa^2)dA
+
\int_\Sigma
\mathring K_\Sigma(J_G,J_G)dA.
}
\]

This is the central identity.

---

## 9. No Lyapunov sign

Neither term on the right has a fixed sign.

### Source-evolution term

\[
\int\psi\rho D_B\kappa
\]

is sign-indefinite.

Although

\[
\int\psi\kappa\rho
=2\mathcal E_\psi>0,
\]

this does not determine the sign of

\[
\int\psi\kappa^2\rho.
\]

because \(\psi\) itself need not have one sign when the source \(\kappa\rho\) changes sign.

### Surface-shear term

\[
\int\mathring K_\Sigma(J_G,J_G)
\]

is also sign-indefinite because \(\mathring K_\Sigma\) is traceless.

Therefore

\[
\boxed{
\mathcal E_\psi\text{ is not a certified Lyapunov functional.}
}
\]

---

## 10. Recurrent mean balance

On a compact recurrent controlled patch family where \(\mathcal E_\psi\) remains bounded and recurrence justifies zero long-time mean derivative,

\[
\boxed{
\left\langle
\int\psi\rho(D_B\kappa+\kappa^2)dA
\right\rangle
+
\left\langle
\int\mathring K_\Sigma(J_G,J_G)dA
\right\rangle
=0.
}
\]

Thus persistent current must be supported by an exact signed compensation between

1. coefficient-source evolution; and
2. anisotropic tangential surface deformation.

The isotropic surface expansion cannot pay this balance.

---

## 11. New compactness fork

Suppose on a recurrent controlled current branch one can additionally make the tracefree tangential strain small:

\[
\|\mathring K_\Sigma\|_\infty\to0.
\]

Then the recurrent mean balance forces

\[
\left\langle
\int\psi\rho(D_B\kappa+\kappa^2)dA
\right\rangle
\to0.
\]

Conversely, if the coefficient-source term remains bounded away from zero, then

\[
\boxed{
\text{persistent anisotropic surface shear is mandatory}.
}
\]

This does not yet contradict compactness, but it turns recurrent redistribution into a specific geometric strain obligation.

---

## 12. Relation to lineage-cycle branches

For both

\[
G_{cycle}^{mean}
\quad\text{and}\quad
G_{cycle}^{rev},
\]

a fixed recurrent redistributive current gives nonzero \(J_G\) on repeated controlled patches.

The new identity says that recurrent Poisson-current energy cannot evolve freely.

It must lie on the signed balance surface

\[
\boxed{
G_{source\ evolution}
+
G_{tracefree\ surface\ shear}
=0
}
\]

in long-time mean.

Therefore the cycle problem is refined to a **source/shear compensation branch**, not a monotone diffusion branch.

---

## 13. Geometry-loss firewall

The derivation assumes:

- one fixed material reference topology;
- controlled Frobenius charts;
- sufficient regularity to differentiate the metric and elliptic solution;
- Dirichlet Hodge projection on a fixed pulled-back domain.

Failure of these assumptions routes to

\[
\boxed{G_{surface/label\ geometry\ degeneration}.}
\]

No shape derivative is claimed through topology change, patch collapse, or loss of Frobenius realization.

---

## 14. Provenance firewall for D_B kappa

The identity deliberately keeps

\[
D_B\kappa
\]

undivided.

The repository's exact CE-H coefficient law may be written schematically as

\[
D_B\kappa
=
L_\rho\kappa
+L_\rho\sigma
+\mathcal R_{geom},
\]

but M17-463 forbids inventing an uncertified termwise formula for the geometric remainder.

M18-080 does not cross that firewall.

---

## 15. Audit verdict

### Certified

1. In fixed material coordinates,
   \[
   \mathcal E_\psi'
   =
   \ell'(\psi)-\frac12a'(\psi,\psi).
   \]
2. CE-H amplitude plus area transport gives
   \[
   D_B(\kappa\rho)+(1-\sigma)\kappa\rho
   =\rho(D_B\kappa+\kappa^2).
   \]
3. Two-dimensional isotropic area deformation cancels exactly from the Dirichlet-form derivative.
4. Only tracefree tangential surface strain remains in the metric contribution.
5. The exact evolution is
   \[
   \mathcal E_\psi'
   =
   \int\psi\rho(D_B\kappa+\kappa^2)
   +
   \int\mathring K_\Sigma(J_G,J_G).
   \]
6. The evolution is sign-indefinite; \(\mathcal E_\psi\) is not a Lyapunov function.
7. On a recurrent compact patch family, coefficient-source evolution and tracefree surface shear must balance in mean.

### Still open

- whether the source term has an independent sign/covariance restriction;
- whether persistent tracefree surface shear is already priced by a known CE-H/non-CE-H ledger;
- common-surface realization of lineage cycles;
- self-helicity/twist and geometry-loss branches;
- ancestry, remote, and critical roots;
- global regularity.

## 16. Next target

M18-081 should audit the tracefree surface-shear term

\[
\boxed{
\int_\Sigma\mathring K_\Sigma(J_G,J_G)dA.
}
\]

The first question is whether \(\mathring K_\Sigma\) is algebraically controlled by the ambient CE-H strain eigenstructure

\[
\Sigma\xi=\sigma\xi,
\qquad
\operatorname{tr}\Sigma=0,
\]

so that on the vortex-transverse plane its tracefree part can be written directly in terms of the two transverse strain eigenvalues/shear components.

If so, recurrent current/shear compensation may connect back to the CP-S / CE-T strain-payer architecture without introducing a genuinely new geometric currency.
