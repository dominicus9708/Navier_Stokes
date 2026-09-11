# M18-064 — Total covariance splits mandatory amplitude-growth segregation into within-state spatial and between-state recurrent-phase channels

**Date:** 2026-09-11  
**Status:** CONNECTIVITY AUDIT / TOTAL-COVARIANCE DECOMPOSITION / SPATIAL-VERSUS-TEMPORAL SEGREGATION FIREWALL

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Purpose

M18-062--063 prove a mandatory positive covariance between

\[
h:=\sigma+\kappa
\]

and amplitude tilt

\[
w:=\rho^{q-p},
\qquad q>p\ge2,
\]

under the joint recurrent probability measure \(\mathbb P_p\):

\[
\boxed{
\operatorname{Cov}_{\mathbb P_p}(h,w)
=
\delta_{pq}\mathbb E_p[w]>0,
}
\]

where

\[
\delta_{pq}
=
\frac32\left(\frac1p-\frac1q\right).
\]

M18-063 suggested using spatial connectivity/analyticity to turn the population split into an interface payment.

That step requires an audit: \(\mathbb P_p\) averages both hull states and spatial points. The covariance could be spatial within one state, temporal/state-to-state across recurrent phases, or both.

The present module separates those mechanisms exactly.

## 2. State marginal and conditional spatial measures

Recall

\[
d\mathbb P_p(Y,y)
=
\frac{\rho_Y(y)^p}{\langle M_p\rangle}
\,dy\,d\mu(Y),
\]

where

\[
M_p(Y)=\int\rho_Y^pdy.
\]

Define the \(p\)-weighted state marginal

\[
\boxed{
d\nu_p(Y)
:=
\frac{M_p(Y)}{\langle M_p\rangle}\,d\mu(Y).
}
\]

For every state with \(M_p(Y)>0\), define the conditional spatial probability

\[
\boxed{
d\pi_{p,Y}(y)
:=
\frac{\rho_Y(y)^p}{M_p(Y)}\,dy.
}
\]

Then

\[
\boxed{
d\mathbb P_p(Y,y)=d\pi_{p,Y}(y)d\nu_p(Y).}
\]

## 3. Conditional means

Define

\[
\boxed{
\bar h_p(Y)
:=
\int h(Y,y)d\pi_{p,Y}(y)
=
\frac{\int h\rho^pdy}{M_p(Y)},
}
\]

and

\[
\boxed{
\bar w_p(Y)
:=
\int w(Y,y)d\pi_{p,Y}(y)
=
\frac{M_q(Y)}{M_p(Y)}.
}
\]

The joint expectations are

\[
\mathbb E_p[h]=\mathbb E_{\nu_p}[\bar h_p],
\qquad
\mathbb E_p[w]=\mathbb E_{\nu_p}[\bar w_p].
\]

## 4. Exact law of total covariance

The standard total-covariance identity gives

\[
\boxed{
\begin{aligned}
\operatorname{Cov}_{\mathbb P_p}(h,w)
={}&
\mathbb E_{\nu_p}
\left[
\operatorname{Cov}_{\pi_{p,Y}}(h,w)
\right]\\
&+
\operatorname{Cov}_{\nu_p}
\left(
\bar h_p,
\bar w_p
\right).
\end{aligned}
}
\]

Insert the exact M18-062 value:

\[
\boxed{
\begin{aligned}
\delta_{pq}\mathbb E_p[w]
={}&
C_{space}^{pq}
+C_{phase}^{pq},
\end{aligned}
}
\]

where

\[
\boxed{
C_{space}^{pq}
:=
\mathbb E_{\nu_p}
\left[
\operatorname{Cov}_{\pi_{p,Y}}(h,w)
\right]
}
\]

and

\[
\boxed{
C_{phase}^{pq}
:=
\operatorname{Cov}_{\nu_p}
(\bar h_p,\bar w_p).
}
\]

Since the sum is strictly positive, at least one satisfies

\[
\boxed{
C_{space}^{pq}
\ge
\frac12\delta_{pq}\mathbb E_p[w]
\quad\lor\quad
C_{phase}^{pq}
\ge
\frac12\delta_{pq}\mathbb E_p[w].
}
\]

This is the canonical connectivity split.

## 5. Spatial segregation branch

Suppose

\[
C_{space}^{pq}>0.
\]

Then a positive \(\nu_p\)-measure set of recurrent states must have nontrivial within-state covariance between

\[
h(Y,\cdot)
\]

and

\[
\rho(Y,\cdot)^{q-p}.
\]

In particular, the joint covariance cannot be generated solely by different time phases.

For such states there exist spatial regions with relatively larger amplitude and larger conditional mean \(h\), and complementary lower-amplitude/lower-growth regions.

### Bounded-core subbranch

If a fixed positive fraction of this covariance remains inside one fixed ball \(B_L\), spatial continuity gives connecting paths between the two regions.

Along any path connecting values separated in \(\rho\) and/or \(h=\sigma+\kappa\), one must encounter

\[
\boxed{
\nabla\rho\neq0
\quad\lor\quad
\nabla\sigma\neq0
\quad\lor\quad
\nabla\kappa\neq0.
}
\]

Uniform smooth compactness converts a fixed value gap over bounded distance into a gradient/transition event after the usual thickness bookkeeping, unless the path crosses a zero/interface where the active CE-H description fails.

Thus the bounded-core spatial branch routes to

\[
\boxed{
G_{\nabla\rho}
\lor
G_{\nabla\sigma}
\lor
G_{\nabla\kappa}
\lor
G_{zero/interface/domain}.
}
\]

These are all existing descendant channels.

### Remote spatial subbranch

If the covariance can only be realized by points escaping every fixed normalized ball, it belongs to

\[
\boxed{
\mathcal R_{remote/critical}
}
\]

or to the already typed remote/tail segregation exit.

Thus spatial covariance does not create a new root.

## 6. Why connectedness alone was insufficient

The domain \(\mathbb R^3\) is connected and the fields are analytic/smooth at each retained time, but this does not imply that the two populations found in M18-063 occur in the same state.

The previous shortcut would have been

\[
\text{joint positive covariance}
\Rightarrow
\text{same-snapshot interface}.
\]

M18-064 forbids that inference.

Only the \(C_{space}^{pq}\) branch may use spatial connectivity directly.

## 7. Recurrent-phase segregation branch

Suppose instead

\[
C_{phase}^{pq}>0.
\]

Then states with larger amplitude-concentration ratio

\[
\boxed{
\bar w_p(Y)=\frac{M_q(Y)}{M_p(Y)}
}
\]

systematically have larger \(p\)-weighted net-growth mean

\[
\boxed{
\bar h_p(Y)
=
\frac{\int(\sigma+\kappa)\rho^pdy}{M_p(Y)}.
}
\]

Thus the mandatory segregation is carried by different recurrent phases rather than primarily by simultaneous spatial separation.

The p-moment equation gives, statewise,

\[
\boxed{
\bar h_p(Y)-c_p
=
\frac1p\frac{M_p'(Y)}{M_p(Y)}
}
\]

whenever \(M_p(Y)>0\).

Hence the phase branch is equivalently a positive covariance between amplitude concentration and the instantaneous logarithmic growth rate of the p-moment:

\[
\boxed{
C_{phase}^{pq}
=
\frac1p
\operatorname{Cov}_{\nu_p}
\left(
\frac{M_p'}{M_p},
\frac{M_q}{M_p}
\right).
}
\]

So a positive phase branch means concentrated-amplitude phases preferentially occur while \(M_p\) is growing faster.

## 8. Temporal transition interpretation

On an ergodic recurrent orbit, any two state subsets of positive invariant measure recur infinitely often.

If \(C_{phase}^{pq}\) is quantitatively positive and the state observables are uniformly temporally equicontinuous, repeated passage between lower- and higher-concentration phases produces a finite temporal transition cost in at least one of

\[
\boxed{
\partial_\theta M_p,
\quad
\partial_\theta M_q,
\quad
\partial_\theta\bar h_p,
\quad
\text{coefficient/amplitude time jets}.
}
\]

If equicontinuity fails, this is precisely a time-jet/compactness decompactification of the type already isolated in M18-021 and related modules.

This is a routing statement, not yet a finite-budget contradiction.

## 9. Phase covariance is also compatible with recurrence

A periodic orbit can have

- a high-concentration growth phase;
- a low-concentration decay phase;
- exact return of all bounded state observables after one cycle.

Therefore

\[
\boxed{
C_{phase}^{pq}>0
\not\Rightarrow
\text{contradiction}.
}
\]

The positive covariance records hysteresis/phase structure, not one-way drift.

This is the same compact-coboundary firewall as M16-016 in a new variable set.

## 10. Combined routing theorem

The exact mandatory covariance of M18-062 therefore has the refined routing

\[
\boxed{
G_{amp-growth\ covariance}
\Longrightarrow
G_{spatial\ covariance}
\lor
G_{recurrent-phase\ covariance}.
}
\]

The first gives

\[
\boxed{
G_{spatial\ covariance}
\Longrightarrow
G_{gradient/interface}
\lor
\mathcal R_{remote/critical},
}
\]

while the second gives

\[
\boxed{
G_{phase\ covariance}
\Longrightarrow
G_{temporal\ transition/time\text{-}jet}
\lor
G_{recurrent\ hysteresis}.
}
\]

No new fourth upstream root is introduced.

## 11. Audit verdict

### Certified

1. The mandatory multi-p covariance splits exactly into within-state spatial covariance plus between-state recurrent-phase covariance.
2. Spatial connectivity may be invoked only on the first branch.
3. Bounded-core spatial segregation routes to amplitude/strain/coefficient gradients or zero/interface loss.
4. Remote spatial segregation routes to existing remote/critical exits.
5. Phase segregation is equivalent to covariance between amplitude concentration and p-moment logarithmic growth rate.
6. Temporal recurrence can support this covariance through hysteretic cycles, so it is not itself contradictory.

### Still open

- quantitative transition thickness in the spatial branch without falling into zero/interface loss;
- a finite budget for temporal transition/time-jet cycles;
- exclusion of recurrent hysteresis after all source/sink identities;
- ancestry closure of derivative/interface payers;
- remote/critical roots;
- global regularity.

## 12. Next target

The most promising branch after this split is the **bounded-core spatial covariance** branch, because it can potentially be converted to an ordinary derivative resource with existing exact ledgers.

M18-065 should derive a quantitative Poincare/transition lower bound: if a fixed ball contains positive weighted mass in two amplitude-growth populations separated by fixed value gaps, what is the minimum

\[
\int_{B_L}\rho^{p-2}|\nabla\rho|^2,
\quad
\int_{B_L}\rho^p|\nabla h|^2,
\]

or related partition-safe interface cost?

The derivation must retain the zero-set and component-separation escape rather than assuming a connected high-amplitude path.