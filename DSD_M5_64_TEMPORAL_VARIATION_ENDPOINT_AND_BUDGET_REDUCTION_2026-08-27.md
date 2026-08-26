# DSD M5-64 — Temporal-Variation Endpoint and Budget Reduction

Date: 2026-08-27

Status: **EXACT TEMPORAL-EXPONENT CLASSIFICATION / FOR THE COVARIANT MOLLIFIED ENTROPY VELOCITY `X`, THE EVENT ACTION `int |X|^q dt` HAS SCALING EXPONENT `q-2` / `q=2` IS THE UNIQUE SCALE-CRITICAL TEMPORAL ENDPOINT / LOWER POWERS ARE GEOMETRICALLY SUMMABLE ON THE ZENO LADDER AND HIGHER POWERS DIVERGE WITHOUT A KNOWN FINITE BUDGET / THE CLOSURE QUESTION IS REDUCED TO AN `L_t^2` ENDPOINT ESTIMATE / GLOBAL REGULARITY UNPROVED.**

## 1. Scaling input from M5-63

For the covariantly transported amplitude band,

\[
X_\Lambda(t)
=
\Lambda X(\Lambda^2t).
\]

A recurrent event interval scales as

\[
I_\Lambda=\Lambda^{-2}I.
\]

For `q>0`, define

\[
\boxed{
\mathcal A_q[I]
:=
\int_I|X(t)|^qdt.
}
\]

---

## 2. Exact scaling exponent

Using `s=Lambda^2 t`,

\[
\begin{aligned}
\mathcal A_{q,\Lambda}[I_\Lambda]
&=
\int_{I_\Lambda}
|\Lambda X(\Lambda^2t)|^qdt\\
&=
\Lambda^{q-2}
\int_I|X(s)|^qds.
\end{aligned}
\]

Therefore

\[
\boxed{
\mathcal A_{q,\Lambda}
=
\Lambda^{q-2}\mathcal A_q.
}
\]

In the M5-61 event-budget notation,

\[
\boxed{
\gamma(q)=q-2.
}
\]

---

## 3. Subcritical temporal variation: `0<q<2`

If

\[
0<q<2,
\]

then

\[
\gamma(q)<0.
\]

On the geometrically separated recurrent ladder `Lambda_n`,

\[
\mathcal A_q(I_n)
\asymp
\Lambda_n^{q-2}.
\]

Hence

\[
\boxed{
\sum_n\mathcal A_q(I_n)<\infty.
}
\]

Thus even a finite global `L_t^q` control with `q<2` would be compatible with infinitely many recurrent terminal pump copies.

A particularly instructive case is `q=1`:

\[
\int_{I_\Lambda}|X_\Lambda|dt
=
\Lambda^{-1}
\int_I|X|dt.
\]

So the physical total variation of the subcritical threshold entropy per copy shrinks like the physical radius.

This explains why the upstroke/downstroke variation itself does not contradict a Zeno accumulation.

---

## 4. Critical temporal variation: `q=2`

At

\[
q=2,
\]

we obtain

\[
\boxed{
\gamma(2)=0.
}
\]

Thus

\[
\boxed{
\mathcal A_2(I_n)
\ge a_*>0
}
\]

on every robust recurrent pump copy, as already established in M5-62/M5-63.

The Zeno sum is therefore nonsummable:

\[
\sum_n\mathcal A_2(I_n)=\infty.
\]

Consequently an independent finite bound of the form

\[
\boxed{
\sum_n
\int_{I_n}|X_{w_{\Lambda_n}}|^2dt
\le C(u_0,\nu)<\infty
}
\]

would immediately rule out the recurrent survivor.

This makes `L_t^2` the exact temporal endpoint for the accumulation route.

---

## 5. Supercritical temporal variation: `q>2`

For

\[
q>2,
\]

we have

\[
\gamma(q)>0.
\]

The per-copy lower action grows with scale:

\[
\mathcal A_q(I_n)
\gtrsim
\Lambda_n^{q-2}.
\]

This is a stronger divergence but, as M5-60/M5-61 emphasized, it is not automatically a stronger contradiction.

A hypothetical singularity is allowed to make supercritical quantities diverge unless a separate finite estimate forbids it.

Thus the proof search gains no advantage by moving to `q>2` unless such an estimate is independently available.

---

## 6. Endpoint reduction through the pressure/dissipation ledger

Recall

\[
X
=
\bar J_w-
u\bar D_w.
\]

M5-56 gives

\[
|\bar J_w|^2
\le
\bar S_w(\bar D_w-\bar A_w)
\le
\bar S_w\bar D_w.
\]

Therefore

\[
\begin{aligned}
X^2
&\le
2\bar J_w^2
+2\nu^2\bar D_w^2\\
&\le
2\bar S_w\bar D_w
+2\nu^2\bar D_w^2.
\end{aligned}
\]

Hence

\[
\boxed{
X^2
\le
2\bar D_w
\bigl(\bar S_w+\nu^2\bar D_w\bigr).
}
\]

A finite endpoint budget for either side would follow, for example, from simultaneous control of

\[
\int\bar S_w\bar D_w\,dt
\]

and

\[
\int\bar D_w^2dt
\]

on the scale-covariant disjoint pump family.

---

## 7. These upper-control terms are themselves critical

M5-63 gives instantaneous scaling

\[
\bar S_\Lambda
=
\Lambda\bar S,
\qquad
\bar D_\Lambda
=
\Lambda\bar D.
\]

Therefore

\[
\bar S_\Lambda\bar D_\Lambda
=
\Lambda^2\bar S\bar D,
\]

and

\[
\bar D_\Lambda^2
=
\Lambda^2\bar D^2.
\]

After multiplication by the event duration `Lambda^{-2}`, both spacetime integrals are exactly scale-invariant.

Thus the upper-bound reduction does not secretly move the problem into a subcritical classical budget. It remains at the same endpoint.

---

## 8. Why the ordinary energy inequality is one power short

The Leray energy inequality controls

\[
\int_0^{T_*}\int|\nabla u|^2dxdt<\infty.
\]

On each recurrent physical copy this ordinary spacetime enstrophy scales as

\[
\Lambda^{-1}.
\]

By contrast, the endpoint quantities

\[
\int X^2dt,
\qquad
\int\bar D_w^2dt,
\qquad
\int\bar S_w\bar D_wdt
\]

all have event exponent zero.

Therefore the basic energy estimate is precisely one scaling power too weak to dominate the recurrent endpoint action by dimensional bookkeeping alone.

Any successful estimate must exploit additional structure rather than Hölder/interpolation that merely preserves the known energy scaling.

---

## 9. DSD audit

### GREEN

`q=2` is the unique temporal power for which the recurrent per-event action is order one.

### RED

`q<2` cannot close the Zeno ladder by accumulation because the event lower bounds are summable.

### RED

`q>2` divergence is not forbidden without an independent supercritical bound.

### GREEN

The endpoint problem can be expressed entirely in the already localized pressure/dissipation variables `bar S_w` and `bar D_w`.

### YELLOW

No finite `L_t^2` scale-covariant budget has yet been derived from the smooth finite-energy hypotheses.

---

## 10. Sharpened branch choice

The accumulation route now has exactly one viable exponent:

\[
\boxed{q=2.}
\]

Therefore further accumulation work should focus only on whether the pressure-Poisson/Hodge structure yields an endpoint estimate for

\[
X\in L_t^2
\]

along the covariant threshold family.

In parallel, M5-51 suggests the direct-rigidity route: because the order-one pressure payer is localized to the core plus finitely many adjacent logarithmic shells, one may attempt to exclude the recurrent pump loop without constructing a finite global endpoint budget.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
