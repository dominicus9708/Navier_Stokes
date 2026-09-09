# DSD M17-456 — Global sign compensation does not localize, and compact coefficients force a moderate negative weighted mass or an explicit decompactification

Date: 2026-09-09  
Canonical ID: **M17-456**

Status: **ACTIVE GLOBAL-TO-LOCAL FIREWALL / NEGATIVE-COMPENSATION EXTRACTION THEOREM**

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Input from M17-455

On the whole-space exact CE-H branch,

\[
P_R=K_{-,R}-K_{+,R},
\qquad
K_{-,R}\ge K_{+,R},
\]

where

\[
K_{-,R}=\int (\kappa_R)_-\rho_R^2dx,
\qquad
K_{+,R}=\int (\kappa_R)_+\rho_R^2dx.
\]

For a baseline-size positive-kappa diffuse carrier, M17-455 gives

\[
\boxed{K_{-,R}\ge c_K>0}
\]

uniformly on the retained record state.

The question is what this actually forces geometrically.

## 2. Global-to-local firewall

Let `N_R` be any chosen neighborhood of the positive diffuse carrier, for example a fixed multiple of its mesoscopic transverse participation radius.

Split

\[
K_{-,R}
=
K_{-,R}^{loc}
+
K_{-,R}^{far},
\]

with

\[
K_{-,R}^{loc}
:=
\int_{N_R}(\kappa_R)_-\rho_R^2dx,
\]

\[
K_{-,R}^{far}
:=
\int_{\mathbb R^3\setminus N_R}(\kappa_R)_-\rho_R^2dx.
\]

For any fixed `0<theta<1`,

\[
\boxed{
K_{-,R}^{loc}\ge\theta c_K
\quad\text{or}\quad
K_{-,R}^{far}\ge(1-\theta)c_K.
}
\]

This tautological split is mathematically important: the exact CE-H sign identity is global and gives no spatial localization of the compensating negative mass.

Therefore one must keep

\[
\boxed{G_{remote\ negative\ compensation}}
\]

as an explicit branch unless an independent localization theorem is supplied.

M17-450--454 transverse geometry may be applied directly only to the local branch.

## 3. Coefficient-magnitude decomposition

Assume the descendant normalized coefficient is compact on the retained branch:

\[
\boxed{|\kappa_R|\le K_*<\infty.}
\]

The uniform record enstrophy bound gives

\[
\boxed{E_R:=\int\rho_R^2dx\le E_I.}
\]

Choose

\[
\boxed{
\kappa_0:=\frac{c_K}{4E_I}.
}
\]

Decompose the negative coefficient set into

\[
Z_R:=\{0<(\kappa_R)_-<\kappa_0\},
\]

and

\[
M_R:=\{\kappa_0\le(\kappa_R)_-\le K_*\}.
\]

The near-zero weighted contribution satisfies

\[
\int_{Z_R}(\kappa_R)_-\rho_R^2dx
\le
\kappa_0E_I
=\frac14c_K.
\]

Hence if `K_- >= c_K`,

\[
\boxed{
\int_{M_R}(\kappa_R)_-\rho_R^2dx
\ge
\frac34c_K.
}
\]

Up to harmless adjustment of constants, a fixed fraction of the compensating weighted mass lies in a **moderate negative coefficient band** bounded away from both zero and infinity.

If the coefficient ceiling `K_*` fails, classify that state instead as normalized coefficient decompactification.

## 4. Fixed enstrophy mass in the moderate band

Because `(kappa_R)_- <= K_*` on `M_R`,

\[
\int_{M_R}(\kappa_R)_-\rho_R^2dx
\le
K_*\int_{M_R}\rho_R^2dx.
\]

Therefore

\[
\boxed{
E_{M,R}
:=
\int_{M_R}\rho_R^2dx
\ge
\frac{3c_K}{4K_*}
=:e_M>0.
}
\]

Thus, under coefficient compactness, the global sign compensation is not merely coefficient mass: it contains a fixed amount of actual vorticity enstrophy on a uniformly negative coefficient band.

## 5. Fixed raw-H2 snapshot charge

On `M_R`, `(kappa_R)_- >= kappa_0`. Hence

\[
H_{M,R}
:=
\int_{M_R}\kappa_R^2\rho_R^2dx
\ge
\kappa_0
\int_{M_R}(\kappa_R)_-\rho_R^2dx.
\]

Therefore

\[
\boxed{
H_{M,R}
\ge
\frac34\kappa_0c_K
=:h_M>0.
}
\]

This does not by itself contradict the `R^-3` raw-H2 ancestry ledger; M17-453 already explains that a fixed snapshot raw-H2 charge persisting for `O(R^2)` own-time units costs only `O(R^-1)` ancestrally.

The point is to isolate a robust moderate-negative population for the geometry audit.

## 6. Thickness decomposition of the moderate band

Let

\[
d_R(x)
:=
\operatorname{dist}\bigl(x,\{\kappa_R\ge-\kappa_0/2\}\bigr)
\]

for `x in M_R`.

For a thickness parameter `L>0`, define

\[
M_R^{thick}(L)
:=
\{x\in M_R:d_R(x)\ge L\},
\]

\[
M_R^{thin}(L)
:=M_R\setminus M_R^{thick}(L).
\]

Then for every `L`,

\[
E_{M,R}
=E_{thick,R}(L)+E_{thin,R}(L).
\]

Hence for any fixed `0<eta<1`,

\[
\boxed{
E_{thick,R}(L)\ge\eta e_M
\quad\text{or}\quad
E_{thin,R}(L)\ge(1-\eta)e_M.
}
\]

If there exists `L_R -> infinity` with a fixed fraction of moderate-negative enstrophy in `M_R^{thick}(L_R)`, M17-454 applies and persistent positive-time residence is forbidden by the palinstrophy ancestry ledger.

Therefore a surviving compact-coefficient local compensation branch must satisfy the boundary-layer confinement property

\[
\boxed{
\forall\eta>0\;\exists L_\eta<\infty
\text{ such that, along the survivor, almost all moderate-negative enstrophy lies within }L_\eta
\text{ own-scales of the }\kappa\approx0\text{ interface.}
}
\]

This is the canonical meaning of `thin/localized negative compensation`.

## 7. Gradient-compactness consequence

Suppose also

\[
\boxed{|\nabla\kappa_R|\le G_*}
\]

in normalized variables.

A point with `(kappa_R)_- >= kappa_0` must then obey

\[
\boxed{
d_R(x)\ge\frac{\kappa_0}{2G_*}.}
\]

Thus the moderate-negative layer cannot collapse below a fixed own-scale thickness unless normalized coefficient-gradient compactness fails.

This does **not** make it mesoscopically thick; it only removes arbitrarily sub-own-scale lamination under a gradient ceiling.

Accordingly the surviving local branch is an `O(1)`-thick boundary/interface layer, not a vanishing-thickness layer, unless `|nabla kappa|` decompactifies.

## 8. Canonical negative-compensation split

Combining Sections 2--7,

\[
\boxed{
\begin{aligned}
H_{K_-\ge c_K}
\Longrightarrow{}&
G_{remote\ negative\ compensation}\\
&\lor G_{coefficient\ magnitude\ decompactification}\\
&\lor H_{moderate\ negative\ weighted\ mass\ with\ fixed\ enstrophy}.
\end{aligned}
}
\]

For the local moderate branch,

\[
\boxed{
\begin{aligned}
H_{moderate\ local\ negative\ mass}
\Longrightarrow{}&
H_{mesoscopic\ sign\ thickness}\Rightarrow\text{M17-454 contradiction if persistent}\\
&\lor G_{O(1)\text{-}thick\ zero/interface\ boundary\ layer}\\
&\lor G_{coefficient\ gradient/high\text{-}jet\ decompactification}\\
&\lor G_{time/chart/interface/genealogy\ loss}.
\end{aligned}
}
\]

The vague phrase `thin negative compensation` is therefore sharpened to either a remote cluster, an own-scale-thick zero-interface layer, or an explicit coefficient/geometric loss.

## 9. What is not proved

M17-456 does not prove that the moderate negative mass lies near the positive carrier.

It also does not prove that an `O(1)`-thick negative interface layer generates enough palinstrophy to contradict M17-307; M17-428 remains the local boundary firewall at exactly that thickness.

A further transition estimate is required to determine whether a bounded-width moderate-negative-to-zero layer must pay through vorticity-amplitude gradients, coefficient gradients, zero-corridor raw-H2, or local-frequency decompactification.

## 10. Next target

The next module should use a bounded-length path from a moderate negative point to the `kappa=0` interface.

Along such a path,

\[
\partial_s(\rho\kappa)
=\kappa\partial_s\rho+\rho\partial_s\kappa.
\]

This suggests a transition dichotomy between

\[
\kappa^2|\nabla\rho|^2
\]

and

\[
\rho^2|\nabla\kappa|^2,
\]

i.e. palinstrophy/amplitude-gradient payment versus the M17-445 coefficient-gradient payment.

## 11. Audit verdict

**PASS — the global sign balance has been localized only as far as the mathematics permits.**

Under coefficient compactness it forces a fixed moderate-negative weighted and enstrophy mass, but that mass may be remote. If local, persistent mesoscopic sign thickness is closed by M17-454, leaving an own-scale-thick zero-interface boundary layer or explicit decompactification as the narrow branch.

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
