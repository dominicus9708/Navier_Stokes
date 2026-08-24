# First-Hitting Analyticity Collapse of Natural-Scale Sparsity

Date: 2026-08-25

Status: **MAX-CENTERED SNAPSHOT GEOMETRY PROVED / EXTERNAL SPARSITY-CRITERION ACTIVATION NOT CLAIMED / GLOBAL REGULARITY NOT PROVED.**

This note audits the `S` branch of the residual genealogy at a normalized first-hitting maximum.

The relevant standard notion of linear sparseness is: a set `S` is linearly `delta`-sparse around `x0` at scale `R` if there exists a unit direction `d` such that its one-dimensional measure on the centered segment `(x0-Rd,x0+Rd)` is at most a `delta` fraction of the segment length.

The purpose here is not to invoke an external regularity theorem wholesale.  It is to determine whether a maximum-centered natural-scale sparsity escape can coexist with the repository's first-hitting analyticity corridor.

We work first in normalized variables

\[
\|\Omega_j(\cdot,0)\|_\infty=1,
\qquad
|\Omega_j(y_j,0)|=1,
\]

with a uniform first derivative bound

\[
\|\nabla\Omega_j(\cdot,0)\|_\infty\le C_1.
\]

---

## 1. Fixed intense-vorticity ball

Fix any threshold `a` with

\[
0<a<1.
\]

Set

\[
\boxed{
r_a:=\min\left\{r_{\rm an},\frac{1-a}{2C_1}\right\},}
\]

where `r_an` is any fixed radius inside the analytic core.

For `|y-y_j|<=r_a`,

\[
|\Omega_j(y,0)|
\ge
1-C_1|y-y_j|
\ge
\frac{1+a}{2}
>a.
\]

Therefore the superlevel set

\[
V_a^j:=\{y:|\Omega_j(y,0)|>a\}
\]

contains a fixed ball:

\[
\boxed{B_{r_a}(y_j)\subset V_a^j.}
\]

**Status: PROVED.**

---

## 2. Natural-scale volume sparsity is impossible at the maximum

For any `R>0`,

\[
\frac{|V_a^j\cap B_R(y_j)|}{|B_R|}
\ge
\min\left\{1,\left(\frac{r_a}{R}\right)^3\right\}.
\]

Hence for every fixed natural-scale upper radius `R0<infinity`,

\[
\boxed{
\inf_{0<R\le R_0}
\frac{|V_a^j\cap B_R(y_j)|}{|B_R|}
\ge
\delta_{\rm vol}(a,R_0)>0,
}
\]

uniformly in `j`.

Thus a maximum-centered intense-vorticity set cannot become arbitrarily volume-sparse on scales comparable to the natural first-hitting radius.

In physical variables this means that if

\[
r_j=\left(\frac\nu{W_j}\right)^{1/2},
\]

then

\[
B_{c_ar_j}(x_j)\subset\{|\omega|>aW_j\}
\]

at the first-hitting snapshot, with `c_a>0` independent of `j`.

**Status: PROVED.**

---

## 3. Centered linear sparsity has a positive lower floor

Let `e` be any unit vector and consider the centered segment

\[
L_{R,e}
:=
\{y_j+se:-R<s<R\}.
\]

Because `B_{r_a}(y_j)` is contained in `V_a^j`,

\[
|V_a^j\cap L_{R,e}|_1
\ge
2\min\{R,r_a\}.
\]

Therefore

\[
\boxed{
\frac{|V_a^j\cap L_{R,e}|_1}{2R}
\ge
\min\left\{1,\frac{r_a}{R}\right\}.
}
\]

In particular, for all `0<R<=R0`,

\[
\boxed{
\frac{|V_a^j\cap L_{R,e}|_1}{2R}
\ge
\delta_{\rm line}(a,R_0)
:=
\min\left\{1,\frac{r_a}{R_0}\right\}>0
}
\]

for **every** direction `e`.

Hence the set is not linearly `delta`-sparse around the maximum at any natural scale `R<=R0` whenever

\[
\delta<\delta_{\rm line}(a,R_0).
\]

This is stronger than a volume statement because it excludes arbitrarily thin center-line occupancy in every direction.

**Status: PROVED for the magnitude superlevel set centered at the max-vorticity point.**

---

## 4. Signed-component version

Some geometric criteria are formulated using superlevel sets of positive or negative vorticity components rather than `|Omega|`.

At `y_j`, choose a Cartesian component `i` and sign `sigma in {+1,-1}` so that

\[
\sigma\Omega_{j,i}(y_j,0)
\ge
\frac1{\sqrt3}.
\]

Fix any threshold

\[
0<a_c<\frac1{\sqrt3}.
\]

Since

\[
\|\nabla\Omega_{j,i}\|_\infty\le C_1,
\]

there is a fixed radius

\[
r_{a_c}^{\rm comp}
\ge
c\frac{1/\sqrt3-a_c}{C_1}
\]

on which

\[
\sigma\Omega_{j,i}>a_c.
\]

Thus the same volume and centered-line occupancy floors hold for a suitable signed component superlevel set, provided the threshold is below the fixed center-component amplitude.

**Status: PROVED.**

---

## 5. High-low segregation forces gradient-magnitude cost

Fix thresholds

\[
0\le b<a<1
\]

and a fixed natural-scale ball `B_R(y_j)`, `R=O(1)`.

Let

\[
H_a:=\{|\Omega_j|\ge a\}\cap B_R,
\qquad
L_b:=\{|\Omega_j|\le b\}\cap B_R,
\]

with volume fractions

\[
\rho_H:=\frac{|H_a|}{|B_R|},
\qquad
\rho_L:=\frac{|L_b|}{|B_R|}.
\]

The occupied analytic core gives

\[
\rho_H\ge c_{a,R}>0.
\]

For `f=|Omega_j|`, the pairwise variance identity and Poincare inequality give

\[
\fint_{B_R}|f-f_{B_R}|^2
\ge
c\rho_H\rho_L(a-b)^2,
\]

and

\[
\fint_{B_R}|f-f_{B_R}|^2
\le
CR^2\fint_{B_R}|\nabla f|^2.
\]

Therefore

\[
\boxed{
R^2\fint_{B_R}|\nabla|\Omega_j||^2
\ge
c\rho_H\rho_L(a-b)^2.
}
\]

Since

\[
|\nabla\Omega|^2
=|\nabla|\Omega||^2+|\Omega|^2|\nabla\xi|^2,
\]

any fixed low-vorticity fraction `rho_L>=lambda>0` forces a fixed normalized palinstrophy amount.

In physical variables, with `d=Rr_j`, this yields

\[
\boxed{
\frac{d^3}{\nu^2}
\int_{B_d}|\nabla\omega|^2dx
\ge
c_{a,b,R,\lambda}>0.
}
\]

Thus genuine high-low segregation rejoins the `P` branch.

**Status: PROVED.**

---

## 6. If low-vorticity volume disappears, the core becomes dense and pays first-order cost

Suppose instead

\[
\rho_L\to0
\]

for a fixed threshold `b>0` on a fixed natural ball.

Then on an asymptotically full fraction of the ball,

\[
|\Omega_j|>b.
\]

Therefore

\[
\int_{B_R}|\Omega_j|^2dy
\ge
b^2(1-\rho_L)|B_R|.
\]

For divergence-free velocity in the whole space the pointwise inequality

\[
|\Omega|^2\le2|\nabla U|^2
\]

gives

\[
\boxed{
R\int_{B_R}|\nabla U_j|^2dy
\ge
c_{b,R}>0.
}
\]

Equivalently, in physical variables,

\[
\boxed{
\frac{d}{\nu^2}
\int_{B_d}|\nabla u|^2dx
\ge
c_{b,R}>0.
}
\]

Thus disappearance of the low-vorticity phase does not create a sparse escape; it produces an ultra-dense high-vorticity core with first-order occupied gradient cost.

**Status: PROVED.**

---

## 7. Natural-scale S branch collapses at a maximum-centered snapshot

Combining the preceding cases:

1. arbitrarily small volume occupancy of the intense set is excluded;
2. arbitrarily small centered-line occupancy is excluded;
3. coexistence of a fixed low-vorticity phase forces palinstrophy (`P`);
4. disappearance of the low-vorticity phase forces a dense first-order gradient cost.

Hence, at a maximum-centered first-hitting snapshot on a fixed natural scale,

\[
\boxed{
S_{\rm natural,max}
\Longrightarrow
P
\quad\lor\quad
\text{occupied first-order cost}.
}
\]

Since the snapshot P branch was already reduced by first-hitting analyticity to an occupied fixed-scale packet or far strain,

\[
\boxed{
S_{\rm natural,max}
\Longrightarrow
\text{occupied first-order packet}
\quad\lor\quad
F_{\rm far\ strain}.
}
\]

**Status: PROVED in the stated snapshot scope.**

---

## 8. What S can still mean

The calculation does **not** eliminate all possible geometric sparseness.

An S escape can still survive if the relevant geometry is

- centered away from the maximum-vorticity point,
- measured at scales much larger than the natural radius,
- measured at a different time than the first-hitting snapshot,
- or defined with a superlevel threshold not covered by the fixed occupied-core threshold.

Those are not maximum-centered natural-scale volume/line sparsity.  They are a non-tight spatial/temporal genealogy problem.

In particular, this note does not claim that the hypotheses of the external geometric regularity criterion are automatically satisfied.  Matching its exact time window, threshold, and universal constants is a separate obligation.

---

## 9. Audit table

| Claim | Status |
|---|---|
| Fixed intense-vorticity ball at normalized first-hitting maximum | **PROVED** |
| Natural-scale volume sparsity at the maximum can tend to zero | **FALSE** |
| Centered-line occupancy can tend to zero on every fixed natural-scale range | **FALSE** |
| Suitable signed component also has a fixed occupied ball below a fixed threshold | **PROVED** |
| Fixed high-low coexistence forces normalized gradient-magnitude/palinstrophy cost | **PROVED** |
| Vanishing low phase forces a dense first-order gradient cost | **PROVED** |
| Natural maximum-centered S branch reduces to P or occupied first-order cost | **PROVED** |
| All possible non-centered / larger-scale / later-time sparsity is excluded | **NOT DERIVED** |
| External geometric sparseness regularity theorem is automatically activated | **NOT DERIVED** |
| Global regularity | **UNPROVED** |

---

## 10. Updated local snapshot frontier

At a normalized maximum-centered first-hitting snapshot, the four former local residual labels

\[
F/S/P/N
\]

have now collapsed substantially:

\[
\boxed{
S\rightsquigarrow P\text{ or occupied cost},
\qquad
P\rightsquigarrow F\text{ or occupied cost},
\qquad
N_{\rm fixed\ order}\text{ is bounded by analyticity}.
}
\]

The genuinely surviving local obstructions are therefore

\[
\boxed{
F_{\rm far\ strain},
\qquad
\text{non-tight geometry/scale escape},
\qquad
\text{order-to-infinity derivative escape},
}
\]

plus the favorable branch where an occupied first-order packet pays return/dissipation cost.

The next proof step should merge these reductions into a single updated genealogy frontier and then attack the remaining non-tight scale-identification bridge.