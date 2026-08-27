# DSD M5-90 — DSD Parallel Logic-Chain Audit Protocol

Date: 2026-08-27

Status: **METHODOLOGICAL REFACTOR / DSD AUDIT IS DEFINED AS AN ALGORITHMIC STRUCTURAL AUDIT DISTINCT FROM NUMERICAL, SCIENTIFIC, OR EMPIRICAL VALIDATION / EACH CANDIDATE IS PROCESSED IN PARALLEL THROUGH FORMATION-AXIOM, AXIAL-PROPERTY, STATIC-AGGREGATION, AND DYNAMICAL CHAINS / MATHEMATICAL CALCULATIONS MAY BE STANDARD OR DSD-DERIVED / GLOBAL REGULARITY UNPROVED.**

## 1. Purpose

The phrase `parallel DSD logic chain` does **not** mean merely solving several mathematical subproblems at the same time.

For one candidate structure `C`, run four logically distinct audits in parallel:

\[
\boxed{
\mathfrak A_{DSD}(C)
=
\bigl(
\mathfrak F(C),
\mathfrak X(C),
\mathfrak S(C),
\mathfrak D(C)
\bigr)
}
\]

where

- `F` = Formation-Axiom / describability chain;
- `X` = axial-property chain;
- `S` = static-aggregation chain;
- `D` = dynamical chain.

The four chains are not four numerical estimates. They are four algorithms for checking whether the same claimed object can be formed, oriented, aggregated, and transported consistently.

---

## 2. Audit is not the calculation

A mathematical calculation may produce an identity, inequality, estimate, compactness statement, or PDE relation.

The DSD audit consumes that output and asks structural questions such as:

1. Is the object appearing in the calculation actually defined in the stated regime?
2. Which part is internal, boundary, or external to the described structure?
3. Which channel/axis carries the term?
4. Can terms from disconnected components legitimately be aggregated?
5. Does the same object persist under the stated dynamics, or does its identity fail at a topology/critical transition?
6. Is an apparent contradiction produced by a forbidden transition, double counting, a missing undefined state, or a genuine incompatibility?

Thus

\[
\boxed{
\text{calculation}
\neq
\text{DSD audit}
}
\]

although DSD logic may also be used to design new calculations.

---

## 3. Formation-Axiom chain F

For each candidate `C`, process the following in order.

### F0 — object formation

List the objects that are claimed to exist.

For the present Navier--Stokes endpoint these may include

\[
U,\ a=|U|,\ \Omega_{\lambda,k},\ \Gamma_{\lambda,k},\ P,\ b,
\]

and the recurrent W1 state.

### F1 — defined / undefined split

Separate regimes in which each object is defined from regimes in which it is not.

Example:

- a regular level component is defined when `grad a != 0` on the level;
- the same regular component label need not remain defined at a critical topology-changing level.

Undefined states are not treated as false states.

### F2 — interior / boundary / exterior partition

For a connected superlevel component

\[
\Omega_{\lambda,k}=\{a>\lambda\}_k,
\]

retain separately:

- interior `Omega`;
- full induced boundary `Gamma`;
- exterior/complement.

A boundary descriptor such as a componentwise pressure mean is not promoted to an independent bulk state.

### F3 — channel existence

A channel may exist even if its current scalar value is zero.

For the current endpoint, distinguish at least:

- normal-crossing channel;
- tangential/angular channel;
- strain/formation channel;
- pressure-work channel;
- recurrent time/scale channel.

### F4 — admissibility

Reject a candidate only if it fails the actual formed class.

Example: a punctured radial source/sink may satisfy local differential equations but is not an admissible smooth whole-space incompressible W1 endpoint because the puncture carries a distributional source.

This is a **formation rejection**, not a numerical contradiction.

---

## 4. Axial-property chain X

The axial chain asks how the formed object is resolved along independent or coupled directions.

### X0 — identify local axes

At a regular amplitude level use

\[
n=\frac{\nabla a}{|\nabla a|},
\qquad
T_y\Gamma_{\lambda,k},
\qquad
e=\frac Ua.
\]

The normal axis, tangential plane, streamline direction, and Leray-time/scale direction are distinct descriptors.

### X1 — project channels

Write

\[
U=(U\cdot n)n+U_{\tau}.
\]

The crossing variable is

\[
b=U\cdot\nabla\log a
=\frac{|\nabla a|}{a}(U\cdot n).
\]

The angular gap records the non-normal part:

\[
G_w
=
\int\frac{w(a)}a|U\times\nabla a|^2.
\]

### X2 — orientation and sign

A signed normal channel and its unsigned quadratic cost are not interchangeable.

The zero-flux condition concerns

\[
\int U\cdot n,
\]

whereas `T` concerns a square of the same channel.

Therefore zero signed flux does not imply zero crossing cost.

### X3 — axis coupling

At the exact minimal-payer endpoint,

\[
P-m=2\nu b,
\]

so the pressure-work channel is locked to the normal-crossing axis.

This is an axial coupling, not merely a pressure-magnitude statement.

### X4 — scale/time axis

W1 recurrence is recurrence in autonomous Leray time, not literal recurrence of physical time evolution.

The scale axis must therefore be audited separately from the physical-energy axis.

---

## 5. Static-aggregation chain S

Static aggregation freezes one admissible state and asks which local descriptors may be consistently combined.

### S0 — choose one state and one resolution

Fix one Leray time, one amplitude band, and one component decomposition.

### S1 — aggregate only compatible pieces

For a connected superlevel volume, the divergence theorem applies to its **full induced boundary**.

Do not impose zero flux independently on each surface component unless separately justified.

### S2 — signed versus unsigned aggregation

Retain separately:

\[
\sum \int U\cdot n
\]

and

\[
\sum \int |U\cdot n|^2.
\]

The first may cancel while the second is strictly positive.

### S3 — no double counting

Componentwise pressure offsets do not pay the pump because they cancel against componentwise zero flux.

Only intra-component pressure variation enters the pressure payer.

### S4 — static closure equations

Collect all exact simultaneous state constraints before declaring a state admissible.

For the M5 endpoint these include, where defined,

\[
X_w>0,
\quad
T>A_w+G_w,
\quad
P-m=2\nu b,
\quad
\nabla\cdot U=0,
\]

plus the pressure-Poisson/amplitude compatibility defects.

---

## 6. Dynamical chain D

The dynamical chain audits whether a statically admissible state can evolve through the claimed sequence of states.

### D0 — state identity

Specify what identifies the state across time: the field itself, a level branch, a component graph, or only a neighborhood in W1 phase space.

### D1 — allowed smooth transitions

Track a regular level component only while the regularity conditions defining it persist.

### D2 — critical/topology transitions

Birth, death, merger, splitting, or change in boundary-component number passes through a critical event where a previously used regular-level descriptor may become undefined.

This is recorded as a state transition rather than silently continuing the old label.

### D3 — recurrence

A recurrent state need not repeat every internal label. It need only return in the topology used to define W1 recurrence.

Therefore recurrence does not automatically identify component labels across all returns.

### D4 — transport of defects

A defect may be transported through recurrence only when its domain, normalization, and required derivative topology are preserved.

---

## 7. Cross-audit stage

After the four chains finish independently, cross-check them.

### F <-> X

Can the claimed axis be attached to every formed object where it is used?

### X <-> S

Are signed and unsigned axial channels being aggregated correctly?

### S <-> D

Does a static component sum remain meaningful through the stated transition?

### D <-> F

Does recurrence return to a genuinely formed object, or only to a limiting descriptor for which some component identity has become undefined?

A contradiction is accepted only after all four pairwise interfaces are passed.

---

## 8. Audit statuses

Use the following logical statuses.

### PASS

The candidate survives this chain under the stated assumptions.

### CONDITIONAL

The chain is valid only under an explicit additional hypothesis.

### SPLIT

The chain creates two or more structurally different successor branches.

### UNDEFINED-TRANSITION

The current descriptor stops being defined; move to a transition state rather than declaring contradiction.

### REJECT

The candidate is incompatible with the formed class or with another simultaneously required exact relation.

These statuses are algorithmic and should not be confused with statistical confidence or numerical error bars.

---

## 9. Operational algorithm

For every new mathematical lemma or candidate endpoint:

1. record the raw mathematical result;
2. run `F0-F4`;
3. independently run `X0-X4`;
4. independently run `S0-S4`;
5. independently run `D0-D4`;
6. cross-audit `F-X`, `X-S`, `S-D`, `D-F`;
7. classify each surviving branch;
8. only then feed the surviving branch back into mathematical calculation.

Thus the overall workflow is

\[
\boxed{
\text{calculate}
\to
\text{four-chain DSD audit}
\to
\text{cross-audit}
\to
\text{branch/prune}
\to
\text{calculate again}.
}
\]

---

## 10. Scope

This protocol does not claim that the Formation Axiom System or axial-property framework replaces standard mathematical proof.

Its role here is an independent algorithmic consistency layer for controlling branch formation, descriptor validity, aggregation, and state transitions during the proof attempt.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]