# DSD M5-56 — Amplitude-Mollified First-Hit Ledger

Date: 2026-08-27

Status: **EXACT AMPLITUDE-AVERAGED THRESHOLD LEDGER / COAREA REMOVES THE POINTWISE LEVEL-SET DENOMINATOR AND CONVERTS THE M5-37 PRESSURE-TAIL DERIVATIVE INTO A FINITE-BAND VOLUME PAYER / A POSITIVE AVERAGED FIRST HIT FORCES A STRICT BANDWISE PRESSURE OVERPAY / NO UNIFORM LEVEL-SET TRANSVERSALITY IS REQUIRED / GLOBAL REGULARITY UNPROVED.**

## 1. Motivation from M5-55

M5-55 showed that the pointwise pressure-tail derivative

\[
-\partial_\lambda Q_P(\lambda)
=
\int_{\Sigma_\lambda}
\frac{|P|^2}{|\nabla a|}\,dS
\]

is a poor object on which to demand a uniform amplitude band, because quantitative level-set transversality is not yet available.

Instead choose a fixed nonnegative smooth amplitude weight

\[
w\in C_c^\infty((0,\infty)),
\qquad
w\ge0,
\qquad
\int_0^\infty w(\lambda)d\lambda=1,
\]

supported in a normalized finite amplitude band

\[
I=[\lambda_-,\lambda_+]
\]

surrounding the pump threshold.

All quantities below are in the normalized W1/ancient-cell variables.

---

## 2. Average the threshold entropy and its ledger

For the M5 threshold entropy `E_lambda`, define

\[
\boxed{
\bar E_w(t)
:=
\int_0^\infty
w(\lambda)E_\lambda(t)d\lambda.
}
\]

Similarly define

\[
\bar J_w
:=
\int w(\lambda)J_P(\lambda)d\lambda,
\]

\[
\bar D_w
:=
\int w(\lambda)D_\lambda^{surf}d\lambda,
\]

and

\[
\bar A_w
:=
\int w(\lambda)A(\lambda)d\lambda.
\]

Since the M5 threshold identity is linear in the amplitude parameter after integration, the exact averaged ledger is

\[
\boxed{
\partial_t\bar E_w
+
\nu\bar D_w
=
\bar J_w.
}
\]

Therefore at a positive averaged first hit, or more generally at any upward crossing satisfying

\[
\partial_t\bar E_w\ge0,
\]

we have

\[
\boxed{
\bar J_w
\ge
\nu\bar D_w.
}
\]

This requires only one first-hit/crossing condition for the averaged observable. It does not require synchronized first hits for every `lambda` in the band.

---

## 3. Coarea converts the averaged pressure-tail derivative into a volume payer

Let

\[
a=|U|,
\qquad
Q_P(\lambda)
=
\int_{a>\lambda}|P|^2dy.
\]

Define

\[
\boxed{
\bar S_w
:=
\int_0^\infty
w(\lambda)
\lambda[-Q_P'(\lambda)]d\lambda.
}
\]

The distributional layer-cake/coarea identity gives directly

\[
\boxed{
\bar S_w
=
\int_{\mathbb R^3}
a\,w(a)|P|^2dy.
}
\]

Thus `bar S_w` is a finite-amplitude-band localization of the M5-54 weighted pressure payer

\[
\mathcal W
=
\int a|P|^2dy.
\]

No pointwise division by `|grad a|` remains.

This identity is valid at the volume/distribution level and therefore avoids the uniform regular-value obstruction isolated in M5-55.

---

## 4. Coarea form of the surface payer

Recall

\[
D_\lambda^{surf}
=A(\lambda)+\lambda B(\lambda),
\]

with

\[
B(\lambda)
=
\int_{\Sigma_\lambda}|\nabla a|dS.
\]

Define

\[
\bar C_w
:=
\int w(\lambda)\lambda B(\lambda)d\lambda.
\]

Coarea gives

\[
\boxed{
\bar C_w
=
\int a\,w(a)|\nabla a|^2dy.
}
\]

Therefore

\[
\boxed{
\bar D_w
=
\bar A_w+ar C_w.
}
\]

The averaged bulk term can also be written without level surfaces. If

\[
W_<(s):=
\int_0^s w(\lambda)d\lambda,
\]

then Fubini yields

\[
\boxed{
\bar A_w
=
\int W_<(a)|\nabla U|^2dy.
}
\]

Every part of the averaged dissipation is therefore a volume quantity.

---

## 5. Averaged pressure flux is also a volume quantity

Using

\[
J_P(\lambda)
=
\int_{\Sigma_\lambda}P\,U\cdot n_\lambda\,dS,
\]

coarea gives

\[
\boxed{
\bar J_w
=
\int w(a)P\,U\cdot\nabla a\,dy.
}
\]

Now apply Cauchy--Schwarz with the amplitude weight:

\[
\begin{aligned}
|\bar J_w|^2
&\le
\left(
\int a\,w(a)|P|^2dy
\right)
\left(
\int w(a)
\frac{|U\cdot\nabla a|^2}{a}dy
\right)\\
&\le
\bar S_w
\int a\,w(a)|\nabla a|^2dy.
\end{aligned}
\]

Hence

\[
\boxed{
|\bar J_w|^2
\le
\bar S_w\bar C_w
=
\bar S_w(\bar D_w-\bar A_w).
}
\]

This is the exact amplitude-mollified analogue of the sharper M5-37 surface Cauchy inequality.

---

## 6. Strict bandwise pressure gap at a positive averaged first hit

At an upward averaged crossing,

\[
\nu\bar D_w
\le
\bar J_w.
\]

Combining with the averaged Cauchy inequality gives

\[
\nu^2\bar D_w^2
\le
\bar S_w(\bar D_w-\bar A_w).
\]

Therefore

\[
\bar S_w
\ge
\nu^2
\frac{\bar D_w^2}
{\bar D_w-\bar A_w}.
\]

As in M5-37,

\[
\frac{D^2}{D-A}
=D+A+\frac{A^2}{D-A}
\ge D+A.
\]

Thus

\[
\boxed{
\bar S_w
\ge
\nu^2\bar D_w
+
\nu^2\bar A_w.
}
\]

Equivalently,

\[
\boxed{
\int a\,w(a)|P|^2dy
\ge
\nu^2\bar D_w
+
\nu^2\bar A_w.
}
\]

This is a genuine finite-band version of the M5-37 strict pressure-tail margin.

---

## 7. Positive averaged bulk-gradient floor

On the normalized W1 pump class, the active high-amplitude excess is confined to the fixed phase cell used in M5-37.

For the threshold entropy underlying M5-37, Poincare/Sobolev on that fixed cell gives statewise control of the form

\[
E_\lambda
\le
C_{cell}A(\lambda)
\]

on the retained positive-excess band.

Integrating against `w` gives

\[
\bar E_w
\le
C_{cell}\bar A_w.
\]

Therefore, if the averaged observable is first hit at a fixed positive level

\[
\bar E_w=\kappa_*>0,
\]

then

\[
\boxed{
\bar A_w
\ge
A_{w,*}
:=
\frac{\kappa_*}{C_{cell}}>0.
}
\]

Consequently

\[
\boxed{
\bar S_w
\ge
\nu^2\bar D_w
+
\nu^2A_{w,*}.
}
\]

The additive margin now occupies a finite amplitude band by construction.

---

## 8. Relation to the global M5-54 payer

Because `w` has fixed compact support and is bounded,

\[
0\le
\bar S_w
=
\int a\,w(a)|P|^2dy
\le
\|w\|_\infty
\int a|P|^2dy.
\]

Thus

\[
\boxed{
\bar S_w
\le
\|w\|_\infty\mathcal W.
}
\]

A strict averaged first hit therefore forces a genuine positive lower requirement on the finite M5-54 resource `W`.

Unlike the single-level M5-37 derivative gap, this requirement is not supported on an amplitude set of zero measure.

---

## 9. What has been solved and what has not

### Solved

The amplitude-thickness problem can be reformulated without proving uniform transversality:

\[
\boxed{
\text{pointwise level derivative}
\longrightarrow
\text{amplitude-mollified volume payer}.
}
\]

The averaged strict gap is mathematically compatible with coarea/Fubini and uses one averaged first-hit condition rather than a synchronized continuum of first hits.

### Not yet solved

It remains to prove that the recurrent pump-to-defect orbit necessarily produces a **nonconstant averaged threshold observable** with a robust positive crossing that is inherited by the syndetic scale returns.

Even if such crossings recur, a second audit is required: the averaged threshold ledger may be an exact time derivative and therefore may telescope over recurrent cycles rather than yield a contradiction.

---

## 10. New proof gate

The next step is therefore twofold:

1. show that one can choose a fixed amplitude weight `w` and crossing level `kappa_*` for which the anchor pump has a temporally transverse crossing of `bar E_w`;
2. transport that crossing through the minimal/syndetic W1 recurrence and then audit the resulting signed long-time balance.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
