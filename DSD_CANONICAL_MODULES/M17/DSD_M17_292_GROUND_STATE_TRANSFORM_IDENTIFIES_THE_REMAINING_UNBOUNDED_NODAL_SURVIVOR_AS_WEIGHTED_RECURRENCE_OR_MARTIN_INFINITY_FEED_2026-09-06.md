# DSD M17-292 — Ground-state transform identifies the remaining unbounded nodal survivor as weighted recurrence or Martin-infinity feed

Date: 2026-09-06  
Canonical ID: **M17-292**

Status: **STRUCTURAL RECLASSIFICATION / AFTER M17-283--291, THE PAYER-FREE UNBOUNDED STATIONARY NODAL SURVIVOR MUST CARRY SUPER-R7 PARABOLIC MASS GROWTH OR EXPLICIT FAR-FIELD INPUT. FOR THE AUTONOMOUS SCHRODINGER-HEAT OPERATOR `L=Delta-q`, `q=|grad xi|^2>=0`, INTRODUCE A POSITIVE STATIONARY SOLUTION/GROUND STATE `h` WHEN ONE EXISTS AND WRITE `a=h u`. THE AMPLITUDE EQUATION `a_tau=L a` THEN BECOMES EXACTLY THE WEIGHTED HEAT EQUATION `u_tau=h^(-2) div(h^2 grad u)`. THUS THE REMAINING QUESTION IS NOT A NEW LOCAL CE-H IDENTITY: IT IS WHETHER THIS GROUND-STATE WEIGHTED DIFFUSION IS CRITICAL/RECURRENT ENOUGH TO FORCE POSITIVE ANCIENT RIGIDITY, OR WHETHER THE OPERATOR/DOMAIN IS SUBCRITICAL AND ADMITS NONTRIVIAL MARTIN-BOUNDARY INPUT FROM SPATIAL INFINITY. CLASSICAL POSITIVE-SCHRODINGER AND MARTIN-BOUNDARY THEORY SHOWS THAT SUCH INFINITY MODES CAN HAVE DOMAIN-DEPENDENT SUBEXPONENTIAL OR SUPEREXPONENTIAL GROWTH, SO NO GENERAL LIouVILLE SHORTCUT IS AVAILABLE WITHOUT A CRITICALITY/RECURRENCE HYPOTHESIS. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Remaining amplitude equation

On a stationary active/nodal component `D`, the raw tangent amplitude satisfies

\[
\boxed{
\partial_\tau a
=(\Delta-q)a,
\qquad
q=|\nabla\xi|^2\ge0.
}
\]

Define

\[
L:=\Delta-q.
\]

M17-284--291 reduce the unbounded nonzero survivor to a genuinely spatial-infinity-driven branch.

---

## 2. Positive stationary reference state

Suppose the elliptic operator admits a positive stationary solution

\[
\boxed{h>0,\qquad Lh=0}
\]

on the unbounded component, with the appropriate boundary behavior.

No uniqueness of `h` is assumed yet.

Write

\[
\boxed{a=h u.}
\]

Since `h` is time independent,

\[
\partial_\tau a=h\partial_\tau u.
\]

Also

\[
\begin{aligned}
L(hu)
&=\Delta(hu)-qhu\\
&=u(\Delta h-qh)+2\nabla h\cdot\nabla u+h\Delta u\\
&=2\nabla h\cdot\nabla u+h\Delta u.
\end{aligned}
\]

Therefore

\[
\boxed{
\partial_\tau u
=\Delta u+2\nabla\log h\cdot\nabla u
=h^{-2}\nabla\cdot(h^2\nabla u).
}
\]

This is the exact Doob/ground-state transform.

---

## 3. Multiplier after the transform

Because

\[
a=h u,
\]

we have on the active set

\[
\boxed{
K
=\partial_\tau\log a
=\partial_\tau\log u.
}
\]

Thus sign-balanced multiplier activity is entirely encoded in the time logarithmic derivative of a **positive ancient solution of the weighted heat equation**.

The Schrödinger potential has moved into the invariant weight

\[
\boxed{d\mu_h=h^2dx.}
\]

---

## 4. Critical/recurrent versus subcritical/infinity-feed split

The natural structural split is now:

### A. Critical/recurrent ground-state channel

If the transformed weighted diffusion

\[
h^{-2}\nabla\cdot(h^2\nabla\cdot)
\]

has a sufficiently strong recurrence/Liouville property for the relevant positive ancient growth class, then one expects

\[
u\equiv\text{constant in time}
\]

and hence

\[
\boxed{K=0,}
\]

contradicting the retained sign-balanced coefficient packet.

This is a **target theorem**, not yet derived in the present repository at full required generality.

### B. Subcritical / Martin-infinity channel

If the operator is subcritical or the weighted diffusion admits nontrivial positive boundary data at spatial infinity, the ancient solution may be maintained by an infinity mode.

Retain

\[
\boxed{G_{Martin\text{-}boundary/infinity\ feed}.}
\]

This is the natural home for M17-287's far-boundary remainder and M17-291's super-R7 growth survivor.

---

## 5. External-theory audit

Relevant classical directions include:

- M. Murata, *Structure of positive solutions to (-Delta+V)u=0 in R^n*, Duke Math. J. 53 (1986), DOI `10.1215/S0012-7094-86-05347-0`: positive stationary Schrödinger solutions, asymptotics, and boundary conditions at infinity.
- Y. Pinchover, *A Liouville-type theorem for Schrödinger operators*, arXiv `math/0512431`: critical operators, ground states, and uniqueness of positive supersolutions under comparison hypotheses.
- D. DeBlassie, *The Martin Kernel for Unbounded Domains*, Potential Analysis (2010), DOI `10.1007/S11118-009-9156-2`: Martin-boundary behavior at infinity can depend strongly on unbounded-domain geometry, including subexponential and superexponential growth regimes.

These references support the **classification strategy**, not a direct proof of the Navier--Stokes branch.

In particular, they warn against assuming that every unbounded positive mode has polynomial growth or a unique simple infinity behavior.

---

## 6. Current infinity gate

Combining M17-284--292 gives

\[
\boxed{
G_{unbounded\ stationary\ nodal\ survivor}
\Longrightarrow
H_{weighted\ recurrence/criticality\ problem}
\lor
G_{Martin\text{-}infinity\ feed}
\lor
G_{ambient/coefficient/interface\ failure}.
}
\]

The local CE-H/director geometry has already been exhausted on this lane.
The remaining issue is global potential theory of the transformed weighted diffusion.

---

## 7. Next target

The most useful next theorem would be a **Ground-State Recurrence Gate (GSRG)**:

under repository-derived bounds on `h`, `grad log h`, director geometry, and volume growth, prove either

\[
\boxed{
\text{weighted diffusion recurrent/Liouville}
}
\]

or produce a quantitative Martin/infinity flux that can be charged back to the parent shell.

This is more precise than attempting another local multiplier identity.

---

## 8. DSD audit

- Existence of a positive ground state `h` is conditional and explicit.
- No classical theorem is claimed to apply automatically to the full DSD/CE-H setting.
- Criticality, recurrence, ground-state uniqueness, and Martin-boundary input are kept as distinct objects.
- Super-R7 growth is not declared contradictory by itself.
- Global 3D Navier--Stokes regularity remains unproved.

---

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
