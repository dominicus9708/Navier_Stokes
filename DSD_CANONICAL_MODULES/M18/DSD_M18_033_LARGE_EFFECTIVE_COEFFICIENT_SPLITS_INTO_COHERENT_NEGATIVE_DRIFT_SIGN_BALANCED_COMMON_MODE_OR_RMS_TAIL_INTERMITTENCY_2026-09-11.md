# M18-033 — Large effective coefficient splits into coherent negative drift, sign-balanced common mode, or RMS-tail intermittency

**Date:** 2026-09-11  
**Status:** ACTIVE DSD ANALYSIS / COEFFICIENT-DISTRIBUTION TRIAGE / COMMON-MODE RECONNECTION

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Purpose

M18-032 replaced coefficient supremum growth by the weighted effective coefficients

\[
K_P^{\rm eff}
=
\frac{q_P}{q_E},
\qquad
K_H^{\rm eff}
=
\left(\frac{q_H}{q_E}\right)^{1/2}.
\]

The remaining question is what

\[
K_H^{\rm eff}\to\infty
\]

means as a coefficient-distribution statement under the same spacetime vorticity-energy measure.

The answer is a three-way structural split:

1. coherent negative-coefficient drift, which is visible to palinstrophy;
2. sign-balanced large absolute first moment, which reconnects to the common-mode sign architecture;
3. RMS-tail intermittency, where raw-H2 is carried by coefficient magnitudes much larger than the weighted L1 scale.

## 2. Probability measure and random coefficient

On one record window with \(q_E>0\), define

\[
\boxed{
d\mu
:=
\frac{\rho^2dxdt}{q_E}.
}
\]

This is a probability measure on spacetime.

Let

\[
X:=-\kappa.
\]

Then

\[
\boxed{
\mathbb E_\mu[X]
=K_P^{\rm eff}
=:m\ge0,
}
\]

and

\[
\boxed{
\left(\mathbb E_\mu[X^2]\right)^{1/2}
=K_H^{\rm eff}
=:s.
}
\]

Cauchy--Schwarz gives

\[
0\le m\le s.
\]

## 3. Coherent signed-drift branch

Fix

\[
0<c_0<1.
\]

Suppose

\[
\boxed{m\ge c_0s.}
\]

Let

\[
Y:=X_+=(-\kappa)_+.
\]

Since

\[
m=\mathbb E[X]
\le\mathbb E[Y]
\]

and

\[
\mathbb E[Y^2]
\le s^2,
\]

Paley--Zygmund gives, for \(0<\theta<1\),

\[
\mu\left(
Y\ge\theta\mathbb E[Y]
\right)
\ge
(1-\theta)^2
\frac{\mathbb E[Y]^2}{\mathbb E[Y^2]}
\ge
(1-\theta)^2c_0^2.
\]

Because \(\mathbb E[Y]\ge m\),

\[
\boxed{
\mu\left(
\kappa\le-\theta m
\right)
\ge
(1-\theta)^2c_0^2.
}
\]

Thus if the effective signed coefficient is a fixed fraction of the RMS coefficient, its growth cannot live on vanishing weighted mass. A fixed positive fraction of the spacetime \(\rho^2\) measure lies at negative coefficient magnitude comparable to \(m\).

This is the **coherent negative-drift branch**.

## 4. Small signed mean: introduce the absolute first moment

Now suppose

\[
\boxed{m<c_0s.}
\]

Define

\[
A_1
:=
\mathbb E_\mu[|\kappa|]
=
\mathbb E_\mu[|X|].
\]

Then

\[
m\le A_1\le s.
\]

Write the sign-separated first moments

\[
a:=\mathbb E[\kappa_-],
\qquad
b:=\mathbb E[\kappa_+].
\]

Since

\[
m=a-b,
\qquad
A_1=a+b,
\]

we have

\[
\boxed{
a=\frac{A_1+m}{2},
\qquad
b=\frac{A_1-m}{2}.}
\]

## 5. Sign-balanced common-mode branch

Fix

\[
c_1>c_0.
\]

Suppose

\[
\boxed{A_1\ge c_1s.}
\]

Then

\[
a\ge\frac{c_1s}{2},
\]

and

\[
b\ge\frac{(c_1-c_0)s}{2}.
\]

Hence both sign-separated coefficient first moments are order \(s\):

\[
\boxed{
\mathbb E[\kappa_-]\gtrsim s,
\qquad
\mathbb E[\kappa_+]\gtrsim s.
}
\]

while their difference is only

\[
m<c_0s.
\]

This is exactly a large common-mode / small differential-mode configuration in coefficient sign space.

The instantaneous late-M17 variables were

\[
K_-(t)=\int\kappa_-\rho^2dx,
\qquad
K_+(t)=\int\kappa_+\rho^2dx,
\]

with

\[
A(t)=K_-(t)+K_+(t),
\qquad
P(t)=K_-(t)-K_+(t).
\]

Therefore the spacetime sign-balanced branch is not a new category. It reconnects directly to the M18-001--011 common-mode / zero-current analysis.

## 6. RMS-tail intermittency branch

The remaining case is

\[
\boxed{
A_1<c_1s.
}
\]

Define the coefficient intermittency ratio

\[
\boxed{
\mathfrak I_\kappa
:=
\frac{s}{A_1}
\ge1.
}
\]

In the strongly intermittent regime,

\[
\mathfrak I_\kappa\to\infty.
\]

The RMS coefficient is then much larger than the weighted absolute first moment.

This means the raw-H2 coefficient square is carried by increasingly extreme coefficient values rather than by coherent bulk displacement.

## 7. Quantitative tail localization of raw-H2

Let

\[
L>0.
\]

On the region \(|\kappa|\le L\),

\[
\kappa^2\le L|\kappa|.
\]

Therefore

\[
\mathbb E[\kappa^2\mathbf1_{|\kappa|\le L}]
\le
LA_1.
\]

Choose

\[
\boxed{
L_*
:=
\frac{s^2}{2A_1}
=
\frac12s\mathfrak I_\kappa.
}
\]

Then

\[
\mathbb E[\kappa^2\mathbf1_{|\kappa|\le L_*}]
\le
\frac{s^2}{2}.
\]

Since

\[
\mathbb E[\kappa^2]=s^2,
\]

we obtain

\[
\boxed{
\mathbb E[\kappa^2
\mathbf1_{|\kappa|>L_*}]
\ge
\frac{s^2}{2}.
}
\]

Thus at least half of the raw-H2 coefficient-square charge lies at coefficient magnitude

\[
\boxed{
|\kappa|
>
\frac12s\mathfrak I_\kappa.
}
\]

When \(\mathfrak I_\kappa\gg1\), this threshold is much larger than the RMS scale itself.

This is a genuine heavy-tail coefficient endpoint.

## 8. Weighted mass of the tail is not controlled from below

The previous result is a lower bound on the **raw-H2 second-moment share**, not on the probability mass

\[
\mu(|\kappa|>L_*).
\]

Without a higher moment or a coefficient ceiling, the same second-moment charge may be carried by an arbitrarily small weighted mass at arbitrarily large coefficient magnitude.

Therefore

\[
\boxed{
\text{large raw-H2 tail charge}
\not\Rightarrow
\text{positive weighted tail mass fraction}.
}
\]

This is the coefficient-distribution analogue of the pointwise-to-integrated payer firewall used throughout M18.

## 9. Canonical effective-coefficient trichotomy

Combining Sections 3--7, large \(K_H^{\rm eff}=s\) splits as

\[
\boxed{
\begin{aligned}
G_{K_H^{\rm eff}\text{-large}}
\Longrightarrow{}&
G_{\rm coherent\ negative\ drift}\\
&\lor G_{\rm sign\text{-}balanced\ common\ mode}\\
&\lor G_{\rm RMS\text{-}tail\ intermittency}.
\end{aligned}
}
\]

The three branches have distinct meanings:

- coherent drift is visible to palinstrophy and occupies positive weighted mass;
- sign-balanced growth returns to the already-developed common-mode zero-current machinery;
- RMS-tail intermittency is a genuine coefficient heavy-tail endpoint.

## 10. Ancestry implications

### Coherent drift

Here

\[
K_P^{\rm eff}\gtrsim K_H^{\rm eff},
\]

so the exact palinstrophy standard-energy charge

\[
R\frac{q_P}{K_P^{\rm eff}}
\]

is the natural genealogy currency.

### Sign-balanced common mode

Large positive and negative first moments with small difference mean the common-mode variable is large while palinstrophy can remain comparatively small. This returns directly to M18-001--011, where regular zero-current and common-mode source-return were already classified.

### RMS-tail intermittency

The standard-energy identity remains exact, but the large effective RMS coefficient can be supported on small weighted sets. Closing this branch requires a tail-thickness, higher-moment, or coefficient-level geometry theorem rather than another supremum estimate.

## 11. Relation to coefficient supremum

The trichotomy depends only on the weighted distribution under \(d\mu\). A diverging unweighted coefficient supremum can lie outside all three effective-growth branches if it carries negligible \(\rho^2\) mass and does not alter \(m\), \(A_1\), or \(s\).

Thus the spectator-supremum firewall of M18-032 remains in force.

## 12. Audit verdict

### Certified

1. Large effective RMS coefficient has a canonical three-way weighted-distribution split.
2. Coherent signed growth occupies a positive fraction of weighted spacetime mass.
3. Sign-balanced large absolute first moment reconnects to the existing common-mode analysis rather than creating a new branch.
4. In the intermittent branch, at least half of raw-H2 coefficient-square charge lies above the explicit threshold \(s^2/(2A_1)\).
5. No positive weighted mass fraction follows for that tail without extra information.

### Not certified

1. Elimination of RMS-tail intermittency.
2. A higher coefficient moment controlling the tail mass.
3. A uniform coefficient-level geometry theorem on the intermittent tail.
4. Global ancestry divergence.
5. Global 3D Navier--Stokes regularity.

## 13. Next target

M18-034 should audit the RMS-tail intermittency branch against the existing coefficient-bin, level-flux, and raw-H2 ancestry machinery.

The central question is whether a tail carrying a fixed fraction of raw-H2 at coefficient magnitude

\[
L_*
=\frac{s^2}{2A_1}
\]

can remain arbitrarily thin in coefficient level and weighted spacetime mass, or whether the existing M18-018--021 level-width/temporal-thickness mechanisms force a lower-order payment.