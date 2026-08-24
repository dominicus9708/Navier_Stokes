# DSD Formal-Axis Terminology Correction — 2026-08-25

Status: **DSD-INTERNAL TERMINOLOGY CORRECTION / PREVIOUS GENERIC `AXIS` WORDING WITHDRAWN / MATHEMATICAL SEPARATION RESULTS RETAINED / GLOBAL REGULARITY NOT PROVED.**

This note corrects terminology in `DSD_INTERNAL_FORMATION_DESCRIBABILITY_AUDIT_2026-08-25.md` and `DSD_RECURRENT_CORE_TYPING_AUDIT_2026-08-25.md` after checking the actual Formation Axiom System and Axis-Property Axiom System definitions.

---

## 1. Formal DSD meaning of an axis

In the Axis-Property Axiom System, an axis is **not** an arbitrary independent bookkeeping variable.

The formal order is:

\[
\boxed{
\text{Formation Stage VI channel}
\to
\text{axis-channel selection}
\to
\text{realization as a one-dimensional line}
\to
\text{typed axis properties}.
}
\]

A selected axis channel must realize exactly one one-dimensional axis line under the primitive axis-realization requirement.

Therefore the words

- location;
- physical scale;
- time/genealogy;
- derivative order;
- channel type

must **not** be called five formal DSD axes merely because they are independent variables in the Navier–Stokes audit.

Unless one separately forms an approved channel for one of these items and realizes that channel as a DSD axis, they remain bookkeeping/index/descriptor coordinates.

---

## 2. Correction of the earlier audit wording

The earlier phrase

\[
\text{`location, scale, time, derivative order, channel type are five axes'}
\]

is withdrawn as formal DSD terminology.

The correct statement is

\[
\boxed{
\text{location, scale, time/genealogy, derivative order, and channel type are}\
\text{distinct descriptor coordinates/tags/indices in the present audit.}
}
\]

The mathematical conclusion that they must not be silently identified remains valid.

Thus the following distinctions survive, but they are now described correctly:

\[
\boxed{
\begin{aligned}
\text{same scale index}&\not\Rightarrow\text{same formed object},\\
\text{same derivative order}&\not\Rightarrow\text{same physical scale},\\
\text{same normalized descriptor}&\not\Rightarrow\text{same material genealogy},\\
\text{global aggregate difference}&\not\Rightarrow\text{local dynamic difference}.
\end{aligned}}
\]

These are **descriptor-coordinate/type separation statements**, not formal axis-property statements.

---

## 3. Why the correction matters

The Axis-Property Axiom System itself insists that

1. a channel must be formed before it may be selected as an axis;
2. the selected axis channel must have a one-dimensional realization;
3. the geometric axis line and the channel tag/history remain distinct;
4. even two channels realizing the same line need not have the same properties;
5. properties have typed input profiles (`tag`, `line`, `sub`, `normal`) and cannot be inferred merely from arity or geometry.

Therefore using `axis` as a synonym for `independent bookkeeping variable` would repeat exactly the kind of premature identification that DSD was designed to prevent.

This correction is not cosmetic. It changes how the Navier–Stokes bridge must be constructed:

\[
\boxed{
\text{first form PDE descriptor channels; only then decide whether any should be}\
\text{realized as formal DSD axes.}
}
\]

---

## 4. Current Navier–Stokes quantities are mostly channels/descriptors, not DSD axes

At present, quantities such as

\[
J_k,\quad Z,\quad Q,\quad \mathfrak R_k,\quad W_j,\quad r_j,
\]

and labels such as

\[
k,\quad j,\quad M,\quad T,\quad N
\]

have been used as analytic descriptors, indices, or assigned values.

They have **not** in general been passed through the formal sequence

\[
\text{formed channel}\to\text{axis selection}\to\text{1D line realization}.
\]

Therefore they should not be called DSD axes without an explicit bridge construction.

**Status: CORRECTED.**

---

## 5. What remains a legitimate use of the Axis-Property layer

The Axis-Property layer can still become relevant if the Navier–Stokes bridge explicitly selects already formed channels whose role is directional and realizes them as one-dimensional lines, for example candidate channels carrying

- a realized vorticity direction where \(\omega\neq0\);
- a strain eigen-direction with its channel tag retained;
- a selected propagation or structural direction if its Formation-stage inputs and roles have first been approved.

But even then DSD requires distinctions such as

\[
\boxed{
\text{same geometric line}
\not\Rightarrow
\text{same tagged channel property}.
}
\]

This is directly relevant to vorticity/strain alignment: geometric alignment alone cannot identify the complete tagged structural channel.

No new physical dimension is created merely because several such directional channels are represented.

---

## 6. Effect on the recurrence audit

In `DSD_RECURRENT_CORE_TYPING_AUDIT_2026-08-25.md`, the statement that the first-hitting index mixes time, scale, center, and normalization remains correct, but these should be called **descriptor coordinates/base data**, not formal DSD axes.

Thus

\[
\boxed{
R1\text{ descriptor reappearance}
\not\Rightarrow
R3\text{ material recurrence}
}
\]

remains unchanged.

The reason is formation and base-change typing, not an alleged equality/inequality between formal DSD axes.

---

## 7. DSD-internal audit lesson

This correction reveals an important methodological rule for the rest of the proof attempt:

\[
\boxed{
\text{Do not import DSD terminology into the PDE bridge before the DSD stage that}\
\text{licenses that terminology has actually been constructed.}
}
\]

In particular:

- `structure` requires a formation witness;
- `channel` requires the Formation Stage VI data;
- `axis` requires an already formed channel plus an axis realization;
- `property` requires the declared typed profile and assignment layer;
- `composition` must respect the Formation Stage VII finite-composition scope;
- `dynamics` must act on these formed/static descriptors without retroactively supplying missing formation data.

Global regularity remains **UNPROVED**.