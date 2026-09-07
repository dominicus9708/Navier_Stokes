# DSD audit-debt closure and open-root registry — Navier–Stokes proof program

Date: 2026-09-07  
Repository: `dominicus9708/Navier_Stokes`  
Scope: supplements `FULL_CANONICAL_CHAIN_ANALYSIS_AND_AUDIT_2026-09-07.md`

## Executive status

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

This note closes the **audit-status ambiguity** left after the full canonical-chain audit.  It does not declare mathematically open proof branches solved.  Instead it separates three notions that must never be conflated:

1. `AUDIT-CLOSED/PASS` — the mathematical step and its dependencies have been checked;
2. `AUDIT-CLOSED/OPEN-ROOT` or `OPEN-BRIDGE` — the audit is complete, but the mathematics remains an explicit proof obligation;
3. `QUARANTINED ROOT-CERT` — historical material is not silently imported; the downstream canonical chain is conditional until a certified root theorem is supplied.

The purpose is to prevent an uninspected historical or external dependency from being counted as a hidden proof step.

---

# A. Legacy M5-001~480 — audit debt is closed by quarantine, not by retroactive proof

The authoritative renumbering map deliberately begins the canonical inventory at legacy `M5-481`.  Legacy `M5-001~480` is not renumbered and requires a separate topic-level inventory.

The later canonical M05 index imports legacy `M5-481~502`; therefore it does not itself certify

\[
\text{arbitrary hypothetical singularity}
\Longrightarrow
\text{the starting survivor used by M5-481}.
\]

The legacy endpoint `M5-474~480` contains a bounded-ratchet ancient-element extraction and terminal-tail reductions, but those statements are conditional on the branch assumptions produced by the earlier legacy tree.

Accordingly the correct root contract is

\[
\boxed{
H_{ROOT\text{-}CERT}
:=
\left[
\text{failure of global regularity}
\Longrightarrow
\text{one of the hypotheses entering the canonical M05 survivor tree}
\right].
}
\]

Until `H_ROOT-CERT` is separately recertified from legacy `M5-001~480`, every downstream implication must be read as conditional on `H_ROOT-CERT`.

### Verdict A

- audit status: **AUDIT-CLOSED / QUARANTINED ROOT-CERT**;
- mathematical status: **OPEN-ROOT**;
- forbidden inference: canonical M05 may not be presented as an unconditional consequence of an arbitrary singularity;
- publication requirement: a topic-level root theorem or an equivalent fresh singularity-to-canonical-survivor reduction.

This removes the earlier label `AUDIT-DEBT` as an ambiguous hidden dependency.  The dependency is now explicit and quarantined.

---

# B. M5-598 non-CE-H branches — audit complete, four independent roots remain

M5-598 gives the same-event master branch menu

\[
\boxed{
CP\text{-}E
\lor CP\text{-}S
\lor CE\text{-}T
\lor Migration
\lor CE\text{-}H.
}
\]

The branch meanings are:

1. `CP-E`: transverse derivative remainder;
2. `CP-S`: transverse strain payer;
3. `CE-T`: exact anchored forced-tension branch;
4. `Migration`: surface-current / palinstrophy replacement branch;
5. `CE-H`: harmonic strain-eigenline branch.

M5-598 itself correctly records that fixed positive normalized local charge is not enough: after conversion to the similarity-generation physical scale, the cost can be geometrically summable.

The later M12–M17 chain is a descendant of `CE-H`; no canonical certificate has been found that eliminates the other four alternatives or proves that they must return to `CE-H`.

### Verdict B

\[
\boxed{
CP\text{-}E,\ CP\text{-}S,\ CE\text{-}T,\ Migration
\quad\text{remain independent OPEN-ROOT branches.}
}
\]

- audit status: **AUDIT-CLOSED / FOUR EXPLICIT OPEN-ROOTS**;
- mathematical status: **OPEN**;
- forbidden inference:
  \[
  \text{all canonical survivors}\Longrightarrow CE\text{-}H;
  \]
- permitted inference:
  \[
  CE\text{-}H\Longrightarrow M12\to M16\to M17.
  \]

Thus the audit is finished even though the four branches are not mathematically solved.

---

# C. M5-599 CE-H analyticity globalization — external theorem mapped

M5-599 uses two analytic-continuation steps.

## C.1 Spatial globalization at a fixed CE-H time

At a CE-H production time, a nonempty open ball satisfies

\[
\omega\times S\omega=0,
\qquad
\omega\times\Delta\omega=0.
\]

The M5-474 ancient element is smooth on every compact subinterval of its ancient lifespan.  Standard Navier–Stokes spatial analyticity for positive time after restarting from an interior time slice makes the two cross-product fields real analytic in `x`; the real-analytic identity theorem then extends their vanishing from the open ball to all of connected `R^3` at that time.

Relevant literature includes:

- Y. Giga, *Time and spatial analyticity of solutions of the Navier-Stokes equations*, Comm. PDE 8 (1983), 929–948, DOI `10.1080/03605308308820290`;
- Z. Grujić and I. Kukavica, *Space Analyticity for the Navier–Stokes and Related Equations with Initial Data in L^p*, JFA 152 (1998), 447–466, DOI `10.1006/jfan.1997.3167`.

## C.2 Mildness on every compact ancient-time slab

M5-474 gives, after the fixed Galilean gauge,

\[
V\in L^\infty_{loc,t}(L^6_x\cap L^\infty_x).
\]

Fix an interior time `s0`.  Since `V(s0) in L6` and

\[
V\otimes V\in L^\infty_tL^3_x,
\]

the projected Duhamel integral is locally meaningful in `L6` because

\[
\|\nabla e^{(t-s)\Delta}f\|_{L^6}
\lesssim
(t-s)^{-3/4}\|f\|_{L^3},
\]

and `(t-s)^(-3/4)` is time-integrable.  Standard `L^p` local uniqueness then identifies the smooth ancient solution with the corresponding mild solution after restarting from each interior slice.  Overlapping restart intervals cover every compact ancient-time slab.

Thus the adjective `mild` needed by bounded-mild analyticity theorems is not an extra unverified assumption on the selected branch.

## C.3 Time analyticity and the derived cross-product fields

Dong–Zhang prove that a bounded mild whole-space Navier–Stokes solution is real analytic in time for every positive time after restart:

- H. Dong and Q. S. Zhang, *Time analyticity for the heat equation and Navier-Stokes equations*, JFA 279 (2020), 108563, DOI `10.1016/j.jfa.2020.108563`.

The theorem supplies factorial time-derivative bounds in `L^infinity`.  On a strictly smaller interior time interval, standard heat/Stokes smoothing applied to the differentiated mild equation gives, for every fixed finite spatial derivative order `m`,

\[
\|\nabla^m\partial_t^nV(t)\|_\infty
\le
C_{m,I}N_I^n n^n.
\]

Only finitely many spatial derivatives are required here: `omega x S omega` uses first derivatives of `V`, and `omega x Delta omega` uses derivatives through order three.  Hence for every fixed spatial point their components are real analytic functions of time on every compact interior interval.

Since the CE-H time set has positive measure, it has an interior accumulation point.  A real-analytic scalar function whose zero set has an interior accumulation point is identically zero on its connected analytic interval; overlapping restart intervals propagate the identity through the connected ancient interval.

Therefore the theorem-to-hypothesis map needed by M5-599 is supplied on the M5-474 bounded ancient branch.

### Verdict C

- audit status: **PASS-EXTERNAL-MAPPED**;
- dependency role: the analyticity theorems remain external mathematics, but their branch hypotheses are now mapped;
- scope: this does **not** prove CE-H impossible; it only validates the reduction of CE-H to the global space-time double-eigenline class.

---

# D. M17-298 cross-scale raw-H2 allocation — natural Vitali repair audited and rejected

At one packet scale `r`, M17-298 has the sound estimate

\[
H_{pkt}\lesssim e^{-2c/r^2}r^{-1},
\]

and a same-scale disjoint/Vitali family in a radius-`R` shell contains at most `O(R^3/r^3)` packets, yielding

\[
H_{bin}(r)
\lesssim
R^3e^{-2c/r^2}r^{-4}.
\]

The unresolved step was the passage from one scale bin to **all** smaller packet scales without overcounting the same raw `H2` charge.

A natural proposed repair is to choose one variable-radius Vitali/Besicovitch family over all candidate scales.  If one had a packet estimate on the fixed dilation used to cover the candidate set, then disjoint selected balls would give

\[
\sum_i r_i^3\lesssim R^3
\]

and, for `r_i<=r_*`, monotonicity of

\[
g(r):=e^{-2c/r^2}r^{-4}
\]

at sufficiently small `r` would yield the desired total bound.

However the actual packet estimate controls the packet's selected middle/core charge.  It does **not** control the raw `H2` measure on the enlarged `5B_i` (or another covering dilation) by the same exponential packet bound.  Smaller nested derivative packets may lie inside that dilation and carry additional raw charge.  Consequently the covering theorem alone cannot transfer the one-packet exponential estimate to a cross-scale shell estimate.

The missing assertion is genuinely something like

\[
\boxed{
\mu(\lambda B_i)
\le C\,e^{-2c/r_i^2}r_i^{-1}
\quad\text{for a fixed }\lambda>1,
}
\]

or an equivalent Carleson/sparse-tree allocation controlling cross-scale multiplicity.

### Verdict D

- audit status: **AUDIT-CLOSED / REPAIR ATTEMPT TESTED**;
- mathematical status: **OPEN-BRIDGE**;
- current safe reading:
  \[
  \text{M17-298 logarithmic floor is conditional on a cross-scale raw-H2 allocation theorem.}
  \]
- M17-299 and every descendant using that logarithmic floor inherit this condition.

---

# E. M17-301 logarithmic lookback — amplitude ceiling is not an independent exit

M17-301 uses a lag

\[
T_j=A\log R_j.
\]

The previous audit grouped two possible failures into

\[
G_{parent\ ceiling/scale\text{-}map\ exit}.
\]

This can be sharpened.

At M5-474 first-hitting normalization,

\[
\Omega_j=\frac{r_j^2}{\nu}\omega,
\qquad
\|\Omega_j(\tau)\|_\infty\le1
\]

for **every represented past normalized time** `tau<=0`.  Thus, while the M17 packet is still represented by the same parent first-hitting solution and scale map, the parent absolute vorticity ceiling cannot fail independently in backward time.

The genuine possible failure is that the M17 own-scale packet description ceases to correspond to the same parent representation before the full logarithmic lookback is reached — for example through domain/packet/genealogy/scale-map exit.

Hence replace

\[
G_{parent\ ceiling/scale\text{-}map\ exit}
\]

by the sharper branch

\[
\boxed{
G_{parent\text{-}to\text{-}M17\ scale\text{-}map/domain/genealogy\ exit}.
}
\]

Conditional on absence of that exit, the ancestor amplitude ceiling is inherited automatically from first hitting.

### Verdict E

- amplitude-ceiling persistence: **PASS on every represented parent past time**;
- scale-map/domain persistence to `T_j=A log R_j`: **OPEN-BRIDGE**;
- the Duhamel identity itself: **PASS for each finite j-dependent lag for which the localized equation is defined**.

---

# F. M17-301 normalized local payment — transferred to the active calculation frontier

The remaining late-stage issue is not an unaudited assertion.  Its status is now an explicit calculation target:

\[
\boxed{
H_{unit\text{-}window\ local\ payment}
\Longrightarrow
H_{nonsummable\ physical\ payment}
\lor H_{strict\ scale\ descent}
\lor H_{bounded\text{-}multiplicity\ genealogy}
\lor H_{finite\ resource/signed\ obstruction}.
}
\]

Regression rule R21 remains mandatory:

\[
\boxed{
\text{fixed normalized payment}
\not\Rightarrow
\text{fixed physical dissipation quantum}.
}
\]

This is the next canonical calculation, beginning at M17-303.

---

# Final registry after audit-debt closure

The outstanding mathematical obligations are now explicit rather than partially audited:

\[
\boxed{
\begin{array}{ll}
R0.& H_{ROOT\text{-}CERT}:\ legacy\ M5\text{-}001\sim480\ root\ reduction,\\
R1.& CP\text{-}E,\ CP\text{-}S,\ CE\text{-}T,\ Migration,\\
R2.& M17\text{-}298\ cross\text{-}scale\ raw\text{-}H2\ allocation,\\
R3.& M17\text{-}301\ parent\text{-}to\text{-}M17\ logarithmic\ scale\text{-}map/domain\ persistence,\\
R4.& M17\text{-}301\ local\ payment\ to\ terminal\ physical/genealogical\ obstruction.
\end{array}
}
\]

The former M5-599 analyticity-hypothesis mapping is no longer listed as an unmapped audit debt; it is an externally sourced but branch-mapped analytic continuation step.

Likewise, a parent amplitude-ceiling failure is no longer counted as an independent M17-301 exit while the parent first-hitting representation remains valid.

Therefore all previously identified **audit debts** have now either been:

- passed with an explicit dependency map;
- quarantined as an explicit root theorem obligation; or
- converted into a named mathematical OPEN-ROOT / OPEN-BRIDGE.

No hidden or merely half-audited item from the 2026-09-07 full-chain audit remains in the active proof tree.

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
