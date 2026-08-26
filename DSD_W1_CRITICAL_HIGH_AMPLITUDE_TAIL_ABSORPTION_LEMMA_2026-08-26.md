# DSD W1 Critical High-Amplitude Tail Absorption Lemma

Date: 2026-08-26

Status: **PROVED AUXILIARY REGULARITY LEMMA / UNIFORM SMALLNESS OF ONE HIGH-AMPLITUDE WEAK-L3 TAIL IMPLIES H1 CONTROL AND CONTINUATION / EXACT TRUNCATED-ENERGY DEFECT `K` IS QUANTITATIVELY EQUIVALENT TO THAT TAIL / THIS DOES NOT YET PROVE THE REQUIRED UNIFORM TAIL SMALLNESS / GLOBAL REGULARITY UNPROVED.**

## 1. Physical high-amplitude split

Let `u` be a smooth finite-energy Navier--Stokes solution on `(t0,T*)`. Fix a physical velocity threshold `L>0` and split

\[
u=v_L+w_L,
\]

where

\[
v_L=u\,\mathbf 1_{\{|u|\le L\}},
\qquad
w_L=u\,\mathbf 1_{\{|u|>L\}}.
\]

No divergence-free property of the two pieces is required below; the split is used only inside the nonlinear estimate. Clearly

\[
\|v_L\|_\infty\le L.
\]

## 2. H1 energy estimate

Test the Navier--Stokes equation with `-Delta u`. For smooth divergence-free `u`,

\[
\frac12\frac d{dt}\|\nabla u\|_2^2
+\nu\|\Delta u\|_2^2
=\int (u\cdot\nabla u)\cdot\Delta u\,dx
\]

up to the harmless sign convention on the right-hand side. Therefore

\[
\left|\int (u\cdot\nabla u)\cdot\Delta u\right|
\le
I_v+I_w,
\]

with

\[
I_v
:=\int |v_L||\nabla u||\Delta u|,
\qquad
I_w
:=\int |w_L||\nabla u||\Delta u|.
\]

The bounded part satisfies

\[
I_v
\le
L\|\nabla u\|_2\|\Delta u\|_2
\le
\frac\nu4\|\Delta u\|_2^2
+C\frac{L^2}{\nu}\|\nabla u\|_2^2.
\]

For the high part, Lorentz Holder gives

\[
I_w
\le
C
\|w_L\|_{L^{3,\infty}}
\|\nabla u\|_{L^{6,2}}
\|\Delta u\|_2.
\]

The Sobolev--Lorentz embedding yields

\[
\|\nabla u\|_{L^{6,2}}
\le C_S\|\nabla^2u\|_2
\le C'_S\|\Delta u\|_2
\]

on `R3`, so

\[
\boxed{
I_w
\le
C_*\|w_L\|_{3,\infty}\|\Delta u\|_2^2.
}
\]

## 3. Small high-tail absorption

Choose

\[
\boxed{
\varepsilon_\nu
:=\frac{\nu}{4C_*}.
}
\]

If for some finite `L` and some `t0<T*`,

\[
\boxed{
\sup_{t_0<t<T_*}
\|u(t)\mathbf1_{\{|u(t)|>L\}}\|_{3,\infty}
\le\varepsilon_\nu,
}
\]

then the high-amplitude nonlinear term is absorbed into viscosity. Hence

\[
\frac d{dt}\|\nabla u\|_2^2
+\frac\nu2\|\Delta u\|_2^2
\le
C\frac{L^2}{\nu}\|\nabla u\|_2^2.
\]

Gronwall on the finite interval `(t0,T*)` gives

\[
\boxed{
\sup_{t_0<t<T_*}\|\nabla u(t)\|_2<\infty.
}
\]

Standard local strong-solution continuation then extends the solution past `T*`.

Therefore:

\[
\boxed{
\text{one uniformly small high-amplitude weak-}L^3\text{ tail}
\Longrightarrow
\text{no finite-time blow-up}.
}
\]

## 4. Truncated-energy boundary coordinate

Let

\[
N_t(\alpha)=|\{x:|u(x,t)|>\alpha\}|.
\]

Define the physical critical truncated-energy tail

\[
\boxed{
K_L^{phys}(t)
:=
\frac L2\int (|u|^2-L^2)_+dx
=L\int_L^\infty\alpha N_t(\alpha)d\alpha.
}
\]

Also define

\[
M_L(t)^3
:=
\sup_{\alpha\ge L}\alpha^3N_t(\alpha).
\]

Up to conventional Lorentz normalization,

\[
M_L(t)
=\|u(t)\mathbf1_{\{|u|>L\}}\|_{3,\infty}.
\]

Since

\[
N_t(\alpha)\le M_L(t)^3\alpha^{-3}
\qquad(\alpha\ge L),
\]

we obtain

\[
\boxed{
K_L^{phys}(t)
\le
M_L(t)^3.
}
\]

Conversely, for `alpha>=2L`, monotonicity of `N_t` gives

\[
\begin{aligned}
K_{\alpha/2}^{phys}(t)
&=\frac\alpha2
\int_{\alpha/2}^\infty\mu N_t(\mu)d\mu\\
&\ge
\frac\alpha2
\int_{\alpha/2}^{\alpha}\mu N_t(\alpha)d\mu\\
&=
\frac{3}{16}\alpha^3N_t(\alpha).
\end{aligned}
\]

Thus

\[
\boxed{
\sup_{\alpha\ge2L}\alpha^3N_t(\alpha)
\le
\frac{16}{3}
\sup_{\ell\ge L}K_\ell^{phys}(t).
}
\]

Therefore uniform vanishing of the `K` tail and uniform vanishing of the high-amplitude weak-`L3` tail are quantitatively equivalent up to fixed constants.

## 5. Exact Leray/physical correspondence

For

\[
\tau=T_*-t,
\qquad
\lambda=L\sqrt\tau,
\qquad
U(Y,s)=\sqrt\tau\,u(x,t),
\]

one has

\[
\boxed{
K(U(s);\lambda)
=K_L^{phys}(t).
}
\]

Hence the DSD zero-amplitude Leray boundary coordinate is precisely the physical high-amplitude critical tail seen along a fixed physical velocity level.

## 6. Contrapositive blow-up certificate

If `T*` is genuinely singular, then for every finite `L` and every `t0<T*`,

\[
\boxed{
\sup_{t_0<t<T_*}
\|u(t)\mathbf1_{\{|u(t)|>L\}}\|_{3,\infty}
>\varepsilon_\nu.
}
\]

Equivalently, the high-amplitude critical tail cannot become uniformly small on any terminal time interval.

This is a rigorous necessary condition for blow-up and is the physical counterpart of the positive W1 boundary defect.

## 7. What remains open

The lemma proves

\[
\boxed{
\text{uniform critical `K`-tightness}
\Longrightarrow
\text{regularity}.
}
\]

It does **not** prove that finite energy, finite ordinary dissipation, or the currently established DSD structural constraints force that tightness. A critical `1/r` corridor is compatible with those subcritical budgets.

Therefore the remaining Millennium-level step is the reverse implication needed on the hypothetical singular corridor: a genuinely new critical mechanism must force the high-amplitude weak-`L3` tail below the absorption threshold, or otherwise directly rule out the corresponding W1 recurrent endpoint.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
