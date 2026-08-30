# DSD M5-324 — Whole-Space Reverse-Oseen Off-Support Localization and Adjoint Tightness

Date: 2026-08-30

Status: **THE KEY HUANG REVERSE-OSEEN LOCALIZATION ESTIMATE TRANSFERS TO R3 / FIXED-RADIUS TERMINAL ADJOINT ESCAPE TO SPATIAL INFINITY IS REMOVED / FULL HUANG THEOREM TRANSFER STILL REQUIRES THE REMAINING COMPACTNESS-SATURATION BOOKKEEPING / GLOBAL REGULARITY UNPROVED.**

## 1. Purpose

`M5-322` listed two possible whole-space transfer gaps for the atomic-rigidity route:

1. terminal adjoint mass might escape to spatial infinity;
2. the delayed Oseen second-order budget might remain uncontrolled.

`M5-323` shows that item 2 is a genuine large-critical endpoint problem.

This note audits item 1 using the exact mechanism of Huang's reverse-Oseen off-support estimate.

## 2. Whole-space reverse Oseen equation

Let

\[
\partial_\rho w+(b\cdot\nabla)w+\nabla\pi=\nu\Delta w,
\qquad
\nabla\cdot w=0,
\]

on `[0,L] x R^3`, with smooth divergence-free drift `b` and initial datum

\[
w(0)=w_0\in L^2_\sigma(\mathbb R^3).
\]

Set

\[
W=\|w\|_{L^\infty_\rho L^2_x},
\qquad
G=\|\nabla w\|_{L^2_{\rho,x}},
\qquad
B=\|b\|_{L^2_\rho L^6_x}.
\]

The global energy identity is

\[
\boxed{
W\le \|w_0\|_2,
\qquad
G\le (2\nu)^{-1/2}\|w_0\|_2.
}
\]

## 3. Pressure estimate is unchanged on R3

Taking divergence gives

\[
-\Delta\pi=\partial_i\partial_j(b_jw_i),
\]

hence

\[
\pi=\mathcal R_i\mathcal R_j(b_jw_i).
\]

Whole-space Riesz boundedness gives

\[
\boxed{
\|\pi\|_{3/2}
\lesssim
\|b\|_6\|w\|_2.
}
\]

Thus the torus pressure normalization is not needed for the localized estimate.

## 4. Whole-space interpolation is at least as strong

On `R^3`, the homogeneous Sobolev inequality gives

\[
\|w\|_6\lesssim\|\nabla w\|_2.
\]

Interpolation yields

\[
\|w\|_{12/5}^2
\lesssim
\|w\|_2^{3/2}\|\nabla w\|_2^{1/2},
\]

and

\[
\|w\|_3
\lesssim
\|w\|_2^{1/2}\|\nabla w\|_2^{1/2}.
\]

Unlike the periodic proof, no spatial-mean-zero correction term is required.

## 5. Localized energy estimate

Let `0<=zeta<=1`, `zeta in W^{2,infinity}(R^3)`. Multiplying by `2 zeta w`, integrating, and using the pressure estimate gives the same structural estimate as Huang:

\[
\boxed{
\begin{aligned}
\int \zeta|w(L)|^2
&\le
\int \zeta|w_0|^2
+C\|\nabla\zeta\|_\infty L^{1/4}BW^{3/2}G^{1/2}\\
&\quad
+\nu\|\Delta\zeta\|_\infty LW^2.
\end{aligned}
}
\]

The constant is independent of pointwise norms or derivatives of `b`.

## 6. Off-support estimate

Assume

\[
\operatorname{supp}w_0\subset B_r(a).
\]

Choose a cutoff satisfying

\[
\zeta=0\text{ on }B_r(a),
\qquad
\zeta=1\text{ on }\mathbb R^3\setminus B_{2r}(a),
\]

with

\[
\|\nabla\zeta\|_\infty\lesssim r^{-1},
\qquad
\|\Delta\zeta\|_\infty\lesssim r^{-2}.
\]

Substituting the energy bounds yields

\[
\boxed{
\begin{aligned}
\|w(L)\|_{L^2(\mathbb R^3\setminus B_{2r}(a))}^2
&\lesssim
r^{-1}(2\nu)^{-1/4}L^{1/4}B\|w_0\|_2^2\\
&\quad+
u r^{-2}L\|w_0\|_2^2.
\end{aligned}
}
\]

This is the direct whole-space analogue of Huang's Lemma 4.2.

## 7. Apply to the Navier–Stokes parent

For the parent drift `b=u`, the smooth finite-energy branch satisfies

\[
\int_t^{T_*}\|\nabla u(s)\|_2^2ds\to0
\qquad(t\uparrow T_*).
\]

By whole-space Sobolev,

\[
\boxed{
B(t,T_*)
=\|u\|_{L^2(t,T_*;L^6)}
\lesssim
\|\nabla u\|_{L^2(t,T_*;L^2)}
\to0.
}
\]

Take Hodge packets `q_j` supported in balls `B_j downarrow {a}` and evolve them backward to a fixed preterminal time `t`. For every fixed radius `r>0`, all sufficiently late packets lie in `B_{r/2}(a)`.

The reverse time length satisfies

\[
L_j=\tau_j-t\le T_*-t.
\]

Hence

\[
\limsup_{j\to\infty}
\|v_j(t)\|_{L^2(\mathbb R^3\setminus B_r(a))}^2
\lesssim
r^{-1}(T_*-t)^{1/4}B(t,T_*)
+\nu r^{-2}(T_*-t).
\]

Letting `t up T_*` gives

\[
\boxed{
\lim_{t\uparrow T_*}
\limsup_{j\to\infty}
\|v_j(t)\|_{L^2(\mathbb R^3\setminus B_r(a))}=0
\quad\forall r>0.
}
\]

Thus the backward adjoint cannot lose its terminal mass at spatial infinity.

## 8. Consequence for the extracted common adjoint

Any weakly extracted common adjoint `A` inherits

\[
\boxed{
\lim_{t\uparrow T_*}
\|A(t)\|_{L^2(\mathbb R^3\setminus B_r(a))}=0
\quad\forall r>0,
}
\]

provided the standard weak-limit passage is performed.

Combined with the atom pairing/Cauchy-saturation part of the Huang construction, this is the exact terminal tightness needed to identify the adjoint energy measure with a point mass at `a`.

## 9. What compactness remains on R3

The torus gives global Aubin–Lions compactness automatically. `R^3` does not.

However the needed sequence is globally bounded in `L^2` and locally compact on every bounded cylinder. Therefore one may combine

- global weak `L^2` compactness;
- local Aubin–Lions strong compactness;
- the off-support terminal tightness above;
- fixed-parent duality with the finite-energy Navier–Stokes state.

This strongly suggests that the common-adjoint extraction can be transferred, but this note does **not** claim the full Huang theorem on `R^3` without replaying every saturation step.

## 10. Formation-axiom interpretation

The previously named `infinity-tightness failure` is not an independent branch once the object is described by the correct variables:

\[
(L,r,B,W,G).
\]

The off-support mass is a determined output of those descriptors. Since the parent has `B(t,T*) -> 0`, no additional infinity degree of freedom survives at the terminal layer.

Thus the whole-space transfer frontier is reduced rather than enlarged.

## 11. Updated Huang-transfer frontier

The current structure is

\[
\boxed{
\begin{array}{c|c}
\text{item}&\text{status}\\
\hline
\text{endpoint measure on R3}&\text{proved in M5-321}\\
\text{point atom extraction}&\text{proved in M5-321}\\
\text{whole-space Oseen energy family}&\text{standard / compatible}\\
\text{reverse-Oseen off-support localization}&\text{proved here}\\
\text{terminal adjoint infinity escape}&\text{removed here}\\
\text{full common-adjoint saturation replay}&\text{to be checked}\\
\text{large-critical parent delayed H2 finiteness}&\text{open; M5-323}
\end{array}
}
\]

The dominant internal obstruction is now the final line.

## 12. Audit verdict

### PROVED

- Huang's reverse-Oseen localization estimate transfers to `R^3`;
- whole-space pressure and Sobolev estimates suffice;
- finite-energy ancestry gives `L^2_tL^6_x` tail smallness;
- terminal adjoint mass cannot escape to infinity at fixed radius.

### NOT YET CLAIMED

- the complete atomic full-tail theorem on `R^3`;
- large-critical delayed Oseen H2 finiteness.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
