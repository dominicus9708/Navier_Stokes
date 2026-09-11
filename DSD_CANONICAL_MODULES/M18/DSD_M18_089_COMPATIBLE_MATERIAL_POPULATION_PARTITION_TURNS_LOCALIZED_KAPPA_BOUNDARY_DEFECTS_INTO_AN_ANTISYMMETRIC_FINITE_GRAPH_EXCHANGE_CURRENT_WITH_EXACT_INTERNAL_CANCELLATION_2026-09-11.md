# M18-089 — A compatible material-population partition turns localized kappa boundary defects into an antisymmetric finite graph exchange current with exact internal cancellation

**Date:** 2026-09-11  
**Status:** MATERIAL-POPULATION EXCHANGE MATRIX / PDE-TO-GRAPH REALIZATION / EXACT INTERNAL CANCELLATION

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Purpose

M18-088 localizes the CE-H amplitude moment to one genuine material population \(P_i\):

\[
\frac1p(M_{p,i})'
=
A_{p,i}-D_{p,i}+B_{p,i}-c_pM_{p,i},
\]

with

\[
B_{p,i}
=
\int_{\partial P_i}
\rho^{p-1}\partial_{n_i}\rho\,dS.
\]

The term \(B_{p,i}\) is the exact signed diffusive exchange defect created by localizing the globally dissipative \(\kappa\) identity.

The present module shows that, for a compatible finite material partition, these defects are not independent population sources.

They assemble into an antisymmetric finite graph current:

\[
\boxed{
e_{ij}^{(p)}=-e_{ji}^{(p)}.}
\]

All internal exchanges cancel exactly when populations are summed.

Thus the population boundary-defect branch is a concrete PDE realization of the conservative finite-lineage current architecture of M18-077.

---

## 2. Compatible material partition

Let the retained local material region \(\Omega_{loc}(\theta)\) be partitioned into finitely many material populations

\[
\boxed{
\Omega_{loc}(\theta)
=
\bigcup_{i=1}^{N}P_i(\theta)
}
\]

with disjoint interiors.

Assume, on the controlled branch:

1. each \(P_i\) is transported by the same material field \(B\);
2. pairwise interfaces
   \[
   S_{ij}:=\partial P_i\cap\partial P_j
   \]
   are sufficiently smooth;
3. the CE-H field \(\rho\) is smooth across internal interfaces;
4. triple junctions or lower-dimensional intersections have zero surface measure for the boundary integrals;
5. the remaining outer boundary is denoted
   \[
   \partial_{ext}\Omega_{loc}.
   \]

Failure of this compatible partition is recorded as

\[
\boxed{G_{population\ interface/realization\ loss}.}
\]

---

## 3. Edge exchange current

For an oriented internal interface from population \(i\) toward \(j\), define

\[
\boxed{
e_{ij}^{(p)}
:=
\int_{S_{ij}}
\rho^{p-1}\partial_{n_i}\rho\,dS,
}
\]

where \(n_i\) is the outward normal of \(P_i\).

On the same geometric interface,

\[
n_j=-n_i.
\]

Therefore

\[
\partial_{n_j}\rho
=-\partial_{n_i}\rho.
\]

Hence

\[
\boxed{
e_{ji}^{(p)}=-e_{ij}^{(p)}.}
\]

This antisymmetry is exact.

---

## 4. External exchange

Define the outer-boundary contribution for population \(i\):

\[
\boxed{
e_{i,ext}^{(p)}
:=
\int_{\partial P_i\cap\partial_{ext}\Omega_{loc}}
\rho^{p-1}\partial_{n_i}\rho\,dS.
}
\]

Then the full localized boundary term decomposes as

\[
\boxed{
B_{p,i}
=
\sum_{j\ne i}e_{ij}^{(p)}
+e_{i,ext}^{(p)}.
}
\]

Thus internal and external exchange are separated exactly.

---

## 5. Exact internal cancellation

Sum the boundary terms over all populations:

\[
\sum_i B_{p,i}
=
\sum_i\sum_{j\ne i}e_{ij}^{(p)}
+
\sum_i e_{i,ext}^{(p)}.
\]

By antisymmetry, every internal interface appears twice with opposite sign:

\[
\sum_i\sum_{j\ne i}e_{ij}^{(p)}=0.
\]

Therefore

\[
\boxed{
\sum_{i=1}^{N}B_{p,i}
=
B_{p,ext}
:=
\sum_i e_{i,ext}^{(p)}.
}
\]

On a closed local network with no external diffusive exchange,

\[
\boxed{
B_{p,ext}=0
\Longrightarrow
\sum_iB_{p,i}=0.
}
\]

Thus internal population diffusion cannot create or destroy the total \(p\)-moment. It only redistributes it.

---

## 6. Population moment network equation

For each population,

\[
\boxed{
\frac1p(M_{p,i})'
=
A_{p,i}
-D_{p,i}
-c_pM_{p,i}
+
\sum_{j\ne i}e_{ij}^{(p)}
+
e_{i,ext}^{(p)}.
}
\]

This is a finite-network source-sink-exchange law.

Define the vector

\[
M_p=(M_{p,1},\dots,M_{p,N})^T.
\]

Choose one orientation for every graph edge and let \(B_G\) be the graph incidence matrix.

Let \(j_p\) collect the oriented internal edge exchanges.

Then schematically

\[
\boxed{
\frac1pM_p'
=
A_p-D_p-c_pM_p
+B_Gj_p
+e_{ext,p}.
}
\]

This is the precise PDE realization of a finite conservative exchange current.

---

## 7. Recovery of the whole local-region equation

Sum over populations.

Because

\[
\mathbf1^TB_G=0,
\]

one gets

\[
\boxed{
\frac1p
\frac d{d\theta}
\sum_iM_{p,i}
=
\sum_iA_{p,i}
-
\sum_iD_{p,i}
-
c_p\sum_iM_{p,i}
+
B_{p,ext}.
}
\]

This is exactly the amplitude-moment balance on the union \(\Omega_{loc}\).

If the outer boundary is sent to whole space with decaying fields, the external term vanishes and M18-060 is recovered.

Thus the graph representation is algebraically consistent with the global PDE balance.

---

## 8. Internal exchange has no independent net source budget

Because

\[
\sum_iB_{p,i}=0
\]

on a closed network, a positive boundary-exchange contribution for one population must be paid by negative contributions elsewhere.

Therefore

\[
\boxed{
G_{boundary\text{-}exchange}^{P_i}
\text{ is not an independent recharge source.}
}
\]

It is a redistribution channel inside the finite population graph.

This is the population analogue of M18-060's global statement that \(\kappa\) is not a net amplitude source.

---

## 9. Long-time mean network balance

On a recurrent compact closed network, assume each \(M_{p,i}\) is bounded and the invariant mean exists.

Then

\[
\left\langle M_{p,i}'\right\rangle=0.
\]

Hence

\[
\boxed{
B_G\langle j_p\rangle
=
-
\left\langle
A_p-D_p-c_pM_p
\right\rangle.
}
\]

Thus the mean exchange current is divergence-free only when each population's internal source-sink-damping balance vanishes separately.

In general, nonzero divergence of the mean graph current transfers moment from source-rich populations to sink-rich populations.

The total divergence still sums to zero.

---

## 10. Source-rich and sink-rich populations

Define the mean internal surplus

\[
\boxed{
s_{p,i}
:=
\left\langle
A_{p,i}-D_{p,i}-c_pM_{p,i}
\right\rangle.
}
\]

Then on the closed network,

\[
\boxed{
B_G\langle j_p\rangle=-s_p.
}
\]

Since

\[
\mathbf1^Ts_p=0,
\]

there must be compensation between populations whenever \(s_p\not\equiv0\).

Thus the network separates populations into, schematically,

\[
\boxed{
\text{moment-source-rich populations}
\to
\text{diffusive graph exchange}
\to
\text{moment-sink-rich populations}.
}
\]

This is a finite conservative redistribution architecture.

---

## 11. Cycle-space component remains invisible to vertex balance

The equation

\[
B_G\langle j_p\rangle=-s_p
\]

determines only the divergence part of the mean current.

If \(j_{part}\) is one particular solution, then every

\[
\boxed{
\langle j_p\rangle
=
j_{part}+j_C,
\qquad
j_C\in\ker B_G
}
\]

has the same population balance.

Thus the conservative cycle-space current of M18-077 reappears exactly as the homogeneous freedom of the population diffusive exchange problem.

Population moment balances alone cannot determine or eliminate \(j_C\).

---

## 12. Reversible zero-mean exchange

Even if

\[
\langle j_p\rangle=0,
\]

instantaneous edge currents may oscillate with positive total variation.

Hence exact internal cancellation does not eliminate the M18-077 reversible branch.

It identifies its physical realization:

\[
\boxed{
G_{cycle}^{rev}
\text{ may be realized as sign-changing diffusive amplitude-moment exchange across material population interfaces}.
}

No contradiction follows from antisymmetry alone.

---

## 13. Multi-p exchange matrices

For every finite \(p\ge2\), there is a distinct edge-current family

\[
e_{ij}^{(p)}
=
\int_{S_{ij}}ho^{p-1}\partial_{n_i}\rho\,dS.
\]

Changing \(p\) reweights the same interface by amplitude.

Therefore the family

\[
\boxed{
\{j_p\}_{p\ge2}
}

contains information about amplitude segregation on each material interface.

If two exponents \(q>p\) have substantially different normalized edge exchange, that difference directly measures amplitude bias of the normal diffusive flux.

This is the network analogue of the M18-069 change-of-measure mechanism.

---

## 14. Exact edge change-of-measure identity

On one oriented interface \(S_{ij}\), write

\[
d\zeta_{ij}^{(p)}
:=
\rho^{p-1}\partial_{n_i}\rho\,dS.
\]

This is a **signed** measure, so it is not a probability measure and the positive covariance formulas of M18-062 cannot be imported directly.

However algebraically,

\[
\boxed{
e_{ij}^{(q)}
=
\int_{S_{ij}}
\rho^{q-p}
\,d\zeta_{ij}^{(p)}.
}
\]

Thus multi-p edge exchange is a signed amplitude reweighting of one common normal-diffusion measure.

Any probabilistic covariance statement requires a Jordan decomposition or a sign-controlled interface sector.

This is the correct firewall.

---

## 15. Closed-network consequence for the M18-088 trichotomy

M18-088 gives for each population

\[
\delta_{pq}
=
\Delta_{strain,i}
+
\Delta_{diff,i}
+
\Delta_{bdry,i}.
\]

The raw boundary exchange numerators cancel globally at each exponent:

\[
\boxed{
\sum_i\langle B_{p,i}\rangle=0,
\qquad
\sum_i\langle B_{q,i}\rangle=0.
}
\]

Therefore boundary exchange can redistribute the universal growth shift among populations but cannot create the total global shift.

At whole-network level, the original global strain/diffusion architecture remains the only net source-sink structure.

---

## 16. Outer-boundary / export branch

If

\[
B_{p,ext}\ne0,
\]

then the local finite network exchanges amplitude moment with its exterior.

This is an explicit

\[
\boxed{G_{external\ diffusive\ export/import}}
\]

branch.

It must not be hidden inside internal lineage exchange.

On the closed compact hard branch under present audit, set it aside as a typed export/realization exit.

---

## 17. Strategic gain

The abstract finite-lineage circulation problem has acquired a concrete PDE edge current:

\[
\boxed{
e_{ij}^{(p)}
=
\int_{S_{ij}}ho^{p-1}\partial_{n_i}\rho\,dS.
}

This is valuable because it gives direct access to

- amplitude weighting;
- normal gradients;
- interface geometry;
- sign decomposition;
- and multi-p comparisons.

The next successful closure, if any, can work on these explicit edge observables instead of an abstract graph current.

---

## 18. Highest-value next target

M18-090 should decompose each interface current into inward/outward Jordan parts:

\[
(\partial_n\rho)_+,
\qquad
(\partial_n\rho)_-.
\]

Then compare the two amplitude exponents \(p<q\).

A key question is whether a nonzero conservative cycle current at both exponents forces an interface-amplitude ordering around a directed cycle that is impossible to close without either

- an amplitude increase/decrease around the cycle;
- a sign reversal;
- or a zero-gradient/interface degeneration.

One must not assume such impossibility in advance: directed cycles can in principle carry sign-changing amplitude-weighted flux.

---

## 19. Audit verdict

### Certified

1. Compatible material interfaces give exact antisymmetric exchange currents \(e_{ij}^{(p)}=-e_{ji}^{(p)}\).
2. Internal population boundary defects cancel exactly when summed.
3. Population moment equations form a finite conservative graph network.
4. Internal boundary exchange is redistribution, not a net amplitude source.
5. Mean graph current solves a divergence equation determined by population source-sink surplus, plus an arbitrary cycle-space component.
6. The abstract M18-077 cycle current is concretely realizable as diffusive amplitude-moment exchange.
7. Multi-p edge currents are signed amplitude reweightings of the same normal-gradient measure.
8. External boundary exchange is a separate export/import branch.

### Still open

- sign/Jordan structure of edge currents;
- exclusion of nonzero cycle-space diffusive circulation;
- reversible edge-current oscillation;
- self-helicity/twist and surface geometry loss;
- ancestry, remote, and critical roots;
- global 3D Navier--Stokes regularity.

## 20. Next target

M18-090 should perform the signed Jordan decomposition of \(e_{ij}^{(p)}\) and audit whether multi-p cycle consistency gives a genuinely new obstruction or merely another reversible amplitude-segregation mechanism.
