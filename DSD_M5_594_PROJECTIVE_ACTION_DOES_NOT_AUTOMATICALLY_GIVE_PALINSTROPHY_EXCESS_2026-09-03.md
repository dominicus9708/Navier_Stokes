# DSD M5-594 — Projective action does not automatically give palinstrophy excess

Date: 2026-09-03

Status: **THE SAME-CARRIER PROJECTIVE ACTION FROM M5-593 IS NOT BY ITSELF A POSITIVE PALINSTROPHY EXCESS. WRITING `A=P_perp Sigma W`, `B=P_perp Delta W`, AND `C=A+B=rho D_B xi`, THE NET TRANSVERSE TERM AFTER MOVING STRETCHING PRODUCTION AGAINST LAPLACIAN DISSIPATION IS `B·C`, WHICH IS SIGN-INDEFINITE. HOWEVER, IF ITS MEAN IS NONPOSITIVE WHILE `|C|^2` HAS POSITIVE MEAN, THEN TRANSVERSE STRAIN MUST HAVE AT LEAST THE SAME L2 SIZE AS THE PROJECTIVE ACTION. THUS THE CP BRANCH SPLITS INTO A GENUINE UNPAID-EXCESS BRANCH OR A SAME-CARRIER TRANSVERSE-STRAIN-PAYER BRANCH. GLOBAL REGULARITY REMAINS UNPROVED.**

## 1. M5-593 notation

On the active production-paying carrier define

\[
A:=P_\xi^\perp\Sigma W,
\qquad
B:=P_\xi^\perp\Delta W,
\]

and

\[
\boxed{C:=A+B=\rho D_B\xi.}
\]

M5-593 Branch CP gives

\[
\boxed{
\left\langle
\mathbf 1_{\mathcal E_{pd}}
\int\chi_{pay}|C|^2dy
\right\rangle
=:c_C>0.
}
\]

## 2. Exact transverse terms in the palinstrophy pairing

M5-547 pairs the vorticity equation with \(-\Delta W\).

The Laplacian dissipation contains

\[
|B|^2.
\]

The stretching-diffusion cross term on the right side is

\[
-\Sigma W\cdot\Delta W,
\]

whose transverse contribution is

\[
-A\cdot B.
\]

Therefore after moving the transverse stretching production to the left side, the net transverse contribution is

\[
\boxed{
\mathcal R_\perp
:=
|B|^2+A\cdot B.
}
\]

Since \(C=A+B\),

\[
\boxed{
\mathcal R_\perp
=B\cdot C.
}
\]

Equivalently,

\[
\boxed{
\mathcal R_\perp
=
\frac12
\left(
|C|^2+|B|^2-|A|^2
\right).
}
\]

## 3. Positive projective action does not fix the sign

The condition

\[
|C|^2>0
\]

does not imply

\[
B\cdot C>0.
\]

For example, for any nonzero transverse vector \(v\), choose

\[
A=2v,
\qquad
B=-v.
\]

Then

\[
C=v,
\qquad
|C|^2=|v|^2>0,
\]

but

\[
\boxed{B\cdot C=-|v|^2<0.}
\]

Thus the candidate implication

\[
\text{projective action}
\Longrightarrow
\text{positive transverse palinstrophy excess}
\]

is false without an additional size/alignment estimate.

This shortcut is retired.

## 4. Event-averaged transverse remainder

Define

\[
\overline{R}_\perp
:=
\left\langle
\mathbf 1_{\mathcal E_{pd}}
\int\chi_{pay}B\cdot C\,dy
\right\rangle.
\]

Then there are two branches.

### CP-E: genuine unpaid transverse excess

\[
\boxed{\overline{R}_\perp>0.}
\]

This is a true same-carrier dissipative remainder that cannot be canceled by the particular transverse strain-diffusion cross term.

It remains to compare it against the other localized derivative-transfer terms, especially advection and cutoff commutators.

### CP-S: no positive transverse excess

\[
\boxed{\overline{R}_\perp\le0.}
\]

Then

\[
\left\langle
\int\chi_{pay} A\cdot C
\right\rangle
\ge
\left\langle
\int\chi_{pay}|C|^2
\right\rangle
=c_C.
\]

By Cauchy-Schwarz in spacetime,

\[
\left\langle
\int\chi_{pay}|A|^2
\right\rangle^{1/2}
\left\langle
\int\chi_{pay}|C|^2
\right\rangle^{1/2}
\ge c_C.
\]

Therefore

\[
\boxed{
\left\langle
\mathbf 1_{\mathcal E_{pd}}
\int\chi_{pay}|A|^2dy
\right\rangle
\ge c_C>0.
}
\]

Thus failure of an unpaid excess forces a positive same-carrier transverse-strain-square charge.

## 5. Interpretation of the strain-payer branch

Because

\[
A=\rho\tau,
\]

CP-S gives

\[
\boxed{
\left\langle
\mathbf 1_{\mathcal E_{pd}}
\int\chi_{pay}\rho^2|\tau|^2dy
\right\rangle>0.
}
\]

This is now localized in the same region and same event set as the positive axial production.

Hence CP-S contains simultaneous

1. axial strain production \(\rho^2\sigma\),
2. transverse strain action \(\rho^2|\tau|^2\), and
3. persistent noncollinear companion geometry.

M5-550's trace-free inequality therefore applies locally:

\[
|\Sigma|^2
\ge
\frac32\sigma^2+2|\tau|^2.
\]

This produces another quantitative local strain/enstrophy threshold, but not yet a contradiction.

## 6. Relation to exact anchoring

On the CE branch of M5-593,

\[
C=0,
\qquad B=-A.
\]

Then

\[
\mathcal R_\perp=B\cdot C=0,
\]

recovering exactly the M5-547 transverse recycling identity.

Thus M5-594 continuously interpolates between

\[
\text{exact anchoring }C=0
\]

and the genuinely projective case \(C\ne0\).

## 7. Updated hard-core split

The production-paying carrier now satisfies one of

\[
\boxed{
\begin{array}{ll}
\text{CE:}&C=0\quad\text{(exact carrier eigenline anchoring)},\\[1mm]
\text{CP-E:}&\langle B\cdot C\rangle_{pd}>0\quad\text{(unpaid transverse remainder)},\\[1mm]
\text{CP-S:}&\langle|A|^2\rangle_{pd}\ge\langle|C|^2\rangle_{pd}>0\quad\text{(transverse-strain payer)}.
\end{array}
}
\]

## 8. Next target

CP-E requires an audit of whether advection/localization can cancel the positive \(B\cdot C\) remainder on every recurrent production window.

CP-S and CE require a shared-source/parallel-budget analysis because transverse strain is either dominant or exactly recycled.

The key gain is that **projective action itself is no longer mistakenly treated as dissipation**; the exact sign-carrying object is \(B\cdot(A+B)\).

Status: **THE PROJECTIVE BRANCH HAS BEEN CORRECTLY SPLIT BY THE ACTUAL PALINSTROPHY SIGN. THE REMAINING OBSTRUCTION IS NOW EITHER A TRUE DERIVATIVE-TRANSFER EXCESS, A SAME-CARRIER TRANSVERSE-STRAIN PAYER, OR EXACT EIGENLINE ANCHORING. GLOBAL REGULARITY REMAINS UNPROVED.**