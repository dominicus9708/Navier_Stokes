# Smooth Temporal Record / Plateau Gate — 2026-08-20

Status: **S-LEVEL FINITE-STAGE TEMPORAL DECOMPOSITION. GLOBAL REGULARITY NOT PROVED.**

This note continues the smooth-only mainline. It determines when the cross-order production required by one geometric vorticity amplification stage must occur: during actual growth of the running vorticity record, or during plateaus of that record.

## 1. Cross-order excess

From `SMOOTH_FINITE_STAGE_TIGHTROPE_LEDGER_2026-08-20.md`, define

\[
\chi=\frac PE,
\]

\[
\mathcal G
=\frac HP-\frac PE\ge0,
\]

and

\[
\boxed{
\mathcal X
=\frac NP-\frac AE.
}
\]

On one finite stage `M_j -> q M_j`,

\[
\boxed{
\frac12\Delta\log\chi
+\frac12\log q
+\nu\int_{I_j}\mathcal G ds
=
\int_{I_j}\mathcal X ds.
}
\]

## 2. First exit: frequency collapse

Fix the explicit threshold

\[
\Delta\log\chi
<-rac12\log q.
\]

Then

\[
\boxed{
\chi_1<q^{-1/2}\chi_0.
}
\]

Repeated occurrence drives the normalized derivative frequency toward zero. On the pruned natural-core lane this is a loss of derivative-core persistence/tightness rather than a `P_V` equality regime.

Therefore the direct `P_V` mainline may restrict attention to stages satisfying

\[
\boxed{
\Delta\log\chi
\ge-rac12\log q.
}
\]

## 3. A fixed positive cross-order payment remains

On such a stage,

\[
\int_{I_j}\mathcal X ds
\ge
\frac14\log q
+\nu\int_{I_j}\mathcal G ds.
\]

Since

\[
\int\mathcal X_+\ge\int\mathcal X,
\]

we get

\[
\boxed{
\int_{I_j}\mathcal X_+ ds
\ge
\frac14\log q.
}
\]

Thus every non-frequency-collapsing smooth stage carries a fixed positive amount of cross-order production excess.

## 4. Split time into record growth and plateau

The running envelope `M(t)` is locally Lipschitz on every compact smooth interval, hence absolutely continuous. Define, up to null sets,

\[
R_j=\{s\in I_j:b(s)>0\},
\]

and

\[
F_j=\{s\in I_j:b(s)=0\}.
\]

Then

\[
I_j=R_j\cup F_j
\]

almost everywhere, and

\[
\int_{R_j}bds=\log q.
\]

The positive cross-order action splits as

\[
\int_{I_j}\mathcal X_+
=
\int_{R_j}\mathcal X_+
+
\int_{F_j}\mathcal X_+.
\]

Therefore at least one of the two alternatives holds:

\[
\boxed{
\int_{R_j}\mathcal X_+ds
\ge\frac18\log q
}
\]

or

\[
\boxed{
\int_{F_j}\mathcal X_+ds
\ge\frac18\log q.
}
\]

This is an exact finite-stage temporal gate.

## 5. Plateau branch

On `F_j`, `b=0`, so the differential tightrope identity reduces to

\[
\boxed{
\mathcal X
=
\frac12(\log\chi)_s
+\nu\mathcal G.
}
\]

Since `G>=0`,

\[
\mathcal X_+
\le
\frac12[(\log\chi)_s]_+
+\nu\mathcal G.
\]

Define the positive variation of normalized frequency on the plateau set by

\[
V_{+,F}(\log\chi)
=
\int_{F_j}[(\log\chi)_s]_+ds.
\]

Then

\[
\boxed{
\int_{F_j}\mathcal X_+ds
\le
\frac12V_{+,F}(\log\chi)
+
u\int_{F_j}\mathcal Gds.
}
\]

Hence if the plateau branch carries at least `1/8 log q`, then at least one of

\[
\boxed{
V_{+,F}(\log\chi)
\ge\frac18\log q
}
\]

or

\[
\boxed{
\nu\int_{F_j}\mathcal Gds
\ge\frac1{16}\log q
}
\]

must hold.

Interpretation:

- the first is an actual normalized derivative-frequency excursion while the vorticity record is not increasing;
- the second is a fixed hyperdissipative spectral-gap payment.

If repeated positive frequency excursions are later reset in order to keep `chi` bounded, the resets require negative cross-order action and therefore a genuine temporal oscillation/shape-reorganization process rather than a stationary `P_V` equality state.

## 6. Record-growth branch

If instead

\[
\boxed{
\int_{R_j}\mathcal X_+ds
\ge\frac18\log q,
}
\]

then a fixed amount of the cross-order payment occurs at times where the running vorticity record is actually increasing.

On the remaining positive-middle danger lane, the L2 determinant production satisfies `A>=0` during the corresponding typed sector. There,

\[
\mathcal X_+
=\left(\frac NP-\frac AE\right)_+
\le
\left(\frac NP\right)_+.
\]

Therefore record-time cross-order payment forces record-time H1 production:

\[
\boxed{
\int_{R_j}\left(\frac NP\right)_+ds
\ge\frac18\log q
}
\]

unless a determinant-sign/spectral-transition interval is entered.

This is exactly the temporal condition needed to invoke the smooth record-point and record-ball tradeoff.

## 7. Current finite-stage trichotomy

Every smooth geometric first-hitting stage now enters at least one of:

### T0 — normalized-frequency collapse

\[
\Delta\log\chi<-rac12\log q.
\]

### P0 — plateau production

The stage pays through positive normalized-frequency variation or the viscous spectral gap while `M` is constant.

### R0 — record-time production

A fixed H1/cross-order action occurs while `M` is actually increasing, so the record-point growth/H1 incompatibility and record-ball derivative-capacity estimates apply.

Thus the direct proof no longer has to assume that dangerous `P_V` production happens at the vorticity record time. The finite-stage ledger proves that if it does not, the plateau itself pays a separately typed frequency/hyperdissipation cost.

## 8. Next target

On the `R0` branch, combine the temporal lower bound with a spatial overlap fraction for the record ball.

- if the record ball contains only a small fraction of record-time H1 production, route to spatial derivative separation;
- if it contains a fixed fraction, use `SMOOTH_RECORD_BALL_DERIVATIVE_CAPACITY_2026-08-20.md` to force record slack/diffusion;
- if determinant production changes sign or the positive-middle spectrum exits, route to the already typed spectral-transition branch.

This remains a finite smooth calculation on every stage.

Status: **EVERY NON-FREQUENCY-COLLAPSING FIRST-HITTING STAGE MUST PAY A FIXED CROSS-ORDER ACTION EITHER DURING RECORD GROWTH OR DURING A PLATEAU. PLATEAU PAYMENT FORCES FREQUENCY EXCURSION/HYPERDISSIPATION; RECORD PAYMENT ACTIVATES THE RECORD-CORE TRADEOFF.**