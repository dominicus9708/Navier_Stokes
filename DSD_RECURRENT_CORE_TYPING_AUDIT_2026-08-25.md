# DSD Recurrent-Core Typing Audit — 2026-08-25

Status: **DESCRIPTOR REAPPEARANCE PROVED ON CONVERGENT FIRST-HITTING SUBSEQUENCES / SAME-BASE DYNAMICAL RECURRENCE NOT AUTOMATIC / MATERIAL AND QUANTITATIVE RETURN RECURRENCE NOT DERIVED / GLOBAL REGULARITY NOT PROVED.**

This note audits the word `recurrent` using DSD itself rather than external Navier–Stokes terminology.

The central DSD rule is:

\[
\boxed{
\text{repeated description}
\neq
\text{repeated dynamical state}
\neq
\text{same formed object returning}.
}
\]

---

## 1. The first-hitting index is not a pure time axis

Work in viscosity-normalized variables for notation. A first-hitting stage has

\[
W_j=q^jW_0,
\qquad
r_j=W_j^{-1/2},
\qquad
t_j\uparrow T^*.
\]

A normalized snapshot is obtained schematically by a stage-dependent map

\[
\mathcal N_j:
 u(x,t)
\mapsto
U_j(y,s)
:=r_j u(X_j+r_jy,t_j+r_j^2s).
\]

Thus increasing `j` changes simultaneously

\[
\boxed{
\text{physical time}
+\text{physical scale}
+\text{center}
+\text{normalization base}.
}
\]

Therefore `j` is a **compound representation index**, not a pure physical-time coordinate.

If

\[
U_{j_m}\approx U_{j_n}
\]

on a normalized compact set, what is directly proved is

\[
\boxed{
\mathcal N_{j_m}u
\approx
\mathcal N_{j_n}u,
}
\]

not that the same physical object has returned between \(t_{j_m}\) and \(t_{j_n}\).

This is the first recurrence typing correction.

---

## 2. Five recurrence levels

To prevent axis collapse, define five levels.

### R0 — formed local germ

A fixed-base compact-window descriptor has a nonzero ancient limit:

\[
\mathcal D_{M,T,N}[U_{j_n}]
\to
\mathcal D_{M,T,N}[U_\infty].
\]

This is formation of a local limiting germ.

**Status: PROVED on the compactness/ancient-extraction branches where the corresponding local bounds are available.**

### R1 — normalized descriptor reappearance

For two late members of the same convergent subsequence,

\[
d_{M,T,N}
\left(
\mathcal D[U_{j_m}],
\mathcal D[U_{j_n}]
\right)
\to0.
\]

This is a repeated **description after stage-dependent recentering/rescaling**.

**Status: PROVED as a consequence of convergence.**

### R2 — same-base dynamical recurrence

Inside one already formed normalized dynamical system, require times \(s_n\) such that

\[
\mathcal D_{M,T,N}[U_\infty(\cdot,\cdot+s_n)]
\to
\mathcal D_{M,T,N}[U_\infty]
\]

with the same base, same coordinates, and same retained channels.

This is genuine recurrence of a normalized dynamical germ.

**Status: NOT DERIVED from first-hitting compactness or R1 alone.**

### R3 — material/object recurrence

Require a gauge-invariant cross-time identification map \(\Phi_{a\to b}\) for a formed physical object such that

\[
\mathcal D_b
\approx
(\Phi_{a\to b})_\#\mathcal D_a,
\]

with location, scale, amplitude, and channel identity retained.

This means the **same formed object** returns/reappears.

**Status: NOT DERIVED from R0/R1.**

### R4 — quantitative return recurrence

For use in the physical dissipation ledger, require in addition

- a retained amplitude lower bound;
- a residence/dwell time;
- a physical radius;
- bounded overlap of selected return intervals.

This is the level needed to create

\[
\mathfrak R_k
=\rho_k^{-1}\sum_\ell\tau_{k,\ell}
\]

and legitimately use

\[
\sum_kJ_k\mathfrak R_k<\infty.
\]

**Status: NOT DERIVED automatically from any weaker recurrence level.**

---

## 3. Exact compactness lemma: what R1 really gives

Let \((\mathscr D,d)\) be the fixed-base descriptor metric space. If

\[
D_{j_n}\to D_\infty,
\]

then by the triangle inequality

\[
\boxed{
 d(D_{j_m},D_{j_n})
\le
 d(D_{j_m},D_\infty)
+d(D_{j_n},D_\infty)
\to0.
}
\]

Hence arbitrarily late normalized stages become arbitrarily close as descriptors.

This is rigorous but only establishes **Cauchy reappearance in descriptor space**.

It does not supply a physical transport map between the corresponding prelimit regions.

**Status: PROVED.**

---

## 4. Why R1 does not imply R2

A convergent sequence of rescaled observations can approach one static or nonrecurrent ancient profile without that profile ever returning under its own time evolution.

Symbolically,

\[
\mathcal N_{j_n}u\to U_\infty
\]

contains no implication of the form

\[
U_\infty(s_n+\cdot)\to U_\infty(\cdot).
\]

The first statement varies the observation map \(\mathcal N_j\). The second holds the base fixed and evolves the formed limit itself.

Thus

\[
\boxed{R1\not\Rightarrow R2.}
\]

This is a DSD axis distinction, not a statement about whether recurrence theorems exist elsewhere.

---

## 5. Why R1 does not imply R3

Suppose two normalized descriptors are close:

\[
\mathcal N_{j_m}u\approx\mathcal N_{j_n}u.
\]

Because \(\mathcal N_{j_m}\) and \(\mathcal N_{j_n}\) use different centers and scales, this only says that two differently based observations have similar structure.

To identify one physical object across the two stages one would need, at minimum, a map

\[
\Phi_{m\to n}
\]

such that the conjugated map

\[
\boxed{
\mathcal N_{j_n}
\circ
\Phi_{m\to n}
\circ
\mathcal N_{j_m}^{-1}
}
\]

preserves the retained object descriptor to the required tolerance.

No such map follows from compactness alone.

Therefore

\[
\boxed{R1\not\Rightarrow R3.}
\]

**Status: PROVED as a logical typing audit; the required cross-time map is NOT DERIVED.**

---

## 6. Recurrence Formation Gate (RFG)

Introduce a DSD gate for promoting descriptor recurrence to a formed recurrent object.

A candidate must satisfy:

1. **base alignment** — the compared descriptors use explicitly related bases;
2. **formation at both times** — the object is formed/defined in the retained channels at both endpoints;
3. **gauge-invariant cross-time map** — identity is not based on absolute center coordinates alone;
4. **channel retention** — the channels defining the object remain applicable and non-negligible under the map;
5. **amplitude/scale compatibility** — similarity is not produced solely by changing normalization;
6. **dynamic closure** — the map is compatible with the retained PDE dynamics;
7. **quantitative dwell**, if the recurrence is used in a dissipation/return ledger.

Call this the

\[
\boxed{\text{Recurrence Formation Gate (RFG)}.}
\]

R1 passes only the descriptor-similarity part. R3/R4 require the remaining items.

---

## 7. Consequence for the current `recurrent` label

The safest DSD typing of the branch currently called

\[
\text{bounded-}Z+\text{recurrent}+\text{non-}L^3
\]

is, unless an independent same-base/material recurrence certificate is explicitly supplied,

\[
\boxed{
\text{bounded-}Z
+\text{descriptor-reappearing ancient branch}
+\text{non-}L^3.
}
\]

The word `recurrent` may still be used as shorthand only if its level is attached, e.g.

- `R1 descriptor recurrence`;
- `R2 same-base dynamical recurrence`;
- `R3 material recurrence`;
- `R4 quantitative return recurrence`.

An untyped recurrence label is no longer allowed in the DSD audit ledger.

---

## 8. Effect on the cubic-tail argument

The corrected bounded-Z static statement

\[
\sum_kJ_k^{3/2}=\infty
\]

belongs to the scale-aggregation layer.

Even if the ancient core satisfies R1 descriptor reappearance, this does not produce R4 return density.

Therefore the attempted closure

\[
\text{R1}+\sum_kJ_k^{3/2}=\infty
\Rightarrow
\text{physical return-energy contradiction}
\]

is invalid.

The earlier return-density audit had already discovered this analytically. DSD now identifies the structural reason:

\[
\boxed{
\text{descriptor recurrence axis}
\neq
\text{material return-time axis}.
}
\]

---

## 9. Interaction with the new local-tail dynamic equivalence result

The bounded-Z remote tail has now been shown to satisfy, on every fixed finite local vorticity base,

\[
\Delta_{M,T,R}^{(N)}\to0.
\]

Thus the tail is not an order-one local dynamic mechanism at R0/R1 level.

Combining this with the recurrence audit gives a cleaner formed object:

\[
\boxed{
\text{local ancient vorticity germ}
}
\]

rather than

\[
\boxed{
\text{a globally recurrent core-plus-tail material object}.
}
\]

The former is actually formed by the available compactness and local dynamic-equivalence arguments; the latter is over-typed unless RFG is passed.

---

## 10. New DSD-corrected frontier

The bounded-Z branch should now be formulated without unproved material recurrence:

\[
\boxed{
\begin{array}{c}
\text{formed nonzero local ancient vorticity germ}\
+\text{first-hitting normalization inheritance}\
+\sup_t\|\Omega(t)\|_2<\infty\
+\text{fixed-base local dynamic tail equivalence}\
+\text{R1 descriptor reappearance on convergent subsequences}
\end{array}
}
\]

The next question is not whether this germ `returns` materially. The next DSD question is:

\[
\boxed{
\text{Can a formed first-hitting ancient germ remain nonzero while its}\
\text{formation-defining local channels close consistently under backward time?}
}
\]

That question belongs to the **formation/dynamic compatibility** layer, not the return-count layer.

---

## 11. Audit verdict

### PROVED

- the first-hitting stage index mixes time, scale, center, and normalization base;
- convergence gives R1 descriptor reappearance;
- R1 does not logically provide a material transport map or return residence;
- any use of recurrence in the energy-return ledger requires additional R3/R4 data.

### NOT DERIVED

- same-base recurrence of the ancient germ from first-hitting compactness alone;
- material recurrence of one formed core object;
- quantitative return recurrence sufficient for \(\mathfrak R_k\gtrsim J_k^{1/2}\).

### DSD correction

The current survivor is better described as a **formed local ancient germ with descriptor reappearance**, not a proven recurrent material core.

Global regularity remains **UNPROVED**.