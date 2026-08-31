# DSD M5-376 — Productive-shell concentration compactness on the scale lattice

Date: 2026-08-31

Status: **ON THE BOUNDED-NORMALIZED-STAGE BRANCH, THE PRODUCTIVE ANGULAR SHELL DISTRIBUTION ADMITS A DISCRETE CONCENTRATION-COMPACTNESS TRICHOTOMY / SCALE-TIGHT PRODUCTIVE ACTION FORCES A FIXED-FRACTION NATURAL-SCALE SHELL ON A SUBSEQUENCE / FAILURE OF SCALE TIGHTNESS FORCES POSITIVE PRODUCTIVE ACTION TO ESCAPE TO SUB-NATURAL OR REMOTE SCALES / THERE IS NO FOURTH INDEPENDENT `DIFFUSE MULTISCALE BUT SCALE-TIGHT` LEAF / THE ANGULAR-MULTISCALE LABEL IS THEREFORE ABSORBED INTO THE EXISTING DERIVATIVE, NATURAL-PARTNER, OR REMOTE/TURNOVER ROUTES / GLOBAL REGULARITY UNPROVED.**

## 1. Purpose

M5-362 decomposed the angular Biot--Savart source into sub-natural, natural, remote, and multiscale-spread possibilities.

M5-374 corrected the productive shell ledger so that all shells are compared at one common center before taking a spatial supremum.

M5-375 then showed that fast diffuse shell proliferation is expensive, but left a slow diffuse branch.

The present checkpoint asks a more basic question:

\[
\boxed{
\text{Can a productive shell distribution be diffuse over more and more shells while remaining tight in normalized scale?}
}
\]

On the discrete dyadic scale lattice, the answer is no.

This is a concentration-compactness statement, not a new PDE estimate.

## 2. Productive event on each bounded-stage first-hitting level

Let

\[
W(t_{j+1})=qW(t_j),
\qquad q>1,
\]

and let

\[
r_j=\sqrt{\frac{\nu}{W(t_j)}}.
\]

On the branch where the existing normalized-stage ceiling applies, M5-340/M5-362 imply that each sufficiently late stage contains a smooth pre-singular event

\[
(x_j,t_j^*)
\]

at which the normalized longitudinal stretching is bounded below by a fixed positive constant.

Use physical source shells

\[
R_{j,k}\asymp 2^kr_j,
\qquad k\in\mathbb Z.
\]

At the common event center define the signed productive shell amplitudes

\[
\boxed{
 a_{j,k}
 :=
 [\widetilde\gamma_{j,k}(x_j,t_j^*)]_+
 \ge0.
}
\]

Let

\[
\boxed{
A_j:=\sum_{k\in\mathbb Z}a_{j,k}.
}
\]

Since

\[
[\sum_k\widetilde\gamma_{j,k}]_+
\le
\sum_k[\widetilde\gamma_{j,k}]_+,
\]

one has

\[
\boxed{A_j\ge c_0>0.}
\]

## 3. Finiteness firewall

At every smooth pre-singular event with nonzero core vorticity, the near-shell productive sum is finite under ordinary local smoothness: the vorticity direction varies at most linearly in distance on the intense core, making the near angular shell contributions summable.

The far-shell productive sum is finite under the finite-energy/far-field control already used in M5-371.

If either summability fails, the event has already entered the near-Dini/high-derivative or remote/non-tight branch and need not be retained in the residual compact-scale analysis.

Thus on the residual branch we may normalize

\[
\boxed{
p_{j,k}:=\frac{a_{j,k}}{A_j}.}
\]

Then

\[
p_{j,k}\ge0,
\qquad
\sum_{k\in\mathbb Z}p_{j,k}=1.
\]

Each `p_j` is therefore a probability distribution on the discrete normalized scale lattice `Z`.

## 4. Definition of scale tightness

Call the sequence `p_j` **scale-tight** if for every `delta>0` there exists a finite integer `K(delta)` such that for all sufficiently large `j`,

\[
\boxed{
\sum_{|k|\le K(\delta)}p_{j,k}\ge1-\delta.
}
\]

This says that the productive source remains, up to arbitrarily small action loss, within a fixed finite number of dyadic shells around the natural vorticity scale.

Failure of this property is scale non-tightness.

## 5. Tightness forces a dominant bounded shell

Assume scale tightness.

Take

\[
\delta=\frac12.
\]

Then there exists a fixed `K` such that for all sufficiently large `j`,

\[
\sum_{|k|\le K}p_{j,k}\ge\frac12.
\]

There are exactly `2K+1` integer shell indices in this set. Therefore

\[
\boxed{
\max_{|k|\le K}p_{j,k}
\ge
\frac{1}{2(2K+1)}.
}
\]

Hence every sufficiently late tight event contains a shell in a bounded normalized scale range carrying a fixed positive fraction of the productive action.

Since the index set `[-K,K]` is finite, an infinite subsequence has one fixed shell index `k_*` with

\[
\boxed{
p_{j_n,k_*}\ge\varepsilon_*>0.}
\]

Thus

\[
\boxed{
\text{scale tightness}
\Longrightarrow
\text{fixed-fraction natural/comparable-scale productive shell on a subsequence}.
}
\]

This is exactly the natural projective/partner source route of M5-362.

## 6. Diffuseness is incompatible with tightness

Define the largest shell fraction

\[
\varepsilon_j:=\sup_k p_{j,k}.
\]

Suppose

\[
\varepsilon_j\to0.
\]

If `p_j` were scale-tight, Section 5 would give a fixed positive lower bound on `epsilon_j`, a contradiction.

Therefore

\[
\boxed{
\varepsilon_j\to0
\Longrightarrow
\{p_j\}\text{ is not scale-tight}.
}
\]

This eliminates the proposed independent state

\[
\boxed{
\text{diffuse over more and more shells but still confined to a fixed normalized scale range}.
}
\]

No such probability sequence exists.

## 7. Non-tightness forces tail escape

If `p_j` is not scale-tight, there exists `delta_0>0` such that for every `K` there are arbitrarily large `j` with

\[
\sum_{|k|>K}p_{j,k}\ge\delta_0.
\]

Choose a diagonal subsequence `j_n` with `K=n`:

\[
\sum_{|k|>n}p_{j_n,k}\ge\delta_0.
\]

Split the tail:

\[
\sum_{k>n}p_{j_n,k}
+
\sum_{k<-n}p_{j_n,k}
\ge\delta_0.
\]

For each `n`, at least one side carries at least `delta_0/2`. Passing to a further subsequence fixes the side.

Therefore one has either

\[
\boxed{
\sum_{k>n}p_{j_n,k}\ge\frac{\delta_0}{2}
}
\]

for all `n` on the subsequence, or

\[
\boxed{
\sum_{k<-n}p_{j_n,k}\ge\frac{\delta_0}{2}.
}
\]

These are the two scale-escape directions.

## 8. Positive tail = remote/ambient source turnover

If

\[
\sum_{k>n}p_{j_n,k}\ge\delta_0/2,
\]

then a fixed positive fraction of the productive longitudinal stretching is generated at normalized distances

\[
\frac{R}{r_{j_n}}\to\infty.
\]

Thus the productive source is not tight around the natural first-hitting core.

This is precisely

\[
\boxed{
T_{\rm remote}
\lor
H_{\rm ambient}
}
\]

in the existing proof tree.

No single remote shell needs to dominate; block tail escape is already enough to establish loss of normalized spatial/source tightness.

## 9. Negative tail = sub-natural derivative/high-frequency escape

If

\[
\sum_{k<-n}p_{j_n,k}\ge\delta_0/2,
\]

then a fixed positive fraction of productive stretching is generated at scales

\[
\frac{R}{r_{j_n}}\to0.
\]

The core is therefore being stretched by progressively finer misaligned vorticity structure below its own natural vorticity scale.

By the M5-362/M5-372 routing, this is

\[
\boxed{
H_{\rm der/occ}
\lor
H_{\rm high-freq}.
}
\]

Again no single shell needs to dominate: negative-tail action itself is the high-frequency scale escape.

## 10. Discrete concentration-compactness trichotomy

Combining Sections 5--9 gives the exact qualitative classification.

For every infinite sequence of productive first-hitting shell distributions, after taking a subsequence one has

\[
\boxed{
\begin{array}{rcl}
\text{scale-tight}
&\Longrightarrow&
\text{fixed-fraction bounded-}k\text{ shell},\\[1mm]
\text{positive scale escape}
&\Longrightarrow&
T_{\rm remote}/H_{\rm ambient},\\[1mm]
\text{negative scale escape}
&\Longrightarrow&
H_{\rm der/occ}/H_{\rm high-freq}.
\end{array}
}
\]

There is no fourth qualitative alternative.

## 11. Consequence for the M5-375 slow-diffuse label

M5-375 introduced a quantitative residual label

\[
H_{\rm slow-scale-spread}
\]

for sequences with

\[
\varepsilon_j\to0
\]

but too slowly to force a finite-dissipation contradiction.

The present result shows that this is **not an independent geometric endpoint**.

Any such slow-diffuse sequence must be scale non-tight and hence already lies in

\[
\boxed{
H_{\rm der/occ}
\lor
T_{\rm remote}/H_{\rm ambient}.
}
\]

M5-375 remains useful quantitatively because it prices how fast the non-tight spread can occur on the non-sub-natural side, but its slow-diffuse label is removed from the terminal qualitative proof tree.

## 12. Updated angular proof tree

The M5-362 four-way angular split

\[
\text{sub-natural}
\lor
\text{natural}
\lor
\text{remote}
\lor
\text{multiscale spread}
\]

now reduces to the concentration-compactness trichotomy

\[
\boxed{
H_{\rm angular}
\Longrightarrow
H_{\rm der/occ}
\lor
P_{\rm angular,natural}
\lor
T_{\rm remote}/H_{\rm ambient}.
}
\]

The independent `H_angular,multiscale` leaf is deleted.

## 13. Updated similarity-gradient reduction

Combining M5-371, M5-372, and the present checkpoint gives the sharper source-level reduction

\[
\boxed{
H_{\nabla,\rm sim}
\Longrightarrow
H_{\omega,\infty}
\lor
H_{\rm der/occ}
\lor
P_{\rm angular,natural}
\lor
T_{\rm remote/core/temporal}
\lor
H_{\rm ambient}.
}
\]

This is a pruning result, not an exclusion of these survivors.

## 14. DSD analysis interpretation

The key descriptive distinction is now **tightness of the normalized source distribution**, not merely the number of listed scales.

A proper DSD state for the productive source must retain

\[
\boxed{
(\text{normalized shell index distribution},\text{total productive action},\text{center/time ancestry}).
}
\]

This prevents the phrase `multiscale` from creating a spurious fourth category when the actual mathematical alternatives are compactness, positive escape, or negative escape.

## 15. Audit firewalls

### Firewall A: productive, not unsigned, distribution

The probability weights are built from positive signed longitudinal-stretching contributions, not from arbitrary vorticity-direction roughness.

### Firewall B: common center

The shell distribution belongs to one productive event center. Shellwise maxima at different centers cannot be mixed into one probability distribution.

### Firewall C: bounded-stage branch

The event extraction uses the existing normalized-stage ceiling. Loss of that ceiling remains a temporal turnover/concentration branch.

### Firewall D: classification is not contradiction

Scale escape is routed to already known H/T branches; it is not thereby excluded.

## 16. Audit verdict

### PROVED

- productive shell weights define a probability distribution on the dyadic normalized scale lattice on the residual smooth finite-source branch;
- scale tightness forces a fixed-fraction bounded-index shell;
- `max shell fraction -> 0` is incompatible with scale tightness;
- scale non-tightness forces positive-tail or negative-tail action escape after subsequence extraction;
- the independent diffuse/multiscale angular leaf is absorbed into natural partner, remote turnover, or sub-natural derivative routes.

### REMOVED FROM THE TERMINAL TREE

\[
\boxed{H_{\rm angular,multiscale}\text{ as an independent qualitative endpoint}.}
\]

### STILL OPEN

- natural-scale productive partner/projective network;
- sub-natural derivative/high-frequency occupancy;
- remote/ambient source non-tightness;
- temporal/core turnover if the bounded-stage event extraction fails;
- vorticity-amplitude escalation branch;
- global regularity.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
