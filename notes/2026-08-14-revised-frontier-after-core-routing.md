# Revised frontier after quadratic-core routing

Date: 2026-08-14

Status: **GLOBAL REGULARITY NOT PROVED / MAJOR LOCAL ESCAPE CHANNELS REMOVED OR TYPED**.

This checkpoint collects the deductions obtained after the nonlinear-creation frontier was localized to one parabolic block.

## 1. Surviving amplitude/scale variables

A surviving bounded-affine intermediate residual branch still has

\[
m=W^{-1/3}\Lambda,
\qquad
\Lambda\to\infty,
\qquad
m\to0,
\]

with vorticity share

\[
\Theta=\frac{V_\omega}{B}.
\]

The natural survival parameter is

\[
\boxed{
H=\Lambda\Theta^{5/6}\to\infty.
}
\]

The source-optimal and finite-energy Hermite radii are

\[
R_S\asymp
W^{1/6}\Lambda^{-1/2}\Theta^{-1/4},
\]

\[
R_H\asymp
W^{1/6}\Lambda^{-1/5},
\]

with

\[
\boxed{
R_H/R_S\asymp H^{3/10}.
}
\]

The physical dissipation lower bound is

\[
D_{\rm phys}\gtrsim H^{-3/2}.
\]

## 2. Source-efficiency refinement

For source efficiency

\[
\mathcal E
=\frac{|J|}{B\sqrt\Theta},
\]

the refined dissipation ledger is

\[
\boxed{
D_{\rm phys}
\gtrsim
H^{-3/2}\mathcal E^{-5/2}.
}
\]

Therefore a surviving disjoint cascade must satisfy

\[
\boxed{
\mathcal E H^{3/5}\to\infty.
}
\]

So inefficient mean-source conversion is no longer free.

## 3. Multiscale dilution removed

Matched heat contraction gives

\[
A_{j+1}\le\rho A_j+q_j,
\qquad
\rho<1.
\]

If previous-checkpoint inheritance is negligible and the final residual pulse has height `m`, then at least one matched block satisfies

\[
\boxed{
B_{Q_j}\gtrsim m.
}
\]

Thus an order-`m` current-step contribution cannot be hidden as infinitely many vanishing commutators.

## 4. Pure affine inheritance separated

In Cauchy coordinates

\[
x=a+Fz,
\qquad
F'=LF,
\qquad
\widetilde\Omega=F^{-1}\Omega,
\]

pure affine transport/stretch becomes anisotropic heat

\[
\partial_t\widetilde\Omega
=
\nu\nabla_z\cdot(G\nabla_z\widetilde\Omega).
\]

Therefore pure affine inheritance belongs to the Gaussian heat-contraction branch.

The distinct mean-vorticity linear coupling is Fourier-skew at frozen coefficients and should be treated as bounded-action redistribution, not global `L2` creation.

## 5. Hermite saturation obstruction

Let

\[
\delta=\frac{K-B}{B}
\]

be the Hermite curvature surplus.

The genuine residual-residual first-chaos vorticity source obeys

\[
\boxed{
\|\Pi_1N_\omega\|_2
\lesssim
B\sqrt\delta.
}
\]

Therefore exact Poincare saturation `delta=0` cannot nonlinearly regenerate a first-chaos residual-vorticity pulse.

Near saturation, one-block first-chaos regeneration requires

\[
\boxed{
mR^4\gtrsim\Theta/\delta.}
\]

At the Hermite radius ceiling this gives the explicit tail floor

\[
\boxed{
\delta
\gtrsim
\Theta W^{-1/3}\Lambda^{-1/5}.
}
\]

## 6. Exact quadratic-core zero-set obstruction

For the quadratic velocity / first-chaos vorticity core,

\[
N_\omega=J+N_{\omega,2}.
\]

Exact computer algebra over the reals gives

\[
\boxed{
N_{\omega,2}=0
\Longrightarrow
J=0.
}
\]

Thus a quadratic core cannot generate Gaussian mean vorticity while producing no second Hermite chaos.

## 7. Explicit mean-source routing

The exact finite-dimensional identity is

\[
J=E_\gamma P+Ab.
\]

The trace piece satisfies

\[
|E_\gamma P|
\le
\sqrt{3/2}\|N_{\omega,2}\|_2.
\]

For any fixed axis `e`, the constant-shift piece satisfies

\[
\boxed{
|Ab|
\lesssim
\sqrt{V_\omega V_\perp}.
}
\]

Therefore

\[
\boxed{
|J|
\lesssim
\|N_{\omega,2}\|_2
+
\sqrt{V_\omega V_\perp}.
}
\]

So the quadratic-core mean source is fully routed to

- second Hermite chaos;
- projective/transverse vorticity defect.

There is no independent `Ab` escape.

## 8. Temporal cancellation removed as an independent channel

Inside an isotropic matched heat block, let `rho2(s)` be the degree-two attenuation factor.

Then

\[
\int L_2N_2
=
L_2\int\rho_2N_2
+
\int(1-\rho_2)L_2N_2.
\]

Hence the trace-generated mean contribution is exactly the sum of

1. the degree-two output surviving to the child;
2. the degree-two output erased by heat.

Adding the projective `Ab` term gives

\[
\boxed{
\text{core mean source}
\Rightarrow
\text{surviving second chaos}
\ \lor\
\text{viscous conversion}
\ \lor\
\text{projective defect}.
}
\]

Temporal sign cancellation merely redistributes mass between the first two terms and is not a fourth mechanism.

## 9. Remaining genuine escape families

After the above reductions, a surviving singular cascade must repeatedly use at least one of the following.

### A. Projective / axis-defect packing

A quantitatively significant transverse vorticity component must recur across scale-time blocks.

Fixed-time low-curvature Carleson packing is already available, but a scale-time conversion to a non-summable physical budget is not yet complete.

### B. Hermite curvature / second-chaos / viscous conversion

Either `delta` is quantitatively non-negligible, or a second-chaos source is created and then removed through the viscous lane.

The current problem is to price repeated creation-and-erasure in a scale-invariant physical budget.

### C. Bounded-affine localization commutator

Pure affine heat inheritance is controlled, but the time-dependent skew redistribution and anisotropic Gaussian localization still require a clean commutator estimate.

### D. Affine / harmonic-pressure degeneration

If the bounded-affine or controlled-tail assumptions fail, the branch exits into the already separated degeneration / far-pressure family.

## 10. Most precise next theorem target

The next closure should no longer be phrased as a generic estimate on `B_Q`.

The sharper target is a scale-time packing theorem for the typed outputs

\[
\boxed{
\mathfrak C
:=
V_\perp
+
\text{Hermite curvature surplus}
+
\text{viscously erased second-chaos action}.
}
\]

One needs a bound strong enough that infinitely many disjoint first-hitting steps carrying the required order-one mean/source action cannot have finite total physical kinetic-energy dissipation.

Equivalently, a successful theorem must supply the positive scale gain still missing between

\[
BR^5\lesssim W^{1/2}
\]

and the critical velocity condition

\[
BR^4\lesssim C,
\]

or reach a different rigidity criterion without passing through global `L3`.

Status: **FRONTIER REDUCED TO PROJECTIVE PACKING, HERMITE/VISCOUS PACKING, LOCAL SKEW COMMUTATOR, OR EXPLICIT DEGENERATION / GLOBAL REGULARITY STILL OPEN.**
