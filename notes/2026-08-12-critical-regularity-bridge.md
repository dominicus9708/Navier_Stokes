# Critical regularity bridge for the DSD-assisted Navier–Stokes project

Date: 2026-08-12

Status: **BRIDGE DESIGN + DERIVED IDENTITIES + OPEN PROOF OBLIGATIONS**.

## 1. Why the first shell descriptor is not enough

The centered shell descriptor from the first-pass note is useful for discovering directional and scale structure, but global regularity should be tied to a standard critical control quantity rather than to an arbitrary new scalar.

A particularly strong external anchor is the classical endpoint result of Escauriaza, Seregin, and Šverák: three-dimensional Navier–Stokes solutions in the critical `L^∞_t L^3_x` class are smooth.

Accordingly the first DSD critical channel is

\[
T_3(t)=\int_{\mathbb R^3}|u(x,t)|^3\,dx.
\]

Under the Navier–Stokes scaling

\[
u_\lambda(x,t)=\lambda u(\lambda x,\lambda^2t),
\]

`T_3` is invariant.

Therefore a genuinely useful DSD route may aim to prove

\[
\sup_{0\le t<T}T_3(t)<\infty
\]

for every finite `T` and every admissible smooth initial datum. If established with the hypotheses needed by the external regularity theorem, this would supply a known regularity bridge instead of requiring a new coercivity theorem from scratch.

This bound is **not currently proved**.

## 2. Formal `L^3` balance for smooth decaying solutions

For a smooth solution with sufficient decay,

\[
\frac{d}{dt}\int |u|^3dx
=3\int |u|u\cdot\partial_tu\,dx.
\]

Substituting Navier–Stokes gives three DSD dynamic contributions.

### Advection channel

\[
-3\int |u|u\cdot(u\cdot\nabla)u\,dx
=-\int u\cdot\nabla |u|^3dx
=0.
\]

Thus global advection does not directly change the `L^3` aggregate.

### Viscous channel

Formally,

\[
3\nu\int |u|u\cdot\Delta u\,dx
=
-3\nu\int
\left(
|u||\nabla u|^2
+\frac{1}{|u|}\sum_k(u\cdot\partial_ku)^2
\right)dx,
\]

with the zero set understood by a standard smooth regularization/limiting argument.

This contribution is dissipative.

### Pressure channel

\[
-3\int |u|u\cdot\nabla p\,dx
=
3\int p\,u\cdot\nabla|u|\,dx.
\]

Therefore the endpoint balance takes the schematic form

\[
\frac{d}{dt}T_3(t)
+3\nu D_3(t)
=3\Pi_3(t),
\]

where

\[
D_3(t)=
\int
\left(
|u||\nabla u|^2
+\frac{1}{|u|}\sum_k(u\cdot\partial_ku)^2
\right)dx
\]

and

\[
\Pi_3(t)=\int p\,u\cdot\nabla|u|\,dx.
\]

For this route, **pressure control is the unresolved endpoint obstruction**. DSD does not remove it by relabeling the terms.

## 3. Axis-property bridge: the velocity-gradient block

Define

\[
G=\nabla u,
\qquad
G_{ij}=\partial_j u_i.
\]

This is a `3 x 3` property/coupling block attached to the three realized spatial axes; its matrix size is not interpreted as a new spatial dimension.

Split

\[
S=\frac12(G+G^T),
\qquad
A=\frac12(G-G^T).
\]

Incompressibility gives

\[
\operatorname{tr}G
=\operatorname{tr}S
=0.
\]

The antisymmetric part carries local rotational information, while the symmetric strain block is the part that changes vorticity magnitude.

## 4. Vorticity channel and the 3D obstruction

With

\[
\omega=\nabla\times u,
\]

the smooth vorticity equation is

\[
\partial_t\omega+(u\cdot\nabla)\omega
=(\omega\cdot\nabla)u+\nu\Delta\omega.
\]

The global enstrophy balance is

\[
\frac12\frac{d}{dt}\int|\omega|^2dx
+\nu\int|\nabla\omega|^2dx
=
\int\omega^TS\omega\,dx.
\]

Thus define the stretching channel

\[
\sigma(x,t)=\omega^TS\omega.
\]

Formation/static aggregation must preserve at least the sign split

\[
\sigma_+=\max(\sigma,0),
\qquad
\sigma_-\max(-\sigma,0),
\]

rather than keeping only the signed sum.

## 5. Exact cancellation witness from the Gaussian benchmark

For the analytic `z`-axis Gaussian double-curl seed used by the baseline code,

\[
\sigma
=64z(x^2+y^2)(2|x|^2-5)^2e^{-3|x|^2}.
\]

Hence the signed stretching is odd in `z`.

For every centered sphere,

\[
\int_{S_r}\sigma\,d\mu_r=0,
\]

while the normalized positive part is

\[
\int_{S_r}\sigma_+\,d\mu_r
=8r^3(2r^2-5)^2e^{-3r^2}.
\]

Across all space the exact benchmark values are

\[
\int_{\mathbb R^3}\sigma\,dx=0,
\]

\[
\int_{\mathbb R^3}\sigma_+\,dx
=\frac{992\pi}{81},
\qquad
\int_{\mathbb R^3}\sigma_-\,dx
=\frac{992\pi}{81}.
\]

Therefore a zero signed aggregate can conceal substantial simultaneous positive and negative vortex stretching.

This is an explicit DSD-style aggregate-cancellation witness. It is **not** a global regularity estimate.

## 6. Pressure closure as a channel-cancellation identity

For a smooth divergence-free velocity field, define

\[
Q=\sum_{i,j}\partial_i u_j\,\partial_j u_i.
\]

Then

\[
\nabla\cdot R_{\rm adv}=-Q,
\]

while incompressible pressure satisfies

\[
-\Delta p=Q
\]

so

\[
\nabla\cdot R_{\rm pres}=+Q.
\]

The viscous channel obeys

\[
\nabla\cdot R_{\rm visc}
=\nu\Delta(\nabla\cdot u)=0.
\]

Therefore

\[
\nabla\cdot
(R_{\rm adv}+R_{\rm pres}+R_{\rm visc})=0.
\]

This is the first exact dynamic closure identity to be retained in the DSD channel representation.

## 7. Scale-critical DSD channel vector

The next working object should retain both fixed-time critical quantities and rate/cumulative channels:

\[
\mathfrak C(t)
=
\left(
\int|u|^3dx,
\int|\omega|^{3/2}dx,
\Pi_3(t),
\Sigma_+(t),
\Sigma_-(t)
\right),
\]

where

\[
\Sigma_\pm(t)=\int\sigma_\pm(x,t)dx.
\]

The first two integrals are invariant under Navier–Stokes scaling.

`Pi_3` and `Sigma_±` scale as rates; their time integrals are scale-invariant:

\[
\int_0^T|\Pi_3(t)|dt,
\qquad
\int_0^T\Sigma_\pm(t)dt.
\]

This makes them natural Structural-Reorganization-Dynamics channels.

## 8. Immediate proof targets

### Target A — critical velocity channel

Establish an a-priori bound for

\[
\sup_{0\le t<T}\|u(t)\|_{L^3}.
\]

The endpoint regularity theorem would then provide an external bridge to smoothness.

### Target B — pressure correlation

Find a non-circular estimate for

\[
\int_0^T\Pi_3(t)dt
\]

that can be absorbed by the viscous term or controlled by already-bounded critical channels.

### Target C — positive stretching

Do not use only

\[
\int\sigma dx,
\]

because cancellation can make it artificially small. Seek control of

\[
\int_0^T\Sigma_+(t)dt
\]

relative to dissipation or a critical norm.

### Target D — translation completeness

All local shell/sector diagnostics must ultimately be evaluated for arbitrary centers `x_0`, not only the benchmark origin.

## 9. External mathematical anchors

- L. Escauriaza, G. A. Seregin, V. Šverák, *L_{3,∞}-solutions of the Navier–Stokes equations and backward uniqueness*, Russian Mathematical Surveys 58(2), 211–250 (2003), DOI `10.1070/RM2003v058n02ABEH000609`.
- L. Caffarelli, R. Kohn, L. Nirenberg, *Partial regularity of suitable weak solutions of the Navier-Stokes equations*, Communications on Pure and Applied Mathematics 35, 771–831 (1982), DOI `10.1002/cpa.3160350604`.

The first is the main critical-norm target for the present bridge; the second is retained as the local/scale-aware regularity reference point.
