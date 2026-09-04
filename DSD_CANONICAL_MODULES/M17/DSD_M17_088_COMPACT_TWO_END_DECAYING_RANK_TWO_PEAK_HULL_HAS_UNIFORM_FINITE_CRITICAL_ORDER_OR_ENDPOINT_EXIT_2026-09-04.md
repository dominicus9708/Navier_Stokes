# DSD M17-088 — A compact two-end decaying Rank-2 peak hull has uniformly finite critical order or exits through endpoint degeneration

Date: 2026-09-04
Canonical ID: **M17-088**

Status: **INTERNAL UNIFORM CRITICAL-ORDER COMPACTNESS GATE / ON A COMPACT ANALYTIC PURE-KERNEL SUBHULL OF TWO-ENDED DECAYING ACTIVE VORTEX-LINE COMPONENTS WITH A UNIFORM POSITIVE PEAK FLOOR AND UNIFORM SEPARATION FROM RANK/INTERFACE LOSS, THE FINITE DEGENERACY ORDERS OF M17-085--087 CANNOT DIVERGE. OTHERWISE A SEQUENCE OF PEAKS WITH ORDERS `nu_j->infinity` HAS A COMPACT LIMIT FOR WHICH EVERY LINE DERIVATIVE OF `g=D_xi log rho` VANISHES AT THE LIMIT PEAK. ANALYTICITY ALONG THE LIMIT VORTEX LINE THEN FORCES `g` TO VANISH IDENTICALLY ON THE CONNECTED ANALYTIC LINE COMPONENT, SO `rho` IS A POSITIVE LINEWISE CONSTANT. THIS CONTRADICTS RETENTION OF THE TWO-END DECAY CLASS WITH NONZERO PEAK FLOOR. THEREFORE `nu<=nu_*<infinity` ON THAT SUBHULL. IF THE LIMIT LOSES TWO-END DECAY, PEAK FLOOR, ACTIVE RANK, OR LINE-COMPONENT COMPACTNESS, THAT LOSS IS AN EXPLICIT ENDPOINT/RANK/INTERFACE EXIT RATHER THAN A PROOF CONTRADICTION. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Compact decaying peak subhull

Consider a compact analytic subhull of pure-kernel Rank-2 states satisfying:

1. each marked vortex-line active component has two decaying/zero ends as in M17-085;
2. each component contains a marked positive amplitude peak;
3. the marked peak has a uniform floor

\[
\boxed{\rho_*\le\rho_{peak}\le\rho^*}
\]

with `rho_*>0`;
4. the marked neighborhood remains uniformly separated from rank loss, angle-interface loss, and the boundary of the pure-kernel chart;
5. the analytic local charts and derivative bounds are precompact strongly enough to pass all fixed finite jets to a subsequential limit.

These are the same type of hard-hull assumptions used elsewhere in M17 when upgrading pointwise finite jet order to a uniform one.

---

## 2. Suppose critical order is unbounded

At each marked peak define

\[
g=D_\xi\log\rho.
\]

Let `nu_j` be the first nonzero line-jet order of `g`, so

\[
D_\xi^m g=0
\qquad(0\le m<\nu_j)
\]

and

\[
D_\xi^{\nu_j}g<0.
\]

Assume for contradiction that

\[
\boxed{\nu_j\to\infty.}
\]

By compactness, pass to a subsequence whose marked states and centered vortex-line charts converge to a limit state and limit peak.

---

## 3. Every fixed line jet vanishes in the limit

Fix any integer `M>=0`.
For all sufficiently large `j`,

\[
M<\nu_j.
\]

Hence

\[
D_\xi^M g_j=0
\]

at the marked peak.
Passing to the compact limit gives

\[
D_\xi^M g_\infty=0.
\]

Since `M` was arbitrary,

\[
\boxed{
D_\xi^M g_\infty=0
\qquad\text{for every }M\ge0.
}
\]

Thus the linewise analytic function `g_infty` has infinite-order vanishing at the limit peak.

---

## 4. Analyticity forces linewise constancy of rho

Analyticity along the limit vortex line gives

\[
\boxed{g_\infty\equiv0}
\]

on a neighborhood of the limit peak.
By analytic continuation along the connected analytic active line component,

\[
\boxed{g_\infty=D_\xi\log\rho_\infty\equiv0.}
\]

Therefore

\[
\boxed{D_\xi\rho_\infty=0}
\]

on that component, so

\[
\boxed{\rho_\infty\equiv\rho_c>0}
\]

there.
The positivity follows from the retained peak floor `rho_*>0`.

---

## 5. Conflict with the retained two-end decay class

The subhull is assumed to retain the two-ended decaying/zero-end component class.
Therefore the limit line component must satisfy

\[
\rho_\infty\to0
\]

at both retained ends.
But Section 4 gives a positive constant value along the connected line.
These are incompatible.

Hence the critical order cannot diverge while all retained subhull hypotheses survive.

Therefore there exists

\[
\boxed{\nu_*<\infty}
\]

such that

\[
\boxed{\nu\le\nu_*}
\]

for every marked peak in the compact two-end decaying hard subhull.

---

## 6. What happens if the compact limit avoids the contradiction

The argument is deliberately conditional on retention of the line-end class.
If an unbounded-order sequence avoids the contradiction, then at least one retained hypothesis must fail in the limit.
Possible exits include

\[
\boxed{
R_{end}^{nondecay/recurrence}
\ \lor\
T_{rank/interface}
\ \lor\
T_{line-chart/completeness}
\ \lor\
\rho_{peak}\to0.
}
\]

These are not silently discarded.
They are exactly the endpoint and degeneration exits already separated by M17-085--086.

---

## 7. Finite family of higher-jet maximum gates

Combine the uniform bound with M17-087.
Every degenerate maximum in the retained subhull has

\[
3\le\nu\le\nu_*.
\]

For each fixed `nu`, survival requires:

\[
D_nD_\xi^jg=0,
\qquad
D_kD_\xi^jg=0
\qquad(0\le j\le\nu-2),
\]

plus the higher-order tilt formulas

\[
\Theta_{\nu,n}
=-\frac{D_nD_\xi^{\nu-1}g}{D_\xi^\nu g},
\qquad
\Theta_{\nu,k}
=-\frac{D_kD_\xi^{\nu-1}g}{D_\xi^\nu g},
\]

and the Riccati compensation margin

\[
\boxed{
\mathcal M_{deg}^{(\nu)}
=rD_ks-\Theta_{\nu,n}D_\xi q>0
}
\]

on every complete persistent `n`-tangent sheet where the reciprocal Riccati comparison applies.

Thus the formerly open-ended degeneracy tower becomes a finite list of explicit jet gates on the retained compact decaying hull.

---

## 8. Oscillatory-tail consequence

If a retained two-ended oscillatory component has infinitely many line maxima, compactness now gives only finitely many allowed critical orders.
Therefore some critical order occurs infinitely often along a recurrent sequence.

This does not itself produce a contradiction, but it reduces the oscillatory branch to recurrent visits to a finite set of maximum-jet types, each carrying the M17-079/080 or M17-087 compensation ledger.

The next useful object is therefore a **critical-type turnover measure**, not another unbounded Taylor expansion.

---

## 9. DSD analysis

The descriptor hierarchy is now finite on the retained decaying compact hull:

\[
\boxed{
\text{line peak}
\to
\nu\in\{1,3,5,\ldots,\nu_*\}
\to
\text{finite jet-lock hierarchy}
\to
\text{positive compensation margin or exit}.
}
\]

This is the Rank-2 analogue of the finite analytic jet reduction previously used for Rank-1 nodal events.

---

## 10. DSD audit

### Audit A — deriving linewise decay from finite energy
Rejected. Two-end decay is a retained branch hypothesis, not a consequence proved here.

### Audit B — assuming compactness preserves global endpoints automatically
Rejected. Endpoint loss is explicitly listed as an exit. The uniform-order conclusion applies only to a subhull in which the two-end class is retained under the chosen compact convergence.

### Audit C — allowing the limit peak amplitude to vanish
Excluded only by the stated hard-hull floor `rho_*>0`. If the floor is lost, `rho_peak->0` is a separate degeneration exit.

### Audit D — claiming uniform analytic radius without hypothesis
Not claimed independently. The compact analytic chart assumption is stated as part of the retained hard subhull.

### Audit E — proof status
The critical-order tower is finite under the stated compact decaying hypotheses, but the finite compensation gates are not yet contradicted.

---

## 11. Corrected Rank-2 decaying frontier

On the compact two-ended decaying pure-kernel hard subhull,

\[
\boxed{
R_{2,pk}^{decay,compact}
\Longrightarrow
\bigvee_{\nu\le\nu_*}
R_{2,max}^{(\nu),\ compensation}
\ \lor\
T_{max/order/interface}.
}
\]

Here `nu=1` is the regular M17-079--080 class and odd `nu>=3` are the M17-087 degenerate classes.

The independent noncritical-tail descriptor is therefore removed on this retained subhull.

---

## 12. Next target — critical-type turnover ledger

The next Rank-2 problem is no longer peak existence or unbounded critical order.
It is whether a recurrent compact solution can cycle among the finite critical types while continuously servicing their positive Riccati compensation margins.

The useful next calculation is to define a type-resolved measure/current over

\[
\nu\in\{1,3,5,\ldots,\nu_*\}
\]

and compare its turnover with

1. M17-080's constant `3/2` margin recharge;
2. M17-078's moving full-spatial-maximum turnover;
3. M17-034's area-curvature continuity ledger.

This is the **Rank-2 Critical-Type Turnover Gate (RCTTG)**.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
