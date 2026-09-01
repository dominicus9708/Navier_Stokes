# DSD M5-528 — Audit: the ancient dilation shift is a similarity-time translation, not an interior spatial-shell translation

Date: 2026-09-01

Status: **ANTI-CONFLATION AUDIT / THE M5-482 TERMINAL STATES SATISFY A PURE SPATIAL DILATION RELATION AT THE TERMINAL SLICE, BUT THE M5-483 COMPLETE ANCIENT CELLS SATISFY PARABOLIC DILATION / AFTER PASSING TO BACKWARD SIMILARITY VARIABLES, PARABOLIC DILATION BECOMES TRANSLATION IN SIMILARITY TIME, NOT TRANSLATION OF THE INTERIOR LOG-RADIUS SHELL INDEX / THEREFORE ONE CANNOT USE ERGODICITY OF THE M5-485 GENERATION SHIFT TO CLAIM THAT A NONZERO INTERIOR REMOTE-SHELL DIRICHLET OBSERVABLE MUST RECUR WITH POSITIVE LOG-RADIUS DENSITY / THE DIFFUSE NONSUMMABLE PACKING BRANCH FROM M5-527 CANNOT BE REMOVED BY THAT SHORTCUT / A SEPARATE SPACE-TIME BRIDGE BETWEEN INTERIOR WEIGHTED PACKING AND THE TERMINAL DILATION TAIL IS REQUIRED / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Terminal spatial dilation

M5-482 starts from terminal time-slice states

\[
U_m^{term}(y)
:=
R_mV(R_my,0).
\]

For consecutive record radii

\[
\lambda_m=R_{m+1}/R_m,
\]

the exact relation is

\[
\boxed{
U_{m+1}^{term}
=D_{\lambda_m}U_m^{term},
\qquad
(D_\lambda f)(y)=\lambda f(\lambda y).
}
\]

At the terminal slice this is a genuine spatial log-radius shift.

---

## 2. Ancient space-time dilation

M5-483 lifts the terminal states to complete ancient Navier--Stokes cells.

The parabolic dilation is

\[
\boxed{
(\mathscr D_\lambda\mathcal U)(y,s)
:=
\lambda\mathcal U(\lambda y,\lambda^2s).
}
\]

The complete genealogy satisfies

\[
\boxed{
\mathcal U_{n+1}
=
\mathscr D_{\lambda_n}\mathcal U_n.
}
\]

This relation carries both spatial and temporal scaling.

---

## 3. Convert each ancient cell to similarity variables

For `s<0`, set

\[
a=-s,
\qquad
\theta=-\log a,
\]

and define

\[
U_n(y,\theta)
:=
\sqrt a\,
\mathcal U_n(\sqrt a\,y,-a).
\]

Now use

\[
\mathcal U_{n+1}(x,s)
=
\lambda_n
\mathcal U_n(\lambda_nx,\lambda_n^2s).
\]

Then

\[
\begin{aligned}
U_{n+1}(y,\theta)
&=
\sqrt a\,\lambda_n
\mathcal U_n(\lambda_n\sqrt a\,y,-\lambda_n^2a).
\end{aligned}
\]

Set

\[
a'=\lambda_n^2a.
\]

Since

\[
\sqrt{a'}=\lambda_n\sqrt a
\]

and

\[
-\log a'
=
\theta-2\log\lambda_n,
\]

we obtain the exact identity

\[
\boxed{
U_{n+1}(y,\theta)
=
U_n\bigl(y,\theta-2\log\lambda_n\bigr).
}
\]

Thus in similarity coordinates the spatial argument `y` does **not** dilate.

The dilation genealogy becomes a time-phase translation.

---

## 4. Consequence for a fixed-annulus observable

Let

\[
G_R(U)
:=
R\int_{A_R}|\nabla U(y)|^2dy.
\]

For the similarity representatives,

\[
G_R(U_{n+1}(\theta))
=
G_R\left(U_n(\theta-2\log\lambda_n)\right).
\]

This is the same fixed spatial annulus observed at a shifted similarity time.

It is **not**

\[
G_{\lambda_nR}(U_n(\theta)).
\]

Therefore the generation shift `sigma` of M5-485 does not directly shift the interior radial shell index.

---

## 5. Why the tempting ergodic shortcut fails

A tempting argument after M5-527 would be:

1. define a nonnegative fixed-shell cost `g`;
2. identify `g(sigma^nY)` with the cost of farther and farther spatial shells;
3. use ergodicity to turn nonzero `g` into positive-density critically occupied remote shells.

Step 2 is false for interior similarity states.

The correct identity is time translation, not radial translation.

Hence Birkhoff recurrence of `g(sigma^nY)` proves recurrence of the fixed-annulus cost **in similarity time**, but not recurrence of the same cost across increasing spatial radii at one time.

Thus

\[
\boxed{
\text{similarity-time recurrence}
\not\Rightarrow
\text{positive-density spatial-shell recurrence}
}
\]

without another theorem.

---

## 6. Why the terminal slice is different

At terminal time

\[
s=0,
\]

the temporal factor in parabolic dilation disappears:

\[
\mathcal U_{n+1}(y,0)
=
\lambda_n\mathcal U_n(\lambda_n y,0).
\]

Therefore the terminal states do carry a genuine spatial dilation genealogy.

This is why M5-482 can convert the terminal critical Dirichlet tail into a complete log-radius hull.

The distinction is

\[
\boxed{
\begin{aligned}
&s<0:\quad
\text{parabolic dilation}
\leftrightarrow
\text{similarity-time translation},\\
&s=0:\quad
\text{parabolic dilation}
\leftrightarrow
\text{pure spatial dilation}.
\end{aligned}
}
\]

Any proof connecting M5-527 interior packing to M5-482 terminal shell recurrence must cross this terminal limit explicitly.

---

## 7. Opposite time ends must also be kept distinct

M5-527 forces

\[
\sum_kb_k(\theta)^{3/2}
\to\infty
\quad\text{as }\theta\to-\infty.
\]

Since

\[
s=-e^{-\theta},
\]

this is the ancient solution's **backward physical infinity**

\[
s\to-\infty.
\]

By contrast, the terminal dilation tail concerns

\[
s\to0^-,
\qquad
\theta\to+\infty.
\]

Thus the desired bridge is not merely a change of coordinates.

It must transport information from one temporal end of the complete ancient orbit to the other or use recurrence/invariance in a way valid for an extended weighted-tail observable.

---

## 8. What M5-485 ergodicity still gives

The M5-485 invariant shift remains highly useful for observables that genuinely live on one normalized stage/cell, such as

1. ratchet marks;
2. fixed-annulus local production;
3. persistent lineage marks;
4. dual-pair geometry;
5. bounded continuous similarity-phase observables.

It cannot by itself control the unbounded-radius tail sum

\[
\sum_kb_k^{3/2}
\]

because this is an extended weighted observable whose divergence can occur through shell index `k->infinity` while every fixed-shell observable remains compact.

---

## 9. Finite truncations clarify the remaining defect

Define

\[
F_N(U)
:=
\sum_{k=0}^{N}b_k(U)^{3/2}.
\]

For every fixed `N`, `F_N` depends on finitely many bounded annuli and is continuous under the global smooth compact topology.

M5-527 says the full quantity

\[
F(U):=\sup_NF_N(U)
\]

must diverge toward backward infinity.

There is no contradiction with compact recurrence because the index at which the additional packing appears may satisfy

\[
N=N(\theta)\to\infty.
\]

Thus every fixed truncation stays compact while the defect escapes to larger and larger radial indices.

This is precisely a **weighted shell-index escape**.

---

## 10. Updated survivor

M5-527--528 refine the low-frequency hard core to

\[
\boxed{
H_{Dir}^{packing\uparrow}
+
H_{index}^{radial\ escape}.
}
\]

That is:

- unweighted global Sobolev compactness remains intact;
- every fixed radial truncation remains compact;
- but the critical `ell^(3/2)` Dirichlet packing required to keep the ancient cell nontrivial escapes to arbitrarily large radial shell index toward backward infinity.

This is more specific than generic failure of `L3`.

---

## 11. Highest-value next target

The next calculation should derive a **local/moving-shell similarity enstrophy balance**.

The similarity enstrophy equation has an explicit dilation transport `y/2`.

If the observation radius is allowed to move by

\[
R'(\theta)=\frac12R(\theta),
\]

that linear dilation flux should cancel exactly.

A scale-critical moving-tail quantity of the form

\[
R(\theta)
\int_{|y|>R(\theta)}|W|^2dy
\]

may then satisfy a balance involving only

1. vortex-stretching production;
2. palinstrophy;
3. nonlinear velocity transport through the moving sphere;
4. diffusive boundary flux.

Such an identity would be the correct space-time bridge for the weighted shell-index escape, because it follows the natural similarity dilation characteristics rather than incorrectly identifying generation shift with radial shift.

---

## 12. Status

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
