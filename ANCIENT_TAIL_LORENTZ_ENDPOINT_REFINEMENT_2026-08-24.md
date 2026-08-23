# Ancient Critical Tail: Lorentz-Endpoint Refinement — 2026-08-24

Status: **EXTERNAL REGULARITY BOUNDARY + DYADIC ENDPOINT DIAGNOSTIC / GLOBAL REGULARITY NOT PROVED.**

The restricted ancient survivor was previously shown to require a global critical velocity tail in order to evade the backward-sequence global `L^3` Liouville route. This note refines the spatial shape of that tail using the known nonendpoint Lorentz regularity boundary.

External input: N. C. Phuc, *The Navier-Stokes equations in nonendpoint borderline Lorentz spaces* (2014), proves regularity for `L_t^infinity L_x^{3,q}` with finite Lorentz index `q`, while the endpoint `L^{3,infinity}` is excluded from that theorem.

The present note does **not** claim an ancient-solution Liouville theorem in `L^{3,q}`. Its role is to identify what an endpoint critical shell stack must look like if the proof route is to avoid falling back into any finite-Lorentz-index regularity regime.

---

## 1. Critical shell model

Let

\[
A_k=\{2^kR_0<|Y|<2^{k+1}R_0\}
\]

and suppose on `A_k` the critical velocity scale is

\[
|V(Y)|\sim \frac{a_k}{R_k},
\qquad
R_k=2^kR_0,
\]

with dimensionless shell amplitude `a_k`.

The shell volume is `~R_k^3`, so

\[
\int_{A_k}|V|^3\sim a_k^3.
\]

Thus

\[
\boxed{
\|V\|_3^3\text{ on the tail}\sim\sum_ka_k^3.
}
\]

A logarithmic `1/R` stack corresponds to `a_k ~ 1`.

---

## 2. Lorentz index as logarithmic shell summability

For geometrically separated critical shells with monotone critical levels, the decreasing-rearrangement characterization gives schematically

\[
\boxed{
\|V\|_{L^{3,q}}^q
\asymp
\sum_k a_k^q,
\qquad 0<q<\infty,
}
\]

up to fixed annular comparability constants.

At the endpoint,

\[
\boxed{
\|V\|_{L^{3,\infty}}
\asymp
\sup_k a_k.
}
\]

Therefore the Lorentz endpoint separates

\[
\boxed{
\ell^q\text{ shell summability for some finite }q
}
\]

from

\[
\boxed{
\text{bounded but non-}\ell^q\text{ critical shell stacks}.
}
\]

---

## 3. Relation to annular Dirichlet criticality

For a critical shell `|V| ~ a_k/R_k`,

\[
|\nabla V|\sim \frac{a_k}{R_k^2}.
\]

Hence

\[
e_k:=\int_{A_k}|\nabla V|^2
\sim
\frac{a_k^2}{R_k}
\]

and

\[
\boxed{
J_k:=R_ke_k\sim a_k^2.
}
\]

Thus finite-Lorentz-index shell summability is equivalent at the critical model level to

\[
\boxed{
\sum_k J_k^{q/2}<\infty.
}
\]

The weak-`L^3` endpoint is instead controlled only by

\[
\boxed{
\sup_kJ_k<\infty.
}
\]

This sharpens the earlier condition

\[
\sum_kJ_k^{3/2}=\infty
\]

which merely expresses failure of strong `L^3`.

---

## 4. Endpoint survivor shape

If the first-hitting/ancient proof route succeeds in transferring any uniform finite-`q` Lorentz bound back to the pre-singular solution, the known nonendpoint regularity theorem would close that subcase.

Therefore a genuine unresolved critical-tail survivor must be prepared to realize the endpoint geometry

\[
\boxed{
\sup_kJ_k<\infty,
\qquad
\sum_kJ_k^{q/2}=\infty
\text{ for every relevant finite }q.
}
\]

The limiting possibility

\[
J_k\to0
\]

is not removed: for example logarithmically slow decay can fail every finite `ell^p` summability test. Thus the previous `vanishing-amplitude diffuse stack` remains possible, but it must decay exceptionally slowly in logarithmic radius.

---

## 5. Interaction with the Leray dilation conveyor

The linear far-tail conveyor preserves

\[
J_R=R\int_{A_R}|\nabla V|^2
\]

while shifting `R -> e^(Delta/2)R`. Therefore a weak-`L^3` endpoint stack is naturally transported by **translation in logarithmic radius**.

A globally recurrent/DSS endpoint stack must consequently replenish its logarithmic shell sequence from smaller scales, returning to the historical-recycling `H_remote/T` route.

A locally recurrent core with a nonrecurrent endpoint stack can still lose the tail to spatial infinity. That is the remaining tail-evacuation problem.

---

## 6. Claim boundary

The external Lorentz theorem is a regularity theorem for the pre-singular Navier--Stokes solution, not by itself a Liouville theorem for every ancient mild solution in `L^{3,q}`. Therefore the statement here is deliberately conditional:

\[
\boxed{
\text{finite-}q\text{ shell summability is a potentially closable regularity subcase;}
}
\]

it is not silently declared impossible for every extracted ancient limit without a transfer lemma.

The exact endpoint `L^{3,infinity}` remains the critical unresolved Lorentz space.

Status: **THE LAST LOW-FREQUENCY TAIL IS REFINED FROM MERE `L3` FAILURE TO AN ENDPOINT LORENTZ SHELL STACK. IN DYADIC CRITICAL VARIABLES, `L^{3,q}` CORRESPONDS TO FINITE `ell^q` SUMMABILITY OF SHELL AMPLITUDES, WHILE `L^{3,infinity}` RETAINS ONLY A SUPREMUM BOUND. THE UNRESOLVED SURVIVOR MUST LIVE AT OR VERY NEAR THIS ENDPOINT UNLESS A FINITE-q TRANSFER LEMMA FAILS. GLOBAL REGULARITY REMAINS UNPROVED.**