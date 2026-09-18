# M19-417 — Minimality forces one fixed residual channel to recur syndetically on every hard-hull orbit

Date: 2026-09-19  
Canonical ID: **M19-417**  
Status: **MINIMAL-HULL CHANNEL UNIFORMIZATION / UNIFORM GLOBAL RESIDUAL GAP + FINITE WINDOW DETECTION + CONTINUITY FORCE ONE FIXED CELL/CHANNEL TO RECUR WITH BOUNDED LOG-RADIUS GAPS ON EVERY MINIMAL-HULL ORBIT / THIS REMOVES ARBITRARILY SPARSE CHANNEL SWITCHING BUT DOES NOT BY ITSELF BREAK CRITICAL SUMMABILITY / GLOBAL REGULARITY UNPROVED**

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Input

M19-413 gives a compact minimal terminal-tail hull \(\mathcal T\) with
\[
\boxed{
\mathbf F(T)
\ge
\varepsilon_{glob}>0
\qquad
\forall T\in\mathcal T.
}
\]

The finite-window reduction of M5-238 gives finitely many fixed normalized punctured cells
\[
K_1,\ldots,K_M
\]
and a threshold \(r_*>0\) such that every \(T\in\mathcal T\) has at least one cell with
\[
\boxed{
\|\mathcal R_T\|_{L^2(K_k)}
\ge
r_*.
}
\]

On each fixed cell decompose the residual into its spherical force/source mode and mean-free angular mode:
\[
\mathcal R
=
\mathcal R_0
+
\mathcal R_\perp.
\]

Orthogonality gives
\[
\|\mathcal R\|_2^2
=
\|\mathcal R_0\|_2^2
+
\|\mathcal R_\perp\|_2^2.
\]

Hence on every detected cell at least one channel has size
\[
\ge
r_*/\sqrt2.
\]

## 2. Build a finite open channel cover

Choose a slightly smaller threshold
\[
0<\rho_*<r_*/\sqrt2,
\]
for example
\[
\rho_*=r_*/2.
\]

For every cell \(K_k\), define
\[
U_{k,F}
=
\left\{
T\in\mathcal T:
\|\mathcal R_{0,T}\|_{L^2(K_k)}
>
\rho_*
\right\},
\]
and
\[
U_{k,A}
=
\left\{
T\in\mathcal T:
\|\mathcal R_{\perp,T}\|_{L^2(K_k)}
>
\rho_*
\right\}.
\]

Because the terminal hull is compact in a smooth punctured topology and the residual map is continuous on each fixed cell, these are open subsets of \(\mathcal T\).

The finite family
\[
\{U_{k,F},U_{k,A}:1\le k\le M\}
\]
covers \(\mathcal T\).

At least one member is nonempty.

Fix one nonempty member and denote it
\[
\boxed{
U_*.
}
\]

Its label is a fixed pair
\[
(k_*,\tau_*),
\qquad
\tau_*\in\{F,A\}.
\]

Thus \(U_*\) represents one fixed normalized cell and one fixed residual channel.

## 3. Minimality gives syndetic returns

M5-52 proves the standard compact-minimal-flow lemma:

for every nonempty open set \(U\subset\mathcal T\), return times to \(U\) are syndetic.

Therefore there exists
\[
\boxed{
L_*<\infty
}
\]
such that along every orbit \(T_q\) in the minimal hull, every sufficiently late interval
\[
[s,s+L_*]
\]
contains a log-shift time \(q\) with
\[
T_q\in U_*.
\]

Hence the same fixed cell/channel event recurs with uniformly bounded log-radius gaps on **every** minimal-hull orbit.

This is stronger than an almost-everywhere ergodic positive-density statement.

## 4. Two possible uniformized endpoints

Exactly one fixed selected type \(\tau_*\) is obtained.

### F-syndetic branch

If
\[
\tau_*=F,
\]
then there exists a fixed normalized cell \(K_{k_*}\) and fixed threshold \(\rho_*>0\) such that
\[
\boxed{
\|\mathcal R_0\|_{L^2(K_{k_*})}
>
\rho_*
}
\]
returns with bounded log gaps on every orbit.

By M19-415 this yields fixed-amplitude stress-flux excursions with bounded log gaps.

Thus the far-field stress-flux non-Cauchy defect is **syndetic**, not merely recurrent.

### A-syndetic branch

If
\[
\tau_*=A,
\]
then
\[
\boxed{
\|\mathcal R_\perp\|_{L^2(K_{k_*})}
>
\rho_*
}
\]
returns with bounded log gaps on every orbit.

By spherical Poincare,
\[
\boxed{
\|\nabla_{S^2}\mathcal R_\perp\|_2^2
\ge
2\rho_*^2
}
\]
on every such return.

Thus the angular residual activity is also syndetic.

## 5. Quantitative event count

Select disjoint return windows exactly as in M5-52.

If each robust channel event occupies a fixed normalized width \(w>0\), one can choose disjoint event windows whose centers satisfy
\[
2w
\le
q_{n+1}-q_n
\le
2w+L_*.
\]

Hence the number of selected channel events up to log radius length \(Q\) satisfies
\[
\boxed{
N(Q)
\ge
\frac{Q}{2w+L_*}
-O(1).
}
\]

Equivalently, across a physical scale ratio \(R=e^Q\),
\[
\boxed{
N(R)
\gtrsim
c_*\log R.
}
\]

Thus the selected channel has both upper critical order \(O(\log R)\) from radial slot counting and a matching positive lower order \(\Omega(\log R)\).

Its multiplicity is genuinely logarithmic.

## 6. Why syndeticity still does not close the ancestry ledger

If the selected channel is angular, M19-414 already gives
\[
Q_R^{H}
\sim
O(\log R)
\]
even under perfect nonreuse.

Therefore
\[
\sum_mR_m^{-3}Q_m^H
\lesssim
\sum_mR_m^{-3}\log R_m
<
\infty.
\]

Syndeticity improves the lower-frequency statement from “positive density on a generic orbit” to “bounded-gap recurrence on every orbit,” but it does not change the physical power of the event.

Hence
\[
\boxed{
\text{syndetic angular residual activity}
\not\Rightarrow
\text{raw-H2 ancestry contradiction}.
}
\]

If the selected channel is force-charge, M19-415--416 show that each fixed excursion is an exact critical annular acceleration event, again with summable unsigned shell cost.

Thus
\[
\boxed{
\text{syndetic force excursions}
\not\Rightarrow
\text{ordinary energy/acceleration-budget contradiction}.
}
\]

## 7. What arbitrary switching is now excluded

Before this step, one could imagine a survivor that avoided every fixed channel by successively moving residual mass between

- different normalized cells;
- the force mode;
- the angular mean-free mode;

with longer and longer gaps for each individual label.

That escape is no longer available on a compact minimal hull.

Because the detector family is finite, one fixed detector/channel open set is visited syndetically by every orbit.

Therefore
\[
\boxed{
\text{all fixed residual channels arbitrarily sparse}
}
\]
is impossible.

The residual can still use the other channels, but at least one canonical channel remains uniformly recurrent.

## 8. Revised residual frontier

The mandatory residual frontier now has a topological strengthening:

\[
\boxed{
R_{gap}
\Longrightarrow
F_{charge}^{syndetic,critical}
\quad\lor\quad
A_{res}^{syndetic,critical},
}
\]
where the disjunction means that at least one fixed channel/cell can be selected as a syndetic witness on the minimal hull.

Both direct channels remain exactly critical under physical restoration.

Therefore the next gain cannot come from frequency of return alone.

It must come from **what the recurrent event does to another state variable**.

The next high-value calculation is a cross-channel observability test:

- on the F-syndetic branch, ask whether every stress-flux excursion forces a simultaneous angular/projective residual or wedge-energy event;
- on the A-syndetic branch, ask whether every angular residual event forces a simultaneous signed stress-flux or pressure-work response.

A same-event coercive coupling would be new information because the separate event counts are already saturated at the logarithmic critical frequency.

\[
\boxed{\text{M19-417 COMPLETE; ONE FIXED RESIDUAL CHANNEL IS SYNDETIC ON EVERY MINIMAL-HULL ORBIT.}}
\]

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
