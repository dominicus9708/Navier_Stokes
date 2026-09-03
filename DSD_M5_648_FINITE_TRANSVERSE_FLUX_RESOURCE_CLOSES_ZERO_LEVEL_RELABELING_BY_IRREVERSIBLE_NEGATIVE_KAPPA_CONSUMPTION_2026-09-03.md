# DSD M5-648 — Finite transverse-flux resource closes the zero-level relabeling branch by irreversible negative-kappa consumption

Date: 2026-09-03

Status: **INTERNAL FINITE-RESOURCE CONTRADICTION, DEPENDENT ON M5-647 ANALYTIC-TRANSVERSAL LEMMA / ON THE `c_*(theta) identically 0` RELABELING BRANCH, EVERY MATERIAL VORTEX LEAF WITH `kappa<0` REMAINS NEGATIVE AND ITS SCALE-CRITICAL MATERIAL VORTICITY FLUX IS FORWARD-MONOTONE DECREASING / M5-640--641 FORCE A FIXED-STRENGTH STRONGLY-NEGATIVE COHERENT PACKET AT EVERY RECURRENT STATE; SMOOTH COMPACTNESS THICKENS EACH SUCH EVENT TO A FIXED SIMILARITY-TIME INTERVAL AND THEREFORE A FIXED IRREVERSIBLE FLUX LOSS / DISJOINT TIME EVENTS CAN BE CHARGED AGAINST THE SINGLE FINITE BASE-SLICE TRANSVERSE-FLUX RESOURCE FROM M5-647, GIVING A FINITE UPPER BOUND ON THE NUMBER OF EVENTS / RECURRENCE REQUIRES INFINITELY MANY, SO THE ZERO-LEVEL RELABELING BRANCH IS CONTRADICTED / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Inputs

Work on the CE-H relabeling branch with synchronized persistent level

\[
\boxed{c_*(\theta)\equiv0.}
\]

The relabeling law is

\[
D_B\kappa=f(\kappa,\theta),
\]

and because the zero level itself is the persistent solution,

\[
\boxed{f(0,\theta)=0.}
\]

Scalar ODE uniqueness therefore preserves the sign of every material `kappa` label:

\[
\kappa(\theta_0)<0
\Longrightarrow
\kappa(\theta)<0
\quad\forall\theta>\theta_0.
\]

M5-640 gives a uniform strongly-negative enstrophy mass floor.

M5-641 upgrades it to a coherent packet with fixed constants

\[
|W|\ge w_*>0,
\qquad
\kappa\le-\kappa_-<0,
\]

on a fixed-size carrier, with a transverse material vorticity flux

\[
\boxed{|\Phi|\ge\phi_*>0.}
\]

M5-642 puts all future retained-core material labels inside one fixed finite base reservoir at a chosen time `theta_0`.

M5-647 constructs on that base slice a complete vortex-flow transverse atlas `T` with finite total absolute flux mass

\[
\boxed{
\|\mu_{flux}\|(\mathcal T)<\infty.
}
\]

---

## 2. Pointwise leaf-flux evolution

On CE-H,

\[
\Delta W=\kappa W.
\]

For an infinitesimal material vortex-tube cross-section with oriented flux element `dPhi`, the exact material-surface flux law gives

\[
\boxed{
D_B(d\Phi)=\kappa\,d\Phi.
}
\]

After choosing the orientation so `dPhi>0`,

\[
\boxed{
D_B\log d\Phi=\kappa.
}
\]

Hence every negative relabeling leaf has forward-monotone nonincreasing flux.

There is no possible future recharge on that same leaf while the sign-preserving relabeling law remains valid.

---

## 3. Uniform time thickening of a strongly-negative packet

The packet extracted in M5-641 lies in a region where `|W|>=w_*>0`, so

\[
\kappa=\frac{W\cdot\Delta W}{|W|^2}
\]

is a smooth bounded state observable there.

All fixed-order spatial/time derivatives are uniformly controlled on the compact hard hull.

Therefore there is a uniform `delta_*>0` such that a transported subpacket of every M5-641 event satisfies throughout

\[
I_j=[\theta_j,\theta_j+\delta_*]
\]

the bounds

\[
\boxed{
\kappa\le-\frac12\kappa_-,
\qquad
\Phi(\theta_j)\ge\phi_*.
}
\]

Shrinking the original carrier constants once is harmless.

---

## 4. Fixed irreversible loss per event

On one such interval,

\[
\frac d{d\theta}\log\Phi
\le-\frac12\kappa_-.
\]

Hence

\[
\Phi(\theta_j+\delta_*)
\le
\exp\left(-\frac12\kappa_-\delta_*\right)
\Phi(\theta_j).
\]

Therefore the flux decrease satisfies

\[
\boxed{
L_j
:=
\Phi(\theta_j)-\Phi(\theta_j+\delta_*)
\ge
\ell_*>0,
}
\]

where

\[
\boxed{
\ell_*
:=
\left(
1-e^{-\kappa_-\delta_*/2}
\right)\phi_*.
}
\]

This loss is scale critical and generation independent.

---

## 5. Select disjoint time intervals

Strongly-negative packets exist at every recurrent state; in particular there are infinitely many future event times.

Select greedily a subsequence

\[
\theta_1<\theta_2<\cdots
\]

such that

\[
\theta_{j+1}\ge\theta_j+\delta_*.
\]

Then the loss intervals `I_j` are pairwise disjoint.

No positive-density estimate is needed for the contradiction; infinitude plus a fixed interval length is enough.

---

## 6. Pull every event back to the one base leaf resource

By the M5-642 outer material barrier, the material labels of every future retained-core packet already lie at `theta_0` inside the fixed reservoir `K`.

Because CE-H vortex lines are material lines (`D_B xi=0` and the full velocity gradient preserves the vorticity eigenline), each transported packet defines the same set of vortex-leaf labels at all times.

Partition the base preimage of each packet through the M5-647 flow-box atlas.

Sliding a piece along the base-time vortex flow to the associated local transversal preserves its signed vorticity flux because

\[
\nabla\cdot W_0=0
\]

and the lateral tube boundary is tangent to `W_0`.

Thus every event loss can be represented as loss of weight on subsets of the fixed base transverse resource `mu_flux`.

Chart overlap is handled by a fixed measurable first-chart assignment; alternatively, finite overcounting is harmless because M5-647 already provides a finite total atlas mass.

---

## 7. Telescoping loss on each leaf

Let `lambda` denote a base vortex-leaf label and let

\[
a_\lambda(\theta)
=
\exp\left(
\int_{\theta_0}^{\theta}\kappa_\lambda(s)\,ds
\right).
\]

For negative relabeling leaves,

\[
0<a_\lambda(\theta)\le1
\]

and `a_lambda` is nonincreasing.

For disjoint time intervals `I_j`, even if the same leaf participates in many packet events,

\[
\sum_j
\mathbf 1_{\lambda\in A_j}
\left[
 a_\lambda(\theta_j)
-a_\lambda(\theta_j+\delta_*)
\right]
\le1.
\]

This is simply telescoping monotone loss; no disjointness of leaf bundles across different events is required.

Integrating against the finite base absolute-flux measure gives

\[
\boxed{
\sum_j L_j
\le
\|\mu_{flux}\|(\mathcal T)
<\infty.
}
\]

---

## 8. Contradiction

But every selected event satisfies

\[
L_j\ge\ell_*>0.
\]

Therefore for the first `N` disjoint events,

\[
N\ell_*
\le
\sum_{j=1}^N L_j
\le
\|\mu_{flux}\|(\mathcal T).
\]

Hence

\[
\boxed{
N
\le
\frac{\|\mu_{flux}\|(\mathcal T)}{\ell_*}
<\infty.
}
\]

This contradicts the existence of infinitely many recurrent strongly-negative packet events.

Thus

\[
\boxed{
R_{relabel}^{c_*=0}
\Longrightarrow\bot.
}
\]

---

## 9. Why this is stronger than a fresh-label counting argument

M5-397/488 count newly formed distinguishable material flux populations when replacements are uncompensated.

The present argument does not need to prove that every strongly-negative event uses a completely new label bundle.

A previously used bundle may return, overlap another event bundle, or be repartitioned.

As long as its `kappa` sign remains negative, every strong event irreversibly consumes part of its remaining material flux.

The total cumulative loss on that same leaf cannot exceed its finite initial flux.

Thus bundle reuse is automatically priced rather than treated as an escape.

---

## 10. Audit firewalls

1. The argument applies to the zero-level relabeling branch because `f(0,theta)=0` makes negative sign preservation exact.
2. It does not yet apply unchanged to a sign-changing synchronized level `c_*(theta)`, where absolute `kappa` need not keep one sign.
3. The finite base transverse resource depends on M5-647 and therefore on fixed-slice real-analytic/subanalytic geometry.
4. The fixed loss requires uniform time thickening inside a region with `|W|` bounded away from zero.
5. No material-volume counting is used.

---

## 11. Updated relabeling frontier

The `c_*=0` no-turnover survivor is eliminated:

\[
\boxed{
R_{relabel}
\Longrightarrow
R_{relabel}^{c_*\not\equiv0}
\lor
\bot.
}
\]

M5-635--636 already show that `c_* not identically 0` produces positive-density high-amplitude detachment onto lower ordered `kappa` levels.

The next step is to normalize flux by the bounded persistent reference level `c_*(theta)` and repeat the finite-resource consumption argument for the **relative multiplier** `kappa-c_*`.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]