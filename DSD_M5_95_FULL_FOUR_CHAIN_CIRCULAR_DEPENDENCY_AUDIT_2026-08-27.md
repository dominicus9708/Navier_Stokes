# DSD M5-95 — Full Four-Chain Circular-Dependency Audit and Acyclic Namespace Freeze

Date: 2026-08-27

Status: **FULL LOGIC-DEPENDENCY RE-AUDIT / DSD AUDIT IS KEPT DISTINCT FROM MATHEMATICAL-NUMERICAL VALIDATION / GLOBAL AND W1-CONDITIONAL NAMESPACES ARE SEPARATED / THREE MAJOR FEEDBACK LOOPS ARE CUT / TWO TECHNICAL W1 INTERFACES ARE LEFT FOR IMMEDIATE REPAIR / GLOBAL REGULARITY UNPROVED.**

---

## 0. Purpose

This memo responds to the newly identified failure mode: a candidate statement can return to its own premise through a long chain of renamed intermediate objects, creating an apparent progress loop even when no single algebraic step is obviously circular.

The DSD audit therefore treats circularity as an **algorithmic graph property**, not as a numerical error.

For every node `N`, run the four independent chains

\[
\mathfrak F(N),\qquad
\mathfrak X(N),\qquad
\mathfrak S(N),\qquad
\mathfrak D(N),
\]

and only then allow the directed edge `N -> N_next`.

The cross-audits are

\[
F\leftrightarrow X,\qquad
X\leftrightarrow S,\qquad
S\leftrightarrow D,\qquad
D\leftrightarrow F.
\]

A later node is forbidden from being used to justify formation of an earlier node.

---

# 1. Two namespaces must never be merged

## 1.1 Global namespace

`GLOBAL` begins from the standard contradiction hypothesis:

\[
\text{smooth finite-energy solution has a first finite singular time }T_*.
\]

Its target is an exhaustive branch routing for **every** possible finite-time singularity.

## 1.2 W1-conditional namespace

`W1-COND` begins only after a trajectory is known to satisfy the retained W1 assumptions: bounded weak-critical tail, bounded shell-frequency/Campanato corridor, local smooth compactness, and the nontrivial normalized core assumptions used in the W1 route.

The current pressure-pump calculations M5-37--94 live in this namespace.

Therefore

\[
\boxed{
W1\text{ closure}\not\Rightarrow GLOBAL\text{ closure}
}
\]

until a separate upstream branch-completeness theorem establishes

\[
\boxed{
GLOBAL\text{ singularity}\Rightarrow W1\text{ or another already excluded branch}.
}
\]

The repository's 2026-08-26 Final Closure Audit already warned that this final upstream re-audit is required. The warning is now promoted to a hard namespace rule.

---

# 2. Acyclic master DAG

The only admissible direction for the present route is

\[
\boxed{
\begin{array}{c}
G0:\ \text{finite-time singularity assumption}\\
\downarrow\\
G1:\ \text{first-hitting / branch router}\\
\downarrow\\
G2:\ \text{W1 admissibility edge (GLOBAL YELLOW until branch-complete)}\\
\downarrow\\
W0:\ \text{pre-recurrence W1 bounded-frequency/tail corridor}\\
\downarrow\\
W1:\ \text{local first-hit/ancient smooth compactness + global }L^p\text{ tightness}\\
\downarrow\\
W2:\ \text{precompact Leray orbit}\\
\downarrow\\
W3:\ \text{omega-limit compact invariant set}\\
\downarrow\\
W4:\ \text{minimal recurrent Leray set}\\
\downarrow\\
W5:\ \text{fixed-band first-hit pump / mollified transverse upstroke}\\
\downarrow\\
W6:\ \text{syndetic returned pump class}\\
\downarrow\\
W7:\ \text{componentwise pressure payer and exact ledger}\\
\downarrow\\
W8:\ \text{exact payer-surplus square }\mathcal E_w\ge0\\
\downarrow\\
W9:\ \text{saturating sequence OR uniform surplus dichotomy}\\
\downarrow\\
W10:\ \text{exact smooth endpoint in the saturating branch}\\
\downarrow\\
W11:\ \text{zero-flux / angular / topology rigidity}\\
\downarrow\\
W12:\ \text{R1/R2 reconnection analysis}. 
\end{array}
}
\]

No arrow may point upward in this diagram.

---

# 3. Circularity audit A — precompactness versus recurrence

## Previous ambiguity

The W1 precompactness memo used phrases such as `recurrent core` while proving the compactness later used to construct the minimal recurrent set.

Read literally, this can form

\[
\text{recurrence}\to\text{precompactness}\to\text{minimal recurrence}.
\]

## Formation audit

The actual analytic inputs to global `L^p` precompactness are:

1. bounded shell Campanato / derivative-frequency data;
2. dyadic `L^p`, `p>3`, tail tightness;
3. local first-hitting/ancient smooth bounds on fixed cylinders.

Minimal recurrence is not mathematically needed for these three inputs.

## Axial audit

`local smoothness` is a regularity axis; `recurrence` is a dynamical/topological axis. They are not the same channel and may not be substituted for one another.

## Static audit

Precompactness is a property of the closure of a forward orbit; it can be checked before selecting a minimal invariant subset.

## Dynamic audit

Only after precompactness is available may the omega-limit and a minimal invariant subset be constructed.

## Verdict

Rename the logical input conceptually as

\[
\boxed{W1_{pre}:=\text{W1 corridor before minimal recurrence is selected}.}
\]

Then

\[
W1_{pre}\to\text{precompactness}\to\text{minimal recurrence}
\]

is acyclic.

**STATUS: GREEN after dependency renaming.**

---

# 4. Circularity audit B — pressure endpoint versus strict gap

## Candidate loop

A dangerous loop would be

\[
\text{assume strict gap}\to\text{endpoint impossible}\to\text{strict gap}.
\]

## Exact input

M5-83 gives the identity

\[
\boxed{
\mathcal E_w
=S_{comp,w}-4\nu^2(A_w+G_w)-4\nu X_w
=\int a w(a)|P-m_k(a)-2\nu b|^2dY.
}
\]

Thus `mathcal E_w >= 0` and the endpoint `mathcal E_w=0` are defined before any endpoint nonexistence statement.

The valid compactness logic is

\[
\boxed{
\inf\mathcal E_w=0
\Rightarrow
\text{saturating sequence}
\Rightarrow
\text{exact endpoint limit}
\Rightarrow
\text{test endpoint}.
}
\]

Only **after** endpoint exclusion and continuity/compactness may one infer

\[
\inf\mathcal E_w>0.
\]

## Verdict

The current M5-83 direction is noncircular.

Any future memo that invokes a positive `epsilon_*` before excluding the exact endpoint is automatically RED.

**STATUS: GREEN.**

---

# 5. Circularity audit C — exact G=0 rejection versus uniform G gap

The legal direction is

\[
\boxed{
\text{statewise exact }G_w=0\text{ obstruction (M5-92)}
\to
\text{compactness contradiction sequence}
\to
G_w\ge G_*>0\text{ (M5-93)}.
}
\]

M5-92 does not use `G_*` and does not use syndetic recurrence. It uses only a frozen smooth bounded positive-amplitude state, incompressibility, exact normality, static boundary aggregation, and the mean-curvature lemma.

M5-93 then adds the dynamic compact returned class.

This direction is acyclic.

A remaining interface is explicit: from the positive crossing integral in the limit one must select a bounded regular amplitude component to which M5-92 applies. This is a coarea/Sard formation lemma, not a recurrence assumption.

**STATUS: GREEN direction / YELLOW interface to be repaired separately.**

---

# 6. Circularity audit D — physical time versus Leray time

M5-79 fixed this interface.

W1 recurrence is recurrence under Leray-time translation of the normalized profile, not recurrence of the unscaled physical state.

The physical energy identity may not be imported as a strict Lyapunov function on the W1 minimal set.

Even formally,

\[
\frac12\frac d{ds}\|U\|_2^2
+\nu\|\nabla U\|_2^2
-\frac14\|U\|_2^2=0,
\]

so `||U||_2^2` is not decreasing in Leray time, and W1 need not possess finite global `L^2_Y` anyway.

**STATUS: GREEN; old physical-energy recurrence contradiction is RED permanently.**

---

# 7. Circularity audit E — first-hit pump versus syndetic recurrence

The valid order is:

1. W1 compact minimal recurrence is already formed;
2. a genuine fixed-band first-hit event gives a nonconstant mollified observable;
3. a transverse positive upstroke interval is selected;
4. recurrence transports that already formed interval;
5. minimality makes the returns syndetic.

Thus recurrence does not create the anchor first-hit property ex nihilo; it reproduces a formed local pattern.

The exact derivative

\[
X_w=\partial_s\bar E_w
\]

is allowed to telescope. M5-58 correctly prevents the returned positive upstrokes from being counted as an accumulating signed budget.

**STATUS: GREEN.**

---

# 8. Circularity audit F — repeated critical costs versus finite budgets

M5-49 and M5-58--64 already remove the false route

\[
\text{infinitely many returns}\Rightarrow\text{infinite ordinary energy/dissipation cost}.
\]

Nested physical scales are not independent packets, and critical order-one actions have no independently proved finite total budget.

The frozen rule is:

- subcritical cost may have a finite physical budget but per-return cost is summable;
- critical cost is order one per normalized return but currently has no finite global budget;
- exact derivatives telescope.

Therefore R1/R2 must seek a **statewise incompatibility or a genuinely new independent budget**, not recount previous critical events.

**STATUS: GREEN pruning / old accumulation routes RED.**

---

# 9. Circularity audit G — componentwise pressure means and topology

M5-83 is exact on regular component branches.

M5-82 replaces differentiated component means by the branch-free condition

\[
\nabla a\times\nabla(P-2\nu b)=0.
\]

M5-84 uses tangent vector fields `L_ij` to interpolate from the scalar residual to this branch-free differential defect.

However, the global weighted integration by parts across topology-changing critical sets was explicitly left YELLOW in M5-84 and must not be silently promoted to GREEN merely because M5-85 localizes the support.

Localization solves migration to infinity and controls the higher derivative factor; it does not by itself prove the foliation/branch-mean weak-derivative statement.

**STATUS: YELLOW. Immediate technical repair required.**

---

# 10. Upstream GLOBAL branch-completeness audit

The current W1 route is not allowed to prove its own global admissibility.

The 2026-08-20 Type-I compactness bridge was explicitly conditional on:

- natural-scale center nesting;
- uniform local scale-invariant `A/C/D/E` bounds;
- coherent pressure/drift gauge;
- strong enough compactness to preserve nontriviality.

Later W1 memos provide a strong internal description once W1 is assumed/obtained, but they do not retroactively turn this old conditional bridge into an unconditional theorem for every finite-time singularity.

The 2026-08-26 proof map likewise states

\[
\boxed{
W1\text{ closure}\ne\text{global regularity until upstream branch completeness is re-audited}.}
\]

Therefore the global edge

\[
G1\to G2\to W1_{pre}
\]

remains an explicit open branch-completeness obligation.

This is **not** a circular proof after the namespace freeze; it is an open directed edge.

**STATUS: YELLOW / GLOBAL BLOCKER, not RED.**

---

# 11. Permanent RED list — routes forbidden from re-entering

The following arrows are deleted from the dependency graph:

1. Leray recurrence `->` physical-energy contradiction.
2. Nested scale returns `->` independent summation of ordinary energy/enstrophy costs.
3. Positive critical return cost `->` contradiction without an independent finite critical budget.
4. `X_w=dE/ds` positive intervals `->` monotone accumulated defect.
5. weak-`L3` boundedness `->` strong `L3` endpoint regularity.
6. Abel/Mellin critical residue `->` pointwise `lambda^3N(lambda)` limit without a Tauberian hypothesis.
7. gauge-dependent pressure sign `->` physical payer sign.
8. fixed single-amplitude first-hit gap `->` a finite amplitude band without mollification or transversality.
9. shrinking mollifier width `->` vanishing crossing cost.
10. remote cell infinity `->` equal-strength pressure reservoir at the core.
11. exact `G=0` impossibility `->` assumed uniform `G_*` without compactness.
12. W1 internal closure `->` global regularity without upstream branch completeness.

Any future calculation that needs one of these arrows must open a new proof obligation rather than reuse the deleted edge.

---

# 12. Four-chain status table

| Node/interface | Formation | Axis | Static aggregation | Dynamics | Overall |
|---|---|---|---|---|---|
| first-hit normalization | GREEN | GREEN | GREEN | GREEN | GREEN |
| pre-recurrence W1 local smoothness | GREEN | GREEN | GREEN | GREEN | GREEN inside W1 assumptions |
| global `Lp`, p>3, precompactness | GREEN | GREEN | GREEN | GREEN | GREEN inside W1 |
| precompactness `->` minimal recurrence | GREEN | GREEN | GREEN | GREEN | GREEN |
| mollified pump anchor | GREEN | GREEN | GREEN | GREEN | GREEN |
| syndetic transfer | GREEN | GREEN | GREEN | GREEN | GREEN |
| pressure payer / centered variance | GREEN | GREEN | GREEN | GREEN | GREEN a.e. regular levels |
| exact surplus square | GREEN | GREEN | GREEN | GREEN | GREEN |
| tangential branch-free interpolation | GREEN locally | GREEN | YELLOW critical-set interface | GREEN | YELLOW |
| exact `G=0` obstruction | GREEN | GREEN | GREEN | statewise | GREEN subject to regular-component selection |
| uniform `G_*` promotion | GREEN | GREEN | GREEN | GREEN | YELLOW until regular-level selection is explicit |
| R1/R2 split | GREEN | GREEN | GREEN | not yet calculated | READY AFTER REPAIRS |
| GLOBAL singularity `->` exhaustive W1/closed branches | YELLOW | YELLOW | YELLOW | YELLOW | GLOBAL BLOCKER |

---

# 13. Stable directed research frontier

After deleting circular arrows, the W1 internal route has two technical repairs before the next structural calculation:

1. prove that the piecewise component pressure mean is annihilated by the tangent flows `L_ij` in the weak/distributional sense across critical topology changes;
2. prove that `T_*>0` plus fixed positive-band localization selects at least one bounded regular level component with positive crossing, so M5-92 applies without assuming topology persistence from approximating states.

Once these two interfaces are closed, the W1 internal DAG can be frozen before R1/R2.

The GLOBAL DAG will still retain the separate upstream branch-completeness YELLOW edge.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
