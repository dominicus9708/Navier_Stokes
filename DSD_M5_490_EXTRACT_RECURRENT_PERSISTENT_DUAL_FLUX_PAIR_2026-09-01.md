# DSD M5-490 — Finite persistent lineages force a recurrent persistent dual-flux pair

Date: 2026-09-01

Status: **FINITE-LABEL RECURRENCE EXTRACTION / M5-455 REFORMS A FIXED-ANGLE DUAL-SOURCE COMPANION ON EVERY QUIET BOUNDED BLOCK, WHILE M5-488--489 SHOW THAT THE COMPACT PERSISTENT ENDPOINT CANNOT QUIETLY CREATE UNBOUNDEDLY MANY NEW FIXED-FLUX LABELS / THEREFORE THE DUAL-SOURCE ROLE MUST BE REUSED BY A FINITE SET OF PERSISTENT MATERIAL-FLUX DESCENDANTS / AFTER A PIGEONHOLE AND SHIFT-COMPACT EXTRACTION, AT LEAST ONE ORDERED/UNORDERED PAIR OF PERSISTENT LINEAGES CARRIES FIXED NONZERO FLUX AND REAPPEARS WITH FIXED NONCOLLINEAR ANGLE AT POSITIVE LOG-SCALE FREQUENCY / THIS PRODUCES A RECURRENT DUAL-PAIR GRAM/FLUX MARK ON THE INVARIANT HULL, BUT RELATIVE ANGLE ITSELF IS NOT A MONOTONE COCYCLE / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Inputs

M5-455 gives on every retained quiet bounded-metric block

\[
\boxed{
N_{metric}^{elliptic}
\Longrightarrow
G_{dual\ flux}^{metric}
\lor
H_{remote/derivative}^{strong}.
}
\]

On the compact endpoint, the strong remote/derivative branch is excluded.

Hence every retained quiet block reforms a dual-source/companion flux geometry with

1. a productive principal carrier;
2. a companion material-flux packet;
3. fixed normalized flux size;
4. a fixed nonzero angular separation, modulo the already typed projective/frequency defect branches.

M5-488 shows that repeated creation of genuinely new fixed-flux material labels is limited by finite storage memory.

M5-489 then isolates the persistent finite-lineage branch.

---

## 2. Finite persistent label set

On a quiet persistent block, let

\[
\mathcal L
=\{1,\ldots,N\},
\qquad
N\le N_{max},
\]

be the coherent fixed-flux material lineages retained in the bounded normalized observation region.

Each lineage `alpha` carries a scale-critical directed vorticity flux

\[
\Phi_\alpha
\]

with

\[
\boxed{
|\Phi_\alpha|\ge\phi_0>0
}
\]

whenever it participates as one of the active dual-source carriers.

The flux threshold `phi_0` is inherited from the fixed-flux formation theorem and the bounded metric comparability constants.

---

## 3. Dual-pair event mark

For each quiet generation/block `j`, select one dual-source pair

\[
(\alpha_j,\beta_j),
\qquad
\alpha_j\ne\beta_j,
\]

from the persistent label set whenever no new-label replacement is used.

Let their coherent local directions at the marked dual-source time be

\[
\xi_{\alpha_j,j},
\qquad
\xi_{\beta_j,j}.
\]

M5-455 supplies a fixed angular separation

\[
\boxed{
\sin\angle(
\xi_{\alpha_j,j},
\xi_{\beta_j,j}
)
\ge s_0>0
}
\]

on the no-angular-defect branch.

Equivalently,

\[
\boxed{
1-
(\xi_{\alpha_j,j}\cdot\xi_{\beta_j,j})^2
\ge s_0^2.
}
\]

---

## 4. Finite-pair pigeonhole

There are at most

\[
\binom{N_{max}}2
\]

unordered persistent lineage pairs.

Suppose dual-source blocks occur with lower density `delta_dual>0` along the retained quiet sequence.

Then at least one pair `(alpha_*,beta_*)` appears with lower/Banach density at least

\[
\boxed{
\delta_{pair}
\ge
\frac{\delta_{dual}}{\binom{N_{max}}2}
>0
}
\]

after passing to a suitable long-block subsequence.

If the dual-source reformation is available on every retained quiet block, `delta_dual` may be taken as the retained-block density.

Thus one fixed pair is reused recurrently.

---

## 5. Shift-compact marked pair extraction

Extend the M5-485 generation state by the pair label and pair geometry:

\[
Z_j^{pair}
=
(Z_j,\alpha_j,eta_j,\Phi_{\alpha_j},\Phi_{\beta_j},G_j),
\]

where

\[
\boxed{
G_j
:=
1-(\xi_{\alpha_j,j}\cdot\xi_{\beta_j,j})^2.
}
\]

On the selected pair subsequence,

\[
G_j\ge s_0^2.
\]

The bounded/no-frequency-defect local smooth compactness keeps the coherent carrier directions and fixed-flux marks stable after extraction.

Hence the marked dilation hull supports an invariant component with pair-event indicator `a_pair` satisfying

\[
\boxed{
\langle a_{pair}\rangle>0,
}
\]

and on the marked pair events

\[
\boxed{
G_{\alpha_*\beta_*}
\ge s_0^2,
\qquad
|\Phi_{\alpha_*}|,
|\Phi_{\beta_*}|
\ge\phi_0.
}
\]

---

## 6. Persistent dual-pair descriptor

Define the scale-critical pair descriptor

\[
\boxed{
\mathcal G_{\alpha\beta}
:=
|\Phi_\alpha\Phi_\beta|
\left[1-(\xi_\alpha\cdot\xi_\beta)^2\right].
}
\]

On every marked recurrence of the extracted pair,

\[
\boxed{
\mathcal G_{\alpha_*\beta_*}
\ge
\phi_0^2s_0^2
=:g_*>0.
}
\]

This quantity measures simultaneous persistence of

1. two nontrivial material-vorticity fluxes;
2. noncollinearity of their coherent directions.

It is invariant under simultaneous reversal of either oriented direction/flux convention because of the squared angle factor and absolute flux product.

---

## 7. Pair descriptor is a mark, not a drift

Although

\[
\mathcal G_{\alpha_*\beta_*}\ge g_*
\]

at positive frequency, this does not imply monotone accumulation.

The two directions may separate and realign recurrently.

Thus

\[
\boxed{
\mathcal G\text{ is a recurrence observable, not a Lyapunov observable.}
}
\]

In particular, no inequality of the form

\[
\mathcal G\circ\sigma-\mathcal G
\ge c a_{pair}
\]

is available.

A periodic DSS orbit could in principle carry a periodic nonzero `mathcal G` mark.

---

## 8. Relative-angle variation is also not a strict cocycle

Let

\[
c_{\alpha\beta}
:=
\xi_\alpha\cdot\xi_\beta.
\]

Since

\[
-1\le c_{\alpha\beta}\le1,
\]

it is bounded.

But recurrent projective motion can make `c` oscillate with

\[
\langle c_{j+1}-c_j\rangle=0
\]

while

\[
\langle|c_{j+1}-c_j|\rangle>0.
\]

Therefore relative angle has the same bounded-recurrence obstruction as scalar material flux in M5-489.

Positive total angular variation does not produce signed drift.

---

## 9. Relation to vorticity-direction regularity theory

Classical geometric-depletion criteria show that sufficient spatial coherence of the vorticity direction can prevent blow-up.

The present survivor carries the opposite kind of mark on a recurrent natural-scale subsystem: two persistent fixed-flux populations repeatedly exhibit an order-one relative angle.

This does **not** contradict those regularity criteria, because failure of a sufficient coherence condition is not a singularity theorem.

It does show that the compact endpoint cannot collapse into a single globally coherent vorticity direction field at every active natural scale.

---

## 10. Combine with M5-486 axial production

Every nonzero invariant similarity component satisfies

\[
\boxed{
\langle Q\rangle
=
\frac14\langle E\rangle+
\langle P\rangle
>0.
}
\]

The recurrent dual-pair subsystem additionally has

\[
\boxed{
\langle a_{pair}\mathcal G_{\alpha_*\beta_*}\rangle
\ge
\delta_{pair}g_*>0.
}
\]

Thus the persistent compact endpoint simultaneously requires

1. positive average axial vorticity stretching;
2. recurrent noncollinear persistent material flux;
3. positive-density projective/tension ratchet or oscillatory flux cost from M5-487--489.

These are now three distinct structural requirements.

---

## 11. Finite-state reuse versus new formation

The key DSD consequence is that the compact endpoint is no longer permitted to explain each new dual-source event by creating an entirely new material source.

Finite memory forces

\[
\boxed{
\text{recurrent dual-source geometry}
\Longrightarrow
\text{reuse of persistent finite labels}
\lor
\text{costed replacement exits}.
}
\]

After selecting the persistent branch, the same finite material architecture must reproduce the dual-source geometry indefinitely in log scale.

This is substantially more rigid than an arbitrary backward DSS/aperiodic ancient solution.

---

## 12. New endpoint class

Define

\[
E_{pair}^{persistent}
\]

as a compact Type-I similarity hull carrying a persistent pair `(alpha_*,beta_*)` with

\[
|\Phi_{\alpha_*}|,
|\Phi_{\beta_*}|
\ge\phi_0
\]

and

\[
\mathcal G_{\alpha_*\beta_*}
\ge g_*
\]

at positive similarity/log-scale frequency.

Then the persistent branch becomes

\[
\boxed{
E_{persistent}^{lineage}
\Longrightarrow
E_{pair}^{persistent}
\lor
E_{cost}^{flux/projective}.
}
\]

On the quietest lane, `E_pair^persistent` is the new hard core.

---

## 13. Highest-value next target

The next useful calculation is no longer another label-count argument.

A finite persistent dual pair suggests two analytic observables.

### D1 — pair interaction matrix

Track the `2x2` matrix of axial/projective strain actions on the two persistent directions,

\[
M_{ab}
:=
\xi_a\cdot\Sigma\xi_b,
\qquad
a,b\in\{\alpha_*,\beta_*\}.
\]

Determine whether positive average global stretching `Q` plus recurrent noncollinearity forces a positive off-diagonal/projective cost that can be compared with M5-487 tension.

### D2 — two-lineage flux/angle transport law

Differentiate the Gram quantity

\[
\xi_{\alpha_*}\cdot\xi_{\beta_*}
\]

along the two material lineages and insert

\[
D_t\xi
=\tau+\mathcal D_\xi.
\]

This gives an exact relative-angle action identity.

Although the net relative angle is recurrent and has zero mean drift, the identity may expose a signed cancellation requirement between strain tilt and directional diffusion on the two persistent lineages.

That cancellation is the next candidate rigidity relation.

---

## 14. Status

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
