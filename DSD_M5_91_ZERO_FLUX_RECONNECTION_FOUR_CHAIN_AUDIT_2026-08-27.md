# DSD M5-91 — Four-Chain Audit of the Zero-Flux Reconnection Endpoint

Date: 2026-08-27

Status: **DSD PARALLEL AUDIT APPLIED / THE ZERO-ANGULAR-GAP ENDPOINT IS NOT IMMEDIATELY CONTRADICTORY / FORMATION REJECTS PUNCTURED SOURCE-SINK ESCAPES, AXIAL AUDIT FIXES SIGN CHANNELS, STATIC AGGREGATION FORCES MULTI-BOUNDARY SIGNED-AREA BALANCE, AND DYNAMICS IDENTIFIES THE ONLY ALLOWED SIGN-CHANGE TRANSITIONS / GLOBAL REGULARITY UNPROVED.**

## 1. Raw mathematical input

Work on one exact positive minimal-payer endpoint inside the fixed active amplitude band.

Let

\[
a=|U|,
\qquad
n=\frac{\nabla a}{|\nabla a|}
\]

on regular levels.

The endpoint conditions include

\[
X_w>0,
\qquad
X_w=\nu(T-A_w-G_w),
\]

and

\[
P-m_{P,k}=2\nu b,
\qquad
b=U\cdot\nabla\log a.
\]

The strongest zero-angular candidate is

\[
G_w=0.
\]

The purpose of this memo is not to derive a new numerical estimate first, but to run the candidate through the four DSD chains.

---

# 2. Formation-Axiom chain F

## F0 — formed objects

At a fixed regular amplitude value `lambda>0`, let

\[
\Omega_{\lambda,k}
\]

be one bounded connected component of the superlevel set and let

\[
\Gamma_{\lambda,k}=\partial\Omega_{\lambda,k}
\]

be its full induced boundary.

If the boundary has several connected surface components, write

\[
\Gamma_{\lambda,k}
=
\bigsqcup_{j=1}^{N_k}\Gamma_j.
\]

These surface components are distinct formed objects inside one connected volume component.

## F1 — defined / undefined

This description is valid only on a regular level, where

\[
|\nabla a|>0
\]

on the boundary.

At a critical topology-changing value, the regular surface labels may cease to be defined. Such an event is recorded as an undefined transition, not a contradiction.

## F2 — boundary is not an external source

The surfaces `Gamma_j` are internal amplitude boundaries of one smooth whole-space velocity field.

They are **not physical walls, sources, drains, or punctures**.

Therefore a punctured radial source/sink model may serve as a local differential model but fails the formed W1 class if it requires a distributional source.

This reproduces the M5-87 rejection at the Formation-Axiom level:

\[
\boxed{
\text{punctured source/sink escape}
\Rightarrow
\text{FORMATION REJECT}.
}
\]

## F3 — componentwise zero-flux channel

For the full boundary of each bounded connected superlevel component,

\[
\boxed{
\int_{\Gamma_{\lambda,k}}U\cdot n\,dS=0
}
\]

up to the fixed sign convention for `n` versus the outward normal.

The full boundary is the correct formed aggregation object.

It is invalid to impose this zero independently on every connected surface piece unless separately proved.

## F4 — Formation verdict

A smooth multi-boundary superlevel component is admissible.

Therefore Formation alone does **not** eliminate the `G=0` endpoint.

Status:

\[
\boxed{\mathfrak F: \text{SPLIT}}
\]

into

1. forbidden punctured/source escape;
2. admissible smooth multi-boundary internal reconnection.

---

# 3. Axial-property chain X

## X0 — axes

On a regular amplitude boundary there are three relevant spatial directions:

- normal axis `n`;
- tangential plane `T Gamma`;
- streamline direction `e=U/a`.

## X1 — zero angular gap

Pointwise zero angular gap means

\[
U\times\nabla a=0.
\]

Since `a=lambda>0` on the level,

\[
\boxed{
U=\sigma\lambda n,
\qquad
\sigma\in\{+1,-1\}.
}
\]

On one connected regular surface `Gamma_j`, continuity forces `sigma` to be constant because it cannot change from `+1` to `-1` without passing through a zero normal component, while `|U|=lambda>0` and `U` is exactly normal.

Thus every connected surface component receives a discrete axial orientation label

\[
\boxed{
\sigma_j=\pm1.
}
\]

## X2 — crossing variable

At `G=0`,

\[
b
=
\frac{|\nabla a|}{a}(U\cdot n)
=
\sigma_j|\nabla a|.
\]

Therefore

\[
\boxed{|b|=|\nabla a|}
\]

on every regular active surface.

## X3 — pressure axis lock

The exact endpoint gives

\[
P-m_{P,k}=2\nu b.
\]

Hence on `Gamma_j`,

\[
\boxed{
P-m_{P,k}
=2\nu\sigma_j|\nabla a|.
}
\]

Pressure fluctuation and crossing orientation have exactly the same sign.

## X4 — Axial verdict

The endpoint does not require zero crossing. It requires two signed crossing orientations carried by different surface pieces if the full component flux is to cancel.

Status:

\[
\boxed{\mathfrak X: \text{PASS WITH DISCRETE SIGN LABELS}.}
\]

---

# 4. Static-aggregation chain S

## S0 — full-boundary signed flux

Using

\[
U\cdot n=\sigma_j\lambda
\]

on each connected boundary surface,

\[
0
=
\int_{\Gamma_{\lambda,k}}U\cdot n\,dS
=
\lambda
\sum_j
\sigma_j|\Gamma_j|.
\]

Because `lambda>0`,

\[
\boxed{
\sum_j\sigma_j|\Gamma_j|=0.
}
\]

Define

\[
A_+
:=
\sum_{\sigma_j=+1}|\Gamma_j|,
\qquad
A_-
:=
\sum_{\sigma_j=-1}|\Gamma_j|.
\]

Then

\[
\boxed{A_+=A_-.}
\]

This is an exact static signed-area balance.

## S1 — single-surface consequence

If the full boundary of the connected volume component had only one connected regular surface, then `sigma` would be constant and

\[
\int_\Gamma U\cdot n
=
\pm\lambda|\Gamma|
\ne0.
\]

Therefore

\[
\boxed{
G=0,\ T>0
\Longrightarrow
N_k\ge2
}
\]

for every active bounded connected component that carries the exact crossing endpoint.

Thus the zero-angular endpoint necessarily has a **multi-boundary topology**.

## S2 — componentwise pressure mean gives the same condition

The componentwise coarea pressure mean obeys

\[
\int_{\Gamma_{\lambda,k}}
\frac{P-m_{P,k}}{|\nabla a|}\,dS=0.
\]

Using the exact endpoint relation,

\[
0
=2\nu
\sum_j\sigma_j|\Gamma_j|.
\]

So the pressure-centering condition produces exactly the same signed-area balance as incompressibility.

This is an important cross-check: the two constraints are compatible, not contradictory.

## S3 — signed flux cancels but pressure work does not

The centered pressure work is

\[
J_{P,k}
=
\int_{\Gamma_{\lambda,k}}
(P-m_{P,k})U\cdot n\,dS.
\]

At the endpoint,

\[
(P-m)U\cdot n
=
2\nu\sigma_j|\nabla a|\,\sigma_j\lambda
=
2\nu\lambda|\nabla a|.
\]

Therefore

\[
\boxed{
J_{P,k}
=
2\nu\lambda
\int_{\Gamma_{\lambda,k}}|\nabla a|\,dS
>0
}
\]

for every nondegenerate active component.

Hence

\[
\boxed{
\text{zero signed mass flux}
\not\Rightarrow
\text{zero pressure work}.
}
\]

The pressure field correlates its sign with the crossing sign so that inward and outward crossing both contribute positive work.

This closes the naive static contradiction.

## S4 — Static verdict

The exact `G=0` endpoint survives static aggregation only in the highly constrained state

\[
\boxed{
\begin{array}{c}
\text{at least two boundary surfaces per active volume component},\\
A_+=A_-,\\
P-m=2\nu\sigma_j|\nabla a|,\\
J_{P,k}>0.
\end{array}
}
\]

Status:

\[
\boxed{\mathfrak S: \text{PASS, BUT TOPOLOGICALLY RIGID}.}
\]

---

# 5. Dynamical chain D

## D0 — tracked objects

Track one regular boundary surface branch `Gamma_j(s)` only while it remains regular and topologically identifiable.

## D1 — sign persistence under exact zero angular gap

On a smooth time interval with

\[
G=0,
\qquad
|U|=\lambda>0
\]

on the tracked surface, the sign label

\[
\sigma_j(s)=\operatorname{sgn}(U\cdot n)
\]

cannot change continuously.

Thus

\[
\boxed{
\sigma_j(s)=\text{constant}
}
\]

on every regular topology-preserving exact-zero-gap interval.

## D2 — allowed sign-change mechanisms

A sign reversal can occur only if the tracked description passes through one of two transitions.

### Route A — angular departure

At some stage

\[
U\times\nabla a\ne0,
\]

so `G` becomes positive and the velocity can pass through a tangential configuration while the normal component changes sign.

### Route B — critical/topology transition

The regular level branch ceases to be defined because

\[
\nabla a=0
\]

or the component graph merges, splits, is born, or dies.

The old sign label is then not continued through the undefined transition without reconstruction.

Therefore

\[
\boxed{
\text{sign change}
\Rightarrow
G>0
\quad\text{or}\quad
\text{critical/topology transition}.
}
\]

## D3 — recurrence caution

W1 recurrence does not by itself require the same individual boundary labels to return.

Hence one may not infer a contradiction merely because the static sign graph is nontrivial.

The recurrent object is the Leray state in the chosen W1 topology, not a permanently labelled surface graph.

## D4 — Dynamical verdict

The surviving exact endpoint splits dynamically into

\[
\boxed{
\begin{array}{ll}
R_{lock}:&\text{topology-preserving, sign-locked multi-boundary recurrence},\\
R_{switch}:&\text{recurrent angular or critical/topology switching}.
\end{array}
}
\]

Status:

\[
\boxed{\mathfrak D: \text{SPLIT}.}
\]

---

# 6. Four-chain cross-audit

## F <-> X

The sign axis is defined only on regular formed boundary surfaces.

PASS.

## X <-> S

Signed normal flux cancels, while its square and pressure covariance remain positive.

PASS; this removes the false `zero flux => zero pump` inference.

## S <-> D

Signed-area balance is a static state constraint. Individual `sigma_j` labels persist only on topology-preserving regular intervals.

PASS with transition bookkeeping.

## D <-> F

Critical topology events require reconstruction of the formed component graph; recurrence alone does not preserve old labels.

PASS.

---

# 7. DSD result of this audit

The zero-flux reconnection bottleneck is not one problem but two structurally different surviving corridors:

\[
\boxed{
\begin{array}{c}
\textbf{Corridor I: sign-locked multi-boundary endpoint}\
G\approx0,\quad A_+=A_-,\quad \text{persistent boundary graph};\\[2mm]
\textbf{Corridor II: switching endpoint}\
\text{sign reconnection through }G>0\text{ or critical/topology events}.
\end{array}
}
\]

This split was not visible if zero flux, angular gap, topology, and recurrence were treated as one calculation.

---

# 8. Next calculations dictated by the DSD audit

The two corridors require different mathematics.

### Corridor I

Use the signed-area identity

\[
A_+(\lambda,s)=A_-(\lambda,s)
\]

across a smooth amplitude interval and differentiate it in `lambda` and/or Leray time to derive geometric compatibility conditions on the persistent nested boundary graph.

### Corridor II

Quantify the cost of either

- nonzero angular departure `G`, or
- repeated critical/topology transitions,

and compare that cost with the endpoint requirement

\[
T>A_w+G_w.
\]

These are now separate proof branches.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]