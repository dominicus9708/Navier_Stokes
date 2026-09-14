# DSD M19-259 — Comparable dyadic scales automatically bound record reuse and reduce coverage to log-scale density plus spacetime incidence

Date: 2026-09-15  
Status: **VALID COMBINATORIAL REDUCTION + NO-GO FOR SPARSE RECORD SEQUENCES / COVERAGE STILL OPEN**  
Parent: M19-258

## 0. Goal

M19-257 required comparable-scale assignment and bounded reuse from physical dyadic GMS shells to M17 records. This module asks whether bounded reuse is genuinely independent once scale comparability is imposed.

For dyadic physical scales it is not. Scale comparability already bounds the number of shell indices to which one fixed record can belong.

The remaining coverage problem separates into:

1. logarithmic scale density of the record radii;
2. space-time incidence/center coherence of the corresponding record windows;
3. representation/genealogy/root eligibility from M19-258.

Global regularity remains unproved.

---

## 1. Dyadic physical scales

Let

\[
r_j=2^{-j}r_0,
\qquad j\ge J_0.
\]

For a record radius \(R_m\), define its logarithmic scale coordinate

\[
a_m:=-\log_2(R_m/r_0).
\]

The M19-257 scale-comparability condition

\[
\Lambda^{-1}r_j\le R_m\le\Lambda r_j
\]

is equivalent to

\[
\boxed{
|a_m-j|\le L_\Lambda,
\qquad L_\Lambda:=\log_2\Lambda.
}
\]

---

## 2. Comparable scale automatically gives bounded shell-index reuse

Fix one record \(m\). If it is assigned only to physical shell indices satisfying the comparability condition, then every admissible \(j\) lies in

\[
[a_m-L_\Lambda,a_m+L_\Lambda].
\]

Hence the number of integer dyadic shell indices available to that record obeys

\[
\boxed{
\#\{j:\Lambda^{-1}r_j\le R_m\le\Lambda r_j\}
\le 2\lceil L_\Lambda\rceil+1.
}
\]

Therefore the M19-257 bounded-reuse constant can be taken as

\[
\boxed{
N_\Lambda=2\lceil\log_2\Lambda\rceil+1
}
\]

provided the shell-to-record map never assigns a record outside its comparable-scale window.

Thus

\[
\boxed{
\text{uniform scale comparability}
\Longrightarrow
\text{uniform shell-index reuse bound}.
}
\]

This removes bounded reuse as an independent combinatorial theorem.

---

## 3. Scale coverage is relative density on logarithmic scale

Every sufficiently small dyadic physical scale is comparable to some record if and only if there exists \(L<\infty\) such that

\[
\boxed{
\forall j\ge J_0\quad\exists m:\ |a_m-j|\le L.
}
\]

In other words, the record scale set

\[
\mathcal A:=\{a_m\}
\]

must be **relatively dense** in the large positive logarithmic half-line.

If the record radii are ordered decreasingly, this is implied by a uniform logarithmic gap bound

\[
\boxed{
\sup_m\log_2\frac{R_m}{R_{m+1}}<\infty.
}
\]

Conversely, an unbounded logarithmic gap sequence creates physical dyadic scales with no uniformly comparable record.

Define the explicit scale-gap exit

\[
\boxed{
\mathcal E_{scale-gap}:
\sup_m\log_2\frac{R_m}{R_{m+1}}=\infty
}
\]

for an ordered cofinal record sequence.

---

## 4. NO-GO: cofinality alone does not give scale coverage

The facts

\[
R_m\downarrow0
\]

and bounded overlap of the corresponding record windows do not imply relative density of \(\{a_m\}\).

A simple abstract counterexample is

\[
R_m=2^{-2^m}r_0.
\]

Then

\[
a_m=2^m,
\qquad
a_{m+1}-a_m=2^m\to\infty.
\]

The record sequence tends to zero, but no fixed \(\Lambda\) makes every dyadic physical scale comparable to a record.

Therefore

\[
\boxed{
R_m\to0
+\text{record-window bounded overlap}
\not\Rightarrow
\mathcal T_{GMS}^{scale-density}.
}
\]

This is a logical NO-GO, not a claim that the actual M17 record sequence is sparse. The actual M17 construction must be audited for a bounded logarithmic gap theorem.

---

## 5. Scale density is necessary but not sufficient for physical coverage

Even if every dyadic radius has a comparable record radius, the corresponding record window may occur at the wrong place or time.

Thus decompose

\[
\boxed{
\mathcal T_{GMS}^{cover}
=
\mathcal T_{GMS}^{scale-density}
+\mathcal T_{GMS}^{incidence}.
}
\]

Here

\[
\mathcal T_{GMS}^{scale-density}:
\quad
\forall j\gg1\ \exists m\text{ with }R_m\asymp r_j,
\]

and

\[
\mathcal T_{GMS}^{incidence}:
\quad
\text{the comparable record window actually covers the required physical space-time shell in one fixed Galilean frame.}
\]

The incidence gate includes the M19-256 tracking quantity

\[
\Theta_m(V)=r_m^{-1}
\sup_{t\in I_m}|X_m(t)-x_0-V(t-t_0)|
\]

and the required time-window comparison between \(I_m\) and the physical parabolic interval of size \(r_j^2\).

---

## 6. Updated active transfer complex

Under the M19-258 same-field whole-space bridge, the current entered-branch complex becomes

\[
\boxed{
\mathcal T_{GMS}^{scale-density}
+\mathcal T_{GMS}^{incidence}
+\mathcal T_{GMS}^{repr}
+\mathcal T_{GMS}^{root}.
}
\]

Bounded shell-index reuse is automatic from the first condition once a uniform comparability constant is fixed.

The first two conditions jointly replace the broader \(\mathcal T_{GMS}^{cover}\).

---

## 7. Permanent firewalls

\[
\boxed{
\text{record scales cofinal at }0
\not\Rightarrow
\text{bounded logarithmic scale gaps}.
}
\]

\[
\boxed{
\text{bounded record-window overlap}
\not\Rightarrow
\text{log-scale density}.
}
\]

\[
\boxed{
\text{log-scale density}
\not\Rightarrow
\text{space-time incidence around the candidate singular point}.
}
\]

\[
\boxed{
\text{scale comparability}
\Longrightarrow
\text{bounded dyadic shell-index reuse},
\]

but this does not control multiple distinct records at one shell; that multiplicity must be handled by the existing M17 record ledger/coverage construction.

---

## 8. Immediate next audit

Inspect the actual M17 record selection rule and determine whether it proves any of the following:

\[
\sup_m\log(R_m/R_{m+1})<\infty,
\]

or an equivalent relative-density statement for record scales.

If no such theorem exists, the canonical survivor is not an untyped transfer failure but the explicit

\[
\boxed{\mathcal E_{scale-gap}}
\]

unless another record-selection/first-hitting argument fills the skipped physical scales.

If scale density is available, the next gate is \(\mathcal T_{GMS}^{incidence}\): space-time/center coverage in one fixed Galilean frame.

Global regularity remains unproved.
