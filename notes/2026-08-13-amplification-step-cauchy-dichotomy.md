# Amplification-step Cauchy dichotomy: deformation versus viscous defect without overlap assumptions

Date: 2026-08-13

Status: **DERIVED AMPLIFICATION-STEP DICHOTOMY / OPEN REPEATED CRITICAL-COST CLOSURE**.

This note supersedes the idea that material turnover and material pruning must first be separated before a Cauchy-defect cost can be obtained.  For a sufficiently large vorticity amplification step, one may pull the *final* dangerous core back to the earlier time.  The earlier global maximum then bounds every pulled-back label, regardless of whether that label belonged to the earlier dangerous core.

No inter-window overlap hypothesis is needed for this estimate.

---

## 1. Amplification checkpoint

Let

\[
W_0=\|\omega(t_0)\|_{L^\infty},
\qquad
W_1=\|\omega(t_1)\|_{L^\infty}=qW_0,
\qquad q>1.
\]

Let the final dangerous core satisfy

\[
C_1\subset\{x:|\omega(x,t_1)|\ge bW_1\},
\qquad 0<b<1.
\]

For a natural-scale thick core assume

\[
|C_1|\ge \theta r_1^3,
\qquad
r_1=aW_1^{-1/2},
\]

so

\[
\boxed{
|C_1|\ge \theta a^3q^{-3/2}W_0^{-3/2}.
}
\]

Pull the final core back to time `t0`:

\[
A_0=X^{-1}(C_1,t_1;t_0).
\]

Incompressibility gives

\[
|A_0|=|C_1|.
\]

Crucially, whether `A0` overlaps an earlier threshold core is irrelevant.  By definition of the earlier global maximum,

\[
\boxed{
|\omega(a,t_0)|\le W_0
\qquad(a\in A_0).
}
\]

---

## 2. Cauchy variable

Restart the flow map at `t0` and write

\[
F=D_aX,
\qquad
\zeta=F^{-1}\omega(X,t).
\]

Then

\[
\boxed{
\partial_t\zeta
=\nu F^{-1}\Delta\omega(X,t).
}
\]

At the restart time,

\[
\zeta(a,t_0)=\omega(a,t_0).
\]

Define the recent deformation bounds on the pulled-back final core:

\[
K_+=\sup_{A_0\times[t_0,t_1]}\|F\|_{\rm op},
\qquad
K_-=\sup_{A_0\times[t_0,t_1]}\|F^{-1}\|_{\rm op}.
\]

---

## 3. Final-core lower bound on the Cauchy variable

For every `a in A0`,

\[
|\omega(X(a,t_1),t_1)|\ge bqW_0.
\]

Since

\[
\omega(X,t_1)=F(a,t_1)\zeta(a,t_1),
\]

we have

\[
|\zeta(a,t_1)|
\ge
\frac{bq}{K_+}W_0.
\]

At `t0`,

\[
|\zeta(a,t_0)|\le W_0.
\]

Therefore whenever

\[
\boxed{
\delta_q:=\frac{bq}{K_+}-1>0,
}
\]

every label in the pulled-back final core obeys

\[
\boxed{
|\zeta(a,t_1)-\zeta(a,t_0)|
\ge
\delta_qW_0.
}
\]

This is the key point: **all final dangerous labels pay the defect**, not merely newly recruited labels.

---

## 4. Integrated `k=2` cost

The exact Cauchy identity and Cauchy--Schwarz in time give

\[
\|\zeta(t_1)-\zeta(t_0)\|_{L^2(A_0)}^2
\le
\nu^2K_-^2\tau
\int_{t_0}^{t_1}\int_{X(A_0,t)}
|\Delta\omega|^2dxdt,
\]

where

\[
\tau=t_1-t_0.
\]

The lower bound above gives

\[
\delta_q^2W_0^2|A_0|
\le
\nu^2K_-^2\tau
\int_I\int_{X(A_0,t)}|\Delta\omega|^2.
\]

Hence

\[
\boxed{
\int_I\int_{X(A_0,t)}|\Delta\omega|^2dxdt
\ge
\frac{
\theta a^3 q^{-3/2}\delta_q^2
}{
\nu^2K_-^2\tau
}
W_0^{1/2}.
}
\]

Introduce the dimensionless duration

\[
\sigma=W_0\tau.
\]

Then

\[
\boxed{
\int_I\int_{X(A_0,t)}|\Delta\omega|^2
\ge
\frac{
\theta a^3 q^{-3/2}
}{
\nu^2K_-^2\sigma
}
\left(\frac{bq}{K_+}-1\right)^2
W_0^{3/2}.
}
\]

For `q` large compared with `K_+/b`, the coefficient behaves like

\[
q^{-3/2}\left(\frac{bq}{K_+}-1\right)^2
\sim
\frac{b^2}{K_+^2}q^{1/2}.
\]

Thus a larger amplification jump strengthens the viscous-defect alternative unless recent deformation grows proportionally with the jump.

---

## 5. Unified dichotomy

Choose a fixed fraction `0<kappa<b` and split by

\[
K_+\ge \kappa q
\]

or

\[
K_+<\kappa q.
\]

### A. Deformation branch

If

\[
\boxed{K_+\ge\kappa q,}
\]

then the recent flow map itself has produced order-`q` stretching on the labels ending in the dangerous core.

This returns to the strain/Lagrangian-deformation chain.

### B. Viscous Cauchy-defect branch

If

\[
K_+<\kappa q
\]

with `kappa<b`, then

\[
\delta_q
>\frac b\kappa-1>0
\]

uniformly in `q`, and the entire final natural core pays a scale-critical `k=2` defect cost.

Therefore

\[
\boxed{
\text{large amplification step}
\Longrightarrow
\text{large recent deformation}
\quad\text{or}\quad
\text{critical viscous Cauchy defect}.
}
\]

No turnover/pruning/overlap classification is required before this dichotomy is applied.

---

## 6. What becomes secondary

The previous material labels remain useful, but their role changes.

- `turnover`: describes *which* labels form the final core;
- `pruning`: describes nested selection of old labels;
- `overlap`: describes continuity of the instantaneous threshold core;
- `amplification dichotomy`: charges **every final dangerous label** to deformation or viscous Cauchy defect.

Thus overlap is now a secondary geometric diagnostic rather than the principal bridge needed to obtain a cost.

This is a substantial simplification of the material branch.

---

## 7. Scaling wall remains

The estimate is still scale-critical.  If

\[
\sigma=O(1),
\qquad
K_\pm=O(1),
\qquad
q=O(1),
\]

then

\[
\int_I\|\Delta\omega\|_2^2dt
\gtrsim W_0^{3/2},
\]

which is exactly the natural `k=2` derivative scaling already identified in the turnover calculation.

Therefore the dichotomy eliminates a combinatorial/material-classification obstacle but does **not** by itself cross the Navier--Stokes criticality barrier.

---

## 8. New principal target

The material part of the proof route can now be organized by amplification checkpoints rather than by all intermediate threshold-core identities:

\[
\boxed{
W_j\to W_{j+1}=qW_j.
}
\]

At each checkpoint, the final dangerous core must choose one of two channels:

\[
\boxed{
\textbf{D-channel: }K_{+,j}\gtrsim q,
}
\]

or

\[
\boxed{
\textbf{V2-channel: }
\int_{I_j}\|\Delta\omega\|_2^2
\gtrsim
W_j^{3/2}
\times\text{dimensionless coefficient}.
}
\]

A proof-producing closure would show that an infinite amplification chain cannot keep choosing D and V2 channels while simultaneously satisfying the previously derived projective/coherence/sparseness and finite-energy constraints.

Status: **OPEN D/V2 AMPLIFICATION-CHAIN CLOSURE**.
