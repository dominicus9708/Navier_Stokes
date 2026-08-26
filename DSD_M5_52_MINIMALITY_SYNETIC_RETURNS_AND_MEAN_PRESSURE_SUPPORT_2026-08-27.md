# DSD M5-52 — Minimality, Syndetic Returns, and Mean Pressure Support

Date: 2026-08-27

Status: **TOPOLOGICAL-DYNAMICS STRENGTHENING OF M5-44 / COMPACT MINIMAL W1 RECURRENCE IMPLIES RELATIVELY DENSE RETURN TIMES TO EVERY STATE NEIGHBORHOOD / UNDER THE EXISTING ROBUST POSITIVE-PUMP MARGIN THIS UPGRADES M5-47 FROM SPARSE RECURRENCE TO POSITIVE LERAY-TIME DENSITY OF PUMP WINDOWS / THE LOCALIZED `p=3` LEDGER THEN FORCES A POSITIVE LONG-TIME MEAN PRESSURE-PLUS-SHELL SUPPORT / GLOBAL REGULARITY UNPROVED.**

## 1. Why M5-44 contains more than an arbitrary return sequence

M5-44 did not assume merely that one profile has a sequence of return times.

It placed the complete W1 ancestor `U^#` inside a **compact minimal recurrent W1 set** `K` under time translation.

Write the translation flow as

\[
T_h:K\to K,
\qquad
T_hU^#(\eta)=U^#(\eta+h).
\]

M5-44 extracted some sequence

\[
h_n\to\infty,
\qquad
T_{h_n}U^#\to U^#.
\]

Minimality actually gives a stronger return property.

---

## 2. Syndetic-return lemma for a compact minimal flow

Let `(K,T_h)` be a compact minimal continuous `R`-flow.

Fix `x\in K` and an open neighborhood `N` of `x`.

Define the return set

\[
\mathcal R(x,N)
:=
\{h\ge0:T_hx\in N\}.
\]

Then `\mathcal R(x,N)` is **syndetic**: there exists `L_N<\infty` such that every interval

\[
[s,s+L_N]
\]

with `s` sufficiently large contains a return time.

### Proof

By minimality, for every `y\in K` there exists a real time `t` such that

\[
T_ty\in N.
\]

Equivalently,

\[
y\in T_{-t}N.
\]

Thus

\[
K
=
\bigcup_{t\in\mathbb R}T_{-t}N.
\]

Compactness gives a finite subcover

\[
K
=
\bigcup_{j=1}^mT_{-t_j}N.
\]

Let

\[
M:=\max_j|t_j|.
\]

For any `s\ge0`, the point

\[
y=T_{s+M}x
\]

belongs to one member `T_{-t_j}N`, so

\[
T_{s+M+t_j}x\in N.
\]

But

\[
s\le s+M+t_j\le s+2M.
\]

Therefore every interval `[s,s+2M]` contains a return.

Hence one may take

\[
\boxed{L_N=2M.}
\]

---

## 3. Exact upgrade of M5-44

For every W1 neighborhood `N` of the anchor state,

\[
\boxed{
\text{return gaps to }N
\text{ are uniformly bounded in Leray time.}
}
\]

Thus the aperiodic branch is not allowed to evade the proof search merely by sending all accurate returns farther and farther apart with unbounded gaps.

The orbit may still be nonperiodic, but it is uniformly recurrent in the standard minimal-flow sense.

This strengthens the topology used in M5-47.

---

## 4. From state returns to robust pump returns

The anchor W1 state contains a positive normalized pump event.

Suppose the retained W1 compactness/strictness data give a neighborhood `N_pump`, a fixed normalized time half-width `w>0`, and a critical local action `A_pump` such that every visit

\[
T_hU^#\in N_{pump}
\]

produces on the window `[h-w,h+w]` the lower bound

\[
\boxed{
\mathcal A_{crit}[h-w,h+w]
\ge a_*>0.
}
\]

This is the natural robustness statement for a strict positive pump under local smooth W1 convergence.

The syndetic lemma gives a bound `L_pump` on all return gaps to `N_pump`.

---

## 5. Disjoint positive-density pump windows

Potential overlap of pump windows must be audited rather than ignored.

Choose returns recursively so that

\[
h_{n+1}
\in
[h_n+2w,\ h_n+2w+L_{pump}].
\]

This is possible by syndeticity.

Then the windows

\[
I_n=[h_n-w,h_n+w]
\]

are disjoint, while their centers obey

\[
2w
\le
h_{n+1}-h_n
\le
2w+L_{pump}.
\]

Therefore the number `N(H)` of selected pump windows up to Leray time `H` satisfies

\[
\boxed{
N(H)
\ge
\frac{H}{2w+L_{pump}}-O(1).
}
\]

Thus robust pump events have positive lower density in Leray time.

---

## 6. Upgrade of the M5-47 critical-action statement

M5-47 stated that **if** recurrent pump copies occur with positive/syndetic density in Leray time, then an order-one critical action per copy yields linear divergence in the log clock.

M5-52 supplies the missing topological reason for syndetic state returns.

Under the robustness assumption of Section 4,

\[
\sum_{I_n\subset[0,H]}
\mathcal A_{crit}[I_n]
\ge
 a_*N(H),
\]

so

\[
\boxed{
\mathcal A_{crit}[0,H]
\gtrsim
c_*H
}
\]

for the selected disjoint pump windows.

Since

\[
H
\sim
\log\frac1{T-t},
\]

this gives the expected logarithmic critical accumulation as the terminal time is approached.

It remains compatible with finite ordinary energy/dissipation by M5-47 and M5-49.

---

## 7. Fixed-core localized `p=3` ledger

Choose a fixed cutoff radius `R_0` large enough to contain the normalized pump core and use the M5-50 cutoff cubic mass

\[
\mathfrak L_{R_0}(\eta)
=
\int\chi_{R_0}|U|^3dy.
\]

Because `K` is compact in the retained local W1 topology,

\[
\boxed{
\sup_{\eta\in\mathbb R}
|\mathfrak L_{R_0}(\eta)|
<\infty.
}
\]

M5-50 gives

\[
\frac13\frac d{d\eta}\mathfrak L_{R_0}
+
\nu\mathcal D_{3,R_0}
=
\mathcal P_{R_0}
+
\mathcal B_{R_0},
\]

where

\[
\mathcal P_{R_0}(\eta)
:=
\int\chi_{R_0}P\,\nabla\cdot(|U|U)dy
\]

and `B_{R_0}` is the cutoff/log-shell boundary term.

Integrating from `0` to `H` gives

\[
\nu\int_0^H\mathcal D_{3,R_0}d\eta
=
\int_0^H(\mathcal P_{R_0}+\mathcal B_{R_0})d\eta
-
\frac13
[\mathfrak L_{R_0}(H)-\mathfrak L_{R_0}(0)].
\]

Divide by `H`.

The last term vanishes as `H\to\infty` because `\mathfrak L_{R_0}` is uniformly bounded.

Therefore

\[
\boxed{
\liminf_{H\to\infty}
\frac1H
\int_0^H
(\mathcal P_{R_0}+\mathcal B_{R_0})d\eta
=
\nu
\liminf_{H\to\infty}
\frac1H
\int_0^H
\mathcal D_{3,R_0}d\eta
}
\]

whenever the relevant averages exist; without existence, the corresponding liminf/limsup inequalities follow from the same bounded-endpoint term.

---

## 8. Positive pump density forces positive mean support

If each robust pump window contains a fixed local `D3` amount

\[
\int_{I_n}\mathcal D_{3,R_0}d\eta
\ge d_*>0,
\]

then the disjoint-window density from Section 5 yields

\[
\liminf_{H\to\infty}
\frac1H
\int_0^H\mathcal D_{3,R_0}d\eta
\ge
\frac{d_*}{2w+L_{pump}}
>0.
\]

Hence the localized `p=3` ledger forces

\[
\boxed{
\liminf_{H\to\infty}
\frac1H
\int_0^H
(\mathcal P_{R_0}+\mathcal B_{R_0})d\eta
\ge
\nu\frac{d_*}{2w+L_{pump}}
>0.
}
\]

This is stronger than saying that pressure must occasionally compete with viscosity.

The recurrent minimal survivor requires a **persistent positive mean pressure-plus-shell support** in normalized time.

---

## 9. Combining with M5-51 pressure locality

The pressure in `P_{R_0}` may be split into sources inside a much larger radius `S` and sources outside `S`.

Under the M5-51 `1/r` tail envelope,

\[
\|P_{>S}\|_{L^\infty(B_{2R_0})}
\le
CM^2S^{-2}.
\]

Since the fixed-core W1 orbit is compact, the factor

\[
\|\nabla\cdot(|U|U)\|_{L^1(B_{2R_0})}
\]

is uniformly bounded.

Therefore

\[
\boxed{
|\mathcal P_{R_0,>S}(\eta)|
\le
C_{W1,R_0}M^2S^{-2}
}
\]

uniformly in `eta`.

For any prescribed `epsilon>0`, choose `S` so large that the remote pressure-source contribution to the long-time mean is below `epsilon`.

Thus the positive mean support from Section 8 must be carried, up to an arbitrarily small error, by

\[
\boxed{
\text{finite-neighbor pressure sources}
+
\text{the cutoff/log-shell boundary term}.
}
\]

---

## 10. New dichotomy

The surviving recurrent cell must satisfy at least one of the following two mechanisms in the fixed normalized core:

### Branch A — persistent near-shell pressure work

A positive long-time mean of the pressure work is generated by the core and finitely many neighboring logarithmic shells.

### Branch B — persistent similarity-shell boundary support

The cutoff boundary term `B_{R_0}` supplies the required positive mean, corresponding to critical cubic content crossing the fixed log-radius shell in similarity coordinates.

A proof can now attack these two mechanisms separately.

Remote cell infinity is only a summable correction by M5-51.

---

## 11. DSD audit

### GREEN — exact from compact minimal flow

- return times to every W1 neighborhood are syndetic;
- aperiodic minimal recurrence cannot have arbitrarily large return gaps to a fixed neighborhood;
- fixed-core localized cubic mass is bounded on the compact W1 orbit;
- its endpoint contribution vanishes after division by long Leray time.

### GREEN conditional on the retained strict pump robustness

- pump windows occur with positive lower density;
- disjoint pump windows can be selected with uniformly bounded gaps;
- any fixed positive local critical action per pump forces a positive long-time mean critical dissipation/action.

### YELLOW — new closure targets

- prove the near-shell pressure-work mean cannot remain positive enough;
- or prove the similarity-shell boundary support is a coboundary/zero-mean term after correct tail renormalization;
- or show equality forces an exact periodic/fixed profile in an already excluded class.

### RED — branch removed

The aperiodic survivor can no longer be defended by assuming that accurate pump returns become arbitrarily sparse in Leray time, provided the M5-44 compact minimal-flow hypothesis is retained.

---

## 12. Updated proof gate

The current gate is now a mean-balance problem on a compact minimal normalized orbit:

\[
\boxed{
\text{positive-density pump dissipation}
=
\text{positive mean near-shell pressure work}
+
\text{positive mean similarity-shell support}.
}
\]

The next calculation should resolve the asymptotic structure of `B_R` for the static `1/r` ancestry.

If its order-one drift contribution can be isolated as an exact tail coboundary/renormalization term, then the remaining positive mean must be carried by finite-neighbor pressure work alone.

That is the next narrow branch.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
