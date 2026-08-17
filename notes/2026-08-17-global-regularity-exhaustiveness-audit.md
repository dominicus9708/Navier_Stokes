# Global-regularity exhaustiveness audit

Date: 2026-08-17

Status: **TOP-LEVEL FIRST-HITTING CAUSAL SPLIT IS EXHAUSTIVE, BUT THE CURRENT `R -> infinity` COHERENT AFFINE-RESIDUAL FIXED POINT IS NOT BY ITSELF AN EXHAUSTIVE DESCRIPTION OF EVERY POSSIBLE BLOW-UP SEQUENCE. A COMPACT/NATURAL-SCALE NON-AFFINE LANE MUST REMAIN EXPLICIT. BOTH LANES CAN BE PLACED UNDER A COMMON MOVING-PHYSICAL-BAND REPOPULATION FRONTIER. GLOBAL REGULARITY NOT PROVED.**

---

## 1. What exhaustiveness means here

The proof challenge must distinguish two claims.

1. **Top-level causal exhaustiveness:** every finite-time amplification step lies in at least one retained branch.
2. **Final-shape exhaustiveness:** every hypothetical singular cascade converges to the single asymptotic fixed point currently being studied.

The first claim is substantially stronger than a heuristic branch diagram and is already available from the exact amplification identity. The second claim is not yet justified for the coherent `R -> infinity` fixed point alone.

---

## 2. Standard continuation gate

Let `T*` be the maximal smooth lifespan for smooth finite-energy decaying incompressible data. The standard Navier--Stokes continuation theory implies that a finite maximal time requires loss of a regularity-controlling vorticity norm; in particular an unbounded first-hitting sequence may be selected:

\[
W_j=\|\omega(t_j)\|_\infty\to\infty.
\]

One may take adaptive ratios

\[
W_j=q_jW_{j-1},
\qquad q_j\to\infty,
\]

because the amplitude is assumed unbounded.

In terminal normalization,

\[
r_j=W_j^{-1/2},
\]

\[
U_j(y,s)=r_ju(x_j+r_jy,t_j+r_j^2s),
\]

\[
\Omega_j(y,s)=r_j^2\omega(x_j+r_jy,t_j+r_j^2s),
\]

first hitting gives the exact cap

\[
\boxed{\|\Omega_j(s)\|_\infty\le1}
\]

on the normalized past, with terminal nontriviality

\[
|\Omega_j(0,0)|=1
\]

(or an arbitrarily close approximate maximizer if a maximum is not attained).

This gate is imported standard PDE continuation theory, not a DSD theorem.

---

## 3. Exact I/V amplification partition is the top-level safety certificate

Pull the actual final dangerous core back to the previous checkpoint. The exact Cauchy-defect formula is

\[
\omega(T)=I+V,
\]

where

\[
I=F(T)\omega(t_-)
\]

is inviscid material stretching and

\[
V=\nu F(T)\int_{t_-}^{T}F^{-1}\Delta\omega(X,t)dt
\]

is viscous rewriting of the Cauchy invariant.

If a final label satisfies

\[
|\omega(T)|\ge bqW_-,
\]

then the triangle inequality gives

\[
\boxed{|I|\ge bqW_-/2
\quad\lor\quad
|V|\ge bqW_-/2.}
\]

Thus every dangerous label lies in the I-lane or V-lane, and at least one lane occupies a fixed fraction of the final core.

Therefore material recruitment, pruning, polarity change, shell import, etc. cannot constitute a third top-level causal mechanism. They are refinements of how I or V is realized.

This is the main top-level exhaustiveness result.

---

## 4. Exact affine/residual partition preserves exhaustiveness inside the I-lane

On a self-consistent Gaussian window,

\[
\nabla U=L+\nabla r,
\]

with

\[
\int\gamma r=0,
\qquad
\int\gamma\nabla r=0.
\]

The terminal vorticity admits the exact affine Duhamel decomposition

\[
\Omega(T)
=F(T,t_0)\bar\Omega(t_0)
+\int_{t_0}^{T}F(T,s)J(s)ds.
\]

Thus the lower-order I-lane is divided into

\[
\boxed{\text{affine inheritance/amplification}}
\]

and

\[
\boxed{\text{non-affine residual source}}.
\]

No third affine/residual term is discarded.

The residual state cost

\[
B=\operatorname{Var}_\gamma(S)
+\frac12\operatorname{Var}_\gamma(\Omega)
\]

is likewise exact.

---

## 5. Threshold complements that are genuinely exhaustive

The later analysis repeatedly uses partitions of the form

- bounded Gaussian condition number / covariance anisotropy;
- spatially tight / non-tight;
- low/compact/high frequency;
- low-Hermite / high-Hermite;
- small/critical/large residual action;
- aligned near-minimal affine amplification / direction or shape defect;
- `lambda_2>0` / `lambda_2<=0`;
- local Betchov mismatch / cubic residual-shape breakdown.

Provided that the complement is retained as an explicit charged branch, each such threshold split preserves the top-level I/V exhaustiveness.

The important audit rule is:

> A branch may be called **closed as independent** only when its complement is retained elsewhere. A conditional theorem on a bounded-affine, bounded-condition, tight, low-curvature track does not delete the complementary track.

---

## 6. Where the present coherent fixed point is genuinely conditional

The dynamic Reynolds-one crossing construction used in the coherent endgame assumes a surviving bounded-condition residual pulse with

\[
m=W^{-1/3}\Lambda\to0.
\]

Then the responsible source time has

\[
\tau_m\asymp m^{-1}\to\infty,
\]

and the first Reynolds crossing satisfies

\[
BR^4=1,
\qquad
R\to\infty.
\]

This is the entry point to the coherent crossing, stochastic-flux, fast-rotation, and critical affine-residual fixed-point analysis.

However first hitting plus bounded-condition BMO control gives only an order-one ceiling on Gaussian gradient oscillation. It does **not** force every surviving sequence to have `m -> 0`.

After passing to a subsequence, the bounded-condition branch therefore has an exhaustive asymptotic split

\[
\boxed{
\text{A. }m_j\to0
}
\]

or

\[
\boxed{
\text{B. }m_j\ge m_0>0.
}
\]

### Lane A: coherent large-radius lane

This is the currently developed route:

\[
m_j\to0
\Longrightarrow
R_j\to\infty
\Longrightarrow
\text{coherent Reynolds crossing}
\Longrightarrow
\text{critical affine-residual / exterior-compensation wall}.
\]

### Lane B: compact/natural-scale non-affine lane

If

\[
m_j\ge m_0>0,
\]

then the residual source can remain order one on an `O(1)` terminal-normalized spatial/time scale. There is no automatic `R -> infinity` coherence gain.

This lane is already typed by

- order-one Gaussian non-affinity;
- scale-local Gaussian band energy or palinstrophy via the pointwise-to-band bridge;
- compactness/ancient-solution alternatives under adaptive first hitting;
- fixed physical frequency non-reuse, forcing the active physical frequency to move to infinity.

But it has **not** been reduced to the same coherent affine fixed point.

Therefore the statement

> every hypothetical singularity must realize the `R -> infinity` coherent fixed point

is currently too strong.

---

## 7. Universal clean-to-crossing productive-strain action does not require `R -> infinity`

The clean deep checkpoint can be chosen with `beta=2`:

\[
W_{\rm deep}=R^2,
\qquad
q=\frac{W}{R^2}.
\]

On every coherent crossing for which the finite-energy radius ceiling guarantees `R^2 << W`, the clean minimum satisfies

\[
E_m\lesssim\frac{R^2}{\sqrt W},
\]

while the crossing core gives

\[
E_c\gtrsim R^3.
\]

Hence

\[
\boxed{
\frac{E_c}{E_m}
\gtrsim
R\sqrt W.
}
\]

The enstrophy/Betchov/Hölder optimization therefore yields

\[
\boxed{
\int_{t_m}^{t_c}
\|\lambda_2^+(t)\|_{L_x^3}^2dt
\gtrsim
c_\nu\log(R\sqrt W).
}
\]

When `R` is bounded below, this is at least

\[
\boxed{
\gtrsim c_\nu\log W.
}
\]

Thus a compact-radius coherent episode would be *more*, not less, expensive in the standard critical middle-strain ledger. This still is not a contradiction, because a singularity is allowed to make that critical norm diverge.

For a genuinely noncoherent compact residual episode, the local Gaussian band/palinstrophy ledger replaces the coherent-core lower bound.

---

## 8. Revised exhaustive final frontier

The globally honest final graph is therefore not a single coherent fixed point. It is

\[
\boxed{
\text{finite-time blow-up}
\Longrightarrow
\text{first-hitting cascade}
\Longrightarrow
\text{I/V lanes}
\Longrightarrow
\begin{cases}
\text{compact/non-affine moving-band cascade},\\
\text{large-radius coherent affine-residual cascade},\\
\text{explicit derivative/covariance/spatial concentration branch}.
\end{cases}
}
\]

The third line is not independent once the band and derivative ledgers are used; it feeds the first or second lane according to whether the active Gaussian scale remains bounded or diverges.

Both surviving lanes share one unavoidable feature:

\[
\boxed{
\text{their active physical frequency/scale cannot remain fixed as }t\uparrow T^*.
}
\]

A fixed finite physical frequency contributes vanishing action on shrinking singular-tail intervals. Therefore every survivor must continually repopulate progressively higher physical bands.

Hence the genuinely common final wall is more accurately stated as

\[
\boxed{
\textbf{cross-time moving-band repopulation}
}
\]

rather than the coherent affine fixed point alone.

The coherent fixed point supplies much stronger geometry inside one sublane, especially local Betchov compensation and Gaussian mean-termination costs. The compact non-affine lane supplies less geometry and is therefore the branch that must not be omitted in a global proof.

---

## 9. What must be shown before claiming global regularity

A complete proof still needs both:

1. **moving-band nonrepeatability:** rule out the compact/non-affine scale-local cascade or show that it necessarily enters a known regularity-controlling contradiction;
2. **coherent compensation nonrepeatability:** rule out the `R -> infinity` critical affine-residual/Betchov compensation cascade.

A single theorem strong enough to control cross-time repopulation of moving scale-local bands could potentially close both at once.

Only after those lanes are closed may the exact I/V partition be invoked backward to conclude that no finite-time amplification cascade exists, and then standard continuation gives `T*=infinity`.

---

## 10. Audit conclusion

The current work **does** have an exhaustive top-level causal partition: the exact I/V amplification identity leaves no third way for a dangerous final label to acquire vorticity amplification.

But the current `R -> infinity` coherent fixed-point picture is **not yet exhaustive as a final asymptotic shape**. The compact/natural-scale non-affine lane must remain explicitly in the proof graph.

This correction is favorable for rigor: it separates

\[
\boxed{\text{what has really been excluded}}
\]

from

\[
\boxed{\text{what has merely been pushed outside the minimal coherent track}}.
\]

Overall status: **TOP-LEVEL EXHAUSTIVENESS SECURED BY EXACT I/V / FINAL-SHAPE EXHAUSTIVENESS REVISED TO TWO SURVIVING MOVING-BAND LANES / GLOBAL REGULARITY NOT PROVED.**