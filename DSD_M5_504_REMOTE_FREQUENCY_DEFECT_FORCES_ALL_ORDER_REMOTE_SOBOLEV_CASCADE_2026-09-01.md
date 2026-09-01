# DSD M5-504 — Remote frequency defect forces an all-order remote Sobolev cascade

Date: 2026-09-01

Status: **ALL-DERIVATIVE ESCALATION / ON THE M5-502--503 UNBOUNDED-PALINSTROPHY SEQUENCE, THE SIMILARITY ENSTROPHY `E` STAYS UNIFORMLY BOUNDED WHILE `P=||grad W||_2^2` DIVERGES / PLANCHEREL PLUS JENSEN'S INEQUALITY GIVES FOR EVERY INTEGER `m>=1` THE SHARP MOMENT LOWER BOUND `D_m >= P^m/E^(m-1)` WITH `D_m=||grad^m W||_2^2` / HENCE EVERY FIXED GLOBAL SOBOLEV DERIVATIVE ORDER DIVERGES ALONG THE SAME SEQUENCE / LOCAL SMOOTH PRECOMPACTNESS BOUNDS EVERY FIXED DERIVATIVE ORDER ON EVERY FIXED BALL, SO THE DIVERGENT PART OF EVERY `D_m` MUST ESCAPE TO SPATIAL INFINITY / THE REMOTE-P BRANCH IS THEREFORE AN EXPLICIT ALL-ORDER REMOTE SOBOLEV-CASCADE ENDPOINT, NOT A LOCAL POINTWISE DERIVATIVE BLOWUP / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Input from M5-502--503

Along a sequence of similarity states/times `theta_n`,

\[
P_n
:=
\|\nabla W(\theta_n)\|_2^2
\to\infty,
\]

while

\[
E_n
:=
\|W(\theta_n)\|_2^2
\le Z_*<\infty.
\]

M5-502 proves that the divergent first-derivative mass escapes every fixed similarity ball.

M5-503 further proves a remote shell scale-frequency defect.

We now audit the entire derivative hierarchy.

---

## 2. Define the full derivative moments

For an integer `m>=0`, define

\[
\boxed{
D_m(\theta)
:=
\|\nabla^m W(\theta)\|_2^2,
}
\]

where `|grad^m W|^2` denotes the full ordered derivative tensor norm.

With the standard Fourier convention, Plancherel gives

\[
\boxed{
D_m
=
\int_{\mathbb R^3}
|\xi|^{2m}
|\widehat W(\xi)|^2d\xi.
}
\]

Thus

\[
D_0=E,
\qquad
D_1=P,
\qquad
D_2=\|\nabla^2W\|_2^2=\|\Delta W\|_2^2
\]

on the whole space, with the last equality understood through the same Fourier multiplier identity.

If some `D_m` is already infinite, all lower-bound statements below hold in the extended sense and the cascade branch is already active at that order.

---

## 3. Spectral probability measure

On the divergent sequence `P_n>0`, necessarily `E_n>0`.

Define the probability measure

\[
d\mu_n(\xi)
:=
\frac{|\widehat W(\xi,\theta_n)|^2}{E_n}d\xi.
\]

Then

\[
\int d\mu_n=1.
\]

Let

\[
X(\xi):=|\xi|^2.
\]

We have

\[
\frac{P_n}{E_n}
=
\int X\,d\mu_n,
\]

and more generally

\[
\frac{D_m(\theta_n)}{E_n}
=
\int X^m\,d\mu_n.
\]

---

## 4. Jensen moment lower bound

For every integer `m>=1`, the function

\[
x\mapsto x^m
\]

is convex on `[0,infinity)`.

Therefore Jensen's inequality gives

\[
\int X^m d\mu_n
\ge
\left(
\int Xd\mu_n
\right)^m.
\]

Hence

\[
\frac{D_m(\theta_n)}{E_n}
\ge
\left(
\frac{P_n}{E_n}
\right)^m.
\]

Equivalently,

\[
\boxed{
D_m(\theta_n)
\ge
\frac{P_n^m}{E_n^{m-1}}.
}
\]

Using `E_n<=Z_*`,

\[
\boxed{
D_m(\theta_n)
\ge
\frac{P_n^m}{Z_*^{m-1}}.
}
\]

Thus for every fixed integer `m>=1`,

\[
\boxed{
P_n\to\infty
\Longrightarrow
D_m(\theta_n)\to\infty.
}
\]

This occurs along the **same palinstrophy-divergent sequence**.

---

## 5. First concrete consequences

For `m=2`,

\[
\boxed{
D_2
\ge
\frac{P^2}{E}
\ge
\frac{P^2}{Z_*}.
}
\]

Therefore the M5-501 fourth-order dissipation quantity

\[
H=\|\Delta W\|_2^2
\]

cannot remain bounded on the remote-P branch.

Indeed

\[
\boxed{
H_n\to\infty.
}
\]

Moreover

\[
\frac{H_n}{P_n}
\ge
\frac{P_n}{Z_*}
\to\infty.
\]

Thus the second derivative scale separates from the first derivative scale.

For `m=3`,

\[
D_3
\ge
\frac{P^3}{Z_*^2},
\]

and similarly for every higher order.

---

## 6. Local smooth compactness pushes every order outward

The marked ancient/similarity hull is smoothly precompact on every fixed compact space-time region away from the terminal boundary.

Hence, for every fixed derivative order `m` and radius `R`, there exists

\[
C_{m,R}<\infty
\]

such that

\[
\boxed{
\sup_{\mathbf Y\in\widehat{\mathfrak H}}
\int_{|y|\le R}
|\nabla^mW_{\mathbf Y}|^2dy
\le C_{m,R}.
}
\]

But globally

\[
D_m(\theta_n)\to\infty.
\]

Therefore

\[
\boxed{
\int_{|y|>R}
|\nabla^mW(y,\theta_n)|^2dy
\to\infty
}
\]

for every fixed `R` and every fixed integer `m>=1`.

Thus each derivative order has its own remote mass escape.

---

## 7. Diagonal all-order formulation

For each fixed `M`, by choosing `n` sufficiently large we can make

\[
D_m(\theta_n)
\]

arbitrarily large simultaneously for all

\[
1\le m\le M.
\]

Indeed the single lower bound

\[
D_m(\theta_n)
\ge
P_n^m/Z_*^{m-1}
\]

holds for every `m`.

Therefore a diagonal subsequence gives the finite-order statement

\[
\boxed{
\forall M<\infty,
\quad
\min_{1\le m\le M}D_m(\theta_n)
\to\infty.
}
\]

This should be read carefully.

It does **not** assert that one fixed state has infinite derivatives of every order.

It asserts that along the sequence approaching the hard endpoint, every preassigned finite derivative hierarchy becomes arbitrarily large.

---

## 8. Define the all-order remote Sobolev cascade

Define

\[
\boxed{
H_{tail}^{remote-Sob}
}
\]

to mean that there exists a sequence `theta_n` such that for every fixed integer `m>=1`,

\[
D_m(\theta_n)\to\infty,
\]

and for every fixed spatial radius `R`,

\[
\int_{|y|>R}|\nabla^mW(y,\theta_n)|^2dy
\to\infty.
\]

Then M5-502--504 give

\[
\boxed{
H_{tail}^{remote-P}
\Longrightarrow
H_{tail}^{remote-F}
\Longrightarrow
H_{tail}^{remote-Sob}.
}
\]

The second implication is understood through the common unbounded-`P`, bounded-`E` sequence and the all-order Fourier moment inequality.

---

## 9. DSD audit: what this does not prove

The cascade must not be misread as a local singularity.

The following are **not** established:

1. one normalized spatial point at which `|grad^m W|` diverges;
2. one compact shell carrying all derivative orders simultaneously with nonvanishing amplitude;
3. a single recentered nontrivial ancient bubble at the intrinsic frequency scale;
4. a contradiction with smoothness at any finite similarity time;
5. convergence of the remote cascade to the M5-481 terminal Dirichlet genealogy.

Local smooth compactness explicitly rules out item 1 on every fixed normalized ball.

The correct description is

\[
\boxed{
\text{bounded local smoothness}
+
\text{bounded global }L^2\text{ vorticity}
+
\text{remote high-frequency occupancy}
}
\]

with the derivative hierarchy escaping spatially outward.

---

## 10. Relation to the M5-501 derivative ledger

M5-501 proposed two future routes:

- bounded `P`: continue to an `H`-evolution ledger;
- unbounded `P`: classify a tail/frequency escape.

M5-502--504 now complete the classification of the second route at the level of Sobolev moments:

\[
\boxed{
\sup P=\infty
\Longrightarrow
H_{tail}^{remote-Sob}.
}
\]

In particular, the unbounded branch cannot be closed by assuming that only palinstrophy grows while higher derivatives remain controlled.

That possibility is mathematically excluded by the moment inequality.

---

## 11. Updated projected-diffusion frontier

The current projected-diffusion component satisfies

\[
\boxed{
\mathcal C_{ax+projdiff}
\Longrightarrow
H_{tail}^{remote-Sob}
\lor
\mathcal C_{bounded-P}^{proj}.
}
\]

The bounded branch retains the quantitative M5-501 thresholds

\[
Z_*P_*\ge K_{EP},
\]

and

\[
P_*\ge P_{min}^{proj}(Z_*,h_{proj}).
\]

The unbounded branch is now a named, explicit endpoint:

\[
\boxed{
\text{all-order remote Sobolev cascade}.
}
\]

---

## 12. Highest-value next target

Two routes now remain sharply separated.

### Route A — bounded palinstrophy

Derive the similarity evolution of

\[
H=\|\Delta W\|_2^2
\]

and audit whether a bounded-`P` recurrent projected-diffusion component can keep `H` bounded without forcing a new threshold or a third-derivative escape.

### Route B — remote Sobolev cascade

Attempt to recenter at the intrinsic shell frequency scale

\[
\ell_n
\sim
\left(
\frac{E_{shell}}{P_{shell}}
\right)^{1/2}
\]

and determine whether the cascade yields

- a nontrivial secondary ancient bubble,
- diffuse frequency occupancy with vanishing local amplitude,
- or terminal-tail strengthening.

The next highest-value calculation is Route A because it attacks the remaining bounded derivative branch without requiring a new concentration compactness theorem.

---

## 13. Status

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
