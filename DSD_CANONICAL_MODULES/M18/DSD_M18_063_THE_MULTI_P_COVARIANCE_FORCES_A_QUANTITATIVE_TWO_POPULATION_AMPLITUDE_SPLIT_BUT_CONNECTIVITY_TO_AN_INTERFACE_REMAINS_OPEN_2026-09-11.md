# M18-063 — Multi-p covariance forces a quantitative two-population amplitude split, but connectivity to an interface remains open

**Date:** 2026-09-11  
**Status:** QUANTITATIVE POPULATION SEPARATION / TOTAL-VARIATION LOWER BOUND / CONNECTIVITY FIREWALL

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Purpose

M18-062 proves, for every \(q>p\ge2\),

\[
\boxed{
\mathbb E_q[h]-\mathbb E_p[h]
=\delta_{pq}
:=
\frac32\left(\frac1p-\frac1q\right)>0,
}
\]

where

\[
h:=\sigma+\kappa
\]

and \(\mathbb P_p\) is the joint recurrent hull/space probability measure weighted by \(\rho^p\).

The present module turns this expectation shift into a quantitative separation of the underlying amplitude populations.

The result is an invariant-measure two-population theorem. It does **not** yet prove that the populations are connected through one spatial/material interface; that remains the next firewall.

## 2. Compact growth-field bound

On the retained compact CE-H hull, \(\sigma\) and \(\kappa\) are bounded on the active recurrent support.

Fix

\[
\boxed{|h|\le H_*<\infty.}
\]

No smallness is assumed.

## 3. Total-variation separation forced by the growth-mean shift

For probability measures \(P,Q\) and a bounded observable \(|f|\le H_*\),

\[
|\mathbb E_Qf-\mathbb E_Pf|
\le
2H_*\|Q-P\|_{TV},
\]

where

\[
\|Q-P\|_{TV}:=\sup_A|Q(A)-P(A)|.
\]

Apply this with

\[
P=\mathbb P_p,
\qquad
Q=\mathbb P_q,
\qquad
f=h.
\]

M18-062 gives the left side exactly as \(\delta_{pq}\). Therefore

\[
\boxed{
\|\mathbb P_q-\mathbb P_p\|_{TV}
\ge
\frac{\delta_{pq}}{2H_*}.
}
\]

Thus the higher-amplitude and lower-amplitude weighted populations cannot become statistically indistinguishable.

## 4. The Radon--Nikodym derivative is monotone in amplitude

M18-062 gives

\[
\boxed{
\frac{d\mathbb P_q}{d\mathbb P_p}
=
L(\rho)
:=
\frac{\rho^{q-p}}{\mathbb E_p[\rho^{q-p}]}.
}
\]

This likelihood ratio is monotone increasing in \(\rho\).

Define the intrinsic amplitude threshold

\[
\boxed{
a_{pq}
:=
\left(\mathbb E_p[\rho^{q-p}]\right)^{1/(q-p)}.
}
\]

Then

\[
L(\rho)\ge1
\quad\Longleftrightarrow\quad
\rho\ge a_{pq}.
\]

For two absolutely continuous measures, a Hahn maximizing set for total variation is

\[
\{L\ge1\}.
\]

Hence the total variation is realized by the **single amplitude threshold set**

\[
\boxed{
A_{hi}:=\{\rho\ge a_{pq}\}.
}
\]

Its complement is

\[
A_{lo}:=\{\rho<a_{pq}\}.
\]

## 5. Quantitative two-population split

Therefore

\[
\mathbb P_q(A_{hi})-\mathbb P_p(A_{hi})
=
\|\mathbb P_q-\mathbb P_p\|_{TV}
\ge
\frac{\delta_{pq}}{2H_*}.
\]

Define

\[
\boxed{
\varepsilon_{pq}
:=
\frac{\delta_{pq}}{2H_*}>0.
}
\]

Then

\[
\boxed{
\mathbb P_q(A_{hi})
-
\mathbb P_p(A_{hi})
\ge\varepsilon_{pq}.
}
\]

In particular,

\[
\boxed{
\mathbb P_q(A_{hi})\ge\varepsilon_{pq}.
}
\]

Also

\[
\begin{aligned}
\mathbb P_p(A_{lo})
&=1-\mathbb P_p(A_{hi})\\
&=1-\mathbb P_q(A_{hi})
+\big(\mathbb P_q(A_{hi})-\mathbb P_p(A_{hi})\big)\\
&\ge\varepsilon_{pq}.
\end{aligned}
\]

Hence

\[
\boxed{
\mathbb P_q(\rho\ge a_{pq})\ge\varepsilon_{pq},
\qquad
\mathbb P_p(\rho<a_{pq})\ge\varepsilon_{pq}.
}
\]

The recurrent component contains quantitatively non-negligible high- and low-amplitude populations.

## 6. Growth-field populations are also separated

Set

\[
m_{pq}:=\frac{c_p+c_q}{2}.
\]

Because

\[
\mathbb E_q[h]=m_{pq}+\frac{\delta_{pq}}2,
\qquad
\mathbb E_p[h]=m_{pq}-\frac{\delta_{pq}}2,
\]

and \(|h|\le H_*\), a simple extremal estimate gives

\[
\boxed{
\mathbb P_q(h\ge m_{pq})
\ge
\frac{\delta_{pq}}{4H_*},
}
\]

and

\[
\boxed{
\mathbb P_p(h\le m_{pq})
\ge
\frac{\delta_{pq}}{4H_*}.
}
\]

Thus the recurrent ensemble also contains positive-measure high-growth and low-growth populations.

These marginal facts are consistent with, but do not by themselves prove, that the high-amplitude and high-growth subsets coincide pointwise.

## 7. Covariance supplies the coupling, but not spatial connectivity

The exact identity

\[
\operatorname{Cov}_p(h,\rho^{q-p})
=
\delta_{pq}\mathbb E_p[\rho^{q-p}]>0
\]

shows that the two separations are statistically coupled: the amplitude tilt toward high \(\rho\) raises the mean of \(h\).

However positive covariance alone does not prove that there exists one connected material tube or one fixed time slice containing both

\[
\rho<a_{pq},\ h\lesssim c_p
\]

and

\[
\rho>a_{pq},\ h\gtrsim c_q.
\]

The two populations could, in principle, be carried by different spatial components, different material lineages, or different recurrent phases.

This distinction is essential.

## 8. Connectivity alternatives

The quantitative population split therefore produces the following next dichotomy.

### A. Connected transition

A fixed positive fraction of the low/high populations is joined inside a coherent spatial/material component over a bounded normalized distance/time.

Then the fixed value separation can be converted, after the existing regularity/thickness arguments, into at least one of

\[
\boxed{
\nabla\rho,
\quad
\nabla\sigma,
\quad
\nabla\kappa,
\quad
\text{threshold/interface current}
}
\]

payments.

These feed the existing palinstrophy, director-geometry, coefficient-gradient, threshold, and zero-corridor branches.

### B. Persistent disconnected segregation

The low/high populations remain separated into distinct spatial/material components or recurrent phases without a bounded transition path.

Then the obstruction is no longer a hidden gradient payer. It is a genuine

\[
\boxed{
G_{component/interface/genealogy\ segregation}
}
\]

branch.

This is already a typed exit in the late M17/M18 tree.

## 9. Relation to the ancestry firewall

Even in the connected case, a fixed normalized gradient/interface payment is not automatically a global contradiction.

M18-058--059 remain in force:

- palinstrophy/raw-H2/D3 have derivative ancestry weights but no finite original-parent total with the required homogeneity;
- standard-energy descent produces a summable chronological factor unless extra growth is proved.

Thus M18-063 improves **classification and formation**, not ancestry economics.

## 10. Audit verdict

### Certified

1. The \(p\)- and \(q\)-weighted recurrent populations have a fixed total-variation separation:
   \[
   \|\mathbb P_q-\mathbb P_p\|_{TV}
   \ge\delta_{pq}/(2H_*).
   \]
2. The maximizing Hahn set is an amplitude threshold because the likelihood ratio is monotone in \(\rho\).
3. Therefore both a high-amplitude \(q\)-population and a low-amplitude \(p\)-population have fixed positive recurrent measure.
4. High-growth and low-growth populations likewise have positive recurrent measure.
5. The exact covariance couples amplitude and growth statistically.

### Firewall

The covariance does not certify a bounded spatial/material path connecting the populations.

Therefore

\[
\boxed{
\text{population separation}
\Longrightarrow
\text{connected derivative/interface payer}
\lor
\text{component/genealogy segregation}.
}
\]

### Still open

- a quantitative connectivity theorem;
- ancestry closure of connected-transition payers;
- closure of persistent component/genealogy segregation;
- remote and critical roots;
- global regularity.

## 11. Next target

M18-064 should audit **connectivity from analyticity and first-hitting core geometry**.

The key question is whether the positive-measure amplitude populations can remain indefinitely disconnected inside the same nontrivial analytic recurrent component, or whether connectedness of \(\mathbb R^3\), analyticity of \(W\), and the coherent carrier construction force an actual transition corridor on a positive-density subset.

Any such corridor would turn the abstract covariance into a concrete gradient/interface event.