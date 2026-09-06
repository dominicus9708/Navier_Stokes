# DSD M17-294 — Derivative feed is Gaussian variance and forces T^(5/2) backward normalized palinstrophy

Date: 2026-09-06  
Canonical ID: **M17-294**

Status: **DERIVATIVE-FEED STRENGTHENING / M17-287 LOWER-BOUNDED TOTAL BACKWARD MASS FROM A NONZERO PRESENT `Delta V`, BUT `Delta p_T` HAS ZERO SPATIAL MEAN. THEREFORE A COHERENT CONSTANT BACKGROUND CONTRIBUTES NOTHING TO THE SECOND-DERIVATIVE FEED. SUBTRACTING THE OPTIMAL GAUSSIAN-WEIGHTED CONSTANT BEFORE CAUCHY--SCHWARZ SHOWS THAT THE REQUIRED `T^(7/2)` QUANTITY IS ACTUALLY GAUSSIAN-WEIGHTED VARIANCE. THE GAUSSIAN POINCARE INEQUALITY THEN CONVERTS THAT VARIANCE INTO A BACKWARD WEIGHTED DIRICHLET/PALINSTROPHY LOWER BOUND `>=c T^(5/2)`. THUS, WHEN THE HEAT-KERNEL CUTOFF REPRESENTATION HAS NO NONVANISHING FAR-BOUNDARY REMAINDER, EVERY NONZERO ANCIENT SECOND-DERIVATIVE CORE FORCES UNBOUNDED NORMALIZED PALINSTROPHY ON GROWING BACKWARD DIFFUSION SCALES. SPATIAL-INFINITY FEED CANNOT HIDE IN A PURE CONSTANT MEAN. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Present derivative witness

As in M17-287, choose a point `z_*` in the retained core such that

\[
\boxed{|\Delta V(z_*,0)|\ge c_0>0.}
\]

Assume the cutoff boundary remainder vanishes for the backward heat representation at time `-T`.

Then

\[
\boxed{
\Delta V(z_*,0)
=
\int_{\mathbb R^3}
\Delta p_T(z_*-y)V(y,-T)dy.
}
\]

---

## 2. Constants do not feed a second derivative

Because

\[
\boxed{
\int_{\mathbb R^3}\Delta p_T(y)dy=0,
}
\]

for every constant vector `c in R3`,

\[
\boxed{
\Delta V(z_*,0)
=
\int\Delta p_T(z_*-y)[V(y,-T)-c]dy.
}
\]

Thus the derivative witness is insensitive to arbitrary coherent constant backgrounds.

This removes the main weakness of the raw total-mass estimate in M17-287.

---

## 3. Gaussian-weighted variance lower bound

Let

\[
w_T(y):=
\exp\!\left(-\frac{|y-z_*|^2}{8T}\right).
\]

Choose the weighted mean

\[
\boxed{
c_T
:=
\frac{\int w_TV(y,-T)dy}{\int w_Tdy}
}
\]

whenever the weighted integrals are finite.

Weighted Cauchy--Schwarz gives

\[
|\Delta V(z_*,0)|^2
\le
\left(
\int\frac{|\Delta p_T(z_*-y)|^2}{w_T(y)}dy
\right)
\left(
\int w_T|V(y,-T)-c_T|^2dy
\right).
\]

By heat-kernel scaling in dimension three,

\[
\boxed{
\int\frac{|\Delta p_T|^2}{w_T}
\asymp T^{-7/2}.
}
\]

Hence

\[
\boxed{
\int w_T(y)|V(y,-T)-c_T|^2dy
\ge cT^{7/2}.
}
\]

If this weighted variance is infinite, retain the stronger spatial-infinity fluctuation exit.

---

## 4. Gaussian Poincare converts variance to gradient energy

For the Gaussian weight `w_T`, the standard Gaussian Poincare inequality gives

\[
\boxed{
\int w_T|V-c_T|^2
\le
C_PT
\int w_T|\nabla V|^2.
}
\]

Combining with Section 3,

\[
\boxed{
\int_{\mathbb R^3}
 w_T(y)|\nabla V(y,-T)|^2dy
\ge cT^{5/2}.
}
\]

This is a true mean-free derivative cost.

---

## 5. Pre-limit normalized palinstrophy meaning

In root packet variables,

\[
V_j(z,\tau)
=\frac{r_j^{3/2}}{m_j^{1/2}}
W_j(q_j+r_jz,\theta_j+r_j^2\tau).
\]

Therefore

\[
\int w_T|\nabla_zV_j|^2dz
=
\frac{r_j^2}{m_j}
\int
w_T\!\left(\frac{y-q_j}{r_j}\right)
|\nabla_yW_j|^2dy.
\]

Thus the tangent lower bound is exactly a growing-radius **normalized palinstrophy** lower bound:

\[
\boxed{
\frac{r_j^2}{m_j}
\int_{B_{O(\sqrt T)r_j}}
|\nabla W_j|^2
\gtrsim T^{5/2}
}
\]

up to Gaussian tails and the limit passage.

---

## 6. New infinity-feed gate

Consequently

\[
\boxed{
H_{nonzero\ ancient\ second\text{-}derivative\ core}
\Longrightarrow
H_{growing\ normalized\ palinstrophy}
\lor
G_{far\text{-}boundary/infinity\ feed}
\lor
G_{Gaussian\ variance\ divergence}.
}
\]

The last branch is itself a stronger mean-free spatial-infinity escape.

In particular, an `R^3` or `R^7` **coherent constant mean** cannot pay the present derivative witness because constants are annihilated by `Delta p_T`.

---

## 7. Effect on M17-284--293

M17-284--293 classified the unbounded nodal survivor through global mass growth, mesoscopic horizon, and ground-state/Martin-boundary language.

M17-294 strengthens that frontier:

- if the infinity mode enters only as a coherent mean, it cannot feed `Delta V`;
- any legitimate derivative feed has a mean-zero variance component;
- that component forces normalized palinstrophy at order `T^(5/2)` unless the representation itself receives a nonvanishing far-boundary term.

Thus the unbounded nodal branch is pushed directly toward the already-listed normalized-palinstrophy or infinity-boundary channels.

---

## 8. DSD audit

- The subtraction constant is chosen only because `Delta p_T` has zero mean; no physical mean is assumed.
- The Gaussian Poincare inequality is applied to the same weighted variance produced by the kernel estimate.
- The result remains conditional on vanishing cutoff boundary remainder; failure is retained explicitly.
- No finite global palinstrophy budget is claimed here; `normalized palinstrophy` remains a hard branch, not a contradiction by itself.
- Global 3D Navier--Stokes regularity remains unproved.

---

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
