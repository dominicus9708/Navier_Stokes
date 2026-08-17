# Frontier: exhaustive moving-band / scale-mixing commutator wall

Date: 2026-08-17

Overall status: **THE GLOBAL LOGIC HAS BEEN AUDITED AND CORRECTED. THE EXACT FIRST-HITTING I/V AMPLIFICATION SPLIT IS TOP-LEVEL EXHAUSTIVE, BUT THE `R -> infinity` COHERENT AFFINE-RESIDUAL FIXED POINT IS ONLY ONE OF TWO FINAL ASYMPTOTIC LANES. A COMPACT/NATURAL-SCALE NON-AFFINE LANE MUST ALSO REMAIN. BOTH LANES ARE NOW UNIFIED BY AN EXACT POSITIVE HEAT-BAND ENSTROPHY EVOLUTION. EVERY DANGEROUS MOVING BAND MUST EITHER PERSIST, BE REPOPULATED BY DIRECT SCALE-CRITICAL STRETCHING, OR BE REPOPULATED BY SCALE-MIXING COMMUTATORS. THE LAST GENUINELY SCALE-TRANSFER-SPECIFIC WALL IS REPEATED POSITIVE COMMUTATOR TRANSFER ON MOVING PHYSICAL BANDS. GLOBAL REGULARITY NOT PROVED.**

---

## 1. Exhaustive top-level gate

Assume for contradiction a finite maximal smooth time `T*`. Standard continuation theory supplies an unbounded vorticity first-hitting sequence

\[
W_j=\|\omega(t_j)\|_\infty\to\infty.
\]

At each amplification step, pull the actual final dangerous labels back to the earlier checkpoint. The exact Cauchy defect formula is

\[
\omega(T)=I+V.
\]

Hence every dangerous label satisfies

\[
\boxed{
|I|\ge\frac12|\omega(T)|
\quad\lor\quad
|V|\ge\frac12|\omega(T)|.
}
\]

Therefore the proof has an exact top-level causal partition:

\[
\boxed{
\text{I: material/deformation amplification}
\quad\lor\quad
\text{V: viscous derivative rewriting}.
}
\]

No material genealogy or DSD interpretation is needed for this exhaustiveness statement.

---

## 2. Correction to the previous single-fixed-point wording

The coherent critical fixed-point analysis assumes a surviving bounded-condition residual pulse with

\[
m_j\to0.
\]

Then the responsible Gaussian scale diverges and one obtains the large-radius Reynolds crossing

\[
R_j\to\infty,
\qquad
B_jR_j^4=1,
\]

followed by coherence, stochastic ancestry, affine-residual pinning, and local Betchov compensation.

However the first-hitting cap plus bounded-condition BMO control does not force `m_j -> 0` on every subsequence. The exhaustive asymptotic split is

\[
\boxed{m_j\to0}
\]

or

\[
\boxed{m_j\ge m_0>0.}
\]

The second case is a compact/natural-scale non-affine critical lane. It is not outside the exact I/V tree, but it is outside the large-`R` coherent fixed-point geometry.

Therefore the previous phrase

> `the single final wall is the coherent affine-residual fixed point`

is replaced by

> `the common final wall is moving physical-band repopulation; the coherent affine-residual fixed point is the geometrically richer large-R sublane.`

---

## 3. Common moving physical scale

Both surviving lanes have physical active scales tending to zero.

### Compact lane

\[
\ell_j\asymp W_j^{-1/2}.
\]

### Coherent large-R lane

\[
\ell_j\asymp\frac{R_j}{\sqrt{W_j}},
\]

or the logarithmically enlarged compensation scale

\[
\ell_{j,\log}
\asymp
\frac{R_j\sqrt{\log R_j}}{\sqrt{W_j}}.
\]

Finite kinetic-energy radius ceilings imply these physical scales still tend to zero.

Hence in every surviving blow-up lane the active physical frequency tends to infinity.

---

## 4. Exact positive heat-band partition

Let

\[
H_a=e^{a\Delta},
\qquad
 a_k=4^{-k}a_0,
\]

and

\[
Q_k=H_{a_k}-H_{a_{k-1}}\ge0.
\]

Then

\[
\sum_kQ_k=I.
\]

Define

\[
E_k=\langle\omega,Q_k\omega\rangle,
\qquad
D_k=\langle\nabla\omega,Q_k\nabla\omega\rangle.
\]

Then

\[
\boxed{\sum_kE_k=E,\qquad\sum_kD_k=P.}
\]

The exact vorticity equation gives

\[
\boxed{
\frac12E_k'+\nu D_k=\Pi_k,
}
\]

with

\[
\Pi_k
=
\frac12\langle[(u\cdot\nabla),Q_k]\omega,\omega\rangle
+\langle(\omega\cdot\nabla)u,Q_k\omega\rangle.
\]

Moreover

\[
\boxed{\sum_k\Pi_k=Q}
\]

and the global enstrophy identity is recovered exactly.

---

## 5. Persistence versus repopulation

If a moving dangerous band is already above half of its required threshold on a long interval, it pays

\[
\boxed{
\int_I E_kdt
\ge\frac12b_k|I|,
}
\]

which is part of the physical dissipation ledger.

Otherwise choose the last half-threshold time and first full-threshold time:

\[
E_k(t_1)=b_k/2,
\qquad
E_k(t_2)=b_k.
\]

Then

\[
\boxed{
\int_{t_1}^{t_2}\Pi_kdt
=\frac14b_k+\nu\int_{t_1}^{t_2}D_kdt
\ge\frac14b_k.
}
\]

Therefore the scale cannot become dangerous merely because the DSD/Gaussian observation scale moved. The actual PDE must positively repopulate it.

---

## 6. Exact nonlinear split inside a repopulating band

Let

\[
P_k=Q_k^{1/2},
\qquad
\eta_k=P_k\omega.
\]

Then

\[
\boxed{
\Pi_k=\mathcal L_k+\mathcal C_k,
}
\]

where

\[
\boxed{
\mathcal L_k=\langle S\eta_k,\eta_k\rangle
}
\]

is direct stretching of the band vorticity and

\[
\boxed{
\mathcal C_k
=
\left\langle
[u\cdot\nabla,P_k]\omega+[P_k,S]\omega,
\eta_k
\right\rangle
}
\]

is scale-mixing commutator transfer.

Thus a half-to-full repopulation interval satisfies at least one of

\[
\boxed{
\int_I\mathcal L_kdt
\ge
\frac12\left(\frac b4+\nu\int_ID_kdt\right)
}
\]

or

\[
\boxed{
\int_I\mathcal C_kdt
\ge
\frac12\left(\frac b4+\nu\int_ID_kdt\right).
}
\]

---

## 7. Direct stretching costs a fixed critical action

Since

\[
|\mathcal L_k|
\le
\|S\|_3E_k^{1/2}D_k^{1/2},
\]

and `E_k<=b` during a first repopulation interval, the direct lane gives

\[
\frac b8+\frac\nu2X
\lesssim
b^{1/2}
\left(\int_I\|S\|_3^2dt\right)^{1/2}
X^{1/2},
\]

where

\[
X=\int_ID_kdt.
\]

Optimizing over `X` yields

\[
\boxed{
\int_I\|S(t)\|_{L_x^3}^2dt
\gtrsim c\nu.
}
\]

This bound is independent of the physical band index and threshold amplitude.

Thus a direct-stretch repopulation is exactly a scale-critical strain event. Infinite direct repopulations are compatible with a singularity only through divergence of a standard critical norm; they are not a hidden low-cost mechanism.

---

## 8. The only specifically cross-scale lane left

The commutator term is

\[
\mathcal C_k
=
\langle[u\cdot\nabla,P_k]\omega,\eta_k\rangle
+
\langle[P_k,S]\omega,\eta_k\rangle.
\]

It vanishes for perfectly scale-constant coefficients and measures

- velocity increments across the active scale;
- strain/eigenframe variation across the active scale;
- neighboring/distant-band import;
- non-affine residual structure;
- derivative/modulation growth.

On the coherent large-R lane, rigid skew rotation commutes with radial heat/Gaussian scales and therefore cannot supply this commutator. Symmetric affine deformation is already charged by the direct strain/affine ledger.

Hence the last genuinely scale-transfer-specific possibility is

\[
\boxed{
\textbf{repeated positive scale-mixing commutator transfer on bands whose physical frequency tends to infinity.}
}
\]

---

## 9. Relation to previous DSD branches

The old branches now fit into the exhaustive band graph as follows.

- high-Hermite/high-curvature -> commutator/derivative transfer;
- spatial non-tightness -> commutator/scale transport or material deformation;
- Gaussian residual source -> band-local non-affinity, hence direct or commutator repopulation;
- affine strain -> direct critical stretching;
- positive-middle strain -> direct productive critical action;
- Betchov exterior compensation -> local buffer band, then persistence/direct/commutator repopulation;
- Gaussian mean termination -> a positive band that must persist or have been repopulated earlier.

Thus DSD remains an audit/refinement layer while the final dynamic statement is an exact scale-resolved Navier--Stokes balance.

---

## 10. Current proof obligations

A global proof must still exclude both ways of making the moving-band cascade singular:

1. infinitely many direct critical stretching events;
2. infinitely many positive commutator-transfer events.

The first is already expressed in a known critical regularity norm and is therefore not by itself contradictory.

The second is the sharper remaining target. A useful next theorem would be a vector-valued commutator packing estimate of the form

\[
\boxed{
\sum_{\text{active }k}
\mathcal C_k^+
\lesssim
\text{critical strain production}
+\text{one-higher-derivative scale-local cost},
}
\]

with a space-time organization strong enough to prevent infinite low-cost repopulation.

Only after both lanes are ruled out can the exact I/V partition be propagated backward to conclude that no finite-time first-hitting cascade exists, after which standard continuation yields global regularity.

Overall status: **TOP-LEVEL BRANCH EXHAUSTIVENESS AUDITED / SINGLE COHERENT-FIXED-POINT OVERCLAIM CORRECTED / COMPACT AND COHERENT LANES UNIFIED BY EXACT HEAT-BAND DYNAMICS / FINAL SCALE-SPECIFIC WALL = MOVING-BAND COMMUTATOR TRANSFER / GLOBAL REGULARITY NOT PROVED.**