# M18-054 — AC event-orientation dictionary separates forward first-hitting nesting, backward ancestor records, second-generation blow-downs, and terminal similarity events

**Date:** 2026-09-11  
**Status:** ANCESTRY-CONVERSION COORDINATE DICTIONARY / RECORD-ORIENTATION CERTIFICATE / MULTIPLICITY FIREWALL

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Purpose

M18-053 chooses \(\mathcal R_{AC}\) as the next primary root and identifies a first obligation:

\[
\boxed{\text{build the exact event-orientation dictionary}.}
\]

The same numerical factor

\[
R=q^{m/2}
\]

appears in several different constructions, but its mathematical meaning changes with the chosen parent and time direction.

Conflating these meanings creates false positive-\(R\) ancestry gains, false multiplicity, or wrong parent-time placement.

This module fixes four representations:

1. forward chronological first-hitting nesting;
2. backward ancestor records in one current-stage normalization;
3. second-generation record blow-downs of the first ancient element;
4. terminal similarity production events.

## 2. First-hitting scale convention

Let

\[
W_j=q^jW_0,
\qquad
r_j=\sqrt{\nu/W_j},
\qquad q>1.
\]

Then for age \(m\ge1\),

\[
W_{j-m}=q^{-m}W_j,
\]

and

\[
\boxed{
r_{j-m}=R_mr_j,
\qquad
R_m:=q^{m/2}>1.
}
\]

This single identity underlies both the correct large-record construction and the false forward-stage shortcut.

## 3. Representation A — forward chronological first-hitting nesting

Choose an earlier/coarser stage

\[
n=j-m
\]

as the coordinate parent.

The later/finer stage \(j\) has physical scale

\[
r_j=R_m^{-1}r_n.
\]

Therefore in stage-\(n\) normalized spatial coordinates its natural radius is

\[
\boxed{R_m^{-1}\ll1.}
\]

Likewise its own parabolic time width is smaller by

\[
\boxed{R_m^{-2}.}
\]

Thus the forward chronological sequence is a **shrinking descendant sequence inside a coarse parent**.

It is not a large-\(R\) blow-down family.

### Consequence

A fixed normalized event at every later first-hitting stage cannot be inserted into the positive-\(R\) standard-energy record ledger merely by calling

\[
R_m=r_n/r_j.
\]

The actual event size in the coarse parent is \(R_m^{-1}\), not \(R_m\).

## 4. Physical cost of a forward own-scale event

For normalized spacetime enstrophy

\[
q_{E,j}
=
\int |\Omega_j|^2dyds,
\]

the corresponding physical kinetic-energy dissipation contribution is

\[
\boxed{q_{E,j}^{phys}\asymp r_jq_{E,j}}
\]

(up to the fixed viscosity normalization convention).

If

\[
q_{E,j}\ge c_*>0
\]

on every stage, then

\[
\sum_jq_{E,j}^{phys}
\lesssim
c_*\sum_jr_j
<\infty.
\]

Hence forward stage frequency is natively ancestry-cheap.

This is the first AC firewall.

## 5. Representation B — backward ancestors seen from one current finer stage

Now choose the later/finer stage \(j\) as the fixed normalization.

The earlier/coarser stage \(j-m\) appears with natural spatial radius

\[
\boxed{R_m=q^{m/2}\gg1}
\]

in stage-\(j\) variables.

Its vorticity amplitude is correspondingly reduced by

\[
R_m^{-2},
\]

and its natural time width is enlarged by

\[
R_m^2.
\]

M5-475 gives the backward first-hitting time law

\[
\boxed{|	au_m|\asymp q^m=R_m^2.}
\]

Thus old first-hitting ancestors populate a geometric sequence of **large backward scales** in one fixed current normalization.

This is a legitimate large-\(R\) geometric history.

## 6. But Representation B is not yet a cross-generation additive ledger

The old ancestor stages in Representation B are different physical epochs and can support scale-resolved statements.

However a local event extracted near the current terminal time \(\tau=0\) is not automatically present inside the old ancestor window near

\[
\tau\sim-R_m^2.
\]

Therefore

\[
\boxed{
\text{large backward ancestor scale}
\neq
\text{automatic placement of a late local payer at that scale}.
}
\]

This is the EVENT-ANNULAR / LOG-ALIGN firewall from M18-036--039.

## 7. Representation C — second-generation blow-down of the first ancient element

Let

\[
(V,\Omega)(x,t)
\]

be the first marked ancient element with backward record times

\[
T_m\asymp q^m,
\qquad
R_m:=\sqrt{T_m}\asymp q^{m/2}.
\]

The second-generation record cell is

\[
\boxed{
V_m(y,s)=R_mV(R_my,R_m^2s),
}
\]

and

\[
\boxed{
\Omega_m(y,s)=R_m^2\Omega(R_my,R_m^2s).
}
\]

This is an actual large-\(R_m\) blow-down.

A first-generation feature at physical ancient scale \(R_m\) becomes order one in the second-generation cell.

## 8. Fixed annular cell time maps to a genuine backward parent annulus

Choose

\[
I=[-b,-a],
\qquad 0<a<b<\infty.
\]

Then the second-generation cell window maps exactly to the first ancient parent window

\[
\boxed{
I_m^{anc}=R_m^2I
=[-bR_m^2,-aR_m^2].
}
\]

Because

\[
R_m^2\asymp q^m,
\]

these intervals have uniformly finite overlap after passing to finitely many residue classes if needed.

This is a genuine additive genealogy feature: different record indices correspond to different old parent-time regions, not merely different coordinate descriptions of one same event.

## 9. Exact resource mapping in Representation C

For palinstrophy,

\[
\boxed{
R_m^{-1}
\int_I\|\nabla\Omega_m(s)\|_2^2ds
=
\int_{I_m^{anc}}\|\nabla\Omega(t)\|_2^2dt.
}
\]

Finite overlap therefore gives

\[
\boxed{
\sum_mR_m^{-1}
\int_I\|\nabla\Omega_m\|_2^2ds
<\infty.
}
\]

The corresponding derivative-order laws are

\[
q_k^{parent}=R_m^{1-2k}q_k^{(m)}.
\]

Thus the second-generation record construction is the correct setting for the known \(R^{-1},R^{-3},R^{-5}\) ancestry ledgers.

## 10. Representation C multiplicity is real only inside fixed parent windows

Suppose cell \(m\) contains payment regions

\[
Q_{m,1},\dots,Q_{m,N_m}\subset\mathbb R^3\times I.
\]

They may be summed only if they are pairwise disjoint or uniformly bounded-overlap **in cell variables**, so that their pullbacks are correspondingly controlled inside the same parent window \(I_m^{anc}\).

Then palinstrophy gives

\[
\sum_m\frac{1}{R_m}
\sum_jc_{m,j}<\infty.
\]

A contradiction needs

\[
\boxed{
\sum_m\frac{1}{R_m}
\sum_jc_{m,j}=\infty.
}
\]

Polynomial/logarithmic record multiplicity is insufficient against geometric \(R_m\).

## 11. Intrinsic rerecording inside one record cell is not new multiplicity

Inside a fixed second-generation cell one may choose a new intrinsic scale \(r\) and rerecord the same event.

For any homogeneous resource exponent \(\alpha\),

\[
q_\alpha[S_r\Omega]=r^\alpha q_\alpha[\Omega],
\]

while the total parent factor changes from \(R\) to \(Rr\).

Thus

\[
\boxed{
(Rr)^{-\alpha}q_\alpha[S_r\Omega]
=R^{-\alpha}q_\alpha[\Omega].
}
\]

Hence intrinsic rerecording exactly preserves parent charge.

It creates no multiplicity and no ancestry gain.

## 12. Representation D — terminal similarity production events

The hard compact similarity system uses a similarity time \(\theta\) moving toward the terminal singular regime.

M5-589--590 produce fixed-duration positive-density events in this similarity time:

\[
I_{\theta_0}\times\mathcal A_*
\]

with a fixed positive local production charge and a recurrent persistent payer lineage.

These are **late/terminal similarity events**.

They are not automatically the same objects as the old backward record annuli

\[
[-bR_m^2,-aR_m^2]
\]

of Representation C.

## 13. Similarity-time recurrence does not imply record-phase alignment

A positive-density set in similarity time can avoid a prescribed geometric/arithmetic sequence of record phases unless an additional synchronization theorem is proved.

Equivalently, after converting physical backward scale to logarithmic similarity time, one needs control of the phase between:

- terminal recurrent production times;
- first-hitting generation times;
- second-generation record centers.

Therefore

\[
\boxed{
\text{positive similarity-time density}
\not\Rightarrow
\text{one payer in every backward record annulus}.
}
\]

This is the LOG-ALIGN problem.

## 14. Rerooting at every production event does not solve multiplicity

One could recenter/rescale the solution separately at every terminal production event.

This produces many locally normalized states, but each now has a different parent normalization.

Without an exact map back to one common parent history, one cannot sum their positive-\(R\) charges.

Thus

\[
\boxed{
\text{many rooted copies}
\neq
\text{many independent records in one parent budget}.
}

This is the second AC firewall.

## 15. Four-representation dictionary

\[
\boxed{
\begin{array}{l|l|l|l}
\text{representation}&\text{chosen parent}&\text{natural ratio}&\text{main use}\\
\hline
A\ \text{forward stages}&\text{earlier coarse stage}&R^{-1}&\text{chronological nesting}\\
B\ \text{backward ancestors}&\text{current fine stage}&R&\text{large-scale old history}\\
C\ \text{second-gen blow-down}&\text{first ancient element}&R&\text{true cross-generation ledger}\\
D\ \text{terminal production}&\text{similarity hull state}&\text{phase/time recurrent}&\text{local payer extraction}
\end{array}
}
\]

Only Representation C presently supplies the fully certified large-\(R\), fixed-parent, annular-safe ancestry ledgers.

Representation B supplies the geometric source of those records but not automatic placement of late terminal payers.

Representation D supplies payer recurrence but not automatic record ancestry.

Representation A supplies chronological first-hitting recurrence but naturally carries summable shrinking-scale physical weights.

## 16. AC problem restated after the dictionary

The main ancestry-conversion problem is now extremely specific:

\[
\boxed{
\text{Representation D payer recurrence}
\stackrel{?}{\longrightarrow}
\text{Representation C nonreused annular payments}
}
\]

or, alternatively,

\[
\boxed{
\text{Representation A/B fresh-carrier recurrence}
\stackrel{?}{\longrightarrow}
\text{sufficient physical ancestral dwell/multiplicity}.
}
\]

The missing object is a **cross-representation event synchronization theorem**.

## 17. Which quantities are already safe under Representation C

If an event is successfully placed in a fixed cell annulus \(I\), then the following parent ledgers are already certified:

\[
\boxed{
\sum_mR_m^{-1}q_{P,m}<\infty,
}
\]

\[
\boxed{
\sum_mR_m^{-3}q_{H,m}<\infty,
}
\]

\[
\boxed{
\sum_mR_m^{-5}q_{D3,m}<\infty.
}
\]

On lower-order standard-energy descendants one may obtain the stronger positive-\(R\) ledger, provided the event truly descends to spacetime enstrophy in the same record family.

Thus event placement, not scale algebra, is the present AC bottleneck.

## 18. Audit verdict

### Certified

1. Forward finer stages are small \(R^{-1}\) events in an earlier parent, not large-\(R\) records.
2. Earlier ancestors are large \(R\) objects in one current finer normalization.
3. M5-478 second-generation blow-down is the legitimate large-\(R\) fixed-parent construction.
4. Fixed annular second-generation time cells map to geometrically separated backward parent windows with bounded overlap.
5. Intrinsic rerecording of one event creates no ancestry gain or multiplicity.
6. Terminal similarity production recurrence is not automatically aligned with backward record annuli.
7. Rerooting each terminal event separately does not create one common additive parent ledger.

### Still open

1. LOG-ALIGN / cross-representation event synchronization.
2. Independent multiplicity strong enough to overcome \(R^{-1}\), \(R^{-3}\), or \(R^{-5}\).
3. Lower-order descent of selected terminal payers inside the correctly aligned record family.
4. Physical dwell amplification for fresh-carrier genealogy.
5. Boundary-only turnover coercivity.
6. Global 3D Navier--Stokes regularity.

## 19. Next target

M18-055 should audit **nonreuse and synchronization mechanisms**.

There are only a few possible sources of genuine cross-representation multiplicity:

1. disjoint parent-time annuli;
2. multiple disjoint payer windows inside one record cell;
3. distinct material labels with finite-memory constraints;
4. positive-density terminal events plus a quantitative phase-equidistribution/synchronization theorem.

The next calculation should determine which of these can actually provide multiplicity of order comparable to \(R_m\), and which are provably too sparse.
