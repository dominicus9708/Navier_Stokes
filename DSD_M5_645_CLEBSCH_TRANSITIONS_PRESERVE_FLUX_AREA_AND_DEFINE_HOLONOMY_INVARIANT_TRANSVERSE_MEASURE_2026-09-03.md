# DSD M5-645 — Clebsch transitions preserve flux area and define a holonomy-invariant transverse flux measure

Date: 2026-09-03

Status: **INTERNAL FOLIATION/FLUX PATCHING / ON OVERLAPPING REGULAR KAPPA-CLEBSCH CHARTS, `W=grad kappa x grad psi_i=grad kappa x grad psi_j` IMPLIES `psi_j=psi_i+F_ij(kappa)`. CONSEQUENTLY `d kappa wedge d psi` IS EXACTLY CHART-INVARIANT. THUS THE LOCAL FLUX AREAS OF M5-644 PATCH TO A HOLONOMY-INVARIANT TRANSVERSE MEASURE FOR THE REGULAR VORTEX-LINE FOLIATION EVEN WHEN NO GLOBAL SINGLE-VALUED CLEBSCH POTENTIAL EXISTS. THE FINITE-RESOURCE GAP IS NOW PRECISE: IF THE FIXED INNER RESERVOIR ADMITS A COMPLETE TRANSVERSAL OF FINITE TOTAL FLUX MEASURE FOR ALL RELEVANT PACKET LEAVES, THEN INFINITELY MANY DISTINCT PACKET LABELS EACH OF FLUX >=PHI_* ARE IMPOSSIBLE. THE UNSOLVED PART IS THE SINGULAR/CRITICAL FOLIATION NEAR W=0 OR GRAD KAPPA=0 AND THE EXISTENCE/FINITE MASS OF SUCH A COMPLETE TRANSVERSAL. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Two local Clebsch charts

On a regular overlap, suppose

\[
W=\nabla\kappa\times\nabla\psi_i
\]

and

\[
W=\nabla\kappa\times\nabla\psi_j.
\]

Subtracting,

\[
\nabla\kappa\times\nabla(\psi_j-\psi_i)=0.
\]

Because `grad kappa!=0`, the gradient of the difference is parallel to `grad kappa`.

Hence locally on each connected overlap there is a scalar function `F_ij` such that

\[
\boxed{
\psi_j=\psi_i+F_{ij}(\kappa).
}
\]

---

## 2. Flux area is transition invariant

Differentiate:

\[
d\psi_j
=d\psi_i+F_{ij}'(\kappa)d\kappa.
\]

Therefore

\[
d\kappa\wedge d\psi_j
=d\kappa\wedge d\psi_i
+F_{ij}'(\kappa)d\kappa\wedge d\kappa.
\]

The second term vanishes, so

\[
\boxed{
 d\kappa\wedge d\psi_j
=d\kappa\wedge d\psi_i.
}
\]

Thus the oriented flux two-form is exactly invariant under Clebsch gauge transitions.

The transition map

\[
(\kappa,\psi_i)
\mapsto
(\kappa,\psi_i+F_{ij}(\kappa))
\]

has Jacobian determinant one in the potential plane.

---

## 3. Holonomy-invariant transverse flux measure

For every local transversal `S` to the regular vortex foliation define

\[
\mu_{flux}(S)
:=\int_S W\cdot n\,dA
=\int_S d\kappa\wedge d\psi.
\]

Because the two-form is globally the vorticity flux form and the chart transitions preserve it, local transverse measures agree on overlaps.

Moreover sliding a transversal along the same vortex-line bundle does not change signed vorticity flux because `div W=0`.

Therefore the regular vortex foliation carries a natural

\[
\boxed{
\text{holonomy-invariant signed transverse flux measure}.
}
\]

On an oriented coherent packet with one vorticity direction the corresponding absolute packet flux is the positive mass of its transverse set.

---

## 4. Conditional finite-resource lemma

Suppose at a reference time `theta_0` the relevant regular vortex-line population in the fixed reservoir admits a complete transversal

\[
\mathcal T=S_1\cup\cdots\cup S_N
\]

with finite total absolute flux mass

\[
\boxed{
\|\mu_{flux}\|(\mathcal T)<\infty.
}
\]

Assume also that distinct material packet labels correspond to disjoint sets of vortex leaves.

Then their intersections with the complete transversal are disjoint in transverse-measure space.

If every packet has

\[
|\Phi_j|\ge\phi_*,
\]

then

\[
\sum_j\phi_*
\le
\sum_j|\Phi_j|
\le
\|\mu_{flux}\|(\mathcal T).
\]

Therefore only finitely many such distinct packet labels can exist.

Thus

\[
\boxed{
\text{finite-mass complete transversal}
\Longrightarrow
\text{M5-641 infinite replacement contradiction}.
}
\]

---

## 5. Why global psi is not required

The conditional argument uses only the transverse measure.

A globally single-valued `psi` is unnecessary because the transition maps preserve

\[
d\kappa\wedge d\psi.
\]

Therefore monodromy of `psi` by shifts `F(kappa)` is harmless for flux counting.

This removes one potential topological loophole identified in M5-644.

---

## 6. What can still obstruct the argument

The remaining issues are more specific:

1. singular vortex points `W=0`, where the one-dimensional foliation degenerates;
2. critical kappa strata `grad kappa=0`, where the kappa-Clebsch chart fails;
3. leaves accumulating on singular strata so that no finite regular complete transversal captures the relevant material packet labels;
4. possible infinite transverse multiplicity/absolute measure caused by singular recurrence;
5. packet preimages that cannot be assigned to disjoint leaf bundles at the reference time without additional genealogy control.

These are now the exact geometric loopholes.

---

## 7. Compact regular subregion

On any compact subset

\[
K\Subset\{W\ne0,\ \nabla\kappa\ne0\},
\]

the regular one-dimensional foliation admits a finite flow-box cover.

A finite union of local transverse disks has finite flux measure because `W` is smooth and the disks have finite area.

Thus the complete-transversal lemma is straightforward **away from the singular/critical set**.

Consequently any infinite packet-generation escape must accumulate essentially on

\[
\boxed{
\{W=0\}\cup\{\nabla\kappa=0\}
}

or exploit repeated leaf multiplicity tied to those strata.

---

## 8. Updated resource frontier

M5-643's broad statement

\[
\text{no global flux transversal proved}
\]

is sharpened to

\[
\boxed{
\text{regular finite-core foliation is flux-countable};
\quad
\text{only singular/critical accumulation can evade finite flux counting}.
}
\]

The next target is therefore the analytic structure of

\[
\{W=0\}\cup\{\nabla\kappa=0\}
\]

and whether a fixed-flux packet can have all its past representative leaves accumulate there while retaining flux `>=phi_*`.

---

## 9. Firewall

The conditional contradiction is not yet invoked globally.

The existence of a finite-mass complete transversal is only asserted on compact regular subregions, where standard flow-box geometry applies.

No theorem about singular foliations is silently imported.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]