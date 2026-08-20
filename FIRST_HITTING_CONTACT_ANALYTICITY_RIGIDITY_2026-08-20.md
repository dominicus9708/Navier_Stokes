# Analyticity Rigidity of the First-Hitting Contact Set — 2026-08-20

Overall status: **CONTACT-SET GEOMETRY REDUCTION — GLOBAL REGULARITY NOT PROVED.**

This note removes one of the flat-contact escapes left by the KKT contact-curvature pairing.

Reference background: positive-time mild Navier--Stokes solutions are spatially analytic; see, e.g., Wang--Gao--Xue, *Joint space-time analyticity of mild solutions to the Navier-Stokes equations*, arXiv:2112.03079, together with the classical spatial analyticity theory cited there.

---

## 1. Contact set

At a first-hitting normalized snapshot define

\[
\mathcal M
=\{x\in\mathbb R^3:|\omega(x)|=1\}.
\]

For a positive-time smooth/mild Navier--Stokes snapshot, `omega(x)` is real analytic in the spatial variables. Therefore

\[
f(x)=|\omega(x)|^2-1
\]

is a real-analytic scalar function.

---

## 2. Positive-volume plateau is impossible

A nonzero real-analytic function on a connected open set has a zero set of Lebesgue measure zero. Therefore, if

\[
|\mathcal M|>0,
\]

then

\[
f\equiv0
\]

on `R^3`, so

\[
|\omega(x)|\equiv1.
\]

But finite-energy vorticity satisfies

\[
\omega\in L^2(\mathbb R^3).
\]

A field with `|omega| = 1` everywhere cannot belong to `L^2(R^3)`. Hence

\[
\boxed{
|\mathcal M|=0
}
\]

for every nontrivial finite-energy analytic snapshot.

---

## 3. Consequence for the KKT multiplier

The formal `L^infinity` KKT multiplier is supported on `mathcal M`. Since `mathcal M` has zero three-dimensional measure, any nonzero limiting contact multiplier cannot remain an ordinary positive-volume plateau density. It must concentrate on a lower-dimensional/singular contact geometry.

Thus the previous flat-contact alternative splits as

\[
\boxed{
\text{flat contact}
\Longrightarrow
\text{lower-dimensional/degenerate analytic maximum set},
}
\]

not a finite-volume region with `|omega|=1`.

---

## 4. Analytic degeneracy alternative

At a contact point, if the quadratic curvature vanishes,

\[
-\omega\cdot\Delta\omega=0,
\]

then the maximum-point inequality gives

\[
\nabla\omega=0
\]

there as well.

For a nonconstant analytic field, complete flatness to all spatial orders at an isolated point is impossible: if every Taylor coefficient of `|omega|^2-1` vanished, analyticity would force the scalar function to vanish identically near the point and hence globally.

Therefore a zero-curvature contact point in a nontrivial analytic solution must reveal its departure from the maximum at some finite higher derivative order.

This does not yet give a uniform quantitative derivative lower bound, because the first nonzero analytic order may vary along a sequence. It does, however, eliminate the fully flat plateau escape.

---

## 5. Revised contact branch

Combining the contact-curvature identity with analyticity gives

\[
\boxed{
\text{contact-dominated threshold}
\Longrightarrow
H
\quad\text{or}\quad
\text{lower-dimensional finite-order degenerate contact geometry}.
}
\]

The next quantitative target is an analyticity-radius/finite-energy estimate showing that increasingly high-order degenerate maxima cannot recur in a tight first-hitting core without higher-derivative growth. Such a theorem would route the remaining singular contact geometry into the derivative hierarchy `H`.

Status: **A NONTRIVIAL FINITE-ENERGY ANALYTIC NAVIER--STOKES SNAPSHOT CANNOT HAVE A POSITIVE-VOLUME MAXIMUM-VORTICITY PLATEAU. ANY NONZERO FIRST-HITTING KKT CONTACT MULTIPLIER MUST LIVE ON A LOWER-DIMENSIONAL OR FINITE-ORDER DEGENERATE ANALYTIC CONTACT SET. GLOBAL REGULARITY REMAINS UNPROVED.**