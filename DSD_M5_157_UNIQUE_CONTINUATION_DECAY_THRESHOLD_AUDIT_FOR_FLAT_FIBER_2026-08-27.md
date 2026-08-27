# DSD M5-157 — Unique-Continuation Decay-Threshold Audit for the Flat Same-Tail Fiber

Date: 2026-08-27

Status: **LITERATURE/SCOPE FIREWALL / EXISTING EXTERIOR PARABOLIC LANDIS-OLEINIK/BACKWARD-UNIQUENESS RESULTS REQUIRE GAUSSIAN OR SUPER-GAUSSIAN TERMINAL DECAY UNDER THEIR GENERAL COEFFICIENT HYPOTHESES; THE CURRENT FUCHSIAN-FLAT CONDITION IS ONLY SUPERALGEBRAIC AND THE NATURAL ANALYTIC HIGH-FREQUENCY ESCAPE CAN BE OF EXPONENTIAL-IN-RADIUS SIZE, SO THESE THEOREMS DO NOT DIRECTLY CLOSE P1_B^S / GLOBAL REGULARITY UNPROVED.**

---

## 1. Current flat condition

After M5-145, a same-tail difference has no algebraic Fuchsian coefficient.

For the relative velocity/vorticity on the W1 far corridor this gives, for every finite `N`,

\[
|Z(Y,s)|+|\delta\Omega(Y,s)|
\le C_N(1+|Y|)^{-N}
\]

with the corresponding finite-derivative versions.

Equivalently in inverse-radius variables,

\[
K(\xi,s,\theta)=O(\xi^{-N})
\qquad\forall N.
\]

This is **superalgebraic**, not automatically Gaussian.

---

## 2. Exterior parabolic Landis--Oleinik threshold

Wu--Zhang's exterior-domain Landis--Oleinik theorem treats bounded solutions of parabolic inequalities with variable coefficients satisfying quantitative regularity/decay assumptions at infinity.

The terminal decay hypothesis in its general form is of the type

\[
\boxed{
|u(x,0)|\le C_k e^{-k|x|^2}
\qquad\forall k>0.
}
\]

That is decay faster than every Gaussian rate.

The theorem is closely related to the Escauriaza--Seregin--Sverak backward-uniqueness framework, but it does not say that arbitrary superpolynomial decay is enough for a general parabolic system with lower-order terms.

---

## 3. Comparison with the M5-154 escape

M5-154 shows that if a nonzero flat fiber survives, its distinguishability must escape to cross-section frequencies at least on the parabolic scale.

A uniform analytic strip gives high-frequency amplitudes of schematic size

\[
e^{-\delta\Omega}.
\]

At

\[
\Omega\sim r
\]

this is only

\[
\boxed{e^{-\delta r},}
\]

which is superalgebraic but much larger than

\[
e^{-k r^2}
\]

for large `r`.

Therefore the analytic frequency-escape scenario is compatible with the current general Landis threshold.

---

## 4. Why superalgebraic is not interchangeable with super-Gaussian

The implication

\[
O(r^{-N})\ \forall N
\Longrightarrow
O(e^{-kr^2})\ \forall k
\]

is false.

Examples such as

\[
e^{-\sqrt r},\quad e^{-r},\quad e^{-(\log r)^2}
\]

illustrate distinct beyond-all-orders rates.

Hence a proof may not invoke a Gaussian Carleman theorem solely from the vanishing of every Fuchsian Taylor coefficient.

---

## 5. Stationary and elliptic results do not directly transfer

There are unique-continuation-at-infinity results for stationary Navier--Stokes/elliptic equations under sufficiently strong algebraic or exponential decay assumptions.

The current fiber is a complete recurrent **time-dependent** solution of a homogeneous relative Leray/Navier--Stokes equation.

Replacing that system by a stationary elliptic equation would discard the very cross-section frequency escape isolated by M5-154.

This is an axial/dynamical mismatch and is therefore RED.

---

## 6. What a direct theorem would need

A theorem closing the present branch would have to exploit more structure than generic parabolic UCI, for example:

- the exact Leray outward drift;
- the common critical `1/r` tail, which makes all relative lower-order coefficients subleading at infinity;
- the homogeneous same-tail difference equation;
- compact complete recurrence in normalized time;
- and/or the Branch-S invariant pair measure.

A sufficient new statement would look schematically like

\[
\boxed{
\text{complete recurrent relative Leray solution}
+
\text{superalgebraic decay at infinity}
\Longrightarrow0.
}
\]

No such theorem has been established in the current repository or identified as a directly applicable literature theorem.

---

## 7. DSD four-chain audit

### Formation — GREEN

The decay classes are kept as actually proved: superalgebraic, not Gaussian.

### Axis — GREEN

Stationary spatial UCI, terminal-time BU, and recurrent Leray-time flatness are treated as different problems.

### Static aggregation — GREEN

Several decay statements are not merged into a stronger one without an implication theorem.

### Dynamics — GREEN

The cross-section frequency escape remains active and is not erased by a stationary analogy.

### Cross-audit — GREEN

This note blocks a shortcut without weakening M5-154/M5-155.

---

## 8. Updated Branch-S gate

The statistically visible flat branch must now satisfy simultaneously

\[
\boxed{
\begin{aligned}
&K=O(\xi^{-N})\quad\forall N,\\
&\Omega_{cross}(\tau)\text{ escapes to the parabolic scale},\\
&K\text{ lies in a uniform reduced analytic strip},\\
&\text{generic Gaussian-UCI hypotheses are not yet reached.}
\end{aligned}}
\]

The next useful calculation is therefore an **NSE-specific spectral-transfer estimate**, not a direct invocation of a generic Landis theorem.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
