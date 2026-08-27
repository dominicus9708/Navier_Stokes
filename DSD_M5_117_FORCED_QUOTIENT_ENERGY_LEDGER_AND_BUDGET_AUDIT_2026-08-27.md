# DSD M5-117 — Forced Quotient Energy Ledger and Budget Audit

Date: 2026-08-27

Status: **W1-CONDITIONAL EXACT FINITE-ENERGY QUOTIENT LEDGER / CANONICAL TAIL SUBTRACTION PRODUCES AN L2 INTERSECTION L3 QUOTIENT WITH A STANDARD RELATIVE ENERGY BALANCE / THE PHYSICAL ENERGY CARRIES THE EXPLICIT e^{-s/2} LERAY WEIGHT, SO O(1) NORMALIZED RECURRENCE IS SUMMABLE AND DOES NOT CONTRADICT FINITE ENERGY / THE FINITE-ENERGY-QUOTIENT SHORTCUT IS RED / GLOBAL REGULARITY UNPROVED.**

---

## 1. Canonical quotient

Fix one canonical tail state `T=T_V` and one fixed divergence-free cutoff/Bogovskii realization `B=B_V` as in the general tail theorem.

Write

\[
\boxed{Q:=V-B.}
\]

Then

\[
Q\in L^2(\mathbb R^3)\cap L^3(\mathbb R^3),
\qquad
\nabla\cdot Q=0.
\]

The quotient equation has the projected form

\[
\boxed{
\mathcal LQ
+\mathbb P\nabla\cdot
\left(
Q\otimes Q+Q\otimes B+B\otimes Q
\right)
=\mathcal F_B,
}
\]

where

\[
\mathcal L
=\partial_s-\nu\Delta+\frac12+\frac12Y\cdot\nabla.
\]

The forcing `F_B` is completely determined by the chosen canonical tail and its cutoff; it is not an external physical force added to the original Navier-Stokes problem.

---

## 2. Exact L2 quotient ledger

Pair the equation with `Q`.

Because `Q` and `B` are divergence-free,

\[
\int Q\cdot(Q\cdot\nabla Q)=0,
\]

and

\[
\int Q\cdot(B\cdot\nabla Q)=0.
\]

The remaining cross-advection is

\[
\int Q\cdot(Q\cdot\nabla B)
=\int Q^T S_B Q,
\]

where

\[
S_B=\frac12(\nabla B+\nabla B^T).
\]

The Leray linear terms give the already-audited global L2 coefficient `-1/4`.

Hence

\[
\boxed{
\frac12\frac d{ds}\|Q\|_2^2
+\nu\|\nabla Q\|_2^2
-\frac14\|Q\|_2^2
+\int Q^T S_BQ
=
\langle\mathcal F_B,Q\rangle.
}
\]

Every term is finite in the quotient class.

---

## 3. Physical-energy renormalization

Define

\[
\boxed{
\mathscr E_Q(s)
:=e^{-s/2}\|Q(s)\|_2^2.
}
\]

This is exactly the physical L2 scaling of the quotient:

\[
\|q_{phys}(t)\|_2^2
=e^{-s/2}\|Q(s)\|_2^2.
\]

Using

\[
\frac d{ds}\left(e^{-s/2}\|Q\|_2^2\right)
=e^{-s/2}
\left(
\frac d{ds}\|Q\|_2^2-rac12\|Q\|_2^2
\right),
\]

the exact ledger becomes

\[
\boxed{
\frac12\mathscr E_Q'(s)
+e^{-s/2}
\left[
\nu\|\nabla Q\|_2^2
+\int Q^TS_BQ
-\langle\mathcal F_B,Q\rangle
\right]
=0.
}
\]

The troublesome `-1/4 ||Q||_2^2` is not a physical energy source; it is exactly removed by the physical scaling factor.

---

## 4. What recurrence costs in this ledger

On the compact W1 recurrent class, for one fixed cutoff construction the quotient quantities remain bounded on each normalized return:

\[
\|Q\|_2,
\quad
\|\nabla Q\|_2,
\quad
\left|\int Q^TS_BQ\right|,
\quad
|\langle\mathcal F_B,Q\rangle|
=O(1)
\]

at the normalized level allowed by the retained quotient estimates.

But every term in the physical ledger is multiplied by

\[
\boxed{e^{-s/2}}.
\]

For a syndetic recurrent sequence

\[
s_n\to\infty
\]

with gaps bounded below after taking a separated subfamily,

\[
\sum_n e^{-s_n/2}<\infty.
\]

Thus infinitely many order-one normalized quotient events can have finite total physical-energy weight.

---

## 5. No new critical budget from the finite-energy quotient

The canonical subtraction changes the function class:

\[
V\notin L^2
\quad\leadsto\quad
Q\in L^2.
\]

But it does **not** change the critical scaling of the terminal recurrence.

The physical energy of each later normalized copy shrinks as

\[
e^{-s/2}.
\]

Therefore

\[
\boxed{
Q\in L^2
\not\Rightarrow
\text{a finite normalized critical recurrence budget}.
}
\]

This is the quotient version of the M5-49/M5-106 budget firewall.

---

## 6. Tail forcing is not an independent payer

The term

\[
\mathcal F_B
\]

is produced deterministically by subtracting the passive tail from the original unforced W1 solution.

Its work

\[
\langle\mathcal F_B,Q\rangle
\]

therefore records exchange between the chosen tail background and the finite-energy quotient.

It must not be added to the original pressure anomaly or cubic residue as a separate external resource.

Doing so would double-count the same state decomposition.

---

## 7. DSD four-chain audit

### Formation

The tail is formed before the quotient, and the quotient before its energy ledger.

### Axis

Normalized Leray energy and physical energy are distinct scale channels linked by the explicit factor `e^{-s/2}`.

### Static aggregation

Tail forcing work is internal exchange, not an additional source.

### Dynamics

Recurrence is inserted only after the exact quotient ledger is derived.

### RED firewall

The following shortcut is forbidden:

\[
\boxed{
Q\in L^2
+
\text{infinitely many recurrent Q-events}
\Rightarrow
\text{infinite physical energy/dissipation}.
}
\]

The `e^{-s/2}` scaling defeats that sum.

---

## 8. Consequence

Canonical tail subtraction remains valuable because it isolates a strong finite-energy core variable.

But its usefulness must come from **uniqueness, spectral, or structural information about the forced quotient equation**, not from a naive finite-energy accumulation contradiction.

Thus the live quotient targets are now:

1. same-tail critical backward uniqueness (M5-115--116);
2. structural constraints on complete recurrent `L2 cap L3` quotient dynamics under the canonical tail forcing;
3. or a genuinely scale-critical finite estimate not supplied by ordinary quotient energy.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
