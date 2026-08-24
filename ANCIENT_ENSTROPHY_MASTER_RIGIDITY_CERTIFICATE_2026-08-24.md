# Ancient Enstrophy Master Rigidity Certificate — 2026-08-24

Status: **STAGE-WIDE VORTICITY TIGHTNESS REDUCES THE BOUNDED-ENSTROPHY ANCIENT ENDGAME TO `K_I, R_Z, epsilon_Z` / VELOCITY TAIL DOES NOT ENTER / GLOBAL REGULARITY NOT PROVED.**

This note combines three tail-independent vorticity-only inputs:

1. the universal trace-free stretching coefficient;
2. the positive-middle/Betchov-residual palinstrophy absorption inequality;
3. the optimized Dirichlet frequency floor forced directly by stage-wide vorticity tightness.

The previous version used a separately constructed logarithmic frequency average `c_log`. On the stage-wide vorticity-tight corridor, the Dirichlet floor is stronger and pointwise, so the master certificate can be simplified.

---

## 1. Restricted ancient inputs

On the vorticity-tight ancient branch, first-hitting inheritance gives

\[
\boxed{
M(t):=\|\Omega(t)\|_\infty
\le \frac{K_I}{|t|}
}
\]

and

\[
\boxed{
Z(t):=\|\Omega(t)\|_2^2
\le
Z_+K_I^{1/2}|t|^{-1/2}.
}
\]

Thus the backward decay exponent is

\[
\alpha=\frac12.
\]

The stage-wide tightness hypothesis is

\[
\int_{B_{R_Z}}|\Omega|^2
\ge
(1-\varepsilon_Z)Z.
\]

Since `||Omega||_infinity<=1`,

\[
\boxed{
Z_+
=\frac{4\pi R_Z^3}{3(1-\varepsilon_Z)}.
}
\]

The optimized Dirichlet cutoff calculation gives the dynamically normalized frequency floor

\[
\boxed{
\frac{Q_{dyn}}{Z_{dyn}}
\ge
\lambda_{tight}
:=
\frac{\Lambda_{tight}(\varepsilon_Z)}{R_Z^2},
}
\]

where

\[
\boxed{
\Lambda_{tight}(\varepsilon_Z)
=
\left[
\sqrt\pi(1-\varepsilon_Z)^{1/4}
-
\varepsilon_Z^{1/4}
\right]^4.
}
\]

Returning to physical/ancient variables,

\[
\boxed{
\frac QZ
\ge
\lambda_{tight}M(t).
}
\]

This is pointwise on the stage-wide tight corridor.

---

## 2. Route A: trace-free stretching plus tightness viscosity

The universal trace-free strain eigenvalue estimate gives

\[
\mathcal P\le\frac1{\sqrt3}MZ.
\]

The enstrophy identity then yields

\[
\frac d{dt}\log Z
\le
2\left(
\frac1{\sqrt3}
-
u\lambda_{tight}
\right)M(t).
\]

Define

\[
\boxed{
\Gamma_{TF}^{tight}
:=
2K_I
\left(
\frac1{\sqrt3}
-
u\lambda_{tight}
\right).
}
\]

If the bracket is nonpositive, the nontrivial ancient branch is impossible without any timing comparison.

If the bracket is positive, backward comparison with `Z=O(|t|^-1/2)` gives

\[
\boxed{
\Gamma_{TF}^{tight}<\frac12
\quad\Longrightarrow\quad
Z\equiv0.
}
\]

Equivalently,

\[
\boxed{
2K_I
\left(
\frac1{\sqrt3}
-
u\frac{\Lambda_{tight}(\varepsilon_Z)}{R_Z^2}
\right)_+
<\frac12.
}
\]

This is the first master route.

---

## 3. Timing-independent tight-radius closure

A particularly clean consequence is

\[
\boxed{
\nu\lambda_{tight}
\ge\frac1{\sqrt3}
\quad\Longrightarrow\quad
Z\equiv0.
}
\]

That is,

\[
\boxed{
R_Z^2
\le
\sqrt3\,\nu\Lambda_{tight}(\varepsilon_Z)
\quad\Longrightarrow\quad
\text{tight ancient branch impossible.}
}
\]

For quarter tails,

\[
\varepsilon_Z=\frac14,
\qquad
\Lambda_{tight}(1/4)
\approx0.7885770233.
\]

Thus for viscosity normalized to `nu=1`,

\[
\boxed{
R_Z\lesssim1.16869819
\quad\Longrightarrow\quad
Z\equiv0
}
\]

independently of `K_I`.

---

## 4. Route B: positive-middle coefficient plus global Betchov absorption

The global determinant/Hadamard/Sobolev estimate gives, for every `0<delta<=1`,

\[
\frac d{dt}\log Z
\le
M
+\frac{32}{729\pi^4}
\delta^{-3}\nu^{-3}Z^2
-2(1-\delta)\nu\frac QZ.
\]

Use

\[
M\le K_I|t|^{-1},
\]

\[
Z^2\le Z_+^2K_I|t|^{-1},
\]

and the pointwise tightness frequency floor

\[
Q/Z\ge\lambda_{tight}M.
\]

Then

\[
\boxed{
\Gamma_B^{tight}(\delta)
=
K_I\left[
1
-2(1-\delta)\nu\lambda_{tight}
+
\frac{32}{729\pi^4}
\frac{Z_+^2}{\nu^3\delta^3}
\right].
}
\]

Hence

\[
\boxed{
\inf_{0<\delta\le1}\Gamma_B^{tight}(\delta)
<\frac12
\quad\Longrightarrow\quad
Z\equiv0.
}
\]

The one-dimensional optimizer is determined by

\[
6\left(
\frac{16}{729\pi^4}
\frac{Z_+^2}{\nu^3}
\right)\delta^{-4}
=2\nu\lambda_{tight},
\]

or equivalently

\[
\boxed{
\delta_*
=
\left(
\frac{16Z_+^2}
{243\pi^4\nu^4\lambda_{tight}}
\right)^{1/4},
\qquad
\delta_{opt}=\min\{1,\delta_*\}.
}
\]

Unlike the previous averaged version, `K_I` cancels from the optimizer because both the Type-I and cubic-enstrophy terms carry the same first-hitting factor.

---

## 5. Master certificate

Define

\[
\boxed{
\Gamma_{best}^{tight}
:=
\min\left\{
\Gamma_{TF}^{tight},
\Gamma_B^{tight}(\delta_{opt})
\right\}.
}
\]

Then the stage-wide vorticity-tight ancient branch is impossible whenever

\[
\boxed{
\Gamma_{best}^{tight}<\frac12.
}
\]

The ancient low-frequency velocity tail, remote velocity radius, and spatial Betchov segregation do not enter this certificate.

---

## 6. Eliminate `Z_+` and `lambda_tight`

Both remaining quantities are explicit functions of the tightness geometry:

\[
\boxed{
Z_+
=
\frac{4\pi R_Z^3}{3(1-\varepsilon_Z)},
}
\]

\[
\boxed{
\lambda_{tight}
=
\frac{
[\sqrt\pi(1-\varepsilon_Z)^{1/4}-\varepsilon_Z^{1/4}]^4
}{R_Z^2}.
}
\]

Thus, for fixed viscosity, the complete tight-branch master certificate depends only on

\[
\boxed{
K_I,
\qquad
R_Z,
\qquad
\varepsilon_Z.
}
\]

This is a genuine reduction from the previous independent list `K_I,Z_+,c_log`.

---

## 7. Remaining global issue

The certificate does **not** prove that every singular candidate is vorticity-tight with a universal `R_Z`. The anti-proof audit already identified diffuse/global enstrophy escape as a separate possibility.

Therefore the correct global proof tree is now:

\[
\boxed{
\text{singular candidate}
\Longrightarrow
\text{stage-wide vorticity-tight branch}
\quad\lor\quad
\text{vorticity non-tight/escape branch}.
}
\]

On the tight branch, the endgame is now the scalar inequality above. The non-tight branch must still be routed through the corrected historical/rebuild/remote mechanisms or bypassed by a local compactness argument.

This distinction is important: the new frequency floor makes the tight branch substantially stronger, but it does not justify silently treating global non-tightness as `T`.

---

## 8. Highest-leverage next targets

Inside the tight branch, only two quantitative improvements remain useful:

\[
\boxed{
K_I\downarrow
\qquad\text{or}\qquad
R_Z\downarrow.
}
\]

`epsilon_Z` may also be optimized, but it is already explicit.

Outside the tight branch, the parallel anti-proof task remains to classify vorticity non-tightness without assuming it is turnover.

Status: **STAGE-WIDE VORTICITY TIGHTNESS CONVERTS PALINSTROPHY INTO A POINTWISE DAMPING TERM AT THE SAME SCALE AS VORTEX STRETCHING. FOR FIXED VISCOSITY THE BOUNDED-ENSTROPHY ANCIENT ENDGAME NOW DEPENDS ONLY ON `K_I,R_Z,epsilon_Z`. QUARTER-TAIL TIGHTNESS WITH `R_Z<=1.1687 sqrt(nu)` IS CLOSED INDEPENDENTLY OF STAGE TIMING. GLOBAL REGULARITY REMAINS UNPROVED.**