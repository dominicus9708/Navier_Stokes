# Critical Riccati saturation skeleton

Date: 2026-08-13

Status: STRESS TEST / NOT A NAVIER-STOKES SOLUTION.

Use the scalar envelope

\[
M'=M^2,\qquad M(0)=q^{-1}.
\]

The first time at which `M=1` is

\[
\boxed{\sigma=q-1}.
\]

The two key actions are exactly

\[
\boxed{\int_0^\sigma M(s)\,ds=\log q}
\]

and

\[
\boxed{\int_0^\sigma M(s)^2\,ds=1-q^{-1}}.
\]

Thus a single critical model simultaneously saturates the current three ledger scales:

1. normalized first-hitting duration of order `q`;
2. BKM / strain-axis action of order `log q`;
3. quadratic residual-Duhamel action of order one.

If the natural spatial radius is represented by

\[
R(s)=M(s)^{-1/2},
\]

then a natural-core enstrophy scale is `M^(1/2)` and

\[
\int_0^\sigma M(s)^{1/2}ds
=2(\sqrt q-1).
\]

After converting from a terminal normalization `W=q W_-`, the factor `W^{-1/2}` turns this into an order `W_-^{-1/2}` physical dissipation scale, independent of the target ratio `q`.

Therefore none of the following, by itself, can close the proof:

- `sigma >= c q`;
- `int ||omega||_infinity dt >= c log q`;
- an order-one residual action per adaptive step;
- scale-critical natural-core dissipation.

A successful closure must prove that actual 3D incompressible geometry cannot realize this simultaneous critical saturation.  Candidate mechanisms retained in the repository are

- middle-eigenvalue / pure-shear compatibility;
- extensional-axis versus off-axis vorticity compatibility;
- material-flux turnover;
- pressure/eigenframe maintenance;
- a genuinely supercritical or logarithmically improved scale-time packing estimate.

This skeleton is henceforth an adversarial audit case: any claimed final inequality should be tested against it before being promoted to a proof route.
