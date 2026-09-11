# M18-037 — Genealogy architecture audit certifies the core derivative ledgers as annular-safe but exposes event-to-annulus localization as the live bridge

**Date:** 2026-09-11  
**Status:** AUTHORITATIVE GENEALOGY MAP AUDIT / LEDGER SAFETY CLASSIFICATION / ANNULAR-LOCALIZATION BRIDGE

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Purpose

M18-036 distinguished two fundamentally different time-window geometries:

- annular normalized windows \(I=[-b,-a]\Subset(-\infty,0)\), whose parent images have bounded overlap on geometric record scales;
- terminal windows touching \(s=0\), whose parent images are nested and cannot be independently counted from scale separation alone.

This module audits the actual late-M17/M18 resource architecture against that criterion.

The conclusion is favorable for the core derivative ledgers: palinstrophy, raw-H2, and D3 were explicitly built on annular windows or on the same finite-overlap genealogy.

The live genealogy bridge is narrower:

\[
\boxed{
\text{selected late-M18 event}
\stackrel{?}{\Longrightarrow}
\text{payment localized inside a certified annular cell}.
}
\]

## 2. Palinstrophy ledger — ANNULAR SAFE

M17-307 fixes

\[
\boxed{
I=[-b,-a],
\qquad
0<a<b<\infty,
}
\]

and maps it to

\[
I_m^{anc}
=[-bR_m^2,-aR_m^2].
\]

For geometric record scales, those parent intervals have uniformly finite overlap after a fixed residue-class decomposition.

Thus

\[
\boxed{
\sum_mR_m^{-1}
\int_I\|\nabla\Omega_m\|_2^2ds<\infty
}
\]

is a genuinely certified cross-generation ledger.

Classification:

\[
\boxed{\text{PALINSTROPHY: ANNULAR-TIME SAFE}.}
\]

## 3. Raw-H2 ledger — ANNULAR SAFE

M17-405 uses the same type of fixed annular interval

\[
I=[-b,-a]\Subset(-\infty,0)
\]

and the exact pullback

\[
R_m^{-3}
\int_I\|\Delta\Omega_m\|_2^2ds
=
\int_{R_m^2I}\|\Delta\Omega\|_2^2dt.
\]

The parent windows again have uniformly finite overlap.

Therefore

\[
\boxed{
\sum_mR_m^{-3}
\int_I\|\Delta\Omega_m\|_2^2ds<\infty
}
\]

is genealogy-safe.

Classification:

\[
\boxed{\text{RAW-H2: ANNULAR-TIME SAFE}.}
\]

## 4. D3 ledger — ANNULAR SAFE UNDER THE SAME RECORD BOOKKEEPING

M17-444 proves

\[
\int_{-\infty}^{0}\|D^3\Omega\|_2^2dt<\infty
\]

and the exact scaling

\[
\int_I\|D^3\Omega_m\|_2^2ds
=R_m^5
\int_{R_m^2I}\|D^3\Omega\|_2^2dt.
\]

It explicitly states that the record ledger is obtained under the same finite-overlap genealogy bookkeeping as M17-405.

Hence

\[
\boxed{
\sum_mR_m^{-5}
\int_I\|D^3\Omega_m\|_2^2ds<\infty
}
\]

is annular-safe whenever the same fixed annular record cell is used.

Classification:

\[
\boxed{\text{D3: ANNULAR-TIME SAFE}.}
\]

## 5. First coefficient jet — CONDITIONALLY ANNULAR SAFE

M17-445 controls

\[
G_m
=
\int_I\int_{U_m(s)}
\rho_m^2|\nabla\kappa_m|^2dyds
\]

through the D3 charge plus a compact-coefficient palinstrophy correction.

Its ancestry bookkeeping uses the same bounded-overlap record genealogy.

Therefore, when

\[
U_m(s)\subset\mathbb R^3
\]

is retained over the certified fixed annular time interval \(I\), the first-coefficient-jet resource is genealogy-safe with weight

\[
R_m^{-5}.
\]

Classification:

\[
\boxed{
\text{FIRST COEFFICIENT JET: ANNULAR SAFE PROVIDED THE RETAINED CE-H CELL LIVES INSIDE THE CERTIFIED }I.
}
\]

## 6. Positive-R standard-energy ledger — SAFE UNDER THE SAME BOUNDED-OVERLAP MAP

M18-010 / legacy M17-479A uses

\[
\sum_mR_mq_{E,m}<\infty
\]

under a representation-safe family of parent record windows with bounded overlap.

If the derivative payment is localized in the same M17-307/M17-405 annular cell, this bounded-overlap hypothesis is automatically supplied by the established record geometry.

If a payment is only known on a terminal window touching \(s=0\), the positive-R standard-energy argument does **not** by itself certify independent counting across scales.

Classification:

\[
\boxed{
\text{STANDARD ENERGY: ANNULAR SAFE / ENDPOINT CONDITIONAL}.}
\]

## 7. Temporal-thickening theorems are local, not genealogy certificates

M18-006 / legacy M17-475 proves that a raw-H2 endpoint spike thickens backward in any available smooth same-branch CE-H window.

M18-025 proves the analogous palinstrophy crossing/occupation estimate.

These are local time-thickness theorems. They do not specify where the selected endpoint lies relative to the fixed annular record cell used by the cross-generation ledgers.

Therefore there are two cases.

### A. Interior-annular endpoint

If a selected endpoint

\[
t_*\in I_0\Subset I=[-b,-a]
\]

and the required backward window remains inside \(I\), then the thickened payment lies entirely inside the annular-safe cell.

The ancestry ledger applies directly.

### B. Terminal endpoint

If the only selected event is tied to

\[
s=0
\]

or to a backward window of the form

\[
[-T,0],
\]

then its parent windows are nested across scales.

The local thickening theorem remains valid, but multiplicity across records is **not** certified by scale separation alone.

## 8. Active-time flux events have the same placement issue

M18-020--021 convert robust flux-loss events with positive active-time measure into spacetime payers.

If the active-time set is contained in a fixed annular cell

\[
\mathcal A_m\subset I=[-b,-a],
\]

then its resulting \(P\), raw-H2, or first-jet payments can be charged to the certified annular ledgers.

If the event is only known arbitrarily close to \(s=0\), the payment is locally valid but cross-record nonreuse remains unproved.

Thus active-time thickness and annular genealogy are separate gates.

## 9. Conductance and effective-scale modules are record-local

M18-028--035 define quantities such as

\[
\mathcal G_{c,I},
\quad
\mathfrak C_I,
\quad
K_P^{eff},
\quad
K_H^{eff},
\quad
K_3^{eff},
\quad
\zeta_P,\zeta_H,\zeta_3.
\]

These are representation-safe inside one specified record interval.

Their parent-charge conclusions are genealogy-safe only when the underlying charges \(q_E,q_P,q_H,q_{J_3}\) refer to the same certified annular interval or another independently bounded-overlap parent family.

Therefore the effective-scale dictionary does not remove the need for event placement.

## 10. Genealogy safety table

\[
\boxed{
\begin{array}{l|l|l}
\text{object} & \text{time support architecture} & \text{genealogy status}\\
\hline
P\text{ ledger} & I=[-b,-a] & \text{certified annular safe}\\
H\text{ ledger} & I=[-b,-a] & \text{certified annular safe}\\
D3\text{ ledger} & \text{same as M17-405} & \text{certified annular safe}\\
\rho^2|\nabla\kappa|^2 & \text{retained cell in }I & \text{conditionally annular safe}\\
E\text{ standard-energy ledger} & \text{bounded-overlap windows} & \text{annular safe / endpoint conditional}\\
\text{raw-H2 spike thickening} & \text{backward local window} & \text{placement required}\\
\text{P spike thickening} & \text{backward local window} & \text{placement required}\\
\text{flux-loss active set} & \text{local record interval} & \text{placement required}\\
\text{endpoint-touching record} & [-b,0] & \text{nested / reuse-unsafe}
\end{array}
}
\]

## 11. The live bridge: ANNULAR-LOC

Define the required localization certificate:

\[
\boxed{\text{ANNULAR-LOC}}
\]

to mean that for each selected record event there exists a fixed annular normalized interval

\[
I=[-b,-a],
\qquad a>0,
\]

independent of the record, such that

1. the event witness lies in a fixed interior subinterval \(I_0\Subset I\);
2. every temporal-thickening or active-time payment used in the argument remains inside \(I\);
3. the relevant CE-H/domain hypotheses remain valid throughout that payment set.

Under ANNULAR-LOC, the existing M17-307/405/444 ledgers automatically supply the required cross-generation bounded overlap.

## 12. What would establish ANNULAR-LOC

Possible valid routes include:

- the original record selection already chooses witnesses in a fixed annular cell;
- a recurrence theorem gives a comparable witness away from the terminal boundary;
- a time-translation/compactness argument moves the selected event to a fixed interior normalized time without changing its certified charge;
- a material/event genealogy theorem produces independent annular descendants.

None of these may be assumed merely because the ancient solution exists for all \(s<0\).

## 13. What does not establish ANNULAR-LOC

The following are insufficient:

- existence of an event at \(s=0\);
- a backward window \([-T,0]\) whose length is fixed in normalized coordinates;
- geometric growth of \(R_m\) by itself;
- rerecording the same endpoint event at another intrinsic scale;
- formal subtraction of nested parent windows.

These all remain compatible with repeated views of one physical event.

## 14. Main consequence

The central genealogy problem is now narrower than 'prove nonreuse for everything'.

The principal derivative ledgers are already ancestry-safe.

What remains is

\[
\boxed{
\text{late selected event}
\to
\text{ANNULAR-LOC}
}
\]

or an independent material/spatial nonreuse certificate.

Thus the next global analysis should focus on **event placement**, not on rebuilding the finite derivative budgets.

## 15. Audit verdict

### Certified

1. Palinstrophy and raw-H2 cross-generation ledgers are explicitly annular-safe.
2. D3 inherits the same finite-overlap architecture.
3. First-coefficient-jet ancestry is safe when retained inside that annular record cell.
4. Temporal thickening and active-time theorems are local and require a separate placement bridge.
5. Endpoint-touching events remain genealogy-unsafe unless independently localized or labeled.

### Not certified

1. ANNULAR-LOC for every late M18 event selected from the hypothetical singularity genealogy.
2. A recurrence/time-translation theorem producing equivalent interior-annular witnesses.
3. Independent material-label nonreuse for endpoint-only events.
4. ROOT-CERT and non-CE-H roots.
5. Global 3D Navier--Stokes regularity.

## 16. Next target

M18-038 should inspect the actual **record-selection mechanism** upstream of M17-307: how the second-generation record times \(T_m\) and canonical survivor witnesses are selected.

The question is whether their defining property is already attained on the fixed annular cell \([-b,-a]\), or only at the terminal normalized time. If the former, ANNULAR-LOC may already be implicit and should be made explicit; if the latter, it is a genuine missing bridge.