# DSD M17-297 — Uniform analyticity does not exclude heat-scale exponentially tiny high-frequency components

Date: 2026-09-06  
Canonical ID: **M17-297**

Status: **ANTI-SHORTCUT / M17-296 LEAVES THE HEAT-SCALE EXPONENTIAL AMPLITUDE DEFECT `a_j <= C exp(-c/r_j^2)`. IT IS TEMPTING TO USE THE PARENT FIRST-HITTING ANALYTICITY BOUNDS TO RULE OUT A SCALE-`r_j` COMPONENT WITH SUCH A TINY COEFFICIENT. THAT IS FALSE. THE EXPLICIT ANALYTIC FAMILY `f_r(x)=exp(-1/r^2) sin(x/r)` HAS FREQUENCY `1/r` BUT EVERY FIXED REAL DERIVATIVE TENDS TO ZERO, AND IT REMAINS UNIFORMLY SMALL ON EVERY FIXED COMPLEX STRIP BECAUSE `-1/r^2` DOMINATES THE STRIP GROWTH `rho/r`. THUS EVEN A UNIFORM POSITIVE ANALYTICITY RADIUS AND ALL FIXED-ORDER DERIVATIVE CEILINGS ALLOW BEYOND-ALL-ORDERS FREQUENCY/AMPLITUDE DECOUPLING. THE EXPONENTIAL SURVIVOR MUST BE ATTACKED BY DYNAMICS, PACKING, GENEALOGY, OR A LOWER-AMPLITUDE PRINCIPLE, NOT ANALYTIC UPPER BOUNDS ALONE. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Explicit analytic test family

For `r>0`, define in one coordinate

\[
\boxed{
f_r(x):=e^{-1/r^2}\sin(x/r).}
\]

Its characteristic oscillation scale is `r`.

For every fixed derivative order `m`,

\[
\boxed{
\|f_r^{(m)}\|_{L^\infty(\mathbb R)}
\le e^{-1/r^2}r^{-m}.
}
\]

As `r->0`,

\[
e^{-1/r^2}r^{-m}\to0
\]

for every fixed `m`.

Therefore any finite collection of derivative ceilings is satisfied with enormous margin.

---

## 2. Even a fixed analytic strip does not help

Extend `f_r` holomorphically to `z=x+iy`.

On a fixed strip

\[
|y|<\rho,
\]

we have

\[
|\sin(z/r)|\lesssim e^{\rho/r}.
\]

Hence

\[
\boxed{
\sup_{|\operatorname{Im}z|<\rho}|f_r(z)|
\lesssim
\exp\!\left(-\frac1{r^2}+\frac\rho r\right).
}
\]

Since

\[
\frac1{r^2}\gg\frac1r,
\]

the right-hand side tends to zero.

Thus the family is compatible with a fixed positive analyticity radius and a uniform analytic sup bound.

---

## 3. Spectral ratio remains large

Despite the tiny absolute coefficient,

\[
\frac{\|f_r''\|}{\|f_r\|}
\asymp r^{-2},
\]

and in squared `H2/L2` form

\[
\boxed{
\frac{\|f_r''\|_2^2}{\|f_r\|_2^2}
\asymp r^{-4}.
}
\]

Thus exactly the relative spectral behavior relevant to the microcarrier survives while all absolute fixed-order derivative amplitudes vanish.

---

## 4. Heat-scale meaning

Under the heat equation, a frequency `1/r` mode evolves by the factor

\[
e^{-t/r^2}.
\]

A current amplitude

\[
e^{-c/r^2}
\]

can therefore arise from an order-one bounded ancestor a fixed `O(c)` time in the past under purely linear diffusion.

This is why the M17-296 exponent is dynamically natural rather than a technical artifact.

---

## 5. Consequence for the proof strategy

The implication

\[
\boxed{
\text{uniform analyticity}
\not\Rightarrow
\text{lower bound on high-frequency coefficient amplitude}
}
\]

must be retained.

Therefore M5-392-type fixed-order/analytic upper bounds cannot by themselves close

\[
G_{heat\text{-}scale\ exponential\ amplitude\ degeneration}.
\]

The branch must return through one of

\[
\boxed{
H_{shell\ packing}
\lor
H_{genealogy/dynamic\ return}
\lor
H_{normalized\ palinstrophy}
\lor
G_{interface/infinity}.
}
\]

---

## 6. DSD audit

- The example is a structural counterexample to an inference, not a Navier--Stokes solution.
- It shows compatibility with analytic **upper** bounds only.
- No claim is made that the full CE-H/director constraints admit this exact sine family.
- The false closure being removed is purely `analyticity => amplitude lower bound`.
- Global 3D Navier--Stokes regularity remains unproved.

---

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
