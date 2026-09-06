# DSD Deep Audit — Graah Thick / Tube-like / Fragmented Trichotomy

Date: 2026-09-06
Source: Hannes Graah, *Global Regularity for 3D Navier-Stokes*, Zenodo 18132364 / 18132365 (2026-01-02).

## Public proof architecture

The public description states:

1. assume a first singular time \(T<\infty\);
2. on every parabolic scale approaching \(T\), vorticity falls into a complete geometric trichotomy: thick / tube-like / fragmented;
3. in every regime there is a **scale-invariant lower bound on dissipation** on a subinterval of comparable length;
4. a Calderon-Zygmund packing produces infinitely many disjoint dissipation intervals accumulating at \(T\);
5. this contradicts the global energy inequality.

## Status

**OPEN_DEEP narrowed to a precise physical-quantum gap.**

If the manuscript's actual regime lemmas provide only the standard scale-invariant local dissipation lower bound, then the stated final packing contradiction is invalid. If they provide a stronger radius-independent lower bound in the *unnormalized globally budgeted physical dissipation*, that stronger theorem must be displayed and checked separately.

---

# Core audit

For 3D NSE the standard scale-invariant local dissipation functional is

\[
E(r)=\frac1r\int_{Q_r}|\nabla u|^2\,dx\,dt.
\]

Suppose a geometric regime gives

\[
E(r_n)\ge c_*>0
\]

on infinitely many pairwise disjoint parabolic time intervals with scales \(r_n\downarrow0\).

Then the corresponding **physical** dissipation payment is only

\[
\int_{Q_{r_n}}|\nabla u|^2\,dx\,dt
\ge c_*r_n.
\]

For a perfectly admissible dyadic scale sequence

\[
r_n=2^{-n},
\]

we have

\[
\sum_n c_*r_n<\infty.
\]

Therefore

\[
\boxed{
\text{infinitely many disjoint intervals}
+\text{scale-invariant lower bound}
\not\Rightarrow
\text{infinite total physical dissipation}.
}
\]

The global energy inequality is compatible with infinitely many such increasingly cheap events.

This is exactly the normalized-cost versus physical-budget firewall already encountered internally in M17-230, M17-235, M17-237 and M17-242.

---

# What would repair the argument

At least one of the following stronger exports is necessary:

### A. Radius-independent physical quantum

\[
\int_{I_n}\int_{\mathbb R^3}|\nabla u|^2\,dx\,dt\ge d_*>0
\]

for every selected interval.

Then infinitely many disjoint intervals do contradict finite energy.

### B. Non-summable scale payments

A lower bound

\[
D_n\ge c\,\psi(r_n)
\]

with

\[
\sum_n\psi(r_n)=\infty.
\]

### C. Positive-density-in-time payment

A mechanism showing that the union of payer intervals has enough physical-time measure and a lower dissipation density that makes the total integral diverge.

A bare statement that the local estimate is "scale invariant" is not enough.

---

# Secondary audit obligations

Even if the physical-quantum bridge is repaired, four earlier steps remain to be checked:

1. **trichotomy exhaustiveness** — every possible vorticity geometry must enter thick/tube/fragmented with no thin-interface or amplitude-degenerate escape;
2. **definite time fraction** — the selected geometry must persist on an interval comparable to the scale, not only at one time slice;
3. **non-overcounting** — dissipation charged to distinct geometric events must be physically disjoint or have uniformly bounded multiplicity;
4. **amplitude firewall** — geometric normalization cannot create an amplitude-independent physical payment.

---

# Survivor

The thick / tube-like / fragmented organization is still a potentially useful branch taxonomy. It is close in spirit to M17's packet/ribbon/thin/interface decomposition and should be retained as a comparison architecture.

The audit targets only the final conversion

\[
\text{scale-invariant local cost}
\to
\text{global finite-energy contradiction}.
\]

---

# M17 regression test

Any future M17 packing argument must write the actual globally budgeted quantity before summing:

\[
\boxed{
\text{normalized packet cost}\neq\text{physical dissipation quantum}.
}
\]

An infinite number of events is irrelevant unless their **unnormalized** payments form a divergent series.

GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.
