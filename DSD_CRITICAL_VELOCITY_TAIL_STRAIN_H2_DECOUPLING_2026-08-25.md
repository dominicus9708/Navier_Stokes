# DSD critical velocity-tail / strain-H2 decoupling audit

Date: 2026-08-25

Status: **1/r VELOCITY TAIL SHOWN H2-NEGLIGIBLE IN STRAIN / NON-L3 VELOCITY ESCAPE DOES NOT BY ITSELF DESTROY STRAIN-H2 PRECOMPACTNESS / LERAY H1 RECURRENCE TAX REMAINS APPLICABLE ON A STRAIN-COMPACT SURVIVOR / GLOBAL REGULARITY UNPROVED.**

This note continues `DSD_CORE_TAIL_STATIC_COMPATIBILITY_DYNAMIC_MAINTENANCE_2026-08-25.md` and `DSD_FIRST_HITTING_LERAY_CLOCK_COBBOUNDARY_2026-08-25.md`.

The purpose is to separate two topologies that must not be conflated:

1. the velocity `L3` topology needed by several ancient Liouville theorems;
2. the derivative/strain `H2` topology used by the repository's Leray H1 recurrence tax.

A borderline `1/r` velocity tail can destroy the first while becoming arbitrarily small in the second.

## 1. Critical tail model

Use the divergence-free tail already audited,

\[
U_T(x)=\chi(|x|)\frac{a\times x}{|x|^2},
\]

with `chi=0` for `r<=R0` and `chi=1` for `r>=2R0`.

For `r>=2R0`,

\[
|U_T|\asymp r^{-1},
\qquad
|\nabla U_T|\lesssim r^{-2},
\qquad
|\nabla^2U_T|\lesssim r^{-3},
\qquad
|\nabla^3U_T|\lesssim r^{-4}.
\]

Let

\[
\Sigma_T=\operatorname{sym}\nabla U_T.
\]

Then

\[
|\Sigma_T|\lesssim r^{-2},
\qquad
|\nabla\Sigma_T|\lesssim r^{-3},
\qquad
|\nabla^2\Sigma_T|\lesssim r^{-4}.
\]

The finite cutoff annulus has the same scale order after differentiation of `chi`.

## 2. Tail L2 strain norm

For the remote region,

\[
\int_{|x|>R_0}|\Sigma_T|^2dx
\lesssim
|a|^2\int_{R_0}^{\infty}r^2r^{-4}dr.
\]

Hence

\[
\boxed{
\|\Sigma_T\|_{L^2(|x|>R_0)}^2
\lesssim
\frac{|a|^2}{R_0}.
}
\]

Thus the strain enstrophy carried by a critical non-L3 velocity tail tends to zero as its normalized onset radius moves to infinity.

## 3. Tail H1 strain norm

Similarly,

\[
\int_{|x|>R_0}|\nabla\Sigma_T|^2dx
\lesssim
|a|^2\int_{R_0}^{\infty}r^2r^{-6}dr,
\]

so

\[
\boxed{
\|\nabla\Sigma_T\|_2^2
\lesssim
\frac{|a|^2}{R_0^3}.
}
\]

This is precisely the `P` quantity appearing in the Leray H1 recurrence identity, up to the core contribution.

## 4. Tail H2 strain norm

One more derivative gives

\[
\int_{|x|>R_0}|\nabla^2\Sigma_T|^2dx
\lesssim
|a|^2\int_{R_0}^{\infty}r^2r^{-8}dr,
\]

hence

\[
\boxed{
\|\nabla^2\Sigma_T\|_2^2
\lesssim
\frac{|a|^2}{R_0^5}.
}
\]

For smooth whole-space fields this controls the same order as the `H=||Delta Sigma||_2^2` channel used in the recurrence tax.

Therefore

\[
\boxed{
\|\Sigma_T\|_{H^2}^2
\lesssim
\frac{|a|^2}{R_0}
}
\]

with the leading contribution coming from the L2 strain term.

Status: **PROVED for the explicit critical tail witness.**

## 5. General power-law audit

More generally, suppose a smooth remote velocity tail has derivative decay

\[
|\nabla^mU(x)|\lesssim C_m r^{-1-m}
\qquad(m=0,1,2,3)
\]

for `r>=R0`.

Then

\[
\boxed{
\|\nabla^mU\|_{L^2(|x|>R_0)}^2
\lesssim
R_0^{1-2m}
\qquad(m\ge1).
}
\]

For strain derivatives,

\[
\boxed{
\|\nabla^k\Sigma\|_{L^2(|x|>R_0)}^2
\lesssim
R_0^{-(2k+1)}
\qquad(k=0,1,2).
}
\]

Thus the borderline velocity tail is increasingly negligible at every derivative level used by the H1 recurrence machinery.

## 6. Why velocity L3 still fails

The same tail has

\[
\int_{|x|>R_0}|U_T|^3dx
\asymp
\int_{R_0}^{\infty}\frac{dr}{r}
=\infty.
\]

Therefore

\[
\boxed{
U_T\notin L^3
\quad\text{while}\quad
\Sigma_T\in H^2.
}
\]

This is not a paradox. The two statements live at different derivative orders and different criticalities.

The ancient Liouville escape and the strain recurrence compactness must therefore be recorded as separate DSD channels.

## 7. Compact-core plus escaping-tail sequence

Let `Sigma_C` be a fixed smooth compactly supported nonzero strain-compatible core and let `Sigma_{T,n}` be critical tails whose onset radii satisfy

\[
R_n\to\infty.
\]

Then

\[
\|\Sigma_{T,n}\|_{H^2}\to0.
\]

Consequently

\[
\boxed{
\Sigma_n:=\Sigma_C+\Sigma_{T,n}
\to\Sigma_C
\quad\text{strongly in }H^2.
}
\]

At the same time the associated velocities may satisfy

\[
U_n\notin L^3
\]

for every `n`.

Hence a sequence can be perfectly precompact in strain `H2` while **never entering the global velocity L3 class**.

Status: **PROVED AS A FUNCTIONAL-TOPOLOGY SEPARATION.**

## 8. Consequence for the Leray H1 recurrence tax

The repository already proves that on a nonzero precompact recurrent strain class `K subset H2`,

\[
\boxed{
\frac12P_s+\frac34P+\nu H=N_L
}
\]

forces

\[
\boxed{
\Lambda_K
:=\sup_K\frac{N_L}{H}
\ge
\nu+\frac34\kappa_K,
\qquad
\kappa_K:=\inf_K\frac{P}{H}>0.
}
\]

The present audit shows that a passive global non-L3 velocity tail does not invalidate this argument merely by existing.

If the strain class remains `H2` precompact and nonvanishing, the recurrence tax continues to apply even while the velocity tail escapes the global `L3` Liouville class.

Therefore

\[
\boxed{
\text{non-L3 velocity tail}
\not\Longrightarrow
\text{loss of strain-H2 recurrence compactness}.
}
\]

## 9. DSD routing

The remaining survivor should be split into two independently audited channels.

### V-tail channel

\[
U\notin L^3
\]

through a critical `1/r`-type velocity shell stack.

This defeats the simple global `L3` ancient Liouville theorem.

### S-recurrence channel

The strain trajectory remains in a nonzero `H2`-precompact recurrent class and must satisfy

\[
\Lambda_K\ge\nu+\frac34\kappa_K.
\]

This channel is not neutralized by the V-tail.

A full singular survivor must satisfy both simultaneously.

## 10. Sharpened LRMG

The Leray Recurrent Motion Gate can now be stated more narrowly:

\[
\boxed{
\begin{gathered}
\text{Can a nonzero H2-precompact recurrent strain trajectory sustain}\
\Lambda_K\ge\nu+\frac34\kappa_K\n\text{ indefinitely, while the associated velocity carries an H2-negligible but}\
\text{globally non-L3 critical tail and all first-hitting formation constraints hold?}
\end{gathered}
}
\]

The next quantitative target is therefore the production-efficiency inequality

\[
\boxed{
\Lambda_K
\stackrel{?}{<}
\nu+\frac34\kappa_K,
}
\]

or one of its strengthened compatibility-gap versions already developed in the repository.

## 11. Audit verdict

### PROVED

- the explicit `1/r` tail has strain-tail costs `L2 ~ R0^{-1}`, `H1 ~ R0^{-3}`, `H2 ~ R0^{-5}`;
- a non-L3 velocity tail may vanish strongly in strain `H2` as it escapes spatially;
- velocity `L3` noncompactness and strain `H2` precompactness are logically compatible;
- therefore the non-L3 tail does not automatically disable the Leray H1 recurrence tax.

### NOT DERIVED

- H2 precompactness of every possible critical-tail survivor;
- the production-efficiency exclusion `Lambda_K < nu+3 kappa_K/4`;
- LRMG;
- contradiction to the bounded-Z singular branch;
- global regularity.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
