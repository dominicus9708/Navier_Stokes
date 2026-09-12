# DSD M19-156 — Compact moderate RSS/RDSS components must contain a fixed-moduli mu=1 degeneracy unless they hit a parameter or compactness boundary

Date: 2026-09-12

Status: **ACTIVE M19 CALCULATION / NONLINEAR HARD-CORE RECOMPRESSION / USING THE ACTUAL ORBIT MODULI ONLY AS COORDINATES ON THE RELATIVE-PERIODIC BOUNDARY-VALUE PROBLEM, A COMPACT NONZERO MODERATE SOLUTION COMPONENT CANNOT LIE ENTIRELY IN THE INTERIOR OF MODULI SPACE WITH FIXED-MODULI STATE DERIVATIVE INVERTIBLE EVERYWHERE / THE IMPLICIT-FUNCTION THEOREM WOULD MAKE THE MODULI PROJECTION OPEN, WHILE COMPACTNESS MAKES ITS IMAGE COMPACT / THEREFORE A MU=1 FIXED-MODULI DEGENERACY OR A TYPED PARAMETER-COMPACTNESS-ISOTROPY BOUNDARY MUST OCCUR / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. This is not the invalid M19-151 homotopy

M19-152 showed that the artificial nonlinearity parameter in M19-151 is removable by amplitude rescaling and therefore cannot provide a global continuation obstruction.

The present argument introduces **no new equation parameter**.

Instead it considers the actual solution set of RSS/RDSS boundary-value problems, using their intrinsic orbit moduli merely as coordinates of that solution set.

This is compatible with the M19-113 firewall

\[
\text{orbit modulus}\ne\text{free external PDE parameter}.
\]

We do not infer that emptiness at one modulus implies emptiness at another.
We use only local Fredholm continuation and topology of a compact solution component.

---

## 2. Abstract fixed-moduli equation

Let `m` denote intrinsic relative-periodic moduli.

For RSS one may take

\[
m=\alpha
\]

in the fixed-axis formulation.

For bounded-period RDSS one may take a local smooth chart of

\[
m=(S,Q_*)
\]

or, in a fixed-axis principal-angle chart,

\[
m=(S,\beta).
\]

After phase and rotation gauges, write the relative-periodic problem as

\[
\boxed{
\mathcal F(U,m)=0.
}
\]

At fixed `m`, the state derivative is the gauge-fixed Fredholm operator

\[
D_U\mathcal F(U,m).
\]

For a periodic return formulation, failure of invertibility corresponds to a nonsymmetry multiplier-one mode of the twisted return map.

---

## 3. Local continuation at a nondegenerate point

Suppose

\[
D_U\mathcal F(U_0,m_0)
\]

is invertible on the symmetry-gauged state space.

Then by the implicit-function theorem there is a neighborhood `V` of `m_0` and a unique local solution graph

\[
\boxed{U=U(m)}
\]

through `(U_0,m_0)`.

Therefore the projection

\[
\pi:(U,m)\mapsto m
\]

restricted to the regular solution set is a local homeomorphism/diffeomorphism onto an open subset of moduli space.

In particular, if an entire connected solution component contains no fixed-moduli degeneracy, its moduli image is open.

---

## 4. Compactness forces a contradiction for an interior regular component

Let `C` be a connected component of nonzero controlled solutions satisfying:

1. `C` is compact in the retained hard topology;
2. its moduli stay inside one smooth interior moduli chart/stratum;
3. `D_U F` is invertible at every point of `C`.

Then

\[
\pi(C)
\]

is open by local continuation.

Since `C` is compact and `pi` is continuous,

\[
\pi(C)
\]

is compact, hence closed in the local moduli chart.

But a nonempty compact subset of an open Euclidean interval/domain (or the interior cylinder used for `(S,beta)`) cannot at the same time be open and remain strictly away from the parameter boundary, unless it is an entire compact connected component of moduli space.

The moderate RSS interval and bounded-period RDSS cylinder are not compact components without boundary in the period/rate direction.

Therefore the three assumptions above cannot all hold.

Hence

\[
\boxed{
\text{compact interior nonzero component}
\Longrightarrow
\text{fixed-moduli degeneracy somewhere on the component}.
}
\]

---

## 5. RSS consequence

M19-153 puts every unresolved moderate RSS survivor into

\[
\alpha_-\le|\alpha|\le\alpha_+
\]

with compact state/tail control, separated from

- `alpha=0`/small-rate exclusion;
- the large-rate exclusion;
- zero amplitude;
- axisymmetry;
- high-mode escape.

Consider a connected component `C_RSS` of such solutions.

If it stays strictly inside the moderate interval and remains compact, then

\[
\boxed{
\exists (U_*,\alpha_*)\in C_{RSS}
:\quad
\ker D_U\mathcal F_{RSS}(U_*,\alpha_*)\ne0
}
\]

after symmetry gauges.

Thus a nonempty compact moderate RSS family forces a nonsymmetry zero mode somewhere.

---

## 6. Bounded-period RDSS consequence

M19-154 puts bounded-period RDSS into the compact intrinsic moduli sector

\[
S_-\le S\le S_+,
\qquad
Q_*\in SO(3)
\]

or its fixed-axis principal-angle version.

After excluding the small-step boundary and restricting to one smooth holonomy/isotropy chart, a compact connected nonzero RDSS component that does not reach

- `S=S_-` excluded boundary;
- `S=S_+` chosen continuation boundary;
- an isotropy/chart degeneration;
- state compactness loss;

must contain

\[
\boxed{
\mu=1
}

in the nonsymmetry twisted Floquet spectrum at some point.

Thus the bounded-period nonlinear RDSS problem also feeds the kernel problem unless it exits through a typed boundary.

---

## 7. Why elliptic multipliers do not satisfy this turning condition

If

\[
|\mu|=1,
\qquad
\mu\ne1,
\]

then

\[
I-\mathcal M_S^{tw}
\]

remains invertible on that eigendirection.

Therefore a purely elliptic crossing does not obstruct the fixed-moduli implicit-function theorem.

The component-turning/termination mechanism detected here is specifically the nonsymmetry `mu=1` kernel of M19-148.

Elliptic modes remain relevant to recurrent center dynamics but are not needed to explain existence of a compact moderate relative-periodic solution component.

---

## 8. Correct global alternative

The moderate relative-periodic branch now satisfies

\[
\boxed{
\mathcal R_{rel-per}^{moderate}
\Longrightarrow
\mathcal T_{kernel}^{nsym}
\lor
\mathcal G_{moduli\ boundary}
\lor
\mathcal G_{isotropy/chart}
\lor
\mathcal G_{state\ compactness}.
}
\]

On the certified compact hard lane, most of the latter exits are already typed:

- small/large RSS rate boundaries are externally excluded;
- bounded-period RDSS has small-step exclusion;
- high-mode/zero-amplitude escapes are removed by M19-153/154;
- long-period escape is the separate `S->infinity` invariant-measure branch.

This substantially merges the moderate nonlinear RSS/RDSS hard core with the fixed-moduli kernel theorem.

---

## 9. Important topology firewall

The argument is component-wise.

It does **not** say that one empty modulus implies all moduli are empty.
It also does not exclude an isolated degenerate solution; such a solution is precisely placed into the kernel branch.

Changes of isotropy may invalidate a single smooth quotient chart and must be treated as a typed symmetry-stratum transition rather than silently crossed.

---

## 10. Revised high-value theorem

The fixed-moduli kernel theorem becomes more valuable:

\[
\boxed{
\mathcal T_{kernel}^{uniform}:
\ker D_U\mathcal F(U,m)
=E_{sym}^{\mu=1}
}

for every controlled moderate relative-periodic state in the compact corridor.

If this theorem holds uniformly and all typed boundary exits are closed, then no compact moderate RSS/RDSS solution component can exist.

---

## 11. Audit verdict

### Certified

- regular fixed-moduli solutions continue locally as graphs over moduli;
- a compact interior component cannot remain fixed-moduli nondegenerate everywhere;
- moderate compact RSS/RDSS existence therefore forces a nonsymmetry `mu=1` point or a typed boundary/compactness/isotropy exit.

### Not certified

- uniform kernel rigidity on the compact corridor;
- closure of every moduli/isotropy boundary;
- long-period RDSS rigidity;
- global regularity.

---

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
