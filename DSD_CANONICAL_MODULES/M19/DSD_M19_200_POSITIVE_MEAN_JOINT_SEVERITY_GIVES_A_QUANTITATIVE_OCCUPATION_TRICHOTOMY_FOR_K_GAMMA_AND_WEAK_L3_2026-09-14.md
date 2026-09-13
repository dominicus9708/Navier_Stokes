# M19-200 — Positive mean joint severity gives a quantitative occupation trichotomy for K, Gamma, and weak-L3

**Date:** 2026-09-14  
**Status:** ACTIVE CALCULATION / OCCUPATION UPGRADE

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Mean-severity lower bound

Set

\[
Y(s):=[K(s)\Gamma(s)W(s)]^{3/2}.
\]

M19-199 gives, on a genuinely aperiodic recurrent hard component,

\[
\boxed{\langle Y\rangle\ge m_*:=c_0\nu\mathcal P_*>0.}
\]

Because W1 has finite least ceilings,

\[
0\le Y(s)\le Y_{max}:=[K^\sharp\Gamma^\sharp W^\sharp]^{3/2}<\infty.
\]

## 2. Positive occupation of a joint severe set

Choose

\[
y_0:=\frac{m_*}{2}.
\]

Let

\[
E_{sev}:=\{s:Y(s)\ge y_0\}.
\]

If its invariant time occupation is \(\theta_{sev}\), then

\[
\langle Y\rangle
\le y_0(1-\theta_{sev})+Y_{max}\theta_{sev}.
\]

Hence

\[
\boxed{
\theta_{sev}
\ge
\frac{m_*/2}{Y_{max}-m_*/2}>0
}
\]

whenever \(Y_{max}>m_*/2\); if \(Y_{max}=m_*/2\), then \(Y\equiv m_*/2\) on the relevant invariant support and the conclusion is even stronger.

Equivalently, with

\[
q_0:=y_0^{2/3},
\]

one has positive occupation of

\[
\boxed{K(s)\Gamma(s)W(s)\ge q_0.}
\]

## 3. Pigeonhole into three finite-high occupation sets

Choose positive thresholds \(k_0,\gamma_0,w_0\) such that

\[
k_0\gamma_0w_0<q_0.
\]

Then

\[
\{K\Gamma W\ge q_0\}
\subset
\{K\ge k_0\}\cup\{\Gamma\ge\gamma_0\}\cup\{W\ge w_0\}.
\]

Therefore at least one of these three sets has invariant time occupation at least

\[
\boxed{
\theta_0:=\frac{\theta_{sev}}{3}>0.
}
\]

Thus genuine aperiodicity forces at least one **persistent finite-high channel**, not merely a large supremum.

## 4. Consequences for the three audits

### K-channel

If

\[
\mu\{K\ge k_0\}\ge\theta_0,
\]

M19-196 gives

\[
\boxed{
\overline H
\ge
c\theta_0 k_0^{8/3}Z_+^{-1/3}.
}
\]

### Gamma-channel

If

\[
\mu\{\Gamma\ge\gamma_0\}\ge\theta_0,
\]

M19-197 splits this positive occupation into active shell derivative payment or positive-occupation denominator/shell-amplitude degeneration.

### weak-L3 channel

If

\[
\mu\{W\ge w_0\}\ge\theta_0,
\]

M19-198 splits the event into persistent critical-tail weak-L3 amplitude or positive-occupation compact-core level-set activity.

## 5. Main gain

M19-195 showed that supremum-only finite-high branches are not persistent payers. M19-199--200 repair that weakness at the joint-product level:

\[
\boxed{
\text{aperiodicity}
\Longrightarrow
\text{positive mean joint W1 severity}
\Longrightarrow
\text{at least one positive-occupation finite-high channel}.
}
\]

The next task is to close or further route the three positive-occupation alternatives rather than their mere supremum versions.