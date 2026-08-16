# Nested-episode double-counting audit and disjointness threshold

Date: 2026-08-16

Status: **AUDIT RESULT. THE LOGARITHMIC PRODUCTIVE-STRAIN ACTION FROM DIFFERENT TERMINAL FIRST-HITTING LEVELS CANNOT BE SUMMED NAIVELY, BECAUSE THE CLEAN-PRECURSOR INTERVALS ARE STRONGLY NESTED FOR GEOMETRICALLY SPACED LEVELS. TIME-DISJOINT CLEAN EPISODES REQUIRE SUPER-POWER LEVEL SEPARATION. THIS PREVENTS A FALSE NONREPEATABILITY PROOF AND IDENTIFIES SCALE-ORTHOGONAL PACKING AS THE REAL MISSING STEP.**

## 1. Deep clean threshold in physical amplitude

For a terminal first-hitting level `W_j`, choose

\[
q_{\beta,j}=W_j/R_j^\beta,
\qquad
0<\beta<4.
\]

The corresponding earlier physical vorticity threshold is

\[
\boxed{
W_{{\rm deep},j}
=\frac{W_j}{q_{\beta,j}}
=R_j^\beta.
}
\]

The coherent-core kinetic-energy barrier gives

\[
R_j\lesssim W_j^{1/10}
\]

(up to logarithmic improvement).

Hence

\[
\boxed{
W_{{\rm deep},j}
=R_j^\beta
\lesssim
W_j^{\beta/10}.
}
\]

For every `beta<4`, this is far below `W_j`.

## 2. Geometric terminal levels produce nested intervals

Suppose

\[
W_{j+1}\asymp cW_j
\]

with fixed `c>1`.

Then

\[
W_{{\rm deep},j+1}
\lesssim
W_{j+1}^{\beta/10}
\ll
W_j.
\]

Because first-hitting times are ordered by the maximum-vorticity level, the first time at which the solution reaches `W_deep,j+1` occurs well before the terminal first-hitting time for `W_j`.

Therefore the clean-predecessor interval for terminal level `W_{j+1}` generally begins **before** the previous terminal episode has ended.

Thus the intervals

\[
I_j=[s_{m,j},s_{c,j}]
\]

cannot be assumed disjoint on a geometric sequence. They are naturally nested/overlapping.

## 3. Threshold for chronological disjointness

To force the next deep threshold to occur only after the previous terminal first hitting, one needs at least

\[
R_{j+1}^\beta>W_j.
\]

Using

\[
R_{j+1}\lesssim W_{j+1}^{1/10},
\]

this requires, up to fixed constants,

\[
W_{j+1}^{\beta/10}\gtrsim W_j.
\]

Equivalently,

\[
\boxed{
W_{j+1}
\gtrsim
W_j^{10/\beta}.
}
\]

Since `beta<4`,

\[
\boxed{
10/\beta>5/2.
}
\]

Thus genuinely time-disjoint clean-to-crossing episodes require super-power level separation, not merely geometric first-hitting separation.

## 4. Consequence for the logarithmic productive-strain action

Each individual episode satisfies

\[
\mathfrak A_{\lambda_2,j}
\gtrsim
c_\beta\log R_j.
\]

It is **incorrect** to conclude

\[
\sum_j\mathfrak A_{\lambda_2,j}=\infty
\]

as a new contradiction merely by summing these lower bounds over geometric terminal levels, because the same spacetime productive-strain event can be included in many nested intervals.

The divergence of the critical strain action is in any case compatible with a hypothetical singularity.

## 5. Two legitimate routes left

The audit leaves two possible ways to make cross-episode accumulation rigorous.

### A. Time-disjoint subsequence

Choose terminal levels separated at least by

\[
W_{j+1}\gtrsim W_j^{10/\beta}.
\]

Then clean intervals can be chronologically separated, but the sequence becomes extremely sparse and ordinary physical energy/dissipation costs can become summable.

### B. Scale-orthogonal packing on nested intervals

Keep denser terminal levels but prove that their productive strain / derivative / material channels occupy distinguishable spatial-frequency scales even when the time intervals overlap.

This requires a genuine Littlewood--Paley, wave-packet, material-probe, or Carleson-type packing theorem rather than scalar time integration.

## 6. Revised missing theorem

The productive-strain frontier therefore needs

\[
\boxed{
\text{nested spacetime action}
+\text{distinct renormalized scales}
\Longrightarrow
\text{bounded-overlap/orthogonality cost}.
}
\]

Without such a scale-sensitive statement, episodewise logarithmic lower bounds double-count the same physical action.

Status: **NAIVE EPISODE SUMMATION REJECTED / DISJOINTNESS REQUIRES `W_(j+1) >= W_j^(10/beta)` / MISSING STEP = SCALE-ORTHOGONAL PACKING OF NESTED PRODUCTIVE CHANNELS.**