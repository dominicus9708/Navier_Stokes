# DSD M18-047 — Iterated remote chain splits into scale descent or spatial export

Date: 2026-09-11

Status: **REMOTE-CASCADE COMMON-FRAME AUDIT. AN ITERATED SATELLITE CHAIN CANNOT BE SUMMED ACROSS RECENTERED NORMALIZATIONS WITHOUT A PHYSICAL REPRESENTATION MAP. AFTER RESTORING PHYSICAL CENTERS AND NATURAL SCALES, EACH STRONGLY REMOTE GENERATION HAS AN EXACT DICHOTOMY: EITHER THE CHILD NATURAL SCALE IS STRONGLY SMALLER THAN THE PARENT SCALE, OR THE CHILD CENTER IS STRONGLY FAR IN PARENT-SCALE UNITS. THIS DOES NOT YET CONTRADICT NAVIER--STOKES, BUT IT REPLACES AN OPAQUE RECURSIVE REMOTE LABEL BY TWO GEOMETRICALLY DISTINCT CASCADE TYPES. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Why a common-frame audit is required

M5-402 permits an iterated chain

\[
S_{remote}^{(m)}
\to
S_{remote}^{(m+1)}
\to\cdots
\]

when ambient strain repeatedly creates another active remote object.

However each generation is defined after recentering and rescaling.

Therefore quantities from different generations cannot be added merely because their normalized forms look identical.

The first task is to reconstruct one physical genealogy.

---

## 2. Physical parent-child variables

Let generation `m` have physical center

\[
x_m
\]

and physical natural length

\[
r_m>0.
\]

In the generation-`m` normalized frame, suppose the next active satellite is located at dimensionless distance

\[
D_m:=\frac{|x_{m+1}-x_m|}{r_m}
\]

and has dimensionless natural scale

\[
\ell_m:=\frac{r_{m+1}}{r_m}.
\]

Then exactly

\[
\boxed{
r_{m+1}=r_m\ell_m,
}
\]

and

\[
\boxed{
|x_{m+1}-x_m|=r_mD_m.
}
\]

The remote-satellite separation parameter is

\[
\boxed{
K_m
:=
\frac{D_m}{\ell_m}
=
\frac{|x_{m+1}-x_m|}{r_{m+1}}.
}
\]

Thus `K_m` has a direct physical meaning: parent-child center separation measured in **child natural radii**.

---

## 3. What `K_m->infinity` does not imply

The condition

\[
K_m\to\infty
\]

does not separately imply

\[
D_m\to\infty
\]

or

\[
\ell_m\to0.
\]

For example, one may have

\[
\ell_m=K_m^{-2},
\qquad
D_m=K_m^{-1},
\]

so that

\[
K_m=D_m/\ell_m
\]

is large even though the child lies close in parent-scale units.

In that case the remoteness comes entirely from extreme scale descent.

Conversely `ell_m` may remain order one while `D_m` becomes large, giving genuine spatial export.

Therefore the old phrase 'remote satellite' combines two distinct mechanisms.

---

## 4. Exact square-root dichotomy

Since

\[
D_m=K_m\ell_m,
\]

for every `K_m>1` one has the elementary dichotomy

\[
\boxed{
\ell_m\le K_m^{-1/2}
\quad\lor\quad
D_m\ge K_m^{1/2}.
}
\]

Indeed, if

\[
\ell_m>K_m^{-1/2},
\]

then

\[
D_m=K_m\ell_m>K_m^{1/2}.
\]

Thus every sufficiently strong remote generation is of at least one of two types.

### Type SD — scale descent

\[
\boxed{
\ell_m\le K_m^{-1/2}.
}
\]

Then

\[
\boxed{
r_{m+1}\le K_m^{-1/2}r_m.
}
\]

### Type SE — spatial export

\[
\boxed{
D_m\ge K_m^{1/2}.
}
\]

Then

\[
\boxed{
|x_{m+1}-x_m|
\ge K_m^{1/2}r_m.
}
\]

The split is exact and uses no additive energy assumption.

---

## 5. Vorticity interpretation of scale descent

Natural vorticity scaling gives

\[
r\sim |\omega|^{-1/2}.
\]

Hence the child-to-parent characteristic vorticity ratio associated with the natural scales is

\[
\frac{W_{m+1}}{W_m}
\sim
\ell_m^{-2}.
\]

On an SD event,

\[
\ell_m^{-2}\ge K_m,
\]

so schematically

\[
\boxed{
\frac{W_{m+1}}{W_m}
\gtrsim K_m.
}
\]

Thus the apparently 'remote' event is, in this subcase, actually a strong local amplitude/scale escalation relative to the parent normalization.

This is naturally adjacent to the Type-II / high-frequency side of the root menu.

No contradiction is claimed: an infinite small-scale cascade is precisely one of the mechanisms that a singularity proof must exclude or classify.

---

## 6. Geometric interpretation of spatial export

On an SE event,

\[
|x_{m+1}-x_m|
\ge K_m^{1/2}r_m.
\]

Thus the next active object leaves every fixed multiple of the parent natural core as `K_m->infinity`.

This is a genuine spatial genealogy/export event rather than merely a finer structure inside the same core.

However it does not automatically produce additive energy:

- the child scale may be large or small;
- successive export directions may vary;
- physical packets need not be simultaneously alive;
- distant generations need not be pairwise disjoint.

Therefore no packing contradiction is yet valid.

---

## 7. Infinite-chain pigeonhole

For an infinite iterated chain with strong remoteness parameters along infinitely many generations, at least one of the two event types occurs infinitely often:

\[
\boxed{
\text{infinitely many SD events}
\quad\lor\quad
\text{infinitely many SE events}.
}
\]

Possibly both occur infinitely often.

This gives the first non-overcounted recursive classification of the remote cascade.

---

## 8. Consequence of infinitely many strong SD events

Along SD indices `m_j`,

\[
r_{m_j+1}
\le
K_{m_j}^{-1/2}r_{m_j}.
\]

If the corresponding `K_{m_j}` tend to infinity, then the local scale ratio has arbitrarily strong contractions.

This suggests a genuine micro-scale/Type-II cascade.

But one must not yet multiply only the SD factors while ignoring intervening generations whose `ell_m` may be greater than one.

Therefore the valid conclusion is only:

\[
\boxed{
\text{arbitrarily strong one-step scale descent occurs infinitely often}.
}
\]

A monotone global scale descent requires an additional control on the intervening expansion factors.

---

## 9. Consequence of infinitely many strong SE events

Along SE indices,

\[
\frac{|x_{m+1}-x_m|}{r_m}
\to\infty
\]

at least along a strong subsequence.

Thus any attempt to keep the entire chain inside one fixed parent-scale compact core fails on those generations.

Again this is not yet an additive-resource contradiction.

The next required bridge is a **material/time overlap or common-parent localization theorem** showing that sufficiently many exported active objects coexist or consume a finite parent resource.

Without that bridge, spatial export is classification rather than closure.

---

## 10. Updated remote-cascade frontier

M18-046 wrote the unresolved remote root as an opaque iterated cascade.

The present module refines it to

\[
\boxed{
\mathcal R_{cascade}
\Longrightarrow
\mathcal R_{SD}
\lor
\mathcal R_{SE},
}
\]

where

\[
\boxed{
\mathcal R_{SD}
=
\text{recurrent strong scale descent / amplitude escalation},
}
\]

and

\[
\boxed{
\mathcal R_{SE}
=
\text{recurrent strong spatial export}.
}
\]

These are structurally different and should be audited with different resources.

---

## 11. Highest-value next calculations

### For SD

Compare the scale-descent events with

- the first-hitting amplitude tower;
- Type-II remaining-time amplification;
- source-scale Euler normalization;
- derivative ancestry.

The main question is whether recurrent SD can be embedded into the already existing Type-II root rather than retained separately.

### For SE

Construct a common-parent spacetime representation and ask whether strong exports force

- bounded-overlap multiple active packets;
- material flux through expanding surfaces;
- kinetic-energy or palinstrophy transport;
- or a realization/export T branch.

A simple spatial sum is forbidden until coexistence is proved.

---

## 12. Status

\[
\boxed{
K_m\to\infty
\Longrightarrow
\ell_m\le K_m^{-1/2}
\lor
D_m\ge K_m^{1/2}.
}
\]

\[
\boxed{
\text{ITERATED REMOTE CASCADE}
\to
\text{SCALE DESCENT}
\lor
\text{SPATIAL EXPORT}.
}
\]

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
