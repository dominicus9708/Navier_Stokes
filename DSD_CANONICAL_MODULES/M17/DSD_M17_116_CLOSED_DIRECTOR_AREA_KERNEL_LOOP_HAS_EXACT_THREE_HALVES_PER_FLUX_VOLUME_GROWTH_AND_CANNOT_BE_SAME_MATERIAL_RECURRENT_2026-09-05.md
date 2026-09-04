# DSD M17-116 — Closed director-area kernel loop has exact three-halves per-flux-volume growth and cannot be same-material recurrent

Date: 2026-09-05
Canonical ID: **M17-116**

Status: **INTERNAL CRITICAL-RIBBON CARRIER CLOSURE / M17-115 FOUND THAT A COMPLETE PERSISTENT CRITICAL RIBBON IS A MATERIAL CIRCULAR `J_xi` KERNEL FIBER. BEFORE WEIGHTING BY THE RICCATI MARGIN, THE BARE GEOMETRY HAS A STRONGER EXACT LAW. A MATERIAL KERNEL LINE ELEMENT SATISFIES `D_B log ds=sigma_k+1/2`, WHILE DIRECTOR-AREA MAGNITUDE SATISFIES `D_B log|J_xi|=sigma_k-1`; HENCE `D_B log(ds/|J_xi|)=3/2` POINTWISE. FOR ANY CLOSED MATERIAL `J_xi` LOOP, THE PER-UNIT-DIRECTOR-AREA-FLUX VOLUME `V_J=oint ds/|J_xi|` OBEYS `V_J(theta)=exp[3(theta-theta_0)/2]V_J(theta_0)`. ON A CIRCULAR CRITICAL RIBBON, `length=2pi/|q|`; THEREFORE A COMPACT SAME-MATERIAL RECURRENT RIBBON WITH `|J_xi|` BOUNDED BELOW AND `|q|` BOUNDED BELOW WOULD KEEP `V_J` BOUNDED, CONTRADICTING THE EXACT EXPONENTIAL GROWTH. THUS THE COMPLETE CRITICAL-RIBBON EXCEPTION OF M17-114 IS CLOSED AS A SAME-MATERIAL COMPACT RECURRENT BRANCH. EULERIAN RECURRENCE CAN STILL USE RIBBON TURNOVER: MATERIAL LOOPS MAY LEAVE THE BOUNDED CORE WHILE DIFFERENT RANK-TWO LOOPS ENTER. THIS IS A RESIDENCE/TURNOVER CLOSURE, NOT GLOBAL REGULARITY. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Material director-area kernel loop

On the pure-kernel branch,

\[
J_\xi=|J_\xi|k\neq0.
\]

Because the director-area two-form is frozen into the `B` flow, its flux lines are transported by the regular material diffeomorphism.

Therefore a closed `J_xi` integral curve at time `theta_0` is carried to a closed material `J_xi` integral curve at later regular times.

Let

\[
\Gamma(\theta)
\]

be such a material loop, with unit tangent `k` and arclength element `ds`.

---

## 2. Exact material stretching of ds

For a material line element tangent to `k`,

\[
D_B\log ds
=k\cdot(\nabla B)k.
\]

The antisymmetric part does not contribute to the quadratic form and

\[
B=U+\frac12y.
\]

Therefore

\[
\boxed{
D_B\log ds
=\sigma_k+\frac12.
}
\]

Equivalently,

\[
D_Bds
=\left(\sigma_k+\frac12\right)ds.
\]

---

## 3. Exact material law for director-area magnitude

M17-026/M17-033 give

\[
\boxed{
D_B\log|J_\xi|
=\sigma_k-1.
}
\]

Hence

\[
D_B\log|J_\xi|^{-1}
=-\sigma_k+1.
\]

---

## 4. Strain cancels in the per-flux line-volume element

Combine Sections 2--3:

\[
\begin{aligned}
D_B\log\left(\frac{ds}{|J_\xi|}\right)
&=\left(\sigma_k+\frac12\right)
-\left(\sigma_k-1\right)\\
&=\frac32.
\end{aligned}
\]

Thus pointwise on every regular material director-area line,

\[
\boxed{
D_B\left(\frac{ds}{|J_\xi|}\right)
=\frac32\frac{ds}{|J_\xi|}.
}
\]

The quantity `ds/|J_xi|` is the physical similarity-volume element per unit director-area tube flux in local flux coordinates.

---

## 5. Closed-loop law

Define

\[
\boxed{
\mathscr V_J(\theta)
:=\oint_{\Gamma(\theta)}
\frac{ds}{|J_\xi|}.
}
\]

Because `Gamma(theta)` is a material closed loop, differentiation gives directly

\[
\boxed{
\frac d{d\theta}\mathscr V_J
=\frac32\mathscr V_J.
}
\]

Hence

\[
\boxed{
\mathscr V_J(\theta)
=e^{\frac32(\theta-\theta_0)}
\mathscr V_J(\theta_0).
}
\]

No strain, pressure, `kappa`, or margin term remains.

This is an exact geometric carrier law.

---

## 6. Apply to the complete critical ribbon

M17-115 gives for a complete critical ribbon

\[
\boxed{
\Gamma(\theta)\text{ is a plane circle},
\qquad
L_k(\theta)=\frac{2\pi}{|q(\theta)|}.
}
\]

Suppose the same material ribbon remains in a compact recurrent class with

\[
\boxed{
|J_\xi|\ge c_J>0
}
\]

and

\[
\boxed{
|q|\ge c_q>0.
}
\]

Then

\[
L_k\le\frac{2\pi}{c_q}
\]

and therefore

\[
\mathscr V_J
=\oint\frac{ds}{|J_\xi|}
\le
\frac{2\pi}{c_qc_J}.
\]

This is uniformly bounded.

But Section 5 gives exponential growth without bound.

Contradiction.

Therefore

\[
\boxed{
R_{ribbon}^{same-material,compact,recurrent}
\Longrightarrow\bot.
}
\]

under the stated nondegeneracy bounds.

---

## 7. Allowed exits from the same-material closure

To avoid the contradiction, a complete material ribbon must lose at least one retained property:

\[
\boxed{
\begin{aligned}
&|J_\xi|\to0 &&\text{asymptotic rank degeneration},\\
&|q|\to0 &&\text{circle radius diverges / full-rank peak degeneration},\\
&\text{ribbon condition fails} &&\text{return to finite peak intersections},\\
&\text{loop leaves the bounded recurrent spatial core} &&\text{Eulerian turnover},\\
&\text{regularity/flow-box fails}.&&
\end{aligned}
}
\]

M17-104 forbids `J_xi` from reaching zero in finite regular material time, but asymptotic loss remains an exit unless a uniform lower bound is retained.

---

## 8. Eulerian turnover is not closed by this argument

A fixed bounded Eulerian core can in principle display recurrent circular-ribbon geometry while different material loops enter and leave.

The exact law says every individual material loop carries an exponentially growing per-flux volume and therefore cannot be the permanently recurrent carrier.

Thus any Eulerian recurrent ribbon pattern requires

\[
\boxed{
\text{closed-loop material turnover through the spatial core}.
}
\]

This is analogous to the M5 residence firewall but uses the director-area flux geometry itself.

No current theorem assigns a nonrecyclable cost to importing a new ribbon loop.

---

## 9. Relation to M17-115 margin neutralization

M17-115 found

\[
\mathscr I_{rib}
=\oint\frac{N_{R2}}{|J_\xi|}ds
\]

with homogeneous margin damping cancelled.

The present module shows that the underlying measure

\[
\boxed{
\frac{ds}{|J_\xi|}
}

itself grows at `3/2`.

Thus margin neutralization does not make the carrier recurrent.
It transfers the exact material expansion into the loop measure.

This resolves the apparent softness of the ribbon margin ledger.

---

## 10. DSD analysis

The critical ribbon has two complementary descriptors:

\[
\boxed{
\text{margin per flux-volume}
\quad\text{and}\quad
\text{flux-volume itself}.
}
\]

The first can have zero mean recharge, but the second expands exactly.
A compact recurrent same-material state would need both to recur, which is impossible.

---

## 11. DSD audit

### Audit A — interpreting M17-115 zero mean margin recharge as full ribbon recurrence
Rejected.

### Audit B — using physical volume of a finite-thickness tube without justification
Avoided. The exact one-dimensional per-flux quantity `oint ds/|J_xi|` is used directly.

### Audit C — claiming every circular ribbon is globally impossible
Rejected. Only same-material compact recurrence is excluded under nondegeneracy bounds.

### Audit D — forgetting Eulerian replacement by different loops
Rejected; this remains the turnover exit.

### Audit E — proof status
The complete critical-ribbon branch is closed only as a same-material compact recurrent carrier, not as an Eulerian recurrent pattern with turnover.

---

## 12. Updated critical-ribbon frontier

The DAPOG exceptional branch now satisfies

\[
\boxed{
R_{ribbon}^{complete}
\Longrightarrow
T_{ribbon}^{material\ turnover}
\ \lor\
D_{J/q}^{asymptotic}
\ \lor\
T_{finite-peak}
\ \lor\
T_{regularity}.
}
\]

Thus the Rank-2 analytic oscillation problem no longer has an unstructured same-material ribbon survivor.

The next high-value step is to incorporate this exact `3/2` per-flux-volume growth into the spatial boundary ledger and ask whether repeated import of fresh closed ribbon loops can coexist with finite total director-area flux and the positive-margin turnover budget.

This is the **Ribbon Flux-Volume Turnover Gate (RFVTG)**.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
