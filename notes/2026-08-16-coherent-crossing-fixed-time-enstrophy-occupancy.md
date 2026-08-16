# A coherent R-scale crossing forces `R^3` enstrophy occupancy on a fixed normalized terminal time block

Date: 2026-08-16

Status: **EXACT CONSEQUENCE OF COHERENT-CORE VOLUME OCCUPANCY AND THE FIRST-HITTING LINEAR ENSTROPHY GROWTH CEILING. IT SHARPENS THE BASIC RECENT-SOURCE COST BEFORE ANY V2 ALTERNATIVE IS INVOKED. GLOBAL REGULARITY NOT PROVED.**

## 1. Coherent crossing enstrophy

At the Gaussian Reynolds-one coherent crossing,

\[
|\bar\Omega|\ge c_0>0,
\qquad
V_\omega\lesssim R^{-4}.
\]

On a fixed fractional ball/cylinder of volume comparable to `R^3`, the vorticity differs from the order-one mean by only a small `L2` fluctuation. Hence

\[
\boxed{
E_c:=\|\Omega(s_c)\|_2^2
\gtrsim R^3.
}
\]

---

## 2. First-hitting linear growth ceiling

On the terminal first-hitting past,

\[
\|\Omega(s)\|_\infty\le1.
\]

The stretching source satisfies

\[
|Q|
\lesssim
\|\Omega\|_\infty E
\lesssim E.
\]

The enstrophy identity

\[
\frac12E'+\nu P=Q
\]

therefore gives

\[
\boxed{
E'(s)\le C_0E(s).
}
\]

---

## 3. Run the growth inequality backward from the crossing

For every fixed `tau>=0` for which `s_c-tau` remains in the first-hitting past,

\[
E_c
\le
E(s_c-\tau)e^{C_0\tau}.
\]

Therefore

\[
\boxed{
E(s_c-\tau)
\ge
E_c e^{-C_0\tau}.
}
\]

Choose any fixed

\[
0<\tau_0<\infty
\]

available uniformly on the late sequence, for example a sufficiently small universal terminal width. Then

\[
\boxed{
E(s)
\gtrsim
R^3
\qquad
(s_c-\tau_0\le s\le s_c),
}
\]

with a fixed constant depending only on `tau0` and the universal source bound.

---

## 4. Fixed-time occupancy cost

Integrating,

\[
\boxed{
\int_{s_c-\tau_0}^{s_c}
E(s)ds
\gtrsim
R^3.
}
\]

Since the recent source horizon

\[
L=W^{1/3+\delta}
\]

diverges, it contains this fixed terminal block for all sufficiently late crossings. Therefore

\[
\boxed{
D_L:=\int_0^L E(s_c-\tau)d\tau
\gtrsim R^3.
}
\]

So an order-one recent source is never supported by a vanishing normalized enstrophy-time action on the coherent branch.

---

## 5. Physical energy-dissipation cost

Using

\[
\int E_{\rm norm}ds
=W^{1/2}
\int E_{\rm phys}dt,
\]

we obtain the physical dissipation lower bound

\[
\boxed{
\nu\int_{t_c-\tau_0/W}^{t_c}
\|\omega(t)\|_2^2dt
\gtrsim
c\nu\frac{R^3}{W^{1/2}}.
}
\]

This can still be summable on a super-separated first-hitting sequence, so it is not a contradiction by itself.

---

## 6. Relation to the recent enstrophy--V2 tradeoff

The recent-source inequality was

\[
D_L^7Z_L^9
\gtrsim\nu^6.
\]

The coherent crossing now supplies

\[
D_L\gtrsim R^3.
\]

Therefore the role of the V2 alternative must be interpreted carefully:

- it is not needed to prove that *some* ordinary enstrophy action exists;
- the coherent core already forces a large `R^3` ordinary occupancy;
- V2 becomes important when one attempts to concentrate the source/coherence transition into thinner spatial or temporal structures than this global occupancy records.

Thus the basic recent source branch is more cleanly written as

\[
\boxed{
\text{coherent crossing}
\Longrightarrow
R^3\text{ normalized enstrophy occupancy}
}
\]

plus, for unusually thin source concentration,

\[
\boxed{
\text{weighted V2 / derivative escalation}.
}
\]

---

## 7. Updated budget hierarchy

Three distinct costs are now available for one late coherent episode:

1. clean-precursor lifespan:
   \[
   s_c-s_m\gtrsim\nu^3E_m^{-2};
   \]
2. clean-to-crossing physical dissipation:
   \[
   \nu\int_{t_m}^{t_c}\|\omega\|_2^2dt
   \gtrsim c\nu^4R^{-\beta};
   \]
3. fixed terminal coherent occupancy:
   \[
   \int_{s_c-\tau_0}^{s_c}Eds
   \gtrsim R^3.
   \]

Each is stronger in a different regime; none has yet been proved non-summable across an arbitrary super-separated cascade.

Overall status: **RECENT SOURCE HAS AN AUTOMATIC `R^3` ORDINARY ENSTROPHY OCCUPANCY / V2 IS NOW A THIN-CONCENTRATION REFINEMENT RATHER THAN THE BASE SOURCE COST.**
