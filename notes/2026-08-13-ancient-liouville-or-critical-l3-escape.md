# First-hitting ancient limit: Liouville or critical L3 mass escape

Date: 2026-08-13

Status: **EXTERNAL LIOUVILLE GATE + DERIVED CONCENTRATION-COMPACTNESS DICHOTOMY / ANCIENT LIMIT CONSTRUCTION STILL CONDITIONAL**.

This note records a precise external gate for the first-hitting ancient-limit route.

Primary reference:

- Dallas Albritton and Tobias Barker, *On Local Type I Singularities of the Navier--Stokes Equations and Liouville Theorems*, J. Math. Fluid Mech. 21 (2019), 43; arXiv:1811.00502.

Their Theorem 1.2 states that if `v` is a mild ancient solution and there exists a sequence `t_k -> -infinity` such that

\[
\sup_k\|v(\cdot,t_k)\|_{L^3(\mathbb R^3)}<\infty,
\]

then

\[
\boxed{v\equiv0.}
\]

The theorem is used here only as an external conditional gate; no claim is made that the present first-hitting compactness route has already verified all of its hypotheses.

---

## 1. First-hitting blow-up scaling

At terminal first-hitting vorticity level `W_j`, let

\[
r_j=W_j^{-1/2},
\]

\[
U_j(y,s)=r_j u(x_j+r_jy,t_j+r_j^2s).
\]

The velocity `L3` norm is scale invariant:

\[
\boxed{
\|U_j(\cdot,s)\|_3
=\|u(\cdot,t_j+r_j^2s)\|_3.
}
\]

The normalized past horizon satisfies

\[
W_jt_j\to\infty
\]

under a hypothetical finite singular time `T*>0`.

---

## 2. Fixed physical past slices vanish locally after blow-up scaling

Fix any smooth physical time

\[
t_0<T^*.
\]

Its normalized time is

\[
s_j=W_j(t_0-t_j)\to-\infty.
\]

Because `u(t0) in L3(R3)`, absolute continuity of the integral gives, for every fixed `R`, uniformly in the moving center,

\[
\int_{B_{Rr_j}(x_j)}|u(x,t_0)|^3dx\to0.
\]

By scale invariance,

\[
\boxed{
\int_{B_R}|U_j(y,s_j)|^3dy\to0.
}
\]

Thus fixed physical history becomes locally invisible at the ancient end of the terminal blow-up normalization.

The same conclusion holds for local critical energy using `H1` regularity at `t0`.

---

## 3. Why the global L3 bound does not automatically transfer

At the moving times `s_j`,

\[
\|U_j(s_j)\|_3=\|u(t_0)\|_3<\infty.
\]

However `s_j` depends on `j` and tends to `-infinity`.  Standard local compactness of `U_j` on each fixed finite normalized time interval does not automatically pass this bound to a prescribed backward sequence of times of one limiting ancient solution.

Therefore the Albritton--Barker theorem cannot be invoked solely from the prelimit equality above.

This is the precise missing compactness/tightness step.

---

## 4. Liouville-or-escape dichotomy

Assume a nontrivial mild ancient limit `U_infty` is successfully extracted and retains the terminal normalization.

If there exists a backward sequence

\[
s_k\downarrow-\infty
\]

with

\[
\boxed{
\sup_k\|U_\infty(s_k)\|_3<\infty,
}
\]

then Albritton--Barker Theorem 1.2 gives

\[
\boxed{U_\infty\equiv0,}
\]

contradicting nontrivial terminal normalization.

Hence every nontrivial ancient residual state avoiding that Liouville gate must fail backward `L3` compactness.

Schematically,

\[
\boxed{
\text{nontrivial ancient limit}
\Longrightarrow
\text{backward critical-}L^3\text{ non-tightness}
}
\]

unless another hypothesis of the external theorem fails.

---

## 5. Spatial interpretation of non-tightness

The prelimit fixed-physical-time slices vanish in every fixed normalized ball while their global `L3` norm is scale invariant.

Therefore the natural concentration-compactness interpretation is **critical mass escape to normalized spatial infinity**.

A useful quantitative tightness condition is:

there exist `s_k -> -infinity` and, for every epsilon, an `R(epsilon)` such that

\[
\int_{|y|>R}|U_\infty(y,s_k)|^3dy<\epsilon
\]

uniformly in `k`, together with a uniform global `L3` bound.

If such tightness can be inherited from the prelimit sequence, the Liouville gate closes the ancient branch.

Failure means that a fixed amount of critical `L3` mass remains outside every fixed observation radius along the backward route.

---

## 6. DSD interpretation

The ancient branch is no longer an untyped infinite-history escape.

It becomes

\[
\boxed{
\text{Liouville-admissible backward }L^3\text{ slices}
}
\]

or

\[
\boxed{
\text{critical }L^3\text{ mass escapes to spatial infinity}.
}
\]

In the second case, the terminal dangerous core must eventually be supplied by information/mass that was outside every fixed normalized observation window in the backward regime.

This should be intersected with the existing shell-flux, pressure-localization, affine-background, and Gaussian residual channels.

---

## 7. Active next target

Derive a critical-shell transport statement of the form

\[
\boxed{
\text{backward }L^3\text{ escape}
+\text{nontrivial terminal core}
\Longrightarrow
\text{order-one inward critical flux across some normalized shell}
}
\]

or show that bounded shell/pressure channels imply `L3` tightness along a backward sequence, which would activate the external Liouville theorem.

Status: **ANCIENT ROUTE REDUCED TO LIOUVILLE OR CRITICAL-MASS ESCAPE / SHELL-TIGHTNESS BRIDGE OPEN**.
