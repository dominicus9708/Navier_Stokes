# Frontier: stochastic ancestry endgame

Date: 2026-08-16

Overall status: **THE DETERMINISTIC PRECOMPRESSION--LATE-INJECTION ESCAPE HAS BEEN REMOVED AS AN INDEPENDENT BRANCH BY THE STOCHASTIC KELVIN THEOREM. THE ENDGAME IS NOW STOCHASTIC-ANCESTOR SPATIAL ESCAPE VERSUS STRAIN/HIGHER-DERIVATIVE GEOMETRIC DEGENERATION. GLOBAL REGULARITY IS NOT PROVED.**

---

## 1. Previous frontier

The previous endgame allowed the hypothetical strategy

\[
\text{almost flux-free material precompression}
\to
\text{late viscous flux injection}
\to
\text{new coherent crossing},
\]

repeated in a parabolic Zeno cascade.

That strategy was sharp for the deterministic material-flux observable because viscosity changes deterministic material vorticity flux.

The present continuation replaces deterministic material ancestry by the exact stochastic Lagrangian ancestry of smooth Navier--Stokes circulation.

---

## 2. External exact input: stochastic Kelvin

For smooth Navier--Stokes velocity `U`, Constantin--Iyer / Eyink give, for every final loop `C_c` and earlier time `t_-`,

\[
\boxed{
\oint_{C_c}U(t_c)\cdot d\ell
=
\mathbb E
\left[
\oint_{X_{t_c,t_-}^{\varpi}(C_c)}
U(t_-)\cdot d\ell
\right].
}
\]

Thus present circulation is a backward martingale in the stochastic-flow representation.

Primary references:

- Constantin--Iyer, CPAM 61 (2008), 330--345.
- Eyink, Physica D 239 (2010), 1236--1240; arXiv:0810.0817, Proposition 2.

---

## 3. Ancestor circulation barrier

At the coherent Reynolds-one crossing choose a loop with

\[
\Gamma_c\gtrsim R^2.
\]

At a `q`-earlier first-hitting checkpoint,

\[
\|\Omega_-\|_\infty\le q^{-1}.
\]

Since

\[
\Gamma_c=\mathbb E\Gamma_-^\varpi,
\]

there exists a realization with

\[
\Gamma_-^\varpi\ge\Gamma_c\gtrsim R^2.
\]

For any spanning surface,

\[
|\Gamma_-^\varpi|
\le q^{-1}A_-^\varpi,
\]

so its minimal filling area obeys

\[
\boxed{
A_{\min,-}^\varpi
\gtrsim
qR^2.
}
\]

A Euclidean filling inequality then yields

\[
\boxed{
L_-^\varpi
\gtrsim
R\sqrt q.
}
\]

Therefore deterministic late injection cannot erase the need for a large backward circulation ancestor.

---

## 4. Diameter--total-curvature product

For every closed `C2` curve,

\[
\boxed{
L(C)
\le
D(C)\mathcal K(C),
}
\]

where

\[
\mathcal K(C)=\int_C|\kappa|ds.
\]

At the earlier checkpoint the natural radius is

\[
r_-=\sqrt q.
\]

Define

\[
N_D=D_-/\sqrt q.
\]

Then the stochastic ancestor satisfies

\[
\boxed{
N_D\mathcal K_-
\gtrsim
R.
}
\]

Hence, for example,

\[
\boxed{
N_D\gtrsim\sqrt R
\quad\lor\quad
\mathcal K_-\gtrsim\sqrt R.
}
\]

A long ancestor cannot remain simultaneously local in natural-radius units and bounded in total curvature.

---

## 5. Total curvature is not a new branch

For a smooth moving curve,

\[
D_tT=(\nabla U)T-(T^TST)T.
\]

The total curvature obeys

\[
\boxed{
\frac d{dt}\mathcal K(t)
\le
2\|S(t)\|_\infty\mathcal K(t)
+
\int_{C_t}|\nabla^2U|ds.
}
\]

The additive Brownian term in the Constantin--Iyer flow has no spatial derivative, so the same spatial geometry calculation applies pathwise to each smooth stochastic-flow realization.

Thus divergent ancestor total curvature routes to

\[
\boxed{
\text{large strain action}
\quad\lor\quad
\text{large velocity-Hessian action along the ancestor}.
}
\]

With the symmetric `sqrt R` split, the curvature branch implies schematically

\[
\boxed{
\int\|S\|_\infty dt
\gtrsim
c\log R
}
\]

or

\[
\boxed{
\int\!\int_{C_t}|\nabla^2U|dsdt
\gtrsim
cR^{1/4}.
}
\]

The powers are routing exponents, not claimed optimal.

---

## 6. Updated branch tree

The previous endpoint

\[
\text{precompression + late injection}
\]

is removed as an independent stochastic-Lagrangian escape.

The exact ancestry gives instead

\[
\boxed{
\text{coherent final circulation}
\to
\text{large stochastic ancestor circulation}
\to
\text{large ancestor filling area/length}.
}
\]

The geometric product then gives

\[
\boxed{
\textbf{A. critical spatial non-tightness / shell-L3 escape}
}
\]

or

\[
\boxed{
\textbf{B. divergent total curvature}
\to
\textbf{critical strain or higher derivative}.
}
\]

Thus the endgame is again a two-class critical obstruction:

\[
\boxed{
\text{scale-space escape}
\quad\lor\quad
\text{strain/derivative degeneration}.
}
\]

The difference from the earlier tree is that this dichotomy is now forced directly by stochastic circulation ancestry and cannot be bypassed by saying that viscosity simply creates a fresh flux at the terminal scale.

---

## 7. Connection to the existing ancient-limit gate

The spatially extended ancestor option feeds the already-recorded route

\[
\text{backward critical-}L^3\text{ tightness}
\quad\lor\quad
\text{critical mass escape}.
\]

If a nontrivial ancient limit inherits uniformly bounded `L3` values along a backward sequence, the Albritton--Barker Liouville theorem would force triviality; therefore a surviving ancient branch must lose critical `L3` tightness or fail another hypothesis of that theorem.

The new stochastic ancestor diameter branch supplies a concrete geometric mechanism for precisely that loss of tightness.

---

## 8. Connection to the derivative tree

The total-curvature/Hessian option feeds

- material-probe `H2` distortion;
- high-Hermite / high-curvature descent;
- derivative covariance and factorial generating-function identities;
- palinstrophy / positive-middle-strain replenishment.

The earlier exact energy-weighted projective identity still prevents viscosity from being a positive generator of the derivative-projective defect.

Thus the derivative branch must remain nonlinearly source-active or else dissipate.

---

## 9. What is closed now

The following are no longer retained as independent endgame explanations:

- pure deterministic material translation;
- one persistent coherent material vortex inherited unchanged;
- deterministic flux reset as genuine creation from zero ancestry;
- precompress-empty-core then late-inject as an ancestry-free Zeno mechanism;
- a long stochastic ancestor that is both spatially local and uniformly bounded in total curvature.

---

## 10. Remaining theorem target

A proof would now need a finite-budget statement excluding repeated realization of

\[
\boxed{
\text{large stochastic-ancestor diameter}
\quad\lor\quad
\text{large strain/Hessian action}
}
\]

at coherent crossings with `R_j -> infinity`.

Equivalently, one needs a scale-time compactness theorem showing that the stochastic ancestor of every late coherent circulation cannot repeatedly escape to more natural radii or generate unbounded geometric curvature while remaining compatible with the finite-energy Navier--Stokes dissipation class.

This remains a genuinely critical three-dimensional problem.

Overall status: **STOCHASTIC KELVIN CLOSES THE LATE-INJECTION ANCESTRY ESCAPE; FINAL FRONTIER = STOCHASTIC SPATIAL ESCAPE VERSUS STRAIN/HESSIAN DEGENERATION; GLOBAL REGULARITY NOT PROVED.**
