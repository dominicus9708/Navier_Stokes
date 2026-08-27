# DSD M5-81 — Coarea Crossing Forcing and the Fragmentation Alternative

Date: 2026-08-27

Status: **QUANTITATIVE LEVELWISE CROSSING FORCING PROVED FROM THE ROBUST POSITIVE PUMP / EVERY EXACT OR NEAR-EXACT RETURNED PUMP HAS A REGULAR AMPLITUDE LEVEL WITH ORDER-ONE TOTAL CROSSING DENSITY / IF M5-80 CANNOT EXTRACT A PERSISTENT CROSSING COMPONENT, THE CROSSING MASS MUST DEGENERATE THROUGH COMPONENT FRAGMENTATION, CRITICAL-LEVEL LOSS, OR SPATIAL/TOPOLOGICAL MIGRATION / GLOBAL REGULARITY UNPROVED.**

## 1. Robust pump input

On the returned upstroke, M5-57 supplies

\[
\boxed{
X_w\ge c_1>0.
}
\]

At exact M5-70 saturation, M5-71 gives

\[
X_w=\nu(T-B),
\qquad
B=A_w+G_w\ge0.
\]

Therefore

\[
\boxed{
T
=B+\frac{X_w}{\nu}
\ge
\frac{c_1}{\nu}.
}
\]

Thus the exact positive endpoint has a uniform lower bound on its total crossing channel.

The same lower bound, up to the explicit M5-69 balance defect, applies to a sufficiently near-saturating returned sequence.

---

## 2. Coarea representation

Let the finite active amplitude band be

\[
I=[\lambda_-,\lambda_+]
\subset(0,\infty),
\]

and let the smooth nonnegative amplitude weight satisfy

\[
0\le w(\lambda)\le W:=\|w\|_{L^\infty(I)}<\infty.
\]

For each regular value, define the total level crossing density

\[
\tau_{tot}(\lambda,t)
:=
\sum_k\tau_k(\lambda,t),
\]

where

\[
\tau_k(\lambda,t)
:=
\int_{\Gamma_{\lambda,k}}
\frac{|\nabla a|}{\lambda}
|U\cdot n|^2\,dS.
\]

M5-78 gives the exact coarea identity

\[
\boxed{
T
=
\int_I
w(\lambda)\tau_{tot}(\lambda,t)\,d\lambda.
}
\]

---

## 3. Uniform integrated crossing lower bound

Since `w<=W`,

\[
T
\le
W\int_I\tau_{tot}(\lambda,t)\,d\lambda.
\]

Combining with the robust pump lower bound gives

\[
\boxed{
\int_I\tau_{tot}(\lambda,t)\,d\lambda
\ge
\frac{c_1}{\nu W}.
}
\]

This is independent of the number of connected superlevel components.

---

## 4. Existence of a quantitatively crossing amplitude level

Let

\[
L_I:=\lambda_+-\lambda_->0.
\]

By the mean-value bound for a nonnegative measurable function,

\[
\operatorname*{ess\,sup}_{\lambda\in I}
\tau_{tot}(\lambda,t)
\ge
\frac1{L_I}
\int_I\tau_{tot}(\lambda,t)\,d\lambda.
\]

Hence every exact positive returned endpoint has some amplitude value satisfying

\[
\boxed{
\tau_{tot}(\lambda,t)
\ge
\tau_*
:=
\frac{c_1}{\nu W L_I}>0.
}
\]

Because `a=|U|` is smooth, Sard's theorem implies that the critical values of `a` have Lebesgue measure zero.

The coarea identity itself is an almost-everywhere regular-level identity.

Therefore the essential supremum can be approached on regular values, and one may choose a regular crossing level with

\[
\boxed{
\tau_{tot}(\lambda,t)
\ge
\frac12\tau_*
}
\]

if desired, avoiding any issue of attainment of the exact essential supremum.

Thus positive endpoint pumping cannot hide entirely on critical amplitude values.

---

## 5. What this proves and what it does not

The previous conclusion is for the **sum over all connected superlevel components** at one regular amplitude value:

\[
\sum_k\tau_k
\ge
\frac12\tau_*.
\]

It does not yet imply that one component has a uniform lower bound independent of the sequence.

If the number of crossing components is `N(lambda,t)`, then trivially one component satisfies

\[
\max_k\tau_k
\ge
\frac{\tau_{tot}}{N}.
\]

Thus a uniform componentwise lower bound would follow from a uniform bound on `N`.

No such uniform topological-complexity bound has yet been proved for W1.

---

## 6. Component-fragmentation escape

Consider a returned saturating sequence `U_n` and choose regular levels `lambda_n` with

\[
\tau_{tot,n}(\lambda_n)
\ge
\frac12\tau_*.
\]

If no connected component carries a fixed fraction of this amount, then necessarily

\[
\boxed{
\max_k\tau_{k,n}(\lambda_n)
\to0
}
\]

while

\[
\boxed{
\sum_k\tau_{k,n}(\lambda_n)
\ge
\frac12\tau_*.
}
\]

Therefore the number/effective multiplicity of crossing components must diverge in the only sense relevant to the crossing measure.

Call this the **component-fragmentation alternative**.

It is a genuine geometric escape from the componentwise M5-75 quotient even though the total crossing budget remains order one.

---

## 7. Persistent-component alternative

Suppose instead that, after subsequence extraction, there exists a selected component `k_n` with

\[
\boxed{
\tau_{k_n,n}(\lambda_n)
\ge\eta_0>0.
}
\]

If additionally

\[
\lambda_n\to\lambda_*
\in(\lambda_-,\lambda_+),
\]

and the selected components stay in one fixed core with a regularity margin

\[
\inf_{\Gamma_{\lambda_n,k_n}}
|\nabla a_n|
\ge\kappa_0>0,
\]

then local analytic W1 compactness plus the implicit-function theorem place the sequence exactly in the M5-80 setting.

Consequently any sequence of vanishing endpoint defects converges to a smooth exact regular crossing endpoint satisfying

\[
K_A=0,
\qquad
\delta_\beta=0,
\qquad
K_\alpha=0,
\qquad
\mathfrak I=0.
\]

This is the desired compactness branch.

---

## 8. Exact new endpoint trichotomy

Combining M5-78, M5-80, and the present coarea lower bound gives the following trichotomy for a positive returned saturating sequence.

After subsequence extraction, at least one of the following occurs.

### A. Persistent regular crossing endpoint

A connected crossing component retains positive mass and uniform regularity in a fixed core.

Then M5-80 produces an exact smooth velocity-only endpoint in the omega limit.

### B. Component fragmentation / topology proliferation

Total crossing remains order one but is split among components whose individual crossing masses tend to zero.

### C. Geometric degeneration or migration

The selected crossing geometry loses one of the compactness margins:

\[
\inf|\nabla a_n|\to0,
\]

or the branch changes topology at nearby critical levels, or the relevant component leaves every fixed core.

Therefore the old vague phrase "critical-level issue" is now sharpened to a finite list of geometric escape mechanisms.

---

## 9. Interaction with the b=0 audit

M5-78 already ruled out

\[
b\equiv0
\]

on the whole active region of a positive exact endpoint.

The present result is stronger in level form:

\[
\boxed{
\text{there exists a regular amplitude level with order-one total crossing density.}
}
\]

Thus the only way the M5-75 dynamical coefficient recovery can fail everywhere componentwise is not global crossing collapse, but rather fragmentation or geometric degeneration of the crossing set.

---

## 10. A natural next quantitative target

The most direct closure target is now a **uniform complexity/transversality lemma** for the W1 analytic compact class.

Any one of the following would be sufficient to remove the fragmentation escape:

1. a uniform bound on the number of connected superlevel components intersecting the active core and band;
2. a lower bound on the crossing mass of at least one component in terms of `tau_tot`;
3. a uniform real-analytic nodal/level-set complexity estimate from the W1 analytic radius and derivative bounds;
4. a direct component-free formulation of the M5-75/M5-76 coefficient locking that acts on the whole regular level union while respecting independent component pressure gauges.

Option 4 is especially attractive because it would avoid proving a hard topological theorem.

---

## 11. DSD audit

### GREEN

The robust positive pump forces

\[
T\ge c_1/\nu.
\]

### GREEN

Coarea therefore forces an order-one total crossing density on at least one regular amplitude level.

### GREEN

Critical values alone cannot carry the entire positive crossing budget.

### GREEN

If one regular component retains a fixed crossing share and regularity margin, M5-80 rigorously passes all endpoint defects to the W1 limit.

### YELLOW

The total crossing density can in principle split among an increasing number of connected components.

### RED

No uniform W1 component-count or transversality theorem has yet been proved, so fragmentation remains an open endpoint escape.

---

## 12. Next calculation

Attempt a **component-free coefficient-locking identity** by summing the pressure-Poisson and amplitude relations over all connected components of one regular level after eliminating the independent component means.

If the independent means can be eliminated without dividing by each component crossing mass, the fragmentation alternative may be removed without any component-count estimate.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
