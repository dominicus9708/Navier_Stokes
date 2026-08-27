# DSD M5-98 — Stability Freeze and Conditional R1/R2 Readiness

Date: 2026-08-27

Status: **POST-AUDIT STABILITY FREEZE / W1-INTERNAL DEPENDENCY GRAPH IS ACYCLIC AFTER M5-95--97 REPAIRS / OLD FEEDBACK ROUTES ARE PERMANENTLY RETIRED / R1-R2 RECONNECTION ANALYSIS IS PREPARED BUT NOT YET STARTED / GLOBAL UPSTREAM BRANCH-COMPLETENESS AND THE FINAL CRITICAL-TAIL/PUMP-ABSORPTION BRIDGE REMAIN OPEN / GLOBAL REGULARITY UNPROVED.**

---

## 0. Meaning of `stable`

In this project, `stable` does **not** mean that all Navier--Stokes proof obligations are solved.

It means the current research graph has passed the DSD algorithmic audit:

1. every object is formed before it is used;
2. every axial/channel decomposition is typed before aggregation;
3. static aggregation does not double count or convert signed cancellation into positive cost;
4. dynamic recurrence does not retroactively justify its own compactness or formation;
5. every unresolved implication is represented as a forward open edge rather than a hidden feedback loop;
6. all known invalid reverse arrows are frozen RED and cannot silently re-enter later arguments.

Thus stability means

\[
\boxed{
\text{acyclic logical state with explicit open edges}
}
\]

rather than `proof completed`.

---

# 1. Results of the full DSD dependency audit

M5-95 separated two namespaces:

\[
GLOBAL
\qquad\text{and}\qquad
W1\text{-COND}.
\]

The hard rule is

\[
\boxed{
W1\text{ closure}\not\Rightarrow GLOBAL\text{ closure}
}
\]

until the upstream finite-time-singularity branch router is independently complete.

Inside W1, the admissible order is frozen as

\[
\boxed{
W1_{pre}
\to
\text{local smooth/tail compactness}
\to
\text{precompact orbit}
\to
\text{omega-limit}
\to
\text{minimal recurrence}
\to
\text{formed pump}
\to
\text{syndetic return}
\to
\text{pressure payer}
\to
\mathcal E_w
\to
\text{endpoint/strict-surplus dichotomy}
\to
\text{reconnection rigidity}.
}
\]

No later node is permitted to justify an earlier one.

---

# 2. Technical repairs completed before the freeze

## 2.1 Branch-mean / critical-topology repair — M5-96

For

\[
L_{ij}
=(\partial_i a)\partial_j-(\partial_j a)\partial_i,
\]

the tangent flow preserves both amplitude and the connected superlevel-component label almost everywhere.

At critical points `grad a=0`, the generator itself vanishes.

Therefore the piecewise component pressure mean field `M(y)` satisfies

\[
\boxed{L_{ij}M=0\quad\text{in distributions}.}
\]

Hence the M5-84 weighted integration by parts has no hidden branch-jump term.

The M5-83 scalar residual may safely be converted to the component-free tangential differential defect on the fixed positive-amplitude cell.

**Status: GREEN.**

## 2.2 Positive-crossing regular-component repair — M5-97

The exact coarea identity is

\[
T_w
=
\int w(\lambda)
\sum_k
\int_{\Gamma_{\lambda,k}}
\frac{|\nabla a|}{\lambda}
|U\cdot n|^2dS\,d\lambda.
\]

Since critical values have measure zero and `U dot grad a=0` at critical points,

\[
T_w>0
\]

forces a regular positive amplitude `lambda` and a connected bounded superlevel component with positive crossing.

The component is selected from the **limit state itself**. No topology persistence from the approximating returned sequence is assumed.

Therefore M5-92 legitimately applies to the M5-93 zero-`G` limit.

**Status: GREEN.**

---

# 3. W1-internal frozen GREEN chain

The following direction is now frozen as the accepted W1-conditional logical spine:

\[
\boxed{
\begin{array}{c}
\text{fixed positive-band first-hit pump}\\
\downarrow\\
\text{mollified transverse upstroke }X_w\ge c_1>0\\
\downarrow\\
\text{syndetic returned pump class}\\
\downarrow\\
J_w=\nu D_w+X_w\\
\downarrow\\
J_w^2\le S_{comp,w}T_w\\
\downarrow\\
T_w\ge T_*>0\quad(\text{on compact returned class})\\
\downarrow\\
\mathcal E_w
=S_{comp,w}-4\nu^2(A_w+G_w)-4\nu X_w\\
\phantom{\downarrow}\quad
=\int aw(a)|P-m_k(a)-2\nu b|^2dY\\
\downarrow\\
\inf\mathcal E_w=0
\Rightarrow
\text{exact smooth endpoint limit}\\
\downarrow\\
G_w=0\text{ subcorridor excluded statewise}\\
\downarrow\\
G_w\ge G_*>0\text{ on the compact returned upstroke class}. 
\end{array}
}
\]

Every arrow above has an explicit forward dependency and no return arrow.

---

# 4. What is NOT frozen as solved

Three conceptually distinct open obligations remain and must not be conflated.

## 4.1 Exact positive-G endpoint rigidity

The exact minimal-payer endpoint may still satisfy

\[
G_w\ge G_*>0,
\qquad
T_w>A_w+G_w,
\qquad
X_w=\nu(T_w-A_w-G_w)>0.
\]

R1/R2 is the prepared attack on this exact endpoint geometry.

## 4.2 Strict-surplus branch after endpoint exclusion

Even if R1/R2 excludes every exact endpoint, compactness would only yield a statewise strict surplus

\[
\mathcal E_w\ge\varepsilon_*>0.
\]

M5-58--64 already show that a repeated positive critical cost is not automatically a contradiction.

Therefore a later step must still connect that strict surplus to either

- a direct statewise impossibility;
- the critical `K`-tail absorption route in Issue #2;
- or an independently finite monotone/critical budget.

R1/R2 must not be advertised as automatically solving this second branch.

## 4.3 GLOBAL upstream branch completeness

The current repository still needs an independent proof-tree audit showing that every finite-time singularity is routed either into W1 or into a genuinely already-excluded alternative.

The old Type-I bridge was explicitly conditional on center nesting, uniform local scale-invariant bounds, pressure gauge control, and preservation of nontriviality.

Later W1 results do not retroactively prove this global edge.

Thus

\[
\boxed{
GLOBAL\text{ branch completeness = explicit YELLOW blocker}.
}
\]

It is an open forward edge, not a circularity.

---

# 5. Permanent RED firewall

The following reasoning patterns are forbidden in all subsequent stages unless independently reproved by a new lemma:

1. physical energy monotonicity applied as a Leray-recurrence Lyapunov contradiction;
2. nested scale copies counted as independent ordinary-energy or enstrophy expenses;
3. repeated critical order-one cost counted against an unproved finite critical budget;
4. positive intervals of `X_w=dE/ds` accumulated without the compensating downstroke;
5. weak-`L3` boundedness treated as strong `L3` compactness;
6. Abel/Mellin residue replaced by a pointwise distribution coefficient without a Tauberian hypothesis;
7. pressure gauge or absolute pressure sign treated as physical work;
8. one first-hit amplitude converted to a whole amplitude band without the mollified construction;
9. mollifier narrowing treated as automatic decay of the coarea crossing density;
10. cell infinity treated as an equal-strength core pressure source;
11. statewise `G=0` rejection converted to a uniform `G_*` without compactness and positive-crossing preservation;
12. W1 conditional closure converted into global regularity without the upstream GLOBAL audit.

This list is part of the dependency graph, not commentary.

---

# 6. Prepared next-stage variables

The next calculation is intentionally **not executed in this memo**.

On a regular positive amplitude component boundary, decompose

\[
\boxed{
U=q n+v,
\qquad
q:=U\cdot n,
\qquad
v\cdot n=0.
}
\]

Since `a=|U|=lambda` on the level,

\[
\boxed{q^2+|v|^2=\lambda^2.}
\]

The normal and tangential quadratic channels are

\[
\boxed{
T_{\lambda,k}
=
\int_{\Gamma_{\lambda,k}}
\frac{|\nabla a|}{\lambda}q^2dS,
}
\]

and

\[
\boxed{
G_{\lambda,k}
=
\int_{\Gamma_{\lambda,k}}
\frac{|\nabla a|}{\lambda}|v|^2dS.
}
\]

Componentwise incompressibility gives the signed static constraint

\[
\boxed{
\int_{\Gamma_{\lambda,k}}q_{out}\,dS=0,
}
\]

with the outward-normal convention fixed when the calculation begins.

The DSD static aggregation now splits reconnection into three formed cases.

### R1 — intra-surface sign reconnection

A connected boundary surface contains both inward and outward normal crossing.

Then `q` changes sign on that surface and passes through

\[
q=0,
\]

where

\[
|v|=\lambda.
\]

Prepared target: a weighted surface coercivity/Poincare/Cheeger-type estimate converting required sign reconnection into a quantitative `G` and/or `A` cost.

### R2 — inter-surface/topological reconnection

Individual connected boundary surfaces may have sign-definite normal crossing, with cancellation occurring only between different boundary surfaces of the same superlevel volume.

Prepared target: a quantitative stability version of the M5-92 cavity/mean-curvature obstruction, measuring how far a smooth divergence-free configuration must depart from exact normality in order to support the required inner/outer flux balance.

### RM — mixed mode

Both mechanisms occur simultaneously.

It will be handled by decomposing the signed crossing into its intra-surface and inter-surface portions before aggregation; neither subcost may be counted twice.

---

# 7. Four-chain protocol for every R1/R2 lemma

Every future candidate inequality must be entered in this order:

## F — Formation

Specify the actual formed component, surface, sign region, zero set, and any cavity. Critical levels are excluded or separately exhausted; no historical label is inherited automatically.

## X — Axis

Specify `n`, outward normal, `q`, tangential `v`, streamline direction, and whether each quantity is signed or quadratic.

## S — Static aggregation

Prove exactly where flux cancels and where positive costs add. R1 and R2 contributions are separated before any sum.

## D — Dynamics

Only after the statewise estimate is established may recurrence transport it. No recurrence assumption may be inserted into the statewise coercivity proof.

Then cross-audit `F-X`, `X-S`, `S-D`, and `D-F` before accepting the lemma.

---

# 8. Readiness verdict

### W1 internal logic

\[
\boxed{\text{STABLE / ACYCLIC / READY FOR R1-R2.}}
\]

The two technical YELLOW interfaces isolated by M5-95 are repaired by M5-96 and M5-97.

### Exact endpoint problem

\[
\boxed{\text{OPEN, with R1/R2 variables and entry conditions prepared.}}
\]

### Strict-surplus / critical-tail absorption problem

\[
\boxed{\text{OPEN and logically downstream/parallel to endpoint exclusion.}}
\]

### Global proof tree

\[
\boxed{\text{ACYCLIC BUT INCOMPLETE: upstream branch-completeness remains YELLOW.}}
\]

Therefore the project is stable enough to resume calculations without returning to the previous circular logic, while still explicitly distinguishing W1-conditional progress from a global proof.

No R1/R2 calculation is started until the next explicit continuation step.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
