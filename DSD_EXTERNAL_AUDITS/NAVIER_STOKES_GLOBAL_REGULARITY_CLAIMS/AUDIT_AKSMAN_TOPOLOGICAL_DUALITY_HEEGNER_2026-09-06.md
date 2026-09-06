# DSD Audit — Aksman Topological Duality / Heegner Spectral Compactification

Date: 2026-09-06
Source family: Michael/Mikhail Aksman, *GLOBAL REGULARITY OF 3D NAVIER STOKES VIA TOPOLOGICAL DUALITY*, Zenodo records including 20635526 and later versions including 21263877.
Audit status: **EQUIVALENCE OPERATOR ASSUMED / CONDITIONAL MODEL TRANSFER**

## 1. Public starting point

The public record formulates the classical NSE and then states, in substance:

\[
\text{Assume there exists a Duality Operator }
T:u(x,t)\mapsto\Phi(\tau)
\]

mapping the velocity field to a modular phase space

\[
\Gamma=SL(2,\mathbb Z)\backslash\mathbb H
\]

with discrete/arithmetic data such as

\[
N=861,\qquad D=-163.
\]

Later versions describe finite spectral information capacity associated with this arithmetic manifold and use it as an ultraviolet/complexity closure mechanism.

## 2. DSD equivalence obligation

Introducing a map to another mathematical object can aid a proof only if the map is shown to preserve enough of the original problem.

For an unconditional solution of the Clay NSE statement, one must prove at minimum:

1. **Existence:** `T(u)` is defined for every solution/data class under consideration.
2. **Faithfulness:** distinct PDE states relevant to blow-up are not identified in a way that discards singularity information.
3. **Dynamics:** NSE evolution maps to a rigorously derived evolution/constraint in the target space.
4. **Nonlinearity:** the quadratic triad/convolution structure is preserved or controlled under `T`.
5. **Norm/regularity bridge:** boundedness/finite capacity of `T(u)` implies the specific Sobolev/BKM/critical norm needed for smoothness of `u`.
6. **Reverse implication:** a target-space compactness statement can be pulled back to the original velocity field with constants independent of unresolved scales.

Without these, target-space regularity need not imply NSE regularity.

## 3. Conditionality in the public formulation

Because the record begins by **assuming** the duality operator, the arithmetic conclusions logically have the form

\[
\boxed{
\text{Duality/equivalence hypotheses}
\Rightarrow
\text{finite target-space capacity}.
}
\]

They do not by themselves establish

\[
\boxed{
\text{classical NSE}
\Rightarrow
\text{those duality/equivalence hypotheses}.
}
\]

Calling the latter unconditional would reverse the dependency.

## 4. Information-capacity audit

A finite number of target labels/bits does not automatically bound an infinite-dimensional PDE state. A finite-dimensional encoding can be:

- lossy;
- data-dependent;
- scale-dependent;
- noninjective;
- insufficient to control derivatives.

Therefore a statement such as “the target manifold has finite spectral information capacity” must be accompanied by a theorem converting that capacity into a uniform NSE norm bound.

Otherwise the argument risks the general invalid inference

\[
\text{finite descriptor complexity}
\not\Rightarrow
\text{finite derivative complexity of the represented field}.
\]

## 5. Arithmetic uniqueness audit

Special arithmetic facts such as class-number-one properties of `D=-163` are valid number-theoretic facts. Their validity does not establish that `D=-163` is a compulsory invariant of arbitrary 3D Navier–Stokes flows.

The mathematical obligation is not to prove the arithmetic theorem again, but to prove the **PDE-to-arithmetic identification**.

## 6. Relation to later vorton versions

Some later versions combine the arithmetic compactification with a vorton UV cutoff. This does not remove the earlier bridge obligation. It adds a second one: the vorton representation/cutoff must itself be equivalent to unrestricted classical NSE, which is audited separately in the exact-vorton files.

## 7. DSD verdict

\[
\boxed{
\text{The target-space duality is an assumption/bridge, not an established consequence of classical NSE in the public formulation.}
}
\]

Therefore arithmetic finite-capacity results are at most conditional until a faithful two-way PDE equivalence theorem is supplied.

Global regularity remains unproved.
