# DSD M17-107 — Director-area-weighted positive margin section has an exact three-halves recharge ledger

Date: 2026-09-05
Canonical ID: **M17-107**

Status: **INTERNAL PURE-KERNEL DIRECTOR-AREA-WEIGHTED MARGIN SECTION GATE / M17-106 SHOWS THAT THE CORRECT PURE-KERNEL CARRIER MEASURE IS THE FROZEN DIRECTOR-AREA TUBE FLUX `dPhi_J`, NOT A POSITIVE VOLUME DENSITY. ON ANY FIXED FAMILY OF DIRECTOR-AREA TUBE LABELS WHOSE PEAK INTERSECTIONS REMAIN UNIQUE, REGULAR, TRANSVERSE (`D_k g!=0`), AND SUB-RICCATI (`M_R2>0`), THE POSITIVE WEIGHTED MARGIN `N_R2=|a|M_R2` CAN BE INTEGRATED DIRECTLY AGAINST `dPhi_J`. M17-080 GIVES `D_B N_R2=-(3/2)N_R2+|a|R_R2`; M17-097 GIVES THE CANONICAL TUBE-SECTION SLIDE `alpha_J=-D_xi(sigma+kappa)/D_k g`. THEREFORE THE FLUX-SECTION INVENTORY OBEYS `d N_J/dtheta=-(3/2)N_J+P_J+S_J`, WHERE `P_J=int |a|R_R2 dPhi_J` IS THE PDE/HIGHER-JET RECHARGE AND `S_J=int alpha_J D_k N_R2 dPhi_J` IS THE REQUIRED SLIDING-SECTION TRANSPORT. ANY RECURRENT POSITIVE INVENTORY MUST SATISFY `mean(P_J+S_J)=(3/2)mean N_J>0`. THIS IS A GENUINE INHERITED-MEASURE THREE-HALVES PAYMENT LAW, BUT IT IS NOT A CONTRADICTION BECAUSE NEITHER CONTRIBUTION HAS A FIXED SIGN AND THE SPLIT BETWEEN PDE RECHARGE AND SECTION SLIDE IS NOT ITSELF AN INVARIANT COST. TANGENCY/BIRTH/DEATH/CHART EVENTS REQUIRE AN EXPLICIT EVENT SOURCE AND ARE NOT SILENTLY INCLUDED. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Retained transverse peak population

Work on the pure-transverse-kernel Rank-2 branch

\[
\rho>0,
\qquad
J_\xi=|J_\xi|k\neq0,
\qquad
D_k\xi=0.
\]

Let

\[
g:=D_\xi\log\rho.
\]

Fix a family `Lambda` of frozen director-area flux-tube labels such that, on a time interval, every label has one chosen peak intersection satisfying

\[
\boxed{
g=0,
\qquad
C:=D_\xi g<0,
\qquad
D_k g\neq0.
}
\]

Assume the chosen peak remains regular and has positive Riccati compensation margin

\[
\boxed{
\mathcal M_{R2}>0.
}
\]

No peak birth/death, tangency, type/chart switch, rank loss, or boundary loss of the selected tube family is included in this first clean ledger.

---

## 2. Frozen tube-label measure

M17-097 identifies the director-area flux carried by a frozen tube label as

\[
\boxed{d\Phi_J(\lambda).}
\]

This measure is materially invariant because

\[
(\partial_\theta+\mathcal L_B)\beta_\xi=0,
\qquad
\beta_\xi=\iota_{J_\xi}dV.
\]

Therefore for the fixed label set `Lambda`, `dPhi_J` has no time-dependent Jacobian factor.

This is the inherited measure required by the present section ledger.

---

## 3. Positive weighted margin

M17-080 defines

\[
\boxed{
N_{R2}:=|a|\mathcal M_{R2}.
}
\]

On the retained positive-margin peak,

\[
\boxed{N_{R2}>0.}
\]

At a material point restricted to the peak set, M17-080 gives the exact law

\[
\boxed{
D_BN_{R2}
=-\frac32N_{R2}
+|a|\mathcal R_{R2}.
}
\]

The explicit higher-jet recharge `R_R2` is the finite signed ledger derived in M17-080.

---

## 4. Canonical slide along the same director-area tube

The peak is not material.
M17-097 follows the same frozen director-area tube while sliding the chosen intersection along `k`.

Define

\[
D_J^*:=D_B+\alpha_JD_k.
\]

Preserving `g=0` gives

\[
0=D_J^*g
=D_Bg+\alpha_JD_kg.
\]

At the peak,

\[
D_Bg=D_\xi(\sigma+\kappa),
\]

so

\[
\boxed{
\alpha_J
=-\frac{D_\xi(\sigma+\kappa)}{D_kg}.
}
\]

This is uniquely fixed on the transverse branch once the same director-area tube is chosen as carrier.

---

## 5. Exact tube-section margin law

Apply `D_J^*` to `N_R2`:

\[
D_J^*N_{R2}
=D_BN_{R2}+\alpha_JD_kN_{R2}.
\]

Use Section 3:

\[
\boxed{
D_J^*N_{R2}
=-\frac32N_{R2}
+|a|\mathcal R_{R2}
+\alpha_JD_kN_{R2}.
}
\]

Define the two signed terms

\[
\boxed{
P_J:=|a|\mathcal R_{R2}
}
\]

and

\[
\boxed{
S_J:=\alpha_JD_kN_{R2}.
}
\]

Then pointwise on the tube-labelled peak section,

\[
\boxed{
D_J^*N_{R2}
+\frac32N_{R2}
=P_J+S_J.
}
\]

---

## 6. Flux-section inventory

Define

\[
\boxed{
\mathscr N_J(\theta)
:=\int_\Lambda
N_{R2}(\lambda,\theta)
\,d\Phi_J(\lambda).
}
\]

Because the label set and `dPhi_J` are fixed on the clean interval,

\[
\frac d{d\theta}\mathscr N_J
=\int_\Lambda D_J^*N_{R2}\,d\Phi_J.
\]

Hence

\[
\boxed{
\frac d{d\theta}\mathscr N_J
=-\frac32\mathscr N_J
+\mathscr P_J
+\mathscr S_J,
}
\]

where

\[
\boxed{
\mathscr P_J
:=\int_\Lambda |a|\mathcal R_{R2}\,d\Phi_J,
}
\]

and

\[
\boxed{
\mathscr S_J
:=\int_\Lambda
\alpha_JD_kN_{R2}\,d\Phi_J.
}
\]

This is the exact director-area-weighted positive-margin section ledger.

---

## 7. Recurrent three-halves payment

Suppose the clean tube-labelled section recurs in the sense that `mathscr N_J` remains bounded and has zero long-time mean drift.
Then averaging Section 6 gives

\[
\boxed{
\left\langle
\mathscr P_J+\mathscr S_J
\right\rangle
=
\frac32
\left\langle
\mathscr N_J
\right\rangle.
}
\]

If a positive flux mass supports a uniform positive margin floor, then

\[
\left\langle\mathscr N_J\right\rangle>0,
\]

and therefore

\[
\boxed{
\left\langle
\mathscr P_J+\mathscr S_J
\right\rangle>0.
}
\]

Thus recurrent sub-Riccati Rank-2 geometry must continuously pay an exact three-halves recharge on the inherited director-area measure.

---

## 8. Meaning of the two payments

The terms have different descriptor roles.

### PDE/higher-jet recharge

\[
\mathscr P_J
=\int|a|\mathcal R_{R2}\,d\Phi_J
\]

contains the explicit strain-gap and higher-jet sources of M17-080.

### Section-slide transport

\[
\mathscr S_J
=\int\alpha_JD_kN_{R2}\,d\Phi_J
\]

appears because the peak cross-section slides along each frozen director-area tube.

It is not an independent material production term.
It records the fact that different spatial points on the same conserved tube can carry different positive margins.

Only their sum is the exact recharge seen by the chosen tube-labelled peak section.

---

## 9. Event source outside the clean interval

If the selected peak intersection hits

\[
D_kg=0,
\]

or is born/dies, changes top-jet chart, loses the positive margin, reaches a spatial endpoint, or leaves the chosen descriptor domain, the fixed clean population description fails.

Then the correct integrated equation has the form

\[
\boxed{
\frac d{d\theta}\mathscr N_J
=-\frac32\mathscr N_J
+\mathscr P_J
+\mathscr S_J
+\mathscr B_N.
}
\]

The event term `mathscr B_N` must be derived from the actual event genealogy.
It is not set to zero merely because the unweighted director-area flux is conserved.

---

## 10. DSD analysis

M17-106 exposed a rank mismatch between a two-form carrier and a volume inventory.
The present gate avoids that mismatch by keeping both descriptors on the same two-dimensional tube-label measure:

\[
\boxed{
\text{frozen tube flux }d\Phi_J
\quad+\quad
\text{peak margin }N_{R2}.
}
\]

This produces a real positive inventory without inventing a pure-kernel volume density.

However, positivity belongs to `N_R2`, not to the signed PDE and slide recharge terms.

---

## 11. DSD audit

### Audit A — treating the peak as material
Rejected by the explicit `alpha_J D_k` slide.

### Audit B — replacing `dPhi_J` by area or volume measure
Rejected. The inventory is defined directly on frozen tube labels.

### Audit C — treating `P_J` and `S_J` as separately invariant costs
Rejected. The split depends on the selected moving peak section; only the full section evolution is exact.

### Audit D — setting event source to zero because director-area flux survives
Rejected. Unweighted carrier flux conservation does not conserve a margin-weighted peak population.

### Audit E — claiming positive mean recharge is contradictory
Rejected. The signed sources may supply it recurrently.

### Audit F — proof status
A canonical positive margin inventory and exact three-halves recharge law are obtained on the clean transverse population, but no upper bound or opposite-sign identity closes the recharge.

---

## 12. Updated Rank-2 frontier

On every clean recurrent transverse tube-labelled positive-margin population,

\[
\boxed{
\left\langle
\mathscr P_J+\mathscr S_J
\right\rangle
=
\frac32
\left\langle\mathscr N_J\right\rangle>0.
}
\]

Thus the remaining question is no longer whether the inherited carrier measure exists.
It does.

The high-value question is whether tangency/type/boundary events can recycle this **margin-weighted** inventory without supplying an independent positive source, or whether the event contribution `mathscr B_N` can be signed or bounded by the existing carrier invariants.

This is the **Margin-Weighted Event Source Gate (MWESG)**.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
