# DSD M19-138 — Antipodal oddness propagates through the full odd-velocity hierarchy and kills every odd pressure resonance

Date: 2026-09-12

Status: **ACTIVE M19 CALCULATION / M19-137 IS EXTENDED BY INDUCTION TO ALL ASYMPTOTIC ORDERS / IF THE LEADING CRITICAL DATUM IS ANTIPODALLY ODD THEN EVERY VELOCITY CORRECTION B_n IS ODD, EVERY QUADRATIC PRESSURE STRESS AND SOURCE IS EVEN, WHILE EVERY ZERO-q PRESSURE RESONANCE HAS ODD DEGREE l=2n+1 / THE ENTIRE PRESSURE NO-LOG SOLVABILITY LADDER IS AUTOMATIC ON THIS PARITY CLASS / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Hierarchy

Use the asymptotic expansion

\[
U\sim\sum_{n\ge0}r^{-(2n+1)}B_n(q,\omega),
\qquad B_0=A,
\]

and

\[
P\sim\sum_{n\ge0}r^{-(2n+2)}\Pi_n(q,\omega).
\]

Assume

\[
\boxed{B_0(q,-\omega)=-B_0(q,\omega).}
\]

We show inductively that

\[
\boxed{B_n(q,-\omega)=-B_n(q,\omega)}
\]

for every `n` for which the log-free correction hierarchy is defined.

---

## 2. Inductive parity step

Assume

\[
B_0,\ldots,B_{n-1}
\]

are all odd.

The order-n velocity forcing consists schematically of:

1. viscous terms `Delta B_{n-1}`;
2. quadratic convective terms `B_a dot nabla B_b` with `a+b=n-1`;
3. the gradient of the order-(n-1) pressure correction;
4. parity-preserving linear angular/log-radial terms already incorporated in the invertible correction operator.

For an odd vector field `B`:

\[
\nabla B
\quad\text{is even},
\qquad
\Delta B
\quad\text{is odd}.
\]

Therefore

\[
(B_a\cdot\nabla)B_b
\]

is odd whenever `B_a,B_b` are odd.

---

## 3. Pressure parity at the previous level

The order-(n-1) pressure stress is

\[
T^{(n-1)}
=
\sum_{a+b=n-1}B_a\otimes B_b.
\]

Odd times odd is even, so

\[
T^{(n-1)}(-\omega)=T^{(n-1)}(\omega).
\]

Two derivatives preserve parity overall, hence the pressure source is even.
The recurrent/decaying pressure solution may therefore be chosen even modulo the already-separated homogeneous gauge sector.
Thus

\[
\nabla\Pi_{n-1}
\]

is odd.

Every term in the order-n velocity forcing is therefore odd.

Because the order-n velocity correction operator preserves antipodal parity and is invertible on the retained nonresonant velocity sector,

\[
\boxed{B_n\text{ is odd}.}
\]

This closes the induction.

---

## 4. Every pressure source is even

Since every `B_n` is odd,

\[
T^{(n)}
=
\sum_{a+b=n}B_a\otimes B_b
\]

is even for every `n`.
Therefore

\[
\boxed{F_n=\partial_i\partial_jT^{(n)}_{ij}}
\]

is also even for every `n`.

---

## 5. Every pressure resonance has odd spherical degree

M19-136 gives the unique zero-q resonance at pressure order `n`:

\[
\boxed{l_{res}=2n+1.}
\]

This degree is odd for every `n`.
Hence every resonant spherical harmonic satisfies

\[
Y_{2n+1}(-\omega)=-Y_{2n+1}(\omega).
\]

Pairing an even pressure source with an odd harmonic gives zero:

\[
\boxed{
\Pi_{2n+1}\mathbb M_qF_n=0
\qquad\text{for every }n\ge0.
}
\]

Thus all resonant no-log conditions are automatic.

---

## 6. Consequence

For antipodally odd critical data,

\[
\boxed{
\text{the complete pressure-resonance ladder supplies no new solvability obstruction}.
}
\]

This includes odd-parity RSS/RDSS tails because rigid rotation preserves antipodal parity.

Therefore any universal critical-tail closure must use something beyond the pressure resonance hierarchy alone.

---

## 7. Mixed-parity branch remains different

The result does not eliminate the pressure hierarchy on mixed-parity data.
If the leading datum contains even and odd components simultaneously, later corrections generally mix parities and the odd resonant pressure moments need not vanish.

Thus the hierarchy still provides potentially useful algebraic constraints on the mixed-parity finite low-mode hard core isolated by M19-129.

The pressure route is therefore reclassified as

\[
\boxed{
\text{mixed-parity algebraic filter},
\quad\text{not a universal Liouville mechanism}.
}
\]

---

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
