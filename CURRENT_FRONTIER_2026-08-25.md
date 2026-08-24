# Current frontier — 2026-08-25

Status: **ACTIVE PROOF CHALLENGE — GLOBAL REGULARITY NOT PROVED**

This file records the newest narrowed frontier after the 2026-08-25 first-hitting / strain-kernel calculations.  It supplements the older `CURRENT_STATUS.md` and `CURRENT_ROUTE.md` without rewriting their historical sections.

## 1. Gradient first hitting

For `M(t)=||nabla u||_infty`, the maximum-norm equation gives

\[
D^+M\le M^2+\|\nabla^2p\|_\infty.
\]

Thus abnormally compressed gradient first-hitting epochs require normalized pressure-Hessian occupancy.  At the natural radius `r=(nu/M)^{1/2}`, the pressure Hessian splits into

\[
\frac{\|\nabla^2p\|_\infty}{M^2}
\lesssim
1+H_{2,r}+\mathcal T_r,
\]

where `H_{2,r}` is a normalized local velocity-Hessian amplitude and `mathcal T_r` is a `2^{-4 ell}` remote shell-gradient tail.

The positive viscosity/high-derivative branch is pruned at the raw gradient maximum: viscosity has favorable sign there.

## 2. Vorticity first hitting

For `W(t)=||omega||_infty`, pressure disappears:

\[
D^+W\le W\,\|S\|_\infty.
\]

At the natural radius

\[
r=(\nu/W)^{1/2},
\]

the far strain obeys

\[
\frac{|S_{>r}|}{W}
\lesssim
\left(\frac r{\nu^2}\|\omega\|_2^2\right)^{1/2}.
\]

This gives a direct first-order energy/enstrophy channel.

## 3. Even strain-kernel cancellation

The strain singular-integral kernel is degree `-3`, even, and has zero spherical average.  On a centered ball, both the constant and linear vorticity Taylor jets cancel.  Therefore

\[
|S_{<r}(x)|
\lesssim
r^2\|\nabla^2\omega\|_{L^\infty(B_r(x))}.
\]

The first-vorticity-derivative branch is not an independent near-strain survivor.

## 4. Direction-contracted refinement

At a maximum-vorticity point with direction `xi_*`, the scalar stretching

\[
\gamma=\xi_*^TS\xi_*
\]

depends only on vorticity transverse to `xi_*`.  The same parity cancellation yields

\[
\boxed{
|\gamma_{<r}(x_*)|
\lesssim
r^2\sup_{B_r(x_*)}
|\xi_*\times\nabla^2\omega|.
}
\]

At the exact maximum, magnitude Hessian is projected out:

\[
\xi_*\times\partial_{ab}\omega(x_*)
=W\,\xi_*\times\partial_{ab}\xi(x_*).
\]

Thus the genuine second-order local survivor is direction curvature / axis conversion rather than magnitude curvature.

## 5. First-hitting energy gate

For first-hitting levels `W_j=q^jW_0`, let

\[
\Theta_j=W_{j-1}(t_j-t_{j-1})
=\frac{\nu(t_j-t_{j-1})}{r_{j-1}^2},
\]

and

\[
\mathfrak Z_j
=\frac1{\nu r_{j-1}}
\int_{I_j}\|\omega(t)\|_2^2dt.
\]

If `mathfrak Q_{2,j}` denotes the normalized time occupancy of the transverse second-vorticity-derivative channel, then

\[
\boxed{
1-q^{-1}
\lesssim
\mathfrak Q_{2,j}
+\sqrt{\Theta_j\mathfrak Z_j}.
}
\]

Hence on a transverse-second-derivative-quiet epoch,

\[
\boxed{
\mathfrak Z_j\gtrsim_q\Theta_j^{-1}.
}
\]

The global energy identity yields

\[
\sum_jr_{j-1}\mathfrak Z_j
\le
L_E,
\qquad
L_E=E_0/\nu^2.
\]

Therefore the quiet branch must obey

\[
\boxed{
\sum_{j\in Q_2}
\frac{r_{j-1}/L_E}{\Theta_j}<\infty.
}
\]

In particular, infinitely many epochs with

\[
|I_j|\lesssim\frac{r_{j-1}^3}{\nu L_E}
\]

cannot all remain transverse-second-derivative quiet.

## 6. Direction-curvature descent

For

\[
b=r^2|P_{\xi^\perp}\nabla^2\xi(x_*)|,
\qquad
k_3=r^3\|\nabla^3\xi\|_\infty,
\]

a Taylor persistence lemma gives a descended radius

\[
\delta\gtrsim r\min\{1,b/(1+k_3)\}.
\]

If high vorticity occupies the descended ball, then the critical palinstrophy cost satisfies

\[
\boxed{
\frac{\mathcal P_\delta}{\nu^2}
\gtrsim
b^2
\min\left\{1,
\left(\frac b{1+k_3}\right)^8
\right\}.
}
\]

If high-vorticity occupancy fails, the branch enters the existing sparseness/segregation track.  If the occupied palinstrophy cost is small, then

\[
1+k_3\gtrsim\varepsilon^{-1/8}b^{5/4}.
\]

Thus direction curvature reduces to palinstrophy, occupancy failure, or a third-direction-derivative escalation.

## 7. Current survivor tree

The latest local first-hitting tree is

\[
\boxed{
\text{candidate singular growth}
\Longrightarrow
\begin{cases}
\text{far enstrophy/energy tax},\\
\text{high-vorticity sparsity or segregation},\\
\text{critical palinstrophy packets},\\
\text{third-and-higher direction/vorticity derivative needles}.
\end{cases}
}
\]

The arbitrary first-vorticity-derivative and arbitrary magnitude-Hessian branches have been pruned from the near vortex-stretching survivor.

## 8. Main unresolved closure

A global contradiction still requires proving that an infinite cascade cannot keep distributing itself among the last three geometric branches while respecting the available global energy/enstrophy ledger.

The next strongest target is a **genealogy summability lemma** linking repeated palinstrophy/sparseness/derivative packets across first-hitting generations to a nonsummable lower-order cost.

Global regularity remains **UNPROVED**.
