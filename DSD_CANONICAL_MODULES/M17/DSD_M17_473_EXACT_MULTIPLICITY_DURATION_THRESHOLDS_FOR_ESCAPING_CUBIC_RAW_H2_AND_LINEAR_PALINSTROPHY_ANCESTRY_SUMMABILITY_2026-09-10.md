# M17-473 — Exact multiplicity/duration thresholds for escaping cubic raw-H2 and linear palinstrophy ancestry summability

**Date:** 2026-09-10  
**Status:** ACTIVE THRESHOLD THEOREM / MULTIPLICITY-DURATION AUDIT

## 1. Scope

M17-472 showed that a fixed order-one normalized source-return payment at each geometric record scale is compatible with both certified ancestry ledgers:
\[
\sum_mR_m^{-3}H_m^{\rm norm}<\infty,
\qquad
\sum_mR_m^{-1}P_m^{\rm norm}<\infty.
\]

This module computes the exact arithmetic threshold that any multiplicity, duration, or allocation gain must cross before those ledgers can yield a contradiction.

It does not assert that such gains exist.

## 2. Abstract weighted-ledger criterion

Let \(R_m\to\infty\) be the certified record factors and let \(Q_m\ge0\) denote the total **non-reusable normalized charge** assigned to record \(m\).

For a resource with ancestry exponent \(a>0\), the parent ledger has the form
\[
\boxed{
\sum_mR_m^{-a}Q_m<\infty.
}
\]

Therefore a contradiction from lower bounds on \(Q_m\) requires
\[
\boxed{
\sum_mR_m^{-a}Q_m=\infty.
}
\]

This weighted divergence condition is the exact criterion. Any simpler growth statement is only sufficient or insufficient relative to it.

For the two current ledgers:
\[
\boxed{a=3\quad\text{for raw-H2},}
\]
\[
\boxed{a=1\quad\text{for palinstrophy}.}
\]

## 3. Geometric record scales

Assume the usual geometric record growth
\[
R_m\asymp R_0\Lambda^m,
\qquad
\Lambda>1.
\]

If
\[
Q_m\asymp R_m^\beta,
\]
then
\[
R_m^{-a}Q_m
\asymp
R_m^{\beta-a}
\asymp
\Lambda^{(\beta-a)m}.
\]
Hence:

- if \(\beta<a\), the weighted series converges geometrically;
- if \(\beta>a\), its terms grow and it diverges;
- if \(\beta=a\), its terms are order one and it diverges.

Thus the power threshold is exactly
\[
\boxed{\beta=a.}
\]

Consequently:
\[
\boxed{
Q_m\sim R_m^3
\quad\text{is the raw-H2 power threshold},
}
\]
\[
\boxed{
Q_m\sim R_m
\quad\text{is the palinstrophy power threshold}.
}
\]

## 4. Borderline logarithmic corrections

At the exact power threshold let
\[
Q_m=R_m^aL_m.
\]
Then
\[
R_m^{-a}Q_m=L_m.
\]
Therefore the question reduces to the ordinary series
\[
\sum_mL_m.
\]

Examples:
\[
Q_m\gtrsim\frac{R_m^a}{m}
\quad\Longrightarrow\quad
\sum_mR_m^{-a}Q_m
\gtrsim\sum_m\frac1m=\infty,
\]
whereas
\[
Q_m\lesssim\frac{R_m^a}{m^{1+\varepsilon}}
\]
is compatible with convergence.

Thus “almost \(R_m^a\)” must be interpreted with the exact residual summability factor; there is no unique pointwise threshold finer than the weighted-series condition.

## 5. Event multiplicity formulation

Suppose record \(m\) contains \(N_m\) pairwise non-reusable events, each paying at least \(q_*>0\) in normalized resource. Then
\[
Q_m\ge q_*N_m.
\]

A contradiction requires
\[
\boxed{
\sum_mR_m^{-a}N_m=\infty.
}
\]

Therefore:

### raw-H2
\[
\boxed{
\sum_mR_m^{-3}N_m=\infty.
}
\]
A pure power multiplicity must reach \(N_m\sim R_m^3\) at threshold.

### palinstrophy
\[
\boxed{
\sum_mR_m^{-1}N_m=\infty.
}
\]
A pure power multiplicity must reach \(N_m\sim R_m\) at threshold.

Crucially, the events must be certified as non-reusable in the relevant parent ledger. Merely counting overlapping descendants does not produce \(N_m\) in this theorem.

## 6. Residence-duration formulation

Suppose a normalized event pays resource at a rate bounded below by \(q_*>0\) per unit normalized own-scale time and persists for total non-reusable residence \(T_m\). Then
\[
Q_m\ge q_*T_m.
\]

The exact divergence conditions become
\[
\boxed{
\sum_mR_m^{-3}T_m=\infty
\quad\text{for raw-H2},
}
\]
\[
\boxed{
\sum_mR_m^{-1}T_m=\infty
\quad\text{for palinstrophy}.
}
\]

Thus a bounded or slowly growing own-scale residence is insufficient on geometric records.

## 7. Logarithmic gains are insufficient

For every fixed \(k\ge0\), geometric \(R_m\asymp\Lambda^m\) implies
\[
\sum_mR_m^{-a}(\log R_m)^k
\asymp
\sum_m\Lambda^{-am}m^k
<\infty.
\]
More generally every polynomial in \(m\) is dominated by the geometric ancestry weight.

Therefore
\[
\boxed{
Q_m=O((\log R_m)^k)
\quad\text{cannot escape either ancestry firewall.}
}

This applies equally to logarithmic multiplicity and logarithmic normalized residence, provided they enter only linearly as resource charge.

## 8. Audit of the earlier logarithmic residence mechanism

M17-379 established, in its own dyadic evacuation setting, a logarithmic lower bound of the form
\[
\sum_j\tau_j^{\rm own}\gtrsim\log(1/r).
\]

M17-473 does not invalidate that result. It classifies its strength relative to the current ancestry problem:

- a merely logarithmic residence gain is too weak to defeat \(R^{-3}\) raw-H2 summability;
- it is also too weak to defeat \(R^{-1}\) palinstrophy summability on geometric record scales.

Hence the M17-379 logarithmic effect can contribute to local structure but **cannot by itself close the ancestral contradiction**.

## 9. Mixed multiplicity-duration gains

If record \(m\) has \(N_m\) non-reusable events with total average payable residence \(T_m^{\rm event}\), then schematically
\[
Q_m\gtrsim N_mT_m^{\rm event}q_*.
\]
The relevant condition is still only
\[
\boxed{
\sum_mR_m^{-a}
N_mT_m^{\rm event}=\infty.
}
\]

Neither factor separately must reach the full power threshold if their product does.

This is the correct target for future packing/allocation arguments.

## 10. Allocation firewall

A large combinatorial count does not automatically imply a large \(Q_m\). To enter the threshold theorem, one must prove that the counted events consume disjoint or quantitatively bounded-overlap pieces of the certified parent resource.

Thus the logical order is
\[
\boxed{
\text{count/residence}
+\text{non-reuse allocation theorem}
\Longrightarrow Q_m
\Longrightarrow
\text{weighted-series test}.
}
\]

Skipping the allocation step is forbidden.

## 11. Consequence for the current proof strategy

M17-472's generic statement “multiplicity or duration gain is needed” can now be sharpened:
\[
\boxed{
\begin{aligned}
\text{raw-H2 route: }&
\sum_mR_m^{-3}Q_m=\infty,\\
\text{palinstrophy route: }&
\sum_mR_m^{-1}Q_m=\infty.
\end{aligned}
}
\]

For geometric records, bounded, logarithmic, and polynomial-in-record-index gains are all insufficient. Any viable route must produce near-power-scale multiplicity/residence, a stronger per-event cost, or a different non-summable resource.

## 12. Audit status

Closed/reduced here:

- ambiguity about how large a multiplicity/duration gain must be;
- any claim that logarithmic residence alone defeats the current ancestry firewalls;
- any use of event counts without a non-reuse allocation theorem.

Still OPEN:

- whether the retained CE-H geometry can produce multiplicity near the threshold;
- whether per-event costs strengthen with record scale;
- whether a bounded-overlap allocation theorem exists;
- whether endpoint temporal thickening produces an additional scale factor;
- all high-jet/tube/interface/genealogy exits and inherited root-level branches.

## 13. Next target

Test the strongest existing packet/covering mechanisms in the M17 chain against the exact thresholds above. In particular audit whether bounded-overlap coefficient cells, dyadic shell packing, recurrent-loop packets, or evacuation residence can yield any \(Q_m\) growing faster than logarithmically or polynomially in the record index without reusing the same raw-H2/palinstrophy resource.

---

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
