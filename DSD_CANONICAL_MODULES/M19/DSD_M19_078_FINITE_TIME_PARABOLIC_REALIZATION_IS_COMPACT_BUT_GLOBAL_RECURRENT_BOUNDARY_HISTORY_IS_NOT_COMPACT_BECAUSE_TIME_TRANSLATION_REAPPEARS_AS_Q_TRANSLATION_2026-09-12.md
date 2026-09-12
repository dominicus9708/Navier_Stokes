# DSD M19-078 — Finite-time parabolic realization is compact but global recurrent boundary history is not compact because time translation reappears as q translation

Date: 2026-09-12

Status: **REALIZATION-COMPACTNESS AUDIT / POSITIVE-TIME VISCOUS EVOLUTION FROM A FIXED FINITE CORE TO A FIXED SPECTATOR BOUNDARY IS SMOOTHING AND COMPACT IN STANDARD LOCAL SOBOLEV/TRACES, BUT THE FULL SCATTERING DATUM IS NOT THE OUTPUT OF ONE SUCH FINITE-TIME MAP: IT IS AN ENCODING OF THE COMPLETE BOUNDARY HISTORY OVER AN UNBOUNDED SIMILARITY-TIME AXIS / HISTORY TRANSLATIONS REMAIN NONCOMPACT AND BECOME EXACT q-TRANSLATIONS / THEREFORE LOCAL PARABOLIC COMPACTNESS DOES NOT IMPLY A FINITE-DIMENSIONAL GLOBAL CENTER OR EXCLUDE APERIODIC RECURRENT SCATTERING / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. The proposed compactness route

M19-077 isolated the missing object as an interior realization map from finite-radius recurrent dynamics to spectator-boundary/scattering data.

A natural hope is:

\[
\text{viscosity}
\Longrightarrow
\text{parabolic smoothing}
\Longrightarrow
\text{compact realization map}
\Longrightarrow
\text{finite-dimensional center}.
\]

M19-078 audits each arrow.

---

## 2. Positive-time local parabolic smoothing is genuine

Fix radii

\[
R_{core}<R_{spec}<\infty
\]

and a bounded spatial domain \(\Omega\) containing the region between them.

For the linearized similarity Navier--Stokes equation along a smooth compact-corridor background,

\[
\partial_\theta W
=L(\theta)W,
\]

standard local parabolic regularity gives, for every positive time lag \(\tau_0>0\), schematic estimates of the form

\[
\boxed{
\|W(\theta_0+\tau_0)\|_{H^{s+2}(\Omega')}
\le
C_{\tau_0,\Omega',\Omega}
\|W(\theta_0)\|_{H^s(\Omega)}
}
\]

for \(\Omega'\Subset\Omega\), modulo the usual pressure/divergence-compatible formulation.

Boundary trace then gives higher regularity on the fixed spectator sphere.

Combining smoothing with Rellich compactness yields:

\[
\boxed{
\text{for fixed }\tau_0>0,
\text{ bounded interior data map compactly into a weaker spectator-boundary trace space.}
}
\]

This is a real compactness statement.

---

## 3. A fixed q-window is also locally compact

At the spectator boundary,

\[
q
=\rho_{spec}-\frac{\theta_{cross}}2,
\qquad
\rho_{spec}:=\log R_{spec}.
\]

A bounded q-window

\[
q\in[q_1,q_2]
\]

corresponds to a bounded similarity-time interval

\[
\theta_{cross}
\in
[2(\rho_{spec}-q_2),\,2(\rho_{spec}-q_1)].
\]

Therefore local-in-time compactness of the boundary history transfers to compactness of the scattering datum on every fixed finite q-window, assuming the usual uniform derivative bounds.

Thus

\[
\boxed{
A_n\text{ is precompact in }X_{loc}(\mathbb R_q)
}
\]

is compatible with the existing corridor.

This agrees with M19-072.

---

## 4. The full scattering datum uses the entire history axis

The scattering object is

\[
A(q,\omega),
\qquad q\in\mathbb R
\]

or at least an unbounded half-line in the relevant tail representation.

At the fixed spectator radius, changing q by \(h\) changes the historical crossing time by

\[
\boxed{
\theta_{cross}(q+h)
=
\theta_{cross}(q)-2h.
}
\]

Hence global q-translation is exactly boundary-history time translation.

The full map is therefore better represented as

\[
\boxed{
\mathscr H:
\text{complete interior trajectory}
\longmapsto
\{B(\theta)\}_{\theta\in\mathbb R}
\longmapsto
A(q),
}
\]

not as one finite-time smoothing operator.

---

## 5. Translation sequence defeats global compactness

Let \(B_0(\theta)\) be any nontrivial smooth bounded boundary history allowed by the abstract regularity class.

Define

\[
\boxed{
B_n(\theta):=B_0(\theta-n).
}
\]

On every bounded time interval, a subsequence may converge locally after using compact recurrent-hull information.

But in a global translation-invariant norm such as an unweighted \(L^p_\theta\), uniform Sobolev space, or bounded-uniform topology retaining the whole axis, the sequence need not be compact.

Under the q-history dictionary,

\[
B_n(\theta)
\leftrightarrow
A_n(q)=A_0(q+n/2)
\]

up to the fixed sign convention.

Therefore the noncompactness is precisely the q-translation escape already seen in M19-072.

Hence

\[
\boxed{
\text{finite-time compactness}
\not\Rightarrow
\text{global history compactness}.
}
\]

---

## 6. Why recurrence does not repair this

A compact recurrent hull is compact in the chosen state topology, which is fundamentally local in physical/similarity space and finite-window in time through the flow.

But a continuous observable of a compact recurrent system can generate a quasiperiodic or more general almost-periodic complete history.

Thus

\[
\boxed{
\text{compact recurrent state hull}
\not\Rightarrow
\text{compact set of full histories modulo no translations in a norm strong enough to kill aperiodicity}.
}
\]

An irrational torus flow remains the abstract model firewall.

Parabolic smoothing does not alter this dynamical fact.

---

## 7. Exponentially weighted history norms are not a free solution

One can force compactness of translated histories by introducing a temporal weight such as

\[
e^{-c|\theta|}
\]

or a one-sided exponential weight.

But such a weight breaks time-translation equivariance.

Under the q dictionary it becomes an exponential q-weight and creates an artificial preference for one historical origin.

The resulting spectral gap can measure transport of a packet through the weight rather than genuine decay of the translation factor.

Therefore

\[
\boxed{
\text{weighted-history compactness}
\neq
\text{translation-factor rigidity}
}
\]

unless a separate argument shows that the weighted norm is dynamically intrinsic.

---

## 8. Compactness of the finite-time evolution operator does not imply compactness of the complete cocycle center

For an autonomous parabolic equation on a bounded domain, compact resolvent often implies discrete spectrum.

The present problem differs in two ways:

1. the domain is effectively whole-space with a critical remote tail;
2. the recurrent background produces a nonautonomous complete cocycle and the scattering variable records an unbounded history axis.

Even if each positive-time local evolution operator

\[
\Phi(\theta+\tau,\theta)
\]

is compact between local spaces, the collection of translated complete histories can still contain an infinite-dimensional or nontrivial recurrent center when viewed through the global factor observable.

One must not infer a finite center dimension from local compactness alone.

---

## 9. What compactness does buy

The local compactness is still useful.

It implies that any hypothetical sequence of extra center modes can, after normalization and symmetry-safe rotation gauge, be extracted on bounded spacetime windows to a nonzero local ancient linearized solution.

Thus a failure of center rigidity can be converted into a **local complete center witness**.

Symbolically,

\[
\boxed{
\text{failure of transverse center rigidity}
\Longrightarrow
\text{nonzero locally smooth bounded complete linearized witness}
}
\]

provided normalization prevents vanishing.

This is a cleaner object for a Liouville theorem.

What compactness does not give is that the witness must be time-periodic or finite-dimensional.

---

## 10. Revised strategy

The correct use of parabolic compactness is therefore not

\[
\text{compactness}\Rightarrow\text{finite center},
\]

but

\[
\boxed{
\text{compactness}
\Rightarrow
\text{extract a normalized bounded complete transverse linearized witness}
\Rightarrow
\text{seek a Liouville/observability theorem for that witness}.
}
\]

This changes the immediate target from global functional-analytic compactness to a concrete PDE classification problem.

---

## 11. New theorem target

After fixing center position and quotienting rotations, suppose there exists a bounded complete linearized solution \(W\) satisfying

\[
\partial_\theta W=L(\theta)W,
\]

with

\[
W\notin\operatorname{span}\{\partial_\theta U\}.
\]

The live theorem is now

\[
\boxed{
\mathcal T_{linear\ Liouville}:
\text{no such normalized bounded complete rotation-transverse witness exists on the recurrent corridor.}
}
\]

If \(\mathcal T_{linear\ Liouville}\) holds, the extra center is excluded without requiring global history compactness.

---

## 12. Next calculation

M19-079 should test the natural energy identity for such a complete bounded witness over the entire similarity-time line.

The key question is whether integrating the radial-A2 weighted energy inequality over \((\theta_-,\theta_+)\) and using recurrence/bounded completeness can force the positive dissipation/gap terms to vanish after suitable long-time averaging, or whether the strain defect can exactly balance them.

This directly probes the proposed linear Liouville theorem.
