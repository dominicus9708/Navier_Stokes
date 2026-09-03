# DSD M5-642 — Outer similarity dilation barrier prevents remote material inflow into the recurrent core

Date: 2026-09-03

Status: **INTERNAL MATERIAL-TRAJECTORY BARRIER / FOR THE SIMILARITY MATERIAL VELOCITY `B=U+y/2`, THE INHERITED TYPE-I/COMPACT-HULL VELOCITY BOUND `||U||_infty<=M_U` GIVES `d|Y|/dtheta >= |Y|/2-M_U`. CHOOSING `R_out>2M_U` MAKES `B·n>0` ON THE FIXED SPHERE `|y|=R_out` FOR ALL HULL STATES. THEREFORE FORWARD MATERIAL TRAJECTORIES CANNOT CROSS THAT SPHERE FROM OUTSIDE TO INSIDE. THE POSITIVE-RATE STRONGLY-NEGATIVE PACKET REPLACEMENT OF M5-641 CANNOT BE FED BY NEW MATERIAL LABELS ARRIVING FROM THE REMOTE SIMILARITY TAIL; ALL FUTURE CORE LABELS MUST COME FROM A FIXED FINITE MATERIAL RESERVOIR ALREADY INSIDE THE BARRIER AT AN EARLIER REFERENCE TIME. THIS IS A SOURCE-LOCALIZATION RESULT, NOT YET A FINITE-RESOURCE CONTRADICTION. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Similarity material radial equation

Let a material trajectory satisfy

\[
\dot Y=B(Y,\theta),
\qquad
B=U+\frac12Y.
\]

For

\[
r(\theta)=|Y(\theta)|,
\]

we have

\[
\dot r
=\frac{Y}{|Y|}\cdot U(Y,\theta)+\frac12r.
\]

The retained Type-I compact ancient class has a uniform similarity velocity bound

\[
\boxed{\|U(\theta)\|_\infty\le M_U<\infty.}
\]

Therefore

\[
\boxed{
\dot r\ge- M_U+\frac12r.
}
\]

---

## 2. Fixed outer barrier

Choose

\[
\boxed{R_{out}>2M_U.}
\]

On the sphere `|y|=R_out`,

\[
B\cdot n
=U\cdot n+\frac12R_{out}
\ge-M_U+\frac12R_{out}>0.
\]

Hence

\[
\boxed{B\cdot n>0\quad\text{on }S_{R_{out}}}
\]

uniformly in similarity time and throughout the compact hull.

The vector field points strictly outward across this sphere.

---

## 3. No forward inward crossing

A forward material trajectory outside `B_{R_out}` cannot cross the boundary inward.

Indeed any first inward crossing would require

\[
\dot r\le0
\]

at `r=R_out`, contradicting the strict outward bound.

Thus

\[
\boxed{
Y(\theta_0)\notin B_{R_{out}}
\Longrightarrow
Y(\theta)\notin B_{R_{out}}
\quad\forall\theta\ge\theta_0.
}
\]

Equivalently, the fixed ball is a forward no-inflow region for material labels.

Labels may leave the ball, but no new label can enter from the remote side.

---

## 4. Consequence for the M5-641 packet conveyor

M5-641 requires indefinite replacement of strongly-negative coherent material packets inside a fixed finite core.

Choose the outer barrier large enough to contain that core.

Then every material label that will ever participate in a future core packet must already lie inside `B_{R_out}` at any earlier reference time before its participation.

Therefore

\[
\boxed{
\text{strongly-negative packet conveyor}
\text{ is fed from one finite inner material reservoir, not from remote inflow.}
}
\]

This complements M5-542, where the remote spectator tail was shown not to pay the core strain/velocity ledger dynamically.

---

## 5. Stronger tail version

The terminal/scattering expansion later obtained in the proof gives

\[
U(y,\theta)=O(|y|^{-1})
\]

in the remote region.

Hence for sufficiently large `r`,

\[
\dot r
=\frac12r+O(r^{-1})>0.
\]

Thus the outer no-inflow behavior is not merely a consequence of a crude `L-infinity` bound; it agrees with the precise remote dilation conveyor structure.

---

## 6. What this does not yet prove

The reservoir

\[
B_{R_{out}}
\]

has finite volume, but it contains a continuum of material labels.

An infinite sequence of future coherent packets can in principle have exponentially shrinking preimages at the reference time because material volume expands as

\[
e^{3(\theta-\theta_0)/2}.
\]

Therefore finite reservoir volume by itself does **not** yet rule out infinitely many future replacements.

That summability issue must be audited explicitly before claiming a contradiction.

---

## 7. Next target

Compare two possible conserved/resources for the packet generations:

1. material volume, whose preimage costs decay geometrically and may be summable;
2. scale-invariant vorticity flux, whose lower bound `phi_*` does **not** acquire the same geometric generation factor on the negative-kappa branch.

If the future fixed-flux packets can be pulled back to disjoint initial flux resources with a finite total absolute-flux bound, a true finite-resource contradiction may result.

If no such global flux transversal/bound exists, that failure must be retained explicitly as the next hard geometric loophole.

---

## 8. Firewall

The uniform `L-infinity` velocity bound is an inherited property of the retained Type-I ancient class. If the final audit weakens that bound, the precise barrier radius must be reconstructed using the remote `O(1/r)` estimate instead.

No finite-resource contradiction is claimed in this note.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]