# DSD M5-201 — Fixed-Lag Contact Weighted-Return Summability Firewall

Date: 2026-08-29

Parent: `DSD_M5_200_FINITE_AGE_PLATEAU_TO_FIXED_LAG_CONTACT_REPLACEMENT_EXPOSURE_AUDIT_2026-08-29.md`

Status: **ANTI-PROOF FIREWALL / POSITIVE-DENSITY MATERIAL CONTACT AT ONE FIXED FINITE GENERATION LAG DOES NOT BY ITSELF CLOSE THE SINGULAR BRANCH / IT CAN PRODUCE A POSITIVE RETURN DENSITY `R_{k0}` FOR THAT LABEL UNDER THE EXISTING TRACKING HYPOTHESES, BUT THE CUBIC-TAIL DISSIPATION CONTRADICTION REQUIRES LOWER RETURN WEIGHT ON AN INFINITE CUBIC-DIVERGENT SET OF AGES / THE PHYSICAL DISSIPATION COST OF REPEATED FIXED-LAG NATURAL-SCALE CONTACT DECAYS LIKE THE ANCESTOR RADIUS AND IS GEOMETRICALLY SUMMABLE / THUS THE CONTACT BRANCH REJOINS THE COMPACT RECURRENT CORE + PASSIVE CRITICAL-TAIL ENDPOINT RATHER THAN BEING FALSELY DECLARED CLOSED / GLOBAL REGULARITY UNPROVED.**

---

## 1. Fixed-lag contact from M5-200

On a positive-density recurrent event set, one fixed generation lag

\[
k_0<\infty
\]

has a material contact packet satisfying, in ancestor units,

\[
\operatorname{rad}C_j
\ge
 d_nr_n,
\qquad
|\omega|
\ge
 c_nW_n,
\qquad
n=j-k_0,
\]

with fixed

\[
d_n,c_n>0.
\]

The contact portion itself has normalized volume at least

\[
\chi_0r_n^3,
\qquad
\chi_0>0.
\]

Thus there is no spatial microcollapse at this fixed lag.

---

## 2. Instantaneous first-order dissipation witness

On the contact region,

\[
|\omega|^2\le2|\nabla u|^2
\]

gives

\[
\int_{contact}|\nabla u|^2dx
\ge
\frac12c_n^2W_n^2\chi_0r_n^3.
\]

Since

\[
W_n=\frac\nu{r_n^2},
\]

we obtain

\[
\boxed{
\int_{contact}|\nabla u|^2dx
\ge
\frac12c_n^2\chi_0
\frac{\nu^2}{r_n}.
}
\]

Equivalently,

\[
\boxed{
r_n
\int_{contact}|\nabla u|^2dx
\ge
c_{ret}\nu^2,
\qquad
c_{ret}:=\frac12c_n^2\chi_0>0.
}
\]

This matches the scale-critical return witness used in the weighted return-density ledger.

---

## 3. If contact occupies positive time measure, `R_{k0}>0`

The weighted return density for one annular label is

\[
\mathfrak R_k
=
\frac1{\rho_k}
\sum_\ell\tau_{k,\ell}.
\]

At fixed lag `k_0`, the tracked physical radius is comparable to

\[
\rho_{j,k_0}
=r_{j-k_0}=r_n.
\]

If the material-contact set contains return intervals satisfying the existing amplitude-retention, shell-tracking, and finite-overlap hypotheses, their total residence produces

\[
\boxed{
\mathfrak R_{k_0}>0.
}
\]

If only a measurable contact-time set is known, standard compactness/regularity may be used to represent it by countably many return intervals up to null sets; this is an implementation detail of the existing weighted-return framework, not a new age-uniform theorem.

Thus fixed-lag contact is a genuine return, not merely Eulerian overlap.

---

## 4. Why one fixed positive return weight is not the cubic-tail contradiction

The finite return-density ledger has the form

\[
\boxed{
\sum_kJ_k\mathfrak R_k<\infty
}
\]

under its tracking and overlap hypotheses.

The cubic-tail contradiction requires an infinite subset `S` such that

\[
\sum_{k\in S}J_k^{3/2}=\infty
\]

and

\[
\boxed{
\mathfrak R_k
\gtrsim
J_k^{1/2}
\qquad(k\in S).
}
\]

Then

\[
\sum_{k\in S}J_k\mathfrak R_k
\gtrsim
\sum_{k\in S}J_k^{3/2}
=\infty.
\]

By contrast, M5-200 produces only one fixed `k_0` after finite pigeonhole.

A single term

\[
J_{k_0}\mathfrak R_{k_0}>0
\]

is perfectly compatible with a finite sum.

Therefore

\[
\boxed{
\mathfrak R_{k_0}>0
\not\Longrightarrow
\text{cubic-tail energy contradiction}.
}
\]

---

## 5. Physical dissipation scaling of one natural-scale return event

Suppose, optimistically, that one contact event persists for a natural ancestor parabolic time

\[
\tau_n
\asymp
\frac{r_n^2}{\nu}.
\]

The contact gradient-energy density from Section 2 is of order

\[
\int|\nabla u|^2dx
\gtrsim
\frac{\nu^2}{r_n}.
\]

The physical viscous energy cost of the event is therefore

\[
\begin{aligned}
\mathcal E_n
&:=
\nu
\int_{I_n}\int|\nabla u|^2dxdt\\
&\gtrsim
\nu
\frac{\nu^2}{r_n}
\frac{r_n^2}{\nu}.
\end{aligned}
\]

Hence

\[
\boxed{
\mathcal E_n
\gtrsim
c\nu^2r_n.
}
\]

The important factor is the remaining length `r_n`.

---

## 6. Fixed-lag repeated events are geometrically summable in physical energy

For first-hitting levels,

\[
r_n=r_0q^{-n/2}.
\]

Therefore

\[
\sum_{n\ge n_0}r_n
<\infty.
\]

Consequently even if every sufficiently late generation carries one natural-time fixed-lag contact event with energy cost comparable to `nu^2 r_n`, the total lower-bound series is only

\[
\boxed{
\sum_n\mathcal E_n
\gtrsim
c\nu^2\sum_nr_n
<\infty.
}
\]

A finite lower bound does not contradict the finite kinetic-energy dissipation budget.

Thus repeated natural-scale material return is **energy-summable** at fixed generation age.

This is the physical reason that a recurrent core can coexist with a passive critical genealogy tail without immediate energy contradiction.

---

## 7. Shorter residence is even less coercive

If the return persists only for a fraction of the natural ancestor time, the energy cost is smaller.

If it persists only through the current-stage remaining time, the existing ancestor-radius audit gives the additional remote-age loss

\[
q^{-k_0}.
\]

At fixed `k_0` this is only a constant factor, but it does not change geometric summability in `n`.

Therefore no residence-time refinement at one fixed lag can turn the series

\[
\sum_nr_n
\]

into a divergent physical energy charge.

---

## 8. Fixed-lag contact also does not force DSS

Another tempting shortcut is

\[
\text{same material lineage returns at fixed lag}
\Longrightarrow
\text{DSS/self-similar recurrence}.
\]

This is not valid.

Material contact certifies overlap of one coherent packet with its ancestor descendant. It does not imply equality of the full velocity/vorticity spacetime block, pressure field, tail, center gauge, or all normalized descriptors.

Hence

\[
\boxed{
\text{fixed-lag material return}
\not\Longrightarrow
\text{DSS}.
}
\]

The similarity recurrence/phase-locking criteria from M5-194M/N remain necessary.

---

## 9. Correct destination of the contact branch

The fixed-lag material-contact branch is exactly compatible with the already isolated endpoint

\[
\boxed{
\text{precompact/recurrent active core}
+
\text{passive critical }1/r\text{ tail}.
}
\]

The active material packet may recycle through a bounded similarity region while the historical critical tail stores old-scale information with summable physical return weight.

Therefore contact is not a new branch to close by ordinary energy summation.

It rejoins the dynamic similarity-rigidity / backward-uniqueness frontier.

---

## 10. What M5-200 still accomplished

This firewall does not undo the previous reduction.

M5-199/200 removed the broad-coherent-core ambiguity by showing:

- arbitrary remote plateau age is impossible on the quiet corridor;
- recurrent plateau reduces to finitely many lags;
- each fixed lag is contact, replacement, or exposure.

M5-201 now identifies the exact fate of the contact descendant:

\[
\boxed{
\text{contact}
\to
\text{compact recurrent material core endpoint},
}
\]

not a spurious energy contradiction.

Replacement and exposure remain separately costed/routed.

---

## 11. Updated terminal frontier

After M5-197--201, the broad-enstrophy side reduces to

\[
\boxed{
\begin{aligned}
\text{derivative shell}
&\to
\text{finite Betchov frequency window},\\
\text{plateau replacement}
&\to
\text{finite-memory positive-frequency exits},\\
\text{plateau exposure}
&\to
H/T/\text{derivative costs},\\
\text{plateau contact}
&\to
\text{compact recurrent core + passive critical tail},\\
\text{nonrecurrent remote mass}
&\to
\text{escaping critical tail}.
\end{aligned}
}
\]

The genuinely hard endpoint is therefore again concentrated in **critical-tail-compatible recurrent dynamics**, not broad-core topology.

---

## 12. DSD verdict

### PROVED / AUDITED

- fixed-lag contact supplies a scale-critical instantaneous gradient-energy witness;
- under return-ledger hypotheses it gives positive return weight for that fixed label;
- one fixed positive return label does not close the cubic-divergent tail;
- natural-time physical energy cost of a fixed-lag event is proportional to the shrinking radius `r_n`;
- repeated fixed-lag event costs are geometrically summable;
- fixed-lag material recurrence does not imply DSS block recurrence;
- the correct endpoint is compact recurrent core plus passive critical tail.

### OPEN

- rigidity of that compact recurrent critical-tail endpoint;
- aperiodic/periodic similarity dynamics beyond known Liouville subcases;
- generic critical-drift backward uniqueness;
- derivative frequency-window constants;
- export/escaping critical tail;
- global regularity.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]

---

## 13. Next target

The highest-value next target returns to the dynamic endpoint already isolated in M5-194E--G:

\[
\partial_sV
+
\mathcal L_{Leray}V
+
(V\cdot\nabla)V
+
\nabla Q=0
\]

with a critical `1/r` tail whose generic first-order drift is not small.

The scalar Carleman route has already been firewalled.

The next nonredundant calculation should therefore test a **matrix/skew-dissipative symmetrizer** for the log-cylinder critical drift, using

\[
\Phi_r-\partial_y\Phi_r+\operatorname{div}_{S^2}\Phi_\tau=0
\]

and separating the divergence-free tangential skew part from the radial compressive part.

This is now more central than further material-return counting.