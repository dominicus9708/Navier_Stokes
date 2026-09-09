# DSD M17-457 — A bounded-width negative-to-zero interface forces a palinstrophy-or-coefficient-gradient payment via Friedrichs on `rho kappa_-`

Date: 2026-09-09  
Canonical ID: **M17-457**

Status: **ACTIVE INTERFACE-PAYER DICHOTOMY / M17-456 LOCAL-THIN BRANCH REFINEMENT**

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Input from M17-456

On the local compact-coefficient compensation branch, M17-456 extracts a moderate negative band with

\[
\kappa_0\le\kappa_-\le K_*,
\]

and fixed enstrophy mass

\[
\boxed{
\int_{M_R}\rho_R^2dx\ge e_M>0.
}
\]

If a fixed fraction of this mass becomes mesoscopically thick, M17-454 closes persistent residence by palinstrophy.

The remaining local branch is therefore an own-scale/bounded-width negative-to-zero interface layer.

## 2. Regular bounded-width interface domain

Let `D_R` be a connected negative-coefficient transition component satisfying:

1. `kappa_R<0` in `D_R`;
2. a nontrivial boundary portion `Gamma_{0,R}` lies on the zero level `kappa_R=0`;
3. the moderate-negative subset inside `D_R` carries
   \[
   \int_{D_R\cap\{\kappa_-\ge\kappa_0\}}\rho_R^2dx\ge e_0>0;
   \]
4. `D_R` has uniformly bounded transverse width and a uniform Dirichlet/Friedrichs constant relative to `Gamma_{0,R}`:
   \[
   \boxed{
   \int_{D_R}|f|^2dx
   \le C_F
   \int_{D_R}|\nabla f|^2dx
   }
   \]
   for scalar `f` whose trace vanishes on `Gamma_{0,R}`, with `C_F<=C_*` independent of `R`.

Failure of item 4 is retained as an interface-geometry/spectral decompactification branch rather than silently absorbed.

## 3. The canonical transition scalar

Define

\[
\boxed{
u_R:=\rho_R(\kappa_R)_-.}
\]

Because `kappa_R=0` on `Gamma_{0,R}`, `u_R` has zero trace there.

On the moderate-negative subset,

\[
u_R^2
=\rho_R^2\kappa_-^2
\ge
\kappa_0^2\rho_R^2.
\]

Hence

\[
\boxed{
\int_{D_R}u_R^2dx
\ge
\kappa_0^2e_0
=:c_u>0.
}
\]

## 4. Friedrichs lower bound

Apply the uniform Dirichlet/Friedrichs inequality:

\[
\int_{D_R}|\nabla u_R|^2dx
\ge
\frac1{C_F}
\int_{D_R}u_R^2dx.
\]

Therefore

\[
\boxed{
\int_{D_R}|\nabla(\rho_R\kappa_-)|^2dx
\ge c_F>0.
}
\]

This is a fixed transition charge independent of record factor.

## 5. Split the transition derivative

Almost everywhere inside the negative region,

\[
\nabla(\rho\kappa_-)
=\kappa_-\nabla\rho+\rho\nabla\kappa_-.
\]

Thus

\[
|\nabla(\rho\kappa_-)|^2
\le
2\kappa_-^2|\nabla\rho|^2
+2\rho^2|\nabla\kappa|^2.
\]

Since `kappa_-<=K_*`,

\[
\boxed{
 c_F
\le
2K_*^2
\int_{D_R}|\nabla\rho_R|^2dx
+
2\int_{D_R}\rho_R^2|\nabla\kappa_R|^2dx.
}
\]

Using

\[
|\nabla\rho|=|\nabla|\Omega||\le|\nabla\Omega|,
\]

we obtain the canonical payer dichotomy

\[
\boxed{
 c_F
\le
C_P P_{D,R}+C_G G_{D,R},
}
\]

where

\[
P_{D,R}:=\int_{D_R}|\nabla\Omega_R|^2dx,
\]

\[
G_{D,R}:=\int_{D_R}\rho_R^2|\nabla\kappa_R|^2dx.
\]

Hence at every retained regular transition time,

\[
\boxed{
P_{D,R}\ge c_P>0
\quad\text{or}\quad
G_{D,R}\ge c_G>0
}
\]

with constants depending only on the compact interface parameters.

## 6. Spacetime dichotomy over a parent-time record

Let the local moderate-negative transition state occupy `beta_R R^2` own-time units inside one parent-time record, with `beta_R` the parent-time fraction.

Integrating Section 5 over those times gives

\[
\boxed{
\int P_{D,R}dt
+
\int G_{D,R}dt
\gtrsim
c\beta_RR^2.
}
\]

Therefore at least one of

\[
\boxed{
\int P_{D,R}dt
\gtrsim
c\beta_RR^2
}
\]

or

\[
\boxed{
\int G_{D,R}dt
\gtrsim
c\beta_RR^2
}
\]

holds up to a factor of two.

## 7. Ancestral consequences are strongly asymmetric

### Palinstrophy-dominated transition

M17-307 uses ancestry weight `R^-1`, so

\[
\boxed{
\mathcal P_{anc,R}
\gtrsim
c\beta_RR.
}
\]

Persistent positive `beta_R` is impossible across growing geometric records.

### Coefficient-gradient-dominated transition

M17-445 uses ancestry weight `R^-5`, so the same `O(R^2)` spacetime charge gives only

\[
\boxed{
\mathcal G_{anc,R}
\gtrsim
c\beta_RR^{-3}.
}
\]

This is summable on geometric records.

Therefore the bounded-width local negative-interface survivor is forced toward a **coefficient-gradient-dominated transition regime** on almost all active record time if it is to avoid the favorable palinstrophy ledger.

## 8. Quantitative palinstrophy-time thinning

Let `delta_R` denote the fraction of the active interface time on which the palinstrophy part carries a fixed fraction of the transition charge.

Then

\[
\mathcal P_{anc,R}
\gtrsim
c\beta_R\delta_RR.
\]

Finite ancestral palinstrophy requires

\[
\boxed{
\sum_m\beta_{R_m}\delta_{R_m}R_m<\infty.
}
\]

Thus, if `beta_R` is bounded below, the palinstrophy-dominated interface times must become extremely sparse. Almost all retained transition payment must asymptotically be routed through `rho^2|nabla kappa|^2` or another explicit exit.

## 9. Geometry firewall

The argument requires a uniform Dirichlet/Friedrichs constant for the negative-to-zero transition domain.

If

\[
C_{F,R}\to\infty,
\]

classify that as

\[
\boxed{G_{negative\ interface\ spectral/shape\ decompactification}}
\]

and apply the M17-449 principle: separate ordinary size growth from scale-free shape degeneration before interpreting it as a neck.

## 10. Updated local-compensation split

\[
\boxed{
\begin{aligned}
H_{local\ moderate\ negative\ compensation}
\Longrightarrow{}&
H_{mesoscopic\ thickness}\Rightarrow\text{M17-454 contradiction if persistent}\\
&\lor H_{bounded\ width\ regular\ interface}\\
&\qquad\Rightarrow
\left(
H_{palinstrophy\ payer}
\lor H_{coefficient\text{-}gradient\ payer}
\right)\\
&\lor G_{interface\ spectral/shape\ decompactification}\\
&\lor G_{coefficient/high\text{-}jet/chart/genealogy\ loss}.
\end{aligned}
}
\]

The only inexpensive analytic survivor inside a regular bounded-width interface is coefficient-gradient-dominated payment because its certified ancestry weight is quintic.

## 11. Audit verdict

**PASS — the own-scale-thick negative-interface branch has an exact payer dichotomy.**

A fixed moderate-negative enstrophy mass cannot approach the zero level through a uniformly regular bounded-width layer for free. It must pay either the favorable palinstrophy currency or the more heavily discounted coefficient-gradient currency. Survival therefore requires asymptotic routing into the latter, spectral/interface degeneration, or another explicit loss.

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
