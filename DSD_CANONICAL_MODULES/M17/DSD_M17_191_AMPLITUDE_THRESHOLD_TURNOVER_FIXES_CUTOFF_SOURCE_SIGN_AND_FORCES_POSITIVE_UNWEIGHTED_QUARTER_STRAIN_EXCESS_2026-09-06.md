# DSD M17-191 — Amplitude-threshold turnover fixes the cutoff-source sign and forces positive unweighted quarter-strain excess

Date: 2026-09-06  
Canonical ID: **M17-191**

Status: **CUTOFF-SOURCE SIGN CLOSURE / M17-186 LEFT OPEN THE POSSIBILITY THAT THE MONOTONE HIGH-AMPLITUDE CUTOFF SOURCE `C_chi^tot=int chi'(rho) rho^3 (sigma+kappa-1)` COULD BE POSITIVE ENOUGH TO MAKE THE UNWEIGHTED QUARTER-STRAIN EXCESS NONPOSITIVE. M5-668 ALREADY GIVES THE EXACT FIXED-AMPLITUDE TURNOVER LAW `T_a=a int_{rho=a}(sigma+kappa-1)/|grad rho| dS` WITH RECURRENT MEAN `bar T_a=-(3/2)bar V_a`. AMPLITUDE COAREA GIVES `C_chi^tot=int chi'(a)a^2 T_a da`, SO FOR A MONOTONE CUTOFF `chi'>=0`, `bar C_chi^tot=-(3/2)int chi'(a)a^2 bar V_a da <=0`. SUBSTITUTION INTO M17-186 YIELDS `Q_sigma^(0)=bar(D_chi+B_chi)+(3/4)int chi'(a)a^2 bar V_a da >0` ON EVERY NONTRIVIAL RETAINED BRANCH. THUS THE `Q_sigma^(0)<=0` CUTOFF-TRANSITION ESCAPE IN M17-187 IS CLOSED. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. M17-186 cutoff source

For a smooth monotone high-amplitude cutoff

\[
0\le\chi\le1,
\qquad
\chi'\ge0,
\]

M17-186 defines

\[
\boxed{
C_\chi^{tot}
:=\int_{\mathbb R^3}
\chi'(\rho)\rho^3
(\sigma+\kappa-1)dy.
}
\]

It enters the recurrent quarter-strain identity

\[
\boxed{
Q_\sigma^{(0)}
=\overline{
D_\chi+B_\chi-\frac12C_\chi^{tot}
},
}
\]

where

\[
D_\chi=\int\chi|\nabla W|^2dy\ge0,
\]

\[
B_\chi=\int\chi'(\rho)\rho|\nabla\rho|^2dy\ge0.
\]

---

## 2. M5-668 threshold-turnover law

For every regular amplitude level `a>0`, define

\[
V_a:=|\{\rho>a\}|
\]

and

\[
\boxed{
\mathcal T_a
:=a\int_{\rho=a}
\frac{\sigma+\kappa-1}{|\nabla\rho|}dS.
}
\]

M5-668 gives

\[
\boxed{
V_a'=\frac32V_a+\mathcal T_a.
}
\]

On the recurrent compact hull,

\[
\boxed{
\overline{\mathcal T_a}
=-\frac32\overline{V_a}
\le0.
}
\]

For every amplitude level with positive recurrent superlevel volume, the inequality is strict.

---

## 3. Amplitude coarea converts the cutoff source to threshold turnover

Use the coarea formula for the scalar amplitude `rho`:

\[
\int f(\rho,y)dy
=\int_0^\infty
\int_{\rho=a}
\frac{f(a,y)}{|\nabla\rho|}dS\,da.
\]

Apply to the M17-186 source:

\[
\begin{aligned}
C_\chi^{tot}
&=\int_0^\infty
\chi'(a)a^3
\int_{\rho=a}
\frac{\sigma+\kappa-1}{|\nabla\rho|}dS\,da\\
&=\int_0^\infty
\chi'(a)a^2\mathcal T_a\,da.
\end{aligned}
\]

Thus

\[
\boxed{
C_\chi^{tot}
=\int_0^\infty
\chi'(a)a^2\mathcal T_a\,da.
}
\]

This also shows that in the sharp-step limit at threshold `a_0`, the cutoff source is exactly `a_0^2 T_{a_0}`.

---

## 4. Recurrent sign of the cutoff source

Take the recurrent mean and use M5-668:

\[
\begin{aligned}
\overline{C_\chi^{tot}}
&=\int_0^\infty
\chi'(a)a^2\overline{\mathcal T_a}\,da\\
&=-\frac32
\int_0^\infty
\chi'(a)a^2\overline{V_a}\,da.
\end{aligned}
\]

Therefore

\[
\boxed{
\overline{C_\chi^{tot}}\le0.
}
\]

If the cutoff transition intersects a positive recurrent-amplitude population on a set of `a` with positive `chi'` weight, then

\[
\boxed{
\overline{C_\chi^{tot}}<0.
}
\]

Thus the cutoff transition cannot supply the positive unweighted source that M17-187 had left as a possible escape.

---

## 5. Positive unweighted quarter-strain excess

Substitute Section 4 into M17-186:

\[
Q_\sigma^{(0)}
=\overline{D_\chi+B_\chi}
+\frac34
\int_0^\infty
\chi'(a)a^2\overline{V_a}\,da.
\]

Hence

\[
\boxed{
Q_\sigma^{(0)}
=\overline{D_\chi+B_\chi}
+\frac34
\int\chi'(a)a^2\overline{V_a}da
\ge0.
}
\]

On a nontrivial high-amplitude recurrent state, either the retained region has nonzero palinstrophy/amplitude-gradient charge or the transition superlevel volume is positive, so

\[
\boxed{Q_\sigma^{(0)}>0.}
\]

In particular, the `P_0<=0` branch of M17-187 is closed.

---

## 6. Revised M17-187 dichotomy

The regular high-amplitude conveyor now necessarily starts from

\[
\boxed{P_0=Q_\sigma^{(0)}>0.}
\]

Therefore only two quarter-strain possibilities remain:

### A. Direct exponential payer

\[
Q_\sigma^{(2)}
\gtrsim e^{-2K_*}Q_\sigma^{(0)}>0.
\]

### B. `kappa`-phase-segregated deficit

If `Q_sigma^(2)` is suppressed, M17-187 forces

\[
\boxed{
P_-
\ge
\frac{[e^{-2K_*}P_0-P_2]_+}
{e^{2K_*}-e^{-2K_*}}.
}
\]

Thus the cutoff-transition escape is removed from this part of the payer tree.

---

## 7. Relation to M5-688

M5-688 still contains an **exponentially `kappa`-weighted** cutoff term

\[
\mathcal C
=\int e^{2k}\overline C_\chi(k)dk.
\]

Section 4 fixes only the sign of its unweighted integral.
Because `e^(2k)` is not constant, `mathcal C` may still have either sign through `kappa`-phase segregation of threshold crossings.

Thus the next useful audit is to quantify how much positive threshold-turnover mass is required for `mathcal C` to become a positive payer despite

\[
\int\overline C_\chi(k)dk<0.
\]

---

## 8. DSD audit

### Audit A — sign of `C_chi^tot`
It is fixed only after time averaging on the recurrent superlevel-volume ledger.

### Audit B — extending the sign to the exponential cutoff payer
Rejected. The exponential `kappa` tilt can reverse a signed distribution.

### Audit C — double-counting threshold turnover and cutoff transition
They are the same source after amplitude coarea; they must not be counted independently.

### Audit D — proof status
One payer escape is closed, but exponential phase segregation remains.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
