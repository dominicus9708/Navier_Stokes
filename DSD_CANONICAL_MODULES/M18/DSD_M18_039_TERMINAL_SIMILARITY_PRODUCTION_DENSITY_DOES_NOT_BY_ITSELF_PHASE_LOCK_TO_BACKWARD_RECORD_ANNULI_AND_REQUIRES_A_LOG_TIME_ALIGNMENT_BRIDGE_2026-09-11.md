# M18-039 — Terminal similarity-production density does not by itself phase-lock to backward record annuli and requires a log-time alignment bridge

**Date:** 2026-09-11  
**Status:** AUTHORITATIVE TIME-DIRECTION FIREWALL / PHASE-LOCK AUDIT / EVENT-ANNULAR BRIDGE

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Purpose

M18-038 separated structural annularity from event annularity.

The production architecture M5-587--590 is strong:

- a fixed finite-depth similarity annulus;
- a fixed positive event duration;
- positive similarity-time density;
- a fixed persistent material lineage carrying a positive share of production.

The backward record architecture M5-477--478 is also strong:

- first-hitting record times \(\tau_m\to-\infty\);
- \(T_m=-\tau_m\asymp q^m\);
- an interior carrier fixed at second-generation time \(s=-1\).

This module audits whether the first structure automatically supplies events in the second.

The answer is no without an additional time-direction/alignment theorem.

## 2. Backward record annuli

Let

\[
T_m=-\tau_m,
\qquad
c_-q^m\le T_m\le c_+q^m.
\]

A fixed normalized annular record window

\[
I=[-b,-a],
\qquad 0<a<b,
\]

corresponds in the first-generation ancient time to

\[
\boxed{
\tau\in[-bT_m,-aT_m].
}
\]

In absolute backward time \(T=-\tau>0\), this is

\[
[aT_m,bT_m].
\]

## 3. Logarithmic backward-time form

Define

\[
\vartheta:=\log T=\log(-\tau).
\]

Then record window \(m\) becomes

\[
\boxed{
J_m
=
[\log T_m+\log a,\,
 \log T_m+\log b].
}
\]

Every \(J_m\) has the same length

\[
\boxed{|J_m|=\log(b/a).}
\]

and its center advances approximately by \(\log q\) per generation.

Thus backward annular genealogy is a fixed-width moving-window problem in logarithmic time.

## 4. A sufficiently wide annulus covers the backward tail

The geometric bounds imply that one can choose fixed \(a,b\) so that

\[
\bigcup_{m\ge m_0}[aT_m,bT_m]
\]

covers every sufficiently large backward time.

For example, choose

\[
a\le c_+^{-1},
\qquad
b\ge q/c_-.
\]

Given large \(T\), choose \(m\) with

\[
q^m\le T<q^{m+1}.
\]

Then

\[
aT_m\le ac_+q^m\le T,
\]

and

\[
bT_m\ge bc_-q^m\ge q^{m+1}>T.
\]

Therefore

\[
\boxed{
T\in[aT_m,bT_m]
}
\]

for at least one \(m\).

At the same time, M18-036 guarantees uniformly bounded overlap.

So the record-annulus geometry itself is not the obstruction.

## 5. What would be enough for EVENT-ANNULAR

Let \(\mathcal E_{back}\subset(-\infty,0)\) be a set of actual first-generation ancient-time payer events.

If \(\mathcal E_{back}\) contains arbitrarily large-backward events, then the covering result of Section 4 places each sufficiently old event into at least one fixed annular record window.

If each event also carries a uniform local time thickness smaller than the interior margin of the chosen annulus, then a subsequence gives EVENT-ANNULAR.

Thus a sufficient bridge is

\[
\boxed{
\text{payer events recur as }\tau\to-\infty
\text{ with uniform normalized thickness}.}
\]

No stronger phase synchronization with the exact first-hitting times is needed once the annulus is chosen wide enough.

## 6. Why M5-589 positive density is not automatically that bridge

M5-587--590 are formulated on the hard ergodic **terminal-vorticity similarity branch**.

M5-589 produces a positive-density set of fixed-length similarity-time production windows in that recurrent terminal similarity dynamics.

M5-590 then attaches one persistent material lineage to those production windows.

By contrast, M5-477--478 select a sequence in the **backward history of the marked ancient element**:

\[
\tau_m\to-\infty.
\]

The existing statements do not identify the terminal-similarity positive-density event set with a positive-density event set in the backward logarithmic coordinate

\[
\vartheta=\log(-\tau)	o+\infty.
\]

Therefore

\[
\boxed{
\text{terminal similarity positive density}
\not\Rightarrow
\text{backward-record EVENT-ANNULAR}
}
\]

from the presently certified results alone.

## 7. Define LOG-ALIGN

Define the missing bridge

\[
\boxed{\text{LOG-ALIGN}}
\]

to mean that the quantitative payer event used in the late CE-H analysis occurs on an unbounded set of backward ancient times whose logarithms meet the fixed-width record-annulus cover with a uniform event margin.

A stronger sufficient form is positive lower density in \(\vartheta=\log(-\tau)\) as \(\vartheta\to+\infty\), but mere unbounded recurrence plus uniform thickness is already enough for an infinite annular subsequence.

Under LOG-ALIGN,

\[
\boxed{
\text{EVENT-ANNULAR follows from M18-036 + the tail cover}.}
\]

## 8. STRUCT-ANNULAR remains valid without LOG-ALIGN

M18-038 used M5-478 and M5-599 to certify that:

- the ancient cell is nontrivial at \(s=-1\);
- CE-H structural identities hold throughout the connected ancient interval, subject to the analyticity theorem.

None of this is revoked.

Hence

\[
\boxed{
\text{STRUCT-ANNULAR is certified while LOG-ALIGN may remain open}.}
\]

This distinction prevents an event-placement gap from being mistaken for loss of the CE-H equations themselves.

## 9. First-hitting recurrence is not the late payer recurrence

M5-477 proves that first-hitting carriers occur at every retained geometric backward generation and saturate the Type-I enstrophy rate.

This does provide an infinite sequence of interior nontriviality events.

However, a first-hitting carrier is not automatically a zero-tube flux-loss event, a common-mode event, a high-conductance collar, or another specific late M18 payer.

Therefore

\[
\boxed{
\text{first-hitting recurrence}
\not\Rightarrow
\text{late-payer recurrence}
}
\]

without a theorem linking the payer property to the carrier.

## 10. Exact current genealogy gap

The late CE-H chain can now be written

\[
\boxed{
\begin{aligned}
\text{first-hitting backward records}
&\Longrightarrow
\text{annular nontriviality / bounded-overlap ledgers}\\
\text{CE-H branch selection}
&\Longrightarrow
\text{global CE-H identities}\\
\text{late payer theorem}
&\Longrightarrow
\text{local payment if its witness occurs}\n\\
&\stackrel{\rm LOG\text{-}ALIGN?}{\Longrightarrow}
\text{annular repeated payments}\\
&\Longrightarrow
\text{ancestry threshold test}.
\end{aligned}
}
\]

Thus the missing bridge is not generic nonreuse; it is the recurrence/alignment of a **specific quantitative payer property** along the backward record history.

## 11. Strategic consequence

Further local CE-H differentiation will not repair LOG-ALIGN unless it proves that one of the late payer properties is forced by every sufficiently old first-hitting carrier.

Therefore there are two productive routes:

1. prove a carrier-to-payer theorem on STRUCT-ANNULAR CE-H;
2. move to the other global branches and audit whether they possess a stronger scale-invariant obstruction that avoids this recurrence bridge.

The second route is now competitive and should be pursued in parallel.

## 12. Audit verdict

### Certified

1. Fixed record annuli can be chosen wide enough to cover the entire sufficiently old backward history while retaining bounded overlap.
2. Any uniformly thick payer event recurring arbitrarily far backward can therefore be assigned to annular-safe record cells.
3. Existing terminal-similarity positive-density production does not, by itself, certify such backward payer recurrence.
4. First-hitting recurrence certifies nontrivial carriers but not every late M18 payer property.
5. LOG-ALIGN is the precise remaining time-direction bridge.

### Not certified

1. LOG-ALIGN for the zero-tube/common-mode/conductance endpoints.
2. A theorem forcing those payer properties at every old first-hitting carrier.
3. Conversion of terminal production density into backward-log-time density.
4. ROOT-CERT/non-CE-H closure.
5. Global 3D Navier--Stokes regularity.

## 13. Next target

M18-040 should broaden the audit to the four non-CE-H survivor branches already present in the M5-598 finite menu:

\[
CP\!\!-​E,
\quad
CP\!\!-​S,
\quad
CE\!\!-​T,
\quad
Migration.
\]

The goal is to classify each branch by:

- its certified local payer;
- whether that payer is signed/unsigned;
- its scale/ancestry class;
- whether it has a recurrence/nonreuse bridge;
- and whether it offers a route stronger than the LOG-ALIGN-limited CE-H path.