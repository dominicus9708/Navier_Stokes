# DSD M17-330 — Zero-kappa crossing is record-scale critical while the three-halves resonant level is representation-dependent

Date: 2026-09-08  
Canonical ID: **M17-330**

Status: **ACTIVE SCALE/REPRESENTATION AUDIT**

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Input from M17-326 and M17-329

M17-326 introduced the directed pure-material-flux crossing currency at level `a`:

\[
\mathcal C_-^{(a)}(I)
:=
\int_I\!\int
(D_B\kappa)_-\,\delta(\kappa-a)\,d\Phi\,d\theta.
\]

At `a=0`, M17-326 found exact record-scale criticality.

M17-329 separately identified two dynamical levels in one fixed similarity representation:

\[
\kappa=0
\]

for raw material-flux growth/decay, and

\[
\kappa=\frac32
\]

for similarity-Jacobian-normalized flux growth/decay.

The present module audits whether these two levels have the same cross-generation status.

## 2. Record blow-down scaling

Under the record blow-down by factor `R`, use

\[
\kappa_R(y,s)=R^2\kappa(Ry,R^2s),
\]

and

\[
h_R:=D_{B_R}\kappa_R
=R^4 h(Ry,R^2s),
\qquad h=D_B\kappa.
\]

The oriented material flux element is scale invariant:

\[
d\Phi_R=d\Phi,
\]

while

\[
ds=R^{-2}dt.
\]

For a fixed numerical level `a`,

\[
\delta(\kappa_R-a)
=
\delta(R^2\kappa-a)
=
R^{-2}\delta\!\left(\kappa-\frac{a}{R^2}\right).
\]

Therefore

\[
\begin{aligned}
\mathcal C_{-,R}^{(a)}(I)
&=
\int_I\!\int
(h_R)_-\delta(\kappa_R-a)d\Phi_Rds\\
&=
\int_{R^2I}\!\int
R^4 h_-\,
R^{-2}\delta\!\left(\kappa-\frac{a}{R^2}\right)
\,d\Phi\,R^{-2}dt.
\end{aligned}
\]

Hence

\[
\boxed{
\mathcal C_{-,R}^{(a)}(I)
=
\mathcal C_-^{(a/R^2)}(R^2I).
}
\]

## 3. Unique fixed threshold

A numerical threshold is fixed by record blow-down only if

\[
a=\frac{a}{R^2}
\]

for all admissible `R`.

Thus the only finite fixed level is

\[
\boxed{a=0.}
\]

Consequently

\[
\boxed{
\mathcal C_{-,R}^{(0)}(I)
=
\mathcal C_-^{(0)}(R^2I),
}
\]

which is the exact criticality of M17-326.

By contrast,

\[
\boxed{
\mathcal C_{-,R}^{(3/2)}(I)
=
\mathcal C_-^{(3/(2R^2))}(R^2I).
}
\]

The level `3/2` is therefore not a record-generation fixed threshold.

## 4. Interpretation of the three-halves level

The value `3/2` arose in M17-329 from

\[
\nabla\cdot B=\frac32
\]

and the renormalized flux law

\[
D_B\log\widehat\Phi
=
\kappa-\frac32.
\]

It is a natural threshold **inside one fixed similarity normalization**.

It is not a scale-homogeneous coefficient level under a further record blow-down.

Thus the following inference is rejected:

\[
\boxed{
\text{critical crossing at }\kappa=0
\Rightarrow
\text{same critical ancestry currency at }\kappa=3/2.
}
\]

## 5. DSD-theory heuristic and standard translation

The useful DSD heuristic is:

> remove representation-dependent offsets before declaring a structural transition invariant.

Its standard mathematical translation is exactly the scaling calculation above.

No DSD axiom is used as a PDE assumption.

The distinction is now:

\[
\boxed{
\kappa=0:
\text{homogeneous / record-scale fixed / cross-generation critical},
}
\]

\[
\boxed{
\kappa=3/2:
\text{fixed-similarity resonant threshold / not record-scale fixed}.
}
\]

## 6. Consequence for the proof strategy

The M17-329 proposed two-threshold transport problem must be split by scope.

### Cross-generation scope

Use only homogeneous quantities such as the zero-level crossing currency.

### Fixed-generation recurrent-hull scope

The `3/2` threshold remains useful for testing whether the similarity-Jacobian-normalized flux is increasing or decreasing.

But any result at `3/2` must be re-derived after each change of similarity scale; it cannot be imported as the same ancestry currency.

## 7. Updated target

The next safe calculation is therefore the fixed-generation stationary pure-flux balance

\[
\partial_k\overline G=k\overline F
\]

and the exact relation between the currents at `k=0` and `k=3/2`.

This can determine whether the already certified negative zero-level current actually forces any current across the resonant level, without assuming it does.

## 8. Audit verdict

**PASS as a representation correction.**

The DSD theoretical layer improved the calculation by preventing a false identification of two numerically distinguished thresholds across record generations.  The canonical conclusion is purely a Navier--Stokes scaling statement.

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
