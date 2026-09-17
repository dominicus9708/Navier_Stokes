# DSD M19-373 — Audit correction: single-law relabeling is closed, but multi-sheet patch transfer remains alongside cross-level forcing

Date: 2026-09-17  
Canonical ID: **M19-373**

Status: **AUDIT CORRECTION / M19-372 SCOPE REDUCTION / MULTI-SHEET PATCHING RESTORED**

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Correction target

M19-372 reimported M5-648--649 and stated that the full relabeling branch is eliminated.

M5-650 is the later authoritative audit correction and shows that this is too strong.

The local implication

\[
\nabla(D_B\kappa)\parallel\nabla\kappa
\Longrightarrow
D_B\kappa=f(\kappa,\theta)
\]

holds only on one connected regular quotient region.

Disconnected components of the same kappa value may carry different local scalar laws.

## 2. What remains certified from M19-372

M5-648--649 still close every connected persistent sheet on which all relevant material kappa levels share one common scalar ODE

\[
D_B\kappa=f(\kappa,\theta).
\]

Thus the valid closure is

\[
\boxed{
R_{single-law\ sheet}\Longrightarrow\bot.
}
\]

This includes both synchronized cases:

\[
c_*\equiv0
\]

and

\[
\langle c_*\rangle=0,\qquad c_*\not\equiv0.
\]

The finite base transverse-flux resource and irreversible absolute/relative flux consumption remain valid on each such common-law sheet.

## 3. Restored multi-sheet survivor

A patched quotient structure may consist of disconnected relabeling sheets

\[
\mathscr S_a
\]

with different local laws

\[
D_B\kappa=f_a(\kappa,\theta).
\]

Then scalar ODE order relative to a reference solution on another sheet need not be preserved.

Thus the relative-flux monotonicity used in M5-649 need not survive transfers between sheets.

This is a genuine recharge/patch-transfer mechanism, not a cosmetic topological detail.

## 4. Correct quotient-free forced observable

M5-650 defines

\[
a:=|W|^2,\qquad b:=W\cdot\Delta W,
\]

so on \(a>0\),

\[
\kappa=b/a.
\]

Define

\[
K:=a\nabla b-b\nabla a=a^2\nabla\kappa,
\]

\[
H:=aD_Bb-bD_Ba=a^2D_B\kappa,
\]

and

\[
M:=a\nabla H-2H\nabla a=a^3\nabla(D_B\kappa).
\]

Then the globally smooth quotient-free cross-level vector is

\[
\boxed{
\mathfrak A:=K\times M
=a^5\big[\nabla\kappa\times\nabla(D_B\kappa)\big]
}
\]

on the active set.

Hence

\[
\mathfrak A\ne0
\]

is genuine local cross-level forcing, while

\[
\mathfrak A=0
\]

permits only local sheetwise relabeling and leaves global patching unresolved.

## 5. Corrected M19 frontier

The M19-372 conclusion is replaced by

\[
\boxed{
E_{CEH}^{critical}
\Longrightarrow
F_{cross-level}^{\mathfrak A\ne0}
\lor
R_{multi-sheet/patch-transfer}
\lor
G_{strain/geometry/high-jet/genealogy/domain\ exits}.
}
\]

Thus genuine transverse kappa acceleration is one principal survivor, but it is not the only quotient survivor.

## 6. Relation to M19-369--371

The transient-seed / persistent-skeleton / renewing-sheath picture remains useful inside a connected relabeling patch.

M5-648--649 show that one such common-law patch cannot support the complete recurrent mechanism forever.

Therefore a global patched survivor must repeatedly execute at least one of:

1. transfer active flux/enstrophy population between distinct relabeling sheets;
2. pass through a critical/nodal patch where local level-sheet parametrization changes;
3. merge or split connected kappa-level components;
4. enter the genuine cross-level forcing set \(\mathfrak A\ne0\).

## 7. Renewed event target

M19-370's event problem now becomes more precise:

\[
\boxed{
\mathcal T_{patch}^{renew}:
\text{show that positive-frequency sheet transfer/critical patching is a finite-memory projective replacement event or carries a finite nonrecyclable signed charge.}
}
\]

If this is proved, the multi-sheet branch may collapse back into the already priced renewal machinery.

If not, patched relabeling remains a genuine open topology/quotient branch.

## 8. Firewall

Do not use M19-372's unrestricted statement

\[
R_{relabel}\Rightarrow\bot.
\]

The authoritative statement is only

\[
\boxed{
R_{single-law\ connected\ sheet}\Rightarrow\bot.
}
\]

M5-650 supersedes the broader reading.

## 9. Audit verdict

**CORRECTION PASS — connected common-law relabeling is closed, but multi-sheet patch transfer remains open.**

The current hard quotient problem is a two-lane frontier: genuine cross-level acceleration measured by \(\mathfrak A\), or repeated sheet-transfer/critical-patching events.

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
