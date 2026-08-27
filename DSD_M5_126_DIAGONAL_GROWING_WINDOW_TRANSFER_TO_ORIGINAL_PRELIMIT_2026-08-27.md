# DSD M5-126 — Diagonal Growing-Window Transfer to the Original Prelimit

Date: 2026-08-27

Status: **LOCAL W1 COMPACTNESS UPGRADED BY A PURE DIAGONAL ARGUMENT TO WINDOWS WHOSE NORMALIZED RADII DIVERGE WHILE THEIR PHYSICAL RADII STILL SHRINK TO THE SINGULAR CENTER / POSITIVE LOG-CYLINDER CUBIC DENSITY TRANSFERS TO THE ORIGINAL SAME-SOLUTION SNAPSHOTS AS DIVERGING `L3` MASS INSIDE VANISHING-ENERGY SHRINKING ANNULI / THIS IS A SHARP CONCENTRATION LAW BUT NOT A CONTRADICTION / GLOBAL REGULARITY UNPROVED.**

---

## 1. Prelimit sequence

Let `t_n up T_*` be the original finite-energy solution times used to extract the W1 state.

Write

\[
\ell_n:=\sqrt{T_*-t_n}\to0
\]

and normalized snapshots

\[
\boxed{
U_n(Y):=\ell_n\,u(x_*+\ell_nY,t_n).
}
\]

After the existing W1 compactness extraction,

\[
U_n\to V
\]

locally smoothly, hence strongly in local `L3`, on every fixed normalized ball.

No expanding-window convergence rate is assumed.

---

## 2. Diagonal growing-window lemma

Choose any deterministic sequence

\[
R_k\uparrow\infty
\]

as slowly as desired.

For each `k`, local convergence on `B_{2R_k}` gives an index `N_k` such that for all sufficiently late chosen indices,

\[
\|U_n-V\|_{L^3(B_{2R_k})}\le k^{-1}.
\]

Because `ell_n->0`, we may increase the same index further so that

\[
\ell_nR_k\le k^{-1}.
\]

Choose an increasing subsequence `n_k` satisfying both requirements and set

\[
\boxed{\mathcal R_k:=R_k.}
\]

Then

\[
\boxed{
\mathcal R_k\to\infty,
\qquad
\ell_{n_k}\mathcal R_k\to0,
}
\]

and

\[
\boxed{
\|U_{n_k}-V\|_{L^3(B_{2\mathcal R_k})}\to0.
}
\]

The same construction works in any fixed local topology supplied by the W1 compactness package, with the accuracy weakened as needed to accommodate the growing ball.

This is a standard diagonal consequence of local compactness; it is strictly weaker than the old fixed-physical-radius EWG.

---

## 3. Formation audit

The growing window does not create a new global W1 approximation.

Its physical radius is

\[
\boxed{
r_k:=\ell_{n_k}\mathcal R_k\to0.
}
\]

Thus it remains inside a shrinking neighborhood of the singular center.

The statement is only:

\[
\boxed{
\text{arbitrarily large normalized log depth}
\quad\text{can be transferred inside an arbitrarily small physical neighborhood.}
}
\]

It does not transfer the W1 tail to one fixed macroscopic physical radius.

---

## 4. Transfer of the cubic log-depth

Fix one sufficiently large normalized inner radius `R_*`.

By M5-118, on a positive-residue ergodic W1 state,

\[
\int_{R_*<|Y|<R}|V(Y)|^3dY
\]

has positive mean growth proportional to `log R` along arbitrarily large radii; for a generic tail trajectory,

\[
\boxed{
\int_{R_*<|Y|<R}|V|^3dY
=\mathscr R_3\log R+o(\log R)
}
\]

up to the harmless fixed choice of radial origin/normalization implicit in the log-cylinder slice density.

Choose the diagonal radii along such a generic subsequence.

Strong `L3` convergence on `B_{2R_k}` then gives

\[
\boxed{
\int_{R_*<|Y|<R_k}|U_{n_k}|^3dY
\to\infty.
}
\]

More quantitatively, after subsequence selection,

\[
\boxed{
\int_{R_*<|Y|<R_k}|U_{n_k}|^3dY
\ge c\log R_k
}
\]

for some `c>0` determined by the positive log-cylinder cubic density.

---

## 5. Translate back to the original solution

The Navier--Stokes `L3` norm is scale invariant.

The normalized annulus

\[
R_*<|Y|<R_k
\]

corresponds to the physical annulus

\[
\boxed{
\ell_{n_k}R_*
<|x-x_*|<
ell_{n_k}R_k.
}
\]

Both radii tend to zero, while their ratio tends to infinity.

Therefore the original same solution obeys

\[
\boxed{
\int_{\ell_{n_k}R_*<|x-x_*|<\ell_{n_k}R_k}
|u(x,t_{n_k})|^3dx
\ge c\log R_k\to\infty.
}
\]

Thus W1 positive residue forces arbitrarily deep critical cubic concentration in shrinking physical annuli of the original solution.

This no longer concerns only the abstract W1 limit.

---

## 6. Ordinary energy on the same annuli vanishes

The Type-I W1 envelope gives on the normalized tail

\[
|U_n(Y)|\lesssim |Y|^{-1}
\]

on the transferred corridor after choosing the diagonal accuracy sufficiently well.

Hence

\[
\int_{R_*<|Y|<R_k}|U_{n_k}|^2dY
\lesssim R_k.
\]

Physical `L2` scales by one factor `ell_n`:

\[
\int |u|^2dx
=\ell_n
\int|U_n|^2dY.
\]

Therefore on the same annulus,

\[
\boxed{
\int_{\ell_{n_k}R_*<|x-x_*|<\ell_{n_k}R_k}
|u(x,t_{n_k})|^2dx
\lesssim
\ell_{n_k}R_k
\to0.
}
\]

The W1 critical survivor consequently has the simultaneous same-solution signature

\[
\boxed{
L^2\text{ energy}\to0,
\qquad
L^3\text{ mass}\to\infty
}
\]

on one sequence of shrinking annuli.

---

## 7. This is not a contradiction

The behavior is compatible with the model critical profile `1/r`.

The `L2` density is subcritical and concentrates too weakly to survive the shrinking physical radius, while the `L3` density counts logarithmic scale depth and therefore diverges.

Thus one must not infer

\[
L^2\to0\Rightarrow L^3\to0.
\]

That would require a uniform amplitude or stronger interpolation input that fails precisely at the critical blow-up scale.

Likewise the ordinary energy inequality does not control this logarithmically divergent cubic concentration.

---

## 8. Relation to the strong EWG

The earlier expanding-window gate asked for convergence up to normalized radius

\[
R_n\asymp\ell_n^{-1},
\]

which corresponds to one fixed physical radius.

The present diagonal gate needs only

\[
\boxed{
1\ll R_n\ll\ell_n^{-1}.
}
\]

It is therefore provable from local compactness alone.

But because the physical outer radius still tends to zero, finite global energy remains compatible with the transferred tail.

Hence the strong EWG is not required to realize arbitrarily long log genealogy, but it would still be required to compare that genealogy directly with one fixed macroscopic physical shell or global terminal trace.

---

## 9. DSD four-chain audit

### Formation — GREEN

The growing window is selected from actual local convergence and remains inside a shrinking physical neighborhood.

### Axis — GREEN

Normalized radius growth and physical radius shrinkage are recorded separately.

### Static aggregation — GREEN

`L2` and `L3` are not mixed: their different scaling exponents are kept explicit.

### Dynamics — GREEN

The result uses one same-solution sequence `t_n` and one W1 limit snapshot.  No independent-copy summation is used.

### Cross-audit — GREEN

The diagonal lemma is derived from upstream local compactness only; the resulting cubic divergence is not fed back to justify W1 compactness.

---

## 10. New frontier

The W1 anomaly now has an original-solution manifestation:

\[
\boxed{
\text{vanishing local energy}
+\text{diverging critical cubic depth}
\text{ in shrinking annuli.}
}
\]

The next viable question is whether the **local energy inequality plus pressure transport** permits this specific two-scale behavior when the cubic mass is not arbitrary but is tied by M5-120/M5-121 to the same-trajectory pressure-overpay/tail-memory cocycle.

A useful next calculation is therefore a local-energy/pressure ledger on the diagonal annuli, with inner and outer moving boundaries chosen to match

\[
\ell_nR_*
\quad\text{and}\quad
\ell_nR_n.
\]

If every term remains compatible with the `1/r` model, that route must also be pruned rather than forced into a false contradiction.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
