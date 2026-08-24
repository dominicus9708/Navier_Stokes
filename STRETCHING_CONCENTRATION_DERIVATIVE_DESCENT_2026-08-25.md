# Stretching Concentration / Derivative Descent — 2026-08-25

## Status

**NEW CALCULATION — RIGOROUS CONCENTRATION DICHOTOMY; GLOBAL REGULARITY NOT PROVED.**

This note continues `GALILEAN_LOCAL_ENSTROPHY_GENEALOGY_GATE_2026-08-25.md` at its remaining stretching branch.

The unresolved certificate there is

\[
R\|\nabla u\|_{L^3(B_{2R})}
\gtrsim \nu
\]

without an already-large physical-scale `L^2` gradient cost.

The purpose here is to show that this cannot remain an unstructured residual: if the `L^2` cost is small, the stretching must become pointwise concentrated, and if that concentration is not spatially occupied it forces the next derivative to rise.

---

## 1. Critical first-derivative quantities

At a fixed time and center define

\[
g_R
:=
R\|\nabla u\|_{L^3(B_{2R})},
\]

\[
G_R
:=
R\|\nabla u\|_{L^2(B_{2R})}^2,
\]

and

\[
H_R
:=
\frac{R^2}{\nu}
\|\nabla u\|_{L^\infty(B_{2R})}.
\]

All three normalized quantities

\[
\frac{g_R}{\nu},
\qquad
\frac{G_R}{\nu^2},
\qquad
H_R
\]

are invariant under the Navier-Stokes scaling.

---

## 2. Exact interpolation gate

The elementary interpolation inequality

\[
\|f\|_3^3
\le
\|f\|_\infty\|f\|_2^2
\]

with `f=grad u` gives

\[
\boxed{
g_R^3\le\nu H_R G_R.}
\]

Equivalently,

\[
\boxed{
\frac{G_R}{\nu^2}
\ge
\frac{(g_R/\nu)^3}{H_R}.
}
\]

Thus if the stretching branch satisfies

\[
g_R\ge\gamma\nu,
\]

then for any `Gamma>0`,

\[
\boxed{
\frac{G_R}{\nu^2}<\Gamma
\quad\Longrightarrow\quad
H_R>\frac{\gamma^3}{\Gamma}.
}
\]

Hence critical `L^3` stretching that avoids `L^2` gradient cost must become pointwise concentrated.

Status: **PROVED.**

---

## 3. General derivative normalization

For derivative order `k>=1`, let

\[
M_{k,R}
:=
\|\nabla^k u\|_{L^\infty(B_R(X))},
\]

and define the critical normalized amplitude

\[
\boxed{
H_{k,R}
:=
\frac{R^{k+1}}{\nu}M_{k,R}.
}
\]

For the next derivative use the enlarged ball

\[
L_{k+1,R}
:=
\frac{R^{k+2}}{\nu}
\|\nabla^{k+1}u\|_{L^\infty(B_{2R}(X))}.
\]

The critical derivative-order `L^2` cost at radius `r` is

\[
\boxed{
\mathcal G_{k,r}(x)
:=
r^{2k-1}
\int_{B_r(x)}|\nabla^k u|^2dy.
}
\]

For `k=1` this reduces to the physical-scale gradient cost.

---

## 4. Derivative persistence-radius lemma

Let `x_* in B_R(X)` be a point at which

\[
|\nabla^k u(x_*)|=M_{k,R}.
\]

Smoothness and the mean-value estimate imply

\[
\big||\nabla^k u(x)|-|\nabla^k u(x_*)|\big|
\le
C_k
\|\nabla^{k+1}u\|_{L^\infty(B_{2R})}
|x-x_*|.
\]

Choose

\[
\rho
=
\min\left\{
\frac R2,
\frac{M_{k,R}}
{2C_k\|\nabla^{k+1}u\|_{L^\infty(B_{2R})}}
\right\}.
\]

Then `B_rho(x_*) subset B_{2R}(X)` and

\[
|\nabla^k u(x)|
\ge
\frac12M_{k,R}
\qquad
(x\in B_\rho(x_*)).
\]

Therefore

\[
\mathcal G_{k,\rho}(x_*)
\ge
c_k\rho^{2k+2}M_{k,R}^2.
\]

In normalized form,

\[
\boxed{
\frac{\mathcal G_{k,\rho}(x_*)}{\nu^2}
\ge
c_k H_{k,R}^2
\min\left\{
1,
\left(\frac{H_{k,R}}{L_{k+1,R}}\right)^{2k+2}
\right\}.
}
\]

Status: **PROVED.**

---

## 5. Consequence: cost or next-derivative escalation

Suppose a derivative-order amplitude `H_{k,R}` is large but every persistence-radius cost produced above obeys

\[
\frac{\mathcal G_{k,\rho}(x_*)}{\nu^2}
<\varepsilon_k.
\]

If the first branch of the minimum were active, one would have

\[
\varepsilon_k
>
c_k H_{k,R}^2.
\]

Thus for a genuinely large `H_{k,R}` the only possible escape is the derivative-concentration branch. Rearranging gives

\[
\boxed{
L_{k+1,R}
\ge
c_k'
\varepsilon_k^{-1/(2k+2)}
H_{k,R}^{(k+2)/(k+1)}.
}
\]

So avoidance of derivative-order `L^2` occupancy forces a superlinear rise of the next normalized derivative amplitude.

For `k=1`,

\[
\boxed{
L_{2,R}
\gtrsim
\varepsilon_1^{-1/4}H_{1,R}^{3/2}.
}
\]

Status: **PROVED CONDITIONAL ON SMALL DESCENDED COST.**

---

## 6. Application to the local-enstrophy stretching branch

From the previous genealogy gate, substantial stretching on a parabolic interval implies either

\[
R\|\omega\|_{L^3}
\gtrsim\nu
\]

or

\[
g_R=R\|\nabla u\|_3
\gtrsim\nu.
\]

In the second case, the interpolation gate now yields

\[
\boxed{
\text{critical }L^3\text{ stretching}
\Longrightarrow
\text{large }G_R
\quad\lor\quad
\text{large }H_R.
}
\]

If `H_R` is large, the persistence-radius lemma yields

\[
\boxed{
\text{large }H_R
\Longrightarrow
\text{smaller-scale }L^2\text{ gradient cost}
\quad\lor\quad
\text{large normalized Hessian amplitude}.
}
\]

The same geometric mechanism is available at every higher derivative order.

Therefore the stretching branch is no longer a single unresolved object; it is forced into either an occupied derivative cost or a derivative-amplitude escalation chain.

---

## 7. What this does and does not close

This calculation proves that arbitrarily thin spatial concentration is not a free escape: avoiding `L^2` occupancy at one derivative order must be paid for by growth of the next derivative.

It does **not** yet prove that the resulting derivative escalation is impossible near a hypothetical singular time.

A smooth pre-singular Navier-Stokes solution may have an analytic radius shrinking toward zero, and a rapidly rising derivative hierarchy is not contradicted merely by smoothness at each earlier time.

Thus the next closure problem is to compare the forced escalation

\[
H_{k+1}
\gtrsim
\varepsilon_k^{-1/(2k+2)}
H_k^{(k+2)/(k+1)}
\]

against the repository's factorially normalized derivative/analyticity track and determine whether an infinite escape chain is compatible with the available parabolic time and dissipation budgets.

---

## 8. Audit table

| Claim | Status |
|---|---|
| `g_R^3 <= nu H_R G_R` | **PROVED** |
| Large critical `L^3` stretching with bounded `H_R` forces `L^2` gradient cost | **PROVED** |
| Large `L^3` stretching with small `G_R` forces large normalized pointwise gradient | **PROVED** |
| Large normalized `k`-th derivative either occupies a smaller ball or forces the `(k+1)`-st derivative upward | **PROVED** |
| Small descended derivative cost forces the displayed superlinear next-derivative escalation | **PROVED CONDITIONAL** |
| The escalation contradicts smoothness by itself | **FALSE** |
| The escalation contradicts the known analyticity radius near a hypothetical singularity | **NOT DERIVED** |
| Global regularity | **UNPROVED** |

---

## 9. Updated local genealogy frontier

The historical local branch is now reduced to

\[
\boxed{
\begin{aligned}
\text{current gradient concentration}
\Longrightarrow {}&
\text{historical shell }L^2\text{ cost}\\
&\lor\ \text{critical }L^3\text{ vorticity}\\
&\lor\ \text{occupied stretching }L^2\text{ cost}\\
&\lor\ \text{derivative-amplitude escalation chain}.
\end{aligned}
}
\]

The last line is the new active escape branch.

The next calculation should therefore join this forced derivative-amplitude escalation to the existing factorial derivative Cauchy-convolution / affine-free remote-pressure track, rather than returning to the already-audited absolute local-energy route.