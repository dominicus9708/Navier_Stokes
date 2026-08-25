# DSD W1 Endpoint Lp Residue and Finite-Core Pressure Payer — 2026-08-26

Status: **CRITICAL L3 RESIDUE IDENTIFIED / POSITIVE INVARIANT PRESSURE-WORK PAYER FORCED / REMOTE PRESSURE PAYMENT EXCLUDED BY R^-2 SHELL SUM / FINAL CORE RIGIDITY STILL OPEN.**

## 1. Invariant critical-shell density

From the all-age co-moving transport and invariant-measure construction, the W1 survivor admits a Leray-flow invariant probability measure mu such that

\[
\boxed{
M_{crit}
:=
\lim_{R\to\infty}
\int\Psi_R(U)d\mu(U)>0,
}
\]

where

\[
\Psi_R(U)=\int_{R<|Y|<2R}|U(Y)|^3dY.
\]

The result holds for the periodic branch and, after the all-age empirical-measure argument, for the aperiodic recurrent branch as well, conditional on the Barker--Prange positive-density input.

## 2. Abelian endpoint residue

Let

\[
p=3+\varepsilon,
\qquad \varepsilon>0.
\]

On a dyadic shell R_k=2^kR_0, set

\[
V_k(z)=R_kU(R_kz),
\qquad 1<|z|<2.
\]

Then

\[
\int_{A_{R_k}}|U|^{3+\varepsilon}dY
=
R_k^{-\varepsilon}
\int_A|V_k|^{3+\varepsilon}dz.
\]

The W1 annular H1 ceiling gives a uniform L6 bound for V_k. Hence the family |V_k|^{3+epsilon} is uniformly integrable for small epsilon, and

\[
\int_A|V_k|^{3+\varepsilon}dz
\to
\int_A|V_k|^3dz
\]

uniformly in the far-shell family as epsilon->0 after the standard finite-core/far-tail split.

Averaging in mu and using

\[
M_\mu(R_k)\to M_{crit},
\]

the dyadic Abelian sum gives

\[
\boxed{
\lim_{\varepsilon\downarrow0}
\varepsilon
\int
\|U\|_{3+\varepsilon}^{3+\varepsilon}
\,d\mu(U)
=
\frac{M_{crit}}{\log2}
=:\mathscr R_3>0.
}
\]

Indeed

\[
\varepsilon
\sum_{k\ge0}R_k^{-\varepsilon}
\sim
\frac1{\log2}
\]

after the harmless fixed factor R_0^{-epsilon}->1.

Thus the 1/r center-mode memory appears as the pole residue of the subcritical Lp norms at p=3+.

## 3. Exact Leray Lp balance

For p>3, multiply the Leray velocity equation by |U|^{p-2}U and integrate over R3. The transport nonlinearity vanishes by incompressibility. One obtains

\[
\boxed{
\frac1p\frac d{ds}\|U\|_p^p
+
\frac{p-3}{2p}\|U\|_p^p
+
\nu D_p(U)
=
\Pi_p(U),
}
\]

where

\[
D_p(U)
=
\int
|U|^{p-2}|\nabla U|^2
+
(p-2)|U|^{p-4}
\sum_j(U\cdot\partial_jU)^2
\,dY
\ge0
\]

(up to the usual equivalent vector diffusion form), and

\[
\Pi_p(U)
:=
\int P\,\nabla\cdot(|U|^{p-2}U)dY
\]

is the pressure-work term.

## 4. Average over the recurrent invariant measure

For each fixed p>3, the W1 compact orbit has uniformly bounded Lp norm, so the generator average of the Lp observable vanishes under mu. Hence

\[
\boxed{
\frac{p-3}{2p}
\int\|U\|_p^p d\mu
+
\nu\int D_p\,d\mu
=
\int\Pi_p\,d\mu.
}
\]

Since D_p>=0,

\[
\int\Pi_p\,d\mu
\ge
\frac{p-3}{2p}
\int\|U\|_p^p d\mu.
\]

Taking p down to 3 and using the residue gives

\[
\boxed{
\liminf_{p\downarrow3}
\int\Pi_p\,d\mu
\ge
\frac{\mathscr R_3}{6}
=
\frac{M_{crit}}{6\log2}
>0.
}
\]

Thus positive critical memory forces positive mean near-endpoint pressure work.

No limit of the diffusion term is required for this lower bound.

## 5. Remote pressure work is summable

Use the established old-shell W1/Type-I pressure bounds on a shell A_R:

\[
\|P-(P)_{A_R}\|_{L^2(A_R)}
\le C_PR^{-1/2},
\]

\[
\|U\|_{L^\infty(A_R)}
\le A_0R^{-1},
\qquad
\|\nabla U\|_{L^2(A_R)}
\le G_0R^{-1/2}.
\]

For 3<=p<=3+delta,

\[
|\nabla\cdot(|U|^{p-2}U)|
\le C_p|U|^{p-2}|\nabla U|.
\]

Therefore

\[
\boxed{
\|\nabla\cdot(|U|^{p-2}U)\|_{L^2(A_R)}
\le C R^{-(p-3/2)}.
}
\]

After subtracting a pressure gauge on each annulus,

\[
\boxed{
|\Pi_p(A_R)|
\le C R^{-(p-1)}.
}
\]

At p=3 this is R^{-2}. Hence on dyadic shells

\[
\sum_{R_k\ge R_*}
\sup_{3\le p\le3+\delta}
|\Pi_p(A_{R_k})|
\le C R_*^{-2}.
\]

Thus the pressure-work tail is uniformly absolutely summable and can be made arbitrarily small by choosing one fixed normalized radius R_* sufficiently large.

## 6. Finite-core payer

Choose R_* so large that the invariant pressure-work contribution outside B_{R_*} is less than

\[
\frac{\mathscr R_3}{12}.
\]

Then for p sufficiently close to 3,

\[
\boxed{
\int
\Pi_p^{B_{R_*}}(U)d\mu(U)
\ge
\frac{\mathscr R_3}{12}>0.
}
\]

Therefore the center-mode critical memory cannot be maintained by its own remote tail pressure. A fixed finite normalized core must provide a strictly positive mean pressure-compression payment.

Formally at p=3,

\[
\nabla\cdot(|U|U)
=|U|\,\widehat U^T S\widehat U,
\]

so the limiting payer has the geometric form

\[
\Pi_3^{core}
=
\int_{B_{R_*}}
P|U|\,\widehat U^TS\widehat U\,dY
\]

when the p->3 limit is justified.

## 7. Updated final channel

The W1 survivor is now reduced to

\[
\boxed{
M_{crit}>0
\Longrightarrow
\text{positive invariant finite-core critical pressure work}.
}
\]

This is substantially narrower than a generic ancient/recurrent Liouville problem. The remote center-mode memory is asymptotically passive; its maintenance is paid by a bounded-radius pressure/strain-direction correlation in the active recurrent core.

What remains open is a coercive routing of this finite-core pressure payer into one of the already controlled projective/turnover/derivative channels, or a direct proof that such a positive invariant pressure payer is impossible on a compact recurrent Leray orbit.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
