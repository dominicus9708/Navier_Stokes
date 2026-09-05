# DSD M17-205 — Fixed-lag material shell enstrophy is comparable to a finite current-shell neighborhood on the bounded-kappa remote branch

Date: 2026-09-06  
Canonical ID: **M17-205**

Status: **GLOBAL MULTIPLICITY BRIDGE / INSTEAD OF FOLLOWING INDIVIDUAL PACKETS, USE THE EXACT CE-H MATERIAL AMPLITUDE LAW AND THE JACOBIAN OF THE SIMILARITY MATERIAL FLOW. FOR ANY MATERIAL SET, ITS ENSTROPHY CHANGES BY THE MULTIPLICATIVE FACTOR `exp int(2 sigma + 2 kappa - 1/2)`. ON A COMPACT STRAIN HULL AND BOUNDED-KAPPA FIXED-LAG CORRIDOR THIS FACTOR IS UNIFORMLY ABOVE AND BELOW. REMOTE TYPE-I VELOCITY ALSO IMPLIES THAT A FIXED-SHAPE DYADIC ANNULUS IS CARRIED, OVER FIXED LAG, INTO A FIXED-FACTOR ANNULUS WITH ONLY FINITELY MANY DYADIC NEIGHBORS. HENCE ANCESTOR SHELL ENSTROPHY IS CONTROLLED BY A FINITE CURRENT NEIGHBORHOOD. BACKWARD MASS EXPLOSION CAN SURVIVE ONLY THROUGH FAILURE OF DYADIC NEIGHBOR COMPARABILITY, UNBOUNDED KAPPA, OR ANOTHER HARD EXIT. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Material enstrophy density

CE-H gives

\[
D_B\rho=(\sigma+\kappa-1)\rho
\]

and

\[
\nabla\cdot B=\frac32.
\]

Let `Phi_T` be the material flow map of `B` from time `theta-T` to `theta`.
Its Jacobian obeys

\[
\boxed{
\det D\Phi_T=e^{3T/2}.
}
\]

Along a trajectory,

\[
\rho_+^2
=\rho_-^2
\exp\left[
2\int_{\theta-T}^{\theta}(\sigma+\kappa-1)d\tau
\right].
\]

Therefore, for any material set `A_-`,

\[
\boxed{
\int_{\Phi_T(A_-)}\rho_+^2dy
=
\int_{A_-}\rho_-^2
\exp\left[
\int_{\theta-T}^{\theta}
\left(2\sigma+2\kappa-\frac12\right)d\tau
\right]dy.
}
\]

---

## 2. Uniform fixed-lag comparability

Assume on the material corridor

\[
|\sigma|\le S_*,
\qquad
|\kappa|\le K_*.
\]

The strain bound is inherited from the compact smooth hull; bounded `kappa` is the current branch assumption.

Then, for fixed `T`,

\[
\boxed{
e^{-C_T}
\int_{A_-}\rho_-^2dy
\le
\int_{\Phi_T(A_-)}\rho_+^2dy
\le
e^{C_T}
\int_{A_-}\rho_-^2dy,
}
\]

where one may take

\[
C_T=T(2S_*+2K_*+1/2).
\]

Thus no fixed-lag material collection of vorticity can lose or gain an unbounded `L2` factor while both `sigma` and `kappa` remain bounded.

---

## 3. Radial motion of remote material points

On the remote Type-I branch,

\[
|U(y,\theta)|\le\frac{A_0}{1+|y|}.
\]

For a material trajectory,

\[
\dot y=\frac12y+U(y,\theta).
\]

Hence

\[
\boxed{
\frac d{d\theta}|y|^2
=|y|^2+2y\cdot U.
}
\]

On a remote annulus, `|y dot U|<=A0`, so solving this scalar differential inequality over fixed `T` gives

\[
\boxed{
|y(\theta)|^2
=e^T|y(\theta-T)|^2+O_T(1).
}
\]

Thus for `R->infinity`,

\[
\boxed{
|y(\theta)|
=e^{T/2}|y(\theta-T)|\,[1+O_T(R^{-2})].
}
\]

---

## 4. Dyadic shell image

Let

\[
A_R^-:=\{c_1R<|y|<c_2R\}
\]

be a fixed-shape ancestor annulus.
For sufficiently large `R`, its material image is contained in a current annulus

\[
\Phi_T(A_R^-)
\subset
\{c_1' e^{T/2}R<|y|<c_2'e^{T/2}R\},
\]

with fixed constants depending only on `T,c1,c2,A0`.

Therefore there exist an integer shift `s_T` and finite integer width `M_T` such that the image is contained in the union of current dyadic shells

\[
\boxed{
\Phi_T(A_j^-)
\subset
\bigcup_{|m|\le M_T}A_{j+s_T+m}^{+}.
}
\]

---

## 5. Shell-mass transfer inequality

Let

\[
E_j^-(\theta-T)
:=\int_{A_j^-}|W|^2dy.
\]

Let `E_l^+(theta)` denote the corresponding current enlarged-shell masses.
Sections 2--4 imply

\[
\boxed{
E_j^-(\theta-T)
\le
C_T
\sum_{|m|\le M_T}
E_{j+s_T+m}^+(\theta).
}
\]

A reverse inequality holds for the material image with the inverse fixed-lag flow, but the upper estimate above is the one needed for the backward-mass gate.

---

## 6. Consequence for M17-162

M17-162 requires a subsequence with

\[
\frac{E_j^-(\theta-T)}{a_j^2}\to\infty.
\]

M17-205 shows that this can occur on the bounded-kappa compact branch only if

\[
\frac{\sum_{|m|\le M_T}E_{j+s_T+m}^+(\theta)}{a_j^2}
\to\infty.
\]

Thus the mass explosion is not created by hidden ancestor packet multiplicity alone. It must already be visible as large **current neighboring-shell occupancy** unless another branch assumption fails.

This converts the multiplicity problem into a finite-neighborhood dyadic packing problem.

---

## 7. DSD audit

- The set `A_-` is materialized before applying the enstrophy formula; an Eulerian shell is not silently treated as material.
- The shell-image statement uses only fixed finite lag and remote Type-I velocity.
- No quiet-strain smallness is required here; only the compact uniform bound on `sigma`.
- If `kappa` becomes unbounded on the material corridor, the estimate is routed to the explicit `G_{kappa,infinity}` branch.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
