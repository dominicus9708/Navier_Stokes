# M19-384 — Same-label log flux is an exact path potential; nonzero graph affinity requires label replacement or reset

Date: 2026-09-18

Status: **NEW MATERIAL-GENEALOGY EDGE FIREWALL / ON ANY FIXED ORIENTED INFINITESIMAL MATERIAL VORTEX-FLUX LABEL IN CE-H, `D_B log dPhi = kappa`. THEREFORE THE PATH-INTEGRATED KAPPA ACTION BETWEEN TWO TIMES IS EXACTLY THE ENDPOINT DIFFERENCE OF `log dPhi`. WHEN A PHASE/COMPONENT GRAPH IS LIFTED TO RETAIN THE MATERIAL LABEL AND ITS FLUX COORDINATE, THIS EDGE ACTION IS AN EXACT POTENTIAL AND HAS ZERO HOLONOMY AROUND EVERY TRUE CLOSED SAME-LABEL CYCLE. A NONZERO COARSE GRAPH CYCLE ACTION CAN ONLY COME FROM HIDDEN FLUX DRIFT, LABEL REPLACEMENT/RESET, RE-REFERENCING, OR A FAILURE OF THE FIXED-LABEL REPRESENTATION. THUS MATERIAL FLUX CAN BREAK RECYCLING ONLY ON REPLACEMENT/RESET EDGES OR SIGN-PRESERVING MONOTONE CORRIDORS SUCH AS M5-648--649, NOT ON AN ORDINARY RECURRENT SAME-LABEL CYCLE. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Exact material leaf-flux law

On CE-H, for an oriented infinitesimal material vortex-tube flux element `dPhi_lambda`,

\[
\boxed{
D_B(d\Phi_\lambda)=\kappa_\lambda d\Phi_\lambda.
}
\]

As long as the orientation and nonzero label are retained,

\[
\boxed{
D_B\log|d\Phi_\lambda|=\kappa_\lambda.
}
\]

Thus for any two times `theta_1<theta_2`,

\[
\boxed{
\int_{\theta_1}^{\theta_2}\kappa_\lambda(\theta)d\theta
=
\log\frac{|d\Phi_\lambda(\theta_2)|}{|d\Phi_\lambda(\theta_1)|}.
}
\]

The integrated coefficient exposure of one material leaf is therefore an exact endpoint difference.

---

## 2. Lift a coarse phase graph by the flux coordinate

Let a coarse recurrent graph have vertices `V_i` describing M19-382 phase/component states.

Suppose a fixed material label passes successively through vertices

\[
V_{i_0}\to V_{i_1}\to\cdots\to V_{i_m}.
\]

For the `r`th edge, define the same-label coefficient action

\[
\boxed{
A_r
:=
\int_{\theta_r}^{\theta_{r+1}}\kappa_\lambda d\theta.
}
\]

Then

\[
A_r
=
\log|d\Phi_\lambda(\theta_{r+1})|
-
\log|d\Phi_\lambda(\theta_r)|.
\]

Hence the edge action is exact on the lifted state space

\[
(V_i,\lambda,\log|d\Phi|).
\]

---

## 3. True same-label closed cycles have zero flux holonomy

If the trajectory returns to the same full lifted material state, in particular

\[
|d\Phi_\lambda(\theta_m)|
=|d\Phi_\lambda(\theta_0)|,
\]

then telescoping gives

\[
\boxed{
\sum_{r=0}^{m-1}A_r=0.
}
\]

Equivalently,

\[
\boxed{
\oint\kappa_\lambda d\theta=0
}
\]

around a true closed same-label/flux cycle.

Thus the integral of `kappa` cannot provide a nonexact graph affinity on a fixed material label.

---

## 4. Apparent coarse-cycle holonomy means hidden flux drift

A coarse phase graph may show a return

\[
V_i\to\cdots\to V_i
\]

while the same label has

\[
|d\Phi_{out}|\ne|d\Phi_{in}|.
\]

Then the coarse graph records a nonzero cycle action

\[
\oint\kappa d\theta
=
\log\frac{|d\Phi_{out}|}{|d\Phi_{in}|}.
\]

This is not a topological holonomy of the complete state.
It is merely an omitted state coordinate: the material flux changed.

Once `log|dPhi|` is restored to the state, the action becomes exact again.

Therefore

\[
\boxed{
\text{coarse nonzero kappa cycle action}
\Rightarrow
\text{hidden same-label flux drift or genealogy change}.
}
\]

---

## 5. Bounded recurrent same-label flux has zero mean drift

Suppose a retained same-label lineage remains nondegenerate with

\[
0<\phi_-\le|d\Phi_\lambda(\theta)|\le\phi_+<\infty.
\]

Then `log|dPhi_lambda|` is bounded.

Hence along any complete recurrent/invariant same-label trajectory,

\[
\boxed{
\lim_{T\to\infty}
\frac1T\int_0^T\kappa_\lambda d\theta
=0
}
\]

whenever the time average exists.

This is the same bounded-coboundary mechanism already used for persistent flux levels.

Again, it yields no positive mean edge affinity.

---

## 6. Where material flux genuinely becomes irreversible

The flux coordinate becomes useful for recycle-breaking only when additional structure supplies one-way behavior.

### A. Sign-preserving same-law corridors

M5-648--649 give precisely this case.
After absolute or relative normalization,

\[
D_B\log\widehat\Phi<0
\]

on the lower ordered population.

Then the finite base transverse-flux resource telescopes irreversibly.

### B. Label replacement or reset

If one event exits label `lambda` and the next retained event is carried by a distinct material population `lambda'`, no single `log Phi_lambda` potential spans the transition.

The graph edge is then a **genealogical replacement edge** rather than a same-label state transition.

### C. Representation failure

Nodal loss, sheet merge/split, domain/interface loss, or other representation exits may also destroy the fixed-label chart.
Such an exit must be priced separately; it cannot be hidden as same-label graph holonomy.

---

## 7. Consequence for M19-383 PDE edge affinity search

M19-383 asks for a PDE-inherited nonexact edge action.

The most obvious candidate,

\[
\int\kappa d\theta,
\]

fails on fixed-label cycles because it is exact:

\[
\int\kappa d\theta=\Delta\log|d\Phi|.
\]

Therefore a successful affinity cannot be built solely from same-label coefficient exposure.

It must live on

\[
\boxed{
\text{replacement/reset edges}
\lor
\text{one-way relative-flux corridors}
\lor
\text{another genuinely dissipative physical action}.
}

---

## 8. Relation to the critical 3/2 seed cascade

M19-360--365 and M5-678--680 already show that late curvature carriers can evade finite base-flux counting by beginning with

\[
\phi_{0,j}\lesssim e^{-3T_j/2}
\]

and amplifying to order-one retained flux.

Thus even replacement edges cannot automatically be charged a generation-independent amount of the base flux measure.

The next replacement theorem must defeat this critical discount, not merely count new labels.

---

## 9. Updated target

The graph recycle problem is now reduced further:

\[
\boxed{
\mathcal T_{replace}^{noncritical}:
\text{show that recurrent replacement/reset edges require a non-discounted physical cost, or force a typed critical 3/2 seed architecture that can be attacked by PDE-specific elliptic/strain structure.}
}

Equivalently, the remaining edge problem is no longer ordinary graph circulation; it is **genealogical replacement under critical exponential base-flux discount**.

---

## 10. Firewall

Do not use `int kappa dt` as a nonexact cycle affinity on a fixed material label.

Do not infer irreversibility from a coarse-state return unless the material flux coordinate and label identity are also restored.

Do not count label replacement against finite base flux without confronting the `e^{-3T/2}` critical discount.

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
