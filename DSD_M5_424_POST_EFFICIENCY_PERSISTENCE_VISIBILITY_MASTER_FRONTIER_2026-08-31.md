# DSD M5-424 — Post-efficiency/persistence/visibility master frontier

Date: 2026-08-31

Status: **MASTER RECONSOLIDATION AFTER M5-416--423 / FORMED AND DIFFUSE REMOTE SOURCE EFFICIENCY DECAYS QUADRATICALLY WITH NORMALIZED DISTANCE, NATURAL MISALIGNED SOURCES PERSIST FOR A FIXED NATURAL-TIME FRACTION OUTSIDE STRONG-STRAIN THROUGHPUT, ONE FIXED PARENT-NATURAL CLUSTER HAS UNIFORMLY BOUNDED CRITICAL MASS, OLD NON-CO-SHRINKING SOURCE COUPLING AGE-DILUTES LIKE `q^-k`, AND THE ENTIRE FAR FIELD OUTSIDE `L_eff ~ X^(1/4)` HAS SMALL DIRECT STRAIN COUPLING / THE LATE HARD CORE IS NOW `STRONG/DELOCALIZED CRITICAL-MASS THROUGHPUT` VERSUS A `NEAR-BALANCED NATURAL ELEMENT` THAT MUST USE EITHER CO-SHRINKING SOURCE LINEAGE OR REPEATED FRESH NATURAL SOURCE HANDOFF / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Purpose

M5-415 reduced the fully pruned proof tree to one critical-throughput class but warned that this still sat at the classical `dot H^{1/2}` barrier.

M5-416--423 then added geometry and dynamics that are not contained in the bare critical norm:

- source efficiency as a function of phase-space scale/distance;
- angular-source derivative tax;
- temporal persistence;
- exact block production/dissipation balance;
- compact-cluster critical-mass cap;
- diffuse-shell critical duality;
- strain-source age dilution;
- full far-field visibility radius.

The present note records the resulting frontier without claiming a closure that has not been proved.

---

## 2. Efficient formed sources are natural and local

M5-416 gives, for a formed source of scale `r` feeding a target of scale `s` at distance `d`,

\[
\boxed{
\eta_{formed}
\lesssim
\frac{s^2r}{(d+r)^3}.
}
\]

With `a=r/s`, `b=d/s`,

\[
\eta\lesssim\frac{a}{(a+b)^3}.
\]

At fixed remote distance `b`, the optimal scale is `a=b/2`, yet

\[
\boxed{
\eta_{max}(b)\lesssim b^{-2}.
}
\]

Subnatural and overcoarse sources are also inefficient.

Thus any near-efficient **formed** source lies in the natural phase-space window

\[
\boxed{
r\asymp s,
\qquad
d=O(s).
}

which is exactly the M5-394 main/companion geometry.

---

## 3. Diffuse remote sources obey the same quadratic law

M5-421 removes the formed-carrier hypothesis.

For one remote shell at radius `R=Ls`,

\[
\boxed{
|S_R|
\lesssim
R^{-2}
\|\omega_R\|_{\dot H^{-1/2}}.
}
\]

Hence a fixed target-strain fraction requires

\[
\boxed{
\|\omega_R\|_{\dot H^{-1/2}}
\gtrsim
\nu L^2,
}
\]

and therefore

\[
\boxed{
X=\|u\|_{\dot H^{1/2}}^2
\gtrsim
\nu^2L^4
}
\]

up to uniform localization constants.

Thus quadratic remote inefficiency is a property of the critical Biot--Savart mapping itself, not a packet model artifact.

---

## 4. The entire far field has one visibility radius

M5-423 pairs the whole exterior kernel directly with the global critical vorticity norm:

\[
\boxed{
|S_{>R}(x_*)|
\lesssim
R^{-2}
\|\omega\|_{\dot H^{-1/2}}.
}
\]

At target scale `s`, the full field outside normalized radius `L` contributes at most

\[
\boxed{
\frac{|S_{>Ls}|}{\nu/s^2}
\lesssim
L^{-2}
\frac{X^{1/2}}{\nu}.
}
\]

Therefore for every `epsilon>0`, all but an `epsilon` fraction of the target strain lies inside

\[
\boxed{
L_{eff}(t,\epsilon)
\asymp
\epsilon^{-1/2}
\left(\frac{X(t)}{\nu^2}\right)^{1/4}.
}
\]

This removes the far-shell double-counting issue for the strain source itself.

---

## 5. One compact parent cluster cannot hold divergent critical mass

M5-420 uses

\[
L^{3/2}\hookrightarrow\dot H^{-1/2}
\]

and the first-hitting cap `|omega|<=qW_j` to show for every fixed normalized radius `C`,

\[
\boxed{
\|\chi_{Cr_j}\omega\|_{\dot H^{-1/2}}
\lesssim
C(C,q)\nu.
}
\]

Thus a fixed finite collection of parent-natural clusters carries only `O(nu^2)` critical mass.

If

\[
X_j\to\infty,
\]

the growth must be delocalized through

- increasing phase-space multiplicity;
- growing normalized windows;
- relative-scale spread;
- diffuse exterior critical mass.

A single bounded main/companion cluster cannot simply become arbitrarily large in critical norm under first-hitting normalization.

---

## 6. Natural source geometry has a derivative tax but no static universal gap

M5-417 defines the transverse vorticity component relative to the main axis,

\[
F=(I-\xi_0\otimes\xi_0)\Omega,
\]

and proves

\[
\boxed{
\mathcal P_\perp
\gtrsim
\mathcal A_{nat}^2.
}
\]

Thus natural productive angular source forces a quantitative transverse-palinstrophy floor.

However the angular stretching source is first order in small angle while derivative energy is quadratic:

\[
\mathcal A_{nat}\sim\delta,
\qquad
\mathcal P_\perp\sim\delta^2.
\]

Therefore one-snapshot misalignment alone does not give a universal strict nonlinear-production versus viscosity gap.

This failed shortcut is permanently firewalled.

---

## 7. The natural dual cluster persists in time or exits through strong strain

M5-418 uses

\[
D_\tau\Omega
=
\Sigma\Omega+\Delta\Omega
\]

and M5-392's stage-wide Laplacian bound.

If local strain/full deformation stays bounded, the main and companion material vectors, amplitudes, angular separation, and geometry persist for a fixed normalized interval

\[
\boxed{
\delta\tau_*>0.
}

Consequently

\[
\boxed{
\int_{J_*}
\mathcal P_\perp(\tau)d\tau
\ge
c_*>0.
}

and each persistent natural event carries a fixed positive critical `dot H^{3/2}` time charge.

If this persistence fails through the time derivative/deformation term, the stage has already entered strong critical strain/interface throughput.

---

## 8. Critical block balance

M5-419 defines

\[
X(t)=\|u\|_{\dot H^{1/2}}^2,
\qquad
Y(t)=\|u\|_{\dot H^{3/2}}^2
\]

and stage charges

\[
D_j=\int_{I_j}Ydt,
\qquad
P_j=\int_{I_j}\mathcal Ndt.
\]

On the persistent natural-cluster corridor,

\[
\boxed{D_j\ge d_*>0.}
\]

The exact identity is

\[
\boxed{
P_j
=
\nu D_j
+
\frac12(X_{j+1}-X_j).
}
\]

Therefore an infinite tower must either accumulate critical mass at a nonnegligible generation rate or have long-block actual nonlinear production asymptotically balance critical viscous dissipation.

Symbolically,

\[
\boxed{
C_{mass\,accum}
\lor
C_{bal}.
}
\]

---

## 9. Source function has finite age even when flux identity does not

M5-396 correctly shows that natural flux

\[
\Phi\asymp\nu
\]

has no age dilution.

M5-422 shows that **source efficiency does**.

For an old source whose physical scale/distance does not co-shrink with the target,

\[
\boxed{
\eta_{source}(k)
\lesssim
q^{-k}
}
\]

up to its critical-amplification factor.

To maintain a fixed target-strain fraction for `k` generations, the source critical norm must grow like

\[
\boxed{
M_k\gtrsim q^k,
\qquad
M_k^2\gtrsim q^{2k}.
}
\]

Thus old-source functional reuse has finite generation memory unless it either:

1. co-shrinks with the target; or
2. enters explicit exponential critical-mass accumulation.

---

## 10. Near-balanced tower cannot rely on a passive old remote reservoir

The M5-419 near-balanced branch is the branch in which critical mass does not accumulate fast enough to explain the whole repeated dissipative charge.

Exponential source amplification belongs instead to the strong mass-accumulation branch.

Therefore a near-balanced late tower must supply its M5-362 stretching source by

\[
\boxed{
G_{co\text{-}shrinking\ source}
\lor
G_{fresh\ handoff}.
}

The first is a persistent material main/source lineage whose active source scale contracts with the target.

The second creates a new efficient natural source after bounded generation age.

A fixed old remote shell is not a sustainable near-balanced payer.

---

## 11. Current master hard core

After M5-416--423, the late proof frontier is best written as

\[
\boxed{
\text{hypothetical singular tower}
\Longrightarrow
C_{strong/deloc\,mass}
\lor
C_{bal}^{co\text{-}shrink}
\lor
C_{bal}^{fresh}
\lor
H_{strong\,interface}.
}
\]

Here:

### `C_strong/deloc mass`

Critical norm grows strongly through remote/growing-window/multiplicity/diffuse content. A fixed parent cluster cannot carry it.

### `C_bal^{co-shrink}`

A compact natural main/companion source lineage contracts with the first-hitting scale while nonlinear critical production remains close to viscous critical dissipation on long blocks.

### `C_bal^{fresh}`

Old source function age-dilutes, so a positive-frequency sequence of fresh efficient natural source handoffs supplies the stretching while the critical energy ledger remains near-balanced.

### `H_strong interface`

Stages that leave the bounded local-cluster persistence corridor through strong local/nonlocal strain, rapid reformation, or equivalent already-typed critical throughput.

This last label is retained as a firewall until every such rapid stage is quantitatively assigned to one of the first three long-time lanes.

---

## 12. What has now been excluded as a quiet mechanism

The following are no longer viable as independent late quiet explanations of first-hitting stretching:

- arbitrarily remote fixed-cost formed source;
- diffuse far source with bounded critical norm;
- one compact cluster accumulating infinite critical mass;
- instantaneous zero-duration natural companion;
- old non-co-shrinking source reused forever at fixed efficiency;
- arbitrarily far exterior source hidden by shell double counting.

Each either loses efficiency, pays explicit critical mass, persists as a local natural element, or requires fresh source formation.

---

## 13. Highest-value next targets

### Target A — co-shrinking lineage rigidity

Use the fact that both main and efficient source must contract at the same geometric first-hitting rate while retaining material/flux identity and fixed angular function.

The goal is to show that such a recurrent co-shrinking material source pair forces either:

- unsustainable material deformation/length growth;
- cancellation/fragmentation capacity H;
- or a compact ancient profile already in a Liouville class.

### Target B — fresh-source nonreuse

A fresh source is born at positive generation frequency and persists for positive natural time.

Prove that its critical derivative/flux action cannot be repeatedly charged to old source regions in a scale-time Bessel/Carleson ledger.

### Target C — strong mass accumulation

Use the quartic visibility law and the fixed-cluster cap to classify whether large `X` is caused by many critical atoms, diffuse growing-window mass, or relative-scale spread, then test whether that reservoir can actually couple back to the active core at the rate required by M5-419.

---

## 14. Firewall against progress overstatement

The tree is narrower, but none of the three hard long-time lanes has been excluded.

In particular,

\[
X(t)\to\infty
\]

is still compatible with a hypothetical singularity, and the quartic visibility cost is a lower bound on that allowed divergence, not a contradiction.

Likewise a co-shrinking material source pair is not known to be impossible.

The near-balance identity is an exact classification tool, not a rigidity theorem.

---

## 15. Audit verdict

### CURRENT HARD CORE

\[
\boxed{
C_{strong/deloc\,mass}
\lor
C_{bal}^{co\text{-}shrink}
\lor
C_{bal}^{fresh}
\lor
H_{strong\,interface}.
}
\]

### MAIN NEW STRUCTURE

- quadratic source efficiency loss with distance;
- quartic critical visibility cost;
- fixed critical mass cap in compact parent windows;
- fixed natural-time persistence;
- functional source age dilution;
- actual stage-averaged production/dissipation balance dichotomy.

### STILL OPEN

- co-shrinking lineage rigidity;
- fresh-source critical nonreuse;
- strong delocalized mass coupling classification;
- generic rapid-interface assignment;
- global regularity.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
