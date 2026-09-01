# DSD M5-512 — Uniform marked nonstationarity thickens to positive phase-space action per generation

Date: 2026-09-01

Status: **DYNAMIC-ACTION THICKENING / M5-509 GIVES A FIXED BALL AND A POSITIVE LOCAL SIMILARITY-TIME SPEED AT EVERY MARKED RECORD STATE / CONTINUITY OF THE SIMILARITY FLOW ON THE M5-508 GLOBAL SMOOTH COMPACT HULL MAKES THIS SPEED FLOOR PERSIST FOR A UNIFORM POSITIVE TIME INTERVAL / THE GENERATION ROOF TIMES HAVE A POSITIVE LOWER BOUND, SO THESE INTERVALS CAN BE CHOSEN INSIDE DISJOINT GENERATION CELLS / CONSEQUENTLY EVERY GENERATION CARRIES A FIXED POSITIVE LOCAL PHASE-SPACE ARCLENGTH AND THE SUSPENSION HAS POSITIVE MEAN DYNAMIC ACTION / THIS ACTION IS UNSIGNED, SO A CLOSED RECURRENT CYCLE CAN PAY IT FOREVER WITHOUT CONTRADICTION / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Input from M5-509

On the globally smooth compact marked section there exist

\[
R_{dyn}<\infty,
\qquad
\delta_{dyn}>0
\]

such that

\[
\boxed{
\|\partial_\theta W_Y\|_{L^2(B_{R_{dyn}})}
\ge
\delta_{dyn}
\qquad
\text{for every marked state }Y.
}
\]

Define the local phase-speed observable

\[
\boxed{
v(Y)
:=
\|\partial_\theta W_Y\|_{L^2(B_{R_{dyn}})}.
}
\]

Then

\[
v(Y)\ge\delta_{dyn}
\]

on the marked record section.

---

## 2. Similarity suspension and generation roof times

The M5-485 marked dilation hull has roof time

\[
\Theta(Y)
=2\log\lambda(Y).
\]

The record-ratio bounds give

\[
1<\lambda_-
\le
\lambda(Y)
\le
\lambda_+<\infty.
\]

Hence

\[
\boxed{
0<\Theta_-
:=2\log\lambda_-
\le
\Theta(Y)
\le
2\log\lambda_+
=:\Theta_+<\infty.
}
\]

Each marked generation therefore contains a uniformly positive amount of similarity time.

---

## 3. Uniform continuity of the local speed along the compact flow

Let

\[
\phi_tY
\]

denote the similarity flow on the smooth compact suspension hull.

On every fixed ball, the Navier--Stokes similarity evolution depends continuously on the state in the all-order topology supplied by M5-508.

Therefore

\[
(Y,t)
\mapsto
v(\phi_tY)
\]

is continuous on compact subsets of the suspension.

In particular, continuity is uniform near `t=0` over the compact marked section.

Thus there exists

\[
0<\tau_{dyn}
\le
\frac12\Theta_-
\]

such that for every marked state `Y` and every

\[
0\le t\le\tau_{dyn},
\]

we have

\[
\boxed{
v(\phi_tY)
\ge
\frac12\delta_{dyn}.
}
\]

This uses only compactness and continuity; no explicit second time-derivative estimate is needed.

---

## 4. Positive local phase-space arclength per generation

Define the local `L2(B_Rdyn)` phase-space arclength accumulated over the initial portion of one generation by

\[
\mathcal L_{dyn}(Y)
:=
\int_0^{\tau_{dyn}}
\|\partial_\theta W_{\phi_tY}\|_{L^2(B_{R_{dyn}})}dt.
\]

The uniform speed floor gives

\[
\boxed{
\mathcal L_{dyn}(Y)
\ge
\frac12\delta_{dyn}\tau_{dyn}
=:\ell_{dyn}>0.
}
\]

Thus every marked generation contributes at least one fixed positive amount of local phase-space path length.

---

## 5. The generation intervals do not overlap

Because

\[
\tau_{dyn}
\le
\frac12\Theta_-,
\]

and every roof satisfies

\[
\Theta(Y)\ge\Theta_-,
\]

the intervals

\[
[\theta_j,\theta_j+\tau_{dyn}]
\]

attached to successive marked generation times `theta_j` lie inside their own roof cells and are mutually disjoint.

Therefore the lower action bound can be summed without double counting.

For `N` generations,

\[
\boxed{
\int_{\theta_0}^{\theta_N}
v(\phi_tY)dt
\ge
N\ell_{dyn}.
}
\]

---

## 6. Positive mean dynamic action

The total similarity time of `N` generations is at most

\[
N\Theta_+.
\]

Hence

\[
\frac{1}{\theta_N-\theta_0}
\int_{\theta_0}^{\theta_N}
v(\phi_tY)dt
\ge
\frac{\ell_{dyn}}{\Theta_+}.
\]

Passing to long-time/invariant averages gives

\[
\boxed{
\langle v\rangle_{susp}
\ge
\frac{\ell_{dyn}}{\Theta_+}
>0.
}
\]

Thus the compact critical survivor has a strictly positive mean local phase-space speed.

---

## 7. Comparison with the earlier ratchet action

M5-469--485 forced positive-density projective/diffusive ratchet action.

M5-512 obtains a different quantity:

\[
\boxed{
\int
\|\partial_\theta W\|_{L^2(B_{R_{dyn}})}d\theta.
}
\]

The former measures a marked geometric mechanism involving vorticity direction and projected diffusion.

The latter measures actual local motion of the full vorticity state in phase space.

Therefore the compact survivor must be active in two senses:

1. positive projective/diffusive ratchet frequency;
2. positive full-state phase-space arclength rate.

They must not be conflated.

---

## 8. DSD audit: path length is not drift

Suppose a trajectory is periodic with period `Theta`.

It may have

\[
\int_0^\Theta
v(\phi_tY)dt>0
\]

while

\[
\phi_\Theta Y=Y.
\]

Thus positive arclength does not produce a bounded state potential `Phi` with

\[
\Phi(\phi_\Theta Y)-\Phi(Y)>0.
\]

Indeed the left side is exactly zero on a closed cycle.

Therefore

\[
\boxed{
\text{positive dynamic action}
\not\Longrightarrow
\text{positive signed cocycle drift}.
}
\]

This is the same structural barrier already visible abstractly in M5-485, now realized by an actual PDE phase-space observable.

---

## 9. Consequence for strict-cocycle design

A candidate closure functional cannot be merely a norm of instantaneous motion, total variation, or accumulated unsigned activity.

To defeat a recurrent cycle it must detect something that cannot cancel after one loop, for example a quantity of the schematic form

\[
\boxed{
\text{signed flux transfer},
\quad
\text{non-exact circulation},
\quad
\text{winding/topological charge},
\quad
\text{or path-memory with irreversible loss}.
}
\]

Whether such an observable exists for the Navier--Stokes marked lineage network remains open.

---

## 10. Relation to M5-511

On the spatial-Type-I exact-periodic branch, M5-511 gives

\[
\Theta\ge\Theta_{gap}>0.
\]

M5-512 independently gives positive arclength in every generation.

Thus a surviving exact periodic orbit would be a genuinely nontrivial finite-size loop in phase space:

\[
\boxed{
\text{period bounded away from zero}
+
\text{path length bounded away from zero}.
}
\]

It cannot collapse to a stationary or infinitesimal-loop limit.

General long-period DSS and aperiodic recurrence are not excluded.

---

## 11. Updated compact hard core

The globally compact recurrence branch now has all of the following:

\[
\boxed{
\begin{aligned}
&\text{nonzero marked carrier},\\
&\text{uniform marked phase speed},\\
&\text{positive phase-space action per generation},\\
&\text{positive axial-production mean},\\
&\text{positive ratchet activity},\\
&\text{no stationary profile},\\
&\text{no arbitrarily short exact DSS loop on spatial-Type-I branch}.
\end{aligned}
}
\]

This is no longer a compactness or derivative-control problem.

It is a recurrence/cycle rigidity problem.

---

## 12. Highest-value next target

The finite persistent-lineage network from M5-497--499 should now be combined with this positive phase-space action.

The precise question is whether every recurrent lineage cycle necessarily carries a signed viscous flux-transfer or helicity/circulation defect, or whether a completely balanced critical cycle is algebraically possible.

The next audit should begin with the exact conservation/balance laws available on one finite lineage cycle and separate signed observables from unsigned activity.

---

## 13. Status

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
