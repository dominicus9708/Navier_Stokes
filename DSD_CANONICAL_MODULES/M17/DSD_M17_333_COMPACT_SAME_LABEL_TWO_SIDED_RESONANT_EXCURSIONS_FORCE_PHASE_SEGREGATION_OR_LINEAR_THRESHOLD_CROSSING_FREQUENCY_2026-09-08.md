# DSD M17-333 — Compact same-label two-sided resonant excursions force phase segregation or linear threshold-crossing frequency

Date: 2026-09-08  
Canonical ID: **M17-333**

Status: **ACTIVE COMPACT-DYNAMICAL REDUCTION / CONDITIONAL ON A COMPACT SAME-LABEL LIFT**

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Input from M17-332

On the non-phase-locked branch, one same material genealogy has, along arbitrarily long intervals, positive-density occupancy on both sides of the resonant level.

Write

\[
q=\kappa-\frac32.
\]

For some `delta>0`, M17-332 gives positive lower densities in

\[
U_-:=\{q<-\delta\},
\qquad
U_+:=\{q>\delta\}.
\]

M17-332 correctly did **not** infer a linear crossing count from this alone.

## 2. Compact same-label lifted hull hypothesis

Assume the material genealogy can be represented by a continuous flow

\[
\varphi^t:X\to X
\]

on a compact metric lifted state space `X`, with `q:X->R` continuous, and the retained trajectory is one orbit of this flow.

This is stronger than compactness of the Eulerian state hull alone: the same-label/genealogy coordinate must also remain in the compact lift.

Failure of this hypothesis is a typed exit:

\[
\boxed{G_{noncompact/path/genealogy\ lift}.}
\]

## 3. Empirical invariant measure

Take the long intervals from M17-332 and the empirical measures

\[
\mu_T
:=
\frac1T\int_0^T\delta_{\varphi^t x}\,dt.
\]

Compactness gives weak-* subsequential limits.  Any such limit `mu` is invariant under the flow.

On a subsequence for which the two-sided occupancy lower bounds persist, choose `delta` away from any limiting boundary atom if necessary.  Then

\[
\boxed{
\mu(U_-)>0,
\qquad
\mu(U_+)>0.
}
\]

## 4. Ergodic-component split

Decompose `mu` into ergodic components.

There are two possibilities.

### Branch A — invariant phase segregation

No single ergodic component gives positive mass to both `U_-` and `U_+`.

Then the sub-resonant and super-resonant populations are carried by different invariant components in the same-label lift.

This is a genuine structural exit:

\[
\boxed{H_{invariant\ phase\ segregation}.}
\]

The ensemble can have both phases while no recurrent same-label component transports between them.

### Branch B — one ergodic component contains both phases

There exists an ergodic invariant probability `nu` such that

\[
\nu(U_-)>0,
\qquad
\nu(U_+)>0.
\]

We now show that sparse crossing cannot survive in this component.

## 5. A finite-lag transition set has positive measure

Because `nu` is ergodic and both open sets have positive measure, there exists a finite time `tau>0` such that

\[
\boxed{
\nu\bigl(U_-\cap\varphi^{-\tau}U_+\bigr)>0
}
\]

or, after interchanging signs,

\[
\nu\bigl(U_+\cap\varphi^{-\tau}U_-\bigr)>0.
\]

Indeed, if every time translate of `U_+` were disjoint from `U_-` modulo `nu`, the invariant saturation of `U_+` would give a nontrivial invariant separation, contradicting ergodicity.

Set

\[
A_\tau:=U_-\cap\varphi^{-\tau}U_+,
\qquad
\alpha_\tau:=\nu(A_\tau)>0.
\]

## 6. Positive density of transition windows

For a `nu`-generic orbit, the continuous-time ergodic theorem gives

\[
\frac1T
\left|
\{s\in[0,T]:\varphi^s x\in A_\tau\}
\right|
\to
\alpha_\tau.
\]

Every such starting time `s` satisfies

\[
q(s)<-\delta,
\qquad
q(s+\tau)>\delta.
\]

By continuity of `q`, the interval `[s,s+tau]` contains at least one crossing of

\[
q=0
\quad\Longleftrightarrow\quad
\kappa=\frac32.
\]

## 7. Linear lower bound on crossing number

Let `N_{3/2}(T)` be the number of distinct topological crossings of `kappa=3/2` up to time `T`, counting separated sign-changing crossing events.

A single crossing time can lie in transition windows `[s,s+tau]` only for starting times `s` in an interval of length at most `tau`.

Hence, modulo endpoint errors,

\[
\left|
\{s\in[0,T]:\varphi^s x\in A_\tau\}
\right|
\le
\tau N_{3/2}(T+\tau)+O(\tau).
\]

Therefore

\[
\boxed{
\liminf_{T\to\infty}
\frac{N_{3/2}(T)}{T}
\ge
\frac{\alpha_\tau}{\tau}>0.
}
\]

Thus, inside one ergodic compact same-label component containing both phases, the resonant threshold is crossed with positive asymptotic frequency.

## 8. Transversality firewall

The result above counts **topological sign-changing crossings**.

It does not yet identify each crossing with the smooth delta-current

\[
\int |D_B\kappa|\,\delta(\kappa-3/2)d\theta.
\]

For that conversion one needs a regular-crossing condition, for example

\[
|D_B\kappa|\ge h_*>0
\]

at a fixed fraction of crossings, or a separate finite-order degeneracy theorem.

Otherwise there is a typed exit:

\[
\boxed{G_{degenerate\ resonant\ crossing}.}
\]

## 9. Scale firewall

M17-330 remains active.

The linear `3/2` crossing frequency is a **fixed-generation recurrent-hull statement**.  It is not itself a record-scale-invariant ancestry currency.

Only the zero-level directed crossing currency of M17-326 has the homogeneous cross-generation scaling.

## 10. DSD-theory role

The useful DSD heuristic is to ask whether apparently coexisting phases belong to the same dynamically closed structure.

The standard mathematical translation is the ergodic-component split:

\[
\boxed{
\text{two phases in empirical state}
\Rightarrow
\text{different invariant components}
\lor
\text{one component with actual repeated transport}.
}
\]

No DSD axiom is used as a PDE hypothesis.

## 11. Updated excursion frontier

Under the compact same-label lift,

\[
\boxed{
H_{two\text{-}sided\ 3/2\ excursions}
\Longrightarrow
H_{invariant\ phase\ segregation}
\lor
H_{linear\ 3/2\ crossing\ frequency}
\lor
G_{noncompact/genealogy\ lift}.
}
\]

The next step is to test whether the linear crossing branch can be converted into a fixed positive PDE payer, and whether the phase-segregation branch is compatible with the global CE-H elliptic negative-`kappa` balance without material replacement.

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
