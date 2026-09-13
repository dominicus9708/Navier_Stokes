# M19-248 — A fixed-thickness regular poloidal shell is excluded by half-line L2 rigidity

**Date:** 2026-09-14  
**Status:** ACTIVE CALCULATION / FIXED-THICKNESS SHELL RIGIDITY

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Purpose

M19-247 finds the canonical leading fixed-distance poloidal shell normal form

\[
v_T=2d\nabla_{S^2}p_0,
\qquad
v_r=d^2\Delta_{S^2}p_0.
\]

Locally this exactly saturates the M19-246 pressure-work currency. The present module asks whether this local normal form can be a globally tight fixed-thickness shell on the expanding cavity.

The answer is no under the retained regular compactness assumptions: the tangential profile grows linearly in the inward distance and cannot belong to the half-line \(L^2\) space unless it is zero.

## 2. Fixed-distance shell blow-up

Let \(R_j\to\infty\), and write

\[
d=R_j-r\in[0,R_j].
\]

For a fixed-thickness boundary shell define

\[
V_{T,j}(d,\omega,s)
:=R_j w_{T,j}(R_j-d,\omega,s),
\]

\[
V_{r,j}(d,\omega,s)
:=R_j^2 w_{r,j}(R_j-d,\omega,s),
\]

and

\[
P_j(d,\omega,s):=R_j^{-1}\pi_j(R_j-d,\omega,s).
\]

Since

\[
dy=(R_j-d)^2dd\,d\omega
=R_j^2(1+o(1))dd\,d\omega
\]

on every fixed \(d\)-interval, the tangential shell \(L^2\) norm becomes the ordinary half-line norm of \(V_{T,j}\).

## 3. Tight regular-shell hypotheses

Consider the retained branch in which:

1. a positive fraction of the normalized one-period velocity mass remains at bounded physical distance from the wall;
2. \(V_{T,j}\) is locally compact in \(L^2_{d,\omega,s}\) and has enough bounded scaled radial/angular/time derivatives to pass the leading shell equation;
3. \(P_j\) has a locally compact leading angular component;
4. the leading critical radial background coefficient is zero, as in M19-244;
5. no scaled-derivative/frequency decompactification occurs.

Any failure of item 2, 3, or 5 is assigned to the already open scaled-derivative/frequency decompactification branch rather than silently treated as regular shell compactness.

Let

\[
V_{T,j}\to V_T,
\qquad
P_j\to p_0
\]

locally along a subsequence.

## 4. Leading half-line equations

M19-247 gives in the limit

\[
\boxed{\partial_dp_0=0,}
\]

and

\[
\boxed{\frac12\partial_dV_T=\nabla_{S^2}p_0.}
\]

The fixed H1 currency plus the M19-245 boundary impedance forces the leading outer trace

\[
\boxed{V_T(0,\omega,s)=0.}
\]

Therefore

\[
\boxed{
V_T(d,\omega,s)
=2d\nabla_{S^2}p_0(\omega,s).
}
\]

## 5. Half-line L2 rigidity

A fixed-thickness tight shell limit must satisfy

\[
V_T\in
L^2\big([0,\infty)_d\times S^2\times[0,S]\big).
\]

But

\[
\int_0^\infty|V_T|^2dd
=
4|\nabla_{S^2}p_0|^2
\int_0^\infty d^2dd.
\]

Hence finiteness is possible only if

\[
\boxed{\nabla_{S^2}p_0=0.}
\]

Then

\[
\boxed{V_T\equiv0.}
\]

The leading incompressibility relation

\[
\partial_dV_r=\operatorname{div}_{S^2}V_T,
\qquad
V_r(0)=0
\]

also gives

\[
\boxed{V_r\equiv0.}
\]

Thus the entire regular fixed-thickness shell limit vanishes.

## 6. Contradiction with fixed-thickness tightness

By hypothesis, a positive normalized mass fraction survives in bounded \(d\). Local compactness would transfer that mass to the half-line limit. But the only admissible leading limit is zero.

Therefore

\[
\boxed{
\text{nonzero radial-free regular cavity escape cannot remain tight at physical boundary distance }d=O(1).
}
\]

The local M19-247 pressure-supported profile is therefore a correct **local asymptotic shape**, but it cannot extend to a nonzero square-integrable half-line shell without a further scale or loss of compactness.

## 7. Consequence

A surviving radial-free escape sequence must do at least one of the following:

\[
\boxed{
\begin{array}{l}
\text{(i) spread to a boundary distance }D_j\to\infty,\\
\text{(ii) lose scaled radial/angular/time compactness,}\\
\text{(iii) leave the radial-free critical branch,}\\
\text{(iv) enter the macroscopic }d\asymp R_j\text{ regime.}
\end{array}}
\]

The macroscopic regular regime is already constrained by M19-238--239. The next calculation is therefore to repeat the shell scaling for a general mesoscopic thickness

\[
1\ll D_j\ll R_j
\]

and determine whether a regular single-scale mesoscopic shell can survive.

## 8. Scope firewall

The theorem is a compactness-rigidity statement. It does not say that every sequence has a strong fixed-distance shell limit.

Therefore

\[
\boxed{
\text{zero regular fixed-thickness limit}
\neq
\text{strong compactness of every escaping cavity sequence}.
}

Any failure of the hypotheses is retained explicitly as decompactification rather than counted as closure.
