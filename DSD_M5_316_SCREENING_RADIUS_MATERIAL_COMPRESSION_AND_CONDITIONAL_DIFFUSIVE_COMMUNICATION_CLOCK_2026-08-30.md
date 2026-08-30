# DSD M5-316 — Screening Radius, Material Compression, and Conditional Diffusive Communication Clock

Date: 2026-08-30

Parent: `DSD_M5_315_STATIC_VELOCITY_SILENCE_VS_DYNAMIC_PRESSURE_HESSIAN_SCREENING_GATE_2026-08-30.md`

Status: **FORMATION/AXIAL PARALLEL ANALYSIS / MATERIAL TRANSPORT FROM A SCREENING SHELL AT RADIUS R TO AN ORDER-ONE CORE REQUIRES LOGARITHMIC INTEGRATED LIPSCHITZ/STRAIN ACTION / IF PRESSURE-HESSIAN ACTION IS QUIET AND THIS TRANSPORT ACTION IS SUBLOGARITHMIC, THE TRANSITION SHELL REMAINS AT DISTANCE AT LEAST R EXP(-A_S) / THE RESIDUAL COMMUNICATION CLOCK IS DIFFUSIVE AT SCALE R^2 EXP(-2 A_S)/nu UP TO THE STANDARD DRIFT/STRETCHING COEFFICIENTS / EARLIER CORE RESPONSE ROUTES TO PRESSURE, TRANSPORT, OR DERIVATIVE ACTION / GLOBAL REGULARITY UNPROVED.**

---

## 1. Setup

Work in a satellite-normalized dynamically screened corridor from M5-315.

Let the active interior core have radius `O(1)` and let the transition/source shell initially lie at radius

\[
R_{scr}\gg1.
\]

Assume the far pressure-Hessian channel has already been placed in the quiet branch, so that nonlocal pressure does not instantly destroy the screening.

The remaining ways for transition information to reach the core are

1. material/advection transport;
2. diffusion;
3. local stretching/nonlinear amplification of an already tiny transmitted signal.

---

## 2. Exact material-distance inequality

Let `X(t)` and `Y(t)` be two trajectories of the velocity field. Then

\[
\frac{d}{dt}|X-Y|
=\frac{X-Y}{|X-Y|}\cdot\bigl(u(X)-u(Y)\bigr).
\]

By the mean-value theorem,

\[
\boxed{
\frac{d}{dt}|X-Y|
\ge
-\|\nabla u(t)\|_{L^\infty(\Gamma_{XY})}|X-Y|,
}
\]

where `Gamma_XY` is any region containing the segment/trajectory corridor between the points.

Thus

\[
\boxed{
|X(t)-Y(t)|
\ge
|X(t_0)-Y(t_0)|
\exp\left(
-\int_{t_0}^t\|\nabla u(s)\|_\infty ds
\right).
}
\]

Define the integrated Lipschitz action

\[
\boxed{
A_S(I):=
\int_I\|\nabla u(s)\|_\infty ds.
}
\]

---

## 3. Logarithmic action needed to collapse a large screening radius

If a material feature begins at distance `R_scr` and reaches an order-one core, then necessarily

\[
R_{scr}e^{-A_S}\lesssim1.
\]

Therefore

\[
\boxed{
A_S\gtrsim\log R_{scr}.
}
\]

Hence a large screened region cannot be erased by material transport with only `O(1)` accumulated Lipschitz action.

This gives the typed alternative

\[
\boxed{
\text{fast material communication}
\Longrightarrow
H_{Lip/log}
\lor
T_{transport}.
}
\]

The first label records a logarithmically growing derivative action; the second records loss of the assumed coherent material corridor.

---

## 4. Residual distance on the quiet transport branch

If

\[
A_S(I)\le A_*
\]

then the transition shell remains at distance at least

\[
\boxed{
D_*(I)
\gtrsim
R_{scr}e^{-A_*}
}

from the tracked core, modulo the already typed center/boundary turnover events.

Thus on the no-pressure/no-transport-H corridor the core is protected by a genuine geometric gap.

---

## 5. Diffusive communication scale

For the heat equation, a source initially at distance `D` influences the center over a time `Theta` through a Gaussian factor of the form

\[
\exp\left(-c\frac{D^2}{\nu\Theta}\right).
\]

For a linear parabolic equation with controlled drift and zero-order coefficients, the same scale survives up to constants/weight factors determined by those coefficient bounds.

Therefore on the retained corridor where drift/strain coefficients are bounded by the no-H assumptions, the natural diffusive communication time associated with the residual distance `D_*` is

\[
\boxed{
\Theta_{diff}
\asymp
\frac{D_*^2}{\nu}
\gtrsim
\frac{R_{scr}^2}{\nu}e^{-2A_*}.
}
\]

This is a **conditional scale statement**, not a claim of finite propagation for Navier--Stokes.

---

## 6. Communication dichotomy

Suppose the screened core changes by an order-one amount on a time interval `Theta` much shorter than

\[
\nu^{-1}R_{scr}^2e^{-2A_*}.
\]

Then the change cannot be attributed to quiet diffusion from the transition shell.

At least one excluded quiet hypothesis must fail:

\[
\boxed{
\text{early screened-core response}
\Longrightarrow
H_{p}
\lor
H_{Lip/log}
\lor
T_{transport}
\lor
H_{local/stretch}.
}
\]

The last term allows local nonlinear amplification of an already transmitted perturbation and must be charged in the standard vorticity/strain ledger.

---

## 7. Pure rotation benchmark

For exact solid rotation,

\[
\operatorname{sym}\nabla u=0,
\]

and material radii are preserved.

Hence

\[
A_S=0
\]

for the deforming part and the transition shell is not advected inward.

The natural communication clock is then genuinely diffusive:

\[
\boxed{
\Theta_{scr}\sim R_{scr}^2/\nu.
}
\]

This explains why the solid-rotation anti-model from M5-282/285 is consistent with a long screened lifetime.

---

## 8. Affine strain benchmark

If an affine strain has an inward eigenvalue of order one, trajectories along that stable direction contract exponentially.

A shell at radius `R` can then approach the core in time

\[
\Theta\sim\log R.
\]

But exactly this behavior accumulates

\[
A_S\sim\log R,
\]

so it belongs to the logarithmic derivative-action branch rather than the quiet screened corridor.

Thus the transport/diffusion split correctly distinguishes the affine-strain and solid-rotation benchmarks.

---

## 9. Relation to the M5-309 affine-break radius

M5-309 gives a first affine transition radius

\[
R_{br}=O(L^{1/5}).
\]

If this transition shell is dynamically screened and no logarithmic transport action occurs, its quiet diffusive communication time is at most/order

\[
\boxed{
\Theta_{br}
\sim
R_{br}^2
=O(L^{2/5})
}
\]

when `nu` is normalized to one and `A_S=O(1)`.

This reproduces the same `2/5` persistence exponent that appeared independently in the parent-Morrey energy-capacity calculation.

The agreement is structural but not yet a contradiction.

---

## 10. What is proved and what remains conditional

### Proved

- exact material distance lower bound under integrated Lipschitz action;
- logarithmic action requirement to advect a radius-`R` shell into an order-one core;
- benchmark consistency for rotation and affine compression.

### Conditional / standard-parabolic bridge

- quantitative Gaussian suppression of transition-shell influence for the full localized Oseen/vorticity system under the retained coefficient bounds;
- conversion of an early core response into one of the typed H/T exits with explicit constants.

### Open

- closure of the long-lived `Theta~R^2` screened branch;
- whether repeated screened episodes produce a nonsummable invariant action;
- the critical detached endpoint after all finite-growth screening has been exhausted.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
