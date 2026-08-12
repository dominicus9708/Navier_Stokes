# DSD four-paper first-pass bridge to the Navier–Stokes proof challenge

Date: 2026-08-12

Status: **MODEL / BRIDGE DESIGN + CONJECTURE / TARGET**.

This note does not claim that Dimensional-Structural Describability (DSD) proves Navier–Stokes regularity. It fixes a conservative first-pass dictionary from the four current DSD layers to the 3D incompressible Navier–Stokes problem on `R^3`, while marking every application-specific identification as a bridge rather than as an existing DSD theorem.

## 0. Baseline Navier–Stokes object

The primary PDE remains unchanged:

\[
\partial_t u+(u\cdot\nabla)u=-\nabla p+\nu\Delta u,
\qquad
\nabla\cdot u=0,
\qquad
\nu>0,
\qquad
x\in\mathbb R^3,\ t\ge0.
\]

The DSD layer is initially an auxiliary description/audit layer. No new force, finite-speed pressure law, extra dimension, or constitutive coefficient may be inserted into the PDE merely because a DSD construction allows one.

## 1. Formation Axiom System -> typed fluid-state formation

### 1.1 Bridge domain

Use the physical domain

\[
X=\mathbb R^3
\]

with time kept as an evolution parameter rather than being counted as a fourth realized spatial axis.

At a fixed time and fixed descriptive resolution, introduce channel families for quantities that already exist in the PDE or are derived from it:

\[
q\in\{u_x,u_y,u_z,p,\omega_x,\omega_y,\omega_z\},
\qquad
\omega=\nabla\times u.
\]

Additional channels such as strain or shell-energy channels may be introduced later, but only as explicitly derived readouts.

### 1.2 Admissibility bridge

The Navier–Stokes-side compatibility conditions are not redefined as DSD axioms. They enter as application-level admissibility requirements, beginning with

\[
\nabla\cdot u=0
\]

and the required smoothness/decay hypotheses of the chosen proof class.

The Formation layer is used to keep separate:

- channel existence;
- applicability at the current coordinate location;
- defined zero;
- defined nonzero value;
- composite equality despite different channel structures.

### 1.3 Coordinate-singularity application

For `r=|x|>0`,

\[
e_r=\frac{x}{|x|},\qquad u_r=u\cdot e_r.
\]

At `r=0`, `e_r` is undefined. Therefore the radial-direction readout at the origin is **inapplicable/undefined**, not automatically a defined value `u_r=0`.

By contrast, for `r>0`, a state satisfying `u_r=0` has an applicable radial channel with a **defined zero** value.

This distinction is mandatory in code and later proof notes; zero-padding at the origin is forbidden.

## 2. Axis-property layer -> fixed spatial rank and derived directions

### 2.1 Realized spatial axes

The ambient spatial realized-axis rank is fixed to three:

\[
\operatorname{rank}_{\rm space}=3,
\qquad
(e_x,e_y,e_z).
\]

The spherical direction `e_r(x)` is a local direction inside the realized 3D span, not a fourth independent axis.

Likewise, adding more diagnostic channels, a larger property matrix, or more spherical sectors must not be interpreted as increasing spatial rank.

### 2.2 Cartesian/spherical double readout

Track the same state through two compatible directional descriptions:

\[
u=(u_x,u_y,u_z)
\]

and

\[
u=u_r e_r+u_t,
\qquad
u_t=u-u_r e_r.
\]

The first is axis-resolved; the second resolves radial versus tangential reorganization. Their agreement becomes an internal consistency test.

### 2.3 Rotational control

The benchmark initial fields obtained by rotating an `x`, `y`, or `z` seed must give equivalent scalar diagnostics up to rotation. A persistent orientation-specific difference is treated first as a numerical/representation anisotropy warning.

## 3. Channel-indexed Static Aggregation -> fixed-time shell descriptors

The static layer is used only at a fixed time slice. It does not itself define evolution.

For each `r>0`, use the normalized shell measure

\[
d\mu_r=\frac{dS}{4\pi r^2}
\]

and form separate component terms.

### 3.1 Primary shell terms

Energy:

\[
T_E(r,t)=\int_{S_r}\frac12|u|^2\,d\mu_r.
\]

Enstrophy-type term:

\[
T_W(r,t)=\int_{S_r}|\omega|^2\,d\mu_r.
\]

Pressure-fluctuation term:

\[
\bar p(r,t)=\int_{S_r}p\,d\mu_r,
\]

\[
T_P(r,t)=\int_{S_r}|p-\bar p|^2\,d\mu_r.
\]

Axis-resolved energy terms:

\[
T_{E_i}(r,t)=\int_{S_r}\frac12|u_i|^2\,d\mu_r,
\qquad i\in\{x,y,z\}.
\]

### 3.2 Do not collapse too early

Define the first working descriptor as a channel-resolved tuple rather than a single scalar:

\[
\mathcal A(r,t)
=
\bigl(
T_E,T_W,T_P,T_{E_x},T_{E_y},T_{E_z}
\bigr).
\]

This is deliberate. Both the Formation and Static Aggregation programs contain explicit information-loss/collision phenomena: equal aggregate readouts can come from different channel or property states. Therefore

\[
T_E^{(1)}=T_E^{(2)}
\]

must never be interpreted by itself as equality of fluid state, vorticity state, or future dynamics.

### 3.3 Directional structural entropy diagnostic

Partition a sphere into angular sectors `A_j`. Let `E_j(r,t)` be the nonnegative energy assigned to sector `j` and

\[
p_j=\frac{E_j}{\sum_kE_k}
\]

when the denominator is nonzero. Define

\[
S_{\rm dir}(r,t)=-\sum_jp_j\log p_j.
\]

This is a directional-distribution diagnostic only. It is not thermodynamic entropy and is not, at this stage, a regularity criterion.

It can test whether an initially axis-concentrated disturbance spreads over the available `4\pi` angular directions or remains concentrated in a small set of directions.

## 4. Structural Reorganization Dynamics -> Navier–Stokes time lineage

### 4.1 Fixed-time recovery

At every fixed `t`, the dynamic state must recover the static shell descriptor `\mathcal A(r,t)`. This is the direct place to use the dynamics paper's fixed-time static-recovery logic.

### 4.2 Reorganization decomposition

Do not replace the Navier–Stokes equation. Instead split its existing right-hand side into three typed reorganization contributions:

\[
R_{\rm adv}=-(u\cdot\nabla)u,
\]

\[
R_{\rm pres}=-\nabla p,
\]

\[
R_{\rm visc}=\nu\Delta u,
\]

so that

\[
\partial_tu
=R_{\rm adv}+R_{\rm pres}+R_{\rm visc}.
\]

This gives the first DSD-to-PDE bridge:

- advection channel: self-transport/reorganization;
- pressure channel: incompressibility-compatible nonlocal correction;
- viscous channel: spatial smoothing/diffusive reorganization.

The labels are bookkeeping semantics, not new physics.

### 4.3 Finite-propagation restriction

The DSD dynamics paper contains finite-propagation and characteristic-speed constructions for appropriate hyperbolic systems and specializations. They are **not imported as a hard `c_info` bound into the standard incompressible Navier–Stokes track**.

Reason: the standard incompressible pressure constraint is elliptic/nonlocal and viscosity is parabolic. Imposing a finite support-front speed would alter the mathematical problem unless a separate equivalence theorem were proved.

Therefore:

- `c_info` may remain a comparison/diagnostic concept;
- it may be used in a future compressible or hyperbolic bridge;
- it is not an assumption in the present Clay-aligned incompressible proof track.

## 5. First candidate scale-aware DSD diagnostic

The centered shell diagnostics can be made dimensionless under the natural Navier–Stokes scaling by considering combinations such as

\[
r^2T_E(r,t),
\qquad
r^4T_W(r,t),
\qquad
r^4T_P(r,t).
\]

Define the exploratory centered quantity

\[
\mathcal D_O(t)
=
\sup_{r>0}
\left[
 r^2T_E(r,t)
 +\alpha r^4T_W(r,t)
 +\beta r^4T_P(r,t)
\right],
\]

with nonnegative bookkeeping weights `\alpha,\beta`.

Status: **CONJECTURE / TARGET DIAGNOSTIC ONLY**.

No coercivity or regularity theorem is currently claimed for `\mathcal D_O`.

For a proof covering arbitrary initial data, an origin-centered quantity is insufficient. The eventual translation-complete version must examine every center:

\[
\mathcal D_{\rm all}(t)
=
\sup_{x_0\in\mathbb R^3}
\sup_{r>0}
\mathcal D(x_0,r,t).
\]

The central benchmark is therefore a discovery tool; the all-center quantity is the structurally relevant proof target.

## 6. What a successful DSD route would still have to prove

A genuine proof route needs all of the following bridges.

1. **Representation bridge:** every admissible smooth Navier–Stokes state used in the proof class yields a well-defined DSD channel/axis/static state without discarding PDE information needed for regularity.
2. **Evolution compatibility:** differentiating the DSD component terms along a Navier–Stokes solution is justified and agrees with the PDE evolution.
3. **Non-collision safeguard:** the chosen descriptor must not identify states whose regularity behavior can differ, unless an additional theorem shows that the lost information is irrelevant.
4. **Coercivity/regularity bridge:** bounded DSD descriptor implies control of a mathematically sufficient regularity quantity.
5. **A-priori bound:** that DSD descriptor remains bounded for every finite time from arbitrary admissible smooth initial data.
6. **Translation/rotation completeness:** the argument must not depend on the disturbance remaining centered at the chosen origin or aligned with a preferred coordinate axis.

Only after Items 4 and 5 are proved does the DSD construction become a possible route to global regularity rather than a descriptive reformulation.

## 7. First computational program

The first implementation should not attempt a full PDE solver immediately. It should verify the bridge algebra and diagnostics in this order:

1. construct smooth divergence-free central benchmark seeds;
2. verify `x/y/z` rotational equivalence;
3. verify undefined radial readout at the origin versus defined-zero radial readout away from the origin;
4. compute Cartesian and radial/tangential channels on the same fields;
5. compute `T_E`, `T_W`, `T_P`, and axis-resolved terms on shells;
6. demonstrate at least one aggregate collision so the code cannot mistake equal scalar readout for equal state;
7. compute directional entropy for angular partitions;
8. test scaling of the candidate shell combinations under rescaled benchmark fields;
9. only then add time integration and check fixed-time static recovery along the trajectory.

## 8. Status labels for this bridge

- **DSD SOURCE RESULT:** result already belonging to one of the four DSD layers.
- **NAVIER–STOKES IDENTITY/ASSUMPTION:** standard PDE-side input used without reinterpretation.
- **BRIDGE DEFINITION:** application-specific dictionary introduced here.
- **COMPUTATIONAL CHECK:** finite/symbolic verification only.
- **CONJECTURE / TARGET:** unproved candidate needed for progress.
- **FAILED ROUTE:** a bridge shown to be non-injective, non-coercive, incompatible with the PDE, or otherwise unable to support a proof.

This status separation is mandatory for all subsequent DSD-assisted Navier–Stokes work.
