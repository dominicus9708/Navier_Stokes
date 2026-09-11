# M18-065 — Within-state covariance forces two active-core populations and hence a transition gradient or component/zero-interface degeneration

**Date:** 2026-09-11  
**Status:** SPATIAL-COVARIANCE FORMATION / ACTIVE-CORE LOCALIZATION / CONDITIONAL POINCARE TRANSITION

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Purpose

M18-064 splits the exact multi-p covariance into

\[
C_{space}^{pq}+C_{phase}^{pq}
=
\delta_{pq}\mathbb E_p[\rho^{q-p}]>0.
\]

The present module develops the spatial branch

\[
\boxed{C_{space}^{pq}>0.}
\]

The goal is to determine what can be formed **inside one snapshot** without assuming an interface by fiat.

The conclusion is:

\[
\boxed{
\text{within-state covariance}
\Longrightarrow
\text{two separated active-core populations}
\Longrightarrow
\text{controlled transition gradient}
\lor
\text{component/zero/thin-neck degeneration}.
}
\]

The second implication is conditional on a controlled connected active component; failure of that control is retained explicitly.

## 2. Conditional p- and q-weighted measures inside one state

For a state \(Y\), define

\[
d\pi_{p,Y}(y)
=
\frac{\rho_Y(y)^p}{M_p(Y)}dy,
\]

and similarly

\[
d\pi_{q,Y}(y)
=
\frac{\rho_Y(y)^q}{M_q(Y)}dy.
\]

Let

\[
\bar h_{p,Y}:=\int h\,d\pi_{p,Y},
\qquad
\bar h_{q,Y}:=\int h\,d\pi_{q,Y},
\]

where

\[
h=\sigma+\kappa.
\]

For that fixed state,

\[
\boxed{
\bar h_{q,Y}-\bar h_{p,Y}
=
\frac{\operatorname{Cov}_{\pi_{p,Y}}(h,\rho^{q-p})}
{\mathbb E_{\pi_{p,Y}}[\rho^{q-p}]}.
}
\]

Thus positive spatial covariance is equivalent to a higher-amplitude-weighted mean growth field inside the same snapshot.

## 3. Extract a positive-measure state family with a fixed conditional gap

M18-064 gives

\[
C_{space}^{pq}
=
\mathbb E_{\nu_p}
\left[
\operatorname{Cov}_{\pi_{p,Y}}(h,\rho^{q-p})
\right].
\]

Assume

\[
C_{space}^{pq}>0.
\]

For each nonzero state define

\[
\delta_Y
:=
\bar h_{q,Y}-\bar h_{p,Y},
\]

and

\[
\bar w_Y
:=
\frac{M_q(Y)}{M_p(Y)}>0.
\]

Then

\[
C_{space}^{pq}
=
\mathbb E_{\nu_p}[\bar w_Y\delta_Y].
\]

A positive integral of this measurable function implies, by countable-level decomposition, that there exist constants

\[
\boxed{
\delta_*>0,
\qquad
w_*>0,
\qquad
m_*>0
}
\]

and a state set

\[
\boxed{\mathcal Y_*}
\]

of positive \(\nu_p\)-measure such that for every \(Y\in\mathcal Y_*\),

\[
\boxed{
\delta_Y\ge\delta_*,
\qquad
\bar w_Y\ge w_*,
\qquad
M_p(Y)\ge m_*.
}
\]

Consequently

\[
M_q(Y)
\ge
w_*m_*.
\]

This step does not assert universal constants independent of the chosen ergodic component. It extracts fixed positive constants on one positive-measure recurrent subfamily.

## 4. Two growth-field populations in every selected snapshot

Fix \(Y\in\mathcal Y_*\).

Set

\[
a_Y:=\bar h_{p,Y},
\qquad
b_Y:=\bar h_{q,Y},
\]

so

\[
b_Y-a_Y\ge\delta_*.
\]

Define thresholds

\[
h_-^Y:=a_Y+\frac{\delta_*}{4},
\]

and

\[
h_+^Y:=b_Y-\frac{\delta_*}{4}.
\]

Then

\[
\boxed{
h_+^Y-h_-^Y\ge\frac{\delta_*}{2}.}
\]

Let

\[
E_-^Y:=\{h\le h_-^Y\},
\qquad
E_+^Y:=\{h\ge h_+^Y\}.
\]

If \(|h|\le H_*\), the elementary extremal estimate for a bounded random variable gives

\[
\boxed{
\pi_{p,Y}(E_-^Y)
\ge
\frac{\delta_*}{8H_*},
}
\]

and

\[
\boxed{
\pi_{q,Y}(E_+^Y)
\ge
\frac{\delta_*}{8H_*}.
}
\]

Thus every selected snapshot contains two positive weighted populations whose net-growth values are separated by a fixed gap.

## 5. Convert weighted mass to physical spatial measure

On the compact hull,

\[
0\le\rho\le M_*.
\]

The low-growth set satisfies

\[
\int_{E_-^Y}\rho^pdy
\ge
\frac{\delta_*}{8H_*}M_p(Y)
\ge
\frac{\delta_*m_*}{8H_*}.
\]

Hence

\[
\boxed{
|E_-^Y|
\ge
\frac{\delta_*m_*}{8H_*M_*^p}.
}
\]

Similarly,

\[
\int_{E_+^Y}\rho^qdy
\ge
\frac{\delta_*}{8H_*}M_q(Y)
\ge
\frac{\delta_*w_*m_*}{8H_*},
\]

so

\[
\boxed{
|E_+^Y|
\ge
\frac{\delta_*w_*m_*}{8H_*M_*^q}.
}
\]

Thus the populations are not merely probability-weight artifacts; they occupy positive Lebesgue measure.

## 6. Localize both populations to one fixed core ball

The retained compact tight hull has uniform vorticity \(L^2\) tail tightness:

\[
\sup_Y
\int_{|y|>L}\rho^2dy
\to0
\qquad(L\to\infty).
\]

For \(r\ge2\),

\[
\int_{|y|>L}\rho^rdy
\le
M_*^{r-2}
\int_{|y|>L}\rho^2dy.
\]

Choose one fixed \(L\) large enough that the p- and q-weighted tail mass is smaller than half of the lower bounds in Section 5.

Then after replacing \(E_\pm^Y\) by

\[
E_{\pm,L}^Y:=E_\pm^Y\cap B_L,
\]

both sets retain fixed positive weighted and Lebesgue measure, uniformly for \(Y\in\mathcal Y_*\).

Therefore the spatial covariance branch is genuinely a **bounded-core two-population branch** unless tail tightness itself fails, in which case it is routed to \(\mathcal R_{remote/critical}\).

## 7. Remove the zero-amplitude ambiguity or record it explicitly

The coefficient \(\kappa\) and hence \(h=\sigma+\kappa\) are naturally an active-set variable.

Choose \(a_0>0\) small.

Inside the fixed ball,

\[
\int_{\{\rho<a_0\}}\rho^pdy
\le
|B_L|a_0^p,
\]

and similarly for \(q\).

Choose \(a_0\) so that these contributions are smaller than half of the retained weighted masses of both populations.

Then each selected state contains positive-measure subsets

\[
\boxed{
F_-^Y
\subset
E_{-,L}^Y\cap\{\rho\ge a_0\},
}
\]

and

\[
\boxed{
F_+^Y
\subset
E_{+,L}^Y\cap\{\rho\ge a_0\}.
}
\]

Hence both populations can be chosen inside the regular active region.

If no such fixed \(a_0\) can be retained in a branch under refinement, that branch is precisely amplitude/nodal depletion and is recorded separately.

## 8. Active-component connectivity split

Consider the superlevel set

\[
\mathcal A_{a_0}(Y)
:=
\{y\in B_L:\rho(y)\ge a_0\}.
\]

There are two possibilities.

### A. Controlled connected component

Positive fractions of \(F_-^Y\) and \(F_+^Y\) lie in one connected component \(C_Y\subset\mathcal A_{a_0}(Y)\) whose geometry admits a record-uniform Poincare constant

\[
\boxed{
\int_{C_Y}|f-f_{C_Y}|^2
\le
C_P L^2
\int_{C_Y}|\nabla f|^2.
}
\]

This includes ordinary uniformly Lipschitz/John-type coherent carrier geometries already used elsewhere in the repository.

### B. Connectivity/geometric degeneration

No such uniformly controlled component carries fixed fractions of both populations.

Then the branch exhibits at least one of

\[
\boxed{
\text{component segregation},
\quad
\text{thin-neck degeneration},
\quad
\rho\downarrow0\text{ between populations},
\quad
\text{carrier/interface/domain loss}.
}
\]

These are already typed exits.

This branch must not be hidden inside a Poincare estimate.

## 9. Quantitative transition-gradient floor on the controlled branch

Assume Branch A.

Let \(A,B\subset C_Y\) denote the retained low- and high-growth subsets with

\[
|A|\ge v_->0,
\qquad
|B|\ge v_+>0,
\]

and

\[
h|_A\le h_-^Y,
\qquad
h|_B\ge h_+^Y,
\]

with

\[
h_+^Y-h_-^Y\ge\frac{\delta_*}{2}.
\]

The pairwise-variance identity gives

\[
\int_{C_Y}|h-h_{C_Y}|^2dy
=
\frac1{2|C_Y|}
\int_{C_Y}\int_{C_Y}|h(x)-h(z)|^2dxdz.
\]

Restrict the double integral to \(A\times B\) and \(B\times A\):

\[
\boxed{
\int_{C_Y}|h-h_{C_Y}|^2dy
\ge
\frac{|A||B|}{|C_Y|}
\left(\frac{\delta_*}{2}\right)^2.
}
\]

The Poincare inequality therefore yields

\[
\boxed{
\int_{C_Y}|\nabla h|^2dy
\ge
c_{trans}>0,
}
\]

where \(c_{trans}\) depends only on the extracted population floors, \(L\), and the uniform carrier Poincare constant.

Thus a controlled same-component realization of the covariance pays a fixed normalized transition-gradient charge.

## 10. Split the growth-field gradient

Since

\[
h=\sigma+\kappa,
\]

\[
|\nabla h|^2
\le
2|\nabla\sigma|^2+2|\nabla\kappa|^2.
\]

Therefore

\[
\boxed{
\int_{C_Y}|\nabla\sigma|^2dy
\ge\frac{c_{trans}}4
\quad\lor\quad
\int_{C_Y}|\nabla\kappa|^2dy
\ge\frac{c_{trans}}4.
}
\]

### Strain-gradient branch

The aligned eigenvalue derivative obeys

\[
|\nabla\sigma|\le|\nabla\Sigma|,
\]

and for divergence-free velocity

\[
\|\nabla\Sigma\|_2^2
=\frac12\|\nabla W\|_2^2.
\]

Thus

\[
\boxed{
G_{\nabla\sigma}
\Longrightarrow
G_{palinstrophy}.
}
\]

### Coefficient-gradient branch

On \(C_Y\subset\{\rho\ge a_0\}\),

\[
\int_{C_Y}\rho^2|\nabla\kappa|^2dy
\ge
 a_0^2
\int_{C_Y}|\nabla\kappa|^2dy.
\]

Hence

\[
\boxed{
G_{\nabla\kappa}
\Longrightarrow
G_{weighted\ coefficient\ gradient}.
}
\]

This is the existing first-coefficient-jet channel.

## 11. Resulting routing theorem

The within-state covariance branch is therefore reduced to

\[
\boxed{
\begin{aligned}
G_{spatial\ covariance}
\Longrightarrow{}&
G_{palinstrophy}\\
&\lor G_{weighted\ coefficient\ gradient}\\
&\lor G_{component/thin\text{-}neck/zero/interface}\\
&\lor\mathcal R_{remote/critical}.
\end{aligned}
}
\]

The abstract amplitude-growth covariance is thus converted into existing derivative/geometric currencies whenever a controlled active transition corridor forms.

## 12. What this does not prove

This does not close the ancestry of palinstrophy or coefficient-gradient payments.

It also does not show that every analytic superlevel component has a uniform Poincare constant. Thin necks and component splitting are genuine geometric exits.

Analyticity alone prevents arbitrary open-set pathology but does not supply a scale-uniform quantitative connectivity constant.

Therefore

\[
\boxed{
\text{analyticity}
\neq
\text{uniform carrier connectivity}.
}
\]

## 13. Audit verdict

### Certified

1. Positive within-state covariance yields a positive-measure recurrent subfamily with a fixed conditional p-to-q growth gap.
2. Each selected snapshot contains two same-time growth populations of fixed positive weighted/Lebesgue measure.
3. Tail tightness localizes them into one fixed normalized core ball unless the remote root activates.
4. Both populations can be retained above a fixed amplitude floor unless nodal depletion activates.
5. If they share a uniformly controlled active component, a fixed \(L^2\) transition-gradient charge follows.
6. That charge routes to palinstrophy or weighted coefficient gradient.
7. Failure of controlled connectivity is explicitly component/thin-neck/zero/interface degeneration.

### Still open

- closure of component/thin-neck/zero-interface degeneration;
- ancestry closure of palinstrophy/coefficient-gradient payments;
- the recurrent-phase covariance branch of M18-064;
- remote and critical roots;
- global regularity.

## 14. Next target

M18-066 should treat the **recurrent-phase covariance** branch.

The key state relation is

\[
\bar h_p-c_p
=\frac1p\frac{d}{d\theta}\log M_p.
\]

One should derive an exact evolution equation for the amplitude-concentration ratio

\[
\mathcal C_{pq}
:=
\frac{M_q^{1/q}}{M_p^{1/p}}
\]

and audit whether the positive phase covariance forces recurrent concentration/deconcentration cycles with a fixed total-variation cost, or whether those cycles are another freely rechargeable compact-hull path functional.