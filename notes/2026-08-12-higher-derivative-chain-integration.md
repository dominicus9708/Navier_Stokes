# Higher-derivative sparseness chains as an external anchor for the DSD cascade

Date: 2026-08-12

Status: **EXTERNAL FRAMEWORK INTEGRATION + DSD BRIDGE / NOT A NEW REGULARITY THEOREM**.

## 1. Why this note is needed

The current DSD-assisted route arrived independently at a scale-indexed cascade block built from moving local oscillation, dissipation, pressure locality, vorticity occupancy, strain and off-diagonal coupling channels.

Before developing a new higher-order hierarchy, this must be compared with established work.

Grujic and Xu's *Asymptotic Criticality of the Navier-Stokes Regularity Problem* develops a sparseness framework for super-level sets of positive/negative components of higher-order spatial derivatives of the velocity.  Their main structural message is that the gap between an a-priori sparseness scale and a regularity sparseness scale decreases with derivative order and becomes asymptotically zero as the order tends to infinity.

Therefore the present project must treat higher-derivative sparseness as an **external anchor**, not as a DSD novelty.

## 2. External derivative-order index

Let

\[
D^{(k)}u
\]

denote a `k`-th spatial derivative block (with components/signs typed as required by the external framework).

The established sparseness classes can be viewed schematically as

\[
D^{(k)}u
\in
Z_{\alpha_k}^{(k)},
\]

where the scale of sparseness is tied to a power of

\[
\|D^{(k)}u\|_\infty.
\]

The precise external definitions and constants remain those of Grujic--Xu; this repository does not rename them as new DSD theorems.

## 3. DSD two-index block

The useful DSD move is to keep **physical scale** and **derivative order** as separate indices:

\[
\boxed{
\mathcal K_{j,k}(t)
}
\]

where

- `j` indexes the physical radius/scale `ell_j` of the moving observation window;
- `k` indexes the spatial derivative order.

A conservative block is

\[
\mathcal K_{j,k}
=
\bigl(
C_j,E_j,\mathfrak H_j,
\operatorname{Occ}_{j,k},
\operatorname{Sparse}_{j,k},
\operatorname{Dir}_{j,k},
\operatorname{Cross}_{j,k},
\ldots
\bigr).
\]

The first three entries come from the present moving weighted-sphere/pressure analysis.  The higher-order occupancy and sparseness entries are read using the established derivative-level framework.

This avoids collapsing two mathematically distinct notions:

\[
\text{smaller physical scale}
\neq
\text{higher derivative order}.
\]

## 4. Dynamic matrix interpretation

There are now two transfer directions.

### Scale transfer

\[
\mathcal K_{j-1,k}
\longrightarrow
\mathcal K_{j,k},
\]

controlled at low order by the weighted one-step inequality and the local pressure-cascade estimate.

### Derivative-chain transfer

Differentiating Navier--Stokes produces interactions schematically of the form

\[
\partial_tD^{(k)}u
-
u\Delta D^{(k)}u
+
\sum_{m=0}^{k}
\binom{k}{m}
D^{(m)}u\cdot\nabla D^{(k-m)}u
+
\nabla D^{(k)}p
=0.
\]

Thus derivative levels have many off-diagonal couplings.

In DSD matrix language, `k` is a channel index and the binomial nonlinear interactions are off-diagonal blocks.  This is a bookkeeping representation of the differentiated NSE, not a new equation.

## 5. Ascending/descending chain anchor

Grujic--Xu identify two key dynamical scenarios described as ascending and descending chains of derivatives.  Their work obtains favorable analyticity/sparseness information in both scenarios and shows asymptotic matching of the relevant scales as derivative order grows.

The present project should not reconstruct these arguments from scratch.

Instead, use the external chain classification as a gate:

\[
\boxed{
\text{any DSD residual singular cascade must also survive the established higher-derivative chain analysis.}
}
\]

## 6. What DSD can still add without duplicating the external framework

Potentially non-duplicative ingredients already derived here are:

1. **moving weighted mean subtraction** — coherent translation is removed at each physical scale;
2. **suitable-weak weighted variance lemma** — the internal velocity difference has a theorem-level local-energy budget;
3. **generalized moving-to-fixed cylinder lemma** — local moving observations can feed ordinary fixed-cylinder regularity criteria;
4. **near-pressure closure** — near pressure enters the same cubic block as relative advection;
5. **affine-free remote-pressure locality** — distant pressure scales are geometrically suppressed after removing dynamically irrelevant affine pieces;
6. **two-index bookkeeping** — physical-scale migration and derivative-order chains can be audited separately and then cross-coupled.

The research question is whether these ingredients supply an estimate missing from the established asymptotic-sparseness framework, not whether the framework can be renamed in DSD terminology.

## 7. Revised residual singular class

A hypothetical singularity in the present route must now evade simultaneously:

- the pressure-free moving-oscillation epsilon gate;
- the vorticity occupancy/linear-sparseness gate;
- vorticity-direction coherence regularity gates;
- middle-strain-eigenvalue regularity gates;
- the established higher-derivative sparseness/chain framework;
- local pressure-scale suppression.

In addition it must sustain the DSD two-index transfer

\[
(j,k)\to(j+1,k),
\qquad
(j,k)\leftrightarrow(j,k+1)
\]

without ever entering one of the regularity regions above.

## 8. Next proof target

The next genuinely useful result would be an **either/or estimate coupling the two indices**, for example a theorem of the schematic form:

\[
\text{strong child-scale concentration at order }k
\Longrightarrow
\begin{cases}
\text{sparseness at order }k+1,\\
\text{or a controlled pressure/strain channel,}\\
\text{or a quantitative cost in dissipation.}
\end{cases}
\]

No such estimate is presently established in this repository.

Status: **OPEN CROSS-INDEX ESTIMATE**.

## External anchor

Z. Grujic and L. Xu, *Asymptotic Criticality of the Navier-Stokes Regularity Problem*, arXiv:1911.00974.
