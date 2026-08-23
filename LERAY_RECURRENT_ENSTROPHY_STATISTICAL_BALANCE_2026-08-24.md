# Leray Recurrent Enstrophy Statistical Balance — 2026-08-24

Status: **EXACT LONG-TIME BALANCE + NECESSARY RECURRENT-ORBIT THRESHOLDS / GLOBAL REGULARITY NOT PROVED.**

This note applies directly to both periodic and aperiodic recurrent Leray survivors.

## 1. Leray vorticity equation

For

\[
V_s+\frac12V+\frac12Y\cdot\nabla V+(V\cdot\nabla)V+\nabla\Pi=\nu\Delta V,
\]

let

\[
W=\nabla\times V,
\qquad
S=\frac12(\nabla V+\nabla V^T).
\]

Then

\[
\boxed{
W_s+W+\frac12Y\cdot\nabla W+V\cdot\nabla W
=SW+\nu\Delta W.
}
\]

Set

\[
Z(s)=\|W(s)\|_2^2,
\qquad
Q(s)=\|\nabla W(s)\|_2^2,
\]

and

\[
\mathcal P(s)=\int W^TSW\,dY.
\]

Because `div V=0`, integration gives the exact global identity

\[
\boxed{
\frac12Z'(s)+\frac14Z(s)+\nu Q(s)=\mathcal P(s).
}
\]

The coefficient `1/4` is the exact Leray dilation contribution in three dimensions.

## 2. Long-time recurrent statistical balance

The restricted ancient route gives a uniform enstrophy bound

\[
0\le Z(s)\le Z_+<\infty.
\]

Integrate over `[-S,0]` and divide by `S`:

\[
\frac{Z(0)-Z(-S)}{2S}
+\frac14\langle Z\rangle_S
+\nu\langle Q\rangle_S
=\langle\mathcal P\rangle_S,
\]

where

\[
\langle f\rangle_S=\frac1S\int_{-S}^0f(s)ds.
\]

Along every subsequence on which the long-time averages converge, the endpoint term vanishes, giving

\[
\boxed{
\frac14\overline Z+\nu\overline Q=\overline{\mathcal P}.
}
\]

The positive-density active-core windows derived in `LERAY_ACTIVE_CORE_INVARIANT_MEASURE_2026-08-24.md` imply

\[
\boxed{
\overline Z>0.
}
\]

Hence every nonzero recurrent statistical state must sustain positive mean vortex stretching.

## 3. Universal stretching ceiling

For divergence-free decaying fields,

\[
\|S\|_2^2=\frac12\|W\|_2^2=\frac12Z.
\]

Let

\[
M(s)=\|W(s)\|_\infty.
\]

Interpolation gives

\[
\|W\|_4^2
\le
\|W\|_\infty\|W\|_2
=MZ^{1/2}.
\]

Therefore

\[
\begin{aligned}
|\mathcal P|
&\le \|S\|_2\|W\otimes W\|_2\\
&=\|S\|_2\|W\|_4^2\\
&\le\frac1{\sqrt2}MZ.
\end{aligned}
\]

Thus

\[
\boxed{
\frac14\overline Z+\nu\overline Q
\le
\frac1{\sqrt2}\overline{MZ}.
}
\]

Equivalently,

\[
\boxed{
\frac{\overline{MZ}}{\overline Z}
\ge
\frac{\sqrt2}{4}
+\sqrt2\nu\frac{\overline Q}{\overline Z}.
}
\]

The universal baseline is

\[
\boxed{\frac{\sqrt2}{4}=0.3535533906\ldots}
\]

before any palinstrophy tax is inserted.

Hence a recurrent nonzero Leray orbit cannot stay entirely in the low-vorticity-amplitude region

\[
M<\sqrt2/4.
\]

More strongly, it must exceed the baseline by an amount determined by its average frequency `Q/Z`.

## 4. Active-core concentration creates a positive average palinstrophy floor

Suppose on the active windows of lower time density `d_*>0`, a fixed ball `B_R` contains enstrophy at least

\[
\int_{B_R}|W|^2dY\ge z_*>0.
\]

Sobolev gives

\[
\|W\|_6^2\le S_3^{-1}Q,
\qquad
S_3=3(\pi/2)^{4/3}.
\]

By Hölder on `B_R`,

\[
z_*
\le |B_R|^{2/3}\|W\|_6^2
\le |B_R|^{2/3}S_3^{-1}Q.
\]

Therefore on every active window,

\[
\boxed{
Q\ge
S_3|B_R|^{-2/3}z_*
=:\kappa_Q(R)z_*.
}
\]

Averaging yields

\[
\boxed{
\overline Q
\ge d_*\kappa_Q(R)z_*>0.
}
\]

Thus the recurrent core pays a strictly positive mean palinstrophy tax even if the remote critical tail is dynamically passive.

## 5. Explicit recurrent-amplitude necessary condition

Since `Z<=Z_+`,

\[
\frac{\overline Q}{\overline Z}
\ge
\frac{d_*\kappa_Q(R)z_*}{Z_+}.
\]

Hence every recurrent survivor must satisfy

\[
\boxed{
\frac{\overline{MZ}}{\overline Z}
\ge
\frac{\sqrt2}{4}
+
\sqrt2\nu
\frac{d_*\kappa_Q(R)z_*}{Z_+}.
}
\]

In particular, if an independent first-hitting estimate supplies

\[
M(s)\le M_+
\]

and

\[
\boxed{
M_+
<
\frac{\sqrt2}{4}
+
\sqrt2\nu
\frac{d_*\kappa_Q(R)z_*}{Z_+},
}
\]

then the recurrent Leray branch is S-closed.

This is a symbolic closure certificate. No unsupported numerical value for the first-hitting constants is inserted here.

## 6. Relation to the projective/H1 route

The statistical balance does not distinguish how the stretching `P` is generated. The existing projective route does:

- coherent positive-middle stretching creates transverse deformation;
- anti-ribbon projective action creates a frequency tax;
- repeated projective action is inserted into the H1 ledger;
- turnover/residual failure leaves the pure recurrent lane.

The present identity supplies the complementary global statement:

\[
\boxed{
\text{every recurrent active core must continuously replenish}
\quad
\frac14Z+\nu Q
}
\]

on average.

Therefore any future projective depletion estimate only needs to show that the allowed recurrent geometry cannot produce this required mean amount.

## 7. Remaining gap

The identity is exact but not itself contradictory. A survivor may have sufficiently large mean vorticity amplitude and stretching to balance the dilation and viscous terms.

The remaining rigidity problem is therefore sharpened to:

\[
\boxed{
\text{can a bounded recurrent Leray orbit with passive critical tail sustain}
\quad
\overline{\mathcal P}=\frac14\overline Z+\nu\overline Q>0
\quad
\text{without entering the existing }P_V/T/H\text{ exits?}
}
\]

Status: **NONZERO RECURRENT LERAY DYNAMICS OBEY AN EXACT STATISTICAL ENSTROPHY BALANCE. THE ACTIVE CORE HAS POSITIVE MEAN PALINSTROPHY AND MUST MAINTAIN A VORTICITY-AMPLITUDE-WEIGHTED STRETCHING LEVEL STRICTLY ABOVE `sqrt(2)/4`, WITH AN ADDITIONAL EXPLICIT VISCOSITY/CONCENTRATION TAX. GLOBAL REGULARITY REMAINS UNPROVED.**