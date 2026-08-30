# DSD M5-325 — Whole-Space Huang Atomic Full-Tail Transfer Theorem Audit

Date: 2026-08-30

Status: **THE HUANG ATOM -> FULL-TAIL SATURATION -> INFINITE DELAYED SECOND-ORDER ACTION ARCHITECTURE TRANSFERS TO SMOOTH FINITE-ENERGY R3 PRETERMINAL FLOWS USING WHOLE-SPACE REPLACEMENTS FOR THE THREE PERIODIC INPUTS / LARGE-CRITICAL PARENT BUDGET FINITENESS REMAINS OPEN / GLOBAL REGULARITY UNPROVED.**

## 1. Purpose

Hao Huang's 2026 theorem is stated on `T^3`. Its scope section explicitly identifies the uses of periodicity:

1. periodic Riesz-transform pressure representation;
2. nested local-Hodge construction in Euclidean chart balls;
3. drift-independent periodic Nash smoothing.

The subsequent saturation mechanism is Hilbert-space/Oseen-energy based.

`M5-321` proves the whole-space endpoint energy measure and atom extraction.

`M5-324` proves the whole-space reverse-Oseen off-support estimate.

This note assembles the remaining replacements and audits the transfer to `R^3`.

## 2. Whole-space setting

Let

\[
u\in C^\infty([t_b,T_*)\times\mathbb R^3),
\qquad \nabla\cdot u=0,
\]

solve unforced 3D Navier–Stokes and satisfy the finite-energy preterminal bounds

\[
E_*:=\sup_{t_b\le t<T_*}\|u(t)\|_2<\infty,
\]

\[
\int_{t_b}^{T_*}\|\nabla u(t)\|_2^2dt<\infty.
\]

Assume the endpoint energy measure has an atom

\[
\boxed{\mu_*(\{a\})=m>0.}
\]

The goal is to reproduce the atomic full-tail construction on `R^3`.

## 3. Periodic input 1: pressure

On `R^3`,

\[
p=\mathcal R_i\mathcal R_j(u_i u_j)
\]

up to the irrelevant time-dependent constant.

Hence

\[
\|p\|_{3/2}\lesssim\|u\|_3^2.
\]

This is the exact replacement used in the endpoint-measure and localized-energy estimates.

Status: **GREEN.**

## 4. Periodic input 2: local Hodge spaces

For an open ball `B subset R^3`, define

\[
\mathcal H(B)
:=\overline{C^\infty_{c,\sigma}(B)}^{L^2(\mathbb R^3)},
\]

and let `Q_B` be the orthogonal projection from `L^2_sigma(R^3)` onto `H(B)`.

If

\[
B_{j+1}\Subset B_j,
\]

then

\[
\mathcal H(B_{j+1})\subset\mathcal H(B_j),
\]

so the orthogonal projections commute and

\[
D_j:=Q_{B_j}-Q_{B_{j+1}}
\]

is the orthogonal projection onto

\[
\mathcal H(B_j)\cap\mathcal H(B_{j+1})^\perp.
\]

If

\[
q_j\in\mathcal H(B_j)\cap\mathcal H(B_{j+1})^\perp,
\]

then inside `B_{j+1}`, `q_j` is divergence free and orthogonal to every compactly supported solenoidal test field. By local de Rham,

\[
q_j=\nabla\phi_j
\quad\text{on }B_{j+1}.
\]

Since `div q_j=0`,

\[
\boxed{\Delta\phi_j=0.}
\]

Thus `q_j` is a harmonic gradient in the inner ball exactly as in Huang's periodic Euclidean-chart construction.

The local projection lower bound from a cutoff energy level is obtained by the same ball-local Bogovskii/Hodge argument already used throughout the repository.

Status: **GREEN.**

## 5. Periodic input 3: Nash smoothing

For scalar advection diffusion

\[
f_t+b\cdot\nabla f=\nu\Delta f,
\qquad \nabla\cdot b=0,
\]

whole-space Kato plus divergence freedom gives `L1` contraction and

\[
\frac12\frac d{dt}\|f\|_2^2+\nu\|\nabla f\|_2^2=0.
\]

The standard whole-space Nash inequality

\[
\boxed{
\|g\|_2^{10/3}
\le C_N\|g\|_1^{4/3}\|\nabla g\|_2^2
}
\]

therefore yields the drift-independent estimates

\[
\boxed{
\|S_b(t,s)\|_{L^1\to L^2}
+\|S_b(t,s)\|_{L^2\to L^\infty}
\lesssim
[\nu(t-s)]^{-3/4}.
}
\]

These are at least as strong as the periodic Nash bounds for positive delay.

Status: **GREEN.**

## 6. Catalogued level crossing and Hodge packets

Because `u(t)` is smooth and finite energy at every fixed preterminal time, for every fixed `h<T_*`,

\[
\|u(t)\|_{L^2(B_r(a))}\to0
\qquad(r\downarrow0)
\]

uniformly over any compact preterminal time interval by smoothness/absolute continuity.

On the other hand the endpoint atom gives, for cutoffs `chi_j=1` near `a`,

\[
\int\chi_j|u(t)|^2\to\int\chi_jd\mu_*\ge m.
\]

Thus Huang's frozen selection order — old-time smallness, then a high-time crossing, then nested Hodge projections — carries over unchanged.

The resulting packets may be chosen orthonormal with

\[
q_j\in\mathcal H(B_j)\cap\mathcal H(B_{j+1})^\perp,
\]

\[
q_j=0\text{ outside }B_j,
\]

and

\[
\boxed{
\langle u(\tau_j),q_j\rangle\to\sqrt m.
}
\]

Status: **GREEN.**

## 7. Oseen evolution family on R3

Define the constrained Oseen evolution

\[
\partial_t h+\mathbb P[(u\cdot\nabla)h]=\nu\Delta h.
\]

On every compact preterminal interval the smooth drift gives the standard `L2_sigma` evolution family.

The exact energy identity is

\[
\boxed{
\|U(t,s)h_s\|_2^2
+2\nu\int_s^t\|\nabla U(\rho,s)h_s\|_2^2d\rho
=\|h_s\|_2^2.
}
\]

The adjoint has the corresponding backward identity and duality relation.

Status: **GREEN.**

## 8. Compact preterminal extraction: replace global torus compactness by tightness

For the backward pulses

\[
v_j(t)=U(\tau_j,t)^*q_j,
\]

energy gives a uniform global `L2` bound and `L2_t H1_x` bound on every fixed preterminal interval.

Local Aubin–Lions gives strong compactness on every fixed spatial ball.

To upgrade from local to global `L2`, use `M5-324` with a large ball `B_R(a)`. Since the terminal packets are eventually contained in `B_{R/2}(a)`, for all `t in [t_b,S]` and sufficiently large `j`,

\[
\|v_j(t)\|_{L^2(\mathbb R^3\setminus B_R(a))}^2
\lesssim
R^{-1}C_1+R^{-2}C_2,
\]

where `C1,C2` depend only on the fixed parent energy/dissipation and terminal interval length, not on `j`.

Hence

\[
\boxed{
\lim_{R\to\infty}
\sup_j\sup_{t\in[t_b,S]}
\|v_j(t)\|_{L^2(|x-a|>R)}=0.
}
\]

Local strong compactness plus this uniform tail tightness yields global strong compactness in

\[
L^2([t_b,S]\times\mathbb R^3).
\]

Thus the global torus Rellich compactness is replaced by

\[
\boxed{\text{local Aubin--Lions}+\text{whole-space spatial tightness}.}
\]

Status: **GREEN.**

## 9. Common adjoint and terminal localization

The extracted adjoint `A` satisfies

\[
\langle u(t),A(t)\rangle=a_\infty,
\]

and the packet lower bound yields

\[
a_\infty^2\ge m.
\]

`M5-324` also gives, for every fixed `r>0`,

\[
\boxed{
\|A(t)\|_{L^2(\mathbb R^3\setminus B_r(a))}\to0
\qquad(t\uparrow T_*).
}
\]

The same Cauchy-saturation argument as Huang now gives

\[
\boxed{
a_\infty^2=m,
\qquad
\|A(t)\|_2^2\to1,
}
\]

and

\[
\boxed{
|A(t,x)|^2dx\stackrel{*}{\rightharpoonup}\delta_a.
}
\]

Furthermore the parent/adjoint atomic-layer alignment is

\[
\boxed{
\lim_{r\downarrow0}
\limsup_{t\uparrow T_*}
\int_{B_r(a)}|u(t)-\sqrt m A(t)|^2dx=0.
}
\]

Status: **GREEN modulo the same Hilbert saturation algebra, whose inputs are now available.**

## 10. Full-tail saturation

The remaining upgrade uses only

- weak convergence in a fixed Hilbert space;
- exact forward/backward Oseen energy identities;
- terminal adjoint norm equal to one.

Therefore the direct-sum norm-saturation argument carries over verbatim to

\[
L^2_\sigma(\mathbb R^3)
\oplus
L^2((t_0,T_*)\times\mathbb R^3).
\]

Hence, after the same frozen subsequence selection,

\[
\boxed{
\sup_{k>j\ge J}
\|U(\tau_k,\tau_j)q_j-q_k\|_2\to0,
}
\]

\[
\boxed{
\sup_{k>j\ge J}
\|U(\tau_k,\tau_j)^*q_k-q_j\|_2\to0,
}
\]

and the corresponding first-order dissipations vanish uniformly on the late triangle.

Status: **GREEN.**

## 11. Second-order action on R3

Fix a late root `J` and set

\[
H(t)=U(t,\tau_J)q_J.
\]

For cells

\[
I_j=[\tau_j,\tau_{j+1}],
\]

define

\[
d_j=\int_{I_j}\|\nabla u\|_2^2,
\quad
a_j=\int_{I_j}\|\nabla H\|_2^2,
\quad
K_j=\int_{I_j}\|\Delta H\|_2^2.
\]

On `R^3`, homogeneous Sobolev gives

\[
\|u\|_6\lesssim\|\nabla u\|_2,
\qquad
\|\nabla H\|_3
\lesssim
\|\nabla H\|_2^{1/2}\|\Delta H\|_2^{1/2}.
\]

Thus Huang's cellwise argument becomes slightly cleaner:

\[
\|H(\tau_{j+1})-H(\tau_j)\|_2
\lesssim
d_j^{1/2}a_j^{1/4}K_j^{1/4}
+\nu\ell_j^{1/2}K_j^{1/2}.
\]

Full-tail saturation and orthogonality give a fixed positive lower bound on the left side. Hence

\[
\boxed{
K_j\ge
\min\{c_1d_j^{-2}a_j^{-1},\ c_2\nu^{-2}\ell_j^{-1}\}.
}
\]

Since

\[
\sum_jd_j<\infty,
\qquad
\sum_ja_j<\infty,
\qquad
\sum_j\ell_j<\infty,
\]

one has `K_j -> infinity`, and the Huang summability argument gives

\[
\boxed{
\int_{\tau_{J+1}}^{T_*}
\|\Delta U(t,\tau_J)q_J\|_2^2dt
=\infty
}
\]

for every sufficiently late fixed root.

The positive Oseen-enstrophy production is also nonintegrable.

Status: **GREEN.**

## 12. Whole-space transferred theorem

Within the standard smooth finite-energy whole-space framework, the preceding replacements establish the transferred implication

\[
\boxed{
\mu_*(\{a\})>0
\Longrightarrow
\text{same-parent full-tail saturated Hodge family}
\Longrightarrow
\mathfrak R_u(\tau_J,\tau_{J+1})=\infty
}
\]

for every sufficiently late root `J`.

This is the `R^3` analogue of Huang's atomic full-tail direction.

## 13. Important scope limit

This transfer does **not** solve the Navier–Stokes problem.

`M5-323` shows that the current large weak-L3 no-H/T corridor does not automatically imply

\[
\mathfrak R_u<\infty.
\]

Thus the atom branch has now been converted into a sharp parent-only operator obstruction, but the critical endpoint finiteness side remains open.

## 14. Updated proof frontier

The affine-shield route now reads

\[
\boxed{
\text{affine shield saturation}
\Rightarrow
\text{endpoint energy atom}
\Rightarrow
\mathfrak R_u=\infty.
}
\]

To close it, it is sufficient to prove on the complementary no-H/T corridor either

\[
\boxed{\mathfrak R_u<\infty}
\]

or any equivalent upper bound contradicting Huang's cellwise second-order action.

## 15. Audit verdict

### PROVED WITH STANDARD WHOLE-SPACE REPLACEMENTS

- endpoint energy measure and atom extraction;
- whole-space local Hodge packets;
- drift-independent Nash smoothing;
- reverse-Oseen off-support localization;
- global preterminal adjoint compactness via local compactness + tail tightness;
- common-adjoint saturation;
- cellwise second-order action divergence.

### STILL OPEN

- finite delayed Oseen H2 budget for the large critical no-H/T parent class;
- final elimination of dynamic turnover/critical endpoint alternatives;
- global regularity.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
