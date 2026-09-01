# DSD M5-518 — Material-marker degeneration is not automatically lineage replacement

Date: 2026-09-01

Status: **REPRESENTATION AUDIT / M5-517 CORRECTLY MAKES THE UNIT-MEAN EFFECTIVE-EIGENVALUE LAW CONDITIONAL ON A UNIFORMLY NONDEGENERATE MATERIAL MARKER, BUT THE COMPLEMENTARY EVENT `rho(marker)->0` MUST NOT BE IDENTIFIED AUTOMATICALLY WITH MATERIAL-FLUX LINEAGE LOSS / A PERSISTENT MATERIAL SURFACE CAN RETAIN FIXED NONZERO VORTICITY FLUX WHILE A PRESELECTED MATERIAL PARTICLE PASSES THROUGH A LOW-VORTICITY REGION AND THE ACTIVE CARRIER MAXIMUM MOVES ELSEWHERE ON THE SAME SURFACE / FINITE-MEMORY REPLACEMENT COUNTS MATERIAL/FLUX IDENTITY CHANGES, NOT CHANGES OF A POINTWISE REPRESENTATIVE / THUS THE ANCHORED HARD CORE SPLITS INTO A UNIFORMLY NONDEGENERATE MARKER BRANCH WITH THE M5-517 EXACT LOG-AMPLITUDE COBoundary, OR A MARKER-MIGRATION BRANCH THAT REQUIRES A SURFACE/PACKET-LEVEL OBSERVABLE / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Why M5-517 needs a representation audit

M5-517 derived, along an anchored coherent material marker,

\[
D_B\log\rho
=\lambda_{eff}-1,
\]

with

\[
\lambda_{eff}
=\sigma+\frac{\Delta\rho}{\rho}-|\nabla\xi|^2.
\]

If

\[
0<\rho_-\le\rho(\theta)\le\rho_+<\infty,
\]

then `log rho` is bounded and

\[
\boxed{
\langle\lambda_{eff}\rangle=1.
}
\]

The question is what happens when the lower bound fails.

It is tempting to label that failure as lineage replacement.  M5-518 audits that temptation.

---

## 2. A lineage is not one point

The persistent objects in M5-393--397 and M5-488--490 are material-flux descendants represented by material surfaces/packets with a directed vorticity-flux label.

A point marker

\[
X_i(\theta)
\]

is only a representative used to sample local amplitude/direction.

The material-flux identity is

\[
\Phi_i(\theta)
=\int_{\Sigma_i(\theta)}W\cdot n\,dA.
\]

The lineage identity is tied to the transported material surface and flux genealogy, not to one distinguished particle on that surface.

Therefore

\[
\boxed{
\text{point-marker identity}
\ne
\text{material-flux lineage identity}.
}
\]

---

## 3. A marker can weaken while the same flux lineage survives

Suppose a selected material point satisfies

\[
\rho_i(X_i(\theta_n),\theta_n)	o0.
\]

This does not imply

\[
\Phi_i(\theta_n)	o0.
\]

The flux integral may remain nonzero because other portions of the same transported surface carry vorticity.

Even if the packet remains spatially coherent, the local point of maximal amplitude may move relative to the original material marker because diffusion redistributes vorticity inside the material surface.

Thus the configuration

\[
\boxed{
\rho_i(X_i(\theta_n))\to0,
\qquad
|\Phi_i(\theta_n)|\ge\phi_0>0
}
\]

is not logically excluded.

---

## 4. Flux plus area gives a packet amplitude floor, not a marker floor

Assume the active coherent material surface has a controlled area

\[
|\Sigma_i(\theta)|
\le A_*.
\]

Then

\[
|\Phi_i|
\le
\int_{\Sigma_i}|W|dA
\le
A_*\sup_{\Sigma_i}|W|.
\]

Hence a fixed flux lower bound gives

\[
\boxed{
\sup_{\Sigma_i(\theta)}|W|
\ge
\frac{\phi_0}{A_*}.
}
\]

This ensures that **some** point on the material surface remains active.

It does not imply that one preselected material point satisfies the same lower bound for all time.

Therefore the natural compact representative may migrate on the same lineage.

---

## 5. Why reselecting the maximizer loses the exact material derivative

Define the packet amplitude

\[
M_i(\theta)
:=
\sup_{x\in\Sigma_i(\theta)}|W(x,\theta)|.
\]

Under the flux/area assumptions, `M_i` has a positive lower bound and the compact Type-I hull gives an upper bound.

However a point attaining the supremum can change with time.

The derivative of `M_i` is then an upper/lower Dini derivative of a moving maximum, not simply

\[
D_B\rho(X_i(\theta),\theta).
\]

Consequently the exact identity

\[
D_B\log\rho
=\lambda_{eff}-1
\]

cannot be transferred without error to

\[
\frac d{d\theta}\log M_i.
\]

At a smooth maximizing point one may exploit

\[
\nabla\rho=0,
\qquad
\Delta\rho\le0,
\]

but switching maximizers and lack of a material trajectory prevent an exact global coboundary.

---

## 6. Finite memory counts lineage changes, not representative changes

M5-488 finite memory limits repeated storage/replacement of genuinely distinct fixed-flux material labels.

If one stays on the same transported material surface and only changes the sampling point, no new lineage label has been created.

Therefore

\[
\boxed{
\text{marker migration}
\not\Longrightarrow
\text{finite-memory replacement cost}.
}
\]

Finite memory becomes applicable only when one proves a change in material/flux identity, not merely a change in the location of the active representative.

---

## 7. Corrected anchored split

The anchored pair branch should therefore be separated as

\[
\boxed{
\mathcal B_{pair}^{anchor}
\Longrightarrow
\mathcal B_{marker}^{nondeg}
\lor
\mathcal B_{marker}^{migrate}.
}
\]

### Nondegenerate material-marker branch

There exists a persistent material marker with

\[
0<\rho_-\le\rho_i(\theta)\le\rho_+.
\]

Then M5-517 applies exactly:

\[
\boxed{
\Sigma_iW_i+\Delta W_i=\lambda_iW_i,
\qquad
\langle\lambda_i\rangle=1.
}
\]

### Marker-migration branch

No single material point remains uniformly active even though the material-flux lineage/packet persists.

Then the pointwise log-amplitude observable is not a bounded material coboundary, and a packet/surface-level scalar is required.

---

## 8. The combined eigenline relation remains valid pointwise where the anchored direction is defined

The representation correction does **not** invalidate the local vector identity derived in M5-517.

At every nonzero anchored material marker,

\[
\boxed{
P_\xi^\perp(\Sigma W+\Delta W)=0
}
\]

and

\[
\boxed{
\tau=-\mathcal D_\xi.
}
\]

What fails without a lower amplitude floor is only the passage from

\[
D_B\log\rho=\lambda_{eff}-1
\]

to a bounded long-time coboundary with zero mean derivative.

This distinction must remain explicit.

---

## 9. Candidate packet-level observables

A replacement for the migrating marker should satisfy two requirements:

1. remain attached to the same material-flux lineage;
2. have an exact or one-sided evolution law.

Natural candidates include

\[
\boxed{
M_i(\theta)=\sup_{\Sigma_i(\theta)}|W|
}
\]

and surface quantities such as

\[
\boxed{
A_{2,i}(\theta)
:=
\int_{\Sigma_i(\theta)}|W|^2dA.
}
\]

The first has a maximum-principle-type inequality but no exact smooth material derivative.

The second has a transport identity, but stretching, surface deformation, and diffusion generate additional terms that must be audited.

Material flux itself already has the exact M5-489 law but is sign-indefinite.

---

## 10. A useful one-sided maximum inequality

At a smooth instantaneous maximum of `rho` on the full spatial field,

\[
\nabla\rho=0,
\qquad
\Delta\rho\le0.
\]

The magnitude equation gives schematically

\[
D_B\log\rho_{max}
\le
\sigma_{max}-1-|\nabla\xi|^2_{max}.
\]

Thus maintaining/growing a normalized vorticity maximum requires axial stretching to pay the explicit similarity damping and directional-gradient loss.

However this is a Dini/maximum-track inequality, not the exact anchored material-marker identity.

M5-518 records it only as a candidate packet-level route.

---

## 11. DSD interpretation

The distinction is one of structural identity versus representative location.

A material lineage is a persistent transported relation.

A point marker is a coordinate chosen to describe part of that relation.

Diffusion can make the best representative migrate without destroying the underlying lineage.

Therefore DSD audit forbids the inference

\[
\boxed{
\text{representative failure}
\Rightarrow
\text{structural identity failure}.
}
\]

This is exactly the kind of hidden inheritance error the audit framework is designed to catch.

---

## 12. Updated hard core

The anchored compact survivor is now accurately split into

\[
\boxed{
\begin{aligned}
&\text{(A) nondegenerate anchored material marker:}\\
&\qquad \tau_i=-\mathcal D_i,
\quad
\Sigma_iW_i+\Delta W_i=\lambda_iW_i,
\quad
\langle\lambda_i\rangle=1;\\[1ex]
&\text{(B) migrating anchored representative on persistent flux surface:}\\
&\qquad \tau_i=-\mathcal D_i\text{ pointwise where defined,}\\
&\qquad \text{but no bounded point-marker log-amplitude coboundary.}
\end{aligned}
}
\]

Neither branch is yet contradictory.

---

## 13. Highest-value next target

The next calculation should derive a surface/packet amplitude balance for the migrating-representative branch.

The cleanest candidate is the material-surface quadratic vorticity content

\[
A_{2,i}(\theta)
=
\int_{\Sigma_i(\theta)}|W|^2dA.
\]

Because the similarity material surface has a known area-vector evolution and the vorticity equation is explicit, one can derive its exact transport law and determine whether anchored transverse cancellation removes enough terms to produce a signed remainder.

If the quadratic surface law remains sign-indefinite, the marker-migration branch will be identified as another genuine recurrent packet cycle rather than mislabeled as replacement.

---

## 14. Status

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
