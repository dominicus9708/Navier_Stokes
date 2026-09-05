# DSD M17-178 — M5 transverse-flux labels do not live on the vertical nodal filament; the previous direct M5-to-`O_V` bridge is conditional

Date: 2026-09-06  
Canonical ID: **M17-178**

Status: **CORRECTIVE DSD AUDIT / M5-647 DEFINES `dmu_0` ON REGULAR VORTEX-LINE FLOW BOXES WITH `W != 0` AND EXPLICITLY NOTES THAT THE ANALYTIC ZERO SET `W=0` CARRIES ZERO VORTICITY-FLUX DENSITY. M17-090'S VERTICAL OCTUPOLE FORMULA `O_V=-(1/5)|Q|_F^2 kappa_3` IS DERIVED AT THE VERTICAL NODAL FILAMENT, WHERE `W=0`, `grad_h q=0`, AND `q_13=q_23=0`. THEREFORE M17-095'S LABEL-BY-LABEL SUBSTITUTION OF NODAL-CORE `O_V` AND `r_V` INTO THE M5 BASE-FLUX CURRENT REQUIRES AN ADDITIONAL MAP FROM REGULAR VORTEX-LINE LABELS TO NODAL CORES, TOGETHER WITH A THEOREM RELATING THE REGULAR-LABEL CROSSING RATE `h_lambda` TO THE NODAL-CORE CROSSING RATE. NO SUCH MAP/THEOREM HAS BEEN DERIVED. CONSEQUENTLY THE DIRECT M5->NODAL-OCTUPOLE BIAS IN M17-095, AND ALL LATER STATEMENTS THAT USE IT AS AN UNCONDITIONAL INPUT, MUST BE READ AS CONDITIONAL. THE LOCAL PRESSURE/OCTUPOLE RESULTS M17-164, M17-166--171 REMAIN VALID INDEPENDENTLY. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. What the M5 base measure actually measures

M5-647 constructs, on one fixed base slice, a countable transverse flow-box atlas for the regular vorticity field.

The base measure is a positive transverse vorticity-flux measure

\[
\boxed{d\mu_0(\lambda)}
\]

on **material vortex-line labels**.

Every contributing flow box lies where

\[
\boxed{W\neq0.}
\]

M5-647 explicitly records that the analytic zero set

\[
Z=\{W=0\}
\]

carries no missing vorticity flux because the flux density itself vanishes there.

Thus

\[
\boxed{\mu_0(Z)=0}
\]

in the sense relevant to the transverse-flux resource.

---

## 2. Where the vertical octupole formula lives

M17-090 is a vertical **nodal-filament** calculation.

At the marked filament,

\[
\boxed{
W=0,
\qquad
\nabla_hq=0,
\qquad
q_{13}=q_{23}=0.
}
\]

The vertical payer octupole then satisfies

\[
\boxed{
O_V
=(\mathcal O_{loc}^{(3)})_{333}
=-\frac15\partial_3(\kappa|Q|_F^2).
}
\]

At a regular nodal `kappa=0` crossing,

\[
\boxed{
O_V=-\frac15|Q|_F^2\kappa_3.
}
\]

The factorization

\[
\boxed{
h_{nodal}=(B_3-v_0)\kappa_3}
\]

is likewise a statement at that nodal filament.

---

## 3. The support mismatch

M5-685 uses

\[
\boxed{
G_\Phi(k,\theta)
=
\int h_\lambda a_\lambda
\delta(k-\kappa_\lambda)d\mu_0(\lambda),
}
\]

where `lambda` is a regular material vortex-line label inherited from M5-647.

M17-095 then inserted

\[
 h=-\frac{5r_V}{|Q|_F^2}O_V
\]

inside the same `dmu_0` integral.

But this substitution is valid only if each M5 label `lambda` has been assigned a vertical nodal core at which

1. `O_V(lambda)` is defined;
2. `r_V(lambda)` is defined;
3. the M5 material crossing rate `h_lambda` equals the nodal-core crossing rate appearing in M17-090.

No such assignment theorem is present in M5-647, M17-090, or M17-095.

Therefore the step

\[
\boxed{
\int h_\lambda a_\lambda\delta(\kappa_\lambda)d\mu_0
\stackrel{?}{=}
-5\int a_\lambda
\frac{r_{V,\lambda}O_{V,\lambda}}{|Q_\lambda|_F^2}
\delta(\kappa_\lambda)d\mu_0
}
\]

is not currently an unconditional identity.

---

## 4. Why analytic continuation does not automatically fix it

The reduced great-circle equations admit analytic continuation of the scalar functions `F`, `G`, and the `(q,x_3)` dynamics toward regular nodal limits.

However analytic continuation of **functions** is not the same as continuation of the **transverse-flux measure** onto the nodal set.

At `W=0`, the physical vorticity-flux density vanishes.

Thus one cannot assign positive M5 flux mass to the nodal filament merely because the semilinear variables extend smoothly there.

---

## 5. Downstream status correction

The following results remain independent and valid as local/global PDE identities:

- M17-082: vertical axial global `l=3` pressure lock;
- M17-089--091: vertical kernel/crossing geometry and local octupole factorization;
- M17-164: localized `-kappa rho^2` pressure-production coefficient is proportional to `O_V`;
- M17-166: radial `l=3` scale-current identity;
- M17-167--168: global `kappa`-production as an axial palinstrophy moment and its outer-tail cancellation cost;
- M17-169--171: semilinear Hessian / hodograph / rotated-gradient identities.

The following statements are **conditional on an additional flux-label-to-nodal-core bridge**:

- M17-095's strict M5-weighted `r_V O_V` bias;
- M17-165's M5-weighted localized pressure-production bias;
- the M5-forced parts of M17-172--177, including the strict zero-loop pressure-variance lower bound.

Their internal geometric identities remain useful, but the M5 forcing cannot presently be attached to them unconditionally.

---

## 6. Correct next bridge

The next valid task is not to relabel `dmu_0` as a nodal measure.

It is to construct an **adapted regular great-circle transverse chart** and compute the physical vorticity-flux form in the coordinates

\[
(q,x_3).
\]

This can determine precisely whether the M5 flux measure becomes ordinary label-plane area on regular `W != 0` charts and what happens as `q` approaches the nodal critical level.

Even if the regular pushforward is exactly Lebesgue area, the nodal critical level is expected to have zero area measure; then a separate trace/localization theorem would still be required to force M5 hysteresis at the nodal slice.

---

## 7. DSD audit

### Audit A — measure support
`dmu_0` is a regular transverse-vorticity-flux measure. It does not automatically charge `W=0`.

### Audit B — descriptor support
`O_V` is a nodal-core descriptor. It must not be attached to arbitrary regular vortex-line labels without a map.

### Audit C — analytic continuation
Function continuation does not imply measure continuation.

### Audit D — downstream claims
The M5-forced zero-loop variance chain is reclassified as conditional rather than deleted; its pure semilinear/pressure identities remain valid.

### Audit E — proof status
This correction weakens one claimed bridge but makes the remaining frontier more precise.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
