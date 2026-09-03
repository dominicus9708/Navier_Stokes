# DSD M5-644 — Local Clebsch representation turns regular kappa levels into additive vorticity-flux coordinates

Date: 2026-09-03

Status: **INTERNAL LOCAL DIFFERENTIAL-GEOMETRIC REDUCTION / CE-H SATISFIES `W·grad kappa=0` AND `div W=0`. ON EVERY SIMPLY CONNECTED REGULAR REGION WHERE `grad kappa!=0`, THESE CONDITIONS GIVE A LOCAL SECOND EULER/CLEBSCH POTENTIAL `psi` SUCH THAT `W=grad kappa x grad psi`. VORTEX LINES ARE THEREFORE LOCAL INTERSECTIONS OF `kappa=const` AND `psi=const`, AND THE VORTICITY TWO-FORM IS `d kappa wedge d psi`; TRANSVERSE VORTICITY FLUX IS ADDITIVE AREA IN THE `(kappa,psi)` POTENTIAL PLANE. THUS THE M5-643 MISSING FLUX TRANSVERSAL EXISTS LOCALLY. THE REMAINING GAP IS GLOBAL: PATCHING `psi` ACROSS THE WHOLE FINITE RESERVOIR MAY FAIL BECAUSE OF VORTEX-SURFACE TOPOLOGY/MONODROMY OR MAY PRODUCE UNBOUNDED POTENTIAL RANGE. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. CE-H first integral and divergence-free field

On CE-H,

\[
\boxed{W\cdot\nabla\kappa=0}
\]

and

\[
\boxed{\nabla\cdot W=0.}
\]

Consider a regular region

\[
\Omega_{reg}\subset\{W\ne0,\ \nabla\kappa\ne0\}
\]

on which the kappa level surfaces form a smooth foliation.

The vector field `W` is tangent to each kappa level surface.

---

## 2. Vorticity flux two-form

Let `vol` be the Euclidean volume form and define the vorticity flux two-form

\[
\beta:=\iota_W\,vol.
\]

Divergence-free means

\[
\boxed{d\beta=0.}
\]

The tangency condition `W·grad kappa=0` is equivalent to the algebraic statement that the flux form has `d kappa` as a factor locally.

On a regular kappa chart one can therefore write

\[
\beta=d\kappa\wedge\alpha
\]

for a local one-form `alpha` tangent to the level foliation.

The closedness condition gives, after restricting to each simply connected level patch, that `alpha` is locally exact up to the irrelevant `d kappa` gauge.

Hence there exists a scalar `psi` such that

\[
\boxed{\beta=d\kappa\wedge d\psi.}
\]

---

## 3. Vector form

Using the Euclidean identification between flux two-forms and vectors,

\[
\iota_{\nabla\kappa\times\nabla\psi}vol
=d\kappa\wedge d\psi.
\]

Therefore

\[
\boxed{
W=\nabla\kappa\times\nabla\psi
}
\]

on the local regular chart.

This is a local Euler/Clebsch representation with `kappa` itself as one Euler potential.

---

## 4. Vortex-line geometry

Since

\[
W\cdot\nabla\kappa=0,
\qquad
W\cdot\nabla\psi=0,
\]

vortex lines are local intersections

\[
\boxed{
\kappa=\text{constant},
\qquad
\psi=\text{constant}.
}
\]

Thus the regular CE-H vorticity foliation is locally integrable by two scalar labels.

This makes precise the quotient picture suggested by M5-611 and the material kappa-level geometry of M5-638.

---

## 5. Exact local flux additivity

Let `S` be a transverse oriented surface patch lying inside one Clebsch chart.

Then

\[
\Phi(S)
=\int_S W\cdot n\,dA
=\int_S\beta.
\]

Using the Clebsch form,

\[
\boxed{
\Phi(S)
=\int_S d\kappa\wedge d\psi.
}
\]

If `(kappa,psi)` are one-to-one coordinates on the patch, this is simply the oriented area of its image in potential space:

\[
\boxed{
\Phi(S)
=\operatorname{Area}_{oriented}\bigl((\kappa,\psi)(S)\bigr).
}
\]

Therefore disjoint local vortex-tube bundles correspond to disjoint regions in the local `(kappa,psi)` flux plane and their signed fluxes are exactly additive.

---

## 6. Relevance to M5-643

M5-643 isolated the missing statement needed for a finite-resource contradiction:

one wants a common coordinate/transversal that counts the non-discounted fluxes of distinct packet labels additively.

M5-644 proves:

\[
\boxed{
\text{such an additive flux coordinate exists locally on every regular kappa chart.}
}
\]

Thus the obstruction is no longer local differential geometry.

It is global patching/resource size.

---

## 7. Globalization alternatives

To finish the flux-resource argument one would need one of the following.

### G1. Global Clebsch/transversal branch

A finite cover can be patched into a global or finitely-sheeted potential coordinate with controlled total `(kappa,psi)` flux area.

Then infinitely many distinct packet labels each carrying `phi_*` could potentially contradict finite total flux area.

### G2. Topological obstruction branch

Global `psi` fails because of monodromy, linked vortex lines, nontrivial level-surface topology, or recurrent foliation geometry.

Then the failure itself becomes a concrete topological survivor rather than an unspecified lack of transversal.

Thus

\[
\boxed{
E_{CEH}^{regular}
\Longrightarrow
G_{Clebsch}^{global/control}
\lor
T_{foliation}^{topological}.
}
\]

---

## 8. Critical kappa set

The representation requires

\[
\nabla\kappa\ne0.
\]

Critical kappa points/strata are not covered by one regular Clebsch chart.

M5-639 already shows that the exact zero-kappa set has zero three-dimensional measure, but critical sets at nonzero kappa may still exist and require separate patching.

Therefore no global Euler-potential representation is assumed at this stage.

---

## 9. Resource firewall

Even if a global Clebsch potential exists, finite `L2` enstrophy does not automatically imply finite total potential-plane area

\[
\int |d\kappa\wedge d\psi|.
\]

A separate quantitative bound is still needed.

Thus M5-644 establishes **local additivity**, not yet a finite global flux budget.

---

## 10. Literature audit note

A targeted literature search did not identify a Liouville/classification theorem directly matching the full time-dependent CE-H system

\[
\Delta W=\kappa W,
\quad
W\cdot\nabla\kappa=0,
\quad
\Sigma W=\sigma W,
\quad
W\in L^2.
\]

Available Liouville results found in the search primarily concern stationary Navier--Stokes classes with additional integrability/decay assumptions and cannot be substituted for the present dynamic recurrent problem without new justification.

---

## 11. Next target

Audit whether the compact finite core and the analytic kappa foliation permit a finite Clebsch atlas whose transition maps preserve flux area strongly enough to bound the total absolute flux of distinct coherent packet labels.

If yes, M5-643 may become a finite-resource contradiction.

If not, identify the exact topological obstruction (linked/recurrent vortex-surface architecture) and retain it as the final geometric branch.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]