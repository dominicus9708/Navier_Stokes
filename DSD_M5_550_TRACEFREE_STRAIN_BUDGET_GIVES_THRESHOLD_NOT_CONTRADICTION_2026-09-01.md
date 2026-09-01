# DSD M5-550 — Sharp trace-free strain budget gives a quantitative threshold, not a contradiction

Date: 2026-09-01

Status: **SHARP MATRIX-BUDGET AUDIT / AT A NONDEGENERATE ANCHORED FIRST-HITTING MARKER M5-549 GIVES `sigma>=1`; FOR ANY TRACE-FREE SYMMETRIC STRAIN TENSOR WITH `Sigma xi=sigma xi+tau`, A SHARP POINTWISE MINIMIZATION GIVES `|Sigma|^2 >= (3/2)sigma^2 + 2|tau|^2` / ACTIVE-CARRIER THICKENING THEREFORE CONVERTS EACH RECURRENT FIRST-HITTING EVENT INTO A FIXED LOCAL STRAIN-ENERGY COST, AND ANCHORED TRANSVERSE ACTION ADDS A SECOND POSITIVE TERM / HOWEVER THE WHOLE-SPACE IDENTITY `||Sigma||_2^2=(1/2)||W||_2^2` ONLY TURNS THIS INTO A LOWER THRESHOLD ON THE CRITICAL ENSTROPHY CAP; WITHOUT AN INDEPENDENT UPPER CONSTANT BELOW THAT THRESHOLD THERE IS NO CONTRADICTION / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Trace-free symmetric strain geometry

Let

\[
\Sigma=\Sigma^T,
\qquad
\operatorname{tr}\Sigma=0,
\]

and fix a unit vector `xi`.

Write

\[
\boxed{
\Sigma\xi
=
\sigma\xi+\tau,
\qquad
\tau\perp\xi.
}
\]

Choose an orthonormal basis with

\[
e_1=\xi.
\]

Then

\[
\Sigma
=
\begin{pmatrix}
\sigma & \tau_2 & \tau_3\\
\tau_2 & a & b\\
\tau_3 & b & c
\end{pmatrix},
\]

with

\[
a+c=-\sigma.
\]

---

## 2. Sharp Frobenius-norm minimization

The Frobenius norm is

\[
|\Sigma|^2
=
\sigma^2
+2|\tau|^2
+a^2+c^2+2b^2.
\]

Under the trace constraint

\[
a+c=-\sigma,
\]

the minimum of

\[
a^2+c^2+2b^2
\]

occurs at

\[
a=c=-\frac\sigma2,
\qquad
b=0,
\]

and equals

\[
\frac{\sigma^2}{2}.
\]

Hence the sharp pointwise inequality is

\[
\boxed{
|\Sigma|^2
\ge
\frac32\sigma^2
+2|\tau|^2.
}
\]

Equality is attained by

\[
\Sigma
=
\begin{pmatrix}
\sigma & \tau_2 & \tau_3\\
\tau_2 & -\sigma/2 & 0\\
\tau_3 & 0 & -\sigma/2
\end{pmatrix}
\]

after rotating the transverse basis so that the remaining transverse off-diagonal entry vanishes.

---

## 3. First-hitting axial floor

M5-549 showed that at an upward first-hitting local maximum of the anchored marker amplitude,

\[
\boxed{
\sigma\ge1.
}
\]

Therefore at that marked point,

\[
\boxed{
|\Sigma|^2
\ge
\frac32
+2|\tau|^2.
}
\]

In particular even the passive anchored case `tau=0` pays a fixed strain magnitude.

If the anchored branch has active transverse cancellation, the strain cost is strictly larger.

---

## 4. Thickening the pointwise cost

The active first-hitting marker lies on the globally smooth compact core.

Uniform bounds on spatial/time derivatives of `Sigma`, `sigma`, and the active marker trajectory imply fixed continuity scales.

Hence there exist

\[
r_s>0,
\qquad
\delta\theta_s>0
\]

such that around every retained first-hitting event,

\[
\sigma\ge\frac12
\]

on a spacetime tube

\[
B_{r_s}(Y_j)\times
[\theta_j-\delta\theta_s,
 \theta_j+\delta\theta_s]
\]

unless one re-enters an already typed derivative/compactness defect, which is absent on the current hard core.

Therefore

\[
\boxed{
\int_{B_{r_s}}|\Sigma|^2dy
\ge c_s>0
}
\]

through a fixed positive time thickness at every such event.

---

## 5. Positive event density gives a mean strain floor

The retained first-hitting/dual genealogy occurs with positive log-scale frequency.

Select a disjoint positive-density subfamily of the thickened time intervals exactly as in M5-493.

Then

\[
\boxed{
\left\langle
\int_{B_{R_core}}|\Sigma|^2dy
\right\rangle
\ge s_{mean}>0.
}
\]

On the active anchored-transverse branch, the additional term

\[
2|\tau|^2
\]

in the sharp matrix inequality strengthens `s_mean` by a fixed positive amount determined by the recurrent transverse charge.

---

## 6. Whole-space Riesz identity

For divergence-free velocity on `R3`, the symmetric and antisymmetric parts of `grad U` are orthogonal in `L2`.

The antisymmetric part satisfies

\[
\|A\|_2^2
=
\frac12\|W\|_2^2,
\]

while

\[
\|\nabla U\|_2^2
=
\|W\|_2^2.
\]

Therefore

\[
\boxed{
\|\Sigma\|_2^2
=
\frac12\|W\|_2^2
=
\frac12E.
}
\]

On the similarity hard component,

\[
E\le Z_*.
\]

Hence

\[
\boxed{
\int|\Sigma|^2dy
\le
\frac12Z_*.
}
\]

---

## 7. Quantitative critical-enstrophy threshold

Combining the recurrent local strain floor with the global strain identity gives

\[
\frac12Z_*
\ge
s_{mean}.
\]

Thus

\[
\boxed{
Z_*
\ge
2s_{mean}
=:Z_{strain}^{min}>0.
}
\]

The active anchored-transverse branch has a larger threshold because `s_mean` includes the `2|tau|^2` contribution.

This is a genuine quantitative restriction on the survivor.

---

## 8. Relation to earlier thresholds

M5-494 already obtained a lower critical-enstrophy threshold from

\[
Q
\le
CE^{3/4}P^{3/4}
\]

and the positive dual palinstrophy mean.

M5-501 obtained a product threshold involving enstrophy and bounded palinstrophy.

M5-550 provides a different, purely local geometric threshold:

\[
\boxed{
\text{recurrent first-hitting axial strain}
\Rightarrow
Z_*\ge Z_{strain}^{min}.
}
\]

The thresholds may be combined by taking their maximum, but they are not presently known to exceed the inherited upper cap.

---

## 9. Two-direction matrix strengthening and firewall

If two noncollinear unit directions `xi_1,xi_2` at the **same spatial point and same time** both obey

\[
\xi_i^T\Sigma\xi_i\ge1,
\]

then trace-free symmetric-matrix optimization gives a stronger lower bound.

Writing

\[
c=\xi_1\cdot\xi_2,
\]

the minimum squared Frobenius norm under both active constraints is

\[
\boxed{
|\Sigma|^2
\ge
\frac{2}{c^2+1/3},
}
\]

when both constraints are active.

For orthogonal directions this gives

\[
|\Sigma|^2\ge6.
\]

However M5-491's firewall remains: the persistent dual lineages generally occupy different points and need not sample one common `Sigma`.

Therefore this stronger two-direction inequality cannot be applied to the pair without an additional same-point/overlap theorem.

---

## 10. Verdict

The sharp trace-free geometry proves that the anchored first-hitting mechanism consumes a fixed strain budget.

But the available global identity supplies a finite critical budget proportional to `Z_*`, and repeated events occur sequentially rather than requiring unbounded simultaneous strain energy.

Thus

\[
\boxed{
\text{strain floor}
\Rightarrow
\text{critical threshold},
}

not

\[
\text{strain floor}
\Rightarrow
\text{contradiction}.
\]

The route closes only if an independent calculation yields

\[
Z_*<Z_{strain}^{min},
\]

which is not currently available.

---

## 11. Updated core-excess search

M5-547--550 have now audited three natural ways to make the anchored branch overpay:

1. projected transverse dissipation — locally recyclable at the anchored marker/tube;
2. parallel amplitude channel — a bounded coboundary on a nondegenerate marker or migration cost;
3. trace-free strain magnitude — gives only a finite enstrophy threshold.

Thus the missing excess is not a simple pointwise strain-amplitude inequality.

The remaining candidate must involve **cycle organization**: how the same finite material lineages repeatedly re-enter first-hitting, migration, and dual-source roles while all scalar budgets return to their recurrent values.

---

## 12. Highest-value next target

Return to the finite lineage transfer graph of M5-498 with the newly localized core marks.

Attach to every recurrent edge/event the now-audited costs:

- axial first-hitting strain floor;
- migration surface-current cost when markers degenerate;
- pair-motion cost on nonanchored events;
- near-recycling label on anchored events.

Then test whether a directed recurrent cycle can be composed entirely of **zero-excess edge types**.

If every directed cycle must contain at least one genuinely nonrecyclable edge, the finite graph itself provides the strict cycle obstruction sought in M5-546.

This graph-level audit is now more promising than another local norm inequality.

---

## 13. Status

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]