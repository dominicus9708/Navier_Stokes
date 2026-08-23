# Remote Strain Morrey Finite-Radius Closure — 2026-08-23

Status: **S-LEVEL CONDITIONAL-ON-MORREY REMOTE-H CLOSURE / GLOBAL REGULARITY NOT PROVED.**

This note gives the strongest current pruning of dynamically active `H_remote`. The same scale-invariant local kinetic-energy Morrey corridor already used in the parent-pressure gate implies direct `R^-2` decay of remote normalized strain.

Therefore, while the Morrey corridor holds, an order-one dynamically active strain source cannot live at normalized radius `R->infinity`. Failure of that Morrey corridor is already an explicit local-energy/turnover exit in the existing proof tree.

This removes the need to pass through vorticity tightness or the weaker `R^3` global time-packing estimate for this particular active-H question.

## 1. Smooth remote strain as a velocity functional

Let

\[
\mathcal S_R
=\int K(y)\psi_R(y)\Omega(y)dy
\]

be the smooth remote strain functional around the fixed no-turnover center `X_*`, where

- `K` is the degree `-3` strain-from-vorticity kernel;
- `psi_R=0` for `|y|<=R`;
- `psi_R=1` for `|y|>=2R`;
- `Omega=curl U`.

Integrating the curl by parts gives

\[
\boxed{
\mathcal S_R
=\int L_R(y)U(y)dy,
}
\]

where, componentwise,

\[
L_R=\operatorname{curl}^*(K\psi_R).
\]

The kernel `L_R` is divergence free in the velocity index and obeys

\[
\boxed{
|L_R(y)|
\lesssim
|y|^{-4}
}
\]

outside the transition annulus, with the same `O(R^-4)` scale on `R<|y|<2R`.

## 2. Scale-invariant local kinetic-energy Morrey corridor

Assume the existing parent/local-energy corridor

\[
\boxed{
\mathcal M_\rho
:=
\rho^{-1}\int_{B_\rho(X_*)}|U(y)|^2dy
\le M_*
}
\]

for all parent radii under consideration.

This is exactly the hypothesis already used in `PARENT_PRESSURE_ESCALATION_FINITE_GATE_2026-08-21.md`. In that note, failure of the Morrey bound is an explicit local-energy/turnover exit rather than part of the pure projective corridor.

## 3. Dyadic remote-strain estimate

Split the exterior into dyadic annuli

\[
A_k
=\{2^kR<|y|<2^{k+1}R\},
\qquad
\rho_k=2^kR.
\]

On `A_k`,

\[
\|L_R\|_{L^2(A_k)}
\lesssim
\rho_k^{-4}|A_k|^{1/2}
\lesssim
\rho_k^{-5/2}.
\]

The Morrey bound gives

\[
\|U\|_{L^2(A_k)}
\le
\|U\|_{L^2(B_{2\rho_k})}
\lesssim
M_*^{1/2}\rho_k^{1/2}.
\]

Therefore

\[
\left|
\int_{A_k}L_RU
\right|
\lesssim
M_*^{1/2}\rho_k^{-2}.
\]

Summing geometrically,

\[
\sum_{k\ge0}\rho_k^{-2}
=R^{-2}\sum_{k\ge0}2^{-2k}
\lesssim R^{-2}.
\]

Hence

\[
\boxed{
|\mathcal S_R|
\le
C_M M_*^{1/2}R^{-2}.
}
\]

The cutoff transition annulus obeys the same scaling and is absorbed into `C_M`.

## 4. Pointwise active-radius ceiling

If the remote source is dynamically active in the pointwise sense

\[
|\mathcal S_R|\ge s_0>0,
\]

then

\[
s_0
\le
C_MM_*^{1/2}R^{-2},
\]

so

\[
\boxed{
R
\le
R_{M,\max}^{pt}
:=
\left(
\frac{C_MM_*^{1/2}}{s_0}
\right)^{1/2}.
}
\]

This bound is independent of the first-hitting amplitude `W`.

Thus no order-one active remote strain can move to normalized infinity while the Morrey corridor remains valid.

## 5. Finite-stage action ceiling

On a normalized stage `I_j` with

\[
L_j\le L_+,
\]

define

\[
\mathcal A_{R,j}
:=\int_{I_j}|\mathcal S_R(s)|ds.
\]

If the Morrey bound holds uniformly through the stage,

\[
\mathcal A_{R,j}
\le
C_MM_*^{1/2}L_+R^{-2}.
\]

Therefore a fixed positive action threshold

\[
\mathcal A_{R,j}\ge a_0>0
\]

forces

\[
\boxed{
R
\le
R_{M,\max}^{act}
:=
\left(
\frac{C_MM_*^{1/2}L_+}{a_0}
\right)^{1/2}.
}
\]

Again this is a uniform finite normalized radius.

## 6. Comparison with previous remote-H bounds

The repository now has three nested active-remote estimates:

### Direct vorticity L2

\[
|\mathcal S_R|
\lesssim
R^{-3/2}Z^{1/2}.
\]

Useful for the `R^3` enstrophy tax and vorticity-tight closure.

### Global physical kinetic energy

\[
|\mathcal S_R|
\lesssim
W^{1/4}\|u_0\|_2R^{-5/2},
\]

which yields

\[
R=O(W^{1/10}),
\qquad
\ell=O(W^{-2/5}).
\]

### Morrey local kinetic energy

\[
\boxed{
|\mathcal S_R|
\lesssim
M_*^{1/2}R^{-2}.
}
\]

This yields a **uniform finite normalized active radius**, which is the strongest estimate whenever the Morrey corridor is available.

## 7. Consequence for H_remote

`H_remote` means derivative mass may escape to normalized radii tending to infinity after first-hitting analyticity has removed local derivative-amplitude blow-up.

The present estimate shows:

- if remote derivative mass at `R->infinity` is dynamically passive, it is removed as a naked obstruction by the localized tightrope ledger;
- if it supplies fixed positive core strain action, then the Morrey bound must fail before `R` can tend to infinity.

Therefore

\[
\boxed{
H_{remote}^{active}
\Longrightarrow
\text{Morrey/local-energy failure}
}
\]

for genuinely remote normalized radii.

The parent-pressure gate already classifies Morrey failure as an existing local-energy/turnover branch.

Thus, **conditional on accepting the same uniform Morrey corridor already required elsewhere in the pure first-hitting route**, active `H_remote` is not an independent terminal branch.

## 8. Velocity-form source evolution strengthens the interpretation

Because `L_R` is divergence free, pairing the normalized velocity equation with `L_R` removes pressure exactly. For a cutoff at fixed physical radius, the scaling derivative cancels the artificial cutoff sweep and one obtains schematically

\[
\boxed{
(\partial_s+b)\mathcal S_\ell
=\mathcal N_\ell+\mathcal V_\ell,
}
\]

where

\[
\mathcal N_\ell
=\int \nabla L_R:(U\otimes U),
\]

and viscosity is supported only in the cutoff annulus because the exterior kernel is harmonic.

The same Morrey estimate gives

\[
\boxed{
|\mathcal N_\ell|
\lesssim M_*R^{-4},
}
\]

and

\[
\boxed{
|\mathcal V_\ell|
\lesssim \nu M_*^{1/2}R^{-4}.
}
\]

Thus at large normalized radius a fixed physical remote source is not only small; its nonlinear/viscous ability to regenerate normalized strain is even smaller (`R^-4`).

A separate note should record the full exact velocity-form identity and stage recurrence, since it gives a clean route from remote source persistence to inward source-radius turnover without the intermediate vorticity-stretching decomposition.

## 9. Updated System-I status

The branch map is now

\[
\boxed{
H_{remote}
\Longrightarrow
\begin{cases}
\text{passive: absent from localized core ledger},\\
\text{active + Morrey bound: impossible at }R\to\infty,\\
\text{active + Morrey failure: local-energy/turnover exit}.
\end{cases}
}
\]

The remaining technical issue is no longer a free remote derivative halo. It is the **uniform Morrey/local-energy control and the turnover branch activated when that control fails**.

Status: **UNDER THE SAME SCALE-INVARIANT LOCAL KINETIC-ENERGY MORREY CORRIDOR ALREADY USED BY THE PARENT-PRESSURE ROUTE, DYNAMICALLY ACTIVE `H_remote` HAS A UNIFORM FINITE NORMALIZED RADIUS. PASSIVE `H_remote` IS REMOVED BY LOCALIZATION. SYSTEM I THEREFORE REDUCES TO MORREY/LOCAL-ENERGY TURNOVER RATHER THAN AN INDEPENDENT REMOTE-H TERMINAL BRANCH. GLOBAL REGULARITY IS NOT PROVED.**
