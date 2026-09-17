# M19-383 — A finite recurrent phase graph carries divergence-free cycle current; exact edge affinities do zero mean work

Date: 2026-09-18

Status: **NEW CANONICAL GRAPH NO-GO / M19-382 INTER-STATE HYSTERESIS AND CUTOFF-COLLAR COMPONENT SEGREGATION CAN BE COARSE-GRAINED TO A FINITE RECURRENT TRANSITION GRAPH ON ANY FIXED FINITE PARTITION. INVARIANT STATIONARITY FORCES THE NET EDGE CURRENT TO BE DIVERGENCE FREE. THEREFORE EVERY EDGE AFFINITY THAT IS THE DIFFERENCE OF A BOUNDED VERTEX POTENTIAL HAS EXACTLY ZERO STATIONARY WORK AGAINST THE CYCLE CURRENT. GRAPH TOPOLOGY OR RECURRENCE ALONE CANNOT PRODUCE THE NEEDED NONREUSABLE RESOURCE. ANY REYCLE-BREAK MUST COME FROM A PDE-SPECIFIC NONEXACT EDGE AFFINITY, A FINITE MATERIAL RESOURCE, OR A GENEALOGICAL RESET/REPLACEMENT EVENT. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Finite recurrent phase partition

Let the retained compact recurrent CE-H component be partitioned into finitely many measurable phase/component classes

\[
\mathcal V=\{V_1,\dots,V_N\}.
\]

The classes may encode, for example,

- sign/size bins of the cutoff-collar coefficient state;
- connected collar-component labels after a finite coarse graining;
- inter-state phase sectors from M19-382;
- regular versus segregated/necked collar states.

No claim is made that this finite partition captures the complete PDE state.

Let

\[
q_{ij}\ge0
\]

denote the stationary mean transition rate from `V_i` to `V_j` whenever such a transition current is well-defined after the standard event thickening.

Define the antisymmetric net current

\[
\boxed{
J_{ij}:=q_{ij}-q_{ji}=-J_{ji}.
}
\]

---

## 2. Stationarity gives Kirchhoff balance

Let

\[
p_i:=\nu(V_i)
\]

be the invariant occupation mass.

For a stationary recurrent process, the mean mass of each class is constant. Hence total mean inflow equals total mean outflow:

\[
\sum_j q_{ji}=\sum_j q_{ij}.
\]

Equivalently,

\[
\boxed{
\sum_jJ_{ij}=0
\qquad\text{for every }i.
}
\]

If `B_G` is an oriented incidence matrix of the finite transition graph and `j` is the edge-current vector, this is

\[
\boxed{B_Gj=0.}
\]

Thus

\[
\boxed{j\in\ker B_G,}
\]

i.e. the stationary net current lives in the graph cycle space.

This is the phase-state analogue of the older M19-275 finite-population graph firewall.

---

## 3. Exact edge affinities cannot pay a positive recurrent cost

Let `phi_i` be any bounded scalar vertex observable.

Define its exact edge increment

\[
\boxed{
\alpha_{ij}:=\phi_j-\phi_i.
}

In incidence notation,

\[
\alpha=B_G^T\phi.
\]

The stationary edge work is

\[
\mathcal W_\phi
:=
\frac12\sum_{i,j}\alpha_{ij}J_{ij}.
\]

Using `B_Gj=0`,

\[
\mathcal W_\phi
=
\phi^TB_Gj
=0.
\]

Therefore

\[
\boxed{
\sum_{i<j}(\phi_j-\phi_i)J_{ij}=0.
}
\]

Any bounded state function transported around a recurrent graph cycle has zero net mean gradient work.

---

## 4. Consequence for M19-382 inter-state hysteresis

M19-382 leaves a nonderivative branch

\[
H_{interstate}^{+}.
\]

If one attempts to close it by assigning a bounded scalar potential to the phase classes, such as

\[
\bar\kappa_i,
\quad
\overline{e^{2\kappa}}_i,
\quad
\bar\gamma_i,
\quad
\bar N_{a,i},
\quad
\bar E_i,
\]

and taking edge differences, the resulting affinity is exact.

Hence its stationary cycle work is zero.

Therefore

\[
\boxed{
H_{interstate}
+\text{ finite recurrent graph topology}
\not\Rightarrow
\text{nonreusable positive resource}.
}

The same is true for a finite graph of collar-component merge/split states if only bounded vertex observables are used.

---

## 5. What a successful edge affinity must contain

To break recurrence, an edge quantity must fail to be a bounded vertex gradient on the coarse recurrent graph.

A viable candidate must therefore contain at least one of:

1. **path dependence** not reconstructible from the endpoint coarse states;
2. **material-label dependence** retained across transitions;
3. **irreversible finite-resource loss**, such as the sign-preserving relative-flux losses in M5-648--649;
4. **generation/ancestry dependence** that prevents the same edge from being reused freely across scales;
5. **PDE dissipative action** whose cumulative value is finite in the original physical variables;
6. a genuine nonexact topological/holonomy quantity proved to be inherited by the PDE, not merely introduced by coarse graining.

---

## 6. Relation to M19-275--277

M19-275 already showed for finite material-population graphs that

\[
\alpha=B_G^T\phi
\quad\Longrightarrow\quad
\alpha\cdot j_C=0
\]

for graph cycle currents.

M19-276--277 then showed that apparent graph-cycle freedom is not an autonomous continuum topological charge: the continuum source/divergence response must still pay for it.

The present module does not claim a new graph theorem.

Its new role is to apply that firewall specifically to the **M19-382 phase-state / cutoff-collar component transition graph** and thereby forbid a false next step:

\[
\text{`there is a recurrent oriented graph cycle, therefore there is a new signed resource.'}
\]

There is not.

---

## 7. Updated recycle-break target

The graph target must be refined from

\[
\mathcal T_{graph}^{recycle-break}
\]

to

\[
\boxed{
\mathcal T_{edge}^{PDE-affinity}:
\text{construct a PDE-inherited nonexact edge action or finite material resource that cannot be represented as a bounded vertex difference.}
}
\]

Natural candidates include

- same-label relative-flux loss on sign-preserving corridors;
- generation-indexed physical palinstrophy/base-gain;
- stress-flux or terminal defect action;
- genealogy replacement incidence;
- path-integrated coefficient action conditioned on a fixed material label.

Each candidate must be audited for exact-coboundary or critical-recycling failure before being used.

---

## 8. Firewall

A positive transition rate is not a positive resource.

A directed recurrent cycle is not an irreversible drift.

A finite graph does not imply finite total transition count.

An antisymmetric edge current can circulate indefinitely on a stationary invariant state.

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
