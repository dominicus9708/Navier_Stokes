# Current status — DSD-assisted Navier–Stokes proof challenge

Date: 2026-08-12

Overall status: **NO GLOBAL REGULARITY PROOF CLAIM**.

The repository currently contains a reproducible bridge from the four DSD layers to the 3D incompressible Navier–Stokes problem on `R^3`, together with exact benchmark identities, deterministic counter-witnesses to several naive shortcuts, and candidate critical/local channels.

## 1. Fixed problem geometry

- Physical/mathematical domain: `R^3`.
- No pool, tank, cube, or finite spherical wall.
- Observation spheres `S_r(x_0)` are sampling/aggregation surfaces only.
- The proof track remains the standard incompressible PDE; no DSD finite-propagation speed is inserted.

## 2. Four DSD layers

1. Formation Axiom System: typed channel existence/applicability and undefined vs defined zero.
2. Axis-property layer: realized spatial rank remains three; local directions and matrix sizes do not create new dimensions.
3. Static Aggregation: retain channel-resolved fixed-time shell/ball descriptors and collision checks.
4. Structural Reorganization Dynamics: retain advection, pressure, viscosity, vorticity stretching, and cross-interaction channels through time.

## 3. Exact benchmark control case

The main analytic benchmark is

\[
\psi=e^{-|x|^2},
\qquad
u_0=\nabla\times\nabla\times(\psi e_z).
\]

It is smooth, rapidly decaying, and divergence free.

Key exact findings include:

- radial direction at the origin is undefined/inapplicable, not zero;
- total shell energy can be isotropic while axis-resolved energy is not;
- shell enstrophy can vanish while velocity energy remains nonzero;
- signed vortex stretching can cancel while positive/negative stretching remain nonzero;
- the centered vorticity direction aligns exactly with the middle strain eigenvector wherever vorticity is nonzero;
- for that benchmark
  \[
  \gamma=\xi^TS\xi=\lambda_2=4ze^{-|x|^2},
  \qquad
  \sigma=|\omega|^2\lambda_2;
  \]
- the vorticity-direction derivative is singular on the axis, but the magnitude-weighted direction-variation channel remains finite/integrable for the benchmark.

## 4. Translation and nonlinear interaction

A translated benchmark recovers its characteristic shell around its translated center, not around a permanently fixed origin. Therefore proof-level local descriptors must be translation complete.

For two divergence-free analytic seeds:

- velocity superposition remains divergence free;
- the quadratic pressure/advection source contains nonzero cross terms;
- vortex stretching also contains nonzero off-diagonal cross terms;
- at the exact point `(1/4,1/2,0)`, the stretching cross term reverses the sign predicted from the two self-stretching terms alone.

Therefore diagonal/self-channel evolution is insufficient.

## 5. Global critical `L^3` route

The critical channel

\[
T_3(t)=\int_{\mathbb R^3}|u|^3dx
\]

satisfies, formally for smooth decaying solutions,

\[
\frac{dT_3}{dt}+3\nu D_3=3\Pi_3.
\]

Advection cancels globally and viscosity is dissipative, but the pressure correlation `Pi_3` remains.

The symmetric single benchmark has `Pi_3=0` exactly by parity. An asymmetric two-seed numerical whole-space pressure audit produces both positive and negative `Pi_3` values, stable across the tested resolutions.

Status:

- endpoint `L^infty_t L^3_x` regularity theorem: **EXTERNAL REGULARITY ANCHOR**;
- obtaining the `L^3` bound from the DSD channels: **OPEN PROOF OBLIGATION**;
- unconditional monotone decay of global `L^3`: **FAILED-ROUTE CANDIDATE**, pending rigorous certification of the numerical pressure counter-witness.

## 6. Local/parabolic route

All-center shell data reconstruct ball data by coarea:

\[
\int_{B_R(x_0)}f\,dx
=\int_0^R\int_{S_r(x_0)}f\,dS\,dr.
\]

This connects the celestial-sphere view to scale-invariant local/parabolic quantities without introducing a container.

Candidate local channels include

\[
C_u(z_0,r)=r^{-2}\int_{Q_r(z_0)}|u|^3,
\]

\[
C_p(z_0,r)=r^{-2}\int_{Q_r(z_0)}|p-\langle p\rangle|^{3/2},
\]

and

\[
E_\nabla(z_0,r)=r^{-1}\int_{Q_r(z_0)}|\nabla u|^2.
\]

The unresolved step is to force a known local regularity gate at every candidate singular point/scale.

## 7. Spherical energy redistribution

For smooth flow,

\[
\partial_t\frac{|u|^2}{2}
+\nabla\cdot\left[\left(\frac{|u|^2}{2}+p\right)u-\nu\nabla\frac{|u|^2}{2}\right]
=-\nu|\nabla u|^2.
\]

This yields distinct sphere/ball channels:

- advective energy flux;
- pressure energy flux;
- viscous energy flux;
- internal viscous dissipation.

For the symmetric benchmark, advective and pressure fluxes cancel by parity and the exact viscous flux is outward across every centered sphere.

For an asymmetric two-seed state, deterministic audits show nonzero signed advective/pressure fluxes; the pressure flux changes sign with radius.

Thus a one-way 'always outward' redistribution assumption is not available in general.

## 8. Strain/eigenvector alignment gate

At `|omega|>0`, let

\[
\gamma=\sum_i\lambda_i a_i,
\qquad
a_i=(\xi\cdot e_i)^2.
\]

The exact upper gate

\[
\gamma_+
\le
\left[\lambda_2+(\lambda_3-\lambda_2)a_3\right]_+
=:U_{\rm align}
\]

follows from `lambda_1 <= lambda_2`.

If `lambda_2<0`, positive stretching requires

\[
a_3>
\frac{-\lambda_2}{\lambda_3-\lambda_2}.
\]

This gives two typed danger mechanisms:

1. positive/noncompressive middle eigenvalue;
2. sufficiently strong alignment with the most extensional eigenvector when the middle eigenvalue is negative.

The scale-local candidate

\[
C_{\rm align}(z_0,r)
=r\int_{Q_r}|\omega|^2U_{\rm align}\,dxdt
\]

is dimensionless, but no a-priori bound is proved.

## 9. Current main proof obligations

1. Control the pressure correlation `Pi_3` without assuming the critical norm bound being sought.
2. Control positive vortex stretching without losing sign/alignment information to aggregation.
3. Extend all-center/cross-interaction estimates from finite benchmark families to arbitrary admissible smooth data.
4. Connect a DSD local critical channel to an established epsilon-regularity gate and prove that the gate activates at every candidate singular point.
5. Obtain a genuine global a-priori estimate.

Until one of these obligations is closed, the project remains a structured proof attempt and reproducibility/audit program, not a solution to the Millennium Prize Problem.

## 10. Reproducibility modules

Current executable modules include:

```text
src/dsd_bridge_baseline.py
src/critical_channel_baseline.py
src/translation_coupling_baseline.py
src/critical_l3_rate_baseline.py
src/coarea_local_bridge.py
src/vorticity_alignment_baseline.py
src/stretching_coupling_baseline.py
src/vorticity_direction_gradient_baseline.py
src/middle_eigenvalue_alignment_baseline.py
src/strain_alignment_gate_baseline.py
src/spherical_energy_budget.py
src/asymmetric_spherical_budget.py
```

`PROOF_MAP.md` is the claim/status authority. `REPRODUCIBILITY.md` is the execution/interpretation authority.
