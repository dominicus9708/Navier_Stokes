# Stochastic ancestor diameter--total-curvature product barrier

Date: 2026-08-16

Status: **EXACT ELEMENTARY CURVE INEQUALITY + STOCHASTIC-KELVIN LENGTH INPUT / SHARPENS THE CRUMPLING BRANCH / GLOBAL REGULARITY NOT PROVED**.

## 1. Input

The stochastic-Kelvin ancestor circulation barrier gives an earlier stochastic ancestor loop `C_-` satisfying

\[
\boxed{
L(C_-)
\gtrsim
R\sqrt q.
}
\]

The earlier first-hitting vorticity level is `1/q`, whose natural radius in terminal-normalized coordinates is

\[
\boxed{r_-=\sqrt q.}
\]

The question is whether the forced large ancestor length can remain both spatially localized and geometrically smooth.

---

## 2. Elementary diameter--curvature inequality

Let `C` be a closed `C2` curve parameterized by arclength `s`.

Write

\[
T(s)=x'(s),
\qquad |T|=1,
\]

and

\[
\mathcal K(C)
:=
\int_C|T'(s)|ds
=
\int_C|\kappa(s)|ds
\]

for the total curvature.

Fix any point `x0` on the curve.  Since the curve is closed,

\[
\int_C\frac d{ds}
\big[(x-x_0)\cdot T\big]ds=0.
\]

But

\[
\frac d{ds}
\big[(x-x_0)\cdot T\big]
=
|T|^2+(x-x_0)\cdot T'
=
1+(x-x_0)\cdot T'.
\]

Therefore

\[
L(C)
=-
\int_C(x-x_0)\cdot T'\,ds.
\]

If

\[
D(C)=\operatorname{diam}(C),
\]

then `|x-x0|<=D(C)`, hence

\[
\boxed{
L(C)
\le
D(C)\mathcal K(C).
}
\]

Equivalently,

\[
\boxed{
D(C)\mathcal K(C)
\ge
L(C).
}
\]

No topology, minimal-surface theory, or Navier--Stokes estimate is used here.

---

## 3. Apply to the stochastic ancestor

For `C_-`,

\[
D_-\mathcal K_-
\gtrsim
R\sqrt q.
\]

Normalize the ancestor diameter by the earlier natural radius:

\[
\boxed{
N_D
:=
\frac{D_-}{\sqrt q}.
}
\]

Then

\[
\boxed{
N_D\mathcal K_-
\gtrsim
R.
}
\]

This is scale invariant: `N_D` and total curvature are dimensionless.

Since

\[
R\to\infty,
\]

we immediately obtain

\[
\boxed{
N_D\to\infty
\quad\text{or}\quad
\mathcal K_-\to\infty
}
\]

along every late subsequence, and more quantitatively, for any splitting parameter `M>0`,

\[
\boxed{
N_D\ge M
\quad\text{or}\quad
\mathcal K_-\gtrsim R/M.
}
\]

Choosing

\[
M=\sqrt R
\]

gives the symmetric form

\[
\boxed{
N_D\gtrsim\sqrt R
\quad\text{or}\quad
\mathcal K_-\gtrsim\sqrt R.
}
\]

Thus every sufficiently late stochastic ancestor is forced to be extreme in at least one of two senses.

---

## 4. Branch interpretation

### D-branch: large normalized diameter

\[
N_D=D_-/r_-\to\infty.
\]

The ancestor loop spans an increasing number of the earlier checkpoint's own natural radii.

This is genuine spatial non-tightness, not merely a long curve hidden locally.  It returns to

- shell transport;
- oriented circulation persistence;
- critical `L3` mass escape;
- the ancient-limit tightness/Liouville gate.

### K-branch: divergent total curvature

\[
\mathcal K_-	o\infty.
\]

The loop can remain within fewer natural radii only by accumulating an unbounded amount of tangent rotation.

This is a cleaner version of the previous reach/crumpling branch.  A helical or many-fold configuration with bounded pointwise curvature but many turns is still detected because total curvature counts all turns.

Therefore repeated mild curvature spread over a very long curve does not evade the descriptor.

---

## 5. Why total curvature is the correct material-flow derivative channel

For a smooth material/stochastic curve, the unit tangent satisfies schematically

\[
D_tT
=(I-T\otimes T)(\nabla U)T.
\]

Differentiating once more along arclength introduces spatial derivatives of `grad U`:

\[
D_t(\partial_sT)
=
\text{terms involving }
\nabla U\,\partial_sT
+
\nabla^2U.
\]

Consequently a large change in total curvature is supported by

\[
\boxed{
\text{strain acting on existing curvature}
\quad\lor\quad
\text{velocity-Hessian forcing}.
}
\]

This routes the K-branch to the existing

- material-probe `H2` distortion;
- higher-derivative radius-collapse;
- derivative covariance / factorial-generating-function channels.

A referee-grade evolution inequality for total curvature should keep cutoff and parametrization factors explicit, but no new causal branch is introduced.

---

## 6. Strengthening of the previous trichotomy

The previous reach estimate gave

\[
\text{large diameter}
\lor
\text{small reach}.
\]

The present identity is stronger for the intended proof architecture:

\[
\boxed{
\text{large normalized diameter}
\lor
\text{large total curvature}.
}
\]

It detects both

- pointwise high curvature;
- many moderate-curvature folds/turns.

Hence a long stochastic ancestor cannot escape by replacing one sharp fold with many gentle folds.

---

## 7. New reduced frontier

Combining stochastic Kelvin with the present product barrier gives

\[
\boxed{
\text{coherent crossing}
\Longrightarrow
\text{stochastic ancestor with }
N_D\mathcal K\gtrsim R.
}
\]

Therefore the late-injection/Zeno branch has been reduced to

\[
\boxed{
\textbf{critical spatial escape}
\quad\lor\quad
\textbf{divergent material total curvature / higher derivative}.
}
\]

The next target is to show that neither quantity can diverge repeatedly along a finite-time first-hitting cascade without violating an already finite spacetime budget.

Overall status: **NO STOCHASTIC ANCESTOR CAN BE SIMULTANEOUSLY LOCAL IN NATURAL-RADIUS UNITS AND UNIFORMLY BOUNDED IN TOTAL CURVATURE / GLOBAL REGULARITY NOT PROVED.**
