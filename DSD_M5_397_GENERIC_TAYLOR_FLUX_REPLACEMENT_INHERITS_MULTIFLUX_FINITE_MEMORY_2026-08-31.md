# DSD M5-397 — Generic Taylor flux replacement inherits the multiflux finite-memory cap

Date: 2026-08-31

Status: **M5-395 REMOVES THE POSITIVE-MIDDLE GEOMETRY FROM THE STEP THAT CREATES A FIXED REPLACEMENT FLUX / THEREFORE THE OLDER COHERENT MULTIFLUX `N^2` ENSTROPHY PACKING THEOREM CAN BE APPLIED TO ANY FIRST-HITTING TAYLOR REPLACEMENT STAGE ON WHICH SURVIVING OLD AND NEW FLUX POPULATIONS REMAIN COHERENTLY STORED IN ONE BOUNDED NORMALIZED REGION / UNDER BOUNDED NORMALIZED ENSTROPHY, ONLY FINITELY MANY SUCH FIXED-FLUX POPULATIONS CAN BE STORED / REPEATED GENERIC REPLACEMENT MUST THEREFORE PRODUCE VISCOUS FLUX CHANGE, PROJECTIVE/NONCOHERENT REORGANIZATION, EXPORT, OR AN ENSTROPHY-H ESCAPE WITHIN A UNIFORM FINITE NUMBER OF UNCOMPENSATED REPLACEMENTS / POSITIVE-DENSITY REPLACEMENT CONSEQUENTLY FORCES POSITIVE-FREQUENCY COSTED EXITS / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Purpose

The older scale-invariant flux replacement routing and coherent multiflux theorem were developed on a specialized coherent positive-middle replacement lane.

Their logic had two parts:

1. create a fixed new-label flux fraction;
2. use material-flux survival plus bounded-region packing to show that indefinite old/new flux storage is impossible.

M5-395 has now replaced Part 1 by a more general theorem:

\[
\boxed{
\text{fixed target-volume replacement in a Taylor carrier}
\Longrightarrow
\text{fixed non-parent target flux }\ge c_{rep}\nu.
}
\]

The present note audits which parts of the older multiflux machinery therefore transfer to arbitrary first-hitting Taylor replacement.

---

## 2. Generic replacement event

At stage `j+1`, let the current Taylor carrier be a fixed normalized cylinder `C_{j+1}` with axis `xi_{j+1}` and directed lower bound

\[
\xi_{j+1}\cdot\omega
\ge c_0W_{j+1}.
\]

Let `A_j(t_{j+1})` be the material image of the selected parent carrier.

Fix `delta>0` and assume

\[
\alpha_j
:=
\frac{|C_{j+1}\cap A_j(t_{j+1})|}{|C_{j+1}|}
\le1-\delta.
\]

M5-395 yields a transverse target patch carrying non-parent directed flux

\[
\boxed{
\Phi_{new,j+1}
\ge c_{rep}\nu,
}
\]

with `c_rep>0` fixed independently of `j`.

This is the only replacement-flux input needed in the present extension.

---

## 3. Audit the parent flux

The previous parent carrier entered stage `j` with directed flux

\[
\Phi_{old,j}\ge c_{old}\nu.
\]

Transport a selected material surface patch of this carrier to `t_{j+1}`.

By the exact material-surface flux identity of M5-393, only two possibilities exist at a fixed flux threshold.

### A. Robust old-flux loss

A fixed fraction of the old signed flux is lost or changed.

Then

\[
\boxed{
T_{replacement}
\to
H_{viscous\ flux}
}
\]

or to the already typed irregular/projective loss if the comparison geometry itself breaks.

### B. Old flux survives

A fixed old material flux amount

\[
\Phi_{old}^{surv}
\ge c_s\nu
\]

remains identifiable at `t_{j+1}`.

Then the same time slice contains:

\[
\boxed{
\text{surviving old material flux}
+
\text{non-parent current target flux}.
}
\]

These are distinct material-label populations by construction.

---

## 4. Where can surviving old flux go?

Relative to a fixed bounded normalized observation region around the current first-hitting core, surviving old flux has only the following typed possibilities.

### A. Coherent local storage

It remains in the bounded region and can be represented, together with the current flux populations, by a common-axis coherent storage cylinder after a fixed finite partition into angular sectors.

### B. Projective/noncoherent reorganization

Its direction differs by an order-one angle, its transverse frame rotates, or no common coherent sector can retain a fixed flux fraction.

This is already

\[
\boxed{
T_{projective/noncoherent}
\lor
H_{direction/capacity}.
}
\]

### C. Export

It leaves every retained bounded normalized storage region.

This is

\[
\boxed{T_{export/remote}.}
\]

Thus only Case A can represent quiet local storage.

---

## 5. Coherent multiflux packing is geometry-independent after fixed flux is known

The older coherent multiflux theorem considers `N` distinguishable material flux populations in one bounded normalized cylinder

\[
\mathcal C=D_R\times[-H/2,H/2]
\]

with common axis `e`.

Suppose each population carries fixed normalized flux at least `phi_0>0` over a fixed axial occupancy fraction `beta>0`.

Then slice-wise Cauchy--Schwarz and disjoint material-label area packing give

\[
\int_{D_R}|\Omega|^2dA
\ge
\frac{n(z)^2\phi_0^2}{A_R}.
\]

After integration in the axial coordinate,

\[
\boxed{
\int_{\mathcal C}|\Omega|^2dY
\ge
c(R,H,\beta)N^2\phi_0^2.
}
\]

Therefore on a bounded normalized-enstrophy branch

\[
\|\Omega\|_2^2\le Z_+,
\]

one has

\[
\boxed{
N\le N_{max}(Z_+,R,H,\beta,\phi_0)<\infty.
}
\]

Crucially, this packing proof does **not** use the positive-middle strain eigenvalue geometry once the fixed-flux populations and common-axis coherent storage description have been formed.

Hence M5-395 supplies exactly the input needed to transfer this finite-memory result to generic Taylor replacement.

---

## 6. Finite-memory theorem for generic Taylor replacement

Work on the bounded normalized-enstrophy branch

\[
\boxed{Z\le Z_+.}
\]

Suppose there are repeated fixed-deficit replacement events

\[
\alpha_j\le1-\delta.
\]

Each such event creates at least one fixed non-parent target flux population of size `>=c_rep nu`.

If old flux populations are neither destroyed nor exported nor projectively/noncoherently reorganized, they accumulate as distinguishable coherent local material flux populations.

But the coherent multiflux theorem permits at most `N_max` such stored populations.

Therefore within at most

\[
\boxed{B:=N_{max}+1}
\]

uncompensated generic replacement events, at least one of the following must occur:

\[
\boxed{
\begin{aligned}
& H_{viscous\ flux},\\
& T_{projective/noncoherent}\lor H_{direction/capacity},\\
& T_{export/remote},\\
& H_Z:\ Z>Z_+.
\end{aligned}
}
\]

Thus generic Taylor replacement has finite material-flux memory.

---

## 7. The unbounded-Z branch is already H

If the normalized enstrophy bound required by Section 6 fails along the replacement sequence,

\[
Z_j\to\infty
\]

or exceeds every retained threshold, then the process has entered precisely a critical mass/occupancy escalation.

Thus

\[
\boxed{
Z\text{ unbounded}
\Longrightarrow
H_{crit\,mass/occupancy}.
}
\]

The finite-memory theorem therefore loses nothing by conditioning on bounded `Z`.

Either `Z` itself is H, or bounded `Z` gives finite flux-storage capacity.

---

## 8. Positive-density replacement forces positive-frequency exits

Suppose fixed-deficit replacement occurs on a set of first-hitting generations of lower density

\[
\underline d_{rep}>0.
\]

Partition the ordered replacement events into consecutive blocks of at most `B=N_max+1` events.

Every full block contains at least one exit of one of the finite types in Section 6.

Hence the total number of costed exits among the first `M` replacement events is at least

\[
\frac{M}{B}-O(1).
\]

Therefore the union of costed exits has positive density relative to replacement events, at least `1/B`.

Since replacement itself has generation density `underline d_rep`, the union has positive lower generation density

\[
\boxed{
\underline d_{exit}
\ge
\frac{\underline d_{rep}}{B}>0
}
\]

up to the fixed endpoint bookkeeping.

There are only finitely many exit categories.

By the infinite pigeonhole principle, at least one category occurs with positive lower frequency along a further subsequence/block selection.

Thus

\[
\boxed{
\text{positive-density generic replacement}
\Longrightarrow
\text{positive-frequency typed H/T exit}.
}
\]

---

## 9. Relation to the existing finite-memory replacement theorem

The older finite-memory theorem already established this positive-frequency mechanism after a fixed replacement flux had been created on its specialized geometry.

M5-397 does not claim a new combinatorial principle.

Its new scope point is:

\[
\boxed{
\text{M5-395 makes the fixed-flux input generic on every fixed-deficit Taylor replacement stage.}
}
\]

Therefore the finite-memory routing no longer needs positive-middle ribbonization merely to enter the flux ledger.

Positive-middle-specific taxes remain positive-middle-specific, but the flux-storage/memory part is generic.

---

## 10. Route the main exits through the later proof tree

The generic exits are already represented in the post-M5-380 tree.

### Viscous flux loss

Regular fixed-flux destruction/reorganization through a thin layer routes to normalized palinstrophy/derivative H; irregular loss remains explicit geometry/projective T/H.

### Projective/noncoherent exit

Order-one directional/frame reorganization is already part of the projective/angular-capacity ledger and cannot be called quiet replacement.

### Export

Formed export enters M5-386--388. On the complete formed weak-critical branch, uniform weak-`L3` closes by Albritton--Barker; weak-`L3` escalation returns to frequency/Campanato H/T.

### Enstrophy escalation

This is directly `H_crit mass/occupancy`.

Thus repeated generic replacement does not create a new fifth type of endpoint.

---

## 11. Near-full contact is not covered by the fixed-deficit theorem

M5-395 and M5-397 require one fixed `delta>0` with

\[
\alpha_j\le1-\delta.
\]

They do not claim a uniform replacement flux if

\[
1-\alpha_j\to0.
\]

That near-full target-contact regime remains governed by M5-393:

\[
\text{near-full material contact}
\Longrightarrow
H_{viscous\ flux}
\lor
T_{projective/replacement}
\lor
G_{persistent\ material\ flux\ funnel}.
\]

Hence fixed-deficit replacement and near-full contact remain disjoint audited branches.

---

## 12. DSD audit

### Valid transfer

- M5-395 supplies a fixed non-parent target flux without positive-middle geometry;
- the coherent multiflux `N^2` packing proof uses only fixed flux, disjoint material labels, common-axis coherent storage, and bounded normalized region/enstrophy;
- failure of common-axis coherence is retained as projective/noncoherent H/T;
- failure of bounded normalized storage is export/remote;
- failure of bounded normalized enstrophy is H.

### Forbidden inference

Do not assume all old flux populations are common-axis coherent.

Do not count exported populations inside the local multiplicity cap.

Do not count a population after robust viscous flux destruction as if the same fixed charge survived.

Do not infer a contradiction from positive-frequency exits alone unless that exit's own later closure applies.

---

## 13. Updated replacement frontier

The generic fixed-deficit replacement branch is now

\[
\boxed{
T_{fixed\ deficit\ replacement}
\Longrightarrow
H_{crit\,mass/occupancy}
\lor
H_{viscous/direction}
\lor
T_{projective/noncoherent}
\lor
T_{export/remote},
}
\]

with positive-frequency transfer whenever replacement itself has positive lower density.

Thus `replacement` no longer needs to remain as an unpriced standalone genealogy leaf on the bounded local formed corridor.

---

## 14. Combined local frontier after M5-393--397

The remaining local formed alternatives are now best written as

\[
\boxed{
G_{persistent\ material\ flux\ funnel/dual-source}
\lor
H_{crit\,mass/frequency/direction}
\lor
H_{nonlocal\ strain}
\lor
T_{projective/export/remote/compactness}.
}
\]

Fixed-deficit replacement has been absorbed into the latter H/T exits.

The next question is whether the **persistent local funnel/dual-source branch**, when it remains spatially tight and avoids those H/T exits, automatically enters the existing complete ancient weak-`L3` Liouville corridor.

---

## 15. Audit verdict

### NEW SCOPE EXTENSION

\[
\boxed{
\text{generic first-hitting Taylor replacement}
\Longrightarrow
\text{finite fixed-flux memory on bounded local }Z.
}
\]

### REMOVED AS STANDALONE LONG-TIME LEAF

Indefinitely repeated quiet fixed-deficit Taylor replacement in a bounded coherent local region.

### STILL OPEN

- persistent local material-flux funnel / dual-source recurrence;
- H critical mass/frequency/direction branches;
- remote/nonlocal strain;
- projective/export/compactness failures;
- global regularity.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
