# DSD Audit — Cox Critical-Endpoint / APMS Minimal-Element Claim

Date: 2026-09-06
Paper family: Joseph Thomas Cox, *Resolving Global Regularity for the 3D Navier–Stokes Equations at the Critical Endpoint*, DOI 10.5281/zenodo.17503936 and related versions.
Audit status: **CORE_HINGE_FAIL — MINIMAL ELEMENT NOT ESTABLISHED**

## 1. Claim architecture

The manuscript uses a Kenig–Merle-style rigidity program:

1. assume failure of a global `L_t^∞L_x^3` bound;
2. define a minimal threshold `M_*`;
3. choose finite-time solutions approaching that threshold;
4. rescale near peak times;
5. extract a nonzero ancient precompact `L^3` profile (APMS);
6. use Type-I/envelope/Carleman machinery to force the APMS to vanish;
7. contradiction.

The decisive dependency is step 2→5. If the definition does not produce a strictly positive finite threshold, the APMS cannot be extracted with the stated normalization.

## 2. Displayed definition

Theorem G.5 writes, in substance,

\[
M_*:=\inf\{M>0:\exists u\text{ suitable with }\sup_{t<T(u)}\|u(t)\|_{L^3}>M\}.
\]

The manuscript then selects `u_n` with finite `T_n` and

\[
\sup_{t<T_n}\|u_n(t)\|_3\downarrow M_*,
\]

and later asserts

\[
\|u_\infty(0)\|_3=M_*>0.
\]

## 3. DSD domain audit

There are two natural readings.

### Reading A — arbitrary suitable solutions

If the quantifier admits ordinary nonzero suitable solutions, then for any solution having positive `L^3` norm at some time, the predicate

\[
\sup_{t<T(u)}\|u(t)\|_3>M
\]

holds for every sufficiently small positive `M`. Hence

\[
M_*=0.
\]

The definition therefore does not isolate a positive blow-up threshold.

### Reading B — only finite-time singular solutions

Suppose `T(u)` is intended to mean a first singular time. A hypothetical finite-time singularity at the scale-critical `L^3` endpoint cannot have a finite uniform `L_t^∞L_x^3` bound; the endpoint regularity theorem would continue it. Thus its supremum over `t<T(u)` must be unbounded. For such a solution, the predicate `sup>M` again holds for every finite `M>0`, and the displayed infimum is again 0.

Thus both natural readings fail to yield the required `0<M_*<∞`.

## 4. Circularity / inheritance audit

The later APMS propositions may prove compactness **given** a bounded near-critical sequence, but Theorem G.5 does not establish the existence of such a sequence by the displayed threshold.

The proof therefore silently consumes:

\[
0<M_*<\infty
\]

and a finite uniformly `L^3`-bounded blow-up sequence, without deriving them from the failure of global regularity.

This is a hierarchy error:

\[
\text{failure of desired a-priori bound}
\not\Rightarrow
\text{positive finite minimal blow-up element}
\]

under the stated definition.

## 5. Surviving components

This audit does **not** refute every technical appendix. In particular, the following may remain independently interesting and should be audited separately:

- pressure-aware localized energy estimates;
- A2-weighted commutators;
- frequency-envelope estimates;
- parabolic Carleman inequalities;
- conditional Type-I alternatives;
- constants and sensitivity ledgers.

Their relevance to global regularity, however, requires a legitimate ancient/critical element to which they apply.

## 6. DSD verdict

\[
\boxed{
\text{KL-1 minimal-element gate fails as written.}
}
\]

Therefore the claimed global closure is not established by the current manuscript architecture.

Required repair: define a genuinely critical quantity and prove existence of a finite positive minimal obstruction with compactness modulo symmetries without assuming the endpoint bound whose failure is being studied.

Global regularity remains unproved.
