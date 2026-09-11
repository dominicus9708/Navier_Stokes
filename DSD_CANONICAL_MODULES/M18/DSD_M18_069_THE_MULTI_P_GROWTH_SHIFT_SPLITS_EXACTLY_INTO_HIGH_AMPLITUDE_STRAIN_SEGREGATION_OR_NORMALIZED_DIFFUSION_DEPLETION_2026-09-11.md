# M18-069 — The multi-p growth shift splits exactly into high-amplitude strain segregation or normalized diffusion depletion

**Date:** 2026-09-11  
**Status:** KAPPA / DIFFUSION RATIO IDENTIFICATION / STRAIN-VERSUS-DIFFUSIVE-SHEATH DICHOTOMY / MATERIAL RESIDENCE INTERPRETATION

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Purpose

M18-062 proves the exact multi-\(p\) growth shift

\[
\mathbb E_q[\sigma+\kappa]
-
\mathbb E_p[\sigma+\kappa]
=
\delta_{pq}
:=
\frac32\left(\frac1p-\frac1q\right)>0
\]

for every finite \(q>p\ge2\).

M18-068 identifies the same hierarchy with generalized material flux-line residence.

The present module separates the growth shift into its strain and coefficient pieces.

The key observation is that the \(p\)-weighted mean of \(\kappa\) is exactly minus the normalized weighted diffusion rate.

Therefore positive high-amplitude \(\kappa\) covariance is not an independent recharge source: it is exactly a **decrease of normalized diffusion under higher-amplitude weighting**.

This yields the sharp dichotomy

\[
\boxed{
\text{high-amplitude strain segregation}
\quad\lor\quad
\text{high-amplitude normalized-diffusion depletion}.
}
\]

## 2. Normalized weighted diffusion rate

M18-060 defines

\[
D_p
=
\int\rho^{p-2}|\nabla W|^2dy
+(p-2)\int\rho^{p-2}|\nabla\rho|^2dy
\]

and proves pointwise in time

\[
\int\kappa\rho^pdy=-D_p.
\]

On the invariant recurrent component define

\[
\boxed{
 d_p
 :=
 \frac{\langle D_p\rangle}
 {\langle M_p\rangle}
 \ge0.
}
\]

With the joint recurrent \(p\)-weighted probability measure \(\mathbb P_p\),

\[
\boxed{
\mathbb E_p[\kappa]
=-d_p.
}
\]

Thus \(d_p\) is the exact recurrent normalized diffusion rate seen by the \(p\)-amplitude population.

## 3. Exact kappa change-of-measure identity

Let

\[
q>p\ge2,
\qquad
w:=\rho^{q-p}.
\]

M18-062 gives the change of measure

\[
\mathbb E_q[f]
=
\frac{\mathbb E_p[fw]}{\mathbb E_p[w]}.
\]

Hence

\[
\operatorname{Cov}_p(f,w)
=
\mathbb E_p[w]
\left(
\mathbb E_q[f]-\mathbb E_p[f]
\right).
\]

Apply this to \(f=\kappa\):

\[
\begin{aligned}
\operatorname{Cov}_p(\kappa,w)
&=
\mathbb E_p[w]
\left(-d_q+d_p\right).
\end{aligned}
\]

Therefore

\[
\boxed{
\operatorname{Cov}_p
\left(\kappa,\rho^{q-p}\right)
=
(d_p-d_q)
\mathbb E_p[\rho^{q-p}].
}
\]

This identity is exact.

Consequently,

\[
\boxed{
\operatorname{Cov}_p(\kappa,\rho^{q-p})>0
\iff
d_q<d_p.
}
\]

A positive coefficient/amplitude covariance means exactly that the higher-amplitude population sees a **less negative mean \(\kappa\)**, equivalently a smaller normalized diffusion rate.

## 4. Exact strain change-of-measure identity

M18-062 gives

\[
\operatorname{Cov}_p(\sigma+\kappa,w)
=
\delta_{pq}\mathbb E_p[w].
\]

Subtract Section 3:

\[
\boxed{
\operatorname{Cov}_p(\sigma,w)
=
\left(
\delta_{pq}+d_q-d_p
\right)
\mathbb E_p[w].
}
\]

Equivalently,

\[
\boxed{
\mathbb E_q[\sigma]
-
\mathbb E_p[\sigma]
=
\delta_{pq}+d_q-d_p.
}
\]

Thus the universal growth shift \(\delta_{pq}\) is partitioned exactly between

- increased strain seen by higher amplitude;
- decreased normalized diffusion seen by higher amplitude.

## 5. Canonical half-gap dichotomy

There are two exhaustive cases.

### A. Diffusion does not fall by more than half the universal shift

If

\[
d_p-d_q
\le
\frac{\delta_{pq}}2,
\]

then

\[
\boxed{
\mathbb E_q[\sigma]
-
\mathbb E_p[\sigma]
\ge
\frac{\delta_{pq}}2.
}
\]

Equivalently,

\[
\boxed{
\operatorname{Cov}_p
(\sigma,\rho^{q-p})
\ge
\frac{\delta_{pq}}2
\mathbb E_p[\rho^{q-p}].
}
\]

Call this

\[
\boxed{G_{strain\text{-}seg}^{pq}.}
\]

### B. Diffusion falls by more than half the universal shift

If

\[
d_p-d_q
>
\frac{\delta_{pq}}2,
\]

then

\[
\boxed{
\operatorname{Cov}_p
(\kappa,\rho^{q-p})
>
\frac{\delta_{pq}}2
\mathbb E_p[\rho^{q-p}]
}
\]

and

\[
\boxed{
 d_q
 <
 d_p-rac{\delta_{pq}}2.
}
\]

Call this

\[
\boxed{G_{diff\text{-}depletion}^{pq}.}
\]

Therefore

\[
\boxed{
G_{multi-p\ growth}
\Longrightarrow
G_{strain\text{-}seg}^{pq}
\lor
G_{diff\text{-}depletion}^{pq}.
}
\]

## 6. Diffusion density in amplitude/director variables

Use

\[
W=\rho\xi,
\qquad |\xi|=1.
\]

Then

\[
|\nabla W|^2
=
|\nabla\rho|^2
+\rho^2|\nabla\xi|^2.
\]

Hence

\[
\boxed{
D_p
=
(p-1)
\int\rho^{p-2}|\nabla\rho|^2dy
+
\int\rho^p|\nabla\xi|^2dy.
}
\]

On the active set define

\[
\boxed{
G_p
:=
(p-1)|\nabla\log\rho|^2
+|\nabla\xi|^2.
}
\]

Then, in the weighted sense,

\[
\boxed{
 d_p
 =
 \mathbb E_p[G_p].
}
\]

The expression is legitimate even though \(\log\rho\) is undefined on \(\rho=0\), because \(\mathbb P_p\) gives zero density there and the weighted numerator is exactly the finite \(D_p\) integral.

## 7. High-amplitude diffusion depletion forces negative amplitude/diffusion covariance

For \(q>p\),

\[
G_q
=
G_p
+(q-p)|\nabla\log\rho|^2
\ge
G_p.
\]

Therefore

\[
\mathbb E_q[G_p]
\le
\mathbb E_q[G_q]
=d_q.
\]

If Branch B holds with

\[
\varepsilon_{pq}
:=
d_p-d_q
>
\frac{\delta_{pq}}2,
\]

then

\[
\mathbb E_q[G_p]
<
\mathbb E_p[G_p]-\varepsilon_{pq}.
\]

Using the change-of-measure formula once more,

\[
\boxed{
\operatorname{Cov}_p
\left(
G_p,\rho^{q-p}
\right)
\le
-\varepsilon_{pq}
\mathbb E_p[\rho^{q-p}]
<0.
}
\]

Thus the diffusion-depletion branch has a precise meaning:

\[
\boxed{
\text{higher-amplitude populations carry smaller normalized}
\;
[(p-1)|\nabla\log\rho|^2+|\nabla\xi|^2]
\text{ on average}.
}
\]

The missing diffusion has not disappeared. It has been displaced toward the lower-amplitude population.

## 8. Diffusive-sheath interpretation

For \(p=2\),

\[
G_2
=
|\nabla\log\rho|^2
+|\nabla\xi|^2
=
\frac{|\nabla W|^2}{\rho^2}
\quad(\rho>0).
\]

Hence Branch B says that increasing the amplitude weight from enstrophy toward higher moments lowers the normalized palinstrophy density.

Schematically,

\[
\boxed{
\text{high-amplitude core: lower normalized diffusion}
\quad\text{and}\quad
\text{lower-amplitude residence/sheath: higher normalized diffusion}.
}
\]

This is a **diffusive-sheath ordering**, not a contradiction.

It is compatible with the late M17 picture in which gradient/coefficient activity can live in a lower-amplitude transition or zero corridor surrounding a smoother active core.

## 9. Material-tube interpretation

M18-068 gives

\[
M_p
=
\int L_{p-1}\,d|\Phi|.
\]

Since \(\kappa\) is constant along each CE-H vortex line,

\[
\mathbb E_p[\kappa]
=
\frac{
\left\langle
\int\kappa L_{p-1}d|\Phi|
\right\rangle
}{
\left\langle
\int L_{p-1}d|\Phi|
\right\rangle
}.
\]

Therefore

\[
\boxed{
 d_p
 =
 -
\frac{
\left\langle
\int\kappa L_{p-1}d|\Phi|
\right\rangle
}{
\left\langle
\int L_{p-1}d|\Phi|
\right\rangle
}.
}
\]

The inequality

\[
d_q<d_p
\]

means that the negative \(\kappa\) debt becomes weaker when the tube ensemble is reweighted from total \(p\)-residence toward stronger high-amplitude concentration.

Thus the negative coefficient debt is preferentially carried by the less concentrated / lower-amplitude residence population.

## 10. Relation to M16-021

For \(p=2\),

\[
L_{p-1}=L_1=L_\rho.
\]

On the flux-neutral branch of M16-021,

\[
\mathbb E_{\Phi}[\kappa]=0
\]

but

\[
\mathbb E_{2}[\kappa]
=
-d_2<0
\]

because the flux measure is reweighted by \(L_1\).

This is exactly the negative covariance

\[
\operatorname{Cov}_{\Phi}(\kappa,L_1)<0.
\]

If Branch B of the present module also holds, then

\[
\mathbb E_q[\kappa]
>
\mathbb E_2[\kappa].
\]

So the same flux-neutral survivor has the ordered means

\[
\boxed{
0
=
\mathbb E_{\Phi}[\kappa]
>
\mathbb E_q[\kappa]
>
\mathbb E_2[\kappa]
}
\]

when the inequalities are strict and \(d_q>0\).

The interpretation is precise:

- flux weighting is neutral in \(\kappa\);
- enstrophy/\(L_1\) weighting sees the strongest negative \(\kappa\) debt;
- stronger high-amplitude weighting sees a less negative coefficient mean.

Therefore the negative debt is concentrated in a lower-amplitude/high-residence sheath rather than the highest-amplitude core.

This is consistent, not contradictory.

## 11. Strain-segregation branch routing

On Branch A,

\[
\operatorname{Cov}_p(\sigma,\rho^{q-p})>0
\]

with a fixed quantitative floor.

M18-064--065 and M18-068 already give the correct refinement:

- within one controlled vortex line/component, this forces same-line axial strain heterogeneity and hence strain-gradient/director/turnover activity;
- if it is carried only between components, lineages, or recurrent phases, it is a typed component/genealogy/phase-segregation branch;
- if it escapes every fixed core, it is remote/critical.

No new source currency is created.

## 12. Diffusion-depletion branch routing

Branch B gives the fixed negative covariance

\[
\operatorname{Cov}_p(G_p,\rho^{q-p})<0.
\]

This means amplitude and normalized diffusion are obligatorily segregated.

There are again two geometric realizations.

### Connected active-core/sheath realization

If high- and low-amplitude populations occur in one controlled component, then the lower-amplitude side carries a larger normalized gradient/director burden.

This routes to

\[
\boxed{
G_{amplitude\ transition}
\lor
G_{director\ transition}
\lor
G_{zero/interface\ sheath}.
}
\]

### Disconnected realization

If the populations live on distinct components/lineages/phases, the branch is

\[
\boxed{
G_{component/genealogy/phase\ diffusive\ segregation}.
}
\]

Again, this is a classification result rather than a finite-budget contradiction.

## 13. Why no monotonicity theorem follows

The sequence \(d_p\) need not be monotone in \(p\).

The weight \(\rho^p\) and the integrand \(G_p\) both change with \(p\).

The present theorem therefore does **not** claim

\[
d_q\le d_p
\quad\text{for all }q>p.
\]

It says only that, for each pair \(p<q\), the mandatory growth shift forces either

- enough positive strain covariance, or
- a quantitatively significant fall of \(d_p\) to \(d_q\).

This pairwise dichotomy is exact and sufficient for branch routing.

## 14. Audit verdict

### Certified

1. \(\mathbb E_p[\kappa]=-d_p\), where
   \[
   d_p=\langle D_p\rangle/\langle M_p\rangle.
   \]
2. The coefficient covariance is exactly
   \[
   \operatorname{Cov}_p(\kappa,\rho^{q-p})
   =(d_p-d_q)\mathbb E_p[\rho^{q-p}].
   \]
3. The strain covariance is exactly
   \[
   \operatorname{Cov}_p(\sigma,\rho^{q-p})
   =(\delta_{pq}+d_q-d_p)\mathbb E_p[\rho^{q-p}].
   \]
4. Therefore every pair \(p<q\) satisfies the quantitative strain-segregation / diffusion-depletion dichotomy.
5. On the diffusion-depletion branch,
   \[
   \operatorname{Cov}_p(G_p,\rho^{q-p})<0
   \]
   with a fixed lower magnitude.
6. For \(p=2\), combining with M16-021 orders the flux-, high-amplitude-, and enstrophy-weighted \(\kappa\) means and locates the negative debt preferentially in lower-amplitude residence/sheath structure.

### Not certified

- monotonicity of \(d_p\) for all \(p\);
- a finite resource consumed by the diffusive-sheath ordering;
- compulsory same-component connectivity of the segregated populations;
- ancestry closure of the resulting gradient/interface events;
- remote/critical closure;
- global regularity.

## 15. Next target

The diffusion-depletion branch now has an exact fixed observable

\[
G_p=(p-1)|\nabla\log\rho|^2+|\nabla\xi|^2
\]

with negative amplitude covariance.

M18-070 should convert this covariance into a **truncated two-population theorem without assuming \(G_p\in L^\infty\)**.

The correct tool is a layer-cake/truncation argument: choose a finite diffusion threshold \(K\) so that a fixed portion of the negative covariance is already visible in the bounded observable

\[
G_p^{(K)}:=\min\{G_p,K\}.
\]

If no finite \(K\) captures a fixed fraction, then the covariance is carried by an arbitrarily high normalized-diffusion tail, which is itself a stronger derivative/concentration branch.

This would distinguish a controlled low-amplitude diffusive sheath from a high-gradient tail escape without introducing an illegitimate \(L^\infty\) bound on \(G_p\).
