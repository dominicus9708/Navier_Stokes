# Unbounded spherical-view baseline for the Navier–Stokes proof challenge

Date: 2026-08-12

Status: **MODEL / TESTBED + OFFICIAL-DOMAIN ALIGNMENT**.

## 1. Domain

The primary domain is the full unbounded three-dimensional space

\[
\Omega=\mathbb R^3.
\]

The fluid is not regarded as being contained in a pool, cube, tank, rigid sphere, or any other finite vessel.

The origin `O` is only an analysis center. For every radius `r>0`, define the observation sphere

\[
S_r=\{x\in\mathbb R^3:|x|=r\}.
\]

The family `{S_r}_{r>0}` is used to analyze the solution in a celestial-sphere-like way. These spheres are **not physical boundaries**. There is no maximum radius.

Equivalently, the geometry is `R^3` viewed through Cartesian coordinates together with spherical shells centered at the origin.

## 2. Baseline PDE

For `x∈R^3`, `t≥0`,

\[
\partial_t u+(u\cdot\nabla)u
=-\nabla p+\nu\Delta u,
\qquad
\nabla\cdot u=0,
\qquad
\nu>0,
\]

with

\[
f\equiv0.
\]

There is no wall boundary condition. The initial data are taken smooth, divergence-free, and rapidly decaying at spatial infinity.

## 3. Analysis center versus physical center

The origin does not mean that the universe or the fluid has a physical center. It is a coordinate and aggregation reference.

The first benchmark family nevertheless places a smooth localized excitation near the origin so that radial and axis-resolved redistribution can be measured cleanly.

Let `ψ∈C_c^∞(B_ε(0))`. For each Cartesian axis `a∈{x,y,z}`, define

\[
u_0^{(a)}
=
\nabla\times\nabla\times(\psi e_a).
\]

Then

\[
\nabla\cdot u_0^{(a)}=0.
\]

These axis families are only benchmark initial data, not a restriction on the eventual proof class.

## 4. Cartesian and spherical decomposition

Record

\[
u=(u_x,u_y,u_z).
\]

For `r=|x|>0`, define

\[
e_r=\frac{x}{|x|},
\qquad
u_r=u\cdot e_r,
\qquad
u_t=u-u_r e_r.
\]

This allows the same flow to be viewed simultaneously as coordinate-axis motion and as radial/tangential redistribution over spherical shells.

## 5. Incompressibility constraint on radial motion

A smooth nonzero purely radial source flow from the origin is incompatible with incompressibility.

If

\[
u=q(r,t)e_r,
\]

then

\[
\nabla\cdot u
=\frac{1}{r^2}\partial_r(r^2q)=0,
\]

so

\[
r^2q=C(t).
\]

Smoothness at `r=0` forces `C(t)=0`.

Therefore the spherical response is not modeled as creation of fluid at the origin. Local outward and inward sectors may coexist, while the total flux through each observation sphere must cancel.

## 6. Shell diagnostics for arbitrary radius

All shell diagnostics are defined for every finite `r>0`; there is no outer boundary `R`.

### Energy density

\[
E(r,t)
=
\frac{1}{4\pi r^2}
\int_{|x|=r}\frac12|u(x,t)|^2\,dS.
\]

### Enstrophy density

With

\[
\omega=\nabla\times u,
\]

define

\[
W(r,t)
=
\frac{1}{4\pi r^2}
\int_{|x|=r}|\omega(x,t)|^2\,dS.
\]

### Pressure fluctuation

\[
\bar p(r,t)
=
\frac{1}{4\pi r^2}
\int_{|x|=r}p(x,t)\,dS.
\]

Track both `\bar p(r,t)` and angular deviation `p-\bar p`.

### Net radial flux

\[
\Phi(r,t)
=
\int_{|x|=r}u\cdot n\,dS.
\]

For a smooth divergence-free field with no internal source,

\[
\Phi(r,t)=0
\]

for every `r>0`.

### Axis-resolved energy

\[
E_i(r,t)
=
\frac{1}{4\pi r^2}
\int_{|x|=r}\frac12|u_i(x,t)|^2\,dS,
\qquad i\in\{x,y,z\}.
\]

## 7. Meaning of the unbounded spherical view

The phrase “sphere” in this project refers to the **way the unbounded 3D field is sampled and aggregated**, not to the shape of a container.

Conceptually:

\[
\mathbb R^3
=
\bigcup_{r\ge0} S_r
\]

in the radial observational sense, with the origin included separately.

No reflection, wall stress, no-slip condition, or artificial geometric anisotropy is introduced at a finite outer surface.

## 8. Meaning of 'wave'

In the incompressible track, 'wave' means radial/spherical-shell redistribution of velocity, pressure, vorticity, and energy. It is not identified with a finite-speed acoustic wavefront.

A compressible finite-propagation track, if added later, must remain distinct.

## 9. Proof-status discipline

Use the repository labels:

- **THEOREM (external)**
- **DERIVED LEMMA**
- **COMPUTATIONAL CHECK**
- **CONJECTURE / TARGET**
- **MODEL / TESTBED**
- **FAILED ROUTE**

The origin-centered benchmark is a diagnostic family only. Any global regularity claim must eventually cover the full admissible initial-data class on `R^3`, not only centered or axis-aligned seeds.

## 10. Planned progression

1. Verify the smooth divergence-free central seed symbolically and numerically.
2. Verify rotational equivalence of the `x/y/z` benchmark families.
3. Implement shell diagnostics for arbitrary `r>0` with no finite outer wall.
4. Track axis-resolved transport, radial/tangential redistribution, pressure, and vorticity simultaneously.
5. Search for scale-invariant a priori bounds on `R^3` rather than bounds induced by a finite container.
6. Generalize beyond centered benchmark data to the full admissible initial-data class required for a proof.
