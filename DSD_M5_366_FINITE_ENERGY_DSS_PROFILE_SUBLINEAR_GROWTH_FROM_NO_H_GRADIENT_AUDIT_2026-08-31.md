# DSD M5-366 — Finite-Energy DSS Profile: Sublinear Growth from No-H Gradient Control

Date: 2026-08-31

Status: **THE GROWTH-HYPOTHESIS BRIDGE FOR THE EXACT `alpha=3/2` DSS ENDPOINT IS CLOSED ON THE NO-DERIVATIVE-ESCAPE BRANCH / UNIFORM `L2` ENERGY PLUS UNIFORM PROFILE-GRADIENT CONTROL GIVES UNIFORM `L∞`, HENCE SUBLINEAR GROWTH / CHAE--WOLF 2023 THEN FORCES THE DSS PROFILE TO BE SPATIALLY CONSTANT, AND FINITE ENERGY FORCES ZERO / GLOBAL REGULARITY UNPROVED.**

## 1. Purpose

M5-365 established the exact relation

\[
 \lambda=q^{2/5},
 \qquad
 S_0=\log q
\]

between a first-hitting `q` step and an `alpha=3/2` Euler DSS period.

The external Chae--Wolf 2023 theorem removes `(alpha,lambda)`-DSS Euler profiles for

\[
 \alpha\ge\frac32
\]

under sublinear growth at infinity.

The remaining bridge was to obtain sublinear growth from the current finite-energy/no-H endpoint.

## 2. Endpoint energy

At the energy-conserving exponent

\[
 \alpha=\frac32,
\]

the similarity transform preserves the `L2` norm.

The Seregin endpoint reduction from M5-363--364 supplies

\[
 \boxed{
 \sup_s\|V(s)\|_{L^2(\mathbb R^3)}
 \le E_*<\infty.
 }
\]

For an exact DSS profile, `V` is periodic in `s` with period `S0=log q`.

## 3. No-H gradient lane

Define the derivative-tail alternative

\[
 H_{\nabla,\infty}
 :=
 \left\{
 \sup_{(y,s)\in\mathbb R^3\times[0,S_0]}
 |\nabla V(y,s)|=\infty
 \right\}.
\]

On the complementary no-H lane, assume

\[
 \boxed{
 \sup_{y,s}|\nabla V(y,s)|
 \le M_*<\infty.
 }
\]

This is the natural global profile-gradient version of the derivative-tightness condition.

## 4. `L2 + Lipschitz -> L∞`

For every fixed `s`, the three-dimensional Gagliardo--Nirenberg estimate gives

\[
 \boxed{
 \|V(s)\|_\infty
 \le
 C
 \|V(s)\|_2^{2/5}
 \|\nabla V(s)\|_\infty^{3/5}.
 }
\]

Hence

\[
 \boxed{
 \sup_s\|V(s)\|_\infty
 \le
 C E_*^{2/5}M_*^{3/5}<\infty.
 }
\]

The exponent can also be recovered directly by the ball argument: a value of amplitude `A` and Lipschitz bound `M_*` occupies a ball of radius `~A/M_*`, which costs `~A^5/M_*^3` of `L2` energy.

## 5. Uniform sublinear growth

The uniform `L∞` bound immediately implies

\[
 \boxed{
 \sup_{s\in[0,S_0]}
 \frac{|V(y,s)|}{|y|}
 \longrightarrow0
 \qquad (|y|\to\infty).
 }
\]

Thus the profile has sublinear growth at spatial infinity in a form stronger than needed for the Chae--Wolf 2023 theorem.

No separate pointwise-decay theorem is required.

## 6. Apply Chae--Wolf 2023

Chae and Wolf, *On the Discretely Self-similar Solutions to the Euler Equations in R^3*, J. Nonlinear Sci. 33 (2023), 115, prove that for

\[
 \alpha\ge\frac32
\]

an `(alpha,lambda)`-DSS Euler profile with sublinear growth at infinity is spatially constant:

\[
 V(y,s)=c(s).
\]

At the current endpoint

\[
 \alpha=\frac32,
\]

all hypotheses of the growth part are now matched on the no-H gradient lane.

## 7. Finite energy kills the spatial constant

Since

\[
 V(s)\in L^2(\mathbb R^3),
\]

a spatial constant belongs to `L2` only if

\[
 c(s)=0.
\]

Therefore

\[
 \boxed{
 V\equiv0.
 }
\]

This contradicts the nontrivial first-hitting/Euler vorticity witness.

Hence

\[
 \boxed{
 \text{nontrivial exact `alpha=3/2` DSS endpoint}
 \Longrightarrow
 H_{\nabla,\infty}.
 }
\]

Equivalently, on the no-H derivative lane the exact DSS endpoint is empty.

## 8. Independent Chae--Wolf 2017 route

There is also a second route.

If

\[
 \sup_s\|\nabla V(s)\|_\infty<\infty,
\]

then in physical Euler variables

\[
 (-t)\|\nabla u(t)\|_\infty
 =\|\nabla V(s)\|_\infty
\]

is uniformly bounded.

Thus the Euler Type-I gradient hypothesis of Chae--Wolf's energy-concentration theorem is satisfied.

Their energy-conserving DSS corollary again gives

\[
 V\equiv0.
\]

The 2017 and 2023 routes are therefore consistent and mutually reinforcing.

## 9. Scope of the H alternative

The statement

\[
 \sup|\nabla V|=\infty
\]

must not be silently called a contradiction.

It is the derivative-at-infinity/high-frequency complement:

\[
 \boxed{H_{\nabla,\infty}.}
\]

To eliminate the original Navier--Stokes singularity, this H branch still needs to be routed through the existing derivative/non-tightness/turnover tree.

## 10. Rotated DSS

The argument above addresses exact non-rotated DSS.

A rotated DSS profile requires a separate theorem/hypothesis match. Existing Euler RDSS exclusion results use an isolated-singularity condition and a vorticity-decay condition at infinity.

Those assumptions are not automatically established here and should remain a separate audit.

## 11. Formation-axiom consequence

The similarity endpoint fork becomes

\[
 \boxed{
 E_{\rm Euler}
 \Longrightarrow
 H_{\nabla,\infty}
 \lor
 E_{\rm RDSS}
 \lor
 E_{\rm aperiodic/reforming}.
 }
\]

The exact non-rotated DSS leaf has been removed from the no-H branch.

## 12. Audit verdict

### DERIVED

- uniform `L2` plus uniform global profile-gradient bound gives uniform `L∞`;
- therefore the profile is uniformly sublinear at infinity;
- finite-energy spatial constants are zero.

### EXTERNAL

- Chae--Wolf 2023 DSS rigidity at `alpha>=3/2` under sublinear profile growth;
- Chae--Wolf 2017 energy-conserving DSS exclusion under Euler Type-I gradient control.

### CLOSED ON NO-H

\[
 \boxed{
 E_{\rm DSS}\cap(\text{no-}H_{\nabla,\infty})
 =\varnothing.
 }
\]

### OPEN

- derivative-at-infinity H;
- rotated DSS;
- aperiodic/reforming similarity dynamics;
- global regularity.

\[
 \boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
