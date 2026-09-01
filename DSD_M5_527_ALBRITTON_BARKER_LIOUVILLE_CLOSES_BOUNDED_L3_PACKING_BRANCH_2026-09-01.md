# DSD M5-527 — Albritton--Barker ancient Liouville theorem closes every backward-sequence bounded `L3` packing branch

Date: 2026-09-01

Status: **EXTERNAL LIOUVILLE CLOSURE OF ONE BRANCH / M5-526 SHOWS THAT `ell^(3/2)` PACKING OF THE SCALE-CRITICAL DIRICHLET SHELL COSTS IMPLIES VELOCITY `L3` CONTROL / ALBRITTON--BARKER (J. MATH. FLUID MECH. 21:43, 2019, THEOREM 1.2) PROVE THAT A MILD ANCIENT NAVIER--STOKES SOLUTION WHICH IS BOUNDED IN `L3` ALONG ANY SEQUENCE OF TIMES TENDING TO BACKWARD INFINITY MUST BE IDENTICALLY ZERO / THE M5-478 SECOND-GENERATION ANCIENT CELL IS NONTRIVIAL AND, ON THE M5-526 `L3` BRANCH, BELONGS TO THE STANDARD MILD `L3` CLASS / THEREFORE NO BACKWARD SEQUENCE CAN HAVE UNIFORMLY BOUNDED `ell^(3/2)` DIRICHLET PACKING / A SURVIVING NONTRIVIAL CELL MUST HAVE `||V(t)||_3 -> infinity` AS `t -> -infinity`, AND M5-526 THEN FORCES THE DYADIC CRITICAL DIRICHLET PACKING SUM TO DIVERGE TOWARD BACKWARD INFINITY / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. External theorem

Use the published result:

Dallas Albritton and Tobias Barker,
`On Local Type I Singularities of the Navier--Stokes Equations and Liouville Theorems`,
Journal of Mathematical Fluid Mechanics 21 (2019), Article 43,
DOI `10.1007/s00021-019-0448-z`,
Theorem 1.2.

Their theorem states:

If `v` is a mild ancient Navier--Stokes solution and there exists a sequence

\[
t_j\downarrow-\infty
\]

such that

\[
\boxed{
\sup_j\|v(\cdot,t_j)\|_{L^3(\mathbb R^3)}<\infty,
}
\]

then

\[
\boxed{v\equiv0.}
\]

This theorem is substantially stronger for the present purpose than merely applying endpoint regularity at one terminal singular time: the terminal value need not be assumed to vanish.

---

## 2. The M5-478 nontrivial ancient cell

M5-478 constructs a smooth ancient Navier--Stokes solution

\[
(\mathcal V,\mathcal P)
\]

on

\[
\mathbb R^3\times(-\infty,0)
\]

with

\[
\boxed{
\int_{B_{\rho_0}(y_*)}
|\mathcal\Omega(y,-1)|^2dy
\ge c_0>0.
}
\]

Hence

\[
\boxed{\mathcal V\not\equiv0.}
\]

It also satisfies the Type-I slice estimates

\[
\|\mathcal V(s)\|_\infty
\le C|s|^{-1/2},
\]

\[
\|\mathcal V(s)\|_6
\le C|s|^{-1/4},
\]

and finite enstrophy on every negative slice.

---

## 3. Similarity variables preserve `L3`

Write

\[
a=-s,
\qquad
\theta=-\log a,
\]

and

\[
U(y,\theta)
=
\sqrt a\,
\mathcal V(\sqrt a\,y,-a).
\]

The `L3` norm is exactly scale invariant:

\[
\begin{aligned}
\|U(\theta)\|_3^3
&=
\int a^{3/2}
|\mathcal V(\sqrt a y,-a)|^3dy\\
&=
\int
|\mathcal V(x,-a)|^3dx.
\end{aligned}
\]

Therefore

\[
\boxed{
\|U(\theta)\|_3
=
\|\mathcal V(-e^{-\theta})\|_3.
}
\]

Backward physical infinity

\[
s\to-\infty
\]

corresponds to

\[
\theta\to-\infty.
\]

---

## 4. Mildness audit on the `L3` branch

Albritton--Barker requires a **mild ancient solution**, not merely a distributional ancient solution.

This hypothesis must be checked.

On the M5-526 packing branch, at every sampled time under consideration,

\[
\mathcal V(s)\in L^3(\mathbb R^3).
\]

The M5-478 cell is already smooth for every `s<0` and obeys the whole-space Navier--Stokes equations with the Galilean/parasitic mode fixed by its spatial integrability and Biot--Savart normalization.

Starting from any sampled negative time `s_0`, standard local well-posedness/mild-solution theory for `L3` initial data produces the Duhamel solution on a forward interval.

Weak--strong/classical uniqueness identifies it with the existing smooth M5-478 cell on the overlap.

Iterating over compact negative-time intervals gives the standard mild representation required by the Albritton--Barker theorem.

Thus on the `L3` packing subbranch,

\[
\boxed{
\mathcal V
\text{ is in the mild ancient class used by Theorem 1.2.}
}
\]

Firewall: this conclusion is invoked only after `L3` integrability is established; smoothness alone is not silently equated with the global mild ancient class.

---

## 5. Backward-sequence packing bound is impossible

For each similarity time `theta`, let

\[
b_k(\theta)
=
R_k
\int_{A_k^*}|\nabla U(y,\theta)|^2dy
\]

as in M5-526.

Suppose there exists a sequence

\[
\theta_j\to-\infty
\]

such that

\[
\boxed{
\sup_j
\sum_{k=0}^\infty
b_k(\theta_j)^{3/2}
<\infty.
}
\]

M5-526 yields

\[
\sup_j
\|U(\theta_j)\|_3
<\infty.
\]

Set

\[
s_j=-e^{-\theta_j}.
\]

Then

\[
s_j\to-\infty
\]

and scale invariance gives

\[
\sup_j
\|\mathcal V(s_j)\|_3
<\infty.
\]

Albritton--Barker Theorem 1.2 therefore gives

\[
\mathcal V\equiv0,
\]

contradicting the M5-478 carrier.

Hence

\[
\boxed{
\text{no backward sequence can have uniformly bounded }
\ell^{3/2}\text{ Dirichlet packing.}
}
\]

---

## 6. `L3` must diverge toward backward infinity

The Albritton--Barker theorem immediately implies a stronger scalar statement.

If

\[
\|\mathcal V(s)\|_3
\not\to\infty
\quad\text{as }s\to-\infty,
\]

then there would exist a constant `M<infinity` and a sequence

\[
s_j\to-\infty
\]

with

\[
\|\mathcal V(s_j)\|_3\le M.
\]

That is forbidden by Theorem 1.2 for the nontrivial cell.

Therefore

\[
\boxed{
\|\mathcal V(s)\|_3
\longrightarrow\infty
\qquad(s\to-\infty).
}
\]

Equivalently,

\[
\boxed{
\|U(\theta)\|_3
\longrightarrow\infty
\qquad(\theta\to-\infty).
}
\]

This is compatible with the compactness of the vorticity hull because velocity `L3` is a low-frequency weighted-tail quantity not controlled by the unweighted positive-Sobolev compactness of `W`.

---

## 7. Packing sum must diverge toward backward infinity

M5-526 gives

\[
\|U(\theta)\|_3^3
\le
C_{int}
+
C
\sum_kb_k(\theta)^{3/2},
\]

where `C_int` is the uniformly bounded contribution of the fixed interior ball.

Since

\[
\|U(\theta)\|_3\to\infty
\]

as `theta->-infinity`, necessarily

\[
\boxed{
\sum_kb_k(\theta)^{3/2}
\longrightarrow\infty
\qquad(\theta\to-\infty).
}
\]

Thus the surviving compact hard core is forced into an increasingly severe **critical Dirichlet packing defect** toward backward similarity time.

---

## 8. Why this does not contradict global `H1` compactness

At first sight the conclusion may appear inconsistent with M5-508 global smooth compactness.

It is not.

Global `H1` compactness controls the unweighted Dirichlet tail

\[
\int_{|y|>R}|\nabla U|^2dy
\]

uniformly.

But the shell packing uses the critical weight

\[
b_k
=R_kE_k.
\]

A packet at radius `R_k` with energy

\[
E_k\asymp R_k^{-1}
\]

has vanishing unweighted `H1` mass as `R_k->infinity` while retaining order-one critical cost `b_k`.

Therefore arbitrarily remote critically weighted shells can disappear in strong unweighted `H1` topology while making the `ell^(3/2)` packing sum diverge.

This is a weighted concentration-compactness defect, not a failure of M5-508.

---

## 9. Exact surviving low-frequency endpoint

M5-526--527 replace the former split

\[
\mathcal P_{Dir}^{3/2}
\lor
H_{Dir}^{nonsum}
\]

by a one-sided necessity for the nontrivial ancient cell:

\[
\boxed{
E_{ancient}^{nontrivial}
\Longrightarrow
H_{Dir}^{packing\uparrow},
}
\]

where

\[
\boxed{
H_{Dir}^{packing\uparrow}:
\quad
\sum_kb_k(\theta)^{3/2}
\to\infty
\text{ as }\theta\to-\infty.
}
\]

Thus the bounded-packing alternative is closed by an external Liouville theorem.

---

## 10. Relation to exact DSS and recurrence

For an exact similarity-periodic/DSS orbit, every scale-invariant state observable repeats periodically in `theta`.

If the Dirichlet packing sum were finite at one periodic phase, periodicity would produce a bounded backward sequence and M5-527 would force the ancient cell to vanish.

Therefore a nontrivial exact DSS survivor, if it exists in the present weak tail class, must have

\[
\boxed{
\sum_kb_k(\theta)^{3/2}=\infty
}

at every periodic phase where the quantity is defined.

This is consistent with the known open status of general backward DSS: such solutions may lie outside `L3` precisely through critical nonsummable spatial tails.

---

## 11. External-dependency firewall

The closure uses only the published Albritton--Barker Theorem 1.2 and standard `L3` mild uniqueness to verify its class.

It does **not** use unverified manuscripts claiming full 3D Navier--Stokes global regularity.

It also does not assert that Escauriaza--Seregin--Sverak endpoint regularity alone makes the ancient solution zero; the direct ancient Liouville theorem is the relevant result here.

---

## 12. Highest-value next target

The hard core is now no longer

\[
\text{finite packing}
\lor
\text{infinite packing}.
\]

Only the second survives.

The next audit should classify how

\[
\sum_kb_k(\theta)^{3/2}\to\infty
\]

can occur while

\[
\sum_kE_k(\theta)<\infty
\]

and the vorticity/Dirichlet hull remains globally unweighted-compact.

There are two qualitatively distinct mechanisms:

1. **critical-shell recurrence:** order-one `b_k` on infinitely many farther shells;
2. **diffuse logarithmic packing:** `b_k->0` but `sum b_k^(3/2)=infinity`.

The M5-482--485 dilation genealogy should now be used to test whether the second diffuse mechanism is dynamically compatible with first-hitting scale ratios bounded away from one.

If dilation recurrence forces a fixed lower mark to recur at positive log-scale density, the diffuse branch collapses to a concrete critically occupied shell cascade.

---

## 13. Status

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
