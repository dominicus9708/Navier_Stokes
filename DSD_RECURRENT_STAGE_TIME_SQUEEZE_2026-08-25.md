# DSD Recurrent Stage-Time Squeeze

Date: 2026-08-25

Status: **TAIL-INDEPENDENT STAGE-TIME LOWER BOUND DERIVED / q=2 OPTIMUM DERIVED / DIRECT COMPARISON WITH MOVING-VARIANCE CEILING DERIVED / GLOBAL REGULARITY NOT PROVED.**

## 1. Recurrent enstrophy balance

For the recurrent Leray vorticity state,

\[
\frac14\overline Z+
u\overline Q
=
\overline{\mathcal P},
\]

where

\[
Z=\|W\|_2^2,
\qquad
Q=\|\nabla W\|_2^2.
\]

The sharp trace-free stretching estimate is

\[
\mathcal P
\le
\frac1{\sqrt3}MZ,
\qquad
M=\|W\|_\infty.
\]

The continuous first-hitting Type-I inheritance gives

\[
M(s)\le K_I.
\]

Therefore

\[
\frac14\overline Z+
u\overline Q
\le
\frac{K_I}{\sqrt3}\overline Z.
\]

Since the recurrent state is nonzero,

\[
\overline Z>0.
\]

Define

\[
\bar\lambda:=\frac{\overline Q}{\overline Z}.
\]

Then every recurrent survivor satisfies

\[
\boxed{
K_I
\ge
\frac{\sqrt3}{4}
+\sqrt3\nu\bar\lambda.
}
\]

Using the active-core frequency floor,

\[
\bar\lambda\ge c_{\log},
\]

we obtain

\[
\boxed{
K_I
\ge
\frac{\sqrt3}{4}
+\sqrt3\nu c_{\log}.
}
\]

This bound is independent of the velocity `L3` tail.

---

## 2. Convert to first-hitting stage length

The first-hitting inheritance gives

\[
K_I
=
\frac{q^2}{q-1}L_+.
\]

Hence every recurrent survivor must satisfy

\[
\boxed{
L_+
\ge
\frac{q-1}{q^2}
\left(
\frac{\sqrt3}{4}
+\sqrt3\nu c_{\log}
\right).
}
\]

In particular, even if the frequency tax is discarded,

\[
\boxed{
L_+
\ge
\frac{\sqrt3}{4}
\frac{q-1}{q^2}.
}
\]

Thus recurrence requires a nonzero minimum amount of normalized first-hitting time per generation.

---

## 3. Optimal geometric ratio

Define

\[
f(q):=\frac{q-1}{q^2},
\qquad q>1.
\]

Then

\[
f'(q)=\frac{2-q}{q^3}.
\]

Therefore the strongest universal stage-time lower bound occurs at

\[
\boxed{q=2.}
\]

At `q=2`,

\[
\boxed{
L_+
\ge
\frac{\sqrt3}{16}
+\frac{\sqrt3}{4}\nu c_{\log}.
}
\]

Numerically,

\[
\boxed{
\frac{\sqrt3}{16}
\approx0.10825317547.
}
\]

Thus any `q=2` recurrent survivor must have normalized stage ceiling at least `0.108253...` even before the positive palinstrophy-frequency tax is inserted.

---

## 4. Insert the active-core lower bound

The active-core invariant-measure calculation gives

\[
c_{\log}
=
\frac{3^{5/3}\pi^{2/3}}{2^{8/3}}
\frac{d_*z_*}{R_*^2Z_+}.
\]

Hence at `q=2`,

\[
\boxed{
L_+
\ge
\frac{\sqrt3}{16}
+
\frac{\sqrt3}{4}
\nu
\frac{3^{5/3}\pi^{2/3}}{2^{8/3}}
\frac{d_*z_*}{R_*^2Z_+}.
}
\]

The first term is universal; the second is the recurrent active-core viscous surcharge.

---

## 5. Compare with the moving-variance ceiling

On the persistent low-turnover moving-core corridor,

\[
L_+
\le
\Pi_V\frac{R_V^2}{\nu}.
\]

Combining with the recurrent lower bound gives the necessary condition

\[
\boxed{
\Pi_V\frac{R_V^2}{\nu}
\ge
\frac{q-1}{q^2}
\left(
\frac{\sqrt3}{4}
+\sqrt3\nu c_{\log}
\right).
}
\]

For the optimal `q=2` choice,

\[
\boxed{
\Pi_V\frac{R_V^2}{\nu}
\ge
\frac{\sqrt3}{16}
+
\frac{\sqrt3}{4}\nu c_{\log}.
}
\]

Therefore the recurrent bounded-`Z` branch is S-closed whenever

\[
\boxed{
\Pi_V\frac{R_V^2}{\nu}
<
\frac{\sqrt3}{16}
+
\frac{\sqrt3}{4}\nu c_{\log}.
}
\]

A still simpler sufficient condition is

\[
\boxed{
\Pi_V\frac{R_V^2}{\nu}
<
\frac{\sqrt3}{16}.
}
\]

This version requires no quantitative knowledge of `Z_+`.

---

## 6. Interpretation of failure

If the stage ceiling cannot beat the recurrent lower bound, then at least one of the quantities hidden in the moving-variance ceiling must remain sufficiently large:

\[
\Pi_V
=
\frac{C_{var}}
{(1-\eta)V_-}
\left[
\frac14(\log q)V_+
+F_0
+\frac12\kappa_V
\right],
\]

or `R_V` itself must be sufficiently large.

Therefore failure of the simple stage squeeze is not untyped. It means one or more of

\[
\boxed{
\text{large moving-core radius}
\lor
\text{weak variance persistence}
\lor
\text{large shell/material flux}
\lor
\text{large endpoint reshaping}.
}
\]

These are precisely the existing `T`/spreading channels.

---

## 7. Relation to the Betchov frequency window

The stage-time squeeze is weaker than the full Young-free Betchov frequency window because it uses only the universal trace-free production ceiling.

Its advantage is that the baseline

\[
\frac{\sqrt3}{16}
\]

at `q=2` is independent of `Z_+`.

Thus the proof program can be organized in the following order:

1. attempt to beat the universal stage floor using the moving-variance ceiling;
2. if that fails only narrowly, insert the positive `c_log` surcharge;
3. if it still fails, use the sharper Betchov quartic frequency window;
4. if all fail, the surviving obstruction is quantitatively large turnover/spreading or large bounded enstrophy.

---

## 8. DSD audit

The comparison uses only finite formed channels:

- first-hitting ratio `q`;
- normalized stage length `L_+`;
- recurrent mean enstrophy and palinstrophy;
- moving-core radius `R_V`;
- persistence/turnover factor `Pi_V`.

No infinite derivative hierarchy or global tail object is needed.

---

## 9. Updated frontier

The highest-leverage quantitative test that is independent of `Z_+` is now

\[
\boxed{
\Pi_V R_V^2/\nu
\stackrel? <
\sqrt3/16
\qquad(q=2).
}
\]

If this strict inequality can be proved on the intended no-turnover corridor, the bounded-`Z` recurrent branch closes before any detailed critical-tail or Betchov analysis is needed.

If it cannot, the amount by which it fails is a direct quantitative measure of the residual turnover/spreading that must be routed to `T`.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
