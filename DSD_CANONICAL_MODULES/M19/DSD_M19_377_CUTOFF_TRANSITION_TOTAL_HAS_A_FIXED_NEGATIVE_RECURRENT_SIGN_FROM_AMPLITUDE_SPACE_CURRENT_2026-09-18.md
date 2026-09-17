# M19-377 — The cutoff-transition total has a fixed negative recurrent sign from the amplitude-space current

**Date:** 2026-09-18  
**Status:** NEW EXACT CROSS-LEDGER IDENTITY / M5-668--669 + M17-186 SIGN CORRECTION

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Motivation

M17-186 defines the high-amplitude cutoff-transition source

\[
C_\chi(k,\theta)
:=
\int
\delta(k-\kappa)
\chi'(\rho)\rho^3(\sigma+\kappa-1)dy
\]

and its total

\[
\boxed{
C_\chi^{tot}(\theta)
:=
\int C_\chi(k,\theta)dk
=
\int\chi'(\rho)\rho^3\gamma\,dy,
}
\]

where

\[
\gamma:=\sigma+\kappa-1.
\]

M17-186 retained the possibility that a positive mean cutoff-transition source could reverse the sign of the unweighted quarter-strain excess.

M5-668--669 provide an exact amplitude-space current that allows this sign to be computed.

## 2. Amplitude-space material current

For a regular amplitude level \(a>0\), define

\[
\boxed{
\mathcal T(a,\theta)
:=
a\int_{\rho=a}
\frac{\gamma}{|\nabla\rho|}dS.
}
\]

M5-668 gives

\[
V_a'
=
\frac32V_a+\mathcal T(a,\theta),
\qquad
V_a:=|\{\rho>a\}|.
\]

On a recurrent invariant component,

\[
\boxed{
\overline{\mathcal T}(a)
=
-\frac32\overline V_a.
}
\]

Thus the mean material current is strictly downward at every occupied positive amplitude threshold.

## 3. Coarea representation of the cutoff source

By the coarea formula,

\[
\begin{aligned}
C_\chi^{tot}
&=
\int_0^\infty
\chi'(a)a^3
\left[
\int_{\rho=a}
\frac{\gamma}{|\nabla\rho|}dS
\right]da\\
&=
\boxed{
\int_0^\infty
\chi'(a)a^2\mathcal T(a,\theta)\,da.
}
\end{aligned}
\]

This identity is distributionally valid through exceptional amplitude levels by approximation; no regular-level selection is needed in the final integrated formula.

## 4. Recurrent sign

Take the recurrent mean and use the M5-668 current law:

\[
\begin{aligned}
\overline{C_\chi^{tot}}
&=
\int_0^\infty
\chi'(a)a^2\overline{\mathcal T}(a)da\\
&=
-\frac32
\int_0^\infty
\chi'(a)a^2\overline V_a\,da.
\end{aligned}
\]

For the monotone high-amplitude cutoff used in M5-683/M5-688/M17-186,

\[
\chi'\ge0.
\]

Therefore

\[
\boxed{
\overline{C_\chi^{tot}}
\le0.
}
\]

It is strictly negative whenever the cutoff transition range has positive recurrent occupied volume.

## 5. Consequence for the unweighted quarter-strain excess

M17-186 gives

\[
Q_\sigma^{(0)}
=
\overline{
D_\chi+B_\chi-rac12C_\chi^{tot}
},
\]

with

\[
D_\chi\ge0,
\qquad
B_\chi\ge0.
\]

Insert Section 4:

\[
\boxed{
Q_\sigma^{(0)}
=
\overline{D_\chi+B_\chi}
+
\frac34
\int_0^\infty
\chi'(a)a^2\overline V_a\,da.
}
\]

Hence

\[
\boxed{
Q_\sigma^{(0)}\ge0,
}
\]

and it is strictly positive on the retained nontrivial cutoff branch.

## 6. Historical audit correction

M17-186 correctly warned that the full-space quarter-strain identity cannot be inserted into a cutoff ledger without the transition term.

However, once M5-668--669 is also imposed, the sentence

\[
\text{``a sufficiently strong positive cutoff-transition source may reverse }Q_\sigma^{(0)}\text{''}
\]

is too pessimistic for the recurrent monotone-cutoff branch.

The exact amplitude-space current forces the opposite sign:

\[
\boxed{
\overline{C_\chi^{tot}}\le0.
}
\]

Thus the cutoff transition strengthens rather than cancels the unweighted quarter-strain excess.

This correction concerns the **unweighted total** \(C_\chi^{tot}\), not the exponentially \(e^{2\kappa}\)-weighted source used in the full M5-688 cycle-work.

## 7. Exponentially tilted source remains distinct

M5-688 also uses

\[
\mathcal C
:=
\int e^{2k}\overline C_\chi(k)dk
=
\left\langle
\int\chi'(\rho)\rho^3e^{2\kappa}\gamma\,dy
\right\rangle.
\]

The amplitude-space sign theorem above does **not** automatically determine the sign of \(\mathcal C\), because \(e^{2\kappa}\) can correlate with the signed amplitude crossing speed on each level.

Thus the remaining cutoff uncertainty is not ordinary threshold turnover itself. It is a \(\kappa\)-phase-weighted threshold-current covariance.

## 8. Updated payer classification

Together with M19-375--376:

\[
\boxed{
\begin{aligned}
D_\sigma
&:\ \text{palinstrophy-order critical occupancy},\\
Q_\sigma^{(2)}
&:\ \text{kappa--line-residence hysteresis},\\
C_\chi^{tot}
&:\ \text{fixed-sign downward amplitude turnover},\\
\mathcal C
&:\ \text{only the kappa-tilted crossing covariance remains sign-indefinite}.
\end{aligned}
}
\]

## 9. Next target

The natural next variable is the joint amplitude/coefficient crossing current

\[
\mathcal T_2(a)
:=
 a\int_{\rho=a}
 e^{2\kappa}
\frac{\gamma}{|\nabla\rho|}dS,
\]

for which

\[
\mathcal C
=
\int\chi'(a)a^2\mathcal T_2(a)da.
\]

One should separate the known downward mean current from the remaining conditional covariance of \(e^{2\kappa}\) with \(\gamma\) on amplitude levels.

---

\[
\boxed{\text{M19-377 COMPLETE; THE UNWEIGHTED CUTOFF-TRANSITION SIGN IS FIXED AND CANNOT CANCEL THE QUARTER-STRAIN EXCESS.}}
\]
