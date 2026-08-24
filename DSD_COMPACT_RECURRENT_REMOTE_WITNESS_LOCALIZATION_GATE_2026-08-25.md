# DSD Compact-Recurrent Remote Witness Localization Gate

Date: 2026-08-25

Status: **RWLG CLOSED ON THE GENUINELY PRECOMPACT FIXED-CENTER H2 RECURRENT CLASS / POSITIVE-DENSITY REMOTE ENSTROPHY FORCES A POSITIVE-DENSITY BOUNDED-RADIUS CRITICAL GRADIENT SHELL / MATERIAL GENEALOGY STILL NOT IDENTIFIED / GLOBAL REGULARITY UNPROVED.**

## 1. Purpose and exact scope

The direct Betchov positive-density gate gives a positive recurrent-time density of standard Leray times at which

\[
Z(s):=\|W(s)\|_2^2\ge z_h,
\qquad
z_h:=\theta\,54\pi^2\nu^{3/2},
\qquad 0<\theta<1.
\]

The remaining Remote Witness Localization Gate (RWLG) asks whether these high-enstrophy/remote-mass witnesses can remain arbitrarily diffuse and arbitrarily remote without producing a finite matching-scale local concentration.

This note closes RWLG on the already-defined genuinely precompact recurrent class `K` used by the H1 recurrence-tax route.

The class assumptions are exactly the existing ones:

- first-hitting center and scale are fixed;
- a fixed gauge eliminates translation drift;
- the strain class is genuinely precompact in the stated H2/H1-tight sense;
- the recurrent orbit remains in `K`;
- the nontrivial normalization prevents convergence to zero.

No statement below is promoted outside that compact fixed-center branch.

---

## 2. Strain precompactness transfers to vorticity L2 precompactness

Let

\[
\Sigma=\operatorname{sym}\nabla V,
\qquad
W=\nabla\times V.
\]

On divergence-free whole-space fields, `Sigma` and `W` are related by order-zero Fourier multipliers. In particular, for every finite Sobolev order used here,

\[
\|W\|_{H^s}\asymp \|\Sigma\|_{H^s}.
\]

Hence the bounded linear map

\[
\Sigma\mapsto W
\]

sends the precompact fixed-center class `K` to a precompact subset of `L2`.

Every compact subset of `L2(R^3)` is uniformly tight. Therefore for every `eta>0` there exists a finite radius

\[
R_T=R_T(K,\eta)<\infty
\]

such that

\[
\boxed{
\sup_{\Sigma\in K}
\int_{|Y|>R_T}|W(Y)|^2dY
<\eta.
}
\]

This is a fixed-center statement; no moving-center or Galilean identification is used.

**Status: PROVED from the existing compact-class hypotheses and boundedness of the strain-vorticity Fourier map.**

---

## 3. Uniform Leray-vorticity amplitude ceiling on the recurrent first-hitting corridor

At a physical time lying in first-hitting stage `j`, the parent first-hitting variables satisfy

\[
\Omega_j=\frac{\omega}{W_j},
\qquad
\|\Omega_j\|_\infty\le q.
\]

Standard Leray vorticity is

\[
W_L=(T^*-t)\omega
=\Theta_j(t)\Omega_j,
\]

where

\[
\Theta_j(t)=W_j(T^*-t).
\]

The recurrent clock corridor gives

\[
0<\Theta_j(t)\le\Theta_+
:=\frac{q}{q-1}L_+.
\]

Therefore

\[
\boxed{
\|W_L(s)\|_\infty
\le M_W,
\qquad
M_W:=q\Theta_+.
}
\]

This ceiling is uniform on the retained recurrent corridor.

---

## 4. Canonical high-enstrophy quantile radius has a positive lower bound

Fix

\[
0<\varepsilon<1.
\]

At a high-enstrophy time define the standard-Leray quantile radius

\[
R_\varepsilon(s)
:=
\inf\left\{
R>0:
\int_{B_R}|W|^2
\ge(1-\varepsilon)Z(s)
\right\}.
\]

Since

\[
|W|^2\le M_W^2,
\]

one has

\[
(1-\varepsilon)Z(s)
\le
\frac{4\pi}{3}M_W^2R_\varepsilon(s)^3.
\]

On the high-enstrophy set `A_theta`, `Z(s)>=z_h`, so

\[
\boxed{
R_\varepsilon(s)
\ge r_h
:=
\left[
\frac{3(1-\varepsilon)z_h}
{4\pi M_W^2}
\right]^{1/3}
>0.
}
\]

Thus the witness cannot collapse to zero Leray radius.

---

## 5. Compactness also gives a uniform upper quantile radius

Choose the uniform-tightness tolerance

\[
\eta_T:=\frac{\varepsilon z_h}{2}.
\]

Section 2 gives `R_T<infinity` such that

\[
\int_{|Y|>R_T}|W|^2
<\frac{\varepsilon z_h}{2}
\le
\frac\varepsilon2 Z(s)
\]

at every high-enstrophy time in the compact recurrent class.

Hence

\[
\int_{B_{R_T}}|W|^2
>
\left(1-\frac\varepsilon2\right)Z(s)
>
(1-\varepsilon)Z(s).
\]

Therefore

\[
\boxed{
R_\varepsilon(s)\le R_T
}
\]

uniformly on every high-enstrophy time in `K`.

Combining Sections 4 and 5,

\[
\boxed{
r_h\le R_\varepsilon(s)\le R_T.}
\]

This is the first uniform two-sided localization of the Betchov high-enstrophy quantile witness on the compact recurrent branch.

---

## 6. A fixed amount of remote mass remains inside a bounded annulus

Fix

\[
0<\alpha<1.
\]

By the defining property of the quantile radius, for every radius strictly below `R_epsilon`, and hence for `alpha R_epsilon`,

\[
\int_{|Y|>\alpha R_\varepsilon}|W|^2
>
\varepsilon Z(s)
\ge
\varepsilon z_h.
\]

The mass beyond `R_T` is at most `epsilon z_h/2`. Consequently

\[
\boxed{
\int_{\alpha R_\varepsilon<|Y|\le R_T}
|W|^2dY
\ge
m_h,
\qquad
m_h:=\frac{\varepsilon z_h}{2}>0.
}
\]

Thus compact recurrence does not merely prevent total escape to infinity. It traps a fixed positive amount of the Betchov remote mass in a uniformly bounded annulus.

---

## 7. Finite dyadic localization forces one critical shell

Set

\[
R_0(s):=\alpha R_\varepsilon(s).
\]

Then

\[
\alpha r_h\le R_0(s)\le \alpha R_T.
\]

Cover the bounded annulus

\[
R_0(s)<|Y|\le R_T
\]

by dyadic shells

\[
A_k(s)
=
\{2^kR_0(s)<|Y|<2^{k+1}R_0(s)\}
\]

up to the last truncated shell.

The number of shells is uniformly bounded by

\[
\boxed{
N_K
:=
1+\left\lceil
\log_2\frac{R_T}{\alpha r_h}
\right\rceil
<\infty.
}
\]

Write

\[
m_k(s):=\int_{A_k(s)}|W|^2dY.
\]

Since their total mass is at least `m_h`, one shell satisfies

\[
\boxed{
m_k(s)\ge \frac{m_h}{N_K}.}
\]

Its radius satisfies

\[
R_k(s):=2^kR_0(s)
\ge\alpha r_h
\]

and is bounded above by a fixed multiple of `R_T`.

Because

\[
|W|^2=|\nabla\times V|^2\le2|\nabla V|^2,
\]

we obtain

\[
\int_{A_k}|\nabla V|^2dY
\ge\frac12m_k.
\]

Therefore the scale-critical shell gradient charge obeys

\[
\boxed{
R_k
\int_{A_k}|\nabla V|^2dY
\ge
J_K,
}
\]

with the explicit positive class-dependent constant

\[
\boxed{
J_K
:=
\frac{\alpha r_hm_h}{2N_K}
=
\frac{\alpha r_h\varepsilon z_h}{4N_K}
>0.
}
\]

The shell radius also satisfies a uniform ceiling

\[
\boxed{R_k\le 2R_T.}
\]

Thus every Betchov high-enstrophy time in the compact recurrent class contains a bounded-radius critical gradient shell.

**Status: PROVED.**

---

## 8. Positive time density transfers to the localized shell certificate

The direct Betchov density gate already gives

\[
\mu(A_\theta)>0.
\]

Section 7 applies to every time in `A_theta` while the orbit remains in `K`.

Hence

\[
\boxed{
\mu\left(
\left\{s:
\exists R\in[\alpha r_h,2R_T]
\text{ with }
R\int_{A_R}|\nabla V|^2\ge J_K
\right\}
\right)
\ge
\mu(A_\theta)>0.
}
\]

So the compact recurrent survivor must carry **positive Leray-time density of bounded-radius critical gradient witnesses**.

This is substantially stronger than merely having a remote shell along an exceptional subsequence.

---

## 9. Relation to the terminal analytic-window genealogy gate

Because the active normalized radius is now bounded above by `2R_T`, the physical shell radius is only a fixed multiple of the current similarity/first-hitting radius.

The first-hitting/Leray clock comparison gives two-sided comparability between those natural radii on the recurrent corridor.

Therefore the terminal analytic window constructed in
`TERMINAL_ANALYTIC_WINDOW_DISSIPATION_GATE_2026-08-25.md`
can be shortened by a fixed class-dependent factor, if necessary, so that it occupies a positive fraction of the bounded shell's parabolic time.

Consequently the bounded-radius shell certificate is eligible for the already-derived terminal local-enstrophy persistence/crossing decomposition.

What follows rigorously is the finite alternative

\[
\boxed{
\text{bounded-radius critical shell}
\Longrightarrow
\text{historical local-gradient/dissipation certificate}
\lor
\text{relative-transport / turnover channel}
\lor
\text{derivative-active channel},
}
\]

with constants depending on the compact class bounds.

This note does **not** identify the Eulerian shell with one particular material ancestor packet.

---

## 10. RWLG verdict on the compact class

The localization question on `K` is now closed:

\[
\boxed{
\text{positive-density Betchov remote witness}
+
\text{fixed-center H2 precompact recurrence}
\Longrightarrow
\text{positive-density bounded-radius critical gradient witnesses}.
}
\]

Therefore an RWLG escape in which every critical witness radius tends to infinity is incompatible with remaining in the genuinely precompact fixed-center class.

Equivalently,

\[
\boxed{
R_{active}(s_n)\to\infty
\Longrightarrow
\text{loss of the compact-class tightness hypothesis}
}
\]

along such a witness sequence.

This loss must be routed outside the compact `P_V` lane, into the already separated remote/non-tight genealogy-tail branch.

---

## 11. DSD audit

The finite formed channels are

- high-enstrophy time `s`;
- compact recurrent class `K` with fixed center/gauge;
- uniform vorticity tightness radius `R_T`;
- quantile radius `R_epsilon(s)`;
- bounded annular mass `m_h`;
- finite shell count `N_K`;
- one finite critical shell with charge `J_K`.

No material identity is inferred from Eulerian overlap.

No infinite shell family is treated as one Stage-VII object; only a finite shell cover of a bounded annulus is used.

---

## 12. What is still not proved

Not derived here:

- a material-ancestor identity for the selected critical shell;
- a universal compact-class radius `R_T` independent of the class `K`;
- closure of the non-precompact remote-tail branch;
- summability contradiction from the positive-density local charges by themselves;
- global regularity.

The remaining genealogy frontier is now sharper:

\[
\boxed{
\text{on compact }K:
\text{ Eulerian remote localization is solved; only material genealogy/return remains},
}
\]

while

\[
\boxed{
\text{outside compact }K:
\text{ the survivor must pay genuine spatial non-tightness / critical-tail escape}.
}
\]

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
