# M19-036 — Finite-lineage marginals do not force same-event alignment, and anti-phase recycling requires a PDE transfer law

**Date:** 2026-09-11  
**Status:** CALCULATION / R-AC CORRELATION FIREWALL / TWO-LINEAGE ANTI-PHASE MODEL / PDE-TRANSFER NECESSITY

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Purpose

M19-034 reduces the remaining ancestry-conversion problem to a same-event correlation theorem.  Spatial shell occupancy and ancestral temporal return are separately available only at weak scale fractions, and their naive product is worse:

\[
K^{-1}\cdot K^{-2}=K^{-3}.
\]

The question here is whether the finite number of persistent lineage labels alone forces the two marginals to align on one lineage.

The answer is no.

## 2. Abstract finite-lineage notation

Let the finite persistent lineage set be

\[
\mathcal L=\{1,\dots,N\}.
\]

At generation/age index \(k\), let

\[
J_{k,i}\ge0
\]

be the represented ancestry mass carried by lineage \(i\), and let

\[
R_{k,i}\ge0
\]

be its normalized ancestral return weight.

Write the marginals

\[
J_k=\sum_iJ_{k,i},
\qquad
R_k=\sum_iR_{k,i}.
\]

A same-event conversion theorem would require a lower bound on a correlated quantity such as

\[
\sum_i J_{k,i}R_{k,i},
\]

or a closely related material-incidence functional.

Knowing only the marginals does not provide such a bound.

## 3. Two-lineage anti-phase construction

Take \(N=2\).  For even \(k\), define

\[
J_{k,1}=J_k,
\qquad
J_{k,2}=0,
\]

and

\[
R_{k,1}=0,
\qquad
R_{k,2}=R_k.
\]

For odd \(k\), interchange the labels:

\[
J_{k,1}=0,
\qquad
J_{k,2}=J_k,
\]

\[
R_{k,1}=R_k,
\qquad
R_{k,2}=0.
\]

Then for every \(k\),

\[
\sum_iJ_{k,i}=J_k,
\qquad
\sum_iR_{k,i}=R_k,
\]

but

\[
\boxed{
\sum_iJ_{k,i}R_{k,i}=0.
}
\]

Thus arbitrarily strong marginal ancestry mass and arbitrarily strong marginal return can coexist with complete same-lineage anti-alignment.

This remains true with any finite number of labels by cyclic permutation.

## 4. Positive density does not fix the problem

Suppose the mass-bearing and return-bearing events both occur on sets of positive generation density.

The two-lineage construction can still place them in complementary lineage sectors at every selected generation.

Hence

\[
\boxed{
\text{positive-density mass}
+
\text{positive-density return}
+
\text{finite lineage}
\not\Rightarrow
\text{same-lineage positive-density alignment}.
}
\]

A finite-label pigeonhole principle selects labels for each marginal separately, but it does not force the selected labels to be the same.

## 5. What would destroy the anti-phase model

The anti-phase construction silently permits the identity of the mass-bearing lineage to switch without cost.

A Navier--Stokes realization cannot be treated this way.  Lineage populations are coupled by actual material/diffusive transfer and by their node balances.

For a population moment \(M_i\), M18-088--089 gives schematically

\[
\boxed{
M_i'
=
S_i
+
\sum_j e_{ji},
}
\]

where

- \(S_i\) is the local source/sink surplus from strain, coefficient/diffusion and the similarity baseline;
- \(e_{ji}=-e_{ij}\) is the antisymmetric inter-population exchange current.

M19-001--004 already shows that persistent non-gradient exchange descends to strain/geometry, palinstrophy/interface, coefficient+diffusion, or geometry/topology loss.

Therefore repeated anti-phase switching can be quiet only if the ancestry mass mark itself fails to be controlled by a population quantity obeying such a balance law.

## 6. Quantitative switching-cost lemma

Consider a scalar nonnegative population mark \(m_i(t)\) satisfying

\[
m_i'=s_i+\sum_j e_{ji},
\qquad e_{ji}=-e_{ij}.
\]

Suppose at time \(t_a\), lineage \(a\) is strongly marked and lineage \(b\) is weak:

\[
m_a(t_a)\ge m_*,
\qquad
m_b(t_a)\le \frac14m_*.
\]

At a later time \(t_b\), suppose the roles reverse:

\[
m_b(t_b)\ge m_*,
\qquad
m_a(t_b)\le \frac14m_*.
\]

Then

\[
|m_a(t_b)-m_a(t_a)|
+
|m_b(t_b)-m_b(t_a)|
\ge
\frac32m_*.
\]

Hence

\[
\boxed{
\int_{t_a}^{t_b}
\left(
|s_a|+|s_b|
+2\sum_j(|e_{aj}|+|e_{bj}|)
\right)dt
\gtrsim m_*.
}
\]

Up to harmless graph-count constants, every genuine order-one switch of the dominant material population requires order-one source/exchange total variation.

Thus infinitely many strong anti-phase switches imply either

\[
\boxed{
\int |S|dt=\infty
}
\]

or

\[
\boxed{
\int |e|dt=\infty,
}
\]

unless the marked amplitude itself degenerates.

## 7. Consequence for the R-AC frontier

The purely combinatorial form of \(\mathcal T_{AC}^{corr}\) is false.

The correct theorem must use a PDE-controlled lineage mark and has the form

\[
\boxed{
\begin{aligned}
&\text{ancestry mass repeatedly changes its dominant lineage}
\\
&\qquad\Longrightarrow
\text{population source/exchange variation}
\lor
\text{mark degeneration}.
\end{aligned}
}
\]

On the quiet branch, where the typed source/exchange exits remain bounded, dominant-lineage switching can occur only finitely many times at a fixed nondegenerate threshold.

Therefore the remaining quiet R-AC problem is reduced from arbitrary finite-lineage anti-alignment to:

\[
\boxed{
\text{one eventually persistent mass-bearing lineage}
\stackrel{?}{\Longrightarrow}
\text{ancestral shell-return occupancy on that same lineage}.
}
\]

This is a material transport/recurrence problem rather than a finite-label combinatorial problem.

## 8. Firewall: the ancestry mark must obey the balance

The switching lemma cannot be applied directly to the abstract cubic ancestry quantity \(J_{k,i}\) unless one proves that it is comparable to, or controlled by, a population state variable satisfying the exact balance law above.

This comparability is not presently certified.

Thus M19-036 does **not** close \(\mathcal T_{AC}^{corr}\).

It identifies the next precise bridge:

\[
\boxed{
\mathcal B_{J\to pop}:
J_{k,i}
\text{ admits a nondegenerate population realization with controlled source/exchange balance}.
}
\]

If \(\mathcal B_{J\to pop}\) holds, repeated lineage switching is already paid by existing M18/M19 currencies, and only same-lineage radial/material recurrence remains.

## 9. Updated R-AC structure

\[
\boxed{
\mathcal T_{AC}^{corr}
\Longrightarrow
\mathcal B_{J\to pop}
+
\mathcal T_{same-line\ radial\ return}
}
\]

modulo already typed source/exchange exits.

This is strictly sharper than the previous generic correlation label.

---

\[
\boxed{\text{M19-036 COMPLETE; FINITE-LINEAGE PIGEONHOLE ALONE CANNOT CLOSE R-AC.}}
\]