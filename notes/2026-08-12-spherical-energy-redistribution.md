# Spherical energy redistribution in the unbounded `R^3` view

Date: 2026-08-12

Status: **DERIVED LOCAL CONSERVATION IDENTITY + EXACT BENCHMARK SPECIALIZATION**.

## 1. Local kinetic-energy identity

For a smooth incompressible Navier–Stokes solution, let

\[
e=\frac12|u|^2.
\]

Using `div u=0` and

\[
u\cdot\Delta u=\Delta e-|\nabla u|^2,
\]

the PDE gives

\[
\boxed{
\partial_t e
+\nabla\cdot\left[(e+p)u-\nu\nabla e\right]
=-\nu|\nabla u|^2.
}
\]

This is the natural dynamic law for the project's celestial-sphere viewpoint. It does not introduce an acoustic wave or a physical boundary.

## 2. Ball/sphere budget

For any analysis center `x_0` and radius `r`, integrate over

\[
B_r(x_0).
\]

Then

\[
\frac{d}{dt}\int_{B_r}e\,dx
+F_{\rm adv}+F_p+F_\nu
=-D_r,
\]

where

\[
F_{\rm adv}
=\int_{S_r}e\,u\cdot n\,dS,
\]

\[
F_p
=\int_{S_r}p\,u\cdot n\,dS,
\]

\[
F_\nu
=-\nu\int_{S_r}\partial_n e\,dS,
\]

and

\[
D_r
=\nu\int_{B_r}|\nabla u|^2dx.
\]

The sign convention is outward flux positive.

This creates four DSD dynamic channels rather than one vague 'wave' quantity:

1. advective transport;
2. pressure transport;
3. viscous transport;
4. internal viscous dissipation.

## 3. Exact centered Gaussian benchmark

For the current `z`-axis Gaussian benchmark,

\[
u_r=4\frac{z}{r}e^{-r^2}.
\]

The energy density is even under `z -> -z`, while `u_r` is odd. Therefore

\[
F_{\rm adv}(r)=0
\]

for every centered sphere.

The pressure source `Q` is even in `z`, hence the unique decaying whole-space pressure is also even. Consequently

\[
F_p(r)=0
\]

by the same parity argument.

The normalized shell mean energy is

\[
T_E(r)
=8e^{-2r^2}
\left(1-\frac43r^2+\frac23r^4\right).
\]

Thus

\[
F_\nu(r)
=-4\pi\nu r^2\frac{dT_E}{dr}
\]

becomes

\[
\boxed{
F_\nu(r)
=\frac{128\pi\nu}{3}
 r^3(2r^4-6r^2+5)e^{-2r^2}.
}
\]

Because

\[
2r^4-6r^2+5
=2\left(r^2-\frac32\right)^2+\frac12>0,
\]

we have

\[
F_\nu(r)>0
\qquad (r>0,\nu>0).
\]

So at the initial benchmark slice, viscosity carries kinetic energy outward across every finite centered observation sphere.

This does **not** mean a finite-speed front exists. Parabolic diffusion has no compact support front in the standard incompressible model.

## 4. Dissipation channel

The shell mean of the velocity-gradient norm is

\[
T_{\nabla u}(r)
=\frac{128}{3}r^2(r^4-4r^2+5)e^{-2r^2}.
\]

Hence

\[
D_r
=4\pi\nu\int_0^r s^2T_{\nabla u}(s)ds.
\]

As `r -> infinity`, the flux vanishes while

\[
\frac{D_\infty}{\nu}
=\frac{35\sqrt2\pi^{3/2}}2,
\]

recovering the whole-space dissipation/enstrophy integral of the benchmark.

## 5. DSD interpretation

### Formation

Each flux mechanism is a distinct channel; zero net advective or pressure flux is a **defined zero**, not absence of that mechanism from the PDE.

### Axis-property layer

The normal `n=e_r` is a local direction in the realized 3D space, not a fourth axis.

### Static Aggregation

At one time slice, retain the signed shell fluxes separately. Do not collapse `F_adv+F_p+F_nu` before checking cancellation.

### Structural Reorganization Dynamics

The time lineage of ball energy is driven by shell flux channels plus internal dissipation. This is the current rigorous meaning of 'spherical redistribution' in the incompressible project.

## 6. Next generalization

The symmetric benchmark hides two channels by parity. For translated/superposed asymmetric data, both

\[
F_{\rm adv}
\]

and

\[
F_p
\]

will generally be nonzero.

The next computational target is therefore an all-center shell-flux audit for the two-seed asymmetric state already used in the pressure and cross-coupling tests.

## Claim boundary

Everything through the benchmark flux formulas above is an exact identity/specialization. No global regularity bound follows from the positivity of the benchmark viscous flux.
