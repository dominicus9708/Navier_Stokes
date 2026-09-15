# DSD M19-262 — Epsilon-smallness route is valid, but current discounted ledgers do not force vanishing critical charge

Date: 2026-09-15  
Canonical ID: **M19-262**  
Status: **EXTERNAL-THEOREM AUDIT / CRITICAL-SMALLNESS NO-AUTOMATIC-CLOSURE / STRONG-L3 VS WEAK-L3 FIREWALL / NEW VANISHING-CHARGE TARGET**

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Purpose

M19-261 isolated three possible ways around the missing physical base-scale gain:

1. direct original-variable derivative budget;
2. scale-invariant epsilon-smallness;
3. CE-H rigidity.

This module audits route 2 against standard external regularity criteria and the already-certified DSD resource economics.

---

## 2. External regularity facts that may legitimately be imported

### 2.1 CKN-type one-point criterion

For suitable weak solutions there is a universal threshold such that sufficiently small scale-invariant local dissipation, schematically

\[
\limsup_{r\downarrow0}
\frac1r
\int_{Q_r(z_0)}|\nabla u|^2dxdt
<\varepsilon_{CKN},
\]

implies regularity at \(z_0\).

### 2.2 Gustafson--Kang--Tsai interior criteria

Known interior epsilon-regularity criteria also allow sufficiently small scale-invariant mixed norms of velocity, vorticity, or vorticity gradient in ranges including

\[
\frac3p+\frac2q\le2
\]

for velocity,

\[
\frac3p+\frac2q\le3
\]

for vorticity, and

\[
\frac3p+\frac2q\le4
\]

for \(\nabla\omega\), subject to the stated endpoint restrictions in the theorem.

Reference: Gustafson, Kang, Tsai, *Interior regularity criteria for suitable weak solutions of the Navier--Stokes equations*, Comm. Math. Phys. 273 (2007), DOI 10.1007/s00220-007-0214-6.

### 2.3 Strong L3 endpoint

Escauriaza--Seregin--Šverák prove smoothness under the classical endpoint strong-space condition commonly denoted \(L_{3,\infty}\), i.e. spatial strong \(L^3\) uniformly in time in their mixed-norm notation.

Reference: Escauriaza, Seregin, Šverák, *L3,infinity-solutions of the Navier--Stokes equations and backward uniqueness*, Russian Math. Surveys 58 (2003), DOI 10.1070/RM2003v058n02ABEH000609.

This must not be confused with the Lorentz spatial weak space

\[
L^{3,\infty}_x.
\]

The repository's historical `weak-L3` branch refers to the latter.

---

## 3. Strong-L3 / weak-L3 firewall

The statement

\[
u\in L_t^\infty L_x^3
\]

is a regularity endpoint.

The statement

\[
u(t)\in L_x^{3,\infty}
\]

with bounded Lorentz weak-L3 size is a different and weaker condition.

Therefore

\[
\boxed{
\text{bounded spatial weak-}L^3
\not\Rightarrow
\text{ESS strong-}L^3\text{ endpoint}.
}
\]

M19-198 already finds that finite-high weak-L3 can be carried persistently by a critical \(r^{-1}\) tail and does not by itself create a finite ancestral contradiction.

Thus the external strong-L3 theorem does not automatically close the current R-critical weak-L3/tail branch.

---

## 4. Why the existing discounted ledgers do not force epsilon-smallness

A typical current ancestry ledger has the form

\[
\sum_mK_m^{-a}q_m<\infty,
\qquad K_m\asymp q^{m/2},
\qquad a>0,
\]

where \(q_m\) is a normalized scale-invariant or higher-derivative record charge.

Because

\[
\sum_mK_m^{-a}<\infty,
\]

this is fully compatible with

\[
q_m\equiv q_*>0.
\]

In particular:

- M17-307 allows order-one normalized palinstrophy charge with \(K^{-1}\) ancestry discount;
- M17-405 allows order-one normalized raw-H2 charge with \(K^{-3}\) ancestry discount.

Hence

\[
\boxed{
\text{finite discounted ancestry ledger}
\not\Rightarrow
q_m\to0.
}
\]

Smallness-based regularity requires a vanishing or sub-threshold statement, not merely a discounted finite sum.

---

## 5. The natural CKN dissipation quantity has the same critical-economics problem

Define

\[
\mathcal E(r;z_0)
:=
\frac1r
\int_{Q_r(z_0)}|\nabla u|^2dxdt.
\]

Since \(|\nabla u|^2\) is equivalent at the whole-space incompressible level to vorticity enstrophy up to the usual identities, \(\mathcal E\) is scale invariant.

Finite global energy dissipation only gives

\[
\int|\nabla u|^2dxdt<\infty.
\]

An order-one value

\[
\mathcal E(r_j)\asymp1
\]

at geometric radii costs physical dissipation of order \(r_j\), and

\[
\sum_jr_j<\infty.
\]

Thus standard energy can pay a persistent Type-I critical dissipation floor at every geometric scale.

This is exactly why boundedness without smallness is not enough.

---

## 6. First-hitting structure does not currently force normalized vanishing

The marked first-hitting normalization has

\[
|\Omega_j(0,0)|=1.
\]

The retained Taylor/material carrier structure supplies nontrivial normalized activity rather than an evident mechanism forcing all critical quantities to zero.

M5-477 further shows Type-I enstrophy saturation along the backward record sequence:

\[
\|\Omega(\tau_m)\|_2^2
\asymp
(-\tau_m)^{-1/2}.
\]

When each record is viewed in its own natural scale, this is compatible with order-one normalized critical activity.

Therefore no existing first-hitting theorem currently yields

\[
\liminf_{j\to\infty}\mathcal E(r_j)=0.
\]

---

## 7. Current field-theory context confirms the exact missing step

Modern quantitative partial-regularity work continues to use the CKN smallness threshold. It is explicitly emphasized in the literature that ruling out a singularity from a merely bounded Type-I scale-invariant dissipation quantity without the required smallness remains a major open difficulty.

Thus the DSD audit should not relabel

\[
\sup_{r\ll1}\mathcal E(r)<\infty
\]

as a known regularity condition.

The missing mathematical content is precisely a mechanism that improves bounded critical activity to sub-threshold activity on at least one admissible scale.

---

## 8. New target: vanishing critical charge

Define a generic smallness target

\[
\boxed{
\mathcal T_{\varepsilon}^{crit}:
\exists r_n\downarrow0
\text{ such that }
\mathcal Q_{crit}(r_n)<\varepsilon_*
}
\]

for one rigorously matched epsilon-regularity quantity \(\mathcal Q_{crit}\).

Possible choices include:

1. CKN local dissipation
   \[
   \mathcal Q_{crit}(r)
   =r^{-1}\int_{Q_r}|\nabla u|^2;
   \]
2. one of the Gustafson--Kang--Tsai scale-invariant velocity/vorticity mixed norms;
3. the already-defined Galilean \(C_V(r)+D_V(r)\) if a direct upper-smallness mechanism is found.

The criterion used must match the theorem exactly; different critical quantities cannot be interchanged without a proved comparison.

---

## 9. Dichotomy after the epsilon audit

The smallness route now has the exact split

\[
\boxed{
\mathcal T_{\varepsilon}^{crit}
\lor
\mathcal E_{crit-floor}.
}
\]

Here

\[
\mathcal E_{crit-floor}
:
\liminf_{r\downarrow0}\mathcal Q_{crit}(r)\ge\varepsilon_*>0
\]

is not itself a contradiction.

It is a persistent scale-critical payer corridor whose physical cost can remain summable under geometric shrinking.

Hence failure of epsilon-smallness must be routed into the existing R-critical / Type-I / recurrent hard-core analysis, not declared impossible.

---

## 10. Consequence for M19-261's three candidate routes

The audit gives:

- **direct physical-budget route:** still OPEN;
- **epsilon-smallness route:** mathematically valid, but no existing discounted ledger forces the required smallness;
- **CE-H rigidity route:** remains independent and may still produce either a direct contradiction or a new decay mechanism.

Accordingly route 2 is not closed, but it is now reduced to one explicit theorem target:

\[
\boxed{
\text{derive a genuine sub-threshold scale-invariant charge from the retained DSD corridor.}
}
\]

---

## 11. Permanent firewalls after M19-262

\[
\boxed{
L_t^\infty L_x^3
\neq
L_t^\infty L_x^{3,\infty}.
}
\]

\[
\boxed{
\text{bounded critical norm}
\neq
\text{epsilon-small critical norm}.
}
\]

\[
\boxed{
\sum K_m^{-a}q_m<\infty
\not\Rightarrow
q_m\to0
\quad(a>0,\ \sum K_m^{-a}<\infty).
}
\]

\[
\boxed{
\text{Type-I boundedness without smallness is not a known closure theorem.}
}
\]

\[
\boxed{
\text{failure of epsilon-smallness}
\neq
\text{contradiction};
\text{ it is a critical-floor survivor.}
}
\]

---

## 12. Immediate next target

The next useful calculation is to test whether the **CE-H exact structure can improve a critical quantity from bounded to vanishing/sub-threshold** without requiring the unavailable physical H3 budget.

In particular, combine

\[
\Delta W=\kappa W,
\qquad
\Sigma W=\sigma W,
\qquad
D_\xi\kappa=0,
\]

with the first-hitting normalization and finite-enstrophy/decay class to ask whether any persistent nonzero critical floor forces one of:

1. nonintegrable strong \(L^3\) mass;
2. forbidden low-frequency/tail behavior;
3. a sign/geometry payer already ruled out in late M17;
4. a direct Liouville-type rigidity contradiction.

Global 3D Navier--Stokes regularity remains unproved.
