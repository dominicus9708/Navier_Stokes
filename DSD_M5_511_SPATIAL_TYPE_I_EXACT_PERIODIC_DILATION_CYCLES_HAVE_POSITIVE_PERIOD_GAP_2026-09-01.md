# DSD M5-511 — Spatial-Type-I exact periodic dilation cycles have a positive period gap

Date: 2026-09-01

Status: **EXTERNAL BREATHER AUDIT / ON THE M5-510 SPATIAL-TYPE-I SUBBRANCH, AN EXACT PERIODIC RETURN OF THE M5-483 PARABOLIC DILATION HULL PRODUCES A BACKWARD DSS SOLUTION / PINEAU--VICOL 2026 THEOREM 1.7 RULES OUT NONZERO DSS SOLUTIONS WITH TYPE-I DECAY WHEN THE SCALING FACTOR IS SUFFICIENTLY CLOSE TO `1` / THEREFORE ANY NONTRIVIAL EXACT PERIODIC DILATION CYCLE IN THE CURRENT MARKED HULL MUST HAVE A STRICTLY POSITIVE MINIMUM LOG-SCALE PERIOD / THIS REMOVES ARBITRARILY SHORT EXACT BREATHERS BUT DOES NOT REMOVE GENERAL DSS CYCLES OR APERIODIC RECURRENCE / THE `L6` VELOCITY INFORMATION FROM FINITE ENSTROPHY DOES NOT UPGRADE TO THE `L3` HYPOTHESIS OF OLDER FULL-PERIODIC NONEXISTENCE THEOREMS / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Exact periodic return in the M5-483 genealogy

The parabolic dilation genealogy satisfies

\[
\mathcal U_{n+1}
=
\mathscr D_{\lambda_n}\mathcal U_n,
\qquad
(\mathscr D_\lambda U)(y,s)
=
\lambda U(\lambda y,\lambda^2s).
\]

Suppose an exact return occurs after `N` stages:

\[
\boxed{
\mathcal U_N=\mathcal U_0.
}
\]

Let

\[
\Lambda
:=
\prod_{j=0}^{N-1}\lambda_j>1.
\]

Then

\[
\boxed{
\mathcal U_0(y,s)
=
\Lambda\mathcal U_0(\Lambda y,\Lambda^2s),
}
\]

so the corresponding physical solution is backward `Lambda`-discretely self-similar.

In similarity time the period is

\[
\boxed{
\Theta
=2\log\Lambda.
}
\]

This was already the exact periodic branch identified in M5-482--483.

---

## 2. Add the M5-510 spatial Type-I subbranch

M5-510 separated

\[
H_{decay}^{U,1}
\]

from the stronger branch

\[
\mathcal C_{spatial-Type-I}^{U},
\]

where

\[
\boxed{
|U(y,\theta)|
\le
\frac{C_I}{1+|y|}
}
\]

uniformly along the relevant compact recurrent hull.

For an exact periodic orbit, this gives exactly the global Type-I bound required for the backward DSS theorem discussed below.

---

## 3. External theorem: Pineau--Vicol 2026

Ben Pineau and Vlad Vicol, *On rotated backwards self-similar solutions of the incompressible 3D Navier--Stokes equations*, arXiv:2607.09619v2 (2026), Theorem 1.7, prove a no-short-breather result.

Specialized to the non-rotated DSS case `alpha=0`, their theorem says:

for each fixed Type-I constant `C_I`, there exists

\[
\underline\lambda(C_I)>1
\]

such that a backward `lambda`-DSS Navier--Stokes solution satisfying the Type-I upper bound is trivial whenever

\[
1<\lambda<\underline\lambda(C_I).
\]

The full theorem also treats rotated DSS under additional rotation/scaling conditions, but M5-511 uses only the `alpha=0` specialization because the M5-483 dilation return by itself does not establish a global rigid-rotation ansatz.

---

## 4. The marked carrier excludes the trivial orbit

The M5-478--485 record genealogy carries a nontrivial marked vorticity cell.

Thus an exact periodic orbit in the surviving marked hull cannot be the zero solution.

Consequently the Pineau--Vicol theorem forces

\[
\boxed{
\Lambda
\ge
\underline\lambda(C_I)>1.
}
\]

Equivalently, the similarity-time period satisfies

\[
\boxed{
\Theta
=2\log\Lambda
\ge
2\log\underline\lambda(C_I)
=:
\Theta_{gap}(C_I)>0.
}
\]

Therefore arbitrarily short exact periodic dilation cycles are impossible on the nontrivial spatial-Type-I branch.

---

## 5. Exact result

Define

\[
\mathcal C_{DSS}^{exact}
:=
\text{an exact periodic return in the parabolic dilation hull}.
\]

Then on the spatial-Type-I branch,

\[
\boxed{
\mathcal C_{DSS}^{exact}
\Longrightarrow
\Theta\ge\Theta_{gap}(C_I)>0.
}
\]

Equivalently,

\[
\boxed{
\text{nonzero exact breather}
\Longrightarrow
\text{finite nonzero minimum log-scale excursion before return}.
}
\]

This is a genuine strengthening of the M5-483 periodic/aperiodic split.

---

## 6. Why older `L3` nonexistence does not close the remaining DSS branch

Chae's asymptotically discretely self-similar nonexistence result excludes a time-periodic similarity profile under a critical spatial integrability hypothesis of the form

\[
U\in C^1(\mathbb R;L^3(\mathbb R^3)\cap C^2).
\]

The present finite-enstrophy vorticity class gives instead, in the canonical Biot--Savart gauge,

\[
U\in L^6.
\]

On the M5-510 spatial-Type-I branch one has

\[
|U(y)|\lesssim(1+|y|)^{-1},
\]

which is borderline weak-`L3` behavior and lies in every `L^p`, `p>3`, but need not lie in `L3`.

Therefore

\[
\boxed{
U\in L^6
\not\Longrightarrow
U\in L^3
}
\]

on the whole space, and the older `L3` theorem cannot be silently imported.

This is consistent with the modern literature, where nonzero backward DSS solutions remain open in the general critical setting outside additional restrictions.

---

## 7. DSD audit: recurrence is not automatically short recurrence

Compactness gives recurrent returns, but it gives no a-priori upper bound forcing the return period to tend to zero.

Likewise, the bounded scale ratios

\[
1<\lambda_-
\le
\lambda_j
\le
\lambda_+<\infty
\]

do not force the product over a periodic cycle

\[
\Lambda=\prod_{j=0}^{N-1}\lambda_j
\]

to lie near `1`.

Hence the Pineau--Vicol short-period theorem does not eliminate every periodic branch.

It only establishes the sharp separation

\[
\boxed{
\text{exact periodic return}
=
\text{short return, impossible}
\quad\lor\quad
\text{long return, still open}.
}
\]

---

## 8. Rotated-periodic firewall

The persistent dual-flux pair can rotate relative to itself and the strain field can generate directional motion.

This does **not** establish that the entire velocity field has the rigid form

\[
U(y,s)
=
R(\alpha s)\widetilde U(R(-\alpha s)y)
\]

or its RDSS analogue.

Therefore the rotation parameter `alpha` from the Pineau--Vicol RSS/RDSS theorems must not be identified with

- the vorticity-direction ratchet;
- the dual-lineage relative angle;
- or a local projective rotation rate.

Only a separately proved global rigid-rotation symmetry would justify that identification.

M5-511 does not make it.

---

## 9. Combined compact periodic frontier

M5-509 removed stationary marked states.

M5-511 removes arbitrarily short exact periodic returns on the spatial-Type-I subbranch.

Thus a nontrivial exact recurrent symmetry, if present, must satisfy

\[
\boxed{
\text{stationary}
\;\text{impossible},
}
\]

and

\[
\boxed{
\text{periodic with }0<\Theta<\Theta_{gap}
\;\text{impossible}.
}
\]

The exact-symmetry survivor is therefore a **finite-period long breather**, while the broader compact hull may remain aperiodic.

---

## 10. Updated frontier

Combining M5-508--511,

\[
\boxed{
\mathcal C_{ax+projdiff}
\Longrightarrow
H_{tail}^{remote-Sob}
\lor
H_{tail}^{remote-E}
\lor
H_{decay}^{U,1}
\lor
\mathcal C_{rec}^{critical},
}
\]

where on the last spatial-Type-I compact branch

\[
\mathcal C_{rec}^{critical}
\]

has

1. uniform marked nonstationarity;
2. no stationary Leray profile;
3. no exact DSS return with period below `Theta_gap(C_I)`;
4. possible long-period exact DSS or aperiodic recurrence.

---

## 11. Highest-value next target

The remaining compact hard core is now visibly a **breather/recurrence problem**, not a compactness problem.

The next internal calculation should thicken M5-509's pointwise marked speed floor into a fixed positive phase-space arclength cost per generation and then audit whether the finite persistent-lineage network can support that cost by pure closed cycles.

If it can, no scalar state-only strict cocycle can close the branch; one would need a path-memory, winding, flux-transfer, or topological observable.

---

## 12. Status

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
