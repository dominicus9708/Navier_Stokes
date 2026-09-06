# M17 frontier addendum — M17-280 through M17-282

Date: 2026-09-06  
Scope: additive continuation after `INDEX_M17_269_279_FRONTIER.md`.

This addendum does not replace earlier indices.

---

## 1. M17-280 — local Rank-0 open patch is not an extension residual

On a raw heat tangent, if a nonempty open patch has

\[
D\xi=0,
\qquad
\xi=\xi_0,
\]

then every orthogonal constant target component

\[
u_\eta=\eta\cdot V,
\qquad\eta\perp\xi_0
\]

is caloric and vanishes on a nonempty open spacetime set.
Caloric unique continuation gives

\[
\boxed{u_\eta\equiv0.}
\]

Thus the whole connected tangent lies in one fixed target line:

\[
\boxed{V=b\xi_0.}
\]

Divergence free gives

\[
D_{\xi_0}b=0,
\]

so `b` is a two-dimensional scalar ancient heat solution.

If `b` never vanishes, its sign is global and M17-275 closes the positive branch.
If `b` vanishes, the explicit nodal branch is reached.

Therefore a local open Rank-0 patch does not remain an independent extension problem.

---

## 2. M17-281 — K-spikes are excluded on the payer-free compact active raw heat tangent

M17-272 gives local

\[
V_j\in W^{2,1}_p
\]

uniformly for every finite `p` on a smaller cylinder.

With an active amplitude floor,

\[
K_j
=\frac{V_j\cdot\Delta V_j}{|V_j|^2}
\]

is uniformly bounded in every finite `L^p`.

Also

\[
\nabla\log a_j
\]

is uniformly bounded.

The exact multiplier equation is

\[
\partial_\tau K_j
=\Delta K_j+2\nabla\log a_j\cdot\nabla K_j.
\]

Parabolic local boundedness therefore gives

\[
\boxed{\|K_j\|_{L^\infty(Q_{1/2})}\le C.}
\]

Hence a dimensionless K-spike cannot occur while the payer-free compact active corridor remains valid.
Its occurrence returns to

\[
G_{nodal/amplitude}
\lor
H_{normalized\ palinstrophy/mass\ escape}
\lor
G_{scaled\ ambient/coefficient}
\lor
G_{interface/domain}.
\]

---

## 3. M17-282 — bounded stationary nodal domains are principal positive modes

On every raw heat-tangent active nodal domain,

\[
\boxed{
\partial_\tau a
=(\Delta-|\nabla\xi|^2)a.
}
\]

The potential

\[
q=|\nabla\xi|^2
\]

is time independent because the director is time independent.

If a connected nodal domain is bounded, regular, and stationary with Dirichlet boundary `a=0`, then `a` is a globally positive solution of an autonomous Dirichlet parabolic equation.
Positive Dirichlet parabolic uniqueness (Mierczynski, arXiv:1708.06813) and autonomy reduce it to the principal eigenmode:

\[
\boxed{
a(x,\tau)=Ce^{\lambda_1\tau}\varphi_1(x).}
\]

Therefore

\[
\boxed{K=\partial_\tau\log a\equiv\lambda_1.}
\]

A bounded stationary nodal domain cannot carry sign-balanced K.

Remaining nodal exits are

\[
\boxed{
G_{moving\ nodal\ interface}
\lor
G_{unbounded\ nodal\ domain}
\lor
G_{irregular\ nodal\ geometry}
\lor
G_{potential/coefficient\ failure}.
}
\]

---

## 4. Updated narrow frontier

After M17-269--282, the payer-free compact raw heat branch is compressed to

\[
\boxed{
\begin{aligned}
R^{hard}_{compact}
\Longrightarrow{}&
H_{normalized\ palinstrophy}\\
&\lor G_{scaled\ ambient/coefficient}\\
&\lor G_{moving/unbounded/irregular\ nodal\ interface}\\
&\lor G_{rank/interface\ microcarrier}\\
&\lor G_{Rank1\ boundary/side\ leakage}\\
&\lor G_{strict\ vanishing\text{-}measure\ subscale}.
\end{aligned}
}
\]

The following former residuals are no longer independent on this lane:

- director second-jet spike;
- regular fold multiplicity;
- fixed-K coherent-mean mass decompactification;
- dimensionless K-spike;
- global no-node Rank-0 tangent;
- local open Rank-0 extension;
- compact closed Rank-1 leaf;
- fixed-width phase-flux escalation;
- bounded stationary nodal domain.

The next useful target is the **moving/unbounded nodal-interface geometry** and its relation to normalized palinstrophy or ambient/interface replenishment.

---

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
