# DSD Audit — Aksman Global Regularity Without Uniqueness / Branching at Reconnection

Date: 2026-09-06
Source family: Michael Aksman, Zenodo records including 21264022, 21432387, 21607213, 21854704, 21940456.
Audit status: **SMOOTH-BRANCHING CONTRADICTS LOCAL STRONG UNIQUENESS; OTHERWISE REGULARITY FAILS AT THE BRANCH**

## 1. Public central thesis

The public descriptions state:

\[
\boxed{
\text{arbitrary smooth data generate globally smooth solutions, but the solution branches non-uniquely at vortex reconnections.}
}
\]

Each reconnection is said to admit finitely many topologically distinct smooth continuations, producing a finite tree of smooth trajectories.

## 2. Local uniqueness audit

For the classical 3D incompressible Navier–Stokes equations, sufficiently regular strong solutions enjoy local uniqueness. In particular, if at a time `t_*` the state

\[
u(t_*)
\]

is smooth enough to serve as classical initial data, then the local well-posedness theorem gives a unique strong solution on some interval

\[
[t_*,t_*+\varepsilon).
\]

Therefore two distinct smooth branches cannot depart from exactly the same smooth state at `t_*` while both solve the same unmodified NSE.

Symbolically:

\[
\boxed{
\text{smooth state at branch time}
\Rightarrow
\text{local strong uniqueness}
\Rightarrow
\text{no smooth branching}.
}
\]

## 3. The only alternative

Suppose the reconnection state is not regular enough for local strong uniqueness to apply.

Then the proposed branch point is itself a loss of the regularity class required by the claimed theorem.

Thus:

\[
\boxed{
\text{branching possible only after leaving the smooth/strong corridor}
}
\]

is incompatible with the statement that every branch is globally smooth through the reconnection.

This yields a direct dichotomy:

\[
\boxed{
\begin{cases}
\text{state is smooth} &\Rightarrow \text{branching impossible},\\
\text{state is not smooth} &\Rightarrow \text{global smoothness already failed}.
\end{cases}
}
\]

## 4. Convex-integration comparison audit

The public description invokes nonuniqueness proved by convex-integration methods as precedent for physical branching.

This analogy does not establish nonuniqueness of classical smooth solutions. Convex-integration nonuniqueness concerns much weaker solution classes/regularities. It does not override weak–strong uniqueness: whenever a classical strong solution exists, admissible weak solutions in the corresponding weak–strong uniqueness class must coincide with it on that interval.

Therefore

\[
\text{weak-solution nonuniqueness}
\not\Rightarrow
\text{smooth-solution branching}.
\]

## 5. Reconnection as physical versus mathematical event

Viscous vortex tubes may undergo changes of topology in physical/numerical descriptions without the velocity field becoming nonunique. A smooth vector field can change the topology of selected vorticity isosurfaces/filament labels while the PDE solution remains uniquely determined.

Thus “reconnection admits several topological rejoinings” is not by itself a theorem that the velocity field has several solutions.

To prove true branching, one would have to construct two distinct smooth velocity fields `u^{(1)},u^{(2)}` satisfying

\[
u^{(1)}(t_*)=u^{(2)}(t_*)
\]

and the same NSE for `t>t_*`, contradicting the standard local strong uniqueness theorem. No topological relabeling alone can do this.

## 6. Relation to the Clay statement

The public text says the Clay formulation requires existence/smoothness but not uniqueness and therefore nonunique smooth branches could still solve the problem.

Even if uniqueness were not part of the particular Clay alternative being targeted, the mathematical NSE itself still has local uniqueness in the smooth class. One cannot gain existence by postulating a behavior forbidden by the local equation.

## 7. Interaction with the vorton/core arguments

This audit is independent of the separate questions of:

- vorton density/completeness;
- finite positive core floor;
- helicity quantum per reconnection;
- finite branch-tree count;
- Kolmogorov-scale UV cutoff.

Those are audited separately. Even granting all of them provisionally, smooth nonunique branching from a common smooth state remains incompatible with classical local well-posedness.

## 8. DSD verdict

\[
\boxed{
\text{“globally smooth but branches non-uniquely at reconnection” cannot hold for the same classical NSE state.}
}
\]

The branch point must either remain smooth, in which case local uniqueness forbids branching, or fail to be smooth, in which case the claimed global regularity has already broken down.

Global regularity remains unproved.
