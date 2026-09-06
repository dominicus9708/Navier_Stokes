# DSD M17-276 — Bounded ancient multiplier on compact Rank-1 phase leaves is constant and excludes sign-balanced K

Date: 2026-09-06  
Canonical ID: **M17-276**

Status: **CONDITIONAL COMPACT-LEAF CLOSURE / M17-274 REDUCES A RANK-1 RAW CE-H HEAT TANGENT TO A GREAT-CIRCLE PHASE `phi` WITH `div(a^2 grad phi)=0` AND `grad K · grad phi=0`. THUS `K` HAS ZERO NORMAL DERIVATIVE ACROSS THE PHASE FOLIATION AND ALL OF ITS SPATIAL VARIATION LIES INSIDE THE TWO-DIMENSIONAL LEAVES `phi=const`. DECOMPOSING THE EXACT MULTIPLIER DIFFUSION `K_tau=a^-2 div(a^2 grad K)` RELATIVE TO A LEAF GIVES A UNIFORMLY PARABOLIC SURFACE EQUATION `K_tau=Delta_S K+b_S·grad_S K`, WHERE THE DRIFT CONTAINS THE TANGENTIAL LOG-AMPLITUDE DRIFT AND THE ACCELERATION OF THE LEAF NORMAL. ON A CONNECTED COMPACT LEAF WITH UNIFORMLY BOUNDED GEOMETRY, AREA/DIAMETER, AND DRIFT, THE PARABOLIC KERNEL HAS A FIXED POSITIVITY/MIXING CONSTANT, SO OSCILLATION CONTRACTS BY A FIXED FACTOR OVER A FIXED TIME. AN ANCIENT UNIFORMLY BOUNDED `K` MUST THEREFORE HAVE ZERO LEAFWISE OSCILLATION. BECAUSE ITS NORMAL DERIVATIVE IS ALREADY ZERO, `K` IS SPATIALLY CONSTANT ON THE CONNECTED RANK-1 PATCH, CONTRADICTING THE CRITICAL SIGN-BALANCED K SURVIVOR. REMAINING EXITS ARE LEAF BOUNDARY/INTERFACE, LEAF DECOMPACTIFICATION/GEOMETRY DEGENERATION, NODAL AMPLITUDE FAILURE, DRIFT BLOWUP, OR K-SPIKE. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Rank-1 phase foliation

M17-274 gives, after a fixed target rotation,

\[
\xi=(\cos\phi,\sin\phi,0)
\]

with

\[
\boxed{\partial_\tau\phi=0}
\]

and

\[
\boxed{\nabla\cdot(a^2\nabla\phi)=0.}
\]

On a constant-rank patch,

\[
|\nabla\phi|>0,
\]

so the level sets

\[
\boxed{S_c:=\{x:\phi(x)=c\}}
\]

form a smooth time-independent two-dimensional foliation.

Let

\[
n:=\frac{\nabla\phi}{|\nabla\phi|}
\]

be the unit normal.

---

## 2. Multiplier has no normal derivative

M17-274 also gives

\[
\nabla K\cdot\nabla\phi=0.
\]

Hence

\[
\boxed{D_nK=0.}
\]

Therefore

\[
\boxed{\nabla K=\nabla_SK}
\]

is tangent to every phase leaf.

---

## 3. Decompose the ambient weighted diffusion

M17-263 gives the exact raw-tangent multiplier equation

\[
\boxed{
\partial_\tau K
=\Delta K+2\nabla\log a\cdot\nabla K.
}
\]

Because `D_n K=0`, differentiating that identity along `n` gives

\[
0=D_n(D_nK)
=\nabla^2K(n,n)+\nabla K\cdot\nabla_nn.
\]

Thus

\[
\boxed{
\nabla^2K(n,n)
=-(\nabla_nn)\cdot\nabla_SK.
}
\]

The Euclidean Laplacian decomposes as

\[
\Delta K
=\Delta_SK+\nabla^2K(n,n)
\]

because the term proportional to the normal derivative vanishes.
Therefore

\[
\boxed{
\Delta K
=\Delta_SK-(\nabla_nn)\cdot\nabla_SK.
}
\]

Also

\[
\nabla\log a\cdot\nabla K
=\nabla_S\log a\cdot\nabla_SK.
\]

Hence

\[
\boxed{
\partial_\tau K
=\Delta_SK+b_S\cdot\nabla_SK,
}
\]

where

\[
\boxed{
b_S:=2\nabla_S\log a-\nabla_nn.}
\]

This is a scalar uniformly parabolic equation on each fixed phase leaf.

---

## 4. Compact-leaf corridor

Assume the retained leaves satisfy uniformly in ancient time:

1. connected compact surface without boundary;
2. area bounded above and below;
3. diameter bounded above;
4. injectivity radius bounded below;
5. curvature bounded;
6. drift bound
   \[
   \boxed{\|b_S\|_{L^\infty}\le B_*;}
   \]
7. non-spike multiplier bound
   \[
   \boxed{|K|\le K_*<\infty.}
   \]

Failure of these hypotheses is retained explicitly rather than hidden in the compact case.

---

## 5. Uniform oscillation contraction

For a connected compact surface with the uniform geometry above and bounded drift, the parabolic transition kernel over one fixed time

\[
\tau_0>0
\]

has a uniform strictly positive mixing lower bound.

Equivalently, there exists

\[
0<q<1
\]

such that

\[
\boxed{
\operatorname{osc}_{S_c}K(\tau+\tau_0)
\le
q\,\operatorname{osc}_{S_c}K(\tau).
}
\]

The constants depend only on the compact-leaf geometry and `B_*`, not on the ancient starting time.

---

## 6. Ancient boundedness forces zero leafwise oscillation

Iterate backward `N` fixed time steps:

\[
\operatorname{osc}_{S_c}K(0)
\le
q^N\operatorname{osc}_{S_c}K(-N\tau_0).
\]

Since

\[
|K|\le K_*,
\]

we have

\[
\operatorname{osc}_{S_c}K(-N\tau_0)
\le2K_*.
\]

Therefore

\[
\operatorname{osc}_{S_c}K(0)
\le2K_*q^N.
\]

Letting `N -> infinity`,

\[
\boxed{
\operatorname{osc}_{S_c}K(0)=0.
}
\]

The same argument applies at every ancient time.
Thus

\[
\boxed{\nabla_SK=0.}
\]

---

## 7. Full spatial constancy

M17-274 already gives

\[
D_nK=0.
\]

Combining with

\[
\nabla_SK=0
\]

yields

\[
\boxed{\nabla K=0.}
\]

Hence `K` is spatially constant on the connected Rank-1 compact-leaf patch.

---

## 8. Contradiction with critical sign balance

The bounded-spike spectral survivor from M17-233/234/239 requires nontrivial critical multiplier occupancy together with a small signed mean, hence retained positive and negative `K` populations.

A single spatial constant cannot realize that structure.

Therefore

\[
\boxed{
H_{Rank1\ compact\ closed\ phase\ leaves}^{bounded\ drift,bounded\ K}
\Longrightarrow\bot.
}
\]

---

## 9. Remaining Rank-1 exits

The surviving alternatives are

\[
\boxed{
G_{phase\text{-}leaf\ boundary/interface}
\lor
G_{phase\text{-}leaf\ decompactification/geometry}
\lor
G_{nodal/amplitude\ degeneration}
\lor
G_{leaf\ drift\ blowup}
\lor
G_{K\text{-}spike}.
}
\]

A bounded open leaf is expected to return to boundary/interface replenishment exactly as in M17-265; an unbounded/decompactifying leaf requires a separate coarea/geometry audit.

---

## 10. DSD audit

- `K` diffusion is reduced to the leaf only after using the exact zero-normal-derivative law.
- Compactness assumptions on leaf geometry are explicit.
- No boundaryless mixing theorem is applied to open leaves.
- Ancient boundedness is used only after establishing a uniform contraction factor.
- Local Rank-1 patches with geometry failure remain open exits.
- Global regularity remains unproved.

---

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
