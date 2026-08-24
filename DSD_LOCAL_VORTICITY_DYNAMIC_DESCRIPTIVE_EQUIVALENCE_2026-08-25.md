# DSD Local Vorticity Dynamic Descriptive Equivalence — 2026-08-25

Status: **PROVED ON FIXED COMPACT ANCIENT WINDOWS FOR ALL FIXED VORTICITY DERIVATIVE ORDERS / GLOBAL TAIL DELETION NOT CLAIMED / GLOBAL REGULARITY NOT PROVED.**

This note continues `DSD_INTERNAL_FORMATION_DESCRIBABILITY_AUDIT_2026-08-25.md`.

The goal is not to construct a new exact globally truncated Navier–Stokes solution. The goal is narrower and DSD-specific:

> determine whether the bounded-enstrophy remote tail remains dynamically distinguishable from zero in the retained local vorticity channels.

---

## 1. Bounded-Z ancient setting

Let \((U,P,\Omega)\) be a smooth ancient Navier–Stokes solution on a fixed compact time window

\[
I_T=[-T,0]
\]

and assume

\[
\boxed{
\sup_{t\in I_T}\|\Omega(t)\|_2^2\le Z_*<\infty.
}
\]

Fix a core ball \(B_M\). For \(R>2M\), define the remote Biot–Savart contribution

\[
W_R(x,t)
:=
\int_{|y|>R}\mathcal K(x-y)\Omega(y,t)\,dy.
\]

The previously proved tail estimate gives, for every fixed integer \(m\ge0\),

\[
\boxed{
\|\nabla^mW_R\|_{L^\infty(B_M\times I_T)}
\le
C_{m,M}Z_*^{1/2}R^{-m-1/2}.
}
\]

Set

\[
V_R:=U-W_R.
\]

This is only a local descriptive decomposition. No claim is made that \(V_R\) by itself is an exact global Navier–Stokes solution.

---

## 2. Exact local vorticity evolution difference

The full vorticity equation is

\[
\partial_t\Omega
+U\cdot\nabla\Omega
=
\Omega\cdot\nabla U
+\nu\Delta\Omega.
\]

If the same local vorticity descriptor is evolved using the near velocity \(V_R\) instead of the full velocity \(U=V_R+W_R\), the retained-channel right-hand side is

\[
\mathcal F_R^{near}
:=-V_R\cdot\nabla\Omega
+\Omega\cdot\nabla V_R
+\nu\Delta\Omega.
\]

The exact full right-hand side is

\[
\mathcal F^{full}
:=-U\cdot\nabla\Omega
+\Omega\cdot\nabla U
+\nu\Delta\Omega.
\]

Therefore

\[
\boxed{
\mathcal F^{full}-\mathcal F_R^{near}
=
-W_R\cdot\nabla\Omega
+\Omega\cdot\nabla W_R.
}
\]

This identity contains no pressure and no time derivative of the artificial decomposition.

It is therefore the natural channel in which to test DSD dynamic descriptive equivalence.

---

## 3. Zeroth-order local dynamic difference vanishes

Define on the fixed compact window

\[
A_0(M,T)
:=
\|\Omega\|_{L^\infty(B_M\times I_T)},
\]

\[
A_1(M,T)
:=
\|\nabla\Omega\|_{L^\infty(B_M\times I_T)}.
\]

Smooth ancient compactness makes these finite.

Then

\[
\begin{aligned}
\|\mathcal F^{full}-\mathcal F_R^{near}\|_{L^\infty(B_M\times I_T)}
&\le
\|W_R\|_\infty A_1
+A_0\|\nabla W_R\|_\infty\\
&\le
C_MZ_*^{1/2}
\left(
A_1R^{-1/2}
+A_0R^{-3/2}
\right).
\end{aligned}
\]

Hence

\[
\boxed{
\mathcal F^{full}-\mathcal F_R^{near}
\to0
\quad\text{uniformly on }B_M\times I_T.
}
\]

Thus the remote bounded-Z tail is dynamically indistinguishable from zero in the zeroth-order local vorticity evolution channel.

**Status: PROVED.**

---

## 4. Every fixed derivative-order vorticity channel also closes

Let \(\ell\ge0\) be fixed. Differentiate the dynamic difference:

\[
D^\ell
\left(
-W_R\cdot\nabla\Omega
+\Omega\cdot\nabla W_R
\right).
\]

By Leibniz,

\[
\begin{aligned}
&\left\|
D^\ell(W_R\cdot\nabla\Omega)
\right\|\\
&\qquad\le
C_\ell
\sum_{a=0}^{\ell}
|D^aW_R|
|D^{\ell-a+1}\Omega|,
\end{aligned}
\]

and

\[
\begin{aligned}
&\left\|
D^\ell(\Omega\cdot\nabla W_R)
\right\|\\
&\qquad\le
C_\ell
\sum_{a=0}^{\ell}
|D^a\Omega|
|D^{\ell-a+1}W_R|.
\end{aligned}
\]

For every fixed \(\ell,M,T\), smoothness gives finite compact-window constants

\[
A_{b}(M,T)
:=
\|D^b\Omega\|_{L^\infty(B_M\times I_T)}
<\infty.
\]

The slowest remote decay occurs in the first sum at \(a=0\):

\[
\|W_R\|_\infty
\lesssim
Z_*^{1/2}R^{-1/2}.
\]

All other remote derivatives decay faster. Therefore

\[
\boxed{
\left\|
D^\ell(
\mathcal F^{full}-\mathcal F_R^{near}
)
\right\|_{L^\infty(B_M\times I_T)}
\le
C_{\ell,M,T,Z_*}R^{-1/2}.
}
\]

Hence for every fixed derivative order,

\[
\boxed{
D^\ell(
\mathcal F^{full}-\mathcal F_R^{near}
)
\to0
\quad\text{uniformly on fixed compact ancient windows.}
}
\]

**Status: PROVED.**

---

## 5. DSD interpretation

Define the retained finite-order local vorticity descriptor

\[
\mathcal D_{M,T}^{(N)}[U]
:=
\left\{
D^\ell\Omega,
D^\ell\mathcal F
:\ 0\le\ell\le N
\right\}_{B_M\times I_T}.
\]

Let the descriptor difference between the full field and the near-field evolution be

\[
\Delta_{M,T,R}^{(N)}
:=
\max_{0\le\ell\le N}
\left\|
D^\ell(
\mathcal F^{full}-\mathcal F_R^{near}
)
\right\|_{L^\infty(B_M\times I_T)}.
\]

Then

\[
\boxed{
\Delta_{M,T,R}^{(N)}
\le
C_{M,T,N,Z_*}R^{-1/2}
\to0.
}
\]

Therefore, relative to every **fixed** base \((M,T,N)\), the bounded-Z remote tail is dynamically descriptively equivalent to zero in the local vorticity channels.

Symbolically,

\[
\boxed{
U
\sim_{\mathrm{DSD},\,M,T,N}^{\omega\text{-dyn}}
U-W_R
\qquad(R\to\infty).
}
\]

This is a channel- and base-relative equivalence, not a global identity.

---

## 6. Why this does not violate channel-absence versus zero

For every finite \(R\), \(W_R\) exists and is generally nonzero. Therefore the tail channel is not absent.

The correct DSD classification is

\[
\boxed{
\text{defined nonzero but dynamically negligible at fixed local base as }R\to\infty.
}
\]

The result only says its induced difference in the retained local vorticity evolution channels tends to zero.

It does not say

\[
W_R=0,
\]

nor that the global non-\(L^3\) distinction disappears.

---

## 7. Why the result is stronger than the previous instantaneous decoupling statement

The previous local tail estimate showed

\[
W_R,\nabla W_R,\ldots\to0
\]

on fixed core balls.

The present note inserts those estimates into the **actual nonlinear vorticity evolution operator** and proves that the induced dynamic difference also vanishes.

Thus the statement has advanced from

\[
\boxed{
\text{small local tail field}
}
\]

to

\[
\boxed{
\text{small difference in the retained local nonlinear dynamics}.
}
\]

This is the DSD dynamic-closure requirement at fixed finite base and fixed finite derivative order.

---

## 8. What remains outside the proved equivalence

The result is not uniform in all possible bases simultaneously.

It does not yet prove uniform closure as

\[
M\to\infty,
\qquad
T\to\infty,
\qquad
N\to\infty.
\]

In particular:

1. the global \(L^3\) aggregation channel remains distinguishable;
2. derivative order growing with \(R\) is not controlled by this fixed-order result;
3. arbitrarily long backward ancient windows may require constants depending on \(T\);
4. the near-field descriptor is not claimed to be an independent exact global solution;
5. no existing global Liouville theorem is being imported.

Thus the equivalence is a **local dynamical germ equivalence**, not a global solution equivalence.

---

## 9. DSD branch correction

The bounded-Z persistent diffuse tail should no longer be kept as an independent **local singular mechanism** merely because it is globally non-\(L^3\).

Within every fixed finite local vorticity base,

\[
\boxed{
\text{remote diffuse tail}
\to
\text{zero dynamic describability difference}.
}
\]

Therefore its remaining role is

\[
\boxed{
\text{global aggregation/topology obstruction},
}
\]

not an order-one local vortex-stretching/transport mechanism.

If a later argument needs the tail to be dynamically active at the core, it must exhibit a retained channel in which the above difference does **not** vanish.

---

## 10. New DSD frontier

The singularity question on the bounded-Z branch now descends to the formed local ancient vorticity germ:

\[
\boxed{
\begin{array}{c}
\text{nonzero recurrent local ancient vorticity germ}\
+\text{first-hitting inheritance}\
+\text{bounded global enstrophy}\
+\text{remote-tail local dynamic equivalence}
\end{array}
\stackrel{?}{\Longrightarrow}
\text{local regularity / contradiction}.
}
\]

This is not the same statement as a global \(L^3\) ancient Liouville theorem.

The next DSD audit should therefore examine whether `recurrent core` itself is being over-typed: descriptor recurrence, material recurrence, and dynamical recurrence must be separated just as scale equality and genealogy were separated earlier.

Global regularity remains **UNPROVED**.