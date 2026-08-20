# Leray H1 Recurrence Tax — 2026-08-20

Status: **STRICT RECURRENT-ORBIT THRESHOLD — GLOBAL REGULARITY NOT PROVED.**

This note strengthens the non-H/T Type-I ancient endgame by rewriting the exact physical H1 strain ledger in autonomous backward-Leray variables.

## 1. Backward Leray variables

Let `tau<0` be ancient physical time and set

\[
a=-\tau,
\qquad
s=-\log a,
\qquad
Y=y/\sqrt a.
\]

Write

\[
U(y,\tau)=a^{-1/2}V(Y,s).
\]

If `S=sym grad_y U`, define

\[
\Sigma(Y,s)=\operatorname{sym}\nabla_YV=aS.
\]

The physical exact H1 ledger is

\[
\frac12\frac d{d\tau}\|\nabla_yS\|_2^2
+\nu\|\Delta_yS\|_2^2
=N(S).
\]

## 2. Exact scaling of the three H1 quantities

Define

\[
P(s)=\|\nabla_Y\Sigma\|_2^2,
\qquad
H(s)=\|\Delta_Y\Sigma\|_2^2,
\qquad
N_L(s)=N(\Sigma).
\]

Then

\[
\|\nabla_yS\|_2^2=a^{-3/2}P(s),
\]

\[
\|\Delta_yS\|_2^2=a^{-5/2}H(s),
\]

and the cubic H1 production has the same critical scaling,

\[
N(S)=a^{-5/2}N_L(s).
\]

Since

\[
\frac{ds}{d\tau}=a^{-1},
\]

we have

\[
\frac d{d\tau}\left(a^{-3/2}P\right)
=a^{-5/2}\left(P_s+\frac32P\right).
\]

Therefore the exact autonomous Leray H1 identity is

\[
\boxed{
\frac12P_s
+\frac34P
+\nu H
=N_L.
}
\]

The additional positive term `3P/4` is the similarity-coordinate recurrence tax.

## 3. Exact periodic orbit consequence

If a nonzero Leray profile were periodic with period `T`, integration over one period gives

\[
\boxed{
\int_0^T N_Lds
=\nu\int_0^THds
+\frac34\int_0^TPds.
}
\]

Hence its H-weighted mean production quotient satisfies

\[
\boxed{
\frac{\int N_Lds}{\int Hds}
=
\nu+rac34
\frac{\int Pds}{\int Hds}
>\nu.
}
\]

Thus exact discrete self-similar recurrence pays a strictly super-viscous H1 threshold even before invoking any external DSS Liouville theorem.

## 4. Precompact recurrent class

Let `K` be a genuinely precompact non-H/T Leray profile class in `H^2`, with the previously established nonvanishing mass floor, and assume the recurrent orbit remains in `K`.

For every nonzero whole-space finite-energy profile,

\[
P>0,
\qquad
H>0.
\]

Compactness and nonvanishing therefore imply

\[
\boxed{
\kappa_K
:=\inf_{\Sigma\in K}\frac{P(\Sigma)}{H(\Sigma)}>0,
}
\]

and also

\[
h_K:=\inf_{\Sigma\in K}H(\Sigma)>0.
\]

Define the variational production ceiling

\[
\Lambda_K
:=\sup_{\Sigma\in K}\frac{N_L(\Sigma)}{H(\Sigma)}.
\]

## 5. Recurrence raises the necessary variational threshold

Take recurrent return pairs `s_n<t_n` satisfying

\[
\|\Sigma(t_n)-\Sigma(s_n)\|_{H^2}\to0
\]

with a nontrivial return-time lower bound

\[
t_n-s_n\ge\ell_0>0.
\]

Integrating the Leray H1 identity gives

\[
\frac12(P(t_n)-P(s_n))
+\frac34\int_{s_n}^{t_n}Pds
+\nu\int_{s_n}^{t_n}Hds
=\int_{s_n}^{t_n}N_Lds.
\]

Using

\[
P\ge\kappa_KH
\]

and

\[
N_L\le\Lambda_KH,
\]

we obtain

\[
\left(
\Lambda_K-\nu-\frac34\kappa_K
\right)
\int_{s_n}^{t_n}Hds
\ge
\frac12(P(t_n)-P(s_n)).
\]

The endpoint difference tends to zero, while

\[
\int_{s_n}^{t_n}Hds
\ge h_K\ell_0>0.
\]

Therefore recurrence forces

\[
\boxed{
\Lambda_K
\ge
\nu+\frac34\kappa_K.
}
\]

This strictly strengthens the previous necessary condition

\[
\Lambda_K\ge\nu.
\]

## 6. Double-gap compatibility test

The earlier finite-energy saturation analysis gives a class-dependent strict efficiency loss. If

\[
N_L
\le
(1-\delta_K)\frac4{\sqrt6}
\int|\Sigma||\nabla\Sigma|^2,
\]

then, with

\[
B_K=\sup_{K}\|\Sigma\|_\infty,
\qquad
\kappa_K^+=\sup_K P/H,
\]

we obtain the class ceiling

\[
\Lambda_K
\le
(1-\delta_K)\frac4{\sqrt6}B_K\kappa_K^+.
\]

A recurrent non-H/T survivor must therefore satisfy the simultaneous necessary inequality

\[
\boxed{
(1-\delta_K)\frac4{\sqrt6}B_K\kappa_K^+
\ge
\nu+\frac34\kappa_K.
}
\]

This is a new compact-class exclusion test. The left side contains the previously identified algebraic/geometric saturation defect; the right side now contains a strictly positive recurrence tax.

## 7. Consequence for the proof strategy

The local variational target should be upgraded from

\[
\Lambda_K<\nu
\]

to the weaker requirement sufficient to exclude recurrent Type-I survival:

\[
\boxed{
\Lambda_K
<
\nu+\frac34\kappa_K.
}
\]

This is potentially easier because `kappa_K>0` follows automatically from genuine H2 precompactness plus nonvanishing.

Equivalently, one no longer has to beat viscosity alone by a uniform margin at every profile. It is enough to show that the compact class cannot simultaneously overcome viscosity **and** the Leray recurrence tax.

Status: **A PRECOMPACT NONVANISHING RECURRENT LERAY `P_V` CLASS MUST SATISFY `Lambda_K >= nu + 3 kappa_K/4`, WHERE `kappa_K=inf(P/H)>0`. THIS STRICTLY RAISES THE VARIATIONAL THRESHOLD AND CREATES A SECOND, DYNAMIC GAP ON TOP OF THE EARLIER STATIC H1 SATURATION GAP.**