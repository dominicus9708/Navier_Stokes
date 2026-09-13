# M19-231 — Expanding-cavity unit modes have a core-compactness or escape-to-infinity dichotomy

**Date:** 2026-09-14  
**Status:** ACTIVE CALCULATION / EXPANDING-CAVITY CONCENTRATION-COMPACTNESS REDUCTION

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Purpose

M19-230 reduces the finite-spectator adjoint-extension problem to the Fredholm compatibility of the compact zero-boundary cavity monodromy. Its cokernel is represented by primal zero-boundary unit modes on a spectator ball.

The next question is what such cavity unit modes can do as the spectator radius tends to infinity.

This module proves a basic but important dichotomy: after normalization and subsequence extraction, an expanding sequence of cavity unit modes either retains nonzero mass in a fixed core and converges locally to a nonzero whole-space relative-periodic linearized mode, or its entire normalized mass escapes every fixed compact set.

The result does not exclude either branch. It separates the genuinely interior obstruction from a new remote-escape obstruction.

## 2. Expanding-cavity setup

Let

\[
R_j\to\infty
\]

and let \(U_j\) be backgrounds in the retained compact bounded-period corridor. Write the corresponding periods and rotational holonomies as

\[
S_j\in[S_*,S^*],
\qquad
Q_j\in SO(3),
\qquad
0<S_*\le S^*<\infty.
\]

After subsequence extraction,

\[
S_j\to S_\infty,
\qquad
Q_j\to Q_\infty,
\qquad
U_j\to U_\infty
\]

in the retained local smooth topology on every fixed compact spacetime cylinder.

Let \(w_j\) be a nonzero primal zero-boundary unit-multiplier mode associated with the cokernel of the M19-230 adjoint cavity problem. Thus, up to the fixed return convention,

\[
\boxed{
\begin{aligned}
\partial_s w_j
&=L_{U_j}(s)w_j-\nabla\pi_j,
\\
\nabla\cdot w_j&=0,
\\
w_j|_{|y|=R_j}&=0,
\\
w_j(S_j)&=\mathcal R_{Q_j}w_j(0).
\end{aligned}}
\]

Normalize by one-period spacetime mass:

\[
\boxed{
\int_0^{S_j}\|w_j(s)\|_{L^2(B_{R_j})}^2\,ds=1.
}
\]

The relative return lets us extend \(w_j\) to all similarity times by repeated period/rotation continuation.

## 3. Local parabolic compactness on every fixed core

Fix

\[
0<r<r'<\infty.
\]

For all sufficiently large \(j\),

\[
B_{r'}\Subset B_{R_j}.
\]

On \(B_{r'}\), the coefficients of the linearized equation are uniformly bounded in every finite smooth norm because the background corridor is locally compact and smooth.

Standard interior estimates for the linearized Navier--Stokes/Oseen system therefore give, on every compact time interval and after using the global period-mass normalization, uniform local bounds of the schematic form

\[
\boxed{
\|w_j\|_{L^2_sH^1_y(B_r)}
+\|\partial_sw_j\|_{L^2_sH^{-1}_y(B_r)}
\le C(r,r',S^*).
}
\]

With one further interior bootstrap on a slightly smaller cylinder, the retained smooth coefficients give the regularity needed to pass the equation and the relative return to the limit.

By Aubin--Lions/local parabolic compactness, a diagonal subsequence satisfies

\[
\boxed{
w_j\to w_\infty
\quad\text{strongly in }L^2_{\mathrm{loc}}(\mathbb R_s\times\mathbb R^3_y),
}
\]

with weak convergence of the corresponding first derivatives on compact sets.

The pressure can be normalized locally and recovered from the divergence constraint; it creates no boundary obstruction on a fixed core because \(R_j\to\infty\).

## 4. The limit solves the whole-space linearized equation

Passing to the limit in the local weak formulation yields

\[
\boxed{
\partial_sw_\infty
=L_{U_\infty}(s)w_\infty-\nabla\pi_\infty,
\qquad
\nabla\cdot w_\infty=0
}
\]

on all of

\[
\mathbb R^3\times\mathbb R.
\]

The boundary condition disappears because the boundary radius diverges.

Using the relative-periodic extensions before taking the limit gives

\[
\boxed{
w_\infty(S_\infty)
=\mathcal R_{Q_\infty}w_\infty(0),
}
\]

and hence the same relative-periodic relation for every shifted period.

Fatou/local exhaustion also gives

\[
\int_0^{S_\infty}\int_{\mathbb R^3}|w_\infty|^2\,dy\,ds
\le1,
\]

so the limit is a finite one-period spacetime-energy linearized mode whenever it is nonzero.

## 5. Core-tight branch

Suppose there exist a fixed radius \(r_0<\infty\), a number \(\delta>0\), and a subsequence such that

\[
\boxed{
\int_0^{S_j}\int_{B_{r_0}}|w_j|^2\,dy\,ds
\ge\delta.
}
\]

Strong local \(L^2\) convergence then gives

\[
\int_0^{S_\infty}\int_{B_{r_0}}|w_\infty|^2\,dy\,ds
\ge\delta,
\]

and therefore

\[
\boxed{w_\infty\not\equiv0.}
\]

Thus any persistent core mass produces a genuine nonzero whole-space relative-periodic solution of the linearized Navier--Stokes equation around a retained limiting background.

This is the **core-compactness branch**.

## 6. Escape-to-infinity branch

If the core-tight alternative fails, then for every fixed \(r<\infty\),

\[
\boxed{
\int_0^{S_j}\int_{B_r}|w_j|^2\,dy\,ds
\longrightarrow0.
}
\]

Because the total one-period mass is normalized to one, the mass leaves every fixed compact set:

\[
\boxed{
\forall r<\infty:
\quad
\int_0^{S_j}\int_{B_{R_j}\setminus B_r}|w_j|^2\,dy\,ds
\longrightarrow1.
}
\]

This is the **escape-to-infinity branch**.

No claim is made that the escaping mass lies in a thin shell adjacent to \(R_j\); it may live at any radius \(\rho_j\to\infty\) with \(\rho_j\le R_j\). This distinction matters for the next calculation.

## 7. Exact dichotomy

Combining the two cases gives

\[
\boxed{
\begin{array}{c}
\text{normalized expanding-cavity unit modes}
\\[2mm]
\Downarrow
\\[2mm]
\text{nonzero whole-space relative-periodic linearized limit}
\\
\text{or}
\\
\text{one-period }L^2\text{ mass escapes every fixed compact set.}
\end{array}}
\]

Equivalently, failure of compactness of the cavity Fredholm obstruction is now typed as spatial escape rather than an unclassified loss.

## 8. Scope firewall: the core limit is not automatically a hard kernel

The cavity cokernel in M19-230 lives in the full zero-boundary solenoidal cavity space. A core limit \(w_\infty\) is therefore a whole-space relative-periodic linearized mode, but it has not yet been shown to lie in the finite-dimensional hard spectral bundle used in M19-202--228.

Hence

\[
\boxed{
\text{nonzero core limit}
\neq
\text{certified nonsymmetry hard kernel}
}
\]

without a separate spectral/observability membership bridge.

This prevents an illegitimate return from the cavity Fredholm reduction directly to the already finite hard resonance list.

## 9. Consequence for the bounded-period frontier

M19-230's cavity compatibility obstruction can now fail only through one of two typed mechanisms:

\[
\boxed{
\mathcal T_{cav}^{comp}
\subset
\mathcal T_{cav}^{core}
\cup
\mathcal T_{cav}^{esc}.
}
\]

Here

\[
\boxed{
\mathcal T_{cav}^{core}:
\text{classify/exclude the nonzero whole-space relative-periodic linearized core limits},
}
\]

and

\[
\boxed{
\mathcal T_{cav}^{esc}:
\text{exclude or classify cavity unit mass escaping to similarity infinity.}
}
\]

The next calculation should attack the escape branch using the remote asymptotic smallness

\[
U=O(r^{-1}),
\qquad
\nabla U=O(r^{-2}),
\]

while retaining the exact similarity drift. A simple unweighted-energy argument must be audited first, because the similarity operator contributes a positive \(+\frac14\|w\|_2^2\) term in the velocity energy balance.

---

\[
\boxed{\text{M19-231 COMPLETE: CAVITY UNIT-MODE NONCOMPACTNESS IS NOW TYPED AS CORE LIMIT OR SPATIAL ESCAPE.}}
\]
