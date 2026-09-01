# DSD M5-494 — Recurrent dual-pair palinstrophy forces a quantitative critical-enstrophy threshold

Date: 2026-09-01

Status: **QUANTITATIVE CLOSURE GATE / CALDERON--ZYGMUND AND SOBOLEV INTERPOLATION GIVE THE SCALE-CRITICAL PRODUCTION BOUND `|Q| <= C E^(3/4) P^(3/4)` IN BACKWARD SIMILARITY VARIABLES / ON A COMPACT HULL WITH UNIFORM ENSTROPHY CAP `E <= Z_*`, INVARIANT AVERAGING AND THE EXACT M5-486 BALANCE FORCE `mean(P) <= C^4 Z_*^3` / M5-493 SUPPLIES `mean(P) >= p_mean > 0`, SO EVERY RECURRENT PERSISTENT DUAL-PAIR SURVIVOR MUST SATISFY A FIXED LOWER CRITICAL-ENSTROPHY THRESHOLD `Z_* >= c p_mean^(1/3)` / THE SMALL-ENSTROPHY COMPACT HULL IS THEREFORE CLOSED, WHILE A QUANTITATIVELY LARGE BUT BOUNDED CRITICAL-ENSTROPHY HULL REMAINS / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Similarity quantities

Use the M5-486 notation

\[
E(\theta):=\|W(\theta)\|_2^2,
\]

\[
P(\theta):=\|\nabla W(\theta)\|_2^2,
\]

and

\[
Q(\theta)
:=
\int W\cdot\Sigma W\,dy.
\]

The exact similarity-enstrophy identity is

\[
\boxed{
\frac12E'
+
\frac14E
+
P
=
Q.
}
\]

On the compact bounded-enstrophy corridor assume

\[
\boxed{
E(\theta)\le Z_*
}
\]

uniformly on the invariant suspension hull.

M5-493 gives

\[
\boxed{
\langle P\rangle
\ge p_{mean}>0.
}
\]

---

## 2. Calderon--Zygmund control of strain

In the whole-space divergence-free setting, the strain is a matrix of zero-order singular integral transforms of vorticity.

Hence for `1<p<infinity`,

\[
\|\Sigma\|_p
\le C_p\|W\|_p.
\]

In particular,

\[
\boxed{
\|\Sigma\|_3
\le C_{CZ}\|W\|_3.
}
\]

Therefore

\[
\begin{aligned}
|Q|
&=
\left|\int W\cdot\Sigma W\,dy\right|\\
&\le
\|\Sigma\|_3
\|W\|_3^2\\
&\le
C_{CZ}\|W\|_3^3.
\end{aligned}
\]

---

## 3. Critical interpolation

Interpolate between `L2` and `L6`:

\[
\|W\|_3
\le
\|W\|_2^{1/2}
\|W\|_6^{1/2}.
\]

Sobolev gives

\[
\|W\|_6
\le C_S\|\nabla W\|_2.
\]

Thus

\[
\begin{aligned}
\|W\|_3^3
&\le
C
\|W\|_2^{3/2}
\|\nabla W\|_2^{3/2}\\
&=
C E^{3/4}P^{3/4}.
\end{aligned}
\]

Consequently

\[
\boxed{
|Q|
\le
C_*E^{3/4}P^{3/4}.
}
\]

This estimate is exactly scale critical in three dimensions.

---

## 4. Insert the enstrophy cap

Since

\[
E\le Z_*,
\]

one has pointwise in similarity time

\[
\boxed{
Q
\le
|Q|
\le
C_*Z_*^{3/4}P^{3/4}.
}
\]

Average over the invariant suspension measure.

By concavity of `x^(3/4)`,

\[
\langle P^{3/4}\rangle
\le
\langle P\rangle^{3/4}.
\]

Hence

\[
\boxed{
\langle Q\rangle
\le
C_*Z_*^{3/4}
\langle P\rangle^{3/4}.
}
\]

---

## 5. Exact averaged balance

Invariance gives

\[
\langle E'\rangle=0.
\]

Therefore M5-486 yields

\[
\boxed{
\frac14\langle E\rangle
+
\langle P\rangle
=
\langle Q\rangle.
}
\]

Combining with Section 4,

\[
\boxed{
\frac14\langle E\rangle
+
\langle P\rangle
\le
C_*Z_*^{3/4}
\langle P\rangle^{3/4}.
}
\]

---

## 6. Universal upper bound on mean palinstrophy

Drop the nonnegative enstrophy term.

If

\[
A:=\langle P\rangle>0,
\]

then

\[
A
\le
C_*Z_*^{3/4}A^{3/4}.
\]

Thus

\[
A^{1/4}
\le
C_*Z_*^{3/4},
\]

and hence

\[
\boxed{
\langle P\rangle
\le
C_*^4Z_*^3.
}
\]

This is an invariant critical production-capacity bound.

---

## 7. Dual-pair lower charge gives a minimum enstrophy threshold

M5-493 gives

\[
\langle P\rangle
\ge p_{mean}>0.
\]

Therefore

\[
p_{mean}
\le
C_*^4Z_*^3.
\]

Equivalently,

\[
\boxed{
Z_*
\ge
Z_{min}^{dual}
:=
C_*^{-4/3}p_{mean}^{1/3}>0.
}
\]

Thus a recurrent persistent noncollinear dual-pair similarity hull cannot live in an arbitrarily small critical-enstrophy class.

---

## 8. Small-enstrophy closure gate

If an extracted bounded lane satisfies the stronger quantitative cap

\[
Z_*<Z_{min}^{dual},
\]

then M5-493 and M5-494 are incompatible.

Hence

\[
\boxed{
Z_*<Z_{min}^{dual}
\Longrightarrow
\text{no recurrent compact dual-pair hull}.
}
\]

The compact lane is therefore reduced to

\[
\boxed{
Z_*
\ge Z_{min}^{dual}.
}
\]

This is a genuine closure of a subbranch, not a proof of global regularity.

---

## 9. Additional bound for mean enstrophy

The full inequality also controls `mean(E)`.

For fixed `Z_*`, maximize

\[
f(A)
=
C_*Z_*^{3/4}A^{3/4}-A
\]

over `A>=0`.

The maximum occurs at

\[
A^{1/4}
=
\frac34C_*Z_*^{3/4}.
\]

Thus

\[
\max f
=
\frac{27}{256}C_*^4Z_*^3.
\]

Since

\[
\frac14\langle E\rangle
\le f(A),
\]

we obtain

\[
\boxed{
\langle E\rangle
\le
\frac{27}{64}C_*^4Z_*^3.
}
\]

This is mainly a consistency bound; the more useful new conclusion is the lower threshold in Section 7.

---

## 10. DSD capacity interpretation

The recurrent dual geometry demands a fixed average palinstrophy resource.

The only source in the similarity-enstrophy ledger is axial stretching production `Q`.

But Calderon--Zygmund plus Sobolev show that a state with critical enstrophy cap `Z_*` has only

\[
O(Z_*^{3/4}P^{3/4})
\]

instantaneous production capacity.

Therefore a positive recurrent geometric palinstrophy demand cannot be supported below a fixed critical mass threshold.

In DSD terms:

\[
\boxed{
\text{dual structural demand}
\le
\text{critical production capacity}
}
\]

becomes the quantitative compatibility condition

\[
Z_*
\ge Z_{min}^{dual}.
\]

---

## 11. Why this does not yet close the large bounded lane

The original bounded corridor assumes only

\[
Z_*<\infty,
\]

not that `Z_*` is universally small.

Therefore a hull with

\[
Z_*\gg Z_{min}^{dual}
\]

can satisfy the present capacity inequality.

It would have to maintain substantial critical enstrophy while repeatedly paying the M5-492 bridge/separator palinstrophy cost.

This is narrower than M5-491 but remains a genuine hard endpoint.

---

## 12. Highest-value next target

The estimate

\[
|Q|
\le C E^{3/4}P^{3/4}
\]

ignores the **direction distribution** of the persistent dual pair.

It treats the vorticity as though all of its mass could align optimally with the stretching strain.

But M5-490--492 force two noncollinear active flux populations and either active direction variation or an active-set separator.

The next target is therefore an orientation-depleted production bound of the schematic form

\[
\boxed{
Q
\le
(C_* - \delta_{dual})
E^{3/4}P^{3/4}
+
\text{controlled exterior/tail term}
}
\]

on recurrent dual events.

A fixed depletion `delta_dual>0` would raise `Z_min^dual`. If the depletion can be made proportional to the same dual-pair geometric charge, it may produce a closed feedback inequality rather than merely a threshold.

---

## 13. Status

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
