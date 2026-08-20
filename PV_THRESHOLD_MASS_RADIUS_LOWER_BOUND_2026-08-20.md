# Mass--Radius Lower Bound for Dangerous P_V Threshold Cores — 2026-08-20

Overall status: **NONVANISHING COMPACTNESS LEMMA — GLOBAL REGULARITY NOT PROVED.**

This note adds a concentration-compactness ingredient to the `P_V` threshold problem. A core whose H1 efficiency reaches the viscous threshold cannot vanish in `L^2` while remaining spatially tight.

---

## 1. Notation

Let

\[
E=\|S\|_2^2,
\qquad
P=\|\nabla S\|_2^2,
\qquad
H=\|\Delta S\|_2^2,
\]

\[
M=\int_{\mathbb R^3}|x-X|^2|S(x)|^2dx
\]

for a chosen center `X`.

Let

\[
N=-\langle\mathcal R_{VI},-\Delta S\rangle
\]

and

\[
\eta=N/H.
\]

The sharp/local trace-free calculation gives

\[
N\lesssim\int|S||\nabla S|^2.
\]

---

## 2. Gagliardo--Nirenberg estimate

Using Holder and Sobolev interpolation,

\[
\int|S||\nabla S|^2
\lesssim
P^{5/4}H^{1/4}.
\]

Therefore

\[
\boxed{
\eta
\lesssim
P^{5/4}H^{-3/4}.
}
\]

The standard interpolation identity

\[
P^2\le EH
\]

implies

\[
H\ge P^2/E.
\]

Hence

\[
\boxed{
\eta\lesssim E^{3/4}P^{-1/4}.
}
\]

---

## 3. Three-dimensional uncertainty bound

For a scalar or matrix field in `H^1 cap L^2`, integration by parts in three dimensions gives

\[
\| (x-X)S\|_2\,\|\nabla S\|_2
\ge
\frac32\|S\|_2^2.
\]

Therefore

\[
\boxed{
MP\ge\frac94E^2.
}
\]

Consequently

\[
P^{-1/4}
\lesssim
M^{1/4}E^{-1/2}.
\]

Substitution yields

\[
\boxed{
\eta(S)
\lesssim
(E M)^{1/4}.
}
\]

This bound has the correct behavior under pure amplitude and coordinate rescaling.

---

## 4. Dangerous threshold implies nonvanishing mass-radius product

If a core reaches the viscous threshold

\[
\eta(S)\ge\nu,
\]

then

\[
\boxed{
E M\gtrsim\nu^4.
}
\]

Define its rms radius

\[
R_S^2=M/E.
\]

Then

\[
EM=E^2R_S^2,
\]

so

\[
\boxed{
E R_S\gtrsim\nu^2.
}
\]

Thus on a tight class with

\[
R_S\le R_*<\infty,
\]

one automatically has

\[
\boxed{
E\ge c(\nu,R_*)>0.
}
\]

A dangerous maximizing sequence therefore cannot disappear weakly to zero while remaining spatially tight.

---

## 5. Combination with the first-hitting amplitude cap

For the full strain on `R^3`,

\[
\|S\|_2^2=\frac12\|\omega\|_2^2.
\]

On a first-hitting core with `||Omega||_infty <= 1`, if the vorticity mass is genuinely localized inside radius `R_S` up to a controlled tail, then schematically

\[
E\lesssim R_S^3.
\]

Combining this with `E R_S >= c nu^2` gives the conditional radius floor

\[
\boxed{
R_S\gtrsim c\,\nu^{1/2}.
}
\]

This last step requires a quantitative localization/tail assumption and is therefore a conditional core estimate, unlike the unconditional `EM >= c nu^4` threshold bound.

---

## 6. Compactness consequence

The threshold localization and curvature bootstrap already provide, on the non-H/non-T branch,

- bounded normalized radius;
- bounded local `H^2` norm at the dangerous threshold cell, unless a new H/T packet appears.

The present estimate adds

- a positive lower bound on local `L^2` strain mass.

Thus a dangerous threshold sequence cannot escape by translation (`T`), by dilation (tightness fixes the moment), by high-curvature concentration (`H`/curvature bootstrap), or by vanishing (`EM` lower bound).

The remaining compactness defect is essentially splitting/dichotomy into multiple comparable threshold cells, which should be classified as multicore turnover `T`.

Status: **ANY P_V CORE REACHING eta >= nu MUST CARRY A DEFINITE MASS--RADIUS PRODUCT. ON A TIGHT NON-H BRANCH THIS GIVES A POSITIVE L2 MASS FLOOR AND REMOVES THE VANISHING ESCAPE FROM THE THRESHOLD MAXIMIZATION PROBLEM. GLOBAL REGULARITY REMAINS UNPROVED.**