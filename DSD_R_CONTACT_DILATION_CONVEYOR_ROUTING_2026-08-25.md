# DSD R-Contact / Dilation-Conveyor Routing

Date: 2026-08-25

Status: **R-CONTACT IDENTIFIED AS A MATERIAL REALIZATION OF THE CRITICAL DILATION CONVEYOR / GLOBALLY RECURRENT R-HALO ROUTED CONDITIONALLY TO HISTORICAL REPLENISHMENT H_REMOTE OR T / NONRECURRENT R-HALO MERGED WITH THE ESCAPING PASSIVE-TAIL TOPOLOGY PROBLEM / FIXED-AGE R DENSITY ALONE DOES NOT ESTABLISH TAIL-WIDE RECURRENCE / GLOBAL REGULARITY UNPROVED.**

## 1. Purpose

The weighted-contact audit shows that retained old material packets have exactly the critical scaling

\[
U\sim R^{-1},
\qquad
\Omega\sim R^{-2},
\qquad
J_R\sim1
\]

when viewed from a later first-hitting scale.

Independently, `ANCIENT_CRITICAL_TAIL_DILATION_CONVEYOR_2026-08-24.md` proves that a passive critical far tail is transported outward in Leray coordinates while preserving the scale-invariant shell quantities.

This note identifies how the R branch fits into that already derived tail dichotomy.

---

## 2. First-hitting clock and dilation factor

The first-hitting/Leray clock satisfies

\[
\boxed{
s_j=j\log q+O(1).}
\]

Hence over one generation the arithmetic clock increment is `log q`, with a bounded coboundary defect.

The passive linear Leray conveyor sends

\[
R\mapsto e^{\Delta s/2}R.
\]

For the arithmetic one-generation increment,

\[
\boxed{
e^{(\log q)/2}=q^{1/2}.}
\]

The age shell radii satisfy exactly

\[
\boxed{
R_{k+1}=q^{1/2}R_k.
}
\]

Thus the first-hitting age ladder and the passive Leray dilation ladder have the same geometric scale ratio.

The bounded clock defect changes only fixed multiplicative constants and does not change the asymptotic shell ratio.

Status: **PROVED from existing clock and conveyor identities.**

---

## 3. Material interpretation

A stage-`n` packet with physical scale `r_n` remains at its own physical scale class while the distinguished current scale decreases through

\[
r_{n+h}=q^{-h/2}r_n.
\]

Viewed in the current normalization, its scale therefore moves through

\[
1,
q^{1/2},
q,
q^{3/2},
\ldots
\]

which is precisely outward motion along the age-shell ladder.

If its vorticity remains of ancestor order `W_n`, its normalized vorticity simultaneously changes as

\[
\frac{W_n}{W_{n+h}}=q^{-h}=R_h^{-2}
\]

up to the fixed base-radius factor.

Therefore retained material ancestry provides the physical genealogy behind the passive critical dilation conveyor.

This is a scale/genealogy statement, not a claim that the packet center follows a fixed radial ray or that the solution is exactly DSS.

---

## 4. Two different meanings of R recurrence

It is essential to distinguish two statements.

### R_fixed

There exists one finite age `k_0` such that weighted material contact occurs on a positive-density recurrent-time subset.

This is what the present FPIRG fixed-shell argument can produce.

### R_stack

An unbounded family of critical shell ages participates in material contact in a way that preserves the global critical shell pattern under recurrent Leray-time returns.

Only `R_stack` is a tail-wide recurrence statement.

The implication

\[
R_{fixed}\Longrightarrow R_{stack}
\]

has **not** been proved.

This distinction prevents a fixed-shell recurrence theorem from being silently promoted to a global-tail recurrence theorem.

---

## 5. Globally recurrent material critical halo

Assume the stronger `R_stack` case: the critical material halo is recurrent in a global topology strong enough that a nontrivial critical shell pattern at finite similarity radii is reproduced after recurrent Leray-time returns.

The passive conveyor moves every old shell outward by a fixed multiplicative factor over a fixed recurrent time.

Therefore reproduction of the global pattern requires new critical shell occupancy to enter from smaller similarity radii.

Schematically,

\[
\boxed{
\cdots\to R/\Lambda\to R\to\Lambda R\to\cdots,
\qquad
\Lambda=e^{T_R/2}>1.
}
\]

This is exactly the historical scale-replenishment mechanism already isolated in the repository.

`FRONTIER_HISTORICAL_RECYCLING_ROUTED_TO_H_T_2026-08-23.md` records the existing reduction

\[
\boxed{
\text{historical recycling}
\Longrightarrow
H_{remote}
\lor
T/\text{parent-energy turnover}.
}
\]

Consequently, under the stated global-recurrence hypothesis,

\[
\boxed{
R_{stack,global-recurrent}
\Longrightarrow
H_{remote}\lor T.
}
\]

Status: **PROVED AS A ROUTING CONSEQUENCE OF THE EXISTING CONVEYOR AND HISTORICAL-RECYCLING GATES; PREMISE `R_stack` NOT YET DERIVED FROM `R_fixed`.**

---

## 6. Nonrecurrent material halo

If the old material shells are not replenished so as to reproduce the global tail, the dilation conveyor carries them to larger and larger similarity radii.

For every fixed core ball `B_M`, the bounded-Z tail-decoupling estimate gives

\[
\|\nabla^mU_{>R}\|_{L^\infty(B_M)}
\to0
\]

for each fixed derivative order.

The far pressure contribution also vanishes locally, and smooth vorticity cutoffs have boundary defects tending to zero in `H^{-1}`.

Therefore the nonreplenished R halo is routed to

\[
\boxed{
\text{locally recurrent active core}
+
\text{nonrecurrent passive material tail escaping to infinity}.
}
\]

This is not a new R-specific terminal leaf; it is exactly the already identified global topology / exact-core-solution obstruction.

Status: **PROVED AS A STRUCTURAL IDENTIFICATION USING THE EXISTING LOCAL-DECOUPLING GATE.**

---

## 7. Why ordinary energy does not separate the two cases

For the critical material scaling,

\[
J_k\sim1,
\qquad
R_k\sim q^{k/2}.
\]

The ordinary physical return cost over only the current remaining-time window carries the geometric loss

\[
K_k^{-2}=q^{-k}.
\]

Therefore both a recurrently replenished halo and an escaping old halo can have finite ordinary physical dissipation in the currently available estimate.

The distinction is dynamical/topological:

- recurrent halo -> replenishment/turnover;
- escaping halo -> local decoupling but global non-L3 topology.

This confirms that attempting to close R solely by a fixed-age energy lower bound is aimed at the wrong invariant.

---

## 8. Relation to FPIRG

FPIRG currently supplies

\[
E_{+dens}
\lor
R_{fixed,+dens}
\lor
T_{multi,+dens}.
\]

The present note refines the R leaf as

\[
\boxed{
R_{fixed,+dens}
\longrightarrow
\begin{cases}
R_{stack,global-recurrent}
&\Rightarrow H_{remote}\lor T,\\
R_{escape}
&\Rightarrow \text{escaping passive-tail topology},\\
\text{insufficient tail-wide information}
&\text{if neither upgrade is proved.}
\end{cases}
}
\]

The third line is the actual current logical gap: fixed-age contact alone does not decide whether the entire non-L3 tail is replenished or escaping.

---

## 9. New bridge target

The next R-specific theorem should not be another fixed-age contact estimate.

It should establish an **all-age upgrade**, for example one of:

\[
\boxed{
R_{fixed,+dens}
+\text{cubic-tail structure}
\Longrightarrow
R_{stack,global-recurrent},
}
\]

or

\[
\boxed{
\text{failure of }R_{stack}
\Longrightarrow
\text{quantitative tail evacuation sufficient to extract an exact Liouville-class core}.
}
\]

The first would route R into the existing `H_remote/T` endgame.

The second would close the escaping-tail topology obstruction directly.

---

## 10. DSD audit

The argument keeps separate:

- fixed-age positive-density contact;
- unbounded-age critical shell stack;
- global recurrent tail pattern;
- historical replenishment;
- locally escaping passive tail.

The scale identity between material ancestry and Leray dilation does not by itself promote local recurrence to global recurrence.

---

## 11. Updated R verdict

### PROVED

- material age ladder and Leray dilation conveyor have the same geometric scale factor;
- retained ancestor packets provide the scale genealogy of the critical `1/R` tail;
- a globally recurrent critical R halo requires historical shell replenishment;
- existing historical recycling then routes that case to `H_remote` or `T`;
- a nonreplenished R halo is the already known locally invisible escaping-tail topology case.

### NOT DERIVED

- `R_fixed -> R_stack`;
- tail-wide weighted contact on a cubic-divergent age set;
- a global recurrence theorem for the material halo;
- an exact global `L3` core after tail evacuation;
- closure of `H_remote` or `T`;
- global regularity.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
