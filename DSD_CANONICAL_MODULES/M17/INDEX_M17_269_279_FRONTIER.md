# M17 continuation frontier — M17-269 through M17-279

Date: 2026-09-06  
Scope: continuation after `INDEX_M17_258_267_FRONTIER.md` and the M17-268 addendum.

This index is additive and does not replace earlier canonical indices.

---

# 1. M17-269 — exact weighted harmonic-map equation for the raw tangent director

For

\[
V=a\xi,
\qquad
\partial_\tau V=\Delta V,
\qquad
\Delta V=K V,
\]

the director satisfies

\[
\boxed{
\Delta\xi
+2\nabla\log a\cdot\nabla\xi
+|\nabla\xi|^2\xi=0.
}
\]

Equivalently,

\[
\boxed{
a^{-2}\nabla\cdot(a^2\nabla\xi)+|\nabla\xi|^2\xi=0.}
\]

A director second-jet spike is therefore classified before coupling it to the M17-145 multiplier commutator.

Bulk `L2` second-jet growth forces first-jet metric growth, log-amplitude coupling, or active-set failure.
A pure `L-infinity` spike with bounded local `L2` mass is a strict smaller derivative scale.

---

# 2. M17-270 — log-amplitude coupling is not free

The exact polar identity is

\[
\boxed{
|\nabla V|^2
=a^2\left(|\nabla\log a|^2+|\nabla\xi|^2\right).
}
\]

On an active corridor `a>=a_*>0`, bulk log-amplitude-gradient growth is normalized palinstrophy.
If the director first jet is unbounded, retain metric escalation.
If only the pointwise log gradient blows up with bounded `L2` mass, retain a strict subscale.
Failure of the amplitude floor is nodal/amplitude degeneration.

---

# 3. M17-271 — first-jet metric escalation reconnects to area/anisotropy

Set

\[
g=|\nabla\xi|^2.
\]

Divergence of

\[
\int g^2
\]

splits as in M17-219 into

\[
\boxed{
G_{fixed\text{-}fraction\ high\ metric}
\lor
G_{metric\ microcarrier}.
}
\]

For Rank 2,

\[
\boxed{
g=2|J_\xi|\mathcal A_\xi.}
\]

Thus the fixed-fraction branch returns to

\[
G_{high\ director\ area}
\lor
G_{high\ anisotropy},
\]

while the microcarrier is a strict subscale.

---

# 4. M17-272 — payer-free parabolic C1-alpha compactness caps regular fold multiplicity

On a fixed payer-free cylinder,

\[
\partial_\tau V_j-\Delta V_j
=-A_j\cdot\nabla V_j+C_jV_j
\]

with bounded local `L2` mass and bounded lower-order coefficients.
Interior parabolic `W^{2,1}_p` estimates for `p>5` give

\[
\boxed{\|V_j\|_{C^{1,\alpha}}\le C.}
\]

With an amplitude floor,

\[
\boxed{\|\xi_j\|_{C^{1,\alpha}}\le C.}
\]

If a regular transverse preimage has

\[
s_2\ge\delta_*>0,
\]

it has a uniform injectivity radius.
Therefore a fixed-area transverse section has uniformly bounded regular multiplicity.

Hence on the payer-free compact heat lane,

\[
\boxed{
G_{fold\ multiplicity}
\Longrightarrow
G_{s_2\to0}
\lor
G_{nodal}
\lor
H_{palinstrophy/mass\ escape}
\lor
G_{ambient/coefficient}.
}
\]

The second-jet spike is no longer an independent final fold escape there.

---

# 5. M17-273 — s2 collapse becomes an actual lower-rank tangent

The same `C1,alpha` compactness gives strong `C1` convergence of directors on active subpatches.
Thus

\[
s_{2,j}\to0
\]

passes to

\[
\boxed{\operatorname{rank}D\xi_\infty\le1.}
\]

If `s1` remains nondegenerate the limit is Rank 1.
If `s1 -> 0` as well, the limit is Rank 0.
Vanishing-measure rank drop remains a microcarrier/subscale branch.

---

# 6. M17-274 — Rank-1 director is a great-circle phase

On a connected Rank-1 patch,

\[
\xi=\gamma(\phi).
\]

The weighted harmonic-map equation forces zero geodesic curvature of `gamma`.
After a fixed rotation,

\[
\boxed{\xi=(\cos\phi,\sin\phi,0).}
\]

The exact Rank-1 system includes

\[
\boxed{
\nabla\cdot(a^2\nabla\phi)=0,
\qquad
\nabla K\cdot\nabla\phi=0,
}
\]

\[
\partial_\tau a=Ka,
\qquad
\Delta a=a(K+|\nabla\phi|^2),
\]

\[
\partial_\tau K=a^{-2}\nabla\cdot(a^2\nabla K),
\qquad
\nabla\cdot(a\xi)=0.
\]

Thus Rank 1 is a scalar amplitude/phase/multiplier system.

---

# 7. M17-275 — global Rank-0 tangent cannot carry sign-balanced K

If

\[
D\xi=0
\]

globally, then

\[
V=a\xi_0,
\qquad
D_{\xi_0}a=0,
\]

so `a` is a nonnegative ancient heat solution in two transverse Euclidean variables:

\[
\partial_\tau a=\Delta_\perp a.
\]

For a nontrivial global entire positive ancient solution, the positive ancient heat representation theorem of Lin--Zhang represents `a` as a positive Laplace transform of positive elliptic modes.
Therefore

\[
\boxed{a_\tau\ge0,
\qquad
K=\partial_\tau\log a\ge0.}
\]

This contradicts the bounded-spike critical sign-balanced `K` survivor.

Reference: F. Lin and Q. S. Zhang, *On Ancient Solutions of the Heat Equation*, CPAM 72 (2019), 2006--2028, DOI `10.1002/cpa.21820`, arXiv `1712.04091`.

Only the **global entire** Rank-0 branch is closed; local Rank-0 patches remain interface/extension problems.

---

# 8. M17-276 — compact closed Rank-1 phase leaves close

Since

\[
\nabla K\cdot\nabla\phi=0,
\]

all `K` variation lies in the two-dimensional phase leaves `S_c`.
The exact multiplier diffusion reduces to

\[
\boxed{
K_\tau=\Delta_SK+b_S\cdot\nabla_SK.
}
\]

On connected compact boundaryless leaves with uniform geometry, bounded drift, and ancient bounded `K`, parabolic mixing gives fixed oscillation contraction.
Iterating from the remote past forces

\[
\boxed{\nabla_SK=0.}
\]

and the normal derivative is already zero, so

\[
\boxed{\nabla K=0.}
\]

This contradicts sign-balanced `K`.

---

# 9. M17-277 — bounded open Rank-1 leaves are interface payers

For a bounded phase leaf with boundary, interior oscillation satisfies

\[
\operatorname{osc}_{S'}K(\tau+\tau_0)
\le
q\operatorname{osc}_S K(\tau)
+C\mathcal B_K.
\]

Ancient boundedness kills the remote-past interior term.
Therefore fixed present sign-balanced oscillation requires recurrent nonzero boundary input:

\[
\boxed{
G_{bounded\ open\ Rank1\ leaf}
\Longrightarrow
G_{phase\text{-}leaf\ boundary/interface\ replenishment}
\lor
G_{geometry/drift/K\ failure}.
}
\]

---

# 10. M17-278 — decompactifying Rank-1 leaves return toward Rank 0 or flux escalation

The phase current

\[
J_\phi=a^2\nabla\phi
\]

is divergence free.
Its flux through a regular phase leaf is

\[
\boxed{
\Phi_\phi(c)=\int_{S_c}a^2|\nabla\phi|\,dA.
}
\]

With amplitude floor and bounded flux, if leaf area tends to infinity then

\[
\fint_{S_c}|\nabla\phi|\to0.
\]

Indeed for every fixed `delta>0`, the leaf-area fraction where

\[
|\nabla\phi|\ge\delta
\]

tends to zero.

Thus bounded-flux leaf decompactification becomes Rank-0 degeneration on dominant leaf area.

---

# 11. M17-279 — phase flux times phase-label width is exactly director energy

On a regular phase tube `phi^-1(I)`, coarea gives

\[
\boxed{
\int_{\phi^{-1}(I)}a^2|\nabla\phi|^2dx
=\int_I\Phi_\phi(c)dc.
}
\]

Without side leakage, `Phi_phi(c)` is constant, hence

\[
\boxed{
E_\phi(I)=\Phi_\phi |I|.
}
\]

Therefore phase-flux escalation over fixed positive phase-label width is normalized palinstrophy.
If palinstrophy stays bounded, flux escalation forces

\[
|I|\to0,
\]

which collapses the great-circle director image and returns toward Rank 0 or a strict interface/subscale.

Thus

\[
\boxed{
G_{Rank1\ leaf\ decompactification}
\Longrightarrow
H_{normalized\ palinstrophy}
\lor
G_{Rank0\ degeneration/image\ collapse}
\lor
G_{nodal/interface/side\ leakage}.
}
\]

---

# 12. Current compressed frontier

The former director-fold / second-jet frontier has been reduced to

\[
\boxed{
\begin{aligned}
R^{hard}
\Longrightarrow{}&
H_{normalized\ palinstrophy}\\
&\lor G_{scaled\ ambient/coefficient}\\
&\lor G_{nodal/amplitude}\\
&\lor G_{rank/interface}\\
&\lor G_{Rank1\ leaf\ boundary/interface}\\
&\lor G_{Rank1\ to\ Rank0\ degeneration}\\
&\lor G_{strict\ vanishing\text{-}measure\ subscale}\\
&\lor G_{K\text{-}spike}.
\end{aligned}
}
\]

The global entire Rank-0 sign-balanced lane is closed.
The compact closed Rank-1 lane is closed.
The remaining lower-rank difficulty is therefore no longer an arbitrary director geometry problem; it is an **extension/interface problem for local Rank-0 degeneration, plus the already existing normalized-palinstrophy/ambient/nodal/K-spike exits**.

The next useful target is to determine whether a local Rank-0 patch produced as a compact tangent can be extended across its rank interface without losing the heat/positivity structure, or whether failure itself carries a quantitative rank-interface / nodal / palinstrophy payment.

---

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
