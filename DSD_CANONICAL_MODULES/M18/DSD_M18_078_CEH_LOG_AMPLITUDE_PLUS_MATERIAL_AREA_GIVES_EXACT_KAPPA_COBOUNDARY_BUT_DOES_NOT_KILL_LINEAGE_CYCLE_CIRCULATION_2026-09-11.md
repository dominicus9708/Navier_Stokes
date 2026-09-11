# M18-078 — CE-H log-amplitude plus material area gives an exact kappa coboundary, but does not kill lineage-cycle circulation

**Date:** 2026-09-11  
**Status:** CE-H MATERIAL COBOUNDARY / CYCLE-COCYCLE AUDIT / NEGATIVE MONOTONICITY RESULT WITH NEW EXACT IDENTITY

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Purpose

M18-077 reduces unavoidable material-label redistribution on the finite persistent lineage network to

\[
G_{cycle}^{mean}
\lor
G_{cycle}^{rev}
\lor
G_{graph/label\ realization\ loss}.
\]

The natural next candidate for a signed cocycle is the exact CE-H amplitude equation

\[
\boxed{
D_B\log\rho=\sigma+\kappa-1.
}
\]

The question is whether this is sufficiently exact to prohibit recurrent lineage circulation.

The answer is only partly positive.

When combined with the material-surface Jacobian, it produces the exact coboundary

\[
\boxed{
D_B\log(\rho A_\Sigma)=\kappa.
}
\]

However this coboundary is attached to one material surface element, whereas a lineage-graph cycle is a transfer path among different persistent carriers. The graph current is not the material derivative of one single `log rho` state variable.

Thus the identity constrains closed material recurrence but does not by itself eliminate cycle circulation.

---

## 2. Vortex-transverse material surface

Work on the controlled Frobenius CE-H patch of M18-073--076, with

\[
n=\xi,
\qquad
f=W\cdot n=\rho.
\]

The material-surface continuity equation used in M18-076 is

\[
\boxed{
D_B\rho
+(1-\sigma)\rho
+\operatorname{div}_\Sigma J_\Sigma
=0.
}
\]

The exact CE-H amplitude equation is

\[
\boxed{
D_B\rho
=(\sigma+\kappa-1)\rho.
}
\]

Subtracting gives the already certified current-source identity

\[
\boxed{
\operatorname{div}_\Sigma J_\Sigma=-\kappa\rho.
}
\]

---

## 3. Material area Jacobian

Let

\[
A_\Sigma(\theta,a)>0
\]

denote the area Jacobian of the vortex-transverse material surface element labeled by material coordinate `a`, relative to one reference time.

The standard material-surface transport law in the present similarity normalization is exactly the coefficient appearing in the surface continuity equation:

\[
\boxed{
D_B\log A_\Sigma=1-\sigma.
}
\]

Equivalently,

\[
D_BA_\Sigma=(1-\sigma)A_\Sigma.
\]

This is the geometric area-stretch factor dual to the flux-density term in Section 2.

---

## 4. Exact kappa coboundary

Divide the CE-H amplitude equation by \(\rho>0\):

\[
D_B\log\rho
=
\sigma+\kappa-1.
\]

Add the material-area equation:

\[
D_B\log A_\Sigma=1-\sigma.
\]

The strain and similarity terms cancel exactly:

\[
\boxed{
D_B\log(\rho A_\Sigma)
=\kappa.
}
\]

Define the local material flux-area density coordinate

\[
\boxed{
\Lambda_\Sigma
:=
\log(\rho A_\Sigma).
}
\]

Then

\[
\boxed{D_B\Lambda_\Sigma=\kappa.}
\]

Thus \(\kappa\) is an exact scalar cocycle along every active vortex-transverse material surface element.

---

## 5. Integral form

Along one material surface element transported from \(\theta_0\) to \(\theta_1\),

\[
\boxed{
\int_{\theta_0}^{\theta_1}
\kappa(X(a,\theta),\theta)\,d\theta
=
\log
\frac{\rho A_\Sigma(\theta_1,a)}
{\rho A_\Sigma(\theta_0,a)}.
}
\]

Therefore if one material element returns exactly to the same local amplitude-area state,

\[
\rho A_\Sigma(\theta_1,a)
=
\rho A_\Sigma(\theta_0,a),
\]

then

\[
\boxed{
\int_{\theta_0}^{\theta_1}\kappa\,d\theta=0.
}
\]

More generally, on a compact recurrent material state where \(\rho A_\Sigma\) stays uniformly above and below zero,

\[
\frac1T\int_0^T\kappa\,d\theta\to0
\]

along recurrence intervals for that same material element.

This is a genuine signed zero-mean constraint.

---

## 6. Why log rho alone was not the correct cocycle

The amplitude identity alone contains the strain term:

\[
D_B\log\rho
=
\sigma+\kappa-1.
\]

Hence a closed amplitude cycle only gives

\[
\oint(\sigma+\kappa-1)d\theta=0,
\]

allowing strain work and coefficient work to compensate.

The material-area factor removes exactly the strain/similarity contribution and isolates \(\kappa\).

Thus

\[
\boxed{
\log(\rho A_\Sigma)
}

is the sharper material state coordinate.

---

## 7. Flux form of the same identity

Multiply the local density \(\rho\) by the material area Jacobian.

Using Sections 2--3,

\[
\begin{aligned}
D_B(\rho A_\Sigma)
&=
A_\Sigma D_B\rho
+
\rho D_BA_\Sigma\\
&=
\kappa\rho A_\Sigma.
\end{aligned}
\]

Hence

\[
\boxed{
D_B(\rho A_\Sigma)
=\kappa\rho A_\Sigma.
}
\]

At first sight this seems to conflict with surface-flux redistribution. There is no conflict: the pointwise material area element can gain or lose local vortex flux, while the divergence current transports that flux across neighboring surface elements.

Indeed

\[
\operatorname{div}_\Sigma J_\Sigma=-\kappa\rho
\]

is exactly the compensating lateral redistribution law.

---

## 8. Closed-patch total flux remains a conservation statement

For a material patch with no current through its boundary, integrate the surface continuity law.

The local \(\kappa\)-growth and lateral current divergence cancel after surface integration, yielding conservation of the total transported vorticity flux through the closed material patch.

Thus the new coboundary should not be interpreted as creation of net vorticity flux.

It is a local redistribution coordinate.

---

## 9. Why the material coboundary does not kill a lineage-graph cycle

M18-077 uses a finite lineage graph current

\[
j(\theta)\in\mathbb R^E.
\]

An edge transfer between two persistent lineages is not generally the trajectory of one fixed material surface element from one vertex state to another.

The graph cycle may be assembled from transfers among different material patches and different times.

Therefore

\[
\boxed{
\oint_{material}\kappa\,d\theta=0
}

for a closed material element does **not** imply

\[
\boxed{
\oint_{lineage\ graph}\alpha\cdot j=0
}
\]

for an arbitrary graph 1-form.

This is the principal cycle-cocycle firewall.

---

## 10. Time-dependent vertex potentials also fail to give automatic cancellation

Suppose one tries to assign a lineage potential

\[
\phi_i(\theta)
\]

from a lineage-averaged version of \(\Lambda_\Sigma\).

With graph storage law

\[
m'=Bj,
\]

one has

\[
\phi\cdot Bj
=
\frac{d}{d\theta}(\phi\cdot m)
-
\phi'\cdot m.
\]

Thus even if the boundary term is recurrent/bounded, the time-dependent potential produces the residual work

\[
\boxed{-\phi'\cdot m.}
\]

A lineage potential that evolves with strain/coefficient dynamics is therefore not an exact graph potential unless this extra term is controlled.

---

## 11. Constant vertex potentials are blind to cycle space

For a time-independent \(\phi\),

\[
(B^T\phi)\cdot j
=
\phi\cdot Bj.
\]

But on a mean cycle current

\[
\bar j\in\ker B,
\]

\[
\boxed{
(B^T\phi)\cdot\bar j=0.
}
\]

Thus a genuine graph cycle current is invisible to every exact vertex-gradient 1-form.

The only way a state potential can exclude circulation is if the physical PDE proves that the admissible current itself is gradient-like in lineage space.

No such constitutive law is presently certified.

---

## 12. Relation to the surface Hodge gradient

On each Frobenius patch,

\[
J_G=\nabla_\Sigma\psi,
\qquad
-\Delta_\Sigma\psi=\kappa\rho.
\]

This is a **spatial surface gradient**.

It must not be confused with a gradient on the discrete lineage graph.

A field can be gradient-like within each surface patch while transfers among multiple patches form a nontrivial graph cycle.

Therefore

\[
\boxed{
\text{surface Hodge exactness}
\not\Rightarrow
\text{lineage-graph exactness}.
}
\]

---

## 13. New constraint on reversible cycles

Although the coboundary does not close the graph cycle, it constrains how a reversible cycle can be realized.

If one fixed material patch returns recurrently with compact nondegenerate \(\rho A_\Sigma\), then its long-time signed coefficient mean must vanish:

\[
\boxed{\langle\kappa\rangle_{material}=0.}
\]

Yet whole-space CE-H has

\[
\boxed{
P
=
-\int\kappa\rho^2dx
\ge0.
}
\]

Thus nontrivial palinstrophy requires a negative \(\rho^2\)-weighted coefficient bias even when an individual compact material recurrence has zero unweighted material mean.

Accordingly, a compact recurrent reversible branch must realize a nontrivial amplitude/coefficient correlation rather than a uniform-sign \(\kappa\) drift.

This is consistent with the amplitude-diffusion covariance/sheath structure already found in M18-062--070.

---

## 14. Exact branch split after the coboundary audit

The material-current route becomes

\[
\boxed{
\text{mandatory CE-H current}
\Longrightarrow
\begin{cases}
G_{self\text{-}helicity/twist},\\
G_{surface/label\ geometry\ loss},\\
G_{cycle}^{mean},\\
G_{cycle}^{rev,cov}.
\end{cases}
}
\]

where the reversible branch now carries the additional material constraint

\[
\boxed{
\langle\kappa\rangle_{material}=0
}
\]

on every genuinely closed nondegenerate material recurrence, while retaining a nonzero amplitude-weighted coefficient bias needed to support palinstrophy.

---

## 15. What kind of cocycle is still needed

The desired next object cannot be merely an exact material scalar potential.

It must be sensitive to cycle-space transfer.

Two possibilities remain natural.

### A. Physical edge 1-form

Construct an edge observable \(\alpha_{ab}\) from the strain/coefficient difference between interacting lineages such that

\[
\sum_{(a,b)\in C}\alpha_{ab}
\]

has a definite sign or vanishes for every realizable CE-H cycle.

### B. Dissipative graph constitutive law

Show that lineage transfer satisfies a relation analogous to

\[
j=-M B^T\phi+j_C,
\]

with a positive mobility and a separately controlled cycle current.

No such law has yet been derived.

---

## 16. Audit verdict

### Certified

1. On a vortex-transverse CE-H material element,
   \[
   D_B\log(\rho A_\Sigma)=\kappa.
   \]
2. Hence \(\kappa\) is an exact material coboundary.
3. A closed nondegenerate material amplitude-area recurrence has zero integrated \(\kappa\).
4. The strain term that contaminates \(D_B\log\rho\) is exactly removed by material area evolution.
5. This material exactness does not imply lineage-graph exactness.
6. Time-dependent lineage potentials produce an extra \(-\phi'\cdot m\) work term.
7. Constant vertex potentials are blind to graph cycle currents.
8. Surface Hodge-gradient exactness is not the same as graph-gradient exactness.
9. Reversible compact material cycles must realize amplitude/coefficient covariance rather than a one-sign \(\kappa\) drift.

### Still open

1. A cycle-sensitive physical graph 1-form.
2. A constitutive law for lineage transfer.
3. The self-helicity/twist branch.
4. Surface/label geometry loss.
5. Ancestry, remote, and critical roots.
6. Global 3D Navier--Stokes regularity.

## 17. Next target

M18-079 should compare two interacting persistent lineages directly.

For a recurrent edge \(a\leftrightarrow b\), define the material amplitude-area potentials

\[
\Lambda_a=\log(\rho_aA_a),
\qquad
\Lambda_b=\log(\rho_bA_b),
\]

and the difference

\[
\Delta\Lambda_{ab}=\Lambda_b-\Lambda_a.
\]

Audit whether the transfer current satisfies any sign relation with

\[
\Delta\Lambda_{ab},
\]

or whether explicit CE-H configurations permit current against either sign.

If no sign law exists, the gradient-flow route should be retired and the remaining cycle problem classified as genuinely conservative/hamiltonian-like rather than dissipative.
