# DSD Internal Formation/Describability Audit — 2026-08-25

Status: **DSD-INTERNAL AUDIT / THREE CATEGORY ERRORS IDENTIFIED / TWO ALREADY REPAIRED / ONE ACTIVE REFORMULATION / GLOBAL REGULARITY NOT PROVED.**

This audit deliberately does **not** ask whether the route matches standard Navier–Stokes proof strategies. The comparison standard is DSD itself:

1. formation before dynamics;
2. describability difference before identification;
3. channel absence distinct from defined zero;
4. axis properties kept distinct before aggregation;
5. static aggregation not silently promoted to temporal genealogy;
6. dynamics applied only to formed objects or to explicitly closed equivalence classes;
7. limits do not automatically commute with formation.

The purpose is to identify where the current Navier–Stokes route stopped using DSD as a structural filter and began treating ordinary analytic descriptors as if they were already formed dynamical objects.

---

## 1. DSD ordering used for this audit

The correct internal order is taken to be

\[
\boxed{
\text{Formation}
\to
\text{Axis properties}
\to
\text{Static aggregation}
\to
\text{Dynamics}.
}
\]

For the present problem this means:

- first decide whether `core`, `tail`, `shell`, `packet`, `ancestor`, `center`, and `recurrent object` are actually formed/describable structures;
- then specify their independent axes: location, scale, derivative order, channel type, and time/genealogy;
- only then build quantities such as \(J_k\), enstrophy, cubic shell mass, return density, etc.;
- only after a cross-time identification map is justified may one speak of persistence, ancestry, rebuilding, or turnover.

This order is stronger than merely writing a time-dependent PDE for a chosen decomposition.

---

## 2. Audit A — equal scale was temporarily promoted to object identity

The exact radius identity

\[
R_{j,k}^{phys}=r_{j-k}
\]

is a relation on the **scale axis**.

It does **not** imply that the age-\(k\) shell at time \(t_j\) is the same material or descriptive object as the maximum-centered packet at time \(t_{j-k}\).

The missing data are at least

\[
\boxed{
\text{location}
+\text{amplitude}
+\text{channel occupancy}
+\text{cross-time identification}.
}
\]

Therefore the inference

\[
\text{same physical radius}
\Rightarrow
\text{same ancestor packet}
\]

would be a DSD category error: equality on one axis was being promoted to equality of complete descriptors.

This error has already been repaired by the amplitude/location genealogy work and the Galilean gauge audit.

**Status: IDENTIFIED AND REPAIRED.**

---

## 3. Audit B — static scale aggregation was temporarily promoted to dynamics

On the bounded-\(Z\), recurrent, non-\(L^3\) branch, the corrected static scale ledger is

\[
\sum_k J_k^{3/2}=\infty.
\]

This is a statement about an aggregation over the **scale axis**.

It does not by itself provide

- a material trajectory;
- a return count;
- a residence time;
- amplitude retention;
- bounded time overlap;
- or a temporal genealogy.

The attempted implication

\[
\sum_kJ_k^{3/2}=\infty
\Rightarrow
\text{large accumulated physical dissipation}
\]

failed precisely because it tried to move from a static scale aggregate to a time ledger without a separately formed dynamic bridge.

The corrected return-density quantity

\[
\mathfrak R_k
=\frac1{\rho_k}\sum_\ell\tau_{k,\ell}
\]

makes the missing temporal axis explicit, and only under amplitude retention and bounded overlap does

\[
\sum_kJ_k\mathfrak R_k<\infty
\]

become legitimate.

Thus DSD correctly diagnoses the earlier issue as

\[
\boxed{
\text{static aggregation}\neq\text{dynamic persistence}.
}
\]

**Status: IDENTIFIED AND REPAIRED.**

---

## 4. Audit C — the ancient global tail was treated as a fully formed dynamical object too early

This is the active issue.

The ancient-limit construction can produce a nontrivial recurrent local core together with a global non-\(L^3\) tail. However the two pieces have different formation status.

### 4.1 Core formation

For every fixed compact space-time window, the first-hitting sequence has local compactness sufficient to form a limiting local field.

The recurrent core therefore has a direct prelimit witness on fixed channels and fixed resolution windows.

Schematically,

\[
\boxed{
\text{finite-window prelimit descriptors}
\to
\text{nonzero ancient core descriptor}.
}
\]

This is compatible with formation before dynamics.

### 4.2 Tail formation

The global non-\(L^3\) tail is different.

Its defining property is an infinite scale aggregation such as

\[
\sum_kJ_k^{3/2}=\infty,
\]

which becomes complete only after passing through arbitrarily many remote shells.

At every finite prelimit stage, only a finite block is simultaneously transferred with controlled approximation. The **infinite aggregate** is therefore a limit-level descriptor, not automatically one prelimit material object.

Hence

\[
\boxed{
\text{limit aggregate exists}
\not\Rightarrow
\text{one formed prelimit dynamical object exists}.
}
\]

Calling the entire global tail a single persistent genealogy therefore requires an additional formation-commutation theorem.

**Status: ACTIVE GAP.**

---

## 5. Formation–limit commutation gate

Introduce the following DSD audit requirement.

Let \(\mathcal D_j\) be the complete descriptor of a prelimit stage and let \(\mathcal A\) be an aggregate object appearing only after \(j\to\infty\).

To use \(\mathcal A\) as a dynamical cause in the prelimit problem, require a family of finite-stage witnesses \(\mathcal A_j\) such that:

1. **formation witness:** \(\mathcal A_j\) exists in the relevant channels at stage \(j\);
2. **base-fixed distinguishability:** its difference from the complementary structure is nonzero at the chosen base/resolution;
3. **cross-time closure:** the relation identifying \(\mathcal A_j\) with \(\mathcal A_{j+1}\) is defined independently of a changing coordinate gauge;
4. **dynamic channel retention:** the channels through which \(\mathcal A_j\) affects the retained core do not vanish in the limit;
5. **uniformity:** these witnesses survive the diagonal/limit passage with constants independent of the finite block size.

Without these items the infinite tail may remain a valid **global static descriptor**, but not a formed prelimit dynamical entity.

Call this the

\[
\boxed{\text{Formation–Limit Commutation Gate (FLCG)}.}
\]

The current persistent diffuse tail has **not** passed FLCG.

---

## 6. Describability difference audit of the bounded-Z tail

The recent local-decoupling estimates show that, for a fixed core window \(B_M\), remote bounded-enstrophy vorticity produces

\[
\|\nabla^mU_{>R}\|_{L^\infty(B_M)}\to0
\qquad(R\to\infty),
\]

and its far pressure derivatives and cutoff commutator also vanish in the corresponding local channels.

But the same tail can retain a nontrivial global aggregation difference:

\[
U\notin L^3(\mathbb R^3).
\]

Therefore there are at least two distinct describability layers:

\[
\boxed{
\Delta_{local,dyn}(R)\to0,
\qquad
\Delta_{global,L^3}\neq0.
}
\]

This distinction is exactly the type of situation for which DSD's describability difference is useful.

The error would be to collapse these into one binary statement `tail exists / tail does not exist`.

Instead the correct DSD statement is:

\[
\boxed{
\text{the tail is globally distinguishable but may be locally dynamically indistinguishable.}
}
\]

---

## 7. Channel absence versus defined zero

The limit

\[
\Delta_{local,dyn}(R)\to0
\]

must not be called `channel absence` automatically.

For each finite \(R\), the far field channel exists and has a defined nonzero value. Only its contribution tends to zero on the fixed core window.

Thus the current classification is

\[
\boxed{
\text{defined nonzero negligible in the local channel as }R\to\infty,
}
\]

not

\[
\boxed{\text{channel absent}.}
\]

Only after a quotient/equivalence construction proves that this channel can be removed without changing the retained dynamics may one replace it by an absent channel in the reduced description.

This prevents DSD from becoming a license to delete a mathematically inconvenient tail.

**Status: REQUIRED DISTINCTION.**

---

## 8. Static aggregation audit: divergent cubic mass need not form a local dynamical structure

The diffuse-shell saturation model shows that one can have

\[
\sum_kJ_k^{3/2}=\infty
\]

while enstrophy and every fixed derivative-order weighted tail remain summable because the physical weights decay geometrically.

DSD interpretation:

- each shell may be individually `defined nonzero negligible` in a chosen local dynamical channel;
- the infinite collection may nevertheless form a `defined non-negligible` object in a global cubic aggregation channel.

Therefore

\[
\boxed{
\text{aggregate non-negligibility in channel }q_1
\not\Rightarrow
\text{componentwise non-negligibility in channel }q_2.
}
\]

In particular, global \(L^3\)-failure cannot be promoted to a local singular mechanism merely because the aggregate diverges.

This is not a regularity proof; it is a correction of the descriptor typing.

---

## 9. Axis audit of the current route

The current Navier–Stokes proof attempt uses at least five axes:

\[
\boxed{
\text{location},\quad
\text{physical scale},\quad
\text{time/genealogy},\quad
\text{derivative order},\quad
\text{channel type}.
}
\]

The DSD audit finds that several failed proof moves occurred when two axes were silently identified:

### scale = genealogy

Rejected by the ancestor-radius audit.

### derivative order = physical scale

Rejected by the derivative-cascade audit: increasing derivative order is not the same as descending physical scale, and distinct derivative dissipations cannot be summed into one finite ledger.

### global aggregation = local dynamics

Rejected by the diffuse-tail saturation model and local-decoupling estimates.

### coordinate center = physical genealogy

Rejected as a Galilean-gauge dependent identification unless the comparison is same-time/material-relative.

These are DSD failures of axis typing, not failures of the Navier–Stokes equations.

---

## 10. DSD-corrected object hierarchy

The present survivor should therefore be retyped as follows.

### Level F1 — formed local ancient core

A nonzero local ancient descriptor obtained from uniform compact convergence on fixed windows.

**Formation status: FORMED.**

### Level F2 — finite remote shell block

A finite collection of annular descriptors transferred from the prelimit sequence.

**Formation status: FORMED AS A FINITE STATIC BLOCK.**

### Level F3 — infinite non-L3 tail aggregate

The infinite scale aggregate obtained after diagonal/ancient passage.

**Formation status: FORMED AS A GLOBAL STATIC LIMIT DESCRIPTOR; PRELIMIT DYNAMIC OBJECT NOT YET DERIVED.**

### Level F4 — persistent material tail genealogy

A single cross-time object with amplitude/location retention and a defined dynamical influence on the core.

**Formation status: NOT DERIVED.**

The prior route occasionally spoke as if F3 automatically implied F4. DSD rejects that promotion.

---

## 11. New DSD target: dynamic descriptive equivalence, not immediate tail deletion

Define a core descriptor family on a fixed window \(B_M\):

\[
\mathcal D_M[u]
=
\{
U,\nabla U,\Omega,\nabla\Omega,\text{pressure oscillation},
\text{local energy/enstrophy flux},\ldots
\}_{B_M}.
\]

For a near/far decomposition indexed by \(R\), define a channelwise difference

\[
\Delta_{M,R}^{(q)}
:=d_q\bigl(\mathcal D_M[u],\mathcal D_M[u_{\le R}]\bigr).
\]

A DSD-local dynamic equivalence would require

\[
\boxed{
\Delta_{M,R}^{(q)}\to0
}
\]

for every retained local channel \(q\), together with a vanishing equation defect

\[
\boxed{
\mathfrak E_{M,R}\to0
}
\]

in a topology strong enough to pass the nonlinear dynamics.

If this holds uniformly on the required ancient time windows, then the remote tail is not absent and not globally equivalent, but it is **dynamically equivalent to zero relative to the selected local base**.

This is the correct DSD notion to investigate.

---

## 12. What DSD does and does not give at this point

DSD by itself does **not** imply

\[
\text{locally dynamically negligible tail}
\Rightarrow
\text{tail may be deleted from Navier–Stokes}.
\]

That would skip the dynamic-closure proof and violate formation/defined-zero discipline.

What DSD does give is the stronger audit statement:

\[
\boxed{
\text{global non-}L^3\text{ distinction alone is not yet a formed local singular mechanism.}
}
\]

Therefore the last survivor should no longer be phrased simply as

`persistent passive non-L3 tail`.

The DSD-correct phrasing is

\[
\boxed{
\text{global static tail difference}
\quad\text{whose local dynamic distinguishability is tending to zero,}
}
\]

with the unresolved question being whether the local zero-difference relation is dynamically closed.

---

## 13. New proof frontier after the DSD audit

The highest-value theorem is now not a general three-dimensional ancient Liouville theorem.

It is the narrower DSD/PDE compatibility theorem:

\[
\boxed{
\begin{array}{c}
\text{bounded-Z ancient solution}\
+\text{nonzero recurrent local core}\
+\Delta_{M,R}^{(q)}\to0\text{ for all retained local channels}\
+\mathfrak E_{M,R}\to0
\end{array}
\Longrightarrow
\begin{array}{c}
\text{the singular-core question descends to the}\
\text{base-fixed local descriptive equivalence class.}
\end{array}
}
\]

After this descent, one must still prove that no nontrivial singular ancient core exists in that quotient/local class. The DSD audit does not supply that final theorem automatically.

But this is materially narrower than trying to remove an arbitrary global non-\(L^3\) tail by a global Liouville theorem.

---

## 14. Audit verdict

### Valid DSD contributions still active

- formation before dynamics;
- channel absence versus defined zero;
- describability difference by channel/resolution;
- independent treatment of scale, time, derivative order, and location axes;
- prohibition on promoting a static aggregate directly to a material genealogy;
- requirement that limit objects have finite-stage formation witnesses before being used as prelimit dynamical causes.

### Corrected errors

1. same radius was too close to being treated as same ancestor object;
2. cubic scale aggregation was too close to being treated as temporal persistence;
3. absolute center displacement was used in a gauge-sensitive form before same-time/material-relative correction.

### Active error/reformulation

The infinite ancient non-\(L^3\) tail has been treated too strongly as one formed persistent dynamical object. What is actually derived is a global static limit difference plus locally vanishing dynamical channels.

### Current DSD verdict

\[
\boxed{
\text{THE ROUTE IS NOT CLOSED, BUT THE FINAL OBSTRUCTION WAS OVER-TYPED.}
}
\]

The next calculation should test **dynamic descriptive equivalence closure** of the bounded-Z tail. If that closure succeeds, the tail ceases to be an independent local singular branch without being falsely declared nonexistent. If it fails, the failure itself identifies a nonvanishing channel through which the tail remains dynamically describable, and that channel becomes the next quantitative target.

Global regularity remains **UNPROVED**.