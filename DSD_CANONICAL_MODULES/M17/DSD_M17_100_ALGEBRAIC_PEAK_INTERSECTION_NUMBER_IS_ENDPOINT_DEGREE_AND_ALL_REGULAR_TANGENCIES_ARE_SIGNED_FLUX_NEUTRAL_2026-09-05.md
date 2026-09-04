# DSD M17-100 — Algebraic peak intersection number is an endpoint degree and all regular tangencies are signed-flux neutral

Date: 2026-09-05
Canonical ID: **M17-100**

Status: **INTERNAL RANK-2 ALGEBRAIC INTERSECTION LEDGER / M17-099 SHOWS THAT A GENERIC QUADRATIC DIRECTOR-AREA/PEAK TANGENCY CREATES OR DESTROYS TWO TRANSVERSE INTERSECTIONS WITH OPPOSITE ORIENTATION, SO THE EVENT HAS ZERO NET SIGNED DIRECTOR-AREA FLUX COST. THE PRESENT MODULE REMOVES THE QUADRATIC RESTRICTION. ON ANY ORIENTED REGULAR DIRECTOR-AREA FLUX-TUBE SEGMENT WHOSE ENDPOINTS STAY OFF THE PEAK SET `g=0`, THE ALGEBRAIC SUM OF TRANSVERSE PEAK INTERSECTIONS IS EXACTLY THE ONE-DIMENSIONAL ENDPOINT DEGREE `I_lambda=[sgn g(s_+)-sgn g(s_-)]/2`. CONSEQUENTLY THIS INTEGER IS INVARIANT UNDER ALL INTERIOR SMOOTH TANGENCIES, HIGHER FINITE-ORDER CONTACTS, AND PAIR CREATION/ANNIHILATION EVENTS AS LONG AS `J_xi!=0`, THE PEAK LEVEL SET REMAINS REGULAR, AND NO ZERO CROSSES AN ENDPOINT. WEIGHTING EACH FROZEN TUBE LABEL BY ITS CONSERVED DIRECTOR-AREA FLUX GIVES A SIGNED INTERSECTION-FLUX CHARGE THAT IS ALSO INVARIANT UNDER SUCH INTERNAL GENEALOGY. THEREFORE TANGENCY OF ANY REGULAR FINITE ORDER IS NOT THE MISSING NONRECYCLABLE DIRECTOR-AREA COST. A CHANGE OF ALGEBRAIC INTERSECTION FLUX REQUIRES ENDPOINT CROSSING, PEAK-SET SINGULARITY, DIRECTOR-AREA/RANK LOSS, OR CHART/INTERFACE CHANGE. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. One frozen director-area tube

On the pure-transverse-kernel Rank-2 branch,

\[
J_\xi=|J_\xi|k\neq0,
\qquad
D_k\xi=0.
\]

The corresponding two-form

\[
\beta_\xi=\iota_{J_\xi}dV
\]

is frozen into the similarity material flow.

Fix one regular director-area flux-tube label `lambda` and an oriented compact tube segment

\[
L_\lambda(\theta)
=\{X_\lambda(s,\theta):s_-\le s\le s_+\}
\]

whose endpoints remain away from the peak set.

Choose the orientation so that increasing `s` follows `k`.

Define the restricted peak descriptor

\[
\boxed{
f_\lambda(s,\theta)
:=g(X_\lambda(s,\theta),\theta),
\qquad
g=D_\xi\log\rho.
}
\]

At every transverse peak intersection,

\[
f_\lambda=0,
\qquad
\partial_sf_\lambda\neq0.
\]

After positive local reparametrization of `s`,

\[
\operatorname{sgn}(\partial_sf_\lambda)
=\operatorname{sgn}(D_kg).
\]

---

## 2. Algebraic intersection number

At a transverse time let the simple roots inside the segment be

\[
s_1<\cdots<s_N.
\]

Define their oriented intersection signs

\[
\boxed{
\varepsilon_i
:=\operatorname{sgn}(D_kg(s_i))
\in\{-1,+1\}.
}
\]

The algebraic peak-intersection number of the tube segment is

\[
\boxed{
I_\lambda
:=\sum_{i=1}^N\varepsilon_i.
}
\]

This is the one-dimensional oriented intersection number of the flux line with the regular level surface `g=0`.

---

## 3. Exact endpoint-degree formula

Between simple zeros, the sign of `f_lambda` is constant.

A root with

\[
\varepsilon_i=+1
\]

crosses from negative to positive, whereas

\[
\varepsilon_i=-1
\]

crosses from positive to negative.

Therefore all interior sign changes telescope, giving

\[
\boxed{
I_\lambda
=
\frac{
\operatorname{sgn}f_\lambda(s_+,\theta)
-
\operatorname{sgn}f_\lambda(s_-,\theta)
}{2}.
}
\]

Equivalently,

\[
\boxed{
I_\lambda
=
\frac{
\operatorname{sgn}g(s_+)
-
\operatorname{sgn}g(s_-)
}{2}.
}
\]

Thus the algebraic count is determined entirely by endpoint signs.

No information about the number of interior maxima/minima is needed.

---

## 4. Immediate invariance under interior tangency

Suppose during a smooth time interval

\[
g(s_-,\theta)\neq0,
\qquad
g(s_+,\theta)\neq0
\]

and neither endpoint sign changes.

Then Section 3 gives

\[
\boxed{
I_\lambda(\theta)=\text{constant}.
}
\]

This remains true even at isolated times when one or more interior intersections become tangent and the transverse representation temporarily fails.

Therefore any interior tangency can only rearrange intersections in combinations whose net oriented sign is zero.

---

## 5. Recovery of the M17-099 fold

At a quadratic fold,

\[
g=0,
\qquad
D_kg=0,
\qquad
D_k^2g\neq0,
\qquad
D_Bg\neq0,
\]

M17-099 gives

\[
0\longleftrightarrow2
\]

intersections with signs

\[
(+1,-1)
\]

or

\[
(-1,+1).
\]

Hence

\[
\Delta I_\lambda=0,
\]

exactly as predicted by the endpoint-degree formula.

Thus the local fold calculation is the first nontrivial member of the general algebraic-intersection law.

---

## 6. Finite higher-order tangency

Consider a finite-order contact of order `m>=2` along the flux tube:

\[
D_kg=\cdots=D_k^{m-1}g=0,
\qquad
D_k^m g\neq0.
\]

A generic one-parameter unfolding has local leading form

\[
\boxed{
A\tau+c\eta^m=0
}
\]

with nonzero `A,c` after smooth local rescaling.

### even m

The roots are created or destroyed in opposite-orientation pairs.
Therefore

\[
\boxed{\Delta I_\lambda=0.}
\]

### odd m

One real intersection continues through the event. Its algebraic orientation is preserved across the local continuation.
Therefore again

\[
\boxed{\Delta I_\lambda=0.}
\]

More complicated finite-order unfoldings factor into the same elementary oriented pair rearrangements. The endpoint-degree identity remains the stronger statement and does not require choosing a specific normal form.

---

## 7. Flux weighting

Let

\[
d\Phi_J(\lambda)
\]

be the conserved director-area flux carried by the frozen tube label `lambda`.

Define the signed algebraic peak-intersection flux on a fixed label family `Lambda` by

\[
\boxed{
\mathcal Q_{peak}^{alg}
:=\int_\Lambda
I_\lambda\,d\Phi_J(\lambda).
}
\]

Since

1. `dPhi_J` is fixed on each regular frozen tube label, and
2. `I_lambda` is fixed while endpoint signs remain unchanged,

we obtain

\[
\boxed{
\frac d{d\theta}\mathcal Q_{peak}^{alg}=0
}
\]

through arbitrary interior regular tangency/type-rearrangement events.

This is an inherited signed intersection ledger, not a newly postulated physical conservation law.

---

## 8. Relation to the positive transverse measure of M17-097

M17-097 uses, on one orientation-fixed transverse component,

\[
d\Phi_J
=J_\xi\cdot n_S\,dA.
\]

That positive-component measure is appropriate only while the chosen crossing orientation remains fixed.

The present algebraic measure instead keeps the tube orientation fixed and assigns each transverse intersection the sign

\[
\varepsilon=\operatorname{sgn}(D_kg).
\]

Hence a tangency may change the **unsigned number** of peak intersections while leaving

\[
\boxed{
\sum\varepsilon\,d\Phi_J
}

unchanged.

This resolves the apparent tension between a changing transverse peak population and conserved director-area flux.

---

## 9. Relation to type ledgers

Critical type `nu` is an internal state attached to an intersection.

Clean type switches already preserve total director-area flux by M17-098.
Tangency pair events may additionally create or remove two intersections.

But after summing over type and orientation, the algebraic carrier obeys

\[
\boxed{
\sum_\nu\sum_{i\in\nu}
\varepsilon_i\,d\Phi_J
=I_\lambda d\Phi_J,
}
\]

which is endpoint controlled.

Therefore neither clean type switching nor regular interior tangency can change the algebraic director-area peak-intersection charge.

---

## 10. What can change the algebraic intersection flux

The endpoint-degree proof fails only if one of its hypotheses fails.

The explicit exit classes are

\[
\boxed{
\begin{aligned}
&g(s_\pm,\theta)=0
&&\text{peak crossing through a chosen tube endpoint},\\
&\nabla g=0\text{ on }g=0
&&\text{singular peak level set / genealogy singularity},\\
&J_\xi=0
&&\text{director-area or rank degeneration},\\
&\text{tube label ceases to remain in the retained domain}
&&\text{endpoint/chart/interface exit}.
\end{aligned}
}
\]

Only such events can alter the endpoint degree or invalidate the frozen flux carrier.

Thus **regular tangency itself is removed from the candidate nonrecyclable-cost list.**

---

## 11. Two-ended decaying components

For a two-ended tube segment chosen far enough into a regime where `g` has fixed nonzero endpoint signs, Section 3 gives a fixed algebraic excess of maxima over minima.

For example, if

\[
g(s_-)>0,
\qquad
g(s_+)<0,
\]

then

\[
\boxed{I_\lambda=-1.}
\]

so the segment contains algebraically one more positive-to-negative crossing than the reverse.

This is consistent with the existence of at least one line maximum, but it does not prohibit arbitrarily many internal maximum/minimum pairs.

No endpoint sign is assumed unless independently established on the retained tail.

---

## 12. DSD analysis

There are now three different notions that must not be conflated:

1. **unsigned peak count** — changes at fold/tangency events;
2. **type population** — changes under internal critical-order switches;
3. **algebraic director-area intersection flux** — endpoint degree of the persistent carrier.

The first two are genealogy descriptors.
The third is the orientation-sensitive carrier ledger.

Only the third survives arbitrary regular internal rearrangement.

---

## 13. DSD audit

### Audit A — interpreting more peak intersections as more director-area charge
Rejected.

### Audit B — assuming tangency itself changes oriented intersection number
Rejected by the endpoint-degree identity.

### Audit C — using the algebraic count when an endpoint lies on `g=0`
Rejected. Endpoint crossing is an explicit source event.

### Audit D — continuing through `J_xi=0`
Rejected. The oriented flux-tube carrier is lost there.

### Audit E — assuming the peak surface is regular at every tangency
The present theorem requires the level-set geometry to remain regular as a surface. Events with `grad g=0` belong to the singular-peak branch.

### Audit F — claiming algebraic intersection conservation proves regularity
Rejected. It only removes regular tangency as a possible nonrecyclable director-area cost.

---

## 14. Updated Rank-2 event hierarchy

After M17-100,

\[
\boxed{
\text{clean type switch}
\ \text{and}\
\text{regular interior tangency}
\Longrightarrow
\text{internal recyclable genealogy}.
}
\]

A genuine change of the algebraic peak-intersection flux requires

\[
\boxed{
E_{nonrecyclable}^{R2}
\subset
E_{endpoint}
\cup
E_{\nabla g=0}
\cup
E_{J_\xi=0}
\cup
E_{chart/interface}.
}
\]

The remaining local hard event is therefore no longer ordinary tangency. It is the **singular peak-set / endpoint / rank-interface gate**.

For persistent tangency, M17-099 still gives the independent compensation problem

\[
D_\xi(\sigma+\kappa)=0,
\qquad
\alpha_T=-\frac{D_kD_\xi(\sigma+\kappa)}{D_k^2g},
\]

but any resulting interior tangency genealogy remains signed-flux neutral while the endpoint-degree hypotheses survive.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
